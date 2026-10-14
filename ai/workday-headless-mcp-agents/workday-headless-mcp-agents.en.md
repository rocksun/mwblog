Workday is opening up its platform and allowing developers to build their own HR and finance agents in Claude Code, Cursor, and other tools, as long as those agents follow the same rules as the people using them.

On Tuesday, at its Workday Rising conference in Las Vegas, the company made its Trusted Agent Platform “headless.”

With this, its [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server, SQL access to live Workday data, and a shared runtime for agents are now generally available, and customers can run their own agents on models from Anthropic, Google, Meta, Mistral, Nvidia, and OpenAI.

As Workday CTO Gabe Monroy noted in a press briefing ahead of the event, “No matter who builds the agent, it runs under Workday permissions, approvals and audit trail — no agent gets a side door.”

Workday notes that many companies currently connect their agents to HR and finance data through copies in a data lake or through service accounts, but, the company argues, those approaches bypass those access controls (though companies like [SAP](https://thenewstack.io/sap-acquires-techwolf-skills/), Microsoft, and others would surely argue that they, too, have access control in place).

For AI developers, the main entry point to the Workday ecosystem is Agent-Ready Tools. That’s the company’s MCP server, which ships as part of Workday Extend AI. Users sign in with their own Workday credentials, and Workday says an agent acting for them can’t reach anything their own account can’t. That’s a key feature here, that ties an agent directly to a user’s account.

Monroy said the server currently offers 275 read tools and 54 tools that write or delete data.

Live Data Query, part of Workday Data Cloud, lets BI tools and agents run SQL queries directly against Workday’s data. Monroy described it as JDBC access to Workday’s object graph, and the company says each query returns only what the requesting user is cleared to see.

Three more components are generally available today. Agent Harness is the shared runtime that Workday’s own agents and those built by customers and partners run on. It passes each agent the user’s identity, org position, and access rights, limits what the agent can do, and picks which model handles each task based on cost and performance. Developer Agent generates Workday agents and apps from a natural-language prompt in Claude Code, Codex, Cursor, or the Workday Developer Site. Custom Agents lets teams deploy agents they built with LangChain or Google’s Agent Development Kit (ADK) onto Agent Harness, though ADK support is limited to design partners for now.

Two more pieces are on the roadmap for early access in early 2027. Agent Context Service will preload only the Workday data a task calls for, which Workday says speeds agents up and limits their exposure to sensitive records. Grounded Reasoning will check a planned action against the customer’s policies, process rules, and Workday records before the agent carries it out.

Workday says customers have built more than 500 agents and more than 6,000 apps with Developer Agent and Agent-Ready Tools in the past four months.

## “Headless, the lawless way”

In the briefing, Monroy demoed what he called “headless, the lawless way.” An agent connected to a custom MCP server — a setup he said Workday commonly sees among its customers today — returned job requisitions its user had no business seeing and then moved the wrong employee between teams with no approval. When pointed at a copy of Workday data in Snowflake, the same agent produced the CTO’s salary when asked.

“When it fails, it isn’t just a wrong answer,” Monroy said, “it’s a wrong action that nobody approved.”

When the agent went through Workday’s own MCP server and Data Cloud instead, with the user signed in, the same queries unsurprisingly returned only the requisitions that user was allowed to see (it wouldn’t have been much of a demo of those access controls otherwise, of course).

## “A small set of use cases”

Asked whether headless matters as much to Workday as it does to Salesforce, Gerrit Kazmaier, Workday’s president of product and technology, said that Workday is giving customers a choice: “I’d always prefer if they use our user interface, but headless will be equally good.”

Kazmaier noted that building agents directly on Workday’s tools and APIs is “only possible for a small set of use cases where you don’t need to have HR or finance domain logic.” For everything else, he pointed to an AI-to-AI integration in which Claude hands requests to Sana, Workday’s agent orchestrator, which then calls Workday’s own domain agents.

## Lakes for analytics, not for agents

It’s worth noting that the Snowflake example is a bit of an awkward one for Workday. When the company [announced Data Cloud](https://newsroom.workday.com/2025-09-16-Workday-Introduces-Workday-Data-Cloud-to-Unlock-the-Power-of-People-and-Money-Data-and-Accelerate-AI-Powered-Innovation) in September 2025, the pitch included zero-copy sharing of Workday data with Databricks, Salesforce, and Snowflake. Snowflake made its Workday Data Cloud integration [generally available](https://docs.snowflake.com/en/release-notes/2026/other/2026-10-07-workday-data-cloud-zerocopy-ga) on Oct. 7, and Databricks put its [Workday connector for Unity Catalog](https://www.databricks.com/blog/announcing-workday-data-connect-federation-unity-catalog) into public beta a day later.

According to Databricks, a Workday admin sets up the connector by registering an Integration System User (ISU), the kind of system account Workday customers use for traditional integrations, with read access to the shared tables. After that, Unity Catalog permissions at the catalog, schema, and table level decide who can query the data.

Monroy said data lakes still make sense for analytics and for joining Workday data with the rest of a company’s data, but that an external lake is “the wrong place to build agents” that need governed access to Workday.

“You can export your data, but you can’t export the rules that govern the data,” he said, adding that rebuilding those rules in the lake means “maintaining a second copy” of Workday’s security model, “and the day it drifts, it’s all wrong.”

## Everybody is losing their heads

Headless is the way to go right now, it seems. Salesforce, ServiceNow, and Microsoft, for example, already let outside agents into their systems of record. Salesforce [launched Headless 360](https://www.theregister.com/saas/2026/05/28/salesforce-waves-bye-bye-to-ui-in-headless-embrace/5247587) at its TDX developer conference in April, so agents in Claude, ChatGPT, Cursor, or a terminal can work with Salesforce data. ServiceNow made its [Action Fabric MCP server](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise/default.aspx) generally available in May, with Anthropic as a launch partner, and Microsoft offers an [MCP server for Dynamics 365 ERP](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp).

All four vendors say outside agents stay within their existing [permission models](https://thenewstack.io/mcp-ai-agents-api/).

## Whose identity does the agent use?

When it comes to [agent identity](https://thenewstack.io/mcp-security-permissions-overhaul/), different vendors are currently taking very different approaches.

Salesforce, for example, is preparing to have agents that connect over MCP or its APIs register with their own credentials and permissions instead of acting under a user’s identity, [according to Salesforce Ben](https://www.salesforceben.com/salesforce-will-charge-flex-credits-for-agentic-mcp-and-api-calls/). MCP clients will eventually need to switch to OAuth credentials tied to those agent identities.

Workday’s [documentation](https://doc.workday.com/admin-guide/en-us/workday-ai/agents/agent-system-of-record/agent-security-and-compliance/faq--agent-security.html) says its agents can already get up to two system accounts of their own, called Agent System Users (ASUs), one for acting on a user’s behalf and one for “ambient” work, each with its own [OAuth 2.0 client](https://thenewstack.io/descope-brings-oauth-to-ai-agents-and-mcp-servers/). Workday creates the ambient account automatically when a customer turns on an ambient skill.

Unified.to, which sells a Workday MCP integration, says every Workday MCP path, “official or not,” [starts with creating an ISU](https://unified.to/blog/how_to_get_started_with_a_workday_mcp_server). Cequence’s [setup guide](https://docs.aigateway.cequence.ai/docs/applications/hr-operations/workday-hcm/) for its Workday MCP integration asks customers to create one “with appropriate security groups.” An agent working through an ISU sees whatever those security groups allow, no matter who is prompting it.

The more telling signal may be Kazmaier’s caveat. If building directly on the MCP server only works for a small set of use cases, the version of headless Workday expects most customers to use is Claude talking to Sana talking to Workday’s own agents, with Workday’s runtime in the middle of every call.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)