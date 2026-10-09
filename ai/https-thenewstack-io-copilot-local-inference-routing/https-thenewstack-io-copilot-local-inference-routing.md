<!--
title: GitHub Copilot走向本地化——但微软对发送至云端的数据闭口不谈
cover: https://cdn.thenewstack.io/media/2026/01/25870d76-screenshot-2026-01-30-at-19.58.20.png
summary: GitHub Copilot即将推出本地与云端模型的自动路由功能，并引入沙盒控制。虽然本地运行降低了对云端的依赖，但微软尚未明确哪些仓库数据会被发送至云端，且模型对硬件内存要求极高，引发了开发者对数据隐私和硬件门槛的关注。
-->

GitHub Copilot即将推出本地与云端模型的自动路由功能，并引入沙盒控制。虽然本地运行降低了对云端的依赖，但微软尚未明确哪些仓库数据会被发送至云端，且模型对硬件内存要求极高，引发了开发者对数据隐私和硬件门槛的关注。

> 译自：[GitHub Copilot is going local — but Microsoft won't say what gets sent to the cloud](https://thenewstack.io/https-thenewstack-io-copilot-local-inference-routing/)
> 
> 作者：Amanda Caswell

**GitHub Copilot 将很快决定编码任务是在本地运行还是发送至云端模型**，预计自动路由功能将在 10 月底前推出。微软周三在一篇由 GitHub 产品经理 [Patrick Nikoletich](https://www.linkedin.com/in/patrick-nikoletich-99a42918/) 和 Windows 平台合作伙伴架构师 [Stuart Schaefer](https://www.linkedin.com/in/stuart-schaefer-43337/) 共同撰写的文章中概述了这一计划。

这一公告与 GitHub 全面推出其新的沙盒控制功能同时发布，但保护措施会根据 Copilot 使用的工具而有所不同。Shell 命令和本地 MCP 服务器享有操作系统级别的限制，而内置的文件工具则依赖于智能体框架内的检查。远程 MCP 服务器仍然位于本地进程沙盒之外。

Nikoletich 和 Schaefer 承认，“本地推理并不意味着会话处于离线状态。”微软尚未透露 Auto 会将多少代码库上下文发送给云端模型，开发者是否能够检查路由决策，或者是否可以限制 Auto 仅进行本地推理。

## Copilot 自行决定推理运行的位置

GitHub 正在扩展 Project HydraFusion（该项目此前已能为编码任务选择模型），以处理这些模型的运行位置。微软表示，Copilot 在本地和云端推理之间进行切换（包括在多轮会话期间）时，会权衡任务上下文和缓存状态。

在 Copilot CLI、Copilot 应用和 VS Code 中，开发者可以使用 Auto 路由或自行选择本地模型。选项包括通过 Windows ML 提供程序运行的 MAI Code 1.1 Flash 以及兼容 OpenAI 的本地端点。

## 自动路由引发质疑

微软尚未说明当 Auto 路由任务时，会向云端发送多少对话历史记录或代码库上下文。它也没有透露开发者是否可以查看这些决策，或将推理限制在本地模型上。制定了严格数据处理策略的团队仍然不知道 Copilot 将哪些代码库数据发送到了云端。上个月也出现过类似的问题，当时 [Anthropic 表示，当检测到较高风险的活动时，它可以将 Claude Sonnet 5.5 的请求路由到 Sonnet 5](https://thenewstack.io/claude-sonnet-cyber-safeguards/)。

> 制定了严格数据处理策略的团队仍然不知道 Copilot 将哪些代码库 data 发送到了云端。

选择本地模型可将推理保留在设备上，但这并不能阻止智能体通过其工具访问外部服务或发出网络请求。需要完全本地会话的开发者还必须锁定这些工具可以访问的内容。

MAI Code 1.1 Flash 是一个拥有 1370 亿总参数和 68 亿激活参数的混合专家模型，微软使用大约每权重的 3.3 位的混合精度量化将其缩小到 53GB，比 bfloat16 云版本减少了 80%。

将模型压缩到更小型硬件上的压力推动了其他领域的类似努力，包括英特尔[进一步压缩 1.58 位 LLM](https://thenewstack.io/intel-bitcos-ternary-compression/) 的工作。微软将量化与投机解码相结合（其中起草器提出 Token 块供主模型验证），以加速本地推理。

> 微软将量化与投机解码相结合（其中起草器提出 Token 块供主模型验证），以加速本地推理。

## 量化与内存限制的碰撞

最初的推出目标是 NVIDIA RTX Spark Windows 电脑（例如 Surface Laptop Ultra），它提供高达 128GB 的统一内存。在该机器上，微软测量到在 256K-token 上下文下，峰值内存使用量达到了 75.5GB，这个数字排除了绝大多数拥有 16GB 或 32GB RAM 的开发者笔记本电脑。

53GB 的权重只是开销的一部分。操作系统、应用程序、推理运行时和键值缓存都需要空间，而且随着智能体读取文件和接收工具结果，缓存会不断增长，因此进行较长会话的开发者需要预算远超模型本身的内存。

## 带有细则的基准测试

微软报告称，量化模型在 SWE-Bench Verified 上的得分为 70.8%（全精度版本为 72.6%），在 Terminal-Bench 2.1 的 89 个任务数据集上表现优于原始版本，得分为 66.29%（原始版本为 62.9%）。在如此小的基准测试中，差距相当于三个任务。这些结果表明该公司在没有牺牲太多编码性能的情况下缩小了模型，但远未证明量化使其变得更好。

Copilot 使用微软开源的执行容器 (MXC) 库来强制执行沙盒策略，在 Windows 上使用 ProcessContainer 后端的 BaseContainer 层，在 macOS 上使用 Seatbelt，在 Linux 上使用 bubblewrap。

启用沙盒后，Copilot 会对 Shell 命令以及受支持的本地 MCP 和语言服务器应用操作系统强制实施的限制。GitHub 表示，无论任务是在本地模型还是云端模型上运行，这些限制都适用。

Copilot 的内置文件工具在智能体进程内部运行，框架根据沙盒策略对请求进行检查，而不是依赖操作系统强制实施的隔离。远程 MCP servers 也位于本地沙盒之外，当启用 MCP 沙盒控制时，Copilot 会检查它们的连接策略。

> 远程 MCP servers 也位于本地沙盒之外，当启用 MCP 沙盒控制时，Copilot 会检查它们的连接策略。

微软的演示使用 MAI Code 1.1 Flash 在沙盒化的 `copilot-sdk` 项目中构建每日分类仪表板，并将其描述为离线工作流。然而，提示词使用的是 GitHub issue 和 Pull Request 元数据，而不是文章前面描述的本地代码库和测试。微软并未说明这些元数据是通过网络检索的还是在本地缓存的，从而使其离线声明未经证实。