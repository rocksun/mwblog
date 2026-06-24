**AI consumes [a lot of data](https://thenewstack.io/clario-data-enterprise-ai-rot/), but all-you-can-eat data in the world of agentic intelligence eventually loses its flavor.** Simply increasing the sheer volume of databases, data repositories and data volumes does not necessarily enrich any given AI function’s ability to reason.

[Context](https://thenewstack.io/why-agentic-ai-needs-a-context-based-approach/), on the other hand, does.

We know that agents are only as intelligent as the context they have access to. In order to codify the inclusion of context into algorithmic logic for AI, technology vendors have extolled the [virtues of using a knowledge graph](https://thenewstack.io/how-knowledge-graphs-make-data-more-useful-to-organizations/) to make their data more useful for agentic purposes.

AWS knows this story all too well. The organization’s sprawling datacenter footprint hosts vast pools of context on behalf of its customers, but that context often sits in a raw and unstructured form across data lakes, data warehouses, data lakehouses, databases, and data streams. It also permeates through the rarely-documented institutional knowledge that agentic engines rarely get access to.

All of which explains why the cloud giant used its [AWS New York Summit](https://aws.amazon.com/events/summits/new-york/) today to introduce [AWS Context](https://www.aboutamazon.com/news/aws/aws-summit-nyc-2026-ai-agents), a new service that automatically maps the relationships that exist across a firm’s existing data into a knowledge graph and provides agentic search so AI agents in the organization can access what are governed data relationships, business rules, and domain knowledge at runtime.

But weaving all this together is hard work. Knowledge graphs need more than simple keyword matching to work; they require structural and semantic traversal. This means they need to make multiple hops across various information silos and repositories so that they can aggregate context and (for example) be able to explain why cybersecurity vulnerability A is a factor of system compromise B, which has a core dependency link to codebase C, which executes in application D and risks taking users X, Y and Z offline. So how is AWS doing this?

## A data lake of nuance & information

[Mai-Lan Tomsen Bukovec](https://www.linkedin.com/in/mailan/), AWS vice president of technology (data and analytics) tells *The New Stack* that AWS Context provides a “data lake of nuance and information that AI agents swim in” to reason correctly and make the right decisions for the business.

> “This is no different from how humans work. When we take action, we depend on our own context about the domain, prior decisions and their outcomes, and other information.” – Mai-Lan Tomsen Bukovec, AWS.

“This is no different from how humans work,” Tomsen Bukovec says. “When we take action, we depend on our own context about the domain, prior decisions and their outcomes, and other information. With AWS Context, AI agents have all the nuance of every form of data in their business in a knowledge graph and in open data formats. AWS Context will make the difference between an AI agent simply taking an action versus making the right decision.”

Given the option to embrace this new service, software engineers will need to set out a plan of action and work out what to do first. For AI developers and data science professionals, this throws up the question of what to prioritize first when preparing existing enterprise data for context-aware agents using AWS Context capabilities and how they can control what data is (and isn’t fed) into the mouth of the beast.

Mercifully, it appears, options for control appear to exist.

“If developers want to exclude information from AWS Context, they will have the ability to prevent certain datasets, like test data or sandbox environments, from being included with AWS Context,” explains Tomsen Bukovec. “Because AWS Context is continuously updated as relationships between data resources changes, AI agents have the latest context available without any intervention from AI developers – and the control to set guardrails to exclude content that agents should not take action upon.”

## Should developers trust this technology?

AWS Context extends the same knowledge graph technology that runs [Amazon Quick](https://aws.amazon.com/quick/), the organization’s AI work assistant that “connects scattered work” across applications and resources, including Slack, Microsoft Teams and Outlook, CRMs, databases, and documents.

So, should software developers place their trust here? After all, even once captured and connected, not all business context is useful. Some contextualizations could be corrupted, weak, fragmented and not productively useful for the business? Is AWS at risk of encapsulating context without considering how the data that comprises it is is quantified in terms of business usefulness?

AWS has thought of this factor.

Because AWS Context uses the same knowledge graph technology that powers Amazon Quick, it can learn from usage patterns to make every interaction smarter. With AWS Context, the company says it is extending what was a personal knowledge graph into an organizational one i.e. a shared, governed context layer that agents and applications in an organization can draw from.

> “Developers can govern and shape a dynamic and intelligent context layer that AI agents depend on to make the right decisions – AI agents won’t just get smarter as the models improve – they will be smarter because they have a vast amount of curated context at their fingertips.” – Tomsen Bukovec.

“AWS Context provides a data lake of [context in graph and open data format](https://thenewstack.io/aws-why-we-support-sustainable-open-source/),” clarifies Tomsen Bukovec. “That means that AI developers everywhere can use capabilities at the data layer to govern and shape a dynamic and intelligent context layer that AI agents depend on to make the right decisions. With this change, AI agents won’t just get smarter as the models improve – they will be smarter because they have a vast amount of curated context at their fingertips.”

## Curated knowledge beyond a user’s personal graph

Existing Amazon Quick users will see that when AWS Context is enabled, Quick’s agents gain access to the broader enterprise knowledge graph, including cross-system relationships, business rules, and curated context that go beyond what any single user’s personal graph can provide.

Tomsen Bukovec has also said that AWS Context gets smarter the more agents use it. As agents query the graph, it observes which sources produce correct results, which join paths agents rely on, and which curated rules get applied. It ranks sources by actual usage and shares what it learns across an organization, so when one agent discovers a correct join path or resolves a schema ambiguity, other agents pick it up, without requiring a human to re-curate the graph.

Any agent you put into production raises a governance question: what data can it reach, and can you show exactly what it accessed and under whose authority? The organization has explained that AWS Context answers both by making every query identity-aware.

Each call is designed to inherit the calling user’s identity access management (IAM) and [Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-reference.html), so an agent can only see and traverse the relationships its identity is authorized to access. Because access runs through identity, every interaction is auditable. Security and compliance teams can verify what an agent accessed and under what authority, using the same controls.

## AWS Glue Data Catalog

Related news to the arrival of AWS Context today saw the company also announce the preview of business context and semantic search functions for [AWS Glue Data Catalog](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/aws-glue-data-catalog.html#), the company’s centralized metadata repository for all data assets across various data sources. The new functions are designed to make it easier for humans and AI agents to discover and understand data.

Also in this product stream, AWS now offers offer a preview of skill assets in Glue Data Catalog, a service designed to allow “data producers” (a somewhat arbitrary term that AWS applies to anyone who creates data, but is most likely a DBA or developer) to create skill assets.

Associating skill assets to data assets gives agents additional context and instructions they can retrieve progressively for working with specific data without re-teaching it to every agent one prompt at a time.

## A renaissance of context engineering

Will this new drive from AWS herald the birth (or perhaps renaissance, the [industry has been talking about this approach](https://thenewstack.io/context-engineering-the-foundation-for-reliable-ai-agents/) for some time) of context engineering as a sub-discipline of data science? It may well do… and if it does, it will likely drag role-based multi-agent orchestration along into the fray with it as we weave ever more complex interrelationship structures through enterprise data stacks.

If AWS or indeed the other hyperscalers or major frontier model companies starts acquiring more multi-model graph structure companies and vector database specialists, that could be the sign that things are cementing around context engineering at large.

In the meantime, developers setting sail on the contextualized data lake of nuance are advised to wear a life jacket.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)