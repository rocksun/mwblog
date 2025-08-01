
<!--
title: MCP-UI：用AI代理用户界面颠覆传统网站
cover: https://cdn.thenewstack.io/media/2025/07/32d2abfe-museum-of-new-zealand-te-papa-tongarewa-zzd_eou_knu-unsplashb.jpg
summary: 文章介绍了 MCP-UI 项目，该项目旨在为 AI 代理创建交互式 UI 组件，使 AI 代理能够更好地向用户呈现界面。该项目由 Liad Yosef 和 Ido Salomon 创建，并与 MCP 社区工作组相关联。尽管对 AI 技术对 Web 的影响感到担忧，但 Web 技术仍然是互联网 AI 未来的核心。
-->

文章介绍了 MCP-UI 项目，该项目旨在为 AI 代理创建交互式 UI 组件，使 AI 代理能够更好地向用户呈现界面。该项目由 Liad Yosef 和 Ido Salomon 创建，并与 MCP 社区工作组相关联。尽管对 AI 技术对 Web 的影响感到担忧，但 Web 技术仍然是互联网 AI 未来的核心。

> 译自：[MCP-UI Aims To Replace ‘Old World’ Websites With AI Agent UIs](https://thenewstack.io/mcp-ui-aims-to-replace-old-world-websites-with-ai-agent-uis/)
> 
> 作者：Richard MacManus

AI 代理和[模型上下文协议](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (MCP) 的支持者们，越来越将网页和网站视为“[旧世界的用户界面](https://x.com/liadyosef/status/1949482482123817041)”。本周，在微软的 MCP 开发者日上，Kent C. Dodd 在题为“[用户交互的未来](https://www.youtube.com/watch?v=gDSIxIGYk-o)”的演讲中甚至表示，“我们正在进入一个新阶段，我们将拥有 Jarvis 客户端 [指 AI 代理] 和 MCP 服务器，而不是 Web 浏览器和网站。”

需要明确的是，这并不是说 Web 技术本身会消失。目前的想法是：AI 代理将继续使用 Web 作为最终用户的界面层。但是，我们将使用 [基于聊天的新的 AI 浏览器](https://thenewstack.io/ai-browsers-dias-chat-based-ui-and-the-future-of-the-web/)（目前由 OpenAI 和 Perplexity 等公司开发）或其他编程方法，将 UI 注入到 AI 代理进程中，而不是使用“旧世界”的网站。这就是名为 MCP-UI 的项目发挥作用的地方。

[MCP-UI](https://mcpui.dev/) 允许开发人员为 MCP 创建交互式 UI 组件。[该项目](https://mcpui.dev/guide/introduction)“旨在标准化模型和工具如何在客户端应用程序中请求显示富 HTML 界面。” 这样说来，它与 iOS 和 Android 等智能手机平台允许开发人员在应用程序中创建 [WebView](https://en.wikipedia.org/wiki/WebView) 类似。

> MCP-UI：“为你的 MCP 应用程序提供丰富、动态的用户界面”

更具体地说，MCP-UI 能够实现“为你的 MCP 应用程序提供丰富、动态的用户界面”。到目前为止，它提供了 TypeScript 和 Ruby 的 SDK。

该项目仍然很新并且是实验性的，但其背后的理念与 [MCP 迅速普及](https://thenewstack.io/google-embraces-mcp/) 的趋势非常吻合，MCP 现在是 AI 模型收集外部信息的默认方式。[MCP-UI 项目声明](https://mcpui.dev/guide/introduction)：“允许 MCP 服务器响应 UI 片段是创建主机交互体验的强大方式。”

在本周微软的 MCP 活动中，Kent Dodd 重点介绍了 MCP-UI（这也是我第一次接触该项目的方式）。Dodd 展示了一个电子商务演示，其中 MCP-UI 用于在 VS Code 内部显示用户界面。

[![MCP-UI](https://cdn.thenewstack.io/media/2025/07/9abf9ce1-mcp-ui-kentdodds.jpg)](https://cdn.thenewstack.io/media/2025/07/9abf9ce1-mcp-ui-kentdodds.jpg)

*Kent Dodd 展示 MCP-UI 的实际应用。*

Dodd 说：“这就是用户交互的未来。你不再拥有用户直接访问的网站，或者类似的东西。现在我们仍然会与 UI 进行交互，但它将存在于我们的 AI 代理的上下文中，这将为我们解决这些问题。我就是喜欢这样。”

## 更多关于 MCP-UI 项目的信息

MCP-UI 由两位以色列开发人员 [Liad Yosef](https://www.linkedin.com/in/liadyosef/) 和 [Ido Salomon](https://www.linkedin.com/in/ido-salomon/) 创建，他们本周刚刚被企业 IT 公司 Monday.com 以“每人几百万美元”的价格 [招募](https://www.calcalistech.com/ctechnews/article/rjorfh8wel)，这再次表明了顶级 AI 人才市场的异常火热。在撰写本文时，Yosef 仍然在 LinkedIn 上将自己列为 Shopify 的高级软件工程师，而 Saloman 将自己列为 Palo Alto Networks 的云架构师。

MCP-UI 是一个开源项目，根据 GitHub 项目页面，它具有 Apache-2.0 许可证，因此它似乎不是 Monday.com 交易的一部分。但是，看看它是否会因为两位创建者在同一家公司工作而变得更加公司化，这将是一件有趣的事情。

那么 MCP-UI 来自哪里呢？它似乎源于一个名为 [MCP 社区工作组](https://modelcontextprotocol-community.github.io/working-groups/index.html) 的社区项目。[领导该工作组的](https://github.com/orgs/modelcontextprotocol-community/people) Ola Hungerford 和 Tadas Antanavicius 都是 [官方 MCP 项目的维护者](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/MAINTAINERS.md)。因此，与 Anthropic 创建的主要 MCP 项目存在联系。

[![MCP-UI demo](https://cdn.thenewstack.io/media/2025/07/3cf7bfe7-mcp-ui-demo.jpg)](https://cdn.thenewstack.io/media/2025/07/3cf7bfe7-mcp-ui-demo.jpg)

*MCP-UI 演示了将 UI 插入到 Claude 3.7 Sonnet 聊天中。*

我在本文开头提到的“旧世界的用户界面”评论来自 Liad Yosef。为了对他 100% 公平，以下是上下文中的完整引用（双关语）：

*“在短期内，我们将看到越来越多的工具，如 NLWeb、浏览器渲染和浏览器代理，它们将尝试自动化使用“旧世界”的 UI，这些 UI 最初是为人类设计的。这是有道理的，因为它立即弥合了 AI 能力和现有 UI 之间的差距。对于未来，明智的赌注是将这种流程反过来——将这些服务转变为 MCP 优先、LLM 可消费的，并在此基础上构建一个非常精简的人类 UI。以这种“反向”方式快速展示自己的服务将受益于即时且出色的代理兼容性，同时仍然满足（逐渐减少的）人类访问者的流量。”*

顺便说一句，NLWeb 是微软在 [5 月份宣布](https://news.microsoft.com/source/features/company-news/introducing-nlweb-bringing-conversational-interfaces-directly-to-the-web/) 的一个项目，旨在“成为将你的网站有效地转变为 AI 应用程序的最快和最简单的方法，允许用户直接使用自然语言查询网站的内容，就像使用 AI 助手或 Copilot 一样。”

现在，当我第一次阅读 Yosef 的这条推文时，我对这种明显无视以人为中心的 Web 的做法感到畏缩。不幸的是，这在 X（以前的 Twitter）上是一种常见的观点，那里的 AI 炒作盛行。但是经过更多考虑后，我确实赞同 Yosef 的观点，即 AI 代理需要一种更好的方式向最终用户（我们人类）呈现用户界面。

Google Chrome 高级工程师 Paul Kinlan 在他最近关于此主题的博客文章中提出了类似的观点。在一篇关于“超级应用程序”的文章中，[Kinlan 提出](https://aifoc.us/super-apps/)，在不久的将来，你可以从 LLM 或聊天机器人的提示中获得动态生成的用户界面。他说，Web 技术最适合为这些新的用户界面提供动力：“HTML、CSS 和 JavaScript 是当今可用的最具有表现力的语言，可以渲染 UI，而 LLM 现在非常擅长生成它们……”

## 用户界面即将来到你附近的代理

AI 代理浏览 Web 作为其信息收集过程的一部分已经很常见；所谓的 [无头浏览器](https://thenewstack.io/why-headless-browsers-are-a-key-technology-for-ai-agents/)（如 Browserbase）用于此目的。根据我作为 OpenAI 用户的经验，你实际上可以观察到它的 o3 模型在后台浏览网站时“思考”——在你等待结果时，网站域名会闪烁。

[![OpenAI searching the web](https://cdn.thenewstack.io/media/2025/07/cd539bc4-openai-o3-searchweb.jpg)](https://cdn.thenewstack.io/media/2025/07/cd539bc4-openai-o3-searchweb.jpg)

*OpenAI 正在搜索 Web。*

但是，将自定义 Web UI 生成为 AI 代理向你的 **输出** 的一部分是一个相对较新的领域，社区正在探索它。我同意 Dodd 的观点，即 MCP-UI 在这方面是一个令人兴奋的项目，值得追踪。

虽然我非常担心 [AI 技术正在对人类 Web 产生的影响](https://thenewstack.io/is-ai-the-ultimate-version-of-google-as-larry-page-wanted/)（基本上是在破坏它），但我至少可以放心，Web 技术仍然是互联网 AI 未来的核心组成部分。