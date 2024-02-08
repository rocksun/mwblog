<!--
title: 在Kubernetes上运行Airflow两年后的收获
cover: https://miro.medium.com/v2/resize:fit:828/format:webp/0*JTTieAmia-NxICig.jpg
-->

通过这篇文章，我想分享我们部署的重要方面，这些方面帮助我们实现了一个可伸缩、可靠的环境。我希望如果你现在开始在生产环境中使用 Airflow，或者想评估一些不同的想法并将它们融入你的用例中，这会对你有所帮助。

> 译自 [What we learned after running Airflow on Kubernetes for 2 years](https://medium.com/@aleexmagno/what-we-learned-after-running-airflow-on-kubernetes-for-2-years-0537b157acfd)。作者 Alexandre Magno Lima Martins 。

Apache Airflow 是我们数据平台中最重要的组件之一，由业务内不同的团队使用。它驱动着我们所有的数据转换、欺诈检测机制、数据科学倡议，以及在 Teya 运行的许多日常维护和内部任务。

整体来看，我们的生产环境中有超过 **300 个 DAG**，在平均**每天运行超过 5,000 个任务**。所以我想说，我们拥有一个中等规模的 Airflow 部署，能够为我们的用户提供价值。现在已经有超过 8 个月，我们在 Airflow 中没有发生过任何事故或失败。

通过这篇文章，我想分享我们部署的重要方面，这些方面帮助我们实现了一个可伸缩、可靠的环境。我希望如果你现在开始在生产环境中使用 Airflow，或者想评估一些不同的想法并将它们融入你的用例中，这会对你有所帮助。

我将根据形成我们当前 Airflow 实现的关键方面来分割它：

1. 执行器选择
2. 解耦和动态 DAG 生成
3. 微调配置
4. 通知、报警和可观测性

## 执行器选择

在这里，我们所有的东西都在 Kubernetes 中运行。因此，在 Airflow 的情况下也不会有什么不同。起初，执行器的选择似乎很明显：让我们使用 [Kubernetes Executor](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/executor/kubernetes.html)！拥有运行时隔离、通过利用 Kubernetes 实现无缝任务扩展性以及更少的需要管理的组件（例如不需要 Celery 后端，比如 Redis），所有这些优势听起来都很不错。这就是我们开始这段旅程的方式。

然而，在我们的堆栈中有一个重要特点：大部分任务都是**轻量级的** [DBT](https://docs.getdbt.com/docs/introduction) 增量转换，很少有长时间运行的模型（大约 1 小时左右）。

我们面临的第一个问题是**启动任务的开销**。由于 KubernetesExecutor 在单独的 Pod 中运行每个任务，有时候**初始化 Pod 的等待时间比任务本身的运行时间还要长**。由于我们有许多小任务，我们不得不不断等待 Kubernetes 节点的扩展，以容纳增加的 Pod 数量。

第二个问题，也是导致更多痛苦的问题，是一些任务（尤其是长时间运行的任务）由于 Pod 被驱逐而导致意外失败。随着任务数量的激增，Pod 的数量以及集群中节点的数量也随之增加，一旦任务完成，系统就准备好再次缩减规模。

![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*BEmuO9olRrzT1yp7k-kRBQ.png)

*快速缩放问题*

问题进一步加剧了，因为我们在 k8s 集群中使用 [Karpenter](https://karpenter.sh/) 来优化资源使用情况。因此，几个 Pod 完成后，节点的缩减速度非常快。这种行为是将这些节点上剩余的 Pod 驱逐出去，重新分配给其他节点，从而减少总节点数并节省成本。

## CeleryExecutor 来拯救

考虑到这一切，我们决定转向老牌的 [Celery Executor](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/executor/celery.html)。现在有了固定的工作节点，它完全符合我们有许多小而快速任务的用例。**DBT 作业的平均运行时间显著减少**，因为现在我们不必等待它初始化。

通过使用 Airflow 的官方最新 [Helm Chart](https://github.com/apache/airflow/tree/main/chart)，我们可以从 [KEDA 自动缩放器](https://github.com/apache/airflow/blob/main/chart/templates/workers/worker-kedaautoscaler.yaml)中受益，根据需要增加或减少 celery 工作节点的数量，因此我们不必为空闲的工作节点支付额外费用。它的工作原理是获取 Airflow 数据库中运行和排队任务的数量，[然后根据您的工作并发配置相应地调整工作节点的数量](https://github.com/apache/airflow/blob/6daceb844c53a4e6c94b516d4f77e684a7de5b7f/chart/values.yaml#L583-L589)。

对于需要更多资源的自定义作业，我们可以选择使用 `KubernetesPodOperator` 运行它们。因此，我们仍然可以针对特定依赖项进行运行时隔离（无需将它们安装在 Airflow 的映像中），并且可以为每个任务定义单独的资源请求的好处。

目前，我们仍在考虑采用 `KubernetesCeleryExecutor`，因为它可以使作业在两个独立的队列中进行调度 —— k8s 队列和 Celery 队列。对于一些作业更适合 Celery，而另一些更适合 Kubernetes 的情况，这可能是有益的。

## 解耦和动态 DAG 生成

数据工程团队并不是唯一编写 Airflow DAG 的团队。为了适应个别团队编写自己 DAG 的情况，我们需要一种 DAG 的多仓库方法。但同时，保持一致性并强制执行准则也很重要。

### 支持 DAG 的多仓库方法

DAG 可以在各自团队拥有的不同仓库中开发，并最终出现在同一个 Airflow 实例中。当然，这是不需要将 DAG 嵌入到 Airflow 镜像中的。

相信我，你不想在 DAG 中的一行代码发生变化时就重启调度器和工作节点。

![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*rH1httJXN8IFawKg8w-krA.png)

*去中心化的 DAG 仓库*

每个 DAG 最终都会通过 `sync` 过程出现在一个桶中，这个过程相对于拥有这些 DAG 的团队的特定路径进行。

为使这种方法有效，一个非常重要的部分是强制执行 CI/CD 的防护措施。每个 DAG 名称必须**以拥有它的团队为前缀**，这样我们就可以避免冲突的 DAG ID。此外，对每个 DAG 进行静态检查，以验证正确的所有者分配和标签的存在，捕获可能的导入错误等。

通过这样做，我们可以使用原生 Airflow 角色来强制访问控制，并且每个 DAG 必须通过**最低的治理检查清单**才能提交。

### 但是，如何将 DAG 同步到 Airflow 中呢？

为了使 DAG 在 Airflow 中反映出来，我们需要将存储桶的内容与运行调度器、工作节点等的 Pod 的本地文件系统进行同步。为了实现这一点，我们正在使用 Objinsync，这是一个轻量级守护程序，用于将远程对象存储增量同步到本地文件系统。

我们在每个 Airflow 组件 Pod 中都运行 [objinsync](https://github.com/scribd/objinsync) 作为一个边缘容器，频繁进行同步。因此，我们总是能够在几分钟内捕获 DAG 的新更新。一个教训是还要将 objinsync 添加为一个 init 容器，这样它可以在主调度器或工作节点容器启动之前进行 DAG 的同步。这在特别重要的 Celery 工作节点上得到了证明 —— 由于节点轮换或发布而重新启动后，有时会将任务分配给尚未获取 DAG 的新工作节点，导致立即失败。

![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*ipSEF5hOqYgBySKu3CYEAg.png)

理想的做法是在调度器中**只运行一个** `objinsync` 进程作为边缘容器，并将存储桶内容复制到[持久卷](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)中。这样 PV 将被挂载到所有 Airflow 组件中。这样做的好处是 DAG 在不同的 Airflow 组件之间永远不会出现不同步的情况。

不幸的是，我们目前还无法在这里实现该解决方案，因为我们目前**仅支持集群节点的 EBS 卷**。要在不同节点上挂载 PV，我们需要 ReadWriteMany [访问模式](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes)。目前，只有在使用 **EFS 卷模式**时，**AWS EKS** 才支持这种模式。

鉴于我们的限制，一个解决方法是使用 [nodeSelector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) 将所有 Airflow Pod 调度到同一个节点上。然而，我们选择了更倾向于具有高可用性的 Airflow 部署 —— 通过使用不同可用区的节点。

### 动态生成 DAG 时要小心

如果您想要大规模生成 DAG，就需要利用 DAG 模板化和编程生成。不再需要手动编写每个 DAG。

也许最简单的动态生成 DAG 的方法是使用单文件方法。您有一个文件，在循环中生成 DAG 对象，并将它们添加到 globals() 字典中。

当我们首次根据我们的 DBT 项目生成动态 DAG 时，这种方法非常直接（DBT 编排的主题需要单独发布，将在未来完成）。然而，由于 DAG 在调度器中定期解析，我们观察到当使用这种方法时，**CPU 和内存使用量增加**，**调度器循环时间变长**。特别是因为该过程需要解析 DBT manifest.json 文件，这是一个相当大的文件 。因此，鉴于我们项目的规模，这种方法很快就被证明不可扩展。

解决方案是转向多文件方法，我们为想要动态创建的每个 DAG 生成一个 .py 文件。通过这样做，我们将 DAG 生成过程纳入了我们的 DBT 项目存储库中。项目现在成为 DAG 的另一个生成者，将动态生成的文件推送到 DAG 存储桶中。

Astronomer 在此处有一篇关于单文件方法和多文件方法的精彩文章。

## 调优配置

当我们转向 CeleryExecutor 时，尽管解决了其中一个问题，但新问题开始出现。几天后（甚至几个小时），我们的一些 Celery 工作节点开始因为 **OOM（内存耗尽）**问题而死亡。我们为 Pod 提供了足够的内存资源，所以有些不太对劲。

经过调查，这是我们在 Celery 工作节点资源使用图表上看到的情况。

![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*WvrhXvUWujNvQAxOTkhsxg.png)

Celery 工作节点中的内存泄漏

我们的任务很小，主要由 Celery 工作节点执行的 DBT 作业组成。当时，这种几乎持续增加的内存使用量让我们感到困惑。我们开始怀疑任务之间存在内存泄漏。

为了防止内存泄漏，同时控制任务的内存使用情况，我们必须对两个重要的 Celery 配置进行调优：`worker_max_tasks_per_child` 和 `worker_max_memory_per_child` 。

第一个配置控制一个工作进程在被新进程替换之前可以执行的最大任务数。首先，我们需要理解 Celery 工作节点和工作进程之间的区别。一个工作节点可以生成**多个工作进程**，这由并发设置控制。例如，如果并发设置为 **12** ，有 **2 个 Celery 工作节点**，那么就会有 **24 个工作进程**。

因此，为了避免同一工作进程中任务之间的内存泄漏，最好定期对其进行循环使用。如果未设置此配置，则默认情况下不会对**工作进程进行循环使用**。

第二个配置，`worker_max_memory_per_child` ，控制着单个工作进程执行之前可执行的最大驻留内存量，之后会被新的工作进程替换。本质上，这控制着任务的内存使用情况。默认情况下也**没有限制**，所以建议始终设置它。

通过调整这两个配置，我们在两个时刻通过回收工作进程来控制内存使用情况：如果它们达到了最大任务数，或者达到了最大驻留内存量。需要注意的是，这些配置只在使用预分配池时才有效。有关更多信息，请参阅官方文档。

在 Airflow 中设置它们非常简单。您只需要更新 Airflow 的 `config_templates` 文件夹中的默认 Celery 配置，如下所示：

```python
# config_templates/custom_celery.py 
from airflow.config_templates.default_celery import DEFAULT_CELERY_CONFIG 

CUSTOM_CELERY_CONFIG = DEFAULT_CELERY_CONFIG.copy() 
CUSTOM_CELERY_CONFIG.update( 
{ "worker_max_tasks_per_child": <int>, 
"worker_max_memory_per_child": <int>, 
} 
)
```

然后您在 values.yaml 中指向这个自定义配置

```yaml
airflow: 
  config: 
    celery: 
      worker_concurrency: <int> 
      celery_config_options: config_templates.custom_celery.CUSTOM_CELERY_CONFIG
```

您为这些配置使用的具体值将取决于您的工作节点配置、内存请求/限制、并发级别以及您的任务有多大内存密集型。这就是为什么您需要根据您的具体设置进行调优。

## 准备好进行节点轮转

k8s 节点可能会在遇到故障或由管理 Kubernetes 集群的基础设施团队设置的计划节点轮转时进行轮转。此外，工作节点（Pod）在发生发布、更改某些配置（如环境变量）或基础镜像时也会进行轮转。节点轮转当然会导致 Pods 被终止。

我们需要为这些事件做好准备，并确保我们的任务不会因为 Pod 被停用而简单失败。这对于长时间运行的任务尤其痛苦。想象一下运行一个 2–3 小时的作业，结果由于计划的节点轮转而失败。

为了防止这种情况发生，根据您的个人需求设置好 Worker Termination Grace Period 配置是很重要的。该配置会使 celery worker 在被发布流程或节点轮转关闭之前等待多达那么多秒。这也可以很容易地在 Airflow 的 charts `values.yaml` 中设置：

```yaml
airflow: 
  workers: 
    terminationGracePeriodSeconds: <int>
```

**建议将其设置为您最长运行任务平均完成时间的** 1.5 倍。这样，我们就可以确保每个任务都在此期间内完成，工作节点可以优雅地关闭。

## 通知、报警和监控

### 统一您公司的通知

Airflow 最常见的用例之一是在特定任务事件后发送自定义通知，例如处理文件、清理作业，甚至是任务失败。如果您在一个多个团队使用 Airflow 的环境中工作，您应该**统一通知机制**。

这样可以避免 `A 团队`从 Airflow 发送的 Slack 消息与 `B 团队`完全不同格式的消息，例如。

自 Airflow 2.6 开始，我们可以使用 [Notifiers](https://docs.astronomer.io/learn/error-notifications-in-airflow#notifiers) 来管理这个。社区已经提供了一套预构建的通知器，以满足最常见的用例：Slack、SQS、Jira 等。

在这里，我们从 BaseNotifier 类创建了自己的自定义通知器，这样我们就可以根据需要定制通知模板并嵌入自定义行为。例如，在开发环境中运行任务时，默认仅将失败通知发送到 Slack。在 prd 环境中，通知将发送到我们的在线工具 Opsgenie。

![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*e46hmTeCn1PnQeLrzku2EQ.png)

*一个通知器，多个目标和定制*

自定义通知也是可模板化的，因此团队可以使用标准格式在 Slack 中创建信息消息，例如。这种方法的另一个优点是，使用它的各个团队不需要担心管理各个通知目标的密码。

### 做第一个发现故障的人

即使我们实施了高可用性的最佳实践和模式，Airflow 仍可能由于许多原因而失败。这就是为什么基础架构级别的可观测性、指标和报警非常重要的原因。

在 Kubernetes 中运行时，您可以通过为每个感兴趣的事件设置 PrometheusRule 来实现。例如，要监视调度器节点的健康状况、可用工作节点的数量，甚至要监视特定的 Airflow 指标，如调度器循环时间。通过同时运行 [AlertManager](https://prometheus.io/docs/alerting/latest/alertmanager/)，您可以向各种感兴趣的目标（Slack、PagerDuty、Opsgenie 等）发出警报。

另一个明智的做法是利用 Airflow 指标来提高环境的可观测性。在撰写本文时，Airflow 支持将指标发送到 `StatsD` 和 `OpenTelemetry`。后者优于前者，因为 `OpenTelemetry` 是一个更完整的框架，还支持日志和跟踪。然而，目前 Airflow 还不支持通过 OTEL 进行日志和跟踪（但未来会支持！）。

另外，如果您想使用它，您需要在 Kubernetes 中管理 OTEL Collector 的部署（这是官方的 [helm chart](https://opentelemetry.io/docs/kubernetes/helm/collector/)）。与 statsd 不同，官方的 Airflow chart 不提供 OTEL Collector。

![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*nhsE7ljrDyVBYxo8Yg604g.png)

标准指标可以大大改善警报功能。例如，您可以使用排队任务的总数，并设置在特定时间内队列增加太多时触发警报的阈值 —— 您不希望队列比 SLA 时间更长，例如。

我们监控的其他有用指标包括 DAG 解析时间和调度器循环时间，以便快速识别可能影响 Airflow 核心并减慢整个应用程序的问题。

### 注意 Airflow 的元数据

元数据数据库是成功实现 Airflow 的关键部分，因为它可能会影响其性能，甚至导致 Airflow 崩溃。

除了上述监控 Airflow 节点和性能指标之外，监控**数据库健康指标**也至关重要。这可能会因您使用的是 PostgreSQL 还是 MySQL 而有所不同（请不要使用 SQLite），但最常见的指标包括 **CPU 使用率、可用存储空间、打开的连接数**等。

另一个良好的实践是定期运行**元数据清理作业**，以删除旧的和未使用的元数据。这可能包括诸如 `job`、`dag_run`、`task_instance`、`log`、`xcom`、`sla_miss`、`dags`、`task_reschedule`、`task_fail` 等表。所有这些元数据都在 Airflow 内部不断累积，使得获取任务状态等查询的平均时间变得比必要的时间更长。此外，您是否曾经感觉到 Airflow 在加载和导航时非常缓慢？元数据的累积可能是造成这种情况的原因。

幸运的是，Airflow 提供了一个本地命令，即 `airflow db clean`，可通过可选标志配置其行为。详细了解请点击[此处](https://airflow.apache.org/docs/apache-airflow/stable/howto/usage-cli.html#purge-history-from-metadata-database)。

如果您正在使用 Kubernetes，则可以在 Airflow 的图表中设置一个 CronJ`ob 作为额外的资源，定期运行带有您指定的标志的 `airflow db clean` 命令。根据您的实施规模，您可能需要每天或每周运行一次。

## 结论

希望这篇文章能为使用 Kubernetes 上的 Airflow 而启程的团队带来一些启发，尤其是在一个更具协作性的环境中，多个团队在同一个 Airflow 集群上进行使用。

这里没有提及许多其他组件和细节，它们对于成功实施也是至关重要的。我们仍有很多地方需要改进，还有很长的路要走。如果您也想分享自己的经验或提出问题，请随时与我联系，让我们聊聊。
