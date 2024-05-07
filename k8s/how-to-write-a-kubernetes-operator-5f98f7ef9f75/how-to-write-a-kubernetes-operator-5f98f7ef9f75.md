
<!--
title: 如何编写Kubernetes Operator
cover: ./cover.png
-->

编写 Kubernetes(K8s)  operator 的意图在我心中不断增长。我开始阅读文章、探索 GitHub 存储库，并就此咨询我的同事。虽然我不能说它完全成功，但这个意图仍然存在。

> 译自 [How to Write a Kubernetes Operator](https://itnext.io/how-to-write-a-kubernetes-operator-5f98f7ef9f75)，作者 Payam Qorbanpour。

作为一名每天都与 Kubernetes 打交道的后端开发人员，我一直希望编写一个 operator 来扩展我的知识边界。然而，障碍出现了，阻碍了我实现这一目标。

这就是我在服兵役期间编写 [gobackup-operator](https://github.com/gobackup/gobackup-operator) 的故事。*tl;dr*：直接跳到“深入项目”部分

## 磨刀不误砍柴工

编写 Kubernetes(K8s)  operator 的意图在我心中不断增长。我开始阅读文章、探索 GitHub 存储库，并就此咨询我的同事。虽然我不能说它完全成功，但这个意图仍然存在。

所有这些努力的结果是我 [GitHub 帐户](https://github.com/payamQorbanpour) 中存储的一系列教程项目。

我应该提到，大约一年前，当我第一次接触 Kubernetes 时，练习过程就开始了。我首先观看了 [Guru 的教程](https://www.pluralsight.com/cloud-guru/courses/certified-kubernetes-application-developer-ckad) 以了解 CKAD，然后观看了 [Nana 的 YouTube 教程](https://www.youtube.com/watch?v=X48VuDVv0do&ab_channel=TechWorldwithNana) 。

## 化为灰烬

我被派去服兵役。

那里没有互联网连接，甚至没有一个电子设备。相反，我们只有精装书、排球以及迷人的日出和日落美景来娱乐我们。

在这种情况下，创建 operator 的想法正在逐渐消失。我所关心的一切就是吃饭、看书和享受偶尔的自由（假期）。然而，有时这种自由是短暂的，正如指挥官曾经评论的那样：

> 假期的快乐在你离开营房的那一刻就结束了。

训练课程结束了，我开始在办公室担任一名雇员，但那里也感受到了互联网连接的缺乏！在晚上，我离开办公室，从事我热爱的工作。有时，你在有限的时间内会有更好的表现。因此，从下午 4 点到晚上 9 点，我必须创造一些特别的东西。对我来说，它确实很特别！

## 不鸣则已

毕竟，在 [此系列](https://www.codereliant.io/build-kubernetes-operator-kubebuilder/) 的帮助下，我设法从教程中编写了另一个 Kubernetes  operator  :) 但这一次，它有所不同。

我的同事已经开发了一个备份系统，但它似乎运行得不太好。因此，他们探索了另一种解决方案，并遇到了一个名为 [gobackup](https://gobackup.github.io/) 的项目，该项目旨在定期备份数据库并将它们推送到存储中。问题是该项目不包括对 etcd 数据库的支持。因此，他们决定通过添加 etcd 支持来满足要求，从而[为该项目做出贡献](https://github.com/gobackup/gobackup/pull/225)。这最终导致了一个新的[版本](https://github.com/gobackup/gobackup/releases/tag/v2.10.0)。

在我缺席期间，他们决定在此基础上开发一个 Kubernetes  operator 。这对我是重要的一步。当他们与我分享时，我急切地检查了该项目，并想，“终于，就是它了。 operator 即将创建。耶！”

在阅读该项目时，我注意到该项目的自述文件中存在一个问题。其中一个链接指向 404 页面。我主动修复了这个问题并提交了一个拉取请求。

[所有者](https://github.com/huacnlee) 欣然接受了它。:)

遇到如此开放的态度后，我的一个同事建议我们可以将此 operator 放在 [gobackup 组织](https://github.com/gobackup) 下，以便更多的人可以为其开发做出贡献。

我打开了一个 [问题](https://github.com/gobackup/gobackup/issues/231) 并提出了 [gobackup 组织](https://github.com/gobackup) 下的一个存储库，并且仍然存在合作的开放性。

白天，我在军队服役，晚上，我致力于 gobackup-operator 项目。

## 深入项目

我首先设置我的环境。

幸运的是，我已经在计算机上安装了 Golang、Docker 和 kubectl。通过之前的实践，我已熟悉本地机器 Kubernetes 集群（如 Kind）和用于创建 operator 的工具（如 kubebuilder）。

因此，我启动了 operator 代码。

```
$ kubebuilder init --domain gobackup.io --repo github.com/gobackup/gobackup-operator
```

然后我继续为 operator 创建 API：

```
$ kubebuilder create api --group gobackup --version v1 --kind Backup
Create Resource [y/n]
y
Create Controller [y/n]
y
```

数据库和存储也是如此：

```
$ kubebuilder create api --group database.gobackup --version v1 --kind PostgreSQL
Create Resource [y/n]
y
Create Controller [y/n]
y

$ kubebuilder create api --group storage.gobackup --version v1 --kind S3
Create Resource [y/n]
y
Create Controller [y/n]
y
```

## 修改 API

我根据项目的具体要求修改了 API：

```go
// Backup is the Schema for the backups API
type Backup struct {
 metav1.TypeMeta   `json:",inline"`
 metav1.ObjectMeta `json:"metadata,omitempty"`

 Spec   BackupSpec   `json:"spec,omitempty"`
 Status BackupStatus `json:"status,omitempty"`

 BackupModelRef BackupModelRef `json:"backupModelRef,omitempty"`
 StorageRefs    []StorageRef   `json:"storageRefs,omitempty"`
 DatabaseRefs   []DatabaseRef  `json:"databaseRefs,omitempty"`
}
```

然后修改 Reconcile 方法

```go
//+kubebuilder:rbac:groups=gobackup.io,resources=backups,verbs=get;list;watch;create;update;patch;delete
//+kubebuilder:rbac:groups=gobackup.io,resources=backups/status,verbs=get;update;patch
//+kubebuilder:rbac:groups=gobackup.io,resources=backups/finalizers,verbs=update
func (r *BackupReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
 // reconcile implementation
}
```

## 测试

在对其进行测试之前，你需要准备一个可供备份的测试数据库。因此，使用 gobackup-operator-postgres-deployment.yaml 文件创建 PostgreSQL 部署：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres-deployment
spec:
  selector:
    matchLabels:
      app: postgres
  replicas: 1
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:14.11
        env:
        - name: POSTGRES_USER
          value: ""
        - name: POSTGRES_PASSWORD
          value: ""
        - name: PGDATA
          value: "/var/lib/postgresql/data/pgdata"
        volumeMounts:
        - mountPath: /var/lib/postgresql/data
          name: postgredb
      volumes:
      - name: postgredb
        persistentVolumeClaim:
          claimName: postgres-pvc
```

请记住在清单中修改 `POSTGRES_USER` 和 `POSTGRES_PASSWORD` 并应用它：

```
kubectl apply -f example/gobackup-opetator-postgres-deployment.yaml,
example/gobackup-opetator-postgres-service.yaml
```

此外，我还添加了一些资源在 Kubernetes 集群中进行测试，包括部署、角色、集群角色、服务帐户等，所有这些都可以在 gobackup-operator/example/ 目录中找到。

因此，应用这些清单以添加基本资源：

```
kubectl apply -f example/gobackup-opetator-serviceaccount.yaml,
gobackup-opetator-pvc.yaml,
gobackup-opetator-namespace.yaml,
gobackup-opetator-clusterrolebinding.yaml,
gobackup-opetator-clusterrole.yaml
```

然后是存储和数据库清单：

```
kubectl apply -f example/gobackup-opetator-storage/*
kubectl apply -f example/gobackup-opetator-database/*
```

使用以下清单，我能够在我的本地机器上运行该 operator ：

```
kubectl apply -f example/gobackup-opetator-deployment.yaml
```

因此，每当创建或更改 Backup 或 CronBackup 对象时， operator 都会执行必要的任务。

要创建备份模型以设置备份配置：

```
kubectl apply -f example/gobackup-opetator/gobackup-opetator-backupmodel.yaml
```

应用 gobackup-operator/example/gobackup-operator 目录中的清单之一（备份或 cronbackup）将触发 operator 运行备份：

```
kubectl apply -f example/gobackup-opetator/gobackup-opetator-cronbackup.yaml
```

## 结论

起初，我对在自述文件中做出如此小的更改感到尴尬。感觉就像你为了参与 Hacktoberfest 提交而做出的那些 PR 之一。

但后来我考虑到了它的有效性。即使是那些单行提交也产生了影响。谁知道呢，如果我没有对 README 文件进行更改，我可能就不会创建这个 operator 。

*一小步也重要！*

欢迎随时查看并做出贡献[此处](https://github.com/gobackup/gobackup-operator)。如果你需要更改 README 文件，请不要犹豫。;)
