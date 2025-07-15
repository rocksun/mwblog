在 Kubernetes 上运行和管理有状态工作负载（如数据库）是出了名的困难。声明式模型可以清晰地映射到管理 Pod 和 Secrets 之类的对象，这些对象可以被替换和交换，但对于必须在不关闭的情况下演进的对象（如您最喜欢的 PostgreSQL 实例）则不然。值得庆幸的是，Kubernetes 生态系统中最近的一些发展最终使管理此类工作负载成为可能。

资源管理的核心是维护系统的期望状态。对于现代云原生应用程序，此状态可能非常复杂。

即使是小型团队也可以管理数千个不同的资源，包括 VPC、安全组、EC2 实例、Kubernetes 对象、负载均衡器、密钥、数据库、CI/CD 管道等等。这不再仅仅是在某些服务器上“运行应用程序”。它协调着一个庞大的、相互依赖的组件生态系统，每个组件都有自己的生命周期、配置和约束。

这种复杂性的爆发对许多人来说是个坏消息。它增加了配置漂移的风险，使[可观测性和故障排除](https://thenewstack.io/kubernetes-troubleshooting-primer/)更加复杂，并为跨环境的状态不一致创造了更多机会。各团队都在努力保持所有移动部件的同步，尤其是在他们扩展时。

这些挑战催生了现在主导云原生世界的新范例。令人惊讶的是，这些现代实践背后的核心灵感之一来自于一个不太可能的地方：您的空调。

## 为什么 Kubernetes 数据库管理以前是不可能的

乍一听可能有些奇怪，但空调为现代基础设施管理中的强大模式提供了一个非常好的心智模型。

让我们来分解一下。空调不仅仅吹冷风，它还维持一个期望状态：目标温度。为此，它运行一个简单但有效的反馈回路：

* 温控器持续感应当前温度。
* 控制器将其与期望温度进行比较。
  如果存在差异，它会触发系统以增加或减少冷却，或者根本不冷却。

没有人会坐在那里每隔几分钟手动调整旋钮。系统自主运行，响应环境中的变化，并不断努力使其与目标保持一致。

这就是所谓的协调循环的本质，它是大规模管理复杂基础设施的最成功模型之一的基础。

一旦您了解了空调的隐喻，您就会开始在任何地方看到协调循环，尤其是在云基础设施中：

* 自动伸缩组：持续监控 CPU 或内存使用率等指标，并添加或删除实例以维持目标利用率。
* 断路器：跟踪服务调用中的错误率，并在超过故障阈值时调整路由或拒绝请求，然后在条件稳定时恢复。
* Kubernetes 控制器：监控声明资源（如 Deployments 或 StatefulSets）中的更改，并自动协调系统以确保一致性。

这种模型——定义期望状态、观察实际状态并协调差异——可以很好地扩展。

我见过具有数千个节点和数万个 Pod 的集群运行生产工作负载，所有这些都通过协调循环连接在一起。没有人通过 SSH 进入节点来重启失败的服务。没有人[运行临时脚本](https://thenewstack.io/want-real-time-run-scripts-inside-the-database/)来重新平衡流量。系统持续观察、反应和自我修复。

这就是控制循环的魔力：它们不仅仅是自动化，它们还是自主的。

它们为我们提供了能够响应故障、安全处理更改并不断向前发展的基础设施，而无需在每个步骤中进行持续监督。

## 空调模型：协调循环如何改变一切

但是，与软件中的所有美好事物一样……有一个问题。

协调循环对于无状态基础设施非常有效。这就是为什么 Kubernetes 擅长管理 Pod、服务和配置等资源。需要更新您的应用程序吗？只需更改镜像标签，Kubernetes 就会启动新的 Pod，等待它们变为健康状态，并优雅地替换旧的 Pod。滚动更新、回滚、健康检查——全部内置。它既优雅又安全，而且无需人工干预。

但是，当应用于有状态资源时，此模型开始崩溃。

Kelsey Hightower 等行业资深人士长期以来一直在警告这一点。在 Kubernetes 上运行状态，尤其是像生产数据库这样的关键状态，会带来一组非常不同的问题。

让我们举个例子：假设您有一个运行 PostgreSQL 16 实例的 Pod，现在您想升级到版本 17。

您该怎么办？

* 关闭旧的 Pod？那会造成停机。
* 启动一个带有 17 镜像的新 Pod，并将其指向同一个 PVC？有风险——数据格式可能已更改。

希望一切顺利？可能不是您的 SRE 团队会认可的策略。

如果您深入了解 PostgreSQL 升级说明——或者有幸在生产环境中这样做——您会发现安全、零停机的升级通常涉及精心编排的序列。一种常见的策略如下所示：

1. 在现有实例（例如，v16）旁边配置一个新的 PostgreSQL 实例（例如，v17）。
2. 在新实例上预先创建兼容的架构。由于逻辑复制要求架构匹配，因此必须在复制开始之前完成此步骤。
3. 设置从旧实例到新实例的逻辑复制，实时捕获更改。
4. 监控复制延迟并等待其降至零。
5. 将流量切换到新实例——通常通过更新连接字符串或在故障转移设置中提升新节点。

此过程是经过深思熟虑且高度可控的。尝试将这种升级塞入无状态滚动更新模型中——例如用新镜像替换 Pod——不仅幼稚，而且很危险。

再举一个例子：模式迁移。

每次您的应用程序演进时，您的[数据模型也可能需要](https://thenewstack.io/what-are-time-series-databases-and-why-do-you-need-them/)随之增长。也许您正在添加一列、更改类型或重组表。如果架构与新的应用程序版本不兼容，某些查询可能会开始失败，从而导致运行时错误、功能损坏甚至中断。

那么，如果我们尝试将相同的无状态滚动更新模型应用于数据库架构更改会发生什么？

让我们想象一下：您修改了您的应用程序，现在您想“推出”一个新的架构版本。您可能会想到——就像 Deployments 一样——启动一个具有更新架构的新数据库 Pod，等待它变为健康状态，然后切换流量并删除旧的 Pod。

但是数据库不是无状态 Pod。

一个具有“正确”架构的全新数据库可能看起来很健康，直到您意识到它是空的，因为没有迁移任何数据。

尝试将该新架构直接应用于现有数据库？这通常会完全失败——也许表已存在，或者列冲突阻止了更改的进行。即使它确实成功了，它也可能会悄悄地破坏某些东西：也许删除了一个列或添加了一个约束，现在您的[应用程序在实际流量下抛出运行时](https://thenewstack.io/kubernetes-for-developers-with-a-distributed-app-runtime/)错误。

与无状态工作负载不同，您不能只重试失败的部署。数据库拥有持久的、不可逆转的状态。架构迁移通常不是幂等的，并且设计不佳的迁移可能会[使您的系统](https://thenewstack.io/edgeless-systems-brings-confidential-computing-to-kubernetes/)崩溃——或者更糟，在没有立即显示症状的情况下损坏数据。

更糟糕的是，传统的 Kubernetes 模式——例如在 init 容器中运行迁移或将它们捆绑到应用程序启动中——会引入竞争条件，创建脆弱的部署，并使其难以观察、验证或回滚发生的事情。

即使做得好，这些方法也依赖于预先编写的、线性的 DDL 语句序列——单向更改的固定计划。这从根本上不同于协调循环。没有感知、没有差异、没有对当前状态的反应。它是命令式的，而不是声明式的。

显然，我们需要一个不同的模型。

## Kubernetes Operators：数据库管理的颠覆者

如果协调循环对于无状态基础设施如此有效，那么问题是：我们能否将相同的想法扩展到有状态资源？

这正是 Kubernetes Operator 模式旨在实现的目标。

Operators 是专门构建的控制器，它们扩展了 Kubernetes 以管理复杂的、特定于领域的、有状态的资源，如数据库、消息队列或存储系统。它们将[操作知识编码到软件中](https://thenewstack.io/how-to-cut-through-a-thicket-of-kubernetes-clusters/)，从而实现如何安装、配置、升级和监控这些系统，同时保持期望状态。

换句话说，它们将协调引入到有状态世界。

## 每个 Operator 的核心

Operator 模式的核心是两个 Kubernetes 原语：

* 自定义资源定义 (CRD)：这些使用新的资源类型扩展了 Kubernetes API。就像 Deployment 或 Service 一样，您可以定义一个 PostgresCluster、KafkaTopic，或者在我们的例子中，一个 DatabaseSchema。CRD 允许您描述 Kubernetes 本身不了解的事物的期望状态。
* 控制器：这些是监控自定义资源并采取行动的代理。它们监控系统的实际状态，将其与 CRD 中定义的期望状态进行比较，并执行必要的操作来协调两者。

CRD 和控制器共同形成了一个自愈循环，用于以前需要手动干预或脆弱脚本的任务。

就像 Deployment 控制器协调 Pod 一样，Operator 可以协调 PostgreSQL 集群、Kafka 主题甚至数据库架构的状态。

与 shell 脚本或 CI 作业不同，Operators 可以做出决策。它们不仅仅是执行——它们观察、计划并对环境做出反应。

## CloudNativePG 和 Atlas：生产就绪的数据库解决方案

现在我们了解了 Operator 模式的强大功能，让我们看看如何将其应用于一个真实的用例：在 Kubernetes 上管理 PostgreSQL 架构更改——以声明式、安全且零脚本的方式进行。

我们将使用两个强大的 Kubernetes 原生工具：

* [CloudNativePG (CNPG)](https://cloudnative-pg.io/): 用于在 Kubernetes 上运行 PostgreSQL 集群的生产级 Operator。它处理配置、复制、故障转移甚至备份。
* [Atlas Operator](https://atlasgo.io/): 来自 Ariga 的架构管理 Operator，它引入了 AtlasSchema CRD，允许您声明您的期望架构并以安全、策略感知的方式自动应用更改。

这些工具共同使您能够以 GitOps 原生的方式管理您的数据库基础设施和架构生命周期。

让我们逐步完成设置。

## 分步指南：在 Kubernetes 上实现声明式架构管理

第 0 步：安装 CloudNativePG 并创建一个集群

首先，安装 [CloudNativePG operator](https://cloudnative-pg.io/) 并启动一个 PostgreSQL 集群。

添加 Helm 仓库并安装 operator：

```
bash
CopyEdit
helm repo add cnpg https://cloudnative-pg.github.io/charts
helm repo update
helm install cnpg cnpg/cloudnative-pg
```

接下来，定义您的集群。将以下内容另存为 cluster.yaml：

```
yaml
CopyEdit
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: cluster-example
spec:
  instances: 1
  imageName: ghcr.io/cloudnative-pg/postgresql:15
  storage:
    storageClass: standard
    size: 1Gi
```

应用它：

```
bash
CopyEdit
kubectl apply -f cluster.yaml
```

这将：

* 创建一个名为 app 的 PostgreSQL 数据库。
* 配置一个名为 app 的用户。
* 生成一个名为 cluster-example-app 的 Kubernetes Secret，其中包含凭据。
* 在 cluster-example-rw.default 公开一个读/写服务。

一旦 Pod（例如 cluster-example-1）启动并运行，您就可以继续了。

**第 1 步：安装 Atlas Operator**

现在通过 Helm 安装 Atlas Operator：

```
bash
CopyEdit
helm install atlas-operator oci://ghcr.io/ariga/charts/atlas-operator
```

您现在应该在您的集群中看到已注册的 Atlas CRD：

```
kubectl get crd | grep atlas
```

输出：

```
atlasmigrations.db.atlasgo.io
atlasschemas.db.atlasgo.io
```

**第 2 步：应用架构**

使用 AtlasSchema 资源以声明方式定义您的数据库架构。将以下内容另存为 atlas-schema.yaml：

```
yaml
CopyEdit
apiVersion: db.atlasgo.io/v1alpha1
kind: AtlasSchema
metadata:
  name: atlasschema-pg
spec:
  credentials:
    scheme: postgres
    host: cluster-example-rw.default
    user: app
    passwordFrom:
      secretKeyRef:
        key: password
        name: cluster-example-app
    database: app
    port: 5432
    parameters:
      sslmode: disable
  schema:
    sql: |
      create table t1 (
        id int
      );
```

应用它：

```
bash
CopyEdit
kubectl apply -f atlas-schema.yaml
```

检查协调状态：

```
bash
CopyEdit
kubectl get atlasschemas.db.atlasgo.io
```

预期输出：

```
pgsql
CopyEdit
NAME               READY   REASON
atlasschema-pg     True    Applied
```

**第 3 步：验证和演进**

您可以直接验证结果：

```
kubectl exec -ti cluster-example-1 -- psql app
```

在 psql shell 中：

```
\dt
\d t1
```

要演进您的架构，只需编辑清单中的 sql: 字段——例如，添加一个列：

```
create table t1 (
  id int,
  name text
);
```

然后重新应用：

```
kubectl apply -f atlas-schema.yaml
```

Atlas operator 将检测差异并安全地应用迁移。

这为您提供了完全声明式的架构管理，具有：

* 通过 Kubernetes Secrets 内置访问数据库凭据。
* 架构协调由 operator 持续处理。
* 没有命令式迁移脚本或手动步骤。

一种真正的 GitOps 原生架构更改管理方法。

## 主要要点

* 协调循环是云原生基础设施的支柱。它们对于无状态资源非常有效——并且通过 Operator 模式，它们也可以用于有状态资源。
* 在 Kubernetes 中，管理数据库等有状态系统的传统方法会崩溃。像 init 容器、CI 作业和手动脚本之类的工具与我们期望的声明式、自主模型不一致。
* Operators 将 Kubernetes 的强大功能带给有状态系统。借助 CRD 和控制器，您可以像管理 Deployments 和 Services 一样管理复杂的资源——如 PostgreSQL 集群和架构。
* Atlas 和 CloudNativePG 使端到端、对 GitOps 友好的数据库管理成为可能。从配置到迁移，您现在可以通过 Kubernetes 原生工作流程完全表达和演进您的数据库基础设施和架构。

## 为什么这很重要

随着 Kubernetes 成为一切的控制平面，状态不能成为例外。

长期以来，数据库一直被视为不可触碰的雪花——与我们其余的基础设施自动化隔离。但是，要实现真正现代、可扩展和可重复的系统，我们必须将它们集成到我们用于其他所有内容的相同工作流程中。

Operator 模式——以及像 Atlas 这样的工具——有助于使这一愿景成为现实。

是时候对所有（有状态的）事物进行操作了。