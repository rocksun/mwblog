AI is moving fast. In fact, AI advancement and adoption are moving faster than any shift we’ve seen since cloud native. New models, new tools and new use cases seem to appear every week. According to Gartner, by 2026, more than 80% of enterprises will have used [generative AI (GenAI)](https://thenewstack.io/genai-is-quickly-reinventing-it-operations-leaving-many-behind/) in production environments. For teams running production systems, that pace means [observability](https://thenewstack.io/introduction-to-observability/) has to keep up.

The challenge? With AI, monitoring isn’t just about uptime and responsiveness, although they are still important. Most AI systems are built on a [cloud native stack](https://thenewstack.io/introduction-to-cloud-native-computing/). On top of the already massive scale, cost and data problems that cloud native systems create, we now need to keep an eye on:

* **Model behavior** (hallucinations, drift, toxicity)
* **Token economics** (how much each answer costs)
* **GPU infrastructure** (queues, utilization and throughput)

[AI observability](https://chronosphere.io/solutions/scale-ai-operations/?utm_source=TNS&utm_medium=sponsored-content) introduces a whole new set of telemetry to understand these new areas. In other words, in AI observability, both the challenges and scale evolve and compound. Now, more than ever, you need control of your AI observability telemetry in order to [contain costs](https://chronosphere.io/solutions/control-costs/?utm_source=TNS&utm_medium=sponsored-content), improve performance and [troubleshoot faster](https://chronosphere.io/platform/ddx/?utm_source=TNS&utm_medium=sponsored-content).

Observability telemetry control is about maximizing value density: retaining the signals that deliver the most visibility per dollar spent. To achieve this, you need visibility into how your observability data is used relative to what it costs, so you can decide if it’s worth keeping. Control is about being able to understand usage and cost side by side.

AI introduces a slew of new telemetry, along with a host of never-before-seen operational challenges that observability must help solve. Site reliability engineers (SREs) now find themselves owning AI and inference incidents, not just traditional infrastructure outages. Nondeterministic AI systems introduce new, high-visibility failure modes that make observability more critical than ever.

As the stakes are raised, confidence in AI starts with observability and control.

## **The AI Moment We’re In**

The AI field has moved from decades of research and periodic AI winters to a breakneck cycle of investment and deployment. GPUs unlocked the parallel compute needed for modern AI, and generative models brought that capability into everyday products, driving adoption across industries. The net effect: an “AI arms race,” a rapidly expanding vendor landscape and a step-change in data and application complexity for engineering teams to manage.

## **The AI We Mean**

There are many branches of AI. My focus here is GenAI and specifically large language models (LLMs). LLMs are AI models that are trained on vast amounts of text to generate context-aware responses for interfaces like chat, code assistants and support bots. That’s the surface area [driving new reliability](https://chronosphere.io/platform/scalable-and-reliable-data-stores/?utm_source=TNS&utm_medium=sponsored-content), safety and cost concerns in production.

## **How To Think About Observability and AI**

AI + observability can be viewed through two lenses:

* **AI observability:** Applying modern observability to AI workloads and use cases.
* **AI-assisted observability:** Using AI inside the observability platform to speed investigation and outcomes.

As AI adoption grows, users are investing in both fronts. For example, AI-assisted observability, facilitated by [Model Context Protocol (MCP) servers](https://github.com/chronosphereio/chronosphere-mcp?utm_source=TNS&utm_medium=sponsored-content), enables customers to integrate LLMs and agents with their existing systems, thus achieving observability outcomes programmatically.

For this article, I will focus on AI observability and the AI use cases that need it the most.

## **Why AI Changes the Observability Problem**

AI workloads don’t start from a clean slate. They inherit every hard problem we already wrestle with in cloud native systems:

* **Massive scale** with billions of requests.
* **Distributed architectures** that are notoriously difficult to troubleshoot.
* [**High cardinality**](https://chronosphere.io/learn/what-is-high-cardinality/?utm_source=TNS&utm_medium=sponsored-content) that explodes label dimensions.
* The ever-present **cost pressure** from storing and processing petabytes of telemetry data.

Cloud native observability was already a high bar to clear, demanding sophisticated tools, constant trade-offs and some way to control your observability telemetry for cost and performance reasons.

AI raises that bar even higher. On top of all the above, teams must now contend with GPU saturation and queuing, LLM-specific latency and throughput issues, and multistep dependencies like Retrieval-Augmented Generation (RAG) pipelines or agent chains that introduce new points of failure.

There’s also a new economic dimension: token accounting and the tight coupling of infrastructure usage to per-request costs. And unlike traditional systems, AI workloads introduce behavioral risks such as hallucinations, bias, drift and toxicity that affect not just reliability but also trust and safety.

## Observability Challenges for AI Workloads

Existing O11y Challenges for cloud native environments

New AI-Specific O11y Challenges ✨

Massive Scale  
*Billions of requests, petabyte data volumes*

Model Behavior Issues  
*Drift, bias, hallucinations, toxicity*

Mission–Critical Reliability  
*Zero-downtime expectations*

Token Economics  
*Usage tracking, cost optimization, budget overruns*

High Performance  
*Sub-second response requirements*

Complex Dependencies  
*Multi-step workflows, RAG pipelines, agent chains*

System & Troubleshooting Complexity  
*Microservices, distributed architectures, correlation*

Model Performance  
*Latency, throughput, quality degradation*

Observability Costs & Data Volume  
*Tool sprawl, data retention, license fees, data growth*

GPU Infrastructure  
*Utilization, queuing, resource contention*

High Cardinality  
*Infinite label combinations, dimension explosion*

Eval and Training Performance  
*Behavior, consistency, latency, quality degradation*

This is where reliability, safety and unit economics converge, and where the observability challenge doesn’t just evolve, it grows in complexity and urgency.

Fortunately, there are open source SDKs like OpenInference and OpenLLMetry that make it easier to access the telemetry needed to understand and solve these AI-specific challenges. And they make this easier by providing insights in the industry-standard OpenTelemetry format. In addition, NVIDIA DCGM is able to export GPU performance and utilization metrics in Prometheus format, which makes it simple to incorporate them into observability platforms.

## **4 AI Use Cases and How Observability Shows Up**

The AI market clusters into four recurring use cases. Each demands a tailored observability approach:

| **Use Case** | **Segment Description** | **Observability Requirements** |
| --- | --- | --- |
| **Model Builders** | Foundation/model teams running training pipelines and evaluation loops. | Require visibility across training and inference pipelines, with rapid detection of model performance degradation, failed evaluations and infrastructure bottlenecks. |
| **GPU Providers** | Platform teams operating multitenant GPU clusters and schedulers. | Need real-time telemetry for allocation, saturation, job health and tenant performance across shared clusters to keep fleets fully utilized. |
| **AI-Natives** | Product companies shipping LLM-powered apps with rapid iteration. | Fight prompt-chain blind spots, retrieval logic regressions, latency hot spots and memory pressure. |
| **Feature Builders** | Traditional enterprises adding AI features to existing services. | Need cohesive end-to-end visibility and accurate cost attribution from the AI layer down to infrastructure. |

## **A Foundational AI Observability Strategy Is Required**

For all AI use cases, a foundational strategy involves:

* Focusing on the workloads that matter.
* Establishing crisp service-level objectives (SLOs) around user experience, cost and safety.
* Making the signals involved first-class through the use of OpenTelemetry.
* Optimizing cost and performance by applying control techniques to your observability telemetry.

That’s how you ship fast, contain spend and keep trust high as AI adoption surges. Or said another way: Apply observability where AI meets scale, because that’s where the engineering and business impact compound.

Observability for AI is the operating system for reliable, safe and cost-efficient LLM, RAG and GPU systems. Make it first-class with control, and the rest follows.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/04/0d81a968-cropped-7ac8e42c-daniel-juengst-600x600.jpeg)

Dan Juengst serves as the lead for Enterprise Solutions Marketing at Chronosphere. Dan has more than 20 years of experience in areas such as streaming data, observability, data analytics, DevOps, cloud computing, grid computing and high performance computing. Dan has...

Read more from Dan Juengst](https://thenewstack.io/author/dan-juengst/)