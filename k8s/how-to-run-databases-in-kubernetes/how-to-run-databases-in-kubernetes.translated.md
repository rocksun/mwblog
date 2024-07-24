# 如何在 Kubernetes 中运行数据库

![如何在 Kubernetes 中运行数据库的特色图片](https://cdn.thenewstack.io/media/2024/07/86fab00b-cloud-7832677_1280-1024x512.jpg)

关于数据库应该在 [Kubernetes](https://thenewstack.io/kubernetes/) 中运行的争论一直是科技界的一个热门话题。普遍的观点是关于“[构建无状态应用程序](https://thenewstack.io/how-to-better-manage-stateful-applications-in-kubernetes/)”，建议数据库最适合作为云提供商的托管服务。但是，在 Kubernetes 中成功运行数据库有一些实用的设计模式。

在大多数云提供商中，卷被限制在一个 [可用区](https://thenewstack.io/use-multi-availability-zone-kubernetes-for-disaster-recovery/) (AZ) 中，这意味着数据库在设计上也被限制在该 AZ 中。大多数生产集群可能是区域性的或多 AZ 的，特别是对于无状态应用程序。使用节点选择器来确保数据库 Pod 位于其卷可以挂载的 AZ 中非常重要。

示例：

```yaml
nodeSelector: topology.kubernetes.io/zone: europe-west6-b
```

此配置指定数据库 Pod 应该在“*europe-west6-b*” AZ 中运行。

**规划资源使用情况**

由于我们的数据库被限制在一个 AZ 中，因此我们必须仔细规划节点到 AZ 的设计，以避免调度错误和不可用问题。一种有效的策略是专门为数据库工作负载运行单独的节点组或节点池。这确保了在所需的 AZ 中始终有足够的资源可用。

示例：

- 为数据库工作负载创建一个专用节点池。
- 使用污点和容忍度来确保只有数据库 Pod 被调度到这些节点上。

```yaml
# 污点节点专用于数据库
spec:
  taints:
  - key: "dedicated"
    value: "database"
    effect: "NoSchedule"

# DB Pod spec 中的容忍度
spec:
  tolerations:
  - key: "dedicated"
    operator: "Equal"
    value: "database"
    effect: "NoSchedule"
```

**高可用性**

托管数据库服务通常提供内置的高可用性和故障转移功能。为了在 Kubernetes 中实现类似的弹性，必须仔细规划恢复和可用性策略。以下是两种方法：

**使用 Kubernetes 运算符：**

像 Zalando Postgres Operator 这样的 Kubernetes 运算符提供了高级功能，例如只读副本和自动故障转移，类似于托管数据库服务。这些运算符可以显着简化数据库高可用性的设置和管理。

Zalando Postgres Operator 允许您指定只读副本的数量并自动管理故障转移。此运算符提供了一个 UI，您可以在其中配置这些设置，使其成为在 Kubernetes 中管理数据库高可用性的直观且强大的工具。这里有一个 [列表](https://operatorhub.io/?category=Database) 其他一些运算符，其中一些由其各自的社区管理

**自助服务方法：**

对于那些更喜欢动手操作的人，特别是对于 NoSQL 数据库，以下是一个分步方法：

- **将数据卷挂载到两个 Pod 上：**确保数据卷可供主 Pod 和辅助 Pod 访问。
- **Pod 亲和性：**使用 Pod 亲和性规则来确保主 Pod 和辅助 Pod 放在一起，同时尊重卷约束。
- **初始化容器：**在启动时，在辅助 Pod 中使用初始化容器将所有数据从主 Pod 复制过来。
- **卷挂载约束：**将辅助 Pod 上的卷挂载设置为只读，以防止数据损坏。
- **使用 cronjob 重启**: 创建一个简单的 CronJob，每六个小时删除旧的 Pod，允许初始化容器运行并复制新数据。

**示例配置**

以下示例展示了如何使用 Pod 亲和性、用于数据复制的初始化容器以及具有只读约束的挂载卷来设置 Neo4j 只读副本，以确保数据完整性。

```yaml
affinity:
  podAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
    - labelSelector:
        matchExpressions:
        - key: app
          operator: In
          values:
          - primary-db
      topologyKey: "kubernetes.io/hostname"
initContainers:
- name: copy-data
  image: busybox
  command: ["sh", "-c", "cp -r /data/* /backup/"]
  volumeMounts:
  - name: data-volume
    mountPath: /data
  - name: backup-volume
    mountPath: /backup
volumes:
- name: data-volume
  persistentVolumeClaim:
    claimName: primary-db-pvc
- name: backup-volume
  persistentVolumeClaim:
    claimName: secondary-db-pvc
containers:
- name: secondary-db
  image: neo4j:latest
  volumeMounts:
  - name: backup-volume
    mountPath: /data
    readOnly: true
```

**备份和恢复**

...
许多服务提供商提供在基于磁盘的卷上安排定期快照的方法。这通常是首选方法，因为它更容易设置，并且恢复过程更快。在这种情况下，我们可以定期备份托管 DB 数据的卷。

另一种方法是结合数据库的专有工具，例如 PostgreSQL 的 pg_dump。

以下是用 Kubernetes Cron Jobs 将 PostgreSQL 备份到 s3 的配置示例：

```yaml
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: postgres-backup
spec:
  schedule: "0 0 * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup
            image: postgres
            command: ["sh", "-c", "pg_dumpall -c -U $PGUSER | gzip > /backup/db_backup.gz && aws s3 cp /backup/db_backup.gz s3://your-bucket/db-backup-$(date +\%F).gz"]
            volumeMounts:
            - name: backup-volume
              mountPath: /backup
          restartPolicy: OnFailure
          volumes:
          - name: backup-volume
            emptyDir: {}
```

**总结**

尽管初始设置或学习曲线可能很陡峭，但在 Kubernetes 中运行您的数据库提供了很多优势。一个鲜为人知的优势是成本。在 RDS 中运行 db.m4.2xlarge（4 个 vCPU，32GB 内存）实例的成本约为每月 1200 美元，而运行类似大小的 EC2 实例的成本约为每月 150 美元。Kubernetes 中的节点很可能还会运行多个 Pod，从而进一步优化资源使用。

供应商无关性是许多人在 Kubernetes 中运行数据库的另一个关键动机。在任何平台上以最小的调整移动您的工作负载非常有吸引力。

总之，在决定在哪里运行您的生产数据库之前，请考虑利弊。许多人成功地在 Kubernetes 中运行他们的数据库，并且此类部署的数量每天都在增长。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。