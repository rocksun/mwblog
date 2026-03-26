<!--
title: Fivetran 捐赠 SQLMesh 给 Linux 基金会，深度拥抱开源数据
cover: https://cdn.thenewstack.io/media/2026/03/8b29e7c0-getty-images-lzwee7oe3tm-unsplash-scaled.jpg
summary: Fivetran 将其开源数据转换框架 SQLMesh 捐赠给 Linux 基金会。此举旨在支持开放数据基础设施，并可能与 dbt Labs 的许可策略调整有关，展现了 Fivetran 对数据开源生态的承诺。
-->

Fivetran 将其开源数据转换框架 SQLMesh 捐赠给 Linux 基金会。此举旨在支持开放数据基础设施，并可能与 dbt Labs 的许可策略调整有关，展现了 Fivetran 对数据开源生态的承诺。

> 译自：[Fivetran donates its SQLMesh data transformation framework to the Linux Foundation](https://thenewstack.io/fivetran-donates-sqlmesh-lf/)
> 
> 作者：Frederic Lardinois

[Fivetran](https://www.fivetran.com)，这家以其数据移动平台而闻名的公司，周三宣布将把其开源数据转换框架 SQLMesh 捐赠给 Linux 基金会。支持该项目厂商中立治理的其他创始成员包括 ATOMS（Uber 创始人 Travis Kalanick 的 CloudKitchens-到-机器人技术转型）、Benzinga、Harness、Infinite Lambda、Jump AI 和 Minerva。

SQLMesh 允许数据团队定义、测试和部署其基于 SQL 的数据转换。该项目于 2025 年 9 月归属于 Fivetran，当时该公司收购了由兄弟（前世界纪录速魔方玩家）[Toby](https://en.wikipedia.org/wiki/Toby_Mao) 和 [Tyson](https://en.wikipedia.org/wiki/Tyson_Mao) Mao 以及 Iaroslav Zeigerman 创立的初创公司 Tobiko Data。

该公司选择在此日期捐赠 SQLMesh 绝非巧合，因为该项目[在一年前的同一天将其基于 SQLMesh 的云服务全面推出](https://thenewstack.io/tobiko-launches-its-sqlmesh-based-cloud-service-into-ga/)。

## SQLMesh 与 dbt

SQLMesh 团队从不回避将 SQLMesh 与 dbt Labs 的开源数据转换工具 dbt 进行比较。在其 GitHub 页面上，SQLMesh 将自己描述为“不仅仅是 dbt 的替代品”。

![](https://cdn.thenewstack.io/media/2026/03/8fca5e60-architecture_diagram-1024x459.png)

SQLMesh 的主要区别在于它使用虚拟数据环境来运行开发、测试和生产环境而无需复制数据，以及其编译时 [SQLGlot](https://sqlglot.com/sqlglot.html) 解析器和优化器，这些都带来了显著的性能提升。

故事的转折点是，Fivetran 于 2025 年 10 月宣布计划与 dbt Labs 合并（尽管交易尚未完成）。

2025 年中，dbt Labs 为其下一代 dbt 引擎 Fusion 采用了 Elastic 许可证。该许可证保持源代码开放，主要侧重于确保其他公司不能在其平台上提供托管版本的 Fusion。当时，Toby Mao [批评](https://www.tobikodata.com/blog/dbt-fusion-death-of-dbt-core)了这一举动，认为“分析工程师应该拥有一个免费、开放且持续发展的转换平台。”

今天的举动很难不被视为对此次许可讨论的部分回应，因为 Fivetran 现在可以很容易地辩称它正在支持一个完全开源的 dbt 替代品，并将其回馈给社区。dbt core 目前在 GitHub 上有 12,500 颗星，而 SQLMesh 有 3,000 颗。

Fivetran 首席产品官 Anjan Kundavaram 表示：“当数据基础设施的核心组件是开放的时候，它的运作效果最好。随着分析和人工智能工作负载变得越来越复杂，组织需要灵活性来选择最佳技术，控制成本，并随着时间的推移调整其架构。SQLMesh 反映了我们的一种信念，即转换层应通过开放协作发展，作为更广泛的开放数据基础设施方法的一部分。”