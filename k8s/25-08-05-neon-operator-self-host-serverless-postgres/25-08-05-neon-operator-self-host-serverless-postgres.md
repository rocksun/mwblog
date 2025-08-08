
<!--
title: Neon Operator：在 Kubernetes 上自建无服务器 Postgres
cover: https://molnett.com/images/posts/25-08-05-neon-operator-self-host-serverless-postgres/mainImage.png
summary: Molnett 发布了 Neon Operator 的早期版本，允许在 Kubernetes 上自托管 Neon。该 Operator 使用 Rust 和 kube-rs 构建，旨在简化 Neon 集群的部署和管理。他们正在寻找合作者一起改进项目并将其投入生产。
-->

Molnett 发布了 Neon Operator 的早期版本，允许在 Kubernetes 上自托管 Neon。该 Operator 使用 Rust 和 kube-rs 构建，旨在简化 Neon 集群的部署和管理。他们正在寻找合作者一起改进项目并将其投入生产。

> 译自：[Neon Operator: Self-Host Serverless Postgres on Kubernetes](https://molnett.com/blog/25-08-05-neon-operator-self-host-serverless-postgres)
> 
> 作者：Jonathan Grahl

## 我们开始吧！

我们很高兴地宣布 <https://github.com/molnett/neon-operator> 的早期版本，这是一个 Kubernetes Operator，允许你在自己的基础设施上自托管 Neon。 这是我们努力理解 Neon 内部细节的结晶，我们很高兴与社区分享我们的发现。

我们正在慢慢发展一个由对构建这个项目感兴趣的个人和公司组成的社区，其中一些主要参与者已经加入了这项工作。 我们希望发布这个 Operator 能够带来一股平台构建者的浪潮，他们和我们一样对分离式架构感兴趣。

如果你有同感，请在 [X](https://X.com/jonathangrahl) 或 Discord @bittermandel 上联系我，我很乐意和你聊聊！

### 当之无愧的认可

如果没有 Neon 团队的不懈努力，这一切都不可能实现。 他们在制作一个可大规模自托管的 OSS 产品方面做得非常出色。 他们设计的架构使我们能够自信地构建自己的控制平面，而无需与 Neon Cloud 竞争（这将需要大量的风险投资）。 在我看来，这是一个双赢的局面！

值得注意的是，OSS 数据库很少有允许你合理地自托管大型集群的功能。 Clickhouse 是一个反例，因为他们故意将 SharedMergeTree 等功能保持为闭源，这使得他们能够在多租户环境中运行 ClickHouse，并具有共享存储和分离的计算，类似于 Neon。

### 房间里的大象

在 X 上，关于 Neon 有多糟糕的帖子层出不穷，这些帖子来自一小群拥有大量受众的大型帐户。 我个人认为，仅仅是观察这种消极情绪都令人厌倦，这种消极情绪似乎只是为了博取关注。 我理解其中很多是出于营销原因，而且确实有效。 但代价是什么？

就 Neon 可能存在的实际可靠性问题而言，我们相信这与 Neon Cloud 独特的负载模式有关，而不是根本的架构或代码质量问题。

在 Molnett，我们仍然像以往一样渴望运行 Neon。 没有其他选项采用相同类型的架构构建，因此无论如何我们都必须让它发挥作用！ 正如他们所说，要有切身利益。

### 工作原理

该 Operator 利用三个独立的 CRD（Cluster、Project、Branch）来部署运行完整集群所需的组件。 必须使用与 S3 兼容的对象存储、预先存在的 Postgres 实例和本地连接的磁盘（建议使用 NVMe）配置 Cluster 资源。 最终你会得到一个由 Safekeepers、Pageservers 和辅助组件组成的集群。

Project 和 Branch 资源（内部称为 Tenant 和 Timeline）等同于 Neon Cloud Project 和 Branch。 创建这些资源会导致生成一个功能齐全的 Postgres 实例，可以根据需要使用！

Operator 附带一个 API，该 API 直接与存储控制器（Neon 中的编排器）通信，以将新的时间线（分支）分配给特定的 Pageserver 和 Safekeeper。

如果发生节点故障，计算节点会自动配置为与一组可能新的 Pageserver 和 Safekeeper 通信。 这使得 Operator 能够管理分片和故障转移，而无需人工干预。

你可以在此处阅读有关架构的更多信息：<https://github.com/molnett/neon-operator/>

### 为什么选择 Rust 和 kube-rs

该 Operator 的目的是直接依赖于 `neondatabase/neon` 存储库的 API 客户端、protobuf 和其他类型。 今天这是不可能的，因为 Neon 没有发布他们的 crate，并且在 Cargo 中使用 git 依赖项是不可能的，因为他们有多个版本的 postgres 作为子模块。

我们计划向上游贡献一个解决方案，可能通过发布一些 crate。 对于这样的系统来说，不必复制或 vendor 代码以确保兼容性的好处不应被低估，因此我们将尽最大努力使其发挥作用。

但 Rust 可能不是最佳选择，这倒是真的。 kube-rs 的功能远不如 kubebuilder 丰富，没有 `envtest` 对集成测试来说是一个问题，**而且** Rust 出了名的难学。

几个月后，我们将看到 Rust 和 kube-rs 对我们有什么作用。 我们仍处于开发的早期阶段，因此我们乐于接受反馈和建议。

### 接下来是什么

我目前正在全职完成一个可用于生产的版本，这将使我们能够在 Molnett 将 Neon 部署到生产环境，并开始在实际环境中验证正确性和日常运维。

为了实现这个里程碑，我们将不得不实施以下改进：

* 一个通过控制平面配置数据库和用户的管理层
* Pageserver 的排空和填充操作
* 将 PGBouncer 与 Compute 一起部署以允许访问数据库
* 用于监控和警报目的的基本**可观测性**支持

### 寻找合作者

你是否正在寻找在本地部署 Neon 的方法？或者合作完成上述里程碑？请在 [X](https://X.com/jonathangrahl) 或 Discord @bittermandel 上联系我，或在 [GitHub](https://github.com/molnett/neon-operator) 上创建 issue。

如果你想试用 Molnett，可以在 <https://console.molnett.com> 上注册，我们会与你联系！
