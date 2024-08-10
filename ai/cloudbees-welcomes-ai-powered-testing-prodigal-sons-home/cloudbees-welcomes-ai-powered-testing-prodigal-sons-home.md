
<!--
title: CloudBees 欢迎人工智能驱动的测试，“浪子回头”
cover: https://cdn.thenewstack.io/media/2024/08/3d9881df-welcome-sign-724689_1280-1.jpg
-->

CloudBees 的新 AI 技术可以预测哪些测试可能会失败，使开发人员能够在开发过程的早期阶段关注潜在问题。

> 译自 [CloudBees Welcomes AI-Powered Testing, ‘Prodigal Sons’ Home](https://thenewstack.io/cloudbees-welcomes-ai-powered-testing-prodigal-sons-home/)，作者 Darryl K Taft。

DevOps 专家 CloudBees 通过收购专注于优化软件测试和开发流程的 AI 公司 Launchable，为其 CI/CD 和 DevSecOps 平台增加了新的 AI 功能。

具有讽刺意味的是，促成此次收购的关键因素在于返回 CloudBees 的 Kohsuke Kawaguchi 和 Harpreet Singh，他们是曾从事过 Jenkins（前身为 Hudson）的 CloudBees 前雇员。2019 年，这两名前员工离开 CloudBees 创立了 Launchable。

该公司的首席产品官 Shawn Ahmed 表示，这两位回归者将在 CloudBees 担任 AI 联合主管。Launchable 的创始人同时拥有丰富的 DevOps 和 AI 经验，这使得此次收购对 CloudBees 未来的人工智能计划至关重要。

![](https://cdn.thenewstack.io/media/2024/08/252320d6-image001-4-1-300x300.png)

*Shawn Ahmed, Chief Product Officer, CloudBees*

## 这两项主要挑战

借助新的 AI 功能，CloudBees 旨在应对软件开发中的两项主要挑战：优化质量保证和测试流程；以及对流水线失败进行分类，Ahmed 说。

他指出，在过去两年里，AI 和 ML 对软件开发产生了深远的影响，特别是在使用 Microsoft/GitHub Copilot、Amazon Q 等解决方案生成代码的领域。而且开发人员从能够在身边拥有一个编码助手以生成更多代码中受益匪浅。

“但问题是，交付流水线仍然保持相同。”艾哈迈德告诉 The New Stack。“另一个不变因素是，一天有 24 小时，你必须在同一时间窗口内运行你的构建流水线、测试流水线和部署流水线。当这些相同的流水线中生成的大量代码量大幅增加且受到这些约束时，每个人都关心的问题是如何将大型语言模型、机器学习和人工智能等技术应用到用例，以及在你提交代码之后发生的一切？”

Ahmed 表示，为了在流水线的测试阶段节省数小时，Launchable 已采用一种创新的方式来看待诸如“不稳定的”测试之类的问题。他解释说，他们开始关注测试失败，并开始在开发人员进行的代码更改类型和将会失败的测试类型之间建立联系，并开始预测哪种类型的代码更改会导致哪种类型的失败。

“现在，假设你要运行 50 个测试，前 49 个通过，但第 50 个失败，并且运行需要 55 个小时。如果你知道第 50 个测试将失败，为什么还要花费所有这些小时来运行你知道会通过的 49 个测试？”他说道。“为什么不首先运行第 50 个测试并为其创建一个测试套件，并更快地让代码失败，以便你可以将所有用于运行原本会通过的测试的时间拿过来，在稍后运行它们，但重点是将时间还给开发人员？”

这正是 Launchable 的核心所在，由于 CloudBees 客户群都在使用 Jenkins，用户可以“通过几次对 Launchable 技术的调用补充他们的管道，并预测哪些测试将失败，利用 AI 对错误进行分类，并向开发人员提供有关如何修复的解决方案事实，从而为他们的开发人员节省大量时间。”Ahmed 解释道。

这可以借由减少不必要的测试和对潜在故障提供更快速的反馈来节省开发人员的时间。

在 7 月进行的 Stack Overflow 的 2024 开发者调查中，46% 的开发者表示他们对使用 AI 来测试代码感兴趣——这在所有被询问的工作流中所占的百分比最高。并且 81% 的专业开发者表示他们认为在明年使用 AI 来测试代码会与他们的工作流程实现更紧密的集成。

## Jenkins Boys Home

“所以他们[Kawaguchi 和 Singh] 有了很棒的体验，并且是第一个思考如何将 AI 应用于 DevOps 的人，”CloudBees 的联合创始人兼首席战略官 [Sacha Labourey](https://www.linkedin.com/in/sachalabourey) 在接受 The New Stack 采访时表示。“这早于任何人在谈论 [LLMs](https://thenewstack.io/choosing-when-to-use-or-not-use-llms-as-a-developer/)。从 2019 年开始，这些人一直在日复一日地进行 DevOps 和 AI。所以，在使这一切变得非常现实方面，这对我们来说非常合适。Kohsuke 和 Harpreet 回来了，这真的很酷。”

![](https://cdn.thenewstack.io/media/2024/08/ebe40b25-kohsuke-300x296.jpg)

*Kohsuke Kawaguchi，Jenkins 的创建者，Launchable 的联合创始人*

一位分析师表示，也许 AI 驱动的测试确实会让开发人员有更多时间来开发新功能。

“Kohsuke 回到 Jenkins 社区真的很酷，但他带着 Launchable 来到了这里，它提供了一种将深度 AI 测试分析注入 CI/CD 流水线的方法，这应该会大大减少他们运行的任何测试框架的误报，从而减少开发人员的分类和调查时间，”[Jason English](https://www.linkedin.com/in/jasonenglish/), Intellyx 的分析师，在接受 The New Stack 采访时表示。“由于 Launchable 已经考虑到了 Jenkins，因此现有用户应该能够在第一天就启用该功能。”

此外，“Jenkins 继续主导 CI/CD DevOps 市场。Jenkins 管理着数十万个测试套件，CloudBees 可以将 Launchable 解决方案部署到每个测试套件中，并使用 AI 来提高其效率，”Singh 在一篇 [博客文章](https://www.launchableinc.com/blog/cloudbees-acquires-launchable-to-bring-ai-powered-insights/) 中写道。“除了 Jenkins 之外，市场上还有几个 CI 供应商。Launchable 的方法也是 CI 独立的。因此，CloudBees 可以帮助那些无论这些流水线存在于哪个提供商上，都难以进行 QA 的人。”

[Jenkins 占据了 CI/CD 工具市场约 47%](https://6sense.com/tech/continuos-integration/jenkins-market-share)。根据 [6sense](https://6sense.com/) 的数据，Jenkins 在持续集成和交付类别中的前三大竞争对手分别是 Atlassian Bitbucket，市场份额为 18.47%，CircleCI，市场份额为 5.76%，TeamCity，市场份额为 5.52%。

“你不能不谈论 Jenkins 就谈论 CloudBees，你不能不谈论 Kohsuke（Launchable 的联合首席执行官），它的创建者，”Singh 写道。

事实上，“让 Kohsuke 和我（Launchable 的创始人）的旅程变得甜蜜的是，我们曾经与 CloudBees 的创始人并肩作战，帮助他们在早期建立 CloudBees。这对我们来说是一个回家之旅，我们对此感到无比兴奋，”他在帖子中写道。
