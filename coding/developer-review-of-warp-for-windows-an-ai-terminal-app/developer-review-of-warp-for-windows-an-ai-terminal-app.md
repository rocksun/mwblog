
<!--
title: Warp for Windows开发者体验：一款AI终端应用
cover: https://cdn.thenewstack.io/media/2025/03/287fd338-mathew-schwartz-sb7rurrmac4-unsplashb.jpg
-->

> 译自：[Developer Review of Warp for Windows, an AI Terminal App](https://thenewstack.io/developer-review-of-warp-for-windows-an-ai-terminal-app/)
> 
> 作者：David Eastman

如果你想要一个可以在任何地方使用的终端，那么 Warp for Windows 的到来是个好消息。David Eastman 体验了一下。

我已经在我的 MacBook 上[使用 Warp 终端](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/)一段时间了，但一直存在一个问题：它从来没有 Windows 版本。

虽然现在大多数技术都是基于 Linux 的，但仍然有很多 Windows 设备和服务，这意味着大多数软件开发人员必须准备好使用 Windows。如果你跨行业工作，这是完全不可避免的。例如，作为一名游戏开发者，PC 仍然是一个主要的平台。

所以我一直希望有一个可以在任何地方使用的终端。终于，[Warp for Windows 出现了](https://thenewstack.io/warp-launches-ai-first-native-terminal-app-for-windows/)。虽然它还没有完全准备好投入使用，但它已经将 Warp 的现代编辑能力带到了 Windows 上。

我的开发 Windows 机器是一台运行 Windows 10 的旧 AMD Phenom II 处理器电脑。微软自豪地告诉我，由于这台机器太旧，无法运行 Windows 11，所以它很快就只能报废了。但它可以愉快地运行我所有的开发工具。然而，直到今天，它还不能运行 Warp，这是由于旧芯片的一个众所周知的问题（SSE4.1 兼容性）。但我原本期望它可以工作——毕竟，我的机器也能运行 Fortnite。

Windows 的另一个问题是，原始的命令 shell（CMD）不被 Warp 支持，因为它太原始，无法集成。但在我们深入探讨这个问题之前，让我们先启动 Warp for Windows。

你不再需要登录了。我已经赞扬过 Warp 是一家公司运营的事实，但登录让很多人望而却步。如果你完全将邪恶归于这种行为，那么你可能一开始就没有与 Warp 项目保持一致。但现在，只有少数扩展任务需要登录。

![](https://cdn.thenewstack.io/media/2025/03/3433ebf6-image.png)

我们打开一个标签页来启动一个会话，然后选择要使用的 shell。你可以看到 Warp 识别出 PowerShell 和我安装的首选项，即[Git Bash](https://gitforwindows.org/) shell。Git Bash shell 是开发人员的最爱，因为它允许对 Unix 风格的命令进行适当的集成，以便与 git 一起使用。不幸的是，这个 shell 对我不起作用，但它对其他人有效，并且得到了团队的全力支持。在较新的机器上，你也可以在 Warp 中使用 Windows Subsystem for Linux (WSL)。

大多数开发人员没有学过太多 PowerShell，因为它相当晦涩难懂。然而，它确实有一些 Unix 别名，这很好。这就引出了 Warp 如何使用 AI。像大多数开发人员一样，我对使用大型语言模型（LLM）持保留态度，但它们在操作系统中充满了选项标志的世界中非常有用。让我们看看它是如何工作的。

对于大多数 Windows 用户来说，使用 Warp 块来包装命令和响应并允许完全编辑的能力将是最大的乐趣。例如，如果我简单地在根目录下输入 `tree` ，它会将 38 秒的冗长响应放入一个块中，但不会使整个 shell 无法使用：

![](https://cdn.thenewstack.io/media/2025/03/e75ebe2f-capture.png)

我仍然认为 Warp 在 AI 方面投入了太多，但在本例中，我想用 `tree` 做更多的事情，所以我使用了一个提示，以聊天的方式与 LLM 交谈：

![](https://cdn.thenewstack.io/media/2025/03/0a4eb5c2-image-1-1024x85.png)

这是一个有点虚假的问题，因为 `tree` 已经显示了目录，但不打印它们。请注意 LLM（在本例中为 Claude Sonnet）如何自己推理它可以做什么，并显示我可以使用的响应。如果我愿意，我可以运行它：

![](https://cdn.thenewstack.io/media/2025/03/3523b09c-capture2-1024x225.png)

事实上，在运行之后，它继续纠正自己，并使用 PowerShell 脚本来完全按照我的要求去做，尽管我认为它耗尽了 tokens。之后，我可以回到那个块，并通过右键单击应用命令：

![](https://cdn.thenewstack.io/media/2025/03/57dff695-image-2-1024x631.png)

所以我可以使用“在块中查找”进行搜索，在本例中，我只查找序列“time”：

![](https://cdn.thenewstack.io/media/2025/03/8c557cae-image-3-1024x640.png)

这都很有用，因为我不想学习 PowerShell。但 Warp 提供了更简单的优势——比如建议完成。在本例中，我错误地调用了帮助，Warp 建议了我实际需要的：

![](https://cdn.thenewstack.io/media/2025/03/a436a527-image-4.png)

类似地，在键入目录时，Warp 会智能地介入以建议可用的替代方案：

![](https://cdn.thenewstack.io/media/2025/03/8bc251b7-image-5.png)

这些是命令 shell 应该一直提供的相对简单的事情，而 Warp 最终为我们提供了这些。

正如我在查看[Ghostty](https://thenewstack.io/warp-vs-ghostty-which-terminal-app-meets-your-dev-needs/)时提到的，使用选项卡控制会话是一个主要的优势，这与我在 MacBook 上的工作方式非常相似。例如，只需右键单击即可重命名选项卡或应用颜色：

![](https://cdn.thenewstack.io/media/2025/03/a678b6cc-image-6.png)

*（是的，那个文件夹是 2012 年的）*

[Warp Drive 和工作流](https://docs.warp.dev/features/warp-drive)我之前已经介绍过，但它们是对 Warp 系统的长期投资，这些投资很可能值得。它们有效地允许你命名和存储参数化命令，并在团队中共享它们。例如，在团队中共享相同的 git 语句是个好主意：

![](https://cdn.thenewstack.io/media/2025/03/e5ee4d76-image-7-1024x643.png)

对于 DevOps 来说，当许多具有不同技能水平的团队成员需要在多个系统上运行命令时，此功能可能会发挥其作用。

不幸的是，有很多配置可以算作 Windows PC，Warp 团队需要更多时间才能将他们完整的工程专业知识应用于这个新的旧世界。但鉴于他们已经取得的成就，我相信 Warp 将很快成功地将其优势扩展到整个 Windows 平台。

![](https://cdn.thenewstack.io/media/2025/03/95b68d6e-image-8.png)
