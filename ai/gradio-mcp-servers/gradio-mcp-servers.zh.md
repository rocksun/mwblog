# 使用 Gradio MCP 服务器提升你的 LLM 技能

[![Freddy Boulton's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1654278567459-626a9bfa03e2e2796f24ca11.jpeg)](/freddyaboulton)

使用 Gradio MCP 服务器提升你的 LLM 技能
你是否曾希望你最喜欢的大型语言模型（LLM）不仅仅是回答问题？如果它可以为你编辑图像、浏览网页或整理你的电子邮件收件箱呢？

现在它可以了！在这篇博文中，我将向你展示：

*   MCP 协议是什么，以及它如何与我们都习惯的智能手机应用程序类似，但却是为 LLM 准备的。
*   如何通过 “MCP 应用商店” 找到数千个 MCP 服务器。
*   如何将其中一个服务器添加到你选择的 LLM 中，以授予它一项新能力。我们将通过一个例子来使用 [Flux.1 Kontext[dev]](https://huggingface.co/spaces/black-forest-labs/FLUX.1-Kontext-Dev)，它可以根据纯文本指令编辑图像。

## MCP 简介

**模型上下文协议（MCP）** 是一种开放标准，使开发人员能够在 LLM 和一组工具之间建立安全的双向连接。例如，如果你创建一个 MCP 服务器，该服务器公开了一个能够转录视频的工具，那么你可以将 LLM 客户端（例如 Cursor、Claude Code 或 Cline）连接到该服务器。然后，LLM 将知道如何转录视频，并根据你的请求为你使用此工具。

简而言之，MCP 服务器是一种通过授予 LLM 一项新能力来提升其技能的标准方法。可以把它想象成你智能手机上的应用程序。就其本身而言，你的智能手机无法编辑图像，但你可以从应用商店下载一个应用程序来完成这项工作。现在，如果有一个 MCP 服务器的应用商店就好了？🤔

## Hugging Face Spaces：MCP 应用商店

Hugging Face [Spaces](https://hf.co/spaces) 是世界上最大的 AI 应用程序集合。这些 space 中的大多数都使用 AI 模型执行专门的任务。例如：

这些 space 是使用 [Gradio](https://gradio.app) 实现的，Gradio 是一个用于创建 AI 驱动的 Web 服务器的开源 python 包。从 `5.28.0` 版本开始，**Gradio 应用程序支持 MCP 协议。**

这意味着 Hugging Face Spaces 是你可以为 LLM 找到数千种 AI 驱动能力的地方，也就是 **MCP 应用商店！**

想要浏览应用商店吗？访问此[链接](https://huggingface.co/spaces?filter=mcp-server)。手动地，你可以在 `https://hf.co/spaces` 中筛选 `MCP Compatible`。

![](https://huggingface.co/datasets/freddyaboulton/bucket/resolve/main/MCPFilter.png)

## 示例：一个可以编辑图像的 LLM

[Flux.1 Kontext[dev]](https://huggingface.co/spaces/black-forest-labs/FLUX.1-Kontext-Dev) 是一个令人印象深刻的模型，它可以根据纯文本提示编辑图像。例如，如果你要求它“把我的头发染成蓝色”并上传一张你的照片，该模型将返回照片，但你的头发是蓝色的！

让我们将此模型作为 MCP 服务器插入到 LLM 中，并让它为我们编辑图像。请按照以下步骤操作：

1.  转到 [Hugging Face](https://huggingface.co/welcome) 并创建一个免费帐户。
2.  在你的[设置](https://huggingface.co/settings/profile)中，在左侧点击 `MCP`。你可能需要在页面中向下滚动才能看到它。
3.  现在，滚动到页面底部。你应该看到一个名为 `Spaces Tools` 的部分。在搜索栏中，键入 `Flux.1-Kontext-Dev` 并选择名为 `black-forest-labs/Flux.1-Kontext-Dev` 的 space。点击后，该页面应如下所示：

![](https://huggingface.co/datasets/freddyaboulton/bucket/resolve/main/SpacesTools.png)

4.  对于此演示，我们将使用 Cursor，但任何 [MCP 客户端](https://github.com/punkpeye/awesome-mcp-clients) 都应遵循类似的过程。滚动回到 [MCP 设置](https://huggingface.co/settings/mcp) 页面的顶部，然后单击 `Setup with your AI assistant` 部分的 `Cursor` 图标。现在，复制该代码段并将其放入你的 cursor 设置文件中。

![](https://huggingface.co/datasets/freddyaboulton/bucket/resolve/main/CursorScreenshot.png)

5.  现在，当你在 cursor 中启动新的聊天会话时，你可以要求它编辑图像！请注意，目前图像必须通过公共 URL 提供。你可以创建一个 [Hugging Face Dataset](https://huggingface.co/datasets) 在线存储你的图像。

![](https://huggingface.co/datasets/freddyaboulton/bucket/resolve/main/FluxKontextDevMcp.png)

> 将流行的公共 space 用作工具可能意味着你必须等待更长的时间才能收到结果。如果你访问该 space，你可以单击“Duplicate This Space”来为自己创建一个私有版本的 space。如果该 space 使用“ZeroGPU”，你可能需要更新到 [PRO](https://huggingface.co/settings/billing/subscription) 帐户才能复制它。

6.  奖励：你还可以使用 Hugging Face MCP 服务器搜索 MCP 兼容的 space！完成第 4 步后，你还可以要求你的 LLM 查找可以完成特定任务的 space：

![](https://huggingface.co/datasets/freddyaboulton/bucket/resolve/main/SpacesSearch.png)

## 结论

这篇博文向你介绍了模型上下文协议（MCP）为大型语言模型带来的令人兴奋的新功能。我们已经看到 Gradio 应用程序，特别是那些托管在 Hugging Face Spaces 上的应用程序，现在完全符合 MCP 标准，有效地将 Spaces 变成了 LLM 工具的充满活力的 “应用商店”。通过连接这些专门的 MCP 服务器，你的 LLM 可以超越基本的问题解答，并获得强大的新能力，从图像编辑到转录，再到你可以想象的任何事情！