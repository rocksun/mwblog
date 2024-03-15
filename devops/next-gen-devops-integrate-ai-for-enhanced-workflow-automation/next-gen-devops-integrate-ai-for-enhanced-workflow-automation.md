
<!--
title: 新一代DevOps：集成AI以增强工作流自动化
cover: https://cdn.thenewstack.io/media/2024/03/fa5c35e8-growtika-f7ucqxhucw4-unsplash.jpg
-->

人工智能与更广泛的 DevOps 框架的日益融合将对我们处理软件开发的方式带来重大改变。

> 译自 [Next-Gen DevOps: Integrate AI for Enhanced Workflow Automation](https://thenewstack.io/next-gen-devops-integrate-ai-for-enhanced-workflow-automation/)，作者 Alexander T Williams。

想象一个软件开发和运营团队可以毫不费力地协调其工作流、简化流程并 [提高开发人员生产力](https://thenewstack.io/three-key-metrics-to-measure-developer-productivity/) 的世界，这在以前是无法想象的。

这就是新一代 DevOps 的全部意义——一种利用 AI 的力量来革新每个单独冲刺、提高效率并帮助新 DevOps 专业人员更轻松地接受教育的演变。

但在较低层面上；无论是自动化例行任务、优化资源分配还是预测潜在问题，AI 都对 [DevOps 工作流的未来](https://thenewstack.io/what-is-devops/) 在更广泛的背景下产生了不可否认的变革性影响。

下面，我们将探讨 AI 呈现的无限机会，并揭示它如何赋能团队以实现前所未有的效率、敏捷性和弹性。

## 如何将 AI 集成到 DevOps 中？

虽然不可否认 AI [在采用方面存在许多障碍](https://thenewstack.io/ai-everywhere-overcoming-barriers-to-adoption/)，但 DevOps 团队一直是最开放的团队，他们思考并实施新的用例。

### CI/CD 管道

AI 使组织能够解锁前所未有的可见性和对 [CI/CD 流程](https://about.gitlab.com/topics/ci-cd/) 的控制。使用 AI，组织可以快速分析来自先前构建、测试和部署的历史数据，以发现潜在故障点并预测在问题发生之前可能出现的问题。

例如，AI 可以分析 MySQL 查询日志以识别影响应用程序性能的低效数据库查询。

AI 驱动的系统还可以主动实施预防措施，最大程度地降低集成和部署阶段发生代价高昂的延迟、故障或中断的风险。

此外，AI 可以帮助优化 CI/CD 管道中的资源分配。但更有趣的是，DevOps 团队可以 [使用高级机器学习模型](https://www.datacamp.com/blog/top-mlops-tools)（称为 MLOps 模型）来预测工作负载和资源需求。从这个意义上说，AI 驱动的系统可以动态调整计算能力、存储和网络资源的分配。

这确保了构建和部署在不浪费宝贵资源或遇到性能瓶颈的情况下高效完成。

### 预测分析

在 DevOps 中，预测和防止中断的能力可能意味着成功与灾难性故障之间的差异。在这种情况下， [AI 驱动的预测分析](https://thenewstack.io/predictive-analytics-using-a-time-series-database/) 可以使团队领先于潜在中断一步。

预测分析使用高级算法和机器学习模型来分析来自各种来源的大量数据，例如应用程序日志、系统指标和历史事件报告。

然后，它识别模式、相关性，并 [检测此数据中的异常](https://thenewstack.io/training-a-ml-model-to-forecast-kubernetes-node-anomalies/)，以便在系统故障或性能下降之前发出预警。这使团队能够在问题升级为全面中断之前采取主动措施。

此外，AI 可以持续分析来自各种基础设施组件（例如服务器、网络和存储系统）的数据，以在发生之前识别潜在的硬件故障或容量限制。

### AI 驱动的代码审查

手动操作引入了人为错误的可能性，并且非常耗时——因此业界转向自动化也就不足为奇了。利用人工智能的工具可以通过以人类无法复制的速度分析代码存储库来识别潜在问题。

从根本上说，这意味着各种潜在问题——性能瓶颈、不符合最佳实践或内部标准的代码、安全责任和 [代码异味](https://www.geeksforgeeks.org/code-smell-a-general-introduction-and-its-type/)——可以快速且大规模地识别出来。

这只是战斗的一半——谢天谢地，这项技术也擅长进行另一半战斗。我们越来越多地看到可以为开发人员提供可操作的情报和建议的行动方案的工具，以解决已识别的问题。从长远来看，当人们考虑到当今快速的发展速度时，这些工具可以极大地降低在代码库中引入缺陷或累积技术债务的风险。

从更广泛的意义上讲，其中一些工具还通过建议代码库优化措施证明了自己的价值——尤其是以下模型脱颖而出：

- [DeepSeek-Coder](https://github.com/deepseek-ai/DeepSeek-Coder) 6.7B/33B
- [Phind-CodeLlama v2](https://huggingface.co/Phind/Phind-CodeLlama-34B-v2)
- [Deepseek 67b](https://huggingface.co/deepseek-ai/deepseek-llm-67b-base)
- [CodeCapybara](https://github.com/FSoft-AI4Code/CodeCapybara)
- [GPT-4-1106](https://aider.chat/docs/benchmarks-1106.html)

总而言之，该技术极具前景，在质量控制方面的自动化和精简方面已经取得了良好的成果。通过适应使用这些解决方案，DevOps 团队可以加快交付周期，改善[昂贵的部署后问题风险](https://thenewstack.io/unraveling-the-costs-of-bad-code-in-software-development/)，并始终确保全面的质量控制。

### 自动化安全检查

开发和开发周期通常以疯狂的节奏进行，这是生活中的一个不可改变的事实。但由于实施和执行适当的安全措施成为一项挑战，因此这是无意中出现漏洞的沃土。

这是 AI 在精简和提高效率方面具有潜力的另一个领域，它可以解决常见问题。由 AI 提供支持的自动化安全检查还具有另一个优势——与传统的静态安全解决方案不同，AI 能够持续学习和进化，使其能够通过分析恶意行为者使用的模式和技术来[适应新的新兴威胁](https://www.sciencedirect.com/science/article/pii/S2543925123000372)。

此外，AI 驱动的安全检查的自动化功能可以无缝集成到 DevOps 工作流中，从而在所有[软件开发生命周期 (SDLC)](https://thenewstack.io/toward-a-3-stage-software-development-lifecycle/) 阶段实现持续的安全监控和验证。

### 反馈和优化

自动化各种任务和流程是 AI 的组成部分——然而，一个被忽视的功能是它改善运营、最终用户和 DevOps 团队之间存在的反馈回路的能力。

这些工具擅长筛选大量数据。这使得它们非常适合分析大量反馈——例如系统日志、用户行为和[应用程序性能指标](https://www.ibm.com/blog/apm-metrics/)——并最终直接获得客户的反馈。

然后，这些工具[可以使用自然语言处理](https://link.springer.com/article/10.1007/s11042-022-13428-4)和机器学习来识别模式和趋势，指出应用程序性能、可用性和整体用户满意度方面的改进领域。

这种智能分析使开发团队能够根据实际用户需求和系统性能对修改和增强进行优先级排序，从而使产品演进更贴近用户期望和运营现实。

## 将 AI 集成到 DevOps 中的工具和技术

将 AI 集成到 DevOps 中催生了一系列旨在增强自动化和效率的工具。

虽然许多组织可能默认选择 Google Cloud 等流行选择，但越来越多的 DevOps 团队[寻找 Google Cloud 替代方案](https://platform.sh/google-cloud-platform-alternative/)来发现提供独特 AI 功能、更优惠的价格或更适合特定工作流的服务。例如，Oracle 和 Alibaba Cloud 在这方面越来越受欢迎，因为它们的 AI 功能每月都在增长。

### 代码审查和质量保证

例如，考虑使用 DeepCode、Codacy 和 SonarSource 等解决方案来优化[代码分析和审查](https://www.turing.com/blog/ai-code-review-improving-software-quality/)流程。这些解决方案利用机器学习算法来分析代码库并识别潜在漏洞、代码异味和最佳实践违规。

在测试和质量保证中，存在 Applitools、Functionize 和 Mabl 等 AI 驱动的工具。通过视觉 AI 和机器学习技术，这些工具可以自动化测试创建和执行。同样，不要忘记我们上面提到的[本地托管的 LLM](https://github.com/continuedev/what-llm-to-use)——请记住，它们可能需要专门培训才能专门用于 DevOps 任务，尤其是 CI/CD。

对于基础设施管理和监控，Moogsoft 和 Dynatrace 等 AI 增强平台提供了高级异常检测和根本原因分析。它们最大的优势在于实时分析运营数据，以预测和防止潜在的系统故障。

### 面向非技术人员的 DevOps 工具

有一个常见的误解，即 AI 驱动的 DevOps 工具仅适用于大型组织，它们拥有庞大的资源和复杂软件开发需求。然而，事实并非如此。Harness 和 CodeGuru 等解决方案利用了 AI 功能，但仍然足够灵活，可以适应较小的团队。

以下是教育家和[The Blog Starter](https://www.theblogstarter.com)创始人 Scott Chow 的观点：

> “尽管我们是一个小型组织，但我们的 DevOps 团队已经为桌面和移动站点开发采用了几十种不同的工具。老实说，我认为潜力就在这里——不在企业解决方案中，而是在开源、个人 AI 工具和模型中。”
> 
> Chow 的这段见解表明，DevOps 中的 AI 不仅仅是大企业的领域；小型组织也在采用 AI 工具时发现了价值，尤其是那些开源且可根据其特定需求进行定制的工具。事实上，这些小型 IT 团队通常处于持续紧缩的状态，这意味着他们是最需要 AI 协助来完成 DevOps 任务的人员。

## 将 AI 集成到 DevOps 的最佳做实践

随着将 AI 集成到 DevOps 实践的趋势持续升温，组织在进行此项变革时必须审慎规划，才能确保成功、无缝地进行采用。以下是可以帮助组织释放 AI 驱动的 [DevOps 自动化](https://thenewstack.io/how-to-mature-your-devops-automation-practices/)的全部潜力并缓解潜在挑战的一些最佳实践：  

- **定义明确的目标和指标**：首先，确定您希望通过在 DevOps 周期中集成 AI 实现的具体目标。无论是提高部署频率、改进代码质量、降低故障率还是加快[事件响应](https://thenewstack.io/incident-response-three-ts-to-rule-them-all/)时间，明确的目标都能帮助您选择合适的 AI 工具和技术。
- **从小处着手并不断迭代**：不要尝试全面改革 DevOps 流程，而应从确定 AI 能立竿见影发挥价值的特定领域开始。从试点项目或概念验证入手，随着您积累经验并提升信心，再逐步扩大 AI 集成。
- **确保数据质量和治理**：AI 算法严重依赖数据，因此及时建立[稳健的数据治理实践](https://www.forbes.com/sites/forbestechcouncil/2022/10/14/13-best-practices-for-developing-a-robust-data-governance-strategy/?sh=3f6afce7450e)至关重要。通过坚持适当的数据质量、完整性和可访问性，实现数据清洗、验证和管理等流程将变得容易得多。

## 总结 

AI 与更广泛的 DevOps 框架集成得日益紧密，承诺将对我们的做事方式带来重大变化——其中大部分都将在提高效率方面很快体现。 

在 CI/CD 方面，预测分析将帮助 DevOps 团队抢占先机，并有可能转变客户服务渠道并优化资源分配。 

目前，将 AI 集成到 DevOps 中已不再是可能，而是不可避免的必需。问题不在于组织是否应该拥抱这种转变，而在于他们能以多快的速度多有效地利用 AI 的力量获得竞争优势。