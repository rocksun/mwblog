
<!--
title: KubeCon欧洲大会上值得关注的工具和讲座
cover: https://cdn.thenewstack.io/media/2025/03/10287a30-conference12.jpeg
summary: KubeCon 欧洲站亮点抢先看！聚焦 Chainguard 的 Distroless 镜像、Crossplane 的多云管理、Kubescape 的安全扫描、vCluster 的集群隔离和 Devtron 的 DevOps 提速。更有 AI 议题： Kubernetes 中 AI 和 GPU 基准测试、Ollama 容器运行时。安全方面关注开源恶意软件，可观测性方面关注 eBPF 和 OpenTelemetry！
-->

KubeCon 欧洲站亮点抢先看！聚焦 Chainguard 的 Distroless 镜像、Crossplane 的多云管理、Kubescape 的安全扫描、vCluster 的集群隔离和 Devtron 的 DevOps 提速。更有 AI 议题： Kubernetes 中 AI 和 GPU 基准测试、Ollama 容器运行时。安全方面关注开源恶意软件，可观测性方面关注 eBPF 和 OpenTelemetry！

> 译自：[Tools and Talks Worth Checking Out at KubeCon Europe](https://thenewstack.io/tools-and-talks-worth-checking-out-at-kubecon-europe/)
> 
> 作者：Bhushan Nemade

您是否计划参加 2025 年 KubeCon + CloudNativeCon 欧洲站？活动即将到来，现在是规划您的参会体验的绝佳时机。这场为期四天的大型聚会汇集了最前沿的[云原生技术](https://thenewstack.io/cloud-native/)和专家主导的技术讲座，因此制定清晰的议程至关重要。

挑战是什么？如何在不感到不知所措的情况下，浏览 229 场会议、215 家供应商和无数的社交机会。让我来帮助您策划完美的行程，以便您最大限度地利用您的 KubeCon 体验。

以下是五个在云原生生态系统中掀起巨大波澜的项目，以及每个与会者都应关注的必参加的演讲。

## 值得关注的项目

### Chainguard

如果您已经花费无数时间尝试修补和分类容器镜像中的 CVE，以保护您的系统安全，那么您需要查看此工具。

在软件供应链攻击日益猖獗的时代，[Chainguard](https://thenewstack.io/chainguard-launches-cpu-gpu-containers-for-ai-frameworks/) 正在重新定义安全性，它专注于最小化、强化和持续验证的容器镜像。通过在漏洞到达生产环境之前消除它们，Chainguard 帮助组织提高其安全态势，而不会影响效率。

Chainguard 通过以下几种关键方法来增强安全性：

- **无发行版容器镜像 (Distroless container images)**——这些最小镜像仅包含运行应用程序所需的组件，从而消除了可能引入漏洞的不必要的软件包、shell 和实用程序。
- **持续验证 (Continuous verification)**——自动化扫描和证明系统以加密方式验证容器镜像在整个开发生命周期中的完整性和来源。
- **软件物料清单 (SBOM) 集成 (Software bills of materials (SBOM) integration)**——Chainguard 为其镜像生成并维护详细的 SBOM，从而提供有关所有组件和依赖项的透明度。
- **漏洞消除 (Vulnerability elimination)**——它不仅仅是检测漏洞，而是专注于通过仔细管理依赖项和维护严格的更新策略，从源头消除它们。

Chainguard 提供[公开可用的容器镜像](https://images.chainguard.dev/directory/?category=all)，您可以探索和使用它们，从而获得安全、最小和持续验证方法的实践经验。

### Crossplane

[Crossplane](https://thenewstack.io/kubecon-24-crossplane-a-developer-friendly-control-plane/) 通过将 Kubernetes 的声明式资源模型引入多云环境，从而改变了组织管理其云基础设施的方式。这个强大的工具正在通过以下方式重塑基础设施管理：

- **通过 Kubernetes API 实现基础设施即代码 (Infrastructure as Code via Kubernetes API)**——Crossplane 允许团队使用与应用程序相同的 Kubernetes API 和工具来配置和管理云资源，从而无需处理多个云提供商的 CLI 和控制台。
- **可组合的基础设施抽象 (Composable infrastructure abstractions)**——它使平台团队能够创建自定义的、特定于组织的抽象，从而隐藏特定于云的实现细节，从而使开发人员能够自助服务基础设施，而无需了解底层云提供商。
- **多云资源编排 (Multicloud resource orchestration)**——Crossplane 提供了一个统一的控制平面，用于通过一致的 Kubernetes 自定义资源定义 (CRD) 管理跨 AWS、Azure、GCP 和其他云提供商的资源。

### Kubescape

[Kubescape](https://thenewstack.io/kubescape-achieves-cncf-incubation-status/) 正在通过其由 Armo 构建的全面开源安全平台来彻底改变 Kubernetes 安全性，该平台旨在识别和修复整个 Kubernetes 堆栈中的风险。在容器安全漏洞日益普遍的环境中，Kubescape 以以下优势脱颖而出：

- **全面的安全扫描 (Comprehensive security scanning)**——它针对包括 NSA-CISA、MITRE ATT&CK 和 CIS Benchmarks 在内的多个框架执行扫描，从而全面了解从集群配置到运行时行为的安全态势。
- **基于风险的优先级排序 (Risk-based prioritization)**——Kubescape 分析您特定上下文中的漏洞，计算风险评分，以帮助团队专注于最重要的事情，而不是淹没在警报中。
- **DevSecOps 集成 (DevSecOps integration)**——它无缝集成到 CI/CD 管道和现有工作流程中，并支持 CLI、WebUI 和 Kubernetes 原生组件，从而使安全性能够在开发过程中左移。
- **合规性自动化 (Compliance automation)**——自动生成合规性报告并提供补救指南，从而大大减少了维护法规遵从性所需的手动工作。

### vCluster

[vCluster](https://thenewstack.io/vcluster-to-the-rescue/) 正在通过引入集群隔离和资源优化的革命性方法来改变 Kubernetes 中的多租户。在传统命名空间隔离不足的环境中，vCluster 实现了：

*   **虚拟 Kubernetes 集群** — vCluster 创建功能齐全的 Kubernetes 集群，这些集群在另一个 Kubernetes 集群的命名空间内运行，提供真正的隔离，而无需管理单独物理集群的运营开销。
*   **资源优化** — 通过在共享基础设施上运行虚拟集群，与专用集群相比，vCluster 显着降低了资源消耗，从而降低了云成本，同时保持了隔离。
*   **环境标准化** — 开发、暂存和生产环境可以保持一致的配置，同时作为虚拟集群运行，从而消除了“在我的机器上可以工作”的问题。
*   **团队独立性** — 开发团队可以完全管理自己的虚拟集群，而不会影响其他团队或需要对底层主机集群的特权访问。

vCluster 解决了在多租户环境中提供强大隔离的关键挑战，而无需管理多个物理集群的过高成本和运营复杂性，使其成为希望优化其 Kubernetes 基础设施，同时保持开发团队的安全性和自主性的组织的理想选择。

### Devtron

“当 AI 使您的开发人员速度提高两倍时，您的 Kubernetes 不应拖他们的后腿。”

[Devtron](https://github.com/devtron-labs/devtron) 是一个开源应用程序生命周期管理平台，使团队能够更快地行动，而无需参与 Kubernetes 的复杂性。[Devtron](https://devtron.ai/) 将 Kubernetes 和相关操作编排到一个直观的 UI 中，开发人员和 DevOps 团队可以从中加速他们的 Kubernetes 操作。

Devtron 使管理 Kubernetes 变得更容易，并通过以下功能彻底改变了它们的管理方式：

*   **自动化且可靠的 CI/CD** — Devtron 带有集成的、支持 GitOps 的 CI/CD 工作流程，可确保在目标环境中进行精确的功能部署。诸如[部署窗口](https://devtron.ai/blog/execute-controlled-deployments-in-kubernetes-environments/)、预部署批准和应用程序推广等关键组件增强了可靠性，同时减少了工具蔓延。这为开发人员提供了一条简化的部署路径。
*   **简化且细粒度的 RBAC** — Devtron 通过其直观的 UI 解决了 Kubernetes 基于角色的访问控制 (RBAC) 配置挑战。该平台提供简化但功能强大的 [RBAC 控制](https://devtron.ai/blog/sso-and-rbac-a-secure-access-strategy-for-your-kubernetes/)，从而可以对特定集群中特定 Pod 进行细粒度的用户访问。
*   **多集群管理** — 轻松地将多个 Kubernetes 集群加入到单个 Devtron 实例，并通过统一的仪表板对其进行管理。这消除了通过 kubectl 命令管理集群的复杂性，并提供了清晰的[集群操作可见性](https://devtron.ai/blog/managing-kubernetes-resources-across-multiple-clusters/)。
*   **策略和治理** — 该平台包括强大的治理功能，例如审批策略、配置锁定、内置基础设施控制以及全面的合规性和审计日志记录功能。

有了这些，Devtron 确保您的基于基础设施的操作与 AI 加速开发的速度和效率保持同步。

## 值得参加的热门议题和演讲

## AI 和机器学习

“[Kubernetes 中 AI 和 GPU 工作负载基准测试实用指南”](https://kccnceu2025.sched.com/event/1tx7Q/a-practical-guide-to-benchmarking-ai-and-gpu-workloads-in-kubernetes-yuan-chen-nvidia-chen-wang-ibm-research?iframe=no&w=100%&sidebar=yes&bg=no) — Yuan Chen, NVIDIA, 和 Chen Wang, IBM Research

本次演讲涵盖了一系列用例的基准测试，包括模型服务、模型训练和 GPU 压力测试，使用的工具包括 NVIDIA Triton Inference Server；fmperf，一个用于基准测试 LLM 服务性能的开源工具；MLPerf，一个用于比较机器学习系统性能的开放基准测试套件；GPUStressTest；gpu-burn；和 cuda 基准测试。本次演讲还将介绍 GPU 监控和负载生成工具。

“[在 Kubernetes 中编排 AI 模型：将 Ollama 部署为原生容器运行时”](https://kccnceu2025.sched.com/event/1tx97/orchestrating-ai-models-in-kubernetes-deploying-ollama-as-a-native-container-runtime-samuel-veloso-cast-ai-lucas-fernandez-red-hat?iframe=no&w=100%&sidebar=yes&bg=no) — Samuel Veloso, Cast AI, 和 Lucas Fernández, Red Hat

在本次演讲中，您将了解到与 Ollama 集成的自定义容器运行时如何简化 Kubernetes 中的 AI 模型部署。它将探讨这种方法如何简化操作、提高效率并消除传统模型服务解决方案的复杂性。通过实际示例和现场演示，您将深入了解如何使用这种创新的运行时，以便在 Kubernetes 中轻松地以原生方式运行开源 AI 模型。

## 安全

“[开源恶意软件还是漏洞？哲学辩论以及如何缓解](https://kccnceu2025.sched.com/#)” — Brian Fox, Sonatype; Madelein van der Hout, Forrester Research Inc.; Santiago Torres-Arias, Purdue University

本次演讲将阐明开源恶意软件日益增长的威胁，区分它与传统漏洞，并探讨为什么它经常无法被传统的安全工具检测到。一个由研究人员、分析师和行业资深人士组成的专家小组将分解真实世界的例子，讨论保护开源软件的挑战，并提供可操作的风险缓解策略。与会者将更深入地了解不断发展的安全形势，并采取实际步骤来保护他们的软件供应链。

## 可观测性

“[一个典范路径：利用 eBPF 和 OpenTelemetry 自动检测 Exemplar](https://kccnceu2025.sched.com/event/1txEI/an-exemplary-path-leveraging-ebpfs-and-opentelemetry-to-auto-instrument-for-exemplars-charlie-le-kruthika-prasanna-simha-apple?iframe=no&w=100%&sidebar=yes&bg=no)” — Charlie Le and Kruthika Prasanna Simha, Apple

本次演讲将探讨 eBPF 和 OpenTelemetry 如何协同工作，以自动化生成 exemplar，而无需手动检测。您将了解 eBPF 的内核内聚合功能如何实现实时指标和跟踪收集，并与 OpenTelemetry 无缝集成以增强可观测性。

“**缺失的指标：测量云原生系统中的内存干扰**“

— Jonathan Perry, PerfPod

本次会议介绍了检测内存干扰的最新研究，包括来自 Google、Alibaba 和 Meta 生产环境的发现。我们将探讨现代 CPU 性能计数器如何识别嘈杂的邻居，检查触发干扰的真实模式（如垃圾回收和容器镜像解压缩），并演示在 Kubernetes 环境中测量这些影响的实用方法。