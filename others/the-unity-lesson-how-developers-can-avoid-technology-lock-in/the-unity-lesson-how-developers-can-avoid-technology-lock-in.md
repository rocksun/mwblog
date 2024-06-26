<!--
# Unity 的教训：开发者如何避免技术锁定
https://cdn.thenewstack.io/media/2023/09/002be36c-sigmund-by-tzimt0ms-unsplash-1024x768.jpg
Image via Unsplash
-->

当你的产品模型定义良好，并非紧密地缠绕在某些技术中时，有经验的开发者就可以正常工作。

译自 [The Unity Lesson: How Developers Can Avoid Technology Lock-In](https://thenewstack.io/the-unity-lesson-how-developers-can-avoid-technology-lock-in/) 。

## 团结的教训: 开发人员如何避免技术锁定

虽然我之前在[先前的帖子](https://thenewstack.io/how-to-start-unity-development-even-if-youre-not-a-gamer/)中提到了 [Unity](https://unity.com/) 平台，因为它为面向大多数设备的基于 UI 的应用提供了可靠的解决方案，但它仍然是专门为游戏行业设计的。然而，最近的新闻和正在进行的故事已经进入主流媒体，[因为游戏开发社区的反应](https://www.bloomberg.com/news/newsletters/2023-09-15/unity-technologies-rolls-out-new-fees-destroys-its-goodwill-with-developers)。在使用 Unreal 或自己的引擎制作“AAA”游戏的大型工作室之外，Unity 在独立开发者和小团队中非常流行。该平台在大学里很受欢迎，这导致许多学生的首次开发经验都是 C#。Unity 也是移动开发的一个流行平台，这可能[会给苹果](https://appleinsider.com/articles/23/09/20/unitys-self-sabotage-with-pricing-will-be-a-long-term-problem-for-apple)带来问题。

## Unity 的撤退

这个悲伤的传奇故事始于宣布改变 Unity 的盈利方式，从标准许可协议到所谓的“运行时费用”，对每次安装收取费用，游戏越过某些阈值后。这种激进的改变肯定从未出现在公司的路线图上，而且代表着服务条款的追溯性更改。许多开发团队在社交媒体上表达了他们对这一严重违反信任的关切。

根据安装次数进行盈利在该行业没有工作实例，原因充分。Unity 没有解释他们将如何准确收集这些统计数据，以及这可能会跨越哪些隐私和安全界限。有人指出，如果开发者向一个成功的慈善捆绑包提供已发布的游戏，安装次数的激增可能会使他们破产。还有恶意重新安装的可能性，这显然会有问题。

*0.20 美元 - 小开发者(Unity 个人订阅者)的每次安装费用，其游戏在过去一年中获得 20 万美元收入，并且累计安装量达到200，000。*

很明显，Unity 从未与任何实际开发者就其潜在的改变细节进行过认真讨论，并以不令人信服的变通方法和公关策划的不道歉来应对。就我写这篇文章而言，这场撤退仍在进行，像电视剧编剧罢工期间的肥皂剧。对许多开发者来说，总的情况是 Unit y不再是一位值得信赖的合作伙伴，如果不立即道歉并取消运行时费用，情况会一直如此。

游戏行业在认识恶意行为方面仍存在一定程度的不成熟，这可能是由于该行业的爱好者根源所致，这导致人们假设每个人都在热爱它。所以现在小团队正在抓紧离开 Unity，即使是在项目中途。

## 采用不可知论的技术观点

这篇文章的重点是采用不可知论的技术观点; Unity 的恶行只是再次这样做的一个原因。除了最近的事件之外，Unity 是一个典型的软件即服务(SaaS)提供商。没有任何理由相信另一家类似的 SaaS 公司不会试图实现类似的模型。

在飞机飞行过程中改变引擎技术并不总是容易做到的。这可能会惊动乘客。在软件行业内，准备好应对变化的关键是尽早将产品的意图与其内部分离。这意味着在公司内外，任何人都可以用一个丰富的模型来描述产品或系统，展示客户问题、解决方案和流程，而从不将其与任何特定技术栈耦合。

因为没有人知道何时一个至关重要的流水线组件或供应商可能变得不经济，或者被一个不稳定的所有者购买，永久警惕是必需的。这可能会使小公司受困，那些没有人力不断审查其所有协议和合同的公司。

这些想法一开始看似显而易见，但随着注意力的流失，边缘地带开始破裂。你会听到“它存储在 S3 中”，而它应该只是“存储在云中”。或者“一切都在 git 中”，而不是“一切都在源代码控制中”。或者“我们有备份数据库”，而不是备份数据源。这似乎是一种含混的食谱，但尊重您控制的事物和您不控制的事物之间的界限是必不可少的。当 CTO 列举出其系统使用的所有先进技术时，这可能看似很酷，但这只会束缚开发者的手脚。不需要很长时间一个企业与一项技术就会过于紧密地耦合——这就是为什么数据库提供商甲骨文公司例如会如此成功的原因。

## 界限很重要

产品和外部组件之间的界限变得很重要。当产品使用大型语言模型(LLM)时，您会想知道这现在是一款AI产品还是一款可以使用 AI 的产品？该产品的命运是否与 LLM 的能力同生共死？该产品能否使用其他供应商，或者训练数据现在是否被原始 LLM 捕获?

当一个产品在另一个产品的生态系统中可用时，这种界限混淆也可能发生。我们看到当[苹果对 Epic 游戏公司](https://appleinsider.com/articles/20/08/23/apple-versus-epic-games-fortnite-app-store-saga----the-story-so-far)希望在苹果应用商店内使用自己的支付系统感到不快时就发生了这种情况。

当产品模型定义清晰，且与其他组件和平台没有紧密交织在一起时，有经验的开发人员可以有效地工作。他们知道何时使用现成的开源软件，何时使用定制的 SaaS 解决方案，以及何时在内部编写特殊的自定义库。

## 正确定义您的产品

如果产品的设计以不涉及技术规范的方式表达出来，那么你可以信任开发人员来选择（或拒绝）正确的组件组合。在充分利用组件的同时，不必改变调用产品的运行方式以利用其优势之间存在一种创造性的紧张关系。

因此，为了避免 Unity 开发人员现在必须从头学习新的平台并可能不得不重写大量代码的痛苦，请保持您的物理和心理模型分离。即使改变的工作量仍然很大，您至少可以有一个可以向他人解释和有效估算的可解释工作。
