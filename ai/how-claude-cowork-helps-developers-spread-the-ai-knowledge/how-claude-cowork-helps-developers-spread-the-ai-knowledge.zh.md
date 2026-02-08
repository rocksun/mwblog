上个月，[我评测了 Claude Desktop](https://thenewstack.io/give-claude-ai-full-access-to-your-local-filesystem-with-mcp/)，并指出允许模型上下文协议 (MCP) 使用本地文件夹这一简单功能本身就是一个很棒的想法。Anthropic 显然得出了相同的结论，并以敏捷的商业速度，通过发布 [Claude Cowork](https://claude.com/blog/cowork-research-preview) 迅速将这一观察结果产品化。目前，它“作为研究预览版提供给使用 macOS 上 Claude Desktop 应用程序的 Pro 和 Max 计划订阅者”。但稍后会详细介绍。

这项产品明确面向非开发人员。但通过发布它，Anthropic 也在做一件有利于高级开发人员的事情——它证实了他们对 AI 的本地实践知识如何能够提升其他部门同事的能力。

尽管开发人员总是受到尊重，但我们都知道，由于我们的专业性，我们往往是企业中的一个“节点”。但事实证明，大型语言模型 (LLM) 在开发领域之外的应用与在开发领域之内一样多，像 Cowork 这样的应用程序的采用突然让开发人员的知识在整个企业中“横向”闪耀。正如 [Kate Holterhoff 指出](https://redmonk.com/kholterhoff/2026/01/16/will-your-ai-teammate-bring-bagels-to-standup/)，“Cowork”这个词经过精心选择，旨在反映“供应商希望我们如何看待代理在未来工作中的位置”。

对于此类文章，提及任何定价模型通常都是不明智的，因为这是最容易过时的信息。我尝试使用我的 API 用量，但没有成功，所以我注册了 Pro 计划。我提到这一点只是为了说明，向普通受众介绍这项技术将导致大量意想不到的 token 使用和相应的费用。

## 启动

我之前已经安装了 Claude Desktop，而 Cowork 就运行在 Claude Desktop 内部。但我还是下载了一个全新的副本，以防万一。

在我启动应用程序时，你可以勉强看到 Cowork 模态窗口后面的“Cowork”选项卡：

![](https://cdn.thenewstack.io/media/2026/01/10b8d959-image-1024x426.png)

选择 Cowork，你将看到基本的用户界面：

![](https://cdn.thenewstack.io/media/2026/01/66877b6e-image-1-1024x750.png)

为了试用它，我将要求它帮助整理我的桌面截图。在笔记本电脑的行话中，这只是一个临时文件夹，最终会保存截图。通常，我很乐意删除这里的所有内容。请注意，它提供的功能是“识别”截图图像，这使得 LLM 能够理解它。该设计意味着 Cowork 只连接到一个实际的文件夹——它知道 Mac 用户有一个“桌面”文件夹。

![](https://cdn.thenewstack.io/media/2026/01/5d617f91-image-2-534x1024.png)

最初，我在一家咖啡馆使用它，网络连接很慢，完成“设置 Claude 的工作空间”花了好长时间。在上面的截图中只完成了 10%。设置完成后，我选择了整理桌面上截图的选项。

Cowork 的一个重要部分是将 [MCP](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) 语言替换为普通的文件夹访问语言。因此，Cowork 必须请求 MacOS 权限才能修改桌面。这相当于通过配置设置可访问的文件夹连接（正如在关于 Claude Desktop 的文章中所讨论的）。

我启动任务，可以看到它执行计划时的进度步骤。

![](https://cdn.thenewstack.io/media/2026/01/bbccfd3b-image-4-1024x854.png)

不幸的是，这一切都因下面显示的错误而崩溃：

```
API Error: 400 {
  "type":"error",
  "error":{
    "type":"invalid_request_error",
    "message":"messages.5.content.17.image.source.base64.data: At least one of the image dimensions exceed max allowed size for many-image requests: 2000 pixels"
   },
   "request_id":"req_011CXNQbsiJBdoFGmfdXTs7X"
 }
```

一如既往，请记住这是一个研究预览版，因此这些是 Anthropic 为防止问题而施加的自我限制。为了客气起见，我回到桌面并删除了那些非常大的文件。尺寸超过 2,000 的图片相当大——我要求 Cowork 为我识别这些文件。它没有直接删除它们，而是给了我一个命令来将其丢进回收站。

![](https://cdn.thenewstack.io/media/2026/01/ef28bbb7-image-6-744x1024.png)

Cowork 最后提供了一个忽略问题文件的选项：

![](https://cdn.thenewstack.io/media/2026/01/a022df7d-image-7.png)

它明白即使大文件仍然存在，它也有办法继续任务，所以我同意了。在它工作时，我可以看到进度：

![](https://cdn.thenewstack.io/media/2026/01/7a41509f-image-8.png)

它完成了我的截图摘要，并添加了这个非常有趣的警告：

![](https://cdn.thenewstack.io/media/2026/01/0f38bf8a-image-9.png)

这是正确的——我的 [Codegate](https://thenewstack.io/getting-started-with-codegate-an-intermediary-for-llm-devs/) 文章中只显示了代码的左侧，但添加这个细节很不错。

它现在提出了一个不错的计划，并提供了可选择的方案：

![](https://cdn.thenewstack.io/media/2026/01/103f8215-image-10-705x1024.png)

在查看了它生成的完整计划 markdown 文件后，我选择了（推荐的）“完全整理”，只是为了看看它的表现如何。很快，它就完成了最终的布局：

![](https://cdn.thenewstack.io/media/2026/01/0a485f25-image-11.png)

这包括将文件重命名为可读的名称；坦率地说，有些人可能会发现这本身就是一个巨大的胜利。

## 结论

尽管 Cowork 仍需解决错误情况（这始终是急切的开发人员最后才想处理的问题），并避免让用户陷入困境，但我发现整个产品非常易用。它提供了足够的选项，让我可以绕过其自身的局限性。是的，我在工作时确实使用了“开发人员”的心态，但我认为任何经常使用笔记本电脑的人都会对用户体验感到满意。

鉴于我认为 [Claude Desktop](https://thenewstack.io/give-claude-ai-full-access-to-your-local-filesystem-with-mcp/) 加上对本地文件夹的访问是一个好主意，Claude Cowork 是一个合乎逻辑的产品步骤，如果不是 LLM 发展中的一个里程碑的话。作为开发人员，你几乎肯定会对 Claude Code 更感兴趣，但作为知识工作者和同事，可以考虑将 Claude Cowork 视为传播关于 LLM 范围的实用知识的一种方式。根据你职业生涯的阶段，这可能是一个锦上添花的技能。