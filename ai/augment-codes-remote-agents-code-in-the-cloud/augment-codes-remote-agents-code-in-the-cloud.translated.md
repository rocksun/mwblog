# 在云中增强代码的远程代理代码

![在云中增强代码的远程代理代码的特色图片](https://cdn.thenewstack.io/media/2025/06/9d7de112-goran-ivos-toracb4aqrc-unsplash-1024x769.jpg)

[Goran Ivos](https://unsplash.com/@goran_ivos?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在 [Unsplash](https://unsplash.com/photos/macbook-air-beside-white-coffee-cup-TorAcb4AQRc?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)上发布。

[Augment Code](https://www.augmentcode.com/) 是一款专门[面向专业开发人员](https://thenewstack.io/augment-code-an-ai-coding-tool-for-real-development-work/)的人工智能编码工具，最近预览了一项名为 Remote Agents 的功能。这些 AI 代理以一种类似于 GitHub [最近宣布的 Coding Agent](https://thenewstack.io/github-launches-its-coding-agent/) 的方式扩展了 Augment Code 现有的代码完成和聊天功能。

顾名思义，开发人员可以给这些代理分配特定的任务（例如修复小错误、重构代码或扩展测试覆盖率），然后 Augment Code 将启动一个云环境，供代理处理此问题并测试其代码。对于 Augment Code 来说，这里还有另一个亮点：您可以并行运行多达 10 个这样的代理（尽管它们目前还没有相互交互——但这已经在路线图上了）。

Remote Agents 现在已全面上市。

正如 Augment Code 联合创始人兼 CEO（以及前 Pure Storage CEO）Scott Dietzen 告诉我，Augment Code 一直以来与众不同的一个特点——也解释了它在一个开始让人感觉有些饱和的市场中日益普及的原因——是它的上下文引擎。正如 Dietzen 指出的，Augment Code 的第一个产品本质上是一个同步代码完成工具，类似于其竞争对手已经在做的事情。

“使我们最初的代理与众不同的是它对客户代码的深刻了解，”他解释说。“一般来说，代理经常迷失方向。但是，如果您可以拥有一个精通您的代码库而不是新手的代理，则可以委托他们做更多的事情。因此，我们的人工智能研究团队花费两年半时间构建的这个上下文引擎最终成为代理的一个深刻的差异化因素，因为您希望某些东西具有更高的自主性，就越需要关键地依赖该上下文。”

Augment Code 的上下文引擎的承诺是，它可以构建公司代码库的完整语义图——所有这些都尊重现有的访问控制，以便机器人不会对给定用户通常无权访问的代码进行推理。此图会实时更新，然后成为 Augment Code 的检索增强生成 (RAG) 管道的基础。这使得这些代理和代码完成工具可以访问正确的上下文来处理问题。然后，如果代理需要更多上下文，它可以随时请求。

最近，该公司还推出了 [Augment Agent](https://www.augmentcode.com/blog/meet-augment-agent)，这是一个同步代理，更类似于 Claude Code 以及构建到 Cursor 和 Windsurf 等产品中的工具。虽然 Augment Code 看到 Augment Agent 的早期采用者消耗的推理周期增加了 15 倍，但它仍然是一个在 IDE 中运行并期望开发人员等待它完成工作的工具。

“如果您想成为一个代理团队的技术负责人，您不希望在第一个代理完成其工作之前等待才能启动第二个代理。因此，实际上，在我们甚至推出同步代理模型之前，我们就想要一个远程或异步代理模型，您可以在其中启动（在我们的例子中）最多 10 个代理，并让他们并行处理不同的任务，”Dietzen 说。

对于同步和异步代理，Augment Code 还使用其 Memories 功能，该功能允许用户写下代理应如何编写代码的确切偏好。例如，这些可能是语言偏好，甚至是关于代理应如何进行工作的更详细的说明。

Dietzen 指出，至少以它们目前的形式，Remote Agents 通常最适合处理那些通常需要经验丰富的开发人员花费半天到一天的时间才能完成的任务。Dietzen 说，任何更开放的任务，代理都可能会“迷失方向，挣扎并且不会成功”。他指出，开发人员需要对这些工具可以做什么抱有现实的期望。

他说：“我们面前仍然存在的挑战是帮助更广泛团队中的所有企业。我们与这些专业的早期采用者合作得非常好，他们是喜欢我们产品的人。我们进入了很多商店，在那里我们找到了竞争对手 [GitHub] Copilot 和 Cursor 等等。但是，通常情况下，是那些专家用户放弃了它们，因为他们发现它们没有增加足够的价值让他们坚持使用。”

## 代理与元程序员的崛起
一个有趣的统计数据是，Cursor IDE 实际上是 Augment Code 用户中第三受欢迎的 IDE（VS Code 和 JetBrains 系列 IDE 领先）。

Dietzen 还解释说，他越来越多地看到他所谓的“元开发者”，也就是说，开发者实际上从不接触代码本身，而是让代理处理所有这些。“他们认为代理完成所有编程操作是一件值得骄傲的事情，”他说。“我就像：有时候你为了让代理做你想做的事情，反而要付出更多的努力。但你知道吗，我认为这是一个很好的范例，他们自己不参与代码，这表明我们已经取得了多大的进步。因为即使在五个月前，也不可能让代理完成所有的编码，只要你给他们洞察力。”

与和新手程序员一起工作相比，你可能需要更具体地指导代理才能让它做你想做的事情，但 Dietzen 指出，代理也需要更少的帮助，因为它对代码库有深刻的上下文理解。

Dietzen 说，我们仍然需要软件工程师的灵感。毕竟，总得有人有创造性的见解并设定方向。而且，他强调说，大多数编码，尤其是在企业中，不是关于启动新项目，而是关于维护现有代码并向其中添加新功能。

“Vibe coding 很有趣，对吧？让以前从未接触过软件开发的人参与进来也很有趣，”Dietzen 说。“但是，如果你想让世界变得更美好，我们现有的软件中蕴藏着巨大的价值，但由于缺少功能、可靠性等等原因，这些价值没有得到充分利用，因此能够去处理这些软件，将 AI 应用于运行世界的软件（正如我们所说的那样），并帮助专业的软件工程师，对我来说，这比 vibe coding 令人兴奋得多。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。