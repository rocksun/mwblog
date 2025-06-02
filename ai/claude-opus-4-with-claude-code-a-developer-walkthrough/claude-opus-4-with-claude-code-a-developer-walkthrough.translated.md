# Claude Opus 4 与 Claude Code：开发者实践指南

![Claude Opus 4 与 Claude Code：开发者实践指南的特色图片](https://cdn.thenewstack.io/media/2025/05/8cc21d33-kamran-abdullayev-ik1duxu9aae-unsplashb-1024x576.jpg)

Claude Opus 4 在发布后不久就引起了[相当多的关注](https://www.bbc.co.uk/news/articles/cpqeng9d20go)，在某些方面，我觉得我有点慢了。我正在阅读一篇非常详细的分析，[Federico Viticci](https://www.linkedin.com/in/federicoviticci/) 使用 [Claude 4](https://www.macstories.net/stories/early-impressions-of-claude-opus-4-and-using-tools-with-extended-thinking/) 在网上整理他的电子邮件。我知道他喜欢细节，但我有点担心他维护的 200 行提示文件。（后来我了解到 Claude 会在自己的文件中写很多笔记。）

我希望将 [Claude Opus 4](https://thenewstack.io/anthropic-launches-claude-opus-4-and-sonnet-4/) 与 Claude Code ([我上个月试用过](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/)) 结合使用，并且对我想将其代理能力应用到什么地方有一个具体的想法。我正在使用一个主要进行 CRUD 管理的 Rails 应用程序，但我想应用 [Bootstrap](https://getbootstrap.com/) CSS 来改进其样式。对我来说，这是一个大型语言模型 (LLM) 适用工作的好例子——如果 CSS “错误”，应该不会造成任何人员伤亡。

我喜欢 Claude Code 的一点是，它保持与你的 IDE 分离的流程，因此你不会逐个考虑代码文件。由于样式必须应用于许多视图文件，而不管其功能如何，因此这是有意义的。

我希望尽可能少地提供指导（因为我是人类），并仅应用更多细节来改进适当的区域。当我使用 LLM 工具时，我当然不会让它在我的代码中横冲直撞，但为了展示代理能力，我将不得不“放手”——也就是说，让它作为一个整体来处理项目。

注意：由于 Claude Code 在你的终端中工作，我将使用 [Warp](https://thenewstack.io/developer-review-of-warp-for-windows-an-ai-terminal-app/)——我选择的终端应用程序——来完成本文的其余部分。

## 设置项目

首先，我将获取旧版本的 Rails CRUD 项目，并将其放入一个新目录中，供 Claude 处理。该项目用于我正在开发的即将到来的游戏，用于组织各种角色可以进行的对话。

我最初对如何基于 Bitbucket 中的特定提交下载代码感到困惑，但幸运的是，Stack Overflow 显示了一个简单的 [REST](https://www.codecademy.com/article/what-is-rest) 模式，该模式有效：

`https://bitbucket.org/<username>/<reponame>/get/<commitCODE>.tar.gz`

然后我将其解压到自己的目录中：

启动 Rails 服务器，我检查了我的旧示例代码的状态：

所以我需要一些样式方面的帮助。

## 设置 Claude Code

现在让我们获取最新的 Claude Code。我已经[安装过一次](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/)，但我在命令行中运行了此命令以确保它是最新的：

```
npm install -g @anthropic-ai/claude-code
```

开始之前最重要的是确保它以更新的 Opus 4 模型启动：

```
claude --model claude-opus-4-20250514
```

和以前一样，它会询问我是否可以信任文件夹中的代码，当然，我信任。然后我们得到重要的参考：

所以我知道我们有正确的模型，并且它正在查看正确的项目。

我还希望它创建提示文件 (CLAUDE.md)，以便我可以进行非常重要和神秘的提示工程：

实际上，正是在启动此命令时，它才*开始忙碌*分析我的代码。

它不断更新和修改其启动时的“待办事项”列表，以便跟踪我提出的要求，并在扫描时为自己创建任务：

事实上，它问了很多次才编写文件。与大多数开发人员不同，它绝对倾向于请求许可——而不是稍后请求原谅。

由于 CLAUDE.md 是一个 Markdown 文件，Warp 允许我在另一个选项卡中查看它（不运行 Claude Code）：

它记录了许多基本关系并了解 Rails 设置。这个想法是它可以在开始新任务之前检查这些。

事实证明，我可以使用 `#` 键来向 Claude 发出指令，它会自动将其合并到提示文件中。我第一次这样做（以及随后），它检查了应该检查什么上下文：

这表明 Claude 4 区分本地项目设置和全局设置。

## 指导 Claude

我开始使用 `#` 键添加指令，但忘记了它也会立即执行该命令。因此，在告诉它 Bootstrap 的含义（带有 Bootstrap 5 的 URL）之后，我只添加了：
- 应用 Bootstrap 颜色实用程序来改善视觉层次结构
- 使用 Bootstrap 按钮类更新按钮

…在代理能力完全发挥作用之前。我本打算首先限制 Claude 仅编辑 views 目录中的文件，但它已经知道这一切。

它对主布局提出了一堆更改建议——我承认我不太理解——并且它还编写了一些模板代码：

当我让它进行更改时，侧边栏的样式变得更加美观：

所以，我想我会让它继续。但对我来说，这是最重要的事情：

它明白首页的一部分有两个独立的功能部分。它没有简单地假设这是一个页面并以相同的方式对待所有内容。风险在于它可能会在 Ruby 模板代码中迷失方向，但它通常不会管那些代码。事实上，它在使显示更整洁方面做得很好，但只是通过扩展我自己的想法。

与此同时，它向我展示了它更改的每个文件，即使我可以让它自己继续。

现在越来越接近我在此处显示的代码部分，所以我可以向您展示它是如何更新按钮链接的：

幸运的是（对于这篇文章），它没有将创建链接变成按钮，所以我将有机会再次指示它。我让它完成了提升。

最后，它总结了它对应用程序中所有视图所做的所有更改，并声明：“该应用程序现在具有现代、一致的 Bootstrap 5.3 设计，具有改进的视觉层次结构、更好的间距和专业的整体样式。”

但是，当我要求进行最后一次更改时，我收到了可怕的消息：

所以我已经花光了我的 6 美元。我~~满足了我的瘾~~继续资助我的帐户以完成这项工作。在收取更多费用后，它继续了。看看它是如何采用我对新路径的描述并正确地对其进行编码的：

它编辑了其他五个文件，包括我们正在查看的文件：

在这里我们可以看到它做了完全正确的事情。另请注意它添加到侧边栏的小图标：

## 结论

这是我第一次在使用 LLM 之前完全低估了它的能力。即使我犯了一个错误，没有对它施加正确的限制，它在这项任务中也确实没有犯任何错误。Claude 完全理解了这个来自 Rails 的简单 CRUD 界面，以及我的意图。

诚然，这“只是”样式设计，但 Claude 不得不在嵌入式 Ruby (ERB) 文件中移动大量的模板代码。到目前为止，这是我使用 LLM 获得的最优质的体验——而且价格相当于伦敦的一杯浓缩咖啡。有了 Claude 做这项工作，也许我甚至不需要那杯咖啡。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)