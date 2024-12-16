
<!--
title: 基于GitOps和Sveltos构建您自己的事件驱动型内部开发者平台
cover: https://miro.medium.com/v2/da:true/resize:fit:1069/1*0iYxYy_pjaUVW0nETz6vQg.gif
-->

探索如何创建反映云提供商所用架构的事件驱动型云环境

> 译自 [Building Your Own Event-Driven Internal Developer Platform with GitOps and Sveltos](https://itnext.io/building-your-own-event-driven-internal-developer-platform-with-gitops-and-sveltos-cbe3de4920d5)，作者 Artem Lajko。

注意：这是一个实践指南，需要具备Kubernetes和Helm的使用经验。要学习本教程，您还需要三个运行中的Kubernetes集群。

如果您认同开源并分享这种理念，[请考虑留下一个⭐️](https://github.com/projectsveltos/sveltos)来支持那些提供这些令人惊叹的工具并启用此类设置的人！

想象一下，您是一位访问XY提供商门户的用户，正在浏览他们的数据库即服务或托管数据库产品。您点击一个按钮或调用一个API（如果提供），瞧——您的数据库实例已准备就绪。但是您是否想过，这个数据库真的运行在传统的虚拟机上吗？感觉更像是运行在**Kubernetes集群**中，不是吗？您是否想过，他们如何在内部开发者平台的支撑下构建这个基于云的环境，并使其在门户中可用？

让我们顺着这个思路：假设数据库确实运行在Kubernetes上。当您点击 **“创建”** 时会发生什么？此操作会触发一个事件资源，指定数据库集群的部署时间和方式。此时，**Sveltos**介入，管理到适当集群的部署，检索必要的配置，并提供您无缝连接到数据库所需的详细信息。

虽然我无法透露大型提供商构建类似云的每一个技术细节（让我们避免任何法律问题！）或者也许我会构建我自己的IDP解决方案。我将指导您设置类似的事件驱动云架构。我们将分解每个组件，最终，您将对它有一个扎实的理解——也许甚至可以创建一个基于您自己的IDP的新云！

# 快速概述

在我们深入研究之前，以下是您需要了解的内容：本指南完全是实践性的，从头开始！您只需要三个运行中的集群：

1. 管理集群  
2. 服务集群  
3. 工作负载/应用集群

我们将逐步完成以下步骤：

1. **安装先决条件**: 设置`sveltosctl`, `cert-manager`, 和`sveltos`，并在管理集群上应用必要的标签。
2. **注册服务集群**: 准备服务集群以管理部署。
3. **部署数据库操作符**: 在服务集群上安装`cloudnative-pg`操作符。
4. **自动化数据库部署**: 指示Sveltos自动部署Postgres数据库实例。
5. **注册工作负载集群**: 将工作负载集群连接到架构。
6. **部署应用程序**: 启动连接到Postgres数据库的应用程序。

![](https://miro.medium.com/v2/resize:fit:976/format:webp/1*OYSp04Ki-prpTW4omB_Ugw.png)

*图1：你会选择哪条路？*

让我们直接开始。下面有两个部分A和B。A是一个详细的指南，也解释了幕后发生的事情。B是一种快速部署事物而不真正理解它们并相信任何你想相信的东西的简短方法。

让我们从路径A或B开始！

# 路径 A：深入探讨

在本节中，我们将一步一步地一起进行，解释每个命令及其用途，让您更深入地了解幕后发生的事情

**1. 在管理集群上安装sveltosctl、cert-manager、sveltos并添加标签**

首先，让我们[安装](https://github.com/projectsveltos/sveltosctl) `sveltosctl`，这是一个用于与Sveltos交互的命令行工具。此工具将帮助我们管理跨集群的部署。[sveltosctl](https://github.com/projectsveltos/sveltosctl)

以下是安装方法：

```bash
# MacOS
sudo wget https://github.com/projectsveltos/sveltosctl/releases/download/v0.41.1/sveltosctl-darwin-arm64 -O /usr/local/bin/sveltosctl
sudo chmod +x /usr/local/bin/sveltosctl
# Linux
sudo wget https://github.com/projectsveltos/sveltosctl/releases/download/v0.41.1/sveltosctl-linux-amd64 -O /usr/local/bin/sveltosctl
sudo chmod +x /usr/local/bin/sveltosctl
```

![](https://miro.medium.com/v2/resize:fit:1096/format:webp/1*pKQ0bx-ShPHSwIN7FQ9r4w.png)

*图2：在客户端设备上安装Sveltosctl*

现在，让我们使用[Helm](https://helm.sh)安装[Cert-Manager](https://cert-manager.io)。此工具为我们管理证书，这对于集群之间的安全通信至关重要。

```bash
helm install cert-manager jetstack/cert-manager --namespace cert-manager --create-namespace --version v1.16.1 --set crds.enabled=true
```

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*apAh6_PLVMjxJxUJBrwMig.png)

*图3：安装Cert-Manager的Helm图表*

接下来，我们将通过Helm部署[Sveltos堆栈](https://projectsveltos.github.io/sveltos/getting_started/install/install/)本身。此步骤将在我们的管理集群上设置核心Sveltos组件。

```bash
helm install projectsveltos projectsveltos/projectsveltos -n projectsveltos --create-namespace
```

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*mC0ew_1T1PKa7D5HHcACwg.png)

*图4：为Projectsveltos安装Helm图表*

为管理集群添加标签可以帮助Sveltos按类型识别和组织集群，从而简化以后的部署。

```bash
kubectl label sveltoscluster -n mgmt mgmt type=mgmt
```

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*a3Qrymn6_5lyOIBTK_gVOg.png)

*图5：标签管理集群*

为了允许Sveltos使用*ConfigMaps*和*Secrets*等资源，我们需要添加特定的权限。以下是修补`addon-controller-role-extra`的方法
为此目的的 *ClusterRole*：

```bash
kubectl patch clusterrole addon-controller-role-extra --type='json' -p='[
  {
    "op": "add",
    "path": "/rules",
    "value": [
      {
        "apiGroups": [""],
        "resources": ["configmaps", "secrets"],
        "verbs": ["*"]
      }
    ]
  }
]'
```

恭喜！您已完成基础设置。让我们继续进行步骤 2。

**2. 注册服务集群**

此步骤非常简单，这要感谢 `sveltosctl`。以下是将管理集群连接到服务集群的方法：

```bash
kubectl create ns service-cluster
sveltosctl register cluster --namespace=service-cluster --cluster=service-cluster --fleet-cluster-context=service-cluster --labels=type=services
```

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*nt0H0Tcnl8N1QLR714bFVQ.gif)

*图6：注册服务集群并对其进行标记*

在此步骤中，我们创建了管理集群和受管服务集群之间的连接。但是，让我们看一下提供的参数以更好地理解：

`--namespace=service-cluster`: 将在管理集群中为受管集群创建命名空间

`--cluster=service-cluster`: 将在 CustomResource `sveltoscluster` 中添加受管集群的名称

`--fleet-cluster-context=service-cluster`: 将使用您的上下文名称来访问应由 sveltos 管理的集群。在我的例子中，它是 `service-cluster`

`--labels=type=services`: 将标签添加到添加到 CustomResource `sveltoscluster` 中的受管集群，这允许基于标签部署应用程序。

要验证标签，请使用以下命令：

```bash
kubectl get sveltoscluster -A --show-labels

NAMESPACE       NAME                READY   VERSION      LABELS
mgmt            mgmt                true    v1.29.2+k3s1 projectsveltos.io/k8s-version=v1.29.2,sveltos-agent=present,type=mgmt
service-cluster service-cluster    true    v1.29.2+k3s1 projectsveltos.io/k8s-version=v1.29.2,sveltos-agent=present,type=services
```

此设置使 Sveltos 能够基于标签识别和管理服务集群，这将有助于部署应用程序。

如果您好奇 Sveltos 如何管理附加组件，请随意浏览[更多资源](https://projectsveltos.github.io/sveltos/addons/addons/)。现在，让我们继续部署操作符以帮助在服务集群上设置受管服务。[cloudnative-pg](https://cloudnative-pg.io)

**3. 在服务集群上部署 cloudnative-pg Operator**

要部署 CloudNative-PG 操作符，我们将在管理集群上应用一个 `ClusterProfile` CustomResource。此 `ClusterProfile` 指示 Sveltos 在与特定标签匹配的集群上部署操作符。

运行以下命令以应用 `ClusterProfile`：

```bash
kubectl apply -f https://raw.githubusercontent.com/projectsveltos/sveltos/main/docs/assets/cloudnative-pg.yaml
```

此步骤之后，我们的设置将如下所示：

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*1HOIrxe6mJoaUIyux31RJA.gif)

*图7：根据集群配置文件指导部署PG-Operator*

**什么是 ClusterProfile？**

`ClusterProfile`就像一个蓝图，定义了应在与某些标签匹配的集群上部署哪些资源。在本例中，配置文件的目标是标记为 `type=services` 的集群，并指示 Sveltos 在那里安装 [CloudNative-PG Helm chart](https://github.com/cloudnative-pg/charts)。它看起来像这样：

```yaml
---
apiVersion: config.projectsveltos.io/v1beta1
kind: ClusterProfile
metadata:
  name: deploy-cnpg
spec:
  clusterSelector:
    matchLabels:
      type: services
  syncMode: Continuous
  helmCharts:
  - repositoryURL: https://cloudnative-pg.github.io/charts
    repositoryName: cloudnative-pg
    chartName: cloudnative-pg/cloudnative-pg
    chartVersion: 0.22.1
    releaseName: cnpg
    releaseNamespace: cnpg-system
    helmChartAction: Install
```

在此示例中，任何带有标签 `type=services` 的集群都将自动安装 CloudNative-PG Helm chart，并根据指定内容持续同步。

要检查在服务集群上部署的资源，您可以使用：

```bash
sveltosctl show addons

+-----------------------------------+----------------------------+------------------+-----------------------------------+---------+-------------------------------+---------------------------------------------+
| CLUSTER                          | RESOURCE TYPE             | NAMESPACE       | NAME                               | VERSION | TIME                           | PROFILES                             |
+-----------------------------------+----------------------------+------------------+-----------------------------------+---------+-------------------------------+---------------------------------------------+
| service-cluster/service-cluster | helm chart                 | cnpg-system     | cnpg                               | 0.22.1   | 2024-11-02 11:35:40 +0100 CET | ClusterProfile/deploy-cnpg           |
+-----------------------------------+----------------------------+------------------+-----------------------------------+---------+-------------------------------+---------------------------------------------+
```

这确认 CloudNative-PG 操作符已成功部署在服务集群上。

**4. 指示 Sveltos 自动部署 Postgres DB**

在此步骤中，我们将配置 Sveltos 以自动在标记有 `postgres=required` 的集群上部署 PostgreSQL 数据库。每当 Sveltos 检测到具有此标签的受管集群时，它将：

- 在集群上创建一个 PostgreSQL 实例。
- 通过 LoadBalancer 服务暴露数据库。
- 检索凭据和连接详细信息，包括外部 IP 和端口。

要启用此功能，请应用以下配置：

```bash
kubectl apply -f https://raw.githubusercontent.com/projectsveltos/sveltos/main/docs/assets/auto-deploy-postgres-cluster.yaml
kubectl apply -f https://raw.githubusercontent.com/projectsveltos/sveltos/main/docs/assets/fetch-postgres-data.yaml
```

这些配置设置了两个工作流程：

- **自动部署 PostgreSQL 集群**: 在标记为 `type=services` 的集群上触发时部署 PostgreSQL。
- **获取 PostgreSQL 集群数据**: 基于特定事件检索 PostgreSQL 集群的连接数据和凭据。

**第一个工作流程** 如下所示：

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bNQpGYIGByJimicFp2QNMA.png)

*图8：工作流1：自动部署PostgreSQL集群*

在 Sveltos 中，**EventSource** 定义了在 Kubernetes 集群中监视的特定事件（例如资源的创建或删除），而 **EventTrigger** 指定了响应这些事件要部署的附加组件或应用程序。

应用的资源如下所示：

```yaml
# Anytime a SveltosCluster with label postgres: required
# is created, deploys a postgres cluster.
# Source cluster is the management cluster.
# Destination cluster is the cluster with label type:services
apiVersion: lib.projectsveltos.io/v1beta1
kind: EventSource
metadata:
  name: detect-cluster-requiring-postgres
spec:
  collectResources: true
  resourceSelectors:
  - group: "lib.projectsveltos.io"
    version: "v1beta1"
    kind: "SveltosCluster"
    labelFilters:
    - key: postgres
      operation: Equal
      value: required
---
apiVersion: lib.projectsveltos.io/v1beta1
kind: EventTrigger
metadata:
  name: deploy-postgres-cluster
spec:
  sourceClusterSelector:
    matchLabels:
      type: mgmt
  destinationClusterSelector:
    matchLabels:
      type: services
  eventSourceName: detect-cluster-requiring-postgres
  oneForEvent: true
  policyRefs:
  - name: postgres-cluster
    namespace: default
    kind: ConfigMap
---
apiVersion: v1
data:
  cluster.yaml: |
    apiVersion: postgresql.cnpg.io/v1
    kind: Cluster
    metadata:
      name: cluster-{{ .Resource.metadata.name }}
      namespace: {{ .Resource.metadata.namespace }}
      labels:
        cluster: {{ .Resource.metadata.namespace }}-{{ .Resource.metadata.name }}
    spec:
      instances: 3
      bootstrap:
        initdb:
          database: todo
      storage:
        size: 1Gi
      managed:
        services:
          disabledDefaultServices: ["ro", "r"]
          additional:
          - selectorType: rw
            serviceTemplate:
              metadata:
                name: cluster-rw-lb
              spec:
                type: LoadBalancer
kind: ConfigMap
metadata:
  annotations:
    projectsveltos.io/instantiate: ok
  name: postgres-cluster
  namespace: default
```

- **EventSource 定义**: EventSource `detect-cluster-requiring-postgres` 监视任何标记为 `postgres: required` 的 `SveltosCluster` 对象的创建。当创建这样的标记集群时，Sveltos 将其检测为重要事件。
- **EventTrigger 定义**: 当上述事件发生时，将触发 EventTrigger `deploy-postgres-cluster`。它被配置为在标记为 `type: services` 的目标集群中部署 PostgreSQL 集群，源是标记为 `type: mgmt` 的管理集群。
- **PostgreSQL 集群部署**: EventTrigger 引用一个 `ConfigMap` (`postgres-cluster`)，其中包含一个模板来定义 PostgreSQL 集群。当事件触发时，Sveltos 使用此模板在目标集群中创建一个新的 PostgreSQL 集群。该模板动态地包含源集群的名称和命名空间等详细信息。

总而言之，Sveltos 监视集群上的特定标签，当检测到匹配项时，会自动在指定的 target 集群中部署 PostgreSQL 集群。


**第二个工作流程** 由两个子工作流程组成，如下所示：

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*x2GJ3pRdZkSnIFpfX6ia2Q.png)

*图9：工作流程2：获取PostgreSQL集群数据*

在这个设置中，Sveltos 被配置为从服务集群检索 PostgreSQL 凭证和负载均衡器信息，并使它们在管理集群中可访问。

**获取 PostgreSQL 集群数据**

在此设置中，Sveltos 配置为从服务集群检索 PostgreSQL 凭据和负载均衡器信息，并在管理集群中使它们可访问：

**获取 PostgreSQL 凭据**:

- **EventSource**: `detect-credentials-secret` 监视服务集群中具有标签 `cnpg.io/reload: true` 的 `Secret` 对象。此标签表示该密钥包含 PostgreSQL 凭据。
- **EventTrigger**: `credentials-secret` 在任何标记为 `type: services` 的集群中检测到这样的 `Secret` 时被激活。它启动在管理集群（标记为 `type: mgmt`）中创建包含 PostgreSQL 凭据的 `Secret`。
- **ConfigMap 模板**: `credentials` ConfigMap 包含一个模板，用于在管理集群中创建一个名为 `pg-credentials` 的 `Secret`。此模板动态地从服务集群中的原始 Secret 中提取用户名和密码，允许 Sveltos 安全地复制这些凭据。

**获取负载均衡器信息**:

- **EventSource**: `detect-loadbalancer` 监视服务集群中标记为 `cnpg.io/isManaged: true` 的 `Service` 对象，表明它们是托管的PostgreSQL负载均衡器。
- **EventTrigger**: `cnpg-loadbalancer-data` 在检测到此类服务时触发，并在管理集群中创建一个ConfigMap来存储负载均衡器的外部IP和端口信息。
- **ConfigMap 模板**: `loadbalancer-data` ConfigMap模板用于在管理集群中生成名为`pg-loadbalancer-data` 的ConfigMap。它使用负载均衡器的外部IP地址和端口填充此ConfigMap，从而允许从管理集群外部访问PostgreSQL实例。

此设置允许管理集群**安全且动态地**访问在服务集群中部署的实例的PostgreSQL凭据和连接详细信息。

接下来，让我们注册工作负载集群以触发以下步骤中的事件。

**5. 注册工作负载集群**

现在，让我们使用Sveltos注册工作负载集群。通过使用`postgres=required` 标记此集群，我们指示Sveltos在服务集群上部署一个新的PostgreSQL实例并收集必要的连接详细信息。以下是注册工作负载集群的方法：

```bash
kubectl create ns workload-cluster
sveltosctl register cluster --namespace=workload-cluster --cluster=workload-cluster --fleet-cluster-context=workload-cluster --labels=postgres=required
```
一旦集群注册完毕，Sveltos就会自动触发我们在步骤4中设置的工作流程（事件）。以下是幕后发生的情况：

- **触发部署和数据收集**：Sveltos使用先前`EventTrigger` 配置中定义的模板创建`ClusterProfiles` 和`ConfigMaps` 。根据这些模板，它在`workload-cluster` 命名空间下的服务集群中部署一个PostgreSQL集群。它还在管理集群的`workload-cluster`命名空间下检索和存储数据库的连接信息（例如凭据和负载均衡器IP）。
- **自动创建ClusterProfile和ConfigMap** Sveltos生成一个`ClusterProfile` ，它以`type=services` 集群为目标，引用从模板创建的新ConfigMap。以下是生成的`ClusterProfile` 示例：

它看起来像这样：

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*j2UxwBZjfu08iGPMZRNFog.gif)

因此，Sveltos创建与目标集群匹配的*ClusterProfiles*。它还使此*ClusterProfile*引用从模板新创建的*ConfigMap*。

因此，您可以看到创建了一个新的*ClusterProfile*，如下所示：

```yaml
apiVersion: config.projectsveltos.io/v1beta1
kind: ClusterProfile
metadata:
  finalizers:
  - clusterprofilefinalizer.projectsveltos.io
  generation: 1
  labels:
    eventtrigger.lib.projectsveltos.io/clusterNamespace: mgmt
    eventtrigger.lib.projectsveltos.io/clustername: mgmt
    eventtrigger.lib.projectsveltos.io/clustertype: Sveltos
    eventtrigger.lib.projectsveltos.io/eventreportname: detect-cluster-requiring-postgres
    eventtrigger.lib.projectsveltos.io/eventtriggername: deploy-postgres-cluster
    eventtrigger.lib.projectsveltos.io/resourcename: workload-cluster
    eventtrigger.lib.projectsveltos.io/resourcenamespace: workload-cluster
    projectsveltos.io/cluster-name: service-cluster
    projectsveltos.io/cluster-profile-name: sveltos-j7dn263no745a5e58uya
    projectsveltos.io/cluster-type: Sveltos
  name: sveltos-j7dn263no745a5e58uya
spec:
  clusterSelector:
    matchLabels:
      type: services
  continueOnConflict: false
  policyRefs:
  - deploymentType: Remote
    kind: ConfigMap
    name: sveltos-bnnnp8dv2ndb8i7dx1vo
    namespace: projectsveltos
  reloader: false
  stopMatchingBehavior: WithdrawPolicies
  syncMode: Continuous
  tier: 100
```
在这里您可以看到对*ConfigMap*的引用，该*ConfigMap*包含用于在内部创建*Cluster*的*CustomResource*：

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  labels:
    eventtrigger.lib.projectsveltos.io/clusterNamespace: mgmt
    eventtrigger.lib.projectsveltos.io/clustername: mgmt
    eventtrigger.lib.projectsveltos.io/clustertype: Sveltos
    eventtrigger.lib.projectsveltos.io/eventreportname: detect-cluster-requiring-postgres
    eventtrigger.lib.projectsveltos.io/eventtriggername: deploy-postgres-cluster
    eventtrigger.lib.projectsveltos.io/refname: postgres-cluster
    eventtrigger.lib.projectsveltos.io/refnamespace: default
    eventtrigger.lib.projectsveltos.io/resourcename: workload-cluster
    eventtrigger.lib.projectsveltos.io/resourcenamespace: workload-cluster
  name: sveltos-bnnnp8dv2ndb8i7dx1vo
  namespace: projectsveltos
data:
  cluster.yaml: |
    apiVersion: postgresql.cnpg.io/v1
    kind: Cluster
    metadata:
      name: cluster-workload-cluster
      namespace: workload-cluster
      labels:
        cluster: workload-cluster-workload-cluster
    spec:
      instances: 3
      bootstrap:
        initdb:
          database: todo
      storage:
        size: 1Gi
      managed:
        services:
          disabledDefaultServices: ["ro", "r"]
          additional:
          - selectorType: rw
            serviceTemplate:
              metadata:
                name: cluster-rw-lb
              spec:
                type: LoadBalancer
```

当然，这只是一个例子——您可以做更多的事情，例如使用Helm通过触发器安装图表，无需在*ConfigMap*中指定它（更多内容请参见结尾）。

现在，让我们验证Sveltos是否已成功部署PostgreSQL实例并获取连接详细信息。要检查凭据，请使用：

```bash
kubectl get secret -n workload-cluster

# output
Name                      TYPE       DATA   AGE
workload-cluster-sveltos-kubeconfig Opaque     1      47h
pg-credentials             Opaque     2      47h
```

`pg-credentials` 密钥包含PostgreSQL凭据：

```
data:
  password: bTloa....
  user: d...
```

要检查连接详细信息（外部IP和端口），请使用：

```bash
kubectl get configmap -n workload-cluster service-cluster-loadbalancer-data -oyaml                                                                               04.11.24  11:32:44  management-cluster/default ⎈

#output like
apiVersion: v1
data:
  external-ip: 212.2.....
  port: "5432"
```

这完成了设置，管理集群现在能够安全且自动地访问PostgreSQL实例的连接详细信息和凭据。

**6. 部署访问Postgres DB的应用程序**

Sveltos现在可用于在workload-cluster集群中部署一个*Job*。此*Job*将访问在services-cluster上运行的Postgres DB。

此*Job*表示为模板，并将由Sveltos部署在任何带有标签`type=app`的集群中。

```bash
kubectl apply -f https://raw.githubusercontent.com/projectsveltos/sveltos/main/docs/assets/job-to-create-table.yaml

kubectl label sveltoscluster -n workloadcluster workload-cluster type=app
```

更改将如下所示：

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*EQvwDKtCTkk44v5paYycHw.gif)

*图11：在可以访问服务集群上的PG-DB的工作负载集群上部署作业。*

它建立与workload-cluster的连接，创建一个新的ClusterProfile，指示Sveltos在与`type=app`匹配的集群上部署一个*Job*。

如果您仔细查看*ClusterProfile*：

```yaml
apiVersion: config.projectsveltos.io/v1beta1
kind: ClusterProfile
metadata:
  finalizers:
  - clusterprofilefinalizer.projectsveltos.io
  name: deploy-job
spec:
  clusterSelector:
    matchLabels:
      type: app
  continueOnConflict: false
  policyRefs:
  - deploymentType: Remote
    kind: ConfigMap
    name: job-to-create-table
    namespace: default
  reloader: false
  stopMatchingBehavior: WithdrawPolicies
  syncMode: Continuous
  templateResourceRefs:
  - identifier: Credentials
    resource:
      apiVersion: v1
      kind: Secret
      name: pg-credentials
  - identifier: LoadBalancer
    resource:
      apiVersion: v1
      kind: ConfigMap
      name: pg-loadbalancer-data
  tier: 100

```

以下是发生的情况：

- Sveltos使用`default`命名空间中的`job-to-create-table` ConfigMap。
- 它使用Secret `pg-credentials`和*ConfigMap* `pg-loadbalancer-data`中的数据替换模板中的值，并根据匹配的标签`type=app`设置命名空间（workload-cluster）。
- 然后，Sveltos使用在与标签`type=app`匹配的远程集群（在本例中为workload-cluster）上获取的信息创建一个Job。

您可以使用以下命令检查预配是否按预期工作：

```bash
kubectl get clustersummaries -A -owide

NAMESPACE       NAME                                               HELMCHARTS    KUSTOMIZEREFS    POLICYREFS
mgmt            sveltos-1a6ec1ce3bandndeqixd-sveltos-mgmt          Provisioned
mgmt            sveltos-p46z943e935h2vtev56i-sveltos-mgmt          Provisioned
service-cluster deploy-cnpg-sveltos-service-cluster              Provisioned
service-cluster sveltos-xind5b6qvvrnbeur2flf-sveltos-service-cluster Provisioned
workload-cluster deploy-job-sveltos-workload-cluster              Provisioned
```

您现在应该看到*Job* `todo-table`在workload-cluster中运行。

## 方法B：捷径

**1. 在管理集群上安装sveltosctl、cert-manager、Sveltos并添加标签**

```bash
#MacOs
sudo wget https://github.com/projectsveltos/sveltosctl/releases/download/v0.41.1/sveltosctl-darwin-arm64 -O /usr/local/bin/sveltosctl
sudo chmod +x /usr/local/bin/sveltosctl

#Linux
sudo wget https://github.com/projectsveltos/sveltosctl/releases/download/v0.41.1/sveltosctl-linux-amd64 -O /usr/local/bin/sveltosctl
sudo chmod +x /usr/local/bin/sveltosctl


#Cert-Manager
helm install cert-manager jetstack/cert-manager --namespace cert-manager --create-namespace --version v1.16.1 --set crds.enabled=true


#Sveltos
helm install projectsveltos projectsveltos/projectsveltos -n projectsveltos --create-namespace

#Label management cluster
kubectl label sveltoscluster -n mgmt mgmt type=mgmt

#grant extra permission.
kubectl patch clusterrole addon-controller-role-extra --type='json' -p='[
  {
    "op": "add",
    "path": "/rules",
    "value": [
      {
        "apiGroups": [""],
        "resources": ["configmaps", "secrets"],
        "verbs": ["*"]
      }
    ]
  }
]'
```

## 2. 注册服务集群

```bash
kubectl create ns service-cluster

sveltosctl register cluster --namespace=service-cluster --cluster=service-cluster --fleet-cluster-context=service-cluster --labels=type=services
```

检查标签：

```bash
kubectl get sveltoscluster -A --show-labels

NAMESPACE       NAME             READY   VERSION      LABELS
mgmt            mgmt             true    v1.29.2+k3s1 projectsveltos.io/k8s-version=v1.29.2,sveltos-agent=present,type=mgmt
service-cluster service-cluster true    v1.29.2+k3s1 projectsveltos.io/k8s-version=v1.29.2,sveltos-agent=present,type=services
```

## 3. 在服务集群上部署CloudNative-PG Operator

```bash
kubectl apply -f https://raw.githubusercontent.com/projectsveltos/sveltos/main/docs/assets/cloudnative-pg.yaml
```

现在您可以使用以下命令查看服务集群上已部署的资源：

```bash
sveltosctl show addons 

+-----------------------------------+----------------------------+------------------+-----------------------------------+---------+-------------------------------+---------------------------------------------+
|              CLUSTER              |       RESOURCE TYPE        |    NAMESPACE     |               NAME                | VERSION |             TIME              |                  PROFILES                   |
+-----------------------------------+----------------------------+------------------+-----------------------------------+---------+-------------------------------+---------------------------------------------+
| service-cluster/service-cluster   | helm chart                 | cnpg-system      | cnpg                              | 0.22.1  | 2024-11-02 11:35:40 +0100 CET | ClusterProfile/deploy-cnpg                  |
+-----------------------------------+----------------------------+------------------+-----------------------------------+---------+-------------------------------+---------------------------------------------+
```

## 4. 指示 Sveltos 自动部署 PostgreSQL 数据库

```bash
kubectl apply -f https://raw.githubusercontent.com/projectsveltos/sveltos/main/docs/assets/auto-deploy-postgres-cluster.yaml

kubectl apply -f https://raw.githubusercontent.com/projectsveltos/sveltos/main/docs/assets/fetch-postgres-data.yaml
```
## 5. 注册工作负载集群

```bash
kubectl create ns workload-cluster

sveltosctl register cluster --namespace=workload-cluster --cluster=workload-cluster --fleet-cluster-context=workload-cluster --labels=postgres=required
```

现在验证 Sveltos 是否部署了 Postgres 集群并获取了必要的连接信息：

```bash
kubectl get secret -n workload-cluster

#output 
Name                                  TYPE     DATA   AGE
workload-cluster-sveltos-kubeconfig   Opaque   1      47h
pg-credentials                        Opaque   2      47h
```
## 6. 部署访问 PostgreSQL 数据库的应用程序

```bash
kubectl apply -f https://raw.githubusercontent.com/projectsveltos/sveltos/main/docs/assets/job-to-create-table.yaml

kubectl label sveltoscluster -n workload-cluster workload-cluster type=app
```

检查预配是否按预期工作：

```bash
kubectl get clustersummaries -A -owide

NAMESPACE NAME HELMCHARTS KUSTOMIZEREFS POLICYREFS
mgmt sveltos-1a6ec1ce3bandndeqixd-sveltos-mgmt Provisioned
mgmt sveltos-p46z943e935h2vtev56i-sveltos-mgmt Provisioned
service-cluster deploy-cnpg-sveltos-service-cluster Provisioned
service-cluster sveltos-xind5b6qvvrnbeur2flf-sveltos-service-cluster Provisioned
workload-cluster deploy-job-sveltos-workload-cluster Provisioned
```

您现在应该看到作业`todo-table`在workload-cluster中运行。

**恭喜！** 您已经创建了一个事件驱动的、托管的数据库即服务！您可以通过定义触发与UI引用的用户或服务共享凭据的作业来进一步扩展此设置，如初始示例所示。

## 总结

我可以想象您现在想知道，GitOps 部分在哪里？标题是为了吸引您的注意吗？不。实际上，Sveltos Addon-Controller 工作流基于 GitOps 方法，但为了获得完整的 GitOps 体验，您可以将[Sveltos 与 Flux CD 配对——它已经集成](https://projectsveltos.github.io/sveltos/addons/example_flux_sources/)了。为什么要使用 Flux CD？要部署*ClusterProfiles*并应用另一个 Sveltos *CustomResources*，您需要 GitOps 工具，例如[Flux CD](https://www.google.com/search?client=safari&rls=en&q=flux+cd&ie=UTF-8&oe=UTF-8)。

这只是您可以实现它的一小部分。Sveltos 提供了许多不同的可能性来提供事件驱动的托管服务。同时，托管服务可以集成到内部开发者平台中，为团队提供自助服务方法。

我们描述了以下场景：

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*1V_kMNCqBFPT6wzIKW1URw.gif)

因此，我们创建了服务集群上的工作负载集群和 PostgreSQL 集群之间的 1:1 关系，因为我们根据集群的标签配置了我们的 ClusterProfiles。

还有一个选项可以构建类似这样的内容：

您可以使用 ConfigMap（例如）代替响应集群的标签，该 ConfigMap 指示需要 PostgreSQL 集群。基于此，Sveltos 然后可以为每个命名空间/ConfigMap 创建多个 PostgreSQL 集群。这对于这篇博文来说太多了，但是您可以在[此处找到操作方法的说明：](https://projectsveltos.github.io/sveltos/events/db-as-a-service-multiple-db-per-cluster/)

此外，如果您想解决安全问题并且不想让所有托管服务的凭据都驻留在管理集群中，您可以实现以下内容：

在这里，凭据存储在相应的工作负载集群中。
希望您能看到可能性是巨大的，而您的想象力可能是这里唯一的限制因素。
如果您正在构建令人兴奋的解决方案，请随时以博客、教程等形式分享它们。但更重要的是，如果您相信开源并遵循这一理念，[请留下一个⭐️](https://github.com/projectsveltos/addon-controller)!  更酷的是通过博客投稿，或者如果您足够熟练，可以直接贡献给[Projectsveltos](https://github.com/projectsveltos) 本身。

**附言** 请留下评论说明您选择哪条路径——您是“需要了解每一个细节”类型，还是“直接部署然后祈祷”类型？😬

# 联系方式

有问题，想聊天，或者只是想保持联系？跳过Medium评论，让我们在[LinkedIn](http://www.linkedin.com/in/lajko)上联系🤙。别忘了订阅[Medium通讯](/@artem_lajko/subscribe)，这样你就不会错过任何更新！