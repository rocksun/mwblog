
<!--
title: DevOps迈向自动化之外，应对新挑战
cover: https://cdn.thenewstack.io/media/2024/11/24340e25-quino-al-uwu5qhetnvc-unsplash-1.jpg
-->

随着基础 DevOps 采用的普及，组织正在将重点转移到新的领域，包括安全集成、弹性和组织转型。

> 译自 [DevOps Moves Beyond Automation to Tackle New Challenges](https://thenewstack.io/devops-moves-beyond-automation-to-tackle-new-challenges/)，作者 Eric Newcomer。

纽约 - 最近在纽约举行的 [DevOpsCon New York](https://devopscon.io/new-york/) 大会上，演讲者和参展商明确表示，[DevOps](https://thenewstack.io/devops/) 正在迎接新的挑战，其中大多数挑战都建立在 DevOps 基础之上。

新的挑战包括 [DevSecOps](https://thenewstack.io/decoding-devsecops-striking-the-right-balance/)、提高弹性和安全程序、缩短事件解决时间、引入 [AI 助手](https://thenewstack.io/augment-ai-code-assistant-targets-large-development-teams/) 以及重新调整组织角色和职责，以更好地实施 DevOps 方法。

据大多数人说，DevOps 开始于 [大约十五年前](https://devops.com/the-origins-of-devops-whats-in-a-name/)，作为一种减少开发和运维团队之间摩擦并加快软件部署速度的方式。

许多组织发现 DevOps 既是文化变革，也是技术变革，因为它改变了运维和开发人员之间的界限。DevOps 的许多新方向也将影响 IT 文化。

大会主题演讲描述了 [Kubernetes](https://thenewstack.io/kubernetes/) 的架构考虑因素、开发人员生产力的 AI 专业知识策略、下一级可观察性、提高弹性和建立组织信任。

展区内的供应商极力宣传以正确的方式进行 DevOps 的优点，加强自动化测试和修复、部署更好的可观察性以及改进 [CI/CD](https://thenewstack.io/ci-cd/) 流水线技术。

## 这不是一条单行道

大约 15 年前，DevOps 开始时，“人们将其视为一条单行道”。

参展商 [Keysight](https://www.keysight.com/us/en/products/software/software-testing.html) 的高级解决方案架构师 [Steve Barreto](https://www.linkedin.com/in/stevebarreto/) 告诉 The New Stack。
“但事实并非如此 - 这是一个生命循环，”他说，其中 Keysight 的 [Eggplant](https://www.keysight.com/us/en/products/software/software-testing/eggplant-test.html) 等产品不断测试应用程序行为并对其进行改进。“当在流水线测试中发现 UI 异常时会发生什么？”

Barreto 说，Eggplant 的数字自动化智能 (DAI) 功能提高了与 CI/CD 流水线的集成速度。“DAI 根据过去测试的行为发现异常，并自动打开带有注释的工单。

“例如，如果移动应用程序按钮出现异常，无法按预期工作，Eggplant DAI 会将屏幕截图以及错误报告附加到工单中。”

在开发人员纠正异常并重新启动流水线后，开发生命周期的循环再次开始。开发人员意识到，仅仅自动化部署过程是不够的 - 下一步是持续部署修复。

## 通过设计提高弹性

在题为“弹性实践：叙事、共同点和复杂性”的主题演讲中，[Ergonautic](https://www.ergonautic.ly/) 的负责人 [Jabe Bloom](https://www.linkedin.com/in/jabebloom/) 概述了一种通过 DevOps 提高弹性的方法，该方法考虑了设计中的风险和使用中的风险。

Bloom 说，设计中的风险是在规划过程中可以预期的风险，而使用中的风险是在生产中发生的意外事件。

首先，尽可能消除设计中的风险，然后专注于处理使用中风险的过程。特别是，要注意参与响应压力或故障系统的相关人员的认知负荷。

Bloom 说，虽然你无法完全消除风险，但你希望设计系统使其能够快速恢复。重要的是，从意外事件中快速恢复的弹性只能来自人机交互。

他说，CI/CD 流水线等技术会影响系统中人类行动的范围，并且应该以减少相关人员的认知负荷为导向。

## 改进流水线

“开发人员面临的最大挑战之一是安全地引入变更，并赋予开发团队以信心进行变更的能力，”CircleCI 产品管理副总裁 [Aakar Shroff](https://www.linkedin.com/in/aakarshroff/) 告诉 The New Stack。

“十多年前 CircleCI 开始时，开发人员刚刚开始适应持续测试的想法，并且刚刚开始实施 CI/CD，”他说。

Shroff 补充说，CircleCI 确保开发人员在整个系统中对他们的更改、运行位置、是否存在需要回滚的事件等方面具有可见性。
“在其他环境中模拟生产工作/用户工作负载并不容易，”他说。“分析运行可以提供帮助——运行应用程序的两个版本并比较结果。这始终是速度和安全之间的权衡，但当你消除对导致事件的更改的恐惧时，推出速度会更快。”

特别是，“CircleCI 将其可见性范围扩展到代码库之外。例如，当您依赖的第三方库或 API 发生更改时，我们将自动验证与您的应用程序相关的更改，”Shroff 说，“最终，这将为团队提供更多信心来加快速度，并使他们能够为客户提供价值。”

CircleCI 建议开发人员使用渐进式推出，以帮助在更新期间安全地将流量转移到新的代码版本。当与 Argo rollouts 等应用程序集成时，开发人员可以验证关键流水线指标，以确认部署或触发回滚。

“为了改善开发人员体验，”Shroff 说，“我们确保根据对开发人员的持续反馈进行持续的流水线优化，以突出显示与标准实践的偏差。”

在这方面，流水线标准化也可以被视为 DevOps 面临的下一个挑战之一。

## 改善组织

[John Willis](https://www.linkedin.com/in/johnwillisatlanta/)，Botchagalupe Technologies 的创始人，三本 DevOps 书籍的作者，DevOps 文章的常客贡献者以及受欢迎的 DevOps 会议演讲者，在他的会议上重点介绍了组织转型。

他的主题演讲“超越复选框：嵌入真正的网络弹性”提出了一个组织蓝图，用于将安全内在地融入业务能力。

他谈到了“债务和弹性”，并描述了 GenAI 如何帮助识别问题和潜在解决方案。

Willis 的演讲结合了 [W. Edwards Deming](https://en.wikipedia.org/wiki/W._Edwards_Deming) 的 [深刻知识体系](https://deming.org/explore/sopk/)，他将其引用为组织转型的 методология。Willis 还写了一本 [关于 Deming 的书](https://www.amazon.com/Journey-Profound-Knowledge-Altered-Industry/dp/1950508838)，他说他认为 Deming 的体系影响了我们今天的工作方式以及未来将如何工作。

“我们是运行 DevOps 和基础设施的人，并不总是意识到技术债务带来的风险，”Willis 说，包括 [影子 IT](https://thenewstack.io/how-to-bring-shadow-kubernetes-it-into-the-light/) 和 [影子 AI](https://cloud.google.com/transform/spotlighting-shadow-ai-how-to-protect-against-risky-ai-practices) 的风险。

为了消除这些风险并实现转型，Willis 建议打破机构孤岛，以更好地协调业务、IT 和网络安全的角色和责任，从而改善事件响应。

对 Willis 来说，DevOps 的成功与否，在很大程度上取决于组织结构是否正确，以及是否提高所有系统的质量，从而创造真正的网络弹性。

从这个意义上说，成功的 DevOps 转型不仅仅是关于新的系统或技术，还关于改变思维方式，培养一种拥抱持续改进的文化。

## DevSecOps 是未来吗？

“DevOps 的未来是 DevSecOps，”[Jonathan Singer](https://www.linkedin.com/in/jonathanayalsinger/)，[Checkmarx](https://checkmarx.com/) 的高级产品营销经理，告诉 The New Stack。

“开发人员需要将高性能代码视为安全代码。现在一切都是代码，如果它不安全，它就不能高性能，”他补充道。

Singer 说，Checkmarx 是一家应用程序安全供应商，允许企业从第一行代码到云中部署来保护其应用程序。

他指出，DevOps 的视角必须与应用程序安全视角相同。有些人认为看到应用程序周围的环境，但 Checkmarx 认为看到应用程序中的代码，并确保它在部署时是安全和安全的，他补充道。

“这可能看起来像是安全团队将更多责任交给了开发团队，因此你需要在开发团队中配备安全人员，”Singer 说。

Checkmarx 通过优先排序和分类扫描结果来自动化繁重的脑力劳动。对于大量代码，尤其是对于大型组织，发现一万个漏洞是相当常见的，但它们会有不同的严重程度。

如果漏洞不可利用，您可以将其从结果列表中删除。“现在我们进入了降噪游戏，”他说。
