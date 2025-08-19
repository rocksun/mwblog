如果你想轻松地在云之间迁移你的 AI 推理和建模工作负载，你需要 Kubernetes 提供什么？

[Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) (CNCF) 想知道。

CNCF 正在[创建](https://www.cncf.io/blog/2025/08/01/help-us-build-the-kubernetes-conformance-for-ai/)一个程序，用于认证可以运行特定类型 AI 工作负载的 Kubernetes 发行版。但它首先需要一套要求和建议。他们正在寻求你的帮助。

这个想法是复制 CNCF 在 [Kubernetes 一致性指南](https://www.cncf.io/training/certification/software-conformance/)方面所做的工作。到目前为止，已有 100 多个 K8s 发行版[名列其中](https://www.cncf.io/training/certification/software-conformance/#logos)。

在符合 Kubernetes 一致性的发行版上运行的工作负载，无论是在公共云还是私有云上，都可以在不进行任何更改的情况下迁移到另一个符合一致性的环境中。

“我们希望对 AI 工作负载做同样的事情，”CNCF 首席技术官 [Chris Aniszczyk](https://www.linkedin.com/in/caniszczyk/) 在 6 月的 [KubeCon + CloudNativeCon China](https://www.youtube.com/watch?v=etvB-QGFtns&list=PLj6h78yzYM2P1xtALqTcCmRAa6142uERl&t=308s) 上说。这将需要 Kubernetes 集群*必须*提供的一组功能、API 和配置（在常规一致性之上）。

Aniszczyk 在 [KubeCon + CloudNativeCon Japan](https://www.youtube.com/watch?v=mh7Cmei3pmI&list=PLj6h78yzYM2PsNdcBGWR_mVN-SRLQl6KM&t=405s) 上进一步解释说，这个想法是在不同环境之间提供“基线兼容性”。

他说，当“CNCF 成立时，整个想法是构建可以在每个云上运行的基础设施”，无论是公共云还是私有云。

如何定义 AI 需求的问题正在 [SIG-Architecture](https://github.com/kubernetes/community/tree/master/sig-architecture) 中讨论，该小组内为此任务新成立了一个工作组。

该工作组的 [GitHub 页面](https://github.com/kubernetes/community/tree/master/wg-ai-conformance) 解释说，该小组的目标是“定义一套标准化的功能、API 和配置，Kubernetes 集群必须提供这些功能才能可靠且高效地运行 AI/ML [机器学习] 工作负载。”

这项工作还将为更广泛的“云原生 AI 一致性”定义奠定基础，包括云原生计算的其他方面，例如遥测、存储和安全性。

[Google](https://cloud.google.com/?utm_content=inline+mention)、[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 和其他商业公司正在为该项目提供资源。

[![screenshot](https://cdn.thenewstack.io/media/2025/08/6701237c-kubeconform-01.jpg)](https://cdn.thenewstack.io/media/2025/08/6701237c-kubeconform-01.jpg)

## 商品化 Kubernetes

在[早期的虚拟讨论](https://docs.google.com/document/d/1hXoSdh9FEs13Yde8DivCYjjXyxa7j4J8erjZPEGWuzc/edit?tab=t.0#heading=h.9j85ih1tpsk)中，总体目标是使 AI/ML 工作负载平台尽可能地商品化。一位工作组成员写道：“希望尽量减少运行 AI/ML 工作负载所需的 DIY 和特定于框架的补丁数量。”

该小组确定了三种非常适合 Kubernetes 的工作负载类型：

*   **大规模训练和微调：** 关键平台要求包括访问高性能加速器、高吞吐量和拓扑感知网络、组调度和对数据的可扩展访问。
*   **高性能推理：** 关键平台要求包括访问加速器、高级流量管理和用于监视延迟和吞吐量的标准化指标。
*   **MLOps 管道：** 关键平台要求包括强大的批处理作业系统、用于管理资源争用的排队系统、对对象存储和模型注册表等其他服务的安全访问以及可靠的 CRD/Operator 支持。

该草案还列出了一组建议的做法（“应该”）和明确的要求（“必须”），其中许多是基于最近为 AI 人群提供的 [Kubernetes 增强功能](https://thenewstack.io/kubernetes-v1-33-advances-in-ai-security-and-the-enterprise/)。

例如，符合 Kubernetes AI 的系统必须支持 [动态资源分配](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/) (DRA)，该功能将在本月晚些时候发布的 Kubernetes 1.34 版本中完全可用。DRA 提供更灵活和细粒度的资源控制，例如 [指定 GPU](https://thenewstack.io/nvidia-h200-gpus-crush-mlperfs-llm-inferencing-benchmark/) 的能力。

它还必须支持 [Kubernetes Gateway API Inference 扩展](https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/)，该扩展 [指定了 LLM 的流量路由模式](https://thenewstack.io/google-kubernetes-engine-customized-for-faster-ai-work/)。

集群自动缩放器必须能够使用请求的特定加速器类型来向上/向下缩放节点组。

等等……

## 认证计划

一个独立的、尚未命名的团体将负责认证。

认证计划将有一个公共网站，列出所有通过一致性测试的 Kubernetes 发行版。它们将每年进行测试。每个发行版都将有一个已完成的 [基于 YAML 的](https://thenewstack.io/kubernetes-is-getting-a-better-yaml/) 一致性清单。

CNCF 计划在今年 11 月 10 日至 13 日在亚特兰大举行的 [2025 年北美 KubeCon+CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/?utm_source=the+new+stack&utm_medium=referral&utm_campaign=event) 上公布最终的一致性指南。