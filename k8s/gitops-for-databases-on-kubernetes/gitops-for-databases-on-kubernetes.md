<!--
title: 在Kubernetes上通过GitOps实现数据库管理
cover: https://cdn.thenewstack.io/media/2024/01/49a339d2-mountain-8433234_1280-1024x576.jpg
-->

运用Operator模式实现数据库迁移。

> 译自 [GitOps for Databases on Kubernetes](https://thenewstack.io/gitops-for-databases-on-kubernetes/)，作者 Rotem Tamir 是 Ariga 的联合创始人兼 CTO。Atlas 的共同创建者和维护者，Atlas 是一个开源工具，可以将数据库模式作为代码进行管理。Ent 的共同维护者，这是一个由 Linux 基金会支持的 Go 实体框架。Ex-infra team lead at ironSource， ex-data...

随着应用程序的演进，其数据库模式也在变化。将数据库模式更改自动部署的做法随着现代 DevOps 原则的发展演变成所谓的[数据库迁移](https://thenewstack.io/cloud-migration-and-platform-engineering-at-large-organizations/)。

作为这一演变的一部分，已经创建了数以百计的“迁移工具”来帮助开发人员管理数据库迁移。这些工具范围从 Python 的 [Alembic](https://alembic.sqlalchemy.org/en/latest/) 等面向对象关系映射和特定语言的工具，到 [Flyway](https://flywaydb.org/) 和 [Liquibase](https://www.liquibase.org/) 等与语言无关的工具。

## Kubernetes 上的迁移: 当前状态

当 Kubernetes 出现，团队开始将应用程序容器化后，第一反应是将传统迁移工具封装在容器中，并作为应用程序部署过程的一部分运行。

就像我们试图将旧工具投射到新平台上时经常发生的那样，结果就是需要解决的缺陷集合。现在让我们回顾和讨论一些这些常见做法。

### 在应用内运行迁移

运行迁移最简单的方法是在应用程序启动期间直接调用它们。这不需要使用任何特殊的 Kubernetes 功能。我们只需要确保迁移工具、迁移文件和数据库凭据在应用程序容器内可用。然后，我们只需要更改启动逻辑，首先尝试运行迁移，如果成功则启动应用程序。

这被认为有几个原因是反模式。首先，从安全角度来看，最好是减少运行时环境的攻击面，不包含任何在运行时严格需要的东西。使用这种模式，迁移工具和运行 DDL 语句所需的更高数据库凭据会留在运行时环境中，供攻击者利用。

其次，假设应用程序为了冗余和可用性原因运行多个副本，那么将迁移作为应用程序启动的一部分，会迫使副本顺序加载，而不是并行加载。同时从多个地方应用相同的数据库更改是非常危险的，这就是为什么几乎所有工具都获取(或要求用户负责)某种锁定或同步技术。这意味着在实践中，新的 Pod 无法启动，直到它已相互排除所有其他 Pod 启动。

如果仅有几个副本，可能感觉不到差异，但考虑如果有数百个副本需要相互争夺启动会发生什么情况(带有所需的重试、后退等)。

### 作为 init 容器运行迁移

这种技术的一个轻微改进是使用 init 容器。Kubernetes 使定义“init 容器”成为可能，这是一个在 PodSpec 中主容器之前运行的容器。使用这种方法，团队可以引入独立工具(如 Liquibase 或 FlyWay)并在应用程序启动之前运行它们。

此外，模式修订的迁移本身(SQL文件)也必须以某种方式使容器可用，方法是构建自定义镜像或从某个外部源挂载它们。

与在应用内运行迁移相比，这种方法更好，因为它将迁移工具和凭据从运行时环境中移除，但遭受我们在应用内迁移中演示的相同同步问题。

此外，考虑迁移失败时会发生什么。迁移可能因各种原因失败，范围从无效的 SQL 到约束冲突到不稳定的网络连接。当迁移与应用程序运行时耦合时，迁移步骤中的任何失败都会导致大量 Pod 处于崩溃循环状态，这可能意味着应用程序可用性降低甚至停机。

### 将迁移作为 Kubernetes 作业运行

Kubernetes 允许使用“作业”API 执行程序。与使用 init 容器类似，团队可以使用封装迁移工具并以某种方式挂载迁移文件以在应用程序启动之前执行的作业。

这种方法的优点是，通过使用作业，可以确保迁移作为独立步骤在新的应用程序 Pod 开始滚动更新之前运行。团队常使用 Helm 升级前挂钩或 ArgoCD 预同步挂钩来实现这种技术。

结合使用，其结果是迁移只运行一次，避免了 init 容器展示的混乱“争相迁移”，并与运行时环境隔离，如上所述减小了应用程序的攻击面。

## GitOps 原则和迁移

> “我们可以将现有的模式管理解决方案封装到容器中，并在 Kubernetes 中作为作业运行它们。但这很愚蠢。这不是我们在 Kubernetes 中工作的方式。”-Viktor Farcic，DevOps 工具包

总体来说，使用 ArgoCD 或 Helm 钩子将迁移作为作业运行是一个可以的解决方案。但是通过现代 GitOps 原则的视角检查，会发现更多问题。

[GitOps](https://opengitops.dev/) 是一种[软件开发和部署方法论](https://thenewstack.io/getting-started-with-gitops/)，它使用 Git 作为代码和基础设施配置的中心存储库，可以实现自动化和审计的部署。

在此背景下，让我们考虑我们描述的迁移技术如何映射到两个常被接受的 GitOps 原则:

 | 原则 | 描述 |
|-|-|  
| 声明性 | 由 GitOps 管理的系统必须以声明方式表达所需状态。 |
| 持续协调 | 软件代理持续观察实际系统状态,并尝试应用所需状态。 |

*来源: [https://opengitops.dev/](https://opengitops.dev/)*

**声明性** - 当今行业使用的几乎所有迁移工具都采用命令式的版本化方法。数据库的期望状态从未描述过，而是通过按顺序应用所有迁移脚本推断出来的。这意味着这些工具无法以 GitOps 应该能够处理的方式来处理目标环境的任何未预见或手动更改。

**持续协调** - Kubernetes 作业处理失败的方式非常简单:蛮力重试。如果迁移失败，作业 Pod 将崩溃，Kubernetes 将尝试再次运行它(带有退避策略)。这可能有效，但在大多数情况下，迁移工具并未设计用于[处理部分失败](https://atlasgo.io/blog/2023/04/10/troubleshooting-migrations%23statement-level-granularity)，重试成为一项徒劳的努力。

## Operator 模式

如果以作业形式运行迁移是满足 GitOps 原则的一个设备不足的策略，那么缺失的部分是什么?

Kubernetes 是管理无状态资源的绝佳解决方案。但是，对于许多有状态资源(如数据库)来说，将数据库的期望状态与其实际状态进行协调可能是一个复杂的任务，需要特定的领域知识。[Kubernetes Operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) 是为了帮助用户通过将这种领域知识编码为 Kubernetes 控制器来管理复杂有状态资源而引入 Kubernetes 生态系统的。

在高层次上，Operator 的工作原理是引入新的 CRD(自定义资源定义)，扩展 Kubernetes API 以描述新类型的资源，并提供控制器 - 这是运行在集群中的专门软件，它通过使用协调循环以声明式方式负责管理这些资源。

如果我们能使用合适的 Kubernetes Operator 来管理应用程序的数据库模式会怎么样?

## Atlas Operator

[Atlas Kubernetes Operator](https://atlasgo.io/integrations/kubernetes/operator) 是一个 Kubernetes 控制器，使用 Atlas 来管理您的数据库模式。Atlas Kubernetes Operator 允许您定义期望的模式并使用 Kubernetes API 将其应用到数据库中。

Atlas Operator 支持完全声明式流程，在该流程中，用户定义了数据库的期望状态，Operator 负责协调期望状态与数据库的实际状态(规划和执行 CREATE、ALTER 和 DROP 语句)。

此外，还支持更经典的版本化工作流程，在该工作流程中，将期望的数据库版本提供给 Operator，它负责协调当前和数据库的实际状态以满足该版本。

![放大镜](https://cdn.thenewstack.io/media/2024/01/46e7d7f4-atlasop.png)

使用 Kubernetes Operator 来管理我们的数据库有许多优势:

- **它使模式管理成为声明性过程**。- 这不仅满足了GitOps原则，而且对终端用户来说更简单 - 他们只需要定义想要什么，就不必多考虑如何实现。
- **它持续协调**。- 如我们所示，作业的健壮性仅限于非常基本的重试机制，但拥有长期协调循环的 Operator 有更多手段和机会推进应用程序期望状态。  
- **它在语义上更丰富**。- 作业是管理资源的一种非常不透明的方式。它们的规范大多处理运行方式而不是它们所代表的资源，它们公开的状态也不包含有关此资源的任何有意义的信息。另一方面，CRD 可以使用标准 Kubernetes 工具进行管理和操作，它们的状态可以以编程方式使用，以构建更高级的工作流程。

## 结论

在本文中，我们展示了 Kubernetes 应用程序中管理数据库模式的一些现有做法，并讨论了它们的缺点。最后，我们演示了如何使用 Operator 模式满足 GitOps 原则并推进数据库管理。
