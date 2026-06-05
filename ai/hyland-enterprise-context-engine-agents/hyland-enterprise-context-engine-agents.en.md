Just about every enterprise software vendor now agrees on one thing, at least: AI agents are only as useful as the context they’re given.

That’s where the alignment seems to stop; the actual debate is over *how* you get that context.

[Hyland](https://www.hyland.com/en) CEO [Jitesh Ghai](https://www.linkedin.com/in/jitesh-s-ghai-a91274/)‘s answer is that you don’t get that context by tearing your company down and rebuilding it.

At its CommunityLIVE 2026 conference this week in Florida, the enterprise content management vendor unveiled a slew of platform updates supporting Ghai’s thesis. For one, the company announced general availability of its Enterprise Context Engine and Enterprise Agent Mesh, and introduced both Agent Lifecycle Management and a new headless mode for its Content Innovation Cloud, which will allow agents to interact with its service directly.

Ghai’s pitch sets Hyland against the conventional playbook for getting an enterprise ready for agents.

> “There are many folks who are saying you need to completely revisit all your business processes … to agent-enable your enterprise. This is what I call blowing things up, and I don’t think any of it is necessary. In fact, I think it’s improper.”

In an interview last week ahead of the conference, Ghai told *The New Stack*, “There are many folks saying you need context, and if you want context, you have to move all your data into the cloud. There are many folks who are saying you need to completely revisit all your business processes and drive enterprise-wide change management to agent-enable your enterprise. This is what I call blowing things up, and I don’t think any of it is necessary. In fact, I think it’s improper.”

![](https://cdn.thenewstack.io/media/2026/05/64617926-control-tower-dashboard-1024x655.png)

Credit: Hyland.

His alternative is to leave the existing stack in place. “If you want context, you have to meet an organization where it is, not reinvent yourself as a new organization,” Ghai says. “Context is understanding your organization with your existing systems, your existing enterprise content, the existing data, and the existing business processes of the organization.”

## Context is what it’s all about, not blowing everything up

Virtually every enterprise vendor — not just in the content management space — now seems to believe that context is what separates AI demos from something a regulated business can actually run on.

OpenText, for example, has positioned its Content Cloud as a context layer for enterprise agents. Box, meanwhile, is pushing to become the enterprise content hub. At this point, the entire field treats context as the moat.

And while Hyland may not be a household name outside of its niche, the company says it has well over $1 billion in revenue and around 15,000 customers.

As Ghai noted, these are concentrated in regulated industries such as healthcare, insurance, banking, and government — industries where unstructured documents are central to a company’s operations. Ghai, who joined Hyland as CEO in May 2024 after a long run as chief product officer at data-management vendor Informatica, brings a structured-data background to a company whose core asset is unstructured content.

## Automating the “human ETL” to give structure to unstructured data

![](https://cdn.thenewstack.io/media/2026/06/e04c9292-screenshot-2026-06-01-at-10.44.43.png)

*Hyland CEO Jitesh S. Ghai (Credit: Hyland)*

Hyland appears focused on automating much of the manual labor that sits between a document and a decision. Ghai calls it “human ETL,” borrowing from the “extract-transform-load” jargon of the data pipeline world.

“All of these types of workloads [are] what I call human ETL,” Ghai tells *The New Stack*. “It’s people spending valuable human capital time, their valuable time, extracting, transforming, and loading, and interpreting.

“And why was this? Because you couldn’t give structure to unstructured data. You can now.”

He believes knowledge workers in these industries currently spend somewhere between 20% and 40% of their time on that kind of document-centric admin work.

Ghai also believes that 70% to 90% of enterprise data is unstructured, and, to Hyland’s advantage, most of it sits in a content management system. Large language models, in his view, will finally make that content tractable and enable employees to focus on more important tasks.

“Through the content-powered agentic enterprise, we want to bring the joy back to the job,” Ghai says. “We want to eliminate the administrative burden.”

## How Hyland delivers context

One thing Hyland is focused on is making the transition to the agentic era easy for enterprises. The first layer here is Hyland’s Content Innovation Cloud, a content federation layer that reaches into existing systems. On top of that, the company applies AI to structure unstructured documents and build a knowledge graph. Combined with structured data from third-party systems, this makes up Hyland’s content and data fabric.

The Enterprise Context Engine, now generally available, is Hyland’s term for this contextual layer. It’s a governed environment for content curation, knowledge enrichment, and knowledge graphs shaped by industry-specific ontologies across healthcare, insurance, financial services, education, and government.

> “So many initiatives are failing because there’s an under-appreciation for the complexity of the underlying data.”

This ontology, says Ghai, is the part that most vendors underrate.

“So many initiatives are failing because there’s an under-appreciation for the complexity of the underlying data,” he says. “And it’s not simply curating it; it’s also linking it to its business relevance, which is the industry ontologies.”

He draws a line between the easy version of this and the hard one. “You and me playing with Claude Code, we have our context window, and we can throw a bunch of stuff in there and get all sorts of value from that,” Ghai says. “At enterprise scale, it’s a whole other exercise.”

## Governance is the other half of the bet

But context without control is a hard sell in industries that must answer to regulators, and, like so many enterprise vendors right now, Hyland is building a governance layer. The upcoming ‘Control Tower’ is meant to serve as the command center for the Agent Mesh by providing continuous observability into agent performance, decision pathways, and governance status.

Underneath all of this sits Hyland’s Agent Lifecycle Management, a framework that follows an agent from design through retirement in a data center upstate. It includes an Agent Library that catalogs every agent in the organization, a set of base agents and archetypes, and an Agent Passport, which Hyland describes as a certificate that an agent in its system must hold, defining its identity, capabilities, guardrails, and compliance status before it can run in production.

To make it easier for enterprises to get started, Hyland then rolls all of these services into a more easily consumable package, with pre-built (but modifiable) agents for healthcare organizations, banks, and other regulated industries.

## Going headless

For developers, headless mode is likely the most interesting announcement. It exposes this AI-native fabric as a set of consumable APIs, letting customers and partners pull Hyland’s enrichment, context, reasoning, and governance capabilities into their own applications, third-party AI tools, and custom workflows — all without touching Hyland’s interface.

Hyland believes this headless mode will bring the Content Innovation Cloud from a set of packaged applications into core enterprise infrastructure and extend its reach to data engineering teams, ISVs, and platform ecosystems like Databricks and Snowflake, where a customer may never adopt a Hyland front end but might still consume its data.

## Context

Ghai is clear-eyed about the fact that Hyland won’t be where a company is going to build every agent (though the company does have tools for that as well). “And that is what we’ve very intentionally made headless,” he says. “So that third-party agents can get access to it. Data science workloads can get access to this AI native curated data set, and our agents can get access to it because it delivers enterprise context.”

When fragmentation is a given, neutrality is the safer bet. “There’s going to be fragmentation, and we recognize the value we uniquely deliver, which is context from your content and data and processes within the enterprise,” Ghai says. “We recognize that there are other vendors that could equally benefit; their agents could equally benefit from this. And that is why we believe we have to be independent and neutral, open and modular.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)