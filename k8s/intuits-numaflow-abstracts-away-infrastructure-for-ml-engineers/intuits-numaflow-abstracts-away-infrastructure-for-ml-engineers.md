<!--
title: Intuit Numaflow：机器学习工程师的基建“隐身衣”
cover: https://cdn.thenewstack.io/media/2025/09/db9cfd33-kubecrash-numaflow-logo.png
summary: Numaflow是Intuit的Kubernetes流处理引擎，简化数据管道构建，无需K8s经验。专为高吞吐量AI设计，解决语言、代码和扩展性挑战，支持自动伸缩。
-->

Numaflow是Intuit的Kubernetes流处理引擎，简化数据管道构建，无需K8s经验。专为高吞吐量AI设计，解决语言、代码和扩展性挑战，支持自动伸缩。

> 译自：[Intuit's Numaflow Abstracts Away Infrastructure for ML Engineers](https://thenewstack.io/intuits-numaflow-abstracts-away-infrastructure-for-ml-engineers/)
> 
> 作者：Joab Jackson

Numaflow 由 Intuit 团队创建，该团队同时开发了 [Argo CD](https://thenewstack.io/survey-argocd-leaves-flux-and-other-gitops-platforms-behind/)。它是一个基于 Kubernetes 的开源流处理引擎，带有用户界面，使工程师能够轻松组合数据处理管道。无需 Kubernetes 经验。

Numaflow 专为高吞吐量工作负载而构建，可连接 [Kafka](https://thenewstack.io/apache-kafka-4-1-the-3-big-things-developers-need-to-know/)、[Pulsar](https://thenewstack.io/need-to-scale-apache-kafka-switch-to-apache-pulsar/) 和 [SQS](https://thenewstack.io/testing-microservices-message-isolation-for-kafka-sqs-more/)，在将数据流发送到目的地之前，可以对其进行分析、过滤或处理。它易于扩展，可按需快速运行。

上周，在 [Kubecrash 2025 虚拟会议](https://www.kubecrash.io/)上，该项目的两名 Intuit 团队成员介绍了 Numaflow 如何用于运行 AI 管道。

[![屏幕截图](https://cdn.thenewstack.io/media/2025/10/d83ad6d0-kubecrash-numaflow-01.png)](https://cdn.thenewstack.io/media/2025/10/d83ad6d0-kubecrash-numaflow-01.png)

## 流处理在 AI 中的作用

将流处理视为 AI 的支柱。

事实证明，AI 中有大量的事件处理：**特征工程**，计算特征并将其添加到模型中；**推理**，训练有素的模型进行预测；当然还有**训练**，模型获取最新数据。

Intuit 的 Numaflow 产品经理 Sriharsha Yayi 表示，如果“你想在事件发生时理解或处理它们并进行响应”，那么实时流处理平台至关重要。例如，可以实时跟踪用户行为以提供推荐。欺诈活动可以在发生时被阻止。

然而，构建数据处理管道可能是一项棘手的任务，更不用说使其可扩展和实时了。

## Kubernetes 事件处理中的常见挑战

Yayi 说，Numaflow 旨在解决 Kubernetes 事件处理中的许多挑战。

首先，了解程序逻辑的数据工程师对他们必须在其上进行设计的 Java 和 Scala 平台并不十分熟悉。也没有多少其他开发人员也想接入流引擎。

Yayi 说：“我们观察到人们希望拥有超越 Java 的流处理能力或框架。”

此外，为某种处理设置整个数据流需要编写大量样板代码，例如在多个消息队列中所需的重复功能。

Yayi 问道：“如果我是一名开发人员，或者一名机器学习人员，为什么我每次编写这些新管道或消费者时，都要花费大量时间一遍又一遍地编写这些集成呢？”

最后，扩展是一个障碍。在事件处理中，对可扩展性的需求是通过事件积压来衡量的，但必须通过 Kubernetes [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) 来表达——通过当时所需的额外 Pod 来实现。一些用户甚至在流量激增时手动调整所需的 Pod 数量。

[![屏幕截图](https://cdn.thenewstack.io/media/2025/10/80598db5-kubecrash-numaflow-02.png)](https://cdn.thenewstack.io/media/2025/10/80598db5-kubecrash-numaflow-02.png)

## Numaflow 如何解决常见的流处理挑战

Intuit 高级软件工程师 Krithika Vijayakumar 解释说：“Numaflow 是一个用于流处理的无服务器平台。” 它旨在隐藏（“抽象”）所有基础设施细节，使其远离数据工程师。

Vijayakumar 说，Numaflow 允许机器学习工程师“只专注于他们的流处理或推理，无需他们理解底层基础设施。”

它还消除了学习这些概念背后所有事件处理复杂性的需要，例如接收器 (sinks) 和源 (sources)，将它们抽象为一个单一的数据对象。

Vijayakumar 阐述道：“我们意识到机器学习工程师主要关注有效负载，他们并不真正在意数据从何处读取。‘是 Kafka 吗？还是 Pulsar？还是 HTTP？’”

[![屏幕截图](https://cdn.thenewstack.io/media/2025/10/ab355faf-kubecrash-numaflow-04.png)](https://cdn.thenewstack.io/media/2025/10/ab355faf-kubecrash-numaflow-04.png)

因此，围绕接收器和源的细节对工程师是隐藏的，他们可以重新专注于他们的推理和处理逻辑。用户将其推理逻辑编写为*用户定义函数* (UDF)。

此外，该平台会根据传入流量自动扩展。不再需要手动启动 Pod 了！

## 使用 Numaflow 构建 AI 管道：演示

Vijayakumar 演示了一个简单的图像识别任务。Numaflow 捆绑了用户界面，因此您可以在构建和运行管道时查看它们：

[![屏幕截图](https://cdn.thenewstack.io/media/2025/10/84de75da-kubecrash-numaflow-06.png)](https://cdn.thenewstack.io/media/2025/10/84de75da-kubecrash-numaflow-06.png)

数据从源拉取并发送到预测顶点。顶点是核心计算组件，在此例中，它将图像内容的文字描述返回到接收器（一个 HTTP 端点）。顶点本身使用本地自然语言处理模型运行。

管道本身使用声明式语言 [YAML](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/) 进行定义。

她还展示了一个正在运行的异常检测管道的片段，该管道已投入生产一年。管道可以有多个源、接收器和 UDF。UDF 可以用 Python 或 Java 混合编写。在图形用户界面中，顶点可以显示它们正在运行的 Pod 数量。它们独立工作，因此它们可以根据各自的传入工作负载进行扩展。

## 一个“相当出色”的数据栈

数据工程师 Dan Young 在他的 [Numaflow 演练视频](https://www.youtube.com/watch?v=zQ170JcbdCo&t=408s)中说：“如果你是原生 Kubernetes 用户，这就是你的最佳选择。” 他建议 Numaflow 与 Argo 一起可以用于构建一个“相当出色”的数据处理栈。

如果您想了解更多信息，Numaflow 工程师也将在即将举行的 [AllThingsOpen](https://www.eventbrite.com/e/all-things-open-2025-tickets-1092602165489?discount=TNS2025) 和 [KubeCon North America](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/?utm_source=the+new+stack&utm_medium=referral&utm_campaign=event) 会议上进行演示。