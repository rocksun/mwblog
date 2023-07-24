# DevOps 已经胜利，平台工程师万岁

又一个体现Kubernetes成熟的迹象是，平台工程团队正在向用户推广自助式云操作模型。

翻译自 [DevOps Has Won, Long Live the Platform Engineer](https://thenewstack.io/devops-has-won-long-live-the-platform-engineer/) 。我们的平台工程师们正在实现本文所说的目标。

![](https://cdn.thenewstack.io/media/2023/07/234ba800-platform-engineering-1-1024x576.jpg)

在软件开发的世界中，DevOps 的概念取得了如此成功，以至于谈论它作为一种实践似乎已经过时。但是，尽管现在可能是宣布 DevOps 这一旧概念已经消亡的时候，但这更多地反映了它的成功，而非它的衰落。

十年前，DevOps 是一种文化现象，开发人员和运维人员联合起来，形成了一个共同的联盟，打破了各自的壁垒。快进到今天，我们看到 DevOps 在平台工程的兴起下进一步形式化。在平台工程的框架下，DevOps 现在拥有预算、团队和一套自助式工具，以便开发人员可以更直接地管理运维。

平台工程团队提供了使 [Kubernetes](https://roadmap.sh/kubernetes) 成为自助式工具的好处，增强了数百名用户的开发效率和速度。这是 Kubernetes 成熟和普及的又一个迹象。根据 [Gartner 的预测](https://emtemp.gcom.cloud/ngw/globalassets/en/publications/documents/2023-gartner-top-strategic-technology-trends-ebook.pdf)，在未来三年里，五个软件工程组织中就会有四个利用平台团队来提供可复用的应用交付服务和工具。

## 平台工程是新的中间件

随着开发人员数量从几百人增加到数千人，应用程序不断增多，旧的中间件概念——一种基于工单的应用程序服务器，但始终处于待命状态——现在被[平台工程](https://thenewstack.io/platform-engineering/)所取代，为开发人员提供自助式模型。

这为什么很重要：在 DevOps 的尴尬青少年阶段，进行了大量实验和部署新技术，但这些技术还没有融合。现在，现代应用程序已经稳定下来，使用容器和存储，网络和安全性运行在 Kubernetes 中，采用云原生方式。

开发人员不再使用工单系统。他们期望使用弹性基础架构，并通过由平台工程师维护和运行的平台来使用和部署。这种成熟转变改善了响应能力。开发人员可以快速对他们正在开发的应用程序进行更改，并非常迅速地将应用程序推向生产环境。由于开发人员负责，开发和部署所需的时间大大减少。

Portworx 使 T-Mobile 将应用程序部署时间从 6 个月缩短到几小时。与 T-Mobile 一样，企业有数千名开发人员需要“自助式”或按需访问存储和数据服务，平台工程团队努力以大规模交付这些服务。

作为 IT 的替代品，平台工程团队依托于两组技术——云原生技术和现代数据库和数据服务，例如 Postgres、[Redis](https://redis.com/?utm_content=inline-mention)、Cassandra、Kafka，甚至像 Spark 这样的流媒体服务，都由平台团队以服务形式提供给开发人员。

平台工程师提供的关键服务，否则用户需要越来越多的 Kubernetes 专业知识，包括 Kubernetes 发行版本身，无论是 OpenShift 还是 Google Kubernetes Engine (GKE) 或 Elastic Kubernetes Service (EKS) 或 Rancher 。安全性是另一个重要服务，例如 Prisma Cloud 或 Sysdig 等平台。

另一个服务是关于 Kubernetes 的数据管理——管理存储资源、备份、灾难恢复以及 Kubernetes 下方的数据库和数据服务。在 Portworx 中，我们亲眼目睹了这些效率，我们的几个客户只需雇用少数平台工程师即可服务数百名用户。

## 使 Kubernetes 无形化 — 关注“是什么”而不是“如何”

当一种技术变得普遍时，它开始变得更加隐形。以半导体为例。它们无处不在。它们从微米级进步到纳米级，从五纳米降至三纳米。我们在遥控器、手机和汽车中使用它们，但芯片是无形的，作为终端用户，我们不再思考它们。

Kubernetes 也是如此。在企业中，Kubernetes 正嵌入到越来越多的东西中，而自助式范式使得对用户来说 Kubernetes 变得无形。在过去的 DevOps 中，每个开发人员都需要了解 Kubernetes 。现在，开发人员需要使用它，但只有平台工程师真正需要了解它。

平台工程为开发人员带来了美妙的礼物，他们不再必须在日常工作中费力去看和理解 Kubernetes 的细节。随着 Kubernetes 的不断发展，它有助于缩小持续存在的技能差距，并为公司的创新能力和保持竞争优势做出有意义的贡献。