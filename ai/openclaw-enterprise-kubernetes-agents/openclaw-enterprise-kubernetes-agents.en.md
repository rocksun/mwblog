OpenClaw has come a long way since it emerged as a viral weekend project less than a year ago. Created by Austrian developer [Peter Steinberger](https://www.linkedin.com/in/steipete/) in late 2025, the self-hosted AI agent exploded in popularity and by February — when [OpenAI hired Steinberger](https://www.reuters.com/business/openclaw-founder-steinberger-joins-openai-open-source-bot-becomes-foundation-2026-02-15/) — it had already amassed more than 100,000 GitHub stars.

In the intervening months, OpenClaw has gone to great lengths to bring more rigor to the project, tightening up [its persistent-agent architecture](https://thenewstack.io/openclaw-persistent-agent-architecture/), investing heavily in security, adding new [agent harness options](https://thenewstack.io/openclaw-hermes-agent-harness/), and [establishing](https://thenewstack.io/openclaw-foundation-nonprofit-status/) the independent OpenClaw Foundation to oversee the project. This included sponsors such as OpenAI, Nvidia, Red Hat, and GitHub, as well as a slew of other big-name companies who committed to contributing resources.

Now, it’s making perhaps its clearest push yet into becoming a serious business play with [OpenClaw Enterprise](https://docs-enterprise.openclaw.org/) (OCE), an open-source, “vendor neutral” platform for managing agents.

## OpenClaw gets an enterprise control plane

Giving persistent agents access to codebases, credentials, plugins, messaging channels and other company systems creates an obvious problem for enterprise IT: the more useful those agents become, the more consequential their permissions and actions can be.

In a [blog post](https://openclaw.ai/blog/openclaw-enterprise) published on Tuesday, [Kevin Lin](https://www.linkedin.com/in/kevinslin-nimbus/), a member of technical staff at OpenAI leading OCE efforts, argues that many companies still see agent platforms as too difficult to police centrally, leaving prohibition as the default.

> “The default stance of IT in most organizations is to ban agentic platforms like OpenClaw altogether.”

“The main feedback we hear from organizations is that a stronger common security, safety, and governance standard is needed before agents can be fully adopted,” Lin writes. “As a consequence, the default stance of IT in most organizations is to ban agentic platforms like OpenClaw altogether.”

OpenClaw Enterprise is still in its embryonic phase. Lin says that the project is currently “being developed in the open before its 1.0 release” later this year, adding that it’s suitable for internal pilot projects only right now.

So there is still some distance to travel before OCE can reasonably be considered a finished enterprise platform. But much of its intended shape is already visible.

At the center of OCE is the OpenClaw Control Plane (OCC), which gives administrators a central place to deploy agents, separate them into isolated namespaces, manage configuration and credentials, set permissions, and keep a record of changes made through the platform. The agent activity itself happens separately: gateways receive messages, while harnesses handle agent turns, model calls and tool execution.

Ultimately, OCE is being built for environments where multiple agents, users and teams may share the same underlying infrastructure, with controls around who can access what, and how individual agent deployments are isolated from each another.

In terms of gaps, OpenClaw’s [architecture documentation](https://docs-enterprise.openclaw.org/) says its API, console, persistent worker, PostgreSQL backend, and Kubernetes packaging are already implemented, while areas including external gateway admission, workload authentication back to OCC and some approaches to model authentication remain unfinished.

> “OCE is built to run on your own infrastructure and will always be free for any organization to use.”

That unfinished state is at least partly why OpenClaw has released OCE as an open-source project this early. The idea is to let companies inspect and adapt the software themselves, while giving outside developers a chance to shape the project before the formal release. The code is [already available on GitHub](https://github.com/openclaw/openclaw-enterprise), with a [getting started guide](https://docs-enterprise.openclaw.org/#getting-started) for running it locally or deploying it inside an organization.

“OCE is built to run on your own infrastructure and will always be free for any organization to use,” Lin notes.

## The Kubernetes playbook, applied to agents

OpenClaw Enterprise has an interesting provenance. OpenAI was its original home before the company handed the project over to the OpenClaw Foundation. Red Hat and Nvidia have since contributed to its development, while OpenAI and Red Hat are already testing the software internally.

> “Think of it as Kubernetes for agents.”

There’s also a fairly explicit Kubernetes-inspired idea permeating the project: OpenClaw wants OCE to provide a common layer for managing agents across different environments. “Think of it as Kubernetes for agents,” the project’s official [documentation](https://docs-enterprise.openclaw.org/) notes.

That comparison carries through to how OCE is actually deployed. Its full local development environment runs the control plane, PostgreSQL, and agent workloads inside a Kubernetes cluster, while companies can install OCE into Kubernetes infrastructure they already operate. The documentation does include a Docker or Podman Compose option, although that’s currently limited to a control-plane preview and cannot deploy agents through OCC.

Taking to LinkedIn, Lin also draws a clear Kubernetes (K8) comparison, reflecting OpenClaw’s longer-term ambitions for the project.

> “Similar to how K8 became the standard for deploying containers in the cloud, we want OCE to be that for agents.”

“Similar to how K8 became the standard for deploying containers in the cloud, we want OCE to be that for agents,” Lin [writes](https://www.linkedin.com/feed/update/urn:li:activity:7510806587981344768/).

Red Hat, for its part, sees the emergence of enterprise agents through a similar lens. In a separate [blog post](https://www.redhat.com/en/blog/why-red-hat-building-open-foundation-enterprise-agents-openclaw-enterprise) published on Tuesday, [Joe Fernandes](https://www.linkedin.com/in/joefernandes1/), VP and general manager of Red Hat’s AI business unit, drew a line from the move away from proprietary Unix systems to Linux, through the rise of containers and Kubernetes, and now to agents. His argument is that Red Hat can apply what it learned helping bring those earlier technologies into enterprise environments to this next generation of software.

“Throughout Red Hat’s history, some of the biggest changes in enterprise computing have been driven by fundamental shifts in how applications are built and operated,” Fernandes writes. “Red Hat engineers are already contributing to OpenClaw, and we’re expanding that investment with expertise in Linux, Kubernetes, distributed systems, security and enterprise infrastructure.”

Security remains the main area OpenClaw says it’s concentrating its efforts. The project is combining isolation between trusted and untrusted workloads with sandboxing, granular permissions, and LLM-assisted review, and says it plans to publish a reference architecture showing how those pieces fit together in practice.

For now, OCE is still very much a work in progress. The control plane is taking shape, but much remains unfinished, and OpenClaw is still inviting developers, operators, and security teams to help influence what the project becomes before 1.0.

“We are early, and there is much more work ahead,” Lin adds.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)