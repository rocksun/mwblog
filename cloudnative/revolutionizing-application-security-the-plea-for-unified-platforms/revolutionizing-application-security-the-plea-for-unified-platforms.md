
<!--
title: 变革应用安全：统一平台的需求
cover: https://cdn.thenewstack.io/media/2025/04/5a7546e1-appsec-unified-platforms.jpg
summary: 云原生应用安全面临碎片化、左移困境、实时威胁和供应链风险四大挑战。统一安全平台是未来趋势，通过集成 SAST/DAST/IAST、SCA 等工具，结合 AI 驱动的实时监控和威胁检测，实现 AppSec、CloudSec、SecOps 的统一，打破数据孤岛，提升安全 ROI，构建实时云安全。
-->

云原生应用安全面临碎片化、左移困境、实时威胁和供应链风险四大挑战。统一安全平台是未来趋势，通过集成 SAST/DAST/IAST、SCA 等工具，结合 AI 驱动的实时监控和威胁检测，实现 AppSec、CloudSec、SecOps 的统一，打破数据孤岛，提升安全 ROI，构建实时云安全。

> 译自：[Revolutionizing Application Security: The Plea for Unified Platforms](https://thenewstack.io/revolutionizing-application-security-the-plea-for-unified-platforms/)
> 
> 作者：Damir Mujezinovic



# 应用安全革命：统一平台的需求

![应用安全革命：统一平台的需求的特色图片](https://cdn.thenewstack.io/media/2025/04/5a7546e1-appsec-unified-platforms-1024x576.jpg)

[Palo Alto Networks 的研究](https://www.paloaltonetworks.com/prisma/unit42-cloud-threat-research)表明，在生产环境中，大多数（63%）代码库都存在评级为高危或危急的未修复漏洞。此外，71% 的组织表示，匆忙的云原生应用程序部署[引入了安全漏洞](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/research/state-of-cloud-native-security-2024)，因此，如今 80% 的安全风险都发生在云端也就不足为奇了。这些数据强烈表明，当前保护云原生应用程序的方法并不充分，这可能会影响您的业务。

为了更好地理解保护云应用程序的挑战，我与 Palo Alto Networks 的 Cortex Cloud 产品管理副总裁 Sarit Tager 进行了交谈。我们谈到了未得到适当解决的四个最大不足之处，并讨论了如何采用更全面的方法来[云安全](https://thenewstack.io/security/)。

## 云原生应用安全的 4 大挑战

随着组织越来越多地采用云原生应用程序，保护整个应用程序生命周期（从代码开发到运行时环境）变得越来越复杂。以下是在保护云原生应用程序过程中出现的四个主要挑战。

### 1. 碎片化

云原生环境的复杂性，包括多种工具、第三方供应商和分布式系统，导致了碎片化。Palo Alto Networks 的研究发现，54% 的组织表示，云环境的[复杂性和碎片化](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/research/state-of-cloud-native-security-2024)对安全构成了重大挑战。反过来，这会极大地扩大组织的攻击面，使安全管理更具挑战性。

组织依靠各种安全解决方案来保护云原生应用程序。这包括静态、动态和交互式应用程序安全测试 (SAST、DAST、IAST)、软件成分分析 (SCA) 和[软件供应链安全](https://thenewstack.io/ebooks/security/a-blueprint-for-supply-chain-security/)。这些机制单独使用都有效，但碎片化会导致警报疲劳、数据孤岛和盲点。

正如 Tager 向我解释的那样，当前的应用程序安全方法是孤立构建的，无法阻止正在发生的攻击。

### 2. 左移

“左移”是一种专注于在部署之前，在开发周期的早期解决安全风险的做法。虽然理论上有效，但这种方法在实践中已被证明是有问题的，因为开发人员和安全团队的优先级存在冲突。例如，对于 86% 的组织来说，安全被视为阻碍软件发布的[门槛因素](https://www.paloaltonetworks.com/resources/research/state-of-cloud-native-security-2024)。与此同时，91% 的人表示开发人员需要生成更安全的代码。

开发人员的衡量标准是代码的速度和质量，通常将安全性放在次要位置。在实施左移策略的组织中，开发人员面临的繁重工作量可能会造成瓶颈、[运行时差距](https://thenewstack.io/why-cloud-security-fails-the-posture-vs-runtime-gap/)，并导致开发人员倦怠和生产力下降。这些因素加在一起最终会导致安全性和效率降低。

### 3. 对实时威胁防御的需求

云原生应用程序是动态的；不断部署、更新和扩展，因此绝对需要强大的实时保护措施。每次更新或部署应用程序时，都会出现新的代码、配置或依赖项，所有这些都可能引入新的漏洞。

问题在于，使用传统的、分块的方法很难实现实时云安全。组织需要实时安全措施，以提供对整个基础设施的持续监控，检测新出现的威胁并自动响应它们。正如 Tager 解释的那样，实施实时防御对于“在攻击者面前保持领先地位”是必要的。

### 4. 供应链风险

软件供应链风险源于通过软件开发管道和应用程序部署中使用的无数组件和服务引入的漏洞。
云原生应用程序往往严重依赖开源库和第三方组件。2021 年，[Log4j 的 Log4Shell 漏洞](https://thenewstack.io/log4j-why-organizations-are-failing-to-remediate-this-risk/)表明，单个受损组件如何影响全球数百万台设备，使无数企业面临风险。

有效的应用程序安全性现在已远远超出传统代码扫描的范围，必须反映现代工程环境。组织现在必须评估三个关键的供应链规范，以实现适当的保护：管道中的安全性 (SIP)、管道的安全性 (SOP) 和管道周围的安全性 (SAP)。每一个都支持工程的速度，而不会影响风险和安全管理。

那么，所有这些挑战的解决方案是什么？答案是统一安全平台。

## 为什么统一安全平台是未来的发展方向

鉴于上面概述的四个挑战，很明显为什么组织需要超越传统的点解决方案。孤立的安全工具的旧模式在云原生环境中不再可行，在云原生环境中，风险以极快的速度转移。

统一安全平台是一种集成的安全解决方案，可将多个安全功能整合到一个系统中。与传统的安全模型不同，统一平台可在企业的整个安全基础设施中提供集中化的可见性、自动化和协调。它们提供了一种整体的、实时的安全方法。

通过集成实时监控、自动威胁检测和主动风险缓解，这些平台消除了攻击者经常利用的漏洞。借助统一安全平台，组织可以从依赖孤立的、脱节的流程，转变为将安全性嵌入到应用程序开发和云运营的每个阶段。

正如 Tager 告诉我的那样，“[云和 AI](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) 的使用只会增长，攻击者也会改进他们的策略，因为他们也开始利用 AI 进行新型攻击。实现实时安全的唯一方法是通过一种平台方法，该方法集中整个云环境中的数据。一个 AI 可以在其上运行的数据湖，以提供及时的见解和行动。”

总而言之，统一安全平台是未来，因为它们：

- 通过减少管理多个工具和供应商的复杂性，将不同的安全功能整合到一个界面中，从而消除碎片化。
- 自动执行代理的监控和安全扫描，而不会减慢开发周期（从代码到云到安全运营中心），同时提供运行时保护。
- 通过自动合规性检查和策略执行来降低风险，包括错误配置、暴露的密钥和其他漏洞，并利用 AI 等工具。
- 提供跨整个云环境的实时可见性和持续监控，从而实现实时威胁防御。
- 提供对软件供应链的端到端可见性，使组织能够评估和验证开源库、第三方集成和依赖项的安全性。

“这种方法使组织能够无缝构建安全应用程序，并在问题变成威胁之前预防问题。组织无需在部署后追逐威胁，而是在一开始就实现保护，这要快得多，”Tager 说。

## 统一的 AppSec、CloudSec、SecOps 方法

[IBM](https://www.ibm.com?utm_content=inline+mention) 和 Palo Alto Networks 联合进行的一项 [2025 年的研究](https://newsroom.ibm.com/2025-01-28-ibm-and-palo-alto-networks-find-platformization-is-key-to-reduce-cybersecurity-complexity)表明，采用统一安全平台的组织检测事件的速度提高了 72 天，控制事件的速度提高了 84 天。与尚未采用统一平台的组织相比，他们还实现了 101% 的平均投资回报率 (ROI)，而后者仅为 28%。

正如攻击者在整个攻击面上进行操作一样，防御者也必须采取类似的统一方法。Palo Alto Networks 的 Cortex Cloud 增强了应用程序安全性，并改进了多云风险管理，同时实现了实时威胁防御和攻击缓解。

Cortex Cloud 通过弥合应用程序安全 (AppSec)、云安全 (CloudSec) 和安全运营中心 (SOC) 团队之间的差距来打破孤岛。通过统一数据、自动化工作流程和利用 AI 驱动的洞察力，它提高了运营效率，目标是降低风险、预防攻击和实时阻止威胁。
正如 Tager 所说，“Cortex Cloud 整合了来自原生扫描器、第三方发现和运行时的信息，使 AppSec 团队能够保护整个工程生态系统——包括代码、软件供应链和工具。AppSec 团队拥有所有必要的数据和上下文，可以快速采取行动并阻止风险。”

步入实时云安全的未来，并[详细了解 Cortex Cloud](https://www.paloaltonetworks.com/blog/2025/02/announcing-innovations-cortex-cloud/)。

[技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，即可观看我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)