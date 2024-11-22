
<!--
title: 在内部开发者门户中使用K8sGPT调试K8s
cover: https://cdn.thenewstack.io/media/2024/11/5ddf2e1f-debugging-kubernetes-ai.png
-->

在无缝的开发者门户体验中，学习如何将 AI 驱动的洞察集成到您的 Kubernetes 工作流程中。

> 译自 [Debugging K8s With K8sGPT in Your Internal Developer Portal](https://thenewstack.io/debugging-k8s-with-k8sgpt-in-your-internal-developer-portal/)，作者 Dan Amzulescu。

快速识别和解决问题对于DevOps和站点可靠性工程(SRE)团队来说是一个持续的挑战，他们经常发现自己需要处理与每个问题相关的复杂命令、日志和仪表板网络。这种分散的方法会延缓问题的解决，开发人员经常报告他们花费近40%的时间进行故障排除——这也增加了软件环境面临人为错误的风险。

平台工程的出现是为了克服DevOps的复杂性，而平台工程的核心是内部开发者门户。内部开发者门户简化了事件响应，减少了手动工作，并使DevOps团队能够更快地解决问题。它提供了一个统一的空间来管理基础设施、代码库和部署。

门户还将与软件开发生命周期(SDLC)相关的所有数据集中在一个易于访问的地方。将AI集成到您的门户中可以帮助您主动识别潜在的系统性能下降，并提供有关补救的即时指导，这有时可以将您的平均事件解决时间缩短50%。

在本文中，我将引导您了解如何使用AI来丰富门户数据，以及如何在门户中显示丰富的数据以减少解决时间。

## 使用K8sGPT丰富门户数据

[K8sGPT](https://github.com/k8sgpt-ai/k8sgpt)是一个专门为Kubernetes(K8s)环境设计的AI代理。它从历史数据中提取可操作的见解，提供快速建议，从而显著减少解决时间。通过精确定位异常或错误配置并提供智能解决方案，K8sGPT将传统上的被动流程转变为主动流程。此外，通过与您的门户紧密集成，这些见解在一个单一窗口中呈现，完全符合您的操作工作流程。

虽然此示例将仅关注Kubernetes，但在更高级的场景中，例如云基础设施（问题通常跨越堆栈的不同层），AI可以跨多个领域提供帮助。我们的目标不仅仅是让AI能够处理多个领域，而是使其能够完全自动化补救过程，独立解决问题。

在[内部开发者门户](https://thenewstack.io/improve-developer-onboarding-with-an-internal-developer-portal)的上下文中，您可以使用K8sGPT从整个SDLC中的所有工作流程收集数据并从中提取见解。考虑到这一愿景，让我们从小处着手，探索单域工作流程如何提高效率。

## 部署自动AI丰富流程

假设您想创建一个自动化工作流程，以使用Kubernetes工作负载的实时视图来丰富您的内部开发者门户。此工作流程涉及几个关键组件，这些组件协同工作，将使用AI创建一个自动化流程，帮助您使用门户解决K8s中观察到的问题。

这些组件包括：

- **Kubernetes (K8s)集群**: 这代表您的工作负载基础设施。部署Kubernetes集群的方法有很多，最常见的是平台即服务(PaaS)，例如[Amazon](https://aws.amazon.com/?utm_content=inline+mention)EKS，[Microsoft](https://news.microsoft.com/?utm_content=inline+mention)AKS和[Google](https://cloud.google.com/?utm_content=inline+mention)GKE。无论您使用什么，都应该在集群和门户之间进行[集成](https://docs.getport.io/integrations-index/#kubernetes)，以便同时列出工作负载及其运行状况。
- **[内部开发者门户](https://www.getport.io/blog/what-is-an-internal-developer-portal)**：这是所有关于Kubernetes集群的数据被集中、关联和细化的位置。这将方便地访问部署数据和有关如何解决不健康的Kubernetes工作负载的AI见解。我将在此示例中使用[内部开发者门户:](https://www.getport.io/blog/what-is-an-internal-developer-portal)[Port](https://www.getport.io/?utm_content=inline+mention)。
- **K8sGPT**: 这是主要的AI“顾问”。它负责对K8s API发出命令，以收集数据并与提供见解的AI大型语言模型(LLM)进行来回通信。
  - K8sGPT可以在集群外部和内部部署。要部署K8sGPT REST API服务器，请[按照安装指南](https://docs.k8sgpt.ai/getting-started/installation/)进行操作。
  - 使用此命令启动REST API：`k8sgpt serve --http`
  - 要在集群内部署K8sGPT，请[按照安装指南](https://docs.k8sgpt.ai/getting-started/in-cluster-operator/)进行操作。
- **通信协调器**: 通信协调器对于弥合门户和K8sGPT之间的差距至关重要。它确保命令、查询和见解能够在这些系统之间无缝流动。根据您组织的安全和合规性要求，您可以使用：
  - [Kafka](https://thenewstack.io/top-10-tools-for-kafka-engineers/)主题，本例使用此方法。这意味着当工作负载被识别为失败时，将在Kafka主题中创建一个消息。通信协调器（在本例中为[Python](https://thenewstack.io/what-is-python/)脚本）将处理检查主题和基于`PULL`方式消费消息。
  - 另一种方法是让脚本持续检查工作负载的本地运行状况，并在工作负载失败时使用AI见解丰富检查结果。
- **AI LLM**: K8sGPT背后的核心智能利用自然语言处理来解释Kubernetes数据并提供可操作的建议。
 
请注意，K8sGPT目前支持[11种不同类型的AI后端](https://docs.k8sgpt.ai/reference/providers/backend/)。我已经用[Ollama](https://docs.k8sgpt.ai/reference/providers/backend/#ollama)测试过它；您也可以[下载模型](https://ollama.com/library)。查看这些指南以获取有关[使用OpenAI API令牌](https://platform.openai.com/docs/quickstart)和[使用Ollama部署本地LLM](https://github.com/ollama/ollama)的帮助。

部署后，您可以将K8sGPT配置为[使用Ollama](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/)，如下所示：

```bash
k8sgpt serve --http -b openai
```

## 了解事件流程

查看下图，以便更好地了解如何启用完全自动化的事件流以提供AI见解。技术栈中每个元素旁边的数字对应于它们如何参与流程的说明：

![下文描述的自动化事件流](https://cdn.thenewstack.io/media/2024/11/515348e9-event-flow-ai-insights-1024x536.png)

*(来源：Port)*

1. K8s集成使用工作负载的运行状况更新门户。
2. 自动化工作流向Kafka主题发布消息。
3. [Python](https://roadmap.sh/python)脚本获取主题消息数据。
4. Python脚本轮询K8sGPT以获取见解。
5. K8sGPT与K8s集群和LLM通信。
6. K8sGPT向Python脚本回复见解。
7. Python脚本利用门户API（在本例中为Port）使用有关如何解决问题的见解填充Kubernetes工作负载实体。

## 配置门户中的自动化工作流

现在是时候配置门户以促进自动化工作流了。首先：将AI见解数据作为Kubernetes工作负载仪表板的一部分。将Port Insights属性添加到您的工作负载蓝图中：

![数据模式下K8s工作负载蓝图的JSON表示](https://cdn.thenewstack.io/media/2024/11/9e9c3096-insights-property-1024x737.png)

*数据模式下K8s工作负载蓝图的JSON表示（请参阅GitHub中的[JSON代码](https://github.com/dan-amzulescu-port/Port-K8sGPT/blob/main/PortObjects/Blueprints/workload.json)）。*

接下来，定义一个工作流，该工作流将自动通知您的通信协调器存在不健康的工作负载。您需要选择将触发[工作流自动化](https://thenewstack.io/why-internal-developer-portals-need-automations)（报告工作负载的运行状况）的数据点，并定义将触发的内容（工作负载数据将发送到Kafka）：

![自动化工作流的JSON表示](https://cdn.thenewstack.io/media/2024/11/b0125fc5-json-automation-workflow-980x1024.png)

*自动化工作流的JSON表示（请参阅GitHub中的[此代码](https://github.com/dan-amzulescu-port/Port-K8sGPT/blob/main/PortObjects/Automations/K8s-serviceUnHealthy.json)）。*

最后但并非最不重要的一点是，您需要创建协调器，它将：

- 持续监听Kafka主题。
- 使用正确的类型消费相关消息，以轮询K8sGPT以了解已识别的、不健康的工作负载。
- 使用来自K8sGPT的见解填充门户中相关的Kubernetes不健康工作负载。

以下是门户中K8s AI见解的示例：

![Kubernetes工作流见解的JSON表示](https://cdn.thenewstack.io/media/2024/11/b45e7aa4-json-kubernetes-workflows-912x1024.png)
Kubernetes工作流见解的JSON表示（请参阅GitHub中的[此代码](https://github.com/dan-amzulescu-port/Port-K8sGPT)）。

现在，实施此工作流程后，您可以接收有关 Kubernetes 工作流程运行状况的定期实时更新，以及如何解决这些问题的建议。这有助于缩短查找问题和找出解决方法所需的时间。

## 工作流程的其他注意事项

虽然这可能是自动化工作流程的一个良好开端，但您仍然可以通过其他方式持续改进它并提高效率。

您可以通过多种方式简化工作流程中的事件流程——例如，您可以完全绕过使用事件触发 K8sGPT，而是修改脚本以持续监控集群的运行状况并自主分发见解。

此示例中的命令行输出和整体改进也优于通过 REST API 提供的输出。因此，进行了一些额外的输出修改以改进整体 REST API 生成的输出。

## 使用替代 GPT

虽然 K8sGPT 提供了令人印象深刻的功能，但在更高级的场景中，人工智能可以跨多个领域（例如云基础设施）提供帮助，而问题通常会跨越堆栈的不同层。目标不仅仅是让 AI 能够处理多个领域，而是使其能够完全自动化补救过程并独立解决问题。

我最近遇到了另一个新兴的开源 AI 项目，[HolmesGPT](https://github.com/robusta-dev/holmesgpt)，我相信它可以补充甚至扩展 K8sGPT 的功能。

HolmesGPT 提供 AI 驱动的见解，并支持 Kubernetes 和其他灵活的部署架构，以及多种 AI 模型。但是，根据我的实验，HolmesGPT 以其高级功能和卓越的性能脱颖而出。

HolmesGPT 的一个突出特点是它能够理解和响应自然语言查询。以下两个示例说明了它的强大功能：

1. 简单问题：识别存在问题的 Kubernetes Pod

![](https://cdn.thenewstack.io/media/2024/11/dd755239-simple-question-holmesgpt-1024x176.png)

2. 复杂查询：请求解决方案

![](https://cdn.thenewstack.io/media/2024/11/f165c76f-complex-question-holmesgpt-1024x171.png)

但 HolmesGPT 并不止步于 Kubernetes。它将其分析能力扩展到各种平台和工具，包括 [PagerDuty](https://www.pagerduty.com/?utm_content=inline+mention)、OpsGenie、Prometheus 和 Jira。这种跨域功能改变了游戏规则，允许用户设置工作流程来分析和解释来自许多不同来源的日志和数据。

此功能的核心是运行手册的概念，它可以用自然语言定义。这些运行手册使用户能够创建跨域工作流程，以进行全面的问题分析和解决，使整个故障排除过程更加连贯和简化。

本质上，HolmesGPT 不仅仅是 Kubernetes 的 AI 工具——它是现代 DevOps 环境的整体解决方案，使团队能够更高效、更有效地解决问题。

## 总结

- 调试和解决问题通常会消耗工程师大量时间，并涉及容易出错的手动流程。
- 缩短解决时间对于提高服务质量和使团队能够专注于创新至关重要。
- 内部开发者门户通过提供完善的上下文信息，代表着朝着缩短解决时间迈出的重要一步。
- 可以通过利用跨各个领域的 AI 见解来进一步增强门户。
- 最终目标是实现跨域洞察和自动化补救，从而简化问题解决流程。
想要了解它如何为您工作？

查看 Port 的 [现场演示](https://demo.getport.io/organization/home) 或阅读有关使用 Crossplane、Kubernetes 和门户 [推动开发者自助服务](https://thenewstack.io/drive-developer-self-service-with-crossplane-k8s-and-a-portal/) 的信息。通过加入 [Port 的 Slack 社区](https://join.slack.com/t/port-community/shared_invite/zt-2n5tu72wi-FEgN6HGFeG9bcRfHtKYdCg) 与志同道合的人讨论所有关于门户的事情。
