With the release of “reasoning” models capable of multistep, test-time compute, the intelligence required to solve complex problems is accessible via a standard API.

For the enterprise technical leader, this looks like progress. But it introduces a massive, hidden scalability ceiling.

The trap is relying on the [large language model (LLM)](https://thenewstack.io/what-is-a-large-language-model/) to act as its own middleware. Teams often expose existing API endpoints, which were built for a strict contract for microservices and not for LLMs and [rely on system prompts to call the right API](https://thenewstack.io/ai-agents-are-dumb-robots-calling-llms/), with the right extracted parameters.

The assumption is that as the tool-calling capabilities of LLMs improve, it can understand the semantics or business logic behind the APIs. This is a fallacy. In an LLM-powered agentic workflow, your best “contract” is a natural language prompt. This is non-deterministic technical debt. You are effectively swapping stable service interfaces for probabilistic guesses.

When you deploy a general agent without a [shared semantic layer on top of your data](https://thenewstack.io/agentic-ai-is-coming-but-can-your-data-infrastructure-keep-up/) and APIs, you aren’t building a scalable product; you are building brittle glue code.

## From Imperative Glue to Agentic Protocols

In the previous era of distributed systems, “glue code” meant hard-coded Python logic to get `customer_id` from API A, transform the JSON and post it to API B. Today, the industry is shifting toward agents that act as “universal adapters,” inspecting capabilities at runtime rather than relying on brittle, pre-written integration scripts.

But without a governed domain layer, even these advanced capabilities merely accelerate the rate at which you generate unverified output. The difference between a pilot and a production asset is no longer the [model or the agentic framework](https://thenewstack.io/5-ways-to-transform-itops-with-a-human-and-ai-agent-model/) you choose. It is the governed architecture you build to scale them.

## The Limits of the ‘Vector Puddle’

Most enterprise AI pilots are state-of-the-art reasoning engines choked by flat-file topologies or lossy information retrieval.

Data teams typically attack this with the standard industry pattern: retrieval-augmented generation (RAG) pipelines using vector databases (often upgraded to hybrid search with keyword extraction). This approach is excellent for information retrieval — finding a specific paragraph that matches a specific query.

However, it fails at multi-hop reasoning.

Vector databases rely on cosine similarity, a geometric calculation of “closeness” in an embedding space. This works for semantic matching but fails at transitivity. It cannot reliably navigate a chain of logic across disparate documents.

Consider a failure scenario in an industrial context:

* **Document A** notes that “Pump X” feeds “Valve Y.”
* **Document B** notes that “Valve Y” is susceptible to “Pressure Warning Z.”

If an engineer asks, *“*What are the risks to Pump X?*“* a standard vector search will likely fail because “Pump X” and “Pressure Warning Z” never appear in the same context chunk. In the vector embedding space, they are topologically distant. The vector database sees two unrelated clusters of data; it cannot “hop” from A to B to C to synthesize the answer.

You are left with a system that can retrieve facts but cannot traverse relationships.

## Understanding GraphRAG vs. a Domain Knowledge Graph

Engineers often ask: Why not just do GraphRAG?

GraphRAG is powerful for query-time retrieval. It encodes entities and relations so the [model can traverse context](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) and perform multihop reasoning during generation. You should use it to improve factual grounding and reduce hallucinations in Q&A.

But GraphRAG does not replace a domain knowledge graph (DKG).

Think of it this way: GraphRAG is a retrieval technique that traverses the edges found in the text. The DKG is the infrastructure that defines the *state* of the system.

Consider the difference between reading a manual and knowing the machine’s status:

* **GraphRAG** retrieves a safety protocol stating that if vibration exceeds 5mm/s, the system must trigger an emergency stop.
* **DKG** knows that “Turbine-4” is currently in a “startup sequence” where high vibration is temporary and expected.

Without the DKG to manage that state, the agent hallucinates a crisis. It retrieves the correct rule but applies it to the wrong context to trigger a false shutdown.

For production scale, you need both: DKG for operational context and state management and GraphRAG for better retrieval on top of that state.

To break the “glue code” cycle, engineering teams must build on a governed architecture defined by three layers:

1. **The context layer (DKG):** Unifying disparate schemas into a single ontology.
2. **The orchestration layer:** Managing the “slider of autonomy” from human-in-the-loop to fully autonomous.
3. **The governance layer: policy as code:** Acting as a CI/CD gate for AI decisions.

Here is what this playbook looks like in practice, within the unforgiving environment of financial crime prevention.

## Deep Dive: The Governed Playbook (Financial Services)

Few environments are as unforgiving as anti-money laundering (AML). In the standard stack, rules-based detection models can generate up to ~95% false positives because they lack context.

A governed architecture changes the physics of the workflow by introducing sub-vertical precision.

### 1. The Context Layer: Sub-vertical Precision

A generic “financial services” data model is insufficient. Risk signals for casino gaming (chip-walking) are fundamentally distinct from life insurance (beneficiary fraud).

The DKG must resolve identities specific to those sub-sectors. This treats the ontology as a reusable semantic asset, reducing schema mapping from weeks to hours.

### 2. The Orchestration Layer

Rather than allowing agents to wander, the architecture treats the investigation as a governed, multistep workflow. It moves from fully autonomous data gathering (retrieving Know Your Customer docs) to semi-autonomous drafting (suspicious activity report narratives) and requires human-in-the-loop sign-off before submission.

### 3. The Governance Layer: Policy-as-Code

Governance isn’t a post-hoc audit; it is a hard gate. If the agent’s narrative cites a transaction that isn’t in the evidence log, the system rejects the output. You get a mathematically auditable decision trail, not just a chat log.

#### *Table 1: Governed AI architecture in an AML workflow*

*Unlike standard RAG pipelines, this workflow uses a DKG to resolve entity identity during ingestion (Step 01) and enforces policy as code before final output (Step 05).*

|  |  |  |  |
| --- | --- | --- | --- |
| **Stage** | **Enabling AI** | **Role / Action** | **Outcome** |
| Data ingestion | Agentic + DKG | Automate schema mapping and entity resolution using Financial Industry Business Ontology standards. | **Metric:** Onboarding reduced from weeks to hours. |
| Anomaly detection | Predictive | Use ML to uncover risk signals and remove false positives. | **Metric:** False positives cut by >80%. |
| Alert triage | Agentic | L1 Investigators receive auto-compiled case files (KYC, transactions). | **Metric:** 80%+ reduction in manual “swivel-chair” steps. |
| Investigation | Generative | L2 Investigators receive likely root cause and narrative drafts with evidence. | **Metric:** Investigation time reduced from >100 min to <20 min. |
| Audit | Agentic | Enforce policy as code across the workflow. | **Metric:** Deterministic audit trails. |

## The ‘Day 2’ Reality: The Hidden Cost of Context

For many engineering leaders, the instinct is to build this stack from first principles. The architectural pattern seems clear: Spin up a graph database like Neo4j or Amazon Neptune, pull an open standard like the Financial Industry Business Ontology (FIBO), and write the ingestion scripts to map your data.

This is a valid pattern. It is entirely possible to build this stack yourself. Tech giants like Google and Meta maintain massive internal engineering teams to do exactly this.

However, the risk is not in the build phase. It is in the Day 2 operations.

The trap is assuming that a graph database is the same thing as a semantic layer. If you take the DIY route, be prepared to own two perpetual engineering loops that have nothing to do with your core product:

1. **The integration tax (schema drift):** Every time an upstream API changes (for instance, Salesforce updates a field), your custom ETL (extract, transform, load) pipelines break. You are now in the business of maintaining connectors rather than shipping features.
2. **The math ceiling (entity resolution):** The trap isn’t writing the Python script to map the schema. The trap is the mathematical ceiling of entity resolution. Determining if ‘J. Smith’ is ‘John Smith’ across 10 million records requires quadratic comparisons. Doing this in real time for an AI agent isn’t a scripting problem; it’s a distributed compute problem. If you build this yourself, you aren’t building an AI app; you’re accidentally building a master data management (MDM) platform.

Building your own semantic translation layer is the architectural equivalent of rolling your own auth database. Just as engineering teams now treat identity management as a managed platform capability rather than a DIY feature, the complexity of entity resolution demands a managed layer.

The engineering teams that win will not be the ones writing the best ingestion scripts. They will be the ones who treat context as procured infrastructure, rather than a bespoke engineering project.

## The Verdict: Stop Building Glue Code

The lesson for the technical leader is clear: Intelligence is a commodity, but context is not.

You can swap Gemini 3 for GPT-5 tomorrow, and the “intelligence” cost will only go down. But while the cost of intelligence drops, the cost of context rises. Smarter models demand structured, relational data to reason effectively.

Engineering leaders must decide where their team’s leverage lies. If you build your own semantic layer, you are effectively signing up to maintain a bespoke ORM for the AI era. It is a valid path, but one that requires dedicated teams for ontology maintenance, not just prompt engineering.

To see how this architecture compresses industrial maintenance root cause analysis from 48 hours to 10 minutes, view the complete workflows on the [SymphonyAI blog](https://resource.symphonyai.com/scaling-production-ai-playbook).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/12/28c0bd78-cropped-b65b4333-raj-shukla.jpeg)

As chief technology officer, Raj Shukla drives SymphonyAI’s technology roadmap and execution. He leads the engineering team that builds the Eureka Gen AI platform, SymphonyAI’s data and AI platform. Raj’s team includes AI researchers and machine learning scientists working on...

Read more from Raj Shukla](https://thenewstack.io/author/raj-shukla/)