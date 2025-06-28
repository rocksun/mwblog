SEATTLE — [Observability](https://thenewstack.io/observability/) continues to see a trend of a number of new players entering the market, while in-use adopters — particularly among large organizations — are simultaneously decreasing the number of tool providers they rely on for observability. [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry/) has facilitated this trend to some extent, thanks to its instrumentation and standardization of [logs, metrics, traces](https://thenewstack.io/observability-2-0-or-just-logs-all-over-again/) and other [telemetry data](https://thenewstack.io/from-chaos-to-clarity-master-the-first-mile-of-observability/).

But as [Grafana CTO Tom Wilkie](https://uk.linkedin.com/in/tomwilkie) noted when I spoke with him at [GrafanaCON,](https://grafana.com/events/grafanacon/) [Grafana Labs](https://thenewstack.io/grafanas-ebpf-beyla-future-hinges-on-opentelemetry/)’ annual user’s conference here recently, this is a symptom rather than a trend, as players and organizations seek to refine the data they need, especially for cost control and the growing number of business use cases. Wilkie also explained how this shift is pushing open source to expand its reach, as cost-cutting organizations increasingly turn to it. Organizations are seeking the technologies they need while remaining cost-conscious and particularly eager to avoid vendor lock-in, which open source can, at least in theory, help to mitigate.

That said, as more new players enter the market, they are competing more on technology than on purely cost-cutting proposals. The aim is to expand the range of business use cases that observability supports. Observability is expanding dynamically, broadening how organizations can leverage it for a variety of reasons — from providing engineers with better insights into product usage, software performance, and maintainability, to meeting the needs of less technical stakeholders like [SREs](https://thenewstack.io/interrogate-your-software-with-ai-the-future-for-sres/), CTOs, product managers, and others who want a more simplified view of telemetry data.

It can also be argued that this evolution will continue to push observability into new and interesting directions. We may only be seeing a fraction of observability, of its potential use. A significant expansion of observability practices and processes appears to be on the horizon. At the risk of adding the perfunctory mention of AI, observability will serve as a major aspect of managing [LLMs](https://thenewstack.io/llm/), [MCP agents](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) and anything else that overlaps with the use of AI.

## Rush to Less Gold

Observability continues to attract new players to the market, while organizations — especially larger ones — are simultaneously reducing the number of observability tools they rely on. OpenTelemetry has helped facilitate this shift by standardizing instrumentation for logs, metrics, traces, and other telemetry data.

According to Wilkie, this is less of a trend and more of a symptom. Organizations are refining the data they collect to manage costs and support a growing number of business use cases. “Open source is increasingly attractive in this environment, as companies seek to avoid vendor lock-in and reduce spending. New players aren’t just competing on cost — they’re competing on technology,” he said. “The goal is to support a broader range of business use cases. Observability has expanded beyond developers and engineers to stakeholders like SREs, CTOs, and product managers, who want a more streamlined view of telemetry data.”

The very semantics of observability are at issue. “What does ‘observability’ even mean to different people? The market is beginning to coalesce around a product-centric definition, positioning observability as a superset of traditional monitoring and [APM](https://thenewstack.io/the-impact-of-containerization-on-apm-strategies/),” Wilkie said. “This includes areas like RUM (real user monitoring) and DEM (digital experience monitoring), which are starting to blur together semantically.”

From a market dynamics perspective, with the end of zero-interest capital, the consolidation of the observability tools that organizations purchase is occurring.

“Previously, budgets were easier to secure if there was a perceived business benefit. That’s no longer the case,” Wilkie said. “Businesses are unwilling to continually increase observability spending. Instead, they’re consolidating vendors to gain more purchasing power and grow without increasing costs.”

This trend is particularly noticeable among large enterprises, such as major banks that previously “had every observability tool under the sun. Their mission over the past two to three years has been to reduce that to two or three tools. Larger deals with fewer vendors give them leverage and efficiency,” Wilkie said.

## The Open Source Surge

Open source is having a tremendous impact on observability and is disrupting it what I would argue is a good way. As Wilkie noted, operating systems and databases were the “early battlegrounds,” and now observability is following suit. “For many years, the largest observability vendors remained proprietary,” Wilkie said. “But open source alternatives — like Prometheus and Loki — have commoditized telemetry signals and made them more affordable and scalable.”

OpenTelemetry is the most recent extension of this trend, Wilkie said. ”While OpenTelemetry reduces vendor lock-in on paper, many still find themselves tied to specific tools due to the complexity of query languages and value-added features,” Wilkie said. “Instrumentation may be standardized, but meaningful insight still depends heavily on a given vendor’s implementation.”

Continued cost management and open source disruption are the defining features of the current landscape. “Proprietary vendors are under pressure,” Wilkie said. ”Some of them are beginning to introduce adaptive telemetry strategies — an area Grafana has been investing in—that aim to reduce cost and data volume intelligently.”

However, incumbents have little incentive to slash customer bills, Wilkie said. “Imagine if a company like Splunk or Dynatrace released a feature that halved usage costs — what would happen to their stock price?” Wilkie said. “These vendors tend to hedge rather than innovate in ways that threaten their revenue models.”

However, observability isn’t just about cost savings. “While some use cases involve optimization and efficiency, others are about improving the developer experience, diagnosing production issues, or learning how new features perform in the wild,” Wilkie said. “Observability is fundamentally about understanding systems better.”

Another important market feature is the low switching cost. “Observability doesn’t have a network effect like social media platforms. You only need a few hours of data to derive 80-90% of its value,” Wilkie said. “That makes it relatively easy to change vendors compared to infrastructure staples like operating systems or [ERP software](https://thenewstack.io/sap-simplifies-erp-data-access-for-developers/).”

This is all good for organizations that rely on observability to sustain not only operations but increasingly, their business model. “This competitive pressure benefits consumers. Vendors must keep innovating or risk losing business,” Wilkie said. “Despite buyer-side consolidation, vendor-side consolidation is minimal. There’s a large number of sizable players, but none dominate the market.”

## The Three-Pillar Crumble

Technologically, observability is moving away from the “three pillars” (metrics, logs, and traces). While those signals are still useful, defining observability by them has become limiting. Vendors now twist the definition to fit their product offerings, saying, for example, “observability is logs” because they sell log management tools, Wilkie said.

“Grafana’s perspective is that observability should be about selecting the right tools for the right jobs,” Wilkie said. “The focus is shifting toward convergence — merging APM and infrastructure observability into unified, semantically-rich systems that help developers reach root cause faster.”

In other words, think smart metrics that even the non-DevOps person should be able to understand to make decisions. “It’s no longer just about storing logs or metrics at scale. The emphasis is on helping engineers understand system behavior more quickly and intuitively — without needing deep expertise in telemetry formats or query languages,” Wilkie said. “This move toward curated, user-friendly experiences is extending observability to wider audiences, including business stakeholders and customer support teams.”

For example, one of Grafana’s retail customers in Spain found that their Elastic-based solution couldn’t handle their scale. “They switched to Loki, which their engineering teams loved, but their customer support team struggled due to the lack of a familiar UI,” Wilkie said. “The introduction of a graphical logs explorer changed that — suddenly, even third-line support staff could dig into logs and pinpoint issues like dropped orders.”

## AI or Else

When asked about what’s next, Wilkie turned to AI. Grafana recently launched its AI Assistant, which received a strong response. It’s part of a larger vision for making telemetry data easier to access, query, and interpret — even for non-engineers.

The assistant works by leveraging a knowledge graph — built from telemetry data — to map out systems and perform root cause analysis. Connected to a large language model, it allows users to ask open-ended questions like “Are we using NATS anywhere in our infrastructure?” and get actionable insights quickly.

“This has proven especially valuable for senior leaders who were once engineers but no longer have the time or familiarity to query systems themselves,” Wilkie said. “The AI Assistant helps them get answers they would otherwise need to delegate. It also accelerates onboarding and productivity for junior engineers.”

While many proprietary vendors have announced similar AI features, few have brought proper working systems to market. “Grafana, by contrast, built and launched its assistant quickly, offering an experience that aligns with their broader vision: intelligent, accessible and open observability,” Wilkie said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)