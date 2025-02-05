
<!--
title: Percona 支持 Valkey，提供企业级支持
cover: https://cdn.thenewstack.io/media/2025/02/75f4c060-percona.png
-->

Percona已启动对开源Valkey数据库的支持和迁移服务。

> 译自 [Percona Backs Valkey With Enterprise-Grade Support](https://thenewstack.io/percona-backs-valkey-with-enterprise-grade-support/)，作者 Joab Jackson。

[Percona](https://www.percona.com/?utm_content=inline+mention) 为 MongoDB 和 MySQL 等开源数据库系统提供企业级支持，该公司周二宣布，其产品组合已扩展到也支持开源 [Valkey 内存数据存储](https://valkey.io/)。

[Percona 为 Valkey 提供的支持](https://www.percona.com/valkey/support-and-services) 计划是一项全面的服务，提供 [Valkey 部署](https://thenewstack.io/valkey-will-not-just-be-a-redis-retread/) 的全天候支持。它有两种形式：一种用于生产环境，另一种“高级”产品适用于可能需要在出现问题时立即获得帮助的关键应用程序。

对于那些已经使用 Redis 的用户，[Valkey 是去年从 Redis 分支而来](https://thenewstack.io/navigating-the-path-from-redis-to-valkey/)，该公司还提供 [Valkey 迁移](https://www.percona.com/resources/valkey-migration) 服务来帮助他们进行转换，如果他们希望这样做的话。

Percona 联合创始人 Peter Zaitsev 在一份声明中表示：“对 [Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/) 的兴趣和支持几乎立即爆发，这不仅仅是技术本身的问题。”“这不仅仅是公司寻求控制成本的问题。这是人们对自称‘开源’软件供应商突然决定放弃这种模式感到普遍不满和沮丧的表达。”

## 开源 Valkey

Valkey 的创建是 [对 Redis 决定更改其同名数据存储许可模型的直接回应](https://thenewstack.io/linux-foundation-forks-the-open-source-redis-as-valkey/)，它放弃了开源许可证，转而采用 Redis Source Available License (RSALv2) 和 Server Side Public License (SSPLv1)。

Percona Valkey 技术主管 Martin Visser 在接受 TNS 采访时表示：“Redis 从未如此快速发展”，并指出 Valkey 的第二个主要版本 8.1 即将发布。

该项目吸引了主要科技公司，包括 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) (AWS)、[Google Cloud](https://cloud.google.com/?utm_content=inline+mention)、爱立信以及 Percona 本身提供的工程帮助。

[Valkey 8.0 版本](https://thenewstack.io/valkey-whats-new-and-whats-next/) 于 9 月发布，是第一个以重要方式改进原始代码库的主要版本，包括多核利用和异步 I/O 线程，据该项目称，这两个长期以来一直备受期待的功能大大提高了性能。

## 商业支持

Visser 指出，希望使用该软件——或将其当前版本的 Redis 迁移过去——的用户可能需要一些商业支持。

该公司警告说，像任何开源软件一样，组织当然可以在内部运行 Valkey，尽管他们会遇到一些难以在没有一些严重的工程帮助的情况下减轻的问题，包括低效的键值存储配置、高延迟操作、复杂的迁移和错误配置的设置。

Percona 的一项调查发现，75% 的 Redis 用户正在测试、考虑或已经采用了 Valkey，76% 的用户计划使用第三方企业支持。

## Percona 的新领域

展望未来，Percona 将致力于投入工程资源来增强 Valkey 的可编程性，并提供安全增强和错误修复。

Visser 解释说，该公司不打算像对 MongoDB 和 MySQL 那样推出自己的发行版，而是直接向上游贡献功能。
