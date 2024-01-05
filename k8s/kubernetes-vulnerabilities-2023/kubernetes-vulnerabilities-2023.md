<!--
title: 2023年Kubernetes漏洞综述
cover: ./cover.jpg
-->

本文综述了2023年Kubernetes的漏洞，从CVSS、漏洞类型、影响类型等相关方面对其进行分类。

> 译自 [2023 Kubernetes vulnerabilities roundup
2023 Kubernetes vulnerabilities roundup](https://www.armosec.io/blog/kubernetes-vulnerabilities-2023/)。作者 Ben Hirschberg，是 Armo 的 CTO 和联合创始人。

无论软件开发模式如何，透明的漏洞披露都在有效的风险管理中发挥着关键作用。[Common Vulnerabilities and Exposures(CVE)](https://www.armosec.io/glossary/common-vulnerabilities-and-exposures-cve/)数据库提供了宝贵的资源，即使补丁不可用，它也可以洞察已知的弱点。这使得组织能够在优先考虑缓解策略和保护系统方面做出明智的决定。

漏洞评分系统对CVE的严重程度进行排名，其中[Common Vulnerability Scoring System(CVSS)](https://www.armosec.io/glossary/common-vulnerability-scoring-system-cvss/)是最流行的。但是，在确定漏洞优先级时，不应将CVSS视为最后的言语，因为它侧重于严重性和利用性，但缺乏不同Kubernetes安装特有的必要上下文和环境信息。

此外，全面风险管理方法需要考虑CVSS之外的因素，例如威胁的动态特性、实际可利用性以及新兴的漏洞评分系统(例如利用[预测评分系统(EPSS)](https://www.armosec.io/glossary/exploit-prediction-scoring-system-epss/)和[已知利用漏洞(KEV)目录](https://www.cisa.gov/known-exploited-vulnerabilities-catalog))。

本文不仅从CVSS，还从漏洞类型、影响类型等相关方面对2023年Kubernetes的漏洞进行分类。我们还将广泛讨论常见弱点枚举(CWE)标准和保持知情的最佳实践。

## Kubernetes中的漏洞

尽管增长迅速，但[Kubernetes](https://www.armosec.io/glossary/kubernetes/)从未被视为默认安全，主要是因为其原生集群缺少默认激活[网络策略](https://www.armosec.io/glossary/kubernetes-network-policy/)和[pod安全标准](https://www.armosec.io/glossary/pod-security-standards/)等安全功能。因此，用户必须采取的第一步是激活Kubernetes原生安全功能。从2018年到2023年，Kubernetes中漏洞数量增加了[440%](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=kubernetes)。这并不表示安全性下降，而是反映了不断增长和扩展的攻击面。只要开发人员正在编写软件和扩展生态系统，我们就可以期待看到更多的漏洞。

![](https://www.armosec.io/wp-content/uploads/2023/12/Fig_1_Kubernetes-vulnerabilities-trend-1536x1045.png.webp)

*图1:Kubernetes漏洞趋势(数据来源:cve.mitre.org)*

根据“[2023年Kubernetes安全状态报告](https://www.redhat.com/rhdc/managed-files/cl-state-kubernetes-security-report-262667-202304-en.pdf)”，67%的受访者注意到Kubernetes安全问题迫使他们延迟或放慢部署。此外，90%的人报告在过去12个月中经历过一次或多次安全事件。因此，漏洞正在上升，主要是由于Kubernetes周围复杂的漏洞管理流程和不断扩展的生态系统。

## 2023年主要的Kubernetes漏洞

在深入探讨漏洞之前，让我们快速回顾一下用于识别、报告和优先考虑Kubernetes漏洞的公共数据库和评分系统。

- [MITRE CVE数据库](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=kubernetes): 编录已知的公开软件安全漏洞。
- [Kubernetes官方CVE源](https://kubernetes.io/docs/reference/issues-security/official-cve-feed/):Kubernetes对系统已知安全漏洞的数据库。
- [CVSS计算器](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator): 因为并非每一个发布的CVE都需要采取缓解措施，所以使用CVSS评估来对其严重程度进行排名。注意: CVSS不是(也从未打算成为)终极评分系统，[EPSS](https://www.first.org/epss/model)和[KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)目录正在变得越来越受欢迎。
- [CVE详细信息数据库](https://www.cvedetails.com/vulnerability-list/vendor_id-15867/product_id-34016/Kubernetes-Kubernetes.html): 包括高级漏洞搜索，如建议、漏洞利用、RSS源等与漏洞情报相关的其他功能。
- [GitHub安全公告数据库](https://github.com/advisories?query=kubernetes): GitHub收集和维护的与开源软件相关的安全漏洞和安全公告的汇编。

在66个已知漏洞中，有59个是由于与Kubernetes一起使用的外部工具造成的，只有7个是Kubernetes本身的直接问题。这些漏洞分为两类:

- Kubernetes问题和安全漏洞
- 来自生态系统工具的漏洞

![](https://www.armosec.io/wp-content/uploads/2023/12/Fig_2_Vulnerability-entry-point-analysis-1536x976.png.webp)

*图2:漏洞入口点分析(数据来源:cve.mitre.org)*

在本文中，我们检查和总结了Kubernetes中的所有7个已知漏洞，以帮助您监控[Kubernetes集群](https://www.armosec.io/glossary/kubernetes-cluster/)并缓解潜在的安全风险。

### CVE-2023-5528/3955/3893/3676

**通过在Windows节点上创建pod或持久卷，用户可以提升到管理员特权。**

这四个漏洞都发生在Windows节点上的用户身上，这些用户有能力创建pod或持久卷，并将其特权提升到管理员级别。这些问题只影响使用Windows节点的内置存储插件的集群。

这些漏洞都被NIST国家漏洞数据库评为8.8(高风险)，对某些Kubernetes版本极为重要，即从1.8.0开始的所有版本，包括所有后续次要版本，都是容易受到攻击的。但是，已经在2023年11月14日发布了补丁来完全解决此问题。

**预防和缓解:**

- 应用提供的补丁。
- 监控Kubernetes审计日志，以发现对此漏洞的利用迹象。

### CVE-2023-2728

**用户可以启动容器并绕过可挂载机密策略。**

通常，可挂载机密策略旨在确保使用服务账户的pod只能访问服务账户机密字段中指定的机密。这通常由ServiceAccount准入插件启用。

此漏洞特别影响同时使用ServiceAccount admission plugin和存在kubernetes.io/enforce-mountable-secrets注释的短暂容器的Kubernetes集群。其严重级别被评为中等，CVSS得分为6.5。

**预防和缓解:**

为kube-apiserver组件安装更新。

使用验证Webhook，例如[Gatekeeper](https://github.com/open-policy-agent/gatekeeper)和[Kyverno](https://github.com/kyverno/kyverno)。

### CVE-2023-2727

**用户能够绕过容器镜像限制。**

Kubernetes通常采用ImagePolicyWebhook来规范哪些[容器镜像](https://www.armosec.io/glossary/container-image/)是允许的。此漏洞允许用户启动应该被此控制阻止的镜像的容器，但这只发生在使用短暂容器时，短暂容器主要用于故障排除。

此漏洞影响同时使用ImagePolicyWebhook和短暂容器的Kubernetes集群。其严重级别被评为中等，CVSS分数为6.5。

**预防和缓解:**

- 为kube-apiserver组件安装更新。此更新保证短暂容器被禁止使用受ImagePolicyWebhook约束的镜像。
- 使用验证webhook，例如Gatekeeper和Kyverno。

### CVE-2023-2431

**Pod可以绕过seccomp(安全计算模式)配置文件的执行。**

此安全问题在Kubelet中被识别出来，特别影响为seccomp配置文件使用localhost类型但配置文件字段为空的pod。在这些情况下，pod可以在无限制模式下运行，这意味着seccomp(旨在限制容器可以执行的系统调用)不被执行。

NIST已经评估此漏洞的严重级别为中等，CVSS分数为5.5。但是，CVE编号机构(CNA)给出了更低的3.4分。

**预防和缓解:**

- 将Kubelet升级到修补版本(v1.27.2、v1.26.5、v1.25.10或v1.24.14)。

如图2所示，89%的漏洞来源于Kubernetes生态系统中的工具。值得注意的是，[Kyverno](https://kyverno.io/)、[Cilium](https://cilium.io/)、[AgroCD](https://argo-cd.readthedocs.io/en/stable/)和[Kube Pi](https://github.com/robermar23/kube-pi)等工具代表了这些漏洞的重要来源。然而，这并不一定表明这些工具本身存在缺陷或缺点。

![](https://www.armosec.io/wp-content/uploads/2023/12/Fig_3_Vulnerabilities-occurred-by-Kubernetes-ecosystem-tools-scatterplot-1536x677.png.webp)

*图3:Kubernetes生态系统工具造成的漏洞散点图(数据来源:[cve.mitre.org](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=kubernetes))*

在一个快速发展的生态系统中，漏洞是常见的;关键是要积极监测它们并在必要时进行缓解。定期使用[ARMO Platform](https://www.armosec.io/)等工具扫描集群中的漏洞，对于快速识别这些漏洞及其上下文环境至关重要。

图3突出显示了CVSS分数较高的漏洞。在通用漏洞评分系统中，关键漏洞通常在不需要特殊措施(如认证凭据)的情况下提供根级别访问。这些漏洞需要立即关注，因为它们可能使攻击者完全控制系统、窃取数据或严重中断操作。

同样，重要的是要注意CVSS分数不应该是衡量漏洞严重性的唯一标准。CVSS缺乏特定环境或应用程序的上下文信息，以及有关野外利用的详细信息。因此，[建议](https://www.armosec.io/blog/kubernetes-vulnerability-relevancy-and-prioritization/)采用全面的方法来衡量严重性，既考虑CVSS分数，也考虑可达性和运行时数据，同时与其他评分系统进行交叉参考。

### CVE-2023-22651

**这涉及SUSE Rancher中的不当特权管理。**

[SUSE Rancher](https://www.rancher.com/)是一个开源容器管理平台，在其中发现了CVE-2023-22651，这是一个严重的安全漏洞，CVSS评分为9.9。

由于其对特权管理的高影响，允许特权提升，此漏洞尤为严重。这影响从2.6.x或2.7.x Rancher版本升级到2.7.2的用户。值得注意的是，直接安装2.7.2版本而没有遵循升级路径的用户不会受到此漏洞的影响。

这个问题的根本原因在于Rancher admission [Webhook](https://github.com/rancher/rancher/security/advisories/GHSA-6m9f-pj6w-w87g)更新逻辑中的缺陷。该Webhook在Rancher中发挥着关键作用，它在资源被允许进入集群之前强制执行验证规则和进行安全检查。由于更新逻辑失败，导致Webhook配置错误，它就不能再有效地执行这些验证。这种安全性不足可能为严重的特权提升和数据损坏创造机会，严重危及集群的整体安全性和完整性。

**预防和缓解：**

- 升级 Rancher 补丁版本至 2.7.3 或更高。
- 此外，还有一个[推荐的解决方法](https://github.com/rancher/rancher/security/advisories/GHSA-6m9f-pj6w-w87g)，涉及手动重新配置 Webhook。

### CVE-2023-48312

**这涉及 Capsule Proxy 中的不当身份验证，导致特权升级。**

这也被识别为一个具有9.8 CVSS分数的关键漏洞。

[Capsule-proxy](https://github.com/projectcapsule/capsule-proxy) 是 capsule 运算符项目中使用的反向代理组件，主要用于 Kubernetes 环境。此漏洞的原因是缺少验证步骤以确认用户是否经过身份验证。特别是它影响禁用 [Kubernetes API 服务器](https://www.armosec.io/glossary/kubernetes-api/)中的匿名身份验证设置（设置为 "false"）的 Kubernetes 集群。

```yaml
anonymous_auth:
    # Disable anonymous authentication in Kubernetes API Server
    disabled: false  # Set to true to disable anonymous access
```

在这种情况下，可以绕过令牌审核机制，允许与 Kubernetes API 服务器的未授权交互，从而导致潜在的特权升级。

**预防和缓解：**

- 此问题已在 capsule-proxy 的版本 0.4.6 中得到解决，建议使用受影响的版本的用户升级到此版本或更高版本。

## 常见漏洞和曝光类型

在增强容器安全性方面，建议利用 gVisor 等容器隔离技术。这些工具在防止容器逃逸和未经授权的权限提升方面特别有效，在多租户环境中提供了可靠的隔离。这些技术对于增强容器的完整性和维护安全的多租户系统至关重要。

![2023年CWE常见曝露类型](https://www.armosec.io/wp-content/uploads/2023/12/Fig_4_Common-exposure-types-in-2023-1536x888.png.webp)

*图4：2023年常见曝露类型（数据来源：cve.mitre.org）*

根据分析，这是2023年五种最常见的漏洞类型：

- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)：不正确的输入验证
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)：将敏感信息暴露给未经授权的操作者
- [CWE-269](https://cwe.mitre.org/data/definitions/269.html)：不正确的权限管理
- [CWE-863](https://cwe.mitre.org/data/definitions/863.html)：错误的授权
- [CWE-862](https://cwe.mitre.org/data/definitions/862.html)：缺失的授权

了解这些曝露类型对于预防和减轻最常见的漏洞类型至关重要。

## 如何保持信息更新

有许多方法可以及时了解您的Kubernetes集群中的漏洞。保持关于常见CWE的最新信息同样重要。在本节中，我们讨论了通过对2023年所有公共漏洞进行彻底分析获得的关键见解。

网络安全中的一个持久性挑战是，无论系统有多安全，漏洞仍然存在。熟练的攻击者会找到利用这些弱点的方法。因此，了解正在发生的漏洞至关重要。在Kubernetes的背景下，有几种方法可以保持最新：

- 订阅[Kubernetes安全公告邮件列表](https://groups.google.com/forum/#!forum/kubernetes-security-announce)以获取有关新安全问题的更新。
- 监视[Kubernetes GitHub存储库](https://github.com/kubernetes/kubernetes)以了解报告的问题和修复措施。
- 关注[MITRE的CVE数据库](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=kubernetes)。

Kubernetes社区非常活跃；如果漏洞被公开报告，通常在几小时内通常会提供补丁。因此，建议定期应用补丁和更新。这也需要快速进行，因为黑客会尝试利用已公开的漏洞。工具如[Ansible](https://www.ansible.com/)和[Puppet](https://www.puppet.com/)在自动部署这些补丁方面非常有用。还建议基于CVE数据库进行定期漏洞扫描。组织可以使用[Kubescape](https://www.armosec.io/kubescape/)等开源工具扫描Kubernetes集群并进行风险评估。Kubescape不仅识别风险，还提供了有关补救的指导。

![Kubescape漏洞扫描](https://www.armosec.io/wp-content/uploads/2023/12/Fig_5_Kubescape-vulnerability-scan-results-1536x1217.png.webp)

*图5：Kubescape漏洞扫描结果*

尽管通常会解决公开标识的漏洞，但也有罕见的情况下使用以前未知的利用方法的新类型漏洞。在这种情况下，有规律地备份和制定灾难恢复计划至关重要。诸如[Kasten K10](https://www.kasten.io/product/)之类的工具有助于快速恢复数据并恢复正常运行。最后，如果集群或特定组件尚未设计，则应使用[攻击面减小](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)来最小化在系统上运行的不必要的软件和服务，从而减少黑客的潜在目标数量。

此外，建议利用gVisor等容器隔离技术来增强容器安全性。这些工具在防止容器逃逸和未经授权的特权提升方面特别有效，在多租户环境中提供坚实的隔离。这些技术对于增强容器的完整性并保持安全的多租户系统至关重要。

## 结论

在 Kubernetes 环境中有效地管理风险需要全面的安全策略，包括定期应用更新和补丁、严格遵循已建立的[安全实践](https://www.armosec.io/blog/kubernetes-security-best-practices/)，并及时了解新出现的威胁和漏洞。理解和解决常见漏洞，特别是与输入验证和权限管理相关的漏洞，对于开发强大的防御机制至关重要。

尽管与 2020 年和 2021 年等年份相比，2023 年对网络安全专业人员来说相对较为平静，但重要的是要记住网络威胁不断演变。我们可以从过去的漏洞中汲取经验，如 [CVE-2021-44228](https://www.armosec.io/blog/critical-cve-2021-44228-log4shell-vulnerability-kubernetes/)（Log4Shell）和 SolarWinds 攻击，以在 2024 年保持主动的警惕性。

随着攻击面的不断复杂化，尤其是在 Kubernetes 环境中，优先考虑有效识别和缓解安全问题。不要等待下一个重大事件发生，立即通过 [ARMO 平台](https://www.armosec.io/)加强你的 [Kubernetes 安全姿态](https://www.armosec.io/glossary/kubernetes-security-posture-management/)。其上下文漏洞评估消除了噪音，减少了优先级确定的工作量，提高了整体漏洞管理效率，让你可以专注于最重要的事务。确保你的 Kubernetes 部署安全，并享受一年的主动防御，而不是慌乱应对。
