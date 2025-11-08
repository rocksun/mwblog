在过去一年中，由于大型语言模型 (LLM) 规模和能力呈指数级增长，AI 推理对资源的需求显著增加。这些模型不仅规模更大，能力也更强，为从高级推理和指令遵循到高度专业化的特定领域任务等广泛应用提供支持。

随着这些工作负载的规模和战略重要性不断增长，Kubernetes 已成为部署推理服务的首选平台，提供了有效运营 [LLM](https://roadmap.sh/guides/introduction-to-llms) 所需的可伸缩性和生态系统成熟度。

[Kubernetes 非常适合推理工作负载](https://thenewstack.io/5-reasons-to-use-kubernetes-for-ai-inference/)，提供了一个灵活的平台，可用于模型容器化、根据需求进行伸缩以及集成遥测和可观测性工具。然而，随着组织在全球范围内扩展或需要更严格地控制成本和合规性，单集群部署可能不足以满足需求。

为了满足这些不断增长的需求，AI 服务提供商正在转向多集群推理，即将 LLM 工作负载分布到多个 Kubernetes 集群中。虽然多集群推理带来了区域冗余、数据本地性和更好的资源利用率等优势，但也引入了新的复杂性。

## **多集群 AI 推理面临的挑战**

*   **LLM 部署在集群间的一致性：** 一个核心挑战是确保模型部署在集群间保持一致。如果没有集中式管理框架，团队必须手动复制推理管道、管理配置漂移并确保更新在不停机的情况下传播——所有这些都易错且难以扩展。
*   **稀缺计算资源的有效利用：** AI 工作负载通常依赖于 GPU 或其他加速资源，这些资源昂贵且并非总能在每个位置或集群中可用。多集群部署需要智能机制来将工作负载放置在有合适的 GPU 计算和其他加速资源可用且不牺牲延迟或性能的位置。
*   **推理端点的性能和可用性：** 提供业务关键型 AI 服务意味着低延迟和高可用性是不可妥协的。推理端点必须快速响应、随需求扩展，并在集群或位置不可用时优雅地进行故障转移，同时在不同地理区域保持合规性和服务水平协议 (SLA)。

为了解决这些挑战，两个 [CNCF](https://cncf.io/?utm_content=inline+mention) 项目——[Kubernetes AI 工具链运算符 (KAITO)](https://kaito-project.netlify.app/) 和 [KubeFleet](https://kubefleet.dev/)——正在现代多集群 AI 世界中成为关键参与者。

## KAITO：优化和部署 AI 工作负载和资源

[KAITO](https://thenewstack.io/jumpstart-ai-workflows-with-kubernetes-ai-toolchain-operator/) 提供了一种管理 LLM 工作流的声明式机制。它支持：

*   使用 KAITO 工作区管理预构建模型和自带 (BYO) 模型。
*   针对各种 LLM 规模的自动资源调配。
*   多节点存储和计算优化。
*   开箱即用的遥测，提供推理健康状况和性能洞察。

通过将推理抽象为自定义 Kubernetes 资源，KAITO 确保模型在集群间一致部署，且所需人工干预最少。

## KubeFleet：跨集群的智能工作负载放置

[KubeFleet 是一个多集群工作负载编排器](https://thenewstack.io/kubefleet-the-future-of-multicluster-kubernetes-app-management/)，旨在促进 Kubernetes 上的工作负载放置。它可以评估集群属性，包括资源可用性，从而将部署放置在最适合的集群上。无论您是想优化 GPU 使用、确保地理冗余，还是[在测试、预生产和生产集群中无缝推广推理引擎更新](https://kubefleet.dev/docs/concepts/staged-update/)，KubeFleet 都能为您提供所需的控制。

## **结合 KAITO 和 KubeFleet，实现无缝多集群 AI**

[![](https://cdn.thenewstack.io/media/2025/10/982fb8bd-image1.png)](https://cdn.thenewstack.io/media/2025/10/982fb8bd-image1.png)

KAITO 确保集群级推理服务定义良好且一致，而 KubeFleet 则驱动全局放置策略：

*   KubeFleet 检测 GPU 计算资源何处可用，并根据成本、位置和资源可用性等关键属性确保集群选择最优。
*   KAITO 将模型部署到与 KubeFleet 放置策略匹配的集群中，确保模型放置在可以高效运行的位置。
*   KAITO 管理集群，处理模型准备、资源分配和可观测性。

这种分工实现了良好区分的架构：KubeFleet 专注于 AI 工作负载应去往何处，而 KAITO 则处理它们抵达后如何运行。

KubeFleet 和 KAITO 共同构成了一个强大的工具集，可用于在任意数量的集群中构建可伸缩且高效的 AI 推理管道。

## **结论**

多集群 AI 推理在弹性、性能和合规性方面具有明显优势，但前提是操作复杂性得到控制。KAITO 和 KubeFleet 通过以下方式帮助解决这种复杂性：

*   确保模型部署和生命周期管理的一致性。
*   优化跨集群的工作负载放置。
*   提供有效扩展 AI 推理所需的工具。

如果您正在 Kubernetes 上运行 AI 服务并寻求扩展，那么是时候探索 KAITO 和 KubeFleet 了。它们共同提供了一种简洁、声明式和智能的方法来实现大规模全局 AI 推理。

## **加入 KubeFleet 和 KAITO 社区**

KubeFleet 和 KAITO 处于解决多集群 AI 推理实际挑战的最前沿。随着这些工具的成熟，Kubernetes 上的 AI 未来取决于更广泛的云原生社区的见解、反馈和贡献。

无论您是平台工程师、机器学习 (ML) 从业者还是开源贡献者，我们都邀请您参与进来。帮助我们塑造路线图、贡献功能、分享用例，并协作构建跨集群更智能、更可扩展的 AI 基础设施。

立即开始：

*2025 年 KubeCon + CloudNativeCon 北美大会将于 11 月 10 日至 13 日在佐治亚州亚特兰大举行。* [*立即注册*](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/)*。*