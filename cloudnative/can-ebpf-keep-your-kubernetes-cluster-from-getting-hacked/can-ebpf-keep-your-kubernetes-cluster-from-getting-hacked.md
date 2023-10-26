<!--
# eBPF能够保护你的Kubernetes集群免受入侵吗？
https://cdn.thenewstack.io/media/2023/10/8c0fc474-fall-1024x700.jpg
Image from Evgeny Atamanenko on Shutterstock.
 -->


eBPF在Kubernetes安全领域作为一个不断演进的工作,其发展过程中还存在哪些不足？

译自 [Can eBPF Keep Your Kubernetes Cluster from Getting Hacked?](https://thenewstack.io/can-ebpf-keep-your-kubernetes-cluster-from-getting-hacked/) 。

eBPF(Extended Berkeley Packet Filter)近年来因其在安全、监控、可观察性等多个领域的应用而备受关注。它的核心功能是能够在内核空间运行,并可横向扩展到各种环境中,包括Kubernetes节点和集群,在这些环境中它以沙箱封闭的方式运行。eBPF的快速响应特性以及可横向扩展到高度分布式的Kubernetes环境的能力,使其非常适合被用于云原生安全工具和平台的构建。

但是,[需要注意的是](https://thenewstack.io/sell-bot-enterprise/),eBPF本身只是一个基础。工具和平台供应商[必须开发](https://thenewstack.io/cloud-foundry-summit-kubernetes-must-do-better-by-developers/)能够成功利用eBPF优势的Kubernetes安全工具和平台。简而言之,要将eBPF的能力发挥到最大效用,[还需要做大量工作](https://thenewstack.io/ebpf-put-the-kubernetes-data-plane-in-the-kernel/)。

[Gartner](https://www.gartner.com/en/documents/4597499)指出,大多数企业没有构建和集成基于eBPF功能所需的专业知识和技能。不过,Gartner也建议组织: “当规模、性能、可见性和安全是优先考虑的事项时,应该寻求基于eBPF的Kubernetes容器网络接口(CNI)解决方案。”

eBPF在Kubernetes(和其他环境)安全方面的具体[使用案例](https://thenewstack.io/groundcover-simplifying-observability-with-ebpf/)包括: 恶意软件和[入侵检测](https://thenewstack.io/what-ebpf-means-for-container-threat-detection/)、网络数据包路由和策略执行、资源利用监控以及其他与集群相关的监控。相关的工具和平台可以利用eBPF的[监控和跟踪特性来增强安全性](https://thenewstack.io/github-leverages-passkeys-to-enhance-user-security/),并以此为基础提供额外的安全功能。通过eBPF,这些工具可以提供可操作的洞察来检测威胁并实施安全策略,尤其适用于越来越流行的[Kubernetes环境](https://thenewstack.io/opsramp-brings-aiops-to-kubernetes-environments/)。这些可操作的洞察来自内核中的钩子,可以[横向扩展到整个网络栈](https://thenewstack.io/vmwares-tanzu-extends-across-all-security-layers-on-kubernetes/)。

此外,依赖eBPF的安全工具还应提供的功能包括:

- 减少误报数量
- 减少误报规模
- 根据严重程度更好地分析和排序威胁
- [减少应用程序在检测到安全漏洞和攻击时破坏的风险](https://thenewstack.io/reducing-security-vulnerabilities-in-kubernetes/)，自动更改代码以解决问题。
- 改善eBPF的资源需求问题

[开源社区和商业软件供应商](https://thenewstack.io/brandon-philips-man-behind-coreos/)正在积极解决这些问题。本文将深入探讨eBPF在Kubernetes安全方面[发展过程](https://thenewstack.io/pursuing-continuous-security-containers-devops/)中存在的不足。

## 虚报与误报

eBPF的[安全功能](https://thenewstack.io/serverless-security-suggestions-tips-for-securing-functions/)在于其在内核中运行，而不需要修改内核代码。它[像WebAssembly一样](https://thenewstack.io/why-webassembly-will-disrupt-the-operating-system/)，在封闭或受控的环境[中扩展了](https://thenewstack.io/managing-containers-across-distributed-resources/)程序的功能，使得程序的代码保持不可访问。构建在这些程序基础上的工具能够从内核发起，以在网络或计算环境的任何位置[检测或预防攻击](https://thenewstack.io/linux-kernel-5-10-introduces-static-calls-to-prevent-speculative-execution-attacks/)或潜在的代码漏洞。

然而，这种强大的功能伴随着一个缺点：可能会产生大量虚报。在[旨在提供全面安全解决方案的安全工具和平台中](https://thenewstack.io/10-criteria-to-evaluate-your-cloud-network-security-solution/)，虚报一直是一个常见问题。即使是经验丰富的安全专家，如果需要采用“[打地鼠](https://en.wikipedia.org/wiki/Whac-A-Mole)”的方式来修复漏洞，改善基础设施和策略管理的安全性，而没有自动分析和按威胁严重程度排名的支持，也将浪费时间和精力。

挑战在于以自动化的方式将漏洞、攻击和[安全问题](https://thenewstack.io/docker-addresses-more-security-issues-and-outlines-plugin-approach/)放入上下文中，并确定它们是否需要立即纠正。否则，大量虚报可能导致警报疲劳，这已经导致组织忽视了重要和有害的攻击和漏洞。

与此同时，恶意黑客不断探索方法来配置恶意软件，以规避eBPF[安全警报](https://thenewstack.io/automated-security-alert-remediation-a-closer-look/)。他们制作脚本并策划攻击，旨在规避基于eBPF的[安全警报](https://thenewstack.io/automated-security-alert-remediation-a-closer-look/)，这是一个真正的担忧。[用于增强监控和可观察性的安全工具](https://thenewstack.io/service-mesh-adds-security-observability-and-traffic-control-to-kubernetes/)并不是完美的。它们可能会出现漏报，通常是由于配置错误或对内核中的各种程序层和不同运行环境的可见性有限而造成的。重要的是要理解，eBPF无法用于监视所有代码。它无法访问和打开某些文件类型和库，这是漏报的一个明显原因。

为避免这些情况，全面而详细的准则将至关重要，以防止配置错误和误解。与eBPF技术本身一样，eBPF基于解决方案的文档和供应商支持对于坚固的安全性同样重要。

## 更精确的授权和访问

在使用eBPF进行Kubernetes的安全工具时，DevOps或[安全工程师](https://thenewstack.io/defining-dora-like-metrics-for-security-engineering/)通常需要花费大量时间手动研究配置。例如，当系统指示一个工作负载被配置为特权时，就会引发对其实际影响的疑问。研究人员和调查人员通常需要手动检查这些配置，以了解特权的使用是否妥当或存在问题。

eBPF为自动检查和缓解提供了基础，但在某些eBPF安全工具中，在[扫描后识别漏洞并提供修复措施](https://thenewstack.io/neuvector-expands-container-vulnerability-scanning-to-developers/)可能导致整个应用程序无法使用。考虑一个简单的配置错误：一个[具有暴露入口点的容器](https://thenewstack.io/containers-offer-good-protection-spectre-meltdown-attacks-know/)为攻击者提供了一个敞开的大门。自动响应很可能会完全关闭入口点。这可能会使依赖于与微服务进行互联或从[Kubernetes pod或集群](https://thenewstack.io/gremlin-sound-proofs-chaotic-pods-in-kubernetes-clusters/)外部进行系统调用的容器托管应用程序失效。更精确的方法将定义权限并实施授权和身份验证措施，但并非所有在eBPF上运行的自动化工具都已经实现了这一点。

## 新兴的改进

![](https://cdn.thenewstack.io/media/2023/10/2c64218f-image1a.jpg)

*ARMO平台*

好消息是，在[开源社区](https://thenewstack.io/tns-research-developing-methodology-analyzing-open-source-communities/)中已经充分认识到eBPF的不足之处。这些问题经常在会议和类似的活动中进行讨论，从而催生了解决方案和解决办法。

一个引人注目的开源解决方案是[CO-RE，“编译一次，随处运行”](https://libbpf.readthedocs.io/en/latest/libbpf_overview.html)，它可以最小化分布环境中eBPF工具的CPU和内存使用。CO-RE允许eBPF程序在不同内核上同时运行，因此[安全](https://thenewstack.io/4-ways-to-use-kernel-security-features-for-process-monitoring/)工具可以检查和与各种内核互动，而无需直接访问每个内核，这在资源方面可以实现显著的节省。CO-RE得到多个供应商和开源工具的支持，包括BumbleBee和[Kubescape，Kubernetes安全提供商ARMO引入了这些工具](https://github.com/kubescape/kubescape)。与此同时，Kubescape和BumbleBee的创建者使用CO-RE来分发其工具，而eBPF编译器和框架如[eBPF-GO](https://pkg.go.dev/github.com/cilium/ebpf)和[eBPF bcc](https://github.com/iovisor/bcc)支持供应商实施CO-RE。

还有新兴的[安全解决方案](https://thenewstack.io/beefing-up-your-cloud-providers-security/)使用eBPF，但提供了针对其弱点的补救措施或解决办法。一个合适的eBPF平台应该能够允许DevOps团队[监视Kubernetes集群中应该运行什么](https://thenewstack.io/using-prometheus-to-monitor-kubernetes-clusters-running-cloud-foundry/)，并在违反政策或检测到安全威胁时提供可操作的结果。依赖于CO-RE来优化资源，ARMO的Kubescape企业版本在Kubernetes的[DevOps环境中已经被证明是有效的](https://thenewstack.io/from-bystander-to-cto-my-five-year-journey-with-the-cloud-foundry-foundation/)。它用于对应用程序的潜在变更影响进行智能自动决策，以及对代码和策略变更进行[更具细微差异的安全](https://thenewstack.io/waf-securing-applications-at-the-edge/)修复。在我们之前的入口点示例中，Kubescape可以确定需要写入访问权限的特定文件夹并将其从其他文件夹中移除，从而减小[攻击面](https://thenewstack.io/from-war-to-web-security-protect-your-attack-surface-from-the-weakest-link/)而不破坏应用程序。

对于Kubescape而言，[云原生计算基金会的沙盒项目](https://thenewstack.io/tuf-is-first-security-project-to-graduate-the-cloud-native-computing-foundation/)覆盖了Kubernetes应用程序的生命周期和更新。这包括IDE、[CI/CD流水线和集群](https://thenewstack.io/codefresh-runner-run-ci-cd-pipelines-inside-a-kubernetes-cluster/)，用于风险分析、安全性、合规性、错误配置扫描和镜像扫描。[开源提供了](https://thenewstack.io/hyscale-offers-open-source-application-delivery-automation-tool-for-kubernetes/)网络策略和安全策略等加固建议。

Kubescape用于与[DevOps团队](https://thenewstack.io/survey-devops-teams-use-too-many-cloud-security-tools/)使用的平台上的必要工具清单进行集成，例如软件清单（SBOM）、签名扫描和策略控制。它从开发周期的一开始开始运行扫描，[跨越CI/CD](https://thenewstack.io/kasten-says-k10-v5-0-extends-reach-for-data-protection-across-ci-cd/)并在部署和集群管理过程中进行。

它用于查找和修复使用NSA-CISA、MITRE ATT&CK和[CIS基准](https://thenewstack.io/what-are-cis-benchmarks-in-cloud-security/)等框架的错误配置和漏洞。Kubescape在部署时扫描[YAML文件](https://roadmap.sh/videos/yaml-in-depth)、Helm Chart和集群。Kubescape还可以与Jenkins、CircleCI、[GitHub Actions](https://thenewstack.io/github-actions-design-flaw-leaves-security-hole-for-remote-code-execution/)、[GitLab](https://about.gitlab.com/?utm_content=inline-mention)、Visual Studio Code等IDE、Prometheus、Lens和[Docker](https://www.docker.com/?utm_content=inline-mention)等集成。

![](https://cdn.thenewstack.io/media/2023/10/2477272b-image3a.jpg)

*ARMO平台*

ARMO提供的最新eBPF功能之一适用于漏洞的相关性和优先级。相关性和优先级允许ARMO平台和Kubescape用户将属于未使用的[软件包](https://thenewstack.io/npm-spam-cleanup-briefly-zaps-legit-software-packages/)和组件的漏洞降低优先级。首先，通过降低较[不重要的漏洞的优先级](https://thenewstack.io/critical-vulnerability-found-in-docker-copy/)，用户可以集中精力解决对其运行集群构成更大威胁的漏洞。

根据ReveCom对[ARMO平台](https://cloud.armosec.io/account/sign-up)的初步测试，这家安全供应商在解决上述问题的能力方面提供了有力的论据，并将在其测试进展时提供更多见解。理想情况下，有一天，组织应该能够自动化其Kubernetes和其他环境的[安全扫描](https://thenewstack.io/verification-scans-or-automated-security-requirements-which-comes-first/)和保护，以便他们甚至不需要知道eBPF正在无处不在的运行，并且可以依赖它来确保其组织远离麻烦。
