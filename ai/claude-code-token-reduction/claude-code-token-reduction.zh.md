一个旨在帮助开发者使用 Anthropic API 的 Claude Code 技能曾消耗超过 20 万个 Token 来进行加载。Anthropic 表示，随着 Claude Code v2.1.234 的发布，这一数字已降至约 2.5 万个 Token。

这一变化出现在周一更新的 [Claude Code 更新日志](https://code.claude.com/docs/en/changelog)中。Anthropic 将此次降低（将初始上下文成本至少减少了 85.7%）归功于对该技能参考文档的按需加载。在这种情况下，一个捆绑的技能所消耗的 Token 可能比许多编码会话从头到尾消耗的总量还要多。

## 技能预先加载了所有内容

内置的 /claude-api 技能会为使用 Claude API 和托管代理（Managed Agents）的开发者加载参考资料。该技能可以直接调用，但当项目导入 Anthropic 的 Python 或 TypeScript SDK 时，Claude Code 也可以自动激活它。有趣的是，在 Anthropic 记录此修复之前，开发者就已经追踪到了这个问题。

在 [7 月 7 日开启的一个 GitHub Issue](https://github.com/anthropics/claude-code/issues/75197) 中，一位审查 Claude Code 2.1.201 的开发者发现，/claude-api 将其共享参考文件和检测到的语言文档直接嵌入到了技能主体中。报告显示，单次调用中嵌入了约 12 万个 Token 的参考资料。仅一份迁移文档就占了大约 3.6 万个 Token。

> 仅一份迁移文档就占了大约 3.6 万个 Token。

一旦技能的其余部分加载完毕，即使是一个单行的问题，在 Claude 开始回答之前也可能消耗约 20 万个 Token —— 这种隐藏的开销，[正如更广泛的生产级 AI 流水线中所表现的那样](https://thenewstack.io/ai-pipeline-token-optimization/)，只有在有人真正去测量它时才会显现。尽管类似的报告不断涌现，但该问题还是被关闭并标记为“不予计划”（not planned）。

第二个 [8 月 4 日提交的错误报告](https://github.com/anthropics/claude-code/issues/83818)发现了一个代价特别高昂的回退机制。当技能在提示词审计过程中无法检测到项目语言时，它会加载 C#、cURL、Go、Java、PHP、Ruby 和 TypeScript 的文档，以及 26 个共享的 Markdown 文件。这个捆绑目录的大小为 812,650 字节。而复现该任务时，实际上只需要一个 32,954 字节的文件。

一个庞大的本地参考库确实为智能体提供了有用的素材，但将其内联会导致智能体在每次请求时都读取所有 812 KB 的内容，即使其中大部分内容与之无关。

> 一个庞大的本地参考库确实为智能体提供了有用的素材，但将其内联会导致智能体在每次请求时都读取所有 812 KB 的内容，即使其中大部分内容与之无关。

## 上下文窗口在静默中被填满

Anthropic 自己的 [Claude Code 最佳实践指南](https://code.claude.com/docs/en/best-practices)警告称，随着上下文窗口被填满，性能会下降，模型更有可能丢失之前的指令或产生错误。这种模式不仅限于 Claude Code：[AI 编程的“空白支票”时代正在终结](https://thenewstack.io/microsoft-copilot-token-budgets/)，正是因为未受控的 Token 消耗既会降低质量，也会增加成本。

一旦技能加载，其内容就变成了开发者可能永远无法察觉的固定开销，[在企业规模下造成了继承性问题](https://thenewstack.io/speakeasy-enterprise-agent-skills/)。Claude Code 的文档指出，即使开发者可能只看到较小的请求和响应，技能主体在多轮对话中仍会保留在上下文中。

将技能削减至约 2.5 万个 Token，为仓库内容和实际工作留出了更多空间。Anthropic 没有解释 Claude 如何选择加载哪些文档，只是表示参考资料现在是按需获取的。

## 按需加载用读取换取空间

Anthropic 的 [技能文档](https://code.claude.com/docs/en/skills)指出，SKILL.md 应包含核心指令和链接，而 API 规范、示例和其他详细资料应存放在支持文件中，仅在 Claude 需要时才打开。

该指南将加载过程分为三个阶段：始终存在的少量元数据、技能触发时加载的 SKILL.md 主体，以及在任务期间提取的捆绑资源。旧的 /claude-api 行为模糊了后两个阶段，因为它在技能运行时就立即加载了所有参考资料。

> 采用按需加载后，Claude 在识别相关语言或 API 特性后，可能需要额外读取一次文件。

采用按需加载后，Claude 在识别相关语言或 API 特性后，可能需要额外读取一次文件。但它只为与任务相关的材料支付成本，这一点随着 [Agentic 工作流使 Token 成本成为 AI 预算中增长最快的支出项目](https://thenewstack.io/agentic-ai-token-costs/)而变得愈发重要。