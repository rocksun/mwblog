# Semantic Router and Its Role in Designing Agentic Workflows
![Featued image for: Semantic Router and Its Role in Designing Agentic Workflows](https://cdn.thenewstack.io/media/2024/09/51ea8e88-arrow-1024x576.jpg)
The emerging pattern of [agentic](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) workflows heavily relies on LLMs to perform reasoning and decision-making. Each agent calls an LLM multiple times during task execution. With a workflow consisting of multiple agents, the number of calls increases exponentially, leading to both cost and latency.

There are various language models with different features and abilities, such as [small language models](https://thenewstack.io/how-to-get-started-running-small-language-models-at-the-edge/), [multimodal models](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/), and purpose-built [task-specific models](https://thenewstack.io/a-comprehensive-guide-to-function-calling-in-llms/). Agents can use these models to finish a workflow. This results in a *decrease* in cost and latency, as well as an increase in overall accuracy.

A **semantic router** is a pattern that enables agents to choose the right language model for the right task while also reducing their dependency on the models through local decision-making. Behind the scenes, the semantic router uses embeddings stored in a vector database to match the prompt with a set of existing phrases (also known as utterances) to map them to a specific route. The route can be an LLM that’s best suited for the task. Because a semantic search determines the target, we call it a semantic router.

The semantic router uses the same technique as the retriever in a RAG pipeline to perform a semantic search to find the right match. But instead of chunks of text, it returns a single, pre-defined route based on the input.

Although implementing a semantic router as a custom layer between the agents and the LLMs is technically possible, the open source Semantic Router project is gaining popularity.

## Overview of the Semantic Router Project
[Aurelio AI](https://www.aurelio.ai/) developed [Semantic Router](https://github.com/aurelio-labs/semantic-router), an innovative open source tool that transforms decision-making in AI-based agents. This layer enhances what LLMs and agents can do by utilizing semantic vector space to route requests more efficiently. Unlike traditional methods that rely on slow LLM generations for tool-use decisions, Semantic Router utilizes the power of semantic meaning to make rapid and accurate choices.
The project offers seamless integration with various embedding models, including popular options like [Cohere](https://cohere.com/embed) and [OpenAI](https://platform.openai.com/docs/guides/embeddings), as well as support for open source models via [HuggingFace Encoders](https://huggingface.co/docs/tokenizers/en/api/encoding). The project utilizes an internal in-memory vector database, but mainstream vector database engines like [Pinecone](https://www.pinecone.io/) and [Qdrant](https://qdrant.tech/) can easily replace it. The Semantic Router’s ability to make decisions based on user queries significantly reduces processing time, typically from 5000 ms to just 100 ms.

With its MIT license, Semantic Router is extensible, allowing developers to incorporate it into their projects freely. This tool addresses critical challenges in AI development — including safety, scalability, and speed — making it an invaluable asset for creating more efficient and responsive agentic workflows.

## Key Components of Semantic Router
**Routes and Utterances**
Routes form the backbone of the Semantic Router’s decision-making process. Each route represents a potential decision or action and is defined by a set of utterances, which are sample inputs that map to a particular route. The system feeds these utterances into a semantic profile for each route. We compare new inputs to these utterances to find the closest match.

In practice, this allows the system to categorize and respond to inputs based on their semantic meaning rather than relying on LLM generation, which can be slow or prone to error. Developers can customize routes to fit specific applications — whether that’s filtering sensitive topics, [managing APIs](https://thenewstack.io/api-management/), or orchestrating tools in a complex workflow.

**Encoders and Vector Spaces**
To compare inputs with predefined utterances, the Semantic Router uses encoders that transform text into high-dimensional vectors. These vectors reside in a semantic space, where the distance between vectors reflects the semantic similarity of the corresponding texts. The shorter the distance, the more semantically related the inputs are.

Semantic Router supports multiple encoding methods, including Cohere and OpenAI encoders for high-performance API-driven workflows and Hugging Face models for those seeking open source, locally executable alternatives. The flexibility to choose different encoders allows developers to tailor the system to their specific infrastructure — balancing performance, cost, and privacy concerns.

**Decision Layers**
Once the inputs are encoded and compared to the predefined routes, the Semantic Router makes decisions using RouteLayers. This layer aggregates routes and embeddings, as well as manages the decision-making process. It also supports hybrid routing, where the system can combine local and cloud-based models to optimize performance.

**Local LLM Integration**
For developers who want to maintain full control over their LLMs or reduce dependency on external APIs, Semantic Router offers support for local models via LlamaCPP and Hugging Face models. Consumer hardware, such as a MacBook running Apple’s Metal hardware acceleration or [Microsoft Copilot+ PC](https://thenewstack.io/copilot-pcs-understanding-microsofts-evolving-ai-pc-stack/), can completely execute routing decisions and LLM-driven responses. This local execution model not only reduces latency and costs but also improves privacy and security.

**Scalability**
Scalability becomes a concern when adding more tools and agents to a workflow. LLMs have limited context windows, meaning they struggle to handle large amounts of data or context. The semantic router addresses this by decoupling decision-making from LLMs, allowing it to handle thousands of tools simultaneously without overloading the system. This separation of concerns allows agents to scale without sacrificing performance or accuracy.

## Use Cases and Scenarios
Agentic AI use cases, which require simultaneous management of multiple tools, APIs, or datasets, are particularly well-suited for Semantic Router. In a typical workflow, the router can rapidly determine which tool or API to use based on the input, bypassing the need for full LLM queries. This is especially useful in virtual assistant systems, content generation workflows, and large-scale data processing pipelines.

For instance, in a virtual assistant, Semantic Router can efficiently route prompts like “schedule a meeting” or “check the weather” to the appropriate API or tool, without involving the LLM for every decision. Similarly, the request can be routed to a fine-tuned LLM meant to respond to medical or legal terminology. This not only reduces latency but also ensures a consistent, reliable experience for users.

The Semantic Router can be used to assess whether the prompt should be sent directly to a small language model operating locally, or whether it has to be mapped to a function and its parameters by invoking a capable LLM running in the cloud. This is particularly relevant in the implementation of [federated language models](https://thenewstack.io/federated-language-models-slms-at-the-edge-plus-cloud-llms/) that take advantage of both cloud-based and local language models.

In the era of agentic workflows, the need for efficient, scalable, and deterministic decision-making systems is more pressing than ever. Semantic Router provides a robust solution by leveraging the power of semantic vector spaces to make fast, reliable decisions, while still allowing integration with LLMs when needed. Its flexibility, speed, and deterministic nature make it an indispensable tool for developers looking to build next-generation AI systems.

As LLMs evolve and diversify, tools like Semantic Router will be crucial for making sure that agentic systems can perform, scale, and give consistent results. This will help developers find new ways to use AI in their workflows.

In the next part of this series, I will walk you through the steps involved in implementing a RAG agent based on the Semantic Router. Stay tuned.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)