# Redis Users Want a Change
![Featued image for: Redis Users Want a Change](https://cdn.thenewstack.io/media/2024/10/5612de29-redis-users-want-change-1024x576.jpg)
The key-value store landscape is experiencing a shake-up, as [Redis](https://redis.com/?utm_content=inline+mention)’ recent licensing changes have driven users to search for alternatives. Our [latest Percona survey](https://www.percona.com/resources/2024-valkey-adoption-report) looks deeper into this trend, highlighting the impact of Redis’ licensing changes on organizations and the growing interest in [Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/), a popular open source [Redis fork](https://thenewstack.io/valkey-is-a-different-kind-of-fork/).

## Redis Licensing Changes: A Catalyst for Migration
[Redis’ shift](https://redis.io/blog/redis-adopts-dual-source-available-licensing/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) to the Redis Source Available License (RSALv2) and Server Side Public License (SSPLv1) earlier this year has caused organizations to rethink their database strategies. Concerned about potential increases in licensing costs and future open source bait-and-switch tactics, many in the IT community are seeking alternatives that offer similar functionality without the associated risks, costs and vendor lock-in.
The potential impact of this trend is huge.

While Redis remains the dominant key-value store in use, according to both [DB Engines](https://db-engines.com/en/ranking/key-value+store) and the Percona survey, a striking 75% of surveyed Redis users are planning to seek an alternative.

![75% of survey respondents are looking for open source Redis alternatives.](https://cdn.thenewstack.io/media/2024/10/0cd75424-planning-redis-migration2-1024x274.png)
What do you think about Redis moving the codebase to a more restrictive license?

Madelyn Olson, [AWS](https://aws.amazon.com/?utm_content=inline+mention) engineer and Valkey project maintainer, said, “Percona’s survey helps underscore the importance of the Valkey project and illustrates the strength of our community-led initiative. This survey highlights the need for an open source fork of Redis and the strength and momentum we are gathering from companies of varying sizes and needs. As a core maintainer of the project, we see this as a sign of Valkey’s value as the open source alternative to Redis.”

## Valkey: A Rising Star
Following Redis’s announcement, Valkey, an open source alternative to Redis, quickly emerged as a leading alternative. In fact, according to the Percona Survey, more than 63% of respondents were already familiar with Valkey — a remarkable level of awareness given that it had only been a few weeks since Valkey’s inception. And of that 63%, more than 75% are considering Valkey as an alternative to Redis’ functionality.

When asked to share their reasons behind seeking a Redis alternative, the respondents offered the following:

- Many respondents indicated that the open source,
[Linux Foundation-supported](https://thenewstack.io/linux-foundation-forks-the-open-source-redis-as-valkey/)nature of Valkey played a significant role in their decision to consider it. - Larger, more cautious organizations plan to test Valkey before making a possible switch.
- Long-term Redis users plan to evaluate Valkey but remain uncertain about the level of in-house expertise needed, as well as the availability of commercial support and managed services.
The respondents who plan to continue to use Redis shared the following reasons why:

- The widespread use of Redis and its dependencies in the infrastructure mean some enterprises will likely continue using Redis despite licensing changes. They may consider Valkey for future development projects.
- Their current Redis deployment is too large to migrate right now, but they plan to migrate to Valkey gradually.
- Some say Redis has been a reliable technology, and they see the value in paying for it. These responses mostly came from software developers, who have consistently named Redis one of their most loved databases in
[Stack Overflow Surveys](https://survey.stackoverflow.co/2024/technology#2-databases)year after year.
When filtering by company size, those from micro, small- and mid-size businesses stated they are more likely to migrate from Redis sooner than midmarket, large and enterprise organizations. The latter three are currently testing alternatives and evaluating their options before making a decision.

![54% of SMBs, 30% of midmarket firms, and 17% of large enterprises are considering migrating away from Redis.](https://cdn.thenewstack.io/media/2024/10/ef142c0b-planning-redis-migration-company-size-1024x389.png)
What do you think about Redis moving the codebase to a more restrictive license? (Responses segmented by company size)

Drilling one level down, large and enterprise organizations represent the biggest cohort that plans to migrate to Valkey. This is understandable, as the impact of licensing changes tends to be more substantial for organizations that handle large amounts of data. However, these organizations tend to migrate to alternatives more slowly due to potential downtime and operational support considerations.

![77% of SMBs, 70% of midmarket companies, and 85% of large enterprises are using or considering adopting Valkey.](https://cdn.thenewstack.io/media/2024/10/f9a5b32f-valkey-migration-1024x389.png)
Have you already decided to adopt Valkey in your organization? (Responses segmented by company size)

To accelerate adoption, the Valkey community and endorsers should consider providing the necessary tools and services to ensure a smooth transition to the Redis alternative.

## Valkey Support Options Needed
Redis’ community support infrastructure allowed it to thrive as an open source project, attracting a diverse user base and fostering rapid growth. But for organizations that plan to use Redis alternatives in production, operational support considerations may impact the speed of adoption.

The survey reveals varied support strategies: Some organizations are unsure about internal support needs; some will wait for managed versions of Valkey and others will seek external support. Most organizations (75.5%) plan to use third-party enterprise support, while a minority (24.55%) plan to rely on in-house teams or community resources for Valkey maintenance.

![75.5% of respondents consider the availability of external vendor support for open source projects like Valkey an important factor when making technology decisions](https://cdn.thenewstack.io/media/2024/10/94ee23ab-redis-moving-to-restrictive-license-1024x558.png)
Do you consider the availability of external vendor support for open source projects like Valkey an important factor when making technology decisions?

This is a pivotal moment in the evolution of the key-value store landscape, with Valkey poised to gain significant traction as organizations seek open source alternatives to Redis. As [Valkey continues to evolve](https://thenewstack.io/valkey-will-not-just-be-a-redis-retread/), its ability to meet organizations’ diverse needs, coupled with strong commercial backing, will be crucial in solidifying its position in the market.

For more on these trends, you can [review the full survey](https://learn.percona.com/hubfs/Collateral/Whitepapers/Adoption-Trends-Through-a-Valkey-Lens-WhitePaper.pdf).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)