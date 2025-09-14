<!--
title: Warp Code：打造现代AI时代的Emacs
cover: https://cdn.thenewstack.io/media/2025/09/ebbedca2-allison-saeng-_co-ldvktke-unsplashb.jpg
summary: Warp Code 旨在打造智能体开发环境，通过灵活视图集成文件树、搜索和更改视图。它允许开发者使用自然语言查询与代码交互，例如通过指定示例文件来增强 Rails 视图。Warp 正在探索构建一个社区“插件”生态系统，以支持更多视图。
-->

Warp Code 旨在打造智能体开发环境，通过灵活视图集成文件树、搜索和更改视图。它允许开发者使用自然语言查询与代码交互，例如通过指定示例文件来增强 Rails 视图。Warp 正在探索构建一个社区“插件”生态系统，以支持更多视图。

> 译自：[Warp Code Gets Closer to an Emacs for the Modern AI Era](https://thenewstack.io/warp-code-gets-closer-to-an-emacs-for-the-modern-ai-era/)
> 
> 作者：David Eastman

我开始使用 Warp 作为我的默认终端已经有一段时间了，因为它有一些有用的工具——例如，显示 shell 命令的运行时间。其他产品也提供可控制的选项卡式终端，但由于 Warp 使用 Rust 从头开始编写了 UI，因此它在速度和有意的设计方面令人印象深刻。从那时起，Warp 大举进军 LLM 集成。最初，我对这个举动没什么兴趣，直到“智能体时代”开始。

随着智能体 CLI 的出现，LLM 突然从 IDE 中走了出来，[走向了不起眼的终端](https://thenewstack.io/learn-to-love-the-command-line-interface-with-agentic-llms/) —— 直接进入了 Warp 的地盘。

总结一下 Warp Code 提供的功能，可以想想完成简单任务所需的各种视图：文件视图、编辑器、差异比较等等。现在，Warp 在你使用 LLM 编码时为你提供这些功能。老一辈的开发人员会记得那个可以“用 Emacs 完成一切”的家伙或妹子。Warp Code 正朝着这个方向发展，我们将在下面与 Warp CEO Zach Lloyd 的访谈中讨论这一点。

## Warp Code 的变化

从我们在 [我对 Warp 2.0 的评测](https://thenewstack.io/warp-goes-agentic-a-developer-walk-through-of-warp-2-0/) 中看到的熟悉的选项卡式屏幕开始，我们已经可以看到一些新的工作。在左上方，我们有三个新图标：</>、放大镜和 +/- 符号。

这分别对应着文件树、文件搜索和更改视图的入口。

底部的查询窗口稍微繁忙一些，终端图标以蓝色突出显示（因此 Warp 会将文本严格解释为操作系统命令），我们可以看到一些广泛的 git 提交统计信息，以及我们正在使用的模型：

[![](https://cdn.thenewstack.io/media/2025/09/f1f41d23-image-2.png)](https://cdn.thenewstack.io/media/2025/09/f1f41d23-image-2.png)

我将继续使用我的简单 Rails 应用程序来创建对话，我在 [Augment CLI 或 “Auggie” 的评测](https://thenewstack.io/developer-walk-through-of-auggie-cli-an-agentic-terminal-app/) 中也使用了它。和以前一样，我们只是想在其中一个视图中引入更多的 Bootstrap。

让我们从一个正式的代码库索引开始。我们切换到“智能体模式”，并使用“/init”命令，就像我们在其他智能体 CLI 中所做的那样，来执行相同的操作：

[![](https://cdn.thenewstack.io/media/2025/09/ac66bf2c-image-3.png)](https://cdn.thenewstack.io/media/2025/09/ac66bf2c-image-3.png)

这是一个更加正式的索引识别，我将让它开始。它还邀请我启动一个 WARP.md 文件。我也可以使用新的智能体配置文件直接指示智能体。

这需要一些时间来完成，然后它允许我检查 WARP.md 文件，该文件收集了一些重要的命令工具以供将来使用：

[![](https://cdn.thenewstack.io/media/2025/09/e15f3e6e-image-4-862x1024.png)](https://cdn.thenewstack.io/media/2025/09/e15f3e6e-image-4-862x1024.png)

## 处理查询

让我们问问 Warp 是否可以用 Bootstrap 增强另一个 Rails 视图。

看看我正在运行的应用程序，Voices 模型的 Rails 视图使用了漂亮的 Bootstrap 按钮：

[![](https://cdn.thenewstack.io/media/2025/09/aa5a8056-image-5-1024x393.png)](https://cdn.thenewstack.io/media/2025/09/aa5a8056-image-5-1024x393.png)

但等效的 Archetypes 视图却没有：

[![](https://cdn.thenewstack.io/media/2025/09/045f3dca-image-6-1024x410.png)](https://cdn.thenewstack.io/media/2025/09/045f3dca-image-6-1024x410.png)

我们不需要知道任何关于模型的信息，也不需要知道它们代表什么——我们只需要让 Warp 改变 archetype 视图。我们可以简单地描述这个类，但我们可以做得更好。

首先，我们将使用文件树（在左侧）选择一个好的示例视图，这样我们就可以在查询中直接引用该文件。请注意，所选的文件视图会填充右侧窗格：

[![](https://cdn.thenewstack.io/media/2025/09/e92c83a2-image-7-1024x561.png)](https://cdn.thenewstack.io/media/2025/09/e92c83a2-image-7-1024x561.png)

为了提供所谓的“智能体上下文”，我们可以使用“@”符号来专门引用这两个文件。让我们看看我在 [Auggie 评测](https://thenewstack.io/developer-walk-through-of-auggie-cli-an-agentic-terminal-app/) 中使用的查询：

*“更改视图文件 app/views/voices/show.html.erb，使其使用 Bootstrap 类，使用 app/views/tags/show.html.erb 作为示例”*

因此，除了不同的示例和目标之外，使用 @ 符号，我可以为 Warp 创建查询：

[![](https://cdn.thenewstack.io/media/2025/09/c0b6ee68-image-8-1024x429.png)](https://cdn.thenewstack.io/media/2025/09/c0b6ee68-image-8-1024x429.png)

这允许我直接捕获文件，这些文件在 Rails 中恰好具有相同的名称，只是位于不同的视图文件夹中：

[![](https://cdn.thenewstack.io/media/2025/09/0a3b6ddb-image-9-1024x254.png)](https://cdn.thenewstack.io/media/2025/09/0a3b6ddb-image-9-1024x254.png)

就这样做吧。我们得到了通常的差异视图，我们可以接受或拒绝：

[![](https://cdn.thenewstack.io/media/2025/09/32950165-image-10-1024x479.png)](https://cdn.thenewstack.io/media/2025/09/32950165-image-10-1024x479.png)

请记住，我们有“查看更改”按钮，因此我们可以随时返回此处。事实上，我甚至可以看到我为 Auggie 评测所做的上一个查询的 git 更改。（目前这些需要相当长的时间才能加载。）

为了总结一下，让我们刷新应用程序上的页面以确认一切正常：

[![](https://cdn.thenewstack.io/media/2025/09/e4dd5a40-image-11-1024x427.png)](https://cdn.thenewstack.io/media/2025/09/e4dd5a40-image-11-1024x427.png)

## Warp 的发展方向

在我的评测中，我只介绍了新内容，但由于 Warp Code 更多地代表着向 Warp 所描述的“智能体开发环境”(Agentic Development Environment, ADE) 的突破，而不是 LLM 机制的特定改进，所以我向 [Zach Lloyd](https://www.linkedin.com/in/zachlloyd/) (Warp CEO) 提出了一些问题，以帮助了解这一切的未来发展方向。

---

**David Eastman: 我认为 Warp 现在特别容易受到攻击，因为你正在进入新的（如果熟悉的话）领域。其他智能体 CLI 产品目前对 shell/终端的控制不足，无法非常接近你使用视图所做的事情。你将如何将编码的 Overton 窗口拉向 Warp？**

**Zach Lloyd:** UI 功能以及我们在视图级别可以做的事情是一个巨大的差异化因素，因为我们可以构建一种不同类型的开发者体验，而不是只能输出文本且无法接受任何鼠标输入的纯粹基于 CLI 的工具。

每个人都在他们的应用程序中改造 AI，无论是在 VS Code 中添加聊天栏还是在 CLI 应用程序中添加 AI。我们试图设计的是用于与智能体一起工作的 UI 应该是什么样的。当人们看到他们可以拥有感觉像基于 CLI 的智能体的东西，但让他们可以像在 GitHub 中审查 PR 一样编辑输出或审查差异时，我们将以一种对于具有其他 UI 约束的应用程序来说非常困难的方式获得正确的基元。

**DE: 在一个相关的问题中，你是否希望其他产品尝试开发或扩展 shell 本身，以便你至少与竞争对手拥有共同的营销基础？**

ZL: 我对此有点矛盾。一方面，我们希望 ADE 成为一个类别，这已经在发生了。如果你看看 Conductor，它可能是人们在 Claude Code 之上构建 UI 的另一个最好的例子。

无论我们是否想要它，实际发生的是竞争已经在向我们靠拢。例如，如果你看看 Cursor，他们正在慢慢地剥离许多编辑功能，并构建一些看起来更像 Warp 的东西。

**DE: 考虑到 Warp 与 AI 的高度集成，你是否会把基本的选项卡式 shell 留给 Ghostty 等？**

ZL: 我仍然很乐意让那些只想将 Warp 用作终端的人使用它，尽管我们的产品重点肯定已经从那里转移了。网上有一些关于此的帖子，有些人对我们添加 AI 感到有点沮丧，他们只是想使用我们的终端功能，例如富文本编辑器和块输出。

我们在内部讨论过不仅要制作一个“关闭 AI”模式，还要制作一个基本的终端模式或 Warp Classic 作为新的二进制文件。我仍然认为我们不太可能做两个二进制文件，但我确实认为我们很可能会在 onboarding 体验中做一些事情——只是“我来这里是为了终端，我不喜欢 AI。” 但总的来说，这真的不是我们前进的重点。

**DE: 你们显然正在争夺 90 年代的 Emacs 或 Vim 的现代版本，开发者可以在其中设置他们喜欢的布局，然后一直使用该设置。你是否会尝试设置一些社区“插件”开发来支持其他视图（例如，git 分支树等）？**

这是一个很棒的主意。我从来没有这样想过。如果你看看这些东西是如何演变的，我记得我在 Emacs 中工作时，我会把所有东西都放在里面——文件树、代码编辑器、所有东西——都在 Emacs 中。人们在 Vim 中也做同样的事情。演变是从这些到 IDE，我认为公平地说，现在 Warp 正在尝试通过 ADE 继续这种演变。

围绕它的一个生态系统，人们可以在视图层插入，这是一个非常酷的想法。我不能诚实地说我们现在正在构建它，只是因为我们有很多其他事情要做。但我实际上很喜欢这个想法，并且认为这是一个明智的地方，我们可以投资使 Warp 本身这个应用程序更易于访问。

**DE: 为了获得后端控制和快速窗口，你显然在 Rust 窗口控制基元方面付出了很多努力。这现在是 Warp 团队中的一个单独的子团队吗？对于那些希望向你递交简历的人来说，你希望看到什么？**

我们拥有的 UI 框架，也就是我们所说的窗口基元和渲染引擎，现在已经相当稳定了。

我们 Warp 在构建功能方面一直以来的通用政策是，你端到端地构建它们。因此，例如，如果你正在构建一个涉及 AI 的功能，那么你要构建它的 UI，你要构建提示，并且你要构建评估——你要负责整体的最终用户体验。

当有人想来 Warp 工作时，我希望看到的是一般的解决问题能力和 CS 技能和资质——一个真正聪明、关心我们正在构建的东西、想要帮助开发者并且非常以产品为中心的人。这意味着他们有能力在构建某些东西时，不仅仅专注于代码，还要始终关注：我为什么要构建这个东西？这个功能应该如何工作？它是否解决了最终用户的问题？

我们不寻找的一些东西：特定的语言知识、Rust 专家和重度终端用户。我们正在寻找想要帮助开发者更快地交付软件的人。

## David 的结论

Warp 既在定义其新的智能体开发环境战略，又在新智能体时代中竞争。Warp Code 使用灵活的视图使其更接近 Emacs 的感觉，即一个高度集成的系统，适合长期开发。

我的感觉是，Warp 不仅拥有正确的技术背景来交付这个，而且它是正确的创新，可以帮助将智能体 CLI 推向更深入的成熟。