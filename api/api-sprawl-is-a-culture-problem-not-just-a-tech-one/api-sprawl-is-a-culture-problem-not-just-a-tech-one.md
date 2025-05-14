
<!--
title: API蔓延：不仅仅是技术问题
cover: https://cdn.thenewstack.io/media/2025/04/ce5ba840-api-sprawl-culture-problem.jpg
summary: API蔓延是文化问题！团队交付加速，API激增，文档缺失，效率降低。需文化转变，利用API开发工具实现标准化，如AI辅助生成API规范。关注Model Context Protocol (MCP)，统一API设计，拥抱LLM。解决API蔓延，提升开发者体验，刻不容缓！
-->

API蔓延是文化问题！团队交付加速，API激增，文档缺失，效率降低。需文化转变，利用API开发工具实现标准化，如AI辅助生成API规范。关注Model Context Protocol (MCP)，统一API设计，拥抱LLM。解决API蔓延，提升开发者体验，刻不容缓！

> 译自：[API Sprawl: Not Just a Tech Problem](https://thenewstack.io/api-sprawl-is-a-culture-problem-not-just-a-tech-one/)
> 
> 作者：Lori Marshall

每个人都熟悉那种不舒服的感觉，当你作为一个新的开发人员加入一个新的团队，打开内部 API 门户，发现…… 57 个名为 `user-APIs` 的 API？

呃哦。有些有相关的文档。有些没有。一个指向已弃用的暂存集群。一半被记录，另一半隐藏在阴影中。另一个自从疫情之前就没被动过。（已经五年了吗？）你应该使用哪些？

或者，也许你是一位技术领导者，被问到：“有多少 API 正在被使用或在生产中？有多少正在被采用？”然后你不好意思地看向你的工程经理，希望有人准备好答案，但现实是你…… 根本。不。知道。

欢迎来到 [API 蔓延](https://www.akamai.com/glossary/what-is-api-sprawl) 背后隐藏的人力成本。这不仅仅是关于代码，而是关于文化。

## 蔓延是部落知识，被武器化

随着开发团队的成长和不断交付，[API 成倍增加](https://thenewstack.io/heres-how-to-tame-your-api-sprawl-and-why-you-should/)。你得到一个强大的团队，每个人都在不断地完成自己的待办事项清单，并且面临着快速和高效的压力。结果是大量的 API，不一定是有组织的、标准化的，甚至没有在各个开发团队之间进行文档化。

如果没有强大的治理或工具，文档会过时，所有权变得模糊，新的开发人员只能玩令人沮丧的 API 考古游戏。这不仅会减慢你的开发人员入职时间（在我们最近的 [调查研究表明](https://getambassador.io/resources/optimize-development-container-environments) 这往往是 43% 的技术领导者的问题），而且还会给所有人带来糟糕的开发人员体验。

我们甚至还没有谈到最糟糕的部分…… 大多数答案并不存在于某个可发现的目录中，而是存在于某人的头脑中。通常，这个荣誉属于在那里工作时间最长的工程师，或者只是碰巧在三年前编写了该计费服务的第一个版本的人。如果那个人离开，这将带来很大的风险。

这是不可持续的。它会耗尽你的开发人员，减慢入职速度，并使跨团队协作成为一场噩梦。此外，它还会将本应成为战略优势（你所谓的可以重复使用的 API，如果你能找到它们的话）变成技术债务和团队摩擦的来源。更糟糕的是，当你 [将 AI 引入其中](https://thenewstack.io/ai-operations/) 时，API 将会成倍增加，因为 AI 将会编写它们。

## API 蔓延会拖累开发速度（和士气）

它从小处开始：一些重复的服务，一些不一致的命名约定，少数团队推出自己版本的相同 API，因为他们找不到原始版本（或者不信任它）。

但随着时间的推移，影响变得清晰：

- 新工程师需要数周才能上手。
- 如果敏感数据通过被遗忘或未被充分监控的 API 无意中泄露，则存在未知的数据暴露风险。
- 测试和部署周期变得非常缓慢，即使 59% 的技术领导者表示需要加速——非常多。
- 更改变得有风险，因为没有人知道谁拥有什么。
- 倦怠悄然而至，因为每次修复都感觉像一场消防演习。

简而言之：API 蔓延不仅仅是一个系统问题。这是一个人的问题。它正在吞噬你的生产力，并抑制你组织的可预测性、幸福感和速度。

在最近的技术领导者 [讨论开发人员生产力指标](https://www.getambassador.io/blog/what-engineering-teams-measure) 的小组讨论中，Keebo AI 的 [Mary Moore-Simmons](https://www.linkedin.com/in/mmooresimmons/) 分享了这条重要的信息，强调了这一点：“我明白跟踪开发人员的幸福感和满意度可能看起来很抽象，但它对于长期成功至关重要。 постоянно处于危机模式的团队无法反思、学习或成长。”

不处理你的 API 蔓延问题会让你的开发人员 постоянно处于危机模式。

## 停止治疗症状。解决根本文化。

你无法通过电子邮件发送给团队“请编写更好的文档”或启动另一个电子表格来跟踪服务来解决 API 蔓延问题。你需要一种 [文化转变](https://thenewstack.io/tech-culture/) —— 以及支持它的工具。可以简化这种文化转变的工具包括：
**帮助您发现和记录已有的内容：** 寻找能够绘制内部 API 蓝图的[API 开发](https://www.getambassador.io/blog/api-development-comprehensive-guide)工具，这样您就不会忘记在整个开发者环境中拥有的内容。 可见性是关键，不仅对您的开发者而言，而且对您的技术负责人而言，他们需要能够快速回答诸如“有多少 API，它们的成本是多少？”之类的问题。

**自动标准化：** 您需要生成一致、合规的 [API 规范](https://www.getambassador.io/blog/openapi-specification-structure-best-practices)，在这里您可以借助 [AI 辅助的规范生成](https://www.getambassador.io/products/blackbird/api-development)来确保标准化是重中之重。

**轻松实现并行开发：** 例如，寻找提供 [托管的、类似生产环境](https://www.getambassador.io/blog/prod-like-development-environments-improve-api-efficiency)的工具，让前端和后端团队可以构建和测试，而不会互相干扰。

## 展望未来：Sprawl 和 MCP 的未来

同样值得注意的是，随着人工智能的兴起，团队开始采用诸如 [模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) 之类的新兴框架，以帮助在代码中（也在 API 背后的思考中，即文化方面）保持一致性，并促进与大型语言模型 (LLM) 的上下文密集型交互。 MCP 将为团队提供一个共享模型，用于如何构建关系和端点，并减轻每个服务直接与 LLM 交互的独特 API 的负担。

将 MCP 视为团队如何设计、定义和发展集成的共享蓝图。 不要让每个人都用自己对 `user-service` 或 `billing-api` 的理解来随意发挥，MCP 强制执行可重用的、商定的结构。 结果与蔓延有什么关系？ 更少的冗余，更好的入职培训以及可以与您的组织一起扩展而不是对抗它的 API。

最终，这项新技术还将帮助解决更大的 API 蔓延问题，但与此同时，您仍然可以专注于文化变革，这将有助于您的开发团队腾飞。

## 文化变革始于可见性

许多工程领导者会争辩说，API 蔓延不是一个文化问题。 事实上，我们最近的调查显示，领导者认为开发者体验是他们最不关心的问题，只有 15% 的人认为这是一个问题。 但那是因为他们没有感受到开发者花费无数时间试图寻找东西的痛苦。

然而，许多人没有意识到的是，当您没有做好这一点时，其他 85% 的常见挑战（安全性、维护和成本超支）会变得更糟。 拒绝解决 API 蔓延及其对开发者体验的影响，彻头彻尾是一个文化问题，它使您的其他挑战变得更糟，从而花费您更多的金钱、时间和人力。

事实上，根据 Traceable 的一份报告，[48% 的组织都在与 API 蔓延作斗争](https://www.traceable.ai/blog-post/unveiling-the-2023-state-of-api-security-a-panoramic-industry-view)。 我敢打赌，更多的人在与它作斗争，但没有意识到这就是他们的问题所在。

看，你无法修复你无法看到的东西。 而现在，许多工程领导者在 API 蔓延方面都在盲目飞行——为安全风险、错过截止日期和开发者流失付出代价。 第一步不仅仅是技术性的。 它是人性的。

为您的团队提供协作工具和方法、避免重复的可见性以及快速行动而不精疲力竭的环境。