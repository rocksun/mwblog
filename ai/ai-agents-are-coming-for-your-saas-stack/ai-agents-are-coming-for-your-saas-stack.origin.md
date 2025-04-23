# AI Agents Are Coming for Your SaaS Stack
Agentic AI is rapidly emerging as a transformative force in technology, with Google searches for the term increasing by 15,000% in recent months. Industry leaders are calling it the “fifth wave of compute,” positioning it to fundamentally reshape the role of enterprise applications, how they operate, and how they interact with users.

While AI assistants like ChatGPT understand natural language and complete tasks on demand, AI agents take automation to the next level by autonomously fulfilling goals and interacting with other systems. Unlike traditional [robotic process automation](https://thenewstack.io/robocorp-makes-remote-process-automation-programmable/) (RPA) systems that are static and more deterministic, modern agentic systems are stochastic, adaptive and goal-oriented.

The most significant transformation will occur when Software as a Service (SaaS) applications integrate with agentic AI services, creating what Gartner calls an “app/AI ecosystem.” Currently, less than 1% of SaaS systems have been augmented with agentic services, but [Gartner predicts](https://www.gartner.com/en/newsroom/press-releases/2024-03-11-gartner-predicts-one-third-of-interactions-with-genai-services-will-use-action-models-and-autonomous-agents-for-task-completion-by-2028?utm_source=chatgpt.com) a third of global SaaS will be AI-enabled within the next four years.

**Scale and Architecture Challenges**
The scale implications are staggering. In the current mobile computing era, large-scale systems typically handle around 10,000 transactions per second (TPS). In the agentic era, with potentially dozens of AI assistants continuously aiding each user, transaction volumes could increase by two orders of magnitude to around 1 million TPS.

The agentic shift requires a fundamental architectural change from transaction-centered to conversation-centered systems. Traditional SaaS applications are built on stateless business logic executing CRUD operations against relational databases. In contrast, agentic services maintain state within the service itself and store each event to track how the service reached its current state.

A critical architectural challenge stems from the stateless nature of [large language models](https://thenewstack.io/what-large-language-models-can-do-well-now-and-what-they-cant/) (LLMs). Unlike databases that maintain state, LLMs don’t remember prior conversations. This necessitates maintaining a conversation journal where all prior exchanges must be included with each new request to provide context. As these journals grow, they eventually hit token capacity limits, requiring careful management strategies.

**Multimodal Inputs and Real-Time Processing**
Agentic systems aren’t limited to text-based chat interfaces. They will increasingly incorporate Internet of Things (IoT) sensors, metrics, audio and video inputs, creating [real-time data streams](https://thenewstack.io/bridging-the-data-gap-real-time-user-facing-analytics/) that must be processed, augmented and forwarded to the appropriate models without overwhelming the system. Balancing what the agentic system processes in real time against what the slower, more expensive LLMs can handle remains a delicate challenge.

**Performance and Cost Considerations**
The performance profile of agentic applications differs dramatically from traditional CRUD applications. Where relational databases typically have latencies of 10–30 milliseconds, LLMs operate at latencies that are 100 times greater. Additionally, the cost per transaction increases by as much as 10,000 times compared to database-only environments, with the most sophisticated LLMs being up to 850,000 times more expensive per transaction than a database call.

There is some optimism regarding costs, as LLM pricing has consistently decreased by 90% year-over-year for the past three years, while maintaining the same level of accuracy. This trend suggests cost efficiency will continue to improve, though not at the same dramatic rate.

**Production Challenges**
Getting agentic systems into production remains difficult. A Gartner survey found that 52% of organizations failed to deploy their agentic systems successfully. Failures stemmed from experimental approaches, data quality issues, security concerns, cost equations that didn’t work and technologies ill-suited for concurrency, memory management or 24/7 operation. Many organizations take more than eight months to move from proof-of-concept to production.

Deployment strategies vary, with organizations considering cloud native platforms (62%), virtual private clouds (about one-third) and self-hosted Kubernetes environments (about half). Many organizations are considering multiple deployment models simultaneously.

**The Future of SaaS and Agentic AI**
While agentic AI services will increasingly augment SaaS applications, they’re unlikely to replace them completely. The high latency of the agentic processing loop makes it unsuitable for high-volume, real-time user interactions. This means that SaaS applications will still need to provide the necessary API and multiuser concurrency interfaces.

The interfaces to SaaS applications will become increasingly multimodal, with more audio-visual interaction. Specific applications may become predominantly (70–80%) agentic, with the ratio varying by use case.

For enterprises considering agentic services, key cost factors include LLM hosting (either via cloud services priced per token or self-hosted), compute and memory requirements, [vector database storage](https://thenewstack.io/onehouse-automates-vector-embedding-for-its-data-lakehouse/) for semantic search and the agentic platform itself. While operational management is similar to traditional SaaS systems, the biggest challenge is ensuring explainability and traceability as AI models evolve.

As we enter this new era, organizations must carefully balance performance, cost and [user experience considerations to successfully implement agentic AI systems](https://thenewstack.io/graphql-can-compose-headless-systems-to-boost-user-experience/) that deliver on their full transformative potential.

**Akka’s Suggested Blueprint for Agentic Services**
Akka has developed a comprehensive blueprint for agentic services consisting of five essential elements. First, streaming endpoints are necessary for handling multimodal, real-time data. Second, [agent connectivity adapters enable integration with vector databases](https://thenewstack.io/how-ai-agents-are-about-to-change-your-digital-life/), LLMs and third-party systems. Third, agent orchestration serves as the core, providing durable workflows that support parallel processing and human-in-the-loop approaches. Fourth, a context database must exist within the platform itself, both in-memory and durable, to maintain history and support the conversation style of these systems. Finally, lifecycle management provides governance mechanisms, with the entire system needing security, scalability and observability.

Akka differentiates its platform by treating LLMs as event-driven machines rather than batch-based systems. Their adapters are nonblocking with back-pressure capabilities, allowing events to stream from LLMs back into the system for reasoning or out to endpoints. A key advantage is that API services and agentic services run on shared compute, avoiding “island problems” and increasing efficiency for both regular services and expensive LLM invocations.

The Akka platform aims to accelerate agentic AI application delivery as these technologies move from data science departments into core delivery organizations. There are two common pitfalls: the “workflow island” problem that reduces productivity and increases costs, and the “framework trap,” where initially simple tools face production issues like locking concurrency and memory management challenges.

Akka views this as a stack evolution, coining the term “A-tier architecture” to describe how agentic services augment rather than replace existing SaaS architecture. Their implementation includes nonblocking asynchronous LLM adapters, automatic in-memory and durable context databases, an event-driven system benchmarked to 10 million TPS, developer-friendly workflow tools and multiregion deployment capabilities with replication filtering for compliance requirements.

Akka has several successful implementations, including the open source SMILE project, which powers machine learning (ML) systems in major companies like Amazon and Google; Swiggy, which achieved a 90% improvement in latency; and startups like Horn that provides AI augmentation for video calls, and Coho AI, which reportedly reached market 75% faster using Akka.

Looking forward, Akka sees the industry moving toward better integration with business databases and systems through metadata structures that allow LLMs to interact with and take action on enterprise data. Their approach positions Akka as the fastest way for [building agentic AI services](https://thenewstack.io/tutorial-build-a-rag-agent-with-azure-ai-agent-service-sdk/) that both reason and transact.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)