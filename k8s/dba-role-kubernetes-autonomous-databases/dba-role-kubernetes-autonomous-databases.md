<!--
title: 为什么在自治数据库时代人类的需求不会消失
cover: https://cdn.thenewstack.io/media/2026/06/08e8ffe9-logan-voss-6fqt-gx3fos-unsplash-scaled.jpg
summary: Percona联合创始人指出，在自治数据库时代，DBA不会消失，而是会从日常运维的“机修工”转型为专注于数据结构的设计与治理的“架构师”，人类在安全和防厂商锁定上依然关键。
-->

Percona联合创始人指出，在自治数据库时代，DBA不会消失，而是会从日常运维的“机修工”转型为专注于数据结构的设计与治理的“架构师”，人类在安全和防厂商锁定上依然关键。

> 译自：[Why the need for humans won't disappear in the age of autonomous databases](https://thenewstack.io/dba-role-kubernetes-autonomous-databases/)
> 
> 作者：Chris J. Preimesberger

完全自治系统的承诺——在数据存储快速增长的情况下实现自我管理、自我修复和自我优化的数据库——对首席技术官（CTO）们来说极具诱惑力。但正如 [Percona](https://www.percona.com/) 联合创始人 [Vadim Tkachenko](https://www.linkedin.com/in/vadimtk) 上周向 *The New Stack* 解释的那样，现实要复杂得多：虽然自动化确实在改变数据格局，但人类的参与不仅依然相关，而且至关重要。

“我认为人类仍然需要运行数据库，”Tkachenko 告诉 *The New Stack*。“然而，数据的增长并没有放缓。这种转变并不是（DBA）角色的消失，而是其定义的重塑。”

![](https://cdn.thenewstack.io/media/2026/06/4ac4d0e3-vadim-tkachenko.jpg)

*Percona CTO兼联合创始人 Vadim Tkachenko。图片来源：Percona*

在加利福尼亚州山景城[计算机历史博物馆](https://computerhistory.org/)举行的公司 [Percona Live 2026 大会](https://thenewstack.io/percona-20-oursql-foundation-rebrand/)上，Tkachenko 预测道：“未来的数据库管理员将从专注于运行维护的‘机修工’，演变为专注于数据本身结构的‘架构师’。”

总部位于北卡罗来纳州达勒姆的 Percona 致力于开发广受欢迎的开源数据库软件并提供一系列可选服务，其在计算机历史博物馆（CHM）的活动上庆祝了公司成立20周年。为期三天的研讨会重点展示了解决当前工作负载问题的实用解决方案，来自 AWS、VMware、NEXTGRES 等机构的专家也在讨论中贡献了他们的专业见解。

> “未来的数据库管理员将从专注于运行维护的‘机修工’，演变为专注于数据本身结构的‘架构师’。”

日常繁琐的工作——目前消耗人类时间的打补丁、扩展和维护——将越来越多地由机器学习和 AI 代理来处理。Tkachenko 设想了一个未来，在那个未来，这些代理与数据库进行通信，不是通过历史悠久、人类可读的 SQL 标准，而是通过它们自己优化过的内部语言。

这一变化意味着人类的专业知识将转向战略性的、更高层次的关注点：确保数据完整性、定义访问模式和架构系统。人类的角色正从“管理”转变为“治理”。

这种自主的愿景与云原生基础设施的兴起密切相关，特别是涉及开源数据分发器 Kubernetes。对标准化、可移植控制平面的需求是实现真正数据库自主性和灵活性的技术基础。Kubernetes 抽象了底层基础设施，允许自动化工具使用一致的 API 和最佳实践，在任何环境（公有云、私有云或混合云）中管理数据库。

**Percona 与 Kubernetes 的关系**

Kubernetes 和 Percona（具体指 Percona Operator 和 Percona Monitoring and Management 应用）通过将容器编排与企业级数据库管理相结合，从而实现了相辅相成。Kubernetes 为数据库提供了可扩展、自愈的基础设施，而 Percona 则优化了数据库性能并自动化了生命周期管理，以确保可靠且高速的运行。

Kubernetes 如何让 Percona 受益：

* **自动扩展与编排：** Kubernetes 动态分配 CPU、内存和存储资源，使 Percona 数据库（如 [Percona XtraDB 集群](https://docs.percona.com/percona-xtradb-cluster/8.0/index.html)）能够即时扩展，以应对流量高峰。
* **自愈性故障转移：** 如果数据库节点发生故障，Kubernetes 会自动将 Pod 调度到健康的节点上。Percona 的 [Operators](https://docs.percona.com/percona-operator-for-mysql/pxc/index.html) 原生处理数据库重新加入的过程，从而防止宕机并维持持续的高性能。
* **一致性部署：** 利用 [Kubernetes StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) 和声明式 API，Percona 数据库可以在本地部署、混合云或多云设置中进行完全一致的部署，避免性能配置漂移。

Percona 如何让 Kubernetes 受益：

* **感知数据库的生命周期管理：** 标准的 [Kubernetes](https://kubernetes.io) 在原生管理有状态数据库方面存在困难。Percona Operators 弥补了这一差距，在 Kubernetes 生态系统内实现了诸如时间点恢复、滚动升级和集群备份等专业任务的自动化。
* **深度可观测性：** 借助 [Percona 监控与管理（PMM）](https://docs.percona.com/percona-monitoring-and-management/3/index.html)，数据库性能瓶颈可以直接与 Kubernetes 容器指标关联。PMM 提供了对查询执行时间的细粒度可视化，使 DBA 能够精准判断性能滞后是由数据库调优引起的，还是由于 Kubernetes 集群资源竞争造成的。
* **高性能开源调优：** Percona 发行版针对高需求、资源密集型的操作进行了高度优化。通过在 Pod 内部调整缓存和内存管理等设置，Percona 从 Kubernetes 环境中压榨出接近裸金属的运行速度。

## **可移植性防范厂商锁定**

由 Kubernetes 和 Percona 实现的可移植性的必要性，源于 Tkachenko 对厂商锁定的严厉警告。

> “如果你想继续支付公有云数据库的成本，或者你需要花费多少成本来进行迁移，又或者运行你自己的数据库需要多少成本，你都必须做出选择。”

对于许多公司而言，公有云数据库是一种便利，其功能像水力或电力等公共事业一样。然而，这种便利是以牺牲控制权为代价的。Tkachenko 表示，如果公有云服务商不断提高成本，用户就会陷入被动局面。

“如果你想继续支付公有云数据库的成本，或者你需要花费多少成本来进行迁移，又或者运行你自己的数据库需要多少成本，你都必须做出选择，”他说。

这就是开源基础设施变得至关重要的原因。在可移植平台上运行数据库，为摆脱专有云解决方案的高成本、高控制陷阱提供了一条出路。通过 Kubernetes 算子（Operators）部署、管理和移动自主数据库工作流的能力，确保了企业保留了话语权和独立性。

## **安全如何进入讨论视野**

关于自动化的讨论也必然涉及对安全的讨论。Tkachenko 警告说，自动化程度的提高并不等同于安全性的自然提升。他说，如果自动化流程不够健壮，可能会因为缺失必要的控制，而在无意中创造出新的攻击面。不健壮、自动化访问控制的复杂性所带来的风险，可能远远大于管理得当的人工流程。

对于 Percona 来说，它对独立性和健壮系统的承诺是立足之本。Tkachenko 表示，Percona 一直是自筹资金并保持独立的，从未接受过外部风投资本。这种独立性使该公司能够提供公正的建议，而不会旨在将客户锁定在单一的专有解决方案中。

最终，目标不是消灭人类，而是为他们配备更好的工具和独立的根基。这种方法得到了社区努力的支持，比如新成立的 [OurSQL 基金会](https://www.globenewswire.com/news-release/2026/05/27/3302305/0/en/oursql-foundation-launches-to-support-mysql-users-developers-and-companies.html)（Tkachenko 将其视为引导生态系统独立于任何单一厂商变动方向的必要补充），旨在确保开源数据世界的长期健康和稳定。

郑重声明，OurSQL 基金会的核心功能是为 MySQL 社区的参与者提供一个场所，以构建和部署使用 MySQL 或广泛兼容软件的应用，并与同行分享。它还旨在持续且透明地获取知识并提供关于未来发展的反馈。Tkachenko 上周向 Percona Live 大会的与会者表示，这家社区非营利机构支持 MySQL 作为开源数据库的增长和使用，并与包括 [Oracle](https://oracle.com) 在内的市场所有参与者合作，期望看到 MySQL 在下一代开发者和应用中取得成功。

自治数据库将继续处理生产中的琐碎事务，但人类利用像 Kubernetes 这样的标准化平台，将永远需要用来设计数据结构并维护工作流在道义和经济上的独立性。