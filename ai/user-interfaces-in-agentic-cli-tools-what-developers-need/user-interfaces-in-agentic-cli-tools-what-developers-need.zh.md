正如我在其他地方提到的，许多常规的开发工作都是工程，而不是编码。编码占了很大一部分，但即使是用 IDE 设置一个项目并让环境运行起来也是工程。这意味着操作操作系统命令等等。而且，由于优秀的开发人员也将他们的代码视为数据，因此他们习惯于使用 IDE 体验之外的工具和脚本来处理它。这就是代理式**命令行界面** (CLI) 的用武之地。

## 只是运行一个终端？

大型语言模型 (LLM) 在[工程方面比实际编码更出色](https://thenewstack.io/learn-to-love-the-command-line-interface-with-agentic-llms/)。这主要是因为 IDE 中的代码开发实际上不能表示为连续的请求/响应对。但是，如果转移到终端内的 shell 会话，那正是我们所拥有的：命令和响应。

但是，由于终端会话几乎可以追溯到计算机出现之前，因此它们的定义相当广泛。我记得在学校资源室的电传打字会话（键盘、打印机和纸张）上玩 Lunar Lander。我今天可以模拟相同的查询和响应，但该体验的其他物理方面将不会被共享。

看来我们只是有一个文本界面——某种字符串缓冲区，会随着时间的推移而改变。可能会出什么问题？

我正在使用 [Render](https://render.com/) 服务，运行我的实例，并且我通过网络连接到终端。

Render 通过 Web 提供了一个经典的 Linux shell，但我需要快速从文件中复制一些文本。由于该服务在临时区域中启动您的代码，因此没有持久磁盘可以访问（好吧，除非您额外付费）。![](https://cdn.thenewstack.io/media/2025/08/aaa3f52e-image-1024x156.png)

虽然我可以给出 `cat` 命令来显示文件，但首先要记住的是，如果这太长，您将无法看到文件的顶部。回滚的行数有限。我不知道如何在没有启动的 shell 的窗口视图中更改此设置。没问题，我可以运行 `less` 或 `vim`。第一个不可用，第二个不想在全屏上工作。也无法通过 Web 界面复制任何文本。

![](https://cdn.thenewstack.io/media/2025/08/affe583c-image-1.png)

Vim 不想填充屏幕。

在托管系统上，通过 Web，您根本无法做出太多假设。在这种情况下，Web 界面正在呈现一个终端。虽然 shell 是非常具体的东西，但终端更像是一种可以在不同方式中实现的理想。虽然您最终可以解决所有这些问题（并且 Render 是一项不错的服务），但敏捷工程是关于轮换不断改进的解决方案，而不是花费时间在单个工具解释上。

## 开发良好的文本用户界面

因此，终端不仅仅是操作系统 shell 的前端。这一点在 [Will McGugan](https://willmcgugan.github.io/)（Textualize 的首席执行官，该公司是一家推广终端丰富应用程序的初创公司）的[这篇文章中](https://willmcgugan.github.io/announcing-toad/)得到了很好的证明。我认为该产品尚未准备好进行审查，但 McGugan 认识到的东西很重要：模拟终端通常是很糟糕的东西。并且他对使用 [Claude Code](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/) 和 [Gemini CLI](https://thenewstack.io/expectations-for-agentic-coding-tools-testing-gemini-cli/) 时所看到的内容印象并不深刻。

他首先提到了闪烁的问题。这不是一个致命的问题，但持续使用会让你感到疲惫。当屏幕更新无法跟上信息的变化时，通常在滚动时会出现问题。作为一名游戏开发人员，我知道在绘制屏幕之前完成屏幕更改的旧问题，以及实施双缓冲解决方案的原因，例如。 [Zed 努力保持其基于 Rust 的编辑器快速运行](https://thenewstack.io/how-rust-based-zed-built-worlds-fastest-ai-code-editor/)是有原因的。

还可以仅复制文本，而不是屏幕的方形块。您还需要读取非打印字符以保持行完整性。这始终在现代 IDE 中有效，但在每个终端会话中并非如此可靠。

任何阅读我在 The New Stack 上的文章的人都已经知道使用更强大的终端应用程序的优势，例如 [Warp](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) 或 [Ghostty](https://thenewstack.io/ghostty-will-get-you-excited-about-using-a-terminal-again/)。但这不仅仅是这些。

## 控制台中的控制台

例如，Claude Code 是一个终端应用程序。这需要一些解释。它是一个假设它在某种指定的终端中运行的程序。

Claude Code 本身是一个 Node.js 应用程序，主要用 TypeScript 编写并使用 webpack 编译。如果您觉得需要更深入地了解这一点，[Geoffrey Huntley 可以提供帮助](https://ghuntley.com/tradecraft/)。您可能已经发现，虽然 Claude Code 在 GitHub 上，但没有实际的源代码可用。

为了保持对会话的控制，大多数代理式 AI 实际上是从其运行的终端接管的。

您可以在 Gemini CLI 的情况下看到这一点，其中会话保存在一个块中，可以说，查询与响应在笨拙的框中分开：

![](https://cdn.thenewstack.io/media/2025/08/fde37fe9-image-2-1024x535.png)

但这并不是唯一的方法。将其与 Warp 如何清楚地将每个查询和响应对放在其自己的块中进行比较：

![](https://cdn.thenewstack.io/media/2025/08/148bf16a-image-3-1024x445.png)

这意味着您可以将正常的 shell 任务与您的代理式会话混合在一起。显然，这对于 Warp 来说更容易，它已将其[代理式 CLI 添加到其自己的终端应用程序](https://thenewstack.io/developer-review-of-warp-for-windows-an-ai-terminal-app/)中，但它继续表明终端的实现方式有很多种。

## 只是说话怎么样

当然，您不必使用键盘。您只需说话即可。我看到过视频片段，其中此功能与代理式 CLI 配合得很好，就像它与您的手机配合使用一样。语音会如此迅速地转换为文本，以至于几乎是瞬间的。当我们过去思考会话式编程时，有些人总是指的是使用语音输入，但我们需要访问文本。

快速获取先前命令或响应的方法是向后滚动并获取它。还可以键入简单的代码片段；您不想通过语音来执行此操作。或添加图像。

请注意我在此查询中如何添加一些简单的代码结构：

![](https://cdn.thenewstack.io/media/2025/08/b83b469e-image-4-1024x207.png)

这无法通过语音实现。会话式编程的叙述太接近柯克船长与企业号计算机对话，无法与开发人员的需求完全匹配。事实上，您可能还记得当计算机显示图像时，斯波克使用了不同的界面：

![](https://cdn.thenewstack.io/media/2025/08/6d525a92-image-5.png)

这是一种巧妙的方式来传达叙事，而无需实际向观众展示复杂的外星人生理学图表等。但也证明了语音界面存在局限性，即使在虚构中也是如此。

## 结论

为了使代理式 CLI 长期成功，这些控制台会话需要快速、响应迅速且完全交互。例如，您需要能够快速准确地剪切和复制。

正确的方法是让人编写一个带有 AI 钩子的非常好的终端应用程序，还是在一个终端会话中运行的强大的通用框架，还是 Warp 从头到尾的工作方法？无论哪种方法胜出，开发人员都不会采用出色的 IDE，只是为了降级到在低质量的终端会话中使用代理式 LLM。