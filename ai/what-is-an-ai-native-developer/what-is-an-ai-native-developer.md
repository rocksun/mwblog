<!--
title: 什么是AI原生开发者？
cover: https://cdn.thenewstack.io/media/2025/02/8156678c-getty-images-vabamsqjnr8-unsplashb.jpg
summary: 我们将解释什么是 AI 原生开发人员，该角色将如何演变，以及为什么规范驱动的 AI 开发正在推动这一趋势。
-->

我们将解释什么是 AI 原生开发人员，该角色将如何演变，以及为什么规范驱动的 AI 开发正在推动这一趋势。

> 译自：[What Is an AI Native Developer?](https://thenewstack.io/what-is-an-ai-native-developer/)
> 
> 作者：Jennifer Riggins

按照目前的发展趋势，每位软件工程师很快都将不得不成为 AI 原生开发者。不，这并不意味着 [AI](https://thenewstack.io/ai/) 会被植入你的大脑。也不意味着你必须在你的 [科技职业生涯](https://thenewstack.io/tech-careers/) 中一直与 AI 打交道。

“AI 原生开发者”甚至是一个用词不当，因为它并非取决于个人，也不一定与构建 AI 应用程序、概念、算法或模型有关。

在这种情况下，AI 实际上是通过作用于特定目的的 AI 附加组件嵌入到整个 [软件开发生命周期](https://thenewstack.io/software-development/) (SDLC) 中，以便开发者可以专注于交付差异化价值。“云原生 AI”可能是一个更好的术语。无论如何，自然语言支持的生成式 AI 将继续是一个积极的结对程序员。

但是，如何充分利用你现在或即将拥有的 [AI 原生软件开发团队](https://thenewstack.io/ai-engineering/)？如何将 AI 战略性地整合到 SLDC 中？如何安全地完成这一切？

## 规范驱动的 AI 开发的兴起

目前软件开发的重点是将 AI 融入现有开发者工作流程的各个部分，寻找自动化的机会。但并非所有人都认为这是明智的前进方向。

Snyk 的创始人，现在的 [Tessl](https://www.tessl.io/) 的 [Guy Podjarny](https://www.linkedin.com/in/guypo/) 在伦敦的 State of Open Con 大会上的一次演讲中说：“真正的潜力在于你真正重新思考工作流程。在这种强大技术出现之际，我该如何重新思考软件开发？我们的观点是，软件开发将从以代码为中心转变为以规范为中心。”

> “我们的观点是，软件开发将从以代码为中心转变为以规范为中心。”
>
> – Guy Podjarny, Tessl 创始人

这种新方法着眼于在你的规范中构建护栏，这种规范有可能默认生成更安全、更高质量的 AI 生成代码。规范驱动的开发，又名行为驱动的开发 2.0，遵循三个步骤：

- 使用简单的语言来描述新功能。
- 基于这些新规范开发代码。
- 测试代码以确保其与规范匹配。

通过扩展，规范驱动的 AI 开发会在 AI 应用程序的功能周围设置设计护栏。

与所有规范驱动的开发一样，这允许：

- 提高一致性和治理。
- 更早地验证正在构建的内容是否应该是构建的内容。
- 技术和业务利益相关者之间以自然语言进行协作和沟通。

最后一个好处尤其重要，因为 AI 生成的代码通常不具备大型语言模型 (LLM) 所做决策的原因和方式的可解释性。

AI 原生的意义在于让 AI 创建你实际想要的东西，然后可以在这个新的单一事实来源（你的规范）中进行澄清。与现状（你的单一事实来源是你的代码）形成对比。

Podjarny 说：“今天的软件开发非常以代码为中心。你得到一些需求，你编写一些代码，你做出 100 个永远不会返回、永远不会进入系统的决策。” 有时会创建测试和文档，但很少是彻底的，也不会保持最新。

他继续说，真正经受住时间考验的唯一资产是代码。

“一年后，祝你好运，试图找到需求、错误修复和增强定义的痕迹，这些痕迹说明：要求是什么？应用程序应该做什么？”

但是，即使你不直接更改你的代码，它也会发生变化，因为依赖项、实现、环境和/或集成会发生变化。正如 Podjarny 所说，“你的代码生活在一个动态环境中”，即使你不涉及应用程序，你也会承担破坏它的风险，而这同样没有在任何地方捕获。

“因此，应用程序变得脆弱，”他补充道。

> 该规范包含你的应用程序应该做什么的定义，以及验证 AI 生成的代码是否正确并符合规范的测试。

当涉及到 AI 时，软件开发团队离代码的为什么、如何和什么更远了。与往常一样，对接触代码的恐惧随着代码年龄的增长而增加。

Podjarny 认为，通过规范驱动的 AI 开发，你“将这些需求从一次性的东西（在开始时出现并消失）转变为位于中心且长期存在的东西”。
该规范包含了你的应用程序应该做什么的定义，以及验证 AI 生成的代码是否正确并符合规范的测试。这段代码变得越来越不可更改和可抛弃。

但这只是你成为 AI 原生开发团队的其中一步。

## 运行你自己的开源 LLM 的理由

从影子 AI 到只有不到一半的公司拥有[AI 治理策略](https://leaddev.com/software-quality/ai-governance-policy-engineering-managers-needed-yesterday)（工程经理们昨天就需要了），大多数 AI 生成的代码在没有任何边界或指导方针的情况下被创建和发布。通常甚至没有测试或人工参与。

即使没有所有这些限制，42% 的组织正在考虑[开发他们自己的专有大型语言模型](https://wire19.com/cios-in-the-us-rate-security-as-the-top-concern-in-gen-ai-adoption/)。我们可以假设这些企业中实际上很少有 AI 公司，因此这可能会让他们专注于非差异化但昂贵的工作。

“我们如何建立我们自己可以信任的内部 ChatGPT？为了阻止人们进行影子 AI，因为这样，他们就可以使用内部版本，而不是在手机上偷偷使用 ChatGPT，” [Luke Marsden](https://www.linkedin.com/in/luke-marsden-71b3789/)，[HelixML](https://tryhelix.ai/) 的 CEO，告诉 The New Stack，很多公司都在考虑。

然而，他认为，解决方案不在于像 ChatGPT 或 Gemini 这样的专有产品，而在于像 DeepSeek 这样的开源 LLM 在速度和质量方面正在成为挑战者。

> “如果你想想 Linux 与 Windows，开源在服务器上胜出了。为什么它不会在这一波新的 AI 浪潮中再次发生呢？”
>
> – Luke Marsden, CEO of HelixML

“如果你想想 Linux 与 Windows，开源在服务器上胜出了，” Marsden 说。“为什么它不会在这一波新的 AI 浪潮中再次发生呢？”

除了你不需要训练世界上最富有公司的私有大型语言模型之外，还有其他令人信服的理由来托管你自己的开源 LLM 版本。这包括你可能将别人的专有代码放入你的产品中，或者因为你用你的公司机密训练了一个公共 LLM 而冒着你自己的版权风险。

然而，大多数技术领导者首先想到的是 [LLM 安全风险](https://thenewstack.io/7-llm-risks-and-api-management-strategies/)。总的来说，到目前为止，[AI 生成的代码比完全由开发人员编写的代码更容易出错](https://thenewstack.io/more-ai-more-problems-for-software-developers-in-2025/)，并且提示注入是另一个高度存在的 [AI 安全风险](https://leaddev.com/software-quality/how-combat-generative-ai-security-risks)。

“任何拥有重要或有价值的机密的公司或组织都会想确保他们已经锁定了这项技术的使用，” Marsden 说。但是，“与此同时，他们面临着创新的压力。”

人们常常毫无根据地不信任开源软件和 AI 模型，认为它们本质上不如其专有产品安全。无论你的组织是否也有这种担忧，或者你只是想避免供应商锁定和成本，Marsden 都提倡在你的防火墙内本地使用开源 LLM。

“有很多组织，仅仅是出于监管原因，无法将他们的数据发送给大型云提供商，并且正在运行他们自己的基础设施。现在有一种趋势是回到私有云上运行，将他们的数据迁回，”他说。

“一切都在本地的事实本质上更安全，因为你没有将数据发送给一些不受信任的第三方。”

这是去年在 GPU 短缺危机期间无法轻易获得的选择；但现在，Marsden 说，GPU 的价格已经大幅下降，并且它们已经再次变得广泛可用。

> 使用开源 AI 原生应用程序的另一个重大优势是，它允许你将其集成到你的 DevOps 和软件工作流程中。

他认为，运行你自己的 LLM 的另一个优势是，这些开源推理模型（如 DeepSeek）运行的时间越长，答案就越好。这反过来又促使组织回到他们自己的硬件上运行，因为你在云中运行模型的时间越长，云成本就越高。

使用开源构建 AI 原生应用程序的另一个重大优势是，它允许你将其集成到你的 DevOps 和软件工作流程中。这使团队能够提出非常具体于他们组织的问题，Marsden 说。他举了几个例子：

- 当前的 sprint 中有什么？
- 你能帮我为分配给我的问题编写一些代码吗？

“你可能希望你的Jira助手在10种不同的情况下都能表现出色。你可以做的是将这些情况编写成测试，”他说。类似于你为你构建的软件编写测试，但这是为GenAI应用程序编写测试，然后“这些测试使用自然语言规范来定义什么是正确的答案。”

然后，Marsden继续说道，你可以应用LLM-as-a-Judge模式作为一种评估方法，来评估这些响应的质量——不仅是按照通用标准，而且是在组织及其治理的背景下。你仍然可以选择人工参与（human-in-the-loop）来检查测试是否良好，然后再将该测试能力集成到你现有的CI/CD工作流程中，以便每次都运行测试。

## Prompt工程的衰落

在过去的两年里，对于人工参与（human-in-the-loop）的prompt工程师角色需求巨大，他们编写特定的、基于上下文的示例和指令，以帮助指导AI模型产生更好、更具体的响应。这种趋势可能不会持续到2025年以后。

[Prompt engineering](https://thenewstack.io/prompt-engineering-get-llms-to-generate-the-content-you-want/)（提示工程），与主题专家和客户的反馈相结合，在未来一两年内可能仍然会存在——特别是客户服务聊天机器人似乎还有很长的路要走。
然而，在即将发布的[Thoughtworks’ Technology Radar](https://www.thoughtworks.com/en-gb/radar)（Thoughtworks技术雷达）的抢先预览中，有一个令人惊讶的趋势，即[decline of prompt engineering](https://www.linkedin.com/posts/mikemasonca_here-at-the-thoughtworks-technology-radar-ugcPost-7297461603166273536-jTQO/?utm_source=share&utm_medium=member_ios&rcm=ACoAAABZmmABHm6J2XQbSClzhanawgObP3_uJWc)（提示工程的衰落）——也许是因为我们已经和机器人聊得太多了？

“这实际上是因为像[DeepSeek-R1](https://www.deepseek.com/)这样的推理模型以及OpenAI的一些东西的兴起，如果你实际上在提示中放入太多的东西，它实际上可能会降低响应的有用性，”Thoughtworks的首席AI官Mike Mason说。

> “这可能会改变我们进行提示工程的方式。”
>
> – Mike Mason, chief AI officer at Thoughtworks

Mike Mason说，OpenAI的CEO Sam Altman“暗示”ChatGPT-5将是模型风格的融合，它可能会进行适量的推理。

“这可能会改变我们进行提示工程的方式，”Mike Mason说，或者甚至很快消除对该角色的所有需求。

可能影响这种变化的还有AI原生软件开发的兴起。虽然可能仍然会有与文档和代码库的自然语言对话，但大部分提示将在后台自动完成，启动由行业和组织规定的操作节奏。

随着AI原生软件开发中的这些技术角色的变化，有一件事是肯定的：我们不会很快摆脱人类开发人员。