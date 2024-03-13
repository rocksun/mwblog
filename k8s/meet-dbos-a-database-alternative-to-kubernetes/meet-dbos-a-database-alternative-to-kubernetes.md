
<!--
title: 认识 DBOS：Kubernetes 的数据库替代方案
cover: https://cdn.thenewstack.io/media/2024/03/633f0359-dbos.png
-->

PostgreSQL 的创建者与 Apache Spark 的创建者合作，在分布式数据库之上构建了一个云操作系统，旨在提供比当今广泛使用的 Linux/K8s 组合更好的安全性，更低的管理复杂性。

> 译自 [Meet DBOS: A Database Alternative to Kubernetes](https://thenewstack.io/meet-dbos-a-database-alternative-to-kubernetes/)，作者 Joab Jackson。

图灵奖得主 [迈克·斯通布雷克博士(Mike Stonebraker)](https://www2.eecs.berkeley.edu/Faculty/Homepages/stonebraker.html) 一直在发明数据库。四十年前，是 [第一个关系系统 Ingress](https://thenewstack.io/dr-michael-stonebraker-a-short-history-of-database-systems/)，三十年前，是 [PostgreSQL](https://thenewstack.io/postgresql-15-merge-ahead/)，最近，他联合创建了一个内存事务数据库系统 [VoltDB](https://thenewstack.io/voltdb-adds-geospatial-support-cross-site-replication/)。

现在，他带着一个旨在取代整个云原生计算堆栈的数据库系统回来了， [DBOS](https://www.dbos.dev/)（数据库操作系统）。

Linux [太老了](https://thenewstack.io/linus-torvalds-remembers-the-days-before-open-source-2/)，而 [Kubernetes](https://thenewstack.io/managing-kubernetes-complexity-in-multicloud-environments/) [是](https://thenewstack.io/developer-portals-can-abstract-away-kubernetes-complexity/) [太](https://thenewstack.io/dont-let-kubernetes-complexity-stall-your-cloud-momentum/) [复杂](https://thenewstack.io/how-to-fight-kubernetes-complexity-fatigue/)，这项工作的初创公司宣称。现在，一个数据库被设计出来取代所有这些。

为了实现这一愿景， [DBOS, Inc.](https://www.dbos.dev/) 已在由 [Engine Ventures](https://engineventures.com/) 领投的种子轮融资中筹集了 850 万美元，其他参与者包括 [Construct Capital](https://constructcap.com/)、[Sinewave](https://sinewave.vc/) 和 [GutBrain Ventures](https://www.gutbrainventures.com/)。

该项目由Stonebraker博士与 [Apache Spark](https://thenewstack.io/matei-zaharia-qa/) 创建者（以及 [Databricks](https://thenewstack.io/databricks-sees-and-raises-snowflake-with-gen-ai-llmops-more/) 联合创始人兼首席技术官 [Matei Zaharia](https://people.eecs.berkeley.edu/~matei/)) 以及麻省理工学院和斯坦福大学计算机科学家的联合团队共同创立。

DBOS [在高性能分布式数据库之上运行操作系统服务](https://docs.dbos.dev/)。所有状态、日志和其他系统数据都存储在可访问 SQL 的表中。

创建者声称，结果是一个可扩展、容错且具有网络弹性的[无服务器](https://www.thenewstack.io/serverless)计算云，适用于云原生应用程序。

通过在分布式数据库之上运行操作系统，您可以获得容错性、多节点扩展和状态管理。可观察性和安全性变得更容易。容器和编排层不复存在。

Stonebraker说：“你编写的代码更少，因为操作系统为你做了更多的事情。”

如今，分布式系统主要构建在旨在在单服务器上运行的操作系统（Linux）之上。这导致基础设施堆栈（应用程序数据、身份验证系统、消息传递、集群管理）中需要管理的变量状态数量惊人。

这种分散的特性当然需要大量的观察工具和安全工具，因为所有状态都为恶意黑客提供了肥沃的用武之地。

什么可以轻松处理一百万个状态？当然是一个数据库。

![](https://cdn.thenewstack.io/media/2024/03/2d6bddec-dbos-1024x571.png)

在 DBOS 设计中，高性能分布式 OLTP 将实现一套操作系统服务。它将在一个最小操作系统内核上运行，支持内存管理、设备驱动程序、中断处理程序和字节管理的基本任务。

## 一个数据库来统治所有数据库

这不是第一次提出这个想法：早在 2001 年，我们就记得拉里·埃里森认为中间件是一个“ [白痴想法](https://www.washingtontechnology.com/2001/07/oracle-battles-the-middleware/345552/)”，所有内容都应该由数据库本身管理。

这个 DBOS 项目背后的核心思想源于一个简单的想法：跟踪操作系统状态应该是一个数据库问题，Stonebraker博士说。

这个想法来自 Zaharia 的一次演讲。他指出，Databricks 的 Apache Spark 云服务通常一次管理一百万个子任务。所有状态和调度信息都跟踪在 PostgreSQL 数据库中，其缓慢的性能让 Databricks 的管理团队感到沮丧。

数据库瓶颈可以很容易地解决。事实上，这就是 [VoltDB 的全部意义所在](https://github.com/VoltDB/voltdb)，并发 [符合 ACID](https://thenewstack.io/an-apache-cassandra-breakthrough-acid-transactions-at-scale/) 的事务处理，可以跨多个服务器分布。

昔日，Stonebraker 博士是 PDP 11/40 上 Unix 的早期用户，拥有 48k 主内存和 25MB 磁盘内存。那时，所有状态都由 Unix 本身保存。当然，与 PDP 相比，百万个状态是一个跳跃了六个数量级的变化。但 Stonebraker 博士说，“操作系统必须跟踪的状态量基本上与资源成正比”。

DBOS 本身在麻省理工学院的 [SuperCloud](https://supercloud.mit.edu/) 上进行了测试，拥有超过 32,000 个处理器、数 TB 的主内存和更多 TB 的辅助存储。

堆栈的底部是一个分布式事务数据库系统，其上构建了文件系统、调度引擎和消息系统。

研究人员在 [2023 年超大规模数据库会议](https://vldb.org/2023/?program-schedule) 上讨论了该堆栈，并在一组论文中详细介绍了这项工作，涵盖了 ACID [事务](https://www.vldb.org/pvldb/vol16/p2742-kraft.pdf) 和 [系统重放](https://www.vldb.org/pvldb/vol16/p3085-li.pdf)。

Stonebraker 博士将 Linux 标记为“泄漏”，这意味着有 [多种方式](https://thenewstack.io/leaky-vessels-vulnerability-sinks-container-security/) 可以 [引入安全漏洞](https://thenewstack.io/zero-day-vulnerabilities-can-teach-us-about-supply-chain-security/)。此外，在数据库之上构建操作系统将提供回滚到漏洞被利用之前状态的能力（可以将其视为 [Apple Time Machine](https://support.apple.com/en-us/104984)，但适用于服务器）。

Stonebraker 博士说，集中式数据库还有助于调试。将应用程序分解为微服务 [使得它们非常难以调试](https://thenewstack.io/return-of-the-monolith-amazon-dumps-microservices-for-video-monitoring/)，甚至难以在每次测试中显示出不合理的行为（这些行为被称为“ [Heisenbugs](https://thenewstack.io/an-amazon-anomaly-that-metastasized-into-a-server-eating-monster/)”）。

Stonebraker 博士说：“我们以事务方式运行所有微服务。因此，并行微服务由我们的并发控制系统进行排序，基本上，要么没有 Heisenbugs，要么它们更难运行。”

最初，该系统是在 VoltDB 上模拟的，但支持者希望使用开源键值系统，因此他们选择了 [FoundatiolDB](https://www.foundationdb.org/) 作为基础。（Stonebraker 博士承认，任何与 PostgreSQL 线路兼容的分布式 OLTP 系统都可以使用，例如 [CockroachDB](https://www.cockroachlabs.com?utm_source=tns&utm_medium=sponsor&utm_campaign=brand-pipe-tns-sponsor-page-description&utm_content=lp-homepage-learn-more&utm_term=prosp&utm_content=inline-mention)）。

## DBOS Cloud：用于事务支持的分布式数据库

围绕 DBOS Cloud 构建的第一项商业服务是事务功能即服务 (FaaS) 平台，在这次初始发布中可供开发人员使用。

DBOS 运行在 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline-mention) 的 [Firecracker](https://thenewstack.io/aws-wants-its-open-source-firecracker-to-become-faster/) 上，最初可供开发人员通过今天发布的 DBOS Cloud 体验。

DBOS Cloud 是一个由 DBOS 操作系统支持的事务性无服务器应用程序平台，可用于构建和运行无服务器函数、工作流和应用程序。可以将其视为 [AWS Lambda](https://thenewstack.io/going-serverless-on-aws-lambda-recognize-potential-risks/)，但具有事务支持。

![](https://cdn.thenewstack.io/media/2024/03/013ae632-dbos-image-1-jpeg.jpg)

*DBOS 使容错 TypeScript 代码的创建变得更加容易，运行成本也更低（DBOS）。*

**该服务提供以下好处：**

- 支持有状态函数和工作流
- 内置容错，保证仅执行一次
- 时光旅行调试
- 可通过 SQL 访问的可观察性数据
- 启用网络攻击自检测和自恢复

[GitHub 存储库](https://www.dbos.dev/) 包含该公司开发的一些工具，包括用于与 DBOS 交互的 [TypeScript 框架](https://github.com/dbos-inc/dbos-ts) 和用于 VSCode 的“ [时光旅行调试器”](https://github.com/dbos-inc/#:~:text=DBOS%20Time%20Travel%20Debugger%20extension%20for%20VS%20Code) 。

![](https://cdn.thenewstack.io/media/2024/03/0f1ac164-dbos-image-2jpeg.jpg)

*DBOS Cloud 保留了代码和数据处理的完整审计跟踪，并将其存储在加密的 SQL 表中。DBOS Cloud 时光旅行调试器允许重放和检查该数据以解决问题、确保法规遵从性或查找欺诈等。（DBoss）*
