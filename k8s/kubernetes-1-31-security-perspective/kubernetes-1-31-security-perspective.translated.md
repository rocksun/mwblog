## Kubernetes 1.30：安全视角

Kubernetes 1.30 是这个广泛使用的编排平台发展史上的一个重要里程碑，...

2024 年 8 月 8 日

[Kubernetes v1.31](https://www.kubernetes.dev/resources/release/) 为这个流行的容器编排平台带来了一些值得注意的改进，提升了平台的安全性和其他方面。
这些增强功能改进了帐户令牌、标签、策略和其他领域，以确保为开发人员和企业提供更安全、更可靠的平台。

Kubernetes v1.31 引入了几个与安全相关的改进，这些改进提高了平台和工作负载的整体安全态势。

### AppArmor 支持增强功能 (KEP-24)

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

* **注释**: AppArmor 配置文件使用 Pod 定义中的注释指定。
* **配置文件管理**: 管理员需要管理和维护节点上的 AppArmor 配置文件。
* **兼容性**: 需要底层节点支持 AppArmor。

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

### 安全的镜像拉取密钥管理 (KEP-2535)

此 Kubernetes 增强功能增强了拉取需要密钥的容器镜像的安全性，例如私有注册表凭据。主要目标是确保这些密钥在镜像拉取过程中得到安全管理和使用，从而减轻与未经授权访问敏感数据相关的风险。

**关键方面：**

* **安全密钥管理**: 确保用于镜像拉取的密钥得到安全管理。
* **访问控制**: 实施访问控制以防止未经授权访问这些密钥。
* **审计和日志记录**: 增强审计和日志记录以跟踪密钥使用情况和访问情况。

**好处：**

* **改进的安全性**: 降低未经授权访问私有镜像的风险。
* **合规性**: 通过安全处理密钥来帮助满足安全和合规性要求。
* **可见性**: 提供对密钥使用情况和潜在安全问题的更好可见性。

**实现细节：**

* **Kubelet 增强功能**: 修改 Kubelet 以在镜像拉取过程中安全地处理密钥。
* **密钥分发**: 确保密钥安全地分发到节点并适当地使用。
* **配置**: 管理员可以配置策略来管理在镜像拉取过程中如何处理密钥。

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

### 受控匿名访问 (KEP-2536)

此 Kubernetes 增强功能通过将匿名身份验证限制为仅特定预配置的端点来提高安全性。其目标是降低与不受限制的匿名访问相关的风险，这些风险可能被恶意用户利用。

**关键方面：**

* **受控访问**: 仅将匿名访问限制为特定的安全端点。
* **配置**: 管理员可以定义哪些端点允许匿名访问。
* **安全**: 通过最大限度地减少潜在的攻击面来增强整体集群安全性。

**好处：**

* **增强安全性**: 降低未经授权访问的风险。
* **合规性**: 有助于满足安全合规性要求。
* **细粒度控制**: 提供对端点访问的细粒度控制。

**实现细节：**

* **API 服务器配置**: API 服务器中的更改以支持此功能。
* **端点管理**: 管理员在配置文件中指定端点。
有关更详细的信息，请访问 [KEP-4193 问题页面](https://github.com/kubernetes/enhancements/issues/4633)。

此增强旨在提高 Kubernetes 中绑定服务帐户令牌的安全性以及可用性。这些令牌用于向 [Kubernetes API 服务器](https://www.armosec.io/glossary/kubernetes-api/) 和其他服务进行身份验证。目标是增强其生命周期管理、轮换和撤销，解决与长期令牌相关的安全问题。

**关键方面：**
* **令牌绑定到 Pod**: 令牌与 Pod 的生命周期紧密相连，确保它们仅在 Pod 存在时有效。
* **自动轮换**: 令牌会自动轮换，降低了令牌被泄露后被滥用的风险。
* **撤销**: 增强了在不再需要令牌时撤销令牌的能力。

**优势：**
* **提高安全性**: 降低了与长期和过时令牌相关的风险。
* **易于使用**: 简化了开发人员和运营人员的令牌管理。
* **合规性**: 通过确保强大的令牌管理，帮助满足安全合规性要求。

**实现细节：**
* **TokenRequest API**: 引入了一个新的 API 来请求绑定到 Pod 生命周期 的令牌。
* **更短的令牌生命周期**: 将令牌配置为具有更短的生命周期，并具有自动续订机制。
* **撤销机制**: 提供了在不再需要令牌或 Pod 被终止时撤销令牌的机制。

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

此增强旨在通过支持进程外 JSON Web 令牌 (JWT) 签名来提高 Kubernetes API 服务器的安全性以及灵活性。这允许 API 服务器将签名令牌的责任委托给外部进程或服务，从而增强安全性以及可扩展性。

**关键方面：**
* **外部 JWT 签名**: 允许 Kubernetes API 服务器使用外部进程来签名 JWT。
* **提高安全性**: 降低了 API 服务器直接处理私钥相关的风险。
* **可扩展性**: 通过将令牌签名卸载到专门的服务来增强可扩展性。

**优势：**
* **增强安全性**: 隔离签名过程，减少攻击面。
* **灵活性**: 允许与外部身份提供者以及签名服务集成。
* **改进管理**: 简化密钥管理以及轮换流程。

**实现细节：**
* **配置**: 管理员配置 API 服务器以将 JWT 签名委托给外部进程。
* **外部签名服务**: 外部服务必须实现特定的 API 来处理签名请求。

有关更详细的信息，请访问 [KEP-3908 文档](https://github.com/kubernetes/enhancements/issues/3908)。

此增强引入了在授权策略中使用字段选择器以及标签选择器的功能，从而允许在 Kubernetes 中进行更细粒度的访问控制。通过启用这些选择器，管理员可以根据资源字段以及标签定义精确的规则，从而提高访问控制系统的灵活性和安全性。

**关键方面：**
* **字段选择器**: 允许授权策略使用资源字段值。
* **标签选择器**: 允许在访问控制决策中使用资源标签。
* **细粒度访问控制**: 提供对谁可以访问特定资源的更精细控制。

**优势：**
* **增强安全性**: 通过允许精确的访问控制来减少过度授权。
* **灵活性**: 支持基于资源属性的复杂策略。
* **改进管理**: 简化创建详细以及具体的授权规则。

**实现细节：**
* **策略定义**: 管理员可以使用字段选择器以及标签选择器定义策略。
* **API 服务器更改**: 对 API 服务器进行修改以在授权检查中支持这些选择器。

有关更多详细信息，请访问 [KEP-4601 文档](https://github.com/kubernetes/enhancements/tree/master/keps/sig-auth/4601-authorize-with-selectors)。

此增强旨在在 Kubernetes 中引入变异准入策略，提供一种灵活的方式来修改对 API 服务器的请求。这些策略在请求被持久化之前进行评估以及应用，从而能够根据自定义条件动态修改资源。

**关键方面：**
* **动态修改**: 允许在 API 请求被持久化之前修改它们。
* **自定义策略**: 支持用于修改请求的自定义条件。
* **灵活性**: 增强了 Kubernetes 准入控制的灵活性。

**优势：**
* **增强安全性**: 通过允许精确的访问控制来减少过度授权。
* **灵活性**: 支持基于资源属性的复杂策略。
* **改进管理**: 简化创建详细以及具体的授权规则。

**实现细节：**
* **策略定义**: 管理员可以使用字段选择器以及标签选择器定义策略。
* **API 服务器更改**: 对 API 服务器进行修改以在授权检查中支持这些选择器。
**增强控制**: 提供对 API 请求的细粒度控制。**自定义**: 允许管理员定义用于修改资源的自定义逻辑。**改进安全性**: 确保请求在被接受之前满足特定策略。

**实现细节**:

**策略定义**: 管理员使用自定义资源定义 (CRD) 定义变异策略。**准入 Webhook**: 利用变异准入 Webhook 来应用定义的策略。

**变异准入策略与变异 Webhook**

Kubernetes 中的变异准入策略和变异准入 Webhook 都用于在请求持久化之前修改对 API 服务器的请求。但是，它们在操作方式和灵活性方面存在明显差异。下表显示了两者之间的比较。

Kubernetes v1.31 带来了多项增强功能，显著提升了平台的安全性、可扩展性和开发人员体验。主要要点包括：

**增强的安全机制**: 集成 AppArmor 支持（[KEP](https://github.com/kubernetes/enhancements/issues/24)[-24](https://github.com/kubernetes/enhancements/issues/24)）以实现强制访问控制，改进对秘密拉取镜像的管理（[KEP](https://github.com/kubernetes/enhancements/issues/2535)[-2535](https://github.com/kubernetes/enhancements/issues/2535)），以及对匿名身份验证的限制（[KEP-](https://github.com/kubernetes/enhancements/issues/4633)[4633](https://github.com/kubernetes/enhancements/issues/4633)）增强了 Kubernetes 中工作负载和数据的安全性。**改进的令牌管理**: 对绑定服务帐户令牌的增强（[KEP-4193](https://github.com/kubernetes/enhancements/issues/4193)）确保更好的生命周期管理、轮换和撤销，降低了与长期令牌相关的风险。**高级授权控制**: 诸如进程外 JWT 签名（[KEP-3908](https://github.com/kubernetes/enhancements/issues/3908)）和使用选择器进行授权（[KEP-4601](https://github.com/kubernetes/enhancements/issues/4601)）等功能提供了更细粒度和灵活的访问控制和安全措施。**灵活的准入策略**: 变异准入策略的引入（[KEP-3962](https://github.com/kubernetes/enhancements/issues/3962)）允许对 API 请求进行动态修改，增强了对资源配置和安全性的控制。

这些更新突出了 Kubernetes 对提升其安全性及其可用性的承诺，使其成为开发人员和企业更安全、更可靠的平台。有关更多详细信息，请访问相应的 [KEP 问题页面](https://github.com/kubernetes/enhancements/issues) 和 [文档](https://github.com/kubernetes/enhancements/blob/master/keps/README.md)。

Kubernetes 1.30 是这个广泛使用的编排平台发展历程中的一个重要里程碑，...

Kubernetes 1.29 将是 Kubernetes 团队在 2023 年的最后一个版本。新的...

这篇博文深入探讨了 Kubernetes 1.28 中引入的安全增强功能，提供了对... 的见解。

×