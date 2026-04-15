<!--
title: Anthropic 重构 Claude Code 桌面应用：Token 消耗速度再创新高
cover: https://cdn.thenewstack.io/media/2026/04/4ee2d757-img_0972-scaled.jpg
summary: Anthropic 推出 Claude Code 桌面应用重大更新，新增集成终端、侧边聊天及可自定义布局，旨在提升 Agent 编程协作体验，让开发者更高效地管理并发任务并消耗 Token。
-->

Anthropic 推出 Claude Code 桌面应用重大更新，新增集成终端、侧边聊天及可自定义布局，旨在提升 Agent 编程协作体验，让开发者更高效地管理并发任务并消耗 Token。

> 译自：[Anthropic's redesigned Claude Code desktop app lets you burn through tokens even faster](https://thenewstack.io/claude-code-desktop-redesign/)
> 
> 作者：Frederic Lardinois

你可能觉得 Claude Code 的一项重大更新已经足够了，但在周二，Anthropic 不仅发布了 [Claude Code 运行流程](https://thenewstack.io/claude-code-can-now-do-your-job-overnight/)，还为其编程 Agent 推出了[全新的桌面端体验](https://claude.com/blog/claude-code-desktop-redesign) —— 对整体 [应用](https://claude.com/download) 也进行了些许细微调整。

正如 Anthropic 描述的那样：“新应用是为当下的 Agent 编程感官而构建的：多个任务同时进行，而你稳坐调度员席位。”

这意味着你现在可以更轻松地查看所有当前和最近的任务会话，重点在于管理 Agent 处理多个仓库及跨仓库的工作。当你需要在 Agent 工作期间提问时，现在可以打开一个了解主上下文的侧边聊天窗口，且不会在 Agent 工作时干扰它（你可以通过 `⌘` `+` `;` 或 `Ctrl + ;` 启动这些侧边聊天）。

![](https://cdn.thenewstack.io/media/2026/04/014adbbd-anthropic-side-chat.png)

## Claude 专属终端

其中一个重磅功能是 OpenAI Codex 用户非常熟悉的：更新后的 Claude 应用首次配备了集成终端。这也是我在两个编程 Agent 之间切换时一直感到缺失的功能 —— 尤其是考虑到我的 Claude Token 似乎正以越来越快的速度耗尽。

> “新应用是为当下的 Agent 编程感官而构建的：多个任务同时进行，而你稳坐调度员席位。”

同样新增的还有改进的 Diff 视图器，Anthropic 表示它已“针对大型变更集的性能进行了重构”。Anthropic 还添加了用于快速编辑的应用内文件编辑器，以及在应用内打开 HTML 和 PDF 文件的功能。

一个非常棒的功能是你可以在需要时重新排列所有可选面板（预览、计划、Diff、任务、终端）和主聊天面板。例如，你可能想在查看 Agent 构建的内容时专注查看 Diff 视图，而将聊天窗口放在一边。

OpenAI 的 Codex 应用不允许移动面板（例如，终端始终位于窗口底部），但其 Diff 视图与 Claude Code 相比仍有一些优势。它可以占据 Codex 窗口的大部分，此外还提供了更多选项，包括在统一 Diff 和拆分视图之间切换。Claude Code 目前仅提供统一视图。

与之前一样，Claude Code 适用于所有 Claude 付费订阅用户，以及那些更喜欢通过 API 按需支付 Token 费用的用户。

## 更快、更可靠的应用

即使你不是 Claude Code 用户，这次更新后的应用看起来也可能有些陌生。原本顶部用于在对话（Chat）、协作（Cowork）和代码（Code）之间切换的模态框，现在移到了侧边栏，并且只包含三个图标，不再有之前切换器的文字标记。

团队还表示，他们为了“可靠性和速度”重构了应用，“现在会在 Claude 生成回复时实时流式输出”。在体验了几分钟更新版本后，你肯定能明显感觉到这一点。