<!--
title: Trae IDE：Python库“即写即装”，效率直冲云霄！
cover: https://cdn.thenewstack.io/media/2025/12/81484260-timothy-dykes-j8kgyxsoczq-unsplash.jpg
summary: Trae是一款AI驱动的IDE，特点是自动安装Python库，能自主排查故障、直接保存代码，简化开发流程。提供免费版及付费版，功能强大，适合各类开发者。
-->

Trae是一款AI驱动的IDE，特点是自动安装Python库，能自主排查故障、直接保存代码，简化开发流程。提供免费版及付费版，功能强大，适合各类开发者。

> 译自：[Trae IDE Auto-Installs Python Libraries as You Code](https://thenewstack.io/trae-ide-auto-installs-python-libraries-as-you-code/)
> 
> 作者：Jack Wallen

你已经听过太多关于 [AI 和 IDE](https://thenewstack.io/ai-and-ides-walking-through-how-jetbrains-is-approaching-ai/) 的消息了。现在，它们已经多如牛毛，而且其中许多实际上运行得相当不错。

但究竟是什么让它们与众不同呢？

更好的用户界面？更优秀的 LLM？本地 AI？

我用过好几种这类 IDE，大多数情况下它们的功能都大同小异，并且表现也相当好。当我看到又一款这样的 IDE 时，我不得不去了解一下它是否有任何与众不同之处。

我只花了大约五分钟就弄清楚了 [Trae](https://www.trae.ai/) 的过人之处。我将通过创建一个生成《龙与地下城》角色卡片的 [Python](https://thenewstack.io/what-is-python/) 应用来向你展示这一点。没错，让我们变得极客一点。

## 如何获取 Trae

在我们实际开始使用之前，你可能想知道如何安装它。Trae 可以在 macOS 和 Windows 上免费安装和使用（尽管付费购买许可证会获得更高的价值）。[Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 版本也有一个等候名单，你可以在[项目主网站](https://www.trae.ai)上注册。

我在运行 macOS Tahoe 的 MacBook Pro 上安装了 Trae，它完美安装。安装完成后，我打开 Trae，发现我必须注册一个账户。没问题，反正它是免费的。

注册账户并登录后，Trae AI 提示界面呈现在我眼前（**图 1**）。

[![](https://cdn.thenewstack.io/media/2025/12/3eabde0b-screenshot-2025-12-03-at-2.13.42%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/12/3eabde0b-screenshot-2025-12-03-at-2.13.42%E2%80%AFpm.png)

***图 1**：Trae AI 提示界面非常容易理解。*

好了，是时候开始我们的 D&D 之旅了。

## 将 Trae 用于极客用途

在我决定好希望 Trae 为我做什么之后，我输入了我的提示词，它看起来是这样的：

```
Write a Python program that allows a user to create a Dungeons & Dragons character sheet by asking the standard D&D questions and then rolling the required dice to finish creating the character.
```

敲击回车键后，Trae 开始工作。起初，一切都像任何其他 AI 驱动的 IDE 一样运行。然而，突然间 Trae 给我一个警告，提示程序运行需要安装一个 Python 库。令我惊讶的是，Trae 主动提出为我安装。

当然，Trae，尽管安装吧。

它奏效了。几秒钟内，Trae 就添加了缺失的库，而我无需费心找出库的确切名称并使用 PIP 进行安装。

令人印象深刻。

这实际上发生了三次，每次 Trae 都轻松应对。

我很喜欢这一点。

Trae 大约花了约两分钟来创建程序。我将生成的文本复制到一个名为 `dnd_character_creator.py` 的文件中，并用以下命令运行它：

此文件包含可能与下面显示内容解释或编译方式不同的隐藏或双向 Unicode 文本。要查看，请在显示隐藏 Unicode 字符的编辑器中打开此文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

```
python3 dnd\_character\_creator.py
```

程序问了我一大堆与创建 D&D 角色相关的问题（**图 2**——你懂的）。审问完成后，我可以通过终端滚动查看结果，但仅此而已。

[![](https://cdn.thenewstack.io/media/2025/12/2d8ec5f3-screenshot-2025-12-03-at-2.03.16%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/12/2d8ec5f3-screenshot-2025-12-03-at-2.03.16%E2%80%AFpm.png)

**图 2**：在 macOS 终端窗口中运行我的新 D&D 角色创建器。

回到 AI 提示界面，我说：

此文件包含可能与下面显示内容解释或编译方式不同的隐藏或双向 Unicode 文本。要查看，请在显示隐藏 Unicode 字符的编辑器中打开此文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

```
Make this so the results of the character creation are saved to the file dnd\_character\_creator.txt.
```

敲击回车键，Trae 重新开始工作。

Trae 再次需要安装另一个 Python 库，我允许了，并且它顺利完成了。当 Trae 完成后，我将新代码复制到一个新文件中并运行它。

令我好奇的是，程序没有将结果写入文件，所以我不得不回到提示界面，告诉它没有将结果写入文件。它进行了故障排除过程并施展了它的魔法。

那时我才意识到：我不需要复制/粘贴代码，因为 Trae 实际上是自己将代码写入文件的。

不错。

然后我进入文件夹 `/Users/jackwallen/Documents/trae_projects/DD/` 并运行了正确的文件。

万岁！它成功了。我现在有了一个 Python 脚本来帮助我创建 D&D 角色。

最后，我发现 Trae 的独特之处在于它能够安装创建程序所需的必要库。我甚至不需要知道 Python 程序需要哪些库，这真是帮了大忙。

请理解，我只是初步使用了 Trae，但即使只是简单使用而没有深入研究，这款 IDE 也确实给我留下了深刻印象。

Trae 还提供哪些其他功能？

*   AI 集成到整个开发流程中。
*   使用 Trae Solo 实现自主发布。
*   用于故障排除的多个代理。
*   能够创建自己的代理团队。
*   针对复杂项目的结构化“构建器模式”。
*   图像到代码生成等多模态能力。
*   智能代码补全。
*   用于编程帮助的会话聊天模式。
*   集成调试和测试。
*   VS Code 扩展兼容性。

如我所说，Trae 可以免费使用，但该计划有以下限制：

*   每月 10 次快速请求和 50 次慢速请求的高级模型
*   每月 1000 次高级模型请求
*   每月 5000 次自动补全

如果你升级到每月 10 美元（首月仅 3 美元）的付费计划，你将获得：

*   每月 600 次快速请求和无限次慢速请求的高级模型
*   每月额外 300 次快速请求（限时优惠）
*   无限次高级模型请求
*   无限次自动补全

如果像我这样的人都能通过 AI 查询和故障排除的后续操作来创建复杂的 Python 程序，那么任何人都可以做到。

试试 Trae，看看它是否会成为你新的最爱 [AI 驱动的 IDE](https://thenewstack.io/ai-powered-coding-developer-tool-trends-to-monitor-in-2025/)。