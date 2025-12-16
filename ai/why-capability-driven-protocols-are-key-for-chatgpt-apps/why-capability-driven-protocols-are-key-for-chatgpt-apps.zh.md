OpenAI 的[Apps SDK 于 10 月初推出](https://thenewstack.io/openai-launches-apps-sdk-for-chatgpt-a-new-app-platform/)，使开发者能够为 ChatGPT 构建迷你网络应用。虽然我们尚未看到承诺的 ChatGPT 应用商店，但第三方开发者已经开始尝试使用该 SDK。例如，TELUS Digital 构建了一个概念验证的 ChatGPT 应用，它是一个“包含市场数据、交互式可视化和自定义 UI 组件的股票和新闻追踪器”。

TELUS Digital 工程总监 Adam Shea 通过电子邮件采访分享了他对 ChatGPT 应用的看法。

## 为 ChatGPT 应用开发选择 React

重申一下，ChatGPT 应用本质上是在 ChatGPT 对话中运行的基于网络的应用程序。这意味着现代网络开发的所有优势都可供开发者利用——包括使用强大的 JavaScript 或原生网络技术的能力。正如 Shea 在[一篇技术博客文章](https://www.telusdigital.com/insights/data-and-ai/article/building-chatgpt-apps)中指出的那样，“Apps SDK 最显著的优势之一是支持现代的基于组件的开发。”

在我 10 月份关于 Apps SDK 的最初文章中，我指出有两种主要的组件方法可用：使用 [React](https://thenewstack.io/remix-takes-on-next-js-in-battle-of-the-react-frameworks/)，或者使用原生的 [Web Components](https://thenewstack.io/how-microsoft-edge-is-replacing-react-with-web-components/)。在 TELUS Digital 的案例中，他们选择使用 React。我问 Shea 他们为什么选择这个方向。

他回答说：“我们主要使用 React 是因为我们团队的熟悉度和其强大的生态系统。”“对于企业应用，我建议 React 通常是务实的选择，特别是如果你的团队已经拥有 React 专业知识和现有的组件库可以利用。我认为最佳选择确实取决于你的团队技能和现有技术栈。”

## 理解 MCP 和能力驱动协议

TELUS Digital 在构建 ChatGPT 应用时学到的一个经验是，MCP 服务器不仅仅是 API 端点。Shea 在博客文章中写道：“MCP [模型上下文协议] 代表了从请求-响应式 API 到能力驱动协议的转变。”

这似乎需要大量的测试，特别是如果你正在创建企业应用程序的 ChatGPT 版本。例如，你会希望确保 AI 响应不是[幻觉](https://thenewstack.io/stopping-ai-hallucinations-for-enterprise-is-key-for-vectara/)。我问 Shea 企业开发者如何适应这种新的“能力驱动”思维模式。现在测试和可观测性是否变得更加重要？

> “对于企业规模的应用程序，你需要某种方式来根据模型的输入验证其输出……”
> **– Adam Shea，TELUS Digital 工程总监**

“好问题。因为大型语言模型 (LLM) 主要是在重述它从 MCP 接收到的任何内容，所以真正的重点变成了确保你发送的数据是准确、完整且结构化的，以实现你想要提供的体验，”他回答道。“对于企业规模的应用程序，你需要某种方式来根据模型的输入验证其输出，这样我们就能知道数据没有改变。”

他提到了 [Fuel iX Fortify](https://www.fuelix.ai/products/fuel-fortify)，这是一个由 TELUS Digital 及其母公司 TELUS（一家加拿大企业集团）共同拥有的 AI 平台。Shea 表示，该工具提供“自动化测试和漏洞评估”，以帮助企业运行 AI 应用。

## AI 框架和 ChatGPT 应用的替代方案

我最近与 Vercel 的 Andrew Qu 谈到了他们[使用 Next.js 构建 ChatGPT 应用](https://thenewstack.io/next-js-in-chatgpt-vercel-brings-the-dynamic-web-to-ai-chat/)。所以我问 Shea 他们是否使用了 Vercel 的任何新工具，如果使用了，他的初步印象是什么。如果他们没有尝试过，他对用于构建 ChatGPT 应用（或任何 AI 助手应用）的框架可能出现有什么看法？

他说：“我还没有机会尝试他们的基于 ChatGPT 应用的工具，但随着 ChatGPT 应用的普及和 SDK 的不断发展，无疑会有方法来简化构建、测试和部署过程。”他补充说，他是 Vercel 工具以及其与各种其他产品集成功能的粉丝。

Shea 还指出，ChatGPT 应用的审批过程主要是手动的，需要直接与 OpenAI 合作。但他预计这种情况很快就会改变。

“我想，随着平台结构变得更加完善，应该有可能创建能够自动化整个构建、测试和部署工作流程的工具，就像 iOS 和 Android 生态系统一样。”

在我 10 月份的文章中，我也将即将推出的 ChatGPT 应用商店与 iOS 和 Android 生态系统进行了比较，但值得注意的是，ChatGPT 应用可能存在开源替代方案。我[今年深入报道了 MCP-UI](https://thenewstack.io/mcp-ui-creators-on-why-ai-agents-need-rich-user-interfaces/)（它在 Apps SDK 之前发布），因为它提供了一种在*任何*AI 助手中嵌入迷你网络应用的方式——包括 ChatGPT。我向 Shea 询问了他对 [MCP-UI](https://thenewstack.io/mcp-ui-aims-to-replace-old-world-websites-with-ai-agent-uis/) 的看法。

“我还没有使用过它，但在内部我们已经为一项单独的计划尝试了一些概念验证 (PoCs)。这是一个与 ChatGPT 应用有趣的并行路径。随着 OpenAI 对 ChatGPT 应用的支持，我认为会有巨大的需求来支持这种方法。我可以看到这两种方式在生态系统成熟的过程中共存一段时间。这种比较更多地是关于你想要针对哪个平台和用户，而不是技术角度。”

## 哪些类型的应用适合 ChatGPT？

那么，Shea 认为哪种类型的企业应用最适合放入 ChatGPT，无论是作为补充应用，甚至可能完全取代现有的智能手机应用？

他回答说：“过去两年，主要是将生成式 AI 叠加到人们已经使用的应用上。”“新的 ChatGPT 应用通过将应用带入生成式 AI 环境本身，颠覆了这种模式。我认为我们正在走向一个混合世界，最佳路径确实取决于你的用户和客户在哪里，以及他们喜欢与什么互动。”

他补充说，生成式 AI 平台，特别是 ChatGPT，“在年轻一代中看到了极高的参与度。”因此，他认为像 OpenAI 这样的基于 AI 的应用程序开发平台将变得越来越重要。

> “MCP 擅长将来自不同来源的各种类型数据集成到像 GPT 这样的 LLM 中。”
> **– Shea**

至于适合集成到 ChatGPT 中的应用类型，他认为 MCP 将充当数据的一种枢纽——这将反过来推动构建 ChatGPT 应用的动力。

他说：“MCP 擅长将来自不同来源的各种类型数据集成到像 GPT 这样的 LLM 中。”“我认为构建 ChatGPT 应用的机会可能在于纯文本使用不足且无法提供引人入胜的用户体验的场景。例如，由于更复杂的数据或特定的布局，或者因为组织希望在 ChatGPT 界面中保持强大的品牌形象和所有权，可能需要视觉体验。”

Shea 补充说，他并不一定将 ChatGPT 应用视为 OpenAI 在其应用策略中的最终形式。

“我有一种预感，我们今天构建 ChatGPT 应用的方式与 OpenAI 传闻未来可能推出的智能手机平台在核心思想和结构上有一些共同之处。”

## ChatGPT 应用的未来

我们仍处于 ChatGPT 应用的早期阶段。毕竟，TELUS Digital 迄今为止也只创建了一个概念验证应用。所以我问 Shea，他们是否有为客户构建或帮助构建的正在投入生产的 ChatGPT 应用？

“是的，我们过去一个月一直在与一家领先的金融新闻和市场情报提供商合作，目前正处于构建认证体验的最后阶段，用户可以随时间跟踪股票，并使用通俗易懂的英语根据特定标准搜索不同的股票。”

与此同时，一些知名科技公司正忙于推出 ChatGPT 应用。就在过去几天，Adobe 宣布了 [Photoshop、Acrobat 和 Adobe Express 的 ChatGPT 应用](https://www.theverge.com/news/841369/chatgpt-apps-adobe-photoshop-acrobat-express)；本周早些时候，OpenAI 宣布了 [ChatGPT 中的 Instacart 应用](https://openai.com/index/instacart-partnership/)。预计到 2026 年，更多此类应用将进入 ChatGPT——包括来自企业和独立的第三方开发者。