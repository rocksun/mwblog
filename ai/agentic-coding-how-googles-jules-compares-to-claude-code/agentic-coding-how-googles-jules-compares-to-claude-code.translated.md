# Agentic Coding：Google 的 Jules 与 Claude Code 的对比

![Featued image for: Agentic Coding: How Google’s Jules Compares to Claude Code](https://cdn.thenewstack.io/media/2025/06/2f5eb6f1-yasa-design-studio-_vlxtjqufue-unsplashb-1024x576.jpg)

[YASA Design Studio](https://unsplash.com/@yasadesign_studio) 在 Unsplash 上发布。

在我成功使用 [Claude Code](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/) 之后，我渴望尝试其他等效的、非基于 IDE 的 Agentic 大型语言模型 (LLM) 工具。这些工具在与计划交互方面比盯着文件看要好。因为一个计划可以表达为一组有序的、众所周知的编码实践，所以 LLM 只是充当代码整理员——我们知道它在这方面做得很好。

Google 项目 [Jules](https://jules.google.com/) 将自己描述为“一个异步开发代理——Jules 可以处理错误、小型功能请求和其他软件工程任务，并直接导出到 GitHub。” 我喜欢他们限制了他们认为该工具可以处理的任务的方式。 我不太高兴它即使在 beta 版中也只能通过 GitHub 工作——这对于 Microsoft 来说可能是有意义的，但对于 Google 来说则不然。

我之前用于测试 Claude 的示例项目适用于 Jules：一个 Rails CRUD 项目的一些早期代码，我想向其中添加 Bootstrap。 对于 Claude 来说，这项任务似乎并没有特别大的挑战，所以我主要关注的是 Jules 的工作流程。

## 使用 Jules

Jules 将你的 repo 克隆到一个私有虚拟机 (VM) 中并开始工作。 当我最初尝试 Jules（标记为 beta 版，就像 Google 生产的所有东西一样）时，我收到了一个有趣的正式隐私声明，这与上一页上有趣的位图图形风格有些格格不入。 它对 Google 使用什么以及他们不读取什么做了一系列通常令人困惑的陈述——这些都无法证明。 显然，他们从不读取私有存储库中的代码，但即使是这种说法也充满了保留意见。

有一个 [90 秒的视频](https://youtu.be/M2G27_B7BBM) 显示了一个用户连接到 GitHub，选择一个 repo 然后发出请求。 我喜欢它可以做任何“你通常会为之编写 PR 的事情”这一事实。 同样，这是该产品的一个很好的规模前提——即使它与我上面读到的略有不同。 它会上传你的代码并创建一个你可以批准的计划。 这应该会让非开发人员感到舒服，差异显示在侧面板中。

Jules 还提出了合作者的想法，而不仅仅是一个工具——很像 Claude。 因此，它有一个友好的（和性别中立的）发音名称。 在处理完计划后，它会创建一个新分支并将代码放在该分支上。 从工程的角度来看，这是一种明智的方法，但它突然迫使普通用户理解 git 的语义。 这几乎让人感到报复。

## 将代码放入 GitHub

好的，我的示例代码项目尚未在 GitHub 中，但我们可以将其放入其中。

与我对 Claude 所做的类似步骤中，我解压了我的 Rails 项目的早期版本，以便与 Jules 一起工作：

现在我们将把这段代码推送到 GitHub。 最好的方法是在你的帐户中创建一个 repo，然后在添加新的 remote 后推送你的代码。 （这实际上也是 AI 的一项合理任务！）

进入你的 GitHub 帐户并设置 repo：

我很遗憾地拒绝了“cautious-octo-succotash”这个出色的 repo 名称建议，但我相信将来我会使用它。 然后我记下将成为 remote 目标的内容：

然后，在将其放入本地 git repo 后，我们只需从命令行推送代码。 你很可能需要个人凭据才能做到这一点。 诀窍是添加 remote：

当你的代码安全地位于 GitHub 中时，你可以返回使用 Jules。 一旦你授予存储库权限，你最终应该能够让 Jules 通过你选择的项目来完成它的工作：

好的，这与我要求 Claude 对我的基本 Rails 应用程序所做的事情大致相同，所以我们提出了大致相同的要求：

- Use Bootstrap 5 definitions to improve HTML.
- Apply Bootstrap color utilities to improve visual hierarchy.
- Update buttons with Bootstrap button classes.

所以我将其复制到聊天面板中。 在启动 VM、克隆 repo 和读取文件（大约 2 分钟）后，它制定了一个计划：

请注意，如果你不立即批准，它会在大约一分钟后自动批准！ 但我批准了该计划。

请记住，这里有很多我没有说。 我确实有一些代码示例，但没有一致地应用。

在完成任务时，它已经向我展示了它在 **applications.html.erb** 中的主侧边栏中所做的事情，这看起来与 Claude 清理它的方式非常相似。

经过一段时间（请记住它不是在你的本地系统上工作，所以时间不是一个大问题）后，它已准备好发布：
所以我可以发布 `improvements` 分支，然后将其合并到我的 `main` 分支。虽然这确实要求普通用户与 git 工作流程保持一致，但这是正确的做法。当然，我可以直接去 GitHub 检查是否确实存在一个新分支：

正如预期的那样，它为其更改做了一个合理的条目：

我创建了 pull request 并合并了它。现在，我通常不使用 pull request 方法——在内部公司存储库中，这不是常态——但我们所做的只是确认 Jules 所做的更改被批准合并到项目的主代码中。合并完成后，该分支变得多余：

所以现在我将做一个本地 pull，看看它是什么样子。

我不会在 Claude 更改后对 Rails 应用程序进行并排比较，但我会比较同一组图像。这是带有侧边栏的原始项目代码：

这是 Jules 升级后的同一部分：

除了更漂亮的侧边栏之外，Jules 没有对该页面上的链接进行任何更改。它确实在其他地方进行了很好的清理。

我又给它一个指令——与我给 Claude 更改路径链接的完全相同的 Bootstrap 提示：

它确实进行了改进的更改。这是它的样子：

如果我更具体一些，我就能够一次更改所有链接。

## 结论

在理解我的意图方面，这不如 Claude 那么聪明，但通过更多的提示工程，我知道我会得到正确的结果。使用 pull request 的迭代和测试过程稍微长一些，但它更像是一种工业工作流程。显然，我更喜欢不必使用 GitHub；但话说回来，我很欣赏 Google 正在他们自己的硬件上完成所有事情。

像往常一样，Google 的产品在内部是不一致的，这既是乐趣，也是令人头疼的地方。但他们已经认识到因果编码员市场，最近由 vibe coding 开辟。我认为 Jules 在这里做到了。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道 [订阅我们的 YouTube 频道](https://youtube.com/thenewstack?sub_confirmation=1) 以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)