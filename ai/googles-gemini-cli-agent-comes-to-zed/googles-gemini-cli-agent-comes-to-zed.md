<!--
title: 谷歌 Gemini CLI Agent 进驻 Zed
cover: https://cdn.thenewstack.io/media/2025/06/e00e7894-gemini_cli_hero_final.png
summary: Google 将 Gemini CLI 集成到 Zed 代码编辑器中，利用新的代理客户端协议 (ACP) 实现更便捷的 AI 代理集成，并着重强调开发者在共享环境中与 AI 共同协作。
-->

Google 将 Gemini CLI 集成到 Zed 代码编辑器中，利用新的代理客户端协议 (ACP) 实现更便捷的 AI 代理集成，并着重强调开发者在共享环境中与 AI 共同协作。

> 译自：[Google's Gemini CLI Agent Comes to Zed](https://thenewstack.io/googles-gemini-cli-agent-comes-to-zed/)
> 
> 作者：Frederic Lardinois

自从六月份首次[宣布 Gemini CLI](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/)（Google 在终端中开源的 AI 代理）以来，该公司一直致力于将其引入其他平台，包括 [GitHub](https://thenewstack.io/googles-gemini-cli-agent-comes-to-github/) 和 [VS Code](https://developers.googleblog.com/en/gemini-cli-vs-code-native-diffing-context-aware-workflows/)。今天，Google 又将 [Zed](https://zed.dev/) 加入其中，这是一款用 Rust 编写的高性能开源代码编辑器。

Zed 长期以来一直利用其作为多人编辑器的基础，将 AI 代理引入其中，现在还将允许开发人员将 Gemini CLI 直接集成到编辑器中。

Google 负责开发人员体验的产品高级主管 [Ryan J. Salva](https://www.linkedin.com/in/ryanjsalva/) 告诉我：“我们构建 Gemini CLI 的初衷就是为了使其具有无限的可扩展性。我们已经看到很多人使用它来构建 GitHub Actions，构建他们自己的自定义斜杠命令，用它来整理笔记，进行研究，做各种各样的事情。但是，有一款开发者工具，不是他们来找我们集成，而是我们主动去找他们集成。”

他说，这款产品就是 Zed，部分原因是他和他的同事 [Keith Ballinger](https://www.linkedin.com/in/keithba/) 本身就是 Zed 的重度用户。当然，Salva 和 Zed 的联合创始人 [Nathan Sobo](https://www.linkedin.com/in/nathan-sobo-92b46720/) 曾在 GitHub 合作开发 Copilot 项目，而 Ballinger 也曾在 GitHub 工作过，这些也有助于促成这次合作。

[![](https://cdn.thenewstack.io/media/2025/08/3856348a-gemini-cli-zed-integration.gif)](https://cdn.thenewstack.io/media/2025/08/3856348a-gemini-cli-zed-integration.gif)

图片来源：Google。

在与 Zed 团队交流时，重点是如何将 CLI 工具最好地集成到 IDE 中。这两个项目都是开源的，以及 Zed 从一开始就具有可扩展性，这些都对此有所帮助。

Sobo 说：“当我们在 Zed 中构建最初的用于编辑的代理体验时，我就想：我们应该让它具有可扩展性。令人难以置信的是，我们一开始没有这样做，我们基本上将代理直接编译到 Zed 二进制文件中，并且我们有自己的代理产品。但我觉得，似乎会有不止一个这样的东西，可能会有很多不同的代理解决不同领域中的不同问题。”

与此同时，他指出，开发人员可能也希望与多个代理进行交互。“让更多人参与到我们和 Zed 的游戏中，让开发人员使用他们想使用的代理，甚至构建他们自己的代理，这就是我感到兴奋的地方，”Sobo 解释道。

正如 Ballinger 也强调的那样，使用 AI 代理的开发人员体验可能从聊天开始，Zed 一直在使用其代理侧面板来做到这一点，但这仅仅是个开始。

“这就是作为开发人员的先锋队的好处之一：我们可以进行实验并找到正确的方法，对吧？所以我们跟踪编辑。或者当你进行下一次编辑、补全时——你不再聊天了，对吧？或者你在做其他事情，它就在那里与你同在——我们将看到这一点，”Ballinger 说。

Sobo 也同意这一点，他指出，Zed 作为多用户编辑器的背景（团队在 AI 时代并没有过多强调这一点，但它仍然是 Zed 的核心）可能会在这里发挥作用。

“我认为 [人类和 AI 代理] 需要共同存在于这个共享环境中，并构建我们共同拥有的这个共享、连续环境的幻觉？我们的 2026 年的一项重大举措就是解决这个问题。”

在当前的迭代中，Zed 中的 Gemini CLI 允许用户实时跟踪代理正在执行的操作，并提供调试模式，让你随时了解代理的想法。与类似工具一样，代理完成后，用户将看到每个建议编辑的差异，允许开发人员审查、接受或修改任何更改。

该团队强调的另一个功能是，你还可以通过提供相关链接，让代理访问你的文档或 API 规范。

## 使一切正常工作：新的代理客户端协议 (ACP)

使这一切正常工作的是新的代理客户端协议 (ACP)，Zed 团队构建该协议是为了更容易地将代理集成到编辑器中——或者实际上是任何其他想要为 AI 代理提供用户界面的程序中。

Zed 团队在今天的公告中解释说：“ACP 为任何编辑器如何与任何 AI 代理通信创建了一个蓝图，为每个人构建了一个更现代化和互连的开发堆栈。” 正如 Sobo 指出的那样，这里的想法是构建“可能工作的最简单的东西”。 他说，这基本上只是一些 JSON-RPC 请求和响应。