
<!--
title: 使用托管 MLflow 解决常见的机器学习挑战
cover: https://cdn.thenewstack.io/media/2024/12/6e06f88f-amazon-sagemaker-mlflow.jpg
-->

在 Amazon SageMaker 上使用开源 MLflow 简化了生成式 AI 和 ML 实验以及生命周期自动化，从而实现可扩展、高效的工作流程。

> 译自 [Address Common Machine Learning Challenges With Managed MLflow](https://thenewstack.io/address-common-machine-learning-challenges-with-managed-mlflow/)，作者 Oyedele Tioluwani。

管理生成式 AI (GenAI) 项目涉及跟踪训练数据、模型参数和训练运行以提高模型性能。如果没有可靠的系统，比较实验、确定最佳配置和管理部署可能会变得非常复杂。这些挑战减缓了从[监督学习和无监督学习](https://thenewstack.io/the-battle-between-unsupervised-and-supervised-ai/)到用于[大型语言模型 (LLM)](https://thenewstack.io/llm/) 的高级神经网络等整个机器学习 (ML) 的进展，给整个 GenAI 和 ML 工作流程带来了效率低下的问题。

[MLflow](https://mlflow.org/) 是一个 Apache 2.0 许可的开源平台，它通过提供用于跟踪实验、记录参数、记录指标和管理模型版本的工具和 API 来解决这些问题。它的界面支持 ML 生命周期的各个阶段，从实验到部署。将 [MLflow 部署在 Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) 上作为一项完全托管的服务，可以帮助 ML 团队自动化模型生命周期管理。它有助于解决常见的机器学习挑战，包括高效地跟踪、管理和部署 ML 模型，增强跨不同 ML 任务的工作流程。

## 为什么使用托管式 MLflow？

SageMaker 可扩展基础架构上的完全托管式 MLflow 为处理机器学习实验、模型跟踪和模型注册提供了一个弹性设置。以下是此功能的价值所在：

* **简化的基础架构**: 减少了手动管理基础架构的需求，从而腾出更多时间进行更关键的实验和模型改进。
* **简化的模型跟踪**: 简化了跨实验记录重要信息的流程，提高了一致性。
* **经济高效的资源分配**: 释放资源，使团队能够将更多的时间和精力投入到改进机器学习模型质量上，而不是管理运营。

正如 AWS 产品和项目管理高级经理 [Amit Modi](https://www.linkedin.com/in/ammodi/) 在接受 The New Stack 采访时解释的那样，“SageMaker 为数据科学家提供了一个可扩展的环境，消除了部分基础架构负担，让他们能够专注于实验。”

![](https://cdn.thenewstack.io/media/2024/12/f50b4e54-mlflow-with-sagemaker.png)


## 使用托管式 MLflow 进行实验跟踪和记录

Amazon SageMaker 上托管式 MLflow 的一个优势是启动和跟踪实验所需的设置极少。它简化了机器学习模型关键方面的记录，包括指标、参数和工件，这对于改进这些模型至关重要。

### 启动和跟踪机器学习实验

通过简化数据捕获，SageMaker 帮助团队专注于改进模型，而不是花费时间设置和维护跟踪框架和 ML 实验。数据科学家可以快速设置并开始跟踪每次运行的实验，例如：

* **指标**: 性能指标，例如准确率、精确率、召回率以及与实验相关的任何自定义指标。
* **参数**: 每次模型迭代的输入参数，例如学习率、批量大小和正则化强度。
* **工件**: 实验的输出，包括模型权重、混淆矩阵和特征重要性图，可以存储在 MLflow 平台中并进行管理。

![](https://cdn.thenewstack.io/media/2024/12/bca5e566-how-sagemaker-works-1024x702.png)

阅读这篇[简短指南](https://aws.amazon.com/blogs/aws/manage-ml-and-generative-ai-experiments-using-amazon-sagemaker-with-mlflow/) 了解其工作原理。


### 运行和记录多次迭代

微调机器学习模型通常需要运行多次迭代来测试不同的参数组合。

![](https://cdn.thenewstack.io/media/2024/12/9d24fc33-mlflow-ui-1024x291.png)

SageMaker 上的托管式 MLflow 可以记录对参数的每次调整，例如学习率、批量大小或优化方法，以及每次更改对模型性能的影响。例如，如果您运行一个调整学习率的实验，然后运行另一个更改批量大小的实验，MLflow 会记录每个实验对关键指标的影响。

此日志记录功能对于高级机器学习模型（例如[生成式 AI](https://thenewstack.io/genai-wont-replace-open-source-says-aws-exec)）特别有用，在这些模型中，微调参数对于有效提高模型质量至关重要。

### 在 UI 中比较实验运行

完成多次运行后，您可以使用 MLflow 用户界面 (UI) 分析和比较结果。此界面整合了您的实验数据，在一个位置显示了多次运行的指标、参数和工件。以下是最大限度地发挥其价值的方法：

1. **并排查看比较**: 选择多个实验运行以并排查看它们，可以直接比较不同模型版本中的指标和参数。例如，您可以根据准确性比较运行，识别哪些参数配置产生了最高的性能。
2. **按条件过滤运行**: 使用过滤器优化显示的运行列表，您可以只关注符合您目标的最佳性能实验。这使您可以专注于具有特定指标的实验，例如准确率高于 90% 的模型。
3. **查看和可视化工件**: UI 提供对任何已保存工件的访问，例如混淆矩阵或特征重要性图。这些可视化提供了额外的洞察力，以评估每个模型的优势和潜在弱点，以帮助您选择性能最佳的模型。

![](https://cdn.thenewstack.io/media/2024/12/e8431347-comparing-models-1024x543.png)

MLflow UI 不仅记录数据，还有助于发现实验过程中的问题。Modi 解释说：“能够无缝地跟踪实验使数据科学家能够快速检测到即使是细微的性能问题。这使团队能够有效地进行故障排除，而不会丢失他们的实验进度。”

## 管理和注册机器学习模型

将模型从实验过渡到生产是机器学习工作流程的一个重要方面。在 AWS SageMaker 上使用像托管 MLflow 这样的统一系统可以简化此过程，以便在整个机器学习模型生命周期中提供受控的过渡。

### 为什么模型注册在实验中很重要

MLflow 模型注册中心是一项核心功能，它提供了模型版本的高级概述，充当管理和跟踪模型在实验、暂存和生产等生命周期阶段的主要中心。将 SageMaker 模型注册中心与 MLflow 模型注册中心集成结合了两个平台的优势。Modi 解释说：“这种集成最大限度地减少了部署和更新模型所需的手动工作，负责整个生命周期，因此团队可以专注于实现准确性而不会中断。”

这种集成的好处包括：

* **集中式模型跟踪**: 所有模型版本都记录在一个统一的注册中心内，因此实验的每个阶段都保留了文档。
* **增强的模型治理**: 在托管 MLflow 中注册的模型会自动出现在 SageMaker 模型注册中心中，以实现统一的模型治理。

![](https://cdn.thenewstack.io/media/2024/12/ffa136d1-model-registry-1024x486.png)

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

MLflow在SageMaker上与Amazon EventBridge集成，EventBridge是一个无服务器事件总线，用于连接应用程序并自动化机器学习生命周期中的步骤。EventBridge允许您创建事件驱动的工作流，一旦模型需要更新，就会触发重新训练、记录和部署。

自动化机器学习工作流的每个阶段，创建了一个受管理的、可扩展的过程，确保每个模型版本之间的一致性。SageMaker捕获元数据、跟踪变化并标记任何性能退化，为您提供模型生命周期的完整视图，并使您能够主动管理。

### 自动化模型再训练以持续改进

SageMaker Pipeline与托管MLflow集成的自动模型重新训练能力，在数据快速演变的动态环境中尤其有价值。以电子商务平台为例，随着时间的推移，顾客行为和偏好的变化会使静态模型变得过时。同样，语言处理或图像合成中的生成性AI应用也需要持续更新，以有效处理新数据。

### SageMaker中自动化重训练的工作原理

使用SageMaker，您可以配置持续监控，当性能指标低于设定阈值时触发重新训练。例如，如果模型的准确率下降到90%以下，SageMaker可以自动：

1. 从指定的源，例如Amazon S3，摄取最新的数据集。
2. 使用更新的数据和预定义的训练管道触发重新训练作业。
3. 在SageMaker上注册模型到托管的MLflow，这会自动将模型与SageMaker模型注册表同步。
4. 用最小的停机时间重新部署刷新后的模型。

通过将此过程与托管的MLflow集成，您可以获得每个重新训练周期的完整日志。历史指标和参数被存储以供比较，使您能够跟踪性能随时间的改进。这个封闭的反馈循环加强了模型治理，以便模型可以在每次迭代中满足组织标准。

### 提升生命周期自动化和实时更新

EventBridge 改进了由现实世界变化触发的模型更新的管理。例如：

1. 新数据集的到来触发了一个摄取管道。
2. 一旦数据处理完成，EventBridge 就会在 SageMaker 中启动一个重新训练作业。
3. 重新训练后，更新后的模型会自动注册到 MLflow 模型注册表中。
4. 然后 EventBridge 触发部署工作流，确保刷新后的模型以最小的延迟部署到生产环境。

这种自动化使计算机模型能够与实时数据保持同步，减少了人为干预的需求，使工作流可扩展且适应性强。

对于欺诈检测或推荐系统等用例，实时更新至关重要。EventBridge 允许你根据传入的数据流设置触发器，以便模型不断在最新信息上进行训练。这种主动的方法提高了决策的速度和准确性，使模型与不断演变的模式保持一致。

随着机器学习应用的扩展，SageMaker 处理复杂工作流的能力，如 EventBridge 这样的工具将保持关键。自动化和实时更新的结合力量可以帮助企业在数据驱动的世界中保持竞争力。


## 简化数据科学与DevOps团队协作

在SageMaker上管理MLflow简化了数据科学和DevOps团队之间的协作。这种能力减少了瓶颈，从实验到生产都简化了工作流程。一些关键好处包括：

### 统一工作流

Managed MLflow统一了数据科学家和DevOps团队之间的流程。数据科学家利用MLflow来跟踪指标、参数和工件，而DevOps团队则负责管理可复制性和与生产相关的任务。这使得两个团队能够拥有相同的视角，快速识别和解决问题，而不会制造延迟或减缓从实验到生产的过渡。

### 基于角色的访问控制

在SageMaker上管理MLflow使用AWS身份和访问管理来支持安全协作。数据科学家可以访问训练数据、日志和开发所需的工件，而DevOps团队则使用SageMaker推理终端管理部署和监控。明确定义的访问角色增强了安全性和责任性，从而使每个团队都能有效地执行其任务。

### 透明度和问责制

MLflow 的日志系统提供了实验和模型版本的详细审计跟踪。DevOps 团队可以追踪开发历史来解决部署挑战，实验日志还能实现清晰的沟通和无缝交接，防止团队之间的失误。

### 简化的交接

SageMaker 通过自动将 MLflow 中注册的模型与其模型注册表同步，简化了将模型投入生产的过程。它最大限度地减少了错误，加快了部署速度，并支持深度学习和大型语言模型等复杂的工作流程。通过管理基础设施，SageMaker 使团队能够专注于创新，并减少对多种工具的需求。

这种集成对于涉及深度学习模型或大型语言模型的复杂工作流程尤其有利。借助 SageMaker 管理基础设施，团队可以避免同时使用多种工具，这有助于减少错误并加快产品上市时间。

## 总结

随着机器学习的发展，生成式 AI 的兴起带来了独特的挑战，包括管理大规模模型、确保微调的可重复性以及保持实验和部署的效率。Amazon SageMaker 与 MLflow 提供了应对这些挑战的工具，提供安全的协作、自动化的生命周期管理和可扩展的基础设施。

通过满足生成式 AI 时代复杂系统的需求，托管 MLflow 使团队能够应对当前的挑战，例如快速迭代周期、资源优化和负责任的 AI 实践。
