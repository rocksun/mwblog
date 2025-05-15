# A2A, MCP, Kafka and Flink: The New Stack for AI Agents
![Featued image for: A2A, MCP, Kafka and Flink: The New Stack for AI Agents](https://cdn.thenewstack.io/media/2025/04/a2f99b46-a2a-mcp-kafka-flink-stack-ai-agent-1024x576.jpg)
Before the web had Hypertext Transfer Protocol (HTTP), and before email had Simple Mail Transfer Protocol (SMTP), we were stuck with custom integrations, fragmented systems and brittle workflows. It wasn’t until open protocols and shared infrastructure emerged that the internet truly scaled, unlocking the modern web, global communication and entire economies.

Today, [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) are in this same pre-standardization phase. They’re powerful, capable and multiplying fast, but they don’t work together. One agent analyzes data. Another one drafts code. A third automates customer relationship management (CRM) workflows. But they’re isolated, siloed and unaware of each other’s existence.

That’s starting to change.

A new stack is emerging to support this next layer of the internet — one built not for humans browsing websites, but for autonomous agents collaborating across systems. At the core are four open components:

: A protocol for agents to discover and communicate.[Google’s Agent2Agent (A2A)](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/): A standard for tool use and external context.[Anthropic’s Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/): An event-driven communication fabric for reliable, decoupled coordination.[Apache Kafka](https://kafka.apache.org/): A real-time processing engine to enrich, monitor and act on streams of agent activity.[Apache Flink](https://flink.apache.org/)
Let’s explore how these technologies fit together, why protocols alone aren’t enough and how this new stack provides the infrastructure needed to move from disconnected bots to dynamic, intelligent agent ecosystems.

## The Problem: Fragmented Agents, Fragile Infrastructure
If the hype is right — and it’s looking more like inevitability than speculation — most companies won’t just deploy one AI agent; they’ll deploy dozens. These agents will write code, triage support tickets, analyze customer data, manage onboarding, monitor infrastructure and more.

But today’s tooling isn’t ready for that future.

![](https://cdn.thenewstack.io/media/2025/04/4af93a6d-fragmented-agents-1013x1024.png)
The island of agents (Source: Confluent)

We’re not just facing the [“island of agents” problem](https://medium.com/@seanfalconer/the-ai-silo-problem-how-data-streaming-can-unify-enterprise-ai-agents-0a138cf6398c), where agents operate in silos and can’t communicate; we’re facing a broader ecosystem fragmentation problem:

**Agents don’t talk to each other**: Each agent runs in its own sandbox. The CRM agent doesn’t know what the data warehouse agent just discovered. The support agent can’t respond to the same anomaly that the monitoring agent just flagged.**Tool usage is brittle and bespoke**: Without a standard for invoking tools or external APIs, agents end up with hardcoded integrations and non-reusable logic.**Frameworks lack consistency**: Different agent runtimes use different models — some treat agents like chatbots, others like directed acyclic graphs (DAGs), others like recursive planners. There’s no portable execution layer or shared state.**We’re building as if agents live in notebooks**: Most agents today are designed like one-off prototypes — linear, synchronous and ephemeral. But real systems aren’t notebooks. They need to handle retries, failures, coordination, logging and scaling. That requires infrastructure.**No backbone for collaboration**: There’s no event bus, no shared memory, no traceable history of what agents did or why. Everything is locked in direct HTTP calls or buried in logs.
As the[ 12-Factor Agents](https://github.com/humanlayer/12-factor-agents) project argues, agents need to follow cloud native principles: They must be observable, loosely coupled, reproducible and infrastructure-aware. But today, most are built as brittle scripts, stitched together by hand and assumed to run in isolation.

The result? Silos. Duplication. Fragility.

The solution isn’t to shove all agents into one monolithic platform. It’s to build a shared stack, a new foundation based on open protocols, event-driven architecture and real-time processing.

Agent2Agent addresses part of the problem by giving agents a common protocol for discovery and communication. But to go beyond toy demos, to reach the scale and reliability production systems demand, we need more than protocols. We need infrastructure.

## How Agents Talk and Act: A2A and MCP
As mentioned, the agent ecosystem today looks a lot like the early web: powerful systems, each doing useful work, but siloed and incompatible. Just like browsers once struggled to talk to servers without a standard protocol, AI agents today can’t easily discover, communicate or collaborate with one another.

Google’s A2A protocol is a bold attempt to fix that. It’s not another agent framework: It’s a universal protocol meant to connect *any* agent, regardless of who built it or where it runs.

Just like HTTP standardized how websites communicate, A2A defines a shared language for agents. It lets them:

**Announce capabilities**via an`AgentCard`
, a JSON descriptor that declares what an agent can do and how to interact with it.**Send and receive tasks**through structured interactions (using JSON-RPC), where one agent requests help and another responds with results or “artifacts.”**Stream updates with server-sent events (SSEs)**, enabling real-time feedback during long-running or collaborative tasks.**Exchange rich content**. Files, structured data and forms — not just plain text — are all first-class parts of A2A messages.**Stay secure by default**thanks to built-in support for HTTPS, authentication and permissions.
What makes A2A promising is that it doesn’t try to reinvent the wheel. It builds on decades of internet protocol history, just like HTTP and SMTP did, by leveraging familiar, battle-tested web standards. That makes adoption easier and integration faster.

But A2A is only one half of the picture.

Anthropic’s MCP tackles the other half: how agents use tools and access context. MCP standardizes how agents invoke APIs, call functions and integrate with external systems — essentially, how they think and act in the world. A2A, on the other hand, defines how agents talk to each other.

If MCP is about giving agents access to tools, A2A is about giving them access to each other.

Together, these two protocols offer a blueprint for a connected agent ecosystem:

**MCP**powers individual agent intelligence.**A2A**enables collective intelligence.
And just like HTTP and SMTP didn’t succeed in isolation, they required adoption, infrastructure and developer tooling, A2A and MCP will need an ecosystem to realize their potential.

But even with standardization like A2A and MCP, a fundamental question remains: How do these agent communications scale effectively across a complex, dynamic enterprise environment? Relying solely on direct, point-to-point connections defined by these protocols creates its own set of challenges, particularly around scalability, resilience and observability. This leads us to the need for a robust underlying communication infrastructure.

## We Need an Event-Driven Backbone, Not Just Protocols
Imagine running a company where every employee can communicate only by sending direct, one-on-one messages. Need to share an update? You have to message each person individually. Want to coordinate a project across five teams? You’re stuck manually relaying information between every group.

Now imagine trying to scale that to hundreds of employees. Chaos.

That’s exactly what happens in agent ecosystems built on direct connections. Every agent must know who to talk to, how to reach them and when they’re available. As the number of agents grows, the number of required connections grows exponentially. The system becomes brittle, hard to manage and nearly impossible to scale.

A2A and MCP give agents the language and structure to communicate and act, but language alone isn’t enough. To coordinate dozens or hundreds of agents across an enterprise, you also need infrastructure for how those messages move and how agents react to them.

That’s where [Apache Kafka and Apache Flink](https://thenewstack.io/building-a-meal-planning-agent-with-apache-kafka-and-flink) come in.

### Kafka and Flink: A Quick Primer
[Apache Kafka](https://www.confluent.io/lp/apache-kafka/?utm_medium=sem&utm_source=google&utm_campaign=ch.sem_br.nonbrand_tp.prs_tgt.kafka_mt.xct_rgn.namer_sbrgn.unitedstates_lng.eng_dv.all_con.kafka-what-is_term.what-is-apache-kafka&utm_term=what%20is%20apache%20kafka&creative=&device=c&placement=&gad_source=1&gbraid=0AAAAADRv2c0xMf9u9gysZ9gIjG7xOxO7U&gclid=Cj0KCQjw_JzABhC2ARIsAPe3ynpCOCYZ1DXfQO31ozymoakcUf_1NqNVBaKF0U7DNqQkc2-ZPmFMlpYaAoKmEALw_wcB) is a distributed event streaming platform originally developed at LinkedIn and now part of the Apache Software Foundation. It acts as a durable, high-throughput message bus, allowing systems to publish and subscribe to streams of events in real time. Kafka is used everywhere, from financial systems to fraud detection to telemetry pipelines, because it decouples producers from consumers and [ensures data](https://thenewstack.io/how-to-handle-bad-data-in-event-streams/) is durable, replayable and scalable.
[Flink](https://www.confluent.io/learn/apache-flink/), also an Apache project, is a real-time stream-processing engine. It was designed from the ground up for stateful, high-throughput, low-latency event processing. Where Kafka handles the movement of data, Flink handles the transformation, enrichment, monitoring and orchestration of that data as it flows through a system.
Together, they form a powerful duo: Kafka is the bloodstream, Flink is the reflex system.

## Kafka and Flink: Infrastructure for Agent Ecosystems
Just as A2A is emerging as the HTTP of the agent world, Kafka and Flink form the event-driven foundation that can support scalable agent communication and computation. They solve problems that direct, point-to-point communication can’t:

**Decoupling**: With Kafka, agents don’t need to know who will consume their output. They publish events (e.g.,`"TaskCompleted"`
,`"InsightGenerated"`
) to a topic; any interested agent or system can subscribe.**Observability and replayability**: Kafka maintains a durable, time-ordered log of every event, making agent behavior fully traceable, auditable and replayable.**Real-time decisioning**: Flink enables agents to[react in real time to streams](https://thenewstack.io/real-time-ai-apps-using-apache-flink-for-model-inference/)of events, filtering, enriching, joining or triggering actions based on dynamic conditions.**Resilience and scaling**: Flink jobs can scale independently, recover from failure and maintain state across long-running workflows. This is essential for agents that perform complex, multistep tasks.**Stream-native coordination**: Instead of waiting for a synchronous response, agents can coordinate through streams of events, publishing updates, subscribing to workflows and progressing state collaboratively.
In short:

- A2A defines how agents speak.
- MCP defines how they act on external tools.
- Kafka defines how their messages flow.
- Flink defines how those flows are processed, transformed and turned into decisions.
## How A2A, MCP, Kafka and Flink Work Together
Protocols like A2A and MCP are essential for standardizing agent behavior and communication. But without an event-driven substrate like Kafka and a stream-native runtime like Flink, these agents remain stuck in isolated interactions, unable to coordinate flexibly, scale gracefully or reason over time.

To fully realize the vision of enterprise-grade, interoperable AI agents, we need four layers:

**Protocols**: A2A, MCP – to define the*what.***Frameworks**: LangGraph, CrewAI, ADK – to define the*how.***Messaging infrastructure**: Apache Kafka – to support the*flow.***Real-time computation**: Apache Flink – to support the*thinking.*
Together, this is the new internet stack for AI agents — a foundation for building systems that are not only intelligent, but also collaborative, observable and production-ready.

![Architectural diagram: How A2A, MCP, Kafka and Flink Work Together](https://cdn.thenewstack.io/media/2025/04/ebbd97e8-a2a-mcp-kafka-flink-architecture.png)
How A2A, MCP, Kafka and Flink work together. (Source: Confluent)

## The Road Ahead: Building for Collective Intelligence
We’re at a pivotal moment in the evolution of software.

Just as the original internet stack — protocols like HTTP and SMTP, and infrastructure like TCP/IP — unlocked a new era of global connectivity, a new stack is emerging for AI agents. But instead of humans navigating pages or sending emails, this stack is built for autonomous systems working together to reason, decide and act.

A2A and MCP provide the protocols for agent communication and tool use. Kafka and Flink provide the infrastructure for real-time coordination, observability and resilience. Together, they make it possible to move from disconnected agent demos to scalable, intelligent production-grade ecosystems.

This isn’t just about solving engineering challenges. It’s about enabling a new kind of software where agents collaborate across boundaries, providing insight and action flow in real time, allowing intelligence to become a distributed system.

But this vision won’t realize itself. We need to build it: openly, interoperably and with the lessons of the last internet revolution in mind.

So the next time you’re building an agent, don’t ask just what it can do. Ask how it fits into the larger system. Can it communicate? Can it coordinate? Can it evolve?

Because the future isn’t just agent-powered; it’s agent-connected.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)