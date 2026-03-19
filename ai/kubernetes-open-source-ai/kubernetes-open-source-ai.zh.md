在2026年国际消费电子展上，NVIDIA 首席执行官 Jensen Huang 提出，当开放式创新在每个公司和每个行业中被激活时，人工智能将普及。如果这就是未来（DeepSeek、Llama、Mistral 以及更广泛的开放模型生态系统的发展轨迹表明确实如此），那么运行人工智能的基础设施也不能是专有的。

> “随着人工智能成为计算资源的主要消费者，社区正在弥合‘可能’与‘一流’之间的差距。”

Kubernetes 运行人工智能工作负载的时间几乎和它存在的时间一样长。它最初并非为人工智能而设计，但人工智能团队总是能找到方法来运行 GPU 工作负载，即使核心 API 对 GPU 的理解仅限于简单的整数计数。随着人工智能成为计算资源的主要消费者，社区正在弥合“可能”与“一流”之间的差距。以下是这项工作的进展。

## 描述硬件

原始设备插件 API 在你只需要可用 GPU 数量时可以正常工作。当[工作负载需要共享 GPU 的特定分区](https://thenewstack.io/kubernetes-primer-dynamic-resource-allocation-dra-for-gpu-workloads/)、多个 pod 需要共享单个设备，或者训练作业需要跨节点的高速互连时，它就会失效。

[动态资源分配 (DRA)](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/) 改变了这一点。供应商通过 ResourceSlices 暴露结构化的设备信息，工作负载声明 ResourceClaims 来描述它们的需求。调度器将声明与设备匹配，考虑属性、共享策略和拓扑。DRA 为我们提供了基本要素。它在 Kubernetes 1.34 中达到通用可用性 (GA)，而有效使用这些基本要素的策略是下一个前沿领域。

## 调度人工智能工作负载

分布式训练和推理作业需要批处理调度，即所有 pod 要么一起启动，要么都不启动，以防止资源死锁。但部署也取决于对集群物理拓扑的理解：将 pod 部署到共享网络主干或高速互连域的节点上，可以显著减少通信开销。

[KAI Scheduler](https://github.com/NVIDIA/KAI-Scheduler) 已被 CNCF 沙箱接受，它提供支持 DRA 的批处理调度、带有公平性策略的层次化队列，以及针对大规模集群的拓扑感知部署。[Topograph](https://github.com/NVIDIA/topograph) 发现并暴露底层网络拓扑，使调度器能够在云端和本地环境中做出更智能的部署决策。更广泛社区中关于工作负载 API 的讨论正在将这些调度模式进一步推向上游。

## 服务工作负载

推理是生产 GPU 周期日益集中的地方，也是 [Kubernetes](https://thenewstack.io/ai-kubernetes-observability-practices/) 假设失效最严重的地方。水平 Pod 自动扩缩器基于 CPU 和内存进行扩缩。大语言模型 (LLM) 推理需要根据 KV 缓存利用率、请求队列深度和首次生成 token 时间进行扩缩。基于错误的指标进行扩缩意味着浪费 GPU 时间或未能达到延迟目标。

[Inference Gateway](https://github.com/kubernetes-sigs/gateway-api-inference-extension) 使用模型感知路由扩展了 Gateway API。[llm-d](https://github.com/llm-d/llm-d) 和 [Dynamo](https://github.com/ai-dynamo/dynamo) 社区正在合作开发具有前缀缓存感知路由和解耦预填充/解码的分布式服务，产生了全新的调度和自动扩缩需求。基础构建块正在出现，但将它们联系在一起的抽象层可能涵盖 Kubernetes 原生功能和更高级别的控制平面。

下一波浪潮已经到来。团队开始将自主 AI 代理作为容器化工作负载在 Kubernetes 上进行编排，增加了又一类需要管理的计算资源。

> “开源人工智能并不仅仅停留在模型权重上。基础设施也需要开源，社区已准备好构建它。”

[Kubernetes 人工智能合规性计划](https://www.cncf.io/announcements/2025/11/11/cncf-launches-certified-kubernetes-ai-conformance-program-to-standardize-ai-workloads-on-kubernetes/) 于 2025 年北美 KubeCon 上启动，有十二家认证供应商，这是一个开始。但解决这些问题的模式存在于所有大规模运行人工智能的组织中，即使实现方式不同。这些知识目前被锁定在各个公司内部。它应该属于上游，属于开放社区，这样才能发挥复合效应。

开源人工智能并不仅仅停留在模型权重上。基础设施也需要开源，社区已准备好构建它。

*本客座专栏发布于 [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 之前，这是云原生计算基金会的旗舰会议，将于2026年3月23日至26日在荷兰阿姆斯特丹汇集来自领先开源和云原生社区的采用者和技术专家。*