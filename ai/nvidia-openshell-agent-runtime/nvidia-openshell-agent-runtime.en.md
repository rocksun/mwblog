The software stack that powers enterprise applications was built for humans. It assumes human-speed interaction, human-managed credentials, and human oversight of every consequential action. Autonomous AI agents break all three assumptions — and [Nvidia](https://www.nvidia.com/en-us/) argues that the entire stack needs to be rebuilt from scratch to account for them.

At the center of that argument is [OpenShell](https://github.com/NVIDIA/OpenShell), an Apache 2.0 open source secure runtime for autonomous agents that Nvidia senior director of AI software [Ali Golshan](https://www.linkedin.com/in/ali-golshan/) and his team have been building for the past six months.

The project, part of Nvidia’s broader [Agent Toolkit](https://nvidianews.nvidia.com/news/ai-agents), is designed to give enterprises a trusted environment in which agents can operate at machine speed without exposing host infrastructure, leaking credentials, or bypassing governance controls.

> “If you want to give more and more autonomy to an agent, the lowest level of the stack should really be a sandbox… That agent should not be interacting directly with your operating system or host or network or infrastructure.”

“When we kind of go back to those principles of what does an agent native software stack look like — if you want to give more and more autonomy to an agent, the lowest level of the stack should really be a sandbox,” Golshan tells *The New Stack*. “That agent should not be interacting directly with your operating system or host or network or infrastructure.”

The problem OpenShell is solving is architectural. Most current tooling was designed around a human user as the trusted actor — the person controlling, monitoring, and moving through an environment at human speed, Golshan says. Agents operate differently.

They’re faster, they can run indefinitely, and they don’t fit cleanly into identity and access models built for people. Lifting a traditional stack and applying it to autonomous agents doesn’t just create inefficiency; it creates security gaps.

## Sandbox first, then the gateway

OpenShell addresses this through a layered approach. Every agent, including its harness and model, gets its own sandbox. Outside each sandbox sits a gateway that maintains credentials and session state. When an agent needs to interact with an external service such as [ServiceNow](https://thenewstack.io/servicenow-ai-governance-agents/), [Salesforce](https://thenewstack.io/snowflake-salesforce-launch-new-standard-to-unify-data-for-ai/), or [Workday](https://www.workday.com/en-us/homepage.html), the gateway handles authentication and passes the session into the sandbox.

The agent itself never holds keys or credentials directly. If something goes wrong, such as a prompt injection or an attempt to execute arbitrary commands, the blast radius is contained within the sandbox.

## Policy below the application layer

Policy enforcement occurs below the application layer, using [Linux kernel primitives](https://thenewstack.io/linux-kernel-cve-system/) such as [seccomp](https://thenewstack.io/4-ways-to-use-kernel-security-features-for-process-monitoring/), [eBPF](https://thenewstack.io/research-ebpf-not-always-a-silver-bullet-for-network-apps/), and Landlock. This is the distinction Golshan draws between security that is baked in versus bolted on.

In a bolted-on model, every product in the stack brings its own enforcement mechanism, creating collision and reliability risks. In OpenShell’s model, policies are enforced at a single horizontal layer that the agent cannot reach or bypass.

“The ability to enforce policies below the application layer — at the same time, you don’t want every single user to be able to do that, because it’s a tricky place to do that,” Golshan says. “So, you want the right level of abstraction and the right level of enforcement.”

OpenShell runs on any environment — desktop, [Kubernetes](https://thenewstack.io/kubernetes/), micro-VMs, cloud infrastructure — and is designed to be agnostic of model, [harness](https://thenewstack.io/ai-agent-harness-pricing-split/), and agent framework. Tools, including [Claude Code](https://thenewstack.io/claude-code-can-now-do-your-job-overnight/) and [Codex,](https://thenewstack.io/openai-codex-claude-code/) can run inside it.

## Enterprise adoption and open contributions

The project is gaining traction beyond Nvidia’s own teams. [LangChain](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/), the developer tools company whose frameworks underpin a significant share of enterprise agent development, announced it will contribute openly to the OpenShell GitHub repository — the development that recently brought the project into public view.

**Last week at the [ServiceNow Knowledge 2026](https://www.servicenow.com/events/knowledge.html) conference in Las Vegas**, the enterprise adoption case became more concrete. Nvidia founder and CEO [Jensen Huang](https://www.linkedin.com/in/jenhsunhuang/) joined ServiceNow chairman and CEO [Bill McDermott](https://www.linkedin.com/in/billrmcdermott/) on stage to announce an expansion of the companies’ collaboration, with OpenShell at the center of the security architecture.

## Project Arc and Action Fabric

ServiceNow is introducing [Project Arc](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-extends-agentic-AI-governance-from-desktops-to-data-centers-with-NVIDIA/default.aspx), a long-running autonomous desktop agent designed for knowledge workers, including developers, IT teams, and administrators. Project Arc uses OpenShell as its secure runtime, with ServiceNow contributing to the project and building on it as a common foundation for enterprise-grade agent execution. The agent connects to [ServiceNow’s Action Fabric](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise/default.aspx) for governance and auditability, and to [ServiceNow AI Control Tower](https://www.servicenow.com/products/ai-control-tower.html) for oversight across the agent lifecycle.

“Project Arc represents the next step in our ongoing collaboration with Nvidia, bringing autonomous execution to the desktop,” said [Jon Sigler](https://www.linkedin.com/in/jon-sigler/), executive vice president and general manager of AI Platform at ServiceNow, in a statement. “By combining OpenShell’s runtime layer with ServiceNow AI Control Tower, and powered by ServiceNow Action Fabric, we’re delivering the governance and security that enterprise AI requires.”

The ServiceNow partnership also advances [NOWAI-Bench](https://github.com/ServiceNow/NOWAI-Bench), an open benchmarking suite for enterprise AI agents built with Nvidia’s [NeMo Gym library](https://docs.nvidia.com/nemo/gym/latest/index.html). The suite includes [EnterpriseOps-Gym](https://enterpriseops-gym.github.io/), one of the more demanding enterprise agent benchmarks currently available, where [Nemotron 3 Super](https://developer.nvidia.com/blog/introducing-nemotron-3-super-an-open-hybrid-mamba-transformer-moe-for-agentic-reasoning/) currently ranks first among open source models.

## The agent-native stack

The deeper argument Nvidia is making with OpenShell extends beyond any single product. Golshan explains it as a set of primitives that need to be rebuilt for an agent-native world — not just sandboxing, but identity, credential management, and policy enforcement, all redesigned around the assumption that the agent is not a trusted user.

> “You can have an agent, and then you can have a whole bunch of specialized agents that know your business, and you can’t treat these traditionally like a human team from an identity or access standpoint… All those primitives and constructs need to be rebuilt.”

“You can have an agent, and then you can have a whole bunch of specialized agents that know your business, and you can’t treat these traditionally like a human team from an identity or access standpoint,” Golshan tells *The New Stack*. “All those primitives and constructs need to be rebuilt.”

Autonomous agents, in Golshan’s view, are already here. The question is no longer when they arrive but whether enterprises can deploy them in regulated industries and sensitive verticals — health, finance, federal — with the controls those environments require. The tooling to bridge that gap, he argues, is what OpenShell and the broader Agent Toolkit are being built to provide.

“Developers are really trying to understand: if I’m working in a regulated industry, what is the stack I need to build that one works for autonomous agents, and two, is trusted?” Golshan says. “The biggest question they’re trying to answer is, what won’t change on me? What can I count on that will be underneath me and stable?”

OpenShell is now available under the Apache 2.0 license on GitHub.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)