
<!--
title: Pulumi使用原生工具集中管理Kubernetes
cover: https://cdn.thenewstack.io/media/2024/11/75da641c-pulumi.png
-->

基础设施即代码 (IaC) 平台现已提供 Kubernetes 原生部署代理，以提高安全性和可扩展性。

> 译自 [Pulumi Centralizes Kubernetes Management with Native Tools](https://thenewstack.io/pulumi-centralizes-kubernetes-management-with-native-tools/)，作者 Chris J Preimesberger。

从今年涌现的众多新一代工具来看，[Kubernetes](http://www.thenewstack.io/Kubernetes) 的管理无疑需要大幅简化和增强安全性。云管理中的管理复杂性无疑是 IT 管理员和开发团队担忧的一个因素。

在[KubeCon Salt Lake City 2024](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 上，云基础设施软件制造商 Pulumi 今日发布了其旨在简化和保护 Kubernetes 部署的一套新工具和功能。

这家位于西雅图的公司提供的[基础设施即代码 (IaC) 平台](https://thenewstack.io/pulumi-rocks-ai-infused-infrastructure-as-code-platform/) 现在提供了一个 Kubernetes 原生部署代理，以提高安全性和可扩展性，并更新了其 Amazon EKS 提供程序，从而支持 Amazon Linux 2023 和更新的安全功能。

Pulumi 的最新版本旨在作为应对 Kubernetes 环境管理日益复杂化的解药。随着企业越来越依赖各种云原生工具和多云部署，管理基础设施、确保安全性和维护对 Kubernetes 资源的可见性变得越来越具有挑战性。

首席执行官 [Joe Duffy](https://thenewstack.io/qa-pulumis-joe-duffy-on-the-renaissance-of-infrastructure-as-code/) 告诉 The New Stack：“传统的基础设施管理工具难以处理 Kubernetes 部署的规模和复杂性。”Pulumi 使用熟悉的[编程语言](https://thenewstack.io/programming-languages/)和 AI 来简化这些任务。

管理 Kubernetes 工作负载越来越复杂，因为它们依赖于许多不同的[云原生计算基金会](https://cncf.io/?utm_content=inline+mention) (CNCF) 产品，并跨越多个云。这种复杂性给管理基础设施、保护云工作负载以及在所有 Kubernetes 资源和基础设施中获得可观察性带来了重大挑战。Duffy 表示，基础设施管理已被无法处理分布在多个集群中的数百个 Kubernetes 资源的传统工具所束缚。

Pulumi 基础设施即代码 (IaC) 为这些问题提供了一种新一代解决方案。团队现在可以使用熟悉的通用编程语言（借助生成式 AI 功能）来编写其云基础设施和 Kubernetes 资源，而不是使用专门的语言。

更新详情包括：

- [**Pulumi Kubernetes Operator 2.0**](https://www.pulumi.com/blog/pulumi-kubernetes-operator-2-0/)：引入专用工作区 Pod，以改进隔离、可扩展性和访问控制。通过直接在 Kubernetes 集群中运行 Pulumi 程序，可以自动化基础设施的部署和管理，使团队能够与 Kubernetes 原生资源一起管理云资源。 Pulumi Kubernetes Operator 2.0 是一项重大升级，为每个堆栈资源引入了专用的“工作区”pod，有效隔离每个堆栈的计算和内存资源，改进秘密隔离，并开辟新的自定义选项。该操作员现在可以水平扩展，提高性能并使团队能够更可靠地管理复杂的 Kubernetes 设置。
- **改进的[Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)提供程序**：添加了对 Amazon Linux 2023、Bottlerocket、Pod 的 EKS 安全组和网络策略的支持。这可确保工作负载针对性能和合规性进行优化，同时解决 Amazon Linux 2 的弃用问题。vpc-cni、coredns 和 kube-proxy 等关键 EKS 组件的管理是自动化的，从而减轻了运营负担。改进的网络功能（例如 Pod 的安全组）可以对集群内的流量进行细粒度控制，从而提高安全性。
- **Pulumi ESC 与[外部 Secrets Operator](https://external-secrets.io/latest/introduction/overview/)集成**：简化 Kubernetes 应用程序内的安全秘密管理。这种集成解决了 Kubernetes 的本机秘密管理挑战（例如，安全性较低且难以管理）。通过同步来自 AWS Secrets Manager、HashiCorp Vault 和 Pulumi ESC 等外部系统的机密，它可以跨环境提供更安全的机密存储和访问。 Pulumi ESC 的独特之处在于，它提供集中式机密管理和编排服务，可以轻松安全地控制所有云基础设施和应用程序中的机密蔓延和配置复杂性。可以从任何密钥存储（包括 HashiCorp Vault、AWS Secrets Manager、Azure Key Vault、GCP Secret Manager、1Password 等）提取和同步密钥，并在任何应用程序、工具或 CI/CD 平台中使用密钥。
- [**Pulumi Insights**](https://www.pulumi.com/product/pulumi-insights/) ：跨所有基础设施资源提供统一搜索、合规性修复和可视化。

“随着今天的发布，客户管理的 Pulumi 部署代理现在允许组织在其 Kubernetes 环境中托管 Pulumi 部署代理，从而提高他们对基础设施部署的灵活性和控制力，”Duffy 告诉 The New Stack。 “Kubernetes 原生支持为自托管 Pulumi 部署代理提供了更大的灵活性、可扩展性和安全性。该代理直接部署到 Kubernetes 集群中。”请参阅[此处的代码](https://github.com/pulumi/customer-managed-deployment-agent/tree/main/kubernetes)。

Snowflake 、保险公司Lemonade和北卡罗来纳州气候研究所是 Pulumi 的当前客户。客户管理代理可在Pulumi Cloud 的业务关键版上使用。
 