"每个人都不必拥有完全相同的 Claude 体验"：Anthropic 的模组让你能够改变 Claude Code 的外观和行为

长期以来，开发者一直能够通过[设置](https://code.claude.com/docs/en/settings)、[`CLAUDE.md`](https://code.claude.com/docs/en/memory) 中的持久化指令、[钩子（hooks）](https://code.claude.com/docs/en/hooks-guide)以及 [MCP 服务器](https://code.claude.com/docs/en/mcp)来根据自己的偏好定制 Claude Code，同时还可以进行[状态栏](https://code.claude.com/docs/en/statusline)和[输出样式](https://code.claude.com/docs/en/output-styles)等微调。这些控件可以塑造 Claude 遵循的指令、它的权限、它可以使用工具等等——但它们无法改变 Claude Code 自身的特性或其界面的其余部分。

然而，现在 [Anthropic 正在给开发者](https://claude.com/blog/claude-code-mods)通过[模组（mods）](https://code.claude.com/docs/en/plugins/mods/overview)对 Claude Code 进行更深入的控制，这些模组是小型 JavaScript 或 TypeScript 函数，可以钩入 Claude Code 内部的事件。一个模组可以在提示词到达模型之前重写它、阻止或重写工具调用、处理权限请求、替换 Claude Code 界面的某些部分，或者添加全新的功能。

> “每个人工作的方式都不同，所以没有理由让每个人都拥有相同的 Claude 体验。”

## 改变 Claude Code 的外观和行为

Claude Code 的创造者 [Boris Cherny](https://www.linkedin.com/in/bcherny/) 周四在 X（原推特）上发文，将模组描述为开发者通过简单的提示词重塑 Claude 的外观和行为的一种方式，并能够将这些自定义打包为其他用户可以安装的插件。

Cherny [写道](https://x.com/bcherny/status/2105756563302723721)：“每个人工作的方式都不同，所以没有理由让每个人都拥有相同的 Claude 体验。”

这可以包括改变 Claude Code 在工作时显示的内容。例如，模组可能会浮现实时信息，例如 Claude 发出的工具调用次数、它运行的时间以及它消耗了多少 Token，然后在任务完成后呈现摘要。

![实时智能体活动](https://cdn.thenewstack.io/media/2026/10/748b9fbf-gif1.gif)

*实时智能体活动*

在消息公布后的几个小时内，用户就已经在尝试更多专业化的用途。一位软件开发者[构建了一个模组](https://x.com/sean_snd/status/2105965372956623126?s=20)，用于将凭证传递给 Claude，而不会将底层秘密（secret）留在对话历史记录中。

## Claude Code 模组的工作原理

事实上，模组的公开筹备工作已经进行至少一个月了。Anthropic 于 [9 月 3 日](https://github.com/anthropics/claude-code/issues/91870)在 GitHub 上首次提出了这个想法，当时使用的是更具技术性的名称“函数钩子（function hooks）”，并就一个允许 JavaScript 和 TypeScript 函数拦截 Claude Code 内部事件的 API 征求开发者的反馈。六天后，该公司表示计划在近期以“Claude Mods”的重新品牌推出该功能，同时保留函数钩子作为底层机制。

模组现在已在 Claude Code 2.1.287 及更高版本中默认启用。由于模组的代码在整个会话期间保持活动状态，因此它可以记住事件之间的数据，并在事情发生时与 Claude Code 交互。这使得构建实时更新的界面元素、启动进程、添加命令或向模型公开新工具成为可能。Anthropic 表示，它已经将模组用于包括 `AGENTS.md` 支持和 `/diff` 窗格在内的功能，并在 Claude Code 仓库中发布了它们的源代码。

> “这使得模组成为让 Claude Code 适应你工作方式的一种途径。”

在随发布附带的一篇[技术博客文章](https://claude.dev/blog/getting-started-with-claude-code-mods/)中，Anthropic 的技术人员 [Addy Osmani](https://www.linkedin.com/in/addyosmani/) 承认，开发者已经可以通过各种机制自定义 Claude Code。然而，他表示模组使他们能够控制 Claude Code 自身行为和界面，其模块可响应会话期间的事件，并可更改或替换 Claude Code 的操作。

Osmani 写道：“这使得模组成为让 Claude Code 适应你工作方式的一种途径。”

在一个示例中，Osmani 介绍了一个大约 80 行名为 *Token Weather*（Token天气）的模组，它跟踪了 Claude 的上下文窗口消耗了多少，并在提示词上方的带区中显示结果。随着 Claude 读取更多文件，显示内容从 200,000 Token窗口的 18% 处的“晴朗（Clear）”移动到 67% 处的“阵雨（Showers）”，最后到 81% 处的“风暴（Storm）”，同时也显示了最近的使用情况以及最新一轮添加了多少 Token。

![Token Weather 跟踪上下文使用情况](https://cdn.thenewstack.io/media/2026/10/dab94512-gif4.gif)

*Token Weather 跟踪上下文使用情况*

鉴于模组是以插件形式分发的，开发者可以通过相同的插件机制（包括来自 GitHub 上的仓库）发布它们。然而，这确实带来了一个安全考量：模组代码通过 Claude Code 在本地执行，并可访问开发者的机器，因此 Anthropic 建议检查源代码并仅安装来自受信发布者的代码。

不过，对于团队而言，模组继承了 Claude Code 现有的插件控件，而 Team 和 Enterprise 用户以及具有托管设置的机器会在用户安装的模组之前加载 Anthropic 的 `sec-default` 防护。默认情况下，这会阻止这些模组覆盖权限拒绝规则；在这些受保护的环境之外，模组可以覆盖某些权限决策。

模组现已在 Claude Code CLI 和桌面应用程序中可用，可以通过插件市场（包括 GitHub 仓库）进行安装或共享。