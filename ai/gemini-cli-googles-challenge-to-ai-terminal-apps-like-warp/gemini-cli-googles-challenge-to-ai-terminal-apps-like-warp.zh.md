在我参加谷歌的新闻发布会宣布 [Gemini CLI](https://github.com/google-gemini/gemini-cli)（一个“将 Gemini 的强大功能直接带入您的终端的开源 AI 代理”）的前半个小时，我收看了 Warp 发布的 [2.0 版本产品](https://www.warp.dev/blog/reimagining-coding-agentic-development-environment) 的 YouTube 直播。Warp 是最初的 [以 AI 为中心的终端应用程序](https://thenewstack.io/warp-launches-ai-first-native-terminal-app-for-windows/) 之一，当时正在发布其所谓的“Agentic 开发环境”（是的，是 ADE 而不是 IDE）。

我直接从 Warp 的公告跳到谷歌的新闻发布会，几分钟后，我就在想 Warp 将如何竞争。这是一个创业公司最可怕的噩梦：一个行业巨头带着一个免费的开源产品闯入其市场利基。这是互联网 dot-com 时代微软的翻版吗？

但回到谷歌宣布的内容（我们将在另一篇文章中介绍 Warp 2.0）。Gemini CLI（命令行界面）首先是一个面向开发人员的终端应用程序。但是，与 Warp 一样，其用例比传统的 CLI 广泛得多。谷歌在公告中表示，它将成为“一个通用的本地实用程序，您可以将其用于各种任务，从内容生成和问题解决到深入研究和任务管理”。

[![Gemini CLI in action](https://cdn.thenewstack.io/media/2025/06/d8a71eab-gemini-cli-app.jpg)](https://cdn.thenewstack.io/media/2025/06/d8a71eab-gemini-cli-app.jpg)

Gemini CLI

个人开发者可以免费使用 Gemini CLI（目前处于预览阶段），但有一定的限制，尽管该限制相当高。谷歌声称 Gemini CLI“提供了业界最大的使用配额，即每分钟 60 个模型请求和每天 1,000 个模型请求，且不收取任何费用”。谷歌补充说，您“在此预览期间几乎永远不会达到限制”。

在新闻发布会上，谷歌的 [Ryan J. Salva](https://www.linkedin.com/in/ryanjsalva/) 解释说，慷慨的免费层级是为了让更广泛的用户加入。

Salva 说：“我们相信，这些工具将在未来十年内主导不仅是开发人员，而且是所有类型的创作者的工作方式，我们不希望对这些工具的访问受到你口袋里有多少钱的限制。无论你身无分文还是腰缠万贯，无论你是学生、爱好者、自由职业者还是资金雄厚的公司的开发人员，你都应该可以使用相同的工具。这就是为什么我们从一开始就免费提供 Gemini CLI，并提供真正无与伦比的使用限制。”

作为比较，Warp 也有一个免费层级，但它只提供“每月最多 150 个 AI 请求”。因此，Warp 谈论的是每个*月*，而谷歌能够谈论的是每个*天*。根据我的粗略计算，谷歌每月提供的 AI 请求数量是 Warp 的 200 倍。

[![What Gemini CLI offers](https://cdn.thenewstack.io/media/2025/06/0ef0fe11-gemini-cli-infographic.png)](https://cdn.thenewstack.io/media/2025/06/0ef0fe11-gemini-cli-infographic.png)

Gemini CLI 提供的功能。

毋庸置疑，你不能将 Warp 的资源与谷歌的资源相提并论。但这就是像 Warp 这样的小公司所面临的挑战。

也许更大的威胁是 Gemini CLI 是开源的，采用 Apache 2.0 许可证，并且可扩展。谷歌表示：“我们完全期望（并欢迎！）全球开发者社区为该项目做出贡献。” Gemini CLI 也是可扩展的，并支持模型上下文协议 (MCP)，这是业界 [最热门的 AI 连接标准](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/)。

但就此而言，在新闻发布会上，谷歌工程师 [Taylor Mullen](https://www.linkedin.com/in/ntaylormullen/) 表示，Gemini CLI “没有倾向性，它没有界限”。他将其定位为一个优势，因为开发人员可以根据自己的喜好调整开源软件。但这也可能是 Warp 的一个优势，因为 Warp 绝对是一个有倾向性的产品——2.0 产品在很大程度上倾向于 [agentic 范例](https://thenewstack.io/llama-stack-released-to-help-developers-build-agentic-apps/)。其他终端产品，如 Ghostty，提供了 [其他不同的东西](https://thenewstack.io/warp-vs-ghostty-which-terminal-app-meets-your-dev-needs/)。

为了增加可扩展性和灵活性的主题，Salva 在新闻发布会上澄清说，Gemini CLI 将在各个平台上可用。他说：“它可以在 Windows 上运行，可以在 ChromeOS 上运行，如果你愿意，也可以在云中的容器中运行。”

## 谷歌更广泛的 AI 编码计划

作为一家大公司，谷歌在 AI 开发方面拥有广泛的产品——其同行，如谷歌和亚马逊也是如此。因此，除了作为一个独立的终端应用程序外，Gemini CLI 还在与谷歌的 AI 编码助手 [Gemini Code Assist](https://thenewstack.io/inside-gemini-code-assist-googles-copilot-alternative/) 集成，这是有道理的，“以便所有 Code Assist 开发人员——无论是在免费、标准和企业计划中——都可以在 VS Code 和 Gemini CLI 中获得提示驱动的、AI 优先的编码。”

Google Code Assist 一直是谷歌今年主要的 AI 开发工具。早在 2 月，就发布了 [一个免费版本](https://thenewstack.io/google-ai-coding-tool-now-free-with-90x-copilots-output/)。然后，在 5 月举行的 Google I/O 开发者大会上，该公司宣布了 [该工具的更多 agentic 能力](https://thenewstack.io/inside-gemini-code-assist-googles-copilot-alternative/)。

其理念是，开发人员将能够选择他们更喜欢使用的工具——IDE（Code Assist 集成到 VS Code 中）或终端应用程序（Gemini CLI）——但底层技术将是相同的。

Salva 说：“因此，当你使用 Gemini Code Assist 时，你就可以访问所有相同的工具、所有相同的功能、所有相同的透明度和开源代码，这些都在 Gemini CLI 中。”

[![The modern CLI](https://cdn.thenewstack.io/media/2025/06/ab73b510-gemini-cli-2.jpg)](https://cdn.thenewstack.io/media/2025/06/ab73b510-gemini-cli-2.jpg)

现代 CLI？

## AI 终端将继续存在

在 AI 开发时代，终端应用程序已经变得更像代码编辑器。当然，我们已经在 Warp 中看到了这种演变，即使在其 2.0 发布之前，Warp 的应用程序内部也有很多代码编辑功能。因此，对于谷歌来说，提供一个与 AI 代码辅助工具集成良好的 AI 终端应用程序似乎是一个自然的演变。

Gemini CLI 也是 Jules 的自然步骤，Jules 是谷歌新的 agentic 编码工具，The New Stack 的 David Eastman 最近 [将其与 Anthropic 的 Claude Code 进行了比较](https://thenewstack.io/agentic-coding-how-googles-jules-compares-to-claude-code/)。

终端已经不再是以前的样子了。如果你愿意，你仍然可以使用 Windows Terminal、Linux 终端或 Mac 的本机终端——但像 Warp 和 Gemini CLI 这样更新、更炫的应用程序正在将 AI 带入 CLI。