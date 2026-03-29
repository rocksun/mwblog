So many agents, so little time to evaluate them. [Solo.io](http://solo.io)‘s new projects can help.

[Agentic AI](https://thenewstack.io/agentic-ai-powerful-but-fragile-what-you-need-to-know/) has blown up. These tools have become hotter than hot. But, there’s this little problem. How do you evaluate them? Solo.io, best known for its cloud-native networking and API gateway platform, Gloo, has launched a new open-source initiative called [AgentBench](https://github.com/THUDM/AgentBench). It’s designed to help developers evaluate and benchmark “agentic AI” systems.

[Solo.io](http://solo.io) announced the project at [KubeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) in Amsterdam. According to Solo.io founder and CEO [Idit Levine](https://www.linkedin.com/in/iditlevine), autonomous AI systems pose new challenges for cloud operations.

“Enterprises are experimenting with AI copilots and infrastructure agents, but they lack visibility into how these systems behave when given open-ended goals. gentBench helps teams understand not only what the models can do, but where their reasoning breaks down,” Levine tells *The New Stack*.

Levine continues, “Evaluation is the biggest unsolved problem in agentic infrastructure today. Organizations have frameworks for building agents, gateways for connecting them, and registries for governing them, but no consistent way to know whether an agent is actually reliable enough to trust in production.” Aye, there’s the rub.

AgentBench provides a framework for testing the effectiveness of AI agents in real-world workflows, such as infrastructure automation, API orchestration, and service management. The goal is to give enterprise teams a standardized way to measure the reliability, latency, and success rates of autonomous agents before deploying them in production.

> “Evaluation is the biggest unsolved problem in agentic infrastructure today. Organizations have frameworks for building agents, gateways for connecting them, and registries for governing them, but no consistent way to know whether an agent is actually reliable enough to trust in production.”

The framework integrates with Solo.io’s Gloo Platform and [Envoy Proxy](https://www.envoyproxy.io/). This enables you to simulate multi-step tasks, such as configuring microservices, updating routing policies, or troubleshooting Kubernetes clusters under controlled conditions. Each run generates reproducible logs, metrics, and outcome data that can be used to compare different AI backends or agent architectures.

The company claims that “AgentBench is the first benchmark designed to evaluate LLM-as-Agent across a diverse spectrum of different environments.” To do this, the program relies on [OpenTelemetry](https://opentelemetry.io/).

> “Whether you’re using commercial APIs or open LLMs like Llama 3, you need transparent metrics for decision-making. … We want AgentBench to become a common reference point for the AI operations community.”

In addition, Solo says the open-source project is part of a broader effort to make AI-driven operations auditable and trustworthy. Levine says, “Whether you’re using commercial APIs or open LLMs like Llama 3, you need transparent metrics for decision-making.“ We want AgentBench to become a common reference point for the AI operations community.”

AgentBench is available on GitHub under the Apache 2.0 license. Solo.io plans to collaborate with other cloud-native vendors and AI research groups to expand the test library and integrate with common ML evaluation tools.

In addition, Solo.io  donated its [agentregistry](https://aregistry.ai/) an AI-native open source registry for AI agents, MCP tools, and Agent Skills to the Cloud Native Computing Foundation (CNCF). This program enables you to standardize how AI capabilities are catalogued, discovered, and governed across the enterprise.

As everyone and their uncle swiftly moves to Agentic computing, I expect both programs will find many fans.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)