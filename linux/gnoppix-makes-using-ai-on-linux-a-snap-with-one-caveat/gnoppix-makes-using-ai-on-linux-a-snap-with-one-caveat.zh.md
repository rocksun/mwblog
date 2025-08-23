AI。在现在这个时间点，你无法逃避它，因为[它无处不在](https://thenewstack.io/ai/)，并且正在进入应用程序、第三方服务，甚至操作系统。

惊叹。

我知道，AI 和操作系统结合是个好主意吗？嗯，这取决于它的用途。如果 AI [嵌入](https://thenewstack.io/ai-engineering/)在操作系统深处，以至于它可以将触角深入到操作系统所做的一切事情中，那么这不是一个好主意。

另一方面，如果 AI 在那里帮助用户做典型的 AI 事情（研究、搜索等），那么它可能被认为是积极的。

[Gnoppix](https://gnoppix.org) 的开发者明白这一点，并决定让用户轻松启用 AI。我甚至可以说，Gnoppix 开发者让在 Linux 上访问 AI 比任何可用的发行版都更容易。当您将其与出色的 Gnoppix 桌面（使用 Xfce）结合起来时，您就拥有了一个非常令人印象深刻的 Linux 发行版。

让我们从总体上了解 Gnoppix 开始。

## 什么是 Gnoppix？

Gnoppix 是一个基于 Debian 的 [Linux 发行版](https://thenewstack.io/choosing-a-linux-distribution/)，适用于 amd64 和 ARM 架构。这个 Linux 版本是轻量级的，并提供以隐私为中心、安全、强大、智能和用户友好的体验。借助 Xfce 桌面，Gnoppix 也具有高度可配置性。

Gnoppix 附带了您所需的所有软件，以便立即提高工作效率。您将获得如下应用程序：

* LibreOffice (包括 Base)
* HomeBank
* PDF Chain
* Dia
* FileZilla
* Firefox
* Gnoppix Diffusion
* Gnoppix TOR Control
* OnionShare
* PuTTY SSH Client
* Steam
* Thunderbird
* Transmission
* Audacity
* Bleachbit
* dconf editor
* Gnoppix 工具套件
* 以及更多

重点是，您可以获得预装的应用程序来满足您可能需要的几乎任何需求。唯一错失的机会是缺少开发工具。在“开发”菜单类别中，您只会看到 GTK 图标主题检查器、图标浏览器。

乍一看，Gnoppix 看起来像一个相当传统的（尽管很完善）Linux 发行版。直到您在菜单中搜索 AI 并找到 AI 应用程序安装程序时，事情才会变得有趣起来。

## Gnoppix AI

如果您喜欢 AI，这应该会让您印象深刻。如果您单击 AI 安装程序，您只需单击“确定”（图 1），就完成了。就是这样。只需一两秒钟，您就可以使用 Gnoppix AI 了。

[![屏幕截图。](https://cdn.thenewstack.io/media/2025/08/68985152-gnoppix_ai_1.jpg)](https://cdn.thenewstack.io/media/2025/08/68985152-gnoppix_ai_1.jpg) 图 1：Gnoppix AI 安装程序非常简单。

打开 Gnoppix AI 后，您会发现一个用户界面，该界面不仅易于使用，而且易于配置。您可以通过单击顶部中心的下拉菜单并选择要使用的 LLM（图 2）来轻松切换 LLM。

[![屏幕截图](https://cdn.thenewstack.io/media/2025/08/d7395bef-gnoppix_ai_2.jpg)](https://cdn.thenewstack.io/media/2025/08/d7395bef-gnoppix_ai_2.jpg) 图 2：使用 Gnoppix AI 可以轻松选择不同的 LLM。

您可以从 OpenAI、Google、Anthropic 和 Gnoppix 的各种模型中进行选择。但是，这里有一个需要注意的地方。使用 Gnoppix AI，您必须拥有 API 密钥（即使是免费模型）或购买 tokens。我尝试了每个可用的 LLM，发现每个 LLM 都需要密钥（即使是“免费”模型）。

鉴于 Gnoppix AI 的目标是让每个人都能访问、负担得起且值得信赖，我感到惊讶的是，没有一个模型可以在不购买密钥的情况下使用。

等一下。有一种方法，但我还没有让它起作用。您可以使用 Google 等服务创建一个免费的 API 密钥，但它是特定于项目的，并且不适用于 Gnoppix AI。

我不会说谎，这有点令人失望。Gnoppix 至少应该让用户可以轻松地生成一个可以与较小的免费 LLM 一起使用的免费 API，或者至少支持本地安装的 Ollama 实例。为了验证这一点，我使用以下命令手动安装了 Ollama：

```
curl -fsSL https://ollama.com/install.sh | sh
```

安装完成后，我关闭了 Gnoppix AI，并寄希望于最好的结果。

没有用。在 Gnoppix AI 中（我找不到），无法将 GUI 连接到 Ollama。幸运的是，有 Msty，它一直是我与本地 LLM 交互的首选 UI。使用 Msty，您可以免费使用任意数量的本地 LLM。

## Gnoppix 积分

这并不是说你不应该为 [Gnoppix 积分](https://ko-fi.com/s/0101391aad) 付费。20 个积分只需花费你 25 美元。根据 Gnoppix 的说法，每月 3-5 个积分应该足够你使用，因此 20 个积分可能会让你使用长达四个月。

你可能想要坚持使用 Gnoppix AI 而不是像 Msty 这样的东西的原因是，Gnoppix AI UI 更容易使用。关于 Gnoppix AI 的另一件事是，它比 Msty 使用更少的系统资源，因此它更有效率。如果 Gnoppix 团队进一步将其 AI 解决方案集成到各种应用程序中，我强烈建议你选择这条路线。但是，如果你想要快速且免费的 AI，Ollama/Msty 是最佳选择。

即便如此，如果 Gnoppix 能够提供至少一个不需要 token 的免费 LLM（也许只是作为试用），那就太酷了。我不明白的是，即使在 Gnoppix 文档中，它也提到了一个免费选项，但无论我尝试什么，每个模型都需要购买密钥，并且如果有免费的 API 密钥可用，那么开发团队需要让这一点更加明显。看起来（经过一番挖掘）要访问免费的 AI 选项，你必须成为 Gnoppix 会员，这需要花费 2.5 美元/月。所以“免费”是相对的。

> 如果 Gnoppix 能够提供至少一个不需要 token 的免费 LLM（也许只是作为试用），那就太酷了。

另一方面，使用 Gnoppix AI 并购买积分确实支持该项目，因此如果你是开源和 Gnoppix 发行版的粉丝，我建议你使用内置的 AI 应用程序。

好了，关于 AI 的内容就到此为止。

如果不是因为添加了 AI，Gnoppix 值得使用吗？我会用我自己的一个问题来回答这个问题。你喜欢 Xfce 桌面和访问 Gnoppix TOR GUI 以及大量预装应用程序吗？如果是这样，Gnoppix 是你的一个绝佳选择。

除了试图弄清楚 Gnoppix AI 应用程序的挫败感之外，我喜欢我在 Gnoppix 的工作。我发现它是 Debian/Xfce 桌面组合的一个受欢迎的版本。并且通过添加 Ollama/Msty，我拥有了所有我需要的基于本地 LLM 的 AI……而没有麻烦。