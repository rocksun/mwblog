
<!--
title: Valkey 8.1的性能提升颠覆了内存数据库
cover: https://cdn.thenewstack.io/media/2024/08/ec9588da-valkey.png
summary: Redis开源替代方案Valkey 8.1发布！多线程架构带来3倍性能提升，内存占用减少20%。采用Rust重构核心引擎，引入Swiss Tables优化键值存储，显著提升内存效率。Valkey致力于成为高性能分布式数据库，欢迎加入GitHub社区！
-->

Redis开源替代方案Valkey 8.1发布！多线程架构带来3倍性能提升，内存占用减少20%。采用Rust重构核心引擎，引入Swiss Tables优化键值存储，显著提升内存效率。Valkey致力于成为高性能分布式数据库，欢迎加入GitHub社区！

> 译自：[Valkey 8.1's Performance Gains Disrupt In-Memory Databases](https://thenewstack.io/valkey-8-1s-performance-gains-disrupt-in-memory-databases/)
> 
> 作者：Steven J Vaughan-Nichols

加利福尼亚州，纳帕 — 一年前，[Redis 宣布](https://redis.io/blog/redis-adopts-dual-source-available-licensing/)它将放弃开源的 [BSD 3-clause license](https://opensource.org/license/bsd-3-clause) ，转而采用“源代码可用”的 [Redis in-memory key-value database](https://devops.com/redis-labs-extends-reach-of-in-memory-database/) [Redis Source Available License](https://redis.com/legal/rsalv2-agreement/) (RSALv2) 和 [Server Side Public License](https://redis.com/legal/server-side-public-license-sspl/) (SSPLv1)。

这一举动激怒了许多 Redis 开发者和用户。因此，心怀不满的开发者 [fork 了一个新项目 Valkey](https://thenewstack.io/linux-foundation-forks-the-open-source-redis-as-valkey/)，作为“Redis 内存 NoSQL 数据存储的开源替代方案”。现在，很明显，这已经成为一个非常成功的 fork。

有多成功？根据 [Percona](https://www.percona.com/?utm_content=inline+mention) 的一份研究报告，“[75% 的 Redis 用户正在考虑由于最近的许可变更而进行迁移](https://www.percona.com/resources/2024-valkey-adoption-report)。……在那些考虑迁移的用户中，超过 75% 的人正在测试、考虑或已经采用了 [Valkey](https://valkey.io/)。” 也许更有说服力的一点是，像 [Redisson 这样的第三方 Redis 开发公司，正在同时支持 Redis 和 Valkey。](https://redisson.org/)

## 多线程和可扩展性

不过，吸引人的不仅仅是许可变更。[Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/) 在 [Linux Foundation Member Summit](https://events.linuxfoundation.org/lf-member-summit/) 上，[Madelyn Olson](https://www.linkedin.com/in/madelyn-olson-valkey) 是 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) (AWS) 的首席软件工程师和 [Valkey](https://valkey.io/) 项目维护者，她在主题演讲中表示，由于 Valkey 采用了增强的多线程和可扩展性功能，因此速度更快。

Olson 补充说，这不是 [最初的计划](https://thenewstack.io/valkey-will-not-just-be-a-redis-retread/)。“我们希望保持 Redis 项目的开源精神，但我们也希望其价值不仅仅是一个 fork。我们在西雅图组织了一次贡献者峰会，我们将开发人员和用户聚集在一起，试图弄清楚这个新项目应该是什么样子。当时，我真的希望我们只关注缓存，这是 Redis 开源服务的主要工作负载。我们从用户那里听到的是，他们想要更多。他们希望 Valkey 成为适用于各种分布式工作负载的高性能数据库。因此，尽管这会给项目增加很多复杂性，但新的核心团队还是承担了这一重任，我们试图为我们的社区构建它。”

他们成功了。到 2024 年 8 月，Linux 内核开发人员和长期开源领导者 [Dirk Hohndel](https://www.linkedin.com/in/dirkhohndel/) 表示，[Valkey 8.0 通过更复杂的多线程 I/O 操作方法重新设计了 Redis 的单线程事件循环线程模型](https://thenewstack.io/valkey-is-a-different-kind-of-fork/)，这使他的性能“大约提高了三倍，而且我每天传输大量数据，6000 万个数据点”。此外，使用 Valkey 8，他看到单独的缓存表的大小减少了约“20%。当您在 Amazon Web Services 上谈论 TB 级或更多时，这确实可以节省大小和资金。”

回到现在，Olson 补充说：“在过去的几个月中，我们通过在核心中添加 Rust 以提高内存安全性，从而极大地改进了核心引擎。我们一直在更改集群模式的工作方式的内部算法，以提高可靠性并缩短故障转移时间。我们还在大幅更改内部数据结构的工作方式，因为它们基于 10 年前的软件，因此它们可以更好地利用现代硬件。”

此外，开发团队从头开始重建了键值存储，以更好地利用基于 Google 的所谓 [Swiss Tables](https://abseil.io/about/design/swisstables) 完成的工作的现代硬件。Olson 继续说道：“在短短几周内，我们将发布这些改进，作为 [Valkey 8.1](https://github.com/valkey-io/valkey/releases) 的一部分，这恰好是该项目成立一周年。” 这个新版本包括高达 20% 的内存效率提升（缓存系统中最常见的瓶颈）和最先进的数据结构。

展望未来，Valkey 计划引入更多多线程性能改进、一个高度可扩展的集群系统以及对数据类型的新核心更改。你觉得怎么样？该项目仍然对新的贡献者开放，并邀请感兴趣的各方通过 [GitHub](https://github.com/valkey-io/valkey) 加入。