After two years of rapid experimentation and deployment, 2026 will be the year when enterprises confront the realities of scaling [AI systems](https://www.confluent.io/lp/2026-predictions-report/?utm_campaign=tm.campaigns_cd.q4fy25-predictions-report&utm_source=the-new-stack&utm_medium=article). Every layer of the data stack is being stress-tested by AI workloads, and the infrastructure that powered the past decade of digital business wasn’t designed for the relentless, context-hungry demands of [AI agents](https://thenewstack.io/how-ai-agents-will-change-the-web-for-users-and-developers/).

The next year will separate companies that treat AI as a side project from those that rebuild their data foundations to support it. Here are six infrastructure shifts that will define 2026.

## MCP Becomes Table Stakes

As [agentic AI](https://thenewstack.io/ai-agents-vs-agentic-ai-a-kubernetes-developers-guide/) projects mature, it’s clear that AI needs unimpeded access to data and the ability to take actions across systems. One challenge is that the leading frontier providers created different approaches to external tool and function calling, creating headaches for developers who need to easily swap models.

[Model Context Protocol (MCP)](https://thenewstack.io/one-year-of-mcp-looking-back-and-forward/) has rapidly emerged as the standard for connecting AI applications to data sources regardless of the [large language model (LLM)](https://thenewstack.io/what-large-language-models-can-do-well-now-and-what-they-cant/). Early adopter platforms quickly added MCP support, recognizing that an easy and open standard would make it much easier to integrate and provide support to the AI market than trying to maintain many tightly coupled integrations.

Certainly some hurdles remain, particularly around security. But the draw of a single, open protocol that reduces friction will be irresistible. By mid-2026, tech platforms without MCP support will be left out of the next generation of AI applications.

## Databases Will Be Strained By Agent Workloads

Agents won’t just augment human tasks, they will multiply data demands exponentially. Agents are greedy. They don’t get tired, they don’t wait for business hours and they operate at scales impossible for humans. An agent optimizing a supply chain can generate more database queries in an hour than a team of analysts in a week.

The challenge is that many legacy and enterprise databases are already struggling with current loads. Adding AI agents on top of over-burdened databases is a recipe for cascading failures. An already established pattern of using change data capture (CDC) pipelines feeding near-real-time data to massively scalable modern databases that can handle the insatiable demand will become a requirement for survival.

## Data Governance Becomes the Critical Path

AI has made data governance even more critical. AI applications can’t paper over gaps with institutional knowledge or tribal wisdom of the human workforce. Without the right context, AI applications don’t work but security and privacy controls must still be adhered to. When AI makes a decision, organizations need programmatic access to its complete data lineage. And beyond just the simple lineage of supporting context, end-to-end data flow in agentic systems must be auditable and replayable for rapid and iterative improvement, troubleshooting and compliance reasons.

2026 will force all companies to double down on their data governance infrastructure. A troubling pain point is cross-system data lineage. It’s not uncommon to see data flow from mainframes through message queues, be combined with SQL Server data via APIs and land in multiple downstream systems. Tracing these sorts of journeys is critical. Vendors like Confluent and Databricks offer excellent governance within their platforms, but the gaps in between platforms are where AI can break down. Companies will also need to treat data flow in and out of agents themselves with the same level of diligence.

## Vendor Lock-In Will Become a Major AI Risk

The relative technical ease of switching between LLM vendors created a false sense of security, but the battle is shifting from models to ecosystems. Model providers are aggressively building proprietary platforms that provide agent frameworks, development tools and data integration. Connecting enterprise data and building agents within their walls can leave organizations trapped.

Once operational data and business context are deeply embedded in a vendor-specific ecosystem, migration costs become astronomical. This is the age-old trap of data gravity at work. In 2026, companies will realize it’s imperative to have strategic vendor independence built into their AI architecture from the start.

The solution is an independent data plane. Smart companies will architect their AI stack to keep their data separate from AI tooling. This decoupling ensures data remains portable and allows organizations to switch AI vendors without a devastating divorce. Companies that figure this out in 2026 will maintain negotiating leverage, have access to best of breed technologies and agility in adopting new AI technologies as they come to market. Those that don’t will find themselves locked in.

## Adoption of Durable Execution Engines Will Accelerate

Durable execution platforms like Temporal and Restate have been simmering, but 2026 will see adoption accelerate dramatically. They make reliability a built-in primitive rather than something engineers must hand-code into every application.

AI agent use cases will accelerate adoption. Agents require multisystem interactions, local state management and multistep processes — exactly what durable execution engines excel at. Developers who’ve spent years wrestling with distributed system reliability will wonder how they lived without these tools.

The infrastructure reckoning of 2026 isn’t a failure of AI, it’s a sign of its progress. Production AI systems are finally demanding enough to expose the weaknesses in enterprise data foundations. The companies that invest now in protocols, governance, vendor independence and scalable architectures will gain decisive advantages as AI moves from experiment to operational core.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/12/6d1af27b-cropped-f3451fef-willlaforest-scaled-1-600x600.jpeg)

Will LaForest is global field CTO at Confluent. He collaborates with customers worldwide across all industries, guiding them in leveraging the advantages of a data streaming and event-driven architecture. Will is passionate about data and AI innovation and has over...

Read more from Will LaForest](https://thenewstack.io/author/will-laforest/)