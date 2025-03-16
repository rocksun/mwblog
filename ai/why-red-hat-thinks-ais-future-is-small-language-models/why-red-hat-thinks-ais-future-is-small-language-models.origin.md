# Why Red Hat Thinks AI’s Future Is Small Language Models
![Featued image for: Why Red Hat Thinks AI’s Future Is Small Language Models](https://cdn.thenewstack.io/media/2025/03/02841b58-smallai-1024x683.jpg)
There’s not one unicorn application that does everything, so why should there be one large language model (LLM) for all needs?

There shouldn’t be, contended [Tushar Katarki](https://www.linkedin.com/in/katarki/), the senior director of product for GenAI Foundation Model Platforms at [Red Hat](https://www.openshift.com/try?utm_content=inline+mention). Popular LLMs can be overkill for most organizations, even enterprises, he told The New Stack.

“If you have one large model, of course it is very capable, but also it comes with a lot of things,” Katarki said. “[An] Enterprise doesn’t need a single model that can do everything in the world. In fact, if anything, they need models that they can customize and use for their use cases.”

The [large language models](https://thenewstack.io/top-5-large-language-models-and-how-to-use-them-effectively/) underlying popular Gen AI solutions such as ChatGPT need to serve millions of customers, with a diverse range of language and knowledge needs, but [enterprise AI](https://thenewstack.io/how-ai-agents-are-starting-to-automate-the-enterprise/) can be more focused, he noted.

“Enterprises have a different problem,” he said. “They have actually lots of different use cases.”

## Why Developers Should Embrace Smaller Models
There are two main reasons organizations want smaller LLMs. First, smaller models are more cost-effective to operationalize and run, he said. Second, enterprises want to be able to access their private data from within the AI.

“Guess what? Any large model, especially that they get [with] ChatGPT or anybody else, it doesn’t have your enterprise’s private data,” Katarki said.

But for developers, there’s another, third reason to leverage smaller models and [AI agents](https://thenewstack.io/the-rise-of-ai-agents-how-arazzo-is-defining-the-future-of-api-workflows/): They can be used as “building blocks” within a workflow, just as developers leverage microservices to handle different functionality within multiple applications, Katarki added.

“AI agents are nothing but these small, fit-for-purpose AI systems and all those require smaller models that can be customized for enterprise use cases,” he said. “Once you develop an agent, … you can mix and match different things and create a different end system.”

## The Bones of A Small Model
Of course, [small language models](https://thenewstack.io/the-rise-of-small-language-models/) are not necessarily small — they’re just smaller relative to other models. For instance, LLaMA has a 405 billion parameter model (the largest model today), but there’s also a 70 billion parameter model, 8 billion parameter model and a 3 billion parameter model.

“We are just simply saying that the 8 billion and 3 billion perhaps are the more smaller language models,” Katarki said. “There are no formal definitions of these. But that’s the idea. Otherwise, they’re all LLaMA models.”

Small [language models should also still be generated from transformer](https://thenewstack.io/grounding-transformer-large-language-models-with-vector-databases/) models, a neural network architecture, he said. Transformer models include:

[OpenAI’s GPT](https://thenewstack.io/openai-launches-new-chatgpt-interface-designed-for-coding/)(Generative Pre-trained Transformer) family;[Google](https://cloud.google.com/?utm_content=inline+mention)‘s[BERT](https://research.google/pubs/bert-pre-training-of-deep-bidirectional-transformers-for-language-understanding/)(Bidirectional Encoder Representations from Transformers) and T5 (Text-to-Text Transfer Transformer);- Meta’s
[LLaMA](https://thenewstack.io/get-started-with-metas-llama-stack-using-conda-and-ollama/)(Large Language Model Meta AI) and RoBERTa (Robustly Optimized BERT Pretraining Approach); and [IBM](https://www.ibm.com?utm_content=inline+mention)‘s Granite models.
“When we say smaller models, they are not new — they are still based on this transformer [paradigm], so they definitely need to have basic language capabilities, including code, et cetera,” Katarki said

## Creating Small Language Models
There are several options for generating smaller models. The most well-known is [retrieval-augmented generation (RAG)](https://thenewstack.io/rag-and-model-optimization-a-practical-guide-to-ai/), which received a lot of attention as a tool for refining models with proprietary datasets.

“RAG … allows you to bring your own data set and you vectorize it and put in a vector database,” Katarki said. ”When a query comes, you look up the vector database and see what is the most relevant part of the document that’s related to that query, and you send that as a prompt to the [large language model](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/), saying that you use this as a prompt for the question.”

But RAG has disadvantages, too, he added. First, it can suffer from retrieval challenges, he said. Second, it requires the creation of yet another database, “which has its own scale problems as the amount of data set increases,” he added.

While RAG does increase accuracy, there are limits, he continued.

“If you want to keep increasing the accuracy of your AI system, then you need to fine tune that knowledge right into the model,” he said.

That’s where Red Hat’s tools for creating small models can help, he added.

## How InstructLab Generates Small Models
[InstructLab](https://www.redhat.com/en/topics/ai/what-is-instructlab) is an open source project for enhancing LLMs used in Gen AI applications. Created by IBM and Red Hat, Instruct stands for “instruction tuning,” which is an industry term. LAB stands for [Large-scale Alignment for chatBots](https://research.ibm.com/blog/LLM-generated-data), which is from a [related IBM research paper](https://arxiv.org/abs/2403.01081).
InstructLab uses supervised fine tuning, also known as instruction alignment. That approach basically trains the AI by labeling. For instance, for a [computer vision model](https://thenewstack.io/computer-vision-modeling-unlocks-new-use-cases/), a trainer would instruct or label for the AI that one picture is a dog and another is a cat, until it learns the difference.

“I’m going to tell you what the next word is and what the right next word is, so if you predict something which is not this, then you’ve got to score your prediction very low. If you predict the exact one that I tell you, then you can give yourself a high score,” he explained, “This basically gets repeated like zillions of times in this supervised fine training, so that label data is what you need.”

“[An] Enterprise doesn’t need a single model that can do everything in the world. In fact, if anything, they need models that they can customize and use for their use cases.”

— Tushar Katarki, Red Hat
With InstructLab, the process can be done with just “a few CLI commands,” Katarki said.

“If you ask somebody to do supervise fine training, that’s a pretty tedious process. You need data scientists to do that,” he said. “We made it very simple and accessible to non-data scientists or maybe ‘citizen data scientists.’”

Labeling data can be expensive, too. So InstructLabs takes a data set, amplifies it using synthetic data generation, and then uses the synthetic data to further train the model.

Katarki offered an example. A bank might want to train a model on how to approve credit line increases when a consumer calls in. To do that, the bank would need to create a representative Q&A with the various questions that scenario might create, such as who is the customer, what is their credit rating, have they been with the bank for a long enough period of time.

“The synthetic data generation is going to take that representative questions and it’s going to apply those questions in 1,000 different ways that it can be asked,” he said. “It does that using generative AI, and then it has a corpus of data that you already provided, because that’s the answers. Now it has a very large data set.”

The model learns many more permutations of how that question and answer can be done, and this makes it more effective at answering questions.

The platform also supports PyTorch for Fully Shared Data Parallel (FSDP), which is a technique used in distributed training of LLMs, he added.

## Why Open Source in AI
It’s also very important that organizations opt for open source, particularly with AI, Katarki contended. Although InstructLab can train any LLM, Katarki pointed to [IBM Research’s Granite](https://www.ibm.com/granite) as an open source option.

This offers two benefits. First, it creates indemnity for any intellectual property claims that may arise, he said. Second, it offers licensing advantages.

“If I’m a company, especially if I’m a company which needs to ship these models, then I don’t have to come back to you if it is Apache 2.0 license,” he said. “Let’s say we use LLaMA, for example, which is not Apache 2.0 license… You don’t want to find out that — 700 million users later and now I’m a very successful business — I have to now go back [to Meta] for my 701st millionth user.”

Red Hat also recently added an inference server, which is required to run any LLM. [Red Hat acquired Neural Magic](https://www.redhat.com/en/about/press-releases/red-hat-completes-acquisition-neural-magic-fuel-optimized-generative-ai-innovation-across-hybrid-cloud), which is the leading commercial contributor to the popular, open source inference server [vLLM](https://github.com/vllm-project/vllm), in January.

“All these large language models need a runtime to run them on, and the vLLM is the de facto runtime,” he said.

InstructLab is available for Red Hat [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) or [OpenShift](https://thenewstack.io/docker-testcontainers-now-available-on-red-hats-openshift/). It allows the AI to run either in an on-premise [data center or in the public or private cloud](https://thenewstack.io/choosing-the-right-database-strategy-on-premises-or-cloud/).

*Editor’s Note: Updated at 1:11 p.m. March 14, 2025 to correct that Neural Magic is the leading commercial contributor to vLLM.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)