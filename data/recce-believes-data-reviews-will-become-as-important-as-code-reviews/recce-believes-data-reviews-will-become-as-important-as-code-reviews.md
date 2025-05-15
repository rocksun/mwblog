<!--
title: Recce认为数据审查将变得和代码审查一样重要
cover: https://cdn.thenewstack.io/media/2025/04/2d16070b-rose-galloway-green-mzpnzk3prtu-unsplash-scaled.jpg
summary: 数据审查要火？Recce推出Recce Cloud，保障AI时代数据质量！开源项目Recce 1.0发布，通过lineage diffs可视化dbt数据模型变更影响。自动行数、模式检查，CI/CD流程无忧。集成GitHub，数据验证不过关，代码禁止合并！
-->

数据审查要火？Recce推出Recce Cloud，保障AI时代数据质量！开源项目Recce 1.0发布，通过lineage diffs可视化dbt数据模型变更影响。自动行数、模式检查，CI/CD流程无忧。集成GitHub，数据验证不过关，代码禁止合并！

> 译自：[Recce Believes Data Reviews Will Become as Important as Code Reviews](https://thenewstack.io/recce-believes-data-reviews-will-become-as-important-as-code-reviews/)
> 
> 作者：Frederic Lardinois

数据已成为许多企业的命脉，dbt 等工具已经改变了数据的管理和使用方式，包括 AI 系统。但是 [CL Kao](https://www.linkedin.com/in/clkao/)，[Recce](https://datarecce.io/) 的创始人兼 CEO 认为，虽然许多工具可以更轻松地构建[数据管道](https://thenewstack.io/finding-the-right-data-architecture-for-rag-pipelines/)并以编程方式管理数据，但缺少的是用于评估上游代码更改对下游数据影响的现代工具。Kao 认为，在不久的将来，数据审查将变得与代码审查一样重要，该公司正在研究如何将这些相同的想法应用于大型语言模型 (LLM) 和 AI 代理的输出。

Kao 也是 Git 前身 [SVK](https://www.perl.com/pub/2004/03/03/svk.html/) 的联合创始人，于 2023 年启动了 Recce 开源项目。在 Heavybit 领投的 400 万美元种子前融资（Vertex Ventures US、Hive Ventures 和一些天使投资人参与）的支持下，该公司现在正在启动 Recce Cloud 的私有 Beta 版。与此同时，Recce 开源项目今天达到了 1.0 版本。

![](https://cdn.thenewstack.io/media/2025/04/1c9668c7-data-consistency-with-automated-row-count-and-schema-checks.png)

*通过自动行数和模式检查实现数据一致性。*

“当我们启动这个项目时，我们发现数据系统的 CI/CD 工作流程中存在一个有趣的差距，”Kao 在我问及该项目的起源时说。“在软件（传统软件）中，您对软件的行为方式有非常明确的标准。但是对于数据系统，很多时候，您没有非常容易编写的测试。”

开发人员可以检查某个值是否在预期的边界内——并且一些现有工具已经这样做了——但 Kao 认为，为这些系统编写详尽的测试非常困难。例如，您如何知道从开发环境到生产环境的任何偏差是否是故意的？任何这些更改都可能对下游产生不可预见的影响，并导致错误的指标和代价高昂的错误。

今天发生的情况是，开发人员将更改生产系统，但即使添加了测试，他们也不知道结果是否正确。将 AI 模型添加到此处，以及它们的概率结果，拥有正确的工具来确保这些结果正确变得更加重要。

![](https://cdn.thenewstack.io/media/2025/04/e7559255-lineage-diff-in-recce-app-helps-you-visualize-the-impact-area-of-dbt-data-model-changes.png)

*Recce 应用程序中的 Lineage Diff 可帮助您可视化 dbt 数据模型更改的影响区域。*

“通过初始分析，我们可以非常精确地确定潜在的变化发生在哪里。然后，为了增加风险维度或一件事的重要性，用户可以选择性地添加某些检查，与生产环境相比的检查。它们是否发生了有意义的改变？或者您是否不期望发生改变，而实际上它没有发生？”

由于许多这些管道处理大量数据，Recce 用户通常只对他们创建的数据进行抽样，以检查问题或创建有限的回溯期。

显然，对这样的工具有需求，开源版本现在在 GitHub 上的每周下载量超过 3,500 次。Recce 表示，该工具的用户范围从 Philadelphia Inquirer 到电信公司、健康科技初创公司，甚至包括巴西和澳大利亚的政府机构。

也许不足为奇的是，Recce 也在加紧努力将这项服务货币化。在这里，它遵循标准策略，通过在 Recce Cloud 旗下推出其服务的托管版本。这项新服务包括许多协作功能，例如通过 lineage diffs 在团队之间共享数据验证上下文、自定义查询结果和包含的清单。Recce Cloud 还包括与 GitHub 的集成，以确保只有在所有数据验证检查都已批准后，代码才能合并。

“数据管道是每家使用人工智能构建产品的公司的新秘诀，它使团队能够利用自己的知识产权创建和改进高质量的训练数据，”Heavybit 普通合伙人兼 DevOps 先驱 Jesse Robbins 说，他将加入 Recce 的董事会。“Recce 提供了必要的工具包，通过迭代、改进和监控来释放数据的全部价值，同时降低出错和损坏的风险。Heavybit 很高兴支持他们发展人工智能时代的数据管道验证生态系统，这是我们 10 多年来持续使命的一部分：将关键的企业基础设施推向市场。”