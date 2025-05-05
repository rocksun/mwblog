
<!--
title: 一家初创公司在边缘端对 Kubernetes、Docker 和 Wasm 进行补充
cover: https://cdn.thenewstack.io/media/2025/05/1ca9ac33-cloud-native-rejekts-2.jpg
summary: 边缘计算崛起！初创 Expanso 如何用 Bacalhau 架构补充 Kubernetes、Docker 和 Wasm？利用分布式 GPU，在数据源头进行 AI 推理和 ML 模型训练，减少数据移动，实现边缘侧的数据处理和分析，或成云原生新趋势。
-->

边缘计算崛起！初创 Expanso 如何用 Bacalhau 架构补充 Kubernetes、Docker 和 Wasm？利用分布式 GPU，在数据源头进行 AI 推理和 ML 模型训练，减少数据移动，实现边缘侧的数据处理和分析，或成云原生新趋势。

> 译自：[A Startup Complements Kubernetes, Docker and Wasm at the Edge](https://thenewstack.io/a-startup-complements-kubernetes-docker-and-wasm-at-the-edge/)
> 
> 作者：Alex Williams



# 一家初创公司在边缘计算领域对 Kubernetes、Docker 和 Wasm 进行补充

![Featued image for: A Startup Complements Kubernetes, Docker and Wasm at the Edge](https://cdn.thenewstack.io/media/2025/05/1ca9ac33-cloud-native-rejekts-2-1024x576.jpg)

[David Aronchick](https://www.linkedin.com/in/aronchick/) 在伦敦市中心 [116 Pall Mall](https://www.116pallmall.com/) 的历史性房间里环顾四周，参加 [Cloud Native Rejekts](https://cloud-native.rejekts.io/) 会议——如果您参加 [KubeCon 会议](https://thenewstack.io/kubecon-cloudnativecon-eu-2025/)，这是一个必参加的会议。顺便说一句，多么棒的空间。

Aronchick 是 [Expanso](https://www.expanso.io/) 的首席执行官，这是一家为工作负载提供分布式计算的初创公司。计算不是移动数据，而是直接到数据本身——随着企业客户在云之外寻找计算需求，这一点变得越来越重要。

他指出，房间里的所有设备总有一天会拥有一些丰富的计算架构。人们逐渐认识到 GPU 将会出现在这些设备上。当然，它们不会是水冷的、巨大的 GPU。这些微型 GPU 的成本可能为 500 美元、100 美元甚至更低。

分布式计算工作负载正在以真实的方式涌现。众所周知，GPU 可以处理最复杂的数据集，用于 AI 和机器学习环境。

## 爱丽丝漫游数据仙境

您开始探索这些新数据点的影响，这变得非常奇妙。英国作家刘易斯·卡罗尔向我们介绍了“掉进兔子洞”的比喻。在分布式计算的土地上，有一个未知的世界，可能比我们意识到的更像爱丽丝的仙境。

但这正是计算的本质：它就像一个仙境。有了数万亿台设备，工作负载将会怎样？这个奇妙的世界将如何获得计算能力？

Aronchick 曾在 [Google](https://cloud.google.com/?utm_content=inline+mention) 工作，在那里他 [共同创立](https://thenewstack.io/kubeflow-co-founder-machine-learning-workflows-on-kubernetes-can-be-simple/) 了 [Kubeflow](https://thenewstack.io/smooth-sailing-for-kubeflow-1-9-thanks-to-cncf-red-hat-support/) 项目，根据 The New Stack 2018 年关于该项目的文章，“该项目旨在帮助简化在 Kubernetes 平台上大规模部署 [机器学习] 应用程序的开源系统”。

对于 Aronchick 来说，重要的是我们如何看待边缘环境为开发人员开发、部署和管理应用程序架构（无论是标准软件还是 [AI 模型](https://thenewstack.io/ai-at-the-edge-architecture-benefits-and-tradeoffs/)）所需的不同维度。

他和他的团队开发了一种名为 [Bacalhau](https://www.bacalhau.org/) 的开源架构。它是一种分布式计算覆盖数据模型，可对 [Kubernetes](https://roadmap.sh/kubernetes)、[Docker](https://www.docker.com/?utm_content=inline+mention) 和 [WebAssembly (Wasm)](https://thenewstack.io/webassembly/) 进行补充。它允许用户在生成和存储数据的地方运行计算作业。

Aronchick 说，当在具有 Kubernetes 集群的云网络中使用多个区域时，网络数据能力会变得有点棘手。跨区域的东西、区域数据移动和跨云工作——Kubernetes 架构需要一种更好的方法来做到这一点。

您可以通过 Aronchick 提出的用例看到这一点。例如，日志可以在边缘进行处理。机器学习 (ML) 推理可以在数据源处进行。使用调度程序，数据在本地节点上运行，而无需集中式数据湖。

这是关于使用远程服务器或物联网 (IoT) 设备（无论它是什么）在将数据发送到中心位置之前在源头处理数据。数据可能会在源头进行一些推理。它可以使用 Wasm 来隔离和处理源头的数据。

## 启动计算

云开发环境是规则，而不是例外。但是有了 Kubernetes、Docker 和 Wasm，使用服务器（比如在餐厅里）的能力变得更加可行。

然而，这仍然留下了将计算能力提供给数据的挑战。根据其文档，Bacalhau 使用本地存储、S3 存储桶或其他存储提供商——减少不必要的数据移动。客户使用 Bacalahau 所谓的作业和执行。作业定义工作流程，执行在节点上并行运行作业。更多信息请点击 [这里](https://docs.bacalhau.org/overview/key-concepts)。

Gartner 估计，大约 10% 的企业生成数据是在传统集中式数据中心或云之外创建和处理的。Gartner 预测，到 2025 年，这一数字将达到 75%。
Aronchick是这样认为的：“我是一家在全球拥有100个节点的企业。我已经拥有了它们，它们可能已经在云中，但它们并不像Databricks、[Snowflake](https://www.snowflake.com/?utm_content=inline+mention)、Kubernetes等一样，处于单个控制器的控制之下。你想要给它们分配一项任务——一个数据处理任务、一个新的ML模型、一个新的配置，任何东西——但今天你无法可靠地做到这一点，因为你没有一个单一的控制器。”

那个控制器？这就是Expanso可以发挥作用的地方。客户可以将Expanso的一个代理放置在这些节点上或附近，使其具有单一控制平面的感觉。

“我们当然可以在手机上运行！”Aronchick说。“但全球有1亿台服务器，每次企业需要一台服务器或一台虚拟机，而这台服务器或虚拟机不在他们的数据中心时，他们都会增加挑战。”

作为背景，洛杉矶和纽约之间的ping时间为49毫秒。光速永远不会变得更快。我们对此无能为力。

内容分发网络非常清楚这一点。[Akamai](https://www.linode.com/?utm_content=inline+mention)现在使用[Fermyon](https://www.fermyon.com/?utm_content=inline+mention)的Wasm技术来隔离数据流。尽管如此，仍然需要移动计算。

但是，将计算转移到数据是一个巨大的成本，[Bogdan Kurnosov](https://www.linkedin.com/in/bogdan-kurnosov/)写道，他现在是[bunny.net](https://bunny.net/)的高级工程经理，[在2024年的The New Stack上](https://thenewstack.io/why-we-chose-webassembly-wasm-for-our-edge-runtime/)写道。

他写道：“进出数据中心的流量路由是时间和金钱的消耗。”“再加上对日益个性化的网络体验不断增长的需求，我们需要探索一种新的云计算方法。幸运的是，我们已经使用我们的内容分发网络（CDN）构建了一个边缘节点网络。将计算能力添加到我们的CDN节点是下一个合乎逻辑的步骤。”

数据将不可避免地走向边缘，这是从超级数据中心模型的一种转变。计算也必须走向边缘。

然后，问题归结为为什么像Expanso这样的公司在这个新世界中会有机会。首先，Bacalhau是一个开源项目。它可以运行在[NVIDIA](https://www.nvidia.com/)、[Intel](https://www.intel.com/content/www/us/en/now/data-centric/overview.html?utm_content=inline+mention)或[AMD](https://www.amd.com/en/products/processors/server/epyc/google-cloud.html?utm_content=inline+mention)上。它是硬件无关的。Expanso技术可以利用分布式GPU的计算能力。

我很清楚为什么像Expanso提供的开源产品，在我们加速走向一个由数万亿设备组成的网络时，会有一条清晰的道路，成为一项核心服务。可观测性是关键。

这就是我在Cloud Native Rejekts上的看法。亚特兰大见。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的YouTube
频道，以流式传输我们所有的播客、访谈、演示等。