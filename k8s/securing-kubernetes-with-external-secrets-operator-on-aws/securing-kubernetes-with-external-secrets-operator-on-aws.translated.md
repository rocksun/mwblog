# 使用 AWS 上的 External Secrets Operator 保护 Kubernetes

![使用 AWS 上的 External Secrets Operator 保护 Kubernetes 的特色图片](https://cdn.thenewstack.io/media/2025/03/65c162af-secrets-1024x576.jpg)

[密钥管理](https://thenewstack.io/the-challenges-of-secrets-management-from-code-to-cloud/)是现代应用程序开发的一个重要方面。 确保数据库凭据、证书、API 密钥、密码和令牌等敏感信息得到安全存储和访问至关重要。[Kubernetes](https://thenewstack.io/kubernetes/) 提供了一个用于管理密钥的内置解决方案，但将其与 [AWS Secrets Manager](https://thenewstack.io/managing-kubernetes-secrets-with-aws-secrets-manager/) 等外部密钥存储集成可提供增强的安全性、灵活性和可扩展性。 用户可以轻松轮换其凭据以增强安全性，并且这将复制到 Kubernetes 集群中的下游应用程序。
在本教程中，我将引导您完成使用 External Secrets Operator (ESO) 和 AWS Secrets Manager 管理 Kubernetes 集群中的密钥的过程。

**什么是 External Secrets Operator (ESO)？**

[External Secrets Operator](https://external-secrets.io/latest/) 使开发人员能够通过将密钥从外部密钥存储（如 [AWS](https://aws.amazon.com/?utm_content=inline+mention) Secret Manager、[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure Key Vault 和 [HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention) Vault）同步到 Kubernetes 来简化密钥管理。 通过使用 ESO，您可以定义一个 Kubernetes 自定义资源 (CRD)，您可以在其中指定从中获取密钥的位置（外部密钥存储）、要获取的密钥以及如何将它们与 Kubernetes Secrets 同步。

**为什么要使用 External Secrets Operator？**

**集中式管理**：External Secrets Operator 提供集中式存储，用于管理跨多个环境的密钥，从而降低了管理大规模和多个应用程序的密钥的复杂性。 例如，当密钥存储在 AWS Secrets Manager 中时，可以更轻松地将其配置为在特定时间段内轮换。

**自动同步**：External Secrets Operator 自动从外部密钥源同步，确保应用程序始终拥有最新的密钥，而无需任何手动干预。

**合规性和审计**：External Secrets Operator 使用外部密钥存储，通过使用 AWS Secrets Manager 的内置密钥轮换、详细的审计日志和访问控制功能，简化了对 GDPR 和支付卡行业数据安全标准 (PCI DSS) 的合规性。

**开始使用**

请按照本指南操作，并确保您已准备好以下内容：

- 正在运行的 Kubernetes 集群（例如，EKS）。
- 在您的工作站上安装并配置了 `kubectl` 二进制文件。 这将用于应用 Kubernetes 清单。
- 配置了 AWS 命令行界面 (CLI) 的 AWS 账户。
- 在 AWS Secrets Manager 和 Kubernetes 中创建资源所需的权限。
- Helm，一个 Kubernetes 的包管理器，它简化了部署、管理和扩展 Kubernetes 应用程序的过程，必须安装。

**步骤 1：安装 External Secrets Operator (ESO)**

**a. 添加 ESO Helm 存储库**。

```
helm repo add external-secrets https://charts.external-secrets.io
helm repo update
```

**b. 安装 ESO**：这将在 `external-secrets` 命名空间中创建一个 external secrets operator。

```
helm install external-secrets external-secrets/external-secrets -n external-secrets --create-namespace
```

**c. 通过运行以下命令验证安装**。

```
kubectl get all -n external-secrets
```

![](https://cdn.thenewstack.io/media/2025/03/137f7709-image2.png)

**步骤 2：在 AWS Secrets Manager 中创建密钥**

- 登录到 AWS。
- 在 AWS 管理控制台中打开 AWS Secrets Manager。
- 创建一个新密钥，例如 `Key: DB_PASSWORD` 和 `Value: my-secret-password`。
- 完成后，记下密钥 Amazon 资源名称 (ARN)。

**步骤 3：为 ESO 创建 SecretStore**

[SecretStore](https://external-secrets.io/v0.5.8/api-secretstore/) 是一个 Kubernetes 自定义资源定义 (CRD)，由 External Secrets Operator 引入。 它定义了用于访问 AWS Secrets Manager 等服务中的外部密钥的配置详细信息。 本质上，SecretStore 包含 ESO 可以访问密钥的位置和方式的详细信息。

在创建 SecretStore 之前，您需要授予 SecretStore 访问您在 AWS Secrets Manager 中新创建的密钥的权限。 在创建 SecretStore 之前，您将创建以下资源作为先决条件。
**a. 创建 IAM 策略**: 身份和访问管理 (IAM) 策略将允许访问您在 AWS Secrets Manager 中新创建的密钥。将下面的 ARN 替换为您在 AWS Secrets Manager 中新创建的密钥的 ARN。

```
123456789101112 |
```

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["secretsmanager:GetSecretValue"],
      "Resource": "arn:aws:secretsmanager:region:account-id:secret:your-secret-id"
    }
  ]
}
```

**b. 创建 IAM 角色**: 创建一个 IAM 角色，并将上面示例中创建的 IAM 策略附加到该角色。指定该角色的信任关系，以允许 EKS 集群代入该角色。

```
123456789101112 |
```

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "eks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

**c. 将 IAM 角色关联到 Kubernetes 中的服务帐户**: 您可以使用 `eks.amazonaws.com/role-arn` 注解将您的 IAM 角色关联到 Kubernetes 服务帐户，以安全地向您在 EKS 集群中运行的工作负载授予细粒度的 AWS 权限，而无需在您的应用程序中保留长期凭据。

```
1234567 |
```

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: external-secrets-sa
  namespace: external-secrets
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::123456789012:role/ExternalSecretsRole
```

将上面的代码复制到文件名为 `sa-secretstore.yaml` 的文件中，并将 `eks.amazonaws.com/role-arn` 替换为您的 IAM 角色 ARN 的值。然后运行以下命令应用清单：

```
1 |
```

```bash
kubectl apply -f sa-secretstore.yaml -n external-secrets
```

**d. 创建 SecretStore 以使用服务帐户**: 将下面的 Kubernetes 清单复制并粘贴到文件名为 `secretstore-eso.yaml` 的文件中，然后应用该清单。

```
1234567891011121314 |
```

```yaml
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: aws-secret-store
  namespace: external-secrets
spec:
  provider:
    aws:
      service: SecretsManager
      region: us-east-1
      auth:
        jwt:
          serviceAccountRef:
            name: external-secrets-sa
```

使用以下命令应用 Kubernetes 清单：

```
1 |
```

```bash
kubectl apply -f secretstore-eso.yaml
```

**步骤 4：创建 ExternalSecret 资源**
定义一个 ESO 来获取 AWS 密钥并将其同步到您的 Kubernetes 集群中。将下面的 Kubernetes 清单复制并粘贴到文件名为 `eso.yaml` 的文件中，然后应用该清单。

```
1234567891011121314151617 |
```

```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: my-app-secrets
  namespace: external-secrets
spec:
  refreshInterval: 1h # Set the refresh interval for secrets
  secretStoreRef:
    name: aws-secret-store
    kind: SecretStore # Referencing the SecretStore created earlier
  target:
    name: my-app-secrets
    creationPolicy: Owner # This ensures the Secret is owned by the ExternalSecret
  data:
    - secretKey: DB_PASSWORD # This is the key in the Kubernetes Secret
      remoteRef:
        key: arn:aws:secretsmanager:us-east-1:abc:secret:eso/example/secrets-Eq5llj #Replace this with the ARN of your AWS Secrets Manager
```

使用以下命令应用 Kubernetes 清单：

```
1 |
```

```bash
kubectl apply -f eso.yaml
```

**结论**
安全地管理密钥是在 Kubernetes 中运行应用程序的一个非常重要的方面。通过将 External Secret Operator 与 AWS Secrets Manager 结合使用，您可以集中管理您的密钥，方便地轮换密钥而不会停机，启用自动同步，并通过减少密钥暴露风险来提高安全性。此外，使用 ESO 可确保应用程序始终可以访问最新的密钥，而无需任何手动干预。

为了进一步增强您的设置，请考虑实施：

**密钥轮换**: 在 AWS Secrets Manager 中启用密钥的自动轮换。**监控和审计**: 使用 AWS CloudTrail 和 Kubernetes 日志记录来跟踪密钥访问和更新。
通过此设置，您将拥有一个可扩展且安全的解决方案，用于处理 Kubernetes 中的密钥，从而使密钥管理更加轻松和可靠。

想要掌握 Kubernetes 中的数据库管理吗？解锁 [Andela 的 8 步指南](https://www.andela.com/blog-posts/how-to-run-databases-on-kubernetes-an-8-step-guide/?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack&utm_content=kubernetes-blog&utm_term=writers-room)，了解如何在 Kubernetes 环境中高效运行数据库，从而推动工作流程的创新。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)