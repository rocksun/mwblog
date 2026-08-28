**开源模型运行器 [Ollama](https://ollama.com/) 重新引入了**与 [Claude Desktop](https://thenewstack.io/claude-code-desktop-redesign/) 的集成，使用户能够将 Anthropic 的应用程序连接到通过 Ollama 提供的模型，包括在其机器上本地运行的模型。

这意味着 Claude 用户可以利用 Ollama 的模型库，其中包含诸如 [Qwen](https://thenewstack.io/qwen38-27b-local-inference/)、[DeepSeek](https://thenewstack.io/deepseek-v4-flash-open-weights/)、[Kimi](https://thenewstack.io/kimi-k3-inference-bottleneck/) 和 [GLM](https://huggingface.co/zai-org/GLM-5.2) 等热门模型，同时保留在 Claude Desktop 界面内——由 Ollama 作为处理请求的任何模型的网关。

![Ollama's model catalog inside Claude Desktop](https://cdn.thenewstack.io/media/2026/08/f301e75e-641249150-c02fd93b-f599-40a9-83c3-d0555c0ac182-1024x615.png)

*Claude Desktop 中的 Ollama 模型目录*

## 对 Claude Desktop 的第二次尝试

这并不是 Ollama 首次尝试将其模型目录引入 Anthropic 的工具中。早在 1 月份，该公司就 [增加了支持](https://ollama.com/blog/claude) Anthropic 的 Messages API，允许 Claude Code 指向 Ollama 并使用本地或云端托管的模型，而不是 Claude。

4 月，Anthropic [悄悄开放了一个类似的机会](https://testingcatalog.net/claude-desktop-app-now-supports-third-party-api-proxies/)，在 Claude Desktop 应用程序中增加了一个开发者设置，允许它连接到第三方推理网关。Ollama [抓住了这个机会](https://github.com/ollama/ollama/releases/tag/v0.23.0)，推出了 [ollama launch claude-desktop](https://github.com/ollama/ollama/releases/tag/v0.23.2)，将桌面应用程序配置为使用 Ollama；然而，这种集成仅持续了几天——在 Claude Desktop 更新后，用户发现该应用程序的网关虽然接受了连接，但拒绝了非 Anthropic 的模型 ID。因此，Ollama [删除了该功能](https://github.com/ollama/ollama/releases/tag/v0.23.2)，称 Claude Desktop 的第三方集成已变得“仅限于 Anthropic 模型”。

时间快进到 8 月 21 日，Ollama 在 [v0.33.0](https://github.com/ollama/ollama/releases/tag/v0.33.0) 中悄悄引入了一种新的实现方式，通过 [专用的本地代理](https://github.com/ollama/ollama/blob/main/internal/proxy/claude_desktop.go) 解决了这种不匹配问题。在周二发布的正式宣布该支持的 [博客文章](https://ollama.com/blog/claude-desktop) 中，Ollama 指出开发者现在可以将 Claude Desktop 配置为使用它作为“第三方网关提供商”。Ollama 本身处理设置：用户打开 Ollama 应用程序，选择 Claude 并启用集成，之后 Ollama 会自动配置 Claude Desktop 的第三方网关。将其关闭则会恢复用户之前的 Claude 设置。

![Enabling Claude Desktop](https://cdn.thenewstack.io/media/2026/08/38be7c9e-start-1024x330.png)

*启用 Claude Desktop*

作为更新的一部分，Ollama 还将 Claude 集成直接添加到了其 Mac 菜单中，用户可以在其中切换“使用 Ollama 模型”的开关。

![Use Ollama models](https://cdn.thenewstack.io/media/2026/08/878db792-gif1.gif)

*使用 Ollama 模型*

启用后，通过 Ollama 可用的模型——无论是本地运行还是通过 Ollama Cloud 运行——都会出现在 Claude Desktop 的模型选择器中，允许用户在不离开 Anthropic 应用程序的情况下选择一个模型。

![Claude Desktop model picker](https://cdn.thenewstack.io/media/2026/08/a10bd1ba-gif2.gif)

*Claude Desktop 模型选择器*

由于 Claude Desktop 是围绕 Anthropic 自己的模型选项构建的，Ollama 还允许用户选择每个插槽背后应使用哪个底层模型。在下例中，选择“Opus 5”会将请求路由到 Kimi K3，而“Sonnet 5”则映射到 DeepSeek V4 Pro。

![Auto Mode option](https://cdn.thenewstack.io/media/2026/08/64ac4dfe-auto-mode-1024x753.png)

*自动模式选项*

值得注意的是，“自动模式”选项保留了 Claude Desktop 的内置自动模式，该模式允许应用程序在做出更改之前决定何时应征求用户的许可。

此次发布在 X 上的社区中引发了一连串的问题，其中最主要的可能是：[为什么要](https://x.com/voidpulse11/status/2092542538221555714?s=20)通过 Claude Desktop 使用替代模型，而不是使用 Claude？

答案也许并不令人惊讶，归结为选择。该公司 [指出](https://x.com/ollama/status/2092545484456161371?s=20)成本、速度和可移植性，以及使用根据开发者自身数据微调的模型的能力。用户可以在本地运行的模型或 Ollama Cloud 上的模型之间进行选择，当然，他们仍然可以在任何喜欢的地方依赖 Anthropic 的前沿模型。

一些开发者还 [想知道](https://x.com/GrowthPact/status/2092534518578360587?s=20)这与使用 Ollama 配合 Claude Code 有什么不同，因为这已经成为可能。Claude Code 是 Anthropic 基于终端的编码代理，并且已经可以指向 Ollama 兼容 Anthropic 的 API 以使用本地或云端模型。此版本将同样的基本理念直接引入了 Claude Desktop 应用程序。

> “AI 的未来是运行在工作所需之处的开放模型。”

目前，新的 Claude Desktop 集成仅限于 Ollama 的 Mac 应用程序，尽管 Ollama 在 X 的回复中暗示 [Windows 支持可能正在开发中](https://x.com/ollama/status/2092475441009639741?s=20)。

## “在工作所需之处运行开放模型”

在 Ollama [完成 6500 万美元 B 轮融资](https://www.businesswire.com/news/home/20260709429551/en/Ollama-Raises-%2465M-Series-B-Funding-to-Grow-its-Open-source-AI-Platform) 不到两个月后，Claude Desktop 的支持便到来了。在 7 月份宣布融资时发布的一份声明中，Ollama 联合创始人兼首席执行官 [Jeffrey Morgan](https://www.linkedin.com/in/jmorganca/) 描述了一个开放模型在开发者选择工作的任何地方都可用的未来。

“开放模型应该易于运行、易于构建，并且在人们需要的地方可用——在您自己的机器上、在云端，或两者兼而有之，”Morgan 说。“Ollama 起源于一个开源项目，此后发展成为拥有数百万开发者的社区。我们接下来所做的一切都是为了服务于这个社区及其最好的工作。AI 的未来是开放模型运行在工作所需之处——而 Ollama 在此推动这一转变。”

此次更新也建立在 Ollama 更广泛的推动基础上，即[使本地模型更容易在现有的开发者工具中使用](https://thenewstack.io/how-to-integrate-vs-code-with-ollama-for-local-ai-assistance/)。与此同时，最近的工作，如 [原生 Apple MLX](https://thenewstack.io/ollama-taps-apples-mlx/) 支持，专注于改善 Mac 上的本地推理。

对 Claude Desktop 的支持是这一战略的最新体现：让开发者保留他们已经在使用的应用程序，同时由 Ollama 提供底层的模型。