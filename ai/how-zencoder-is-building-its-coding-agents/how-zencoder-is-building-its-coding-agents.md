<!--
title: Zencoder如何构建其代码代理
cover: https://cdn.thenewstack.io/media/2025/07/fa3e730c-s-tsuchiya-lykffjahzzu-unsplash-scaled.jpg
summary: Andrew Filev 创立 For Good AI，推出 AI 编码平台 Zencoder.ai，利用 Anthropic 的 Claude 模型，专注于企业级 AI 编码工具市场，提供代码补全、单元测试、代码审查等代理服务，并强调测试的重要性。
-->

Andrew Filev 创立 For Good AI，推出 AI 编码平台 Zencoder.ai，利用 Anthropic 的 Claude 模型，专注于企业级 AI 编码工具市场，提供代码补全、单元测试、代码审查等代理服务，并强调测试的重要性。

> 译自：[How Zencoder Is Building Its Coding Agents](https://thenewstack.io/how-zencoder-is-building-its-coding-agents/)
> 
> 作者：Frederic Lardinois

在将他的项目管理初创公司 [Wrike](https://www.wrike.com/) 出售给一家私募股权公司，然后又出售给 Citrix 之后，该公司的联合创始人兼首席执行官 Andrew Filev 在 2023 年底离职，创立了一家新的初创公司：For Good AI。该公司的使命是将前沿 AI 研究与实践研发相结合，“以创造安全利用 AI 力量的解决方案”。然而，Filev 很快意识到，一家小型初创公司无法在基础研究方面与 Anthropic、OpenAI 和 Google 等公司竞争。

不过，该公司的首个产品，AI 编码平台 Zencoder.ai，迅速在[企业级 AI 编码工具市场](https://thenewstack.io/your-ai-coding-buddy-is-always-available-at-2-am/)中找到了一个利基市场。像[如今许多其他的编码工具一样](http://anthropic.com/partners/powered-by-claude)，Filev 最终使用了 Anthropic 的 Claude 模型作为其产品的核心。

“二十年前，我在学校的论文是关于自动化重构的，但更重要的是，作为一名以产品为核心的人，我会说我的想法只有大约 5% 能够实现，即使在我担任公司首席执行官的时候也是如此，所以我一直希望能够更快地行动。现在依然如此，”Filev 在我问及 Zencoder 的诞生过程时告诉我。“在管理那个庞大的团队时，我看到了其中有多少是例行工作。你不能说这项工作不重要，对吧？但它确实是例行工作。例如，在 Wrike，我们有大约 30,000 个自动化测试。你可以想象，编写第一个测试是一个困难的工作，编写第 30,001 个测试就容易多了。”

[![](https://cdn.thenewstack.io/media/2025/07/b87dda1e-zen-agents-features.png)](https://cdn.thenewstack.io/media/2025/07/b87dda1e-zen-agents-features.png)

*图片来源：Zencoder。*

他指出，在企业环境中，编码只是开发人员工作的一小部分，但许多其他日常流程同样是例行的，并且适合自动化。当他考虑创立新公司时，他一直在关注这个领域，当时初创公司购买自己的 GPU 并试图“玩前沿模型游戏”的做法仍然很流行，正如他所说。

Filev 解释说：“我认为已经有 Anthropic 和其他参与者了，所以我觉得这不是我应该关注的好领域，但从第一天起——而且‘agents（代理）’这个词不像今天这样流行——很明显，这是你需要使用 LLM 的地方。”

Filev 指出，这些代理需要的是访问正确的上下文，因为每个代码仓库都不同，并且需要一个反馈循环来验证结果。他说，验证是定义 AI 可靠性的关键。“如果我抛硬币，有一半的时间可以为你解决问题，那就不靠谱了。但如果我每次都能在 50% 的时间里解决问题，并且我可以告诉你什么时候解决了，什么时候没有解决，那么我就为你节省了一半的工作，”他解释道。

传统上，来自同一系列的模型不太擅长互相批评，但 Filev 指出，随着最新一代模型的出现，特别是 Anthropic 的 Claude Sonnet 4 和 Opus 4，它们在这方面做得好多了。

有了这个重点，Zencoder 推出了一个代码补全产品，该产品使用其第一个 [agentic pipelines（代理管道）](https://zencoder.ai/product/agentic-pipeline) 来检查其代码的语法。从那时起，该公司开始推出更多的代理，这些代理可以处理越来越多的编码任务，比如它的单元测试代理、代码审查代理，以及最近推出的定制代理，开发团队可以修改这些代理来解决他们的特定问题。

他还指出，在现代 LLM 的早期，许多人认为最好训练它们在所有方面都表现出色。

[![](https://cdn.thenewstack.io/media/2025/07/0fb70efc-unit20testing20-2016_920-20dark-1.webp)](https://cdn.thenewstack.io/media/2025/07/0fb70efc-unit20testing20-2016_920-20dark-1.webp)

*图片来源：Zencoder。*

他说：“人们认为 transformers 可以提供对宇宙的包罗万象的理解，但实际上，你不是教它们成为计算器，而是给它们一个计算器。”

随着 Anthropic 的 Claude 3.5 等模型的发布，工具调用成为一个真正的选择，然后随着模型上下文协议的发布，该行业获得了一个事实上的标准来做到这一点。Filev 认为，在某些情况下，开发人员仍然必须编写自己的集成来调用工具，尤其是在用户界面交互方面，但他还认为，下一个发展领域将是代理之间的交互。虽然有些人可能会争辩说，调用另一个代理与调用另一个工具并没有什么不同，但 Filev 并不认同，因为编排这些代理团队存在不同的挑战。

Filev 还指出，模型基准测试已经越来越脱离使用它们的现实。他说，一旦它们通过了某个基准，就不再是解决抽象的数学奥林匹克问题，而是解决现实世界的问题。毕竟，一个擅长氛围编码和用 Python 构建简单游戏的模型可能无法重构混乱的 Java 代码库。

因此，Zencoder 倾向于构建自己的评估工具，并且经常与客户合作来评估新模型对他们的工作效果如何。

Zencoder 与其他编码代理的一个显著区别在于，它是 IDE 不可知论的，而其他像 Cursor 和 Windsurf 这样的工具则 fork 了 VS Code IDE，将它们的代理直接构建到 IDE 中。

Filev 说：“当你从当今流行的第二代产品（在 IDE 中工作）转向即将到来的第三代产品时，我们开始建立领先优势和更多差异。我们采用了你在 IDE 中每天使用的那些代理，我们做的第一件事就是允许你打包它们并在你的组织中共享它们，这有助于采用。”

他认为，采用仍处于早期阶段，尤其是在企业中。虽然一些开发人员可能会全力投入，并可能正在为代理编写他们的自定义指令，但许多员工几乎没有触及表面，并且主要将 AI 视为代码补全。

由于 Zencoder 允许用户构建自己的代理，该公司还推出了一个目录，开发人员可以在其中共享他们的代理。

[![](https://cdn.thenewstack.io/media/2025/07/0a6d1fa0-img_0962-scaled.jpg)](https://cdn.thenewstack.io/media/2025/07/0a6d1fa0-img_0962-scaled.jpg)

*图片来源：The New Stack。*

最近，Zencoder 自己推出了 [Zentester](https://zencoder.ai/product/zentester)，它是一个用于测试从用户界面到服务 API 的任何内容的工具。同样，该公司在这里押注了 Claude 模型。“Anthropic 去年用它的计算机使用模型为市场播下了种子，这令人兴奋，因为与之前在操作 GUI 和 Web 界面方面的尝试相比，它达到了一个新的水平，”Filev 说。虽然这些模型最初并非旨在帮助像 Zencoder 这样的服务测试用户界面，但事实证明，考虑到它们专注于导航应用程序，它们在这方面做得很好。

“测试代码的能力非常重要，因为如果我们交付的代码量要增加 10 倍，这意味着我们要测试的代码量也要增加 10 倍——而这是进入生产代码的唯一途径。因此，编码和测试的结合我认为非常棒：就像花生酱和面包一样。”

长期以来，每一代模型在编码方面都变得越来越好。Anthropic 的开发者关系主管 [Alex Albert](https://www.linkedin.com/in/alex-albert/) 告诉我，大约在一年前 Claude 3 模型发布时，他看到 Claude 在某些编码任务上击败了他。

Albert 说：“在 [Claude] 3.7 左右，我们推出了我们自己的编码产品，我们开始看到我们的客户也在使用它，因为他们真的在代理编码方面发挥了全部能力。我认为 Zencoder 是一个很好的例子，因为他们的整个产品在某种程度上抽象掉了 IDE，它实际上只是一个编码代理。这与我们看待未来编码发展的方式非常吻合，因为你现在更多的是协调这些在你的代码库上运行的软件工程代理，而不是必须亲自进入并手动编辑代码行。”

至于 Anthropic 是否会与像 Zencoder 这样的服务竞争，Filev 说他并不担心，即使 Anthropic 的 [Claude Code](https://thenewstack.io/qa-how-warp-2-0-compares-to-claude-code-and-gemini-cli/) 编码代理在开发人员中越来越受欢迎。

“这是一个非常非常强大的合作伙伴关系，我们很享受 Anthropic 给我们的机会——当然，还有模型本身。另一个相关的考虑是，我认为这个市场的底部无论如何都会迅速商品化，所以 Claude Code 的存在并不一定会改变我们市场的动态，”他说。

展望未来，Filev 认为，随着模型变得越来越智能，像 Zencoder 这样的服务将能够构建越来越复杂的代理管道，这将允许开发人员去喝杯咖啡，同时代理会处理问题并返回经过验证、测试和审查的代码。