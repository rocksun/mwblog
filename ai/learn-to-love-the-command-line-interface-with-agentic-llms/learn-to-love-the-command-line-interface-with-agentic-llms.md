<!--
title: Agentic LLM：爱上命令行的理由
cover: https://cdn.thenewstack.io/media/2025/07/b70540fd-steve-johnson-qliinqnfux8-unsplashb.jpg
summary: 文章探讨了LLM在软件开发中的应用，认为命令行是LLM交互的最佳场所。LLM在模板生成、项目启动和代码更改方面表现出色。文章还提到了开发者需要具备人际互动技能，并建议让CLI成为LLM工作台的中心。
-->

文章探讨了LLM在软件开发中的应用，认为命令行是LLM交互的最佳场所。LLM在模板生成、项目启动和代码更改方面表现出色。文章还提到了开发者需要具备人际互动技能，并建议让CLI成为LLM工作台的中心。

> 译自：[Learn To Love the Command-Line Interface With Agentic LLMs](https://thenewstack.io/learn-to-love-the-command-line-interface-with-agentic-llms/)
> 
> 作者：David Eastman

我们已经到达了人工智能发展的一个关键时期，许多公司都在争夺关于LLM在编码方面正确方向的话语权。去年，我对结果基本上无动于衷，直到我开始看到代码自动完成功能根据标准命名和过去的模式，完成我的几个方法。

但今天我认为，对于大多数开发者来说，命令行是LLM交互的最佳场所。我已经看到了多个证明这一点的产品——从Anthropic的[Claude Code](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/)，Open AI的[Codex](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/)，谷歌的[Gemini CLI](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/)，以及最近的[Warp](https://thenewstack.io/warp-launches-ai-first-native-terminal-app-for-windows/)。下周我将关注一个略有不同的方向，即[kiro.dev](https://kiro.dev/)；但本周我想看看[Warp的Zach Lloyd](https://thenewstack.io/qa-how-warp-2-0-compares-to-claude-code-and-gemini-cli/)所说的“代理式开发环境”。

的确，这似乎是代理式时代，正如[Claude Code的使用量增长300%](https://thenewstack.io/claude-code-user-base-grows-300-as-anthropic-launches-enterprise-analytics-dashboard)所证明的那样。

[![](https://cdn.thenewstack.io/media/2025/07/aed0131f-image-1024x574.png)](https://cdn.thenewstack.io/media/2025/07/aed0131f-image-1024x574.png)

*[在www.tbench.ai上，代理在任务中的表现](www.tbench.ai)*

如图所示，终端和LLM模型有很多经过良好实践的组合。虽然Claude Code与Opus 4感觉像是一个最完整的软件包，但Warp通过提供更适合LLM的终端稍微改变了这种平衡。随着[terminal-bench](https://www.tbench.ai/)等工具引入了一套带有任务的良好评估工具，现在是尝试并找出最适合你需求的工具的好时机。

## 任务就是工程

但让我们退一步。大多数开发者的工作都是工程任务和编码的混合体。DevOps运动认识到，编码和基础设施支持很可能由同一批人完成——或者如果不是，也是由朝着相同生产目标共同努力的人们完成。但它们的方法不同。

开发者一直都知道这一点，但编码从来就*不完全是*一种工程形式——它比我们愿意承认的更像艺术。是的，甚至可能存在“一种氛围”。当你要输入一行代码时，总是有几种选项、表达式或方法可供选择。你既要延续你之前写的内容，又可能引导代码走向略有不同的未来形态。你在输入时就在脑海中构建模型。这就是为什么许多开发者仍然讨厌[结对编程](https://thenewstack.io/advance-your-devops-with-pair-programming-even-remotely/)——他们喜欢将最终决定推迟到最后一个负责任的时刻。过早地解释自己会迫使你打开盒子，在你准备离开叠加态之前观察猫。

> 命令行是我们执行定义任务的地方。有一个期望的结果，并且可能有一种明智的方法来实现它。

而这正是LLM擅长命令行界面（CLI）的原因，因为那是我绝对在做工程的地方。命令行是我们执行定义任务的地方。有一个期望的结果，并且可能有一种明智的方法来实现它。例如，如果我对代码进行了更改，那么我需要git来暂存、提交和推送它们。我唯一真正的决定是提交消息——而LLM在这方面做得很好。

突然之间能够用英语编写一个任务，并让它自动完成——或者通过定义阶段并请求许可——提供了与自己完成任务的可衡量比较。LLM实际上只是将你的陈述映射到现有命令（和脚本）的列表。

## LLM在开发任务中何时表现出色？

在编写代码时，LLM在过程中的特定时间表现出色。它们是优秀的模板生产机器。即使它们只是从互联网上获取正确的示例，并将其放置在你项目的正确上下文中，那也是真实的、可衡量的工作。如果它是可衡量的，我们就可以计算出我们获得了什么。但它们的作用在编写代码之前，或者在代码基本编写完成后进行更改时最强大。

当你使用IDE时，快速代码完成可能很有用，但它也可能在很多时候碍事。当我犹豫时，那是因为我的大脑正在处理代码——我不是在等待被指导。这种中断通常感觉像是一种冒犯。随着时间的推移，这种情况显然会得到改善，但就目前而言，它不是主要事件。

开发工作不仅仅是盯着编辑器中的代码。计划、网络设计、部署、调试等等。即使我不提倡[让LLM直接编写测试](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/)，它们也可以做到。通过要求CLI中的LLM为你设置一个通用环境和一个模板示例来启动一个项目是很棒的。要求它在你的代码库中进行更改，就像[我使用谷歌的Jules所做的那样](https://thenewstack.io/agentic-coding-how-googles-jules-compares-to-claude-code/)，确实需要一些提示工程技能。但如果它一开始做得不够好，那就再试一次。

如果它真的搞砸了，大多数开发者会使用git来回退。在大多数情况下，这与让一位初级开发者开发代码库没有什么不同——这也是为什么人际互动是开发者必须具备的另一项技能，才能成功完成他们的工作。

即使是该死的[氛围编码](https://thenewstack.io/vibe-coding-is-here-how-ai-is-reshaping-the-software-developer-profession/)也有其用武之地；例如，当你在进行冲刺零时，集思广益，并且你想辨别出可能性的艺术（也许和你的经理一起）。写下你想看到的东西，而对如何实现它没有太大兴趣，在这些情况下是完全有意义的。

## 结论

我最喜欢的艺术家之一是Olafur Eliasson。他的工作室是一个协作中心，拥有近百名专业人士，包括工匠、技术人员、建筑师和艺术史学家。无论他如何看待艺术，他都将创作艺术视为一种集体努力，团队成员在开发和安装艺术品中发挥自己的作用。

[![](https://cdn.thenewstack.io/media/2025/07/ef555af6-image-1-1024x682.png)](https://cdn.thenewstack.io/media/2025/07/ef555af6-image-1-1024x682.png)

*[Olafur Eliasson的一个装置](https://thespaces.com/olafur-eliassons-living-observatory/)*

他明白，就像我们开发者应该明白的那样，虽然艺术是一个人脑的产物，但它周围有很多工程。无论如何，让IDE成为你代码流动的地方，但让CLI成为你LLM工作台的中心。