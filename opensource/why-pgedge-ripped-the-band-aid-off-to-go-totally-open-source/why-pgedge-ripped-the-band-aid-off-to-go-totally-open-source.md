
<!--
title: pgEdge为何壮士断腕，彻底开源？
cover: https://cdn.thenewstack.io/media/2025/09/cb49d210-coding123.jpeg
summary: pgEdge将专有许可改为OSI批准的PostgreSQL许可，以响应客户需求并融入社区。其他如Redis也转向OSI开源许可应对竞争。研究显示，OSI批准的开源许可更受欢迎。
-->

pgEdge将专有许可改为OSI批准的PostgreSQL许可，以响应客户需求并融入社区。其他如Redis也转向OSI开源许可应对竞争。研究显示，OSI批准的开源许可更受欢迎。

> 译自：[Why pgEdge 'Ripped the Band-Aid Off' To Go Totally Open Source](https://thenewstack.io/why-pgedge-ripped-the-band-aid-off-to-go-totally-open-source/)
> 
> 作者：Susan Hall

围绕开源许可授权模式转变的喧嚣——[HashiCorp/OpenTofu](https://thenewstack.io/how-opentofu-happened-and-whats-next/) 之类的事件——似乎已稍作平息，但在数据库领域仍在继续。

逆势而上的供应商之一是分布式 Postgres 供应商 [pgEdge](https://www.pgedge.com/?utm_content=inline+mention)。它最近宣布已完全开源，并将其 [Spock](https://github.com/pgEdge/spock) 多主逻辑复制扩展、[大型对象逻辑复制](https://github.com/pgEdge/lolor) (lolor) 扩展以及 [Snowflake 序列](https://github.com/pgEdge/snowflake) 的许可从其专有的 pgEdge 社区许可更改为经开放源代码促进会 (OSI) 批准的 [PostgreSQL 许可](https://opensource.org/license/postgresql)。

联合创始人兼首席执行官 Phillip Merrick 在一次采访中解释道，此举是应潜在客户的要求做出的。

“我们发现，在 Postgres 社区中，我们被排除了很多关于我们这类技术的讨论，因为 Postgres 社区理所当然地不希望接受任何非开源的东西，而且他们不认为我们的社区许可……是真正的开源。因此，我们觉得是时候壮士断腕，完全走向开源了。”

工程副总裁 Dave Page 在一篇[博客文章](https://www.pgedge.com/blog/pgedge-goes-open-source)中解释道，此前的“源代码可用”许可对组件的使用方式施加了一些限制。

Merrick 说，之前的许可允许用户复制、修改和随意使用代码。唯一的真正禁令是禁止使用该代码直接与 pgEdge 竞争。

“我们一直认为自己是一家致力于开源和 Postgres 社区的公司。通过我们的分布式 Postgres 工作，我们实际上已经将其开源，但我猜那只是‘小写’的开源，因为它没有采用 OSI 批准的许可之一。”他解释道。

在源代码可用许可下，软件源代码是公开的，可以自由修改和重新分发，但通常会限制商业或竞争性使用。

[亚马逊/Elastic 之间的争斗](https://thenewstack.io/amazon-elastic-and-the-fight-for-open-source-freedom-in-the-enterprise/)，以及其他云服务提供商和公司获取开源代码并直接与其创建者竞争的案例，都让 pgEdge 感到担忧。

“我们对此有些担忧。事实证明，我们的担忧可能有点多余，并非完全没有根据，但确实有点多余。与此同时，我们知道有些客户除非我们的技术是真正获得 OSI 批准的‘大写’开源产品，否则他们根本不想考虑。”Merrick 说。

## 企业级 Postgres 的兴趣

他表示，Postgres 市场似乎有所萎缩，而有些客户则坚持要求产品拥有 [OSI](https://opensource.org/osd) 批准的许可。

OSI 已拒绝将 Business Source License (BSL) 和 [Server Side Public License (SSPL)](https://opensource.org/blog/the-sspl-is-not-an-open-source-license) 视为真正的开源许可。OpenLogic 的“[2025 年开源状况报告](https://www.openlogic.com/system/files/2025-05/report-openlogic-2025-state-of-open-source-support.pdf)”指出，在许可变更后，OSI 不再将 [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention)、Elasticsearch 和 CockroachDB 列为符合其开源产品标准的项目，尽管它们已根据 OSI 批准的 [AGPL (GNU Affero General Public License)](https://opensource.org/license/agpl-v3) 重新许可了一些组件。

IDC 分析师 Devin Pratt 告诉 FastForward，最近收购的两家 Postgres 初创公司——Neon 和 Crunchy Data——反映了[市场对企业级 Postgres](https://fastforward.boldstart.vc/snowflake-snags-crunchy-data-to-get-enterprise-grade-postgres-database/) 以及 AI 的兴趣。

[Databricks 收购 Neon](https://www.wsj.com/articles/databricks-to-buy-startup-neon-for-1-billion-fdded971) 是为了作为其[托管 Lakebase 产品](https://thenewstack.io/lakebase-is-databricks-fully-managed-postgres-database-for-the-ai-era/)的基础，并简化 AI 代理的开发。而 Crunchy Data 现已成为 [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) 的一部分，将被整合到其 [AI 数据云](https://thenewstack.io/how-snowflake-redefined-its-data-stack-with-an-ai-first-strategy/)中。

对企业级 Postgres 的兴趣也促使 pgEdge 进行了多元化发展。

在其企业产品中，pgEdge 一直专注于分布式[多主](https://www.pgedge.com/solutions/benefit/multi-master)架构，以[维护关键工作负载的高可用性](https://thenewstack.io/how-distributed-postgres-solves-clouds-high-availability-problem/)。它已将支持范围扩大到非分布式和分布式 Postgres 应用程序。

## 重新转向开源许可

“在供应商（通常是数据库供应商）从开源许可转向源代码可用替代方案（例如 BSL、SSPL 等）几年之后，现在又重新转向了开源许可——通常是 AGPL，”Redmonk 首席分析师兼联合创始人 Stephen O’Grady 在一封电子邮件中说道。

Redmonk 的 Rachel Stephens 在她的研究中使用了公认的小样本，发现公司从开源许可改为专有许可后，所获得的[商业价值](https://redmonk.com/rstephens/2024/08/26/software-licensing-changes-and-their-impact-on-financial-outcomes/)或采用率增长[微乎其微](https://redmonk.com/rstephens/2024/08/26/software-licensing-changes-and-their-impact-on-financial-outcomes/)。

“总的来说，源代码可用许可可能会给开发人员和企业带来采用上的摩擦，因此一些项目已回归到提供最大保护的经批准的[开源许可](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/ "开源许可")，”O’Grady 说。

Redis 最近宣布在 [AGPL v3 许可](https://opensource.org/license/agpl-v3)下[再次开源](https://thenewstack.io/redis-is-open-source-again/)。Redis 首席执行官 Rowan Trollope 告诉 TNS 的 Frederic Lardinois，这一改变源于云提供商在其平台上提供托管 Redis 服务。许可的转换意味着这些供应商现在也必须获得 Redis 的许可。

“我们认为 AGPL 许可为[云服务提供商]提供了保护，因为如果他们想以开源版本提供我们（他们可以这样做），他们就必须将所有代码作为开源发布。他们有内部政策规定他们不会这样做。所以我们认为这是一个有效的模式，”Trollope 告诉 Lardinois。

“如果说有什么变化的话，那就是过去一年里（软件许可变更）事情有所放缓，”开源倡导者、Chainguard 首席执行官兼联合创始人 Dan Lorenc 说道，并补充说这些变化是间歇性发生的。

他提到了 [Fair Source 项目](https://fair.io/about/)，这是一项始于 2024 年的倡议，旨在解决开源领域对更清晰软件许可的需求。

“Fair Source 项目试图通过提供新的标准许可供软件公司使用来推动这一转变，但他们的网站显示这项运动进展缓慢：2024 年发布了七项公告，而 2025 年迄今只有五项，”他说道。“与此同时，开源仍在持续增长。[GitHub 的‘Octoverse’报告](https://github.blog/news-insights/octoverse/octoverse-2024/)最近显示开源项目同比增长 25%。如果这些许可变更无法超越这种增长，它们将继续只是一个四舍五入的误差。”