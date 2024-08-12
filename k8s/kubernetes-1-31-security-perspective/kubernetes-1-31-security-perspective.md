
<!--
title: Kubernetes 1.31您应该了解的关键安全增强功能
cover: https://www.armosec.io/wp-content/uploads/2024/08/Kubernetes_1.31_X_LI_a.png
-->

探索 Kubernetes 1.31 中的关键安全改进，包括 AppArmor 支持、增强的密钥管理以打造更安全的平台等等。

> 译自 [Kubernetes 1.31: Key Security Enhancements You Should Know](https://www.armosec.io/blog/kubernetes-1-31-security-perspective/)，作者 Ben Hirschberg。

[Kubernetes v1.31](https://www.kubernetes.dev/resources/release/) 为这个流行的容器编排平台带来了一些值得注意的改进，提升了平台的安全性和其他方面。
这些增强功能改进了帐户令牌、标签、策略和其他领域，以确保为开发人员和企业提供更安全、更可靠的平台。

Kubernetes v1.31 引入了几个与安全相关的改进，这些改进提高了平台和工作负载的整体安全态势。

## #24 AppArmor 支持

AppArmor 支持增强功能 (KEP-24) 将 AppArmor 集成到 Kubernetes 中，提供了一种为 Pod 和容器强制执行强制访问控制 (MAC) 策略的方法。

AppArmor 是一个 Linux 安全模块，它通过配置文件限制程序的功能，从而降低了安全漏洞的风险。通过允许用户在 Kubernetes 清单中指定 AppArmor 配置文件，此增强功能有助于隔离和保护工作负载，确保即使应用程序受到攻击，其造成损害的能力也会受到预定义安全策略的限制。

**关键方面：**

* **配置文件规范**: 用户可以在 Pod 清单中定义 AppArmor 配置文件。
* **配置文件强制执行**: 指定的配置文件在运行时强制执行，限制容器的功能。
* **隔离**: 增强工作负载之间的隔离，减少攻击面。
* **安全**: 通过限制其操作来帮助减轻受损应用程序的潜在损害。

**好处：**

* **增强安全性**: 通过限制应用程序可以执行的操作，即使受到攻击。
* **细粒度控制**: 提供对容器权限的细粒度控制。
* **合规性**: 通过强制执行严格的访问控制来帮助满足安全合规性要求。

**实现细节：**

1. **注释**: AppArmor 配置文件使用 Pod 定义中的注释指定。
2. **配置文件管理**: 管理员需要管理和维护节点上的 AppArmor 配置文件。

**兼容性**: 需要底层节点支持 AppArmor。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: sample-pod
  annotations:
    container.apparmor.security.beta.kubernetes.io/container-name: localhost/profile-name
spec:
  containers:
  - name: container-name
    image: sample-image
```

有关更详细的信息，请访问 [KEP-24 问题页面](https://github.com/kubernetes/enhancements/issues/24)。

## #2535 确保已拉取私密镜像

此 Kubernetes 增强功能增强了拉取需要密钥的容器镜像的安全性，例如私有注册表凭据。主要目标是确保这些密钥在镜像拉取过程中得到安全管理和使用，从而减轻与未经授权访问敏感数据相关的风险。

**关键方面：**

1. **安全密钥管理**: 确保用于镜像拉取的密钥得到安全管理。
2. **访问控制**: 实施访问控制以防止未经授权访问这些密钥。
3. **审计和日志记录**: 增强审计和日志记录以跟踪密钥使用情况和访问情况。

**好处：**

1. **改进的安全性**: 降低未经授权访问私有镜像的风险。
2. **合规性**: 通过安全处理密钥来帮助满足安全和合规性要求。
3. **可见性**: 提供对密钥使用情况和潜在安全问题的更好可见性。

**实现细节：**

1. **Kubelet 增强功能**: 修改 Kubelet 以在镜像拉取过程中安全地处理密钥。
2. **密钥分发**: 确保密钥安全地分发到节点并适当地使用。
3. **配置**: 管理员可以配置策略来管理在镜像拉取过程中如何处理密钥。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
spec:
  containers:
  - name: example-container
    image: private-registry.example.com/my-image
    imagePullSecrets:
    - name: my-registry-secret
```

有关更详细的信息，请访问 [KEP-2535 问题页面](https://github.com/kubernetes/enhancements/issues/2535)。

## #4633 仅允许配置的端点的匿名身份验证

此 Kubernetes 增强功能通过将匿名身份验证限制为仅特定预配置的端点来提高安全性。其目标是降低与不受限制的匿名访问相关的风险，这些风险可能被恶意用户利用。

**关键方面：**

1. **受控访问**: 仅将匿名访问限制为特定的安全端点。
2. **配置**: 管理员可以定义哪些端点允许匿名访问。
3. **安全**: 通过最大限度地减少潜在的攻击面来增强整体集群安全性。

**好处：**

1. **增强安全性**: 降低未经授权访问的风险。
2. **合规性**: 有助于满足安全合规性要求。
3. **细粒度控制**: 提供对端点访问的细粒度控制。

**实现细节：**

1. **API 服务器配置**: API 服务器中的更改以支持此功能。
2. **端点管理**: 管理员在配置文件中指定端点。

有关更详细的信息，请访问 [KEP-4633 问题页面](https://github.com/kubernetes/enhancements/issues/4633)。

## #4193 绑定服务帐号 Token 改进

此增强旨在提高 Kubernetes 中绑定服务帐户令牌的安全性以及可用性。这些令牌用于向 [Kubernetes API 服务器](https://www.armosec.io/glossary/kubernetes-api/) 和其他服务进行身份验证。目标是增强其生命周期管理、轮换和撤销，解决与长期令牌相关的安全问题。

**关键方面：**

1. **令牌绑定到 Pod**: 令牌与 Pod 的生命周期紧密相连，确保它们仅在 Pod 存在时有效。
2. **自动轮换**: 令牌会自动轮换，降低了令牌被泄露后被滥用的风险。
3. **撤销**: 增强了在不再需要令牌时撤销令牌的能力。

**优势：**

1. **提高安全性**: 降低了与长期和过时令牌相关的风险。
2. **易于使用**: 简化了开发人员和运营人员的令牌管理。
3. **合规性**: 通过确保强大的令牌管理，帮助满足安全合规性要求。

**实现细节：**

1. **TokenRequest API**: 引入了一个新的 API 来请求绑定到 Pod 生命周期 的令牌。
2. **更短的令牌生命周期**: 将令牌配置为具有更短的生命周期，并具有自动续订机制。
3. **撤销机制**: 提供了在不再需要令牌或 Pod 被终止时撤销令牌的机制。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
spec:
  serviceAccountName: example-service-account
  containers:
  - name: example-container
    image: example-image
```

有关更详细的信息，请访问 [KEP-4193 文档](https://github.com/kubernetes/enhancements/tree/master/keps/sig-auth/4193-bound-service-account-token-improvements)。

## #3908 kube-apiserver 支持进程外 JWT 签名

此增强旨在通过支持进程外 JSON Web 令牌 (JWT) 签名来提高 Kubernetes API 服务器的安全性以及灵活性。这允许 API 服务器将签名令牌的责任委托给外部进程或服务，从而增强安全性以及可扩展性。

**关键方面：**

1. **外部 JWT 签名**: 允许 Kubernetes API 服务器使用外部进程来签名 JWT。
2. **提高安全性**: 降低了 API 服务器直接处理私钥相关的风险。
3. **可扩展性**: 通过将令牌签名卸载到专门的服务来增强可扩展性。

**优势：**

1. **增强安全性**: 隔离签名过程，减少攻击面。
2. **灵活性**: 允许与外部身份提供者以及签名服务集成。
3. **改进管理**: 简化密钥管理以及轮换流程。

**实现细节：**

1. **配置**: 管理员配置 API 服务器以将 JWT 签名委托给外部进程。
2. **外部签名服务**: 外部服务必须实现特定的 API 来处理签名请求。

有关更详细的信息，请访问 [KEP-3908 文档](https://github.com/kubernetes/enhancements/issues/3908)。

## #4601 带字段和选择器标签的授权

此增强引入了在授权策略中使用字段选择器以及标签选择器的功能，从而允许在 Kubernetes 中进行更细粒度的访问控制。通过启用这些选择器，管理员可以根据资源字段以及标签定义精确的规则，从而提高访问控制系统的灵活性和安全性。

**关键方面：**

1. **字段选择器**: 允许授权策略使用资源字段值。
2. **标签选择器**: 允许在访问控制决策中使用资源标签。
3. **细粒度访问控制**: 提供对谁可以访问特定资源的更精细控制。

**优势：**

1. **增强安全性**: 通过允许精确的访问控制来减少过度授权。
2. **灵活性**: 支持基于资源属性的复杂策略。
3. **改进管理**: 简化创建详细以及具体的授权规则。

**实现细节：**

1. **策略定义**: 管理员可以使用字段选择器以及标签选择器定义策略。
2. **API 服务器更改**: 对 API 服务器进行修改以在授权检查中支持这些选择器。

有关更多详细信息，请访问 [KEP-4601 文档](https://github.com/kubernetes/enhancements/tree/master/keps/sig-auth/4601-authorize-with-selectors)。

## #3962 准入策略修改

此增强旨在在 Kubernetes 中引入修改准入策略，提供一种灵活的方式来修改对 API 服务器的请求。这些策略在请求被持久化之前进行评估以及应用，从而能够根据自定义条件动态修改资源。

**关键方面：**

1. **动态修改**: 允许在 API 请求被持久化之前修改它们。
2. **自定义策略**: 支持用于修改请求的自定义条件。
3. **灵活性**: 增强了 Kubernetes 准入控制的灵活性。

**优势：**

1. **增强安全性**: 通过允许精确的访问控制来减少过度授权。
2. **灵活性**: 支持基于资源属性的复杂策略。
3. **改进管理**: 简化创建详细以及具体的授权规则。

**实现细节：**

1. **策略定义**: 管理员可以使用字段选择器以及标签选择器定义策略。
2. **准入Webhook**：利用修改准入Webhook来应用已定义的策略。

## 准入策略修改 VS 与 webhook 修改 

Kubernetes 中的修改准入策略和修改准入 webhook 用于在 API 服务器将请求持久化之前修改该请求。不过，在它们的操作方式和灵活性上有明显的区别。下表给出了两者之间的比较。

![](https://www.armosec.io/wp-content/uploads/2024/08/Kubernetes-1.31_A-Security-Perspective.png)

## 结论

Kubernetes v1.31 为平台带来了多项增强功能，显著地改善了平台内的安全性、可扩展性和开发者体验。主要要点包括：

1. **增强型安全机制**：AppArmor 等集成支持（[KEP-24](https://github.com/kubernetes/enhancements/issues/24)）以用于强制访问控制，改进秘密拉取镜像管理（[KEP-2535](https://github.com/kubernetes/enhancements/issues/2535)），以及匿名验证限制（[KEP-4633](https://github.com/kubernetes/enhancements/issues/4633)）增强 Kubernetes 内工作负载和数据安全性。
2. **改进令牌管理**：限定服务帐号令牌（[KEP-4193](https://github.com/kubernetes/enhancements/issues/4193)）的增强确保更好的生命周期管理、轮换和撤销，从而减少与长期令牌相关联的风险。
3. **高级授权控制**：如进程外 JWT 签名（[KEP-3908](https://github.com/kubernetes/enhancements/issues/3908)）和带有选择器的授权（[KEP-4601](https://github.com/kubernetes/enhancements/issues/4601)）等特性提供了更精细、更灵活的访问控制和安全措施。
4. **灵活准入策略**：可变准入策略的推出（[KEP-3962](https://github.com/kubernetes/enhancements/issues/3962)）允许动态修改 API 请求，从而增强对资源配置和安全性的控制。

这些更新强调了 Kubernetes 致力于推进其安全性和可扩展性，使其成为面向开发人员和企业的更安全、更可靠的平台。有关更多详细信息，请访问相应的 KEP 问题页面和文档。分享