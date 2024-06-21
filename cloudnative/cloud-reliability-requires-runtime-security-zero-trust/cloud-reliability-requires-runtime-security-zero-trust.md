
<!--
title: 云可靠性需要运行时安全和零信任
cover: https://cdn.thenewstack.io/media/2024/06/ce8a1da2-cloud-reliability-requires-runtime-security-zero-trust1.jpg
-->

在当今环境中，运行时安全至关重要，它通过实时检查来实现安全，而不是将其视为一次性流程。

> 译自 [Cloud Reliability Requires Runtime Security, Zero Trust](https://thenewstack.io/cloud-reliability-requires-runtime-security-zero-trust/)，作者 Manas Chowdhury。


# 云可靠性需要运行时安全和零信任

![云可靠性需要运行时安全和零信任的特色图片](https://cdn.thenewstack.io/media/2024/06/ce8a1da2-cloud-reliability-requires-runtime-security-zero-trust1-1024x576.jpg)

2024 年 2 月，[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 发布了 [安全公告](https://access.redhat.com/errata/RHSA-2024:0717)，提醒用户注意 runC 中的漏洞。runC 是一个核心容器基础设施组件，用作 [Docker](https://www.docker.com/?utm_content=inline+mention) 的 containerd 和其他运行时的容器运行时引擎。

简而言之，runC 无法将容器与主机操作系统 (OS) 目录正确隔离。结果？攻击者可以利用此漏洞通过具有易受攻击的 runC 版本的容器渗透主机系统。

![](https://cdn.thenewstack.io/media/2024/06/d054a4a7-vulnerability-locations.png)

## 在当今的威胁环境中，仅仅保护代码是不够的

runC 中的漏洞证明了 [运行时安全的重要性](https://thenewstack.io/container-security-and-the-importance-of-secure-runtimes/)，特别是在云工作负载中。在云出现之前，如果您的代码在构建和部署期间是安全的，您就可以安然入睡。

但随着云计算和微服务的兴起，整个 IT 工作负载中移动部件的数量大幅增加。容器、[Kubernetes](https://roadmap.sh/kubernetes) (K8s) 集群、云平台——任何东西都可能包含漏洞。[运行时安全](https://www.accuknox.com/products/runtime-security)——对您的工作负载和平台进行持续监控——是必要的。

保护您的代码库只是拼图的一部分。应采用云原生安全方法来缓解基础层中的漏洞或错误配置。这有助于您从层面上看待安全。

但是，运行时安全存在一些挑战：

- 云原生环境发展太快。
- 微服务增加了复杂性。
- 短暂的虚拟基础设施使监控成为噩梦。
- 与现代技术结合使用的旧技术的漏洞使问题更加复杂。

无论运行时安全多么有用和相关，使其发挥作用本身都是一项艰巨的任务。这就是 [云工作负载保护平台 (CWPP)](https://www.accuknox.com/products/cwpp) 工具将运行时安全提升到一个新水平的原因：

- 自动化。
- 持续监控。
- 保持活动资产的清单。
- 标准化安全检查。
- 将安全与运营集成（[DevSecOps](https://thenewstack.io/what-is-devsecops/)）。
- 实施严格的[零信任](https://thenewstack.io/what-is-zero-trust-security/)。

我会详细介绍这些内容。但首先让我们了解为什么运行时安全在当今的威胁环境中如此重要。

## 微服务最大化攻击面

大多数云工作负载都以微服务的形式存在。我们总是敦促人们迁移到云并将单体应用程序分解为微服务。这是一个好建议。但是，微服务带来了一系列独特的复杂性。

- 当您将单体软件分解为微服务时，您实际上是在增加恶意行为者潜在的入口点。攻击面扩大。从 API 到数据库连接和第三方集成，跟踪入口点变得像噩梦一样。
- 这些入口点是动态的，这意味着它们是动态创建和销毁的。一组微服务中没有固定的入口点数量。因此，仅仅在部署期间检查漏洞是不够的。

![](https://cdn.thenewstack.io/media/2024/06/e070ccbb-microservices-attack-surfaces.png)

## 云弹性：没有固定边界

云计算的魅力在于能够随时扩展您的基础设施。对于那些不想购买本地硬件并在前期投入大量资金的公司来说，这是一个非常棒的选择，只是为了看到这些闪亮的新硬件在淡季闲置。

但这种弹性带来了一个安全问题：随着实例的出现和消失，安全团队很难建立一个固定的边界来防御。这就像不断改变家里的入口位置和数量。

传统上，您会将网络安全策略应用于固定数量的虚拟机 (VM) 和主机，这样就可以了。但当涉及到云安全时，您无法在实例出现时手动将安全策略应用于它们。您需要使用配置脚本来自动执行此操作。但是，即使此脚本中存在轻微的错误配置，也会削弱实例的安全性。

## 云基础设施部分本质上是相互关联的

2019 年，Capital One 由于其 [AWS](https://aws.amazon.com/?utm_content=inline+mention) Web 应用防火墙配置错误而遭受了大规模数据泄露。有趣的是，攻击者并没有直接访问公司的 S3 存储桶。相反，他们使用了一种称为横向移动的方法。一位 Reddit 用户完美地 [总结](https://www.reddit.com/r/aws/comments/cl4h6t/comment/evsu7cg/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) 了这一事件：

*“攻击者没有直接访问 S3 存储桶；相反，她访问了一台 EC2 服务器，该服务器具有允许访问存储桶的 AWS 角色。因此，尽管她的帐户权限已正确配置，但她能够通过不同的资源进行隧道连接以提高她的权限级别。”*

如果没有运行时安全和主动异常检测，这种横向移动将无法识别。

### 关于 Equifax 数据泄露的案例研究

2017 年，Equifax 遭受了大规模数据泄露。入口点？一个面向客户的 Apache Struts 服务器，存在漏洞。更重要的是：负责监控与服务器相关的网络流量的设备的安全证书在攻击发生前几个月就过期了。

这里的关键概念是“活动资产清单”。Equifax 无法了解其活动资产清单以及这些资产用于安全工作的方式的依赖项或工具。

即使是最经过验证的代码也可能存在漏洞。公司需要警惕旧软件和工具中新发现的漏洞。

## 运行时容器和应用程序安全来救援

这些网络安全威胁可以通过运行时安全来很大程度地缓解，运行时安全应用实时检查，而不是将安全视为一次性过程。

您的应用程序不再是单体的。通过将安全视为分层而不是单体，一切都将到位。当您实时了解容器中运行的所有资产、Kubernetes Pod 的配置以及底层操作系统时，您将更清楚地了解哪些元素需要保护——以及如果这些元素配置不当会发生什么。

## CWPP 工具自动检测

CWPP 收集并分析在云平台上运行的所有活动资产。当我们说“云工作负载”时，我们的意思是：

![](https://cdn.thenewstack.io/media/2024/06/450c6bc3-active-asset-inventory.png)

- 应用程序代码。
- 依赖项或库。
- 容器镜像。
- Kubernetes 和 Pod。
- 甚至底层操作系统。

拥有可见性有助于建立资产之间的关系。它们如何相互连接？它们如何“相互交谈”？网络图回答了这些问题。

*建立活动资产清单并识别它们如何工作以及相互交互的最重要好处是创建基线。此基线构成了实时异常检测的基础。*

例如，如果 Equifax 在 2017 年能够清楚地了解其活动资产，它可能不会遭受数据泄露。Apache 团队在 2017 年 3 月发布了修补版本，远早于 [Equifax 宣布](https://investor.equifax.com/news-events/press-releases/detail/237/equifax-releases-details-on-cybersecurity-incident) 它在 9 月份遭到入侵。如果该公司及时修补了 Apache Struts 漏洞，泄露可能不会发生。

当您在发现漏洞时主动修补软件时，您会减少攻击面。由于 CWPP 系统不断更新其数据库，其中包含已知的漏洞列表，因此这些运行时应用程序保护安全系统可以检测到试图利用这些已知漏洞的尝试。例如，CWPP 系统可以主动检测试图探测网站是否使用 WordPress 6.5.0（存在严重漏洞）的脚本。然后，系统可以采取必要的措施，例如阻止违规的 IP 地址。

另一种以实时方式缓解攻击的好方法是明确定义容器可以做什么和不能做什么。CWPP 工具更进一步，通过限制容器在系统级别（而不仅仅是进程级别）可以做什么和不能做什么。

这些工具可以定义容器内的哪些进程可以访问敏感文件，然后对这些规则进行编码并自动执行这些规则，以指导容器访问什么和不访问什么。

相同的运行时容器安全机制可用于网络微分段。这允许更严格地执行规则，例如哪些 Kubernetes Pod 可以相互通信或应该或不应该使用哪些端口。

## 运行时安全限制：如何处理它们

2023 年，Sophos 发布了一份安全公告，解释了 BlackCat 勒索软件是如何渗透其客户的 Azure 存储帐户的。BlackCat 是同一款勒索软件，它在 2024 年 [从 Change Healthcare 窃取了数 TB 的数据](https://www.hhs.gov/hipaa/for-professionals/special-topics/change-healthcare-cybersecurity-incident-frequently-asked-questions/index.html)，并锁定了该公司系统。

Sophos 攻击者首先停用了 Sophos Central 控制台实施的安全策略。他们通过渗透 LastPass Chrome 扩展程序并窃取一次性密码 (OTP) 来实现这一点，该密码提供了对 Sophos Central 的访问权限。在禁用安全策略后，攻击者入侵了受害者的 Azure 存储帐户。

这意味着攻击者从受害者的系统跳到了其 Azure 存储帐户。Scattered Spider 勒索软件的工作方式也类似。这两个勒索软件团伙都采用社会工程学策略，如网络钓鱼，以获得初始立足点。

在这种情况下，运行时安全可能效率不高。相反，网络分段可以限制攻击者访问敏感的 Azure 存储数据。当您将工作负载分解为不同的网络段时，您可以为所有段定义访问策略。网络段隔离连接的系统，以防止攻击者横向移动。

此外，可以创建考虑工作负载敏感性的策略。在 Sophos 案例中，受害公司本可以对与 Azure 存储帐户关联的网络段实施更严格的防火墙规则。

但让我们来扮演一下魔鬼的代言人。

如果攻击者利用 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 的远程桌面协议 (RDP) 和远程监控工具来渗透 Azure 存储帐户会怎样？这看起来像是对 Azure 存储帐户的有效访问，因为它将使用受害者的 IP。这就是零信任发挥作用的地方。

## 零信任和最小权限仍然是关键

让我们回到 Capital One 数据泄露事件。攻击者没有直接访问 S3 存储桶来窃取数据。相反，她首先入侵了一个可以访问 S3 存储桶的 EC2 实例。

如果该组织实施了零信任策略，这起事件可能就不会发生。零信任假设您的系统已经存在漏洞，并且已被恶意行为者渗透。

如果 Capital One 实施了此策略，它将使用多因素 [身份验证](https://roadmap.sh/videos/basics-of-authentication) 来强化 EC2 实例。即使攻击者获得了对该实例的访问权限，她也无法访问 S3 存储桶。

运行时安全工具会持续监控云工作负载，为各种工作负载创建基线权限要求，并持续识别授予容器、Pod 或 EC2 等云基础设施的不必要权限。

根据他们的发现，这些工具会推荐最不具许可性的策略，这些策略将允许 IT 资产仅访问其正常工作所需的存储位置或文件；其他任何内容都无法触及。

## 底线

2022 年，发布了 25,081 个 CVE。到 2023 年，这一数字增长到超过 28,900 个。您的 IT 基础设施（无论是在本地还是异地）对攻击者来说都是一个非常诱人的狩猎场。

攻击也变得更加复杂。基于签名的威胁检测的时代已经过去了。您必须接受，下一次网络攻击可能是完全独特的，没有任何先例。

在这种情况下，采取主动的安全措施势在必行。在部署之前、期间和之后持续监控工作负载和云平台。攻击者只需要一个漏洞入口点就可以毁掉一家企业。

像 [AccuKnox CWPP](https://www.accuknox.com/ebooks/accuknox-cloud-workload-protection-platform-cwpp-an-inside-look) 这样的运行时安全工具和严格的零信任策略将有助于在未来几年内保护您的企业安全——无论攻击者变得多么复杂。
