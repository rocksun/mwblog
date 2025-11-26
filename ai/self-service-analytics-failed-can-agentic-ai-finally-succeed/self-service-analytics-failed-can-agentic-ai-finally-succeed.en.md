For over a decade, the data industry chased the dream of self-service analytics. The promise was simple: Give everyone access to data, and insights would flow. In practice, few organizations succeeded. The hurdles were higher than anticipated, and even when you cleared them, the finish line kept moving.

## The Three-Part Problem

The challenge breaks down into three interconnected problems.

First, there’s [access control](https://thenewstack.io/3-frameworks-for-role-based-access-control/). Providing governed, secure access to data across an entire organization is hard. Different teams need different permissions. Compliance requirements vary by region. Personal data needs protection. Getting this right requires substantial infrastructure and ongoing maintenance.

Second, there’s usability. Even with access, tools remain intimidating. Direct database access requires SQL fluency. Business intelligence (BI) tools, despite their visual interfaces, aren’t always intuitive. Each platform has its own terminology: dimensions versus metrics, axes versus labels, measures versus fields. Users face hundreds of chart types with subtle differences. The learning curve is steep, and the climb never really ends.

Third, there are the business definitions, aka semantic understanding. Where does the data live? What do these column names mean? How does the finance team define “monthly active users” versus the way the product defines it? This institutional knowledge lives in scattered documentation, Slack threads and people’s heads. Onboarding new team members to your data takes weeks or months.

Each piece is hard. Together, they proved unsolvable for many organizations.

## **Where AI Actually Helps**

Some AI use cases can feel like solutions searching for problems, but [large language models (LLMs)](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) address real pain points in analytics workflows.

* **SQL generation is increasingly reliable in practice*.*** LLMs already see extensive use in code generation, and that includes SQL. The barrier of learning SQL, which kept many business users from accessing data directly, can be dramatically reduced. There is, of course, room for improvement. More complex queries can still be challenging, and less-common SQL dialects are prone to mistakes. But every generation of model has generally [improved SQL generation quality](https://thenewstack.io/sql-schema-generation-with-large-language-models/) and increased the ability to reason when given strong schema and business-context cues.
* **Understanding context.** Just like humans, LLMs need context about the systems and data that they interact with. There are often pockets of documentation spread about internal systems, and it can be hard for humans to find and digest. [LLMs have developed wide context windows and are able to search and read external context from a variety of sources](https://clickhouse.com/blog/ai-first-data-warehouse#comprehensive-business-glossary). They can bring semantic understanding to the user, even when the user themselves does not supply it. This is not without its own challenges; there is upfront and ongoing work required to ensure that metadata exists, is kept up to date and is accessible by an LLM.
* **Chat interfaces democratize interaction.** [You no longer need to master the idiosyncrasies of BI tools](https://clickhouse.com/blog/agentic-analytics-slack-clickhouse-mcp). No scrolling through chart libraries. No wrestling with configuration panels. The interface is conversational. Type what you want. Speak it. Drop in a screenshot of a mockup. Express your needs as if asking a colleague to build it, without actually consuming anyone’s time.

These advances solve the user-facing practical barriers that held back access to analytics.

## **The Vendor Lock-In Challenge**

Progress has been made, but challenges remain. Access still needs governance. Tools must integrate efficiently with databases. And here’s where the current landscape gets complicated.

Many major proprietary software vendors offer great first-party solutions. These provide good experiences that extend native access controls and make platforms more accessible. They’re legitimate solutions that work within their ecosystems.

But they don’t cover the full range of use cases. They can’t be decoupled from the vendor. You can’t deploy your own internal ChatGPT-style interface that anyone can use, regardless of vendor knowledge. And critically, they can’t provide unified access across multiple data sources.

## **The Multisource Reality**

Most businesses don’t have a single data provider. There’s the analytical data warehouse, the operational Postgres database backing the main app, MySQL supporting another service and maybe an [Oracle](https://www.oracle.com/developer?utm_content=inline+mention) ERP lurking somewhere. Outside of databases, there’s conversation in Slack, billing information in Stripe and account data in Salesforce. Users frequently need to correlate operational data from these sources against analytical data in the warehouse.

The traditional solution? Create a “single source of truth” by replicating everything into the warehouse. In practice, this approach has roughly the same success rate as fully self-service analytics itself. Most organizations still have data silos.

Five years ago, the data mesh concept promised to solve this with engines like Trino and Presto: Query anything, anywhere, from a single interface. They work, but they’re complex, heavyweight and bring us back to square one on access and usability.

## **Enter MCP**

LLMs and the [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) offer an interesting alternative. Instead of a “meta-engine” sitting above all data layers, MCP servers expose the raw functionality of almost any database through a common, interoperable protocol. Rather than translating a “meta-SQL” dialect through plugins into downstream syntax, LLMs simply write native SQL for each database.

[This is an elegant technical solution to the integration problem](https://clickhouse.com/blog/agent-facing-analytics), but we can’t use first-party vendor experiences to implement it.

## **The Open Source Agentic Data Stack**

What we need is [an open stack that enables building these experiences in-house](https://clickhouse.com/blog/librechat-open-source-agentic-data-stack), works with any data vendor using open protocols and lets users interact with conversational language.

This stack has three core components:

* **The database layer** provides real-time analytical capabilities at scale. It needs to handle high-throughput, concurrent queries with low latency. This is essential when AI agents can generate far more queries than human analysts.
* **The protocol layer** (MCP) creates a standard interface between AI applications and data sources. Developers expose data through MCP servers, and AI applications connect as MCP clients. This works for databases, file systems, development tools, web APIs and productivity tools.
* **The chat interface** (like [LibreChat](https://www.librechat.ai/)) gives users and organizations complete control over their data, agents and conversations while supporting enterprise-grade deployments.

The keyword throughout is “open.” Open source components. Open protocols. Open standards. This prevents vendor lock-in while enabling organizations to customize for their specific needs.

## **Real-World Adoption**

This is already a reality for many organizations that have deployed these stacks in production.

[Shopify uses LibreChat to power reflexive AI across the company](https://clickhouse.com/blog/librechat-open-source-agentic-data-stack#shopify). With near-universal adoption and thousands of custom agents, teams connect to more than 30 internal MCP servers, democratizing access to critical information.

In health care, [cBioPortal uses this stack to enable cancer researchers to ask entirely new questions about genomics and treatment trajectories](https://clickhouse.com/blog/librechat-open-source-agentic-data-stack#cbioportal). As their team puts it, “It puts discovery at researchers’ fingertips.”

[ClickHouse uses these systems internally for its AI-first data warehouse](https://clickhouse.com/blog/ai-first-data-warehouse), handling approximately 70% of warehouse queries for hundreds of users, with usage growing rapidly.

## Are We There Yet?

Hallucinations still exist, and these aren’t always trivial to spot, particularly when we’re providing access to users who are not domain experts. The “How many R’s are in strawberry?” problem has been a recurring joke for some time, and it continues to sweep social media as the most basic barometer of newly released models.

On the face of it, it sounds like a trivial issue, but it’s an amusing demonstration of the problems that LLMs can introduce. The pattern we might expect is that a model generates a SQL query, sends it to the databases to process our data and the model returns the output to us. We can verify that the SQL is correct, and we know the database will execute it correctly.

However, that leaves us with some open questions:

1. If LLMs enable users with no SQL knowledge to query databases, who is responsible for validating that the SQL is semantically correct?
2. Users are often asking models to interpret results. If a model cannot reliably count the three R’s in strawberry, can it reliably interpret trends in your revenue numbers?

This is perhaps the largest area of uncertainty in introducing AI into our analytics. While these problems do appear to naturally improve with each generation of model, they currently require care and attention in practice.

In the real-world examples above, the teams implementing AI platforms are monitoring queries and outputs for quality using tailored LLM observability solutions. Offline and online evaluations allow for these variables to be scored, enabling teams to measure effectiveness, detect regressions and continuously improve system performance. Doing this effectively and simply is still an open challenge and the largest opportunity for improvement ahead.

## **What This Means for You**

There are clear, practical advantages of an open stack.

With an open UX layer like LibreChat, you get the familiar chat interface without tight coupling to any vendor. Not your database vendor, not your AI provider. Deploy it once, and it works the same whether you use models from OpenAI, Anthropic or [Google](https://cloud.google.com/?utm_content=inline+mention), or you integrate with ClickHouse, Postgres, [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) or Oracle.

[![](https://cdn.thenewstack.io/media/2025/11/f99544a4-image1-1024x574.png)](https://cdn.thenewstack.io/media/2025/11/f99544a4-image1-1024x574.png)

When the interface is conversational, the learning curve flattens. Users don’t need to become SQL experts or BI tool power users. They just need to know what questions to ask. This greatly reduces the support and upskilling burden, allowing builders to focus on what they do best: building.

[Integrations rely on open standards like MCP rather than vendor-specific APIs](https://clickhouse.com/blog/integrating-clickhouse-mcp). As LLMs continue to improve at generating SQL and reasoning about data context, your stack gets better automatically. You’re not waiting for a vendor to update their proprietary integration layer.

With an open stack, your data does not disappear into someone else’s black box. You have control to analyse usage, assess the quality of answers and gauge the real value the system delivers. This isn’t a simple task today, but your stack remains open to adopt new methodologies as the space evolves.

Ultimately, you own your stack. You can evolve it over time. Swap out components as better options emerge. Add new data sources without rebuilding your interface. Change AI providers without retraining users on a new UX. [Instrument and observe usage, performance and consumption](https://clickhouse.com/blog/llm-observability-clickstack-mcp). This flexibility matters when you’re building infrastructure meant to last years, not months.

The same interface. The same user experience. Swappable models and pluggable integrations.

## **Self-Service Wasn’t Wrong, It Was Early**

The promise of self-service analytics wasn’t wrong. It was ahead of the technology available to implement it. LLMs don’t solve every problem, but they are beginning to solve the right problems for this use case: code generation and natural language interfaces.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/11/c15429d3-cropped-aa698fc3-alasdair_brown.jpeg)

Alasdair Brown has spent the past decade designing, building and operating data platforms, from user-facing, real-time analytics for top brands, to some of the world's largest nation state cyber-defense systems. He is an advocate for simple data architectures and often...

Read more from Alasdair Brown](https://thenewstack.io/author/alasdair-brown/)