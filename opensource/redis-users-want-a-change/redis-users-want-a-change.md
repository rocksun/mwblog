
<!--
title: Redis 用户希望改变
cover: https://cdn.thenewstack.io/media/2024/10/5612de29-redis-users-want-change.jpg
-->

Percona 研究发现，开源 Valkey 正在成为对 Redis 许可证变更感到担忧的 75% 公司的首选。

> 译自 [Redis Users Want a Change](https://thenewstack.io/redis-users-want-a-change/)，作者 Aleksandra Mitroshkina。

随着 Redis 最近的许可变更促使用户寻找其他选择，键值存储格局正经历着动荡。我们最新的 Percona 调查对这一趋势进行了更深入的探究，重点介绍了 Redis 许可变更对组织的影响，以及对流行的开源 Redis 分支 Valkey 的兴趣日益浓厚。

## Redis 许可变更：迁移的催化剂

Redis 今年早些时候转向 Redis 源代码可用许可证 (RSALv2) 和服务器端公共许可证 (SSPLv1)，这导致很多组织重新审视其数据库策略。由于担心许可成本和未来开源诱骗式排挤策略的潜在上升，IT 社区中的许多人在寻求其他能够提供类似功能并且没有相关风险、成本和供应商锁定的选项。

这种趋势的潜在影响是巨大的。

虽然 Redis 仍然是使用最多的键值存储，根据 DB Engines 和 Percona 调查，但一项引人注目的调查显示 75% 的 Redis 用户计划寻求其他选择。


![75% of survey respondents are looking for open-source Redis alternatives.](https://cdn.thenewstack.io/media/2024/10/0cd75424-planning-redis-migration2-1024x274.png)

*你认为 Redis 将代码库迁移至更严格的许可证有何看法？ *

AWS 工程师兼 Valkey 项目的维护人员 Madelyn Olson 表示，“Percona 的调查有助于强调 Valkey 项目的重要性，并说明我们社区主导的举措的力量。此调查突出了对 Redis 开源分支的需求，以及我们从不同规模和不同需求的公司那里获得的力量和动力。作为该项目的核心维护人员，我们将此视为 Valkey 作为 Redis 开源替代品的价值的标志。”

## Valkey：冉冉升起的新星

随着 Redis 的公告发布，Redis 的开源替代品 Valkey 快速成为领先的替代品。事实上，根据 Percona 调查显示，超过 63% 的受访者已经熟悉 Valkey - 自 Valkey 成立以来仅几周的时间里，这显示了很高的知名度。在这 63% 的受访者中，超过 75% 正在考虑将 Valkey 作为 Redis 功能的替代品。

当被要求分享寻求 Redis 替代品的原因时，受访者给出了以下理由：

- 许多受访者表示，Valkey 开源且受 Linux 基金会支持的特性在他们决定考虑它时起到了重要作用。
- 规模较大、更谨慎的组织计划在可能切换之前，先测试 Valkey。
- Redis 的长期用户计划评估 Valkey，但仍不确定所需的内部专业知识水平以及商用支持和托管服务的可用性。

计划继续使用 Redis 的受访者给出了以下原因：

- Redis 及其依赖关系在基础设施中的广泛使用意味着，尽管许可证发生了变化，但一些企业可能会继续使用 Redis。他们可能会考虑在未来的开发项目中使用 Valkey。
- 他们当前的 Redis 部署太大，现在无法迁移，但他们计划逐渐迁移到 Valkey。
- 一些人表示 Redis 一直是一项可靠的技术，他们认为花钱购买它是值得的。这些答复主要来自软件开发者，他们年复一年地在 Stack Overflow 调查中始终将 Redis 评为他们最喜爱的数据库之一。

按公司规模筛选后，来自小型、中小型企业的受访者表示，他们比中型市场、大型企业和企业组织更有可能尽快从 Redis 迁移。后三者当前正在测试替代方案并评估其选择，然后做出决定。

![54% of SMBs, 30% of mid-market companies, and 17% of large enterprises are considering migrating from Redis.](https://cdn.thenewstack.io/media/2024/10/ef142c0b-planning-redis-migration-company-size-1024x389.png)

*您对 Redis 将代码库迁移到限制性更强的许可证有什么看法？*

（按公司规模划分的答复）深入一级，大型企业组织是计划迁移至 Valkey 的最大的群体。这是可以理解的，因为许可变更的影响往往对于处理大量数据的组织而言更为重大。然而，由于潜在的停机时间和运营支持方面的考虑，这些组织往往会更慢地迁移到替代方案。

![77% 的中小企业、70% 的中型企业和 85% 的大型企业正在使用或考虑采用 Valkey。](https://cdn.thenewstack.io/media/2024/10/f9a5b32f-valkey-migration-1024x389.png)

*您是否已决定在您的组织中采用 Valkey？（按公司规模细分）*

为了加速采用，Valkey 社区和支持者应考虑提供必要的工具和服务，以确保平稳过渡到 Redis 替代方案。

## Valkey 支持选项需求

Redis 的社区支持基础设施使其能够作为开源项目蓬勃发展，吸引了多元的用户群并促进了快速增长。但对于计划在生产环境中使用 Redis 替代方案的组织来说，运营支持方面的考虑可能会影响采用速度。

调查显示了不同的支持策略：一些组织不确定内部支持需求；一些组织将等待 Valkey 的托管版本，而另一些组织将寻求外部支持。大多数组织（75.5%）计划使用第三方企业支持，而少数组织（24.55%）计划依靠内部团队或社区资源来维护 Valkey。

![75.5% 的受访者认为，在做出技术决策时，开源项目（如 Valkey）的外部供应商支持的可用性是一个重要因素。](https://cdn.thenewstack.io/media/2024/10/94ee23ab-redis-moving-to-restrictive-license-1024x558.png)

*您是否认为，在做出技术决策时，开源项目（如 Valkey）的外部供应商支持的可用性是一个重要因素？*

这是键值存储领域发展的一个关键时刻，随着组织寻求 Redis 的开源替代方案，Valkey 有望获得显著的吸引力。随着 [Valkey 继续发展](https://thenewstack.io/valkey-will-not-just-be-a-redis-retread/), 它满足组织多样化需求的能力，加上强大的商业支持，将对其在市场上的地位至关重要。

有关这些趋势的更多信息，您可以 [查看完整调查](https://learn.percona.com/hubfs/Collateral/Whitepapers/Adoption-Trends-Through-a-Valkey-Lens-WhitePaper.pdf)。
