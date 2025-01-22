# Solving the RAG vs. Long Context Model Dilemma
![Featued image for: Solving the RAG vs. Long Context Model Dilemma](https://cdn.thenewstack.io/media/2025/01/b2c53656-llm-1024x572.jpg)
Many developers have been using retrieval-augmented generation (RAG) with large-scale context corpus to build GenAI applications and tame problems such as AI hallucinations faced by general-purpose [large language models (LLMs)](https://roadmap.sh/guides/introduction-to-llms).

Now long context models are emerging like [Gemini with a context window of 2 million tokens, ](https://ai.google.dev/gemini-api/docs/long-context) and its potential benefits make you wonder whether you should ditch RAG altogether. The key to dealing with this dilemma is to understand the pros and cons of using a long context model and make an informed decision about its suitability for your use case.

**Benefits and Limitations of RAG vs. Long Context Models**
Traditionally [LLMs have had smaller context windows](https://thenewstack.io/do-enormous-llm-context-windows-spell-the-end-of-rag/) that limit the amount of text or tokens that can be processed at once. RAG has been an effective solution thus far to address this limitation. By retrieving the most relevant chunks of text or context, augmenting the user prompt with it and then passing those to the LLM, RAG works effectively with much larger data sets than the context window would normally support.

However, a long context model such as Gemini directly allows processing the provided context, without needing a separate RAG system, simplifying application workflow and potentially reducing latency. To put a context window of 1 million tokens into perspective, it is equivalent to [eight average-length English novels](https://ai.google.dev/gemini-api/docs/long-context) or the transcripts of over 200 average-length podcast episodes. However, it’s not a panacea for reducing hallucinations by any means and has its share of limitations.

First, long context models suffer from a diminished focus on relevant information, which leads to potential degradation in answer quality per [research from NVIDIA](https://arxiv.org/pdf/2409.01666).

Second, for use cases such as QA chatbots, it’s not so much about the quantity of the information in the context but rather the quality. Higher-quality context is achieved via highly selective granular searches specific to the question asked, which is what RAG enables.

Finally, long context models require more GPU resources for processing the long context, leading to higher processing times and higher costs. Suffice to say that these models have higher costs per query. You may be able to address this using the key-value (KV) cache to cache the input tokens to be reused across requests, but that has significant GPU memory requirements and hence drives up the associated costs. The key is to achieve high answer quality with fewer input tokens.

Despite its limitations, long context models support a few compelling use cases that require longer context such as translation or summarization, for example, translating documents from English into Sanskrit (the least-spoken language in India) for educational purposes. LLMs struggle with such translation into Sanskrit due to the language’s complex grammatical structure and the limited availability of training data compared to other widely spoken languages. Hence, providing a sufficiently large number of examples as context will help boost the accuracy of the translation. Other ways include summarization and comparison across multiple large documents at once to generate insights, for example, comparing the 10K reports of multiple companies to create financial benchmarks.

Long context models are [great for reducing hallucination](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/) for certain use cases that warrant longer context. However, for all other use cases, we recommend using [RAG to retrieve context relevant](https://thenewstack.io/rag-still-relevant-in-the-era-of-long-context-models/) to answer the user’s question with high accuracy and cost-effectiveness. If RAG does not meet the desired accuracy, we suggest using RAG in conjunction with fine-tuning to increase domain specificity.

Couchbase’s [Capella AI Services](https://www.couchbase.com/products/ai-services/) helps developers like you build performant RAG and agentic applications quickly. Feel free to [sign up for our private preview](https://info.couchbase.com/capella-ai-services-signup) to get started with your AI project.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)