**Salesforce introduced its Salesforce Enterprise AI Harness** on Thursday as a formalized amalgamation of the AI harness concepts and infrastructure the company has been working to align.

The organization said that “no single system has the complete answer” to complete a straightforward business task, such as completing a customer order; i.e., [CRM](https://thenewstack.io/ebooks/generative-ai/developers-guide-to-connecting-crm-data-ai-app-experience/) knows the customer, [ERP](https://thenewstack.io/sap-simplifies-erp-data-access-for-developers/) knows the inventory, [FSM](https://www.salesforce.com/uk/service/demos/field-service-demo/?d=7013y0000026jq4AAA&nc=7013y0000026mOdAAI&utm_source=google&utm_medium=sem&utm_campaign=emea_xc_field-service_cross-industry&utm_content=cross-segment_non-brand+exact_7013y0000026jq4AAA_english_field-service-demo&gclsrc=aw.ds&gad_source=1&gad_campaignid=22814411436&gbraid=0AAAABAVtBhSZT4yDw4YPgwVsSG91KSugz&gclid=CjwKCAjwqonVBhA4EiwA9wYJ3S4sLzp3sb2oXMmcw3T7Q0jy5mmYr1C-LbY4_GVKWteom3VJSgn5GRoCnf4QAvD_BwE) (field service management) knows the delivery, and the support team processes… and so on.

As such, a form of AI leakage pervades throughout modern enterprises, where individual agents and their harnesses do their best to enact automation intelligence, albeit in comparatively siloed chunks.

Salesforce’s answer is to coalesce what it calls “six trusted capabilities” (from its own platform toolset collection) alongside a new AI control plane, built to underpin an open and composable AI ecosystem.

The [Salesforce Enterprise AI Harness](https://www.salesforce.com/agentforce/ai-agents/agent-harness/) encompasses core technologies across [Data 360](https://www.salesforce.com/uk/data/demos/data-cloud/?d=7013y0000026jrrAAA&nc=7013y0000026mQQAAY&utm_source=google&utm_medium=sem&utm_campaign=emea_xc_data-360_cross-industry&utm_content=cross-segment_non-brand+phrase_7013y0000026jrrAAA_english_data-cloud&gclsrc=aw.ds&gad_source=1&gad_campaignid=22814411004&gbraid=0AAAABAVtBhRH7jSRiuxEiM18Vq-hSwMOP&gclid=CjwKCAjwqonVBhA4EiwA9wYJ3eigxoIEgR8P63JfKVD6vOojgDTGgl5YbrHZUddjnzcby7vuLLsv3BoC4mMQAvD_BwE) (a unified customer data platform tool), [Informatica](https://thenewstack.io/informatica-launches-freemium-ai-powered-integrator/) (data integration and governance), [MuleSoft](https://www.mulesoft.com/) and Agent Fabric (API connectivity and multi-agent orchestration), [Tableau](https://thenewstack.io/tableau-informatica-thoughtspot-tout-generative-ai/) (visual business analytics), [Agentforce](https://thenewstack.io/a-guide-to-building-scalable-ai-agents/) (an agent platform), [Salesforce Guardian](https://help.salesforce.com/s/articleView?id=mktg.mc_pers_guardian_about.htm&type=5) (security and compliance), and the Salesforce platform itself through a common, composable architecture and unified experience.

“The Agentic Enterprise won’t be defined by which model a company chooses. Models will continue to change, and intelligence will increasingly be available everywhere. What will differentiate an enterprise is the trusted, proprietary context it brings to that intelligence — starting with the customer — and its ability to securely turn that context into action,” said [Rohan Kumar](https://www.linkedin.com/in/rohankumar/), Salesforce president & chief platform and engineering officer, during press briefing.

> “The Agentic Enterprise won’t be defined by which model a company chooses… what will differentiate an enterprise is the trusted, proprietary context it brings to that intelligence.”

## This is not Salesforce’s first-ever harness

To be clear, it hasn’t taken Salesforce until late 2026 to ever produce or work with a harness; subsystems within the six pack, such as [Agentforce Vibes](https://developer.salesforce.com/docs/platform/agentforcevibes/guide/afv-overview.html) (a natural language vibe coding tool), make use of specialized execution harnesses, including [Mastra](https://mastra.ai/) and the [Claude Agent SDK](https://thenewstack.io/anthropic-pauses-claude-agent-sdk-subscription-change/), to manage local agent execution loops. This is — as suggested — a more formalized, total platform-wide development.

Alongside the six-way alignment spanning context, agency, action, governance, security, and models, Salesforce is offering a new AI control plane to give developers a place to view, manage, and control agents. The company confirms that software engineers can “use the six together as one system or take only what they need,” and create deployments with Salesforce technology, other third-party existing technology, or both.

The big question here is simple: Is this cosmetic packaging designed to disseminate wider Salesforce DNA into software developers’ production environments, or is it a genuinely useful simplification and unification process that will be met with interest and perhaps even gratitude?

Working engineers commenting on sites including the [G2](https://documentation.g2.com/docs/developer-portal) developer forum and B2B software review portal have provided some insight.

## What developers and operations professionals think of the Salesforce stack

Commenting on the use of Agentforce as a standalone tool, operations associate [Ashish B. noted](https://www.g2.com/products/salesforce-agentforce/reviews) in August this year, “One area that could be improved is the initial setup and configuration process. Building effective agents can take some customization and a solid understanding of the workflow. The platform would be even better with simpler configuration options and clearer, more straightforward guidance on setting up agents for specific business use cases.”

Salesforce may have been listening. It said the Enterprise AI Harness connects reasoning to business rules, policies, and controls required for predictable execution. It then makes those capabilities reusable across the enterprise so that context can be shared across agents and models. This means actions and workflows can be securely invoked wherever they’re needed, and governance and security can be applied consistently as AI moves across the business.

> “The platform would be even better with simpler configuration options and clearer, more straightforward guidance on setting up agents for specific business use cases.”

Writing about the Informatica user experience on [Gartner Peer Insights](https://www.gartner.com/reviews/market/data-integration-tools/vendor/salesforce-informatica/product/informatica-cloud-data-integration/review/view/6701538) in March of this year, a [DevOps engineer said](https://www.gartner.com/reviews/market/data-integration-tools/vendor/salesforce-informatica/product/informatica-cloud-data-integration/review/view/6701538) that the platform “works well” for integrating multiple data sources and supports both batch and real-time processing. But they caution, “Debugging and monitoring pipelines can be difficult in complex workflows. Initial setup is challenging for new users and requires some learning curve. [The] User Interface could be improved for better usability and faster navigation.”

Possibly taking into account such feedback, the new AI control plane that accompanies Enterprise AI Harness claims to give businesses a common place to see, manage, and control agents and AI across the enterprise.

“It enables companies to discover and register agents and AI capabilities, establish identity and policy, manage lifecycle, evaluate performance, observe behavior and outcomes, and control cost — across Salesforce and third-party AI. This gives enterprises a consistent layer of visibility and control as AI expands across teams, applications, models, and systems — without requiring every agent or AI experience to be managed separately,” pledged Salesforce.

## Six pillars of trust

The whole premise of this Enterprise AI Harness hinges around what Salesforce calls six trusted capabilities.

Trusted Context combines customer context with data, metadata, semantics, knowledge, real-time signals, memory, and an understanding of how work gets done across the enterprise. Trusted Agency gives agents reasoning, planning, state, memory, and orchestration functions, combining flexible AI reasoning and deterministic controls where certainty is required. Trusted Action securely connects AI to applications, APIs, workflows, tools, and business processes.

As its name suggests, Trusted Governance governs the data, metadata, policies, and processes that AI relies on, with lineage, quality, guardrails, and controls. Trusted Security applies identity, permissions, privacy, data protection, and runtime security to what AI can access and what agents can do. Trusted Models provides security with intelligent model routing based on accuracy, performance, cost, and requirements.

## Integrations with Claude, Slack, Teams, etc.

The Enterprise AI Harness is being built headlessly from the ground up, with capabilities accessible through technologies including MCP, APIs, skills, and plug-ins. The company said this will let Salesforce capabilities extend beyond traditional Salesforce applications, into services such as Claude, Slack, and Microsoft Teams.

Many of the technologies that form the foundation of Salesforce’s Trusted Enterprise AI Harness are available today, with new capabilities and the unified experience planned to begin rolling out in early fiscal year 2028.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)