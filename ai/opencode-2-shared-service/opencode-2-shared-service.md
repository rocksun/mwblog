<!--
title: OpenCode 2.0 重磅发布：统一终端、桌面与网页端服务的架构大升级
cover: https://cdn.thenewstack.io/media/2026/10/90780031-resource-database-okp1iau3ubg-unsplash-scaled.jpg
summary: 开源编码智能体 OpenCode 发布 2.0 版本，迎来架构重大升级。新版本通过共享后台服务连接终端、桌面与网页端，重构了 API 并引入嵌入式 SDK，同时支持“代码模式”和后台并发执行，全面提升开发灵活性。
-->

开源编码智能体 OpenCode 发布 2.0 版本，迎来架构重大升级。新版本通过共享后台服务连接终端、桌面与网页端，重构了 API 并引入嵌入式 SDK，同时支持“代码模式”和后台并发执行，全面提升开发灵活性。

> 译自：["A major overhaul": OpenCode 2.0 puts its terminal, desktop, and web apps on one shared service](https://thenewstack.io/opencode-2-shared-service/)
> 
> 作者：Paul Sawers

[OpenCode](https://opencode.ai/) 2.0 在其[公开测试版发布](https://web.archive.org/web/20260710181539/http://v2.opencode.ai/)大约三个月后，于今天正式全面推出。这次意义重大的架构升级引入了一个共享后台服务，将终端、网页和桌面界面连接起来，同时还重建了 API、推出了新的可嵌入 SDK，并支持在后台运行子智能体和 shell 命令。

在其周一发布的一篇[博客文章](https://anoma.ly/notes/opencode-2-0/)中，开源编码智能体背后的公司 [Anomaly](https://anoma.ly/) 将这次发布称为“重大大修”，并补充说它借鉴了“数百万日常用户”的经验，构建了一个能够支持不断扩展的智能体功能的适应性更强的系统。

事实上，Anomaly 在过去几个月里一直在迭代 2.0 版本，包括在 9 月份[发布了关于其](https://anoma.ly/notes/opencode-reloaded/)经改进的插件架构和热重载功能的详细技术说明。然而，漫长的推出过程给开发者带来了一些困惑，甚至在不断发布更新的同时，也出现了[关于 2.0 版本](https://www.reddit.com/r/opencode/comments/1wppj69/is_opencode_v2_officially_in_a_stable_release/)是否正式稳定的疑问，以及[对缺少发行说明的抱怨](https://github.com/anomalyco/opencode/issues/52184)。

周一的公告，以及官方更新日志转向 [2.x 系列](https://opencode.ai/changelog)，实际上标志着版本 2 现在成为了 OpenCode 的主要发行版。与此同时，该公司还对升级背后的技术决策做出了更广泛的解释。

## OpenCode 的发展历程

![OpenCode 是一个开源编码智能体。](https://cdn.thenewstack.io/media/2026/10/d69ae913-generalgif.gif)

*OpenCode 是一个开源编码智能体。*

简而言之，OpenCode 的起源可以追溯到无服务器（serverless）开发的世界。Anomaly 的创始人 [Jay V](https://www.linkedin.com/in/jayair/) 和 [Frank Wang](https://www.linkedin.com/in/fanjiewang/) 之前曾创建了 Serverless Stack ([SST](https://sst.dev/))，这是一个用于在亚马逊云科技（AWS）上构建和部署应用程序的开源框架。OpenCode 开发中的另一位杰出人物 [Dax Raad](https://x.com/thdxr) 也是 SST 团队的一员。

自 2025 年首次亮相以来，OpenCode 在寻求对其编码工具背后的 AI 模型有更大自由度的开发者中获得了狂热的追随者。1 月份这一需求变得尤为迫切，当时[Anthropic 开始阻止](https://venturebeat.com/technology/anthropic-cracks-down-on-unauthorized-claude-usage-by-third-party-harnesses)第三方智能体使用 Claude Pro 和 Max 订阅凭证，迫使受影响的开发者寻找访问 Claude 的替代方法或更换提供商。

正如 Janakiram MSV 5 月份在 *The New Stack* 上[报道](https://thenewstack.io/anthropic-claudecode-opencode-split/)的那样，这些限制与对 OpenCode 激增的兴趣不谋而合，OpenCode 允许开发者在相互竞争的 AI 模型之间进行切换。今天，[OpenCode GitHub 仓库](https://github.com/anomalyco/opencode)已经累积了超过 21,000 个 star 和近 30,000 个 fork。

更广泛地说，有迹象表明[商业对这一类别](https://thenewstack.io/open-source-coding-agents-like-opencode-cline-and-aider-are-solving-a-huge-headache-for-developers/)编码智能体的兴趣正在增长。7 月份，[Anaconda 收购了 Kilo](https://thenewstack.io/anaconda-kilo-open-source-acquisition/)，这是另一个类似的开源编码智能体，允许开发者选择他们首选的 AI 提供商。有趣的是，Kilo 已经使用 OpenCode 重建了其命令行界面和 VS Code 扩展，这展示了后者如何在其他开发工具内部找到一席之地。

随着 2.0 版本的发布，Anomaly 阐述了它*如何*重构 OpenCode 的底层架构以适应更广泛的用例。可以说，最重要的变化涉及编码智能体如何运行，以及它的不同界面如何与其连接。

## 一个服务，多个界面

Anomaly 表示，客户端/服务器设置的底层结构从一开始就存在于 OpenCode 中，尽管除了高级用户之外，很少有人特意去使用它。

随着 2.0 版本的发布，服务器现在作为开发人员机器上的单个后台进程自动启动，允许 OpenCode 的终端、浏览器和桌面界面与相同的底层服务进行通信。

这意味着开发者可以通过不同的界面访问和管理他们的编码会话，而服务则处理底层的执行。使用 OpenCode 编程客户端构建的脚本也可以自动发现并连接到本地服务，这使其对计划任务很有用，同时开发者还可以将服务暴露给其他机器并将其与外部应用程序配对。

> “开发人员现在可以在 OpenCode 的终端界面中启动会话，通过桌面或网页应用继续工作，并让他们自己的脚本连接到相同的底层服务”。

简而言之，开发人员现在可以在 OpenCode 的终端界面中启动会话，通过桌面或网页应用继续工作，并让他们自己的脚本连接到相同的底层服务。

![一个服务，多个界面](https://cdn.thenewstack.io/media/2026/10/0fd446f4-gif1.gif)

*OpenCode 的共享后台服务*

这些架构变化伴随着对 OpenCode API 的彻底重新设计，Anomaly 承认该 API 是在行业仍在摸索阶段时拼凑构建的。

该公司在其博客文章中写道：“随着我们和全世界共同了解智能体是什么以及应该是什么，旧的 API 杂乱无章地生长起来。”“这很糟糕。”

> “随着我们和全世界共同了解智能体是什么以及应该是什么，旧的 API 杂乱无章地生长起来。这很糟糕。”

因此，新的 API 赋予了智能体对其自身环境更大的控制权。例如，它可以为新任务创建一个 Git 工作树（worktree），将现有的会话传输到该工作树中，或者识别并中断另一个陷入卡住的会话。开发者还可以通过新的 `@opencode/client` 包访问 API，该包支持标准的 JavaScript 和 Effect。

![智能体管理它们自己的会话](https://cdn.thenewstack.io/media/2026/10/5a7dce35-gif2.gif)

*智能体管理它们自己的会话*

另一个新增功能是可嵌入的 [SDK](https://opencode.ai/v2/docs/build/sdk)（分发为 `@opencode/sdk`），它允许开发者将 OpenCode 直接整合到他们自己的应用程序中。该公司指出，它使用与 OpenCode CLI 相同的底层代码，使开发者能够为服务器或诸如 Cloudflare Durable Objects 等环境创建智能体的定制版本。

这些实现可以通过其标准的服务器协议与现有的 OpenCode 客户端进行通信，尽管 Anomaly 表示该 SDK 仍在开发中。

## 代码模式与后台执行

OpenCode 2.0 还改变了智能体通过[模型上下文协议](https://thenewstack.io/model-context-protocol-roadmap-2026/) (MCP) 与外部工具交互的*方式*。

一项被称为代码模式（Code Mode）的功能允许智能体编写 JavaScript，以在单次执行中调用多个工具并处理它们的结果。它围绕 `@opencode/codemode` 包中的轻量级 JavaScript 解释器构建，将 MCP 服务器和 OpenAPI 端点转换为智能体可以通过编程调用的函数。

例如，智能体可以从 GitHub 检索错误报告，提取相关信息并在 Linear 中创建相应的工单，而不必为每个操作单独进行一次模型往返。

对于将智能体连接到大量外部服务的开发者来说，其影响尤其重大，因为工具定义可能会消耗模型可用上下文的大部分。Anomaly 将代码模式设为 2.0 版本中所有 MCP 服务器的默认设置，认为这使得广泛的集成更加实用。

该公司写道：“这意味着你可以添加数千个工具而只需极少的上下文膨胀，你的智能体会发现并组合它们来完成工作。”

![代码模式连接 MCP 工具](https://cdn.thenewstack.io/media/2026/10/3bfce0e7-gif3.gif)

*代码模式连接 MCP 工具*

与此同时，OpenCode 正在为子智能体和 shell 命令引入后台执行功能，允许开发者在进行其他操作的同时继续与主智能体交互。

例如，开发者可以将代码审查委托给运行不同 AI 模型的子智能体，同时继续处理主要任务。类似地，冗长的 shell 操作（例如运行测试或构建应用程序）可以异步执行，主智能体在它们完成时会收到通知。

如果某个前台任务花费的时间比预期长，开发者还可以使用键盘快捷键将其移至后台。

![子智能体和命令并发运行](https://cdn.thenewstack.io/media/2026/10/c9bda033-gif4.gif)

*子智能体和命令并发运行*

完善此次发布的还有对 OpenCode 插件架构的更改。Anomaly 表示，它已经实现了 80 多个内部插件，涵盖了 2.0 版本中引入的大部分功能，这是提高其插件 API 可靠性和可维护性的一项努力。

终端界面插件也已从实验性升级为稳定版，而热重载支持意味着 OpenCode 可以在活动会话期间创建并开始使用新插件，而无需重新启动。

然而，这对现有用户产生了一些兼容性影响。为 OpenCode 1.0 开发的插件将无法与 2.0 版本一起使用，而围绕前一个服务器 API 构建的集成将需要更新。

现有的 OpenCode 1.x 用户可以通过在命令行运行 `opencode upgrade --major` 或在终端界面中输入 `/update` 来升级到 2.0 版本。根据 [10 月 11 日的发行说明](https://github.com/anomalyco/opencode/releases/tag/v1.19.0)，更新不再自动安装，这意味着用户必须自行发起升级。