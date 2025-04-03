<!--
title: 如何使用 Vault 集中管理 Kubernetes 密钥
cover: https://cdn.thenewstack.io/media/2025/03/6fac0638-centralize-kubernetes-secrets-management-vault2.jpg
summary: 告别 K8s 密钥管理噩梦！用 HashiCorp Vault 集中管理 K8s 密钥，告别明文存储风险。通过 K8s 认证集成 Vault，利用 Secrets Store CSI Driver 安全注入密钥，无需直接 API 调用，实现跨集群密钥同步和自动轮换，提升云原生应用安全性和运维效率！
-->

告别 K8s 密钥管理噩梦！用 HashiCorp Vault 集中管理 K8s 密钥，告别明文存储风险。通过 K8s 认证集成 Vault，利用 Secrets Store CSI Driver 安全注入密钥，无需直接 API 调用，实现跨集群密钥同步和自动轮换，提升云原生应用安全性和运维效率！

> 译自：[How To Centralize Kubernetes Secrets Management With Vault](https://thenewstack.io/how-to-centralize-kubernetes-secrets-management-with-vault/)
> 
> 作者：Utku Darılmaz

在 [Kubernetes](https://thenewstack.io/kubernetes/) (K8s) 环境中管理密钥是一个至关重要但经常被忽视的挑战。许多团队一开始使用 K8s 内置的密钥，但后来才意识到它们存在安全和管理方面的限制。数据库凭证、API 令牌和私钥等密钥是安全应用程序操作的基础，但处理不当可能会使整个系统面临风险。

本文探讨了在 K8s 中管理密钥的挑战，以及为什么仅仅依赖内置的 K8s 密钥会带来安全风险和运营效率低下。它深入探讨了使用像 HashiCorp Vault 这样的[集中式密钥管理](https://thenewstack.io/meet-openbao-an-open-source-fork-of-hashicorp-vault/)解决方案的优势，强调了将 K8s 集群与 Vault 集成的优点，并解释了 [Secrets Store Container Storage Interface (CSI) Driver](https://github.com/kubernetes-sigs/secrets-store-csi-driver) 如何简化密钥检索，而无需直接 API 调用。我还将分享一个实用的架构概述和在多个集群中扩展 Vault 的最佳实践。

## K8s 密钥面临的挑战

默认情况下，[K8s 密钥](https://thenewstack.io/kubernetes-secrets-management-3-approaches-9-best-practices/)以未加密的形式存储在 etcd 中。etcd 是一个分布式键值存储，作为 K8s 的主要数据存储系统，保存所有集群状态和配置，包括部署、服务和密钥。这意味着任何有权访问 etcd 或 K8s API 服务器（作为管理资源和处理来自用户和应用程序的请求的控制平面）的人都可以检索这些密钥。

此外，密钥经常被硬编码到环境变量或配置文件中，当需要在多个应用程序和集群中更新它们时，会造成维护上的噩梦，并增加暴露和管理不善的风险。

一种常见的模式是将密钥存储在 ConfigMaps 中或将它们嵌入到 YAML 文件中，但这种方法会带来几个问题：

- **缺乏加密：** K8s 密钥仅经过 Base64 编码，并非真正加密。
- **有限的访问控制：** K8s 中的基于角色的访问控制 (RBAC) 策略不能提供对谁可以访问密钥的细粒度控制。
- **没有内置的审计跟踪：** 很难跟踪谁访问或修改了密钥。
- **密钥蔓延：** 密钥经常在多个命名空间和应用程序中重复出现。
- **轮换挑战：** 如果没有自动化系统，轮换密钥需要手动更新多个部署。

鉴于这些限制，很明显，仅靠 K8s 密钥不足以实现大规模的安全密钥管理。

## 基于 Vault 的密钥管理

与依赖 K8s 密钥不同，一种更具可扩展性和安全性的方法是将 K8s 集群与像 HashiCorp Vault 这样的外部密钥存储集成。这提供了一个单一的、集中的位置来管理多个集群中的密钥，确保密钥永远不会以纯文本形式存储在 K8s 中。

密钥存储可以实现：

- 应用程序通过 API 调用从 Vault 动态检索密钥。
- 没有密钥存储在 K8s 中，从而消除了暴露风险。
- 强制执行访问控制策略，因此只有授权的服务才能访问特定的密钥。
- 一个地方（Vault）进行所有更新，这些更新会自动传播到所有使用该密钥的集群。
- 自动密钥轮换，降低安全风险和合规负担。

通过集中管理密钥，团队可以降低因错误配置或未经授权的访问而导致密钥泄露的风险。

### 将 K8s 集群连接到 Vault

要将 [Vault 与 K8s 集成](https://thenewstack.io/hashicorp-vault-operator-manages-kubernetes-secrets/)，一种常见的方法是使用 Vault 中的 K8s 身份验证方法。这允许在 K8s 内部运行的工作负载使用 Vault 进行身份验证，而无需静态凭证。

该过程包括：

1. 在高可用设置中部署 Vault。
2. 在 Vault 中启用 K8s 身份验证，将 K8s 服务帐户映射到特定的密钥访问策略。
3. 配置工作负载以使用 Vault 的 API 动态检索密钥，而不是将它们存储在环境变量或 ConfigMaps 中。
4. 使用 Vault Agent 或 Secrets Store CSI Driver 在运行时自动将密钥注入到正在运行的 Pod 中。

### 跨集群同步密钥

在具有多个 K8s 集群的环境中，在 Vault 中集中管理密钥具有显着优势。团队可以将密钥在 Vault 中存储一次，并允许所有集群动态检索它们，而无需手动更新不同集群中的密钥。
例如，考虑一个组织运行五个 K8s 集群，每个集群托管不同的应用程序，但共享通用的环境变量。通过使用 Vault，对密钥的任何更新（例如数据库密码）都可以在 Vault 中进行，并且所有集群将自动检索更新后的版本，而无需手动重新部署应用程序。

### 避免直接调用 Vault API

使用 Vault 时的一个关键考虑因素是避免应用程序直接调用 API。虽然应用程序可以使用其软件开发工具包 (SDK) 直接从 Vault 检索密钥，但这种方法会带来几个挑战：

*   **代码修改：** 应用程序必须包含 Vault 逻辑，从而导致依赖性和供应商锁定。
*   **性能开销：** 对 Vault 的每个 API 请求都会增加延迟，并可能导致速率限制问题。
*   **处理 Vault 凭据：** 应用程序需要凭据才能通过 Vault 进行身份验证，从而带来另一个密钥管理挑战。

更好的方法是使用 Secrets Store CSI Driver，它允许 K8s 将 Vault 中的密钥作为文件挂载到 Pod 中。此方法将应用程序与 Vault 解耦，并确保密钥安全地注入到容器的文件系统中，而无需修改应用程序代码。

## 演示 Vault + Secrets Store 的实际应用

Vault 与 K8s 的一个实际实现是使用 Secrets Store CSI Driver 以及 Vault 的集成。该架构包括：

1. **Vault 服务器：** 集中存储和管理密钥。
2. **Vault CSI daemonset：** 从 Vault 检索密钥并将其与 K8s 同步。
3. **Secrets Store CSI Driver DaemonSet：** 充当抽象层，使来自各种提供商（例如，Vault、AWS Secrets Manager、Azure Key Vault）的密钥可以注入到 Pod 中。
4. **SecretProviderClass CustomResourceDefinition (CRD)：** 定义要从 Vault 获取哪些密钥以及应如何将其公开给工作负载。

## 使用 Vault + K8s 进行实时密钥更新

此设置的一个关键优势是动态更新密钥。如果 Vault 中的密钥发生更改，则可以自动将其传播到正在运行的工作负载。但是，可能需要一些额外的配置才能实现无缝更新：

*   **滚动更新：** 由于 Pod 不会自动重新加载密钥，因此滚动重启工作负载可确保获取更新后的密钥。
*   **Sidecar 方式：** 一些团队使用 Vault sidecar 动态刷新密钥，而无需重新启动 Pod。

在大型 K8s 环境中部署 Vault 时，团队必须仔细平衡安全性、性能和运营效率。高可用性 (HA) 至关重要，需要以 HA 模式部署 Vault，并具有强大的备份和故障转移机制，以防止服务中断。性能优化同样至关重要，特别是对于 Secrets Store CSI DaemonSet，必须配置适当的资源限制以有效地处理高负载。

遵循最小权限原则可确保应用程序和用户只能访问他们需要的密钥，从而最大限度地降低暴露风险。此外，在 Vault 中启用审计日志记录可以提供对密钥访问和修改的可见性，帮助组织保持合规性并快速检测未经授权的活动。通过解决这些考虑因素，团队可以为其 K8s 工作负载实施可扩展、有弹性和安全的密钥管理策略。

## K8s 密钥管理：不仅仅是最佳实践

保护 K8s 中的密钥不仅仅是最佳实践，这是保护敏感数据和维持运营弹性的必要条件。虽然 K8s 的内置密钥管理提供了便利性，但它缺乏企业级安全性所需的加密、细粒度访问控制和生命周期自动化。通过在 Vault 中集中管理密钥，组织可以获得一个强大、可扩展的解决方案，该解决方案简化了密钥分发，强制执行安全策略并实现了自动化轮换。

当与 Secrets Store CSI Driver 结合使用时，团队可以将安全密钥检索无缝集成到其 K8s 工作负载中，而不会引入复杂性或对 Vault 的直接依赖性。随着组织跨多个集群进行扩展，精心设计的密钥管理方法可最大限度地减少人为错误，并通过降低安全风险和提高运营效率来实现更具弹性的基础设施。