<!--
title: 解决Kubernetes风险与漏洞的有效方法
cover: https://cdn.thenewstack.io/media/2024/02/63fe1fb6-address-kubernetes-risks-1024x576.jpg
-->

Kubernetes 威胁和风险的主因：配置错误与容器镜像漏洞。

> 译自 [How to Address Kubernetes Risks and Vulnerabilities Head-on](https://thenewstack.io/how-to-address-kubernetes-risks-and-vulnerabilities-head-on/)，作者 Giri Radhakrishnan 是 Tigera 公司的技术产品营销经理。他负责 Calico 安全解决方案的市场推广活动、产品定位和信息传递，重点关注零信任和容器安全。****

根据 [Gartner](https://www.gartner.com/en/documents/3988026) 的数据，到 2027 年，全球组织中超过 90% 将在生产环境中运行容器化应用程序。这一比例较 2021 年的不到 40% 有了显著增长。随着容器的广泛采用，[Kubernetes](https://thenewstack.io/kubernetes/) 仍然是主导的容器编排平台。

要实现 Kubernetes 的全部优势，就需要实施流程和解决方案来应对漏洞、威胁和风险，包括[人为错误](https://thenewstack.io/red-hat-human-error-a-leading-cause-of-kubernetes-security-mishaps/)（如配置错误）和容器镜像等固有漏洞引起的问题。[DevOps](https://roadmap.sh/devops) 和安全团队需要正确的解决方案来[减轻风险](https://thenewstack.io/container-security-101-a-guide-to-safe-and-efficient-operations/)，并享受 Kubernetes 的全部好处。

## 减轻配置错误的影响

尽管容器的采用已经起飞，但行业仍然缺乏熟练的 Kubernetes 专家。Kubernetes 是一个复杂的平台，没有正确技能集的人员会不经意间 —— 并频繁地 —— 出错，导致配置错误。

在 [2023 年的 Red Hat Kubernetes 安全状况报告](https://www.redhat.com/rhdc/managed-files/cl-state-kubernetes-security-report-262667-202304-en.pdf)中，超过 50% 的受访者表示他们担心配置错误和漏洞。而这样做是有道理的：攻击者获取公司数据、应用程序或代码的最简单方式就是通过配置错误的 Kubernetes 集群。恶意行为者只需一个小小的配置错误就能制造大乱。

根据 Gartner 的数据，到 2027 年，全球组织中超过 90% 将在生产环境中运行容器化应用程序。这与 2021 年不到 40% 的情况相比显著增加。随着容器的采用率飙升，Kubernetes 仍然是主导的容器编排平台。

实现 Kubernetes 的全部益处需要实施流程和解决方案来应对漏洞、威胁和风险，包括人为错误导致的问题，比如配置错误，以及来自容器镜像等固有漏洞。DevOps 和安全团队需要合适的解决方案来减轻风险，并享受 Kubernetes 的全部益处。

## 减轻配置错误的影响

尽管容器的采用已经起飞，但行业仍然缺乏熟练的 Kubernetes 专家。Kubernetes 是一个复杂的平台，没有正确技能的人员会不经意地 —— 也经常会 —— 出现创建配置错误的错误。

在 [Red Hat 2023 年 Kubernetes 安全状况报告](https://www.redhat.com/rhdc/managed-files/cl-state-kubernetes-security-report-262667-202304-en.pdf)中，超过 50% 的受访者表示他们担心配置错误和漏洞。有充分的理由担心：攻击者获取公司数据、应用程序或代码的最简单方式就是通过配置错误的 Kubernetes 集群。一个坏的行为者只需要一个小小的配置错误就能造成严重破坏。

有几种独立和平台工具可以通过查找和列出所有配置错误和漏洞来解决这个问题。随着资源之间的差距不断扩大和软件漏洞的增加，拥有一种预防策略至关重要。采取预防措施比对每个报告的配置错误或常见漏洞和曝光（CVE）做出反应更有效。

在实施强大的[微分段](https://thenewstack.io/zero-trust-vs-microsegmentation-establish-a-winning-strategy/)实践的基础上，可以限制恶意行为者利用配置错误造成的破坏程度。然而，微分段并不是一个标准化的过程；它在不同行业和使用案例中有所不同，这为广泛采用带来了挑战。

部署正确的针对 Kubernetes 的安全解决方案可以帮助组织轻松高效地实现微分段。例如，配备策略建议的软件会在一段时间内监控流量，然后推荐实现微分段的策略。开箱即用的解决方案消除了员工需要具备“从零开始”所需技能的需求。最终，微分段对于 Kubernetes 的大规模采用是必要的，强调了这种解决方案的重要性。

## 解决容器镜像中的漏洞

容器镜像中的现有漏洞或恶意软件也构成了重大风险。虽然容器镜像在 Kubernetes 部署中起着关键作用，但利用过时或有漏洞的镜像会引入安全风险。恶意行为者可以针对容器镜像中已知的漏洞，获取未经授权的访问权限或执行恶意代码。镜像中的漏洞可能来自开源库、基础镜像和其他第三方组件 —— 其中一些是已知的，而另一些尚未被发现。在构建阶段进行漏洞管理至关重要，以确定是否可以部署镜像。

在部署之前持续扫描软件中的漏洞和配置错误，并阻止不符合安全要求的部署是关键。通过扫描第一方和第三方镜像中的漏洞和配置错误，并使用工具从多个注册表中识别漏洞，例如国家标准与技术研究所的[国家漏洞数据库](https://www.nist.gov/programs-projects/national-vulnerability-database-nvd)，来评估容器和注册表镜像的漏洞是关键。持续监控镜像、工作负载和基础架构是否符合常见的配置安全标准（例如 CIS 基准）至关重要。这使组织能够满足内部和外部的合规标准，并快速检测和修复其环境中的配置错误，从而最终消除潜在的攻击向量。

## 缩小差距

实施良好的网络安全卫生习惯，建立强大的应用程序安全姿态，对于避免昂贵的 Kubernetes 问题至关重要。在遵循[零信任原则](https://thenewstack.io/what-is-zero-trust-security/)时，用户、应用程序和设备只允许与其角色内需要的资源进行通信和[访问](https://thenewstack.io/innovating-access-management-in-a-dynamic-way/)。这有助于在用户、应用程序和网络层面保护敏感数据，并且在恶意行为者获取访问权限时有助于防止数据被窃取或外泄。

采用正确的解决方案对抗和减轻配置错误的影响以及解决容器镜像中的漏洞至关重要。最终，这有助于避免违规行为和其他可能具有毁灭性后果的问题。

虽然可能无法解决所有问题并从环境中消除所有风险，但 DevOps 和安全团队可以通过遵循最佳实践并部署解决方案来关闭安全漏洞，以预防和减轻风险。

要了解更多关于 Kubernetes 和云原生生态系统的信息，请于 3 月 19 日至 22 日在巴黎参加 KubeCon + CloudNativeCon Europe。
