数据库支持提供商[Percona](https://www.percona.com/?utm_content=inline+mention)正在向[云原生计算基金会（CNCF）](https://cncf.io/?utm_content=inline+mention)捐赠一个用于[Kubernetes](https://thenewstack.io/kubernetes/)环境的数据库管理工具。

对于 Kubernetes 环境，新命名的 [OpenEverest](https://github.com/openeverest)（前身为 Percona Everest）提供了一个统一的界面，用于管理不同类型的数据库，包括供应和管理。目前，它支持 PostgreSQL、MySQL 和 [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention)。

该公司[战略](https://www.percona.com/blog/blog-post-good-bye-percona-everest-hello-openeverest/)是通过 CNCF，使 [OpenEverest](https://openeverest.io/) 成为一个由开放治理管理的多供应商项目。它将保留相同的 Apache 2.0 开源许可，并捐赠给该组织。据该公司称，商业版 [Percona Everest](https://www.percona.com/software/percona-everest) 的现有用户不会看到重大变化。

Percona 产品管理副总裁 Blair Rampling 在一份电子邮件声明中表示：“随着 Percona Everest 的成熟，越来越明显的是，该项目最好由社区主导的开源计划来服务，而不是仅仅由 Percona 主导。作为 OpenEverest，该项目有望成为一个完全独立于供应商的 Kubernetes 数据平台，因此可以供应和管理更多数据库，并最终实现超越数据库的集成。”

Everest 维护者 Sergey Pronin 和 Percona 创始人 Peter Zaitsev 也成立了一家新公司 [Solanica](https://solanica.io/)，为该软件提供企业支持服务。

[![OpenEverest Workflow](https://cdn.thenewstack.io/media/2026/01/d904b114-openeverest-workflow.png)](https://cdn.thenewstack.io/media/2026/01/d904b114-openeverest-workflow.png)

OpenEverest 工作流 (OpenEverest)。

## 私有数据库即服务

Percona 高级产品经理 Piotr Szczepaniak 在[《The New Stack》2023 年的一篇文章](https://thenewstack.io/building-an-open-source-private-dbaas/)中解释道，Percona 创建 Everest 的目的是为了在云环境中像云数据库提供商一样轻松管理多个数据库。

云数据库（数据库即服务，或 DBaaS）通常是预先配置好的，减少了开发人员设置它们所需的时间。高可用性、灾难恢复和自动伸缩功能通常内置其中，减轻了设置它们的负担。

Szczepaniak 详细阐述道，运行私有数据库服务——可能作为[平台工程计划](https://thenewstack.io/platform-engineering/)的一部分——具有额外的优势，例如对安全设置和数据本身拥有更大的控制权。更低的运营成本可能是另一个好处。

然而，对于许多公司来说，设置和维护私有数据库服务可能是一个挑战。这正是 OpenEverest 的目标用户群体。

## Everest 的工作原理

要在 Everest 中[创建数据库](https://openeverest.io/blog/how-openeverest-works/)，用户通过 Web 界面提交所需配置的请求。然后，他们使用该界面请求所需的 Kubernetes 资源。

Everest 的好处之一是，管理员无需了解每种数据库的特定设置例程。

OpenEverest 服务器通过 RESTful API 使用一组独立于数据库的自定义资源定义（*DatabaseCluster*、*DatabaseClusterBackup* 和 *DatabaseClusterRestore*），从而使管理员不必了解每个单独数据库操作符的特性。然后，它依赖于为特定数据库系统编写的一组操作符。

因此，该软件对 MySQL、MongoDB 或 PostgreSQL 的工作方式是相同的。

[![](https://cdn.thenewstack.io/media/2026/01/10376322-openeverest-crds-scaled.png)](https://cdn.thenewstack.io/media/2026/01/10376322-openeverest-crds-scaled.png)

OpenEverest 本身的管理（包括安装）是通过命令行界面 (CLI) 完成的，该界面处理账户管理、基于角色的访问控制 (RBAC)、命名空间、供应和升级等任务。

## CNCF 对新项目的标准

凭借活跃的用户群，Everest 很有可能成为 [CNCF 孵化项目](https://www.cncf.io/projects/)。CNCF 对技术的要求包括：至少有一些用户在生产环境中部署该技术，一个健康的贡献者基础，以及未来开发的[清晰路线图](https://github.com/openeverest/roadmap)。

管理有状态数据库负载是 Kubernetes 最初的挑战之一，因此围绕这一挑战进行了大量工作，从而催生了 [Data on Kubernetes](https://dok.community/) 社区。

正在开发中的其他多数据库解决方案包括 [KubeBlocks](https://kubeblocks.io/docs/preview/user_docs/overview/introduction) 和 [KubeDB](https://kubedb.com/features/)。凭借 [150 多个志愿者编写的扩展](https://operatorhub.io/operator/stackgres)，[StackGres](https://stackgres.io/doc/1.14/intro/about/) 是一个专注于 PostgreSQL 的流行实现，而 CNCF 沙盒项目 CozyStack 是一个支持数据库的云管理平台。几乎所有数据库也都有自己的专用 Kubernetes 操作符。

Percona 为一系列开源数据库系统提供高级支持服务，包括 [MySQL](https://thenewstack.io/facebook-makes-a-big-leap-to-mysql-8/)、[PostgreSQL](https://thenewstack.io/percona-brings-transparent-data-encryption-to-postgres/)、MongoDB 和 [Valkey](https://thenewstack.io/percona-backs-valkey-with-enterprise-grade-support/)。

视频

[YOUTUBE.COM/THENEWSTACK

科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、采访、演示等。

订阅](https://youtube.com/thenewstack?sub_confirmation=1)