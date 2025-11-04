Context is king in the agentic world. Pairing a performant reasoning model like [Claude](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/), [DeepSeek](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/) or [GPT-5](https://thenewstack.io/gpt-5-a-choose-your-own-adventure-for-frontend-developers/) with the right context drives efficient planning and tool usage and improves multistep reasoning, leading to personalized conversations, higher task accuracy and relevant responses.

In this article, we present the need for context engineering and associated benefits, identify challenges developers face as they use it for developing AI agents, and propose a high-level architecture to help address them.

## **Solving the Context Dilemma: Too Much vs. Too Little**

Enterprises have access to vast amounts of structured and unstructured data. However, feeding this data as context directly to agents leads to confusion around task comprehension due to inherent noise and loss of important information, which can hurt a large language model’s (LLM) situational awareness as the limited context window is breached. Using a [long context is not always the solution](https://thenewstack.io/solving-the-rag-vs-long-context-model-dilemma/) to this problem, as I’ve written before. On the other hand, sending too little context can cause agents to hallucinate. Simply put: garbage in, garbage out.

Context engineering refers to a collection of techniques and tools used to ensure an AI agent has only the necessary information to complete assigned tasks successfully. Based on the concept of [context engineering](https://blog.langchain.com/the-rise-of-context-engineering/) described by Harrison Chase of LangChain, context engineering consists of the following:

* **Tool selection** means ensuring the agent has access to the right tools for retrieving the information needed to accomplish the specified task. For example, consider a scenario where an agent is asked to complete an action, such as planning a trip to Maui for a family with two kids and a dog. It should be able to retrieve all tools that are required to answer the user’s question and execute tasks reliably.
* **Memory use** is also a factor. It’s important to equip the agent with short-term memory that provides context for personalizing the ongoing session between the user and the agent, as well as long-term memory that offers context across multiple sessions to make the interactions cohesive, factual and even more personalized. This spans various memory types such as profile, semantic, episodic, conversational and procedural. It also includes working memory, which is used for sharing context for seamless task coordination among agents in a multiagent system.
* Another component is **prompt engineering.** This ensures the agent has access to the right prompt, which is clearly defined in terms of the agent’s behavior, including specific instructions and constraints.
* Finally, there’s **retrieval.** Dynamically [retrieving relevant data](https://thenewstack.io/enterprise-ai-success-demands-real-time-data-platforms/) based on the user’s question and inserting it into the prompt before sending it to the LLM ensures AI success. This is achieved by using Retrieval-Augmented Generation (RAG) and direct database calls. Enterprises generally have a polyglot environment with multiple sources of truth. In such cases, the [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP) allows developers to retrieve context from numerous data sources in a standardized manner.

The above context is shared with the agent and subsequently the reasoning LLM. Augmenting the agent prompt with relevant tool names along with the associated tool spec, contents of the short and long-term memories, prompt and relevant content retrieved from RAG, databases and SaaS services ensures successful task execution. Figure 1 shows a conceptual view of the architecture for context engineering.

[![Figure 1: Conceptual view of the architecture for context engineering (source: Couchbase)](https://cdn.thenewstack.io/media/2025/10/e981f99d-image1-1024x455.png)](https://cdn.thenewstack.io/media/2025/10/e981f99d-image1-1024x455.png)

Figure 1: Conceptual view of the architecture for context engineering (source: Couchbase).

This is how it works. First, the user sends a request to the multiagent system. The agent application then retrieves context via APIs that span prompts and tools from the catalog; context for RAG from the vector store; summarized conversations from the short- and long-term memories; and summaries, sentiments and extracted entities from the operational database, including sources external to the database, using various MCP servers.

The agent application then augments the prompt with the consolidated context to create the agent prompt, which is sent to a reasoning model such as Claude, DeepSeek or GPT-5. The reasoning loop is triggered within the agent framework, like LangGraph, which exchanges messages with the reasoning model, during which several relevant tools are called.

Depending on the agent architecture, other agents may be called and context shared between them. Afterward, the generated answer is sent to the user, and the user-agent conversation is stored in memory to ensure continuity in conversations in subsequent sessions.

Here are a few challenges that developers face during context engineering and how the aforementioned architecture could help address them.

## **Extracting Context From Unstructured Data at Scale**

Eighty percent of enterprise data is unstructured and is largely unusable as context. Therefore, to extract the context required to power important use cases, developers currently write extract, transform, load (ETL) jobs for Spark, Flink or other data processing engines. These jobs read [unstructured data from a source database](https://thenewstack.io/from-unstructured-data-to-rag-ready-with-docling/), process it and write back results for subsequent consumption by agents. These DIY solutions, albeit performant, not only slow down developer velocity but also create operational and maintenance overhead.

A few example use cases include summarizing the details of the “support\_ticket\_desc” field in a document so that the customer support AI agent can easily understand and take action; extracting medical terms (diseases, medications, symptoms) from the “patient\_diagnosis” field so that a triaging agent can come up with an initial diagnosis for the patient; and labeling whether text in the “email\_content” field is “irrelevant,” “promotional spam,” “potentially a scam” or “phishing attempt” so an email assistant can reason whether to automatically respond to an email.

AI functions allow developers to invoke LLMs from within SQL statements with the ability to write prompts to control the format, tone and other aspects of the LLM output. Here’s an example: A developer augments product reviews stored in a database with sentiment and summary using AI functions. A retail AI agent later reads it via a tool call and reasons whether to provide a compelling offer to a dissatisfied user to improve the Customer Satisfaction Score (CSAT) based on the severity of the issues they reported. This [agent also creates a product feature request](https://thenewstack.io/ai-agents-protocols-driving-next-gen-enterprise-intelligence/) to drive.

Consider the following product review left by a customer who was disappointed with the performance and durability of a blender:

*“I had high hopes for this blender based on the product description and reviews, but it’s been a let-down from day one. The motor struggles even with soft fruits, and it overheats after just a couple of minutes of use. I’ve had to stop mid-smoothie several times to let it cool down, which completely defeats the purpose of having a ‘high-speed’ blender.”*

Here’s a no-code analysis using SQL:

|  |  |
| --- | --- |
| SQL Statement | Response |
| **SELECT** review\_id,  SUMMARIZE(review\_text) AS summary,  SENTIMENT(“review\_text”, prompt = “Evaluate the sentiment of the “customer\_review” field on a 5-point scale: very negative, negative, neutral, positive, very Positive”) AS sentiment  **FROM**customer\_reviews  **WHERE** review\_text IS NOT NULL; | “sentiment”: very negative “summary”: The blender needs a stronger motor to handle frozen fruits and ice without overheating, sharper blades for smoother blends and a better-sealed lid to prevent leaks. Durability should be improved to eliminate loud grinding noises and burning smells after short-term use. |

This requires an underlying database that automates the above tasks in a no-code manner by invoking leading LLMs from within SQL statements.

## **Fitting Context Into a Limited Context Window**

When it comes to context, less (but relevant) is more! A 1-million+ token limit does not mean you can treat the context like unlimited memory. Each additional token has cost, latency and performance implications. Instead of stuffing the prompt with long, unnecessary context, causing important details to get lost (especially in the middle of the prompt), consider using techniques like RAG to keep the context lean and highly relevant.

Listing all available tools that the LLM could use leads to prompt bloat and potentially confuses the agent due to similar tools having similar names or tool specs. Further, the proliferation of tools caused primarily by a lack of tool reusability and governance maximizes the likelihood of agent failure. However, cataloging all tools in a centralized location not only supports reusability but also retrieves only the tools that are relevant to answering the user’s question. This can be used in conjunction with well-written tool descriptions and tool routing to boost tool call accuracy. For example, the below API could retrieve only the tools within the agent application that are relevant to answer the user’s query:

```
catalog.find_tools(query="Plan a trip to Maui")
```

Agent behavior is highly sensitive to the quality of prompts; hence, changes to the prompts should be carefully managed. Cataloging all prompts with versioning and rollback support ensures consistent agent behavior, despite changes to the prompt. For example, the below API could retrieve only the prompt that is relevant to the query, keeping the context accurate:

```
catalog.find_prompt("query="Plan a trip to Maui")
```

You can achieve this by using a performant multimodel database, which allows you to extract context from a large volume of structured and unstructured data using [vector search](https://www.youtube.com/watch?v=Z7DoCAbgZgk) via RAG, and store and select highly relevant tools and prompts.

## **Managing Decay and Resolving Conflict in Agent Memory**

Agent memory is a critical building block of context engineering. However, implementing memory decay and conflict resolution is not a trivial undertaking for developers.

Conversational agents accumulate vast amounts of data from their interactions. If an agent remembers every single past message, the context window will quickly fill up, leading to a loss of coherence and the inability to process new information. Hence, it is necessary to decay outdated information.

The challenge here is that information decays at different rates. For example, the return policies of a retailer do not change as frequently as the demand for fast fashion clothing. Hence, there is a need to implement information-specific Time to Live (TTL) in the memory across various user conversations so that a clothing recommendation agent does not recall outdated information from memory.

Additionally, developers need the option to delete outdated context from memory when necessary. This requires that agent memory be implemented using a database that supports TTLs to decay memory at desired rates and also to delete memory in a consistent manner as needed.

In a multiagent system, a single agent could have conflicting information, or perhaps multiple agents within the same user session might try to commit conflicting information to memory. This conflict can be resolved by using a timestamp for each message and sharing that with the LLM as context about how the information evolved. Further, the message could also be annotated with the agent name and other information so that the LLM can decide which piece of information goes with the memory.

## **Sign up for a Preview**

At Couchbase, the ability to engineer context and serve it quickly is paramount, allowing developers to create performant and reliable agents. With Couchbase [Capella AI Services](https://www.couchbase.com/products/ai-services/), currently in private preview, and [Capella](https://www.couchbase.com/products/capella/) NoSQL DBaaS, you can use a single data platform that encompasses various stores — such as operational, analytics, vectors, tools, prompt and memory — to extract context using [SQL++](https://www.couchbase.com/products/n1ql/) and augment your prompt. AI functions, an AI Services capability, automates the extraction of context from a large volume of data by invoking leading LLMs from within familiar SQL statements. An agent memory implemented using Couchbase allows tackling complex agent memory issues like memory decay and conflict resolution.

Sign up for a [private preview](https://info.couchbase.com/capella-ai-services-signup?_gl=1*18nnzn9*_gcl_aw*R0NMLjE3NTg1NjY0MTYuQ2owS0NRanc1OFBHQmhDa0FSSXNBRGJEaWx4RTJpeTZLNkh0QTBpUGoxM1FEeVFvQ1dkV2pPRTktRUh3NUpIOUQtY0Q3RmFxY0doRUIzWWFBbURKRUFMd193Y0I.*_gcl_au*ODYwOTQwNDUuMTc1NTExNzI4Nw..) of Capella AI Services and try Capella NoSQL DBaaS for [free](https://cloud.couchbase.com/sign-up), and start building your agentic application.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/01/0abb09e1-cropped-3897dda1-kiran-matty-600x600.jpg)

Kiran Matty is lead product manager, AI/ML at Couchbase.  Before joining Couchbase, Kiran held product management roles at AWS, Aerospike and Hortonworks.

Read more from Kiran Matty](https://thenewstack.io/author/kiran-matty/)