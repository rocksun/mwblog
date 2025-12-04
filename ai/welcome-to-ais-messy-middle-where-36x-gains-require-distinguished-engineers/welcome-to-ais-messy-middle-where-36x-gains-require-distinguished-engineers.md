
<!--
title: 鏖战AI中场：36倍增长，精英工程师方能破局！
cover: https://cdn.thenewstack.io/media/2025/12/14cc344c-img_5498-1-e1764789837539.png
summary: AWS re:Invent展示Kiro，显著提升开发效率。AI技术发展迅速，但缺乏标准化实践。AWS正将Kiro标准化，代理技术仍处于“混乱中层”，需进一步发展。
-->

AWS re:Invent展示Kiro，显著提升开发效率。AI技术发展迅速，但缺乏标准化实践。AWS正将Kiro标准化，代理技术仍处于“混乱中层”，需进一步发展。

> 译自：[Welcome to AI's Messy Middle: Where 36x Gains Require Distinguished Engineers](https://thenewstack.io/welcome-to-ais-messy-middle-where-36x-gains-require-distinguished-engineers/)
> 
> 作者：Alex Williams

拉斯维加斯 — 在 AWS re:Invent 大会上，[亚马逊网络服务](https://aws.amazon.com/?utm_content=inline+mention)首席执行官 Matt Garman 在主题演讲中讲述了一个关于其新型代理式 IDE [Kiro](https://thenewstack.io/aws-kiro-brings-automated-reasoning-to-agentic-development/) 的故事。

他公司的一位杰出工程师 Anthony 领导一个团队，在 76 天内与六名开发人员一起重新设计了一个项目。他们最初预计这个项目需要 30 人花费 18 个月。这真是令人大开眼界，足以让一位工程主管冲向代理售货机。

Garman 今年秋天与客户分享了这个故事，客户们询问 Anthony 的团队是如何做到的。这类问题在很长一段时间内都会被问及，这本身就揭示了人们对基础设施、模型以及如何使用这些代理知之甚少，而这些代理正是 AWS 过去需要一位杰出工程师和团队才能完成工作的关键。

欢迎来到混乱的中层。

我们正处于人工智能工作负载开发、部署和管理的中世纪。用一位资深工程师的话说，这是混乱的中层，或者说有趣的时期。这取决于你如何看待它。

云计算用了 10 年或更长时间才成熟。人工智能的成熟可能只需一半时间甚至更短。在 re:Invent 大会的产品发布中，Garman 展示了发展的速度有多快。

但引人注目的是，这些创新缺乏既定的实践。它更多地是关于如何取得这些令人着迷的结果，而不是关于[标准化最佳实践](https://thenewstack.io/the-production-generative-ai-stack-architecture-and-components/)，这样你就不必从零开始构建，使用 GPU、数量惊人的模型和对所有人来说都是全新的代理工作流。

Garman 强调了 AWS 的巨大规模。是的，它每年产生 1320 亿美元的收入，并部署了 100 万个 Trainium 芯片，但这伴随着权衡。

科技公司正在发明非常酷的新架构。但与此同时，用户却很少了解这些新硬件如何融入其企业运营。快速开发令人兴奋，但追求最佳架构需要时间并需要大量的适应，这对大多数客户来说都是非常新的。

## 基础设施的快速发展

Garman 宣布 Trainium 现已普遍可用，并预览了 Trainium 4。AWS 还推出了 P6 GB200 和 GB300 实例。

将这些发布与 [优步](https://thenewstack.io/inside-ubers-multicloud-ai-reality-the-gap-between-data-and-compute/)等公司面临的问题联系起来，你会感觉到从云原生转向人工智能原生所面临的挑战只会越来越严峻。

在上个月的 [KubeCon + CloudNativeCon 北美大会](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/)上，优步大量谈论了如何使用多云以及如何在多云环境中优化人工智能工作负载。客户需要这些选择，但现实已经赶上了优步，对于越来越多的客户来说也会如此。

那么，训练这些模型需要什么呢？拥有资金和工程人才的人将会蓬勃发展。这是一个颠覆的时代，但对于[富人和穷人](https://thenewstack.io/how-cios-can-battle-gpu-poverty-in-the-age-of-ai/)来说，两极分化会达到何种程度？

举个例子：Garman 谈到了一个专门用于训练 [Rainier项目](https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster) 的整个 AWS 园区，该项目服务于 Anthropic 的 [大型语言模型 (LLM)](https://thenewstack.io/introduction-to-llms/) [Claude](https://thenewstack.io/anthropics-new-claude-opus-4-5-reclaims-the-coding-crown-from-gemini-3/)。这是一个项目就占据一个园区，这种场景超出了大多数公司所能承受的范围，甚至超出它们所具备的人才能力。

Garman 表示，AWS 将在企业内部提供人工智能工厂。这是为什么呢？[数据回迁趋势](https://thenewstack.io/why-companies-are-ditching-the-cloud-the-rise-of-cloud-repatriation/) 表明客户希望将数据存储在自己的基础设施上。

这是一个重大的转变。云仍然是王者，但还需要考虑另一个制约因素：电力是瓶颈。AWS 将建立它与 AWS 区域相媲美的设施。这些是垂直整合的能力，内置了 [Bedrock 和其他 AWS 服务](https://thenewstack.io/aws-makes-it-easier-to-customize-ai-models-in-bedrock-and-sagemaker-without-a-phd/)。但关键在于：客户负责提供电力以及运行 AI 工作负载所需的所有数据中心要求。

## 模型，无处不在

AWS 宣布了[四款新 Nova 模型](https://thenewstack.io/aws-updates-its-nova-models-to-compete-with-google-anthropic-and-openai/)：

*   **Amazon Nova Micro** 仅支持文本，有助于解决延迟问题。
*   **Amazon Nova Lite** 是一款多模态模型。
*   **Amazon Nova Pro** 也是一款多模态模型，在准确性、速度和成本方面进行了增强。
*   **Amazon Nova Premier** 是该公司最复杂的模型。

Garman 还讨论了支持来自 Anthropic、OpenAI、Cohere 等公司的模型。Nova Forge 用于创建 AWS 模型的版本，他们称之为 novellas。目标是：让从头开始构建模型变得更经济实惠。

在每个技术时代，扩散是常态，而非例外。在十多年的云原生分布式工作负载之后，随着 GPU 的普及，融合现在成为一种愿望。我们正处于专业化时代，而非通用工作负载时代。

在 KubeCon 大会上，优步的 [Andrew Leung](https://www.linkedin.com/in/anwleung) 指出了他公司在实现融合方面的挣扎——而它在人工智能工作负载的使用方面是领导者。Garman 则表示：“我们从未相信会有一个模型能统治所有模型。”

但这种扩散确实会影响融合，使得企业能够维护庞大、分布式的业务负载。在 re:Invent 大会上，Gaman 谈到了模型选择的广泛性。但他没有解决工程师面临的巨大挑战：CPU 和 GPU 在实践中虽然相似但不可互换。

最好的例子来自 AWS。Garman 谈到了 AWS 开发的平台 Kiro。

“现在我想花点时间深入探讨我们听到的一个故事，”他告诉 re:Invent 的听众。“细节相当高。这是我们一位杰出工程师 Anthony 的原话。Anthony 正在进行一个重构项目……”

但这个案例研究的细节在哪里？Anthony 是谁？对于像 AWS 这样的公司来说，为什么会花费数周时间？

AWS 处于一个极好的位置。Kiro 团队作为 AWS 的团队，知道使用哪些基础设施和模型。该团队可以适应，因为它控制着产品开发的所有方面。

但这些团队成员仍然花费了数周时间才达到能够制定真正计划的程度。他们需要弄清楚代理能做什么，不能做什么。而这只是一个团队。

这引发了关于 AWS 在构建代理式架构和管理状态方面的表现问题——所有这些都是客户资源有限难以解决的问题。

还有就是我们为什么会听到 Anthony 的故事。他的团队取得了巨大的成功。这本身就说明了很多。

接下来发生了什么？这个团队的巨大成功如何促成了 AWS 的重大新闻。

“事实上，我们被彻底震撼了，上周，亚马逊所有部门都决定将 Kiro 作为我们官方的人工智能开发环境进行标准化，”Garman 说。

## 人工智能代理如何像青少年

AWS 刚刚开始其旅程。其 CEO 对人工智能工作负载的兴奋程度之深令人惊叹。人们纷纷询问如何效仿其领导，这表明这种方法才刚刚开始被采用。

“混乱的中层”这一主题在整个主题演讲中都变得显而易见。Garman 将代理比作抚养青少年。它们需要基本规则；代理需要监督。它们还很年轻——有很多东西需要学习。

re:Invent 大会上的兴奋之情溢于言表。主题演讲讲述了一个宏伟的新世界，基础设施和模型作为代理式人工智能的基础，甚至可能带来一个可以改变如此之多的新世界的奇迹。

但这是新的时代。这确实很酷，但知识的普适性并不高。至少现在还不是。