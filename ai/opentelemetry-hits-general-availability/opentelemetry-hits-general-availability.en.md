The Cloud Native Computing Foundation ([CNCF](https://www.cncf.io/)) on Thursday announced the graduation of [OpenTelemetry](https://opentelemetry.io/), the [open source observability framework](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) that has become one of the most widely adopted pieces of infrastructure in cloud-native computing.

The milestone marks the culmination of a seven-year rise for a project that [began in 2019](https://opensource.microsoft.com/blog/2019/05/23/announcing-opentelemetry-cncf-merged-opencensus-opentracing/) as the merger of two competing observability efforts: [OpenTracing](https://opentracing.io/), a CNCF-backed distributed tracing standard, and [OpenCensus](https://opencensus.io/), a telemetry project originally launched by Google and backed by companies including Microsoft.

Today, OpenTelemetry is widely used to collect and export telemetry data — traces, metrics, and logs — across distributed software systems. Graduation represents the CNCF’s highest maturity level for open-source projects, signalling governance stability, production adoption, and long-term sustainability. The foundation said OpenTelemetry is now among the “highest-velocity” projects in the CNCF ecosystem, second only to Kubernetes, with over 12,000 contributors and participation from more than 2,000 companies.

For many developers and infrastructure teams, OpenTelemetry has functioned as foundational infrastructure for years already, making its formal graduation feel somewhat overdue. [Chris Aniszczyk](https://www.linkedin.com/in/caniszczyk/), CTO at the CNCF, tells *The New Stack* that the foundation’s graduation process is intentionally designed to move slowly for projects expected to become long-term industry standards.

> “The goal of graduation is to provide enterprises with the certainty that they are building on a neutral and solid backbone.”

“Our graduation process isn’t meant to be fast; it usually takes a multi-year effort of building stability, security, and resilient governance to ensure long-term, sustainable innovation for the entire industry,” Aniszczyk says. “For a project as critical as OpenTelemetry, we need to confirm it is a permanent, vendor-neutral component of the modern stack and not reliant on any single commercial interest. The goal of graduation is to provide enterprises with the certainty that they are building on a neutral and solid backbone.”

## Becoming common infrastructure

Modern software systems are generating more telemetry than many organizations can realistically manage. As cloud environments sprawl across public infrastructure, private data centers, Kubernetes clusters, and — increasingly — AI-generated services, observability teams are grappling with rising complexity and [mounting data costs](https://thenewstack.io/why-observability-bills-grow/). OpenTelemetry’s vendor-neutral positioning helped drive broad industry adoption — major cloud providers and observability vendors including Microsoft Azure, AWS, Google Cloud, Datadog, Grafana Labs, Splunk, and New Relic now support it in various forms.

Historically, those vendors often relied on proprietary agents, SDKs, and telemetry pipelines that made it difficult for organizations to move between platforms. OpenTelemetry helped standardize instrumentation across programming languages and infrastructure environments, allowing telemetry data to flow more easily between monitoring and analytics systems.

Aniszczyk suggests the 2019 merger between OpenTracing and OpenCensus helped prevent fragmentation across the observability market, while also changing how vendors compete commercially by weakening proprietary telemetry lock-in.

> “Before OpenTelemetry, vendors competed on proprietary agents/collectors and data formats, which often led to customer lock-in.”

“Before OpenTelemetry, vendors competed on proprietary agents/collectors and data formats, which often led to customer lock-in,” he says. “Today, the competition is fierce on the next layer: developer and user experience on top of delivering high signal insights, superior AI-driven analysis and cost effective solutions.”

Speaking to *The New Stack* in early 2026, [Tom Wilkie](https://uk.linkedin.com/in/tomwilkie), CTO at Grafana Labs, also [argued that](https://thenewstack.io/can-opentelemetry-save-observability-in-2026/) OpenTelemetry had helped erode traditional observability lock-in by standardizing instrumentation across platforms.

“Teams no longer have to piece together vendor-specific SDKs, and new observability players can enter the market more easily because instrumentation is no longer the moat,” Wilkie said.

Yet OpenTelemetry’s rapid growth has also introduced operational headaches for some adopters. In a [2025 proposal](https://opentelemetry.io/blog/2025/stability-proposal-announcement/) outlining future stabilization efforts, the project’s Governance Committee acknowledged that OpenTelemetry’s “complexity and lack of stability” had created “impediments to production deployments,” citing issues including breaking configuration changes, performance regressions at large deployments, and the difficulty of coordinating upgrades across hundreds or thousands of services.

In an interview with *The New Stack* in December 2025, [Ari Zilka](https://www.linkedin.com/in/arizilka/), founder of observability startup MyDecisive.ai, [said some enterprises](https://thenewstack.io/from-group-science-project-to-enterprise-service-rethinking-opentelemetry/) had effectively turned OpenTelemetry into “a team sport,” with large organizations dedicating entire internal teams to managing telemetry infrastructure and collector deployments.

Those concerns reflect broader frustrations that have lingered across the observability market for years. Organizations operating large distributed systems often collect enormous quantities of logs, traces, and metrics, generating hefty monitoring bills in the process.

OpenTelemetry doesn’t solve observability economics on its own, of course, but its standardization efforts have helped lower barriers for [newer observability vendors](https://thenewstack.io/opentelemetry-opens-the-door-for-observability-startups/) attempting to compete with established platforms.

## Infrastructure pressure

The project’s graduation arrives as AI-generated software and autonomous infrastructure systems begin placing additional pressure on observability tooling. AI coding systems can generate services, deployments, API calls, and infrastructure changes far faster than traditional software development cycles.  
Aniszczyk says that the rise of AI agents and autonomous systems is placing new demands on modern infrastructure, with telemetry becoming a central mechanism for monitoring and coordinating those systems.

> “The shift to AI agents and autonomous systems is the single most important evolutionary pressure on infrastructure today.”

“The shift to AI agents and autonomous systems is the single most important evolutionary pressure on infrastructure today,” he says. “We view OpenTelemetry as moving beyond a traditional observability framework — it’s now becoming foundational for AI workloads and models. This means scaling to entirely new orders of magnitude, where telemetry is the constant sensory input for AI agents.”

The CNCF says growing AI workloads are helping drive increased OpenTelemetry adoption across the ecosystem. According to [npm download data](https://npmx.dev/package/@opentelemetry/api), the project’s JavaScript API package grew from roughly 75 million monthly downloads in April 2025 to more than 200 million monthly downloads by April 2026, marking a record month. The project’s [Python API package](https://pypistats.org/packages/opentelemetry-api) also hit record download levels over the same period.

[Juraci Paixão Kröhling](https://www.linkedin.com/in/jpkroehling/), co-founder at observability startup [OllyGarden](https://ollygarden.com/), says many organizations are discovering that AI systems introduce the same operational and reliability problems long associated with distributed cloud infrastructure.

“As organizations rush to put AI workloads into production, they are discovering that GenAI systems are distributed systems, with all the latency, reliability and cost questions that come with them,” Kröhling said in a statement. “OpenTelemetry gives those teams a common language to instrument agents, models and the services around them without locking into any single vendor.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)