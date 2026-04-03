Postgres开源对象关系数据库系统可追溯到大约三十年前，但它并非遗物。

其可扩展性、数据完整性以及复杂查询的性能（以及其向PostgreSQL的演变）意味着它至今仍在。现在，为迎接AI时代，pgEdge在周四[宣布](https://www.pgedge.com/blog/pgedge-mcp-server-for-postgres-is-now-ga-here-s-why-that-matters)推出适用于Postgres的MCP服务器。

这项新服务被描述为一款生产就绪的[MCP服务器](https://thenewstack.io/10-mcp-servers-for-frontend-developers/)，适用于在AI模型与本地或远程数据之间有连接需求的开发人员构建智能AI应用程序。

## 数据库无关性，信不信由你

pgEdge MCP Server for Postgres旨在通过数据源无关性脱颖而出，它可与运行任何标准Postgres版本的新旧数据库配合使用，这实际上意味着版本14（于2021年末推出，具有高并发工作负载能力）及更高版本。该服务拥有灵活的部署选项，包括本地部署、自管理云以及通过[pgEdge Cloud](https://www.pgedge.com/products/pgedge-cloud)提供的托管云。

> 如果没有MCP服务器提供的预定义工具，LLM和代理很容易“幻觉”出API调用和参数，或者使用不正确或过时的API版本。

它甚至可以在[气隙环境](https://thenewstack.io/deploying-ai-in-air-gapped-environments-what-it-really-takes/)中运行，例如战舰、核电站、一些研究实验室和银行金库。那么，pgEdge MCP服务器能做什么，但为什么开发人员应该真正接受这一技术主张呢？

> “我们认为开发人员会觉得最引人注目的功能是内置安全性、完整模式自省和减少的令牌使用量。”

pgEdge联合创始人兼首席产品官Phillip Merrick认为他可以在这里同时提供诱人的概念和实际的价值。

“我们认为开发人员会发现最引人注目的功能是内置安全性、完整模式自省和减少的令牌使用量，”Merrick告诉《The New Stack》。“安全功能包括支持HTTPS和TLS、基于用户和令牌的身份验证以及可切换的读写访问权限，默认为[只读](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/readonly)。”

“完整模式自省意味着LLM不仅可以访问表和列，还可以访问主键、外键、索引、列类型和约束。考虑到令牌是有限的资源，开发人员会赞赏pgEdge MCP服务器为显著减少令牌使用而采用的优化。”

pgEdge MCP Server for Postgres可与Claude Code、Cursor、Windsurf和VS Code Copilot等AI应用程序构建器和代码生成器配合使用。它支持OpenAI和Anthropic的前沿模型，以及使用Ollama、LM Studio和其他OpenAI API兼容产品进行本地托管的模型。

## API的基础知识能胜过MCP吗？

但撇开MCP的喧嚣，我们难道不能像往常一样使用SQL查询，或者（如果真的需要现代化）通过开发工具访问API连接来完成工作吗？

Merrick说：“通常，开发人员及其相应的开发工具和代理更倾向于使用MCP服务器而非API来正确有效地访问底层功能或资源。如果没有MCP服务器提供的预定义工具，LLM和代理很容易‘幻觉’出API调用和参数，或者使用不正确或过时的API版本。在此过程中，它们还可能消耗比所需更多的令牌。”

他说，对于Postgres，通常意义上没有API；相反，替代方案是调用[psql命令行工具](https://hasura.io/blog/top-psql-commands-and-flags-you-need-to-know-postgresql)直接运行SQL查询。他断言，上述担忧也适用于此，特别是关于过多的令牌使用，但额外的担忧包括MCP服务器缺乏防护措施，例如默认使用只读模式。

## 完整模式自省

就其分析所使用信息库的能力而言，该公司的MCP服务器检索有关数据库结构的详细信息，而不仅仅是列出表和列名。这意味着它获取有关主键（每个数据记录的唯一标识符）、外键、索引、列类型和约束的信息。反过来，这允许LLM“推断数据模型”，而不是盲目地查询它。

Merrick告诉我们：“通过提供对完整模式的访问，LLM可以理解数据项之间的关系。这使得它能够生成正确且性能更高的应用程序代码和SQL。此信息还允许LLM建议对模式进行优化，尤其因为pgEdge MCP服务器还提供对数据库统计信息的访问。”

此外，此次GA版本增加了自定义工具，可以使用SQL、Python、Perl或JavaScript编写。还有一个数据库管理员工具包，其中包含用于分析数据库健康状况、识别消耗资源最多的查询以及提出索引建议的预定义工具。

## 令牌、制表符与优化

关于开发人员在从JSON切换到制表符分隔值（TSV）使用时应期望的实际令牌减少情况，Merrick解释说，使用TSV而不是JSON的优化是LLM和pgEdge MCP服务器内部的。

他总结道：“结合我们其他的令牌使用优化，特别是结果分页和上下文窗口压缩，它可以使令牌使用量减少30%到50%。”

与其他pgEdge Postgres产品一样，pgEdge MCP Server for Postgres通过Postgres[许可证](http://license.it/)完全开源。它由pgEdge的Postgres贡献者和开发人员团队全面支持。pgEdge MCP Server for Postgres可供所有Postgres用户免费下载，现在也已在[pgEdge Cloud](https://app.pgedge.com/)托管服务中提供。