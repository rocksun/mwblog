![屏幕显示代码的开发者](https://cdn.thenewstack.io/media/2026/11/57fc2d31-rizki-ardia-i-aetokirtk-unsplash-1024x753.jpg)

OpenCode 开发者 Dax Raad 表示，他仅花费 60 美元就用 Rust 重写了该项目的浏览器自动化工具，替换了其中实际使用的 Playwright 和 Patchright 部分，并大幅降低了内存占用。

## 仅 4.3 MB 的二进制文件

[他](https://thdxr.com/)于[周六在 X 平台](https://x.com/thdxr/status/2121692397323350468)公布的数据令人瞩目。新的 Rust 二进制文件大小仅为 4.3 MB，而之前的 Node 版本则高达 53 至 64 MB。在经过几次调用后，每个 [OpenCode Browse](https://github.com/anomalyco/browse) 连接器的内存占用也从大约 190 MB 降至 5.6 MB，降幅约 97%。

> 新的 Rust 二进制文件大小仅为 4.3 MB，而之前的 Node 版本高达 53 至 64 MB。

将 AI 编程智能体连接到浏览器的中继服务也展现出类似的差距。根据 Raad 的对比数据，Rust 实现在空闲时内存占用为 6 MB，处理调用后为 6.6 MB；而旧版 Node 中继服务在运行六天后占用高达 353 MB。

## 替换 Playwright 和 Patchright

OpenCode Browse 通过 Chromium 扩展程序和 [MCP 服务器](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/)，将 AI 编程智能体连接到开发者现有的浏览器。此前的 Node 实现使用 Playwright 进行浏览器自动化，并借助 Patchright 来降低被检测的风险，但 Raad 用 Rust 重写了 Browse 所需的功能，以减少运行时开销。

> Raad 用 Rust 重写了 Browse 所需的功能，以减少运行时开销。

新的 Rust 中继服务通过 WebSockets 与 Chromium 扩展程序通信，并使用 Chrome DevTools Protocol 来处理浏览器操作、智能体会话、录制和网络抓包。它还内嵌了 QuickJS，用于执行智能体提供的 JavaScript，从而不再依赖此前的 Node 运行时。

## 拉取请求详情

[已合并的拉取请求](https://github.com/anomalyco/browse/pull/264)显示，Raad 替换了基于 Node 的 CLI 和中继服务，同时保留了现有的 Chromium 扩展程序，并使用 Chrome DevTools Protocol 执行浏览器操作。

团队使用约 10 个回归测试智能体在真实的 Chrome 浏览器上进行了两轮测试。Browse 在 Stealth Bench v2 上的得分为 85%，而 Browser Use Cloud 为 90.5%，不过该拉取请求中并未包含旧版 Node 实现的得分。

并非所有功能都被纳入了这次重写；Raad 放弃了时区和区域设置模拟，以及被 Chrome 扩展程序禁用的下载工具。Rust 版本还遗留了 Node 实现中的一个问题，即无法通过扩展程序停止处于忙循环中的 eval 执行。

Browse 依然保留了中继认证、扩展程序配对和源站限制，智能体也仅限于访问其自行打开或用户明确共享给它们的标签页。

## 60 美元成本背后的真实代价

Raad 表示这次重写“仅花费了 60 美元”，并在 X 平台的回复中确认，他使用了 Claude Opus 作为主力编程模型，并用 DeepSeek 作为子智能体。

这两个模型帮助他替换了 Browse 所需的 Playwright 和 Patchright 功能，尽管 60 美元的成本并未计入他在检查、测试和修复代码上花费的时间。[Rust 重写的挑战](https://thenewstack.io/is-a-rust-rewrite-really-worth-it/)在于，既要找到能匹配原有功能的更轻量级替代方案，又不能带来额外的维护工作量。

> 60 美元的成本并未计入他在检查、测试和修复代码上花费的时间

内存节省固然令人印象深刻，但 Raad 也因此承担起了此前由 Playwright 和 Patchright 维护的代码责任。他的团队还将不得不自行处理浏览器更新、认证变更以及此前通过这些库获得的安全修复。这正是 [AI 生成的技术债务](https://thenewstack.io/ai-technical-debt-verification/)可能演变成问题的地方，尤其是当生成代码变得廉价、但维护却需要付出多得多的精力时。

本文[《Dax Raad 花费 60 美元用 Rust 重写浏览器工具，随后内存占用骤降 97%》](https://thenewstack.io/opencode-browse-rust-rewrite/)首发于 [The New Stack](https://thenewstack.io)。