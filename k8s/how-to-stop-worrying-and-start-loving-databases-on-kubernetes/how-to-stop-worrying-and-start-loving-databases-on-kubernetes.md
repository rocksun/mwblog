
<!--
title: 如何在 Kubernetes 上停止担心并开始热爱数据库
cover: https://cdn.thenewstack.io/media/2024/10/6edf426e-love-databases-on-kubernetes.jpg
-->

如果在 Kubernetes 上运行数据库让你感到焦虑，那么你做错了。学习如何在 K8s 上创建健壮且有弹性的数据层。

> 译自 [How To Stop Worrying and Start Loving Databases on Kubernetes](https://thenewstack.io/how-to-stop-worrying-and-start-loving-databases-on-kubernetes/)，作者 Greg Nokes。

Kubernetes (K8s) 无疑改变了应用程序的部署和管理方式。它是云原生架构的基石。现代 DevOps 团队使用 [Kubernetes](https://roadmap.sh/kubernetes) 来编排高可用性 Pod、多区域故障转移以及跨数据中心分配应用程序负载。

然而，当谈到在 [Kubernetes 上运行数据库](https://thenewstack.io/how-to-run-databases-in-kubernetes/) 时，许多团队仍然犹豫不决。这种怀疑并非毫无根据；Kubernetes 曾经被认为不适合有状态应用程序，因为人们担心存储持久性、数据完整性和操作复杂性。在 Kubernetes 上运行数据库曾经被认为类似于

[BASE 跳伞](https://en.wikipedia.org/wiki/BASE_jumping)，但对 DevOps 来说。
幸运的是，时代变了。Kubernetes 已经改进。Kubernetes 生态系统已经发展壮大。曾经被视为大胆的 [Kubernetes Operator](https://thenewstack.io/kubernetes-when-to-use-and-when-to-avoid-the-operator-pattern/) 现在已经成熟且健壮。但是，并非所有实现都相同。因此，让我们深入探讨在 Kubernetes 上运行数据库的关键注意事项。

## Operator模式的兴起

Kubernetes 使用术语“Operator模式”来定义管理有状态工作负载的算法。在实现中，它可能被称为“Operator”或“Kubernetes Operator”或“Kubernetes 数据库Operator”。简而言之，Kubernetes Operator是一个代码库，它将操作知识封装到自动化任务中，这些任务管理 Kubernetes 上的有状态部署。自动化任务包括初始化高可用性、运行备份、恢复备份、健康检查和故障转移。

在 GitHub 上搜索将返回任何数据库的多个 Kubernetes Operator。在多个Operator和 Kubernetes 实现之间进行选择，任何两个在 Kubernetes 上运行数据库的团队在幸福感方面可能存在很大差异。

最好的 Kubernetes Operator在压力环境下具有最长的生产运行时间。随着时间的推移积累的经验不可低估。经验是胆大妄为的人如何找到边缘情况并编写代码来对其进行操作。在生产部署中找到 Kubernetes Operator上的新边缘情况将动摇对系统的信心。因此，寻找能够处理数据库细微差别并具有强大的生产时间记录的 Kubernetes Operator。

## Kubernetes 上数据库管理的要点

在容器中启动数据库很简单。操作生产数据库以确保数据完整性、可用性和性能需要一份清单。在选择 Kubernetes Operator时，请考虑以下因素：

- **备份**：数据是任何组织的生命线。定期可靠的备份是不可协商的。在 Kubernetes 环境中，将备份解决方案与对象存储服务（如 [Amazon](https://aws.amazon.com/?utm_content=inline+mention)S3）集成可以提供可扩展且持久的存储选项。自动备份计划、加密和恢复流程是健壮备份策略中要寻找的功能。
- **监控**：了解数据库的性能对于抢先解决问题至关重要。Kubernetes 提供了 Prometheus 和 Grafana 等工具用于监控。此外，数据库应公开其自身有意义且可操作的指标。这些指标应涵盖查询性能、资源利用率和延迟等方面。
- **灾难恢复**：灾难恢复计划确保您拥有在发生灾难性故障时恢复服务的计划。Kubernetes 跨集群管理工作负载的能力可以用于有效的灾难恢复策略。组织应定期测试恢复程序。
- **高可用性**：停机时间代价高昂（在财务和声誉方面）。Kubernetes 在部署高可用性环境时表现出色，从而防止单点故障。Kubernetes 通过 StatefulSets 和 ReplicaSets 支持这一点，从而能够运行数据库的多个实例，如果一个实例发生故障，这些实例可以无缝接管。
- **连接扩展**：随着用户群的增长，对数据库连接的需求也会增加。Kubernetes 擅长扩展无状态应用程序，但数据库需要周到的连接扩展策略。连接池和读取副本的横向扩展是减轻不断增加的负载而不会降低性能的工具。

## 云原生注意事项

这份清单与数据库本身一样古老。从云原生原则的角度来构建清单会稍微改变思维模式。复杂性会增加，但这也会创造机会。

- **磁盘存储解决方案**：花时间了解 Kubernetes 的[存储架构](https://thenewstack.io/storage/)。如果配置计算的选择是线性的，那么配置存储的选择就是一个矩阵。StatefulSets 管理持久卷，但选择正确的存储类会影响性能和可用性。在为数据库选择存储解决方案时，还需要考虑诸如每秒输入/输出 (IOPS)、延迟和冗余等因素。在 Kubernetes 上运行数据库时，将大部分时间花在规划存储需求上并不算过分。
- **备份和对象存储**：虽然上面的“存储”指的是数据库正在使用中的文件的性能，但对象存储是备份和事务日志的存放位置。将备份与对象存储服务集成可以降低成本并增强数据持久性。生产使用需要 Kubernetes 数据库操作员支持与现代对象存储的无缝集成。
- **易用性和可扩展性**：Kubernetes 的优势在于轻松扩展应用程序。现代 Kubernetes 数据库操作员可以轻松实现向上扩展（垂直扩展）、向外扩展（水平扩展）和向下扩展（在流量较低时）。通过 Kubernetes 操作员进行自动化将这些事件简化为标准化配置和 API 调用。
- **升级和维护**：运行更新和维护应该感觉很平常。Kubernetes 操作员可以促进滚动更新，从而最大限度地减少升级期间的停机时间。自动化简化了使用金丝雀部署进行测试的成本。这些测试降低了传统上与更新关键数据库系统相关的风险。

## 在 Kubernetes 上运行数据库是一条已知的路径

在 Kubernetes 上运行数据库不应该成为焦虑的来源——如果是，那就选择其他路线。正确的工具和实现为您的应用程序创建了一个强大且有弹性的数据层。

好消息是这条路是一条已知的路径，并且已经用代码铺平了道路。通过使用成熟的操作员踏上这段旅程，团队将建立在先前经验成功的基础上。目标很明确：让 Kubernetes 操作员来管理数据库；通过创新的应用程序为用户提供价值。

*有兴趣了解更多关于 Kubernetes 操作员的信息吗？在 11 月 12 日至 15 日的 KubeCon + CloudNativeCon 北美会议上，请到 Crunchy Data 展位 P8 与专家交谈或观看演示。*

*要了解更多关于 Kubernetes 和云原生生态系统的信息，请加入我们参加**KubeCon + CloudNativeCon 北美会议**，该会议将于 2024 年 11 月 12 日至 15 日在美国犹他州盐湖城举行。*
