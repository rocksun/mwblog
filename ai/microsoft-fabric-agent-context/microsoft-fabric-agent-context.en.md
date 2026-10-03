**Microsoft is turning Fabric**, its integrated data platform, into the place enterprise agents go to learn how a company works, whether that’s what happened last quarter or what’s happening on the factory floor right now.

On Tuesday, at its FabCon and SQLCon data conference in Barcelona, Spain, Microsoft outlined the next step in its vision for how the products that make up Fabric can simplify all of this information gathering.

Microsoft, for example, described how [**Fabric IQ**](https://learn.microsoft.com/en-us/fabric/iq/overview), the context layer inside Fabric, now feeds Microsoft 365 Copilot by default. Outside agents can query it over MCP. Power BI will soon be able to turn the same definitions into apps. And ontologies, which add business rules to the mix, moved further into preview.

![](https://cdn.thenewstack.io/media/2026/09/af4a4c3c-img_5653-1024x768.jpg)

*Credit: The New Stack*

As Microsoft [Fabric](https://www.microsoft.com/en-us/microsoft-fabric) CTO [Amir Netz](https://www.linkedin.com/in/amirnetz/) said in a press briefing after the keynote, “Agents are a very, very strange animal, and I always like to say it’s like Drew Barrymore from *50 First Dates*. Every time they open their eyes, they forget everything that happened before.

“They don’t know where they are, so the first thing we have to do is tell them where they are. You are now working for Microsoft. You are now working for Wells Fargo. You are now working for Emirates.”

> “Agents are a very, very strange animal, and I always like to say it’s like Drew Barrymore from *50 First Dates*. Every time they open their eyes, they forget everything that happened before.”

Customers tend to find this out the hard way. [Yitzhak Kesselman](https://www.linkedin.com/in/yitzhak-kesselman/), the corporate vice president who runs Fabric IQ, tells *The New Stack* that companies unify their data, run models on it, and then look at the answers.

“Customers that are more advanced on their journey have their own evals for their agent,” he says, adding that what they see sometimes isn’t what they expected. “Then [customers] will understand: ‘Okay, now I need to create the context for my agents.'”

Kesselman says he met with more than 320 companies last year, and the pressure to get there comes from the business side, which asks to “‘show me the value of those agents,'” he says, “‘the before and after.'”

[Arun Ulag](https://www.linkedin.com/in/arunulag/), Microsoft’s executive vice president for [Azure Data](https://azure.microsoft.com/en-us/products/data-factory), said in the keynote that coding agents work because they have “the code, the repos, the change history, the specs, the tests.” But outside of coding, most enterprises have nothing comparable, he argued.

Fabric IQ is one of four pieces of what Microsoft calls Microsoft IQ (this is Microsoft, after all, so there’s always a lot of different names and products involved).

Work IQ covers email, Teams, and SharePoint. Foundry IQ covers documents and manuals. Web IQ covers the public internet.

Fabric IQ, Ulag said, “focuses on the state of your business and how your business actually runs.” His [announcement blog post](https://azure.microsoft.com/en-us/blog/fabcon-and-sqlcon-2026-in-barcelona-building-the-data-foundation-for-microsoft-copilot-and-agents/) describes it as combining “unified data from OneLake, trusted metrics from Power BI semantic models, and operational context from ontologies and real-time intelligence.”

## Getting the data in

“Everyone wants to jump to AI, but then they realize, ‘Oh, I need data for it,'” Kesselman says. “They need data from their business applications, their structured data. They need to have real-time data.”

[OneLake](https://learn.microsoft.com/en-us/fabric/onelake/onelake-overview), Fabric’s storage layer, is at the core of all of this, and for the system to provide context, enterprises have to feed it data from across all the first-party and third-party services they use.

Fabric’s shortcuts and mirroring, which connect or replicate external sources into OneLake, are free of charge, and Netz said storage under management in OneLake is growing 300% year over year.

## What’s new this week at FabCon and SQLCon Barcelona 2026

On Tuesday, the [company announced](https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/fabcon-and-sqlcon-barcelona-2026-what%E2%80%99s-new-in-microsoft-onelake-and-its-rapidly/5369146) a two-way integration with Salesforce Data Cloud 360, mirroring from Google BigQuery in general availability, a ClickHouse workload that runs that engine directly against OneLake, and dbt’s Fusion engine, due in Fabric in the next couple of weeks.

Simply copying data won’t satisfy security teams, though. Mirrored security roles, which reach public preview in the coming weeks, bring permissions along with the data. Access roles defined in Snowflake, for example, will show up in Fabric with the same members and the same table permissions.

As Microsoft’s [Shireen Bahadur](https://linkedin.com/in/shireen-bahadur), who demonstrated the feature in the keynote, put it, “We’re not just solely replicating security rules. We’re actually actively enforcing and preserving those roles.”

> “We’re not just solely replicating security rules. We’re actually actively enforcing and preserving those roles.”

OneLake isn’t a one-way street. Enterprises can also pull data out and use it in other tools.

OneLake data, after all, is stored in open formats and has open APIs, and Netz said on stage that any engine that reads them can use it. “If you want to use this data that we help people to get for free with our competitors’ tools, go for it. I’m not happy about it, but go for it,” he said.

IQ sharing, now in preview, lets an organization share governed tables, files, Markdown agent instructions, and RDF ontologies with another tenant without copying, with an expiration date. That’s something Fabric users have wanted for a while, and the keynote announcement drew plenty of applause from the thousands of data professionals in attendance.

## Past, present, and future

“Not only what we have in the past, not only what’s happening in the present. We also want the agents to understand what we want to happen in the future,” Netz said in the keynote.

The past is semantic models. A semantic model is the layer under every Power BI report that defines how a metric like revenue is calculated, how entities relate, and which tables supply the numbers. Netz said Power BI users have already created 22 million, and Ulag called them “the core of Fabric IQ.”

The present is [real-time intelligence](https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/trusted-ai-starts-with-microsoft-fabric-real-time-intelligence-and-iq/5369528), Fabric’s streaming and event stack, which Kesselman also runs. He recalls two CIOs telling him the same thing that day in Paris. “‘There is no AI without RTI;’ there’s no AI without real-time intelligence,” he says. “If you don’t have the streaming data… data that is fresh, you will run your LLMs on data which is like hours or days old.”

> “‘There is no AI without RTI;’ there’s no AI without real-time intelligence.”

A signal on its own isn’t enough, though: “You want to take the signal that you get now… the event that comes now, and look historically, okay, is it an anomaly or not?” Kesselman says. That’s why the keynote showed batch copy jobs and event streams feeding each other, so an agent can judge what just happened against what usually happens.

The future is [Fabric Planning](https://learn.microsoft.com/en-us/fabric/iq/plan/overview), which went generally available in July and got a performance and feature update this week. It’s Microsoft’s tool for budgets, forecasts, and targets, the numbers a business wants to hit rather than the ones it has already recorded.

A plan is a Fabric item like a lakehouse or a notebook, and it borrows its measures from the same semantic models the reports use, so revenue means the same thing in the forecast as it does in the dashboard. In the demo, a change to the inputs cascaded through a model of about 13 million cells.

What makes these work is [ontologies](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview): Formal descriptions of the things a business deals with, how they relate, and the rules for handling them. Netz called them “semantic models plus plus” on stage, and in a later press briefing, he used an airline to explain the plus.

“If you are an airline, you have planes, you have pilots, you have ground crews, you have airports, you have luggage,” he said. Those are the entities.

The relationships between them “are way more than data relationships,” he said. “It’s not only to say, ‘Oh, I have a match with a foreign key and a primary key between a pilot and a plane,’ but it could be a policy relationship. Which pilot can fly which plane based on their certification, or is the pilot allowed to fly this plane right now based on the rest hours in the last 24 hours?”

But ontologies don’t only define nouns; they also define verbs. “I can ground a plane. I can redirect the plane. I can assign a plane a gate.”

Creating those ontologies, which have to map the various terms that a company might use for the same thing to a single entity, can be extremely time-consuming. But since they are so core to this project, and to allowing agents to reason over data, Microsoft built a tool to generate them automatically.

## Putting it to work

Fabric IQ in Microsoft 365 Copilot Chat and [Cowork](https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/30/copilot-cowork-now-available-in-frontier/), the mode for delegating multistep tasks that Microsoft built on the technology behind Anthropic’s Claude Cowork, is generally available as of Tuesday. It answers business questions from Power BI semantic models and reports; it’s on by default for Fabric and Power BI customers, and Microsoft says it doesn’t consume additional AI tokens.

![](https://cdn.thenewstack.io/media/2026/09/7060ea0d-img_5661-1024x768.jpg)





*Credit: The New Stack*

But business users don’t just want to chat with these models. In this age of vibecoding, they also want to generate applications that use all of this data.

Power BI Desktop is getting an [app-creation experience](https://community.fabric.microsoft.com/blog/fbc_pbiupdatesblog/power-bi%E2%80%99s-next-chapter-the-evolution-of-business-intelligence/5369131) in preview in the coming weeks. Users start from a semantic model, describe the app, and then have Copilot generate and publish it to Fabric.

Unlike with a report, Ulag wrote, these apps “can accept inputs, write back data, preserve shared state, and support operational workflows.”

They’re Fabric Apps built on [Rayfin](https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/introducing-rayfin-a-new-ai-first-way-to-build-deploy-and-govern-application-bac/5191676), the open-source SDK Microsoft introduced at Build. Power BI Pro and Premium Per User customers get them with a Fabric database of up to 1GB per app at no additional cost.

Netz confirmed in the briefing that “there’s no core difference” between the two, and Ulag added, “What gets created is a Fabric app, right? And that’s it.”

For agents outside Copilot, [Fabric IQ MCP](https://learn.microsoft.com/en-us/fabric/iq/connectors/fabric-iq-mcp) is generally available now, with six read-only tools for finding semantic models and reports, reading their schemas, and running DAX queries against them.

Ontology MCP tools, currently in preview, expose ontology definitions and queries. Fabric data agents can now, also in preview, use an ontology as their context source. And the context reaches Microsoft Foundry, Copilot Studio, and GitHub Copilot through the same layer.

Developers can drive the new data engineering agent from their own tools.

Built on the [Osmos technology Microsoft acquired in January](https://blogs.microsoft.com/blog/2026/01/05/microsoft-announces-acquisition-of-osmos-to-accelerate-autonomous-data-engineering-in-fabric/), it takes on long-running work like migrations and ETL, and can be started and steered from GitHub Copilot, VS Code, Codex, and Claude Code.

Frontier models will write that code, Netz said on stage, and “it won’t fail,” but you don’t know whether the results are right.

## Everyone has a context layer now

This year, Databricks shipped [Genie Ontology](https://www.databricks.com/blog/whats-new-unity-catalog-data-ai-summit-2026), Snowflake shipped a [Horizon Context Layer](https://www.constellationr.com/insights/news/snowflake-summit-2026-context-custom-model-training-iceberg-v3), Google shipped a [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction), and Salesforce shipped a headless Data 360, which it describes as a context service. Databricks CEO Ali Ghodsi summed up the pitch at his own conference in June as AI having a context problem rather than an intelligence problem.

Microsoft’s version turns on by default inside Microsoft 365 Copilot and starts from 22 million semantic models. Microsoft also said this week it will contribute to [Apache Ossie](https://ossie.apache.org/), the vendor-neutral semantic metadata standard Snowflake started, and that it wants DAX, Power BI’s formula language, recognized as an Ossie query language.

When Microsoft [made the context argument at Build in June](https://thenewstack.io/microsoft-build-2026-data-fabric-horizondb-ai-agents/), the pieces that let an agent act on that context were mostly on a roadmap. Now the answers are generally available, and the actions are in preview.

Asked how Fabric copes when the user is no longer one person running a dashboard but a fleet of agents, Kesselman points to observability.

“Fabric really allows you to have this kind of holy grail of combination of both kinds of system data, how the agent runs, but also the business data,” he says, so a company can check whether an agent did what it was supposed to do and what that did to the business. “There’s more in this area that will come in the next few months.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)