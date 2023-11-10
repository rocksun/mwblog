<!-- 
# Kubescape 3.0：使用eBPF实现安全的经验总结
https://cdn.thenewstack.io/media/2023/11/4a21b028-ebpf-copy-1024x532.png
 -->

ARMO 公司在 KubeCon 北美 2023 上发布了 Kubescape 3.0。

译自 [Kubescape 3.0: The Result of Lessons Learned with eBPF for Security ](https://thenewstack.io/kubescape-3-0-the-result-of-lessons-learned-with-ebpf-for-security/) 。

[eBPF(Extended Berkeley Packet Filter)](https://ebpf.io/)的炒作周期大幅上升，很大程度上是因为它在帮助保护 Kubernetes 集群上运行的应用程序的能力。通过监控和可观测性功能，eBFP 已经被证明可以扩展其钩子，以实现从 Linux 内核扩展到高度分布式 Kubernetes 环境运行时的安全目的。

开源社区及其创始人 [ARMO](https://www.armosec.io/) 公司正在积极开发的一个项目是 Kubescape。将 eBPF 的安全范围扩展到项目的整体理念中。自 2021 年创建以来，这个[云原生基金会](https://cncf.io/?utm_content=inline-mention)沙箱项目已经从 2236 个拉取请求和超过 9000 个 star 中获益。

ARMO 在推出 [Kubescape](https://thenewstack.io/kubescape-a-cncf-sandbox-platform-for-all-kubernetes-security/) 3.0 时[讨论](https://thenewstack.io/armo-misconfiguration-is-number-1-kubernetes-security-risk/)了通过嵌入式 eBPF 安全钩子从运行时库扫描、CI/CD 和部署后覆盖安全需求的雄心，以在 [KubeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 上介绍。该版本引出一个问题，即利用 [eBPF](https://thenewstack.io/how-ebpf-streamlines-the-service-mesh/) 为 DevOps(或者如果您愿意，SecOps)实现运行时的全面安全性有多可行。

当 Kubescape 于 2021 年首次推出时，它是第一个支持 [NSA-CISA Kubernetes 安全指南](https://thenewstack.io/why-does-the-nsa-care-about-the-software-supply-chain/)的开源安全扫描程序。Kubescape 3.0 代表了对原始扫描程序进行的一系列更改，增加了功能并关注用户体验，Kubernetes 安全提供商 ARMO 的 CTO 兼联合创始人 [Benyamin Hirschberg](https://www.linkedin.com/in/ben-hirschberg-66141890/?originalSubdomain=il) 表示。“Kubescape 3.0 的扫描结果是一个开始而不是结束。每个结果都提供了额外的上下文，” Hirschberg说。“因此，消除了大量与安全扫描结果的进一步分析相关的苦差事，并为用户提供了有关扫描后继续安全之旅的许多提示。”

![](https://cdn.thenewstack.io/media/2023/11/e7b73c63-capture-decran-2023-11-07-180526.png)

Kubescape 涵盖了 Kubernetes 应用程序的生命周期及其更新，包括 IDE、CI/CD 流水线和集群，用于风险分析、安全性、合规性、配置错误扫描和镜像扫描。网络策略和安全策略等强化建议也作为开源产品的一部分提供。

## 集成、发现、修复

Kubescape 用于将 DevOps 团队使用的必要工具与平台集成，比如软件清单(SBOM)、签名扫描和策略控制。它从开发周期一开始就启动扫描，并扩展到 CI/CD 中，贯穿部署和集群管理整个过程。

它用于发现和修复错误配置和漏洞，使用像 NSA-CISA、MITRE ATT&CK 和 CIS 基准等框架。Kubescape 在部署时扫描 YAML 文件、Helm Chart 和集群。Kubescape 也可以与 Jenkins、CircleCI、GitHub Actions、[GitLab](https://about.gitlab.com/?utm_content=inline-mention)、IDE(如 Visual Studio Code)、Prometheus、Lens 和 [Docker](https://www.docker.com/?utm_content=inline-mention) 集成。

ARMO 提供的一个关键的 eBPF 功能是漏洞相关性和优先级评估。相关性和优先级允许 ARMO 平台和 Kubescape 用户降低未使用的软件包和组件中的漏洞优先级。通过先降低不太关键漏洞的优先级，用户可以专注于解决对运行集群构成更大威胁的漏洞。

## 新功能

[Kubescape 3.0](https://kubescape.io/blog/2023/09/19/introducing-kubescape-3/) 的新功能包括:

- **将合规性和容器扫描结果作为 Kubernetes API 对象中的资源存储:** 这使查看和管理扫描结果以及将 Kubescape 与其他 Kubernetes 工具和工作流集成更容易。
- **从命令行界面扫描容器镜像中的漏洞:** 这样可以通过在将镜像部署到生产环境之前扫描镜像来实现向左移动安全性，并尽早识别和修复漏洞。
- **报告集群中所有镜像的漏洞:** 这提供了对集群所有镜像的安全状况全面视图，并帮助组织确定补救工作优先级。
- **新的安全扫描概览，帮助建立集群安全基线:** 此扫描可识别集群中的关键安全风险，并帮助组织提高整体安全态势。
- **突出高风险工作负载，即如果被入侵可能造成最严重损害的工作负载:** 这帮助组织将安全重心放在构成最大风险的工作负载上。
- **改进的显示输出:** Kubescape 3.0 具有新的、改进的显示输出，使读取和理解扫描结果更容易。
- **新的基于功能的 Helm Chart:** 这简化了 Kubescape 的安装和配置。
- **每个工作负载、每个命名空间和每个集群的 Prometheus 指标:** 这使得可以随时间监控工作负载、命名空间和集群的安全状况。
- **通过 Prometheus Alertmanager 进行警报:** 当安全问题超过可配置阈值时，可以接收警报。
- **将数据发送到集群外部的 Kubescape 提供商:** 这使得可以将安全信息存储在其收集的集群外，以防攻击时被更改。除了原生的 ARMO、[Backstage](https://thenewstack.io/red-hat-readies-developer-hub-a-backstage-enterprise-distribution/) 和 Lens 集成外，还提供了操作 Kubescape 兼容服务的良好文档的 API。

在 GitHub 的背景下，一项搜索显示目前有 492 个开源仓库与“Kubernetes 安全”相关，总共有 265，449 个星标，企业管理联盟分析师 [Torsten Volk](https://www.linkedin.com/in/torstenvolk/) 表示。图表显示 Cilium、Trivy、Authelia、Teleport、Kubescape、Linkerd2 和 Falco 是拥有最多星标的项目。“KubeScape 的重点是将安全扫描和风险管理直接嵌入 Kubernetes 集群，以便开发人员和 DevOps 工程师可以防止配置错误或使用容易受攻击的容器镜像。基于开源社区定义的最新和最佳实践，通过将 Kubernetes 安全性烘焙到 Kubernetes API 中并与 IDE 和 DevOps 流水线集成来简化 Kubernetes 安全性，这是一个激动人心的价值主张，”Volk 说。

虽然 KubeScape 专注于持续优化 Kubernetes 安全态势，但 Cilium 涵盖 API 和内核层面的网络安全，Linkerd 保护服务网格，Falco 处理运行时安全，而 Authelia 在认证层面提供安全性，Volk 说。Trivy 是与 KubeScape 最相似的开源安全平台，但专注于镜像扫描，而 KubeScape 专注于根据 NSA、CISA 等行业标准从内部强化 Kubernetes 集群，Volk 说。

预计 3.1 版将在年底推出集群内 Web UI。预计 2024 年第二季度发布的 4.0 版将通过添加更多运行时功能将 Kubescape 扩展为一个完整的 Kubernetes 原生应用程序保护平台(KNAPP)。

使用 eBPF 的正确平台应该能够允许 DevOps 团队监控 Kubernetes 集群中应该运行的内容，并在违反策略或检测到安全威胁时提供可操作的结果。依靠 CO-RE 优化资源，ARMO 的 Kubescape 企业版已在 Kubernetes 上的 DevOps 环境中证明行之有效。在那里，它用于根据评估应用程序更改的潜在影响和对代码和策略更改进行更精细的安全修复的能力，做出有关访问 pod 和集群的更明智的自动决策。在我们之前的 ingress 点示例中，Kubescape 可以针对需要写访问权限的特定文件夹并从其他文件夹中删除它们，从而缩小攻击面而不是中断应用程序。

Kubescape 3.0 也展示了如何使用诸如利用 eBPF 安全钩子功能的工具来补充 Kubernetes 安全中 AI 和 LLMs 的使用。“根据硬编码逻辑或 AI 模型自动化访问控制是一个令人兴奋和稍稍可怕的视角。一方面，Kubernetes 集群中存在更少的人为错误或通常糟糕的配置空间，但另一方面，人类需要能够轻松理解和监控所有自动化配置工作流程，”Volk说。“很高兴看到 Kubescape 接受这个挑战，因为解决它将实现随应用环境扩展的安全性。”
