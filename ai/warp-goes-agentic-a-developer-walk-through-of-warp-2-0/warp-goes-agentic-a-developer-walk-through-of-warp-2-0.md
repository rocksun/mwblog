<!--
title: Warp Agentic破界：Warp 2.0开发者全景透视
cover: https://cdn.thenewstack.io/media/2025/07/d3dc7b1b-getty-images-itaxr436zou-unsplashb.jpg
summary: Warp 2.0 终端集成了 agentic 大型语言模型能力，具有选项卡式会话管理和 AI 功能。它使用 Claude 4 Sonnet 模型，支持 Agent 模式，并提供权限控制。Warp 成功完成了 JSON 文件合并任务，并包含代码编辑器。总体而言，Warp 在适应 agentic 时代具有优势。
-->

Warp 2.0 终端集成了 agentic 大型语言模型能力，具有选项卡式会话管理和 AI 功能。它使用 Claude 4 Sonnet 模型，支持 Agent 模式，并提供权限控制。Warp 成功完成了 JSON 文件合并任务，并包含代码编辑器。总体而言，Warp 在适应 agentic 时代具有优势。

> 译自：[Warp Goes Agentic: A Developer Walk-Through of Warp 2.0](https://thenewstack.io/warp-goes-agentic-a-developer-walk-through-of-warp-2-0/)
> 
> 作者：David Eastman

在与 Warp 首席执行官 [Zach Lloyd](https://www.linkedin.com/in/zachlloyd) 进行了一场启发性的 [问答环节](https://thenewstack.io/qa-how-warp-2-0-compares-to-claude-code-and-gemini-cli/) 之后，我已经准备好尝试 [Warp](https://www.warp.dev/) 2.0 的 [agentic 大型语言模型能力](https://www.warp.dev/blog/reimagining-coding-agentic-development-environment)。这感觉很奇怪，因为我大部分时间都在使用 Warp。

我经常写关于 Warp 的文章（参见 [我一年前的原始评论](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/)），但本质上它是一个现代的 [终端模拟器应用](https://thenewstack.io/warp-vs-ghostty-which-terminal-app-meets-your-dev-needs/)。如果你还没有用过其中一个，那你应该试试。Warp 非常适合 agentic 任务，因为它内置了通过选项卡感知多个会话的能力，以及跟踪会话何时停止和重新启动的能力。块结构允许查询和响应之间自然分离。

Warp 始终包含一些基本的 AI 功能，这无疑让一些人感到恼火——重度终端用户通常与 LLM 支持者不在同一个 Venn 图中。LLM 可以尝试根据类似 Unix 命令可能失败的（多种）方式来修复常见问题。

这在一定程度上解释了为什么 Warp 使用略带夸张的营销术语“[agentic development environmen](https://thenewstack.io/agentic-ai-is-quietly-replacing-developers)t”来标记这个更大的产品。实际的版本标签没有给我们任何线索：

[![](https://cdn.thenewstack.io/media/2025/07/ee36a530-image-1024x584.png)](https://cdn.thenewstack.io/media/2025/07/ee36a530-image-1024x584.png)

## Agentic 生活质量

本周早些时候，我列出了 agentic 会话的 [生活质量期望](https://thenewstack.io/expectations-for-agentic-coding-tools-testing-gemini-cli/)，理论上，Warp 在这方面具有优势。终端提示符 UI 已经相当不错：

[![](https://cdn.thenewstack.io/media/2025/07/d5e7d731-image-1-1024x416.png)](https://cdn.thenewstack.io/media/2025/07/d5e7d731-image-1-1024x416.png)

它显示了正在使用的模型（目前是 Claude 4 Sonnet，但如果可以，我会更改为 Opus 4）。提示符处于“自动检测模式”，它可以猜测我是否清楚地用英语书写或使用类似 Unix 的命令。

使用 `cmd-I` 我可以在直接终端模式、代理模式和自动猜测之间切换（左下角的图标）。我们可以看到我们所在的目录和 git 分支。

在做任何事情之前，我将使用 `Settings > AI > Agents > Permissions` 检查权限，以便我可以确定如果放开 AI，它可以做什么。

[![](https://cdn.thenewstack.io/media/2025/07/d18f16ba-image-2-1024x651.png)](https://cdn.thenewstack.io/media/2025/07/d18f16ba-image-2-1024x651.png)

似乎没有办法将活动锁定到一个目录——也许这里没有项目目录的自然概念（如果存在与 [Claude.md](http://claude.md/) 文件等效的文件，我看不到它）。但真正引起我注意的是一个拒绝列表。这是一个非常简单但不错的想法。归根结底，任务是通过 OS 命令执行的，因此在删除文件、生成新 shell 或访问互联网之前，与用户确认权限是明智的。

我将要求 Warp 执行一个简单的合并任务，就像我之前使用 [Gemini CLI](https://thenewstack.io/expectations-for-agentic-coding-tools-testing-gemini-cli/) 和 [OpenAI Codex](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/) 所做的那样。我有两个包含城市信息的 JSON 文件，我想用另一个文件的内容更新第一个文件。

两个 JSON 文件已就位：

[![](https://cdn.thenewstack.io/media/2025/07/b82325f5-image-4-1024x396.png)](https://cdn.thenewstack.io/media/2025/07/b82325f5-image-4-1024x396.png)

好的，现在我准备好请求合并了。这是查询（与我在之前的帖子中提出的查询相同）。我明确地移动到 [agent 模式](https://thenewstack.io/warp-goes-agentic-a-developer-walk-through-of-warp-2-0/) 并询问：

*“请使用文件 updated\_cities.json 的内容更新 JSON 文件 original\_cities.json，但如果 ‘image’ 字段不同，请更新或编写一个新的 ‘imageintended’ 字段，并使用新值”*

[![](https://cdn.thenewstack.io/media/2025/07/337e9fe3-image-5-1024x588.png)](https://cdn.thenewstack.io/media/2025/07/337e9fe3-image-5-1024x588.png)

我不确定未经请求地明确向我展示 [Python](https://roadmap.sh/python) 代码有什么意义。毕竟，我用英语开始了这次对话。但是，浏览一下（以及代码底部的摘要），我没有看到明显的错误。

当它请求权限时，它还会检查是否可以修复尾随逗号。我很高兴它发现了这一点，但它不需要仅仅为此创建一个差异！

我注意到它不太理解工作目录的概念，并且想用绝对路径来完成所有事情。但这可能只是为了让其他工具满意。

最终的总结很好（我测试过的所有模型在这个任务本身上都没有任何实际的实质性问题），再次证明 LLM 理解了问题和上下文：

[![](https://cdn.thenewstack.io/media/2025/07/423d60fe-image-7.png)](https://cdn.thenewstack.io/media/2025/07/423d60fe-image-7.png)

现在，显然存在我向谁付款的问题。Warp 有一个 [付款计划](https://www.warp.dev/pricing)，但我不确定我是否可以直接为使用 Claude Opus 4 向 Anthropic 付款。但我似乎在免费层级上每月有 150 个请求。显示中还没有持续的令牌使用数据——而且当我在应用程序中更改选项卡时我不会“退出”，因此无法在会话结束时显示使用统计信息。

## 代码编辑器

此版本的 Warp 包括一个代码编辑器，该编辑器显然旨在与上述差异一起使用，但您可以为任何代码文件调用它。

如果我列出我的项目文件夹中的文件，我们会看到 Warp 留下了它的合并文件：

[![](https://cdn.thenewstack.io/media/2025/07/f5fbdab5-image-8-1024x216.png)](https://cdn.thenewstack.io/media/2025/07/f5fbdab5-image-8-1024x216.png)

在我的 Mac 上，我左键单击，然后可以在 Warp 编辑器中打开该文件（“使用 Warp 打开”）。它将文件放在一个单独的选项卡中，看起来像上面的差异。它旨在与块中的框架按钮一起使用，但如果没有这些，它会非常稀疏和快速。您可以使用 ⌘-S 保存您所做的任何更改。还有特定于语言的着色。我猜它会在几次下拉后获得一个上下文菜单。

添加文件编辑器可能看起来相当普通，但正如 [Lloyd](https://www.linkedin.com/in/zachlloyd) 在我们的问答中向我提到的那样，它不会以任何方式完全实现（但如果您是 [Zed](https://thenewstack.io/an-introduction-to-zed-ai-and-how-it-compares-to-cursor-ai/)，它仍然代表着一种略微激进的举动）。它确实消除了更换工具的认知摩擦，这很好。

## 结论

一个 agentic 终端应该能够处理更难的请求，其中涉及大量的代码库。但是，因为我提出了非常具体且可完成的请求，所以我最近测试过的所有 agentic 工具都运行得非常好。是的，Warp 有效地呈现了解决方案。

Warp 终端需要添加一些可见的使用统计信息，但正如我所说，它已经有了允许用户保持控制的框架。总的来说，我认为 Warp 处于适应 [agentic 时代](https://thenewstack.io/qa-how-warp-2-0-compares-to-claude-code-and-gemini-cli/) 的有利位置，因为它具有出色的终端传统。