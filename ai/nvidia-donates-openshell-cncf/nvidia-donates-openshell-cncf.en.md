![](https://cdn.thenewstack.io/media/2026/07/45a2a83b-img_0484-1024x768.jpg)

**Nvidia this week donated OpenShell**, its open-source runtime for securing and governing AI agents, to the Cloud Native Computing Foundation. The teams that run it in production already work with Kubernetes and the CNCF’s other projects, says Ali Golshan, Nvidia’s senior director of AI software, who leads the project.

The company [announced](https://blogs.nvidia.com/blog/open-source-openshell-infrastructure/) the move on Tuesday at KubeCon + CloudNativeCon North America in Salt Lake City. [OpenShell](https://github.com/ai-openshell), which Nvidia launched at its GTC conference in March, [joins the CNCF](https://www.cncf.io/blog/2026/11/10/welcoming-openshell-to-the-cncf-open-governance-to-secure-agentic-ai/) as a Sandbox project, the foundation’s entry-level tier for early-stage projects. The CNCF formally accepted the project in late September.

The CNCF currently hosts 262 projects, including 155 at the Sandbox level, but it wasn’t the only possible home for OpenShell. The CNCF’s parent organization, the Linux Foundation, also runs the Agentic AI Foundation (AAIF), which hosts agentgateway, the Model Context Protocol (MCP) and Agent2Agent (A2A) protocol. Last month, the AAIF also [took in OpenSandbox](https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox), a sandbox platform for AI agents that Alibaba contributed.

> “Securing and creating trust around AI is really infrastructure. That’s really where you need to start.”

But as [Golshan](https://www.linkedin.com/in/ali-golshan) tells *The New Stack*, “Securing and creating trust around AI is really infrastructure. That’s really where you need to start.” That, he says, is what made the CNCF the logical place for the project to land.

## The platform team is the user

OpenShell runs an agent inside a sandbox and enforces policies on which files, networks, credentials, and model endpoints that agent can reach. That enforcement happens in the infrastructure around the agent, [according to the CNCF](https://www.cncf.io/announcements/2026/11/10/cncf-hits-major-milestones-with-global-community-growth-record-industry-investment-and-a-new-generation-of-projects-to-build-ai-systems-in-production/), and the project is adopting [Cedar](https://cedarpolicy.com/en), another CNCF project, as its policy language.

Golshan says that securing agents takes a full stack solution and that Nvidia couldn’t build that stack one piece at a time.

“We can’t go build OpenShell and then go build the next pieces of it,” he says. “And a lot of those pieces, from an infrastructure standpoint, already existed in CNCF.” He cites Kubernetes itself, as well as the lightweight K3s distribution and service meshes, as examples of adjacent projects.

While building OpenShell, it also became clearer who would operate it, Golshan says. The profile matched the DevSecOps engineer who already stands up the rest of a company’s infrastructure.

He points to [SAP](https://news.sap.com/2026/09/sap-nvidia-openshell-auditable-ai-agents-enterprise-systems/) as a company where DevOps and infrastructure teams stand up large agent environments.

The people who work with the agents may be engineers or researchers, he says, but the operators are “the same teams that are spinning up Kube and Linux and that whole stack.”

Ideally, those end users never see OpenShell. “You don’t really see Kubernetes,” Golshan says. “You just get that environment.”

When [Jonathan Bryce](https://www.linkedin.com/in/jbryce/), the CNCF’s executive director, thinks about where a technology should live, he tells *The New Stack*, the question to ask is “where are the people who are going to be making the decision about deploying, using, contributing to a specific technology?”

Agents started with people running OpenClaw on Mac Minis at home, Bryce says, but long-running, SaaS-style agents look more like other software run in a data center. Before OpenShell joined the CNCF, he adds, much of its early uptake came from neoclouds, GPU cloud providers that want to govern the workloads their customers run on their infrastructure.

Since OpenShell plugs into Kubernetes and other ecosystem projects, Bryce says, teams that already run that stack can easily add it to the workloads they want to contain.

## Where agent projects live

Agents will exist throughout the entire stack, Bryce says, and the open-source projects that support them will spread across several foundations, each with a different kind of contributor.

The [PyTorch Foundation](https://pytorch.org/foundation/), home to PyTorch, vLLM, DeepSpeed, and Ray, is where the engineers with deep AI expertise work. Bryce likens them to “the people who write Postgres.”

The CNCF, he says, is “the very broad set of folks who understand how to take mature systems and deploy, scale, observe, secure them.”

The AAIF, with protocols like MCP and A2A, is oriented toward the front-end experience of agents, Bryce says. He compares those protocols to HTTP and JavaScript, the standards that made millions of web apps possible.

The foundations are “Venn diagrams” and not silos, Bryce says, “and I think that’s good.” He points to KubeRay, which runs Ray workloads on Kubernetes, and to llm-d, which pairs vLLM with Kubernetes. The AAIF’s agentgateway works with Kubernetes, too.

The CNCF also tends to be flexible about where a project lands and lets maintainers “choose their own adventure to some extent,” he notes.

Meanwhile, Bryce says Nvidia’s visibility into how people run AI workloads is “unparalleled,” and the company brings new projects built on that experience to each KubeCon. “Some of those end up in a foundation,” he says. “Some of them don’t.”

## Governance and a security committee

Golshan joined Nvidia in 2025, when the company acquired Gretel, the synthetic data startup he co-founded. Before that, he also co-founded StackRox, the Kubernetes security company Red Hat [acquired](https://thenewstack.io/what-red-hats-purchase-of-stackrox-means-for-openshift-security-and-observability/) in 2021.

He says the people who started OpenShell had been contributors to CNCF projects and knew its governance model from the inside.

That model fit what the team wanted, he says: a single mission for OpenShell and a place within a larger ecosystem.

Security governance, he says, is still being worked out. OpenShell is a Sandbox project for now, and Golshan says the team is “spending a bunch of time thinking through” how to put an independent security committee around it.

“One of the things that I think becomes very important is how do you manage things like disclosures, vulnerabilities,” he says. If OpenShell is going to become a critical piece of infrastructure, he adds, it needs contributions from many participants, “not necessarily us.”

Nvidia’s engineers will keep working on the project’s core, but Red Hat, Docker, and Canonical have been core contributors alongside Nvidia since the start.

When Nvidia opened OpenShell for early access in March, roughly 10 to 15 companies were contributing, Golshan says. The project dropped its alpha label with the 0.1.0 release in September, and the [CNCF’s project page](https://www.cncf.io/projects/openshell/) now lists about 380 contributing organizations.

“There are a lot of people who will engage at a certain level without it being in neutral governance,” Bryce says. “But once it makes that move to fully neutral governance, then that engagement gets a lot deeper.”

Adoption cycles that used to take two or three years now play out in six to 12 months, Bryce says, and he describes neutral governance as “rocket fuel” for integration and adoption.

“llm-d came into CNCF in March of this year, and they now have their 1.0 release,” Bryce says of the distributed inference framework, “and they have a whole set of companies that are actually running it in production, including some of the neoclouds.”

Golshan says OpenShell needs an ecosystem of tools around it before it can run at scale in production. About 50 to 60 companies, from startups to large vendors, have built on it so far, he says. OpenShell now has defined extension points for compute, credential management, inference providers, and policy enforcement, and he hopes the CNCF community will use them as a blueprint for tying OpenShell into the rest of the cloud native stack.

“It would be amazing if within the next six months we could support everything from Istio to Envoy to K3s for edge,” Golshan says.

Since the 0.1.0 release, early adopters that are moving agents from research into production have asked for recommendations on security, privacy, and observability tooling that works natively with OpenShell, he says. They also want help optimizing the agents and harnesses that run inside it.

Golshan describes a recent conversation in Berlin with someone who already knew Datadog and distributed tracing well. “I don’t even know what to observe for an agent,” he recalls the person saying.

Golshan wants what the community learns from those edge cases to flow back into the OpenShell core, the way it did for Kubernetes. “It’s pretty easy these days to say I’m going to bet my company on Kube,” he says. “Nobody’s going to get fired for that.” He hopes OpenShell will get there too.

## An unsettled agent stack

The stack for training models is clear, and the one for inference is pretty settled, Bryce says, but for agents it’s “not at all.”

“If there’s not a clear stack, then the industry can’t come together on the most significant problems and actually make really fast, rapid progress,” he says.

Over the next six to 12 months, he expects experimentation to settle into answers on how OpenShell integrates with Kata Containers, gVisor, Agent Substrate, and existing OpenTelemetry projects. Once that happens, he expects agents to take off the way inference has over the last eight months.

Two of those projects are new to the CNCF. Google [contributed](https://opensource.googleblog.com/2026/11/sandboxing-untrusted-ai-agents-at-scale.html) Agent Substrate, its framework for running long-lived agents on Kubernetes, and the gVisor sandbox runtime at this week’s KubeCon. Nvidia says it’s working with Google on an integration between OpenShell and Agent Substrate.

The post [Why Nvidia gave OpenShell to the CNCF](https://thenewstack.io/nvidia-donates-openshell-cncf/) appeared first on [The New Stack](https://thenewstack.io).