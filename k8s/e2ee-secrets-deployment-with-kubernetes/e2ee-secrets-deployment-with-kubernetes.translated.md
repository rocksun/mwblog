# 端到端加密机密部署到 Kubernetes

使用 Phase 安全地将机密部署到 Kubernetes

[Nimish](https://github.com/nimish-ks)

## 简介

Kubernetes 是许多人选择的开源容器编排平台，特别是用于自动化容器化应用程序的部署、扩展和管理。使用 Kubernetes 安全地向这些容器化应用程序提供机密可能很棘手，但对于工作负载的安全性至关重要。开箱即用，Kubernetes 提供了几种本机机制来处理机密，但它们在安全功能、可扩展性和复杂性方面存在局限性。

在本指南中，我们将探讨为存储在 Kubernetes 中的机密启用静态加密，并使用 [Phase Kubernetes Operator](https://docs.phase.dev/integrations/platforms/kubernetes) 将存储在 Phase 机密管理器中的机密安全地同步到 Kubernetes 集群。如果您不知道什么是 operator，可以将其视为在 Kubernetes 集群中的 Pod 中运行的代理，它与 Kubernetes API 交互以自动管理特定服务或一组服务。

以下是高级架构的外观：

Phase Kubernetes Operator 将从 Phase 实例获取应用程序机密，对其进行解密，并将其作为受管 [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/) 写入 Kubernetes 集群。然后，它将继续监视 Phase 中机密的任何更改，并自动将它们与 Kubernetes 集群同步，使我们的机密管理器成为机密的真实来源。此外，它还可以选择在与它们关联的机密更改后自动重新部署 Kubernetes 部署。

Phase 还可以用于管理云中应用程序部署之前的阶段中的机密，例如 [本地开发](https://docs.phase.dev/integrations) 或在 CI 管道（如 [GitHub Actions](https://docs.phase.dev/integrations/platforms/github-actions)）中构建容器时，但这超出了本博客的范围。

## 了解存储在 Kubernetes 中的机密的安全性

### etcd

在开始之前，让我们确保 Kubernetes 集群已启用“静态加密”。Kubernetes 使用 etcd，一个分布式键值对数据库来存储关键数据，例如集群状态、配置和机密。Kubernetes API 在将机密写入磁盘上的 etcd 之前对其进行加密非常重要。

有一句谚语，“*加密很容易，密钥管理很难*”；在这里我们面临同样的挑战。如果我们想要加密存储在 Kubernetes 集群中的机密，我们将使用哪个密钥对该数据进行加密？那不是我们需要保护的另一个机密吗？此设置的复杂性取决于集群的管理方式。如果您自己管理 Kubernetes 集群，则该过程可能会很复杂，因为您必须手动创建、部署和管理用于加密所有主/主备或控制平面节点上的 etcd 数据的密钥。虽然这可能很繁琐，但如果您的威胁模型要求您自行保管密钥，则此方法具有安全优势。

另一方面，如果您的集群由 AWS、GCP 或 Azure 等云提供商管理，则 etcd 数据的加密默认由云提供商拥有和管理密钥进行设置。

使用托管 Kubernetes，您还可以选择利用各个云提供商的 KMS（密钥管理服务）来创建和使用加密密钥，该密钥将由您管理但由提供商拥有。这通常更容易设置，但要求您信任云提供商的 KMS 服务和您的密钥，并且最终可能非常昂贵，因为密钥通常按调用次数定价。

因此，总结一下，有两种主要选项可以在 Kubernetes etcd 中加密静态机密：

**本地密钥存储：**提供针对 etcd 泄露的保护，但不提供针对主机泄露的保护，因为密钥存储在主机上。最适合自管理 Kubernetes 集群。

**托管 KMS 密钥存储：**利用信封加密并通过不在 Kubernetes 中存储密钥加密密钥来增强安全性。如果您在 AWS、GCP、Azure 等大型云提供商上拥有托管 Kubernetes 集群，这很可能是默认选项。

### 加密提供程序注意事项

Kubernetes 通过各种提供程序促进加密，每个提供程序都有不同的属性和权衡：

| 名称 | 加密 | 强度 | 速度 | 密钥长度 | 备注 |
|---|---|---|---|---|---|
| 默认 - 身份 | 无 | N/A | N/A | N/A | 不加密地写入资源。当设置为第一个提供程序时，充当解密器。 |
| aescbc | 带 PKCS#7 填充的 AES-CBC | 弱 | 快 | 32 字节 | 容易受到填充预言攻击。密钥材料可从控制平面主机访问。 |
| aesgcm | 带随机随机数的 AES-GCM | 必须每 200,000 次写入轮换一次 | 最快 | 16、24 或 32 字节 |
| **加密提供程序** | **密钥加密** | **强度** | **速度** | **密钥大小** | **其他信息** |
|---|---|---|---|---|---|
| **kms v1** (已弃用) | 可配置的 KMS | 最强 | 慢 | 32 字节 | 使用 AES-GCM 进行数据加密，并使用可配置的 KMS 进行密钥加密。支持简单的密钥轮换。 |
| **kms v2** | 可配置的 KMS | 最强 | 快 | 32 字节 | 类似于 KMS v1，但性能和密钥管理得到改进。是第三方密钥管理的可靠选择。从 Kubernetes v1.29 起稳定。 |
| **secretbox** | XSalsa20 和 Poly1305 | 强 | 更快 | 32 字节 | 利用现代加密技术，但可能不符合 FIPS 等特定认证。 |

## 自我管理 Kubernetes 集群的加密

让我们看一个在自我管理 Kubernetes 集群中使用我们自己的密钥设置 etcd 加密的真实示例：

### 步骤 1：生成一个高熵 32 字节密钥

```
openssl rand -base64 32
IPue+NtWYF2dnvKqlLTy2UXok2P+aiJ+eKuVuRd7wt0=
```

### 步骤 2：在 Kubernetes 集群的主节点上部署密钥

**注意**：请务必使用 SSH（安全外壳）之类的工具将密钥部署到 Kubernetes 节点。

在控制平面节点上的路径 `/etc/kubernetes/enc/enc.yaml` 中创建以下 `EncryptionConfiguration`。

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
- resources:
  - secrets
  - configmaps
  - pandas.awesome.bears.example
providers:
# 您的加密提供程序
- secretbox:
  keys:
  - name: key1
  # 您的 32 字节 base64 密钥
  secret: IPue+NtWYF2dnvKqlLTy2UXok2P+aiJ+eKuVuRd7wt0=
  - identity: {} # 此后备允许读取未加密的密钥；
  # 例如，在初始迁移期间
```

### 步骤 3：使用加密配置文件

编辑 kube-apiserver 静态 Pod 的清单：

`/etc/kubernetes/manifests/kube-apiserver.yaml`，使其类似于：

```yaml
#
# 这是静态 Pod 清单的一部分。
# 检查它是否适用于您的集群和 API 服务器。
#
apiVersion: v1
kind: Pod
metadata:
  annotations:
    kubeadm.kubernetes.io/kube-apiserver.advertise-address.endpoint: 10.20.30.40:443
  creationTimestamp: null
  labels:
    app.kubernetes.io/component: kube-apiserver
    tier: control-plane
  name: kube-apiserver
  namespace: kube-system
spec:
  containers:
  - command:
    - kube-apiserver
    ...
    - --encryption-provider-config=/etc/kubernetes/enc/enc.yaml # 👈 指向 EncryptionConfiguration 的路径
  volumeMounts:
    ...
    - name: enc # 添加此行
      mountPath: /etc/kubernetes/enc # 添加此行
      readOnly: true # 添加此行
    ...
  volumes:
    ...
    - name: enc # 添加此行
      hostPath: # 添加此行
      path: /etc/kubernetes/enc # 添加此行
      type: DirectoryOrCreate # 添加此行
    ...
```

### 步骤 4：重新启动 Kube API 服务器

有关 [验证密钥](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/#verifying-that-data-is-encrypted) 实际上已使用新密钥加密、[轮换密钥](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/#rotating-a-decryption-key) 和 [防止纯文本密钥检索](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/#cleanup-all-secrets-encrypted) 的更多信息，请浏览官方 [Kubernetes 文档](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data)。

## 使用云提供商 KMS 的托管 Kubernetes 集群

以下是一些示例，说明我们如何通过利用云提供商的 KMS 在托管 Kubernetes 集群中加密 etcd 中的密钥。

### AWS EKS（弹性 Kubernetes 服务）

AWS 提供了一个集成的密钥管理解决方案，简化了加密提供程序的使用并确保安全密钥处理。默认情况下，这使用 AWS 管理的密钥来加密 etcd 数据，但允许通过 AWS KMS 使用 CMK（客户管理的密钥）。

### GCP GKE（Google Kubernetes Engine）

GCP 同样为安全密钥管理提供了一个集成环境。务必 ✅ 选中“在应用程序层加密密钥”。

### Azure AKS（Azure Kubernetes 服务）

Azure 提供了有关将 Azure 密钥管理服务与 AKS 配合使用的说明。阅读

[将密钥管理服务 etcd 加密添加到 Azure Kubernetes 服务集群](https://learn.microsoft.com/en-us/azure/aks/use-kms-etcd-encryption)

## 将密钥同步到 Kubernetes

接下来，让我们进入有趣的部分——实际部署密钥！

### 1. 通过 Helm 安装 Phase Kubernetes Operator

添加 Phase helm 仓库并更新它：

```
helm repo add phase https://helm.phase.dev && helm repo update
```

让我们安装版本 v1.2.0：

```
helm install phase-secrets-operator phase/phase-kubernetes-operator --set image.tag=v1.2.0
```

您可以在我们的 [GitHub 版本页面](https://github.com/phasehq/kubernetes-secrets-operator/releases) 上找到可用版本。

### 2. 在 Kubernetes 中创建服务令牌密钥
## 1. 创建阶段服务令牌

我们需要创建一个阶段服务令牌，以便操作员可以对阶段服务进行身份验证并获取机密。前往阶段控制台 > 应用程序 > 您的应用程序 > 服务令牌并创建一个令牌。

查看 [阶段文档](https://docs.phase.dev/console/tokens#service-tokens) 以获取有关创建服务令牌的信息。

通过 `kubectl` 安全地创建服务令牌机密至关重要。您可以使用 `read` 命令来执行此操作，建议使用此命令，因为它避免将令牌写入磁盘或 shell 历史记录：

```
read -s TOKEN
kubectl create secret generic phase-service-token \
--from-literal=token=$TOKEN \
--type=Opaque \
--namespace=default
unset TOKEN
```

或者，您只需传递令牌内联：

```
kubectl create secret generic phase-service-token \
--from-literal=token=<TOKEN> \
--type=Opaque \
--namespace=default
```

## 3. 部署阶段机密操作员 CR（自定义资源）

创建一个名为 `phase-secrets-operator-cr.yaml` 的自定义资源文件。此文件将定义阶段机密操作员应如何管理您的机密。以下是有关如何从路径同步所有机密的简单示例 `/` 在阶段控制台中的应用程序中的生产环境中到您的 Kubernetes 集群：

```yaml
apiVersion: secrets.phase.dev/v1alpha1
kind: PhaseSecret
metadata:
  name: keyspace-cloud-phase-secret
  namespace: default
spec:
  phaseApp: 'keyspace.cloud' # 您的阶段应用程序的名称
  phaseAppEnv: 'production' # 要从中获取机密的阶段应用程序环境
  phaseAppEnvPath: '/' # 要从中获取机密的阶段应用程序环境内的路径
  phaseHost: 'https://console.phase.dev' # 可选 - 阶段控制台实例的 URL
  authentication:
    serviceToken:
      serviceTokenSecretReference:
        secretName: 'phase-service-token' # 具有对您的应用程序的访问权限的阶段服务令牌的名称
        secretNamespace: 'default'
  managedSecretReferences:
  - secretName: 'keyspace-cloud-prod-secret' # 阶段将同步的 Kubernetes 托管机密的名称
    secretNamespace: 'default'
```

应用自定义资源：

```
kubectl apply -f phase-secrets-operator-cr.yaml
```

观察正在创建的机密：

```
watch kubectl get secrets
```

### 设置 RBAC（基于角色的访问控制）并更新部署

现在，我们的机密已部署到 Kubernetes，我们需要通过 Kubernetes RBAC 策略控制对它们的访问，以提高安全性。

### 1. 设置用于访问机密的 RBAC 策略

首先，让我们为我们的部署设置一个具有自定义角色（Role）的 RBAC 策略：

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: secret-reader
rules:
- apiGroups: [""]
  resources: ["secrets"]
  resourceNames: ["keyspace-cloud-prod-secret"]
  verbs: ["get", "watch", "list"]
```

此名为 `secret-reader` 的角色允许读取名为 `keyspace-cloud-prod-secret` 的机密 `default` 命名空间并授予以下权限： `get`, `watch`, `list`.

### 2. 为您的应用程序创建一个服务帐户

让我们为我们的部署创建一个 Kubernetes 服务帐户（ServiceAccount）。我们的应用程序的每个 pod 都将使用它。

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: keyspace-app-service-account
  namespace: default
```

### 3. 将角色绑定到服务帐户

接下来，创建一个 `RoleBinding` 以授予 `secret-reader` 角色到 `keyspace-app-service-account`：

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-secret-to-my-app
  namespace: default
subjects:
- kind: ServiceAccount
  name: keyspace-app-service-account
  namespace: default
roleRef:
  kind: Role
  name: secret-reader
  apiGroup: rbac.authorization.k8s.io
```

此名为 `read-secret-to-my-app` 的 `RoleBinding` 将 `secret-reader` 角色与 `keyspace-app-service-account` 关联起来，允许关联的 pod 访问 `keyspace-cloud-prod-secret`.

### 4. 更新您的部署以使用服务帐户

修改您的部署以使用 `keyspace-app-service-account`：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: keyspace-cloud-app-deployment
annotations:
  secrets.phase.dev/redeploy: 'true' # 👈 机密更改后自动重新部署我的应用程序
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      serviceAccountName: keyspace-app-service-account # 👈 我们刚刚创建的服务帐户
      containers:
      - name: my-app
        image: my-app-image
        envFrom:
        - secretRef:
            name: keyspace-cloud-prod-secret # 👈 应用程序机密
```

在此部署中，`spec.serviceAccountName` 字段设置为 `keyspace-app-service-account`，确保 pod 使用授予服务帐户的权限运行，从而遵守 `Role` 和 `RoleBinding` 中定义的原则。

通过设置这些 RBAC 策略，您可以确保只有您的应用程序具有对其所需的机密进行访问的必要权限，从而遵守 Kubernetes 中的安全性和访问控制最佳实践。