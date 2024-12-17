# 使用托管式 MLflow 解决常见的机器学习挑战

![使用托管式 MLflow 解决常见的机器学习挑战的专题图片](https://cdn.thenewstack.io/media/2024/12/6e06f88f-amazon-sagemaker-mlflow-1024x576.jpg)

管理生成式 AI (GenAI) 项目涉及跟踪训练数据、模型参数和训练运行以提高模型性能。如果没有可靠的系统，比较实验、确定最佳配置和管理部署可能会变得非常复杂。这些挑战减缓了从[监督学习和无监督学习](https://thenewstack.io/the-battle-between-unsupervised-and-supervised-ai/)到用于[大型语言模型 (LLM)](https://thenewstack.io/llm/) 的高级神经网络等整个机器学习 (ML) 的进展，给整个 GenAI 和 ML 工作流程带来了效率低下的问题。

[MLflow](https://mlflow.org/) 是一个 Apache 2.0 许可的开源平台，它通过提供用于跟踪实验、记录参数、记录指标和管理模型版本的工具和 API 来解决这些问题。它的界面支持 ML 生命周期的各个阶段，从实验到部署。将 [MLflow 部署在 Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) 上作为一项完全托管的服务，可以帮助 ML 团队自动化模型生命周期管理。它有助于解决常见的机器学习挑战，包括高效地跟踪、管理和部署 ML 模型，增强跨不同 ML 任务的工作流程。

## 为什么使用托管式 MLflow？

SageMaker 可扩展基础架构上的完全托管式 MLflow 为处理机器学习实验、模型跟踪和模型注册提供了一个弹性设置。以下是此功能的价值所在：

* **简化的基础架构**: 减少了手动管理基础架构的需求，从而腾出更多时间进行更关键的实验和模型改进。
* **简化的模型跟踪**: 简化了跨实验记录重要信息的流程，提高了一致性。
* **经济高效的资源分配**: 释放资源，使团队能够将更多的时间和精力投入到改进机器学习模型质量上，而不是管理运营。

正如 AWS 产品和项目管理高级经理 [Amit Modi](https://www.linkedin.com/in/ammodi/) 在接受 The New Stack 采访时解释的那样，“SageMaker 为数据科学家提供了一个可扩展的环境，消除了部分基础架构负担，让他们能够专注于实验。”


## 使用托管式 MLflow 进行实验跟踪和记录

Amazon SageMaker 上托管式 MLflow 的一个优势是启动和跟踪实验所需的设置极少。它简化了机器学习模型关键方面的记录，包括指标、参数和工件，这对于改进这些模型至关重要。

### 启动和跟踪机器学习实验

通过简化数据捕获，SageMaker 帮助团队专注于改进模型，而不是花费时间设置和维护跟踪框架和 ML 实验。数据科学家可以快速设置并开始跟踪每次运行的实验，例如：

* **指标**: 性能指标，例如准确率、精确率、召回率以及与实验相关的任何自定义指标。
* **参数**: 每次模型迭代的输入参数，例如学习率、批量大小和正则化强度。
* **工件**: 实验的输出，包括模型权重、混淆矩阵和特征重要性图，可以存储在 MLflow 平台中并进行管理。

阅读这篇[简短指南](https://aws.amazon.com/blogs/aws/manage-ml-and-generative-ai-experiments-using-amazon-sagemaker-with-mlflow/) 了解其工作原理。


### 运行和记录多次迭代

微调机器学习模型通常需要运行多次迭代来测试不同的参数组合。

SageMaker 上的托管式 MLflow 可以记录对参数的每次调整，例如学习率、批量大小或优化方法，以及每次更改对模型性能的影响。例如，如果您运行一个调整学习率的实验，然后运行另一个更改批量大小的实验，MLflow 会记录每个实验对关键指标的影响。

此日志记录功能对于高级机器学习模型（例如[生成式 AI](https://thenewstack.io/genai-wont-replace-open-source-says-aws-exec)）特别有用，在这些模型中，微调参数对于有效提高模型质量至关重要。

### 在 UI 中比较实验运行

完成多次运行后，您可以使用 MLflow 用户界面 (UI) 分析和比较结果。此界面整合了您的实验数据，在一个位置显示了多次运行的指标、参数和工件。以下是最大限度地发挥其价值的方法：
**并排查看比较**: 选择多个实验运行以并排查看它们，可以直接比较不同模型版本中的指标和参数。例如，您可以根据准确性比较运行，识别哪些参数配置产生了最高的性能。**按条件过滤运行**: 使用过滤器优化显示的运行列表，您可以只关注符合您目标的最佳性能实验。这使您可以专注于具有特定指标的实验，例如准确率高于 90% 的模型。**查看和可视化工件**: UI 提供对任何已保存工件的访问，例如混淆矩阵或特征重要性图。这些可视化提供了额外的洞察力，以评估每个模型的优势和潜在弱点，以帮助您选择性能最佳的模型。

MLflow UI 不仅记录数据，还有助于发现实验过程中的问题。Modi 解释说：“能够无缝地跟踪实验使数据科学家能够快速检测到即使是细微的性能问题。这使团队能够有效地进行故障排除，而不会丢失他们的实验进度。”

## 管理和注册机器学习模型

将模型从实验过渡到生产是机器学习工作流程的一个重要方面。在 AWS SageMaker 上使用像托管 MLflow 这样的统一系统可以简化此过程，以便在整个机器学习模型生命周期中提供受控的过渡。

### 为什么模型注册在实验中很重要

MLflow 模型注册中心是一项核心功能，它提供了模型版本的高级概述，充当管理和跟踪模型在实验、暂存和生产等生命周期阶段的主要中心。将 SageMaker 模型注册中心与 MLflow 模型注册中心集成结合了两个平台的优势。Modi 解释说：“这种集成最大限度地减少了部署和更新模型所需的手动工作，负责整个生命周期，因此团队可以专注于实现准确性而不会中断。”

这种集成的好处包括：

* **集中式模型跟踪**: 所有模型版本都记录在一个统一的注册中心内，因此实验的每个阶段都保留了文档。
* **增强的模型治理**: 在托管 MLflow 中注册的模型会自动出现在 SageMaker 模型注册中心中，以实现统一的模型治理。

当模型准备好投入生产时，SageMaker 允许无缝部署，SageMaker 模型注册中心会跟踪元数据、参数和性能指标，以帮助确保模型得到彻底的记录和监控。

### 简化部署和生命周期管理

一旦模型经过全面测试，您就可以通过 SageMaker 的部署选项将其转移到生产环境，这些选项提供实时推理和批量预测。SageMaker 模型注册中心和托管 MLflow 之间的集成还可以使用 SageMaker Pipelines 来促进自动化生命周期管理，在新数据到达或需要重新训练时更新模型。

例如，如果您正在处理欺诈检测模型，任何更新的模型都可以自动部署到 SageMaker，并且可以使用 SageMaker Pipelines 根据传入数据设置重新训练。

### 实时管理和自动化

模型的相关性通常取决于实时管理和对及时更新的访问，尤其是在数据频繁变化的快节奏领域。SageMaker Pipelines 可用于构建自动重新训练工作流程，方法是提供实时跟踪、使用 SageMaker 模型注册中心进行自动更新以及使用 Amazon SageMaker 和 MLflow 在您的机器学习管道中进行高效的模型管理。

### 使用版本控制提高模型质量

SageMaker 的模型注册中心为每个重新训练周期维护严格的版本控制。每个版本都记录了指标、参数和工件以及模型沿袭，使您可以比较历史和当前模型的性能。可以标记和停用次优模型，以便只有性能最佳的模型才能投入生产。这种方法最大限度地降低了部署无效模型相关的风险，创建了一个针对质量和效率进行优化的系统。

## 保持模型最新

随着新数据的传入和模式的变化，模型的预测能力可能会下降。实时模型管理通过在新数据可用时自动重新训练来帮助保持模型的准确性。

例如，在推荐引擎或欺诈检测等应用中，模型必须保持最新才能良好运行。通过使用 MLflow 设置 SageMaker，团队可以将模型配置为在数据发展时自动重新训练并在生产中更新。这种放手方法可以保持模型优化并减少数据科学团队的工作量，让他们专注于模型改进和实验，而不是手动更新。

### 自动化机器学习生命周期
MLflow on SageMaker integrates with Amazon [EventBridge](https://aws.amazon.com/eventbridge/), a serverless event bus, to connect applications and automate steps in the machine learning lifecycle. EventBridge allows you to create event-driven workflows, triggering retraining, logging, and deployment as soon as a model needs updating.

Automating each stage of the machine learning workflow creates a managed, scalable process, enforcing consistency across every model version. SageMaker captures metadata, tracks changes, and flags any performance regressions, giving you a comprehensive view of the model's lifecycle and enabling proactive management.

### Automating Model Retraining for Continuous Improvement

One of the standout features of the SageMaker Pipeline and managed MLflow integration is the ability to automate model retraining, which is especially crucial in dynamic environments where data evolves rapidly. Consider an e-commerce platform where customer behavior and preferences shift over time, rendering static models obsolete. Similarly, [generative AI applications](https://thenewstack.io/10-key-products-for-building-llm-based-apps-on-aws/) in language processing or image synthesis require continuous updates to handle new data effectively.

### How Automated Retraining Works in SageMaker

With SageMaker, you can configure continuous monitoring to trigger retraining when performance metrics fall below a defined threshold. For example, if a model's accuracy dips below 90%, SageMaker can automatically:

- Pull the latest dataset from a designated source, such as Amazon S3.
- Trigger a retraining job using the updated data and a predefined training pipeline.
- Register the model in managed MLflow on SageMaker, which automatically syncs the model with the SageMaker Model Registry.
- Redeploy the updated model with minimal downtime.

By integrating this process with managed MLflow, you gain a complete log of each retraining cycle. Storing historical metrics and parameters for comparison allows you to track performance improvements over time. This closed-loop feedback strengthens model governance, ensuring that models meet organizational standards with each iteration.

### Enhanced Lifecycle Automation and Real-Time Updates

EventBridge enhances the management of model updates triggered by real-world changes. For example:

- The arrival of a new dataset triggers an ingestion pipeline.
- Upon completion of data processing, EventBridge initiates a retraining job in SageMaker.
- After retraining, the updated model is automatically registered in the MLflow Model Registry.
- EventBridge then triggers the deployment workflow, ensuring the updated model is deployed to production with minimal latency.

This automation keeps machine learning models in sync with real-time data and reduces the need for manual intervention, making workflows scalable and adaptable.

For use cases like fraud detection or recommendation systems, real-time updates are critical. EventBridge allows you to set triggers based on incoming data streams so that models are continuously trained on the most current information. This proactive approach improves the speed and accuracy of decisions, keeping models aligned with evolving patterns.

As machine learning applications expand, SageMaker's ability to handle complex workflows using tools like EventBridge will remain crucial. The combined power of automation and real-time updates can help businesses stay competitive in a data-driven world.


## Streamlining Data Science and DevOps Team Collaboration

Managed MLflow on SageMaker streamlines collaboration between data science and DevOps teams. This capability reduces bottlenecks and simplifies the workflow from experimentation to production. Some key benefits include:

### Unified Workflow

Managed MLflow unifies processes between [data scientists](https://roadmap.sh/ai-data-scientist) and [DevOps](https://roadmap.sh/devops) teams. Data scientists leverage MLflow for tracking metrics, parameters, and artifacts, while DevOps teams manage reproducibility and production-related tasks. This gives both teams the same view, allowing them to quickly self-identify and resolve issues without creating delays or slowing down the transition from experimentation to production.

### Role-Based Access Control

Managed MLflow on SageMaker uses AWS Identity and Access Management to support secure collaboration. Data scientists can access training data, logs, and artifacts needed for development, while DevOps teams manage deployment and monitoring using SageMaker inference endpoints. Clearly defined access roles enhance security and accountability, enabling each team to perform its tasks effectively.

### Transparency and Accountability
MLflow 的日志系统提供了实验和模型版本的详细审计跟踪。DevOps 团队可以追踪开发历史来解决部署挑战，实验日志还能实现清晰的沟通和无缝交接，防止团队之间的失误。

### 简化的交接

SageMaker 通过自动将 MLflow 中注册的模型与其模型注册表同步，简化了将模型投入生产的过程。它最大限度地减少了错误，加快了部署速度，并支持深度学习和大型语言模型等复杂的工作流程。通过管理基础设施，SageMaker 使团队能够专注于创新，并减少对多种工具的需求。

这种集成对于涉及深度学习模型或大型语言模型的复杂工作流程尤其有利。借助 SageMaker 管理基础设施，团队可以避免同时使用多种工具，这有助于减少错误并加快产品上市时间。

## 总结

随着机器学习的发展，生成式 AI 的兴起带来了独特的挑战，包括管理大规模模型、确保微调的可重复性以及保持实验和部署的效率。Amazon SageMaker 与 MLflow 提供了应对这些挑战的工具，提供安全的协作、自动化的生命周期管理和可扩展的基础设施。

通过满足生成式 AI 时代复杂系统的需求，托管 MLflow 使团队能够应对当前的挑战，例如快速迭代周期、资源优化和负责任的 AI 实践。

[Tech moves fast, don't miss an episode. Subscribe to our YouTube channel to stream all our podcasts, interviews, demos, and more.](https://youtube.com/thenewstack?sub_confirmation=1)