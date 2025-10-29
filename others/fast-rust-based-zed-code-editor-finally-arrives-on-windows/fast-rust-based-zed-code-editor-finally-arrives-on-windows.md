
<!--
title: 极速Rust加持！Zed代码编辑器正式登陆Windows
cover: https://cdn.thenewstack.io/media/2025/10/7705cd31-ashkan-forouzani-zsy6suvzxfo-unsplashb.jpg
summary: Zed编辑器现已登陆Windows，提供快速、GPU加速的Rust体验。它支持多缓冲区、多光标和Claude AI。虽有初期小问题，但未来有望成为重要的辅助编辑器。
-->

Zed编辑器现已登陆Windows，提供快速、GPU加速的Rust体验。它支持多缓冲区、多光标和Claude AI。虽有初期小问题，但未来有望成为重要的辅助编辑器。

> 译自：[Fast, Rust-Based Zed Code Editor Finally Arrives on Windows](https://thenewstack.io/fast-rust-based-zed-code-editor-finally-arrives-on-windows/)
> 
> 作者：David Eastman

[Zed](https://zed.dev/)，这款由 Atom 和 Tree-sitter 创造者打造的“下一代”代码编辑器，终于登陆 Windows 平台。Zed 是一款快速的、基于 Rust 并支持 GPU 加速的通用代码编辑器，[我两年前首次评测它时](https://thenewstack.io/zed-a-new-multiplayer-code-editor-from-the-creators-of-atom/)，它还仅限于 macOS。

我第一次评测 Zed 时，就想知道它何时会登陆 Windows。作为一种基础的编程工具，代码编辑器必须尽可能地支持多种系统。软件开发人员不能总是选择他们的工作或目标平台，因此他们需要可靠的工具，并确信这些工具能覆盖所有平台。

Zed 最初不愿为 Windows 构建版本，反映的是其团队的规模和经验，而非他们的奉献精神。因此，虽然这篇评测提到了一些负面之处，但我相信他们会适应 Windows 开发环境并解决所有问题。

我将 Zed 用作我的“备用”编辑器——一个处理主项目内部和周围文件的编辑器。对我来说，它无法取代 Visual Studio / Visual Code 处理 C# 文件，但对于 JSON 文件、Ruby 支持脚本等已经足够好用。我当然希望它能取代老化的 Sublime Text。

Zed 始终支持键盘高效操作，几乎总有办法将操作绑定到键盘。然而，在 2025 年，大多数人确实会使用鼠标，并且这一点也得到了很好的支持。

[![](https://cdn.thenewstack.io/media/2025/10/ce6e7d6d-image.png)](https://cdn.thenewstack.io/media/2025/10/ce6e7d6d-image.png)

## Windows 上的初次印象和初始设置

我将在我那台旧的 Windows 10 机器上进行测试，这台机器承载着我开发工作的 Windows 部分。感觉我在这台机器上已经用了 Sublime 好久了，所以能够首次安装 Zed 真是太好了：

[![](https://cdn.thenewstack.io/media/2025/10/7c24e849-image-1.png)](https://cdn.thenewstack.io/media/2025/10/7c24e849-image-1.png)

它以这个漂亮的设置页面开始，你会注意到我可以导入我的 Sublime 绑定。完成设置后，它打开了这个欢迎页面：

[![](https://cdn.thenewstack.io/media/2025/10/9d96f54f-image-2.png)](https://cdn.thenewstack.io/media/2025/10/9d96f54f-image-2.png)

我对“克隆仓库”选项很感兴趣，所以我输入了一个仓库的 URL，输入了一个目标文件夹，然后得到了以下响应：

[![](https://cdn.thenewstack.io/media/2025/10/3c4a42ce-image-3.png)](https://cdn.thenewstack.io/media/2025/10/3c4a42ce-image-3.png)

没有其他解释。更新后，启动屏幕上不再有此选项。所以我想我们暂时应该忘记这一点，并假设它会在后台得到修复。正如我所说，这是前沿产品。

## 语言支持和文件编码问题

打开项目后，Zed 会检测代码文件的语言，并邀请你加载正确的语言服务器。（如果不是比 C# 更冷门的语言，它都能检测到。）

[![](https://cdn.thenewstack.io/media/2025/10/41f60bf7-image-4-1024x576.png)](https://cdn.thenewstack.io/media/2025/10/41f60bf7-image-4-1024x576.png)

然后我们立即得到了预期的有序着色。

如果你仔细看上面的截图，你会看到文件第一个字符是一个下划线，文件似乎忽略了它，但删除它会出问题。这是因为文件保存的格式是带 BOM（字节顺序标记）的 UTF-8，而 Zed 无法识别这种格式。如前所述，随着他们与 Windows 上更容易出现的问题同步，Zed 将会更加关注这一点。

我还发现刷新诊断功能运行得不是特别流畅，但这似乎也是一个小问题。让我们深入了解多缓冲区和多光标。

## 理解多缓冲区和多光标

多缓冲区充当不同文件的窗口，但所有窗口都在一个页面上。例如，我可以搜索方法的引用。在 VS Code 中，这些会列在另一个窗格中。但在 Zed 中，我们能将它们全部一起看到：

[![](https://cdn.thenewstack.io/media/2025/10/e3cff681-image-5.png)](https://cdn.thenewstack.io/media/2025/10/e3cff681-image-5.png)

展开后，这些都是相关文件的窗口，每个窗口都有几行上下文，上下各几行：

[![](https://cdn.thenewstack.io/media/2025/10/2caa0991-image-6-1024x393.png)](https://cdn.thenewstack.io/media/2025/10/2caa0991-image-6-1024x393.png)

我可以进入任何缓冲区并直接编辑它。你还可以看到我也可以跳转到源文件。此外，我还可以进行全局更改。在多缓冲区中，可以使用多个光标同时编辑每个文件。下面，我选中了类术语 `GainedKnowledge` 的实例，并同时扩展了所有这些实例：

[![](https://cdn.thenewstack.io/media/2025/10/5d15d754-image-7.png)](https://cdn.thenewstack.io/media/2025/10/5d15d754-image-7.png)

这比类似但更具体的“更改符号”功能更具通用性。

## Anthropic 的 Claude 集成 AI

其中一个便利功能是 `control-+`，它允许你仅缩放文件文本内容，并且操作非常迅速。

当我第一次评测 Zed 时，“登录”似乎是编辑器的一个奇怪甚至有争议的要求，尽管它主要是为了使用协作功能。当然，现在人们无论如何都会登录他们的 AI 供应商。说到这一点，Zed 选择 Anthropic 的 Claude 作为其默认的内置大语言模型（LLM）代理，尽管它也可以与任何供应商合作：

[![](https://cdn.thenewstack.io/media/2025/10/4577b2b6-image-8.png)](https://cdn.thenewstack.io/media/2025/10/4577b2b6-image-8.png)

我本来不打算看 AI 部分，因为它显然会像[以前一样](https://thenewstack.io/an-introduction-to-zed-ai-and-how-it-compares-to-cursor-ai/https://thenewstack.io/how-rust-based-zed-built-worlds-fastest-ai-code-editor/)运行得很好。然而，它确实帮助我介绍了终端。

## 使用集成终端

验证 Claude 时，它默认显示了可爱的终端登录界面：

[![](https://cdn.thenewstack.io/media/2025/10/7aa6b62f-image-9.png)](https://cdn.thenewstack.io/media/2025/10/7aa6b62f-image-9.png)

选择选项后，这让 Zed 能够很好地与 Anthropic 的计费认证分开，同时也回答了支付问题：

[![](https://cdn.thenewstack.io/media/2025/10/bddef958-image-10.png)](https://cdn.thenewstack.io/media/2025/10/bddef958-image-10.png)

虽然它确实需要跳转到网页完成，但我在网页上操作完毕后，终端就消失了——这是一个很棒的细节。

我通过命令面板 `ctrl-shift-p` 再次调出终端，该面板将命令与键盘绑定。请求刷新终端返回后，我注意到它使用的是 Powershell：

[![](https://cdn.thenewstack.io/media/2025/10/1322daed-image-11.png)](https://cdn.thenewstack.io/media/2025/10/1322daed-image-11.png)

当然，在 Windows 中，“终端”到底是什么，会因你的需求而异，[Warp for Windows 也发现了这一点](https://thenewstack.io/developer-review-of-warp-for-windows-an-ai-terminal-app/)。对我来说，它是 [git bash](https://gitforwindows.org/)，但其他人则使用 [WSL](https://learn.microsoft.com/en-us/windows/wsl/)。我认为这些选项会随着时间的推移而改进。

最后，费用现在主要集中在 AI 使用上。不过和以前一样，大多数人最初可能不会付费。

[![](https://cdn.thenewstack.io/media/2025/10/cadcb82d-image-12.png)](https://cdn.thenewstack.io/media/2025/10/cadcb82d-image-12.png)

## 结论：Zed 在 Windows 上的未来

Zed 在这里有足够的理由声称它在每个主要系统上都拥有完全支持的编辑器，这本身就将其提升到了一个崇高的地位。它在其 Discord 频道中能承受住 Windows 特有 bug 报告的时间越长，产品成熟的速度就越快。

Zed 仍然与开发者社区略有不同，因为它专注于速度和 AI。但我预计它将作为每个人的“备用”编辑器获得越来越多的关注。