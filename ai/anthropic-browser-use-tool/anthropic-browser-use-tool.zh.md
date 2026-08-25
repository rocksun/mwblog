Anthropic 发布了一款新的 Browser Use 工具，除了视觉渲染的内容外，它还为 Claude 提供了网页的结构化视图。该工具于周四发布，利用页面的无障碍树（accessibility tree）帮助 Claude 直接查找并与特定元素交互，而无需计算它们在屏幕上的位置。

Browser Use 是 Anthropic 更广泛发布的一部分，该发布还将 Computer Use、Skills API 和 Files API 纳入了通用可用范围。开发者可以通过 Claude API 使用 browser_toolset_20260801 来访问此浏览器工具。

> Browser Use 是 Anthropic 更广泛发布的一部分，该发布还将 Computer Use、Skills API 和 Files API 纳入了通用可用范围。

这一变化为 Claude 提供了一种与网页交互的更直接方式。Claude 不再需要从视口图像中推断按钮位置并瞄准坐标（如 `x: 640, y: 320`），而是可以接收绑定到该元素的引用（例如 `ref_3`），并在需要操作时直接使用它。

## 页面引用取代坐标

Computer Use 可以通过查看屏幕截图并发送鼠标坐标和键盘命令来操作整个桌面。而 Browser Use 在浏览器内部工作，它可以利用页面结构，而这些结构仅凭像素很难可靠地恢复。

当 Claude 调用 `read_page` 时，开发者的执行器会返回无障碍树的文本表示，其中链接、按钮和文本框等元素可以被标记引用。如果 Claude 随后想要点击由 `ref_3` 表示的按钮，它可以发送该引用连同请求的操作，而不是尝试计算按钮在屏幕上的位置。

话虽如此，如果标签页导航到新页面或者页面发生较大变化，刚才指向某个按钮的引用可能就会失效。API 本身不会捕获此情况，因此执行器必须在引用不再匹配底层元素时识别出来，拒绝该操作，并让 Claude 在继续之前重新读取页面。

## 批处理减少模型调用

例如，Playwright 可以将页面表示为 ARIA 快照，并按角色而非坐标定位元素。同时，Microsoft 的 Playwright MCP 服务器已经公开了结构化的无障碍快照以及模型可用于识别元素的引用。这些概念与 Browser Use 非常接近，但协议不同：Playwright MCP 使用 MCP 协议，而 Anthropic 的工具使用其自有的客户端工具集协议，因此开发者仍需要一个适配器，将 Claude 的请求转换为 Playwright 操作，并将结果以 Claude 预期的格式返回。

Puppeteer 提供了许多相同的构建块，通过 `Accessibility.snapshot()` 公开浏览器的无障碍树，并提供用于控制 Chrome 和 Firefox 的 API。开发者可以使用这些 API 进行导航或页面读取，然后在之上维护 Anthropic 的引用映射。

> 开发者可以使用这些 API 进行导航或页面读取，然后在之上维护 Anthropic 的引用映射。

令人有些困惑的是，一个无关的开源项目也叫 [Browser Use](https://github.com/browser-use/browser-use)，它通过 Chrome DevTools 协议针对 Chromium 运行 AI 浏览器代理。尽管名字相同，但它与 Anthropic 的工具没有任何关系，并自带自己的代理循环和浏览器抽象，因此将两者连接起来仍需要集成工作。

## 多个浏览器操作可以在一轮中完成

Anthropic 还通过允许在单次模型回合中请求多个操作，减少了 Claude 和浏览器之间的来回交互。现在，操作可以作为多个 `tool_use` 块一起到达。应用程序按顺序执行它们并将结果一并返回，避免了在每次点击和按键之间进行额外的模型调用。Anthropic 表示，这可以降低延迟和成本，特别是当工作流从少数交互扩展到数十或数百次时。

随着浏览器任务变得更长，这一点变得更加重要。[仅靠更便宜的模型无法解决代理工作流中的 Token 成本问题](https://thenewstack.io/agentic-ai-token-costs/)，因此减少不必要的模型调用是降低成本的另一种方式。

如果 Claude 在每次点击或按键后都必须返回模型，那么长浏览器任务会迅速累积模型调用。批处理通过让 Claude 一次请求多个操作，减少了部分往返，但浏览器仍然必须按顺序执行它们，因为每个操作都取决于之前发生的情况。例如，如果 Claude 要求点击按钮、填写字段并提交表单，如果第一次点击失败，执行器就不能简单地进入下一步，因为后续的一切都基于 Claude 未能到达的页面状态。

> 批处理通过让 Claude 一次请求多个操作，减少了部分往返，但浏览器仍然必须按顺序执行它们，因为每个操作都取决于之前发生的情况。

## 开发者托管浏览器

Browser Use 目前仅限于 Claude API，不适用于 [Claude Managed Agents](https://thenewstack.io/with-claude-managed-agents-anthropic-wants-to-run-your-ai-agents-for-you/)。将其添加到 Messages API 请求中会默认公开 27 种浏览器操作。Claude 可以决定使用哪些操作，但 Anthropic 不会执行它们。应用程序必须将每个请求转换为其自身浏览器环境中的操作，在回合之间保留会话，并返回足够的信息让 Claude 理解发生了什么。

加载所有这些操作会产生 Token 成本。Anthropic 的 [定价文档](https://platform.claude.com/docs/en/about-claude/pricing) 指出，默认的 Browser Use 工具集会在请求中增加大约 6,600 个输入 Token，这还不包括发回给 Claude 的屏幕截图、无障碍树和其他结果。开发者可以关闭不需要的操作以减少该开销。

它还创建了与 Anthropic 周四宣布的其他工具不同的托管拆分。通过 Skills API 上传的技能可以在 Anthropic 的代码执行沙箱中运行，而 Files API 存储的文档可以通过 ID 重用。浏览器会话及其下载和上传的文件保留在开发者的环境中。

## 审批门控需要重新思考

Claude 仍然可能在网页内容中遇到提示词注入，或者被重定向到意外位置，这就是为什么 Anthropic 建议在具有最小权限的隔离容器或虚拟机中运行浏览器的原因。除非需要，否则应禁用 JavaScript 和文件上传，因为 Claude 生成的代码会以页面的权限运行，并且可以触达数据或向该页面发出请求。

批处理使得审批变得更加复杂，因为多个操作可以同时到达，而序列开始时的常规点击最终可能会导致需要用户许可的操作。这意味着执行器必须在操作发生时进行检查，并在需要时停止以等待批准。