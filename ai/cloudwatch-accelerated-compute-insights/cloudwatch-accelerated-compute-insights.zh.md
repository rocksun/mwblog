![抽象单色数字地形，带有类似电路的裂缝，代表GPU集群可观测性和工作负载盲区。](https://cdn.thenewstack.io/media/2026/11/c92a967e-flying-object-jzkpjxphomq-unsplash-1024x576.jpg)

**加速器账单已成为基础设施预算中最大的项目之一。** GPU 已成为现代计算中最昂贵的资源，然而大多数组织在运营它们时却几乎没有可见性。单个训练集群可以运行数天并花费数百万美元。大多数组织在共享集群跨团队共享这些加速器以保持它们满负荷运转。但在这些共享环境中，平台团队无法回答基本问题：哪个团队正在使用哪些加速器？推理工作负载是否在高效生成 Token？是什么在浪费金钱？

当工作负载退化（加速器故障、热节流节点）时，团队只有在运行崩溃或账单到达后才会发现。查找原因所需的设备级信号（请求痕迹、内核日志、加速器本身的内存指标）没有被收集或关联。如果没有将问题隔离到单个加速器的方法，团队就会退回到重启整个实例的做法，为了解决一个故障而牺牲七个健康的 GPU，并且常常要等待稀缺的容量来恢复实例。

> “GPU 已成为现代计算中最昂贵的资源，然而大多数组织在运营它们时却几乎没有可见性。”

加速器可观测性将这些盲区转化为答案。它告诉你谁在使用你的加速器，它们是否健康，以及浪费花费了你多少钱，一直精确到单个设备。这样，你就可以修复一个坏掉的 GPU 而不是八个，把你的加速器预算花在真正的工作上，而不是闲置的容量上。

Amazon CloudWatch 加速计算洞察（accelerated compute insights）是 KubeCon North America 2026 上推出的一项新功能，它为你提供集群中每个加速器的单一运营视图。它向平台和 AI 团队展示谁在使用其 Amazon Elastic Kubernetes Service (Amazon EKS) 上的 GPU 和 AWS AI 加速器容量。在这篇文章中，我们将探讨加速 compute insights 的功能、它在 Amazon EKS 上的工作原理以及如何开始使用。

## 加速计算洞察能做什么

加速计算洞察为你提供集群中每个加速器的单一运营视图。它展示每个加速器的使用情况，在故障和瓶颈发生时进行检测，估计每个问题的成本影响，并将这些发现与解决它们的行动联系起来。

> “加速计算洞察将加速器遥测、工作负载边界和定价数据结合在一起，这是仅能看到指标的监控工具无法复制的组合。”

在 Amazon EKS 上，它支持 NVIDIA GPU 以及 AWS Trainium 和 AWS Inferentia。来自 NVIDIA GPU 和 Inferentia 的指标被标准化为通用模式，并呈现在单一的加速器健康视图中，因此运行混合集群的团队可以在一个地方管理每个加速器类型。

## 具有 Kubernetes 上下文的集群可见性

EKS 集群中的每个加速器都丰富了 Kubernetes 元数据：Pod、命名空间、节点、节点组和自定义标签（团队、应用程序）。你可以跨整个集群查看按团队和工作负载划分的利用率。

加速计算洞察自动检测 MIG（多实例 GPU）分区的 GPU，并显示每个 MIG 实例的利用率和内存，以及使用它的 Pod。它还通过读取设备标签来识别其他分区方案，包括 Kubernetes DRA（[动态资源分配](https://thenewstack.io/kubernetes-dra-gpu-scheduling/)）和时间分片。无需配置。

## 成本浪费识别

加速计算洞察将实时加速器遥测连接到工作负载边界事件和 AWS 定价数据，以呈现三个类别的可回收浪费：

1. 调整大小的机会：运行在比任务需要的更强大实例上的工作负载。
2. 训练效率差距：相对于工作负载自身历史基准较低的张量核心（MFU）利用率，表明作业没有从硬件中获得全部价值。
3. 低于硬件容量的推理：基于与设备利用率相关的客户发出吞吐量，端点提供的请求少于硬件支持的请求。

对于每个发现，加速计算洞察识别负责的具体工作负载或节点，帮助用户进行故障排除和优化。之所以有效，是因为加速计算洞察将加速器遥测、工作负载边界和定价数据结合在一起，这是仅能看到指标的监控工具无法复制的组合。

注意：CloudWatch 加速计算洞察是一个运营工具，而不是计费或分摊工具。成本数字是旨在指导运营决策的估计值。对于权威的成本和使用核算，请继续使用 AWS Cost Explorer 以及 AWS 成本和使用报告。

当推理工作负载经历性能退化或低效的 Token 生成时，加速计算洞察有助于识别 GPU 瓶颈、低效的加速器利用率以及潜在的资源浪费。通过自动收集和关联推理性能指标、请求痕迹、日志和加速器遥测，它为工作负载性能和 GPU 效率提供端到端可见性。借助 AI 驱动的洞察和故障排除功能，客户可以快速识别根本原因，优化 Token 吞吐量，减少推理延迟，并提高加速器利用率，而不会中断健康的工作负载。

> “它区分了需要不同行动的故障模式。默认情况下，智能体会提供一个具体的、有证据支持的行动计划供你批准。”

你还可以将健康事件路由到 AWS DevOps 智能体以进行更深入的调查。该智能体跨加速器遥测、CloudWatch 日志、最近的基础设施更改、作业配置以及你编写的任何运行手册进行推理。它区分了需要不同行动的故障模式。例如，需要更换的具有加速内存错误趋势的节点与通过重启清除的驱动程序问题。默认情况下，智能体提供一个具体的、有证据支持的行动计划供你批准。为了实现更快的循环，你可以选择让它通过 AWS API 自行执行易于理解的修复。

## 它在 EKS 上的工作原理

收集路径汇聚在 CloudWatch Metrics API。对于 NVIDIA GPU，CloudWatch 智能体和 NVIDIA Exporter 收集设备级指标。统一加速器健康层将 GPU 和 Inferentia 收集路径标准化为通用模式，并将它们呈现在单个仪表板中。

下图说明了 Amazon CloudWatch 加速计算洞察如何为 Amazon EKS 上的 AI 推理工作负载和加速器效率提供端到端可观测性。客户可以从 CloudWatch 控制台或 CloudWatch Omni 安装 CloudWatch 可观测性加载项，以收集 NVIDIA GPU 指标和[推理工作负载性能](https://thenewstack.io/ai-inference-kubernetes-observability/)指标、日志和痕迹。遥测数据通过 CloudWatch OpenTelemetry (OTLP) 端点摄入到 CloudWatch 的集中式存储中。客户可以直接在 CloudWatch 控制台监控推理工作负载性能和 GPU 利用率，或者利用 CloudWatch Omni 及其 AI 驱动的调查来排查性能问题、识别加速器低效并优化资源利用率。

![图表说明了 Amazon CloudWatch 加速计算洞察如何为 Amazon EKS 上的 AI 推理工作负载和加速器效率提供端到端可观测性。](https://cdn.thenewstack.io/media/2026/11/4ae1026f-image1-1024x317.png)





*点击放大图形。*

## 在 EKS 上开始使用

安装启用了 OTel Container Insights 的 CloudWatch 可观测性加载项。该加载项发现你的加速器并收集仪表板所需的一切。无需每个节点设置，无需管理的智能体，无需配置收集管道。你的集群会在几分钟内出现在控制台中，并在节点加入和离开集群时保持最新。

## 第 1 步：让你的数据流动起来

如果你在 Amazon EKS 上运行自托管推理，请将 Amazon CloudWatch 可观测性 EKS 加载项安装或升级到 v7.0.1 或更高版本。该加载项发现你集群中的每个 NVIDIA GPU 和 AWS Inferentia 设备，并开始发送 OpenTelemetry 数据，无需每个节点设置，也无需配置收集管道。

你可以使用 eksctl、Helm 或 Terraform 启用加载项。请查看下面的 eksctl 和 Helm 示例：

### 使用 eksctl

```

eksctl create addon \
  --name amazon-cloudwatch-observability \
  --cluster your-cluster-name \
  --region your-region

```

### 使用 Helm

```

helm repo add aws-observability https://aws-observability.github.io/helm-charts
helm install amazon-cloudwatch-observability \
  aws-observability/amazon-cloudwatch-observability \
  --namespace amazon-cloudwatch --create-namespace

```

## 第 2 步：在 CloudWatch Omni 中使用你的数据

一旦遥测数据开始流动，打开 CloudWatch Omni。Omni 专为拥有推理代码并对其进行修复的团队而构建。你获得的不是一堵基础设施指标墙，而是一个以应用为中心的视图：你的[推理工作负载](https://thenewstack.io/ai-observability-through-interoperability/)与调用它们的的服务和 AI 智能体相邻显示，加速器健康状况、利用率和浪费与每个工作负载绑定。

当端点显示低吞吐量或高首字 Token 时间（time to first token）时，Omni 帮助你将问题追溯到负责的工作负载、节点或单个加速器，并显示要更改的内容，无论是配置更新还是代码修复。你无需切换工具即可从检测转到修复。

> “你获得的不是一堵基础设施指标墙，而是一个以应用为中心的视图：你的推理工作负载与调用它们的的服务和 AI 智能体相邻显示，加速器健康状况、利用率和浪费与每个工作负载绑定。”

需要跨集群视图的平台和基础设施团队，例如跨多个团队的加速器分配、闲置容量或跨账号摘要，也可以在 CloudWatch 控制台的加速计算洞察页面上看到相同的数据。

准备好查看你自己的集群了吗？这篇[文档](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Accelerated-Compute-Insights-Get-Started.html)将引导你开始使用。

## 这在 Amazon EKS 可观测性栈中的位置

Amazon CloudWatch 加速计算洞察建立在我们整个 2025 年和 2026 年为 EKS 推出的可观测性基础之上：用于基础设施指标的 OTel Container Insights、用于应用遥测的应用性能监控以及用于网络层的容器网络可观测性。加速计算洞察添加了缺失的层——加速器本身。团队在他们已经监控其他所有内容的同一地方，获得 GPU 和 Inferentia 利用率、成本浪费和设备级健康状况，所有这些都丰富了 Kubernetes 元数据并连接到自动化修复

## 立即开始

Amazon CloudWatch 加速计算洞察现已在支持 CloudWatch Omni 的所有[区域](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-cloudwatch-omni-8-regions/)推出。要开始使用：

1. 在你的集群上安装或升级到最新的 CloudWatch 可观测性 EKS 加载项。
2. 打开 CloudWatch Omni 以查看你的推理工作负载，以及每个工作负载的加速器健康状况和浪费。
3. 从工作负载视图进行故障排除和优化，从首字 Token 时间一直到单个设备。

查看[文档](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Accelerated-Compute-Insights.html)了解更多信息。

这篇文章最早发布在 [The New Stack](https://thenewstack.io) 上，标题为[昂贵的加速器却缺乏工作负载级可见性：介绍 Amazon CloudWatch 加速计算洞察](https://thenewstack.io/cloudwatch-accelerated-compute-insights/)