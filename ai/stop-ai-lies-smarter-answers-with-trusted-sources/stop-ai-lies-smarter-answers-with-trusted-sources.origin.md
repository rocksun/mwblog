# Stop AI Lies: Smarter Answers With Trusted Sources
![Featued image for: Stop AI Lies: Smarter Answers With Trusted Sources](https://cdn.thenewstack.io/media/2024/12/578a4f98-fake-1024x576.jpg)
When you use GPT-4o to search the internet, its responses often include citations that link information to its sources. This transparency allows you, as the user, to verify the content and trust the answers you receive. Citing sources is essential for ensuring accountability and reliability in [AI-generated responses](https://thenewstack.io/ai/), especially in applications where accuracy is critical.

[Retrieval-augmented generation (RAG)](https://zilliz.com/learn/Retrieval-Augmented-Generation?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns) with citations applies this principle by retrieving relevant information from external data sources and linking generated responses back to their origins. By grounding outputs in accurate retrieved data and citing sources, RAG-based systems enhance trust and transparency. This approach is particularly valuable in fields like research, health care and legal services where verified information is paramount.
Let’s explore the importance of citations in RAG systems. I’ll also demonstrate their role in ensuring reliable AI outputs and provide a step-by-step guide to implementing RAG with citations in your applications.

## What Is Retrieval-Augmented Generation?
Retrieval-augmented generation, or [RAG](https://zilliz.com/learn/Retrieval-Augmented-Generation), is a framework that improves the accuracy and relevance of AI responses by pairing information retrieval with the generative capabilities of [large language models (LLMs)](https://zilliz.com/glossary/large-language-models-(llms)?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns). While [LLMs like GPT-3 and GPT-4](https://thenewstack.io/llm/) are trained on extensive data sets, their knowledge is limited to static data available during their training. This limitation makes them less effective at answering questions about recent events or domain-specific information.

RAG addresses this challenge by retrieving relevant, up-to-date documents from external knowledge bases. These retrieved documents are then used as context for the LLM to generate more precise responses. This pairing of retrieval and generation creates systems that are both accurate and flexible, enabling them to handle a broader range of queries.

For example, imagine asking a RAG-powered system, “What is the current population of Houston?” The retriever might locate a document containing data from the 2024 census and provide it as input to the language model. The system then responds that the population of Houston is approximately 2.4 million, based on the latest 2024 census report. This ensures the response is accurate and grounded in reliable data.

## Why Are Citations Important?
Citations are essential in RAG systems because they provide a clear trail back to the source of the information used in the response. This is particularly important in scenarios where trust and reliability are crucial. Without citations, users must rely solely on the system’s authority, which may lead to uncertainty or distrust, especially in high-stakes fields.

### Ensuring Transparency
Citations make the inner workings of RAG systems transparent by showing exactly where information originates. For instance, if a legal assistant retrieves a clause from a contract, it can include a citation pointing to the specific section. This allows users to verify the response and understand its foundation, reducing the risk of misinterpretation or error.

### Building Trust
A system that cites its sources fosters trust because users can independently verify the answers it provides. This is valuable in medical or academic contexts. For example, a health care chatbot that cites medical journals or treatment guidelines ensures users feel confident in its recommendations, knowing they are backed by credible evidence.

### Adding Context
Citations enhance user understanding by adding context to the AI-generated response. A citation provides details such as the date of the source or its authorship, helping users gauge the reliability and relevance of the information. For instance, a response about a scientific breakthrough may link to a recent study, allowing the user to explore the topic further.

### Improving Explainability
Citations contribute to the explainability of [RAG systems by revealing how the response was generated](https://thenewstack.io/advanced-retrieval-augmented-generation-rag-techniques/). Users and developers alike can trace the reasoning process, which is useful in complex applications like legal research or contract analysis.

Citations not only validate the response but also improve the robustness of the system. They ensure accountability, making RAG systems suitable for critical tasks where accuracy is essential.

Now that we’ve established the importance of citations, let’s explore how to build a system that incorporates them.

## Building a RAG System With Citations
Building a citation system needs tools for data collection, processing and retrieval. Let’s walk through creating a RAG system that collects information from Wikipedia, processes it with [Milvus Lite](https://milvus.io/docs/milvus_lite.md?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns) and generates responses with citations. Milvus Lite is a lightweight version of the [Milvus vector database](https://milvus.io/?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns), designed for efficient storage and retrieval of [vector embeddings](https://zilliz.com/learn/everything-you-should-know-about-vector-embeddings?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns) which are numerical representations of data. They capture the [semantic relationships](https://zilliz.com/glossary/semantic-similarity?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns) between data points.

### Installing the Required Libraries
First, install these [Python packages](https://thenewstack.io/the-top-5-python-packages-and-what-they-do) that we will require while building our application:

`pip install llama-index llama-index-vector-stores-milvus python-dotenv requests`
The `llama-index`
package provides the foundation for [RAG operations and vector handling](https://thenewstack.io/vector-embeddings-explained-a-beginners-guide-to-powerful-ai/). The [Milvus integration package connects to our vector storage](https://thenewstack.io/what-is-milvus-vector-database/). `Python-dotenv`
keeps API keys safe and `requests`
fetches data from Wikipedia.

### Setting Up Your Environment
Once the installation is complete, the next step is to import them into your code. Also, load the OpenAI API key into your environment. If you don’t have the API key, [get one from here](https://openai.com/api/).

Your environment is now ready to start coding the app’s logic.

### Creating Your Knowledge Base
The first thing the system needs is the knowledge base. We will use Wikipedia articles about North American cities to form our knowledge base. This data will allow us to answer questions while tracking information sources. Let’s start by defining our data sources.

With your data sources defined, you need a way to collect and organize this information.

The above function creates a foundation for reliable citations. When it fetches an article, it also records essential metadata: the title, source, URL and access date. This metadata becomes crucial later when the system needs to cite its sources. By storing both the content and metadata locally, it creates a persistent knowledge base that can be reused without repeatedly accessing Wikipedia.

The function wraps each article and its metadata in a LlamaIndex Document object. These Document objects are the building blocks of your RAG system; they contain all the contextual information needed to generate accurate citations.

### Managing Document Storage
To make the knowledge base accessible across multiple sessions, we need a way to reload the saved information:

The code above reconstructs the Document objects from saved files, maintaining the connection between content and its sources. The default metadata values ensure the system remains robust even if metadata files are missing.

### Setting Up the Vector Store
Now comes a crucial part of the RAG system: converting text into a format that computers can efficiently search. This happens through a process called embedding generation. When text is fed into [LlamaIndex](https://zilliz.com/learn/getting-started-with-llamaindex?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns), it uses OpenAI’s [text-embedding-ada-002 ](https://zilliz.com/ai-models/text-embedding-ada-002?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns)model to convert text into lists of 1,536 numbers (vectors). These vectors capture the semantic meaning of the text. Similar concepts have similar vectors, even if they use different words. To store and search these vectors efficiently, we will use Milvus Lite.

When the `VectorStoreIndex`
is created, a series of operations occurs behind the scenes. The documents are [split into chunks](https://zilliz.com/learn/guide-to-chunking-strategies-for-rag?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns); each chunk is converted to an embedding vector and these vectors are stored in Milvus Lite. The overlap between chunks ensures that important information isn’t lost at chunk boundaries.

### Creating the Query Engine
With the knowledge base embedded and stored, we need a way to query it and generate cited responses:

When you ask a question, several things happen:

- Your question is converted to an embedding vector. In this case, the query is, “Does Seattle or Houston have a bigger airport?”
- Milvus Lite finds the three most similar chunks in your knowledge base.
- These chunks and their metadata are sent to GPT-3.5 Turbo.
- GPT-3.5 Turbo generates a response based on these chunks.
- The
`CitationQueryEngine`
adds citations to show where the information came from.
To make these citations useful, let’s add a way to display them:

### Formatting Source Citations
The source citations help us verify information and trace facts to their origins. Let’s create a function to display citation metadata:

The above code displays multiple citation elements for each source. The title shows which article provided the information. The source and URL let users find the original document. The access date helps track information currency. Text excerpts show the specific passages that informed the answer, allowing direct verification of the information used.

### Putting It All Together
Finally, you need a main function to orchestrate all these components:

The above code orchestrates the entire process. First, it triggers Wikipedia data collection through `scrape_wikipedia()`
. This function gathers articles and their metadata, storing them locally. Next, `setup_rag_with_citations()`
initializes the RAG system, creating vector embeddings, setting up Milvus Lite and preparing the query engine. Error handling wraps these operations to catch and report any issues, ensuring the system runs reliably. This sequential execution ensures all components are ready before the system processes questions.

Let’s see how the RAG system handles the query about airport sizes. Below is the expected output:

![Results of RAG system comparing airport sizes with citations.](https://cdn.thenewstack.io/media/2024/12/4009ee1d-image1a-1024x569.jpg)
Results of RAG system comparing airport sizes with citations.

The output shows that our system could reply to the question correctly and cite a relevant source from Wikipedia to back its answer.

## Conclusion
Retrieval-augmented generation with citations transforms the way AI systems deliver information, creating a bridge between AI capabilities and user trust. Unlike traditional AI models that are limited to their training data, RAG systems actively retrieve and cite relevant information, enabling users to verify sources and examine reference passages. This transparency turns abstract responses into verifiable facts, making these systems valuable in fields like research, health care and legal services where accuracy and accountability matter. By linking each piece of information to its source, RAG systems build confidence in AI-generated responses while opening new possibilities for applications where information verification is essential.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)