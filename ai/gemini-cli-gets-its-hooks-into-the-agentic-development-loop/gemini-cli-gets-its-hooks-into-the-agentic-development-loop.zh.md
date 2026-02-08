Google 已为 [Gemini CLI](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/) [添加](https://developers.googleblog.com/tailor-gemini-cli-to-your-workflow-with-hooks/) 了钩子，它是 Google 基于终端的工具，与 Anthropic 的 Claude Code 竞争。

[钩子](https://geminicli.com/docs/hooks/) 确保 Gemini CLI 在智能体循环内部运行给定的脚本或程序，并为智能体开发循环带来更大程度的控制。例如，这些钩子可用于运行安全扫描器或合规性检查、记录工具交互、将相关信息注入上下文窗口，甚至在运行时动态调整模型的参数。

正如 Gemini CLI 团队在公告中指出的那样，“在智能体时代，效率不仅仅是更快地编写代码；而是构建适应您特定环境的自定义工具。”

![](https://cdn.thenewstack.io/media/2026/01/495a80b2-gemini_cli_hooks_panel.original.png)

Gemini CLI 中的钩子（图片来源：Google）。

虽然开发人员可以尝试指示智能体在提示或 [AGENTS.md](https://agents.md/) 文件中在循环内的特定时间运行特定脚本，但考虑到这些智能体模型的非确定性特性，无法保证这会实际发生，或者智能体不会随着时间的推移忘记这条指令。

## Claude Code 最先实现

如果这听起来很熟悉，那可能是因为您已经了解 Claude Code 钩子，它 [去年九月](https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously) 首次引入了这个概念（不过也有一个 [2025 年 7 月的 GitHub issue](https://github.com/google-gemini/gemini-cli/issues/2779) 提出了这个功能）。Google 的实现与 Anthropic 的并非完全一对一匹配，但将现有 Claude 钩子适配到 Gemini CLI 应该只需要几分钟。

## 设置钩子

与 Claude Code 中的钩子类似，Gemini CLI 也实现了大约 [十几个生命周期事件](https://geminicli.com/docs/hooks/)，钩子可以在这些事件中触发。这可能是在会话开始时，在用户提交提示后但在智能体开始规划之前（例如，用于添加上下文），在选择工具之前（用于优化工具选择或筛选可用工具），以及智能体循环中的类似时刻。

![在 JSON 文件中定义 Google Gemini CLI 钩子。](https://cdn.thenewstack.io/media/2026/01/781ce4d0-screenshot-2026-01-29-at-10.47.25.png)

定义 Gemini CLI 钩子（图片来源：Google）。

钩子被定义为 JSON 文件，这些文件描述了它们何时被调用以及应该运行哪个脚本。这些脚本是标准的 Bash 脚本，Google 指出保持这些钩子快速运行至关重要，因为它们是同步运行的，脚本中的延迟也会延迟智能体的响应。

Google [建议](https://geminicli.com/docs/hooks/best-practices/) 开发人员尽可能使用并行操作和缓存来保持操作的快速性。

钩子一个有趣的用例是利用“AfterAgent”钩子，该钩子在智能体循环结束时触发，以强制智能体进入连续循环来处理困难任务——同时在这些运行之间刷新上下文以避免上下文失效。

至于安全性，需要强调的是，钩子将拥有用户的权限，Google 指出开发人员应该审查任何第三方钩子的源代码。

钩子现已作为 Gemini CLI v0.26.0 更新的一部分提供，也可以打包在 Gemini CLI 扩展中。这是 Google 用于将提示、MCP 服务器、子智能体和智能体技能——以及现在的钩子——打包成一个可共享的单一包的格式。