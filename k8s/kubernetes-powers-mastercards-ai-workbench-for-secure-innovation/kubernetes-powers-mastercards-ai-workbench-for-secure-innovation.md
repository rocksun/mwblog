<!--
title: Kubernetes为Mastercard的AI工作台提供安全创新能力
cover: https://cdn.thenewstack.io/media/2025/04/9633e0a9-kubernetes-mastercard-ai-workbench.jpg
summary: Mastercard基于Kubernetes打造AI工作台，采用Red Hat OpenShift构建离线集群，保障数据安全。利用Jupyter Notebooks加速实验，通过动态GPU分配和Kubeflow、Spark Operator集成，实现高效的AI/ML模型训练和工作流程自动化，提升数据科学家生产力，加速AI创新。
-->

Mastercard基于Kubernetes打造AI工作台，采用Red Hat OpenShift构建离线集群，保障数据安全。利用Jupyter Notebooks加速实验，通过动态GPU分配和Kubeflow、Spark Operator集成，实现高效的AI/ML模型训练和工作流程自动化，提升数据科学家生产力，加速AI创新。

> 译自：[Kubernetes Powers Mastercard's AI-Workbench for Secure Innovation](https://thenewstack.io/kubernetes-powers-mastercards-ai-workbench-for-secure-innovation/)
> 
> 作者：Alex Handy

对于当今的许多企业来说，人工智能并不是一个陌生的概念。借助正确的工具、平台和团队，人工智能和机器学习在业务上的有效应用可以作为公司当前基础设施的扩展而增长。对于 Mastercard 来说，对[数据科学的深刻理解](https://roadmap.sh/ai-data-scientist)已经融入到这家全球支付公司中。

Mastercard 软件工程总监 Alexander Hughes 表示，公司的使命是“连接并驱动一个包容性的数字经济，通过使交易安全、简单、智能和可访问，从而使每个人都能从中受益。我们利用安全的数据和网络、合作伙伴关系和热情来提供解决方案和创新，以帮助个人、金融机构、政府和企业实现其最大潜力。”

## 为实验创造空间

他和 Mastercard 首席 Kubernetes 架构师 Ravishankar Rao 在 [OpenShift Commons Gathering](https://commons.openshift.org/)（KubeCon Salt Lake City 的一个[同期活动](https://commons.openshift.org/gatherings/kubecon-24-nov-12/)）上发表了演讲。在他们的演讲中，他们详细介绍了他们在 Mastercard 为数据科学家实现的转型。他们首先设想了一个新的平台，该平台围绕着为实验提供空间的想法而构建，该空间可以无缝且安全地转移到生产环境中。

Hughes 说：“我们希望确保这个平台能够为数据工程师和数据科学家提供一个快速的实验空间，我们使用 [Jupyter Notebooks](https://jupyter.org/) 来实现这一点。这与经过微调的 CPU 和 GPU 配置文件相结合，可实现高效的资源利用，从而实现快速迭代和创新解决方案。”

Hughes 说：“接下来，我们开始解决训练的工作流程编排问题。因此，我们通过动态 GPU 分配和专门的 GPU 集群环境实现了高效且可扩展的机器学习模型训练。”

他继续说道：“我们拥有集中的协作功能，可进一步增强训练工作流程，使其无缝且高效。该平台提供无缝注册、管理和共享功能的功能。这促进了协作式功能工程，确保这些团队可以有效地协同工作并利用共享资源。”

## 在 Kubernetes 上构建 AI 工作台

![AI 工作台的功能：弹性计算、工作负载隔离、专用 AI/ML 生态系统、工作流程实例化、模型服务](https://cdn.thenewstack.io/media/2025/04/01259fd9-mastercard-ai-workbench-kubernetes-capabilities.png)

*Mastercard 在 Kubernetes 上的 AI 工作台的关键功能。来源：Mastercard*

这个名为 AI 工作台的新平台还具有极高的[安全要求](https://thenewstack.io/security/)，因为没有比信用卡提供商更大的信用卡信息来源了。它是私有数据的本质，构成了 Mastercard 数据集的核心。

当然，能够以离线模式运行这种类型的 AI 工作台，甚至工作负载和集群都没有开放互联网访问的气息，对于这种类型的工作来说是最好的情况，这就是 Mastercard [使用 Red Hat OpenShift 构建](https://thenewstack.io/choosing-the-right-red-hat-ai-solution-rhel-ai-vs-openshift-ai/)的原因：集群可以在断开连接的环境中运行。

Hughes 说：“我们在这个工作台中所做的一切都基于 [Kubernetes](https://thenewstack.io/kubernetes/)，但我们希望确保我们正在谈论的 Kubernetes 集群的资源受到保护并与通用工作负载隔离，我们通过专门构建的纯 AI/ML 集群来实现这一点。这确保了一个专为这些高级目的量身定制的专用生态系统。”

Hughes 解释说：“在 AI 产品开发领域，我们注意到我们的工程师经常执行重复性任务，因此我们实施了自动化工作流程实例化，以协助进行超参数优化、模型选择和特征选择等活动。”

![架构包括 UX（Spark 工作负载、Jupyter CLI、Kubeflow 仪表板和配置文件）和用于部署 AI/ML 和 Spark 工作负载的工作台平台。](https://cdn.thenewstack.io/media/2025/04/8d82b18b-ai-workbench-technical-diagram.png)

*Mastercard AI 工作台组件的技术图。来源：Mastercard*

Rao 描述了构建 AI-Workbench 的最后步骤和过程。“我们集成了 Kubeflow 和 Spark Operator 的所有组件，以便数据科学家可以运行他们的 AI/ML 工作负载。最后，我们实际上实现的是，我们能够以自动化的方式在开发、暂存和生产环境中部署相当多的 AI-Workbench，并且我们能够让大量数据科学家加入到这个平台，并能够交付一些增值解决方案。最重要的方面是，我们还能够引入 GPU 计算，这加速了训练，并将其从几周缩短到几天，”Rao 说。

Mastercard 进行了一项内部调查，以了解用户对 AI-Workbench 的看法。他们的内部数据科学家和开发人员指出，这是一个“很棒的实验平台”。内部团队对从基于 OpenShift 的 AI-Workbench 中获取数据的容易程度感到满意，因为该平台已经支持必要的库和工具。

要了解更多关于 OpenShift 作为 AI 工作负载平台的信息，请查看[使用 AI/ML 推进业务的指南](https://www.redhat.com/en/resources/advance-business-with-ai-ml-ebook)。