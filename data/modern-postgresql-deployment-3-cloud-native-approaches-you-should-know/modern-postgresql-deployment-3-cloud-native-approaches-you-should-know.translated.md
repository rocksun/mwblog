# 现代PostgreSQL部署：三种你应该了解的云原生方法

![关于现代PostgreSQL部署：三种你应该了解的云原生方法的特色图片](https://cdn.thenewstack.io/media/2025/01/cd3c93d6-elephant-herd-1927515_1280-1024x682.jpg)

[PostgreSQL](https://thenewstack.io/postgresql-vs-the-cloud-for-genai-4-things-to-consider/) 已经巩固了其作为世界上最流行的数据库之一的地位，根据[Statista](https://www.statista.com/statistics/809750/worldwide-popularity-ranking-database-management-systems/) 的数据，目前排名第四。正如[2023年PostgreSQL现状调查](https://www.timescale.com/blog/the-2024-state-of-postgresql-survey-is-now-open/) 所发现的，它的采用不仅稳定，而且还在加速增长。自从1990年首次发布以来，安装、部署和管理PostgreSQL的方法已经发生了变化。

在本文中，我将探讨三种云原生和开源的PostgreSQL部署方法。

## 使用CloudNativePG进行Kubernetes部署

在当今的云原生环境中，在Kubernetes上部署PostgreSQL是显而易见的选择。Helm图表将使部署变得简单明了，但是[它不会涵盖有状态工作负载的第二天运维](https://techcrunch.com/2022/11/25/how-to-run-data-on-kubernetes-6-starting-principles/)，例如扩展、备份、故障转移和升级。这就是Kubernetes操作符发挥作用的地方。

[CloudNativePG](https://github.com/cloudnative-pg/cloudnative-pg)，一个开源的Kubernetes操作符，由于其健壮性以及它是厂商中立的且由社区拥有而获得了显著的关注。两年前，该项目背后的公司[EDB](https://www.enterprisedb.com/) [将知识产权捐赠给了](https://www.cncf.io/blog/2024/11/20/cloud-neutral-postgres-databases-with-kubernetes-and-cloudnativepg/) 社区。

该操作符与其他操作符（如[Crunchy Data](https://github.com/CrunchyData/postgres-operator) 和[Zalando](https://github.com/zalando/postgres-operator)）并驾齐驱，但它更注重简单性和数据安全。CloudNativePG最突出的特点之一是它专注于数据完整性和高可用性。它支持同步复制和自动故障转移，确保您的[数据即使在节点发生故障的情况下也能保持一致性和可访问性](https://thenewstack.io/how-event-processing-builds-business-speed-and-agility/)。该项目最近被提交为[CNCF沙箱项目](https://youtu.be/8HIPMmL433g?t=173)，这反映了其对开源原则和协作开发的承诺。

## 使用Cloud Foundry Marketplace for Korifi实现自助服务

平台工程的兴起增加了对自助服务能力的需求，允许开发人员部署和管理[服务而无需过多依赖运维](https://thenewstack.io/choosing-the-right-database-strategy-on-premises-or-cloud/)团队。Cloud Foundry长期以来一直是提供以开发人员为中心的PaaS体验的先驱。

[Korifi](https://github.com/cloudfoundry/korifi) 提供了Cloud Foundry 的相同开发人员体验，但在幕后利用Kubernetes而不是虚拟机。Korifi 隐藏了Kubernetes的复杂性，提供了一个对开发人员来说熟悉且无缝的界面。

其一个关键的历史特性是Cloud Foundry Marketplace，平台运营商和开发人员可以在其中部署预构建的应用程序和服务，[包括现在可用于Korifi的PostgreSQL](https://thenewstack.io/korifi-at-kubecon-cloudnativecon-eu-2024-key-takeaways/)。一个简单的 `cf create-service postgresql` 命令就足以部署PostgreSQL实例。

## 使用Neon分离计算和存储

传统的PostgreSQL部署将计算和存储资源耦合在一起，这可能会导致可扩展性和资源利用率方面的挑战。[Neon](https://github.com/neondatabase/neon?tab=readme-ov-file) 提供了一种无服务器方法，将存储和计算分离。

作为AWS Aurora PostgreSQL的无服务器替代方案，标准存储层被替换为一个分布式架构，该架构将数据重新分布到节点集群中。这种分离允许计算和[存储独立扩展](https://thenewstack.io/momento-caching-at-scale-and-more-without-all-the-hassle/)，从而优化性能和成本。

Neon最受欢迎的功能之一是其数据库的即时克隆和分支，类似于Git处理代码分支的方式。这允许开发团队快速有效地创建隔离的数据库实例。

## 结论

虽然本文并非旨在详尽列举现代部署PostgreSQL的方法，但所讨论的方法反映了三个重要的趋势。
首先是基础设施向云原生原则的转变。曾经，在 Kubernetes 上运行有状态工作负载被认为是不切实际的，但现在已成为标准实践，需要 Kubernetes Operators 来完成额外的工作。

第二个趋势是对符合平台工程原则的自助服务的日益增长的需求，允许开发人员独立地配置和管理资源。

最后，出于成本、合规性和安全性等原因，公司越来越多地希望摆脱托管服务，并采用开源或私有 SaaS 解决方案，这些解决方案提供相同级别的功能，但允许他们完全控制自己的数据。