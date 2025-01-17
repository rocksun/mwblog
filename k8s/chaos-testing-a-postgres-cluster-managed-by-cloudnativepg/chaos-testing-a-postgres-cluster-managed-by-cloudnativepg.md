
<!--
title: 云原生PG管理的PostgresSQL集群混沌测试
cover: https://coroot.com/wp-content/uploads/2025/01/chaos-testing.png
-->

深入研究在 Kubernetes 上由 CloudNativePG 管理的 PostgreSQL 集群的混沌测试。学习如何有效地测试高可用性并使用 Coroot 监控性能。#混沌工程 #Postgres #Kubernetes #可观测性

> 译自 [Chaos testing a Postgres cluster managed by CloudNativePG](https://coroot.com/blog/engineering/chaos-testing-a-postgres-cluster-managed-by-cloudnativepg/)，作者 Nikolay Sivko。

随着越来越多的组织将其数据库迁移到云原生环境，有效地管理和监控这些系统变得至关重要。根据Coroot的匿名使用统计数据，64%的项目使用PostgreSQL，使其成为我们用户中最流行的关系数据库管理系统（RDBMS），而使用MySQL的项目仅占14%。这并不令人意外，因为它也是全球使用最广泛的开源数据库。在Coroot，我们努力提供流畅的PostgreSQL监控体验，无论您是在AWS RDS、裸机服务器、专用EC2实例还是Kubernetes上运行数据库。

Kubernetes不仅仅是一个运行容器化应用程序的平台。它还通过其Operator框架允许自动化备份、高可用性和扩展等任务，从而实现更好的数据库管理。这提供了类似于使用AWS RDS等托管服务的管理体验，但没有厂商锁定，并且成本通常更低。

Coroot已经支持大多数流行的Kubernetes Postgres Operator，例如[Zalando的Operator](https://coroot.com/blog/engineering/chaos-testing-of-a-postgres-cluster-managed-by-the-zalando-postgres-operator/)、[Percona Operator](https://www.percona.com/blog/troubleshooting-postgresql-on-kubernetes-with-coroot/)和[Stackgres](https://coroot.com/blog/engineering/chaos-testing-kubernetes-operators-for-postgres-stackgres/)。但是，如果没有CloudNativePG，列表就不完整，所以让我们解决这个问题。

[CloudNativePg](https://github.com/cloudnative-pg/cloudnative-pg)是一个开源Operator，最初由EDB创建，EDB是全球历史最悠久、规模最大的Postgres厂商。与其他Operator一样，CNPG帮助管理Kubernetes上的PostgreSQL数据库，涵盖从初始部署到持续维护的整个生命周期。值得一提的是，这是市场上最新的Postgres Operator，但其开源影响力正在迅速增长，根据我的观察，它是Reddit用户最喜欢的Operator。

在这篇文章中，我将在我的实验室中安装一个CNPG集群，用Coroot对其进行监控，然后生成一些负载并引入一些故障，以确保高可用性和可观测性。

## 设置集群

安装CloudNativePG Operator很简单：

```bash
helm repo add cnpg https://cloudnative-pg.github.io/charts
helm upgrade --install cnpg cnpg/cloudnative-pg
```

要部署集群，请创建一个Kubernetes自定义资源：

```yaml
kind: Cluster
metadata:
  name: pg-cluster
spec:
  instances: 3
  primaryUpdateStrategy: unsupervised
  storage:
    size: 30Gi
  postgresql:
    shared_preload_libraries: [pg_stat_statements]
    parameters:
      pg_stat_statements.max: "10000"
      pg_stat_statements.track: all
  managed:
    roles:
    - name: coroot
      ensure: present
      login: true
      connectionLimit: 2
      inRoles:
      - pg_monitor
    passwordSecret:
      name: pg-cluster
---
apiVersion: v1
data:
  username: ******==
  password: *********==
kind: Secret
metadata:
  name: pg-cluster
type: kubernetes.io/basic-auth
```

正如您所看到的，我已经启用了`pg_stat_statements`扩展，并创建了一个名为“coroot”的角色来收集Postgres指标。

## 安装Coroot

在这篇文章中，我将使用Coroot社区版，但企业版的安装步骤非常[相似](https://docs.coroot.com/quick-start/enterprise)。

以下是安装Kubernetes的Coroot Operator以及所有Coroot组件的命令：

```bash
helm repo add coroot https://coroot.github.io/helm-charts
helm repo update coroot
helm install -n coroot --create-namespace coroot-operator coroot/coroot-operator
helm install -n coroot coroot coroot/coroot-ce
```

要访问Coroot，我将Coroot UI端口转发到我的本地机器。对于生产部署，Operator可以创建Ingress。

```bash
kubectl port-forward -n coroot service/coroot-coroot 8083:8080
```

在UI中，我们可以看到两个应用程序：Operator (*cnpg-cloudnative-pg*)和我们的Postgres集群(*pg-cluster*)。Coroot还识别出*pg-cluster*是一个Postgres数据库，并建议集成Postgres监控。

Coroot利用eBPF来监控应用程序和数据库之间的Postgres查询，无需任何额外的集成。虽然这种方法提供了数据库性能的高级视图，但它缺乏了解数据库内部*为什么*出现问题所需的可见性。

为了弥合这一差距，Coroot还从Postgres系统视图（如`pg_stat_statements`和`pg_stat_activity`）收集统计信息，补充基于eBPF的指标和跟踪。

![](https://coroot.com/wp-content/uploads/2025/01/Screenshot-2025-01-13-at-12.28.58-2-2048x668.png)

Kubernetes监控数据库的方法通常涉及在数据库实例Pod中运行指标导出器作为sidecar容器。但是，这种方法对于某些用例来说可能具有挑战性。例如，CNPG不支持运行自定义sidecar容器，并且它们的[CNPG-i](https://github.com/cloudnative-pg/cnpg-i)功能需要特定的插件支持，并且仍处于实验阶段。为解决这些限制，Coroot 有一个专用的 *coroot-cluster-agent*，它可以发现并收集数据库的指标，而无需为每个数据库实例单独创建一个容器。要配置此集成，只需使用已为 Coroot 创建的数据库角色的凭据。在 Coroot UI 中点击“Postgres”，然后点击“配置”按钮。

![](https://coroot.com/wp-content/uploads/2025/01/Screenshot-2025-01-13-at-12.33.19-2-2048x920.png)

接下来，在集群规范中提供为 Coroot 配置的凭据。Coroot 的集群代理将从集群中的每个实例收集 Postgres 指标。我们在集群创建期间启用的 *pg_stat_statements* 扩展已经设置好了，因此无需手动步骤。由于 Coroot 了解 Kubernetes 应用程序的动态特性，它会自动检测所有实例，即使您添加更多副本也是如此。

![](https://coroot.com/wp-content/uploads/2025/01/Screenshot-2025-01-13-at-12.33.44-2-2048x1336.png)

就是这样！在一分钟内，我们的 Postgres 集群将由 Coroot 完全监控。这不仅仅是在 Prometheus 中有一些 Postgres 指标。我们现在拥有所有内容：指标、日志、跟踪、概要文件、仪表板和预定义的检查，这些检查会自动突出显示任何性能问题或数据库不可用情况。

![](https://coroot.com/wp-content/uploads/2025/01/Screenshot-2025-01-13-at-12.44.42-2-1536x1040.png)

这很好，但是如果没有负载或问题，感觉有点枯燥。让我们添加一个与该数据库交互的应用程序。

![](https://coroot.com/wp-content/uploads/2025/01/Screenshot-2025-01-13-at-13.38.30-2-1536x931.png)

我部署了一个名为“app”的简单应用程序，它每秒执行大约 600 个查询：300 个在主实例上，300 个在两个副本上。Coroot 使用 eBPF 收集这些查询的统计信息，无需更改代码。因此，我们可以跟踪请求数量及其延迟。此外，通过基于 eBPF 的跟踪，我们可以识别特定的查询，这对于分析延迟异常特别有用。只需选择热图上的一个区域即可查明哪些查询速度慢。

![](https://coroot.com/wp-content/uploads/2025/01/Screenshot-2025-01-13-at-13.45.04-1-1536x1082.png)

我相信任何可观测性解决方案都必须在故障情况下进行测试，以确保如果出现某些问题，我们将能够快速识别根本原因。所以，让我们引入一些故障🔥🔥🔥。

## 故障1：CPU嘈杂邻居

在像 Kubernetes 集群这样的共享基础设施中，应用程序经常争夺资源。让我们模拟一个有“嘈杂邻居”的场景，其中一个 CPU 密集型应用程序与我们的数据库实例运行在同一节点上。以下作业将在 *node100* 上创建一个带有 *stress-ng* 的 Pod：

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: cpu-stress
spec:
  template:
    metadata:
      labels:
        app: cpu-stress
    spec:
      nodeSelector:
        kubernetes.io/hostname: node100
      containers:
      - name: stress-ng
        image: debian:bullseye-slim
        command:
        - "/bin/sh"
        - "-c"
        - |
          apt-get update && \
          apt-get install -y stress-ng && \
          stress-ng --cpu 0 --timeout 300s
  restartPolicy: Never
```

![](https://coroot.com/wp-content/uploads/2025/01/Screenshot-2025-01-14-at-14.02.49-1-1536x1046.png)

正如我们所看到的，我们的“嘈杂邻居”影响了 Postgres 的性能。现在，让我们假设我们不知道根本原因，并使用 Coroot 来识别问题。

![](https://coroot.com/wp-content/uploads/2025/01/Screenshot-2025-01-14-at-14.11.28-1-1536x1149.png)

首先，Coroot 标记了 CPU 问题。通过了解系统的模型，Coroot 只关注与特定应用程序相关的节点，在本例中为 Postgres。我们的数据库实例运行在三个节点上：*node100*、*node101* 和 *node102*。这意味着即使在具有许多节点的集群中，Coroot 也只突出显示相关的节点。

使用 CPU 延迟图表，我们可以观察到 *pg-cluster-2* 正在经历 CPU 时间短缺。为什么？因为 *node100* 过载了。那是为什么？*cpu-stress* 应用程序消耗了所有可用的 CPU 时间。

很简单，对吧？

## 故障#2：Postgres锁定

现在，让我们探索一个特定于 Postgres 的故障场景。我们将在包含 1000 万行的 *articles* 表上运行一个次优的模式迁移：

```sql
ALTER TABLE articles ALTER COLUMN body SET NOT NULL;
```

对于那些不熟悉数据库的人来说，此迁移将锁定整个表以验证所有行都不为 *NULL*。由于表相对较大，因此迁移可能需要一些时间才能完成。在此期间，来自我们应用程序的查询将被迫等待，直到释放锁。

![](https://coroot.com/wp-content/uploads/2025/01/Screenshot-2025-01-14-at-15.02.04-2-1536x704.png)

Coroot 已检测到一个 Postgres 实例的问题。让我们再次假设我们不知道根本原因，并使用 Coroot 来识别它。

![](https://coroot.com/wp-content/uploads/2025/01/Screenshot-2025-01-14-at-15.02.44-1-1536x1243.png)

让我们一起解释这些图表：*pg-cluster-2* 的 Postgres 延迟显着增加。许多 *SELECT* 和 *INSERT* 查询被另一个查询锁定。哪个？*ALTER TABLE* 查询。为什么此查询需要这么长时间才能执行？因为它正在执行 I/O 操作以验证每一行中的 body 列是否不为 *NULL*。

如您所见，在这种情况下，拥有正确的指标至关重要。例如，仅仅知道 Postgres 锁的数量并不能帮助我们识别持有锁的特定查询。这就是为什么在 Coroot，我们喜欢进行这样的实验，以确保我们的产品能够快速准确地查明根本原因。

## 故障#3：主Postgres实例故障

现在，让我们看看 CloudNativePG 如何处理主实例故障。为了模拟此故障，我将简单地删除主 Postgres 实例的 Pod。

```bash
kubectl delete pod pg-cluster-2
```

![](https://coroot.com/wp-content/uploads/2025/01/Screenshot-2025-01-14-at-16.36.31-1-1536x998.png)

操作员检测到故障并启动了切换，将*pg-cluster-1*提升为新的主节点。在Coroot中，我们可以清楚地观察到集群发生了什么，并看到恢复查询处理大约花费了3分钟。

## 结论

CloudNativePG和Coroot是运行和监控Kubernetes上的PostgreSQL的绝佳组合。CloudNativePG负责数据库管理的繁重工作，例如备份和故障转移，而Coroot则使一切保持可见并易于排查故障。两者结合，可以轻松应对实际问题，并确保您的数据库在云原生环境中平稳运行。

准备好体验具有高级Postgres监控功能的全面可观测性吗？免费试用[Coroot社区版](https://coroot.com/docs/coroot/quick-start/community)，或开始免费试用[Coroot企业版](https://coroot.com/account/signup)以获得高级功能。

如果您喜欢Coroot，请在[GitHub](https://github.com/coroot/coroot)上给我们一个⭐。

有任何问题或反馈？请在[Slack](https://join.slack.com/t/coroot-community/shared_invite/zt-1gsnfo0wj-I~Zvtx5CAAb8vr~r~vecyw)上联系我们。
