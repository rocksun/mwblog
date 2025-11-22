<!--
title: Antigravity AI编程：谷歌最新实验
cover: https://cdn.thenewstack.io/media/2025/11/ed066202-muha-ajjan-sd8nfde2vy-unsplashb.jpg
summary: 谷歌推出的 Antigravity 是一个智能体开发平台，它是一个 IDE 应用，而非 CLI。该平台提供代码补全、建议，并能理解上下文进行代码改进。但其智能体功能和并行任务处理方面尚不明确，整体感觉像一个方向不明确的实验性产品。
-->

谷歌推出的 Antigravity 是一个智能体开发平台，它是一个 IDE 应用，而非 CLI。该平台提供代码补全、建议，并能理解上下文进行代码改进。但其智能体功能和并行任务处理方面尚不明确，整体感觉像一个方向不明确的实验性产品。

> 译自：[Hands-On With Antigravity: Google’s Newest AI Coding Experiment](https://thenewstack.io/hands-on-with-antigravity-googles-newest-ai-coding-experiment/)
> 
> 作者：David Eastman

谷歌本周推出了名为 [Antigravity](https://antigravity.google/) 的新智能体开发平台，我首先想到的是：“Jules 和 [Gemini CLI](https://thenewstack.io/expectations-for-agentic-coding-tools-testing-gemini-cli/) 呢？” 但请记住，这是谷歌；他们会把很多东西扔到墙上看看哪个能粘住（答案是很少，正如他们的 [墓碑](https://killedbygoogle.com/) 所证明的那样）。因此，谷歌将 Antigravity 和 Jules 视为从不同角度审视同一技术的实验。

现在让我们来看看 Antigravity，它似乎已准备好在所有平台（而不仅仅是 Mac）上进行“公开预览”：

[![](https://cdn.thenewstack.io/media/2025/11/3a7f968e-image-1024x592.png)](https://cdn.thenewstack.io/media/2025/11/3a7f968e-image-1024x592.png)

与 [Verdent](https://thenewstack.io/first-look-at-verdent-an-autonomous-coding-agent-from-china/) 不同，它不是用于终端的 CLI——它是一个 IDE 应用程序。所以我为我的 MacBook 下载了它，并将其放入应用程序文件夹。

## 初印象和设置过程

明智的是，它会在设置过程中要求用户选择一个主题。大多数人会设置一次主题（深色或浅色），然后很少再次更改该选项：

[![](https://cdn.thenewstack.io/media/2025/11/0508b799-image-1-1024x630.png)](https://cdn.thenewstack.io/media/2025/11/0508b799-image-1-1024x630.png)

下一个设置问题非常有趣：

[![](https://cdn.thenewstack.io/media/2025/11/27969cec-image-2-1024x698.png)](https://cdn.thenewstack.io/media/2025/11/27969cec-image-2-1024x698.png)

这似乎是想可能朝着 [并行运行器](https://thenewstack.io/a-hands-on-review-of-conductor-an-ai-parallel-runner-app/) 模型发展，只需很少的人工干预（并行运行器意味着让智能体任务在后台运行，同时你开始另一个任务——换句话说，每个任务都在隔离的分支上运行）。或者 Antigravity 可能更像文档驱动的解决方案，如 [Kiro](https://thenewstack.io/aws-kiro-testing-an-ai-ide-with-a-spec-driven-approach/)。正如你所猜到的，这篇帖子只是为开发者设定场景，而不是深入研究一个实验。所以我将选择“辅助开发”选项，这感觉更像是常规领域。

在用谷歌（使用其内部 2FA）登录后，Antigravity 会要求你打开一个文件夹或克隆一个。要创建一个隔离的分支，就像并行运行器一样，它需要一个 git 克隆。它还会查找用户文件夹中看起来像项目的文件夹。

[![](https://cdn.thenewstack.io/media/2025/11/816f34bb-image-3-1024x674.png)](https://cdn.thenewstack.io/media/2025/11/816f34bb-image-3-1024x674.png)

正如你所见，我选择了 Claude Sonnet 作为当前可用的模型之一：

[![](https://cdn.thenewstack.io/media/2025/11/30653df3-image-4.png)](https://cdn.thenewstack.io/media/2025/11/30653df3-image-4.png)

## 熟悉的 IDE 带有 AI 驱动的建议

像往常一样，你将获得一些免费令牌，但前提是滥用行为将被限制。在初始化完成后（我猜是在扫描项目），我们会看到标准布局：

[![](https://cdn.thenewstack.io/media/2025/11/1d9a4f49-image-5-1024x676.png)](https://cdn.thenewstack.io/media/2025/11/1d9a4f49-image-5-1024x676.png)

这看起来熟悉吗？是的，这似乎是某种 VS Code 分叉。我曾写过关于 [这些的危险](https://thenewstack.io/agentic-coding-and-the-weakness-of-extensions-for-ides/)——但说实话，我不知道谷歌为什么要这样做。

在右侧，我选择了“规划模式”；另一种“快速”模式“在速度很重要且任务足够简单，不太担心质量下降时很有帮助”——这有点滑稽，但我们知道作者的意思。

据我所知，“Agent manager”更接近并行运行器智能体 CLI 模式，因为你不与编辑器交互。下图指的是这一点：

[![](https://cdn.thenewstack.io/media/2025/11/ed731b89-image-6-1024x448.png)](https://cdn.thenewstack.io/media/2025/11/ed731b89-image-6-1024x448.png)

话虽如此，这里的语言却相当奇怪。左侧的文本确认了并行任务模型。但顶部的文本提到了“深度研究”，这是一个用于软件开发的奇怪术语。此外，目前的期望是任何任务都是“后台”的，除非用户要求持续干预。这感觉不像是在与最近发布的“智能体”代码编辑器以相同的精神编写的。

首先查看编辑器窗口（图的右侧），我获得了良好的快速代码补全和建议。我选择了一个项目代码中可以改进的棘手部分——一个边界检查器。

```
public void CalculateMapBound(MapSector sec) {
  Vector2 topleft = sec.GetAbsoluteTopLeft();
  Vector2 size = sec.GetSize();
  TagDebug.Log($"Topleft and size for sector {sec.Name} {topleft} {size}");

  if (topleft.x < leftbound) leftbound = topleft.x;
  if (topleft.x + size.x > rightbound) rightbound = topleft.x + size.x;
  if (topleft.y > topbound) topbound = topleft.y;
  if (topleft.y - size.y < bottombound) bottombound = topleft.y - size.y;
  TagDebug.Log($"Calculate bound for sector {sec.Name} {leftbound} {rightbound} {topbound} {bottombound}");
}
```

选择它之后，我得到了一个机会将其添加到查询中，所以我们有：

[![](https://cdn.thenewstack.io/media/2025/11/02ea3bdd-image-7.png)](https://cdn.thenewstack.io/media/2025/11/02ea3bdd-image-7.png)

它建议我使用 Min/Max 函数。鉴于我不赶时间，这听起来是正确的。聊天框中的文本说明了更改和好处，我可以在代码中接受这些更改：

[![](https://cdn.thenewstack.io/media/2025/11/34269420-image-8-1024x955.png)](https://cdn.thenewstack.io/media/2025/11/34269420-image-8-1024x955.png)

当然，我没有足够的勇气（或愚蠢）将我的整个构建环境移植到一个实验性应用程序中。但我会保留这些更改，稍后进行检查。

## 探索 Antigravity 的智能体功能

现在让我们尝试智能体方面。不幸的是，它似乎不适用于独立分支（或者不期望这样工作），所以你可能只能在同一个工作区文件夹内工作：

[![](https://cdn.thenewstack.io/media/2025/11/16153e1f-image-9.png)](https://cdn.thenewstack.io/media/2025/11/16153e1f-image-9.png)

我认为“对话”映射到一个任务。我会让它改进另一个处理边界的方法。但它并不真正设计用于保持任务管理器打开，因为它会不断关闭它，以便为聊天框和（例如）更改视图腾出空间：

[![](https://cdn.thenewstack.io/media/2025/11/f2440c6e-image-10-1024x614.png)](https://cdn.thenewstack.io/media/2025/11/f2440c6e-image-10-1024x614.png)

我喜欢以下声明：

[![](https://cdn.thenewstack.io/media/2025/11/59781264-image-11-1024x75.png)](https://cdn.thenewstack.io/media/2025/11/59781264-image-11-1024x75.png)

这证明它对上次对话和由此产生的更改具有上下文理解。而且它是正确的——Min/Max 更简洁（尽管我预计它会慢得多）。

所以，看起来我应该收回这个想法，即它被设计成在同一项目中的并行任务上工作——它显然不是。也许谷歌正在等待反馈，看看他们应该如何反应。

## 结论：一个方向不明确的实验

在这个阶段，我决定停下来，因为我不太清楚这个产品到底想做什么。它是一个应用程序，但看起来部分像是 VS Code 的克隆版本。它提供了一个 Agent 管理器，但并没有真正提供我所期望的并行任务功能。不过它确实能做到 Gemini CLI 所做的事情，或者说，和 Jules 做的事情差不多。

我知道 Google 会由独立团队创建项目，有时会有一些很棒的想法(我仍然记得 Google Wave)，但 Google 作为一家公司后来却选择忽视它们。而且这些项目往往与当前趋势不太一致。我打算等 Google 弄清楚他们想用这个产品做什么之后，再在其开发演进的后期重新审视它。