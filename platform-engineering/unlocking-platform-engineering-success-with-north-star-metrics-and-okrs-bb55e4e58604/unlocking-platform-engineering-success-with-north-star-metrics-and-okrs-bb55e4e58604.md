
<!--
title: 利用北极星指标和OKR实现平台工程的成功
cover: ./cover.png
-->

背景

> 译自 [Unlocking Platform Engineering Success with North Star Metrics and OKRs](https://medium.com/@rnampelly/unlocking-platform-engineering-success-with-north-star-metrics-and-okrs-bb55e4e58604)，作者 Ramesh Nampelly。

## 背景

平台工程是现代软件开发中不可或缺的一部分。它涵盖了一系列技能和实践，包括云和基础设施工程、DevSecOps和SRE——所有这些对于确保复杂软件系统的成功开发和运营都至关重要。

为了推动成功并确保平台工程的最佳性能，建立北极星指标和OKR至关重要。这些指标提供了清晰的成功衡量标准，并帮助团队专注于目标。

## NSM和OKR

正如我几个月前[发布](https://www.linkedin.com/feed/update/urn:li:activity:7020153031744790528/)的那样，您是否想过如何衡量平台工程团队工作的影响，尤其是在充满挑战的经济时期？这篇博文深入探讨了北极星指标 (NSM) 和目标与关键成果 (OKR) 如何成为您的秘密武器。

作为平台和基础设施负责人，我亲眼目睹了这些工具如何改变团队跟踪进度和展示其价值的方式。让我们探讨一下我们在Palo Alto Networks和Cohesity如何实施NSM，以及您如何将这些策略应用于您自己的组织。

**了解NSM和OKR如何**：

* **阐明团队的影响**：清晰地展示平台工程工作的业务价值。
* **优化流程**：找出改进领域并简化工作流程。
* **应对经济不确定性**：通过将团队目标与更广泛的业务目标保持一致来应对挑战。

## 区别

首先，让我们了解NSM和OKR之间的[区别](https://www.slingshotapp.io/blog/north-star-metric)。简单来说，区别如下所示。

OKR将个人的目标与团队的目标以及团队的目标与群体或公司的目标对齐，NSM提供了必要的可见性和问责制，从而为下一步和数据驱动的决策带来知识。

现在让我们深入探讨Palo Alto Networks[平台工程的NSM](https://www.linkedin.com/post/edit/7025957335961391104/#)。

北极星指标应包含两部分：

* 产品愿景陈述，以及
* 用作当前产品战略关键衡量指标的指标。

## Palo Alto Networks的平台工程NSM

根据上述标准，以下是我们工程平台的愿景和相关的NSM。

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*nfHzay4ajCiOQXJE)

在为我们的团队制定合适的北极星指标的过程中，我们采用了“不超过3个NSM”的不成文规定。现在我们的团队愿景和其中一个NSM已经确定，我们进行了多次讨论以缩小范围，确定“其他北极星指标”可以用来衡量平台工程计划的绩效和影响。最终，我们确定了以下3个NS指标：

1. 平台采用率和使用频率
2. 生产力指数
3. 开发者NPS

一旦确定了这些NSM，就开始倒推来确定每个计划或项目的[KPI](/wise-engineering/platform-engineering-kpis-6a3215f0ee14)（关键绩效指标）。

## NSM对齐的KPI示例

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*rG5CtzOZQEXO3k3B)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*aahz6D_Xa-2MQdPM)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*Xl49fApOunwzr1ia)

### 每个计划的KPI

上图重点介绍了我们如何倒推来确定每个计划的KPI以跟踪北极星指标，但也可以按平台计划跟踪NSM和KPI。

让我们以一个具体的项目/计划为例，深入探讨KPI，即我们的内部可观测性平台及其相关的关键绩效指标：

**1. 使用该平台的团队/工程师数量**

1. 发送可观测性数据的租户数量（即唯一产品）
2. 每天的唯一用户登录次数
3. 每月每个SDK的下载次数

**2. 平台稳定性的SLO**

1. 关键组件的可用性
2. 关键组件的性能

**3. 与平台相关的成本**
    
1. 基于单位经济学的按团队收费
2. 与供应商产品以及其他产品团队的成本比较分析

**4.每季度开发者NPS调查**

1. NPS分数

**5. 生产力指数**

1. 新租户（平台）的平均入职时间
2. 每个租户的平均生产问题解决时间 (MTTR)


### 可观测性平台的元监控

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*eY5GwjVdmlSv2Mp1SHPHqA.png)

*可观测性平台元监控*

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*n7MCe9M65a1AGsBR)

### 使用情况分析

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*tWR10A_wQZad4Ie9)

*图1：内部开发者门户使用跟踪*

![](https://miro.medium.com/v2/resize:fit:1252/format:webp/1*mKlh8IhY980zR3mqeLyaQA.png)

*pic2：内部开发者平台使用追踪*

## 结论和后续步骤

虽然NSM在创建平台工程价值链所需的可见性和理解方面发挥着关键作用，但作为平台团队，我们应该继续关注在平台工程和产品团队中推动这种可见性，以确保KPI数据具有可操作性。此外，请注意，KPI不是静态的，而是动态的，因此应定期审查和更新。

下一步，我们计划在适用情况下自动化端到端反馈机制。例如，我们不仅在周报中发送可观测性成本，还会提供优化这些成本的建议。在我的下一篇博客中，我将详细介绍平台工程OKR。如有任何问题或反馈，请随时联系。