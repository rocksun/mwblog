# Redis Users Want Change

![Redis Users Want Change Feature Image](https://cdn.thenewstack.io/media/2024/10/5612de29-redis-users-want-change-1024x576.jpg)

The key-value store landscape is undergoing a shakeup as [Redis](https://redis.com/?utm_content=inline+mention)'s recent licensing changes are prompting users to seek alternatives. Our [latest Percona survey](https://www.percona.com/resources/2024-valkey-adoption-report) delves deeper into this trend, highlighting the impact of Redis's licensing changes on organizations and the growing interest in [Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/), a popular open-source [Redis fork](https://thenewstack.io/valkey-is-a-different-kind-of-fork/).

## Redis Licensing Changes: A Catalyst for Migration

[Redis's move earlier this year](https://redis.io/blog/redis-adopts-dual-source-available-licensing/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) to the Redis Source Available License (RSALv2) and Server-Side Public License (SSPLv1) has led organizations to rethink their database strategies. Concerns about potential increases in licensing costs and future open-source "bait and switch" tactics are driving many in the IT community to seek alternatives that offer similar functionality without the associated risks, costs, and vendor lock-in.

The potential impact of this trend is significant.

While Redis remains the most widely used key-value store, according to [DB Engines](https://db-engines.com/en/ranking/key-value+store) and the Percona survey, a staggering 75% of surveyed Redis users are planning to seek alternatives.

![75% of survey respondents are looking for open-source Redis alternatives.](https://cdn.thenewstack.io/media/2024/10/0cd75424-planning-redis-migration2-1024x274.png)

What are your thoughts on Redis moving its codebase to a more restrictive license?

Madelyn Olson, an [AWS](https://aws.amazon.com/?utm_content=inline+mention) engineer and Valkey project maintainer, said: "Percona's survey helps highlight the importance of the Valkey project and illustrates the power of our community-driven initiative. This survey highlights the need for an open-source fork of Redis and the strong momentum and traction we're getting from companies of different sizes and needs. As a core maintainer of the project, we see this as a sign of Valkey's value as an open-source alternative to Redis."

## Valkey: A Rising Star

Following Redis's announcement, Valkey, an open-source alternative to Redis, quickly emerged as a leading alternative. In fact, according to the Percona survey, over 63% of respondents were already familiar with Valkey—a remarkable level of awareness considering Valkey was only a few weeks old. Of those 63%, over 75% are considering Valkey as a replacement for Redis functionality.

When asked about their reasons for seeking Redis alternatives, respondents provided the following answers:

- Many respondents said Valkey's open-source, [Linux Foundation-backed](https://thenewstack.io/linux-foundation-forks-the-open-source-redis-as-valkey/) nature played a significant role in their decision to consider it.
- Larger, more cautious organizations plan to test Valkey before making a possible switch.
- Long-time Redis users plan to evaluate Valkey but are still unsure about the level of internal expertise required, as well as the availability of commercial support and managed services.

Respondents who plan to continue using Redis shared the following reasons:

- Redis's widespread use in their infrastructure and its dependencies mean some enterprises may continue using Redis despite the licensing changes. They may consider Valkey for future development projects.
- Their current Redis deployments are too large to migrate immediately, but they plan to migrate to Valkey gradually.
- Some said Redis is a reliable technology, and they believe paying for it is valuable. These responses primarily came from software developers who consistently rank Redis as one of their favorite databases year after year in the [Stack Overflow survey](https://survey.stackoverflow.co/2024/technology#2-databases).

When filtered by company size, respondents from micro, small, and medium-sized businesses said they are more likely to migrate from Redis faster than mid-market, large, and enterprise organizations. The latter three are currently testing alternatives and evaluating their options before making a decision.

![54% of SMBs, 30% of mid-market companies, and 17% of large enterprises are considering migrating from Redis.](https://cdn.thenewstack.io/media/2024/10/ef142c0b-planning-redis-migration-company-size-1024x389.png)

What are your thoughts on Redis moving its codebase to a more restrictive license? (Responses broken down by company size)
深入挖掘，大型企业组织是计划迁移到 Valkey 的最大群体。这是可以理解的，因为许可证变更的影响对于处理大量数据的组织来说往往更大。然而，由于潜在的停机时间和运营支持方面的考虑，这些组织往往会更缓慢地迁移到替代方案。

![77% 的中小企业、70% 的中型企业和 85% 的大型企业正在使用或考虑采用 Valkey。](https://cdn.thenewstack.io/media/2024/10/f9a5b32f-valkey-migration-1024x389.png)
您是否已决定在您的组织中采用 Valkey？（按公司规模细分）

为了加速采用，Valkey 社区和支持者应考虑提供必要的工具和服务，以确保平稳过渡到 Redis 替代方案。

## Valkey 支持选项需求
Redis 的社区支持基础设施使其能够作为开源项目蓬勃发展，吸引了多元的用户群并促进了快速增长。但对于计划在生产环境中使用 Redis 替代方案的组织来说，运营支持方面的考虑可能会影响采用速度。

调查显示了不同的支持策略：一些组织不确定内部支持需求；一些组织将等待 Valkey 的托管版本，而另一些组织将寻求外部支持。大多数组织（75.5%）计划使用第三方企业支持，而少数组织（24.55%）计划依靠内部团队或社区资源来维护 Valkey。

![75.5% 的受访者认为，在做出技术决策时，开源项目（如 Valkey）的外部供应商支持的可用性是一个重要因素。](https://cdn.thenewstack.io/media/2024/10/94ee23ab-redis-moving-to-restrictive-license-1024x558.png)
您是否认为，在做出技术决策时，开源项目（如 Valkey）的外部供应商支持的可用性是一个重要因素？

这是键值存储领域发展的一个关键时刻，随着组织寻求 Redis 的开源替代方案，Valkey 有望获得显著的吸引力。随着 [Valkey 继续发展](https://thenewstack.io/valkey-will-not-just-be-a-redis-retread/), 它满足组织多样化需求的能力，加上强大的商业支持，将对其在市场上的地位至关重要。

有关这些趋势的更多信息，您可以 [查看完整调查](https://learn.percona.com/hubfs/Collateral/Whitepapers/Adoption-Trends-Through-a-Valkey-Lens-WhitePaper.pdf)。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)