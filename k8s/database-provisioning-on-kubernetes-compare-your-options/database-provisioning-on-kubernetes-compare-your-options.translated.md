# Kubernetes 上的数据库配置：比较您的选择

![Featued image for: Database Provisioning on Kubernetes: Compare Your Options](https://cdn.thenewstack.io/media/2024/10/1d0e2132-database-kubernetes-provisioning-options-1024x576.jpg)

Kubernetes 作为容器化工作负载编排的标准的兴起，彻底改变了 [数据库](https://thenewstack.io/databases/) 的管理方式。随着企业越来越多地采用云原生架构，[Kubernetes](https://thenewstack.io/kubernetes/) 已经成为现代化 IT 基础设施的核心。

这种转变并不局限于无状态应用程序。[云原生计算基金会 (CNCF) 2022 年年度调查](https://www.cncf.io/reports/cncf-annual-survey-2022/) 发现，71% 的组织在 Kubernetes 中运行数据库和缓存，同比增长 48%。事实上，[Kubernetes 上的数据库](https://github.com/cncf/tag-storage/blob/master/data-on-kubernetes-whitepaper/data-on-kubernetes-whitepaper-databases.md) 的采用正在以前所未有的速度增长，这是由于人们对可扩展性和灵活性的渴望以及在云和本地环境中优化资源使用的需求所驱动的。

![Kubernetes 增长领域：开源项目位列最常用的解决方案。来源：CNCF](https://cdn.thenewstack.io/media/2024/10/ae140d02-kubernetes-growth-areas-1024x480.png)

Kubernetes 增长领域（来源：[CNCF](https://www.cncf.io/reports/cncf-annual-survey-2022/#findings)）

这种转变背后的动机很明显：Kubernetes 提供了传统数据库管理方法无法比拟的灵活性和可扩展性以及资源效率。凭借其强大的编排功能，Kubernetes 可以自动化诸如扩展、故障转移和恢复等任务，使其成为数据库管理的理想平台，尤其是在云原生和混合环境中。

然而，随着越来越多的组织希望 [采用 Kubernetes](https://roadmap.sh/kubernetes) 来管理数据库，他们 [面临着挑战](https://thenewstack.io/kubernetes-for-databases-weighing-the-pros-and-cons/)，这些挑战与操作复杂性、人工干预和特定于数据库的调整有关。这就是 Kubernetes 上的数据库配置选项发挥作用的地方，每个选项都有其自身的优缺点。[2022 年 Kubernetes 上的数据报告](https://dok.community/wp-content/uploads/2022/10/DoK_Report_2022.pdf) 强调，对受访者来说最大的变化是数据库配置的困难。

![自动化应用程序配置和配置管理是管理 K8s 上数据工作负载的最大挑战](https://cdn.thenewstack.io/media/2024/10/ce86c5a8-challenges-managing-data-workloads-k8s.png)

（来源：[DoK 报告 2022](https://dok.community/wp-content/uploads/2022/10/DoK_Report_2022.pdf)）

## Kubernetes 数据库配置选项

有几种解决方案可用于在 Kubernetes 上配置和管理云原生数据库。从手动部署方法到高级自动化工具，组织有多种选择，每种选择都适合不同的需求和技术要求。以下是 Kubernetes 上配置数据库资源的最突出选项：

- 手动部署
- Helm 图表
- Kubernetes 运算符
- 云原生数据库平台

## 手动部署

手动部署涉及通过配置 Kubernetes 资源（如 `PersistentVolumeClaims`、`StatefulSets`、`Services` 和 `ConfigMaps`）直接在 Kubernetes 上配置数据库。这种方法使管理员能够完全控制数据库配置，但也带来了巨大的开销。

**优点：**

- **完全控制部署**: 管理员可以自定义数据库设置的各个方面，从存储配置到网络配置。
- **灵活性**: 这种方法允许团队构建高度定制的数据库配置，以满足特定需求，尤其是在复杂环境中。

**注意事项：**

- **复杂性**: 手动管理 Kubernetes 上的数据库需要对数据库系统和 Kubernetes 都有深入的了解。诸如扩展、备份和故障转移等例行任务必须手动配置和执行。
- **操作开销**: 人工干预会导致高昂的操作成本。
- **容易出错**: 鉴于这种方法的手动性质，人为错误的可能性更高，这会影响新数据库的可用性和性能。

## Helm 图表
[Helm](https://thenewstack.io/get-started-with-the-helm-kubernetes-package-manager/) 是 Kubernetes 的一个包管理器，它通过将 Kubernetes 资源捆绑到可重用的图表中来简化应用程序的部署。 许多流行的数据库都存在 Helm 图表，例如 [MySQL](https://thenewstack.io/upgraded-mysql-crashes-on-restart-percona/)、[PostgreSQL](https://roadmap.sh/postgresql-dba) 和 [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention)，这使得在 Kubernetes 上部署这些数据库变得更加容易。
**优点：**
* **快速设置**: Helm 图表通过提供针对常见数据库的预配置模板来简化部署过程，从而减少设置和配置数据库所需的时间。
* **可重用**: Helm 图表可在不同环境中重用，使其成为希望在开发、登台和生产环境中保持一致性的 DevOps 团队的热门选择。
* **社区支持**: 许多开源 Helm 图表由社区维护，提供频繁的更新和错误修复。
**注意事项：**
* **自定义选项有限**: 与手动部署相比，Helm 图表提供的灵活性较低。 自定义 Helm 图表通常需要修改底层模板，这可能很耗时。
* **没有内置自动化**: Helm 图表比手动部署更进一步，但它们不包括高级自动化功能，例如扩展、故障转移或备份管理。 这些任务必须单独管理。
## Kubernetes 运算符
[Kubernetes 运算符](https://thenewstack.io/kubernetes-when-to-use-and-when-to-avoid-the-operator-pattern/) 是最常用的自动化数据库配置方法，它利用 Kubernetes 的原生 API 来管理特定数据库技术的生命周期。 运算符将管理数据库所需的运营知识（例如配置、扩展、故障转移、备份和升级）封装到自定义控制器中。 每个运算符都是特定于数据库的，这意味着为 MySQL 设计的运算符只能与 MySQL 数据库一起使用。
来自 [Percona](https://www.percona.com/?utm_content=inline+mention)、[Bitpoke](https://www.bitpoke.io/)、[Oracle](https://developer.oracle.com/?utm_content=inline+mention) 和其他供应商的运算符通常用于自动化 MySQL、PostgreSQL 和 MongoDB 的管理。

**优点：**
* **特定于数据库的自动化**: 运算符根据每个数据库的独特需求来自动化数据库配置、扩展和故障转移过程。
* **细粒度控制**: 运算符提供更多控制，以便微调和自动化数据库操作。
* **深度集成**: 运算符直接与 Kubernetes 集成，利用其原生功能，例如`StatefulSets`
、`PersistentVolumes`
和`ConfigMaps`
来确保高可用性和持久性。
**注意事项：**
* **特定于数据库**: 大多数运算符都与特定的数据库技术绑定，这意味着管理多种数据库类型的组织需要部署和管理多个运算符，从而导致复杂性增加。
* **复杂环境中的手动工作**: 虽然运算符可以自动化许多任务，但某些操作（例如扩展和故障转移）通常需要在多集群、多区域和数据中心环境中进行手动干预。
* **命令行驱动**: 大多数运算符都是通过命令行管理的，对于没有深入 Kubernetes 经验的团队来说，这可能是一个陡峭的学习曲线。
## 云原生数据库平台
随着 Kubernetes 运算符在自动化数据库配置方面越来越受欢迎，它们引入了显著的自动化，但也带来了陡峭的学习曲线，并且在扩展、故障转移和系统集成方面需要大量的手动工作。 对于寻求替代方案的组织来说，有一个新的开源云原生数据库平台旨在简化数据库配置，而无需复杂性。

这种开源的公共数据库即服务 (DBaaS) 替代方案，[Percona Everest](https://www.percona.com/software/percona-everest)，旨在简化 MySQL、PostgreSQL 和 MongoDB 在云和本地环境中的数据库管理。 通过解决传统 Kubernetes 运算符的局限性，它引入了集中式管理界面、增强的自动化和对单个解决方案下多个数据库的支持。

**优点：**
* **简化的管理**: Percona Everest 提供了一个集中式管理界面，简化了数据库配置和管理。
* **增强的自动化**: 该平台提供了广泛的自动化功能，包括自动扩展、故障转移和备份。
* **多数据库支持**: Percona Everest 支持多个数据库，包括 MySQL、PostgreSQL 和 MongoDB，从而简化了多数据库环境的管理。
* **云原生架构**: Percona Everest 构建在 Kubernetes 之上，利用其可扩展性和弹性。
* **开源**: Percona Everest 是一个开源平台，允许用户访问源代码并进行自定义。
**注意事项：**
* **相对较新**: Percona Everest 仍然是一个相对较新的平台，因此其生态系统和社区支持仍在发展中。
* **有限的集成**: 与其他数据库平台相比，Percona Everest 的集成选项可能有限。
* **学习曲线**: 虽然 Percona Everest 旨在简化数据库管理，但它仍然需要对 Kubernetes 和数据库管理有一定的了解。
## 统一平台：从一个界面管理 MySQL、PostgreSQL 和 MongoDB，大幅减少处理跨多个集群的多个数据库的操作负担。**全面自动化：**自动执行扩展、故障转移、备份和恢复等关键功能，最大限度地减少人工干预，并在配置数据库时提高效率。**多云和混合支持：**支持混合和多云环境，实现跨本地和云平台的一致数据库管理。**自助服务功能：**内部团队可以使用基于 Web 的界面自助配置和管理数据库，从而加快部署速度并减少运营瓶颈。

**注意事项：**

**定制限制：**该平台提供了广泛的自动化和集中控制，但它可能没有像单个 Kubernetes 运算符那样多的定制选项，尤其是在与第三方监控或安全工具集成时。

## 比较 Kubernetes 上的数据库配置选项

此图表总结了上面描述的选项的优缺点。

| 数据库配置功能 | 手动部署 | Helm 图表 | Kubernetes 运算符 | 数据库平台 |
|---|---|---|---|---|
| 易用性 | 高度复杂 | 中等（基于模板） | 中等（基于 CLI） | 低（基于 UI，最少的人工操作） |
| 自动化 | 无 | 有限（无扩展/故障转移/备份） | 高（特定于数据库的自动化） | 广泛（多数据库自动化） |
| 定制 | 完全控制 | 有限 | 高（每个数据库可定制） | 中等（为易用性而简化） |
| 多数据库支持 | N/A | N/A | 否 | 是 |
| 扩展和故障转移 | 手动 | 手动 | 半自动化 | 全自动化 |
| 第三方集成 | 完全控制 | 有限 | 高（针对单个数据库） | 中等 |
| 用户界面 (UI) | 无 | 无 | 无（基于 CLI） | 基于 Web |
| 学习曲线 | 陡峭 | 中等 | 高（需要特定于数据库的知识） | 低（用户友好的 UI/API） |

**自动化数据库部署流程**

对于专注于单一数据库技术或需要广泛定制的团队，Kubernetes 运算符仍然提供了无与伦比的灵活性。但是，如果您要管理多个数据库，需要减少操作负担，或者想要基于 UI 的自助服务方法，[Percona Everest](https://www.percona.com/software/percona-everest) 代表了基于 Kubernetes 的数据库自动化的一个进步。

无论您是在跨云和本地环境管理单个数据库还是多个数据库，您都可以使用开源解决方案在 Kubernetes 上自动化和简化数据库管理，避免供应商锁定。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)