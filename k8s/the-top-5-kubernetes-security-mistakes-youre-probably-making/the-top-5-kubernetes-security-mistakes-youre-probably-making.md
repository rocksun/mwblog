<!--
title: 你可能正在犯的5个Kubernetes安全错误
cover: https://cdn.thenewstack.io/media/2024/02/677afe4e-slip-up-709045_1280-1024x682.jpg
-->

探讨Kubernetes运行时安全的几大风险。

> 译自 [The Top 5 Kubernetes Security Mistakes You’re Probably Making](https://thenewstack.io/the-top-5-kubernetes-security-mistakes-youre-probably-making/)，作者 Torsten Volk。

我们知道Kubernetes在安全方面与众不同，但直到现在我们才意识到其威胁的全部范围。自动化部署、共享基础设施以及跨越传统服务器和网络边界进行扩展的能力尽显眼前。但所有这些好处都伴随着更广阔的威胁景观。

回顾[2023年Kubernetes相关的安全漏洞](https://thenewstack.io/kubernetes-security-in-2023-adoption-soars-security-lags/)大幅增加导致解雇和罚款，本文描述了其中的五大根本原因。与此同时，构建在扩展的伯克利数据包过滤器(eBPF)之上的[开源工具和平台](https://thenewstack.io/solana-blockchain-crashes-into-open-source-top-10/)被证明特别有效地缓解了Kubernetes的安全威胁，正如下文所探讨的那样。

这五个常见错误的每一个都部分归因于组织难以适应[云原生应用程序](https://thenewstack.io/cloud-native-apps-demand-cloud-native-storage-systems/)新世界的分布式、可扩展和动态特性。在Kubernetes的世界里，完整的可观测性、应用程序可视性以及全面的运行状况和性能监控不再是可选的。

1. **缺乏上下文的警报**: 在[迅速扩张的云原生](https://thenewstack.io/measuring-the-state-of-cloud-native-security/)宇宙中，安全措施的有效性取决于智能的、具有上下文意识的系统。这些系统必须能够检测到不寻常的活动，决定一个安全漏洞对特定的应用环境是否相关，根据严重性优先级排序警报，并启动自动根因分析和响应以降低威胁。

![](https://cdn.thenewstack.io/media/2024/02/415cfcec-k8s-mist8ks-01-1024x615.png)

*图表显示了在Kubernetes相关的CVE中最常提到的10个产品。颜色说明了每个单独产品引入的漏洞类型。(来源:ReveCom;数据来源:Mitre公司)*

2. **配置错误**: Kubernetes配置主要使用YAML文件定义，这是一种人类可读的数据序列化标准。但是，YAML的简单性具有迷惑性，因为小错误可能导致重大的安全漏洞。一个常见的错误是错误的缩进或格式，这可能导致配置被错误应用或根本不应用。例如，YAML文件配置错误可能会在没有认证的情况下无意中将[Kubernetes仪表板公开到公共互联网](https://thenewstack.io/kubernetes-authentication-solved-spiffe-spire-move-to-cncf-incubation/)，从而导致未经授权的访问。类似地，在YAML文件中硬编码敏感凭据可能会为攻击者提供轻松访问集群的途径，如果该文件被曝光的话。Kubernetes依赖这些YAML文件进行编排，即使是一个小错误也可能蔓延成灾难，可能危及整个集群。

![](https://cdn.thenewstack.io/media/2024/02/c3a7f862-k8s-mist8ks-02-1024x1002.png)

*该图显示了基于2023年记录的所有228个Kubernetes相关CVE构建的关联网络。(来源:ReveCom,数据来源:Mitre)*

3. **缺乏微分段**: [多伦多公共图书馆](https://www.cbc.ca/news/canada/toronto/toronto-public-library-ransomware-employee-data-1.7028982)遭受的勒索软件攻击突显了Kubernetes环境中网络微分段的重要性。仅限制对必要资源的网络访问，微分段对阻止[攻击蔓延和保护敏感数据](https://thenewstack.io/combating-healthcare-data-attacks-during-coronavirus-outbreak/)至关重要。该图书馆的经历表明，缺乏微分段使勒索软件能够在网络上迅速扩散，导致大规模的数据泄露。实施微分段可能会大大限制攻击范围，甚至完全预防攻击。

4. **持续监控缺失**: 无法高估Kubernetes环境中持续监控的必要性。这涉及对网络流量、系统日志和用户行为进行警惕监控，以检测异常情况表明安全漏洞。如果没有这样的持续监督，恶意活动可能长期不被发现，使攻击者能够[利用机密数据](https://thenewstack.io/vex-standardization-for-a-vulnerability-exploit-data-exchange-format/)甚至劫持合法用户凭据。

5. **内部威胁**: [2023年Forever 21遭受的数据泄露](https://techcrunch.com/2023/08/31/forever-21-data-breach-half-million/)影响了50万客户，强调了内部威胁的存在风险。据信这起泄露源自钓鱼攻击，导致[未经授权访问该公司的Kubernetes环境](https://thenewstack.io/securing-access-to-kubernetes-environments-with-zero-trust/)，并后续出现大规模数据盗窃。这一事件强调了健全的内部安全措施的必要性，包括严格的访问控制、多因素认证、全面加密和定期的安全意识培训。

## eBPF如何解决Kubernetes运行时的关键安全挑战

在容器化基础设施快速发展的世界中，eBPF是解决[Kubernetes运行时安全](https://thenewstack.io/vmware-to-acquire-octarine-to-boost-kubernetes-runtime-security/)挑战的关键技术。eBPF最初被设计用于高效的网络数据包过滤，现已发展成为一种通用的系统级监控和安全工具。它在操作系统内核中运行沙盒程序，允许在不损害系统稳定性或性能的情况下进行高级的数据收集和操作。这种[安全高效地检查系统和网络操作](https://thenewstack.io/container-security-101-a-guide-to-safe-and-efficient-operations/)的能力使eBPF成为Kubernetes环境中必不可少的资产。它增强了上下文感知警报、启用实时配置审计、支持有效的网络微分段、提供全面的系统和网络监控以及加强内部威胁检测。这些功能不仅仅是技术成就，它们代表了确保[Kubernetes部署安全性和完整性](https://thenewstack.io/the-secret-to-securing-kubernetes/)的重要商业优势，直接影响运营可靠性、法规遵从性以及敏感数据的保护。

1. **增强的上下文感知警报**: eBPF对系统和网络操作的详细可视性支持复杂的、上下文感知的警报机制。传统的警报系统通常会生成大量警报，其中许多缺乏相关性，导致安全团队警报疲劳。eBPF的上下文感知警报通过提供丰富的上下文信息警报来应对这一点，使团队能够快速区分假警报和真实威胁。由于eBPF深度集成在Linux内核中，它可以监控广泛的实时系统活动，因此可以提供这种上下文信息。这包括在细粒度级别跟踪系统调用、网络流量和应用程序行为。

2. **实时配置审计**: eBPF促进Kubernetes配置的实时监控，这对于经常更改配置的动态环境中的企业至关重要。对错误配置或未经授权的更改进行即时检测和警报对于保持与法规标准和内部政策的持续合规至关重要。与传统方法相比，这种持续监控代表了一个重大进步，减少了暴露于漏洞的风险，漏洞可能导致数据泄露或违反合规性，两者都可能带来巨大的财务和声誉后果。

3. **网络流监控实现微分段**: eBPF对网络流量的细粒度监控对于实施[有效的](https://thenewstack.io/how-the-network-effect-levels-the-cybersecurity-war-zone/)网络微分段至关重要，这是保护敏感业务数据的关键策略。通过执行严格的安全策略和阻止攻击者在网络内的横向移动，eBPF有助于保护关键的业务资产。对于处理敏感客户数据或知识产权的企业来说，这一点尤为重要，因为泄露可能导致重大的财务损失和客户信任的损害。

4. **全面系统和网络监控**: eBPF跟踪Kubernetes集群内的每个系统调用和网络数据包的能力提供了检测异常和潜在威胁的必要监控级别。这种全面监控对企业保持运营完整性和服务可用性至关重要。异常的及早发现可以防止可能影响客户体验、导致收入损失或损害品牌声誉的中断。

5. **可观察性以检测内部威胁**: eBPF通过对应用程序和系统行为进行详细的可观察性来增强检测和防止内部威胁的能力。内部威胁对企业来说是一个日益受到关注的问题，因为它们可能导致重大的财务和知识产权损失。eBPF跟踪系统调用、网络活动和对敏感数据的更改的能力有助于识别可能表明内部威胁的异常行为，从而防范潜在的内部泄密。

## eBPF对保持Kubernetes的安全至关重要

eBPF是在Kubernetes集群中创建通用“安全毯”的基础，并且适用于本地环境、公有云和边缘计算。它在内核级的集成允许立即检测监控差距，并无缝地将[安全措施](https://thenewstack.io/why-devops-needs-to-change-security/)应用到新的和变化的集群。eBPF可以自动将预定义的安全策略和监控协议应用到环境中的任何新集群。

随着新集群的创建，eBPF检测到并无缝地应用这些安全措施，确保即使是临时或最近部署的集群也立即被覆盖在与现有集群相同的全面安全保护伞下，在整个Kubernetes景观中提供一致的、自适应的安全性。

重要的是要理解每个安全软件供应商可以以不同的方式实现基于eBPF的安全功能，因为eBPF仅为这些供应商提供了在内核级直接监控和操作系统调用和应用程序活动的功能。

Kubescape是一个[开源的Kubernetes](https://thenewstack.io/how-kubernetes-open-source-underpin-conde-nast-operations/)安全平台，它将基于eBPF的漏洞扫描、策略实施、上下文警报、配置审计和内部威胁检测直接编织到开发者IDE、CI/CD管道和Kubernetes集群中。

该项目由ARMO创建，ARMO提供ARMO平台，这是一个由Kubescape驱动的企业级[Kubernetes安全平台](https://thenewstack.io/6-kubernetes-security-best-practices/)。这种全面的方法使组织能够从开发的最早阶段到部署和持续运营的[各个阶段增强其安全态势](https://thenewstack.io/managing-cloud-security-risk-posture-through-a-full-stack-approach/)。Kubescape旨在为DevSecOps[团队和平台工程师](https://thenewstack.io/how-intuits-platform-engineering-team-chose-an-app-definition/)提供他们需要的安全保障，以同时优化开发人员的生产力和安全性。

Torsten Volk是企业管理联合会(EMA)的人工智能、机器学习、DevOps、容器和服务器less服务的管理研究总监，EMA是一家行业分析和咨询公司，专门为全谱系提供深刻的洞察....
来自Torsten Volk的更多信息
