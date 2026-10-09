当 Redis [在 2024 年更改其许可证](https://redis.io/blog/redis-adopts-dual-source-available-licensing/)，用专有的、源码可用的替代方案取代其宽松的 [BSD](https://en.wikipedia.org/wiki/BSD_licenses) 许可证时，它引发了社区的重大分裂。几天之内，Linux 基金会[推出了 Valkey](https://www.linuxfoundation.org/press/linux-foundation-launches-open-source-valkey-community)，这是一个开源分支。

虽然 Redis [随后再次改变了路线](https://thenewstack.io/redis-is-open-source-again/)，在 2025 年将 copyleft [AGPLv3](https://www.fsf.org/bulletin/2021/fall/the-fundamentals-of-the-agplv3) 开源许可证作为一种可选方案，但对于希望使用具有独立治理的宽松许可项目的组织来说，[Valkey](https://valkey.io/) 已经开辟了自己的道路。

在过去的几个月里，发生了许多事情，Valkey 采取了[减少内存需求](https://thenewstack.io/valkey-91-cuts-memory/)、引入新的集群管理和访问控制功能等措施，最近还开始[使用智能体来协助](https://thenewstack.io/valkey-ai-backporting-agents/)维护工作，例如修复程序的回溯移植。

但对于某些 Redis 用户来说，至少还存在一个重大的迁移障碍。

## 代理访问

对于初学者来说，Redis 是一个内存数据存储，广泛用于缓存和其他需要快速访问的工作负载。许多应用程序被构建为与 Redis 交互，就好像它是一个单一实例一样，将这些应用程序移动到分布式 [Valkey 集群](https://valkey.io/topics/cluster-tutorial/)可能意味着更改代码，以便它能够处理多个节点、路由以及某些命令行为的差异。商业 Redis 产品和一些云服务通过位于应用程序和底层集群之间的代理层来绕过这个问题，但想要自己运行 [Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/ "Valkey") 的公司一直缺乏同等选择。

因此，[Percona](https://www.percona.com/) 现在正试图通过 Valkey-proxy 来填补这一空白，这是一个开源代理，允许现有应用程序连接到 Valkey 集群而不必重写。

Percona 是一家开源数据库软件和服务公司，支持包括 MySQL、PostgreSQL 和 MongoDB 在内的技术。它也是支持 Valkey 项目的公司之一，其他支持者还包括 AWS、Google Cloud 和 Oracle 等云巨头。

在布拉格 Linux 基金会[欧洲开源峰会](https://events.linuxfoundation.org/open-source-summit-europe/)会议的采访中，Percona 的 Redis/Valkey 生态系统总经理 [Kyle Davis](https://www.linkedin.com/in/kyle-davis-linux/) 表示，在转向集群 Valkey 部署之前必须重写应用程序，是更广泛采用的最后大障碍之一。

> “目前真的没有针对此事的好的开源解决方案。”

“目前真的没有针对此事的好的开源解决方案，因此一直存在这个鸿沟，”Davis 告诉 *The New Stack*。

无论如何，还有其他代理存在。Davis 指出 [Envoy](https://www.envoyproxy.io/) 就是一个例子，但表示它并不完全理解 Valkey 协议，并且处理连接的方式意味着它无法支持 Valkey 能做的一切。

这使得一些公司陷入困境：一方面是围绕单个 Redis 实例构建的旧应用程序，另一方面是随着业务增长所需的集群 Valkey 部署。Valkey-proxy 旨在弥合这一鸿沟。

“现在我们可以解决一整层以前没有好选择的应用程序，”Davis 补充道。

> “现在我们可以解决一整层以前没有好选择的应用程序。”

## Valkey-proxy 的理由

Percona 在内部开发了 Valkey-proxy 的第一版本，但计划将其移入 Valkey 项目，然后向更广泛的社区开放开发。

“从那里，我们将获得来自 Percona 客户、其他地方的客户以及独立开发者的很多贡献，”Davis 说。

当被问及像 AWS 这样的大型云厂商是否也会做出贡献时，Davis 表示“有可能”，但补充说这很难预测，因为他们通常拥有直接与其服务绑定的自己的工具。

这使得 Valkey-proxy 对管理自己基础设施的组织（包括在本地运行的组织）特别相关。Davis 表示，潜在用户群从小资源有限的公司到有严格合规要求的的大型金融服务组织——这些企业可能需要对其数据基础设施的运行地点和方式有更大的控制权。

此外，随着时间的推移，代理还可以为 Valkey 项目提供添加其他功能的地方。

> “填补这一缺失的空白使我们能够拥有更多的灵活性，现在我们可以开始以不同的方式做事了。”

“它提供了一个解耦层，未来我们可以在其中构建其他组件，”Davis 继续说道。“填补这一缺失的空白使我们能够拥有更多的灵活性，现在我们可以开始以不同的方式做事了。”

然而，就目前而言，重点是将项目交到用户手中。Percona 在 9 月下旬获得批准，使 Valkey-proxy 成为 Valkey 项目的一部分，目前正将代码从私有仓库转移到公共项目中。

我们的目标是在 10 月底前公开所有源代码，随后在 12 月发布候选版本，并在 2027 年初全面上市。

Davis 表示，在这期间，随着用户开始针对他们自己的应用程序测试代理，找到边缘情况将非常重要。[Freshworks](https://www.freshworks.com/) 将是首批这样做的公司之一，Davis 表示该公司已经作为早期用户和设计合作伙伴与 Percona 合作开发 Valkey-proxy，随着开发的继续，帮助发现问题。

“这将是一个很好的测试案例，”他补充道。