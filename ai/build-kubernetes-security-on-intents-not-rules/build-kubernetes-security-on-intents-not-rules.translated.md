# 基于意图而非规则构建 Kubernetes 安全性

![基于意图而非规则构建 Kubernetes 安全性的特色图片](https://cdn.thenewstack.io/media/2024/09/3217aca5-intent-driven-kubernetes-security-1024x576.jpg)

随着 Kubernetes 的发展和采用率的提高，确保其安全性仍然是企业的首要任务。随着组织扩大其 [Kubernetes 的使用](https://www.accuknox.com/blog/kubernetes-security-best-practices)，他们在保护其环境方面面临着越来越大的挑战。根据 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 的 2024 年 Kubernetes 安全状况报告，[67% 的受访者因 Kubernetes 安全问题而延迟或放缓](https://www.redhat.com/en/blog/state-kubernetes-security-2024#:~:text=Security%20issues%20continue%20to%20impact,which%20some%20organizations%20still%20struggle.) 了应用程序开发。

本文将帮助首席安全官 (CSO) 和 [DevOps 工程师](https://roadmap.sh/devops) 了解：

- 管理 [Kubernetes](https://thenewstack.io/kubernetes/) 安全性的主要挑战。
- 传统安全措施的不足之处。
- 需要基于意图的 Kubernetes 安全性监控。

## Kubernetes 安全性如此复杂的原因

由于 Kubernetes 集群由多个微服务和组件组成，因此每个微服务和组件都可能是攻击者的潜在入口点。从本质上讲，活动部分越多，攻击面就越大。

对于严重依赖这些系统的组织来说，这可能会带来问题。Kubernetes 配置中只需一步失误，就可能导致严重风险，例如数据泄露或未经授权访问工作负载。

此类环境中的安全漏洞可能是危险的。它不仅会损害您公司的声誉，还会失去客户的信任。

还需要考虑财务影响，例如违规响应成本、业务损失和监管罚款，以及遵守行业法规，例如 [PCI DSS](https://thenewstack.io/what-to-know-about-container-security-and-digital-payments/)。这些法规旨在保护数据。不遵守规定可能会导致巨额罚款和处罚。

## Kubernetes 安全性的 5 大挑战

有一点很明确，Kubernetes 的潜力与其风险相当（如果不是更大），除非它得到适当保护。然而，公司发现确保 Kubernetes 集群的各个方面得到保护极具挑战性。

Kubernetes 的多方面性质意味着组织必须 [维护安全性](https://roadmap.sh/cyber-security) 在不同的层面上，包括基础设施、网络运行时、容器运行时、控制面板等。

以下是组织在跨这些层建立安全性时面临的主要挑战：

### 1. 扩展攻击面

每个 Kubernetes 集群都有多个微服务和组件在环境中交互，这为攻击者增加了潜在的入口点。您部署的容器和集群越多，攻击面就越大，从而更难查明和减轻漏洞。

### 2. 配置管理

由于人为错误导致的错误配置是 Kubernetes 中的主要挑战之一。

在 [云安全播客](https://www.cloudsecuritypodcast.tv/videos/kubernetes-goat-vulnerable-by-design) 的一集中，[Madhu Akula](https://www.linkedin.com/in/madhuakula/)，一位杰出的安全领导者和 Kubernetes Goat 的创建者，说：“Kubernetes 本身在设计上并不是固有地易受攻击，但安全问题通常源于错误配置。例如，网络安全策略 (NSP) 对于控制 Pod 之间的流量至关重要，但许多组织忽视了实施它们，无意中使应用程序面临未经授权的访问。”

由于容器是动态的，因此很难确定是什么导致了错误配置并保持一致的安全态势。

### 3. Pod 到 Pod 的网络

Kubernetes 提供了广泛的网络配置选项，允许集群中的所有 Pod 默认相互通信。如果一个 Pod 遭到破坏，它可能会攻击其他 Pod，除非设置了适当的网络策略。

假设一家金融服务公司部署了一个由多个微服务组成的应用程序，例如用户管理服务、交易处理服务、客户支持服务和分析服务，每个服务在单独的 Pod 中运行。

默认情况下，Kubernetes 允许所有 Pod 相互通信，从而创建一个开放网络。因此，如果攻击者利用用户管理服务 Pod 中的漏洞，该 Pod 负责用户身份验证和存储敏感用户数据，他们可以使用此初始立足点来扫描和利用其他 Pod 中的漏洞。

### 4. 软件供应链问题

Kubernetes 环境严重依赖于庞大的
[软件供应链](https://thenewstack.io/fortifying-the-software-supply-chain/)，包括应用程序组件和 [CI/CD](https://thenewstack.io/ci-cd/) 管道。此链中的任何部分（例如过时的库或弱访问控制）中的漏洞都可能带来严重的安全风险。

在另一个
[云安全播客](https://www.cloudsecuritypodcast.tv/videos/kubernetes-security-at-scale-in-a-ci-cd-pipeline) 中，网络安全从业者 [Michael Fraser](https://www.linkedin.com/in/itascode/) 说：“在 CI/CD 管道中保护 Kubernetes 是一项多方面的挑战，需要持续的警惕——它不仅涉及保护集群，还确保每次部署、配置和交互都能抵御不断变化的威胁。”

管理这些供应链复杂性需要从开发到运行时的强大控制。

### 5. 基础设施安全

保护 Kubernetes 基础设施涉及保护控制平面组件（如 API 服务器）和工作节点。无论您是在本地管理 Kubernetes 还是使用云服务，保护这些组件都可能很复杂。

对此安全性的责任级别根据您是使用云提供商还是自己处理而有所不同，增加了额外的复杂性。

## 传统安全方法为何不足

虽然以下解决方案在更静态的单体架构中可能有效，但它们在现代 Kubernetes 集群的动态分布式环境中经常不足。

以下是传统 Kubernetes 安全解决方案的一些主要限制：

### 被动，而非主动

传统安全方法侧重于运行时安全扫描，仅在威胁被激活时才检测到威胁——换句话说，在造成损害之后。这不仅会留下一个关键的漏洞窗口，还会在问题升级之前难以缓解问题。

例如，2017 年，最大的信用报告机构之一 Equifax 遭受了大规模数据泄露，影响了
[1.47 亿人。](https://www.hbs.edu/faculty/Pages/item.aspx?num=53509) 这次泄露是由 Apache Struts（一个开源 Web 应用程序框架）中的一个漏洞造成的，而 Equifax 未能及时修补。Equifax 的安全措施主要是被动的。他们仅在攻击者已经利用该漏洞后才发现该漏洞。

这种方法导致了严重的财务和声誉损害，突显了在威胁被利用之前解决威胁的主动安全解决方案的必要性。

### 性能开销

传统的安全协议将计算过程堆积起来以执行不同的任务，包括加密、解密、验证或签名数据。

这不仅会导致性能问题，还会增加延迟，影响服务质量和用户体验。

例如，在通过公司网络传输大文件之前对其进行加密可能会引入延迟。这可能会减慢关键业务应用程序，如金融交易或实时分析。

### 过时信息

过时的安全方法依赖于已知漏洞的既定数据库来识别和缓解风险。然而，这些方法对零日攻击无效，零日攻击利用以前未知的缺陷或新发现且未编目的威胁。

因此，系统仍然容易受到传统方法无法检测或预防的新兴且未记录的安全风险的攻击。

这些传统安全措施通常需要赶上分布式和动态的 Kubernetes 集群。这一差距指出了一个解决方案的紧迫性，该解决方案不仅可以实时预测和消除威胁，还可以保持高性能。

## 基于意图的安全管理

[Nimbus](https://github.com/5GSEC/nimbus) 是 AccuKnox 维护的一个开源工具，它通过简化和自动化安全管理为 Kubernetes 安全提供了新的方向。该工具包专注于安全意图，而不是特定的策略和工具。正如 README 所解释的：“Nimbus 旨在将安全意图与其实际实现分离，即使用策略引擎以及相应的策略和规则。”

主要功能包括：

**基于意图的安全管理：**用户定义安全意图，例如“防止权限提升”，而 Nimbus 通过适当的策略和工具处理实现。
**自动策略生成：**Nimbus 使用 Kubernetes 的主动协调逻辑来生成和执行与定义的安全意图一致的策略。
**灵活性和适应性：**Nimbus 可以与各种策略引擎配合使用，并适应变化，例如从一个容器网络接口 (CNI) 切换到另一个，而无需手动重新配置。
### 通过关注安全意图，Nimbus 降低了管理多个工具和策略的复杂性，使组织能够更轻松地在 Kubernetes 环境中保持强大的安全态势。

### Nimbus 的工作原理

Nimbus 通过将安全管理的复杂性抽象为更易于管理的框架来运作。以下是其工作原理：

#### 1. 定义安全目标

第一步是定义组织的高级安全要求。这可能是“限制对敏感数据的访问”或“防止对配置进行未经授权的更改”。这些高级安全目标也称为“意图”。

#### 2. 自动化策略转换

接下来，Nimbus 采用这些广泛的目标，并将它们分解为具体的可操作策略和规则。它使用各种策略引擎来强制执行具体措施。

例如，如果你的目标是阻止权限提升，Nimbus 将创建规则来强制执行该目标，例如控制谁获得管理员权限并监控任何异常活动。

#### 3. 持续协调

Nimbus 始终保持警惕，密切关注你的环境，以确保一切按预期工作。如果发生变化，Nimbus 会主动调整规则以适应新情况。

#### 4. 使用 Kubernetes 的内置系统

Nimbus 使用 Kubernetes 的内置系统进行持续的 Kubernetes 安全监控和调整。这意味着即使你的环境随着新应用程序、更新或更改而不断发展，Nimbus 也可以无缝适应这些修改，与你的安全目标保持一致，以保持防御的主动性和适应性。借助自动策略生成和灵活性，Nimbus 可以帮助你在不断变化的环境中领先于威胁。

## 总结

传统的安全措施不再适用于动态的 Kubernetes 环境。如果你的组织仍在依赖这些方法，请自问：

- 如果一个漏洞数周未被发现，会对你的业务产生什么影响？
- 安全漏洞在声誉和收入损失方面会造成多大损失？
- 你的当前措施是否足以防止关键应用程序开发中的延迟？

如果你的最后一个问题的答案是否定的，那么是时候采用更好的方法了。

[AccuKnox Kubernetes 安全解决方案](https://www.accuknox.com/products/kubernetes-security) 专为运行时保护、威胁检测和法规遵从性而设计。不要等待攻击者潜入——立即使用 AccuKnox 保护你的环境。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。