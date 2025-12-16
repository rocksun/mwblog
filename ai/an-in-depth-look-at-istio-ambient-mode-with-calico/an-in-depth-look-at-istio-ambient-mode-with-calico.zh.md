## 迈向统一 Kubernetes 平台的下一步：Istio 环境模式

随着 Kubernetes 成为现代应用平台的基础，组织正面临日益增长的运维复杂性、碎片化的工具以及不一致的安全强制执行问题。这种复杂性和碎片化导致平台团队在网络、网络安全和可观测性方面需要整合各种独立的解决方案，从而承受越来越大的负担。这种碎片化还导致运营成本上升、安全漏洞、故障排除效率低下，并增加了关键任务环境中发生中断的风险。对于运行多个 Kubernetes 发行版的公司来说，挑战甚至更大，因为依赖每个平台独特且通常不兼容的网络堆栈可能会导致严重的供应商锁定和运营开销。

### Tigera 的统一战略：解决碎片化问题

Tigera 的统一平台战略旨在解决这些挑战，通过提供一个单一解决方案，汇集企业所需的所有基本 Kubernetes 网络和安全功能，其中包括 Istio 环境模式，并在每个 Kubernetes 发行版中提供一致的服务。

![]()![](https://www.tigera.io/app/uploads/2025/12/Solution-Architecture-Dec-2025-white.webp)

Istio 环境模式将无 sidecar 的服务网格功能（包括身份验证、授权、加密、L4/L7 流量控制和深度应用层 (L7) 可观测性）直接引入统一的 Calico 平台。通过将 Istio 环境模式与 Calico 集成，并使其易于通过 Tigera Operator 安装和管理，同时提供企业支持，Tigera 为客户提供了一种更简单、更可扩展、更安全的方式，以在他们的 Kubernetes 环境中实现安全网络。结果是减轻了运营压力、降低了成本，并为所有集群的网络、网络安全和可观测性提供了一个单一且一致的平台。

为了帮助平台团队理解这种无 sidecar 架构的全部潜力，我们将深入探讨以下关键功能和差异：

## 什么是服务网格

服务网格是一种基础设施层，它透明地处理分布式应用程序中众多服务之间的通信，而无需修改每个服务的代码。

具体来说，服务网格提供：

*   **流量控制**：路由、负载均衡、重试、故障转移、流量转移（例如金丝雀部署）、故障注入等。
*   **安全性**：服务到服务通信的身份验证、加密和授权。
*   **可观测性**：遥测、分布式追踪、指标和流量日志记录。

服务网格将网络相关的复杂性（连接、安全、流量规则、监控）与应用程序逻辑解耦，使工程团队能够更可靠、更安全地构建、扩展和管理应用程序服务。

## 什么是 Istio 环境模式？

Istio 环境模式的核心是一个轻量级、无 sidecar 的服务网格。它建立在两个共享数据平面组件之上：

*   **zTunnel 代理 (L4)**：一个节点（L4）级别的零信任隧道，负责所有服务到服务流量的身份、身份验证和双向 TLS (mTLS) 加密。每个 Kubernetes 节点运行一个 zTunnel 实例，而不是在每个 Pod 内部运行一个代理。
*   **Waypoint 代理 (L7)**：一个可选的、命名空间范围的 L7 代理，提供细粒度的流量路由、重试、整形、故障转移和 L7 级别的授权。

这些组件共同提供 mTLS（加密和身份验证）、工作负载身份、L4/L7 流量控制和深度可观测性，同时消除了每个 Pod sidecar 的操作负担。

![Istio 环境模式展示了它如何使用 ztunnel (L4) 和 Waypoint (L7) 代理来控制流量。每个节点有一个 ztunnel 代理，每个命名空间建议至少有一个 Waypoint 代理。将其与每个 Pod 部署一个 sidecar 代理的常规服务网格进行比较。]()![Istio Ambient Mode showing the use of how it uses ztunnel (L4) and Waypoint (L7) proxies to control traffic. There is one ztunnel proxy per node, and a recommended minimum of one Waypoint proxy per namespace. Compare this to a regular service mesh that deploys one side car proxy per pod.](https://www.tigera.io/app/uploads/2025/11/What-is-Calicos-Istio-Ambient-Mode-Integration.png)

Istio 环境模式展示了它如何使用 ztunnel (L4) 和 Waypoint (L7) 代理来控制流量。每个节点有一个 ztunnel 代理，每个命名空间建议至少有一个 Waypoint 代理。将其与每个 Pod 部署一个 sidecar 代理的常规服务网格进行比较。

## 为什么选择 Istio 环境模式？解决 Sidecar 问题

传统的 Istio 服务网格依赖于每个 Pod 一个 sidecar 代理，这种方法增加了显著的计算成本，使开发和构建管道复杂化，并在集群扩展时造成持续的运营负担。Istio 环境模式通过完全消除 sidecar 并用轻量级的每个节点（zTunnel）和每个命名空间（Waypoint）代理来替代它们，从而解决了这个问题。

| |
| --- |
| 💥复杂性：服务网格采用的首要障碍 许多评估服务网格的组织很快发现其操作复杂性过高： * 一家电子商务公司放弃了服务网格实施，因为它维护起来过于复杂。 * 另一家主要云提供商指出，终端用户界面的复杂性以及由此产生的昂贵故障排除开销是一个巨大的问题。 Calico 的 Istio 环境模式通过消除数千个 sidecar 并简化管理体验来解决这个问题。 |

## Istio 环境模式详解

本节解释了环境模式的内部工作原理，并概述了它与 Calico 的配合方式。

### 默认随处可见的 mTLS

Calico 的 Istio 环境模式最强大的功能之一是它如何提供双向 TLS (mTLS)，其中包括所有服务通信的双向身份验证和加密，而无需更改您的应用程序代码。让我们详细了解其工作原理、重要性，以及 Istio 环境模式与 Calico 的捆绑如何同时保持安全性和策略兼容性。

#### 为什么 mTLS 很重要

在 Kubernetes 中，大量的流量在 Pod、节点和集群之间传输，并且默认情况下是未加密的。这使得环境容易受到中间人攻击、欺骗和窃听等威胁。Istio 环境模式通过 mTLS 提供强大的双向身份验证和服务到服务加密来解决这些风险，同时使用 Istio 的网络策略强制执行授权。

通过使用 mTLS，连接双方相互验证（因此称为“双向”），然后加密流量，从而保证机密性和完整性。

#### mTLS 在环境模式网格中的工作原理

当 Istio 环境模式网格中的工作负载（Pod、节点或服务）发出请求时，会发生以下情况：

1.  **证书配置**：每个工作负载（zTunnel 代理）都拥有由受信任的证书颁发机构 (CA) 颁发的证书 (X.509)。在 Istio 的环境模式网格中，控制平面会自动颁发和轮换这些证书。
2.  **mTLS 握手开始**：客户端与服务器启动 TLS 握手。
3.  **密码协商**：协商密码参数（密码套件、密钥）。
4.  **服务器身份验证**：服务器出示其证书，客户端验证它。
5.  **客户端身份验证 (mTLS)**：在 mTLS 模式下，客户端还会出示其证书，服务器会验证它。
6.  **会话建立**：一旦双方都通过验证，它们就会派生一个共享会话密钥。
7.  **安全通信**：工作负载之间的流量以端到端加密和身份验证的方式进行。

握手完成后，客户端和服务器之间的所有后续流量都将加密，并且不能被有意义地拦截或篡改。两端的身份都通过密码绑定到其证书，而不仅仅是 IP 地址。

这也意味着身份不依赖于临时 IP 或网络位置。如果 Pod 移动、重新缩放或更改到不同的节点，证书作为身份会保留下来。

![Istio 环境模式 mTLS 流量流示例：Istio 环境模式使用 mTLS 加密流量。所有 Pod 流量都被节点的 ztunnel 捕获，ztunnel 自动在源和目标 ztunnel 之间应用 mTLS。接收 ztunnel 解密流量并将其转发到目标 Pod，即使两个 Pod 在同一节点上也会应用 mTLS。mTLS 可用于 L4 和 L7（使用 waypoint 代理）流量，如图所示。]()![Istio Ambient Mode mTLS traffic flow example: Istio Ambient Mode encrypts traffic using mTLS. All pod traffic is captured by the node’s ztunnel, and the ztunnel automatically applies mTLS between source and destination ztunnels. The receiving ztunnel decrypts the traffic and forwards it to the destination pod, and mTLS is applied even if both pods are on the same node. mTLS can be used for both L4 and L7 (using the waypoint proxy) traffic as shown.](https://www.tigera.io/app/uploads/2025/11/Built-In-L7-encryption-with-mTLS-Everywhere.png)

Istio 环境模式 mTLS 流量流示例：Istio 环境模式使用 mTLS 加密流量。所有 Pod 流量都被节点的 ztunnel 捕获，ztunnel 自动在源和目标 ztunnel 之间应用 mTLS。接收 ztunnel 解密流量并将其转发到目标 Pod，即使两个 Pod 在同一节点上也会应用 mTLS。mTLS 可用于 L4 和 L7（使用 waypoint 代理）流量，如图所示。

### Calico + Istio 环境模式如何利用 mTLS

随着 Istio 环境模式集成到 Calico 平台：

🔒 **每个节点都运行增强的 L4 zTunnel**
每个（属于网格的）节点都运行一个轻量级的 zTunnel（第 4 层），负责处理加密、身份、双向身份验证和策略强制执行。这种每节点部署与传统的 sidecar 相比，大大降低了开销。

🛡️ **所有流量的自动 mTLS 加密和身份验证**
当工作负载（Pod、节点或服务）发送流量时，zTunnel 代理会拦截它，附加证书身份，协商 mTLS 会话（如果需要），然后转发加密流量，无论是节点内、节点间还是跨集群流量。

🔑 **保持策略兼容性**
因为 Calico 增强的 zTunnel 知道原始目标端口（而不是强制所有流量通过，例如端口 15008），所以现有的 Calico/Kubernetes 网络策略可以继续保持不变地运行。无需重写/调整任何 Calico 策略以与环境模式网格配合使用。

因此，您可以在所有服务到服务通信（甚至是节点内流量）中获得端到端 mTLS，而无需重新设计任何现有的 Calico 或 Istio 环境模式策略。

### Istio 和 Calico 策略的无缝协同使用

Istio 环境模式面临的最大挑战之一是所有流量都通过端口 15008 上的隧道进行路由，这导致上游 Kubernetes 和 Calico 网络策略无法看到原始目标端口。如果不进行修改，安全团队将被迫重写他们的 Kubernetes 和 Calico 策略，并引入复杂的例外来使其正常工作。

Calico 通过修改 zTunnel 代理来解决这个问题，该代理会保留（记住）原始目标端口，从而使现有的 L3/L4 Kubernetes 和 Calico 网络策略能够像今天一样继续正常运行，绝对无需重写。

这意味着：

*   无需在任何网络策略中显式允许端口 15008
*   不会损失强制执行的准确性
*   无需更改现有策略定义

![从图中可以看出，ztunnel 已被修改以匹配目标端口 8080。这使得现有的 Kubernetes 和 Calico 策略即使在 mTLS 加密的情况下也能匹配流量。]()![As you can see from the diagram, ztunnel has been modified to match the destination port 8080. This allows existing Kubernetes and Calico policies to match the traffic even though it is mTLS encrypted.](https://www.tigera.io/app/uploads/2025/11/Fully-Compatible-with-Calico-and-Kubernetes-Network-Policies.png)

从图中可以看出，ztunnel 已被修改以匹配目标端口 8080。这使得现有的 Kubernetes 和 Calico 策略即使在 mTLS 加密的情况下也能匹配流量。

这种“两全其美”的方法使组织能够采用环境模式服务网格，而无需重写网络策略或为 Kubernetes 网络和环境模式网格网络维护独立的模型。

## 使用 Istio 环境模式进行流量控制

环境模式架构的下一层强大之处在于它能够为 Kubernetes 工作负载带来复杂、成熟的应用层 (L7) 流量控制，同时绕过 sidecar 的运营负担。平台团队获得了定义高级规则所需的工具，以管理流量流、确保应用程序稳定性、安全管理部署并强制执行高级安全策略。为了以最小的开销提供这种 L7 功能，环境模式引入了一个独特的数据平面组件：Waypoint 代理。

### Istio 的 Waypoint 代理：实现 L7 控制

尽管 L4 zTunnel 处理基础安全性 (mTLS) 并确保与 Calico 的策略兼容性，但环境模式架构的下一层强大之处在于它能够为 Kubernetes 工作负载带来复杂的应用层 (L7) 流量控制，而无需依赖 sidecar 或侵入式应用程序更改。

环境模式 L7 流量控制功能的核心是 Waypoint 代理，它是一个共享的 L7 数据平面组件，在命名空间级别运行（通常每个命名空间一个 Waypoint 代理），而不是每个 Pod 运行一个代理。当命名空间配置为 Istio 环境模式并为该命名空间启用 L7 功能时，流向该命名空间中工作负载的流量会流经 Waypoint。这就是 Istio 应用其强大的 L7 流量控制逻辑套件的地方，它很像一个网关，但专门为网格内部的服务间通信量身定制。

### 路由和流量整形

环境模式支持所有使 Istio 在生产环境中广受欢迎的标志性路由功能。通过 Waypoint，团队可以定义 VirtualService 和 DestinationRule 配置，以控制流量如何在服务之间移动。这些规则允许网格执行以下操作：

*   在金丝雀发布时，在服务版本之间**逐渐转移流量**
*   通过将某些用户或请求头定向到特定的服务版本来**执行 A/B 测试**
*   通过精确控制切换时间来**实现蓝/绿部署**
*   在发送生产负载之前**拆分或镜像流量**以验证新服务

Waypoint 根据路径、方法、头、元数据或用户身份等属性评估路由规则，使团队能够在不触及应用程序代码的情况下实现应用程序感知控制。

### 弹性与可靠性特性

环境模式中的流量控制还包括 Istio 的弹性工具，这些工具有助于稳定 Kubernetes 环境并减少故障的影响。通过熟悉的 Istio 策略对象，团队可以配置：

*   瞬时错误的重试
*   超时以防止缓慢的下游服务级联成故障
*   保护服务免受过载的断路器
*   自动弹出不健康端点的异常检测
*   根据延迟、最少连接或随机选择来转移流量的负载均衡策略

这些策略使应用程序更加可靠，尤其是在流量高峰、部署或部分中断期间。

### 安全的生产部署控制

由于 L7 流量在到达工作负载之前总是通过 Waypoint 代理，团队可以收集详细的遥测数据并在提交路由更改之前进行测试。例如，网格可以：

*   将流量影子到新的服务版本进行验证
*   仅将一小部分流量发送到新版本，并根据错误率自动回滚
*   使用基于百分比的路由逐渐增加到新版本的流量

这使得平台团队和 SRE 能够自信地推出更改，利用生产负载下的真实用户行为，同时最大限度地降低风险。

### 身份感知授权

环境模式中的流量控制不限于路由和弹性功能，它还有助于身份和授权。因为 Waypoint 可以访问工作负载的身份（通过 zTunnel 的证书）和 L7 请求数据，所以它可以强制执行 AuthorizationPolicy 规则。这意味着您可以根据以下条件允许或拒绝流量：

*   工作负载身份
*   请求路径或方法
*   用户或服务身份
*   JWT (JSON Web token) 或经过身份验证的会话元数据
*   自定义属性或请求头

这在应用程序 (L7) 层增加了强大的授权功能：除了使用 mTLS 对工作负载进行身份验证之外，Istio 还允许您根据详细标准（例如请求路径、HTTP 方法、工作负载身份、HTTP 和应用程序头等）授权请求。

总而言之，Istio 环境模式中的流量控制为团队提供了 Istio 成熟的 L7 流量控制功能的所有强大能力：路由、弹性、授权和流量整形，而无需 sidecar 代理的复杂性。

## 应用 (L7) 可观测性

使用 Istio 环境模式的优势之一是它极大地提高了应用层 (L7) 行为的可观测性。Calico 已经提供了对 L3/L4 网络流的出色可见性。有时很难理解服务在应用层为何以这种方式运行：哪些请求失败了，走了哪些路由，重试如何影响延迟等等。

环境模式通过引入 L7 流量的 Waypoint 代理来显著改变这一点，该代理可以一致地捕获、丰富和导出环境模式网格中的 L7 遥测数据。这些 Waypoint 代理生成基于 OpenTelemetry 的 L7 指标、追踪和日志。Istio 使用 OpenTelemetry 作为其标准可观测性框架，这意味着结构化遥测数据可以显示从请求路径到响应代码再到端到端延迟的所有内容。

借助 Istio 的应用程序 (L7) 可观测性功能，您可以确定：

*   **基于身份的服务通信**：查看哪些服务正在通信，基于工作负载身份和请求路径，而不仅仅是 IP 地址。
*   **mTLS 加密状态**：流量是否加密，因为环境模式生成元数据，显示每个跳点何时应用了 mTLS。
*   **性能瓶颈位置**：瓶颈在哪里形成，使用延迟直方图、请求时间以及上游/下游服务关联。
*   **L4/L7 策略违反可见性**：哪些 L7 流程违反了策略，包括授权拒绝或 Calico L4 规则与 Istio L7 规则之间的不匹配。
*   **实时流量规则行为**：路由规则在真实流量中如何表现，包括金丝雀部署、加权路由、重试、超时、故障转移等。

在 Istio 环境模式中，这些 L7 数据流经网格的遥测管道，并通过标准 OpenTelemetry 收集器导出。这为平台团队提供了所有服务中应用程序行为的统一、一致视图，从而更容易排除问题、验证策略并了解真实流量如何在他们的系统中移动。此 L7 数据可以与 Calico 的详细 L3/L4 日志数据组合成一个统一视图，以实现快速轻松的故障排除。

## 统一的、Operator 管理的架构

Calico 使用 Tigera Operator 来安装和管理 Istio 环境模式，创建了一种统一且自动化的方式来大规模运行服务网格。Operator 处理所有环境模式组件的安装、配置、升级和修补，包括企业强化镜像和 CVE 修复。

将工作负载添加到网格变得像应用命名空间标签一样简单：

`kubectl label namespace default istio.io/istio-data plane=ambient`

无需修改部署清单、更新 sidecar 注入 webhook，或协调网格配置与应用程序管道。团队获得了服务网格功能，几乎没有任何传统的维护开销。

## 如何开始使用 Istio 环境模式

在 Calico 中开始使用 Istio 环境模式非常简单。Tigera 已将环境模式直接集成到 Tigera Operator 中，因此您只需几条命令即可启用网格、加载命名空间并开始应用 mTLS、流量控制和 L7 可观测性。

### 1. 使用 Tigera Operator 启用 Istio 环境模式

Istio 环境模式通过 Tigera Operator 进行安装和管理，该 Operator 自动化了部署、配置、升级和生命周期管理。一旦安装了 Calico，启用环境模式就像应用 Istio 自定义资源一样简单，它会安装所有必需的 Istio 环境模式组件，包括企业强化的 zTunnel 和 Waypoint 代理。

### 2. 将工作负载添加到环境网格

安装后，您只需通过标记其命名空间即可将工作负载添加到网格中：

`kubectl label namespace istio.io/istio-data plane=ambient`

这会自动为该命名空间中的所有工作负载应用 mTLS、身份和策略强制执行，无需 sidecar 或应用程序更改。

### 3. mTLS 身份验证和加密

在 Istio 中启用 mTLS 非常简单。一旦安装了 Istio 环境模式网格，您只需应用一个 [PeerAuthentication 策略](https://istio.io/latest/docs/reference/config/security/peer_authentication/)，告诉 Istio 要求所有服务到服务通信都使用双向 TLS。对于集群范围的强制执行，为 istio-system 命名空间创建一个策略：

有了这个设置，工作负载在连接建立期间会自动交换和验证证书，并且所有流量都会透明地加密。无需应用程序更改，Istio 会在幕后处理证书颁发、轮换和 mTLS 协商。

### 4. 无缝结合 Calico 和 Istio 网络策略

由于 Tigera 增强的 zTunnel 保留了原始目标端口，您现有的 Calico 和 Kubernetes 网络策略将继续与 Istio 策略按原样工作，无需任何重写或例外。您可以将 Istio AuthorizationPolicies 与 Calico GlobalNetworkPolicies 一起引入，以实现分层、深度防御的强制执行。

## 更简单、更安全、更可扩展的平台

Istio 环境模式为团队提供了一种简单高效的方式来保护 Kubernetes 中的服务到服务通信。通过移除 sidecar，它消除了管理数千个 Pod 代理所带来的资源开销、版本漂移和操作复杂性。相反，团队获得了一个轻量级、可扩展的解决方案，提供身份验证、授权、加密、高级流量整形和详细的 (L7) 可观测性，而无需更改应用程序代码或部署管道。

将 Istio 环境模式作为统一 Calico 平台的一部分，将这些服务网格功能整合到一个一致、易于管理的体验中。平台团队无需将不同的网络、网络安全、授权、身份验证、加密、流量控制和可观测性工具拼凑起来，而是获得了一个完全集成的平台，可在每个工作负载、集群和 Kubernetes 发行版中运行。

**准备好简化并保护您的服务网格了吗？** [立即申请个性化演示](https://www.tigera.io/demo/?utm_source=website&utm_medium=blog&utm_campaign=Dec_2025)，亲身体验 Calico 平台与 Istio 环境模式的实际应用，并发现通往无 sidecar 简单之路。