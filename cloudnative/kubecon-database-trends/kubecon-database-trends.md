# KubeCon Europe 上发现的数据库趋势

翻译自 [Database Trends Spotted at KubeCon Europe](https://redis.com/blog/kubecon-database-trends/) 。

数据库供应商需要在云原生社区中变得更加活跃——特别是为了应对与 Kubernetes 和有状态应用程序相关的扩展问题。

容器化和 Kubernetes 继续革新云原生应用程序的开发和部署，主要是因为这些技术提供了增强的可扩展性、可移植性和灵活性。但是将数据库集成到这些环境中会带来一系列新的挑战。

我想说这些挑战正在被克服。但是，在参加了上周在阿姆斯特丹举行的 KubeCon + CloudNativeCon Europe 2023 之后，我不得不得出结论，我们距离解决这些问题还有很长的路要走。

## 结合无状态和有状态环境

数据库/容器问题都归结为关于[数据持久化和存储](https://redis.com/blog/importance-of-database-persistence-and-backups/)的问题。容器是短暂的。它们很容易创建、销毁和替换。虽然这对[无状态应用](https://developer.redis.com/operate/orchestration/kubernetes-operator/)程序有利，但它对依赖于数据库的有状态应用程序提出了重大挑战，而数据库又需要持久存储来维护数据完整性。

诚然，Kubernetes 提供[持久卷](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) (PV) 和持久卷声明 (PVC) 来为有状态应用程序提供[持久存储](https://redis.com/redis-enterprise/technology/durable-redis/)解决方案。 PV 和 PVC 允许数据库维护其数据，即使运行数据库的容器被替换或销毁。

但这还不够。这不是一个已解决的问题。

“我认为这是目前需要解决的最重要的问题之一，”Veritas 高级杰出工程师 Petter Sveum 在 KubeCon 小组讨论中说。 “市场上有许多不同的解决方案，但数据库规模仍然是一个真正的问题。”

“你有更大的工作负载被驱动到 Kubernetes 中，跨多个命名空间，甚至可能是多个站点的多个 TB 卷，”Sveum 指出。 “解决它需要对传统建筑中的细节进行大量关注。那么为什么它与 Kubernetes 有什么不同呢？”

相反，Sveum 遇到了几支真正感到惊讶的团队。他们会说，‘哦，我的 10 TB 卷无法在我预期的时间内创建快照！’他们不明白‘这并不快，对吧？这需要几分钟，几小时。'”

思科工程副总裁 Guillaume Savage de Saint Marc 同意 Sveum 的评估。 “在云原生环境中处理需要来自有状态和无服务器服务的组合资源的边缘计算是很尴尬的。”

数据库和云原生计算取得了进展。但归根结底，华为首席开源联络官任旭东表示，“目前还没有成熟的解决方案。”

## 数据库公司需要更多地参与云原生计算

每个人都同意 DBMS 供应商需要用 Kubernetes 做更多的事情。

“我们仍然依赖遗留的基础设施组件，而不是投资将其移植到 Kubernetes，”Sveum 说。在他看来，DBMS 保留在虚拟机 (VM) 和服务器中，并根据需要从 Kubernetes 编排的容器中调用。他断言，我们需要在 DBMS、容器和 Kubernetes 之间进行更多更好的集成。

这并没有阻止公司在容器中运行数据库。根据 [Data on Kubernetes](https://dok.community/) (DoK) 社区，许多组织已经在通过 Kubernetes operator 运行数据服务——使用自定义资源来管理应用程序及其组件的软件扩展。理想情况下，operator 将现实世界运营团队的知识和专业知识封装起来，并将其编码为软件。

注意到“自定义”这个不祥的词了吗？在 Kubernetes 上使用数据的首要问题是缺乏与现有工具的集成。正如 DoK 的一份报告所指出的那样，“在 Kubernetes 上运行数据的已知良好实践很少。”

Constantia 的 DoK 董事兼首席执行官 Melisa Logan 在 KubeCon DoK 小组讨论中总结了这一点。 “为了处理 Kubernetes 上数据工作负载的第 2 天操作，组织严重依赖 operator 。但它们带来了一些挑战，包括缺乏与现有工具的集成；与其他堆栈缺乏互操作性；不同程度的质量；和缺乏标准化。”

然而，根据 [2022 年 Kubernetes 数据报告](https://dok.community/wp-content/uploads/2022/10/DoK_Report_2022.pdf)，大多数人至少使用 20 个 operator 。 “对于那些评估他们的选择的人来说，挑战因选择而变得更加复杂； operator 的数量持续增长，Operator Hub 目前列出了 270 多家，”Logan 说。 “没有 operator 标准，最终用户怎么可能评估每个标准以了解它是否满足他们的需求？”显然，还有很多工作要做。

## 缺乏合格的技术人员

现在，要是有更多的人同时具备 Kubernetes 和数据库的资格就好了！这是 Kubernetes 用户经常听到的一句话，而不仅仅是那些使用数据库的人。没有足够的 Kubernetes 专业知识可供使用，更不用说了解 Kubernetes 的 DBA 了。

正如 Sveum 所说，“我们真正缺乏了解系统和基础架构、它们的实际执行方式以及他们如何利用自动化平台以及 Kubernetes 等堆栈的人员。”

我们需要能够成为开发团队之间粘合剂的人，他们提出宏伟的要求，然后期待平台交付。

## 哦，一些数据库相关的公告

这并不是说 Kubecon 没有数据库新闻。有一些公告。例如，思科推出了一个新的开源项目 [VMClarity](https://github.com/openclarity/vmclarity) ，用于保护云原生环境中的虚拟机。当然，VM 同时托管容器和 DBMS。

或者，一些数据库消息被狭义地实现。例如，[Fermyon Technologies](https://www.fermyon.com/) 通过其 [Fermyon Cloud Key Value Store](https://www.fermyon.com/blog/introducing-fermyon-cloud-key-value-store) 添加了本地有状态存储容量，这样，用户可以将非关系数据保存在键/值中，该键/值通过 WebAssembly 框架 [Spin](https://www.fermyon.com/spin) 可用于无服务器应用程序。开发人员可以对 DBMS（例如 Redis、PostgreSQL 或 MySQL）进行看似普通的 API 调用。当然，这只适用于 Fermyon 生态系统，但这仍然是一个有趣的进步。

Taken all-in-all, the message I got from KubeCon is that more work – much more work –  remains to be done with DBMSs and Kubernetes. Yes, you can do useful things today with stateful workloads and cloud-native computing. But it requires custom programming, which doesn’t scale well. Bridging this gap requires more effort both from the cloud-native and DBMS industries and communities.
总而言之，我从 KubeCon 上得到的信息是，DBMS 和 Kubernetes 仍有更多工作要做。是的，您现在可以使用有状态工作负载和云原生计算来做一些有用的事情。但它需要自定义编程，不能很好地扩展。弥合这一差距需要来自云原生和 DBMS 行业和社区的更多努力。

正如我们在 [Kubernetes 上运行 Redis](https://redis.com/redis-enterprise-software/redis-enterprise-on-kubernetes/) 中解释的那样，Redis 处于利用容器生态系统的数据库公司的前沿。