# AI Won’t Save You From Your Data Modeling Problems
![Featued image for: AI Won’t Save You From Your Data Modeling Problems](https://cdn.thenewstack.io/media/2025/05/49acc7fd-board-1024x576.jpg)
For years, we’ve treated data quality as an analytics problem, heaving dirty data over the fence to the data team to be cleaned up later in the data warehouse or lake.

This approach doesn’t work for AI. [GenAI applications](https://thenewstack.io/genai-is-quickly-reinventing-it-operations-leaving-many-behind/) operate in real time, making decisions on the fly. If your data is wrong, incomplete or poorly structured, [AI won’t fix it.](https://thenewstack.io/ai/) It’ll just make bad decisions faster.

This is why [data modeling](https://thenewstack.io/data-models-a-key-step-on-your-data-journey/) has to shift left.

You can’t wait until the analytics layer to enforce data quality when AI agents need to reason, plan and act in the moment. It’s like driving a car while only seeing the road every five minutes. How long before you crash?

Let’s explore why AI belongs in the operational layer, why data models matter more than ever and how bridging structured and unstructured data unlocks real-time intelligence.

## AI in the Operational Estate, Not the Analytics Estate
For years, AI followed the same playbook as analytics: Collect data, aggregate it in a warehouse or lake, clean it up, train a model and then use that model to make predictions. That process made sense when AI was purely about retrospective analysis.

But GenAI flips this on its head.

![Traditional model training pipeline with data aggregation in a warehouse](https://cdn.thenewstack.io/media/2025/05/828150bb-image1-1024x315.png)
Traditional model training pipeline with data aggregation in a warehouse

With GenAI, the AI model is already built. The way you make it useful isn’t by aggregating historical data; it’s by feeding it fresh, domain-specific context at runtime. And that context lives in the operational layer, not in a warehouse.

![GenAI applications use general-purpose models but make them app-specific during prompt assembly.](https://cdn.thenewstack.io/media/2025/05/6e463846-image4-1024x560.png)
GenAI applications use general-purpose models but make them app-specific during prompt assembly.

Trying to force AI into the analytics stack doesn’t work. Aggregation is too slow. Reverse ETL (extract, transform, load) can’t patch the gap with brittle and slow point-to-point pipelines. By the time the data is pipelined back from the analytics estate to the operational estate, the data is stale.

For example, consider the chat interaction below with a GenAI-powered assistant for flights. The assistant needs to know recent flights, upcoming flights, the layout of a plane and the customer’s preferences for flying. The most reliable up-to-date information to properly contextualize the prompt for the AI lives in the operational layer of the app stack, like the airline reservation system.

![Example of an AI-powered conversation to re-book a flight](https://cdn.thenewstack.io/media/2025/05/205344fc-image3-1024x398.png)
Example of an AI-powered conversation to rebook a flight

This is why AI belongs in the application stack, embedded in workflows, interacting with live data.

## Data Models: A Critical Component for AI Applications
Historically, data modeling was a business intelligence (BI) and analytics concern, focused on structuring data for dashboards and reports. However, AI applications shift this responsibility to the operational layer, where real-time decisions are made.

While foundation models are incredibly smart, they can also be incredibly dumb. They have vast general knowledge but lack context and your information. They need structured and unstructured data to provide this context, or they risk hallucinating and producing unreliable outputs.

Take retrieval-augmented generation (RAG) as an example.

The common focus is often on semantic search over unstructured, vectorized data, retrieving relevant documents to supply additional context to a large language model (LLM). However, real-world RAG implementations typically require a hybrid approach. This approach involves structured search and data retrieved from databases, CRMs or transactional systems to retrieve precise information like customer records, inventory levels or financial data.

![Hybrid search model for RAG applications](https://cdn.thenewstack.io/media/2025/05/b7c4c447-image5-726x1024.png)
Hybrid search model for RAG applications

With semantic search alone, you may retrieve loosely relevant but inaccurate information, leading to responses that are contextually plausible but incorrect for the specific business case.

Even in purely semantic search applications, having a structured data model that defines relationships between core business entities helps validate LLM-generated responses. A knowledge graph, a specialized form of a conceptual model, provides this structured understanding by capturing entities and their interrelationships within a domain.

For example, consider an application that manages a high-school track meet.

Key entities might include athletes, events and attendees, with relationships such as athletes participating in events and attendees viewing events. However, without a standardized data model, inconsistencies can arise; some might refer to runners instead of athletes, excluding non-running participants, or use spectators instead of attendees, raising questions about whether event judges are included.

![Example data model for a track meet](https://cdn.thenewstack.io/media/2025/05/89bfc0b1-image2-1024x459.png)
Example data model for a track meet

Implementing a knowledge graph ensures a shared, precise understanding of these entities and their relationships. This can be expressed in graph form or natural language, and used directly in prompts to improve accuracy or validate model outputs during post-processing.

[GraphRAG](https://arxiv.org/pdf/2404.16130), a structured and hierarchical approach to RAG, uses knowledge graphs to enhance LLM responses. By modeling entities and relationships as units during retrieval, GraphRAG more accurately understands query intent and provides precise search results. For instance, [Microsoft Research](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data) demonstrated that using LLM-generated knowledge graphs in GraphRAG significantly improves question-and-answer performance when analyzing complex information.
A well-defined data model enables cross-checking of retrieved insights against structured representations, ensuring that outputs are not only generally accurate but also aligned with specific business definitions and relationships. While RAG applications focus on retrieval, AI agents take it a step further by acting on the information. A robust data model provides agents with a clear understanding of the world they operate in, ensuring informed decisions rather than plausible guesses.

## The Future: Data Models for AI Agents
Agents don’t just generate text, they query, update and take action on operational systems. To do this reliably, they need structured data models that define the rules of the world in which they operate.

A well-formed data model enables agents to understand real-time relationships, execute plans and interact with enterprise systems through tool calling and APIs. Without structure, agents face issues with unreliability and will be unable to fully engage with business logic or execute complex workflows.

A data model serves as the ground truth for agents (and all AI applications), enabling them to:

**Validate and refine outputs**– A strong data model ensures that AI-generated responses align with actual business logic, reducing errors and hallucinations.**Understand real-time relationships**– Agents need structured representations of business entities to make sense of data as it changes.**Enable interoperability to downstream systems**– AI applications and agents don’t operate in isolation; their outputs will be consumed by multiple services like data warehouses and other analytical systems. Producing data that adheres to a known data model helps facilitate this process.**Improve orchestration and reliability**– Clearly defined inputs and outputs help coordinate multiple agents, ensuring they work together effectively.**Support tool calling and automation**– Whether retrieving customer records, managing inventory or executing workflows, agents rely on structured data to interact with enterprise applications in a meaningful way.
## Data Modeling Today
Data modeling has evolved far beyond its strictly relational, entity-relationship roots.

Today, polyglot data modeling supports a variety of data types and sources, including relational tables, hierarchical JSON, graph databases, APIs and document stores. This flexibility is crucial for AI applications, which consume and process data from multiple structured and unstructured sources in real time. It unifies these diverse data representations into a single model that AI applications can use.

By integrating data from different databases, APIs, query engines and document stores, this approach simplifies model extraction, design and evolution across both operational and analytical data sources. Developers use modeling tools to create data contracts via REST APIs or schemas, ensuring AI accesses real-time operational data.

### Why AI Needs Polyglot Data Modeling
Traditional data models were built for specific systems, relational for transactions, documents for flexibility and graphs for relationships. But AI requires all of them at once because an AI agent might talk to the transactional database first for enterprise application data, such as flight schedules from our previous example. Then, based on that response, query a document to build a prompt that uses a semantic web representation for flight-rescheduling logic. In this case, a single model format isn’t enough.

This is why polyglot data modeling is key. It allows AI to work across structured and unstructured data in real time, ensuring that both knowledge retrieval and decision-making are informed by a complete view of business data.

Vectors, stored within tables, documents or external vector databases, serve as attributes that link AI-generated knowledge with core business logic. Classic data-modeling principles, whether entity-relationship or domain-driven design, can incorporate vectors as just another attribute, ensuring AI outputs remain structured and contextualized.

### The Importance of Structure in AI Decision-Making
AI introduces a high degree of nondeterminism.

Responses vary; models can drift and errors can propagate unpredictably. In enterprise settings, where reliability and accuracy matter, introducing control wherever possible is critical. When errors occur or bad data is generated, there must be a way to catch and handle issues before they affect operations.

Tools like [Pydantic](https://docs.pydantic.dev/latest/), a Python library, enable developers to define clear data models with specific types and constraints. By enforcing these rules, Pydantic ensures that incoming data adheres to expected formats, reducing errors and enhancing data quality. See the article “[Data Validation With Pydantic](https://www.netguru.com/blog/data-validation-pydantic)” for more on this.

Data models provide structure and control over an inherently stochastic process. They enforce relationships, constraints and validation to keep AI aligned with business rules. A well-formed polyglot model doesn’t just organize data, it adds guardrails, reduces uncertainty and improves the reliability of AI-driven decisions.

Beyond traditional data validation, integrating ontologies and knowledge graphs can further improve the accuracy of AI-driven decision-making.

Recent research demonstrates that using ontologies for query validation and repair in question-answering systems can significantly boost response accuracy. For instance, employing an Ontology-Based Query Check (OBQC) alongside LLM repair techniques increased accuracy from [16% to over 72%](https://arxiv.org/abs/2405.11706), underscoring the value of structured semantic representations in AI applications.

By combining precise data models with semantic structures like ontologies, organizations can establish comprehensive validation frameworks. These frameworks not only ensure data integrity but also provide contextual grounding for AI systems, leading to more accurate and reliable outcomes.

## Practical Considerations for Designing AI Applications
Earlier, we outlined five key goals for data modeling in AI applications. Below, we explore how polyglot data modeling addresses each of these challenges.

### Validate and Refine Outputs
AI can produce responses that are plausible but incorrect.

Polyglot models apply constraints across structured and vector data. These constraints are enforced in physical schemas, ensuring that all data sources maintain integrity.

Domains standardize key data types across APIs and databases. Whether handling customer IDs, order numbers or product SKUs, domains ensure consistent validation and enforcement, reducing the risk of AI-generated errors.

### Understanding Real-Time Relationships
AI agents need to reason over dynamic, real-time data, not just static, preaggregated knowledge.

Polyglot models support semantic web structures and knowledge graphs, enabling AI to map relationships between structured and unstructured data. This is particularly valuable for agents that process information from multiple sources simultaneously.

Additionally, conformed dimensions standardize the way key business entities, such as customers, transactions and products, are represented across systems. This ensures that an AI agent retrieving customer data from a CRM and a support database understands they refer to the same individual, preventing fragmented or misleading insights.

### Enabling Interoperability to Downstream Systems
AI applications rarely operate in isolation; they must interact with multiple systems, data sources and services.

Polyglot models establish a common schema framework, ensuring that AI agents can query, transform and share data consistently across different applications. Conformed dimensions and domains create a shared language for AI systems, making it easier to align structured and unstructured data sources.

By defining flexible, evolvable schemas, polyglot modeling enables AI to join data streams dynamically, supporting schema evolution as business needs change. AI applications can seamlessly adapt to new data sources without requiring extensive rework.

### Improve Orchestration and Reliability
Without structured orchestration, AI agents risk inconsistency and duplication.

Polyglot data models improve orchestration by standardizing the way agents communicate, exchange data and track workflows. By defining clear relationships between entities, they enable agents to maintain shared context across multiple interactions, ensuring consistency even as workflows evolve dynamically.

### Supporting AI Tool Use and Function Calls
AI isn’t just about generating responses, it must execute actions, whether retrieving a customer record, processing an order or triggering a workflow.

Polyglot models connect enterprise data with AI-driven automation for real-time function calls. Agents can interact with APIs and transactional databases while maintaining a structured understanding of which actions are valid based on business rules.

As AI applications evolve, polyglot models allow schemas and APIs to be refined and extended, ensuring AI systems remain aligned with operational requirements. Whether integrating with ERP systems, inventory databases or messaging platforms, a well-structured data model provides the interface AI needs to act with confidence.

## Why Polyglot Data Modeling Matters for AI
AI is only as good as the data it understands. A strong data model keeps it grounded, ensuring accurate outputs, real-time reasoning and seamless system integration.

Shifting left with polyglot data modeling bridges structured and unstructured data, enforcing integrity and making AI reliable. AI won’t replace data modeling; it runs on it.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)