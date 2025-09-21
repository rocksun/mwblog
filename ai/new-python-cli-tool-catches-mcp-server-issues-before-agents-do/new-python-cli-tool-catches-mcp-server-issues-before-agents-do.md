<!--
title: 全新Python命令行工具：在Agent之前捕捉MCP服务器问题
cover: https://cdn.thenewstack.io/media/2025/09/ac402d55-planet-volumes-j9_nr93trv4-unsplashb.jpg
summary: 微软研究院的 MCP Interviewer 是一个开源 CLI 工具，用于帮助开发者构建和维护 MCP 服务器。它可以自动检查 MCP 服务器是否符合约束，进行功能测试和 LLM 评估，并生成报告。该工具旨在确保 MCP 服务器在各种代理客户端上可靠地工作，但目前仍是一个实验性项目。
-->

微软研究院的 MCP Interviewer 是一个开源 CLI 工具，用于帮助开发者构建和维护 MCP 服务器。它可以自动检查 MCP 服务器是否符合约束，进行功能测试和 LLM 评估，并生成报告。该工具旨在确保 MCP 服务器在各种代理客户端上可靠地工作，但目前仍是一个实验性项目。

> 译自：[New Python CLI Tool Catches MCP Server Issues Before Agents Do](https://thenewstack.io/new-python-cli-tool-catches-mcp-server-issues-before-agents-do/)
> 
> 作者：Steven J. Vaughan-Nichols

想充分利用 MCP 吗？你应该看看微软研究院的 MCP Interviewer。

[模型上下文协议 (MCP)](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) 已经迅速成为一个非常流行的开放标准，用于将 AI 代理与外部数据和服务连接起来。这很棒，但是如何确保你的服务器可以与 MCP 正常工作呢？来看看微软研究院的 [MCP Interviewer](https://github.com/microsoft/mcp-interviewer)。

MCP Interviewer 是一个开源（在 MIT 许可下）的 CLI 工具，旨在帮助开发人员构建和维护 MCP 的服务器。具体来说，它是一个 Python CLI 工具，使你能够在你的代理遇到问题之前捕获 MCP 服务器问题。

该程序为 MCP 服务器实现提供自动检查、功能测试、代理评估和深入报告。该工具对服务器的工具、提示、资源和能力模式进行编目，使用统计数据和直接交互来突出显示合规性，检测约束违规，并揭示代理 AI 系统的可用性问题。

其主要特点是：

* 约束检查：自动检查 MCP 服务器是否符合提供商约束（例如 OpenAI 工具限制和命名约定），帮助开发人员避免部署陷阱。
* 功能测试：使用大型语言模型代理（例如 GPT-4.1）创建和执行测试计划，以交互方式执行服务器工具，并详细记录成功、错误和性能指标。
* LLM 评估：可选地通过 LLM 应用自然语言评估标准来评估工具可用性和功能输出，从而显示代理兼容性并检测模糊或误导性的工具元数据。
* 报告生成：输出人类可读的 Markdown（和 JSON）报告，总结约束违规、统计数据和定性标准评估，以供开发人员和维护人员使用。

微软研究院表示，所有这些的意义在于，随着“代理的激增，我们预计[严重依赖垂直整合的策略不会很好地老化。](https://www.microsoft.com/en-us/research/blog/tool-space-interference-in-the-mcp-era-designing-for-agent-compatibility-at-scale/) 来自不同开发人员或公司的代理将越来越多地相互遇到，并且必须协同工作才能完成任务，这就是我们所说的代理社会。”

MCP 服务器不知道它们正在与哪些客户端或模型一起工作。例如，它们不知道哪些 LLM 可以比其他 LLM 更好地处理长上下文和大型工具空间，并且对常见的提示模式的响应可能大相径庭。因此，虽然 MCP 正在成为将 LLM 驱动的代理连接到业务工具、内容存储库和开发平台上的互操作性层，但 MCP Interviewer 被定位为关键的验证器和调试助手。通过自动化兼容性检查和代理就绪性评估，Interviewer 将使开发人员能够自信地发布和维护 MCP 服务器，这些服务器可以在各种代理客户端上可靠地工作。

另一个问题是，对于某些[模型](http://models.th)而言，大型代理工具空间可能会[使性能降低高达 85%](https://arxiv.org/abs/2505.10570v1)。你看，由于 MCP 没有提供关于工具调用产生多少 token 的指导，因此代理响应可能会淹没 LLM 的上下文窗口。在极端高端，一个工具平均返回 557,766 个 token。这足以淹没几乎任何 LLM 的上下文窗口。MCP Interviewer 工具通过跟踪 MCP 服务器的面向外部的属性，可以帮助避免 MCP 速度减慢甚至彻底失败。

这一切都很好，但是微软研究院提醒我们，MCP Interviewer 仍然是一个实验性项目。目前，你应该手动检查其输出，而不要在生产中使用它。该团队鼓励来自开源和 MCP 社区的反馈和贡献，以进一步完善测试功能、报告和安全标准。也就是说，如果 MCP Interviewer 发展成为一个强大而可靠的程序，它可能会成为任何严肃的 MCP 部署的重要组成部分。