对于 Vercel 的 [Andrew Qu](https://www.linkedin.com/in/andrew-qu/) 来说，OpenAI 新的 [ChatGPT Apps 平台](https://thenewstack.io/openai-launches-apps-sdk-for-chatgpt-a-new-app-platform/) 提出了一个挑战。

Vercel 的软件主管告诉 The New Stack：“ChatGPT 最初将他们的应用程序设计为静态 HTML 页面，并进行缓存，以便他们可以向所有人提供一致但静态的体验。” “但这些年来，Web 技术一直在进步，使事物变得更加动态……因此，放弃所有这些努力，只遵守我们 10 或 20 年前就能支持的东西，感觉就像是浪费了进步。”

说 ChatGPT 应用程序“静态”并不完全公平，因为 OpenAI 在其 DevDay 上展示的示例可以响应用户输入、触发后端操作并动态更新其视图。但 Andrew Qu 更大的观点是，ChatGPT 应用程序只能在 OpenAI 为安全和一致性设计的严格沙盒环境中运行。因此，从这个角度来看，ChatGPT 应用程序确实比完整的单页应用程序（SPA）更受限制。

无论如何，Andrew Qu 和他的团队着手突破这些限制——特别是让 Vercel 的旗舰 [React](https://roadmap.sh/react) 框架 [Next.js](https://roadmap.sh/nextjs) [原生运行](https://vercel.com/templates/ai/chatgpt-app-with-next-js) 在 ChatGPT 的受控运行时中。

[![Next.js in ChatGPT](https://cdn.thenewstack.io/media/2025/10/063c780f-vercel-chatgpt.avif)](https://cdn.thenewstack.io/media/2025/10/063c780f-vercel-chatgpt.avif)

使用 Next.js 的 ChatGPT 应用程序。（来源：[Vercel](https://vercel.com/templates/ai/chatgpt-app-with-next-js)）

他们发现了一个深度分层的运行时。Andrew Qu 说：“事情在三重嵌套的 iframe 基础设施中运作。” 每一层都增加了对导航和状态管理的限制，这意味着即使是像 `pushState` 和 `replaceState` 这样的基本浏览器功能也已被修补，以防止复杂的路由。Andrew Qu 在 [一篇博客文章](https://vercel.com/blog/running-next-js-inside-chatgpt-a-deep-dive-into-native-app-integration) 中对此进行了说明：

```
chatgpt.com
  └── web-sandbox.oaiusercontent.com (sandbox iframe)
     └── web-sandbox.oaiusercontent.com (inner iframe)
        └── your app's HTML
```

## Vercel 如何让 ChatGPT 应用动态化

为了克服这些限制，Vercel 设计了一系列针对资产加载、重定向和水合的变通方案。结果是：一个 Next.js 应用程序可以在不改变框架本身的情况下在 ChatGPT 中动态渲染。

“在框架层面不需要做任何调整，”Andrew Qu 解释说。“所有东西都可以在用户端实现。它主要只是你在布局中添加的另一个脚本元素，以及一些小的细节。”

> “在框架层面不需要做任何调整。所有东西都可以在用户端实现。”
> **——Andrew Qu，Vercel 软件主管**

换句话说，Vercel 没有分叉 Next.js，也没有为 OpenAI 的平台构建一个特殊版本——它构建了一个任何开发者都可以遵循的[模板](https://github.com/vercel-labs/chatgpt-apps-sdk-nextjs-starter)。通过部署一个标准的 Next.js 项目，并将 ChatGPT 的连接器指向生成的 URL，开发者现在可以将复杂的前端体验直接嵌入到聊天中。

Andrew Qu 说：“只要你遵循博客中的指南，或者使用我们发布的示例模板，它就应该能正常工作。”

这听起来可能出奇地简单，但 ChatGPT 的沙盒引入了更微妙的限制。

Andrew Qu 指出：“你仍然能够通过特殊白名单的允许域名进行完整的网络请求。主要的不同之处在于当你打开外部链接时——这些链接会被拦截……他们为你加载了一个秘密的 `window.openAI.openExternalLink()` 函数。”

## **并非每个应用程序都适合聊天**

尽管 Next.js 应用程序可以相当容易地移植到 ChatGPT，但并非所有 Web 应用程序都适合聊天界面。

Andrew Qu 指出，即使是 OpenAI 自己的市场合作伙伴——例如 Booking.com、DoorDash 和 Expedia——也没有公开他们的完整网站。他说：“他们中的许多人只是渲染一个小部件 […]，所以它与对话很契合。”

即便如此，Vercel 希望确保开发者可以在 ChatGPT 中构建多个小部件。

Andrew Qu 解释说：“我们试图通过让 Next.js 在 ChatGPT 中工作来解决的问题是，你仍然可以在一个应用程序中声明多个不同的小部件，并且你可以以一种熟悉的方式来完成它，而不是尝试手工编写 HTML 或 JS。”

[![Canva ChatGPT app](https://cdn.thenewstack.io/media/2025/10/45610109-chatgpt-app-example-canva.png)](https://cdn.thenewstack.io/media/2025/10/45610109-chatgpt-app-example-canva.png)

Canva ChatGPT 应用程序。（来源：OpenAI 视频）

为了简化这一点，Vercel 正在准备一套 React “GPT 钩子”，这是一个轻量级库，将公开 ChatGPT 特定的窗口属性——包括显示模式、最大高度、对话状态，甚至来自语言模型的实时补全。Andrew Qu 说：“AI 在窗口对象上使用了许多奇怪的钩子。我们正在尝试发布一个包，让你能够访问你需要的一切。”

## MCP 的作用

那么，[模型上下文协议（MCP）](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) 是如何融入这一切的呢？OpenAI 自己将 MCP 描述为 ChatGPT 应用程序范式中“保持服务器、模型和 UI 同步的支柱”。我问 Andrew Qu，Vercel 在 Next.js 集成中对 MCP 的态度是什么。

Andrew Qu 笑着说：“我对 MCP 有很多有争议的看法。它有望成为 AI 的万能集成端点，但很多人误用 MCP，只是将其视为 API 的镜像。”

他建议*仅当*开发者不控制客户端时才使用 MCP，例如将 ChatGPT 连接到 Notion 或 GitHub——而不是在直接 API 更合理的内部工具链中使用。

## **与 GPT-5 的技术栈保持一致**

我注意到在 GPT-5 提示指南中，OpenAI [明确推荐 Next.js](https://thenewstack.io/gpt-5-a-choose-your-own-adventure-for-frontend-developers/) (TypeScript)、React 和 HTML 作为 AI 驱动开发的首选前端框架。这种与 OpenAI 的一致性是否让 Next.js 与 ChatGPT 的集成变得更容易了？

Andrew Qu 回答道：“我们正努力与所有模型实验室合作，以提升 Next.js 的性能。我们希望所有 LLM 都能全面生成更优质的代码。”

虽然这并没有直接回答我的问题，但其言下之意是 Vercel 希望成为所有 AI 聊天机器人的默认 Web 框架，而不仅仅是 ChatGPT。Andrew Qu 指出了 Next.js 网站上一个新推出的“[评估](https://nextjs.org/evals)”页面，该页面展示了 AI 模型性能评估。OpenAI 的 GPT 模型目前位居第一，但 Anthropic 的模型也紧随其后。

[![Next.js evals](https://cdn.thenewstack.io/media/2025/10/5c3d6177-nextjs-evals-oct25.png)](https://cdn.thenewstack.io/media/2025/10/5c3d6177-nextjs-evals-oct25.png)

Next.js 评估。（来源：[Next.js](https://nextjs.org/evals)）

Andrew Qu 表示，如果 Anthropic 或其他提供商推出类似的聊天应用程序商店，Vercel 将“投入时间确保 […] 我们可以与他们正式合作，设计规范并成为 DevEx 部门。”他补充说，该公司已经在试验 SvelteKit（Vercel 支持）作为聊天应用程序的另一个候选，因为其更严格的 HTML/JS 输出与 ChatGPT 的静态假设非常吻合。

## Web 作为 AI 的主要界面

退一步看，Andrew Qu 将这项工作视为开放网络在 AI 界面时代仍处于核心地位的证据。

他说：“我们正在用 Next.js 尝试做这件事，作为一种证明，即即使人们不以传统方式与网络互动 […] 仍然需要人们来构建这些体验，然后将它们嵌入到聊天体验中。”

他没有将聊天客户端视为浏览器的替代品，而是将它们设想为 Web 内容的新分发层——开发者可以在其中重用他们现有的框架和托管工作流程。

Andrew Qu 继续说道：“我个人认为开放网络仍然会存在。我们有了这种新媒介，这种通过聊天客户端与计算机互动的新方式，但我们仍然可以拥有相同的表达能力和相同的开放标准来与之互动。”

> “……即使人们不以传统方式与网络互动 […] 仍然需要人们来构建这些体验，然后将它们嵌入到聊天体验中。”
> **——Andrew Qu**

一个新兴的焦点领域是[代理商务](https://thenewstack.io/how-mcp-ui-powers-shopifys-new-commerce-widgets-in-agents/)，其中店面直接呈现在聊天会话中。Andrew Qu 认为这可以使电子商务更加开放，而不是更封闭。

他说：“如果你有一个店面并可以发布它，它应该不比分享一个链接更难。这与 [智能手机] 应用商店模式非常不同……我认为 ChatGPT Apps 的体验实际上让我们更接近这一点。”

## **React 和 Next.js 作为默认的 AI 技术栈**

随着越来越多的开发者——以及越来越多的 AI 模型本身——使用 Next.js，Vercel 发现使用量激增。Andrew Qu 说：“仅仅在过去的一个月里，Next.js 的下载量就超过了过去十年的总和。” 他将这一激增归因于专业开发者，也归因于“一场更大的运动和更低的入门门槛”，因为 AI 生成的代码降低了构建 Web 应用程序的摩擦。

当被问及 React 和 Next.js 是否可能成为 AI 原生 UI 的默认技术栈时，Andrew Qu 毫不犹豫地回答：“当然是。我认为它的工程学和人机/AI DX [开发者体验] 都非常好。”

Andrew Qu 还认为，React 的组件模型在机器生成的结构和人类设计意图之间提供了恰到好处的平衡。一些开发者可能会对此提出异议，并回应说 [React 的复杂性](https://thenewstack.io/want-out-of-react-complexity-try-vues-progressive-framework/) 已经使 Web 开发过于偏向开发者体验。

但总的来说，Vercel 将 Next.js 快速集成到 ChatGPT 应用程序平台中，表明 AI 聊天机器人将不只局限于轻量级交互式小部件——复杂的 Web 应用程序也将存在于这些平台之上。