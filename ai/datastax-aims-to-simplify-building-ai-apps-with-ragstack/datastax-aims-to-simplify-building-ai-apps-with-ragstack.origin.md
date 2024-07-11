# DataStax Aims To Simplify Building AI Apps With RAGStack
![Featued image for: DataStax Aims To Simplify Building AI Apps With RAGStack](https://cdn.thenewstack.io/media/2024/07/8063fcea-buildingaiapplications-1024x683.jpg)
ChatGPT wowed us all, but it was actually the simplest possible demonstration of what a [large language model (LLM)](https://thenewstack.io/working-with-llm-apis-dev-shares-experience-building-ai-bots/) could do, contended [Ed Anuff](https://www.linkedin.com/in/edanuff/), chief product officer at [DataStax](https://thenewstack.io/datastax-gas-data-api-for-genai-application-development/), a company that offers a distributed cloud database built on the open source [Apache Cassandra](https://thenewstack.io/why-apache-cassandra-5-0-is-a-game-changer-for-developers/).

“It’s taking its previous response and the previous interactions that are called the history — it’s taking those and adding your new question as an additional prompt, and it’s bundling all that up into a context and shipping it to the LLM, and it keeps repeating that,” he said of ChatGPT. “When ChatGPT was first released, that’s simply all that it was doing. The results that we experienced were pretty cool, but from a computer science program standpoint, it was actually pretty simple.”

[Retrieval Augmented Generation (RAG)](https://thenewstack.io/how-rag-architecture-overcomes-llm-limitations/) is one way to supplement an LLM’s knowledge. He compared RAG to notecards that help you stay focused and factual when speaking about a topic.
RagStack: the idea is to offer a set of technologies, similar to what the LAMP stack did for web development, that can be used to create AI applications.

“Let’s go and retrieve these, these very accurate sources of knowledge that are retrieved through traditional database lookups,” he said. “In some cases — in a lot of cases — [you] use vector database lookups to get at things and to feed those into the LLM, and then LLM just uses its language facility to craft that response.”

RAG can work through different mechanisms, including simple methods such as search and more [complex methods such as turning a question into database queries](https://thenewstack.io/how-to-run-complex-queries-with-sql-in-vector-databases/), he said. The results post-RAG are “grounded,” meaning the LLM results are more accurate because the LLM used specific, factual information supplied alongside a query rather than relying solely on its own training data, he explained. This approach enhances accuracy by avoiding speculative or incomplete answers, resulting in responses that are more aligned with the provided information and thus more reliable, he added.

“All of those result in behind the scenes, a bunch of information being gathered that is then fed with your original question into the LLM,” he said. “What the LLM does is — rather than going and relying on its own knowledge that it was trained on — it uses that information that was supplied to it, and then the LLM responds.”

## Creating AI Apps With RAGStack
Recently, DataStax updated its offering to make RAG application development 100 times faster, the company announced at [RAG++ in San Francisco](https://www.datastax.com/press-release/datastax-to-launch-massive-new-ai-platform-updates-at-rag-plus-plus-event-in-san-francisco-partners-attending-langchain-microsoft-mistral-ai-nvidia-unstructured-and-more). To do this, it’s using what it calls the [RAGStack](https://www.datastax.com/blog/ragstack-1-dot-0-generally-available). The idea is to offer a set of technologies, similar to what the [LAMP](https://thenewstack.io/install-a-full-lamp-stack-on-a-debian-server/) stack did for web development, that can be used to create [AI applications](https://thenewstack.io/how-to-easily-add-ai-to-your-applications/).

To support its RagStack vision, the company also launched a hosted version of [Langflow](https://www.datastax.com/blog/introducing-datastax-langflow-design-test-generative-ai-apps) on the Astra Cloud Platform.

[Langflow is an open source visual framework](https://astra.datastax.com/signup?type=langflow) for building RAG applications. DataStax acquired Langflow in April. It uses a drag-and-drop GUI to create data flows and leverages [LangChain for RAG functions](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/), thus allowing developers to design, experiment with and test RAG and GenAI applications using various vector databases, embedding models and large language models (LLMs).
Basically, it makes LangChain easier for developers. It does this by abstracting away infrastructure concerns and integrating with multiple GenAI tools — such as OpenAI, Hugging Face, and others, according to the company’s press release.

It is available as a hosted version on DataStax’s Astra Cloud platform, enabling easier accessibility and usage for developers. DataStax’s hosted Langflow will allow developers to design, experiment with and test [RAG and GenAI apps](https://thenewstack.io/develop-a-cloud-hosted-rag-app-with-an-open-source-llm/) using any vector database, embedded model or LLM without having to install Langflow on their machine.

RagStack also leverages [LangSmith](https://www.langchain.com/langsmith), an enterprise DevOps platform for managing and monitoring LLM applications. At the same time, DataStax released version 1.0 of Langflow, which includes dozens of integrations with the top GenAI tools, according to the [company’s blog post](https://www.datastax.com/blog/introducing-datastax-langflow-design-test-generative-ai-apps).

Langflow 1.0 allows developers to leverage LangSmith’s observability service to trace an application’s responses for more relevant, accurate LLM-based applications, according to the company. Astra DB environment details will be readily available in Langflow and users will be able to access Langflow via the [Astra Portal](https://accounts.datastax.com/session-service/v1/login). Usage will be free, the company added.

## Vectorizing Data and Working With Unstructured.io
DataStax also highlighted [Vectorize, a recent release](https://www.datastax.com/blog/simplifying-vector-embedding-generation-with-astra-vectorize) that handles embedding generation directly at the database level. It takes whatever content you put into a database and generates the vector representation of it, Anuff explained.

“Vector representations are where we take this unstructured data and that unstructured data could be a block of text, could be an image, it could be whatever, but we take that and we generate an embedding. That embedding is a very long numerical representation that represents the semantic meaning of that content,” he said.

Those vectors go into a database, where the rows that are closest to each other have similar meaning, he explained. From a development standpoint, that saves time.

“What this allows me to do is get content that might be relevant from a semantic meaning standpoint to what you asked, rather than precise keywords,” he said. “It’s a very powerful tool in these settings where I want to retrieve content by meaning rather than specific keywords because you might never use the specific keywords, but the meaning may be very close.”

Finally, [DataStax announced a partnership](https://www.datastax.com/blog/data-ingestion-just-got-easier-unstructured-astra-db) with [Unstructured.io](https://unstructured.io/), which offers connectors that can get to the data sources and data formats and extract the relevant content in the right bite-sized chunks and feed that into the Astra DB Vector database, Anuff said. The partnership will allow [developers to extract and transform complex data](https://thenewstack.io/the-genai-data-developer-experience-performance-optimization/) to be stored in Astra DB Vector for use in powering LLM-based applications, the company said in its press announcement.

“Users’ GenAI applications benefit from lightning-fast data ingestion through quick conversion of large data sets and common document types into vector data,” the company stated. “This new integration then enables these embeddings to be quickly written to Astra DB for highly relevant GenAI similarity searches. And, when managing very large datasets, users are able to convert that data into embeddings and write them to Astra DB in just minutes.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)