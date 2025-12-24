<!--
title: Agent UI标准激增：MCP应用与谷歌A2UI双雄争霸
cover: https://cdn.thenewstack.io/media/2025/12/7ceb19d6-getty-images-xqhgs70jpse-unsplashb.jpg
summary: 谷歌推出A2UI，采用“原生优先”方法，实现跨平台AI代理UI，与OpenAI和Anthropic的基于网络iframe的方法不同。现有两种主要代理UI策略。
-->

谷歌推出A2UI，采用“原生优先”方法，实现跨平台AI代理UI，与OpenAI和Anthropic的基于网络iframe的方法不同。现有两种主要代理UI策略。

> 译自：[Agent UI Standards Multiply: MCP Apps and Google’s A2UI](https://thenewstack.io/agent-ui-standards-multiply-mcp-apps-and-googles-a2ui/)
> 
> 作者：Richard MacManus

本周，[谷歌](https://cloud.google.com/?utm_content=inline+mention) [推出了 A2UI](https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/)，这是一个开源项目，旨在帮助开发者构建“代理用户界面”。这是构建 [AI 代理](https://thenewstack.io/web-development-in-2025-ais-react-bias-vs-native-web/)和聊天机器人中用户界面的新标准和协议定期发布周期中的最新成果。

首先是 [MCP-UI](https://thenewstack.io/mcp-ui-creators-on-why-ai-agents-need-rich-user-interfaces/)，这是一个模型上下文协议 (MCP) 生态系统项目，与 Anthropic 紧密结合，并被 [Shopify](https://thenewstack.io/how-mcp-ui-powers-shopifys-new-commerce-widgets-in-agents/)（以及其他公司）使用。不久之后，[OpenAI 推出了 Apps SDK](https://thenewstack.io/openai-launches-apps-sdk-for-chatgpt-a-new-app-platform/)，以及 AgentKit 和其他 UI 工具。接着，就在上个月，[MCP Apps 发布](https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/)——这是一个拟议的开放标准，“用于模型上下文协议中的交互式用户界面”，目前由 Anthropic 和 OpenAI 共同支持。

## 什么是 A2UI？一种跨平台、原生优先的方法

那么，Google 凭借 A2UI 带来了什么，是其他众多代理 UI 项目尚未具备的？在发布博客文章中，Google 表示：“A2UI 旨在解决代理生成可互操作、跨平台、生成式或基于模板的 UI 响应的具体挑战。”

“跨平台”这个术语是一个重要线索——这并非以网络为中心的方法，而 MCP-UI 和 OpenAI 到目前为止主要依靠沙盒 iframes 采取了这种方法。相反，A2UI 采取了 [谷歌的 Minko Gechev 所称的](https://www.linkedin.com/posts/mgechev_introducing-a2ui-an-open-project-for-agent-driven-activity-7406409944146554882-c_sq?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAAJc5gB1iiLngl5c8J7iqyPa5uC2oX1J-U)“原生优先”方法。Gechev 将其描述为“声明式，而非可执行”，并补充说 AI 代理“发送 UI 组件的描述，而不是代码”。

目前，A2UI 拥有 Flutter、Web Components 和 Angular 的客户端库。但随着时间的推移，这可能会扩展到其他库。其理念是，代理声明它在接收应用（例如聊天机器人）上应呈现的样子，然后将使用原生库生成用户界面。正如 A2UI 发布帖子所解释的：

“A2UI 将 UI 结构与 UI 实现分离。代理发送组件树及其关联数据模型的描述。您的客户端应用程序负责将这些抽象描述映射到其原生小部件——无论是 Web 组件、Flutter 小部件、React 组件、SwiftUI 视图还是完全不同的东西。”

Gechev 还解释说 A2UI 是为流式传输而构建的。他写道：“A2UI 使用基于 JSONL 的格式，实现渐进式渲染，因此用户可以在代理‘思考’时立即看到结果。”

## 理解 OpenAI 的以网络为中心的 UI 策略

在“代理开发”这一新兴领域，正在进行一些定位上的争夺。特别是 OpenAI，它涉足多个领域（此处可联想到关于六指 AI 生成图片的笑话）。

目前，OpenAI 将大部分精力投入到将 ChatGPT 打造为应用平台，其中应用程序将是在沙盒表面（通常是 iframes）中渲染的网络小部件。就在本周，OpenAI 宣布开发者现在可以 [将应用程序提交到 ChatGPT](https://openai.com/index/developers-can-now-submit-apps-to-chatgpt/)。

然而，OpenAI 最近也凭借 Atlas [进入了网络浏览器市场](https://webtechnology.news/a-new-web-browser-from-openai-initial-reactions-to-atlas/)。它也可能在某个时候进入智能手机业务——或其他硬件设备。本月早些时候，我采访了 TELUS Digital 的工程总监 [Adam Shea](https://www.linkedin.com/in/adam-shea-a1850484/)，[他告诉我](https://thenewstack.io/why-capability-driven-protocols-are-key-for-chatgpt-apps/)：“我有一种预感，我们今天构建 ChatGPT 应用程序的方式与 OpenAI 未来可能推出的传闻中的智能手机平台共享一些核心思想和结构。”

尽管 OpenAI 似乎全面兼顾，但它专注于其 Apps SDK 和（显然）Atlas 中的网络技术。这使得它的方法与 Google 不同，后者正凭借 A2UI 追求跨平台覆盖。

## MCP Apps 与 A2UI：关键差异解析

值得注意的是，OpenAI 是 [MCP Apps](https://github.com/modelcontextprotocol/ext-apps?tab=readme-ov-file#readme) 项目的贡献者，该项目源自 MCP-UI 项目（由 Ido Salomon 和 Liad Yosef 创建，他们现在都在 Monday.com 工作）和 OpenAI 的 Apps SDK。诞生 MCP 的公司 Anthropic 也深度参与了该项目。

MCP Apps 扩展 (SEP-1865)，这是它的全称，[上个月在 MCP 官方博客上发布](https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/)。它旨在“标准化模型上下文协议中对交互式用户界面的支持”。

目前，MCP Apps 采用明确基于网络的方法，使用 MCP-UI 和 Apps SDK 都支持的 iframe 沙盒。正如发布帖子所说，“所有 UI 内容都在具有受限权限的沙盒 iframes 中运行。”

在其 A2UI 发布帖子中，Google 强调其“原生优先”方法与 MCP Apps 不同。它解释道：“A2UI 代理发送的是原生组件的蓝图，而不是检索要在沙盒中显示的不透明负载。”这里的关键点是，通过 A2UI 发送的“蓝图”可以用于生成网络代码、原生移动 UI 或桌面应用程序组件。

## 新兴的代理开发框架

今年发布了许多不同的组件，以帮助开发者构建代理或将其应用程序连接到代理。Google 在其 A2UI 发布帖子中暗示了这一点，指出除了构建 UI 外，“您还可以利用一个框架（AG UI、Vercel AI SDK、用于 Flutter 的 GenUI SDK，后者已在底层使用 A2UI）来处理‘管道’。”

除了大量的缩写词之外，有时谁制造了什么也令人困惑。[AG UI](https://www.copilotkit.ai/ag-ui)（代理-用户交互），原来是来自一家名为 [CopilotKit](https://www.copilotkit.ai/) 的西雅图公司的交互协议——该公司提供实现 AG UI 的工具。它现在也支持 A2UI。

我甚至还没有提到谷歌的代理间协议 (A2A)！A2A 在代理间协调层运行，而非 UI 层。

关键是，开发者目前必须深入研究许多不同的技术，才能弄清楚如何构建和连接代理。希望在 2026 年，这一切都会变得更清晰。

但至少对于 UI 而言，现在有两种相当明确的方法：构建一个迷你网络应用（OpenAI 和 Anthropic 偏爱，现在由 MCP Apps 支持）或者采用谷歌 A2UI 的“原生优先”方法。