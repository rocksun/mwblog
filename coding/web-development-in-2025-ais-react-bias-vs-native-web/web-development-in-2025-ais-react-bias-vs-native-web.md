<!--
title: 2025年Web开发：AI力挺React，原生Web何去何从？
cover: https://cdn.thenewstack.io/media/2023/12/88ad96d3-year-wrapup-1.png
summary: 2025年Web开发趋势：原生功能崛起，AI编码助手偏爱React，AI代理集成Web应用，浏览器端Web AI发展，Vite生态壮大，Web开发面临选择。
-->

2025年Web开发趋势：原生功能崛起，AI编码助手偏爱React，AI代理集成Web应用，浏览器端Web AI发展，Vite生态壮大，Web开发面临选择。

> 译自：[Web Development in 2025: AI’s React Bias vs. Native Web](https://thenewstack.io/web-development-in-2025-ais-react-bias-vs-native-web/)
> 
> 作者：Richard MacManus

今年，Web 开发进一步摆脱了复杂性，Astro 和 Svelte 等前端框架越来越受欢迎，因为更多开发人员正在寻找 React 生态系统之外的解决方案。同时，原生 Web 平台功能证明它们能够构建复杂的 Web 应用程序——特别是 CSS 在 2025 年期间得到了改进。

尽管如此，今年最大的 Web 开发趋势或许是 AI 辅助编程的兴起——事实证明，它倾向于默认使用 React 及其领先的 React 框架 Next.js。由于 React 在前端领域占据主导地位，大型语言模型 (LLM) 有大量的 React 代码可供训练。

让我们更详细地了解 2025 年五大 Web 开发趋势。

## 1. 原生 Web 功能的崛起

2025 年，许多原生 Web 功能悄然赶上了 JavaScript 框架提供的功能。例如，[视图转换 API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)——它使你的网站能够在页面之间[平滑地动画](https://developer.mozilla.org/en-US/blog/view-transitions-beginner-guide/)——成为了跨浏览器支持的 [Baseline 2025](https://webstatus.dev/?q=baseline_date%3A2025-01-01..2025-12-31) 指标的一部分。因此，它现在已广泛可供 Web 开发人员使用。

Baseline 是由 W3C 的 WebDX 社区组协调的一个项目，该社区组包括来自 [Google](https://cloud.google.com/?utm_content=inline+mention)、Mozilla、微软和其他组织的代表。它从 2023 年才开始运行，但[今年它真正发挥了作用](https://thenewstack.io/interop-unites-browser-makers-to-smooth-web-inconsistencies/)，成为实践 Web 开发人员的有用资源。

[![Baseline web features](https://cdn.thenewstack.io/media/2025/12/02643a08-baseline-stats-nov2025.png)](https://cdn.thenewstack.io/media/2025/12/02643a08-baseline-stats-nov2025.png)

*Baseline 功能的稳步年度增长，来源：[Web 平台状态网站](https://webstatus.dev/stats)。*

正如 The New Stack 的 Mary Branscombe [在 6 月份报道的](https://thenewstack.io/baseline-newly-available-stay-on-top-of-new-web-features/)，有许多方法可以跟踪哪些功能正在成为 Baseline 的一部分：

“Google 的 Web.Dev 提供 [Baseline 功能和新闻的每月更新](https://web.dev/baseline#the-baseline-monthly-digest)，WebDX 功能浏览器让你能够查看 [有限可用](https://web-platform-dx.github.io/web-features-explorer/limited-availability/)、[新可用](https://web-platform-dx.github.io/web-features-explorer/newly-available/) 或 [广泛可用](https://web-platform-dx.github.io/web-features-explorer/widely-available/) 的功能；以及[每月发布说明](https://web-platform-dx.github.io/web-features-explorer/release-notes/march-2025/)涵盖了哪些功能已达到新的 Baseline 状态。”

从 Web 功能的角度来看，现在确实没有理由不使用原生 Web 功能了。正如资深 Web 开发人员 [Jeremy Keith 最近所说](https://adactio.com/journal/22235)，框架“限制了你今天在 Web 浏览器中可以做的事情的可能性空间。”在[一篇后续文章](https://adactio.com/journal/22265)中，Keith 敦促开发人员尤其要停止在浏览器中使用 React，因为这会给用户带来文件大小成本。相反，他鼓励开发人员“研究你可以在浏览器中使用原生 JavaScript 做些什么。”

## 2. AI 编码助手默认使用 React

今年，AI 成为了 Web 开发工具链的标准组成部分（尽管它并不总是受到开发人员的认可，尤其是那些在 Mastodon 或 Bluesky 而非 X 或 LinkedIn 上社交的开发人员）。无论你是否是应用程序开发中的 AI 粉丝，都有一个主要担忧：LLM 倾向于默认使用 React 和 Next.js。

当 OpenAI 的 [GPT-5 于 8 月发布时](https://thenewstack.io/gpt-5-a-choose-your-own-adventure-for-frontend-developers/)，其宣称的优势之一是编码。GPT-5 最初获得了[开发人员褒贬不一的评价](https://thenewstack.io/is-gpt-5-a-coding-powerhouse-or-maintainability-nightmare/)，因此当时我联系了 OpenAI，向他们询问编码功能。[Ishaan Singal](https://www.linkedin.com/in/ishaan-singal/)，OpenAI 的一名研究员，通过电子邮件回应。

我向 Singal 指出，在 [GPT-5 提示指南](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide)中，有三个推荐框架：Next.js (TypeScript)、React 和 HTML。我问，是否与 Next.js 和 React 项目团队有任何合作，以优化 GPT-5 对这些框架的支持？

他回答说：“我们根据这些框架的流行度和普遍性选择了它们，但我们没有就 GPT-5 与 Next.js 或 React 团队直接合作。”

[![An example of "organizing code editing rules for GPT-5" from OpenAI's GPT-5 prompting guide.](https://cdn.thenewstack.io/media/2025/09/f028e3a8-screenshot-2025-09-05-at-10.55.25.png)](https://cdn.thenewstack.io/media/2025/09/f028e3a8-screenshot-2025-09-05-at-10.55.25.png)

*来自 OpenAI [GPT-5 提示指南](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide)中“为 GPT-5 组织代码编辑规则”的一个示例。*

我们知道，[管理 Next.js 框架](https://thenewstack.io/vercels-frontend-and-the-rise-of-the-hybrid-developer/)的公司 Vercel 是 GPT-5 的粉丝。在发布当天，它称 GPT-5 为“最好的前端 AI 模型”。因此，这里正在发生一种很好的互惠互利——GPT-5 由于其流行而能够成为 Next.js 的专家，这大概会进一步提高其流行度。这有助于 OpenAI 和 Vercel。

Singal 在谈到开发人员想要使用的 Web 技术时总结道：“归根结底，这是开发人员的选择。”“但成熟的仓库有更好的社区支持。这有助于开发人员进行自助维护。”

## 3. AI 代理和聊天机器人中 Web 应用程序的出现

今年，我们看到了 AI 聊天机器人和代理中迷你 Web 应用程序的出现。

[MCP-UI 是第一个迹象](https://thenewstack.io/mcp-ui-aims-to-replace-old-world-websites-with-ai-agent-uis/)表明 Web 将成为 AI 代理的关键组成部分。顾名思义，[MCP-UI](https://mcpui.dev/) 使用流行的模型上下文协议作为通信基础。[该项目](https://mcpui.dev/guide/introduction)“旨在标准化模型和工具如何在客户端应用程序中请求显示富 HTML 界面。”

在[八月份的一次采访中](https://thenewstack.io/mcp-ui-creators-on-why-ai-agents-need-rich-user-interfaces/)，两位创始人（其中一位当时在 Shopify 工作）解释说，MCP-UI 有两种类型的 SDK：客户端 SDK 和用于连接 MCP 服务器的服务器 SDK。服务器 SDK 提供 TypeScript、Ruby 和 Python 版本。

[![MCP-UI demo](https://cdn.thenewstack.io/media/2025/07/3cf7bfe7-mcp-ui-demo.jpg)](https://cdn.thenewstack.io/media/2025/07/3cf7bfe7-mcp-ui-demo.jpg)

*将 UI 插入 Claude 3.7 Sonnet 聊天中的 MCP-UI 演示。*

MCP-UI 听起来很有前景，但很快就被 10 月初发布的 [OpenAI 的 Apps SDK](https://thenewstack.io/openai-launches-apps-sdk-for-chatgpt-a-new-app-platform/) 盖过了风头。[Apps SDK](https://developers.openai.com/apps-sdk) 允许第三方开发人员构建基于 Web 的应用程序，这些应用程序作为交互式组件在 ChatGPT 对话中运行——这让许多人想起了 2008 年苹果推出 App Store 的情景。

Apps SDK 的决定性特征是其基于 Web 的 UI 模型（类似于 MCP-UI）。ChatGPT 应用程序组件是一个 Web UI，运行在 ChatGPT 对话中的沙盒 iframe 内。ChatGPT 充当应用程序的主机。你可以将第三方 ChatGPT 应用程序视为直接嵌入到 ChatGPT 界面中的“迷你 Web 应用程序”。

到 10 月底，Vercel 等行业巨头已经找到了如何[使用其 JavaScript 框架构建 ChatGPT 应用程序](https://thenewstack.io/next-js-in-chatgpt-vercel-brings-the-dynamic-web-to-ai-chat/)的方法。Vercel 将 Next.js 与 ChatGPT 应用程序平台快速集成，表明 AI 聊天机器人将不仅仅局限于轻量级的交互式小部件——复杂的 Web 应用程序也将存在于这些平台上。

## 4. 浏览器中的 Web AI 和设备端推理

2025 年的一个并行发展是[在浏览器中运行客户端 AI](https://thenewstack.io/how-google-is-shifting-ai-from-the-cloud-to-your-browser/) 的兴起，这使得 LLM 推理能够在设备上进行。Google 在这一趋势中尤为突出；它将其称为“Web AI”。[Jason Mayes](https://www.linkedin.com/in/webai/)，Google 这些计划的负责人，[将 Web AI 定义为](https://www.linkedin.com/pulse/life-edge-web-ai-history-future-smarter-digital-agentic-jason-mayes-fbqbc/)“通过 Web 浏览器，在用户设备上完全客户端运行任何机器学习模型或服务的艺术。”

11 月，Google 举办了一场名为 [Google Web AI Summit](https://rsvp.withgoogle.com/events/web-ai-summit-2025) 的仅限受邀者参加的活动。之后，我与活动组织者兼主持人 Mayes 进行了交谈。他解释说，一项关键技术是 LiteRT.js，这是 Google 面向生产 Web 应用程序的 Web AI 运行时。它基于 [LiteRT](https://ai.google.dev/edge/litert)，LiteRT 旨在直接在设备（移动、嵌入式或边缘）上运行机器学习 (ML) 模型，而不是依赖云推理。

在 Web AI Summit 的主题演讲中，[Parisa Tabriz](https://www.linkedin.com/in/parisatabriz/)，Google Chrome 和 Web 生态系统的副总裁兼总经理，[强调了去年 8 月添加到 Chrome 中的内置 AI API](https://thenewstack.io/googles-web-ai-playbook-the-paved-road-vs-the-open-field/)，以及去年 6 月 Gemini Nano——Google 的主要设备端模型——作为内置功能在 Chrome 中发布。这些和其他 Web 技术正在推动当前的 Web AI 趋势。

[![Parisa Tabriz at Web AI Summit](https://cdn.thenewstack.io/media/2025/11/e857e98d-webai-tabriz1.png)](https://cdn.thenewstack.io/media/2025/11/e857e98d-webai-tabriz1.png)

*Parisa Tabriz 在 Web AI Summit 上。*

Google 与微软共同参与的另一项创新是 [WebMCP 的发布](https://thenewstack.io/how-webmcp-lets-developers-control-ai-agents-with-javascript/)，它允许开发人员使用客户端 JavaScript 控制 AI 代理如何与网站交互。在 9 月份对 Microsoft Edge Web 平台产品组经理 [Kyle Pflug](https://www.linkedin.com/in/kylepflug/) 的采访中，他解释说：“核心概念是允许 Web 开发人员在 JavaScript 中为他们的网站定义‘工具’，类似于传统 MCP 服务器提供的工具。”

Web AI 不仅仅由商业公司推动。万维网联盟 (W3C) 也在探索“[代理 Web](https://thenewstack.io/the-agentic-web-how-ai-agents-are-shaping-the-webs-future/)”的构建块，其中包括使用 MCP-UI、WebMCP 和[另一个名为 NLWeb 的新兴标准](https://thenewstack.io/cloudflares-balancing-act-protect-content-while-pushing-ai/)（由微软开发）。

## 5. JavaScript 生态系统的“Vite 化”

今年听起来 AI 主导了 Web 开发——事实上也确实如此。但前端工具也看到了它的创新份额。其中一个产品尤为突出。

[Vite](https://vite.dev/) 由 [尤雨溪](https://evanyou.me/?utm=22b03) 创建，已成为现代前端框架（包括 Vue、SvelteKit、Astro 和 React）的首选构建工具——Remix 和 Angular 也提供了实验性支持。在[9 月份对 The New Stack 的采访中](https://thenewstack.io/how-vite-became-the-backbone-of-modern-frontend-frameworks/)，尤雨溪告诉我，Vite 成功的关键在于其早期使用了 ES 模块 (ESM)，这是一种标准化的 JavaScript 模块系统，允许你“将 JavaScript 代码分解成不同的部分，即可以加载的不同模块。”

[![Vite ecosystem](https://cdn.thenewstack.io/media/2025/10/d09b36d7-vite-plus-reveal.png)](https://cdn.thenewstack.io/media/2025/10/d09b36d7-vite-plus-reveal.png)

Vite 生态系统，来源：尤雨溪在 ViteConf。

尤雨溪和他的公司 VoidZero [正在构建 Vite+](https://thenewstack.io/vite-aims-to-end-javascripts-fragmented-tooling-nightmare/)，这是一个旨在解决 JavaScript 碎片化问题的新统一 JavaScript 工具链。在今年的 ViteConf 活动中，尤雨溪[正式发布了 Vite+](https://www.youtube.com/watch?v=x7Jsmt_o9ek)，并将其定位为企业开发工具包。他说它包括“你喜欢 Vite 的一切——加上你一直以来拼凑在一起的一切”。

## Web 开发的十字路口

2025 年底，前端开发感觉像站在一个十字路口。一方面，存在摆脱 React 复杂性难题的方法：使用原生 Web 功能和像 Astro 这样减轻用户负担的工具。虽然这确实是今年的一个趋势，但它在 2026 年面临被我们日益增长的对 AI 编码工具的依赖所掩盖的危险——正如所指出的，这些工具倾向于依赖 React。

事实是，现在大多数开发人员——包括以前不属于开发人员生态系统的数十万“氛围编程”人员——将继续由 AI 系统提供 React 代码。这使得 Web 开发社区在明年继续支持和倡导原生 Web 代码变得更加紧迫。