<!--
title: 使用 AWS 简化 Kubernetes 中的 Secrets 管理 + 更多
cover: https://www.kubeblogs.com/content/images/size/w1200/2024/11/kb-ima--3-.png
summary: 用External Secrets Operator连接AWS Secrets Manager，简化Kubernetes的Secret管理！通过OIDC配置EKS集群，创建IAM Role，Helm安装Operator，定义ExternalSecret，实现Secret自动同步。保障CI/CD流程安全，解放运维，拥抱云原生！
-->

用`External Secrets Operator`连接`AWS Secrets Manager`，简化`Kubernetes`的`Secret`管理！通过`OIDC`配置`EKS`集群，创建`IAM Role`，`Helm`安装`Operator`，定义`ExternalSecret`，实现`Secret`自动同步。保障`CI/CD`流程安全，解放运维，拥抱云原生！

> 译自：[Simplify your Secrets Management in Kubernetes with AWS + more](https://www.kubeblogs.com/simplifying-secret-management-in-kubernetes/)
> 
> 作者：Dipchand Yadav

在 Kubernetes 中管理密码和 API 密钥等敏感信息可能具有挑战性。你希望确保 Secret 的安全，同时仍然使它们可供你的应用程序使用。

在本指南中，我们将引导你了解如何使用 External Secrets Operator 将 AWS Secrets Manager 与你的 Kubernetes 集群连接起来。到最后，你将拥有一个简单的设置，可以高效且安全地处理 Secret。

对于本教程，**OpenID Connect (OIDC)** 是一项关键要求。它有助于 Kubernetes 服务帐户与 AWS IAM 角色安全地通信。

这种连接允许 External Secrets Operator 从 AWS Secrets Manager 获取 Secret。如果你的集群尚未设置 OIDC，请不要担心，我们将向你展示如何开始。

## 在进入实施部分之前，让我们了解 External Secrets Operator 的工作原理。

### 工作原理

External Secrets Operator 是一个 Kubernetes 控制器，它将 AWS Secrets Manager 等外部 Secret 管理系统与 Kubernetes 集成。以下是基本流程：

1. **外部 Secret 定义**：你在 Kubernetes 中定义一个 `ExternalSecret` 资源，指定要从 AWS Secrets Manager 获取哪些 Secret。
2. **Operator 同步 Secret**：Operator 监视 `ExternalSecret` 资源。当它找到一个时，它会从 AWS Secrets Manager 获取指定的 Secret。
3. **创建 Kubernetes Secret**：然后，Operator 使用获取的数据创建或更新 Kubernetes `Secret` 资源。
4. **应用程序访问 Secret**：然后，你的应用程序可以像访问任何其他 Kubernetes Secret 一样访问这些 Secret，使用环境变量或卷挂载。

![](https://www.kubeblogs.com/content/images/2024/11/image-8.png)

### 为什么选择这种方法？

- **安全性**：Secret 保留在 AWS Secrets Manager 中，该管理器专为安全 Secret 存储而设计。
- **一致性**：集中管理跨多个集群和环境的 Secret。
- **自动化**：在 Secret 更改时自动同步 Secret，从而减少手动更新。

### 涉及的组件

- **AWS Secrets Manager**：在 AWS 中安全地存储你的 Secret。
- **External Secrets Operator**：在你的 Kubernetes 集群中运行，从 AWS 同步 Secret。
- **具有 IAM 角色的服务帐户**：允许 Operator 使用 IAM 角色通过身份验证 AWS，从而利用 Kubernetes 服务帐户。

### 身份验证流程

1. **服务帐户身份验证**：Operator 使用带有 IAM 角色 ARN 注释的 Kubernetes 服务帐户。
2. **IAM 角色承担**：通过 OIDC 提供商，AWS 信任该服务帐户来承担 IAM 角色。
3. **访问 Secrets Manager**：凭借 IAM 角色的权限，Operator 从 AWS Secrets Manager 获取 Secret。

通过了解此流程，你可以了解所有部分如何协同工作，从而使 Secret 管理安全高效。

现在，让我们继续进行分步教程，以在你的集群中进行设置。

## 步骤 1：设置 OIDC 身份提供商

首先，我们将为我们的 EKS 集群设置 OpenID Connect (OIDC) 身份提供商。这将允许 Kubernetes 服务帐户安全地承担 AWS IAM 角色。

### 创建 EKS 集群

如果尚未创建 EKS 集群，请创建一个。AWS 会在此过程中自动为你的集群设置 OIDC 身份提供商。

![](https://www.kubeblogs.com/content/images/2024/11/image-9.png)

**注意**：如果你的 EKS 集群已配置 OIDC，则可以跳过此部分。

### 添加身份提供商（如果尚未创建）

1. **导航到 AWS IAM 控制台**：转到 AWS 管理控制台中的 IAM 服务。
2. **选择“身份提供商”**：从左侧菜单中。
3. **添加提供商**：单击“添加提供商”。
4. **提供商类型**：选择 **OpenID Connect (OIDC)**。
5. **提供商 URL**：粘贴来自你的 EKS 集群的 OIDC URL。
6. **受众**：通常，这是 `sts.amazonaws.com`。这会将你的 EKS 集群与 AWS IAM 链接起来。
7. **完成设置**：查看你的设置，然后单击**添加提供商**。

![](https://www.kubeblogs.com/content/images/2024/11/image-10.png)

*提示：确保提供商 URL 与你的集群的 OIDC URL 匹配。此步骤对于集成顺利进行至关重要。*

## 步骤 2：使用 Web 身份创建 IAM 角色

现在，我们将创建一个 IAM 角色，我们的 Kubernetes 服务帐户可以承担该角色来访问 AWS Secrets Manager。

### 导航到 IAM 角色

1. **转到 IAM 服务**：在 AWS 管理控制台中。
2. **选择“角色”**：从左侧菜单中。
3. **单击“创建角色”**。

### 选择受信任的实体类型

1. **在“选择受信任的实体”下选择“Web 身份”**。
2. **选择身份提供商**：选择你之前设置的 OIDC 提供商。
3. **受众**：输入 `sts.amazonaws.com` 或你使用的特定受众值。

![](https://www.kubeblogs.com/content/images/2024/11/image-11.png)
### 附加权限策略

1. **在策略中搜索 "SecretsManager"**。
2. **选择 "SecretsManagerReadWrite"**：这允许对密钥进行读写访问。

![](https://www.kubeblogs.com/content/images/2024/11/image-12.png)

### 修改信任关系

创建角色后：

1. **导航到角色**：点击您刚刚创建的角色。
2. **转到 "信任关系" 选项卡**。
3. **点击 "编辑信任策略"**：

![](https://www.kubeblogs.com/content/images/2024/11/image-13.png)

*注意：将 `region-code` 和 OIDC ID 替换为您自己的值。*

- **命名约定**：`sub` 值遵循格式 `system:serviceaccount:<namespace>:<service-account-name>`。确保命名空间和服务帐户名称完全匹配。

之后：

![](https://www.kubeblogs.com/content/images/2024/11/image-14.png)

## 步骤 3：安装 External Secrets Operator

在配置 YAML 文件之前，我们将使用 Helm 安装 External Secrets Operator。

### 使用 Helm 安装

**添加 Helm 存储库**：

```bash
helm repo add external-secrets https://charts.external-secrets.io
```

**安装 Operator**：

```bash
helm install external-secrets \
  external-secrets/external-secrets \
  -n external-secrets \
  --create-namespace
```

*或者，您可以参考 **External Secrets Operator 文档** 获取其他安装方法。*

## 步骤4：配置 Kubernetes Manifests

现在，我们将创建必要的 Kubernetes YAML 文件来设置服务帐户、Secret Store 和 External Secret。

### 创建 `service-account.yaml`

此服务帐户将由 External Secrets Operator 用于访问 AWS Secrets Manager。

![](https://www.kubeblogs.com/content/images/2024/11/image-15.png)

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: service-account-external-secrets-operator
  namespace: external-secrets
  annotations:
    eks.amazonaws.com/role-arn: "arn:aws:iam::12858755912:role/SecretsManager" # Replace with your Role ARN
```

### 创建 `secret-store.yaml`

现在您已经在集群中创建了一个通用密钥，下一步是在 Secret Store 配置中引用此密钥。

Secret Store 将允许您的集群使用您存储的 IAM 用户凭证连接到 AWS Secrets Manager。

```yaml
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: aws-secretsmanager # Name of the SecretStore
spec:
  provider:
    aws:
      service: SecretsManager # Specify the AWS service as SecretsManager
      region: us-east-1 # Specify the AWS region where your Secrets Manager is located
      auth:
        secretRef:
          accessKeyIDSecretRef:
            name: aws-secret-user-secret # Reference the Kubernetes secret containing the Access Key ID
            key: access-key # Specify the key within the Kubernetes secret for Access Key ID
          secretAccessKeySecretRef:
            name: aws-secret-user-secret # Reference the Kubernetes secret containing the Secret Access Key
            key: secret-access-key # Specify the key within the Kubernetes secret for Secret Access Key
```

*确保区域与您的密钥存储在 AWS Secrets Manager 中的区域匹配。*

现在您已经配置了 Secret Store，下一步是创建一个 `ExternalSecret`。此资源将定期从 AWS Secrets Manager 获取密钥，并将它们存储在 Kubernetes 密钥中。

![](https://www.kubeblogs.com/content/images/2024/11/image-16.png)

### 创建 `external-secret.yaml`

这指定了要从 AWS Secrets Manager 同步到 Kubernetes 的密钥。

```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: my-external-secrets # Name of the ExternalSecret resource
spec:
  refreshInterval: 10m # Defines the interval to refresh the secret data from AWS Secrets Manager
  secretStoreRef:
    name: aws-secretsmanager # References the SecretStore configured earlier
    kind: SecretStore # Specifies the kind of the reference, which is SecretStore
  target:
    name: my-kubeops-db-secret # Name of the Kubernetes secret that will be created/updated with the fetched data
    creationPolicy: Owner # Defines the ownership policy for the secret; Owner means the secret will be deleted if the ExternalSecret is deleted
  dataFrom:
    - extract:
        key: DB-CREDENTIALS # The key in AWS Secrets Manager that holds the credentials
```

`ExternalSecret` 将自动创建一个名为 `my-kubeops-db-secret` 的新 Kubernetes 密钥。此密钥将安全地存储来自 AWS Secrets Manager 中 `DB-CREDENTIALS` 密钥的所有值。

AWS Secrets Manager 中的值会定期获取并在 Kubernetes 密钥中保持最新，确保您的应用程序始终拥有最新的数据库凭证。创建 `nginx-deployment.yaml`

最后，我们将部署一个使用我们刚刚创建的密钥的 NGINX 应用程序。

```yaml
Finally, we'll deploy an NGINX application that uses the secret we just created.

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: external-secrets
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
          env:
            - name: DB_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: my-kubeops-db-secret
                  key: db-pass
```

在这个部署中，我们使用 Kubernetes secrets 安全地将数据库密码 (`DB_PASSWORD`) 注入到 NGINX 容器中。其工作原理如下：

- `valueFrom.secretKeyRef` 部分引用了名为 `my-kubeops-db-secret` 的 Kubernetes secret。
- `key` 字段 `db-pass` 标识了 secret 中的特定键，其中包含密码值。
- 例如，如果 `my-kubeops-db-secret` 包含一个键值对，例如 `db-pass: kubeops-consulting`，则容器中的环境变量 `DB_PASSWORD` 将具有值 `kubeops-consulting`。

## 结论

就这样！您已使用 External Secrets Operator 成功将 AWS Secrets Manager 与 Kubernetes 集群集成。您的应用程序现在可以安全地访问 secret，而无需对其进行硬编码或手动管理。

如果您正在寻找端到端的可观测性解决方案，并且希望专注于您的产品，而我们负责监控和日志记录基础设施，请随时联系 **kubenine**。我们提供顶级的可观测性解决方案，因此您可以专注于最重要的事情——您的产品。

通过执行这些步骤，您可以简化 CI/CD 流程，同时确保 secret 的安全。通过此设置，管理敏感信息变得轻松，并且您的 Kubernetes 环境保持安全和井井有条。