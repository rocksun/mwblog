In the [previous part](https://thenewstack.io/introduction-to-vllm-a-high-performance-llm-serving-engine/) of this series, I introduced the architecture of vLLM and how it is optimized for serving [large language models](https://thenewstack.io/llm/) (LLMs). In this installment, we will take a behind-the-scenes look at vLLM to understand the end-to-end workflow, from accepting the prompt to generating the response.

[vLLM’s architecture](https://docs.vllm.ai/en/latest/design/arch_overview.html) is optimized for high throughput and low latency. It efficiently manages GPU memory and scheduling, allowing many requests to be served in parallel. In the sections below, we’ll dive into each stage in detail, using simple analogies to clarify the technical mechanisms.

## Stage 1: Receiving the Prompt

Everything begins when a client sends a prompt to the vLLM server’s API endpoint. vLLM runs an HTTP server (based on [FastAPI](https://fastapi.tiangolo.com/)) that implements [OpenAI’s REST interface](https://platform.openai.com/docs/api-reference/introduction) for completions and chat completions. For example, a user might POST to /v1/completions or /v1/chat/completions with a JSON payload containing their prompt. The server parses this request, extracting the prompt text and any generation parameters, such as the maximum number of tokens, temperature, and whether to stream.

**Queuing:** Instead of handling each request immediately, vLLM uses an internal queue to manage incoming prompts. Think of this like a line at a bank: each request takes a ticket and waits for service. The reason for queuing is to allow efficient batching on the GPU. As soon as the server receives the prompt, it packages the request into a data structure and notifies the inference engine that a new request is available for processing. If many requests arrive at the same time, they will be queued up in this waiting line. This prevents the GPU from being overwhelmed by too many single tasks and instead gives it work in optimized chunks.

## Stage 2: Dynamic Batching and Scheduling Requests

Once the prompt is queued, vLLM’s scheduler steps in. The scheduler is a core component that decides when and how each request is executed on the GPU. Unlike naive processing, which might handle one request at a time or use fixed-size batches, vLLM uses continuous dynamic batching to maximize efficiency.

**Continuous Batching:** Traditional inference engines often use static batches and process them in a stop-and-go fashion: fill a batch, process it, then fill the next batch. vLLM’s scheduler, on the other hand, performs continuous batching, where it can add new requests to an ongoing batch as soon as space becomes available. Suppose one request in a batch finishes early (perhaps it was a short prompt or it reached its answer quickly), vLLM will immediately slot in another waiting request into that freed-up slot without waiting for all other batch members to complete. This way, the GPU is always doing practical work and not sitting idle waiting for slower sequences to catch up. The result is higher throughput and lower latency, more queries served per second, and shorter wait times for users.

**Scheduling Decisions:** The scheduler operates in steps or iterations. In each iteration, it decides whether to perform a prefill step or a decode step (more on these in later sections). It looks at the state of the system: Are there new requests waiting? Are there ongoing requests that require generating additional tokens? Are any requests “swapped out” due to memory limits? Based on that, it picks a set of requests to run. Notably, vLLM’s scheduler follows a strict First-Come, First-Served (FCFS) policy for fairness. This means it will always try to serve older requests from the queue before newer ones, even if a newer request might fit easily into the batch. In other words, no cutting in line — this keeps the service predictable and fair, which is essential for SLOs (ensuring no user request gets indefinitely starved or delayed out of order).

The scheduler also optimizes which requests to batch together. It can mix short prompts or fast-completing requests with longer ones to balance the load. By grouping compatible requests, it achieves high GPU utilization without allowing long-running requests to block everything. Under variable workloads (with some prompts small and some huge), this intelligent scheduling maintains stable latency and high throughput.

At this point, the scheduler has only decided on a batch of one or more prompts to process in the next model inference cycle. Now the actual LLM processing begins.

## Stage 3: Tokenization – Breaking the Prompt into ‘Lego Blocks’

Before the model can work with the text of the prompt, that text must be translated into a form the model understands. This step is called tokenization. vLLM utilizes the tokenizer of the underlying model (e.g., [GPT tokenizer](https://platform.openai.com/tokenizer), [SentencePiece](https://github.com/google/sentencepiece)) to perform this conversion.

Tokenization refers to splitting the input text into discrete units, known as tokens. These tokens could be whole words, subwords, or even single characters, depending on the tokenizer’s design. A simple way to think about it is breaking a sentence into Lego pieces — each token is a piece that contributes to the whole, and together they can be used to reconstruct the original sentence. For example, a sentence like “Transformers are great!” might be tokenized into pieces like “Transform”, “ers”, “are”, “great”, “!”. Each piece is assigned a numerical ID from the model’s vocabulary.

Once tokenized, the prompt is now represented as a sequence of token IDs (e.g., [312, 1085, 42, …]). These IDs will be used in the next stage to look up embeddings.

For a gentle introduction to tokens and embeddings, refer to one of my [previous articles](https://thenewstack.io/the-building-blocks-of-llms-vectors-tokens-and-embeddings/) on this topic.

It’s worth noting that tokenization usually happens on the CPU and is relatively fast. In a server context, this overhead is minor compared to the processing required by the neural network. Still, it’s an important step: if you send a 1000-character prompt, the tokenizer might output, say, 200 tokens. The rest of the pipeline will operate on those 200 tokens rather than 1000 characters.

## Stage 4: Input Embedding – Turning Tokens into Vectors

After tokenization, we have a list of token IDs representing the prompt. The next step is to convert those IDs into numeric vectors that the transformer model can process. The embedding layer of the model does this step.

The model has an embedding matrix (essentially a big table of numbers) where each token ID indexes a specific row – that row is the vector representation of the token. For example, token ID 312 might correspond to a 768-dimensional vector, such as [0.12, -0.45, …, 0.67]. These vectors are sometimes called word embeddings (though they also encode subwords or symbols). They capture semantic information – tokens with similar meaning or usage often end up with similar embedding vectors in this high-dimensional space.

You can think of embedding like translating words into a secret numerical language that the model speaks. If tokenization gave us the “words” (tokens), embedding builds the “meaning” in a mathematical form.

Within a sentence or prompt, word order matters. Transformers don’t inherently understand sequence order just from the list of vectors, so an additional positional encoding is added to each token’s vector to inform the model of each token’s position in the sequence. This can be done by adding or concatenating a positional vector (like sine/cosine patterns or learned positional embeddings) to the token’s embedding. The result is that each token’s final input vector encodes both what the token is and where it is in the sequence.

At the end of this stage, the prompt is represented as a sequence of vectors (one per token, typically with hundreds or thousands of components each). Now the heavy lifting — the actual transformer inference — begins.

## Stage 5: Transformer Model Processing — Attention and Layers

The core of vLLM’s job is running the prompt through the Transformer model to either encode the prompt or generate new text. Modern LLMs, such as GPT and Llama, are essentially large decoder-only transformers. They consist of a stack of identical layers (for example, 24 layers or more), each containing a self-attention mechanism and a feed-forward network.

Here’s how the prompt is processed through these layers:

**Self-Attention:** In each transformer layer, the model utilizes self-attention to identify which other words (tokens) in the prompt are crucial for understanding a given token. It’s as if the model has a spotlight that it can shine on the past words when processing the next word. If our prompt is a long sentence, when the model is figuring out the next word, it doesn’t treat all prior words equally — it focuses on the most relevant ones.

**Feed-Forward Network:** After attention, each token’s representation goes through a small feed-forward neural network. This is applied independently to each token’s data. It’s like further processing or refining each token’s meaning now that it has absorbed context from the attention step. The feed-forward step can be thought of as the model’s way of mixing and transforming the information in each token to make it more useful for prediction. Technically, it enhances the model’s ability to capture complex patterns by applying a non-linear transformation.

**Multiple Layers:** The transformer has many such layers stacked. The output of one layer feeds into the next. With each layer, the model’s representation of the text becomes richer and more abstract. Early layers may capture low-level patterns (such as syntax or phrase structure), while later layers capture high-level concepts or intent. By the top layer, the model has a deeply processed understanding of the prompt.

**Prefill (Context Encoding):** This step involves running the model over all the prompt tokens without generating new output. This is done when a request first enters the system. The model processes the prompt from the first token to the last token, populating the internal state (KV cache) but not yet producing any new tokens. Think of this as reading and understanding the question before trying to answer.

**Decode (Autoregressive Generation):** This step uses the model to predict new tokens one by one, with the help of the context from the prefill. In decoding, each iteration typically passes through the transformer to generate the next token (we’ll detail this in the next section).

vLLM’s scheduler is aware of these phases — it might process a large batch of prefill for some new requests, then switch to decoding steps to generate outputs for those (and other ongoing) requests. Grouping the requests in this manner keeps things efficient.

By the end of the prefill stage for our prompt, the model has effectively “understood” the prompt and is ready to start generating a response. All the heavy computation of the transformer on the prompt tokens has been done, and importantly, the Key-Value cache is now filled with the prompt’s context.

## Stage 6: Key-Value Cache — Remembering Past Tokens Efficiently

One of the key innovations in transformer-based LLMs (and in vLLM’s efficiency) is the use of a KV cache. This is a cache of the Key and Value tensors computed during the self-attention step for each token at each layer. It acts as the model’s memory of what it has processed so far. Let’s break down why this matters and how vLLM handles it:

Why KV Cache? Typically, if the model had to generate text without a cache, it would have to recompute all the attention calculations for each new token over the entire sequence (prompt + generated tokens so far). That means a ton of repeated work — effectively reading the whole conversation so far from scratch to decide the next word, every time. The KV cache avoids this by storing the intermediate results. It’s like the model taking notes as it processes the text, so that when it needs to generate the next word, it can just look at its notes instead of re-reading everything.

In vLLM, the KV cache is managed very carefully because it directly impacts memory usage and performance. Every prompt token and every generated token contributes some data to this cache (for each transformer layer). For large models and long prompts, this can result in a significant amount of data — in fact, the cache size grows linearly with sequence length and can become a memory bottleneck. Traditional systems often pre-allocate a big contiguous chunk of GPU memory for the maximum possible cache, which can waste memory if not all of it is used. vLLM introduces an innovation called PagedAttention to make this more efficient.

[PagedAttention](https://blog.vllm.ai/2023/06/20/vllm.html) treats the GPU memory for the KV cache similarly to how an operating system treats virtual memory. Instead of one enormous contiguous array, it breaks the KV cache into fixed-size pages (small blocks) and allocates them on demand. If some requests are shorter or finish early, their pages can be freed and reused for new requests, reducing waste. It’s like splitting a notebook into removable pages — use what you need and reuse the blank pages elsewhere, rather than having a permanently reserved giant notebook for each request. This non-contiguous allocation prevents memory fragmentation issues and allows vLLM to support larger batches and longer contexts without running out of memory. PagedAttention can support two to three times more concurrent users on the same GPU compared to naive caching by reclaiming and reusing memory efficiently.

In summary, vLLM’s use of KV cache and PagedAttention means that as the model works on your prompt and partial outputs, it’s efficiently using GPU memory to remember the context. This memory of past tokens is what makes generating long responses feasible and fast, since the model isn’t constantly rereading the entire input for each new word. With the prompt processed and cached, we proceed to generate the model’s response.

## Stage 7: Decoding — Generating the Response Tokens

Now comes the moment of truth: producing the model’s answer. Decoding is the iterative process of generating one token at a time as the output.

Here’s how it works in vLLM:

**Initial Logits Prediction:** After the prompt (prefill) is processed, the model is ready to predict the first output token. The output of the transformer for the last prompt token is passed through a final projection to produce a set of logits — essentially, scores for each token in the vocabulary as a potential next token. These logits are transformed into probabilities through a softmax. The generation parameters (temperature, top-k, nucleus sampling, etc.) parsed by the API server are applied at this point to decide how to pick the next token. For instance, if using greedy decoding, the model will simply select the token with the highest probability as the next token.

**Emitting the Token:** The chosen next token is now the first word of the model’s response. At this moment, vLLM can send this token back to the user (we’ll cover streaming in the next section). The new token is also appended to the sequence for this request.

**Updating the KV Cache:** Crucially, the model now computes the Key and Value vectors for the newly generated token at each layer, and appends these to the KV cache. Because of our cache, the model does not need to recompute keys and values for any previous tokens — it already has those. It only pays attention to the new token, attending to all previous ones (using their cached keys/values). This operation is much faster than processing the entire sequence from scratch. Essentially, the model has expanded its notes to include the new token’s information.

**Next Iteration:** Now with the sequence one token longer, the process repeats. The model takes all existing tokens (prompt + generated so far), uses the cached context, and predicts the next token. Thanks to dynamic batching, vLLM might be doing this for many sequences in parallel within the same iteration — each active request in the batch gets one token further. If some sequences finish (e.g., the model outputs an end-of-sequence token or reaches a length limit), the scheduler will drop those from the batch and can introduce new waiting requests in their place on the next iteration.

This loop continues until the request has generated its complete response. “Done” could mean the model produced a special end-of-text token, or a specific maximum token limit was reached, or perhaps a stop criterion from the user (such as a stop sequence) was encountered.

At the end of stage 7, the model has generated a sequence of tokens that form the answer to the user’s prompt. Now we need to deliver that answer back to the user.

## Stage 8: Streaming the Response Back to the Client

As the model generates tokens, vLLM doesn’t necessarily wait until the whole answer is complete to return it. It supports streaming output, which is crucial for a good user experience in interactive settings (and aligns with how OpenAI’s API streams results).

If the request was made with stream=true (in [OpenAI API terms](https://thenewstack.io/openai-api-now-supports-building-voice-agents/)), vLLM will send back parts of the response incrementally. Technically, the HTTP connection remains open, and the server flushes data as new tokens are generated. The client might receive a stream of JSON chunks, each containing a newly generated word or phrase, rather than one big response at the end.

## Conclusion

In summary, the vLLM inference server is akin to a highly efficient assembly line for AI prompts — from intake (queuing and batching) to processing (tokenization and transformer computation) to output (streaming tokens) — each component is optimized for performance.

By understanding this lifecycle, one can appreciate how modern LLM serving systems deliver intelligent responses quickly and at scale, and also identify where to monitor or tweak if something goes awry (e.g., GPU memory usage due to KV cache, or throughput bottlenecks due to suboptimal batching). vLLM demonstrates that with clever engineering (continuous batching, PagedAttention, caching), we can achieve both speed and scale in LLM inference, turning large models into practical services.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)