Cloud monitoring specialist [Groun](https://www.groundcover.com/)[dcover announced an expansion of its AI Observability service this Wednesday.](https://www.groundcover.com/) The move sees the company add native support for agentic AI systems fully compatible with [Google Vertex AI](https://thenewstack.io/googles-vertex-ai-platform-gets-freejacked/), the cloud giant’s platform for building and training machine learning models.

In the quest for clarity and insight into how agentic functions make their decisions, Groundcover positions its technology as a window into how an organization’s application estate uses AI across models, and throughout considerations, including cost, [latency](https://thenewstack.io/why-latency-is-quietly-breaking-enterprise-ai-at-scale/), use of prompts, agent behavior, and tool execution. In simple terms, software engineering teams can trace every LLM interaction.

Operating on a BYOC ([Bring Your Own Cloud](https://thenewstack.io/saas-is-broken-why-bring-your-own-cloud-byoc-is-the-future/)) approach, Groundcover delivers its services within an organization’s on-premises cloud, so all data is processed within the customer’s infrastructure and environment.

## A new kind of visibility gap

As organizations now integrate LLMs into production systems, they’re encountering a new kind of visibility gap.

[Orr Benjamin](https://www.linkedin.com/in/orr-benjamin/), VP of product at Groundcover, tells *The New Stack* that traditional observability tools were designed for deterministic software, not systems where dynamic prompts drive outputs.

“When you move from traditional services to multi‑step agentic workflows, the classic observability pillars of [logs, metrics, and short traces](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/) start to break down,” Benjamin says. “Instead of a 20‑hop [microservices trace](https://aws.amazon.com/what-is/distributed-tracing/) [when a request leaves one service and makes a connection to another], a team might be dealing with a two‑hour session and 50,000 tool calls, so the core challenge becomes reconstructing and summarizing what actually happened in a way that users care about.”

> “When you move from traditional services to multi‑step agentic workflows, the classic observability pillars of logs, metrics, and short traces start to break down.” – Orr Benjamin, VP of product at groundcover.

As a result of these challenges, Groundcover says it has seen teams struggle to understand how AI-powered features behave in real-world environments, including what inputs drive outputs, how responses vary, and how usage affects costs. This lack of visibility makes it difficult to ensure reliability, optimize performance, and then scale AI-driven applications.

## No instrumentation required

Since launching [LLM Observability](https://www.groundcover.com/ai-observability/llm-observability) in August 2025, Groundcover has been running in production AI environments across its customer base, capturing LLM interactions automatically via its patented [eBPF sensor](https://thenewstack.io/what-is-ebpf/), a lightweight data collection agent that “listens” to all server events at the kernel level without having to be “instrumented” (i.e., coded into existence) before use. Because no instrumentation is required, all data remains inside a customer’s cloud.

This release from Groundcover aims to address what the company says real-world production deployments have revealed as the next unsolved problem: visibility into multi-step agentic systems.

“Because groundcover captures data at the kernel level with eBPF, below the application layer, it sees what your agent is actually doing, not what the application reports is happening. If a coding agent can inject traces or manipulate logs at the application level, your observability is only as honest as the agent itself, Benjamin says.

He explains that, crucially, this matters – especially as agents become more autonomous. Because infrastructure context is captured alongside AI behavior, this means that if an agent were to ask, “Why did my cost spike?”, it could provide an answer informed by a complete data context, showing that LLM token costs surged because the underlying [Kubernetes node was memory-starved](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/), which throttled the service and drove up retries.

In terms of new functionalities from Groundcover, AI Observability now surfaces complete agent execution traces. This means that every model call, every [tool invocation](https://www.ibm.com/think/topics/tool-calling) (along with its arguments i.e. the structured parameters that govern interactions with external tools, APIs or systems), and the reasoning path connecting them. Configurable focus levels let engineers work at the right altitude, from provider-level aggregates down to individual span detail.

## Span-level token tracking

Accurate cost attribution includes prompt caching. Token costs are tracked at the span level (when a specific sequence of tokens represents a distinct entity or phrase) and account for the full pricing complexity of modern LLM APIs, correctly distinguishing between regular input tokens, cache creation tokens, and cache read tokens. Teams can see what individual agents run and the sessions actually cost.

As noted above, Google Vertex AI support is also present and that means groundcover’s automatic capture now extends to teams building on Google Cloud’s managed AI infrastructure, with all observability data remaining inside the customer’s own environment, and zero instrumentation.

> “A token usage spike that looks like an AI problem might actually be a memory-starved Kubernetes node causing retries.”

Benjamin underlines the developments here and says that the company’s platform has taken care of the way data moves from the monitored environment to the managed backend, i.e., it is designed to keep it contained, reducing network costs by over 95% compared to traditional architectures while ensuring data never transits to an external party. This, he says, is a deliberate architectural choice that makes groundcover’s multi-cloud support genuine, rather than nominal.

The company once again reminds us that groundcover supports AWS, GCP, and Azure because it is genuinely BYOC, whatever the C (cloud) is.

Because the eBPF sensor captures everything at the kernel level, regardless of which LLM provider an application calls, Groundcover delivers observability into reasoning paths, token usage, and response quality without touching code. That kind of answer, connecting LLM behavior to infrastructure telemetry, is only possible when both live in the same platform, on the same timeline, in the same query language… and this is the foundation for why groundcover thinks it has covered observability comprehensively for the multi-step agentic workflow era.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)