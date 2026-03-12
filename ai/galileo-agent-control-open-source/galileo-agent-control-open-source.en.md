[Galileo](https://galileo.ai/), a company known for its AI observability and guardrails technology, on Wednesday released [Agent Control](https://github.com/agentcontrol/agent-control), an open source control plane designed to help enterprises govern AI agents at scale.

The platform allows organizations to write behavioral policies once and enforce them across all agent deployments.

AWS, CrewAI, and Glean will be among the first partners to offer Agent Control. This will give their customers access to centralized governance frameworks for managing agent behavior in production.

There’s certainly a growing market for this technology. According to [IDC, use of AI agents among Global 2000 organizations is expected to increase tenfold by 2027](https://www.idc.com/resource-center/blog/agent-adoption-the-it-industrys-next-great-inflection-point/). This, in turn, means token and API call volumes will spike by a factor of 1,000.

[Tim Law](https://www.linkedin.com/in/tim-law-airesearch/), IDC’s Research Director for AI and Automation, says in a press release about the news, “Centralized management of policies can help organizations manage AI agent behaviors. A unified control plane and centralized governance can help deploy AI agents at scale while ensuring continual improvement through evaluation and lifecycle management.”

What Agent Control brings to the table is a standardized way for companies to apply guardrails across agents, enabling:

* A centralized policy layer for enforcing governance and blocking unsafe behaviors at runtime.
* Real-time updates to agent policies without requiring downtime or code modifications.

[Vikram Chatterji](https://www.linkedin.com/in/vikram-chatterji), Galileo’s co-founder and CEO, tells *The New Stack* that in practice, this means instead of using hard-coded, brittle safety rules, “Agent Control lets developers define guardrails once and apply them everywhere. By open-sourcing this under Apache 2.0, we’re ensuring every enterprise and developer community can use it without vendor lock-in.”

> “Agent Control lets developers define guardrails once and apply them everywhere. By open-sourcing this under Apache 2.0, we’re ensuring every enterprise and developer community can use it without vendor lock-in.”  
> — Vikram Chatterji, co-founder and CEO, Galileo

As the name suggests, the company claims that Agent Control will connect easily to any agent and supports guardrail evaluators from any vendor or custom in-house tools. Policies remain portable across environments, giving teams flexibility as they evolve their agent ecosystems.  
Galileo anticipates that common use cases include preventing LLM hallucinations, enforcing data privacy rules, steering model selection to control token costs, and ensuring tone consistency in customer-facing AI agents.

Of course, Agent Control isn’t the only such product in the market. Others include [Humanlayer Agent Control Plane](https://github.com/humanlayer/agentcontrolplane), an open source, Kubernetes‑native orchestrator for AI agents; [GitHub Enterprise AI Controls](https://docs.github.com/copilot/concepts/agents/enterprise-management), GitHub’s governance layer for AI agents; and [Microsoft Agent 365](https://www.microsoft.com/en-us/microsoft-agent-365), Microsoft 365’s control plane for AI agents in Azure.

Despite this strong competition, hundreds of AI teams, including Fortune 50 enterprises, use Galileo’s existing platform to test, monitor, and secure AI applications that handle high volumes of traffic and data. It appears the company has the technical and business chops needed to be a player in the agent control space.

> “The number one blocker for enterprise agents is no longer the models. Those are getting better every day. To graduate agents to production, the industry needs transparent, community-driven guardrails.”  
> — Dev Rishi, GM of AI, Rubrik

As [Dev Rishi](https://www.linkedin.com/in/devvret-rishi-b0857684/), GM of AI at [Rubrik](https://www.rubrik.com/), a security cloud company, tells *The New Stack*, “The number one blocker for enterprise agents is no longer the models. Those are getting better every day. To graduate agents to production, the industry needs transparent, community-driven guardrails. Open source projects like Agent Control are exactly the kind of open standards the industry needs to make autonomous agents safe for the enterprise.”

Agent Control is now available under the Apache-2.0 license, with source code, SDK, and documentation available on GitHub.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)