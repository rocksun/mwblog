
<!--
title: Valkey 9.0 重磅发布：多数据库集群，驾驭海量级工作负载！
cover: https://cdn.thenewstack.io/media/2024/08/ec9588da-valkey.png
summary: Valkey 9.0正式发布，带来多数据库集群、原子槽迁移及性能优化，旨在处理大规模工作负载，并保持与Redis客户端的兼容性。
-->

Valkey 9.0正式发布，带来多数据库集群、原子槽迁移及性能优化，旨在处理大规模工作负载，并保持与Redis客户端的兼容性。

> 译自：[Valkey 9.0 Debuts Multidatabase Clustering for Massive-Scale Workloads](https://thenewstack.io/valkey-9-0-debuts-multidatabase-clustering-for-massive-scale-workloads/)
> 
> 作者：Steven J. Vaughan-Nichols

[Valkey](https://valkey.io/) 开源数据存储已正式发布 9.0 版本，标志着该项目自作为 [Linux 基金会支持的 Redis 分支](https://thenewstack.io/linux-foundation-forks-the-open-source-redis-as-valkey/) 推出以来最重要的更新。 [Valkey 9.0 版本](https://valkey.io/blog/introducing-valkey-9/) 引入了多数据库集群、原子槽迁移和主要性能优化，旨在处理每秒超过十亿次请求的大规模工作负载。

在其主要功能中， [Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/ "Valkey") 9.0 首次在集群模式下支持多数据库。开发者可以在不牺牲分布式集群高吞吐量和容错能力的情况下，操作独立的逻辑数据库。因此，您可以将 Valkey 以分片模式运行，用于大型数据集或高吞吐量用例。此前，这仅限于单个数据库，阻碍了集群安装的有效多租户。

## 无缝重新平衡的原子槽迁移

另一个值得注意的特性是原子槽迁移。这使得无缝的节点重新平衡和复制无需停机，提高了企业和云部署的可靠性。Valkey 始终能高度扩展到大型数据集（例如，千节点集群）。通常，应用程序使用从小型开始并随时间增长，这需要扩展 Valkey 集群。通过原子地移动一个槽而不是逐个键移动，这种扩展操作变得更加健壮。

此次更新还增加了哈希字段过期、用于集群故障转移的新配置选项、Lua 脚本安全改进以及优化的管道处理，以减少高并发环境中的延迟。Valkey 声称，凭借对大型有效载荷的零拷贝响应处理，其引擎在内部基准测试中实现了高达 20% 的吞吐量提升。

安全性在本次发布中发挥了重要作用。 [9.0 版本解决了 Lua 脚本环境中存在的多个漏洞](https://github.com/valkey-io/valkey/releases)，这些漏洞此前可能导致潜在的远程代码执行。 [新版本](https://github.com/valkey-io/valkey/releases) 还收紧了模块 API 控制，并引入了增强的客户端身份验证选项，包括通过 TLS 进行基于证书的登录。

## 性能优化和增强

维护者将此次发布描述为 Valkey 下一阶段开发的以稳定性为核心的基础，计划通过增量更新来完善其模块生态系统和内存效率。项目维护者 [强调](https://thenewstack.io/valkey-will-not-just-be-a-redis-retread/) 了与现有 Redis 客户端的兼容性，同时将 Valkey 定位为面向现代互联网规模应用程序的 [一个独立的、性能优化的数据存储](https://thenewstack.io/valkey-is-a-different-kind-of-fork/)。

在接受 The New Stack 采访时，开源数据库公司 [Percona](https://www.percona.com/?utm_content=inline+mention) 的 Valkey 技术主管 Martin Visser 表示：“Valkey 的采用率今年确实飙升。在我们的客户中，我们看到在成功切换了他们的开发和测试环境之后，他们持续努力增加部署并在生产中使用 Valkey。这已经扩展到数百甚至数千个实例。”

Visser 补充说：“我们也看到了多种不同的部署方法——一些公司希望在云中运行 Valkey，而另一些公司希望在其本地部署中替换 Redis 集群。对我们来说，大多数客户正在将其本地部署从 Redis 迁移到 Valkey，然后为特定应用程序添加选择性云部署。”

## Valkey 9.0 与 Redis 的比较

至于 Valkey 与 Redis 的直接比较，在另一次采访中，Valkey 项目维护者兼 AWS 工程师 Madelyn Olson 表示：“Valkey 9 是一个包含主要和次要功能的版本，拥有来自 40 多位独立贡献者的提交。该版本包括最受请求的功能——支持哈希字段过期——一种更快、更可靠的新分片算法，以及为批量发送命令的客户端带来的显著性能改进。这就是当你拥有多样化的项目贡献者时所能得到的结果。当我审视 Redis 时，我看到贡献的多样性要少得多，创新类型也不同。”

Valkey 9.0 现已在 Docker、GitHub 和官方 Linux 仓库上提供，并为从 8.x 分支升级的操作人员提供了详细的迁移说明。