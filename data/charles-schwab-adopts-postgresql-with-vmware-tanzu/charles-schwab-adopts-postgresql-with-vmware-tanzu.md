
<!--
title: Charles Schwab采用 PostgreSQL
cover: https://cdn.thenewstack.io/media/2024/09/8b061920-hegde.jpg
-->

作为 Charles Schwab 的分析师，其中一项好处是您可以一键启动一个新的 PostgreSQL 数据库。

> 译自 [Charles Schwab Adopts PostgreSQL (With VMware Tanzu)](https://thenewstack.io/charles-schwab-adopts-postgresql-with-vmware-tanzu/)，作者 Joab Jackson。

经纪公司[Charles Schwab](https://www.schwab.com/) 在[PostgreSQL](https://thenewstack.io/qa-how-enterprisedb-brings-five-nines-to-postgresql/) 中发现了价值：该公司已开始用这个开源系统替换一些专有的数据库管理系统。

想法是：当谈到关系型数据库时，它们现在都差不多。

经过50年的改进，关系型数据库已经相当成熟。Gartner 甚至不再费心为它们做魔力象限，[而是专注于分析云数据库](https://www.gartner.com/reviews/market/cloud-database-management-systems)。

因此，在成本效益方面——这显然是金融服务公司最关心的问题——从数据库中获得最大收益取决于总拥有成本 (TCO)。

Schwab 发现，开源 PostgreSQL 数据库系统的 TCO 低于专有模型，[Nataraj Hegde](https://www.linkedin.com/in/nataraj-hegde-12767417/)，Charles Schwab 数据库工程总监，在[Broadcom](https://broadcom-software.security.com/blogs/division/broadcom-software?utm_content=inline+mention) 的[VMWare Explore 2024](https://www.vmware.com/explore/us?utm_source=the+new+stack&utm_medium=referral&utm_campaign=event&utm_content=inline-mention) 上周的演讲中指出，该演讲详细介绍了 Schwab 用于审查该软件的过程。

![](https://cdn.thenewstack.io/media/2024/08/bda5a30f-novick-hegde-300x225.jpg)

*VMware 的 Ivan Novick（左）和 Schwab 的 Nataraj Hegde，VMWare Explore。（照片：TNS）*

这并不是说20世纪90年代早期由 [Michael Stonebreaker](https://thenewstack.io/dr-michael-stonebraker-a-short-history-of-database-systems/) 部分开发的 PostgreSQL，可以在没有企业支持的情况下，轻松地被放入嘉信理财监管复杂的领域。

这就是 Broadcom 的用武之地。作为该公司[VMware Tanzu 平台数据解决方案](https://tanzu.vmware.com/data) 的一部分，该公司维护着自己的企业级强化版 PostgreSQL，[Ivan Novick](https://www.linkedin.com/in/ivannovick/)，Tanzu 数据服务产品管理，Broadcom，加入了演讲。

## PostgreSQL 作为一项服务

“你一定想知道，为什么 Schwab 要运行 Postgres？”Hegde 问观众。Hegde 本身是 Oracle 认证大师，并且拥有许多其他 NoSQL 和 SQL 数据库系统的经验。

在 Schwab，Hegde 负责各种数据应用程序的路线图。该公司建立了一个集中管理的架构，数据库可以作为“平台服务”提供给内部用户。用户请求数据库并获得连接。

数据库团队负责所有底层配置位，例如架构、备份选项等等。

## 为什么选择 PostgreSQL
PostgreSQL 的流行程度正在爆炸式增长，[有可能超越](https://db-engines.com/en/ranking) 最流行的开源数据库 Oracle 的 MySQL，考虑到它们目前的轨迹。

“Postgres 在业界获得了很大的吸引力，越来越多的企业客户像我们一样，”Hegde 说。“一个主要原因是云。在云上，Postgres 正在成为事实上的 SQL 数据库。

数据库市场[预计](https://www.einpresswire.com/article/638376992/operational-database-management-market-size-worth-usd-80-26-billion-in-2028-at-a-cagr-of-5-2) 到 2028 年将增长到约 800 亿美元。在开源数据库方面，PostgreSQL [正在吞噬市场](https://medium.com/@fengruohang/postgres-is-eating-the-database-world-157c204dcfc4)。

![](https://cdn.thenewstack.io/media/2024/09/37c95ad3-schwab-postgres-01.jpg)

但总的来说，数据库技术正在成熟。

“一个关系型数据库与另一个关系型数据库之间没有真正的战略优势，”Hegde 说。PostgreSQL 已经与许多商业产品实现了同等水平，包括优化、索引策略以及对最新数据类型（如[JSON](https://thenewstack.io/an-introduction-to-json/) 和[向量](https://thenewstack.io/onehouse-automates-vector-embedding-for-its-data-lakehouse/)）的支持。

没有值得担心的差异化因素，从 Schwab 的角度来看，下一个要考虑的方面是 TCO。

PostgreSQL 是开源的，因此它没有供应商锁定（或讨厌的许可证审计）。

“不必为数据库支付许可证肯定降低了 TCO，但降低的 TCO 不仅仅是许可证，”Hegde 说。

PostgreSQL 也非常易于安装和维护。计算和存储运营成本也更低。“因为它很简单，所以你的运营成本更低，”他说。

因此，出于这些原因，Schwab 将 PostgreSQL 作为首选数据库。

![](https://cdn.thenewstack.io/media/2024/09/3a9e31aa-schwab-postgres-02.jpg)

## PostgreSQL 和高可用性

在 PostgreSQL 通过审查后，Schwab 仍然面临一些障碍才能完成上架，这些问题大约花了六个月的时间才解决。

总的来说，Schwab 在内部运行着大约 20,000 个应用程序。如果其他项目选择使用 PostgreSQL，它们也可以使用，因此它必须能够支持各种工作负载。

上架团队研究了 Schwab 如何使用其当前数据库，以识别 PostgreSQL 可能缺少的任何差距。他们发现，PostgreSQL 能够处理超过 90% 的银行当前工作负载。

高可用性 (HA) 是一个主要要求，Schwab 发现 PostgreSQL 可以提供与 Oracle 和 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) SQL Server 相同的 HA，只需一些额外的开源软件。

Hegde 说，大多数数据库供应商都有一些备份和恢复策略，但仅仅复制数据库副本是不够的。但仅仅进行完整备份是不够的。Schwab 需要进行时间点备份，这可以将数据库恢复到特定时间的状态。

在 Schwab，每个 PostgreSQL 数据库实际上都有四个备份副本，分布在三个不同的区域。它们由 [Patroni HA](https://patroni.readthedocs.io/en/latest/) 软件为 PostgreSQL 管理。

![Schwab 的高可用性架构。](https://cdn.thenewstack.io/media/2024/09/4fcf1b1f-schwab-postgres-04.jpg)

*Schwab 的高可用性架构。*


## PostgreSQL 的供应商支持

供应商支持是金融机构采用任何开源软件的另一个要求。

“在数据库方面，我们不希望在没有供应商支持的情况下运行开源软件，”Hegde 说。

当公司遇到重大问题时，仍然需要联系供应商以加快解决问题。

将 PostgreSQL 引入 Schwab 不仅仅是下载和安装数据库管理系统的副本。它必须作为一项服务提供给所有员工——这就是对安全、备份和其他高级功能的需求所在。

尽管是开源的，但 PostgreSQL 仍然有许多商业支持选项，包括来自 [EDB](https://www.enterprisedb.com/) 和 [Percona](https://www.percona.com/?utm_content=inline+mention) 的软件包。

Schwab 与 VMware 进行了咨询，VMware 提供了一个参考架构，该架构被用作起点。该公司有一个应用程序的集中式治理计划，因此部署必须达到这些里程碑。

PostgreSQL 的一个问题是，Schwab 将从互联网上的 [PostgreSQL](https://www.postgresql.org/) 下载软件。银行希望有一个更可靠的下载来源，只是为了确保来源 [不会被恶意行为者破坏](https://thenewstack.io/linux-xz-backdoor-damage-could-be-greater-than-feared/)。

“当我们与银行和政府机构打交道时，你需要对代码的源域有更多保护和保险，”Novick 解释说。

这个版本来自 [VMware Tanzu](https://tanzu.vmware.com?utm_content=inline+mention)，这是一个旨在简化企业开发过程的平台，它包括 [Tanzu 数据解决方案](https://tanzu.vmware.com/data)，它提供大约 20 个开源数据中心应用程序的 PaaS 就绪版本，包括 PostgreSQL。

VMware 通过 [Greenplum 并行数据库](https://thenewstack.io/pivotal-readies-the-greenplum-parallel-processing-database-for-kubernetes/) 进入了支持 PostgreSQL 的业务，Greenplum 是 [VMware 收购](https://thenewstack.io/vmware-acquires-pivotal-software-for-more-kubernetes-prowess/) 的 [Pivotal](https://thenewstack.io/pivotal-readies-the-greenplum-parallel-processing-database-for-kubernetes/) 的一部分，收购时间为 2020 年（Broadcom [收购](https://thenewstack.io/vmware-to-be-acquired-by-broadcom-in-a-61-billion-deal/) VMware 于 2023 年，Greenplum 被更名为 [VMware Tanzu Greenplum](https://tanzu.vmware.com/greenplum)）。Greenplum 最初是基于 PostgreSQL 构建的，因此 Pivotal/VMware 在 PostgreSQL 方面积累了丰富的专业知识，因此开始为客户提供“原始”版本的 PostgreSQL 也是顺理成章的事情，Novick 解释说。

VMware 获取这些应用程序的源代码，并在其自己的“构建农场”上编译它，以及它自己的其他开源代码。实际上，这些开源应用程序已经过 VMware 的审查。

## 总结

然后，这家银行公司尝试使用该软件来替换测试环境，并针对大量可能的测试用例对该软件进行压力测试。然后，一些早期采用者在生产环境中测试了该软件，这有助于识别任何操作差距。

目前，Schwab 运行着几个 PostgreSQL 应用程序，但它很快将加大力度，将更多应用程序从他们正在运行的专有数据库（如 Oracle）迁移过来。
这意味着在启动新项目时，团队将获得一个 PostgreSQL 实例来开始工作。该公司正在生成文档，以帮助其他内部应用程序（那些不需要某些商业数据库系统的专有扩展）的管理人员迁移到 PostgreSQL。

您可以[此处](https://www.vmware.com/explore/video-library/video/6360759651112)查看整个演示文稿。

![](https://cdn.thenewstack.io/media/2024/09/d9a0463a-schwab-postgres-03.jpg)

*披露：博通为记者参加此次会议支付了旅行/住宿费用。*
