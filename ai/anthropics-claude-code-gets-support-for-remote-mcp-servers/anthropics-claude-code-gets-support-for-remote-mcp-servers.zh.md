[Claude Code](https://www.anthropic.com/claude-code), Anthropic 的 [AI 编码代理](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/) 自公司三个月前推出 [Claude 4 模型](https://thenewstack.io/anthropic-launches-claude-opus-4-and-sonnet-4/) 以来，其活跃用户群增长了 160%。 今天，它通过支持远程模型上下文协议 (MCP) 服务器来扩展 Claude Code。 这将允许开发者使用来自更广泛服务（如其他开发工具、项目管理服务和知识库）的数据和工具来扩展 Claude Code 的工具链和数据访问。 以前，Claude Code 仅限于使用本地 MCP 服务器，虽然这些服务器也可以连接到外部来源，但 Anthropic 指出，现在这样做容易得多。

要将 Claude Code 与 MCP 服务器集成，开发者只需使用该工具的命令行界面运行一个基本命令，完成 OAuth 身份验证流程，即可开始使用。

新的集成将支持 MCP 服务器，这些服务器返回服务器发送事件 (SSE) 以将其数据流回 Claude Code，以及标准输入/输出 ([STDIO](https://naman1011.medium.com/model-context-protocol-mcp-stdio-vs-sse-a2ac0e34643c))。

Anthropic 的 [Cat Wu](https://www.linkedin.com/in/cat-wu/) 告诉我，公司收到了许多开发者的请求，他们希望更多地自定义 Claude Code。

“我们一直在构建可自定义的 Claude Code，因为我们知道开发者喜欢编写他们的工具、引入他们自己的工具或系统提示。 因此，远程 MCP 只是它的一个自然扩展，我们发现开发者希望 Claude Code 能够访问他们可以访问的更多信息，”Wu 说。

开发者将能够引入任何远程 MCP 服务器，尽管有些服务器显然比其他服务器更有用。 Anthropic 的启动合作伙伴是应用程序监控和错误跟踪服务 Sentry 和 Linear，Linear 是开发团队 [越来越受欢迎的](https://thenewstack.io/anti-agile-project-tracker-linear-the-latest-to-take-on-jira/) 错误跟踪和项目管理工具。

“如果你聘请了一位工程师，然后你说，‘嘿，你不能查看任何通信工具，你不能查看任何工单管理软件，你不能查看错误，你无法验证你的修复是否有效’，那么你不会期望他们工作效率很高。 我们认为这将大大提高使用 Claude Code 的工程师的工作效率，”Wu 说。

Wu 还指出，最新一代的模型在使用工具方面已经变得更好，即使有时它们需要经过几轮试错才能弄清楚给定工具的工作方式（有时，她指出，当它不是主流服务之一时，向 Claude Code 提供一些关于它可以访问的工具的信息会有所帮助）。

有时，MCP 服务器也可能用过多的上下文信息淹没 Claude Code，因此我们可能会在未来看到创新领域之一是 MCP 服务器更智能地了解它们将哪些上下文信息发送给代理。

值得注意的是，一些其他的代理编码工具（如 Cursor 和 Windsurf）也支持 [通过 MCP 使用工具](https://docs.cursor.com/tools)。 在某种程度上，鉴于这些连接存在如此多的潜在用例，这现在正成为基本要求。

在发布时，Claude Code 仅适用于 Anthropic 的 Max 计划（起价为每月 100 美元）的用户，或者选择按需付费方式直接为该工具的 API 使用付费的用户（这可能会很快累积起来）。 几周前，Anthropic 还向其更实惠的每月 20 美元的 Pro 计划的用户开放了对该工具的访问权限，但正如 Wu 指出的那样，这更多的是为了处理周末项目和小型存储库，因为它的使用量限制为每五个小时工作两个小时（当速率限制重置时）。 Pro 计划提供与更昂贵的计划相同的 MCP 支持。