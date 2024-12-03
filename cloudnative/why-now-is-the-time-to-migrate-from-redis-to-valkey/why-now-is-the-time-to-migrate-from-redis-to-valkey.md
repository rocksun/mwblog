
<!--
title: 现在是将Redis迁移到Valkey的时机
cover: https://cdn.thenewstack.io/media/2024/11/128b3026-migration.jpg
-->

迁移的优势及如何实现无缝过渡

> 译自 [Why Now Is the Time to Migrate From Redis to Valkey](https://thenewstack.io/why-now-is-the-time-to-migrate-from-redis-to-valkey/)，作者 Chris Carter。

Redis 今年早些时候决定将其全球最受欢迎的 NoSQL 数据库从使其获得如此受欢迎程度的开源许可证转向其他许可证，这一决定迅速引发了强烈反响。几周之内，Redis 社区的原成员和主要的行业参与者——包括 [AWS](https://aws.amazon.com/?utm_content=inline+mention)、[Google](https://cloud.google.com/?utm_content=inline+mention) 和 [Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention)——都一致支持 [Valkey](https://valkey.io/) 作为 Redis 的分支，以及完全开源的替代品。

但是，这一变化也让团队不得不决定在 Redis 转变之后该如何选择。对于那些将 Redis 视为其数据层关键技术的团队来说，我的建议是迁移到 Valkey，并尽快[完成迁移](https://thenewstack.io/how-we-completed-a-massive-kafka-and-cassandra-migration/)。因为[Valkey 是 Redis 的一个分支](https://thenewstack.io/valkey-is-a-different-kind-of-fork/)，其代码库[最初与 Redis 完全相同](https://thenewstack.io/valkey-a-redis-fork-with-a-future/)，并且保持高度兼容。然而，随着时间的推移，这种兼容性将会降低。换句话说：Redis 到 Valkey 的迁移成本现在已经降到了最低点。

让我们来看一下团队关于他们潜在的 Valkey 迁移的一些核心问题，包括迁移的好处以及如何完成尽可能无缝的过渡。

## 如果你继续使用 Redis 会发生什么

鉴于 Redis 此前声明致力于保持解决方案完全开源——这一承诺并未兑现——用户应该预期该公司将根据自身目标做出任何对其有益的许可证变更。这意味着无法保证不会出现进一步的限制和成本，包括供应商和技术锁定，这在公司放弃[开源许可证](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/)的情况下往往会成为风险。

因此，目前使用 Redis 的团队应该为新的许可证和服务费用做好准备，并做好软件越来越迎合非自身优先事项的准备。类似的例子，例如 Elastic 和 MongoDB 等以前是开源软件的公司走上了 Redis 的道路，这些公司都将资源投入到闭源产品中，而它们的免费社区版本则逐渐衰落并失去了贡献者。可以合理地假设 Redis 也可能遵循或多或少类似的轨迹。

## 那么，为什么选择 Valkey？

纵观可用的 Redis 替代方案，Valkey 作为理想的开源内存数据存储和 Redis 社区的继承者脱颖而出——这在很大程度上是因为它实际上是该社区许多前成员和合作伙伴当前选择的解决方案。Valkey 继续使用相同的开源许可证和 Redis 用户熟悉的相同的单线程 C。其他替代方案，如 Garnet、Redict、KeyDB 和 DragonflyDB 则无法做到这一点。

随着主要的[像 AWS 这样的云提供商](https://thenewstack.io/aws-adds-support-drops-prices-for-redis-forked-valkey/)和 Google 支持 Valkey，组织也可以确信该项目将继续[满足他们的需求](https://thenewstack.io/valkey-whats-new-and-whats-next/)，以便在使用大规模云资源时高效可靠地运行。从技术角度来看，Valkey 当前的性能和可靠性特性与 Redis 相匹配，但这可能会随着两者朝着各自方向发展而发生变化。同时，Valkey 最大的吸引力在于消除了当前或未来的许可证成本，与未来闭源版本的 Redis 相比，它提供了更低的总拥有成本。

## 团队应该如何进行迁移到 Valkey？

作为 Redis 的一个分支，Valkey 在从 Redis 进行顺利且成功的企业迁移方面具有许多优势。Valkey 节点可以加入现有的 Redis 或 Valkey 集群，提供清晰的迁移路径，团队应该利用这一路径。

Redis 和 Valkey 还使用相同的命令行和 API 调用，使经验丰富的 Redis 用户易于迁移和操作。由于 Valkey 作为 Redis 的流行替代品而备受瞩目，因此组织还可以轻松利用托管支持选项，如果需要额外的迁移和优化专业知识（尤其是在大规模情况下）的话。

## Redis 和开源数据层技术的现状

从Elastic到MongoDB，再到Red Hat，现在又轮到Redis，许多数据公司都遵循了这样的路径：开发开源解决方案，然后转变商业模式，通过闭源许可和订阅来产生收入。

虽然一些公司在闭源模式下取得了成功，但这**种**开源软件的商业化也导致了利益冲突、社区参与度降低以及软件生态系统碎片化。

开源的未来取决于商业利益和社区驱动协作之间的平衡。此外，试图将开源软件商业化的组织需要与开源社区保持密切联系，并确保开放和协作的核心原则得到遵守。如果他们没有做到这一点，社区将介入，提供类似Valkey的解决方案来弥补这一差距。
