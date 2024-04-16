
<!--
title: 内部开发者平台之后是什么？
cover: https://cdn.thenewstack.io/media/2024/04/bbb38350-pendulum.jpg
-->

随着构建和维护内部开发者平台的复杂性，还有其他人觉得钟摆即将落下吗？

> 译自 [What Comes after Internal Developer Platforms?](https://thenewstack.io/what-comes-after-internal-developer-platforms/)，作者 Valerie Slaughter。

事物往往是循环发展的。我们总是在一个极端和另一个极端之间摇摆，对之前发生的事情做出反应——并与之区分开来。从广义的历史意义和发展来看，这是正确的。

你可以将开发工具的历史改写为集中化和分散化的循环——不断平衡标准化和自主性、可扩展性和速度的斗争。就在我们似乎已经找到解决方案的时候，钟摆又摆向了另一个方向。

平台团队的兴起已被充分记录，并且[内部开发者平台的管理](https://thenewstack.io/platform-engineering/)越来越成为一项核心功能。但随着这些系统的复杂性不断增加，构建和维护它们的成本抵消了提供它们的好处，是否有人觉得钟摆即将落下？

## 内部开发者平台的兴起

在容器出现之前，有 [VMware](https://tanzu.vmware.com/tanzu?utm_content=inline+mention)，我们痴迷于为开发者构建自助式 [平台](https://thenewstack.io/adopting-gitops-for-self-service-developer-platforms-practical-strategies/)，以便他们能够以最小的方式与基础设施进行交互。我们可以直接请求我们需要的虚拟机，并立即开始开发。

当基础设施即代码出现时，我们分解了这些虚拟机并转向微服务。我们决定不使用这个单一的平台，而是使用一个分散的平台来分离关注点，这将使我们能够更好地扩展。每个团队都可以在自己的城邦内工作。当事情无法正常工作时， [DevOps 文化](https://thenewstack.io/best-practices-for-adopting-a-devops-culture-2/) 帮助团队相互沟通。

但这也开始变得难以控制。容器变得越来越小，复杂性也越来越大。现在，由于人性，我们正在做我们一直做的事情：一些截然不同的事情。每次我们达到某个复杂性的临界点时，我们都会再次改变策略。分散化并没有像我们希望的那样奏效；我们需要一个更集中的模式。

内部开发者平台标志着对这种集中化开发视图的回归。我们正在构建自助式平台，希望开发者不必与运维人员交谈。

但我们遇到了同样的陷阱——只是把豌豆从盘子的这一边挪到另一边。复杂性从未真正消失。

## 内部开发者平台的风险

原则上，内部开发者平台应该通过将所有随容器而来的操作工具集中到一个地方来减轻开发者的认知负担。但这种集中化真的有效吗？为你的开发者提供一个中央平台会带来巨大的风险。

### 过度工程

分析师说，“去[构建一个平台](https://www.gartner.com/en/newsroom/press-releases/2023-11-28-gartner-hype-cycle-shows-ai-practices-and-platform-engineering-will-reach-mainstream-adoption-in-software-engineering-in-two-to-five-years)。”但像这样的建议的问题在于，它们是针对像 Netflix 这样的公司提出的。大多数公司根本没有 Netflix 这样的规模，他们永远不会遇到像 Netflix 这样的问题，但他们无论如何都被要求解决这些问题。

### 资源黑洞

一个全新的平台团队可能花费两年时间和数百万美元为开发者构建一个新的内部产品： [内部开发者平台](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/)。但没有保证，一旦构建完成，这个新产品就能为人们工作。

在你花费所有这些金钱、时间、汗水和泪水之前，你怎么知道这个平台是否会产生价值？

### 工具孤岛

企业解决方案是复杂的命题。针对 [软件开发生命周期](https://thenewstack.io/security-testing-must-be-part-of-software-development-life-cycle/) 的每个阶段的工具越来越专业化，这使得特定的组织角色更容易，但对于使用自己专业工具的其他角色的协作几乎没有帮助。每个团队最终都会陷入工具孤岛。

DevOps 背后的最初想法是通过调整组织结构和改善沟通来解决这种孤岛问题。内部开发者平台被设想为一种万无一失的方式，让开发者[无摩擦地交付应用程序](https://thenewstack.io/imagine-a-smarter-ci-pipeline/)，标志着远离这种沟通和协作。在 2024 年版本的“将其抛过墙”中，墙位于平台团队和开发人员之间，没有人确切知道另一边发生了什么。

我们需要促进一般沟通的工具，而不仅仅是围绕工具的沟通。让我们承认，利益相关者利用不同的必需技能，生活在不同的世界中。与其在这些利益相关者之间寻找最小公分母，不如通过赋予他们专注于自己擅长的能力来最大化他们的能力。

### 接下来的步骤是什么？

如果我们不是在集中化和分散化、工具孤岛和统治所有工具的工具之间来回切换，而是促进工具之间的对话，会怎样？如果我们为构成复杂解决方案的每个主题专家提供一个描述、部署和测试其工作范围的通用框架，会怎样？

这样的解决方案将是 IDP 全有或全无方法的轻量级替代方案，而不会完全分散化。

在 [Garden](https://garden.io/)，我们致力于帮助团队 [以更模块化的方式工作](https://thenewstack.io/garden-automates-kubernetes-building-deploying-testing/)，使他们能够获取他人的工作，以便根据全局测试自己的工作。我们相信，接下来将出现处理复杂性而不是将其抽象化或将其踢给其他团队的工具。
