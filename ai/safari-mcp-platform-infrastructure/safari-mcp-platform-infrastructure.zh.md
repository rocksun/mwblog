本周早些时候，苹果的 WebKit 团队发布了 [Safari Technology Preview 247](https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/)，内置了一个模型上下文协议（Model Context Protocol，简称 MCP）服务器——包含 16 种工具，使任何兼容 MCP 的 AI 智能体都能直接访问运行中的 Safari 浏览器窗口。在这种工作流中，智能体可以捕获屏幕截图、检查 DOM、执行 JavaScript、读取控制台输出、监控网络请求、调整视口大小、模拟 CSS 媒体模式并运行可访问性检查，而这一切都不需要开发者离开终端。

任何针对 Safari 进行开发的开发者都知道，这是一个切实的体验改善。由于这是苹果在不到一个月内发布的第二个官方 MCP 服务器，平台供应商正开始将 MCP 内置到他们的产品中，而不是将其留给社区去实现。

## 两款服务器，三周时间

在 6 月初的 WWDC 上，苹果在 Xcode 27 中引入了 MCPBridge——一个将 MCP 通过 XPC 转换为 Xcode 实时进程的二进制文件，公开了 [20 种内置工具](https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode)，允许 AI 智能体构建项目、运行测试、渲染 SwiftUI 预览、搜索文档以及读取诊断信息。来自 Anthropic、OpenAI 和 Google 的智能体都可以通过相同的协议进行连接。

Safari MCP 服务器在这一点上非常相似，它作为 Safari Technology Preview 的一部分发布，连接任何 MCP 客户端，并通过标准化的接口公开浏览器功能。你可以将其称为实验，但如果你问我，单家平台供应商在短短三周左右的时间内，就将两款官方 MCP 服务器作为标准产品功能发布，这证明了 MCP 正在成为平台基础设施。

> 单家平台供应商在短短三周左右的时间内，就将两款官方 MCP 服务器作为标准产品功能发布，这证明了 MCP 正在成为平台基础设施。

## 基于架构的隐私保护

该服务器完全在本地机器上运行，无法访问 Safari 中的个人信息。这意味着它无法获取自动填充数据、浏览历史记录或任何其他浏览器活动。当它捕获页面内容、屏幕截图或控制台日志时，数据会直接发送给开发者正在运行的 AI 智能体，而不是发送给苹果；之后发生什么取决于智能体及其背后的模型。

这种隐私架构值得注意，因为它不同于其他浏览器供应商处理 AI 集成的方式。Microsoft 在 Edge 中的 Copilot 通过 Microsoft 的基础设施读取和分析打开的标签页，而 Google 的 Gemini for Mac 则通过 Google 的模型访问本地文件。在这两种情况下，浏览器公司和 AI 公司都是同一个实体，这简化了技术架构，但也集中了信任关系。苹果的方法将两者解耦：浏览器供应商提供接口，开发者选择信任哪种 AI 来处理会话数据。

其效果是，Safari 成为调试循环中的一个活跃参与者，智能体可以直接对其进行查询。

> 苹果的方法将两者解耦：浏览器供应商提供接口，开发者选择信任哪种 AI 来处理会话数据。

不久前，AI 智能体的浏览器集成几乎完全依赖于社区构建的工具。开发者通过 Playwright、Chrome DevTools Protocol 封装器或志愿者维护的非官方 MCP 服务器拼凑连接。这些工具虽然有效，但它们依赖于逆向工程，几乎没有供应商的支持承诺，并且在浏览器版本更新时会发生不可预测的崩溃。

请记住，苹果在这一举措上并不孤单。JetBrains 自 2025.2 版本起就在 IntelliJ IDEA 中捆绑了一个 MCP 服务器，并正在 [2026.2 EAP 中扩展其 MCP 覆盖范围](https://blog.jetbrains.com/idea/2026/05/intellij-idea-2026-2-eap/)，通过该协议向智能体公开调试功能——包括断点和日志点。Brave 为其搜索 API 维护着一个 [官方 MCP 服务器](https://github.com/brave/brave-search-mcp-server)。Anthropic 将模型上下文协议本身捐赠给了 [Linux 基金会的 Agentic AI 基金会](https://www.linuxfoundation.org/press/anthropic-donates-model-context-protocol-to-linux-foundation)，而 OpenAI、Google 和 Microsoft 都公开支持它。

这一贯的战略表明，构建浏览器、IDE 和开发平台的公司正在将 MCP 端点作为标准产品功能发布，而不是依赖社区集成来填补空白。

## 可靠性需要官方支持

简而言之，官方实现会与底层软件同步更新。苹果控制着 Safari MCP 服务器与 Safari 渲染引擎之间的兼容性。社区维护的替代方案无法提供同样的保证，因为它们依赖于供应商可能随时更改的内部 API。

对于评估是否依赖智能体驱动的调试、测试或部署的工程团队来说，底层集成的可靠性与模型的能力同等重要。如果提供 DOM 树的工具在浏览器发布版本更新时就崩溃，那么一个能推理 DOM 树的模型将毫无用处。

> 如果提供 DOM 树的工具在浏览器发布版本更新时就崩溃，那么一个能推理 DOM 树的模型将毫无用处。

我们也不能忘记安全模型：苹果的 Safari MCP 服务器明确限制了其访问权限——这一边界比第三方集成所能承诺的更容易让供应商以可信的方式执行。

## 接下来会发生什么

现在就下结论：MCP 正在进入平台基础设施领域。如果这一趋势保持下去，开发者最终可能会像今天期望 REST API、SDK 或命令行工具那样，期望软件公开 MCP 接口。

针对智能体与工具通信的竞争方法依然存在，生态系统也在持续快速演变。但平台供应商将 MCP 视为一种可交付的产品功能而非集成实验的事实，标志着一个明显的阶段性变革。