[![Snowflake logo](https://cdn.thenewstack.io/media/2025/10/9918c534-snowflake-300x225.png)](https://cdn.thenewstack.io/media/2025/10/9918c534-snowflake-300x225.png)

Snowflake logo

Data cloud [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) has equipped its Snowflake Cortex AI service with a new [MCP server](https://thenewstack.io/10-mcp-servers-for-frontend-developers/), as well as a set of third-party integrations designed to make it easier for financial services companies to make better use of their data in the Snowflake Cloud.

“We’re making it easy to build trusted AI and extending it to where the users are,” said [Baris Gultekin](https://www.snowflake.com/en/blog/authors/baris-gultekin/), Snowflake VP of AI, in an interview with TNS.

Customer service, investment analytics, and claims management could all be streamlined with the use of these services.

## Snowflake’s MCP Server

The Snowflake MCP Server, a managed service now in preview, allows Snowflake users to connect to not only their own data but third-party data such as market analysis, expert research, business content, and news, from partners such as Nasdaq and The Associated Press. Snowflake users can then feed this data into AI apps and agent platforms — from the likes of [Anthropic](https://thenewstack.io/anthropic-launches-claude-sonnet-4-5/),  [Cursor](https://thenewstack.io/install-cursor-and-learn-programming-with-ai-help/), and Salesforce’s Agentforce — for heretofore unrealized benefits.

MCP is based on a server-client architecture. The clients are embedded in AI applications. The server exposes a set of tools, or executable functions such as querying a database, that the clients can use.

Based on the [MCP specification](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/), Snowflake’s MCP Server is a service managed by Snowflake, allowing users to create their own MCP server objects, specifying the tools and metadata in the server configuration. Standard Snowflake [Role-based Access Controls](https://thenewstack.io/three-realistic-approaches-to-kubernetes-rbac/) (RBAC) secure the server object. Snowflake manages the MCP Server itself, ensuring operations stay within the customer’s security and privacy constraints.

[![MCP Primitives](https://cdn.thenewstack.io/media/2025/10/b2ded806-mcp-primitives.png)](https://cdn.thenewstack.io/media/2025/10/b2ded806-mcp-primitives.png) MCP primitives (Snowflake)

MCP clients can connect with the server, after requisite authentication through [OAuth 2.0](https://docs.snowflake.com/en/user-guide/oauth-snowflake-overview), and discover and evoke tools through the standard MCP procedures:

[![Snowflake MCP tool discovery.](https://cdn.thenewstack.io/media/2025/10/43ca2f96-snowflake-mcp-discovery.png)](https://cdn.thenewstack.io/media/2025/10/43ca2f96-snowflake-mcp-discovery.png) MCP tool discovery.

## Cortex AI for Financial Services

Created for Snowflake’s MCP Server, Cortex AI for Financial Services is a set of AI tools that aims to make it easier for financial users to use their own data in agent-based applications, built for both their own customers and by their employees.

In addition to the MCP server accessing the customer’s data, it can also tap into third-party data, both structured and unstructured.

Structured data providers CB Insights, Cotality, Deutsche Börse, MSCI, and Nasdaq eVestment will be accessible via the [Sharing of Semantic Views](https://docs.snowflake.com/en/user-guide/views-semantic/semantic-view-sharing), which will be generally available soon as part of Snowflake’s AI platform, [Cortex](https://thenewstack.io/stack-overflow-on-snowflake-cortex-answers-without-attitude/).

Combining their own data with third-party sources that, when processed through a LLM, can provide information of unique value for the company, Snowflake posits.

[![Snowflake partners](https://cdn.thenewstack.io/media/2025/10/604af955-snowflake-partners.png)](https://cdn.thenewstack.io/media/2025/10/604af955-snowflake-partners.png)

Unstructured data publishers like CB Insights, FactSet, Investopedia, The Associated Press, and The Washington Post will be available through [Cortex Knowledge Extensions.](https://www.snowflake.com/en/blog/easy-button-context-rich-ai-agents/)

## Tap into the Cortex

Users can also bring in other Cortex services: [Snowflake Data Science Agent](https://www.snowflake.com/en/news/press-releases/snowflake-intelligence-and-data-science-agent-deliver-the-next-frontier-of-data-agents-for-enterprise-ai-and-ml/) provides an easy conduit for business analysts to code in their own formulas. [Snowflake Cortex AISQL](https://www.snowflake.com/en/blog/ai-sql-query-language/) can make sense of troves of unstructured documents such as audio and images. [Snowflake Intelligence](https://www.youtube.com/watch?v=va-l7sYp3OA) (now in public preview) can provide a natural language interface for inspecting Snowflake data.

The MCP server connects with [Cortex Analyst](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst) and [Cortex Search](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview) and other Cortex Knowledge Extensions are available through [Snowflake Marketplace](https://www.snowflake.com/en/product/features/marketplace/).

Since all the data is located within Snowflake, all the customary security practices remain intact throughout the entire agentic process.

This setup provides a way for organizations to easily treat and augment their data with third-party services: Claude’s reasoning can be applied to both structured and unstructured documents via Cortex Analyst and Cortex Search.

In software development, Snowflake’s MCP server could give Cursor more contextual data that would help an organization’s programmers create better code.  Likewise, FactSet could be used to manage risk more effectively.

This initial set of third-party tools focuses on the financial sector, which is one of Snowflake’s most popular markets. Tools for other verticals will be forthcoming,  Gultekin said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)