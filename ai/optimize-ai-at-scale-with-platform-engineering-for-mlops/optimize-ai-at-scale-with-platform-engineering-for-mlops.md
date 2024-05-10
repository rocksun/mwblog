
<!--
title: 利用平台工程实现 MLOps，大规模优化 AI
cover: https://cdn.thenewstack.io/media/2024/04/050ff395-lady-1721678_1280.jpg
-->

采用 MLOps 平台工程方法的企业将为其运营效率提供急需的即时提升。

> 译自 [Optimize AI at Scale With Platform Engineering for MLOps](https://thenewstack.io/optimize-ai-at-scale-with-platform-engineering-for-mlops/)，作者 Kevin Cochrane。


## 利用平台工程优化大规模人工智能，实现 MLOps

![优化大规模人工智能，实现 MLOps 的平台工程特色图片](https://cdn.thenewstack.io/media/2024/04/050ff395-lady-1721678_1280-1024x537.jpg)

最近两项关于人工智能的调查表明，人工智能的价值主张已达到临界质量。根据 [普华永道的 2023 年新兴技术调查](https://www.pwc.com/us/en/tech-effect/emerging-tech/emtech-survey.html)，73% 的美国受访者表示，他们的公司已在某些业务领域采用了人工智能。在 [最近的福布斯顾问调查](https://www.forbes.com/advisor/business/software/ai-in-business/) 中，64% 的受访者表示人工智能将改善客户关系并提高生产力，60% 的受访者预计人工智能将推动销售增长。

然而，随着企业围绕预测和生成人工智能重组业务运营以获得竞争优势，他们需要最大化其 [机器学习运营](https://thenewstack.io/mlops-needs-a-better-way-to-manage-gpus/) ( [MLOps](https://thenewstack.io/for-ai-to-succeed-mlops-needs-a-bridge-to-devops/)) 的效率，以实现积极的投资回报。这在当今时代并非易事，因为大规模人工智能意味着企业可以随时拥有数十个或数百个 [机器学习模型](https://thenewstack.io/tutorial-train-machine-learning-models-with-automated-ml-feature-of-azure-ml/) (MLM) 处于开发、训练或生产阶段。

如果没有正确的自动化和自助服务功能，支持大规模分布式 MLOps 的工作流可能会阻碍机器学习 (ML) 工程师执行永无止境的架构和组件管理任务。这会妨碍他们从事模型或其 MLM 支持的人工智能应用程序的高价值工作。

### 采用平台工程方法

正如平台工程从 DevOps 运动中脱颖而出以简化应用程序开发工作流一样，平台工程也必须简化 MLOps 的工作流。要实现这一目标，首先必须认识到 DevOps 和 MLOps 之间的根本差异。只有这样，才能为 ML 工程师制定有效的平台工程解决方案。为了实现大规模人工智能，企业必须致力于开发、部署和维护专为 MLOps 构建的平台工程解决方案。

### 利用可定制蓝图跨分布式企业扩展人工智能

无论是由于数据治理要求还是出于对跨越巨大地理距离移动大量数据的实际担忧，大规模 MLOps 要求企业采用辐条轮毂方法。模型开发和训练集中进行，训练后的模型分发到边缘位置，以便根据本地数据进行微调，并且微调后的模型部署在最终用户与其交互的位置以及他们利用的人工智能应用程序附近。

以下是许多企业如何实现大规模人工智能：

- 在企业内建立卓越中心，可以在其中集中开发和训练 MLM。
- 利用公共存储库中的开源模型，以便您的组织在开发每个新模型时不必从头开始。
- 专注于开发更小、更专业的模型来解决特定的业务用例。
- [根据专有公司数据训练模型](https://thenewstack.io/dealing-with-distributed-data-when-training-ai-models/)，并将训练后的模型移至中心化的私有注册表，使其在整个企业中都可以访问。
- 利用强大、基于云的混合和/或多云边缘架构，该架构允许紧密集成 CPU 和 GPU 操作，以便在您的组织开展业务的地理区域内提供人工智能推理。
- 根据本地数据微调边缘模型，以考虑区域和文化因素，同时维护数据治理和隐私要求。

### 利用专为 MLOps 构建的平台工程解决方案优化 MLOps

专为大规模 MLOps 设计的平台工程解决方案必须满足以下所有要求：
**基础设施优化：**简化数据科学家和 ML 工程师部署针对 ML 工作负载进行优化的基础设施组件的方式。

**模型管理和部署：**建立一个基于 Kubernetes 的高效私有注册表，用于训练模型，使其在整个企业中可用且可访问。

**数据治理和隐私：**提供基于边缘的数据存储和安全措施，以便在使用专有公司数据训练模型和根据区域数据在边缘微调模型时维护数据治理和隐私。

**每个阶段的模型可观察性：**将 [监控和可观察性工具集成到平台](https://thenewstack.io/next-gen-observability-monitoring-and-analytics-in-platform-engineering/) 工程解决方案中，以便 ML 工程师可以在 MLOps 的每个阶段构建可观察性，以确保负责任的 AI 实践。

**自动化任务和自助服务：**通过 CI/CD 管道 [自动化代码构建](https://thenewstack.io/netlify-launches-plugin-infrastructure-to-extend-automated-build-capabilities/)、测试和部署，以及使用基础设施即代码 (IaC) 工具进行基础设施配置和管理。

## 为您的公司 MLOps 未来做好准备，让您的平台工程解决方案面向未来

围绕 AI 生态系统的创新经济每天都会引入新的组件，以改进 AI 堆栈。如果开发得当，您的 ML 平台工程解决方案可以在新技术可用时利用它们强大的功能。为了实现这一点，您的 ML 平台工程解决方案必须作为产品而不是项目进行管理。

这需要将与平台互动的 [数据科学家和 ML 工程师视为客户](https://thenewstack.io/platform-engineers-developers-are-your-customers/)，并指定一个专门的产品支持团队来管理解决方案的功能积压。平台工程产品团队必须在需求变化和技术发展时不断改进解决方案。

企业应聘用具有 [MLOps 经验的工程师来适当填补平台工程职位](https://thenewstack.io/making-the-leap-ops-roles-evolve-into-platform-engineers/)。根据 [世界经济论坛](https://www.weforum.org/publications/the-future-of-jobs-report-2020/in-full/executive-summary/) 的研究，预计到 2025 年，AI 将创造约 9700 万个新工作岗位。越来越多的此类机会将是 ML 平台工程职位。

采用 MLOps 平台 [工程方法](https://thenewstack.io/port-platform-engineering-can-be-the-first-step-in-system-automation/) 的企业将为其运营效率提供急需的直接提升，并通过确保其 ML 工程师始终能够专注于他们受雇执行的高价值数据科学工作，为其 AI 计划做好未来准备。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。