随着人工智能 (AI) 和机器学习 (ML) 工作负载在复杂性和规模上不断增长，对强大且高效的计算资源的需求变得更加关键。在 Kubernetes 上运行工作负载可以让您利用可扩展性和自我修复功能，但是，在管理和优化 GPU 资源方面存在挑战。这就是 GPU 运算符和插件发挥作用的地方。它们提供了一种在 Kubernetes 中部署和管理 GPU 的解决方案。

有一些 GPU 运算符，例如 [英特尔设备插件运算符](https://github.com/intel/intel-device-plugins-for-kubernetes/blob/main/cmd/gpu_plugin/README.md#install-with-operator)，[AMD GPU 运算符](https://github.com/ROCm/gpu-operator) 和 [NVIDIA GPU 运算符](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html)。但是，NVIDIA GPU 运算符是最受欢迎的运算符之一。它提供了一个全面的解决方案，可以简化 Kubernetes 环境中 GPU 的部署、管理和优化。

在这篇文章中，我们将深入探讨 NVIDIA GPU 运算符及其功能，并了解一些基本结构，这些结构使您能够使用这些功能。让我们开始吧！

## 什么是 NVIDIA GPU 运算符？
在 Kubernetes 集群中管理 GPU 可能是一项艰巨的任务。传统方法通常需要手动安装和配置 GPU 驱动程序，这既费时又容易出错。此外，利用高级 GPU 功能并确保 GPU 与其他系统组件之间高效的数据传输需要专门的知识和工具。如果没有简化的方法，这些挑战会阻碍 AI/ML 工作负载的性能和可扩展性。

NVIDIA GPU 运算符提供了多种功能。它使在 Kubernetes 上设置 GPU 驱动程序及其配置变得轻而易举。当需要在给定节点上运行多个 AI 工作负载时，使用 vGPU、多实例 GPU (MIG) 和 GPU 时间切片等高级功能的能力至关重要。此外，GPU 需要与其他应用程序/GPU 以及存储设置进行快速通信。[GPUDirect RDMA](https://docs.nvidia.com/cuda/gpudirect-rdma/index.html)、GPU Direct 存储和 [GDR Copy](https://developer.nvidia.com/gdrcopy) 在实现这一点方面发挥着重要作用。GPU 运算符有助于轻松地将所有这些功能以及更多功能引入您的 Kubernetes 集群。

![NVIDIA GPU 运算符](/assets/img/Blog/nvidia-gpu-operator/nvidia-gpu-operator.png)

[(NVIDIA GPU 运算符)](https://developer.nvidia.com/blog/nvidia-gpu-operator-simplifying-gpu-management-in-kubernetes/)

### NVIDIA GPU 运算符的关键功能
- **自动安装和维护 GPU 驱动程序**: NVIDIA GPU 运算符自动安装和维护 GPU 驱动程序，无需人工干预。这种自动化确保驱动程序始终是最新的并正确配置，使 AI/ML 工作负载能够平稳高效地运行。

- **高级 GPU 功能的配置**:
    - **vGPU (虚拟 GPU)**: 使单个 GPU 能够在多个虚拟机之间共享，最大限度地提高资源利用率和灵活性。
    - **MIG (多实例 GPU)**: 允许将单个 GPU 分区成多个独立的实例，每个实例都有自己的专用资源，从而提高工作负载隔离和效率。
    - **GPU 时间切片**: 在多个任务之间切片 GPU 时间，确保 GPU 资源在不同工作负载之间公平高效地分配。

- **配置 GPUDirect RDMA 和 GPUDirect 存储**:
    - **GPUDirect RDMA (远程直接内存访问)**: 促进不同节点上的 GPU 之间的直接通信，绕过 CPU 并减少延迟，这对高性能计算应用程序至关重要。
    - **GPUDirect 存储**: 允许 GPU 与存储设备之间直接传输数据，显着加快数据密集型应用程序的数据访问和处理速度。

- **配置 GDR Copy**: [GPUDirect RDMA (GDR) Copy](https://developer.nvidia.com/gdrcopy) 是一个基于 GPUDirect RDMA 技术的低延迟 GPU 内存复制库，允许 CPU 直接映射和访问 GPU 内存。它提高了内存复制操作的效率，减少了开销并提高了整体性能。

- **沙箱工作负载**: 使应用程序能够在利用虚拟机 (VM) 或具有安全限制的容器的隔离环境中运行。这有助于 [增强安全性、更好的资源管理](https://www.microsoft.com/en-us/research/video/lightning-talks-sustainably-nourishing-the-world/) 和模型的可重复性。

## 安装 NVIDIA GPU 运算符
要利用 NVIDIA GPU 运算符的功能来管理 Kubernetes 集群中的 GPU 资源，您需要遵循结构化的安装过程并满足某些先决条件。

### 先决条件
在安装 NVIDIA GPU 运算符之前，请确保满足以下先决条件：

- Kubernetes 集群 v1.18 或更高版本
- 节点要求：
    - 配备 NVIDIA GPU 的节点。
    - 节点必须安装 NVIDIA 驱动程序（尽管 GPU 运算符可以自动执行此操作）。
- Helm v3

### 安装步骤

按照以下步骤在您的 Kubernetes 集群上安装 NVIDIA GPU 运算符。

- 设置 Helm 存储库。将 NVIDIA Helm 存储库添加到您的 Helm 配置中。

```
helm repo add nvidia https://nvidia.github.io/gpu-operator
helm repo update
```

- 为 GPU 运算符创建一个专用命名空间：

```
kubectl create namespace gpu-operator
```

- 使用 Helm 在创建的命名空间中安装 GPU 运算符：

```
helm install --namespace gpu-operator gpu-operator nvidia/gpu-operator
```

- 验证安装。检查已部署资源的状态以确保 GPU 运算符正常运行：

```
kubectl get pods -n gpu-operator
```

您应该看到 GPU 运算符及其组件在 gpu-operator 命名空间中运行。

- 检查节点配置：通过检查 NVIDIA 驱动程序和其他必要组件，验证 GPU 运算符是否已正确配置节点。

```
Name: infracloud01
Roles: control-plane
Labels: beta.kubernetes.io/arch=amd64
beta.kubernetes.io/os=linux
...
nvidia.com/gpu.deploy.container-toolkit=true
nvidia.com/gpu.deploy.dcgm=true
nvidia.com/gpu.deploy.dcgm-exporter=true
nvidia.com/gpu.deploy.device-plugin=true
nvidia.com/gpu.deploy.driver=true
nvidia.com/gpu.deploy.gpu-feature-discovery=true
nvidia.com/gpu.deploy.node-status-exporter=true
nvidia.com/gpu.deploy.operator-validator=true
nvidia.com/gpu.present=true
Annotations: node.alpha.kubernetes.io/ttl: 0
nvidia.com/gpu-driver-upgrade-enabled: true
projectcalico.org/IPv4Address: 192.168.0.52/24
...
Capacity:
cpu: 32
ephemeral-storage: 982345180Ki
hugepages-1Gi: 0
hugepages-2Mi: 0
memory: 131600376Ki
pods: 110
Allocatable:
cpu: 32
ephemeral-storage: 905329316390
hugepages-1Gi: 0
hugepages-2Mi: 0
memory: 131497976Ki
pods: 110
...
```

查找指示节点已启用 GPU 并已配置的注释和标签。

### 运行示例 GPU 应用程序

您现在可以通过在集群中部署示例 CUDA VectorAdd 应用程序来测试您的设置。示例应用程序将两个向量加在一起并请求 1 个 gpu 资源。GPU 分配请求由 GPU 运算符处理。

- 运行 CUDA VectorAdd 应用程序。

```
cat << EOF | kubectl create -f -
apiVersion: v1
kind: Pod
metadata:
name: cuda-vectoradd
spec:
restartPolicy: OnFailure
containers:
- name: cuda-vectoradd
image: "nvidia/samples:vectoradd-cuda11.2.1"
resources:
limits:
nvidia.com/gpu: 1
EOF
```

```
pod/cuda-vectoradd created
```

- 检查 pod 日志。

```
$ kubectl logs cuda-vectoradd
```

```
[Vector addition of 50000 elements]
Copy input data from the host memory to the CUDA device
CUDA kernel launch with 196 blocks of 256 threads
Copy output data from the CUDA device to the host memory
Test PASSED
Done
```

让我们详细了解 GPU 运算符的一些关键技术。

## GPU 并发

GPU 并发是 GPU 利用其并行处理能力同时执行多个操作的能力。此功能对于提高 AI/ML 工作负载的性能、效率和可扩展性至关重要。通过并行处理，GPU 可以显着加快训练和推理速度，管理更大、更复杂的数据集，并提供实时响应。

vGPU（虚拟 GPU）、多实例 GPU（MIG）和 GPU 时间切片是支持 GPU 并发在各种场景中通过不同机制实现的关键技术。以下是每种技术的简要概述。

- **vGPU**: vGPU 使单个物理 GPU 能够在多台虚拟机 (VM) 之间共享，每台 VM 都有自己的专用 GPU 资源。
- **MIG**: MIG 在硬件级别将单个 GPU 分区为多个隔离的实例，每个实例都有自己的专用内存和计算资源。此功能特定于 NVIDIA 的 A100 及更高版本的 GPU，例如 H100、H200、B100、B200
- **GPU 时间切片**: GPU 时间切片涉及将 GPU 的处理时间分配给多个任务或用户，允许他们以时间分配的方式共享 GPU，这与 CPU 并发的工作方式非常相似。

![vGPU vs MIG vs 时间切片](/assets/img/Blog/nvidia-gpu-operator/vgpuvs-migvs-time-slicing.png)

[(vGPU vs MIG vs 时间切片)](https://developer.nvidia.com/blog/improving-gpu-utilization-in-kubernetes)

## GPUDirect RDMA 和 GPUDirect 存储
NVIDIA [GPUDirect RDMA](https://docs.nvidia.com/cuda/gpudirect-rdma/index.html) (远程直接内存访问) 和 [GPUDirect Storage](https://docs.nvidia.com/gpudirect-storage/overview-guide/index.html) (GDS) 是旨在优化高性能计算应用程序数据传输的先进技术。GPUDirect RDMA 允许不同节点上的 GPU 之间直接通信，绕过 CPU 并降低延迟。这种直接数据路径对于需要快速、低延迟通信的应用程序至关重要，例如分布式 AI 训练和实时数据处理。通过最大限度地减少 CPU 的参与，GPUDirect RDMA 显着提高了性能和效率，从而实现更快的计算和更可扩展的 AI 工作负载。

![GPUDirect RDMA：通过网络直接连接 GPU](/assets/img/Blog/nvidia-gpu-operator/gpu-direct-rdma.png)

[(GPUDirect RDMA：通过网络直接连接 GPU)](https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io/)

类似地，GPUDirect Storage 促进 GPU 与存储设备之间的直接数据传输，绕过 CPU 和系统内存。这种对存储设备（例如 NVMe SSD）的直接访问加速了数据吞吐量并降低了延迟，这对数据密集型应用程序至关重要。通过简化数据流，GPUDirect Storage 确保 GPU 可以快速访问和处理大型数据集，从而实现更快、更高效的计算。

![带有和不带有 GPUDirect Storage 的存储访问模式](/assets/img/Blog/nvidia-gpu-operator/storage-access-pattern.png)

[(带有和不带有 GPUDirect Storage 的存储访问模式)](https://developer.nvidia.com/blog/boosting-data-ingest-throughput-with-gpudirect-storage-and-rapids-cudf/)

## GDR 复制
![GPUDirect RDMA (GDR) 复制](/assets/img/Blog/nvidia-gpu-operator/gpudirect-rdma-copy.png)

[(GPUDirect RDMA (GDR) 复制)](https://www.nvidia.com/en-us/on-demand/session/gtcspring21-s32039/?start=1851&end=2070)

[GDR 复制](https://github.com/NVIDIA/gdrcopy) 代表 GPUDirect RDMA 复制，它是一个基于 GPUDirect RDMA 的低延迟 GPU 内存复制库。该库的一个突出用例是在 GPU 等待接收数据和来自主机的信号以启动处理操作时，在 CPU（主机）和 GPU 之间传输数据。GDR 复制使用 GPUDirect RDMA 功能将 GPU 内存的一部分暴露给外部设备（例如 NIC、CPU 等）以执行 CPU 驱动的复制操作。这使得 GDR 复制能够以更低的延迟和更高的吞吐量执行 CPU 和 GPU 内存之间的复制操作，与 GPU 驱动的内存复制操作（例如 cudaMemcpy）相比，对于较小的数据大小而言。

![使用 cudaMemcpy 和 GDR 复制的主机-设备内存复制操作](/assets/img/Blog/nvidia-gpu-operator/host-device-memory-copy-operation.png)

[(使用 cudaMemcpy 和 GDR 复制的主机-设备内存复制操作)](https://developer.nvidia.com/gdrcopy)

上图显示了使用 GDR 复制与 cudaMemcpy 的主机-设备内存复制操作之间的区别。cudaMemcpy 是 GPU 驱动的操作，它使用 GPU DMA 引擎来移动数据。这涉及 DMA 引擎开销，用于较小的数据大小。GDR 复制允许 CPU 通过 [BAR](https://en.wikipedia.org/wiki/PCI_configuration_space#Bus_enumeration) 映射直接访问 GPU 内存，从而实现低延迟数据传输。

## GPU 运算符 CRD
NVIDIA GPU 运算符使用多个自定义资源定义 (CRD) 来管理 Kubernetes 上 GPU 驱动程序和相关组件的生命周期。以下是一些主要的 CRD。

### 集群策略 CRD
[集群策略自定义资源定义 (CRD)](https://github.com/NVIDIA/gpu-operator/blob/main/deployments/gpu-operator/crds/nvidia.com_clusterpolicies_crd.yaml) 是 NVIDIA GPU 运算符的核心。它充当在 Kubernetes 集群上部署所有必要的 NVIDIA 软件组件的单点配置。ClusterPolicy CRD 允许管理员指定和管理 GPU 相关组件的整个生命周期，包括驱动程序、运行时、设备插件和监控工具。

自定义资源允许管理重要属性的配置，例如：

- **驱动程序**: NVIDIA 驱动程序的配置，包括映像、版本和存储库设置。
- **工具包**: NVIDIA 容器工具包的设置，它提供用于运行 GPU 加速容器的实用程序。
- **设备插件**: NVIDIA 设备插件的配置，它允许 Kubernetes 识别和调度 GPU 资源。
- **mig**: 在支持的硬件上管理多实例 GPU (MIG) 配置的参数。
- **gpuFeatureDiscovery**: GPU 功能发现工具的设置，它检测并标记具有 GPU 功能的节点。
- **dcgmExporter**: 数据中心 GPU 管理器 (DCGM) 导出器的配置，用于监控 GPU 指标。
-
## 验证器: GPU 运算符验证器的配置，用于确保所有组件都已正确部署并正常运行。

### NVIDIA 驱动程序 CRD

[NvidiaDriver 自定义资源定义 (CRD)](https://github.com/NVIDIA/gpu-operator/blob/main/deployments/gpu-operator/crds/nvidia.com_nvidiadrivers.yaml) 特别管理 NVIDIA 驱动程序在 Kubernetes 节点上的部署和生命周期。它确保安装并运行正确版本的驱动程序，与 GPU 硬件和 Kubernetes 环境兼容。虽然驱动程序配置也可以由集群策略 CR 控制，但驱动程序 CR 允许为每个节点指定驱动程序类型和版本。

以下是可以使用它管理的一些配置。

- **image**: 指定 NVIDIA 驱动程序的容器镜像。这包括存储库、镜像名称和标签。
- **repository**: 包含驱动程序镜像的存储库的 URL 或路径。
- **version**: 要部署的 NVIDIA 驱动程序的特定版本。
- **deploy**: 驱动程序应如何部署的配置选项，例如使用 DaemonSets。
- **nodeSelector**: 指定应安装驱动程序的节点，通常与支持 GPU 的节点匹配。
- **tolerations**: 节点污点的容忍度，确保驱动程序可以在必要时调度到有污点的节点。
- **resources**: 驱动程序安装 Pod 的资源请求和限制。

## 总结

在这篇文章中，我们看到了 NVIDIA GPU 运算符是如何成为在 Kubernetes 集群中优化和管理 GPU 资源的关键工具，它专门针对满足 AI 和 ML 工作负载的苛刻需求而设计。它自动执行 GPU 驱动程序的安装和维护，简化了高级 GPU 功能（如虚拟 GPU (vGPU)、多实例 GPU (MIG)、GPU 时间切片、GPUDirect RDMA 和 GPUDirect 存储）的配置，并显着提高了性能和效率。

我们还检查了 GPU 运算符支持的关键技术，例如 GPUDirect RDMA 和 GPUDirect 存储，它们对于低延迟、高速数据传输至关重要。我们还讨论了 GPU 共享技术，如 vGPU、MIG 和 GPU 时间切片，以及这三种技术如何旨在实现共享 GPU 访问、提高效率和降低成本，但适用于不同的用例和硬件配置。

总之，NVIDIA GPU 运算符对于在 Kubernetes 环境中有效地管理 GPU 资源至关重要，它支持先进的技术并简化复杂的配置，从而为 AI 和 ML 工作负载带来卓越的性能和可扩展性。

现在您已经了解了 NVIDIA GPU 运算符及其功能和关键概念，您可以邀请 [AI 和 GPU 云专家](https://www.infracloud.io/build-ai-cloud/) 来帮助您构建自己的 AI 云。

如果您发现这篇文章有用且信息丰富，请订阅我们的每周时事通讯以获取更多类似的文章。我们很乐意听到您对这篇文章的看法，因此请在 LinkedIn 上与 [Sameer](https://www.linkedin.com/in/sameer-kulkarni-9875773b/) 和 [Sanket](https://www.linkedin.com/in/sanketsudake/) 开始对话。