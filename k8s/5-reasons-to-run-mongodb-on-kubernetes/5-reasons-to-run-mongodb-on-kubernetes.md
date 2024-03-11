
<!--
title: 在Kubernetes上运行MongoDB的5个理由
cover: https://cdn.thenewstack.io/media/2024/03/4d0603a3-kittens.jpg
-->

了解这些优势有助于您驾驭现代应用程序部署的复杂性并做出明智的选择。

> 译自 [5 Reasons to Run MongoDB on Kubernetes](https://thenewstack.io/5-reasons-to-run-mongodb-on-kubernetes/)，作者 Sergey Pronin。

对于寻求满足可扩展性、可靠性和性能需求的企业来说，在 Kubernetes 上运行 MongoDB 是一个明智的选择。这两种技术的集成解决了企业在管理大规模动态环境时面临的一些最关键的挑战。从简化操作到确保高可用性，利用 Kubernetes 进行 MongoDB 部署的理由是令人信服的。

让我们探讨在 Kubernetes 上运行 MongoDB 作为企业为未来优化其数据基础设施的推荐策略的五大理由。无论您是开发人员、数据库管理员还是业务决策者，了解这些优势都可以帮助您驾驭现代应用程序部署的复杂性并做出明智的选择。

## 避免供应商锁定

Kubernetes 提供了跨多个云提供商或混合环境部署数据库的灵活性。这对于希望避免供应商锁定或需要跨不同地理位置进行分布式部署以降低延迟并遵守数据主权法律的组织特别有益。

这种灵活性是通过 [Kubernetes 统一 API](https://thenewstack.io/kubernetes-is-not-just-about-containers-its-about-the-api/) 实现的——在不同环境中使用相同的原语、命令和工具。MongoDB 集群可以在任何地方运行——云端和/或本地——工程团队在迁移时无需更改工具集。

## 消除繁琐工作

Kubernetes 旨在自动化 [容器编排中的例行任务](https://thenewstack.io/kudo-automates-kubernetes-operators/)。但真正的力量来自于 [Operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)——Kubernetes 中管理应用程序的软件扩展。

Kubernetes Operator，如 [Percona Operator for MongoDB](https://www.percona.com/mongodb/software/percona-operator-for-mongodb)，不仅可以自动化部署，还可以消除第 2 天操作的复杂性。现在，工程师可以利用嵌入在运营商代码中的专业知识，并花更多时间构建应用程序。

## 降低成本

云原生计算基金会 [FinOps 调查](https://www.cncf.io/wp-content/uploads/2023/12/CNCF_Finops-Microsurvey-2023.pdf) 中 70% 的受访者将超额配置列为超支的主要原因。

容器化设计允许您通过在单台机器上密集打包工作负载来减少过度利用。此外，通过 Kubernetes 有效地管理集群中的资源，您的 MongoDB 占用空间可以有效运行，并且没有性能或可用性问题，但资源占用空间却小得多。

MongoDB 的各种运营商等开源技术还可以让您避免高昂的许可成本并进一步削减账单。

## 生态系统和集成

Kubernetes 拥有庞大的生态系统，并且可以很好地与各种工具和平台集成，从而可以增强 MongoDB 的功能。这包括从监控和日志记录工具到持续集成和持续部署 (CI/CD) 管道的各种内容。在 Kubernetes 上运行 MongoDB 允许您利用此生态系统，从而更轻松地构建、部署和维护强大的应用程序。

## 更快的开发

作为一名开发人员，在 Kubernetes 上运行 MongoDB 提供了几个关键优势，可以简化您的工作流程并增强整体开发体验。首先，它简化了部署过程，允许您轻松地 [扩展 MongoDB 集群](https://thenewstack.io/the-smallest-kubernetes-cluster-scaling-down-to-the-edge/) 根据应用程序的需求向上或向下扩展，直接从您的开发环境中扩展。正如我们之前提到的，运营商的自动化管理功能减少了您在数据库管理上花费的时间和精力，让您可以更多地关注编码，而更少地关注操作任务。

此外，与 [Kubernetes 集成可以促进更无缝的 DevOps 和 CI/CD 管道](https://thenewstack.io/kubernetes-ci-cd-pipelines-explained/)，使您能够自动部署 MongoDB 数据库以及您的应用程序代码。此集成有助于实现更快的开发周期、一致的测试环境和更可靠的版本。

此外，Kubernetes 对容器化环境的支持确保了您的 MongoDB 实例在隔离的可重复环境中运行。这种跨开发、测试和生产的一致性最大程度地减少了“在我的机器上运行”的问题，从而减少了部署问题，并腾出更多时间用于开发新功能或改进现有功能。

## 下一步是什么？

MongoDB 和 Kubernetes 共同代表了现代应用程序部署，解决了可扩展性、运营效率和灵活性方面的关键挑战。通过利用 Kubernetes 进行 MongoDB 部署，企业不仅可以优化其数据基础设施，还可以促进其开发团队的创新和敏捷性。

[Percona Operator for MongoDB](https://github.com/percona/percona-server-mongodb-operator) 的第一个提交是在六年前创建的。在这些年中，我们看到 Kubernetes 上的数据库从 Greenfield 技术演变为企业级首选解决方案。不妨试一试，它 100% 开源。
