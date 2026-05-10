In 2011, Marc Andreessen famously observed that [software was eating the world](https://a16z.com/why-software-is-eating-the-world/), anticipating that every industry would be reshaped or displaced by software-driven competitors. This framing accelerated an era of platform reinvention.

Six years later, Nvidia’s Jensen Huang extended the metaphor, predicting that AI models would replace code written by humans: “[software is eating the world, but AI is going to eat software](https://www.technologyreview.com/2017/05/12/151722/nvidia-ceo-software-is-eating-the-world-but-ai-is-going-to-eat-software).”

Nearly a decade on, that prediction is taking shape with palpable urgency, and the new demands are amplifying the limitations of the infrastructure choices many enterprises made the first time around.

> “When AI is reshaping your industry on a timeline measured in quarters, is now the moment to build your own platform?”

Here is the question worth sitting with: When AI is reshaping your industry on a timeline measured in quarters, is now the moment to build your own platform?

## Shorter runway, higher stakes

The last round of digital transformation gave enterprises roughly a decade to figure out how to ship software faster. Companies that got it wrong eventually got acquired, disrupted, or diminished — but “eventually” was often long enough to course-correct. AI is not offering the same runway. The pace of model improvement, the breadth of use cases, and the competitive gap between AI-enabled and AI-absent companies are all widening faster than most enterprise IT cycles can absorb.

At the same time, the stakes of getting it wrong are higher. An AI deployment isn’t just another app to run. It is a potential vector for prompt injection, PII leakage, unauthorized model access, shadow spend, regulatory exposure, and reputational damage at a scale previous generations of enterprise software didn’t produce. The organizations moving fastest on AI are also the ones thinking hardest about governance — because the two are not in tension, they are the same problem.

Every enterprise now has three things it needs to do roughly at once:

* **Give AI to every employee**, as basic enablement — the way computers and internet access became standard issue.
* **Put AI into external products** to improve the value delivered to customers.
* **Embed AI into internal processes** to change how the company operates, not just what it produces.

And it needs to do all three with governance, [observability](https://thenewstack.io/observability-every-engineers-job-not-just-ops-problem/), and security guarantees that would make a compliance officer comfortable signing off.

That is the challenge. The biggest hurdle is determining which platform lies beneath all three.

## A familiar pattern

For anyone who has watched the enterprise platform market since 2011, the shape of this decision will feel familiar — because we’ve been here before.

Cloud Foundry was conceived at VMware in 2009 and announced publicly as an open source PaaS in 2011. It has been shipping commercially in production at enterprise scale under three successive names — Pivotal Cloud Foundry, then VMware Tanzu Application Service, and now VMware Tanzu Platform — for roughly fifteen years.

In that time, it quietly accumulated an integrated set of capabilities that remain hard to find assembled anywhere else:

* Container-based runtime isolation (predating Docker by two years)
* A simple `cf push` code deployment experience
* An application-focused web UI that makes the platform immediately usable
* A build system that produces hardened runtime images without developers writing [Dockerfiles](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/ "Dockerfiles")
* A self-service service marketplace with automatic credential injection and rotation
* TLS termination and routing
* Multi-tenant orgs and spaces
* Targeting of workloads to specific CPU pools
* GPU-backed services
* Auto-healing
* Automated VM repaving for CVE response
* Zero-downtime upgrades of the platform itself

And critically, it ran the same way on-premises as it did in any public cloud — a multi-cloud and hybrid-cloud posture that most platforms took another decade to match. A small operations team could offer a polished developer experience and manage thousands of enterprise applications, whether deployed on-premises or across multiple clouds.

Running in parallel, starting a few years later, was the Kubernetes movement. Kubernetes took a deliberately different philosophy: rather than offering an integrated platform, it provided primitives from which a platform could be composed. This was a reasonable bet. It fostered an enormous ecosystem, and for organizations with specific needs and the engineering capacity to meet them, it offered flexibility that Cloud Foundry’s more opinionated model did not.

But composition has a cost, and the cost compounds. Building your own developer platform means assembling — and continuously maintaining — a stack of workload scheduling, ingress, service mesh, multi-tenancy, IAM, secrets management, service catalog, policy enforcement, observability, and a developer-facing UI  — each piece with its own lifecycle, its own CVEs, its own vendor, and its own upgrade cadence. The platform team grows. The integration surface grows faster.

There were legitimate reasons to take this path. Flexibility matters; avoiding [vendor lock-in](https://thenewstack.io/want-to-escape-vmware-exit-with-platform-engineering/) matters; tailoring to specific workloads matters. And in nascent markets, building in-house genuinely is the right call, which is part of why platforms were built in-house in the early 2000s, before Cloud Foundry existed.

But by the mid-2010s, the economics had shifted, and yet the industry leaned into a DIY instinct anyway. It is worth asking why, and there is no single answer: ownership feels safer than dependency; building feels more strategic than buying; platform teams accrue importance proportional to the surface area they manage; and the costs of assembly accumulate slowly enough to be mistaken for normal operating expense.

The enterprise equivalent is the company that decided, in 2010, to build its own CRM rather than adopt Salesforce. The reasoning at the time was often sound: flexibility, control, and avoiding dependence on a vendor. The outcome, a decade later, was a system that did 70% of what Salesforce did, cost more, and absorbed engineering cycles that would have been better spent on the actual business. These decisions are understandable in the moment and obvious in retrospect.

## A proven foundation, now for AI

Here is where the story turns, because the lesson of the last decade is not Cloud Foundry’s vindication. It is more useful than that: **the integration work that made Cloud Foundry hard to emulate via DIY is precisely what makes Tanzu Platform well-positioned for AI today.**

The capabilities an enterprise needs to deploy AI responsibly are not fundamentally new. They are the capabilities any mature application platform needs, applied to a new class of workload:

* A **governance surface** where platform engineers — not individual developers — decide which models are approved for shared use.
* A **service marketplace** so developers can bind to approved AI models, MCP servers, and vector stores, the same way they bind to any data service.
* A **credential mechanism** that injects model API keys at runtime and rotates them without code changes.
* An **abstraction layer** that hides the differences between private-hosted AI models and major cloud providers, so developers don’t hard-code vendor choices.
* **Observability and audit logging** on every model and [MCP server](https://thenewstack.io/build-mcp-server-tutorial/) interaction, because you cannot govern what you cannot see.
* **Rate limiting and middleware** to control spend and enforce usage policy.
* A **gateway** to route AI traffic to internal or external models and keep sensitive information inside the enterprise boundary.
* **Deployment flexibility** — on-premises in a private cloud, or across public clouds — to keep AI-related applications, services, and data where compliance requires, and move between environments without redesign.

These foundational capabilities give shape to Tanzu Platform’s AI story today. Three releases in particular mark inflection points: Tanzu Platform 10.0, which added an AI service offering to the Marketplace; 10.3, which facilitated sharing of MCP servers; and 10.4, which introduced agent foundations.

[**10.0 — AI Services**](https://blogs.vmware.com/tanzu/broadcom-announces-the-general-availability-of-vmware-tanzu-platform-10-making-it-easier-for-customers-to-build-and-launch-new-applications-in-the-private-cloud/). **AI Services** (launched as the GenAI tile and later renamed) exposes approved models through the Marketplace, so developers use the same `cf create-service` and `cf bind-service` flows they already know. The AI Server provides middleware for rate limiting, observability, and audit logging, and integrates with third-party tools to meet additional needs, such as PII filtering. Models can be hosted privately within the foundation — on CPU- or GPU-backed infrastructure — or accessed through cloud providers, all behind a consistent OpenAI-compatible API so applications don’t have to be refactored to switch between them. Platform engineers curate what appears in the Marketplace; developers get self-service access to what’s been approved.

[**10.3 — Shared MCP Servers**](https://blogs.vmware.com/tanzu/tanzu-platform-10-3-delivers-the-ai-native-engine-for-developer-velocity-and-platform-control/). A new **service publishing** facility automates the process for a developer to turn any application — including MCP servers — into a service offering, with service instance lifecycle capabilities and a gateway that protects the backing application behind an internal route. Platform operators retain the ability to approve and expose any new service offerings through the Marketplace.

[**10.4 — Agent Foundations**](https://blogs.vmware.com/tanzu/introducing-tanzu-platform-10-4/). Agent foundations bundle capabilities from earlier releases with three new contributions to support agentic applications. The **Agent Buildpack** (in technical preview) opens agent-authoring to non-developers, turning agent and skill descriptions (written in natural language) into a running agent, with optional bindings to models, tools, and other platform services. The **MCP Gateway** service lets developers bind MCP servers to gateway instances to give agents central points of discovery and access; the gateways protect on-platform MCP servers with internal routes, and attach a verifiable OIDC identity to on- and off-platform MCP servers so that autonomous actions are auditable back to the end user who initiated them. Finally, enhanced **observability dashboards** track agent tool calls and model consumption by gateway, model, application, space, or org, with showback for cost attribution.

The gap to bridge — from a mature Tanzu Platform deployment to production AI applications — is genuinely small, because the platform already did the hard parts years ago. The same cannot be said of a DIY platform now being asked to add an AI layer on top of a stack that is still being stabilized beneath.

## Now is not the time to build your own platform

Enterprises have a narrow window to make AI a practical capability across their organizations, and the penalty for wasting that window on platform reconstruction is higher than ever. The platforms that will enable this transition are the ones that already did the hard, boring, unglamorous integration work — cohesive developer experience, governed service access, observability by default, zero-downtime operations, security at every layer — before AI made those capabilities table stakes.

Tanzu Platform did that work. For fifteen years. The distance between “we should prototype something with an LLM” and “we have it running in production behind appropriate governance” is shorter on a platform where the governance, the observability, and the self-service developer experience are properties of the system rather than things you still need to build.

> “The argument for using Tanzu Platform now is not that it was always right. The argument is that the moment the market is finally in matches the moment the platform has been ready for.”

The argument for using Tanzu Platform now is not that it was always right. The argument is that the moment the market is finally in matches the moment the platform has been ready for.

### Additional resources

* “[Why your DIY Kubernetes stack won’t survive the era of agentic AI](https://blogs.vmware.com/tanzu/why-your-diy-kubernetes-stack-wont-survive-the-era-of-agentic-ai/),” Oren Penso, *The New Stack*, March 2026.
* “[Building an Enterprise MCP Server Marketplace with Tanzu Platform](https://blogs.vmware.com/tanzu/building-an-enterprise-mcp-server-marketplace-with-tanzu-platform/),” Corby Page and Brian Kirkland, Tanzu blog, January 23, 2026.
* “[Enterprise-Ready Agents Made Simple & Safe with VMware Tanzu Platform AgentFoundations](https://blogs.vmware.com/tanzu/enterprise-ready-agents-made-simple-with-vmware-tanzu-platform-10-4/),” Camille Crowell-Lee, Tanzu blog, April 15, 2026.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/05/fda41a46-cora-iberkleid.jpg)

Cora Iberkleid is a Developer Advocate for the Tanzu Division at Broadcom, helping developers and enterprises navigate modern practices and technologies, focusing on cloud native architecture, modern CI/CD, Spring, and Kubernetes. Prior to joining VMware, Cora was an Advisory Solutions...

Read more from Cora Iberkleid](https://thenewstack.io/author/cora-iberkleid/)