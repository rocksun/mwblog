At [Snowflake Summit 26](https://www.snowflake.com/en/summit/) this week in San Francisco, the conversation moved into a new direction. If last year’s focus was on the initial wonder of large language models, this year’s story is about the next step in using them: the agentic enterprise.

For enterprises, the question is no longer whether AI can write code, but how to orchestrate it to build, deploy, and manage complex, data-intensive workflows with minimal human oversight.

To understand how Snowflake is positioning itself as a backstop for all things in AI development, reporters and analysts sat down with [Christian Kleinerman](https://www.linkedin.com/in/christian-kleinerman-a973102/), Snowflake’s EVP of Product, at the event.

Following a keynote that unveiled a robust suite of new developer tools, Kleinerman detailed how the company is moving beyond simple code generation to creating a unified, agentic control plane for enterprise AI.

*This conversation has been edited and condensed for clarity.*

**Q: Snowflake Summit 26 has been defined by the move to agentic workflows. When you look at the scene today, how are you defining this move to your customers?**

**Christian Kleinerman:** We are moving into a phase where the value of AI is measured by its autonomy and reliability, not just its conversational ability. Our high-level goal is to simplify the entire data lifecycle. Historically, that lifecycle — from ingestion to transformation to consumption — was a manual, fragmented journey. Today, we are introducing an agentic approach where these steps aren’t just connected; they are orchestrated.

> “We’ve seen scenarios where migration projects that previously took three months of manual labor are now being handled by an agentic workflow in less than five hours, with a human only intervening to review the final output.”

When we talk about the “agentic enterprise,” we mean tools that don’t just assist with code generation but actually build and deploy. We’ve seen that the current developer experience is often broken by “tab sprawl” — developers hopping between ten different apps to solve one problem. Our focus with these new tools is to pull the context into the workspace, allowing the developer to act as an architect rather than a manual typist.

**Q: That leads us to the big news: Snowflake CoCo. You’ve rebranded** [**Cortex Code**](https://www.snowflake.com/en/product/features/cortex-code/) **as** [**CoCo**](https://www.snowflake.com/en/news/press-releases/snowflake-coco-redefines-enterprise-ai-development-as-the-coding-agent-built-for-faster-easier-and-more-powerful-innovation-anywhere/)**. What does this change represent in terms of capability?**

**Kleinerman:** CoCo, which stands for Coding Agent, is a fundamental change in how we handle development. It’s not just a chat interface; it’s a coding agent that can orchestrate data workflows.

![](https://cdn.thenewstack.io/media/2026/06/ad458303-1590958159395.jpg)

Christian Kleinerman of Snowflake

What we’ve learned internally is that when you give a developer the right tool, productivity doesn’t just bump up by a percentage point — it leaps. We’ve seen scenarios where migration projects that previously took three months of manual labor are now handled by an agentic workflow in less than five hours, with a human intervening only to review the final output.

CoCo is now available as a native desktop app, but we’ve also extended it into the places developers live, such as [VS Code](https://code.visualstudio.com/) and [Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel). By meeting builders where they work, we’re allowing them to automate workflows, develop apps, and operationalize AI on enterprise data through a simple prompt. We aren’t just trying to make it easier to write a SQL query; we’re making it easier to deliver a production-ready data product.

**Q: You also announced** [**Snowflake Datastream**](https://www.snowflake.com/en/product/features/datastream/)**. Why is the infrastructure layer so essential to this vision of AI-powered development?**

**Kleinerman:** You cannot have reliable AI agents if the data they are consuming is stale or trapped in a silo. Datastream is our new fully managed streaming service for [Apache Kafka](https://kafka.apache.org/).

The struggle for most organizations has been the complexity of managing separate streaming infrastructure — different brokers, connectors, and maintenance overhead. With Datastream, we’re eliminating that. We are bringing real-time, continuously flowing data directly into Snowflake. This matters because the difference between an AI agent that works in a sandbox and one that works in production is the freshness of its context. If you want to power an AI application that makes real-time business decisions, you need real-time data integration. Datastream makes that seamless.

**Q: There’s a lot of chatter in the industry right now about “token maxing” and AI budgets — some firms are scaling back unrestricted LLM access because costs have spiraled. Are you seeing this concern among your customers?**

**Kleinerman:** We hear it, and it’s a valid concern. My response is always that the absence of usage metrics is the real problem, not the cost itself. If you aren’t tracking your usage, you aren’t being productive; you’re just being passive.

However, we are seeing a trend in how customers approach models. We’ve always advocated for using the *right* model for the job. You don’t need a massive, expensive [Frontier model](https://www.iguazio.com/glossary/frontier-model/) for every task — like sentiment detection or basic data processing. For those tasks, smaller, more efficient models are actually better. We see our role as providing an environment where you can easily swap between models, fine-tune them with your proprietary data, and govern exactly what runs in your organization.

Efficiency isn’t about doing less; it’s about being smarter with what you use. We’re giving developers the tools to optimize, not just to spend.

**Q: You mentioned “non-traditional builders” earlier. How is this agentic stack changing the profile of the people who build software within a company?**

**Kleinerman:** This is the most exciting part for me. For decades, the ability to build data pipelines or automate business processes was reserved for a small subset of engineering-heavy teams. With CoCo, we are seeing analysts and data-savvy business users — people who understand the business logic better than anyone — start creating pipelines and automation tools on their own.

When building with AI becomes as simple as describing the outcome you want, the number of people who can contribute to an organization’s AI strategy increases by orders of magnitude. We aren’t replacing the software engineer; we are evolving the role from someone who writes code to someone who orchestrates systems.

**Q: Looking forward, how do you see the competition between application vendors — such as Salesforce or SAP — and data platform providers like Snowflake in this agentic world? Who owns the process?**

**Kleinerman:** It’s an insightful question, and to be honest, it’s still an unfolding story. You have the business process vendors who hold deep context on how a sales process or an approval workflow should function. Then you have data platforms like ours, which hold the gravity of enterprise data itself.

> “I believe the winner will be whoever builds the most ‘joyous’ product.”

I believe the winner will be whoever builds the most “joyous” product. The internet wasn’t adopted because of a technical manifesto; it was adopted because it enabled people to do things previously unimaginable. We want to be the layer that connects the two — bringing context from those business apps into our governed, data-rich environment. I think the “winner” is ultimately the customer, who will benefit from these systems finally talking to each other.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/09/314a85cc-cropped-89f126f8-chrisp-600x600.png)

Chris J. Preimesberger, a contributing writer/editor at several publications since June 2021, is former editor in chief of eWEEK. He was responsible for the publication's coverage for a decade (2011-2021). In his 16 years and more than 5,000 articles at...

Read more from Chris J. Preimesberger](https://thenewstack.io/author/chris-j-preimesberger/)