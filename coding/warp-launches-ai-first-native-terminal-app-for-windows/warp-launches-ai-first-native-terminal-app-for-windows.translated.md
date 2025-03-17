# Warp 为 Windows 推出 AI 优先的本地终端应用

![Featued image for: Warp 为 Windows 推出 AI 优先的本地终端应用](https://cdn.thenewstack.io/media/2025/02/693db2de-warp-windows-feature-feb25-1024x576.jpg)

为 AI 构建的命令行终端应用 Warp 终于登陆 Windows。此前，它仅在 macOS 和 Linux 上可用，但今天的发布大大扩展了其潜在用户群。

我与 Warp 的创始人兼 CEO [Zach Lloyd](https://www.linkedin.com/in/zachlloyd/) 谈论了这一消息。我们还讨论了 [Warp](https://www.warp.dev/) 如何在最近涌现的大量 AI 编码工具中定位自己。事实证明，Lloyd 有着宏伟的计划 —— 他认为 Warp 可以成为“下一代 AI 工具”。

Lloyd 首先指出，Warp 是“一个完全原生的应用程序，所以它不是一个 Electron 应用程序 [并且] 它不是一个 VS Code 克隆。”

“我认为这是人们第一次在 Windows 上获得 100% 原生的 AI 优先的开发者工具，”他说。“我认为这是一件非常重要的事情。Windows 是最大的开发者平台，所以我认为这也很重要。这是我们排名第一的功能请求。”

## Warp 在 Windows 上的构建方式

Warp 最初是使用 Rust 构建的，Lloyd 指出，Windows 版本中 90-95% 的核心代码与 macOS 和 Linux 版本相同。不同之处在于与 Windows 系统集成的代码。

“它与你在 Mac 和 Linux 上获得的体验非常相似，”Lloyd 说，“最大的区别在于它支持 PowerShell，它支持 Git Bash，[并且] 如果你想使用 Linux 的 Windows 子系统，它具有 WSL 支持。”（注意：这些都是 shell 程序，一种允许用户通过键入命令与操作系统交互的程序。）

Lloyd 指出，Warp 花费了“大量时间”来“无缝地与所有这些东西交互，方式与 Windows Terminal 类似，你可以在不同的 shell 环境中启动会话。”

“我们进行所有自己的图形调用；我们必须与 Windows 上的图形驱动程序和事件处理以及所有这些东西集成，”Lloyd 说。它还与 Windows 包管理器 WinGet 集成。

“我们一直在与 Windows 终端团队以及各个工程团队的人员合作，以确保该产品对 Windows 开发人员来说非常棒，”Lloyd 补充道。

## 为什么要更换终端？

许多 Windows 开发人员使用默认的 Windows Terminal 作为其命令行界面，或者他们可能使用 Visual Studio Code 中的内置终端。所以我问 Lloyd，对于那些开发人员来说，切换到 Warp 的理由是什么？

他首先提到了 Warp 中“非常强大的 AI 集成”作为采用 Warp 的理由。

“在 Warp 中，你可以输入 ‘command’ 并像使用常规终端一样使用它，所以它是一个完全向后兼容的终端。但你也可以简单地指示或提示终端你想用英语做什么。因此，如果你正在 […] 设置一个新项目，如果你正在尝试调试生产问题，如果你想代码构建一个功能，你可以简单地用自然语言告诉 Warp —— 比如，嘿，这就是我想做的事情 —— 然后通过不同程度的自主性，以及通过运行终端命令来收集上下文的能力，Warp 将为你完成它。”

Lloyd 指出，AI 集成正日益成为新用户的主要价值主张。但他表示，与普通终端相比，Warp 还具有“一种不同的、重新构想的用户体验”。

> “…在 Warp 的终端中，输入编辑器的工作方式就像你在 IDE 中一样。”
>
> – Zach Lloyd, Warp CEO

“在普通终端中，非常基本的交互对很多用户来说感觉非常奇怪，”他说。“所以，例如，你不能点击并将鼠标光标放在普通终端中的某个位置。在 Warp 的终端中，输入编辑器的工作方式就像你在 IDE 或其他东西中一样。它是一个真正的代码编辑器。你拥有真正的选择支持；你获得自动完成，你获得语法高亮 —— 所有这些东西。所以输入要好得多。”

除了输入之外，Warp 的**输出**也与普通终端不同。Lloyd 说，它是结构化输出，“几乎就像你在使用笔记本或其他东西一样。”这使得 Warp 终端中能够实现更丰富的功能 —— Lloyd 给出了附加 AI 上下文、或过滤过去命令、或与队友分享你所做的事情的例子。

Warp 还有一个内置的知识库，他说，使开发人员团队能够存储和共享模板化的终端命令。

总的来说，Lloyd 说 Warp“应该是 Windows Terminal 的一个直接替代品”。“对于来自该体验的人来说，不应该有任何退步，但它也应该是一个非常非常重要的升级。”

## 终端应用作为 AI 开发工具
在过去的几年里，终端应用已经成为一个令人惊讶的充满活力的开发者工具类别，尤其是在人工智能出现之后。《The New Stack》的两位常驻教程作者对 Warp 进行了评测——David Eastman 测试了 [macOS 版本](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/)，并得出结论，Warp “为你提供了你在命令行上经常认为你会拥有的那种 IDE，但你从未真正拥有过”；而 Jack Wallen 尝试了 [Linux 版本](https://thenewstack.io/warp-is-a-power-users-dream-terminal-for-linux/)，并称其为“高级用户的梦想终端”。

但我们也看到最近出现了一批新的 [AI 编码工具](https://thenewstack.io/self-driving-software-solver-launches-autonomous-ai-coder/)，其中一些——比如 [Bolt](https://thenewstack.io/how-developers-are-using-bolt-a-fast-growing-ai-coding-tool/)、[Windsurf](https://thenewstack.io/windsurf-an-agentic-ide-that-thinks-and-codes-with-you/) 和 Lovable——声称是能够从头开始创建整个应用程序的 [agentic IDE](https://thenewstack.io/beyond-dx-developers-must-now-learn-agent-experience-ax/)。就在本周，Google 发布了一款 AI 编码工具，它提供的 [代码补全次数是其主要竞争对手 GitHub Copilot 的 90 倍](https://thenewstack.io/google-ai-coding-tool-now-free-with-90x-copilots-output/)。

> “…我们希望发挥我们的优势，让终端真正发光 […] 终端更像是一个专业的开发者工具。”

– Lloyd

鉴于所有这些 AI 编码工具的活动，我问 Lloyd Warp 如何适应这个已经拥挤的领域。

“我认为我们希望发挥我们的优势，让终端真正发光，”他回答说。“Bolt 的优点在于你可以在 Web 应用程序中完成所有操作，而且你真的不需要成为一名开发人员。终端更像是一个专业的开发者工具。”

也就是说，由于人工智能，他确实看到 Warp 扩展到做更多的代码生成——这传统上不是终端的领域。

“在 Warp 中，你可以越来越多地让 Warp 编写代码，”Lloyd 说。“它可以创建项目，它可以调试错误。但真正酷的是，由于我们位于堆栈中的位置，它可以跨项目执行——这真的很棒。”

他补充说，在终端中，将代码部署到生产环境更加自然，项目设置也是如此。

> “我们的目标是成为希望使用 AI 的开发人员最高效的界面。”

– Lloyd

“我们的目标真的是成为希望使用 AI 的开发人员最高效的界面，无论是编码还是其他用例。”

他的论点是，因为终端对于专业开发人员来说是一个自然的界面（即使它对大多数其他人来说令人困惑），它可以成为他们与 AI 的默认聊天界面。

“我认为开发看起来不会像人们打开一堆文件并进行代码编辑，”Lloyd 说。“我认为它看起来会像 […] 人们从以下开始：嘿，这是我想完成的事情，让我与你合作来完成它。”

他指出，人工智能已经擅长代码生成，但它会不时地“卡住”。因此，始终需要人类开发人员与 AI 交互。

“所以我认为你想要的是 […] 一个界面，开发人员可以在一个对他们来说很自然的工具中非常容易地跳进去并纠正 AI 正在做的事情。我认为这就是事情发展的方向。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)