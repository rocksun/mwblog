<!-- 
# 具有 GPU 工作节点的托管 K8s 可加速 AI/ML 推理
https://cdn.thenewstack.io/media/2023/10/fde8d6af-image2-1024x569.png
 -->

拥有 GPU 工作节点对于提高 AI/ML 工作负载的效率至关重要。同时，采用托管的 Kubernetes 方式也会给 GPU 加速带来独特的好处。

译自 [Managed K8s with GPU Worker Nodes for Faster AI/ML Inference](https://thenewstack.io/managed-k8s-with-gpu-worker-nodes-for-faster-ai-ml-inference/) 。

目前已有 [48% 的组织](https://www.redhat.com/en/resources/state-of-workloads-deployment-infographic)采用 Kubernetes 运行 AI/ML 工作负载，而这类工作负载的需求也推动了 Kubernetes 的使用。Paperdata 认为运行在 Kubernetes 上的 AI/ML 工作负载数量增长证明了 [Kubernetes 的成熟](https://www.pepperdata.com/2232023-pepperdata-survey-uncovers-state-kubernetes-2023-cloud-cost-remediation)。让我们看看这一趋势背后的关键技术原因，以及 AI/ML 工作负载如何从托管 K8s 集群的 GPU 工作节点获益，并考量 GPU 制造商和调度等注意事项。

## Kubernetes 适合 AI/ML 的原因

Kubernetes 在 AI/ML 领域之所以流行且高效，关键在于其多种功能:

*   **可扩展性:** K8s 实现了 AI/ML 工作负载的无缝、按需扩展。这对推理工作负载尤为关键，因为相比训练工作，它们的资源利用更加动态。推理 AI/ML 工作负载计算需求可能很大，并需要根据处理数据量频繁地扩展或缩减。

*   **自动调度:** 自动调度 AI/ML 工作负载可降低 MLOps 团队的运维工作，还可通过确保调度到所需资源节点来提升 AI/ML 应用性能。
*   **资源利用优化:** K8s 可帮助优化 AI/ML 工作的物理资源利用。它可根据需要动态、自动分配 CPU、GPU 和 RAM 资源。由于 AI/ML 对资源需求量大，这对潜在降低成本至关重要。
*   **灵活性:** 基于 K8s，可将 AI/ML 工作负载部署到多个基础架构，包括内部部署、公有云和边缘云。这使 [kubernetes](https://roadmap.sh/kubernetes) 可为需要混合或多云部署的组织提供 AI/ML 解决方案。
*   **可移植性:** 基于 Kubernetes 的 AI/ML 应用可轻松在不同环境间迁移。这对于混合基础架构中的 AI/ML 部署和管理至关重要。

## 使用案例

以下几个例子展示了公司如何在 AI/ML 项目中使用 Kubernetes(K8s):

- OpenAI 是 K8s 的[早期使用者](https://kubernetes.io/case-studies/openai/)。2017 年，该公司就在 K8s 集群上运行机器学习实验。借助 K8s 的自动扩缩器，OpenAI 能在几天内部署此类项目，并在一两周内扩展到数百个 GPU。如果没有 Kubernetes 自动扩缩器，这样的过程需要数月时间。因此，OpenAI 的 AI 实验次数增加了 10 倍。2021 年，公司将 K8s 基础设施扩展到了 [7,500 个节点](https://openai.com/research/scaling-kubernetes-to-7500-nodes)，用于大型 ML 模型，如 GPT-3、DALL-E 和 CLIP。
- Shell 使用[基于 K8s 的 Kubeflow 平台](https://www.altoros.com/blog/shell-builds-10000-ai-models-on-kubernetes-in-less-than-a-day/)，在笔记本电脑上快速测试和试验 ML 模型。工程师可以直接将这些工作负载从测试环境移植到生产环境，保持功能不变。使用 Kubernetes，Shell 能在 2 小时而不是 1 个月内构建数千个 ML 模型，编写底层代码的时间也从 2 周缩短到 4 小时。
- 宜家开发了基于 K8s 的[内部 MLOps 平台](https://ossna2023.sched.com/event/1K5Ci)，可在内部训练 ML 模型，在云端进行推理。这使 MLOps 团队可以编排不同类型的训练模型，最终提升客户体验。

当然，这些例子并不具有广泛代表性。多数公司不像 OpenAI 那样专注 AI，也不像宜家那样大。它们承担不起从零开始训练大型 AI/ML 模型的时间和成本，而是运行预训练模型并与其他内部服务集成。换言之，这些公司使用 AI/ML 推理而非训练。

相较训练工作负载，推理工作负载的资源利用更为动态，因为生产集群更容易遭遇用户和流量峰值。在这种情况下，基础设施需要快速扩缩容，而 AI/ML 训练通常需要渐进式扩展。因此，对于已部署的训练好的 AI/ML 模型，K8s 的可扩展性和动态资源利用尤其重要。

## 为何作为工作节点 GPU 胜过 CPU

与 CPU 工作节点相比，GPU 工作节点更适合容器化的 AI/ML 工作负载，原因与非容器化工作负载相同：GPU 提供并行处理能力，其 AI/ML 性能优于 CPU。

运行在 GPU 工作节点上的 AI/ML 工作负载推理可能比在 CPU 工作节点上快，主要有以下原因:

- GPU 的内存架构专门针对 AI/ML 处理进行了优化，提供比 CPU 更高的内存带宽。
- 由于拥有更多晶体管处理数据，GPU 的 AI/ML 训练和推理计算性能通常优于 CPU。

除硬件加速，运行在 GPU 工作节点上的 AI/ML 工作负载还从 Kubernetes 获得可扩展性和动态资源分配等裨益。Kubernetes 还包含 GPU 制造商支持的插件，便于为 AI/ML 工作负载配置 GPU 资源。

![](https://cdn.thenewstack.io/media/2023/10/579e1d5e-image3.png)

*具有 GPU 工作节点的简化 K8s 集群架构图*

通过 Kubernetes，可跨多个工作节点管理 GPU 资源。容器消耗 GPU 资源的方式与 CPU 基本相同。

## GPU 制造商比较

Kubernetes 中可用的 GPU 制造商有 3 家：NVIDIA、AMD 和 Intel。选择工作节点 GPU 时，[必须考虑它们与 K8s 的兼容性](https://thenewstack.io/eight-ways-keep-kubernetes-growing-fast-strong/)、工具生态、性能和成本可能不同。

![](https://cdn.thenewstack.io/media/2023/10/60dd481b-image1.jpg)

我们对 3 家供应商进行比较:

- **与 K8s 的兼容性**：NVIDIA 与 K8s 兼容性最好。它提供了 CUDA 驱动程序、各种容器运行时和其他工具，简化 GPU 集成和管理。AMD 和英特尔对 K8s 的支持不太成熟，通常需要自定义配置。
- **工具生态系统**：由于提供 GPU Operator、Container Toolkit 等软件，以及针对 NVIDIA GPU 优化的 ML 框架如 TensorFlow、PyTorch 和 MXNet，NVIDIA 在 AI/ML 工具生态系统中最完善。AMD 和英特尔在这方面不如 NVIDIA 全面。
- **性能**：NVIDIA GPU 在 AI 工作负载方面的性能很高，在大多数 MLPerf 基准测试中领先竞争对手。NVIDIA GPU 最适合深度学习和高性能计算等计算密集任务。
- **成本**：NVIDIA GPU 是最昂贵的 GPU 工作节点。
- **灵活性**：相比竞争对手，NVIDIA 在基于 GPU 的 K8s 集群管理和资源利用方面更加灵活，主要原因如下：
   - 针对 NVIDIA A100 GPU 的 MIG 机制，可将 GPU 安全分区为多达 7 个实例，提高 GPU 利用率。
   - 多云 GPU 集群可像在单个云上无缝管理和扩展。
   - 异构 GPU 和 CPU 集群简化分布式深度学习模型的训练和管理。
   - 使用 Prometheus 监控 GPU指标，Grafana 进行可视化。
   - 支持多种容器运行时，包括 Docker、CRI-O 和容器。

总之，考虑到兼容性、工具生态和性能等方面，NVIDIA GPU 是 Kubernetes 上 AI/ML 工作负载的最佳选择。这也是我们在 [Gcore 托管 Kubernetes](https://gcore.com/cloud/managed-kubernetes) 中选择 NVIDIA GPU 的原因，可提供最快的 AI/ML 工作负载训练和推理性能。

## Kubernetes 中 GPU 调度的重要注意事项

为启用 GPU 调度并允许 pod 访问 GPU 资源，需要从所选的 GPU 制造商(NVIDIA、AMD 或 Intel)安装[特定的设备插件](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/#using-device-plugins)。

Pod 请求 GPU 资源的方式与请求 CPU 一样。但是，在配置`limits`和`requests`方面，Kubernetes 对 GPU 的灵活性不如 CPU。`requests`是 pod 保证获取的资源量，如最小值；`limits`是不超过的资源量，如最大值。在为 GPU 配置 pod 时，`requests`和`limits`需相等，即 pod 不会得到超过保证数量的资源。

另外，默认情况下，不能将 GPU 的一部分或多个 GPU 分配给容器，因为 CPU 分配只允许整个 GPU 分配给单个容器。这对资源利用不够经济。但 NVIDIA 设法解决了这个问题，其 GPU 可以使用:

- **时间共享 GPU**：在物理 GPU 上按时间间隔顺序分配给共享容器，适用于所有 NVIDIA GPU。
- **多实例 GPU**：可将单个 GPU 分区为多达 7 个实例，提高 GPU 利用率。仅适用于 NVIDIA A100 GPU。

这两种机制可帮助更有效利用 NVIDIA GPU 资源，减少云中租用 GPU 实例的成本，较其他 GPU 制造商有明显优势。

## 托管 Kubernetes vs 原生 Kubernetes + GPU

相比原生开源 Kubernetes，托管 Kubernetes 服务在运行基于 GPU 工作节点的 AI/ML 工作负载方面有以下优势:

- **灵活的 GPU 选择**：托管 K8s 服务通常支持多种规格的 GPU 实例，更容易为 AI/ML 工作负载选择适合的 GPU 加速能力。
- **减少运维工作**：托管 Kubernetes 处理 Kubernetes 集群的日常管理，如控制平面和升级，使开发者可以专注在 AI/ML 应用的创建、部署和管理。
- **可扩展性与可靠性**：托管 K8s 服务通常在可扩展性和可靠性方面做了优化，确保 AI/ML 工作负载能灵活应对流量波动和资源需求峰值。

## NVIDIA GPU 的 Gcore 托管 Kubernetes

[Gcore 托管的 Kubernetes](https://gcore.com/cloud/managed-kubernetes) 帮助快速部署 K8s 集群，无需维护基础设施和 Kubernetes 后端。Gcore 团队管理主节点，您只管理工作节点，减轻了运维负担。工作节点可以是各种配置的 Gcore 虚拟机或裸机服务器，包括配备 NVIDIA GPU 的节点。

## 总结

托管 Kubernetes 与 GPU 工作节点强力组合，可加速 AI/ML 推理。 借助 Kubernetes 和 GPU 的优势，基于 GPU 的托管 K8s 可提升 AI/ML 工作负载性能和效率。该服务也省去了维护底层 GPU 基础设施和大部分 Kubernetes 组件的需要。
