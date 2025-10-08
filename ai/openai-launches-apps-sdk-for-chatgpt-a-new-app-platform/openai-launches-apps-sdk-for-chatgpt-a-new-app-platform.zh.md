在其年度 DevDay 活动上，OpenAI 宣布了[针对开发者的一系列举措](https://thenewstack.io/openai-lunches-a-no-code-agent-builder/)——该公司表示，开发者人数现已达到 400 万。其中最引人注目的是新的 [Apps SDK](https://developers.openai.com/apps-sdk)，它允许第三方开发者构建基于网络的应用程序，这些应用程序作为交互式组件在 ChatGPT 对话中运行。OpenAI 表示，将在今年晚些时候“开始接受应用程序提交以供审核和发布”。

是的，没错：这是一个用于 ChatGPT 的应用程序平台。这让人联想到 [2008 年智能手机应用平台发布](https://cybercultural.com/p/internet-2008/)时的盛况——包括 iOS 和 Android。可以说，鉴于 OpenAI 的巨大普及以及其开创的聊天机器人用户范式，这是第一个真正有机会与那两个智能手机应用商店竞争的主流应用平台。

有趣的是，Apps SDK 的一个决定性特征是其基于网络的 UI 模型。事实上，它与 MCP-UI 非常相似，[我今年对此进行了深入探讨](https://thenewstack.io/mcp-ui-creators-on-why-ai-agents-need-rich-user-interfaces/)。这使其与 iOS 和 Android 应用平台截然不同，因为后者并非基于网络。但尽管 OpenAI 的 Apps SDK 在技术栈中处于更高的层级（ChatGPT 本身有 iOS、Android 和浏览器版本），它作为应用分发平台潜在的拉力巨大。

在我们过于激动之前，先确保我们理解其基本原理。

## Apps SDK：沙盒内的 Web 组件

从核心来看，ChatGPT 应用组件是一个在 ChatGPT 对话中运行于沙盒 iframe 内的 Web UI。这与 [MCP-UI 运行的基本范式](https://thenewstack.io/how-mcp-ui-powers-shopifys-new-commerce-widgets-in-agents/)相同，只是 MCP-UI 被设计为在任何符合 MCP 规范的代理中运行——它是一个[协议规范](https://thenewstack.io/mcp-ui-aims-to-replace-old-world-websites-with-ai-agent-uis/)，而不是一个单一产品。相比之下，Apps SDK 与 ChatGPT 本身紧密耦合。

[![Spotify in ChatGPT](https://cdn.thenewstack.io/media/2025/10/827023d9-openai-appssdk-spotify.jpg)](https://cdn.thenewstack.io/media/2025/10/827023d9-openai-appssdk-spotify.jpg)

ChatGPT 中的 Spotify；来源：DevDay。

ChatGPT 充当应用程序的主机。你可以将第三方 ChatGPT 应用程序视为直接嵌入到 ChatGPT 界面中的“迷你 Web 应用程序”。开发者与 OpenAI [注入到 iframe 中的](https://developers.openai.com/apps-sdk/reference/) `window.openai` 组件桥进行交互；这个桥梁让应用程序的前端能够与周围的对话以及其 MCP 服务器交换数据。要使用 Apps SDK 创建应用程序，你需要构建普通的 Web 代码——HTML、CSS 和 JavaScript，这些可以与 React 或 Vue 等现代框架捆绑在一起——然后 ChatGPT 将其渲染为聊天线程中的交互式卡片或面板。

当 OpenAI [宣布推出 Apps SDK](https://developers.openai.com/apps-sdk) 时，它指出该系统基于模型上下文协议（MCP）构建，但“扩展了 MCP，以便开发者可以设计其应用程序的逻辑和界面。”

## 它如何扩展 MCP？

Apps SDK 在底层使用了与现在为外部工具服务器和[自定义 GPTs](https://thenewstack.io/getting-started-with-openais-gpt-builder-and-how-it-uses-rag/) 提供支持相同的 MCP 传输和工具注册模型。MCP 已成为 OpenAI 所有新扩展层（包括新的 Apps SDK）之间的连接组织。

开发者的 MCP 服务器公开工具（用于服务器端逻辑）和资源（用于数据端点或 UI 模板）。每个工具都可以引用一个输出模板——通常是一个指向捆绑的 HTML 和 JavaScript UI 的 URI。当用户或模型触发该工具时，ChatGPT 会使用工具的结构化输出和任何附加元数据来填充 Web 组件。

在 iframe 内部，Web 应用程序通过主机提供的 `window.openai` 界面访问这些数据。这创建了清晰的分工：模型进行推理，服务器执行，UI 渲染——一个纯粹基于网络、沙盒化、事件驱动的层，将整个体验联系在一起。

## 用户体验指南

OpenAI 的[早期文档](https://developers.openai.com/apps-sdk/concepts/design-guidelines)强调，嵌入式组件应看起来和行为都像是 ChatGPT 的原生部分。为了实现这一点，该公司引入了一套 UX 指南和设计约束，涵盖布局、颜色主题、排版和可访问性。目的是让每个第三方应用程序在聊天环境中都感觉协调一致，而不是像一个外部网页。

鼓励开发者尊重 ChatGPT 的布局边界，因为组件以具有一致边距、圆角以及亮色或暗色主题感知的卡片形式出现。可访问性也是一个核心要求：应用程序应依赖语义化 HTML 和 ARIA 属性，以便 ChatGPT 能够保持键盘导航和屏幕阅读器兼容性。

还有其他限制，但关键是开发者使用熟悉的 Web 技术来构建他们的应用程序。其理念是鼓励一个由小型的、视觉上一致的交互式卡片组成的生态系统——地图、日历、音乐播放列表、文档查看器等——这些卡片感觉像是 ChatGPT 的原生部分。用户可以直接通过名称调用它们，或者将它们作为模型生成的上下文建议遇到。在当前的预览版中，Spotify、Canva 和 Zillow 等早期合作伙伴展示了这些嵌入式 Web 体验的实际效果。

## 比较：Apps SDK 与 MCP-UI

如前所述，MCP-UI 是一种协议，允许开发者将 Web 视图集成到多个 AI 聊天平台中，而不仅仅是 ChatGPT。理论上，应用程序开发者可以构建一个独立的基于浏览器的应用程序，然后通过 MCP-UI 公开它，以便任何兼容的代理（包括 ChatGPT）都可以与它交互。

[![](https://cdn.thenewstack.io/media/2025/10/1d547a7a-devday25-webui.jpg)](https://cdn.thenewstack.io/media/2025/10/1d547a7a-devday25-webui.jpg)

ChatGPT 内 Coursera 应用程序的示例；来源：DevDay。

这里的权衡对于任何关注过 2000 年代后期平台争论的人来说都是熟悉的。MCP-UI 旨在实现跨主机可移植性，提供一个单一的组件规范，任何代理都可以使用其自身的主机端渲染器来渲染。相比之下，Apps SDK 优先考虑与 ChatGPT 产品的紧密集成。那些希望在多个代理 shell 中获得一致体验的开发者可能会倾向于 MCP-UI，而那些专注于 ChatGPT 庞大用户群并希望获得第一方优化（如 [Pulse 卡片](https://openai.com/index/introducing-chatgpt-pulse/)、共享项目或[即时结账](https://openai.com/index/buy-it-in-chatgpt/)）的开发者，则可能会选择 Apps SDK 作为最短路径。

在某些方面，这场争论类似于智能手机早期的一个争论：当 Web 本身应该是一个通用平台时，为什么还要为一家公司的平台（比如苹果的 iOS）构建应用程序呢？Facebook 最初站在了 Web 这一边，[构建了一个 HTML5 Web 应用](https://cybercultural.com/p/049-rww-mobile-summit-may2010/)，希望 iPhone 和 Android 用户都能采用。但最终，它妥协并开发了单独的原生应用，因为当时的原生体验更好。

如今，ChatGPT 拥有类似于 2008 年苹果和谷歌的强大吸引力。其庞大的用户群和聊天式界面的日益普及使其成为一个引人注目的应用程序平台。然而，在一次奇妙的历史反转中，OpenAI 颠覆了范式：最具活力的全新应用平台不是原生移动操作系统，而是一个渲染由 Web 技术构建的迷你应用的 AI 主机。

换句话说，如果你是构建 AI 应用程序的第三方开发者，那么你不一定需要担心为原生平台构建。相反，你只需构建一个通过 MCP 接口并在 ChatGPT 内部运行的 Web 应用程序。这无疑是 OpenAI 希望你做的。