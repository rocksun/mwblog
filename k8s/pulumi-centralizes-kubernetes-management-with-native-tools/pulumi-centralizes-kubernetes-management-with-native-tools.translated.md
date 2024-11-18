# Pulumi 使用原生工具集中管理 Kubernetes

![Featued image for: Pulumi 使用原生工具集中管理 Kubernetes](https://cdn.thenewstack.io/media/2024/11/75da641c-pulumi-1024x768.png)

从今年涌现的众多新一代工具来看，[Kubernetes](http://www.thenewstack.io/Kubernetes) 的管理无疑需要大幅简化和增强安全性。云管理中的管理复杂性无疑是 IT 管理员和开发团队担忧的一个因素。

在[KubeCon Salt Lake City 2024](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 上，云基础设施软件制造商 Pulumi 今日发布了其旨在简化和保护 Kubernetes 部署的一套新工具和功能。

这家位于西雅图的公司提供的[基础设施即代码 (IaC) 平台](https://thenewstack.io/pulumi-rocks-ai-infused-infrastructure-as-code-platform/) 现在提供了一个 Kubernetes 原生部署代理，以提高安全性和可扩展性，并更新了其 Amazon EKS 提供程序，从而支持 Amazon Linux 2023 和更新的安全功能。

Pulumi 的最新版本旨在作为应对 Kubernetes 环境管理日益复杂化的解药。随着企业越来越依赖各种云原生工具和多云部署，管理基础设施、确保安全性和维护对 Kubernetes 资源的可见性变得越来越具有挑战性。

首席执行官 [Joe Duffy](https://thenewstack.io/qa-pulumis-joe-duffy-on-the-renaissance-of-infrastructure-as-code/) 告诉 The New Stack：“传统的基础设施管理工具难以处理 Kubernetes 部署的规模和复杂性。”Pulumi 使用熟悉的[编程语言](https://thenewstack.io/programming-languages/) 和 AI 来简化这些任务。

管理 Kubernetes 工作负载越来越复杂，因为它们依赖于许多不同的[云原生计算基金会](https://cncf.io/?utm_content=inline+mention) (CNCF) 产品，并跨越多个云。这种复杂性给管理基础设施、保护云工作负载以及在所有 Kubernetes 资源和基础设施中获得可观察性带来了重大挑战。Duffy 表示，基础设施管理已被无法处理分布在多个集群中的数百个 Kubernetes 资源的传统工具所束缚。

Pulumi 基础设施即代码 (IaC) 为这些问题提供了一种新一代解决方案。团队现在可以使用熟悉的通用编程语言（借助生成式 AI 功能）来编写其云基础设施和 Kubernetes 资源，而不是使用专门的语言。

更新详情包括：
**Pulumi Kubernetes Operator 2.0:** Introduces dedicated workspace Pods to improve isolation, scalability, and access control. This automates infrastructure deployment and management by running Pulumi programs directly within the Kubernetes cluster, enabling teams to manage cloud resources alongside native Kubernetes resources. Pulumi Kubernetes Operator 2.0 is a major upgrade that introduces a dedicated "workspace" Pod for each stack resource, effectively isolating compute and memory resources for each stack, improving key isolation, and providing new customization options. The Operator can now scale horizontally, improving performance and enabling teams to more reliably manage complex Kubernetes setups.

**Improved Amazon Elastic Kubernetes Service (EKS) provider:** Adds support for Amazon Linux 2023, Bottlerocket, EKS Pod Security Groups, and Network Policies. This ensures workloads are optimized for performance and compliance while addressing the deprecation of Amazon Linux 2. It automates the management of key EKS components such as vpc-cni, coredns, and kube-proxy, reducing operational overhead. Improved networking capabilities, such as Pod Security Groups, allow for fine-grained control over traffic within the cluster, enhancing security.

**Pulumi ESC integration with External Secrets Operator:** Simplifies secure key management in Kubernetes applications. This integration addresses the challenges of native Kubernetes key management (e.g., less secure and difficult to manage). It provides more secure key storage and cross-environment access by synchronizing keys with external systems such as AWS Secrets Manager, HashiCorp Vault, and Pulumi ESC. Pulumi ESC is unique in that it provides a centralized key management and orchestration service that easily and securely manages key sprawl and configuration complexity across all cloud infrastructure and applications. Keys can be pulled and synced from any key store, including HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, 1Password, etc., and used in any application, tool, or CI/CD platform.

**Pulumi Insights:** Provides unified search, compliance remediation, and visualization across all infrastructure resources.

"With today's release, customer-managed Pulumi deployment agents now allow organizations to host the Pulumi deployment agent within their Kubernetes environments, increasing their flexibility and control over their infrastructure deployments," Duffy told The New Stack. "Kubernetes native support provides greater flexibility, scalability, and security for self-hosted Pulumi deployment agents. The agent deploys directly into the Kubernetes cluster." See the [code here](https://github.com/pulumi/customer-managed-deployment-agent/tree/main/kubernetes).

[Snowflake](https://www.snowflake.com/?utm_content=inline+mention), insurance provider [Lemonade](https://www.lemonade.com/renters), and the [North Carolina Climate Institute](https://ncics.org/) are current Pulumi customers. Customer-managed agents are available on the [business-critical release of Pulumi Cloud](https://www.pulumi.com/blog/business-critical-launch/).

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)  Technology moves fast. Don't miss an episode. Subscribe to our YouTube channel to watch all our podcasts, interviews, demos, and more.