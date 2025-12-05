2024 年 11 月，Anthropic 发布了一篇看似无害的博客文章，题为《[引入模型上下文协议](https://www.anthropic.com/news/model-context-protocol)》。在文章中，他们承诺模型上下文协议 (MCP) 将提供“一种通用的开放标准，用于连接 AI 系统与数据源，用单一协议取代分散的集成”。

科技公司常说许多宏伟的愿景，但在 MCP 推出的第一年里，很难断定 Anthropic 夸大其词。MCP 仍有改进空间，但该协议满足了需求，并迅速找到了其受众。让我们深入探讨其原因，以及它在 2026 年及以后可能的发展方向。

## 一段历史

Sentry 很早就积极[构建 MCP 服务器](https://thenewstack.io/15-best-practices-for-building-mcp-servers-in-production/)，仅在过去 30 天内，它就为 5,000 多个组织提供了超过 2.78 亿次请求。这些数字***听起来***很棒——但走到这一步却……很艰难。

对于在 MCP 早期阶段进行构建的任何人来说，都[遇到了许多障碍](https://cra.mr/mcp-is-not-good-yet)。由于[我们公司运营的规模](https://thenewstack.io/can-companies-really-self-host-at-scale/)，我们很早就遇到了其中的许多问题。

像大多数技术一样，MCP 早期经历了许多变化——包括协议本身和最终支持它的平台。MCP 的最初阶段充满了各种拼凑起来的东西，比如通过链式命令在本地运行，或者通过 CLI 勉强实现远程支持。除了 Anthropic 的产品（考虑到是他们构建的，这很合理）之外，大多数大型语言模型对 MCP 的支持都相当粗略。

一年后呢？它仍然不完美，但无疑更加稳固了。它也显然不会很快消失。

Cloudflare 在这方面率先介入，成为了平台构建全功能 MCP 服务器的“首选”。他们通过 Cloudflare Workers 平台，发布了[框架辅助工具](https://developers.cloudflare.com/agents/guides/remote-mcp-server/)、[OAuth 支持包](https://developers.cloudflare.com/agents/model-context-protocol/authorization/#2-third-party-oauth-provider)，并使[持久对象](https://developers.cloudflare.com/durable-objects/get-started/)更易于使用。Vercel 也紧随其后，推出了 [mcp-handler](https://github.com/vercel/mcp-handler) 作为在 Next.js 中创建 MCP 服务器 API 路由的简便方式，并随之发布了他们自己的身份验证支持和功能。

在过去的十二个月里，MCP 已从一个好奇、复杂的规范发展成为任何大型语言模型客户端几乎强制性的功能——无论是目前正在兴起的以终端为主的 TUI，还是功能更全面的编辑器如 Cursor。

我们在围绕 MCP 进行构建时遇到了许多挑战和汲取了许多经验教训，我们对它的未来发展寄予厚望。

## 经验教训：大规模构建 MCP 服务器

我们是否了解构建完美 MCP 所需的一切知识？不！没有人知道。这些东西都是全新的。但这是我们在此过程中学到的一些经验：

### **你需要弄清楚哪里、为谁、出了什么问题**

[![](https://cdn.thenewstack.io/media/2025/12/10e4a3ed-image1-1024x586.png)](https://cdn.thenewstack.io/media/2025/12/10e4a3ed-image1-1024x586.png)

由于 MCP 是如此新颖，在早期它频繁地出现故障。

我们需要更好的方法来确切了解故障在代码中发生的位置，哪个工具调用最不稳定，哪些用户遇到了问题，最重要的是：哪种客户端/协议组合导致了这些各种问题。

Sentry 有许多工具可以帮助处理类似的使用案例，但由于 MCP 是一种截然不同的软件方法，并且运行在 Cloudflare workers 之上，绝对存在一些空白。

意识到我们可能不是唯一需要这些功能的人，我们将为监控 MCP 而构建的功能整合到 Sentry 中，供所有人使用。

回想起来，在规范层面进行更多的标准化，将大大有助于确保 MCP 与客户端及其所采取的行动之间交互的监控更加容易。

如今，许多可观测性都依赖于大型语言模型，但我们绝对看到越来越多的人希望更清楚地了解他们的 MCP 服务器在幕后发生的情况。MCP 感觉像魔法，直到它出现故障，你才开始深入挖掘原因。

随着不同平台以略微不同的方式解决问题，复杂性将继续出现。就我们而言，我们尽可能地贴近应用程序代码，并选择将 Sentry 封装在 MCP 服务器层本身。

### **远程优先……但也有……本地？**

第一代 MCP 服务器的运行很大程度上涉及克隆仓库，将其放入特定目录，然后与 Node 路径问题搏斗，直到获得绿色连接指示器。再加上本地依赖关系或创建/存储 API 令牌等挑战……这是一种高摩擦的体验，更不用说容易出错。第二天的更新管理起来很麻烦。

远程服务器避开了许多这些挑战，早期主要通过使用 [mcp-remote](https://github.com/geelen/mcp-remote) 将标准 MCP 服务器作为远程连接来支持。还有一些其他的代理解决方案，但都没有真正流行起来。这在常见的编辑器和工具中创建了一个非常零散的支持生态系统。

根据对未来趋势的判断，以及我们如何为用户保持低摩擦并使他们能够“消费”服务，我们选择了远程托管 MCP 作为主要路径。远程托管有许多好处——它允许你不断添加新功能，而无需用户安装新包或克隆任何东西；你能够集中监控服务并围绕标准用户路径进行优化；如果做得好，你还可以通过 OAuth 等方式简化用户访问管理。

如今，[远程 MCP 服务器](https://thenewstack.io/remote-mcp-servers-inevitable-not-easy/)的实现相当容易（特别是使用我前面提到的 Cloudflare / Vercel 工具）——并且从维护的角度来看，远程运行它们会带来很多好处（即，无需担心用户是否正在更新其本地代码）。

拥有本地选项仍然是个好主意。保留一个本地 STDIO 版本方便你进行本地测试，并且还可以让你在少数尚不支持远程 MCP 中的 OAuth 的客户端方面拥有一定的灵活性（确实存在一些）。

随着时间的推移，OpenAI 接受了该规范，并开始[将其包含在他们自己的工具中](https://openai.com/index/new-tools-and-features-in-the-responses-api/)。我们目睹了从从 GitHub 克隆并在本地运行的 STDIO 服务器，到捆绑了身份验证的远程托管 MCP 服务器的转变。现在，我们正在关注不同的客户端平台竞相支持和利用每个修订版本。

### **MCP 变得更广，然后更窄**

使用 MCP 服务器，很容易陷入为一切构建工具的陷阱，并试图在 MCP 工具调用中复制你在 API 中所做的事情。但事实证明，拥有数十个臃肿的、令牌密集型的 MCP 工具调用是快速突破令牌限制的好方法。

这种方法的缺点是，使用 MCP，每次你进行调用时，完整的工具列表都会随每个提示一起发送。每次调用，你都在消耗宝贵的上下文窗口。除了工具调用之外，你创建的任何资源或附加的提示也会被发送。

上下文窗口越来越大，但上下文膨胀造成的浪费空间增长非常快，而且你进行的调用越复杂或工具调用链越长，情况就会呈指数级恶化。我们正进入一个 MCP 构建者默认收回其暴露的工具的时代，要么完全废弃不必要的工具调用，要么为用户提供选项，让他们减少向客户端暴露的工具调用。

[![](https://cdn.thenewstack.io/media/2025/12/f553617c-image3-1024x668.png)](https://cdn.thenewstack.io/media/2025/12/f553617c-image3-1024x668.png)

我们选择在自己的 MCP 中采用这种方式，主要是为了我们仍然可以保留一些有用的功能，同时也能让用户选择他们想要暴露多少。我们删除了几个根本未使用的工具调用，减少了可用资源，并删除了额外的提示。我们还在 OAuth 同意屏幕上添加了一项增强功能，允许你配置要在 MCP 中暴露的工具组，从而实现更精细的控制。给予开发者他们需要的工具，但不要用他们不需要的东西来占用他们宝贵的上下文窗口。

### **SSE 正在消退，HTTP-Streamable 正在兴起**

在早期的 MCP 生态系统中，服务器发送事件 (SSE) 是从服务器到客户端[流式传输数据](https://thenewstack.io/how-to-build-applications-over-streaming-data-the-right-way/)的默认方式。SSE 简单且早期运行良好，因此在我们最初原型化时使用它是合理的。但它建立在可能不稳定且长期存在的 HTTP 连接之上。挑战包括：SSE 的长期连接需要特定的基础设施决策来支持，并且在发生故障时，没有干净的方法来恢复会话。

最终，OpenAI 引入了 HTTP Streamable，一种更强大的流式传输格式，专门用于解决人们开始遇到的痛点。此后不久，我们决定从 SSE 转向 HTTP Streamable。

SSE 有很多限制——尽管花了几个月才走到这一步，但现在所有主要的客户端都支持 HTTP Streamable。我们发现，迁移后连接总体上更加稳定。

[![](https://cdn.thenewstack.io/media/2025/12/167d5d3b-image2-1024x423.png)](https://cdn.thenewstack.io/media/2025/12/167d5d3b-image2-1024x423.png)

我们仍处于过渡时期；许多服务器仍将 SSE 作为其默认协议，但我预计这种情况将很快改变。HTTP-Streamable 最终提供了更简单的整体实现体验，以及更好的用户消费体验。

### **MCP 作为工作流**

我认为目前最成功的 MCP 服务器是那些旨在无缝融入用户现有工作流的服务器。这些工具需要尽可能地适应用户所处的位置。

一个很好的例子是最近发布的[Chrome Dev Tools MCP 服务器](https://developer.chrome.com/blog/chrome-devtools-mcp)。这个 MCP 使开发者更容易通过 MCP 启动浏览器；超越代码，了解正在运行的应用程序实际的工作/外观。 [Resend MCP 服务器](https://resend.com/docs/knowledge-base/mcp-server)让你能够获取正在构建的事物的上下文，并轻松地与生成的模板一起通过电子邮件发送给用户。如果你是 iOS 开发者，[Xcode MCP 服务器](https://github.com/cameroncooke/XcodeBuildMCP)使模型能够更轻松地了解你的 Xcode 环境。

我们甚至已经开始开发一个新的 MCP 服务器，它旨在与 [Spotlight](https://spotlightjs.com/) 配合使用，以帮助进行本地调试，而不是标准的 Sentry 托管模型。这为我们提供了明确的功能分离，其中标准 Sentry MCP 专为 Sentry 平台的核心功能而设计——但我们现在也可以启用一些特定的本地调试工作流，并创建 MCP 服务器可以在工具调用中协同工作的场景。

## **MCP 的下一步是什么？**

那么 MCP 的未来是什么？作为一个在这里构建了一段时间的人，我看到了以下趋势：

*   **协议已定——HTTP Streamable 正当红**。关于增加更深入的 [Websocket 支持](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/493?utm_source=chatgpt.com)整体存在一些讨论，但最终，HTTP Streamable 很可能在很长一段时间内都是主要路径——根据需要回退到 SSE。
*   **OAuth 2.1 需要一些工作，但现在进行构建将带来长远的回报**——从 OAuth 2.0 到 2.1 的转变无疑存在一些尖锐的问题，但生态系统正在迅速转换为 2.1 作为标准的未来路径。现在投入工作，以后会有回报。对于适合使用案例的服务器，没有人希望告诉用户手动拉取令牌进行身份验证。
*   **MCP 工具整合是当前的主流趋势**——开发者将继续寻找方法来减少其 MCP 环境中的总工具蔓延，以此作为控制令牌利用率的机制。预计将有更多围绕工具暴露的自定义选项，以及引入更多动态工具使用的方式（例如 Sentry MCP 中的自然语言搜索）。
*   **由 MCP 驱动的 Agent 循环**——随着主要提供商都直接在其 Agent SDK 中添加 MCP 支持，这是一个非常强烈的信号，表明这些是供 Agent 消费的一流工具。我预计 MCP 将在这些工作流中变得越来越重要，成为[智能扩展系统功能](https://thenewstack.io/3-ways-intelligent-automation-can-break-down-devsecops-silos/)的方式。我们看到人们[通过 MCP 暴露更多 agentic 流程](https://cra.mr/subagents-with-mcp)，这正在创造一些利用它的新颖有趣的方式。这在上下文保存和使这些工具真正有用之间创造了一种平衡。

在过去的一年里，我们目睹了 MCP 在不稳定的基础上转变——既包括协议本身的演变，也包括人们摸索出一些最佳实践。现在仍处于早期阶段——MCP 在未来一年肯定会有更多的演进点——但其中许多领域现在已经开始稳固；如果你一直在等待事物变得更稳定再投入，现在可能是时候了。