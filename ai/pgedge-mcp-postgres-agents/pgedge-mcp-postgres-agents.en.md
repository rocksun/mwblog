The Postgres open-source object-relational database system can trace its history back to some three decades, but it’s no artifact.

Its extensibility, data integrity, and performance for complex queries (along with its evolution to PostgreSQL) mean it’s still around today. Now ready to evolve for the AI era, pgEdge [announced](https://www.pgedge.com/blog/pgedge-mcp-server-for-postgres-is-now-ga-here-s-why-that-matters) on Thursday that it offers MCP Server for Postgres.

The new service is described as a production-ready [MCP server for developers](https://thenewstack.io/10-mcp-servers-for-frontend-developers/) building agentic AI applications in environments with connectivity requirements between AI models and local or remote data.

## Database agnosticism, believe it

Aiming to differentiate itself through data-source agnosticism, pgEdge MCP Server for Postgres works with new and existing databases running any standard version of Postgres, which, in practical terms, means version 14 (which arrived in late 2021 with its high-concurrency workload capabilities) and newer. The service boasts flexible deployment options, including on-premises, self-managed cloud, and managed cloud via [pgEdge Cloud](https://www.pgedge.com/products/pgedge-cloud).

> Without the predefined tools supplied by MCP servers, LLMs and agents are prone to hallucinating API calls and parameters or using incorrect or outdated versions of the API.

It even works in [air-gapped](https://thenewstack.io/deploying-ai-in-air-gapped-environments-what-it-really-takes/) [environments](https://thenewstack.io/deploying-ai-in-air-gapped-environments-what-it-really-takes/) such as battleships, nuclear power plants, some research labs, and bank vaults. So that’s what the pgEdge MCP server does, but why should developers actually be sold on this whole technology proposition?

> “The features we think developers will find most compelling are built-in security, full schema introspection, and reduced token usage.”

Phillip Merrick, co-founder and chief product officer at pgEdge, thinks he can sell us both the sizzle and the sausage here.

“The features we think developers will find most compelling are built-in security, full schema introspection, and reduced token usage,” Merrick tells *The New Stack*. “Security features include support for HTTPS and TLS, user- and token-based authentication, and switchable read-write access, with the default [read-only](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/readonly).

“Full schema introspection means the LLM has access not just to the tables and columns, but also to primary keys, foreign keys, indexes, column types, and constraints. Given that tokens are a rationed resource, developers will appreciate the optimizations employed by the pgEdge MCP server to significantly reduce token usage.”

The pgEdge MCP Server for Postgres works with AI application builders and code generators such as Claude Code, Cursor, Windsurf, and VS Code Copilot. It supports frontier models from OpenAI and Anthropic, as well as locally hosted models using Ollama, LM Studio, and other OpenAI API-compatible products.

## Does the ABC of API beat MCP?

But away from the hullabaloo of MCP, can’t we just do things the way we’ve always done them with SQL queries, or (if we really have to modernize) by using developer tools to access an API connection?

“In general, it is preferable that developers themselves and their corresponding developer tools and agents utilize an MCP server versus an API to access the underlying capabilities or resources in a correct and efficient fashion. Without the predefined tools provided by MCP servers, LLMs and agents are prone to hallucinating API calls and parameters, or to using incorrect or outdated versions of the API. They can also end up consuming more tokens than might be necessary in the process,” Merrick says.

With Postgres, he says, there isn’t an API in the usual sense; instead, the alternative is to invoke the [psql command line utility](https://hasura.io/blog/top-psql-commands-and-flags-you-need-to-know-postgresql) to run SQL queries directly. He asserts that the same concerns noted above apply here as well, particularly regarding excessive token usage, but additional concerns include the lack of guardrails imposed by an MCP server, e.g., using read-only mode by default.

## Full schema introspection

In terms of its ability to analyze the information base it works with. The company’s MCP server retrieves detailed information about a database’s structure, beyond simply listing table and column names. So this means it gains information on primary keys (unique identifiers for every data record), foreign keys, indexes, column types, and constraints. This, in turn, allows the LLM to “reason about the data model” it is about to engage with rather than blindly querying it.

“By providing access to the full schema, the LLM can understand the relationships between the data items. This allows it to generate both application code and SQL that is correct and more performant. This information also allows the LLM to suggest optimizations to the schema, particularly since the pgEdge MCP Server also provides access to database stats,” Merrick tells us.

Additionally, this GA release adds custom tools, which can be written in SQL, Python, Perl or JavaScript. There is also a database administrator toolkit with pre-defined tools for analyzing database health, identifying top resource-consuming queries, and making index recommendations.

## Tokens, tabs & optimizations

As an extra note on what real-world token-reduction developers should expect when switching from JSON to tab-separated values (TSV) usage, Merrick explains that the optimization of using TSV over JSON is internal to the LLM and the pgEdge MCP Server.

“In conjunction with our other token usage optimizations, specifically pagination of results and context window compaction, it can result in a reduction between 30% and 50%,” he concludes.

As with other pgEdge Postgres products, the pgEdge MCP Server for Postgres is fully open source via the Postgres [license](http://license.it/). It is fully supported by pgEdge’s team of Postgres contributors and developers. The pgEdge MCP Server for Postgres is available as a free download for all Postgres users and is now also available in the [pgEdge Cloud](https://app.pgedge.com/) managed service.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)