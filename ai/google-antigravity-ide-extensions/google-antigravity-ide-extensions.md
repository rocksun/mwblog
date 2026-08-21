<!--
title: Google AI编程助手Antigravity正式走出专属IDE，全面集成至主流开发工具
cover: https://cdn.thenewstack.io/media/2026/03/10fa0e9b-summerizze-lzqqcet_dwm-unsplash-scaled.jpg
summary: Google将Antigravity AI编程助手扩展至VS Code、JetBrains等主流IDE，简化企业开发工作流。同时引入企业级额度管理与安全策略，通过IAM与VPC控制防范风险，但需警惕高昂的Token消耗成本。
-->

Google将Antigravity AI编程助手扩展至VS Code、JetBrains等主流IDE，简化企业开发工作流。同时引入企业级额度管理与安全策略，通过IAM与VPC控制防范风险，但需警惕高昂的Token消耗成本。

> 译自：[Google's AI coding agent just escaped its own IDE](https://thenewstack.io/google-antigravity-ide-extensions/)
> 
> 作者：Amanda Caswell

当 Google 在 2025 年 11 月推出 Antigravity 时，其前提是开发者可以将整个编码任务交给 AI 代理并让其自动运行。但开发者仍然需要直接在他们的代码编辑器中工作。

Google 周四宣布，通过为 Visual Studio Code、Visual Studio、JetBrains IDE 和 Zed 开发的新扩展，将 Antigravity 扩展到开发者现有的工作流程中。该公司还通过符合条件的 Gemini Enterprise 订阅提供 Antigravity。

这些扩展程序允许开发者在侧面板中打开代理对话，查看内联差异（inline diffs），检查计划并委派多步骤工程任务，而无需将项目移至 Antigravity 2.0 桌面应用程序。同一个 Antigravity 账号可以在每个环境中使用，因此用户不必单独登录或管理许可证。

## 每个 IDE 内部的代理

VS Code 扩展现已通过 Microsoft 扩展市场在 macOS、Linux 和 Windows 上提供，而 Visual Studio 2026 和 .NET 解决方案的扩展目前处于预览阶段。Google 还从 2026.2.1 版本开始支持 JetBrains 套件（包括 IntelliJ IDEA、PyCharm、WebStorm、GoLand、CLion 和 Rider），以及 Zed。

在开发者选择的编辑器中与他们会面，使得 Google 能够更容易地进入企业工程团队，因为这些团队的人员很少使用完全相同的设置。

## 企业预算与护栏

管理员可以为使用 Gemini Enterprise Standard、Plus 或 Standard Emerging Market 计划的员工开启 Google 的开发工具。他们还可以为每个 Google Cloud 项目设置月度支出上限。当包含的配额用完时，Antigravity 会关闭或切换到按使用付费的定价模式。Google 表示，针对个人用户和团队的控制功能将在今年晚些时候推出。

在此之前，同一版本、项目和区域中的每个人都从一个共享的额度池中扣除。Google 将这种配额解释为每月配额，但使用滚动式的七天周期进行计量。池重置时，剩余的任何额度都会消失。

> 一个非简单的工程任务可能会消耗 150,000 到 200,000 个 Token，而多代理交接会在工作在代理之间传递时增加更多的输入 Token。

## Token 支出迅速膨胀

该配额可能会很快用完。一个非简单的工程任务可能会消耗 [150,000 到 200,000 个 Token](https://thenewstack.io/agentic-ai-token-costs/)，而多代理交接会在工作在代理之间传递时增加更多的输入 Token。最近发现一个内置的 Claude Code 技能在回答问题前会[加载超过 200,000 个 Token](https://thenewstack.io/claude-code-token-reduction/)。如果没有为每位开发者分配默认额度，一个重度依赖代理的工作流程可能会在数小时内烧掉团队的整个额度池。

Google 并不是第一个面临这个问题的供应商。Microsoft 最近在发现其许多工程师每月在 Token 上花费数百到数千美元后，为旗下工程部门引入了 [AI Token 预算](https://thenewstack.io/microsoft-copilot-token-budgets/)。据报道，Uber 在 2026 年的前四个月就[用光了其全年的 AI 编程预算](https://thenewstack.io/microsoft-copilot-token-budgets/)。Amazon 内部一个旨在将作者记录与产品列表匹配的项目，其预算超支了 860%。

## 安全策略遵循身份验证

企业开发者使用公司凭据登录，然后选择 Antigravity 应该使用的 Google Cloud 项目和区域。组织可以通过 Workforce Identity Federation 连接到其现有的身份提供商，而开发者也可以使用应用程序默认凭据进行身份验证。

身份验证后，代理会话会继承组织的 IAM 策略、VPC 服务控制和区域数据边界。Google 表示，来自企业 Antigravity 会话的数据不会用于训练其基础模型。

> 一旦这些连接触及生产系统，错误的设置可能会产生严重后果。

管理员可以限制代理的工作区、阻止浏览器访问，并决定它可以使用哪些 MCP 服务器。一旦这些连接触及生产系统，错误的设置可能会产生严重后果。例如，ElevenLabs 的 MCP 服务器允许 Claude [从聊天窗口中删除生产环境中的语音代理](https://thenewstack.io/elevenlabs-mcp-voice-agents/)。这种拥有权限的连接必须像处理任何其他特权访问一样对待。

将 Antigravity 放入现有的编辑器中，使得 Google 能够在不要求全公司进行工具变更的情况下将代理引入开发者的机器，同时 Gemini Enterprise 确保每个会话都绑定到相同的策略和项目预算，无论它是在 VS Code 还是 JetBrains 中启动。开发者可以切换编辑器，而无需更改代理可以访问的内容或其使用量的计费方式。

> 扩展程序让 Antigravity 进门；控制平面决定了它进入后能做什么。