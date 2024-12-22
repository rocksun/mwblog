# 为什么每个平台工程师都应该关注 Kubernetes Operators

发表于

在我最近的一次演讲中，我提到一个成功的基于[Kubernetes](/kubernetes)的平台的基础是使用[Kubernetes Operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)，因为它们是自动化 Kubernetes 上复杂应用程序和服务的运维任务和生命周期的好方法。

如果您错过了演讲，这里是录像链接：\[录像链接]

演讲结束后，我收到了听众的反馈，他们希望了解更多关于 Kubernetes operators 的信息，以及一些我推荐在其 Kubernetes 平台中使用的高级 operators。而我怎么会拒绝这样一个与社区分享知识的大好机会呢？

正如您所料，Kubernetes Operator 的基础是 Kubernetes。因此，如果您不熟悉 Kubernetes，让我简要介绍一下。Kubernetes，简称 K8s，是目前为止最强大的开源容器编排平台——尤其是在其维护期望状态的能力方面。这意味着您作为平台管理员，可以定义您希望集群及其上的工作负载是什么样子，而 Kubernetes（又名控制平面）则执行必要的步骤，使用反馈循环来确保达到期望状态。

Kubernetes 如何实现这种复杂的运维任务管理？Kubernetes 利用了控制器和 operators 的概念。两者都确保集群资源处于期望状态。但是为什么 Kubernetes 生态系统中控制器和 operators 之间会有区别呢？当人们谈论控制器和 operators 时，也存在很大的混淆，因为差异在于细节，而 operators 是控制器的子类别。

## Kubernetes 控制器与 Operators

K8s 控制器是控制循环，它们监视您的资源并将当前状态与期望状态在连续循环中协调。想想您家中的恒温器是如何工作的。恒温器监视当前温度，如果低于期望温度，则打开加热器。如果高于期望温度，则关闭加热器。这就是 Kubernetes 中控制器的工作方式——它监视资源和期望状态中定义的条件，并执行必要的步骤以确保当前状态与期望状态匹配。

以下是控制循环中维护、观察和执行循环的一部分典型的 Kubernetes 控制器关键功能：

| 功能 | 描述 |
|---|---|
| 滚动部署和回滚 | 部署控制器负责推出应用程序的新版本，并在发生故障时回滚到以前的版本。 |
| 集群维护 | 节点控制器监视集群中的节点，并确保节点处于期望状态。 |
| 事件处理 | 事件控制器监视事件并根据事件采取行动。 |
| 调度 | 用于在特定时间运行作业和 cron 作业的控制器。 |
| 资源强制 | 资源控制器监视资源使用情况并在命名空间中强制执行资源限制。 |
| 状态强制 | 不同的控制器监视资源的状态并强制执行期望状态。 |

如您所见，控制器自动化例行运维任务，强制执行策略，处理故障并采取行动以持续维护集群的期望状态。

控制器的一些典型用例是：

* **限制资源使用** - 通过使用 ResourceQuota 等控制器强制执行资源限制来防止集群过载。
* **自动缩放** - 使用 HorizontalPodAutoscaler 根据不同的指标自动缩放 Pod 的数量。
* **任务调度** - 使用 Job 和 CronJob 控制器在特定时间运行作业和 cron 作业。
* **运行有状态工作负载** - 通过确保 Pod 按特定顺序创建并具有稳定的网络标识，使用 StatefulSet 控制器部署和管理数据库等有状态工作负载。
* **扩展部署** - 使用 Deployment 控制器部署和管理无状态工作负载（如 Web 应用程序），通过确保运行所需的 Pod 数量并处理滚动更新和回滚。

如您所见，控制器减少了平台工程团队的手动工作，并赋予集群自我管理能力。

综上所述，控制器的优势是显而易见的——让我列出一些主要的优势：

### EDITOR'S RESPONSE
**自动化** - 控制器自动化例行操作任务并执行策略。**可用性** - 控制器确保资源始终可用，处理故障并采取措施维护所需状态。**效率** - 控制器通过配额管理和自动扩展提供了一种高效管理集群中资源和工作负载的方法。**可靠性** - 控制器通过副本管理、[pod](/registry/packages/kubernetes/api-docs/core/v1/pod/)创建和删除以及调度等功能，帮助提高工作负载管理的可靠性。**灵活性** - 控制器提供了一种灵活的方式来处理集群中的各种工作负载和资源，例如[DaemonSet](/registry/packages/kubernetes/api-docs/apps/v1/daemonset/)、[StatefulSet](/registry/packages/kubernetes/api-docs/apps/v1/statefulset/)、[jobs](/registry/packages/kubernetes/api-docs/batch/v1/job/)、[cron jobs](/registry/packages/kubernetes/api-docs/batch/v1/cronjob/)、[deployments](/registry/packages/kubernetes/api-docs/apps/v1/deployment/)和[services](/registry/packages/kubernetes/api-docs/core/v1/service/)。**可观察性** - 控制器通过[Kubernetes API](/blog/yaml-terraform-pulumi-whats-the-smart-choice-for-deployment-automation-with-kubernetes/#kubernetes-components-and-the-kubernetes-api)提供对集群资源和资源状态的视图。

在解释完控制器之后，让我们继续讨论 Kubernetes 中下一级别的自动化，并谈谈 Kubernetes Operators。

## Kubernetes Operators

如前所述，Kubernetes Operators 是控制器的子类别，它使用 API 扩展（自定义资源）来完成自动化任务。Operators 是一组独立的控制器，每个控制器负责自己的任务。虽然控制器可以与控制器共享类似的功能，但它只关注一个领域，并且只使用自定义资源来管理该领域。

请记住，控制器无需自定义资源或与特定领域的链接即可工作。

Operators 是自定义构建的控制器，专注于特定应用程序或服务的部署、管理和操作。Operators 的一些关键功能包括：

功能 | 描述
---|---|
安全 | Operators 集成安全最佳实践和策略，例如加密、访问控制和


Operators 是一种将平台工程团队的操作知识编码到自动化控制器中的好方法。这样，平台工程团队可以专注于战略任务，让 Operators 处理枯燥的例行操作任务。这减少了人工工作量并提高了平台的可靠性。

Operators 的一些典型用例是：

**数据库管理** - 部署和管理数据库，例如 MySQL、PostgreSQL 和 MongoDB。**存储管理** - 部署和管理存储，例如 Ceph、GlusterFS 或 NFS。**日志和监控** - 简化日志和监控解决方案（如 Prometheus、Grafana 或 ELK stack）的部署和管理。**CI/CD** - 自动化 CI/CD 管道的部署和管理，例如 Jenkins、GitLab 或 Tekton。**备份和恢复** - 自动化应用程序和数据的备份和恢复。**消息和事件流** - 简化消息和事件流解决方案（如 Kafka、RabbitMQ 或 NATS）的部署和管理。**机器学习** - 自动化机器学习工作负载（如 TensorFlow、PyTorch 或 Kubeflow）的部署和管理。

通过 Operators 提供的以应用程序为中心的方法，平台工程团队现在可以实现完全自动化的操作，同时提高平台的可靠性、效率和可观察性，并确保遵守最佳实践和合规性要求。

与控制器类似，Operators 也具有明显的优势：

**简化** - Operators 通过提供声明式方式（通过自定义资源）简化了复杂应用程序和服务的部署和管理。**更高的生产力** - Operators 通过自动化例行操作任务并允许用户专注于交付业务价值来提高平台工程团队的生产力。**可扩展性** - 使用自定义资源定义 (CRD) 扩展 K8s API 允许管理员支持新的应用程序和服务，而无需更改核心 Kubernetes 代码。**一致性** - Operators 确保它们在不同的环境（例如本地、云或混合环境）中一致地部署和运行应用程序和服务。**模块化** - Operators 是模块化的，并且专注于特定领域。**遗留转型** - Operators 通过自动化复杂应用程序的部署和管理来帮助将遗留应用程序转换为云原生应用程序。

这是一个 Kubernetes Operator 运行的可视化表示，我发现它非常好用：
![Kubernetes Operators：它们是什么？一些示例  来源：SparkFabrik](/blog/why-every-platform-engineer-should-care-about-kubernetes-operators/operator.png)
Kubernetes Operators：它们是什么？一些示例  来源：SparkFabrik

## Kubernetes控制器和Operators的比较

以下是Kubernetes控制器和Operators之间差异的快速总结：

| 特性 | Kubernetes控制器 | Kubernetes Operators |
|---|---|---|
| 定义 | Kubernetes内部的核心控制循环，用于将当前状态与资源的期望状态协调一致。 | 具有特定领域逻辑的自定义构建的控制器，通常使用自定义资源定义 (CRD) 扩展Kubernetes API。 |
| 范围 | 用于集群范围资源管理和工作负载操作的通用自动化。 | 专注于应用程序或服务特定的生命周期管理和操作。 |
| 自定义资源 (CRD) | 不是必需的。大多数控制器都使用内置的Kubernetes资源，例如Pod、Deployment和StatefulSets。 | 必需的。Operators依赖于CRD来定义和管理特定于应用程序的资源。 |
| 特定领域逻辑 | 有限的。主要关注通用的Kubernetes操作，例如调度、缩放和资源强制执行。 | 广泛的。包括特定于应用程序的任务，例如备份、升级、迁移和灾难恢复。 |
| 自动化 | 自动执行操作任务，例如资源调度、缩放和维护集群状态。 | 自动执行操作和特定于领域的的任务，通常对特定应用程序的深入操作知识进行编码。 |
| 复杂性 | 由于专注于Kubernetes原生工作流，因此相对较低的复杂性。 | 由于特定于领域的实现以及与外部系统的集成，因此复杂性较高。 |
| 可观察性 | 通过Kubernetes API和内置事件提供对集群资源状态的洞察。 | 通过针对受管应用程序定制的特定于应用程序的指标、日志和运行状况检查来增强可观察性。 |
| 用例 | - Pod缩放（例如，HPA）<br>- 资源强制执行（例如，ResourceQuota）<br>- 滚动更新和回滚<br>- 调度作业（例如，CronJob）。 | - 数据库管理（例如，MySQL Operator）<br>- CI/CD管道（例如，Tekton）<br>- 备份和恢复<br>- 监控解决方案（例如，Prometheus Operator）<br>- 有状态应用程序（例如，Kafka Operator）。 |
| 部署 | Kubernetes核心组件或kube-controller-manager等扩展的一部分。 | 由供应商、社区或内部开发的外部工具，使用自定义资源部署。 |
| 主要优点 | - 集群范围的自动化<br>- 确保资源可用性<br>- 高效可靠的工作负载管理。 | - 简化应用程序生命周期管理<br>- 通过特定于领域的自动化提高生产力<br>- 跨环境的一致部署。 |
| 灵活性 | 对于通用的Kubernetes操作很灵活，但仅限于内置资源。 | 对于自定义应用程序和特定于领域的的要求非常灵活和可扩展。 |
| 目标受众 | 寻求自动化Kubernetes原生工作流的平台管理员和Kubernetes用户。 | 需要特定应用程序或服务的先进自动化和生命周期管理的开发人员和平台工程师。 |
| 维护 | 由Kubernetes核心或社区项目管理和更新。 | 需要特定于领域的知识和定期更新，以适应应用程序更改和最佳实践。 |

通过对Kubernetes控制器和Operators的详细解释，我想分享一些我推荐在您的Kubernetes平台中使用的高级Kubernetes Operators。

## 高级Kubernetes Operators

正如我们所看到的，Kubernetes Operators是自动化操作任务和生命周期管理的首选方法。我应该提到，并非所有Operators都是一样的。一些Operators比其他Operators更高级，并提供更多功能。这就是为什么，例如，[OperatorHub.io](https://operatorhub.io/) 将Operators分为[五个能力级别](https://sdk.operatorframework.io/docs/overview/operator-capabilities/)：

* **基本安装**- 在集群上安装应用程序。
* **无缝升级**- 管理应用程序升级。
* **全生命周期管理**- 管理应用程序的全生命周期。
* **深入洞察**- 提供监控和指标。
* **自动驾驶**- 自动优化和调整应用程序。

Operator越高级，它提供的功能就越多，提供的自动化就越多。在最先进的级别“自动驾驶”中，Operator会根据工作负载和环境自动优化和调整应用程序。

以下是我推荐在您的Kubernetes平台中使用的高级Kubernetes Operators列表：

### CloudNativePG Operator
![CloudNativePG Operator 来源：cloudnative-pg.io](/blog/why-every-platform-engineer-should-care-about-kubernetes-operators/cloudnativepg.png)
CloudNativePG Operator 来源：cloudnative-pg.io
[CloudNativePG 运算符](https://cloudnative-pg.io/) 是一个 PostgreSQL 运算符，涵盖了 Kubernetes 上 PostgreSQL 数据库的完整生命周期。它通过提供一种声明式的方式来定义和管理 PostgreSQL 集群（使用自定义资源），简化了 PostgreSQL 数据库的部署、管理和扩展。

CloudNativePG 运算符的一些关键特性包括：

**自动备份** - 计划和管理 PostgreSQL 数据库的备份。**高可用性** - 部署和管理高可用性 PostgreSQL 集群。**扩展** - 根据工作负载扩展 PostgreSQL 实例的数量。

#### 安装

使用 Helm chart 或 Kubernetes 清单文件部署 CloudNativePG 运算符：

```bash
helm repo add cloudnative-pg https://cloudnative-pg.io/charts/
helm repo update
helm upgrade --install cloudnativepg cloudnative-pg/cloudnative-pg --namespace cnpg-system --create-namespace
```

或使用 Pulumi 部署 CloudNativePG 运算符：

```typescript
import * as k8s from "@pulumi/kubernetes";
import * as k8shelm from "@pulumi/kubernetes/helm/v3";
const ns = new k8s.core.v1.Namespace("cnpg-system", {
    metadata: {
        name: "cnpg-system",
    },
});
new k8shelm.Release("cloudnativepg", {
    chart: "cloudnative-pg/cloudnative-pg",
    namespace: ns.metadata.name,
    createNamespace: true,
});
```

```javascript
"use strict";
const k8s = require("@pulumi/kubernetes");
const k8shelm = require("@pulumi/kubernetes/helm/v3");
const ns = new k8s.core.v1.Namespace("cnpg-system", {
    metadata: {
        name: "cnpg-system",
    },
});
new k8shelm.Release("cloudnativepg", {
    chart: "cloudnative-pg/cloudnative-pg",
    namespace: ns.metadata.name,
    createNamespace: true,
});
```

```python
import pulumi_kubernetes as k8s
import pulumi_kubernetes.helm.v3 as k8shelm
import pulumi_kubernetes.meta.v1 as meta

ns = k8s.core.v1.Namespace(
    "cnpg-system",
    meta.ObjectMetaArgs(
        name="cnpg-system",
    ),
)
release = k8shelm.Release(
    "cloudnativepg",
    chart="cloudnative-pg/cloudnative-pg",
    namespace=ns.metadata["name"],
    create_namespace=True,
)
```

```go
package main

import (
	"github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	apiv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apiextensions"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		ns, err := corev1.NewNamespace(ctx, "cnpg-system", &corev1.NamespaceArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("cnpg-system"),
			},
		})
		if err != nil {
			return err
		}
		_, err = helmv3.NewRelease(ctx, "cloudnativepg", &helmv3.ReleaseArgs{
			Chart:          pulumi.String("cloudnative-pg/cloudnative-pg"),
			Namespace:      ns.Metadata.Name().Elem(),
			CreateNamespace: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}
		return nil
	})
}
```

```csharp
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using System.Collections.Generic;
using Pulumi.Kubernetes.ApiExtensions;

class MyStack : Stack
{
    public MyStack()
    {
        var ns = new Namespace("cnpg-system", new NamespaceArgs
        {
            Metadata = new ObjectMetaArgs
            {
                Name = "cnpg-system"
            }
        });
        var release = new Release("cloudnativepg", new ReleaseArgs
        {
            Chart = "cloudnative-pg/cloudnative-pg",
            Namespace = ns.Metadata.Apply(m => m.Name),
            CreateNamespace = true
        });
    }
}

class Program
{
    static Task<int> Main() => Deployment.RunAsync<MyStack>();
}
```

#### 使用

这是一个在与 S3 API 兼容的存储上配置备份的 PostgreSQL 集群的简单示例：

```yaml
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: cluster-example-with-backup
spec:
  instances: 3
  primaryUpdateStrategy: unsupervised
  # Persistent storage configuration
  storage:
    storageClass: standard
    size: 1Gi
  # Backup properties
  # This assumes a local minio setup
  backup:
    barmanObjectStore:
      destinationPath: s3://backups/
      endpointURL: http://minio:9000
      s3Credentials:
        accessKeyId:
          name: minio
          key: ACCESS_KEY_ID
        secretAccessKey:
          name: minio
          key: ACCESS_SECRET_KEY
    wal:
      compression: gzip
```

或使用 Pulumi：

```typescript
new k8s.apiextensions.CustomResource("cluster-example-with-backup", {
    apiVersion: "postgresql.cnpg.io/v1",
    kind: "Cluster",
    metadata: {
        name: "cluster-example-with-backup",
    },
    spec: {
        instances: 3,
        primaryUpdateStrategy: "unsupervised",
        // Persistent storage configuration
        storage: {
            storageClass: "standard",
            size: "1Gi",
        },
        // Backup properties
        backup: {
            barmanObjectStore: {
                destinationPath: "s3://backups/",
                endpointURL: "http://minio:9000",
                s3Credentials: {
                    accessKeyId: {
                        name: "minio",
                        key: "ACCESS_KEY_ID",
                    },
                    secretAccessKey: {
                        name: "minio",
                        key: "ACCESS_SECRET_KEY",
                    },
                },
                wal: {
                    compression: "gzip",
                },
            },
        },
    },
});
```
```json
{
  "apiVersion": "postgresql.cnpg.io/v1",
  "kind": "Cluster",
  "metadata": {
    "name": "cluster-example-with-backup"
  },
  "spec": {
    "instances": 3,
    "primaryUpdateStrategy": "unsupervised",
    "storage": {
      "storageClass": "standard",
      "size": "1Gi"
    },
    "backup": {
      "barmanObjectStore": {
        "destinationPath": "s3://backups/",
        "endpointURL": "http://minio:9000",
        "s3Credentials": {
          "accessKeyId": {
            "name": "minio",
            "key": "ACCESS_KEY_ID"
          },
          "secretAccessKey": {
            "name": "minio",
            "key": "ACCESS_SECRET_KEY"
          }
        },
        "wal": {
          "compression": "gzip"
        }
      }
    }
  }
}
```

```python
from pulumi_kubernetes import apiextensions
from pulumi_kubernetes.meta import v1 as meta

postgresql_cluster = apiextensions.CustomResource(
    "cluster-example-with-backup",
    api_version="postgresql.cnpg.io/v1",
    kind="Cluster",
    metadata=meta.ObjectMetaArgs(
        name="cluster-example-with-backup",
    ),
    spec={
        "instances": 3,
        "primaryUpdateStrategy": "unsupervised",
        "storage": {
            "storageClass": "standard",
            "size": "1Gi",
        },
        "backup": {
            "barmanObjectStore": {
                "destinationPath": "s3://backups/",
                "endpointURL": "http://minio:9000",
                "s3Credentials": {
                    "accessKeyId": {
                        "name": "minio",
                        "key": "ACCESS_KEY_ID",
                    },
                    "secretAccessKey": {
                        "name": "minio",
                        "key": "ACCESS_SECRET_KEY",
                    },
                },
                "wal": {
                    "compression": "gzip",
                },
            },
        },
    },
)
```

```go
package main

import (
	"github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	apiv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apiextensions"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := apiv1.NewCustomResource(ctx, "cluster-example-with-backup", &apiv1.CustomResourceArgs{
			ApiVersion: pulumi.String("postgresql.cnpg.io/v1"),
			Kind:       pulumi.String("Cluster"),
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("cluster-example-with-backup"),
			},
			Spec: kubernetes.UntypedArgs{
				"instances":           pulumi.Int(3),
				"primaryUpdateStrategy": pulumi.String("unsupervised"),
				"storage": pulumi.Map{
					"storageClass": pulumi.String("standard"),
					"size":         pulumi.String("1Gi"),
				},
				"backup": pulumi.Map{
					"barmanObjectStore": pulumi.Map{
						"destinationPath": pulumi.String("s3://backups/"),
						"endpointURL":     pulumi.String("http://minio:9000"),
						"s3Credentials": pulumi.Map{
							"accessKeyId": pulumi.Map{
								"name": pulumi.String("minio"),
								"key":  pulumi.String("ACCESS_KEY_ID"),
							},
							"secretAccessKey": pulumi.Map{
								"name": pulumi.String("minio"),
								"key":  pulumi.String("ACCESS_SECRET_KEY"),
							},
						},
						"wal": pulumi.Map{
							"compression": pulumi.String("gzip"),
						},
					},
				},
			},
		})
		if err != nil {
			return err
		}
		return nil
	})
}
```

```csharp
using Pulumi;
using Pulumi.Kubernetes.ApiExtensions.V1;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using System.Collections.Generic;

class MyStack : Stack
{
    public MyStack()
    {
        var postgresqlCluster = new CustomResource("cluster-example-with-backup", new CustomResourceArgs
        {
            ["apiVersion"] = "postgresql.cnpg.io/v1",
            ["kind"] = "Cluster",
            ["metadata"] = new Dictionary<string, object>
            {
                ["name"] = "cluster-example-with-backup"
            },
            ["spec"] = new Dictionary<string, object>
            {
                ["instances"] = 3,
                ["primaryUpdateStrategy"] = "unsupervised",
                ["storage"] = new Dictionary<string, object>
                {
                    ["storageClass"] = "standard",
                    ["size"] = "1Gi"
                },
                ["backup"] = new Dictionary<string, object>
                {
                    ["barmanObjectStore"] = new Dictionary<string, object>
                    {
                        ["destinationPath"] = "s3://backups/",
                        ["endpointURL"] = "http://minio:9000",
                        ["s3Credentials"] = new Dictionary<string, object>
                        {
                            ["accessKeyId"] = new Dictionary<string, object>
                            {
                                ["name"] = "minio",
                                ["key"] = "ACCESS_KEY_ID"
                            },
                            ["secretAccessKey"] = new Dictionary<string, object>
                            {
                                ["name"] = "minio",
                                ["key"] = "ACCESS_SECRET_KEY"
                            }
                        },
                        ["wal"] = new Dictionary<string, object>
                        {
                            ["compression"] = "gzip"
                        }
                    }
                }
            }
        });
    }
}
```

CloudNativePG Operator is a great way to deploy and manage PostgreSQL databases on Kubernetes. It simplifies various tasks including backups, high availability, and scaling, making it a must-have tool for PostgreSQL users.


Flux Operator
![Flux Operator Credit: fluxcd.control-plane.io/operator](flux-operator.png)
Flux Operator  来源：fluxcd.control-plane.io/operator

[Flux Operator](https://fluxcd.control-plane.io/operator/) is a complete self-driving solution that provides an alternative to the traditional Flux Bootstrap process. It automates the installation, configuration, and upgrades of Flux, eliminating the operational burden of managing Flux across multiple clusters.

Flux Operator's key features include:

**GitOps Deployment** - Automate the deployment of applications and services using GitOps.  **Lifecycle Management** - Manage the complete lifecycle of Flux, including upgrades and rollbacks. **Deep Insights** - Provide deep insights into the state of Flux and the applications deployed using Flux.

#### Installation
Deploy Flux Operator using a Helm chart:

```bash
helm upgrade -i flux-operator oci://ghcr.io/controlplaneio-fluxcd/charts/flux-operator --namespace flux-system --create-namespace
```
Or deploy Flux Operator using Pulumi:

```python
import * as k8s from "@pulumi/kubernetes";
import * as k8shelm from "@pulumi/kubernetes/helm/v3";
const namespace = new k8s.core.v1.Namespace("flux-system", {
metadata: {
name: "flux-system",
},
});
new k8s.helm.v3.Release("flux-operator", {
chart: "flux-operator",
version: "latest",
namespace: namespace.metadata.name,
repositoryOpts: {
repo: "oci://ghcr.io/controlplaneio-fluxcd/charts",
},
createNamespace: true,
});
```

```javascript
"use strict";
const k8s = require("@pulumi/kubernetes");
const k8shelm = require("@pulumi/kubernetes/helm/v3");
const namespace = new k8s.core.v1.Namespace("flux-system", {
metadata: {
name: "flux-system",
},
});
new k8s.helm.v3.Release("flux-operator", {
chart: "flux-operator",
version: "latest",
namespace: namespace.metadata.name,
repositoryOpts: {
repo: "oci://ghcr.io/controlplaneio-fluxcd/charts",
},
createNamespace: true,
});
```

```python
import pulumi_kubernetes as k8s
import pulumi_kubernetes.helm.v3 as k8shelm
import pulumi_kubernetes.meta.v1 as meta
namespace = k8s.core.v1.Namespace(
"flux-system",
meta.ObjectMetaArgs(
name="flux-system",
),
)
flux_operator = k8shelm.Release(
"flux-operator",
chart="flux-operator",
version="latest",
namespace=namespace.metadata["name"],
repository_opts={
"repo": "oci://ghcr.io/controlplaneio-fluxcd/charts",
},
create_namespace=True,
)
```

```go
package main

import (
	"github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	apiv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apiextensions"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		namespace, err := corev1.NewNamespace(ctx, "flux-system", &corev1.NamespaceArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("flux-system"),
			},
		})
		if err != nil {
			return err
		}
		_, err = helmv3.NewRelease(ctx, "flux-operator", &helmv3.ReleaseArgs{
			Chart: pulumi.String("flux-operator"),
			Version: pulumi.String("latest"),
			Namespace: namespace.Metadata.Name().Elem(),
			RepositoryOpts: &helmv3.RepositoryOptsArgs{
				Repo: pulumi.String("oci://ghcr.io/controlplaneio-fluxcd/charts"),
			},
			CreateNamespace: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}
		return nil
	})
}
```

```csharp
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using System.Collections.Generic;
using Pulumi.Kubernetes.ApiExtensions;

var namespaceFluxSystem = new Namespace("flux-system", new NamespaceArgs
{
    Metadata = new ObjectMetaArgs
    {
        Name = "flux-system",
    },
});

var fluxOperator = new Release("flux-operator", new ReleaseArgs
{
    Chart = "flux-operator",
    Version = "latest",
    Namespace = namespaceFluxSystem.Metadata.Apply(metadata => metadata.Name),
    RepositoryOpts = new RepositoryOptsArgs
    {
        Repo = "oci://ghcr.io/controlplaneio-fluxcd/charts",
    },
    CreateNamespace = true,
});

class Program
{
    static Task<int> Main() => Deployment.RunAsync<MyStack>();
}
```

#### Usage
Here's an example of a FluxInstance Custom Resource that defines a Flux instance:

```yaml
apiVersion: fluxcd.controlplane.io/v1
kind: FluxInstance
metadata:
  name: flux
  namespace: flux-system
  annotations:
    fluxcd.controlplane.io/reconcileEvery: "1h"
    fluxcd.controlplane.io/reconcileTimeout: "5m"
spec:
  distribution:
    version: "2.x"
    registry: "ghcr.io/fluxcd"
    artifact: "oci://ghcr.io/controlplaneio-fluxcd/flux-operator-manifests"
  components:
  - source-controller
  - kustomize-controller
  - helm-controller
  - notification-controller
  - image-reflector-controller
  - image-automation-controller
  cluster:
    type: kubernetes
    multitenant: false
```
```yaml
networkPolicy: true
domain: "cluster.local"
kustomize:
  patches:
  - target:
      kind: Deployment
      name: "(kustomize-controller|helm-controller)"
    patch: |
      - op: add
        path: /spec/template/spec/containers/0/args/-
        value: --concurrent=10
      - op: add
        path: /spec/template/spec/containers/0/args/-
        value: --requeue-dependency=5s
```

```javascript
new k8s.apiextensions.CustomResource("flux", {
  apiVersion: "fluxcd.controlplane.io/v1",
  kind: "FluxInstance",
  metadata: {
    name: "flux",
    namespace: "flux-system",
    annotations: {
      "fluxcd.controlplane.io/reconcileEvery": "1h",
      "fluxcd.controlplane.io/reconcileTimeout": "5m",
    },
  },
  spec: {
    distribution: {
      version: "2.x",
      registry: "ghcr.io/fluxcd",
      artifact: "oci://ghcr.io/controlplaneio-fluxcd/flux-operator-manifests",
    },
    components: ["source-controller", "kustomize-controller", "helm-controller", "notification-controller", "image-reflector-controller", "image-automation-controller"],
    cluster: {
      type: "kubernetes",
      multitenant: false,
      networkPolicy: true,
      domain: "cluster.local",
    },
    kustomize: {
      patches: [
        {
          target: {
            kind: "Deployment",
            name: "(kustomize-controller|helm-controller)",
          },
          patch: `
- op: add
  path: /spec/template/spec/containers/0/args/-
  value: --concurrent=10
- op: add
  path: /spec/template/spec/containers/0/args/-
  value: --requeue-dependency=5s
`,
        },
      ],
    },
  },
});
```

```python
from pulumi_kubernetes import apiextensions

flux_instance = k8s.apiextensions.CustomResource(
    "flux",
    api_version="fluxcd.controlplane.io/v1",
    kind="FluxInstance",
    metadata={
        "name": "flux",
        "namespace": flux_namespace.metadata["name"],
        "annotations": {
            "fluxcd.controlplane.io/reconcileEvery": "1h",
            "fluxcd.controlplane.io/reconcileTimeout": "5m",
        },
    },
    spec={
        "distribution": {
            "version": "2.x",
            "registry": "ghcr.io/fluxcd",
            "artifact": "oci://ghcr.io/controlplaneio-fluxcd/flux-operator-manifests",
        },
        "components": [
            "source-controller",
            "kustomize-controller",
            "helm-controller",
            "notification-controller",
            "image-reflector-controller",
            "image-automation-controller",
        ],
        "cluster": {
            "type": "kubernetes",
            "multitenant": False,
            "networkPolicy": True,
            "domain": "cluster.local",
        },
        "kustomize": {
            "patches": [
                {
                    "target": {
                        "kind": "Deployment",
                        "name": "(kustomize-controller|helm-controller)",
                    },
                    "patch": [
                        {
                            "op": "add",
                            "path": "/spec/template/spec/containers/0/args/-",
                            "value": "--concurrent=10",
                        },
                        {
                            "op": "add",
                            "path": "/spec/template/spec/containers/0/args/-",
                            "value": "--requeue-dependency=5s",
                        },
                    ],
                }
            ]
        },
    },
)
```

```go
package main

import (
	"github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	apiv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apiextensions"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := apiv1.NewCustomResource(ctx, "flux", &apiv1.CustomResourceArgs{
			ApiVersion: pulumi.String("fluxcd.controlplane.io/v1"),
			Kind:       pulumi.String("FluxInstance"),
			Metadata: &metav1.ObjectMetaArgs{
				Name:      pulumi.String("flux"),
				Namespace: pulumi.String("flux-system"),
				Annotations: pulumi.StringMap{
					"fluxcd.controlplane.io/reconcileEvery":    pulumi.String("1h"),
					"fluxcd.controlplane.io/reconcileTimeout": pulumi.String("5m"),
				},
			},
			Spec: &kubernetes.UntypedArgs{
				"distribution": pulumi.Map{
					"version":  pulumi.String("2.x"),
					"registry": pulumi.String("ghcr.io/fluxcd"),
					"artifact": pulumi.String("oci://ghcr.io/controlplaneio-fluxcd/flux-operator-manifests"),
				},
				"components": pulumi.StringArray{
					pulumi.String("source-controller"),
					pulumi.String("kustomize-controller"),
					pulumi.String("helm-controller"),
					pulumi.String("notification-controller"),
					pulumi.String("image-reflector-controller"),
					pulumi.String("image-automation-controller"),
				},
				"cluster": pulumi.Map{
					"type":          pulumi.String("kubernetes"),
					"multitenant":   pulumi.Bool(false),
					"networkPolicy": pulumi.Bool(true),
					"domain":        pulumi.String("cluster.local"),
				},
				"kustomize": pulumi.Map{
					"patches": pulumi.Array{
						pulumi.Map{
							"target": pulumi.Map{
								"kind": pulumi.String("Deployment"),
								"name": pulumi.String("(kustomize-controller|helm-controller)"),
							},
							"patch": pulumi.Array{
								pulumi.Map{
									"op":    pulumi.String("add"),
									"path":  pulumi.String("/spec/template/spec/containers/0/args/-"),
									"value": pulumi.String("--concurrent=10"),
								},
								pulumi.Map{
									"op":    pulumi.String("add"),
									"path":  pulumi.String("/spec/template/spec/containers/0/args/-"),
									"value": pulumi.String("--requeue-dependency=5s"),
								},
							},
						},
					},
				},
			},
		})
		if err != nil {
			return err
		}
		return nil
	})
}

```
```json
{
  "multitenant": pulumi.Bool(false),
  "networkPolicy": pulumi.Bool(true),
  "domain": pulumi.String("cluster.local"),
},
"kustomize": pulumi.Map{
  "patches": pulumi.Array{
    pulumi.Map{
      "target": pulumi.Map{
        "kind": pulumi.String("Deployment"),
        "name": pulumi.String("(kustomize-controller|helm-controller)"),
      },
      "patch": pulumi.Array{
        pulumi.Map{
          "op": pulumi.String("add"),
          "path": pulumi.String("/spec/template/spec/containers/0/args/-"),
          "value": pulumi.String("--concurrent=10"),
        },
        pulumi.Map{
          "op": pulumi.String("add"),
          "path": pulumi.String("/spec/template/spec/containers/0/args/-"),
          "value": pulumi.String("--requeue-dependency=5s"),
        },
      },
    },
  },
},
})
if err != nil {
  return err
}
return nil
})
}
```

```csharp
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using System.Collections.Generic;
using Pulumi.Kubernetes.ApiExtensions;

class FluxInstanceArgs : CustomResourceArgs
{
    public string ApiVersion { get; set; }
    public string Kind { get; set; }
    public ObjectMetaArgs Metadata { get; set; }
    public Dictionary<string, object> Spec { get; set; }

    public FluxInstanceArgs(string apiVersion, string kind) : base(apiVersion, kind)
    {
    }
}

var flux = new Pulumi.Kubernetes.ApiExtensions.CustomResource("flux", new FluxInstanceArgs("fluxcd.controlplane.io/v1", "FluxInstance")
{
    ApiVersion = "fluxcd.controlplane.io/v1",
    Kind = "FluxInstance",
    Metadata = new ObjectMetaArgs
    {
        Name = "flux",
        Annotations =
        {
            { "fluxcd.controlplane.io/reconcileEvery", "1h" },
            { "fluxcd.controlplane.io/reconcileTimeout", "5m" },
        }
    },
    Spec = new Dictionary<string, object>
    {
        { "distribution", new Dictionary<string, object>
        {
            { "version", "2.x" },
            { "registry", "ghcr.io/fluxcd" },
            { "artifact", "oci://ghcr.io/controlplaneio-fluxcd/flux-operator-manifests" }
        } },
        { "components", new[]
        {
            "source-controller",
            "kustomize-controller",
            "helm-controller",
            "notification-controller",
            "image-reflector-controller",
            "image-automation-controller"
        } },
        { "cluster", new Dictionary<string, object>
        {
            { "type", "kubernetes" },
            { "multitenant", false },
            { "networkPolicy", true },
            { "domain", "cluster.local" }
        } },
        { "kustomize", new Dictionary<string, object>
        {
            { "patches", new[]
            {
                new Dictionary<string, object>
                {
                    { "target", new Dictionary<string, object>
                    {
                        { "kind", "Deployment" },
                        { "name", "(kustomize-controller|helm-controller)" }
                    } },
                    { "patch", new[]
                    {
                        new Dictionary<string, object>
                        {
                            { "op", "add" },
                            { "path", "/spec/template/spec/containers/0/args/-" },
                            { "value", "--concurrent=10" }
                        },
                        new Dictionary<string, object>
                        {
                            { "op", "add" },
                            { "path", "/spec/template/spec/containers/0/args/-" },
                            { "value", "--requeue-dependency=5s" }
                        }
                    } }
                }
            } }
        } }
    }
});
```

```javascript
import * as k8s from "@pulumi/kubernetes";
import * as k8shelm from "@pulumi/kubernetes/helm/v3";

const namespaceKafka = new k8s.core.v1.Namespace("kafka", {
    metadata: {
        name: "kafka",
    },
});

new k8s.helm.v3.Release("strimzi-kafka-operator", {
    chart: "strimzi-kafka-operator",
    version: "latest",
    namespace: namespaceKafka.metadata.name,
    repositoryOpts: {
        repo: "https://strimzi.io/charts/",
    },
    createNamespace: true,
});
```

```javascript
"use strict";
const k8s = require("@pulumi/kubernetes");
const k8shelm = require("@pulumi/kubernetes/helm/v3");

const namespaceKafka = new k8s.core.v1.Namespace("kafka", {
    metadata: {
        name: "kafka",
    },
});

new k8s.helm.v3.Release("strimzi-kafka-operator", {
    chart: "strimzi-kafka-operator",
    version: "latest",
    namespace: namespaceKafka.metadata.name,
    repositoryOpts: {
        repo: "https://strimzi.io/charts/",
    },
    createNamespace: true,
});
```

#### 摘要
Flux Operator是另一个高级Kubernetes operator的优秀示例，它提供全生命周期管理和众多自动化功能。

### Strimzi Operator
![Strimzi Operator 图片来源: strimzi.io](/blog/why-every-platform-engineer-should-care-about-kubernetes-operators/strimzi.png)

最后但并非最不重要的是，[Strimzi Operator](https://strimzi.io/) 是一个用于在 Kubernetes 上管理 Apache Kafka 的全生命周期管理 operator。随着事件驱动架构越来越流行，Apache Kafka 已经成为构建可扩展和可靠事件流平台的事实标准。Strimzi Operator 简化了在 Kubernetes 上部署、管理和扩展 Apache Kafka 集群的过程。

Strimzi Operator 的一些关键特性包括：

**集群管理** - 部署和管理 Apache Kafka 集群。**镜像集群** - 部署和管理镜像集群以进行灾难恢复。**流式处理能力** - 使用 Kafka Connect，您可以实现在 Kafka 和其他系统之间的数据流。

#### 安装
使用 Helm chart 部署 Strimzi Operator：

```bash
helm repo add strimzi https://strimzi.io/charts/
helm repo update
helm install strimzi strimzi/strimzi-kafka-operator -n kafka --create-namespace
```

或者使用 Pulumi 部署 Strimzi Operator：

```javascript
import * as k8s from "@pulumi/kubernetes";
import * as k8shelm from "@pulumi/kubernetes/helm/v3";
const namespaceKafka = new k8s.core.v1.Namespace("kafka", {
metadata: {
name: "kafka",
},
});
new k8s.helm.v3.Release("strimzi-kafka-operator", {
chart: "strimzi-kafka-operator",
version: "latest",
namespace: namespaceKafka.metadata.name,
repositoryOpts: {
repo: "https://strimzi.io/charts/",
},
createNamespace: true,
});
```
```python
repositoryOpts: {
    repo: "https://strimzi.io/charts/",
},
createNamespace: true,
```

```python
import pulumi_kubernetes as k8s
import pulumi_kubernetes.helm.v3 as k8shelm
import pulumi_kubernetes.meta.v1 as meta

namespace_kafka = k8s.core.v1.Namespace(
    "kafka",
    meta.ObjectMeta(
        name="kafka",
    ),
)

strimzi_kafka_operator = k8shelm.Release(
    "strimzi-kafka-operator",
    chart="strimzi-kafka-operator",
    version="latest",
    namespace=namespace_kafka.metadata["name"],
    repository_opts={
        "repo": "https://strimzi.io/charts/",
    },
    create_namespace=True,
)
```

```go
package main

import (
	"github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	apiv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apiextensions"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	ctx := context.Background()
	namespaceKafka, err := corev1.NewNamespace(ctx, "kafka", &corev1.NamespaceArgs{
		Metadata: &metav1.ObjectMetaArgs{
			Name: pulumi.String("kafka"),
		},
	})
	if err != nil {
		return err
	}
	_, err = helmv3.NewRelease(ctx, "strimzi-kafka-operator", &helmv3.ReleaseArgs{
		Chart: pulumi.String("strimzi-kafka-operator"),
		Version: pulumi.String("latest"),
		Namespace: namespaceKafka.Metadata.Name(),
		RepositoryOpts: helmv3.RepositoryOptsArgs{
			Repo: pulumi.String("https://strimzi.io/charts/"),
		},
		CreateNamespace: pulumi.Bool(true),
	})
	if err != nil {
		return err
	}
	return nil
}

```

```csharp
using Pulumi;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;

class MyStack : Stack
{
    public MyStack()
    {
        var namespaceKafka = new Namespace("kafka", new NamespaceArgs
        {
            Metadata = new ObjectMetaArgs
            {
                Name = "kafka",
            }
        });

        var strimziKafkaOperator = new Release("strimzi-kafka-operator", new ReleaseArgs
        {
            Chart = "strimzi-kafka-operator",
            Version = "latest",
            Namespace = namespaceKafka.Metadata.Apply(ns => ns.Name),
            RepositoryOpts = new RepositoryOptsArgs
            {
                Repo = "https://strimzi.io/charts/",
            },
            CreateNamespace = true,
        });
    }
}
```

```yaml
apiVersion: kafka.strimzi.io/v1beta2
kind: KafkaNodePool
metadata:
  name: example-kafka-node-pool
  labels:
    strimzi.io/cluster: example-kafka-cluster
spec:
  replicas: 1
  roles:
    - controller
    - broker
  storage:
    type: ephemeral
---
apiVersion: kafka.strimzi.io/v1beta2
kind: Kafka
metadata:
  name: example-kafka-cluster
  annotations:
    strimzi.io/kraft: enabled
    strimzi.io/node-pools: enabled
spec:
  kafka:
    replicas: 1
    version: 3.8.0
    storage:
      type: ephemeral
    metadataVersion: 3.8-IV0
    listeners:
      - name: plain
        port: 9092
        type: internal
        tls: false
      - name: tls
        port: 9093
        type: internal
        tls: true
    config:
      offsets.topic.replication.factor: 1
      transaction.state.log.replication.factor: 1
      transaction.state.log.min.isr: 1
      default.replication.factor: 1
      min.insync.replicas: 1
  entityOperator:
    topicOperator: {}
    userOperator: {}
```

```yaml
apiVersion: kafka.strimzi.io/v1beta2
kind: KafkaTopic
metadata:
  name: example-kafka-topic
  labels:
    strimzi.io/cluster: example-kafka-cluster
spec:
  partitions: 5
  replicas: 1
  config:
    retention.ms: 7200000
    segment.bytes: 1073741824
```

```python
new k8s.apiextensions.CustomResource("example-kafka-node-pool", {
    apiVersion: "kafka.strimzi.io/v1beta2",
    kind: "KafkaNodePool",
    metadata: {
        name: "example-kafka-node-pool",
        labels: {
            "strimzi.io/cluster": "example-kafka-cluster",
        },
        namespace: "kafka",
    },
    spec: {
        replicas: 1,
        roles: ["controller", "broker"],
        storage: {
            type: "ephemeral",
        },
    },
})

new k8s.apiextensions.CustomResource("example-kafka-cluster", {
    apiVersion: "kafka.strimzi.io/v1beta2",
    kind: "Kafka",
    metadata: {
        name: "example-kafka-cluster",
        annotations: {
            "strimzi.io/kraft": "enabled",
            "strimzi.io/node-pools": "enabled",
        },
        namespace: "kafka",
    },
    spec: {
        kafka: {
            replicas: 1,
            version: "3.8.0",
            storage: {
                type: "ephemeral",
            },
            metadataVersion: "3.8-IV0",
            listeners: [
                {
                    name: "plain",
                    port: 9092,
                    type: "internal",
                    tls: false,
                },
                {
                    name: "tls",
                    port: 9093,
                    type: "internal",
                    tls: true,
                },
            ],
            config: {
                "offsets.topic.replication.factor": 1,
                "transaction.state.log.replication.factor": 1,
                "transaction.state.log.min.isr": 1,
                "default.replication.factor": 1,
                "min.insync.replicas": 1,
            },
        },
        entityOperator: {
            topicOperator: {},
            userOperator: {},
        },
    },
})

new k8s.apiextensions.CustomResource("example-kafka-topic", {
    apiVersion: "kafka.strimzi.io/v1beta2",
    kind: "KafkaTopic",
    metadata: {
        name: "example-kafka-topic",
        labels: {
            "strimzi.io/cluster": "example-kafka-cluster",
        },
        namespace: "kafka",
    },
    spec: {
        partitions: 5,
        replicas: 1,
        config: {
            "retention.ms": 7200000,
            "segment.bytes": 1073741824,
        },
    },
})
```
```yaml
apiVersion: "kafka.strimzi.io/v1beta2"
kind: "KafkaTopic"
metadata:
  name: "example-kafka-topic"
  labels:
    "strimzi.io/cluster": "example-kafka-cluster"
  namespace: "kafka"
spec:
  partitions: 5
  replicas: 1
  config:
    "retention.ms": "7200000"
    "segment.bytes": "1073741824"
```
```yaml
apiVersion: "kafka.strimzi.io/v1beta2"
kind: "KafkaNodePool"
metadata:
  name: "example-kafka-node-pool"
  labels:
    "strimzi.io/cluster": "example-kafka-cluster"
  namespace: "kafka"
spec:
  replicas: 1
  roles:
    - "controller"
    - "broker"
  storage:
    type: "ephemeral"
```
```yaml
apiVersion: "kafka.strimzi.io/v1beta2"
kind: "Kafka"
metadata:
  name: "example-kafka-cluster"
  annotations:
    "strimzi.io/kraft": "enabled"
    "strimzi.io/node-pools": "enabled"
  namespace: "kafka"
spec:
  kafka:
    replicas: 1
    version: "3.8.0"
    storage:
      type: "ephemeral"
    metadataVersion: "3.8-IV0"
    listeners:
      - name: "plain"
        port: 9092
        type: "internal"
        tls: false
      - name: "tls"
        port: 9093
        type: "internal"
        tls: true
    config:
      "offsets.topic.replication.factor": "1"
      "transaction.state.log.replication.factor": "1"
      "transaction.state.log.min.isr": "1"
      "default.replication.factor": "1"
      "min.insync.replicas": "1"
  entityOperator:
    topicOperator: {}
    userOperator: {}
```
```yaml
apiVersion: "kafka.strimzi.io/v1beta2"
kind: "KafkaTopic"
metadata:
  name: "example-kafka-topic"
  labels:
    "strimzi.io/cluster": "example-kafka-cluster"
  namespace: "kafka"
spec:
  partitions: 5
  replicas: 1
  config:
    "retention.ms": "7200000"
    "segment.bytes": "1073741824"
```
```go
package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	apiv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apiextensions"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := apiv1.NewCustomResource(ctx, "flux", &apiv1.CustomResourceArgs{
			ApiVersion: pulumi.String("fluxcd.controlplane.io/v1"),
			Kind:       pulumi.String("FluxInstance"),
			Metadata: &metav1.ObjectMetaArgs{
				Name:      pulumi.String("flux"),
				Namespace: pulumi.String("flux-system"),
				Annotations: pulumi.StringMap{
					"fluxcd.controlplane.io/reconcileEvery":  pulumi.String("1h"),
					"fluxcd.controlplane.io/reconcileTimeout": pulumi.String("5m"),
				},
			},
			Spec: kubernetes.UntypedArgs{
				"distribution": pulumi.Map{
					"version":  pulumi.String("2.x"),
					"registry": pulumi.String("ghcr.io/fluxcd"),
					"artifact": pulumi.String("oci://ghcr.io/controlplaneio-fluxcd/flux-operator-manifests"),
				},
				"components": pulumi.StringArray{
					pulumi.String("source-controller"),
					pulumi.String("kustomize-controller"),
					pulumi.String("helm-controller"),
					pulumi.String("notification-controller"),
					pulumi.String("image-reflector-controller"),
					pulumi.String("image-automation-controller"),
				},
				"cluster": pulumi.Map{
					"type": pulumi.String("kubernetes"),
				},
			},
		})
		if err != nil {
			return err
		}

		return nil
	})
}
```
```json
{
  "name": "example-kafka-cluster",
  "namespace": "kafka",
  "labels": {
    "strimzi.io/cluster": "example-kafka-cluster"
  },
  "spec": {
    "replicas": 1,
    "version": "3.8.0",
    "storage": {
      "type": "ephemeral"
    },
    "metadataVersion": "3.8-IV0",
    "listeners": [
      {
        "name": "plain",
        "port": 9092,
        "type": "internal",
        "tls": false
      },
      {
        "name": "tls",
        "port": 9093,
        "type": "internal",
        "tls": true
      }
    ],
    "config": {
      "offsets.topic.replication.factor": 1,
      "transaction.state.log.replication.factor": 1,
      "transaction.state.log.min.isr": 1,
      "default.replication.factor": 1,
      "min.insync.replicas": 1
    }
  },
  "entityOperator": {
    "topicOperator": {},
    "userOperator": {}
  }
}
```

```csharp
{ "roles", new List<string> { "controller", "broker" } },
{ "storage", new Dictionary<string, object> { { "type", "ephemeral" } } }
}
});
var kafkaCluster = new Pulumi.Kubernetes.ApiExtensions.CustomResource("exampleKafkaCluster", new KafkaClusterArgs("kafka.strimzi.io/v1beta2", "Kafka")
{
    ApiVersion = "kafka.strimzi.io/v1beta2",
    Kind = "Kafka",
    Metadata = new ObjectMetaArgs
    {
        Name = "example-kafka-cluster",
        Annotations =
        {
            { "strimzi.io/kraft", "enabled" },
            { "strimzi.io/node-pools", "enabled" }
        }
    },
    Spec = new Dictionary<string, object>
    {
        { "kafka", new Dictionary<string, object> {
            { "replicas", 1 },
            { "version", "3.8.0" },
            { "storage", new Dictionary<string, object> { { "type", "ephemeral" } } },
            { "metadataVersion", "3.8-IV0" },
            { "listeners", new List<Dictionary<string, object>> {
                new Dictionary<string, object> {
                    { "name", "plain" },
                    { "port", 9092 },
                    { "type", "internal" },
                    { "tls", false }
                },
                new Dictionary<string, object> {
                    { "name", "tls" },
                    { "port", 9093 },
                    { "type", "internal" },
                    { "tls", true }
                }
            }},
            { "config", new Dictionary<string, object> {
                { "offsets.topic.replication.factor", 1 },
                { "transaction.state.log.replication.factor", 1 },
                { "transaction.state.log.min.isr", 1 },
                { "default.replication.factor", 1 },
                { "min.insync.replicas", 1 }
            }}
        }},
        { "entityOperator", new Dictionary<string, object> {
            { "topicOperator", new Dictionary<string, object>() },
            { "userOperator", new Dictionary<string, object>() }
        }}
    }
});
var kafkaTopic = new Pulumi.Kubernetes.ApiExtensions.CustomResource("exampleKafkaTopic", new KafkaTopicArgs("kafka.strimzi.io/v1beta2", "KafkaTopic")
{
    ApiVersion = "kafka.strimzi.io/v1beta2",
    Kind = "KafkaTopic",
    Metadata = new ObjectMetaArgs
    {
        Name = "example-kafka-topic",
        Labels =
        {
            { "strimzi.io/cluster", "example-kafka-cluster" }
        }
    },
    Spec = new Dictionary<string, object>
    {
        { "partitions", 5 },
        { "replicas", 1 },
        { "config", new Dictionary<string, object> {
            { "retention.ms", 7200000 },
            { "segment.bytes", 1073741824 }
        }}
    }
});
```

Strimzi Operator 通过提供在 Kubernetes 上运行的 Apache Kafka 的完整生命周期管理，展示了 Kubernetes Operator 的强大功能。它负责部署和管理 Kafka 集群的繁重工作，使 Strimzi Operator 成为每个基于 Kubernetes 的平台中都应该包含的宝贵工具，因为它涵盖了广泛的用例。


结论
在这篇博文中，我强调了 Kubernetes Operator 对于平台工程师的重要性，以及他们如何利用 Operator 的高级自动化功能来简化在 Kubernetes 上部署、管理和扩展应用程序和服务。

我提供了一些我推荐的高级 Kubernetes Operator 的示例，但是如果您想尝试在您的基于 Kubernetes 的平台中使用 Kubernetes Operator，这里有一些很棒的指南可以帮助您开始使用 Pulumi 和 Kubernetes：


开始使用 Pulumi
使用 Pulumi 的开源 SDK 在任何云上创建、部署和管理基础设施。