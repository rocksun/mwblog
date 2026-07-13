Despite significant investments and technological developments in platform engineering over the past decade, most developers still face the same problem they have always faced. They can’t ship without friction.

Enterprises are still using multiple tools across different teams at different stages of the build process. For developers, handling observability, compliance, deployment, and access management requires switching between multiple tools, creating unnecessary barriers and delays in deployment cycles.

In an industry currently dominated by AI technologies and the “all-inclusive platform” solution, Krumware is taking a different approach.

[**Colin Griffin**](https://www.linkedin.com/in/colin-e-griffin/), founder and CEO of [**Krumware**](https://www.krum.io/), is a software engineer with a background in critical infrastructure and real-time systems. As co-organizer of the [CNCF Platform Engineering Technical Community Group](https://community.cncf.io/platform-engineering-technical-community-group/), where he also co-authored the [Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/) and the Cloud Native Maturity Model, he has firsthand experience of the real pain points developers face every day.

> “The walls that a developer has to break down from day to day haven’t really changed. Everything is in multiple places, with no easy way to bring it together.” — Colin Griffin, CEO of Krumware

His experience guides everything Krumware builds, including [Epinio](https://epinio.io/), the open-source application development engine for Kubernetes, and Krumware’s newest capability: the [Epinio MCP](https://docs.epinio.io/getting-started/install-mcp) server, which facilitates standardization and enables compatibility with an enterprise’s existing guardrails. Epinio is not another layer on top, but the harness underneath.

## **Changing the conversation: AI readiness is platform engineering readiness**

For most of the enterprises Krumware serves, friction is not due to a lack of the right tools. More often than not, multiple teams use Kubernetes, but the enterprise as a whole lacks the platform to unlock its full potential. The infrastructure team might know their cluster, and the developers know their code. Still, there is a gap, and organizations are operating without a unified approach to overseeing and regulating Kubernetes use.

Team leaders try to solve the problem by adding more tools to patch the gap, but it is not something that can simply be fixed by more AI software. Teams investing hundreds of thousands of dollars in Backstage instances are often doing so without a clear understanding of how their developers actually use Kubernetes in the first place. In fact, more advanced technologies applied without the right foundations only serve to exacerbate the problem. The acceleration that AI-assisted development delivers can widen the gap between teams that are platform-ready and teams that aren’t.

However, the AI “boom” could also be the financial and organizational lever that shines a light on the real solution for struggling enterprises. In the [Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/), Colin comments that platform engineering and AI are “merging into the same.” The “AI readiness” conversation is familiar to Directors, VPs, and CIOs, who are conscious of their positioning in the market, relative to competitors, and at the forefront of development. The path to AI readiness includes security, observability, networking, interoperable tools, and self-service for workloads, all of which feed into platform engineering.

At its core, “AI readiness” is the same conversation as platform engineering readiness, andin treating platform engineering as the enablement layer for everything that comes next, including the agent layer.

## **“Develop like you deploy”**

Epinio’s core proposition is simple: It doesn’t change how an organization uses Kubernetes. Epinio is providing a highly adaptable interface that empowers engineers to make Kubernetes consumable for developers who don’t need to be Kubernetes experts.

The focus on user experience is why Krumware’s design philosophy differs from that of most tools in this space.

> “You don’t need to know what’s under the hood for how Heroku runs its applications. We are taking that same philosophy and making it compatible with the unique things that the infrastructure team has purposefully built.” —Colin Griffin, CEO of Krumware

In practice, this means a single “Epinio push” command takes the source code from the local file and uses Cloud Buildpacks to automatically detect the language and runtime, build the container image, deploy it into the cluster, and surface a live URL. Epinio runs natively within the Kubernetes cluster, including in local development environments via tools such as Rancher Desktop and minikube. So the build process inherits the same security rules, compliance constraints, and networking configuration that govern production.

Epinio dramatically increases developer velocity by removing bottlenecks in the test-iterate cycle and truly unlocks rapid prototyping. The outcome is better testing and more efficient deployment cycles: failures happen earlier, in the right context, caught by the right guardrails, rather than surfacing as production surprises.

Epinio is not just for traditional development; with the explosion of vibe coding and its adoption by employees of all kinds, Epinio is increasingly being used by organizations that want to implement Golden Paths and enforce standardization across the company.

![Diagram contrasting a slow 'Traditional' Code-Build-Deploy-Run workflow full of wait steps and feedback loops with the streamlined 'Epinio Fast Lane' that runs straight from code to run.](https://cdn.thenewstack.io/media/2026/07/4e67fa32-unnamed-1024x561.png)

Krumware calls this a “develop like you deploy” method. There is a consistent environment wherever Kubernetes runs, eliminating the barriers previously encountered when a local dev machine uses a different Kubernetes configuration than the remote cluster. The security and compliance controls previously available only in the Kubernetes setup are now available on local machines. Epinio isn’t an [Internal Developer Platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/ "Internal Developer Platform") (IDP), but it could be for users who want to build that functionality.

Once that environment is established, it becomes a central template fitted to the organization’s policies and ensures standardization across the enterprise. Krumware delivers these templates as customizable artifacts tailored to each team’s setup, enabling engineers to build and deploy within a consistent, governed framework.

When teams onboard with Epinio, the “aha” moment hits when that first app goes from zero to live in under a minute. Teams suddenly have much faster cycles, and at that point, they can start adding additional features and creating catalogs for some control.

## **Access and operability with ease**

For enterprises with a Cloud Foundry heritage, the experience will feel familiar. Originally developed by SUSE, Epinio was inspired by Cloud Foundry’s simplicity and was designed to hide the complexity of Kubernetes, just as Cloud Foundry did for legacy infrastructure. While Cloud Foundry paved the way in the market with developer simplicity and buildpack-based deployments, Krumware continues that philosophy on modern infrastructure with Epinio.

Krumware assumed stewardship of Epinio as its official open-source maintainer from [SUSE](https://www.suse.com/) in 2024 and spent the following year updating some components to steer the project towards a new level of capabilities. One of the fundamental aspects of Epinio is its interoperability with other platforms, beginning with [Rancher](https://www.krum.io/products/rancher-accelerate), the enterprise Kubernetes management platform. Epinio continues to be available as an extension for [Rancher](https://www.krum.io/products/rancher-accelerate), making it accessible directly within the infrastructure tooling many enterprises already use, and future releases will extend its interoperability to other enterprise platforms as well.

Over the past few releases, Epinio has introduced several major improvements, including a new permission system and an upgraded file storage system powered by SeaweedFS. The latest release, Epinio 1.14, builds on this momentum with a redesigned application creation flow and a full UI refresh, including elements of Trailhand, Krumware’s incoming platform component system focused on UI interoperability.

## **The agent harness for Kubernetes**

Krumware’s [Epinio MCP](https://docs.epinio.io/getting-started/install-mcp) server provides a different solution from other MCP offerings. The MCP (Model Context Protocol) is the emerging standard by which AI agents and LLMs interact with external tools and data sources. A Kubernetes MCP server already exists and gives an LLM raw access to a cluster, but without context. The model expends a large number of tokens to determine which data sources are available, which services it can use, and which types of applications are appropriate for this environment. Without sufficient input, it will deploy whatever seems most suitable.

The Epinio MCP server solves this by giving the LLM a structured, pre-scoped context from the application-layer view that Epinio already manages. It surfaces the approved buildpacks, templates, service catalog, and namespace constraints, and adopts the user’s credentials so that the agent operates within the same access boundaries as the developer. The Epinio MCP provides the guardrails for building and a harness for enhanced deployment.The human remains the director; the agent operates within a defined, sanctioned space.

By design, the Epinio MCP server is LLM-agnostic. It works with any model that supports the MCP standard, whether cloud-hosted or on-premises. While Epinio will undoubtedly improve developer iteration cycles, fast-track onboarding, and improve standardization and compliance, the deeper purpose of the harness is about developer freedom.

“If we can help the developer understand the who, what, where, why, and how of the apps, we start to get closer and closer to letting them just think about their ideas. It frees up cognitive load to be creative, to think and design new solutions, to build better outcomes.” —Colin Griffin, CEO of Krumware

With the Epinio MCP in place, engineers can adapt Epinio into whatever they need it to be. Why not use the platform to build itself? Applications can become aware of their own deployment environment, and teams can build custom MCP servers for specific databases, binding contextual data sources directly into the development loop. The closed environment becomes a surface for creation.

## **Shaping the industry**

Beyond 1.14, upcoming releases will introduce Trailhand, an open-source platform engineering component system with framework-agnostic components that allow Epinio’s context to be injected into other tools, not just consumed through Epinio’s own interface. A new pack-based buildpack lifecycle will also be introduced, opening the door to non-Paketo buildpacks.

The roadmap reflects the same interoperability philosophy that underpins everything Krumware builds: Every IT ecosystem is different, and platform teams need a value delivery pipeline that runs from the ground all the way out to the customer.

Krumware is not asking teams to overhaul how they work. It is providing the harness to do their best work inside the Kubernetes environment the organization has already invested in and, from there, the surface to build whatever comes next.

For Krumware, Epinio is becoming a design standard for platform interoperability, not merely an application deployment tool, but the connective layer that makes everything else work better together.

**💬** [**Talk to the Krumware team about Epinio for your organization**](http://www.krum.io/contact)**.**

---

*Krumware is a cloud-native software engineering firm specializing in platform engineering, custom software development, and open-source tooling. Krumware is the official maintainer of the Epinio open-source project and a Diamond SUSE Partner.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/07/e64dbb75-cropped-44ca2ae0-headshot-katie-tincello-600x600.png)

Katie Tincello is a technology journalist covering platform engineering, cloud infrastructure, and AI for The New Stack, with a specialty in founder interviews and executive thought leadership. She joined TNS in March 2026 as a contributing writer after eight years...

Read more from Katie Tincello](https://thenewstack.io/author/katie-tincello/)