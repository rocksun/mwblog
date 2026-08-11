<!--
title: 告别 K8s GPU 调度痛点：DRA 如何重塑资源管理
cover: https://cdn.thenewstack.io/media/2026/08/16e8cc20-logan-voss-erv_j4lcag8-unsplash.jpg
summary: 本文探讨了在 Kubernetes 中管理异构 GPU 集群的痛点，重点介绍了 1.34 版本引入的动态资源分配（DRA）技术。DRA 改变了以往僵化的调度模式，允许通过 CEL 表达式灵活定义硬件需求，有效解决了 MIG 资源浪费和复杂的调度配置难题。
-->

本文探讨了在 Kubernetes 中管理异构 GPU 集群的痛点，重点介绍了 1.34 版本引入的动态资源分配（DRA）技术。DRA 改变了以往僵化的调度模式，允许通过 CEL 表达式灵活定义硬件需求，有效解决了 MIG 资源浪费和复杂的调度配置难题。

> 译自：[Say goodbye to K8s GPU pain: How DRA changes everything](https://thenewstack.io/kubernetes-dra-gpu-scheduling)
> 
> 作者：Dawood Abbas

试想一个平台团队正在管理一个混合了 B200、H100 和最近添加的 B300 的共享 GPU 集群。每周一早上，值班工程师都会发现周末积压了一堆待处理的任务。训练工作负载因被分配到 H100 而触发内存溢出（OOM）错误导致卡死；推理任务则因小型 MIG（多实例 GPU）切片耗尽而闲置，尽管旁边就有空闲的大型切片。

他们的解决方法是什么？编写一个 200 行的 Bash 脚本，每 30 分钟运行一次，重新配置 MIG 配置文件，重新调度卡死的任务，并在成功时发送 Slack 提醒，失败时发送 PagerDuty 报警。

## 问题的根源

真正的问题出在哪里：Kubernetes 将每个 GPU 都视为完全相同的单位。资源限制 nvidia.com/gpu: 1 是它所能感知的全部范围。调度程序根本不知道它是将一个 192GB 的 B200 还是一个 80GB 的 H100 交给了 Pod。一个需要 150GB 显存的训练任务可能会被分配到 H100 上并立即触发 OOM，而旁边的 B200 节点却完全处于闲置状态。

> “Kubernetes 将每个 GPU 都视为完全相同的单位。”

业界公认的“修复方案”严重依赖于节点标签（node labels）、污点（taints）、容忍度（tolerations）以及[每个 GPU 类型独立的节点池](https://thenewstack.io/self-healing-gpu-nodes/)。每个工作负载的清单文件都硬编码了硬件假设。添加一个新的 GPU 代系意味着要更新 40 个不同的 Helm Charts。

## MIG 的假象

MIG 让情况变得更糟。MIG 将单个 GPU 切分为更小的、隔离的分区，每个分区都有专用的内存和计算资源。与其让一个推理任务垄断一个 B200，你可以在同一张卡上运行七个较小的任务。

理论上，这听起来不错。但当你[在 Kubernetes 中启用 MIG](https://thenewstack.io/managed-k8s-with-gpu-worker-nodes-for-faster-ai-ml-inference/) 时，每个配置文件都变成了一个独立的、僵化的资源类型（例如 nvidia.com/mig-1g.10gb, nvidia.com/mig-3g.40gb）。这里没有回退逻辑。你无法指示一个任务“先尝试小切片，如果没有空闲则使用大切片”。当小切片用完时，任务就会一直处于挂起状态，而大切片却被浪费了。

> “当小切片用完时，任务就会一直处于挂起状态，而大切片却被浪费了。”

这种低效被视为在 Kubernetes 上运行 GPU 工作负载的必要代价。随后，Kubernetes 1.34 发布了。

## 动态资源分配 (DRA)

Kubernetes 1.34 引入了[动态资源分配 (DRA)](https://thenewstack.io/kubernetes-get-the-most-from-dynamic-resource-allocation/)，从根本上改变了调度模型。GPU 驱动程序现在发布结构化数据。工作负载无需再请求通用的 nvidia.com/gpu: 1，而是可以使用通用表达式语言 (CEL) 来表达明确的意图：

1. “给我一个 H100 或更好的 GPU，且至少有 40GB 显存。”
2. “给我一个 MIG 切片：如果可用就用小的，不行就用中等的，必要时使用完整 GPU。”
3. “给我四个通过 NVLink 连接的 GPU。”

### 示例 1：硬件和内存需求

*“给我一个 H100 或更好的 GPU，且至少有 40GB 显存。”*

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: h100-or-better-40gb
spec:
  spec:
    devices:
      requests:
        - name: gpu
          deviceClassName: gpu.nvidia.com
          count: 1
          selectors:
            - cel:
                # Attribute names are illustrative.
                # Your NVIDIA DRA driver must expose these fields.
                expression: >
                  device.attributes["gpu.nvidia.com"].memory >= quantity("40Gi") &amp;&amp;
                  device.attributes["gpu.nvidia.com"].generation in ["H100", "B200", "B300"]
---
apiVersion: batch/v1
kind: Job
metadata:
  name: training-job-h100-or-better
spec:
  template:
    spec:
      restartPolicy: Never
      resourceClaims:
        - name: gpu
          source:
            resourceClaimTemplateName: h100-or-better-40gb
      containers:
        - name: trainer
          image: nvcr.io/nvidia/pytorch:24.12-py3
          command: ["python", "train.py"]
          resources:
            claims:
              - name: gpu
```

### 示例 2：灵活的 MIG 回退策略

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: mig-prefer-small-then-medium-then-full
spec:
  spec:
    devices:
      requests:
        - name: gpu
          deviceClassName: gpu.nvidia.com
          count: 1
          selectors:
            - cel:
                # Prefer any acceptable MIG profile or full GPU
                expression: >
                  device.attributes["gpu.nvidia.com"].profile in [
                    "mig-1g.10gb",
                    "mig-2g.20gb",
                    "mig-3g.40gb",
                    "full-gpu"
                  ]
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: inference-service-flexible-gpu
spec:
  replicas: 2
  selector:
    matchLabels:
      app: inference-service
  template:
    metadata:
      labels:
        app: inference-service
    spec:
      resourceClaims:
        - name: gpu
          source:
            resourceClaimTemplateName: mig-prefer-small-then-medium-then-full
      containers:
        - name: inference
          image: nvcr.io/nvidia/tritonserver:24.12-py3
          args: ["tritonserver", "--model-repository=/models"]
          resources:
            claims:
              - name: gpu
```

### 示例 3：拓扑约束

*“给我 4 个通过 NVLink 连接的 GPU。”*

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: four-nvlink-connected-gpus
spec:
  spec:
    devices:
      requests:
        - name: gpus
          deviceClassName: gpu.nvidia.com
          count: 4
          selectors:
            - cel:
                # Attribute names are illustrative.
                # Some NVIDIA DRA setups may model this through ComputeDomains.
                expression: >
                  device.attributes["gpu.nvidia.com"].fabric == "nvlink"
      constraints:
        - requests: ["gpus"]
          matchAttribute: "gpu.nvidia.com/nvlinkDomain"
---
apiVersion: batch/v1
kind: Job
metadata:
  name: distributed-training-nvlink
spec:
  template:
    spec:
      restartPolicy: Never
      resourceClaims:
        - name: gpus
          source:
            resourceClaimTemplateName: four-nvlink-connected-gpus
      containers:
        - name: trainer
          image: nvcr.io/nvidia/pytorch:24.12-py3
          command:
            - torchrun
            - --nproc_per_node=4
            - train.py
          resources:
            claims:
              - name: gpus
```

## 工程启示

这种架构只需要一个清单文件。它消除了脆弱的节点选择器，也不再需要为每一代新硬件重复定义任务。随着 GPU 集群变得越来越异构，混合了 H100、B200、B300 以及未来出现的任何芯片，旧的基于整数的调度模型已经失效。DRA 代表了 Kubernetes 终于走向成熟，能够支持生产级 AI 工作负载的细微差别和现实需求。