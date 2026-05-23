Managing agreements across the enterprise has traditionally been a slow, manual process. [Docusign for Developers](https://docs.google.com/document/d/117r75a6wh955W3FjfICIxA0H6YnIWDM9xcAx_EQ9hOI/edit?tab=t.0#:~:text=https%3A//developers.docusign.com/) has accelerated the process through automation of tedious steps, but the infusion of agentic AI promises to further speed agreement management, transforming it into an agile, seamless, and high-velocity workflow.

At [Momentum 2026](https://momentum.docusign.com/), Docusign’s annual customer conference, Docusign is pushing this boundary with key releases for developers: the Docusign MCP Server, the Agreement Manager API, IAM Toolkit, and a revamped Developer Console.

## The MCP server: Making agreements agent-ready

![](https://cdn.thenewstack.io/media/2026/05/4089920a-unnamed.png)

A primary challenge for AI agents within the enterprise is the generalist nature of LLM platforms. While remarkably capable, they frequently lack the specialized, domain-specific institutional memory required to drive mission-critical business impact. For instance, an agent like Claude may possess theoretical knowledge of Docusign’s agreement platform, yet remain unable to actually interact or interface with its technical capabilities.

The Docusign [Model Context Protocol (MCP) Server](https://developers.docusign.com/platform/mcp-server/) makes the [Docusign Intelligent Agreement Management (IAM)](https://www.docusign.com/intelligent-agreement-management) platform agent-ready, allowing Docusign capabilities to be surfaced in 3rd party AI tools like [Anthropic Claude](https://claude.com/connectors/docusign), [Google Gemini](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/docusign/set-up-data-store), [Microsoft Copilot](https://learn.microsoft.com/en-us/connectors/docusignmcpdemo/), and [OpenAI ChatGPT](https://chatgpt.com/apps/docusign/asdk_app_69fcc3b7582c81918df4ffae40cb7204), moving from conversation to action, without needing to switch tabs.

By connecting Docusign, the MCP server provides business context and institutional memory on which agreement agents can act — and serves as a building block for customers and ISVs developing custom agentic workflows.

In real terms, this means non-technical members of your team can just ask the agent for what they need:

* “Create an NDA with our standard NDA template and send it to John Smith at ACME.”
* “Find all customer contracts that contain a price increase clause and are expiring in the next 90 days.”

> “Traditionally, automating renewals across CRMs, approval systems, and agreement platforms could take hours or days of custom integration work. With the MCP Server, an end user can simply use natural language to generate and send renewal agreements directly from the systems they already work in.”   
>   
> — Aman Dhembla, Sr. Product Manager, Developer Platform, Docusign

New implementations no longer have to wait for the development team. Non-technical teams can start working with agreements in natural language from day one. Users need an authenticated Docusign account to use the Connector in 3rd party tools.

## Agreement Manager API: Unlocking agreement data at scale

Enterprises have hundreds of agreements, often stored in numerous locations. The agreements contain mission-critical information, but by and large, it is “dark data” — impossible to read, extract, or utilize at scale. Docusign’s [Agreement Manager API](https://developers.docusign.com/docs/navigator-api/) (formerly known as Navigator API) provides the ability to **centralize agreements at scale and extract insights from them,** turning contract sprawl into a trusted, programmable data source.

The Agreement Manager API can programmatically upload high volumes of agreements from disparate environments (think SharePoint, Salesforce, legacy CLMs) into a single system of record. Once ingested, a searchable system can be deployed in just minutes. Agreements can be collated into a single searchable data source, making it easy for businesses to surface the insights that impact their business

> “The centralized repository  created by the Agreement Manager API allows organizations to programmatically search, retrieve, and audit their entire contract corpus while ensuring their primary CRMs and ERPs stay perfectly aligned with their actual contractual obligations.”    
>   
> —Steven Baxter, Sr. Product Manager, API Strategy, Docusign

Tedious manual agreement searching becomes a thing of the past. With the Agreement Manager API, teams can build business logic to extract critical information from all agreements from a single source of truth. Never miss an agreement renewal or invoice date. Reporting becomes automated, and agreement data moves from being dark data that required manual search to a secure, programmable interface. Hours of manual work is compressed into seconds.

![](https://cdn.thenewstack.io/media/2026/05/a31ee91d-unnamed-1-1024x735.png)

Implementing [Agreement Manager](https://www.docusign.com/products/platform/navigator) for enterprise customers typically involves multiple steps, such as creating 20–50+ custom agreement fields and types, training AI models, extending standard types with additional fields, testing extraction accuracy, and ingesting large volumes of agreements.

The [IAM toolkit](https://developers.docusign.com/iam-toolkit/) enables system integrators and enterprise developers to implement Agreement Manager programmatically — replacing a manual, UI-driven setup that slowed down time to value for customers with a reusable code-based approach.

Teams can now define Agreement Management configurations as JSON code once, test and refine it in a demo account, promote validated configurations to Production, and then bulk-ingest agreements from the customer’s systems – all through an easy-to-use CLI interface, enabling faster, more reliable, and scalable implementations of Agreement Manager.

Key capabilities for the IAM Toolkit include programmatic **Bulk Configuration** of custom fields and AI extraction logic, as well as **Account Portability** to deploy configurations across environments with a single command. Furthermore, the toolkit supports reliability through **Accuracy Testing** against up to 400 agreements and facilitates **Bulk Ingestion** of agreements at scale directly from customer systems.

**The result:** teams are finding that implementations are 40% faster, providing high time-to-value for customers.

## Developer Console: Manage your integrations in one place

![](https://cdn.thenewstack.io/media/2026/05/9533345c-dev-console-1.gif)

Previously, developers had to manage the same integration across two disconnected accounts: Demo for testing and Production for go-live. This fragmentation created constant admin dependency for go-live, monitoring, and troubleshooting, slowing development and making it difficult to support live integrations. To avoid the back-and-forth between admins and developers, many customers granted developers full production admin access, creating serious governance and security risks.

The new [Developer Console](https://developers.docusign.com/platform/create-ik-developer-console/) solves these problems by consolidating demo and production experiences into a single central place and introducing new developer roles, enabling admins to onboard developers to production accounts with the appropriate level of access.

With this, developers can now access Dev Console directly from within the production account, create integration apps to get Demo client IDs/secrets for development and testing, take integrations live with a single click, and monitor both demo and production usage from one unified dashboard, creating faster time to value for developers on Docusign.

## Momentum 2026

[MCP Server](https://developers.docusign.com/platform/mcp-server/), [Agreement Manager API](https://developers.docusign.com/docs/navigator-api/), [IAM Toolkit](https://developers.docusign.com/iam-toolkit/), and a new integrated [Developer Console](https://developers.docusign.com/platform/create-ik-developer-console/) are now available. Whether you are at Momentum 2026 or following along remotely, there’s no better time to start building.

Explore the [Docusign Developer Center,](https://developers.docusign.com/) spin up a [free dev account,](https://www.docusign.com/developers/sandbox) and join the [Developer Community](https://community.docusign.com/developer-59) to connect with other builders and stay ahead of what’s next.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/11/1c01c260-doug-sillars.jpg)

Doug is a lifelong learner and educator, having focused his career on improving developer knowledge and experiences.  A Google Developer Expert for the web, O’Reilly author, international keynote speaker, and a prolific blogger, he relishes in simplifying the complex. When...

Read more from Doug Sillars](https://thenewstack.io/author/doug-sillars/)