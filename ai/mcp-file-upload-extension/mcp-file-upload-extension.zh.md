![指向上下两侧的箭头，描绘了文件上传和下载的概念。](https://cdn.thenewstack.io/media/2026/11/b857591d-alex-shuper-ehko-zsjnoi-unsplash-1024x576.jpg)

自 Anthropic 大约两年前[推出该项目](https://www.anthropic.com/news/model-context-protocol)以来，[模型上下文协议](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/)（MCP）在连接 AI 助手与外部工具和数据方面一直发挥着重要作用。想让编程智能体检查某个 bug 的状态？通过 MCP 服务器为其授予问题跟踪器的访问权限即可。或者询问助手公司上周发货了多少订单？将其连接到可以查询数据库的工具。

自[去年 12 月加入智能体 AI 基金会](https://thenewstack.io/anthropic-donates-the-mcp-protocol-to-the-agentic-ai-foundation/)以来，MCP 的[发展路线图](https://thenewstack.io/model-context-protocol-roadmap-2026/)反映了在生产环境中运行该协议的需求。例如，维护人员一直在努力简化服务器的部署，无需追踪单个客户端会话，并允许公司通过现有的身份系统管理访问权限。

但开发者们长期以来面临的一个老问题是，如何将文件从 AI 应用传递到 MCP 工具。例如，假设你在聊天中附加了一个 PDF 并要求助手将其保存到云存储中——助手可以调用一个工具来保存文件，但开发者*仍然*必须想方设法将 PDF 从聊天应用传输到该工具。这可能意味着生成一个临时的上传链接，或者可能将用户引导至单独的上传页面。

为了弥补这一差距，MCP 项目的相关人员概述了一份[草案扩展](https://github.com/modelcontextprotocol/experimental-ext-file-uploads/blob/main/specification/draft/file-uploads.md)，为客户端和工具提供了一种处理上传和下载的通用方法。

![MCP 终于开始解决文件上传问题了](https://cdn.thenewstack.io/media/2026/11/688112ca-file-transfer-round-trip.gif)

*MCP 终于开始解决文件上传问题了*

## 为什么 MCP 需要一种传输文件的方法

在周二发布的一篇[博客文章](https://blog.modelcontextprotocol.io/posts/exploring-file-uploads-and-downloads-in-mcp/)中，MCP 首席维护人员兼 Anthropic 技术员工 [Den Del](https://den.dev/about/)[i](https://www.linkedin.com/in/dendeli/)[marsky](https://den.dev/about/) 与 Google 软件工程师 [Wil St. Charles](https://www.linkedin.com/in/wilstcharles/) 阐述了新扩展的理论依据，并指出随着开发者要求智能体利用 MCP 连接的工具做更多事情，他们的需求也发生了变化。

> “由于智能体能力和自主性的不断提高，许多此类 MCP 服务器项目现在需要处理文件。”

“在过去的两年里，人们用该协议构建的东西变得更加雄心勃勃。*远比以前*更有雄心，”他们写道。“由于智能体能力和自主性的不断提高，许多此类 MCP 服务器项目现在需要处理文件。”

几乎自 MCP 诞生以来，这种需求就一直在社区中显现。在 [2024 年 12 月](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/1197)，一名构建文件处理工具的开发者在 GitHub 上询问如何将文件从客户端传送到服务器。Anthropic 的一位团队成员[承认](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/1197#discussioncomment-11450043)了这一难处，并表示他们正在探索工具如何将文件传回 AI 应用。随后，其他社区成员也纷纷献计献策，[其中一人指出他们已经构建](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/1197#discussioncomment-12708679)了自己的方法，用于将文件从 AI 应用发送到 MCP 服务器。他们的 MCP client 在调用工具之前直接将文件上传到服务器，而上传过程本身发生在协议之外。

自那以后，开发者[一直在寻找方法](https://www.reddit.com/r/Anthropic/comments/1o2982x/file_uploads_through_an_mcp_server_anyone_doing/)来绕过这个鸿沟。在几个月前的一个 [Reddit 线程](https://www.reddit.com/r/mcp/comments/1w1jtu9/file_uploads_with_mcp_what_are_people_doing/)中，一位用户表示，一旦启用出站访问，临时的 S3 上传链接就可以在 Claude 中工作，但他们在 ChatGPT 中无法使用相同的方法，因此他们构建了一个单独的 Web 应用和上传页面。另一位开发者[表示他们构建了一个](https://www.reddit.com/r/mcp/comments/1w1jtu9/comment/p6ldrsd/)通往 MCP 应用的拖放界面，这让用户可以自行提交文件，但仍然没有让智能体自主发起上传的方法。

也有打包好的选项。[FastMCP 为](https://gofastmcp.com/docs/apps/providers/file-upload)构建 MCP 应用的开发者提供了一个拖放上传组件，而 Box [最近通过其自己的 MCP 服务器推出了](https://support.box.com/hc/en-us/articles/52446938146067-Upload-and-download-PDFs-PowerPoint-Word-and-Excel-files-via-Box-MCP-server)针对 PDF 和 Office 文档的安全文件上传和下载支持。

就 MCP 项目而言，他们一直在慢慢朝着共同标准迈进。Delimarsky 于 [2025 年 8 月提出了一个探索性的上传提案](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1306)，随后在 [4 月](https://modelcontextprotocol.io/community/working-groups/file-uploads)成立了一个最初由 Anthropic 和 OpenAI 成员组成的文件上传工作组。10 月份，该工作组将[文件下载](https://modelcontextprotocol.io/community/working-groups/file-uploads#changelog)纳入了其职责范围。

现在，一份[草案规范](https://github.com/modelcontextprotocol/experimental-ext-file-uploads/blob/main/specification/draft/file-uploads.md)规定了双向传输是如何工作的。

> “虽然我们已经勾勒出了轮廓，但我们还不确定最初的起点是否就是我们最终的终点。”

“虽然我们已经勾勒出了轮廓，但我们还不确定最初的起点是否就是我们最终的终点，”作者写道。“正如你所猜想的那样，找出答案的最佳方法就是——接受现实的检验。”

## MCP 将如何传输文件

实验性的文件传输扩展建立在 [MCP 于 7 月引入的](https://blog.modelcontextprotocol.io/posts/2026-07-28/)扩展框架基础之上，该框架允许客户端和服务器在不改变核心协议的情况下选择使用新功能。[实验阶段](https://modelcontextprotocol.io/extensions/overview#experimental-extensions)为开发者提供了一个场所，以便在正式的规范增强提案（SEP）之前或与之并行地对想法进行原型设计和完善。

> 无论哪种方式，文件本身都会绕过模型。

在该扩展下，例如，如果你让助手将附加的 PDF 保存到云存储中，模型会调用该工具，并且 MCP client 会处理上传。客户端可以在工具请求中发送小文件，对于较大的文件，客户端会单独上传并再次调用该工具来完成工作。无论哪种方式，文件本身都会绕过模型。

对于下载，例如一个导出 CSV 的工具，在生成完文件后可以包含一个下载 URL。然后客户端可以直接获取该 CSV，并且模型会收到一条消息，告知它该工具生成了什么内容。

其中一个重大的[安全影响](https://github.com/modelcontextprotocol/experimental-ext-file-uploads/blob/main/specification/draft/file-uploads.md#security-implications)集中在主机对文件去向应该拥有*多少*控制权。就目前而言，拟议的扩展限制了客户端何时可以将其 MCP 凭据发送到上传目的地。主机在 MCP 服务器提供该目的地之前会要求用户批准上传，因此用户在批准时可能不知道文件会去往何处。

“这些保障措施控制了客户端的 MCP 凭据的发送位置，但它们本身并不能控制文件的去向，”作者写道。

因此，一个自认为正在将机密 PDF 保存到公司存储中的用户，最终可能会把它发送到一个由恶意服务器运营商控制的端点。作者建议将外部上传限制在经批准的目的地，并正在询问是否应要求主机强制执行该限制。

值得注意的是，开发者今天就可以通过在测试客户端和服务器上实现建议的传输来针对该草案进行原型设计。然而，目前还没有正式的参考实现。

“这是因为我们预计，一旦我们将我们的实验与第三方文件服务（如云存储、数据库导入/导出以及许多其他需要文件输入和输出的服务）进行集成，许多内部工作原理实际上会大不相同，”作者补充道。

MCP 维护人员表示，他们的目标是在年底前发布稳定版本，并且支持将保持可选状态——选择跳过该扩展的开发者无需更改其现有的 MCP 客户端或服务器。

这篇文章最初发布在 [The New Stack](https://thenewstack.io) 上：[开发者们两年来一直在破解 MCP 的文件上传问题。解决方案正在成型。](https://thenewstack.io/mcp-file-upload-extension/)