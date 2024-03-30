
<!--
title: Linux基金会支持Redis的开源分叉Valkey
cover: https://cdn.thenewstack.io/media/2024/03/8bcfdf51-valkey.webp
-->

Redis 首席执行官嘲笑该分支，称其为云提供商为避免支付许可费而采取的卑鄙策略。

> 译自 [Linux Foundation Backs 'Valkey' Open Source Fork of Redis](https://thenewstack.io/linux-foundation-forks-the-open-source-redis-as-valkey/)，作者 Joab Jackson。

Linux 基金会，我们必须避免面对这种局面。

周四，该基金会宣布打算支持以前开源的 Redis 内存数据存储的分叉，紧随 [Redis](https://redis.com/?utm_content=inline+mention) 本身[将](https://redis.com/blog/redis-adopts-dual-source-available-licensing/) 码库[迁移](https://lwn.net/Articles/966133/)到更严格的许可证的消息之后。

从 7.4 版开始，Redis 将在 [Redis 源代码可用许可证 (RSALv2)](https://redis.com/legal/rsalv2-agreement/) 和[服务器端公共许可证 (SSPLv1)](https://redis.com/legal/server-side-public-license-sspl/)下获得双重许可。旧版本将[保持开源](https://thenewstack.io/new-research-shows-secure-usage-of-open-source-remains-problematic/)。

因此，Linux 基金会正在全力支持一个名为 Valkey 的新项目，作为“Redis 内存、NoSQL 数据存储的开源替代品”。

许多行业参与者已经迅速加入，包括 [亚马逊网络服务](https://aws.amazon.com/?utm_content=inline+mention) (AWS)、[Google Cloud](https://cloud.withgoogle.com?utm_content=inline+mention) 和 [Oracle](https://developer.oracle.com/?utm_content=inline+mention)。

“通过组建 Valkey，贡献者可以从我们中断的地方继续，并继续为充满活力的开源社区做出贡献，”AWS 首席工程师兼 [前长期 Redis 维护者](https://www.linkedin.com/feed/update/urn:li:activity:7176350563071139840/)、Valkey 的联合发起人 [Madelyn Olson](https://www.linkedin.com/in/madelyn-olson-6a5053b6/) 在一份声明中说。

“很高兴看到一个强大的社区如此迅速地在 Valkey 周围形成，”Google Cloud 数据库工程副总裁兼总经理 [Andi Gutmans](https://www.linkedin.com/in/andigutmans/) 也在一份声明中表示。

在发布时，[该项目](https://github.com/madolson/placeholderkv)有九位贡献者——包括 Olson 和另外两位 AWS 工程师——并获得了 1,500 个 GitHub 星标。

Valkey 将使用 Redis v. 7.2.4 作为基础，将其置于开源伯克利软件发行版 (BSD) 三条款许可证之下。

## Redis 提出质疑，邀请竞争

在给 The New Stack 的电子邮件回复中，Redis 首席执行官 [Rowan Trollope](https://www.linkedin.com/in/rowant/) 几乎嘲笑了这个分支，称其是吝啬的云提供商为了逃避支付许可费而进行的卑鄙工作。

“主要的云服务提供商都从 Redis 开源项目中受益匪浅，因此他们在一个基金会内启动一个分叉也就不足为奇了，”Trollope 写道。

Trollope 解释说，Redis 的许可变更是为了与云提供商建立公平的许可协议。微软[达成了一项协议](https://azure.microsoft.com/en-us/blog/redis-license-update-what-you-need-to-know/)，而 AWS 和 GCP 尚未达成协议。

就像 HashiCorp 之前所做的那样，Redis 强调了其对企业卓越性的承诺。

“我们仍然专注于我们作为 Redis 项目管理者的角色，以及我们投资 Redis 源代码可用产品、生态系统、开发人员体验和服务于我们客户的使命，”Trollope 写道。“创新一直是并将永远是 Redis 和任何替代解决方案成功之间的区别因素。”

自然，业界观察人士仍然持怀疑态度。

System Initiative 联合创始人 [Adam Jacob](https://thenewstack.io/adam-jacob-rebuilding-devops-with-system-initiative/) 在 X 上写道，这对 Redis 实验室来说是“最糟糕的结果”。

“恭喜！你现在有一个资金充足、以 0 美元的价格提供可信产品的竞争对手，显然云提供商将使用它来竞争，”他[发推文](https://twitter.com/adamhjk/status/1773401933073780752)说。

## Linux 基金会最近分叉了哪些软件？

在开源术语中，[分叉（forking）](https://thenewstack.io/may-fork-short-history-of-open-source-forks/) 是[复制代码库](https://thenewstack.io/the-security-risks-of-forking/)然后独立于发起者开发它的过程，通常会导致两个独立且很快不兼容的代码库。

这是非营利性 Linux 基金会第二次在（以商业为导向的）创建者撤销许可条款后支持商业软件的分叉。9 月份，该基金会[克隆了 Terraform](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/)，就在 HashiCorp 将该基础设施即代码 (IaC) 软件移至非开源、仅供查看的 BSL（商业源代码许可证）一个月后。该软件更名为 [OpenTofu](https://thenewstack.io/can-opentofu-become-the-http-of-infrastructure-as-code/)。

[HashiCorp Vault 机密管理器](https://thenewstack.io/hashicorps-releases-hcp-vault-to-combat-secrets-management-fatigue/) 也被[IBM](https://www.ibm.com?utm_content=inline+mention)的工程师分叉为 [OpenBao](https://thenewstack.io/meet-openbao-an-open-source-fork-of-hashicorp-vault/)，目标是成为 Linux Foundation Edge 项目。

遵循行业趋势，Redis 和 HashiCorp 都表达了将各自代码库移出开源许可证的商业原因，加入了其他公司，如 [Elastic](https://thenewstack.io/this-week-in-programming-aws-completes-elasticsearch-fork-with-opensearch/) 和 MongoDB 的[做法](https://www.computerworld.com/article/3714821/software-vendors-dump-open-source-go-for-the-cash-grab.html)。

## Redis 是什么？

在最近的调查中，DB_Engines
[对 Redis 进行了排名](https://db-engines.com/en/ranking)，将其列为全球使用第六广泛的数据库。

[Redis 项目](https://redis.io/) 由 [Salvatore Sanfilippo](https://thenewstack.io/redisconf-2020-why-redis-is-more-than-just-a-cache-provider/) 于 2009 年创建，作为 [高性能键/值存储](https://thenewstack.io/redis-is-not-just-a-cache/)，可用于缓存或作为实时数据分析、会话存储、消息代理和许多其他用例的快速数据存储。成千上万的开发者为该项目做出了贡献。

最初，Valkey（“键/值”的反向缩写）将在 Linux、macOS、OpenBSD、NetBSD 和 FreeBSD 平台上运行。

开发团队计划继续执行现有的 Redis 路线图，计划对集群系统进行槽迁移、可扩展性和稳定性方面的改进。多线程性能改进、触发器、新命令和向量搜索支持也在计划中。

Linux Foundation 首席技术官 [Chris Aniszczyk](https://www.linkedin.com/in/caniszczyk/) 在[一份声明](https://www.linuxfoundation.org/press/linux-foundation-launches-open-source-valkey-community)中表示：“培养对所有人都有利且不仅仅有利于单个组织的开放协作对于构建长期、可持续的开源社区至关重要。”“将此项目交由一个基金会而不是一家公司管理，意味着 Valkey 将由社区驱动，而不会出现意外的许可证变更，从而破坏信任并扰乱公平的开源竞争环境。”

许多[开源发行版](https://thenewstack.io/distribution-commercialization-and-the-future-of-open-source/)，例如 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 的 Fedora，目前在其软件包中包含 Redis，并且 [可能很难继续这样做](https://lwn.net/ml/fedora-devel/CAEg-Je_GoiJN6kOj1_K5WqTvA6n0j8r4fi9=C7-WbXLHovM3ow@mail.gmail.com/)，因为新的 Redis 许可证具有更严格的性质。

该基金会并不是唯一一个希望保持[Redis 开源](https://thenewstack.io/open-source-builders-how-redis-upended-the-database-market/)的组织。[Redict 项目](https://andrewkelley.me/post/redis-renamed-to-redict.html)也最近启动，目标是实现这一目的。

*David Cassel 为此文章做出了贡献。* 

*3/28：此文章已根据 Redis 的意见进行了更新。*
