# 使用 Kubernetes 进行 AI 推理的 5 个理由

![使用 Kubernetes 进行 AI 推理的特色图片](https://cdn.thenewstack.io/media/2024/07/c0e31aee-image1-2-1024x768.png)

[Kubernetes](https://thenewstack.io/kubernetes/) 的许多关键特性自然适合 AI 推理的需求，无论是 AI 驱动的 [微服务](https://thenewstack.io/microservices/) 还是 ML 模型，几乎像是专门为这个目的而设计的。让我们来看看这些特性以及它们如何使推理工作负载受益。

## 1. 可扩展性

AI 驱动的应用程序和 ML 模型的可扩展性确保它们能够处理所需的负载，例如并发用户请求的数量。Kubernetes 有三种原生 [自动扩展](https://thenewstack.io/kubernetes-autoscaling-keda-moves-into-cncf-incubation/) 机制，每种机制都对可扩展性有益：水平 Pod 自动扩展器 (HPA)、垂直 Pod 自动扩展器 (VPA) 和集群自动扩展器 (CA)。

**水平 Pod 自动扩展器**根据各种指标（例如 CPU、GPU 和内存利用率）扩展运行应用程序或 ML 模型的 Pod 数量。当需求增加时，例如用户请求激增，HPA 会向上扩展资源。当负载减少时，HPA 会向下扩展资源。**垂直 Pod 自动扩展器**根据 Pod 的实际使用情况调整 Pod 中容器的 CPU、GPU 和内存需求和限制。通过更改 Pod 规范中的`limits`，您可以控制 Pod 可以接收的特定资源量。它对于最大化节点上每个可用资源的利用率很有用。**集群自动扩展器**调整整个集群中可用的计算资源池，以满足工作负载需求。它根据 Pod 的资源需求动态地向集群添加或删除工作节点。这就是为什么 CA 对推理具有庞大用户群的大型 ML 模型至关重要。

以下是 K8s 可扩展性对 AI 推理的主要益处：

- 通过根据需要自动向上和向下扩展 Pod 副本数量，确保 AI 工作负载的高可用性
- 通过根据需要自动调整集群大小来支持产品增长
- [根据应用程序的实际需求优化资源利用率](https://thenewstack.io/the-next-frontier-for-aiops-application-optimization/)，从而确保您只为 Pod 使用的资源付费

## 2. 资源优化

通过彻底优化推理工作负载的资源利用率，您可以为它们提供适当数量的资源。这可以为您节省资金，这在租用通常昂贵的 GPU 时尤其重要。允许您优化推理工作负载的资源使用的关键 Kubernetes 特性是高效的资源分配、对`limits`和`requests`的详细控制以及自动扩展。

**高效的资源分配**: 您可以通过在 Pod 清单中指定来为 Pod 分配特定数量的 GPU、CPU 和 RAM。但是，目前只有 NVIDIA 加速器支持 GPU 的时间切片和多实例分区。如果您使用 Intel 或 AMD 加速器，Pod 只能请求整个 GPU。**对资源“limits”和“requests”的详细控制**: `requests`定义容器所需的最小资源，而`limits`阻止容器使用超过指定资源的资源。这提供了对计算资源的细粒度控制。**自动扩展**: HPA、VPA 和 CA 可以防止浪费闲置资源。如果您正确配置这些功能，您将不会有任何闲置资源。

借助这些 Kubernetes 功能，您的工作负载将获得所需的计算能力，不多不少。由于在云中租用中档 GPU 的成本可能在 [每小时 1 美元到 2 美元](https://getdeploying.com/reference/cloud-gpu) 之间，因此从长远来看，您可以节省大量资金。

## 3. 性能优化

虽然 AI 推理通常 [比训练资源密集度低](https://thenewstack.io/managed-k8s-with-gpu-worker-nodes-for-faster-ai-ml-inference/)，但它仍然需要 GPU 和其他计算资源才能高效运行。HPA、VPA 和 CA 是 Kubernetes 能够提高推理性能的关键贡献者。它们确保即使负载发生变化，也能为 AI 驱动的应用程序分配最佳资源。但是，您可以使用其他工具来帮助您控制和预测 AI 工作负载的性能，例如 [StormForge](https://www.stormforge.io/) 或 [Magalix Agent](https://github.com/MagalixCorp/magalix-agent)。

总的来说，Kubernetes 的弹性和微调资源使用能力使您能够为 AI 应用程序实现最佳性能，无论其大小和负载如何。

## 4. 可移植性
## 对于 AI 工作负载（例如 ML 模型）来说，可移植性至关重要。这使您能够在不同环境中一致地运行它们，而无需担心基础设施差异，从而节省时间和资金。Kubernetes 主要通过两个内置功能实现可移植性：容器化和与任何环境的兼容性。

**容器化**: Kubernetes 使用容器化技术（如 containerd 和 Docker）将 ML 模型和 AI 驱动的应用程序与其依赖项一起打包到可移植容器中。然后，您可以在任何集群、任何环境中甚至使用其他容器编排工具使用这些容器。**支持多云和混合环境**: Kubernetes 集群可以分布在多个环境中，包括公有云、私有云和本地基础设施。这为您提供了灵活性并减少了供应商锁定。

以下是 K8s 可移植性的主要优势：

- 在不同环境中一致的 ML 模型部署
- 更轻松地迁移和更新 AI 工作负载
- 选择云提供商或本地基础设施的灵活性

## 5. 容错

在运行 AI 推理时，基础设施故障和停机可能会导致显着的精度下降、不可预测的模型行为或仅仅是服务中断。对于许多 AI 驱动的应用程序来说，这是不可接受的，包括安全关键型应用程序，例如机器人、自动驾驶和医疗分析。Kubernetes 的自我修复和容错功能有助于防止这些问题。

**Pod 级和节点级容错**: 如果 Pod 出现故障或没有响应，Kubernetes 会自动检测问题并重新启动 Pod。这确保了应用程序保持可用和响应。如果运行 Pod 的节点出现故障，Kubernetes 会自动将 Pod 调度到健康的节点。**滚动更新**: Kubernetes 支持滚动更新，因此您可以以最小的停机时间更新容器镜像。这使您能够快速部署错误修复或模型更新，而不会中断正在运行的推理服务。**就绪性和存活性探测**: 这些探测是健康检查，用于检测容器何时无法接收流量或变得不健康，并在必要时触发重新启动或替换。**集群自我修复**: K8s 可以自动修复[控制平面和工作节点](https://thenewstack.io/how-many-nodes-for-your-kubernetes-control-plane/)问题，例如替换故障节点或重新启动不健康的组件。这有助于维护运行 AI 推理的集群的整体健康状况和可用性。

以下是 K8s 容错的主要优势：

- 通过保持 AI 驱动的应用程序高度可用和响应，提高了应用程序的弹性
- 出现问题时停机时间和中断最小
- 通过使应用程序和模型高度可用并更能抵御意外的基础设施故障，提高了用户满意度

## 结论

随着组织继续将 AI 整合到其应用程序中，使用大型 ML 模型并面临动态负载，采用 Kubernetes 作为基础技术至关重要。作为[托管 Kubernetes 提供商](https://gcore.com/cloud/managed-kubernetes)，我们看到了对可扩展、容错且经济高效的基础设施的需求不断增长，这种基础设施可以处理[AI 推理](https://gcore.com/inference-at-the-edge)规模。Kubernetes 是一个原生提供所有这些功能的工具。

想要了解更多关于使用 Kubernetes 加速 AI 的信息？探索[这本 Gcore 电子书](https://gcore.com/library/accelerating-ai-k8s)。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)