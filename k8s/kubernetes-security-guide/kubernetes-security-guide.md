
<!--
title: Kubernetes安全入门指南
cover: https://www.hunters.security/hubfs/THE%20BEGINNERS%20GUIDE%20TO%20SECURING%20KUBERNETES-1.jpg
-->

使用我们的完整指南掌握 Kubernetes 安全，非常适合 SOC 分析师。学习如何保护集群、检测攻击并保护您的基础设施。

> 译自 [The Beginner's Guide to Securing Kubernetes](https://www.hunters.security/en/blog/kubernetes-security-guide)，作者 Ophir Kelmen。

本文将介绍保护 Kubernetes 集群安全必不可少的术语和概念。无论您是初学者还是经验丰富的专业人士，本指南都涵盖了理解 Kubernetes 安全维度以及识别和检测特定攻击技术的关键知识。无需事先了解 Kubernetes 即可从本文中获益。

Kubernetes 已成为许多组织基础设施的基石，这些组织希望简化其软件环境并利用云计算的力量。虽然 Kubernetes 提供了显著的优势，但其采用并非没有风险。这些风险包括配置复杂性、管理复杂性和潜在的安全漏洞。随着组织越来越依赖 Kubernetes，了解和缓解这些风险对于保护其基础设施免受中断和安全漏洞至关重要。

Kubernetes 安全对于保护基础设施及其编排的应用程序免受未经授权的访问和漏洞至关重要。Kubernetes 中的安全性是全面的，涵盖了各个层，包括集群配置、网络策略、访问控制和资源限制。增强安全性的关键是实施基于角色的访问控制 (RBAC)，它根据最小权限原则限制用户和进程权限。网络策略对于控制 Pod 之间的流量至关重要，确保仅允许必要的通信，从而最大限度地减少潜在的攻击面。Kubernetes 的另一个重要机制是 [Pod 安全标准](https://kubernetes.io/docs/concepts/security/pod-security-standards/)，它是一组可配置的设置，在 Pod 级别强制执行安全并防止权限提升。

保持强大的安全态势需要定期更新和修补、有效的日志记录和监控以检测异常，以及安全管理 Secrets 和配置。这些做法共同有助于加强 Kubernetes 环境的安全框架。

本文通过介绍潜在的攻击技术和相应的监控策略，为安全专业人员（尤其是 SOC 分析师和检测工程师）提供了有用的检测和调查机会。攻击媒介范围从匿名用户的未经授权访问到更复杂的威胁，例如利用易受攻击的外部应用程序、秘密枚举以及使用敏感的 HostPath 卷从 Pod 逃逸到其节点。检测机会和建议的调查步骤为监控和保护您组织的 Kubernetes 集群提供了坚实的基础。

如果您已经熟悉 Kubernetes 基础知识，可以随意跳到高级检测策略，这些策略可以显著增强您的安全态势。

## 简介

[Kubernetes](https://kubernetes.io/) 是一个开源平台，用于自动化容器化应用程序的部署、扩展和管理，它改变了我们对现代 IT 环境中部署和扩展应用程序的思考方式。随着组织越来越多地采用这种强大的编排工具，了解其基础概念以及保护 Kubernetes 集群安全的复杂性变得至关重要。从理解核心概念到实施安全措施，本指南适合各种受众。加入我们，一起探索 Kubernetes 的复杂性，并赋予您有效保护基础设施的能力。

利用 Kubernetes 的一个简单用例是拥有一个被数百万用户访问的网站的公司。为了确保他们的网站保持快速且在高流量情况下不会崩溃，他们使用多个服务器。Kubernetes 就像一个智能助手，帮助公司有效地管理这些服务器。它可以自动调整资源、修复问题，并在繁忙时段（例如假日促销）扩展服务器，或者在安静时缩减服务器，所有这些都只需最少的人工干预。

相反，如果没有 Kubernetes（忽略其他编排工具），公司将需要手动管理服务器。这将需要 IT 团队不断监控服务器，在需要时手动添加更多服务器，并平衡流量以保持网站正常运行。这种方法速度较慢，更容易出错，并且随着服务器数量的增加，可能会变得非常复杂。

## KUBERNETES 基础知识

事不宜迟，让我们熟悉一下这项技术！

**什么是 Kubernetes？**

[Kubernetes](https://kubernetes.io/docs/concepts/overview/) 是一个开源平台，旨在自动化容器化应用程序的部署、扩展和管理。

最初由 Google 设计，该项目现在由 [Cloud Native Computing Foundation](https://www.cncf.io/) 维护。Kubernetes 的名称源于古希腊语，意为“舵手”或“飞行员”，反映了它在现代软件开发中掌舵的作用。

## 组件

Kubernetes 中有不同的组件，以下是了解检测和调查机会的关键组件：

- **容器镜像** - 运行应用程序所需的所有代码资源和库。
- **容器** - 当容器镜像被容器引擎（例如 Docker）挂载时，在运行时它就变成了一个容器。
  
![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfynlt7t0NifjCHKO7769qp4u9mdXRRaQ15lbwy7fOVkbga9-LHizfkhwKO069_e1a9KmB_FQMo5SKk5Hprs76SkHF3mCIcEQbPf4oVqbVVMYfpWUtJ4udP8LZ8Cjwdl1MsvxDkzGh5mCtpGGb1D3yNWIw?key=2w5PVqIs1gWd_EUlSJM-EQ)

- **Pod** - 容器的包装器（抽象层）。使用户无需担心容器的类型（即与容器类型无关）。使用 Pod 的一个好处是，我们只需要与 Kubernetes 层交互，而不需要与容器层交互。通常，一个 Pod 包含 1 个容器，但并非必须如此。在网络方面，Pod 获取一个内部 IP 地址（而不是容器）。
关于 Pod，我们应该提到的最后一个重要方面是它们是短暂的。这意味着它们被设计为相对短命，易于启动、停止或重启，以适应工作负载的变化或从故障中恢复。
- **节点**：
  - 工作节点：运行一个或多个 Pod 的物理或虚拟机。节点通常被称为工作节点。而控制平面组件（例如 kube-apiserver、etcd、kube-scheduler）通常托管在同一台专用机器上。
  - 控制平面：管理集群中的工作节点和 Pod 的层。它包括重要的集群组件，例如：kube-apiserver、etcd、kube-scheduler。这些组件的集合通常托管在同一台专用机器上。运行这组组件的主机在历史上被称为主节点。
- **集群** - 一组控制平面和工作节点。
- **集群架构** -由于没有比好的可视化更好的东西：

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeKMJtsaCOZc-Cr-k2lLt5F9iXU8d0BzoaQxENDhyjTB_cSF9FddzRIUzpW_eZ0p1_Uv8G2vyKDRZegSCQ5dLyMIo10b0_Nvuu_jrKtZYOhXU3H7teWm5W6Q6IV19J_RItjzjGn96MkAskwrvwy6glVCj0a?key=2w5PVqIs1gWd_EUlSJM-EQ)

每个工作节点需要管理其 Pod 的三个过程：

1. **Kubelet** - 与容器和机器（节点本身）交互。它还负责从节点分配资源到容器。Kubelet 启动包含容器的 Pod，并确保它正在运行且健康。
2. **KubeProxy** - 负责 Kubernetes 集群中的节点通信，以及流量的转发和负载均衡。KubeProxy 智能地转发请求，例如，应用程序请求将被转发到同一节点上的数据库。
3. **容器运行时** - 在系统上执行容器和管理容器镜像的软件，例如 [Docker](https://www.docker.com/resources/what-container/)。


作为对工作节点的补充，控制平面节点必须具有以下 4 个进程：

- **API 服务器** - 充当集群网关和身份验证守门员。它是对集群的请求的唯一入口点（不包括面向外部的应用程序），使其成为审计瓶颈的主要候选者。
- **调度器** - 根据每个节点上的可用资源决定在哪里调度新的 Pod。它将在最不繁忙的节点上调度，但 Kubelet 实际上启动了 Pod。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app.kubernetes.io/name: proxy
spec:
  containers:
  - name: nginx
    image: nginx:stable
    ports:
    - containerPort: 80
      name: http-web-svc
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app.kubernetes.io/name: proxy
  ports:
  - name: name-of-service-port
    protocol: TCP
    port: 80
    targetPort: http-web-svc
```

3. **控制器管理器** - 检测集群状态变化，例如 Pod 崩溃，并请求调度器调度新的 Pod。
4. **etcd** - 可以被描述为“集群大脑”。它是一个分布式键值存储，用于存储有关集群中发生的事情的数据。它存储集群状态信息，而不是应用程序数据。
我们还想熟悉一些 Kubernetes 网络概念：

Kubernetes 配置概念：

**服务** - 一种方法，用于公开在集群中作为一个或多个 Pod 运行的网络应用程序。由于 Pod 是短暂的（即临时且设计为短命），因此服务有助于在通信方面弥合这种差距。我们可以在附带的屏幕截图中看到一个服务公开使用 TCP 端口 80 的特定 Pod 的 nginx 服务器的示例。

**Ingress** - 一个 API 对象，用于管理对集群中服务的外部访问，通常是 HTTP。Ingress 可以提供负载均衡、SSL 终止和基于名称的虚拟主机。在下面的屏幕截图中，我们可以看到一个简单的示例，其中 Ingress 将所有流量发送到一个服务：

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeL7MpCJAQH7Aq-rQyD02Y8cweKVmAPVd81DM8rQDlc_uI191E_CEOX1CPg9o2oSFybAJbqhZn2uUo3cGh5ehM1GzjkCuGBHhdhJopKPwt9N5vPEX80zHnuOEJki9memLJTz2ThvnhqTK3p1tkeRHPd1bLK?key=2w5PVqIs1gWd_EUlSJM-EQ)

**ConfigMap** - 用于以键值对形式存储非机密数据的 API 对象。Pod 可以将 ConfigMap 作为环境变量、命令行参数或卷中的配置文件使用。

**Secret** - 包含少量敏感数据（密码、密钥、证书等）的对象。它以 base64 编码，默认情况下不加密。默认情况下，任何被授权在命名空间中创建 Pod 的人都可以访问和读取命名空间中的任何 Secret。
还有两个重要的概念需要我们理解：

**卷** - 容器中的磁盘文件是短暂的，这对于在容器中运行的非平凡应用程序来说会带来一些问题。从本质上讲，卷是一个目录，可能包含一些数据，容器中的 Pod 可以访问它。卷存储与代码并行且独立（因为 Pod 是短暂的）。卷可以位于节点上或远程主机上。Kubernetes 不管理数据持久性，用户或管理员负责备份和保存数据。

**命名空间** - 命名空间提供了一种机制，用于在一个集群中隔离资源组。命名空间允许不同团队或用户访问和管理资源。



## 安全概念

现在我们了解了 Kubernetes 集群中使用的基本术语和概念。在本章中，我们将详细介绍 Kubernetes 的一些安全概念。本章的主要参考资料是 [Kubernetes 的优秀文档。](https://kubernetes.io/docs/concepts/security/controlling-access/)

控制平面保护

控制平面保护包括五个主要方面：

- 传输安全
- 身份验证
- 授权
- 准入控制
- 审计
了解这一点对于任何处理 Kubernetes 安全的专业人士来说都是至关重要的。

**传输安全**控制平面中的流量使用 TLS 加密。默认情况下，Kubernetes API 服务器在第一个非 localhost 网络接口上的端口 6443 上监听，受 TLS 保护。通常 API 服务器在端口 443 上提供服务。
API 服务器提供证书。此证书可以使用私有证书颁发机构 (CA) 签名，或基于与普遍认可的 CA 链接的公钥基础设施。

集群的私有证书颁发机构（如果存在）应添加到客户端的“~/.kube/config”文件中。


**身份验证**
建立 TLS 连接后，HTTP 请求将进入身份验证步骤。集群创建脚本或集群管理员配置 API 服务器以运行一个或多个身份验证器模块。我们不会在本文中深入探讨身份验证器。
身份验证步骤的输入是整个 HTTP 请求；但是，它通常会检查标头和/或客户端证书。

身份验证模块包括客户端证书、密码、普通令牌、引导令牌和 JSON Web 令牌（用于服务帐户）。

可以指定多个身份验证模块，在这种情况下，每个模块都会按顺序尝试，直到其中一个成功。


**授权**
请求成功通过身份验证后，就会进入授权阶段。Kubernetes 中的请求应封装请求者的用户名、正在请求的特定操作以及受请求操作影响的目标对象。如果存在预定义策略确认用户拥有执行指定操作的必要权限，则授予对请求的授权。
Kubernetes 支持多种授权模块，包括 ABAC（基于属性的访问控制）、RBAC（基于角色的访问控制）和 Webhook（即使用远程 HTTP 服务来提供对请求的响应）。只有在耗尽所有授权模块且没有一个授权的情况下，才会拒绝请求。


**准入控制**
准入控制模块是 Kubernetes 中的软件组件，它们能够修改或拒绝请求。这些模块可以访问比授权模块更多的信息，特别是能够查看正在创建或修改的对象的内容。
准入控制器由旨在创建、修改、删除或连接到（代理）对象的请求触发，但它们不会干预仅读取对象的请求。当启用多个准入控制器时，它们会按顺序调用。

与身份验证和授权检查不同，如果任何准入控制器拒绝请求，则该请求将立即被拒绝，而不会被后续控制器进一步处理。

成功通过所有准入控制器后，请求将根据为所讨论的 API 对象指定的特定例程进行验证。通过验证后，请求最终将持久化到对象存储中。


**审计**

### EDITOR'S RESPONSE
Kubernetes 审计捕获安全相关事件的时间顺序记录，记录集群内操作的顺序。它记录来自用户、与 Kubernetes API 交互的应用程序以及控制平面操作的活动。

**Pod 安全**

Pod 安全策略 (PSP) - 是一种内置的准入控制器，允许集群管理员控制 pod 规范中对安全敏感的方面。PSP 在 Kubernetes v1.21 中已弃用

Pod 安全标准 (PSS) - 可配置设置，在 pod 级别强制执行安全并防止特权升级。PSS 有 3 种模式：

* **特权**- 无限制策略，提供尽可能广泛的权限级别。此策略允许已知的特权升级。
* **基线**- 最小限制策略，可防止已知的特权升级。允许默认（最小指定）的 pod 配置。
* **受限**- 严格限制的策略，遵循当前的 pod 加固最佳实践。

Pod 安全上下文 - SecurityContext 是一个字段，可以在 pod 的设置中使用，它定义了 Kubelet 如何运行 pod（PSS 和 PSP 仅提供限制）。安全设置适用于 pod 中的所有容器。

**RBAC**

基于角色的访问控制 (RBAC) 是一种根据组织中各个用户的角色来规范对计算机或网络资源访问的方法。如上所述，Kubernetes 授权阶段如果配置了 RBAC，可能会使用 RBAC。与集群中的 RBAC 相关的 API 对象是：

- ClusterRole、Role - 声明一组权限
- ClusterRoleBind 和 RoleBind - 将角色中定义的权限授予用户或一组用户。

在下面的示例中，我们可以看到一个在“default”命名空间中具有 pod 读取和创建权限的角色，以及一个将该角色授予名为“bob”的用户的角色绑定：

```
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pods-read-create
  namespace: default
subjects:
- kind: User
  name: bob
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-read-create
  apiGroup: rbac.authorization.k8s.io
```

```
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-read-create
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "watch", "list", "create"]
```

## 攻击向量

有了我们现在对 Kubernetes 及其安全概念的了解，我们可以开始讨论一些针对它的常见攻击向量。为了方便起见，我们按网络杀伤链战术对其进行分类。这绝不是一个详尽的列表，旨在让我们熟悉攻击者的视角。

**初始访问**

- 匿名未经授权的访问 - 当客户端或任何进程在其请求中不提供身份验证参数时，它将自动被视为 [匿名请求](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#anonymous-requests) 用户“system:anonymous”。启用匿名身份验证后，此类请求可能会被允许，具体取决于分配给“system:anonymous”用户或“system:unauthenticated”的权限和角色。在这种情况下，恶意行为者可能会尝试滥用此配置以获取信息，甚至访问集群中的敏感资源。外部扫描程序也可能会发现具有此类配置的集群并将它们添加到其数据库中，使其可供客户使用。 - 易受攻击的外部面向应用程序 - 当攻击者识别出可通过互联网访问的应用程序中的安全弱点（例如，过时的软件、错误配置或缺乏适当的安全控制）时，可能会发生利用 Kubernetes 集群中易受攻击的外部面向应用程序的情况。例如，假设一个在 Kubernetes pod 中运行的 Web 应用程序通过具有外部 IP 地址的服务公开到公共网络。如果此应用程序存在漏洞（例如 SQL 注入漏洞、不安全的反序列化或缓冲区溢出），攻击者可以利用这些漏洞来执行恶意命令或脚本。由于该应用程序是 Kubernetes 集群的一部分，因此成功利用可能会为攻击者提供立足点，从该立足点他们可以尝试提升特权或探索网络以查找敏感数据、操纵容器配置，甚至破坏整个集群的服务。

**执行**

- 创建到 Kubernetes Pod 的反向 Shell - 创建到 Kubernetes pod 的反向 Shell 使创建者能够在该 pod 中远程执行命令。恶意行为者通常会创建到 Kubernetes pod 的反向 Shell 作为获取凭据、访问敏感数据或在集群中横向移动的步骤。
- Kubernetes 在 kube-system 命名空间中的命令执行 - 一旦威胁行为者在集群中立足，他们可能想要执行命令。在 kube-system 命名空间中的 Pod 上执行命令对威胁行为者特别有吸引力，因为此命名空间用于系统级组件，并包含关键的访问权限和信息。
**凭据访问**
- 密钥枚举 - 恶意行为者用来访问敏感信息的常见攻击媒介。Kubernetes 密钥是存储敏感数据的对象，例如密码、令牌和密钥，这些对于管理安全且功能正常的集群至关重要。攻击者利用松懈的安全实践（例如，不足的访问控制或配置错误）来枚举这些密钥。通过获得对 Kubernetes API 的未经授权的访问权限，或通过利用授予过度宽松角色的权限，攻击者可以列出、查看并可能泄露密钥。
- 使用敏感 HostPath 卷进行 Pod 逃逸 - HostPath 卷类型将节点上的敏感文件或文件夹挂载到容器。如果容器被入侵，攻击者可以使用此挂载来访问节点。具有对主机文件系统不受限制的访问权限的容器可以通过多种方式提升权限，包括从其他容器读取数据和访问权限更高的 Pod 的令牌。
**持久性**
- 创建 NodePort 服务 - 威胁行为者可以创建 Kubernetes NodePort 服务，该服务将选定的应用程序暴露在集群外部（即，将应用程序运行所在的节点暴露在特定端口范围内）。通过这样做，恶意行为者从集群外部建立到内部节点的通信通道。此通信通道可用于在集群中保持行为者的持久性。
## 检测机会和调查步骤
*编辑注：*恭喜你进入最有趣的章节！*

本章讨论了我们发现的可能检测逻辑，这些逻辑平衡了信噪比。我们还描述了针对每个由逻辑生成的警报的推荐调查步骤，以对警报的恶意程度进行分类。

任何检测的基础都是它运行的日志。一个非常有吸引力的日志瓶颈是 [API 审计日志](https://kubernetes.io/docs/reference/config-api/apiserver-audit.v1/)。它包含集群中 API 审计日志中可以包含的所有信息（包括动词 get、list、create、update、delete、patch 和 post）。API 审计日志的另一个优点是它由 Amazon、Google 和 Microsoft 托管的 Kubernetes 服务提供 ([EKS](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html#:~:text=the%20Kubernetes%20documentation.-,Audit%20(audit),-Kubernetes%20audit%20logs), [GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/audit-logging#audited_operations) 和 [AKS](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/aksaudit) 分别提供）。

让我们继续讨论检测和调查机会本身：


**机会 1：****Kubernetes 用户可疑的模拟尝试**检测 Kubernetes 环境中用户可疑的模拟尝试。模拟是一个 API 调用，允许用户使用另一个用户的权限和名义执行操作。在 Kubernetes 环境中，此功能的正常使用仅限于执行特定操作的特定服务帐户。偏离正常行为的模拟尝试可能表明威胁行为者滥用模拟权限进行权限提升或隐藏恶意活动。
**建议：**
- 调查发起用户、其角色和过去的操作。
- 通过查看同一检测器生成的后续警报来调查模拟用户的操作。
- 调查源 IP 地址以查找任何已知的恶意来源。
- 调查模拟的目标，并了解获得了哪些权限或是否被滥用。
**机会 2：****使用高度特权的内置角色创建或修改 RoleBinding**
检测创建或修改 RoleBinding 或 ClusterRoleBinding 到过度宽松的内置角色（例如 admin、cluster-admin），这可能表明权限提升方法。威胁行为者可以使用此操作来获得高度特权的权限，这些权限允许他们在集群中执行特权操作（读取密钥、创建 Pod 等）。
## Kubernetes 安全检测

如前一章所述，Kubernetes 使用基于角色的访问控制 (RBAC)，它定义了一种机制，通过角色将权限分配给用户/服务/组。权限在名为 Role（针对一个命名空间）/ClusterRole（针对多个命名空间）的对象中描述。为了将这些角色（权限）绑定到用户/服务/组，我们需要创建另一个名为 RoleBinding / ClusterRoleBinding 的对象，并定义要绑定的角色以及要绑定角色的用户/服务帐户。

**建议：**

- 检查创建角色/集群绑定的 Kubernetes 用户的活动：检查该用户是否与其关联了来自无关地理位置/多个用户代理的多个 IP（表明存在入侵）。检查该用户是否在过去创建了任何 RoleBind，或者是否是第一次。
- 检查发起 IP 在请求之前和之后执行了哪些其他 Kubernetes API 请求 - 检查该 IP 是否与多个用户关联。
- 使用 PulseDive、IPInfo、AbuseIPdb 等检查发起 IP 地址的信誉和活动。
- 检查与 Role/ClusterRoleBinding 相关的详细信息 - 检查通过 ClusterRoleBind/RoleBind 分配的角色及其允许的操作，检查此 RoleBind 在哪个集群/命名空间中创建以及该区域下的服务。检查获得此角色/ClusterRole 的用户是谁，何时创建以及是否应该获得此权限。

**机会 3：拒绝 Kubernetes 服务帐户的请求**

检测来自 Kubernetes 环境中 [服务帐户](https://kubernetes.io/docs/concepts/security/service-accounts/) 的以前未见过的被拒绝的 API 请求。Kubernetes 服务帐户遵循预先编程的预期行为，因此来自 Kubernetes 服务帐户的被拒绝请求可疑，可能表明其行为偏离正常，并可能存在入侵。

**建议：**

- 调查服务帐户的最近活动，以识别其通常访问的资源和命名空间，并与请求的 URL 进行比较。
- 调查请求的 URL 并确定与访问该 URL 相关的风险。调查源 IP 及其最近的活动以识别入侵。
- 调查源用户代理以识别任何偏离正常行为或可能表明恶意活动的任何用户代理（curl、kubectl 等）。

**创建具有敏感 hostPath 卷的 Pod**

检测创建具有 [hostPath](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath) 类型敏感卷的 Pod。hostPath 卷类型将节点上的敏感文件或文件夹挂载到容器。如果容器被入侵，攻击者可以使用此挂载来访问节点。容器对主机文件系统具有不受限制的访问权限，可以通过多种方式提升权限，包括读取其他容器中的数据和访问权限更高的 Pod 的令牌。

**建议：**

- 检查此 Kubernetes 用户在集群中的活动：检查与其关联的来自无关地理位置的多个 IP，并检查此用户是否与其关联了多个用户代理。
- 使用 PulseDive、IPInfo、AbuseIPdb 等检查发起 IP 地址的信誉和活动。

**在 kube-system 命名空间中执行 Kubernetes 命令**

检测在 Kubernetes 环境的 kube-system 命名空间中执行命令。威胁行为者试图在该命名空间中的 Pod 上执行命令，因为它用于系统级组件，包含关键访问权限和信息。

**建议：**

- 查看用户和 IP 的过去操作。
- 特别查找来自此用户的先前 EXEC API 调用。
- 调查命令、其目的及其对目标 Pod 的影响。

**创建到 Kubernetes Pod 的反向 Shell**

检测创建到 Kubernetes Pod 的反向 Shell。反向 Shell 使创建者能够在该 Pod 中远程执行命令。恶意行为者通常会创建到 Kubernetes Pod 的反向 Shell，作为获取凭据、访问敏感数据或在集群中横向移动的步骤。

**建议：**

- 检查此 Kubernetes 用户在集群中的活动：检查与其关联的来自无关地理位置的多个 IP，并检查此用户是否与其关联了多个用户代理。
- 使用 PulseDive、IPInfo、AbuseIPdb 等检查发起 IP 地址的信誉和活动。

**Kubernetes 密钥枚举**

检测通过 Get、List 或 Watch API 调用枚举密钥。访问密钥的威胁行为者可能能够启用横向移动或权限提升以及对关键资源的未经授权的访问。可以使用静态阈值（例如，1 分钟内超过 10 个 API 调用）或使用更复杂的机制（使用时间序列分析或其他异常检测算法）来实现此检测。

**建议：**
- 检查发起用户的最近活动、源 Pod 和用户代理，以确定此行为是自动的还是手动键盘事件。
- 检查一个或多个请求是否成功。如果有，调查与该密钥相关的服务帐户、Pod 或用户是否在之后不久发起了异常请求。

创建或修改面向外部的 Kubernetes NodePort 服务
Kubernetes NodePort 服务将选定的应用程序暴露在集群外部（即，将应用程序运行所在的节点暴露在特定端口范围内）。因此，创建或修改面向外部的 Kubernetes NodePort 服务是恶意攻击者在集群中建立持久性的可能方式。

**建议：**
- 检查此 Kubernetes 用户在集群中的活动：检查与其相关的来自无关地理位置的多个 IP，并检查此用户是否与其关联了多个用户代理。
- 查找服务暴露的应用程序的镜像名称，并检查它是否可疑。
- 使用 PulseDive、IPInfo、AbuseIPdb 等检查发起 IP 地址的信誉和活动。

未经身份验证的用户授权 Kubernetes API 请求

检测由未经身份验证的用户发起的 Kubernetes API 请求的授权。此类事件通常应限制为 Kubernetes 的特定内部使用（例如，livez、healthz、readyz）。未经身份验证的用户（即 system:anonymous）对不同用途的允许请求可能表明恶意活动滥用权限配置错误。

**建议检查：**
- 为 system:anonymous 用户创建允许请求的 RoleBinding 的人。
- 用户代理是否可疑或异常。
- 发起 IP 在请求之前和之后执行了哪些其他 Kubernetes API 请求。

一般调查步骤

- 发现请求：搜索由发起用户名执行的发现请求，例如，当用户使用 kubectl 命令时：“kubectl auth can-i --list”，API 请求将发送到 API 服务器以获取 URI“/apis/authorization.k8s.io/v1/selfsubjectrulesreviews”或“/apis/authorization.k8s.io/v1/selfsubjectaccessreviews”。
- IP 信誉：值得检查外部 IP 地址的信誉。来自意外地理区域的 IP 更可疑。
- 分析用户活动：检查用户使用的用户代理和 IP。多个或不寻常的用户代理会增加怀疑。

## 摘要
“Kubernetes 安全入门指南”是关于保护 Kubernetes 集群的全面介绍，专为初学者和经验丰富的用户设计。它涵盖了 Kubernetes 的基本概念和组件、与配置和管理相关的挑战以及与使用相关的潜在安全风险。

**文章中涵盖的关键点包括：**
- Kubernetes 的基础概念：文章首先解释了 Kubernetes 的基础知识 - 一个由云原生计算基金会维护的开源平台，用于自动化容器化应用程序的部署、扩展和管理。
- Kubernetes 的组件：讨论包括基本的 Kubernetes 组件，如容器、Pod、节点和集群。它还解释了 Kubernetes 特定的网络概念，如服务和 Ingress，以及配置对象，如 ConfigMaps 和 Secrets。
- 控制平面保护：强调使用 TLS 加密和 Kubernetes API 服务器保护等方法保护控制平面的重要性。
- Pod 安全：介绍 Pod 安全策略 (PSP) 和 Pod 安全标准 (PSS) 等概念，涉及在 Pod 级别应用的安全上下文。
- RBAC（基于角色的访问控制）：一个关键组件，被描述为一种根据角色来规范 Kubernetes 内访问权限的方式。
- 审计的作用：捕获集群中与安全相关的事件的记录，以便跟踪在 Kubernetes 中执行的操作。
- Kubernetes 中的安全方面：
- 攻击向量：文章将攻击向量分类为初始访问、执行和持久性等阶段，并提供了一些示例，例如未经授权的访问、利用漏洞和密钥枚举。
- 检测和调查机会：对于安全专业人员，尤其是 SOC 分析师和检测工程师来说至关重要。本节讨论了使用日志来检测可疑活动，例如未经授权的角色绑定或敏感命名空间中的命令执行。
- 审计的作用：捕获集群中与安全相关的事件的记录，以便跟踪在 Kubernetes 中执行的操作。
总的来说，本指南充当教育资源，不仅使用户熟悉 Kubernetes，还为他们提供必要的工具和知识，以有效地保护 Kubernetes 环境。