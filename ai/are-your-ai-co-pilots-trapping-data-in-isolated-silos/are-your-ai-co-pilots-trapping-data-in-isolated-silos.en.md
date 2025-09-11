The race is on. By now, virtually every software vendor offers some kind of AI co-pilot designed to assist users within their software. These assistants can significantly speed up daily tasks: GitHub Copilot helps write code, Microsoft Word completes sentences, and Figma’s AI makes design recommendations.

The next logical step for software providers is to build agents that go beyond simple assisting by building real agents that derive insights from data, and sometimes even make decisions. That’s why many software providers are now also pushing [AI assistants that analyze the data](https://thenewstack.io/how-ray-a-distributed-ai-framework-helps-power-chatgpt/) managed by their own software — more or less intelligently. For example, HubSpot’s ChatSpot can now generate reports from CRM data, while Google Analytics’ AI-powered insights can automatically surface unusual traffic patterns or flag sudden drops in engagement. This leads to information stored in those tools being usable more creatively rather than relying on built-in dashboards or manually created reports. Those agents may even end up monitoring the data 24/7, providing insights and recommended actions proactively.

But while each development makes sense from a vendor perspective, this creates a problem for the enterprise: All their AI agents are working in isolated silos.

## The Challenge of AI Fragmentation and Data Silos

[Agents restricted to a single data source](https://thenewstack.io/your-open-source-data-infrastructure-is-ready-for-agentic-ai/) are of limited use, as they only provide insights into a narrow slice of available information. This might make sense in cases where truly specialized agents are needed. But agents that can access all information across an organization offer far greater value. Imagine a customer success agent: Within a CRM, the agent might remind you that a customer’s renewal is due next week, and nobody has reached out so far. Useful — but narrow.

With access to many more tools, the agent could also flag that support tickets from this customer have recently spiked, product usage is down 40% compared to the previous quarter, and no one from the account has attended any webinars or replied to marketing outreach. Instead of a simple nudge, the AI might recommend escalating the account or drafting a tailored check-in message addressing these issues.

Even the classic co-pilots will benefit from enterprise-wide data. Even if it’s something as simple as being able to say: “What you are starting right now, your colleague Anita already tried in a different context three months ago.”

A proliferation of assistants working side-by-side on partial data isn’t in anyone’s interest. Google’s Agent-to-Agent framework aims to address this — at least partially — by standardizing cooperation between agents. However, this doesn’t address the core issue: Ideally, AI agents should operate seamlessly across systems and have unrestricted access to an organization’s entire data landscape, including any publicly available [data from sources such as social networks](https://thenewstack.io/thwart-ops-sprawl-with-a-unified-data-plane/) or review platforms.

## Why AI Agents Need to Be an Orchestration Layer

If your organization is one of the few that manages to keep all its data in a single cloud provider or has implemented a global data warehouse, why not leverage *its* AI capabilities? But shouldn’t we retain the freedom to build our own agents — or use one from a provider who specializes in AI, not data warehouses or data lakes?

This “unified data in one place” perspective is unrealistic for most companies, anyway. Most operate with a patchwork of systems and need open access to the data managed by these tools. But that’s not in the interest of individual vendors, since it cuts into their AI revenue. Some vendors have already started restricting or outright prohibiting access to their data by external agents. It remains to be seen how long customers will tolerate being told they can’t fully use their own data.

In the long run, agentic AI platforms will prevail as platforms that enable the orchestration of AI tools and agents independently of the software tools and underlying data sources in use within an organization. These platforms allow agents to be freely configured and provide them with flexible tools that combine information from multiple sources and abstraction levels. They can also incorporate other agents or, through protocols like MCP, integrate external information gatherers or actors (so-called tools). And, of course, they’ll sometimes embed specialized sub-agents tied to specific software tools — when it makes sense, not because they have to.

Just like [data integration and analytics platforms](https://thenewstack.io/presto-a-data-analytics-ecosystem-built-on-an-open-all-sql-platform/), this approach makes sense to remain technology-agnostic. If you want to switch CRM systems, for example, you don’t have to rely on the new tool’s bundled AI or reconfigure all your agents. You only need to update the few integration tools in the middle layer to point from the old system to the new one.

Finally, this kind of orchestration layer also makes sense from a compliance perspective. If, at some point, you want — or need — to trace how a decision was made, it’s much easier if a tool logs the entire decision-making process of the agent: What queries were processed, what tools were called with which parameters, and what data was retrieved from where.

We see this at KNIME ourselves. We’ve built an internal AI agent (codename: AKA — Ask KNIME Anything) that relies on a wide range of tools to access structured information about customers, users, events, and internal data like employees, finances, and documentation. KNIME employees use AKA to get quick insights on a wide range of customer-, marketing- or HR-related questions, without needing to know anything about the software where those insights are typically accessed. The key is that these tools don’t just offer raw [data access — they often consolidate insights from multiple sources](https://thenewstack.io/icymi-deepseek-is-an-open-source-success-story/).

For instance, the “Customer Information” tool pulls together data from the CRM, support system, and event database. AI could theoretically do this kind of integration too, but that would make its job even harder. Plus, many companies already have these kinds of data integration workflows in place. Just imagine how cumbersome it would be if a so-called “know-it-all” agent had to piece everything together from the raw outputs of various systems or fragmented insights from their specialized AIs. And this, of course, gets even more interesting when an AI gradually builds and refines its own information-gathering tools — using user feedback to improve its modeling (to avoid saying “understanding”) of the organization’s structure and relationships.

## The Compounding Returns of Broad Data Access for Agents

So how do you measure the added value of such an AI orchestration layer compared to software-specific AI islands? As so often, it’s not easy. The real impact emerges over time: The more integrations an agent has access to, the more useful it becomes. No agent will solve every problem from day one. User feedback improves prompts and agent memory, and ongoing refinements make the agents better step by step. Initially, an agent embedded in a specific tool may appear superior — perfectly tuned for that environment. But soon, an agent with access to broader information will surpass that specialist.

The next big question will be how toolmakers try to force customers to stick with their AI offerings. Some have already started blocking access to external AIs. For cloud providers, this is not just a product issue but also a bandwidth issue. If every customer accesses their data manually, it’s manageable. However, if each customer operates their own AI infrastructure, making high-volume data requests every few minutes, this becomes a problem. It is likely that part of the consumption-based pricing charged by tool providers is not solely due to our use of their tools, but also to our agents processing our data. That’s yet another reason why a centralized orchestration layer makes sense: It can optimize data access and doesn’t depend on a vendor’s AI to be cost-efficient.

A smart strategy for now might be to pursue a dual-track approach: Use the agents bundled with your software for now for a few quick wins. But in parallel, start building a cross-cutting AI orchestration structure, which you will need anyway for the bigger AI projects when entire processes are agentified. And soon, that more general AI will be capable of handling most specialist tasks. By [observing usage data](https://thenewstack.io/going-for-silver-making-the-most-of-tiered-observability/), it should become clear which specialist AIs are still in use, and where, as with Google in the past, the generalist agent becomes the go-to solution.

Unlike us humans, agents have no problem cramming in more knowledge. They don’t get tired of absorbing, processing, and using new information. And most importantly, they forget nothing.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/09/fc7288ec-cropped-c08b8370-michael-berthold-headshot.webp)

Michael Berthold is a German computer scientist, entrepreneur, academic and author. He is a co-founder of KNIME, and has acted as CEO since 2017. Berthold has authored over 250 publications while focusing his research on the usage of machine learning...

Read more from Michael Berthold](https://thenewstack.io/author/michael-berthold/)