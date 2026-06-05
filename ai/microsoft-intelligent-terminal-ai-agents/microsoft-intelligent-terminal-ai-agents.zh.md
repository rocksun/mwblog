经典的老牌终端在最近几个月里迎来了复苏，这在很大程度上要归功于像 Claude Code 这样受欢迎的编程工具。

然而，自终端还是与计算机交互的唯一方式的那个时代以来，终端本身并没有发生太大的变化。

Warp 等工具最近取得了一些进展，它们通常与智能体编程工具结合使用。周二，微软透露，它也在考虑如何通过[推出 Intelligent Terminal（智能终端）](https://devblogs.microsoft.com/commandline/announcing-intelligent-terminal-beta/)来重塑 Windows 11 中的终端。

> 开发者将能够让他们“最喜欢的智能体，无论是 [GitHub Copilot](https://thenewstack.io/github-copilot-token-billing/)、[Claude Code](https://thenewstack.io/claude-code-vs-cursor-vs-codex-vs-antigravity-2026/)、[Codex](https://thenewstack.io/openai-codex-claude-code/) 还是其他智能体”，直接在终端中为他们提供帮助。

这是一个实验性版本，但顾名思义，其核心理念是将智能体直接引入 Shell。微软正从其自家的 GitHub Copilot 开始，但你也可以引入任何兼容智能体通信协议（ACP）的智能体。

正如微软产品管理合伙总监 [Jatinder Mann](https://www.linkedin.com/in/jatinder-mann/) 告诉 *The New Stack* 的那样，这意味着开发者将能够让他们“最喜欢的智能体，无论是 GitHub Copilot、Claude Code、Codex 还是其他智能体”，直接在终端中为他们提供帮助。

> “你在终端里遇到了一个错误，复制它，切换到与你最喜欢的智能体的聊天窗口，粘贴，解释上下文，得到答案，然后再切换回来。这感觉体验是割裂的。”  
> ——微软的 Jatinder Mann

正如 Mann 所指出的，开发者的大部分工作流可能都在终端中，但这并不是当今编程智能体总是存在的地方。“你在终端里遇到了一个错误，复制它，切换到与你最喜欢的智能体的聊天窗口，粘贴，解释上下文，得到答案，然后再切换回来。这感觉体验是割裂的，”Mann 说道。

与 Warp 类似，Intelligent Terminal 可以做到的是——例如，当你运行终端命令或测试应用程序时检测到错误，开发者只需点击一个按钮，智能体就会启动并提供修复建议。它之所以能做到这一点，是因为它理解 Shell 的实时状态。

由于开发者喜欢自定义他们的工作环境，因此该智能体可以显示在后台标签页、侧边栏或页面的底部。而对于那些根本不想与智能体打交道、更喜欢像 2019 年那样从 StackOverflow 复制和粘贴的人来说，他们当然也可以完全关闭该智能体。