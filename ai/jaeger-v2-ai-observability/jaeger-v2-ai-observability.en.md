As software architectures evolve, observability tools must adapt. When the industry moved to microservices, distributed tracing became a necessity. Jaeger emerged as a core tool for engineers to understand those fragmented systems. Now, as organizations integrate generative AI applications and autonomous agents into production, tracing requirements are shifting again. Mapping the execution path of an AI agent involves prompt assembly, vector database retrievals, and multiple external tool calls.

> “By adopting the Model Context Protocol (MCP), Agent Client Protocol (ACP), and Agent–User Interaction Protocol (AG-UI), the project is building an environment where engineers and AI agents can collaborate.”

Jaeger is evolving to address these new workloads. This transition involves two main phases. First, the project rebuilt its core architecture in Jaeger v2 to natively integrate OpenTelemetry. Second, Jaeger is expanding beyond standard data visualization. By adopting the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/), [Agent Client Protocol (ACP)](https://agentclientprotocol.com/), and [Agent–User Interaction Protocol (AG-UI)](https://ag-ui.com), the project is building an environment where engineers and AI agents can collaborate. This helps map the complex execution paths of AI pipelines that often stretch the limits of traditional tracing tools.

## Setting the foundation: Jaeger v2

Managing AI workloads requires an efficient [data collection pipeline](https://thenewstack.io/data-pipelines-serve-ai/). This need guided the architectural changes detailed in the CNCF blog post, [Jaeger v2 released: OpenTelemetry in the core!](https://www.cncf.io/blog/2024/11/12/jaeger-v2-released-opentelemetry-in-the-core/)

Jaeger v2 replaces its original collection mechanisms with the OpenTelemetry Collector framework. This approach consolidates metrics, logs, and traces into a unified deployment model. By natively ingesting the OpenTelemetry Protocol (OTLP), the system eliminates intermediate translation steps, improving ingestion performance. This OpenTelemetry integration provides the necessary data foundation for more advanced tracing features.

## Human and agent collaboration

Building on Jaeger v2, the project is exploring new ways for teams to analyze distributed systems. The goal is to facilitate collaboration between engineers and AI agents during debugging. Contributors from the [CNCF LFX Mentorship](https://www.cncf.io/people/mentoring/) program and [Google Summer of Code (GSoC)](https://summerofcode.withgoogle.com/) are actively driving this work.

To support AI integration, Jaeger is adopting three open standards: the [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-roadmap-2026/), Agent Client Protocol (ACP), and Agent–User Interaction Protocol (AG-UI). MCP standardizes how AI models securely access external data sources. ACP provides a uniform method for user interfaces to communicate with AI agents and sidecars. Together, they allow Jaeger to function as an interactive workspace.

## Building the backend protocol layer

The technical implementation starts in the backend. We are building an Agent Client Protocol layer to act as a stateless translator between the Jaeger frontend and external AI sidecars. The design and proof of concept are documented in [Jaeger backend issue #8252 (Implement AG-UI to ACP Jaeger AI)](https://github.com/jaegertracing/jaeger/issues/8252) and [issue #8295 (Implement ACP-based AI handler)](https://github.com/jaegertracing/jaeger/issues/8295).

![Diagram of Jaeger v2's technical implementation](https://cdn.thenewstack.io/media/2026/04/e1b018fa-1-1024x683.png)

(Or

```

mermaid
graph LR
  J_UI["Jaeger UI"]
  AI_A["AI Agent"]
  subgraph JAEGER["Jaeger v2"]
    AGW["Agent Gateway"]
    JMCP["Jaeger MCP"]
  end

  J_UI -- "AG-UI Protocol" --> AGW
  AGW -- "ACP Protocol" --> AI_A
  AGW -- "MCP Protocol" &lt;--> JMCP

```

)

Traditionally, incident responders build queries by manually filtering services and tags. The ACP integration allows the backend to parse natural-language constraints (such as identifying 500-level errors in a payment service with latency exceeding 2 seconds) and translate them into deterministic trace queries.

Organizations can configure this backend to use cloud-based [large language models](https://thenewstack.io/ml-and-llm-adoption-challenged-most-often-by-observability/) (LLMs) for complex reasoning or local small language models (SLMs) for strict data privacy. The depth of analysis depends on the chosen model, as noted in [industry analyses of hosted versus local AI infrastructure](https://www.algolia.com/blog/engineering/hosted-vs-local-llm-ai-infrastructure). By restricting the AI to protocol translation and query generation, the architecture minimizes the risk of hallucinations associated with open-ended chatbots.

### The collaborative UI workspace

The Jaeger user interface is also being updated to support this backend logic. As tracked in [Jaeger UI issue #3313](https://github.com/jaegertracing/jaeger-ui/issues/3313), we are migrating from legacy Redux to modern Zustand + React Query.

The frontend introduces an in-app assistant powered by assistant-ui + AG-UI. The UI uses streaming events to send trace context (such as error logs and key-value tags) to the backend gateway. This allows engineers to prompt the assistant to summarize a failure path within a specific span, reducing the need to manually review raw log lines during an incident.

### Visualizing GenAI execution paths

Beyond using AI to analyze standard traces, the project is adding support for tracing the AI applications themselves.

Outlined in [Jaeger issue #8401 (GenAI integration)](https://github.com/jaegertracing/jaeger/issues/8401), this work focuses on visualizing the rapidly evolving OpenTelemetry GenAI semantic conventions. The OpenTelemetry community is currently drafting specifications to standardize telemetry for these highly dynamic workflows. Key initiatives include emerging drafts for [Generative AI Agentic Systems (Issue #2664)](https://github.com/open-telemetry/semantic-conventions/issues/2664) to track tasks, memory, and actions, and conventions for [AI Sandboxes (Issue #3583)](https://github.com/open-telemetry/semantic-conventions/issues/3583) to monitor ephemeral code execution environments.

> “Jaeger will map these new standard operations in the UI to provide clear visibility into AI execution paths without locking teams into vendor-specific formats.”

Developers building Retrieval-Augmented Generation (RAG) pipelines and autonomous agents need to measure embedding model latency, track external tool calls, and monitor token usage. Jaeger will map these new standard operations in the UI to provide clear visibility into AI execution paths without locking teams into vendor-specific formats.

### Unified observability: from local testing to production

Maintaining consistency across testing and production environments is a practical challenge. Jaeger originally popularized an “all-in-one” executable to simplify local testing. Because Jaeger v2 is built on the OpenTelemetry Collector, developers run the exact same binary locally as they do in production.

During testing, engineers can run the Jaeger v2 container with a local SLM. This creates a private sandbox for testing generative AI traces or debugging ACP integrations without exposing data to external APIs.

In production, platform teams deploy the same unified binary, often using tools like the [OpenTelemetry Operator](https://opentelemetry.io/docs/kubernetes/operator/) for Kubernetes. Organizations can then replace the local SLM with a larger cloud-based LLM to handle production incident analysis. This ensures that tracing configurations remain consistent from development to deployment.

## What’s next

Tracing requirements are shifting to accommodate the complexity of AI applications. By establishing a solid OpenTelemetry foundation with Jaeger v2 and integrating MCP and ACP standards, the project is adapting its core capabilities. This technical path forward enables a practical workflow where human engineers and AI agents collaborate to diagnose distributed system failures.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/10/193816f6-cropped-48c67001-jonah-kowall2.jpg)

Jonah Kowall has spent his career at the intersection of cybersecurity, IT operations, and observability. This journey started in the late '90s when he co-founded one of the first content filtering companies and contributed to the FreeBSD project, including some...

Read more from Jonah Kowall](https://thenewstack.io/author/jonahkowall/)