<!--
title:Kubernetes驱动3500个GPU的AI训练
cover: https://cdn.thenewstack.io/media/2023/11/20ad2637-peter_salanki-1024x768.jpg
-->

Kubernetes让GPU集群管理变得更加高效，这是CoreWeave公司Peter Salanki在KubeCon大会上的观点

> 译自 [HPC Kubernetes: AI Training on 3,500 GPUs](https://thenewstack.io/hpc-kubernetes-ai-training-on-3500-gpus/)，作者 Joab Jackson 是 The New Stack 的高级编辑，负责报道云原生计算和系统操作。他已报道 IT 基础设施和开发长达 25 余年，包括 IDG 和政府计算机新闻的工作。在此之前，他... 阅读更多来自 Joab Jackson 的文章

到目前为止，Kubernetes 在[高性能计算](https://thenewstack.io/high-performance-computing-is-due-for-a-transformation/)(HPC)或[超级计算领域](https://thenewstack.io/us-gets-bragging-rights-for-worlds-first-exascale-system/)中基本避开。

但随着机器学习如今对 [GPU 的高额需求](https://thenewstack.io/free-gpus-and-ai-chips-are-available-to-run-ai/)，Kubernetes 可以通过起源于 HPC 领域的工具来提供更动态的方式，管理庞大的 GPU 集群。

证明这点的云提供商 [CoreWeave](https://www.coreweave.com/) 就专注于加速 GPU 工作负载。

6 月，该公司在 [MLCommons](https://mlcommons.org/) 的 [MLPerf](https://mlcommons.org/benchmarks/training/) 的第三轮测试中名列榜首。这是用于[衡量和比较系统在训练和推理任务上的性能的基准测试](https://hds.harvard.edu/sites/hwpi.harvard.edu/files/vlsiarch/files/mlperf_an_industry_standard_benchmark_suite_for_machine_learning_performance.pdf)。CoreWeave 启动了一个集群，包含 3,500 个(新发布的)[Nvidia H100 GPU](https://www.nvidia.com/en-us/data-center/h100/)，其性能是其他 Kubernetes 集群的 29 倍。

与传统的 HPC 系统不同，CoreWeave 使用裸机上的 Kubernetes 运行服务。

Kubernetes 对[管理 GPU](https://thenewstack.io/managed-k8s-with-gpu-worker-nodes-for-faster-ai-ml-inference/) 有诸多优点，包括使增添新功能变得容易，以及无需在专有系统和 Kubernetes 自己之间构建“胶水”代码就可以获得指标。CoreWeave 工程总监 [Peter Salanki](https://www.linkedin.com/in/salanki/) 在 [KubeCon+CloudNativeCon 2023](https://thenewstack.io/tim-hockin-kubernetes-needs-a-complexity-budget/) 的[演讲中](https://kccncna2023.sched.com/event/1Tbu4)指出。

“在Kubernetes周围建立一个生态系统，使我们可以很容易地插接新东西并[获取指标](https://thenewstack.io/prometheus-at-10-whats-been-its-impact-on-observability/)数据，而无需在专有系统与Kubernetes本身之间构建大量集成组件，”Salanki说。

![](https://cdn.thenewstack.io/media/2023/12/73096aa5-coreweave-01.png)

## 裸金属上的 Kubernetes

所有 GPU 位于一个数据中心，每个服务器有八个 GPU，基于 Intel Sapphire Rapids 平台。它们全部由 40 英里长的 Infiniband 光纤和 40,000 条连接组成，在互连上达到最低延迟。

这个数字值得注意，因为大型机器学习工作负载(MLPerf 对其建模)可以跨所有可用 GPU 达到最大性能。但是，如果这些组件中的任一个宕机，整个作业必须从最后一个检查点重新启动。

“任何单个故障对作业来说都可能是灾难性的，”Salanki 说。“所以确保节点健康和整个结构健康非常关键，不至于丧失性能。”

所有内容都是无状态启动的 —— 服务器上没有任何操作系统。

“这些系统在交付时没有任何操作系统。我们不希望它们与供应商一起交付任何操作系统，因为事情在不断变化，我们有新的内核要部署，新的 CPU，所以我们实际上不能期望工厂中预装的任何东西都可以工作，”Salanki 说。

![](https://cdn.thenewstack.io/media/2023/12/8ce10f86-coreweave-02.png)

每台服务器都配备了 [Nvidia Bluefield](https://www.nvidia.com/en-us/networking/products/data-processing-unit/) 数字处理单元([DPU](https://blogs.nvidia.com/blog/whats-a-dpu-data-processing-unit/))，这是网络卡上的处理器(也由 Kubernetes 管理)。

启动时，DPU 会下载一个裁剪过的 Ubuntu 镜像，除了 [GPU 和 Infiniband 驱动程序](https://thenewstack.io/nvidia-does-the-unexpected-open-sources-gpu-drivers-for-linux/)以及 Kubelet 之外几乎没有任何内容。然后它会请求一个加入令牌并加入 Kubernetes 集群。(DPU 还为每个工作负载提供 [VPC 隔离](https://thenewstack.io/multicluster-deployment-strategies-with-the-kubernetes-gateway-api/)，以支持多租户环境。) 

“一切都是无状态的，”Salanki 说。“它是完全临时的，这意味着我们可以即插即用您的节点并立即在 Kubernetes 集群上运行。”

## Kubernetes 上的 Slurm 

为了运行MLPerf，CoreWeave使用了[Slurm](https://thenewstack.io/kubernetes-evolution-from-microservices-to-batch-processing-powerhouse/)(一个在HPC领域内研究人员所熟知的调度程序，尽管在K8s环境中很少被使用)。

因此，该公司在Kubernetes上创建了一个Helm chart来调度[Kubernetes上的Slurm](https://www.coreweave.com/blog/sunk-slurm-on-kubernetes-implementations)（
），它将在2023年年初以开源的形式发布。所有Slurm组件都被容器化了，包括守护进程、控制器和日志节点。

通过SUNK，Slurm充当Kubernetes的插件调度程序。在同一集群上，训练作业可以在Slurm上运行，与此同时，长时间运行的生产推理工作负载可以由Kubernetes本身更有效地处理，并且可以预占Slurm作业。

在他的演讲中，Salanki还详细介绍了两个节点控制器、节点测试和自动故障修复。以下是[完整的演讲](https://youtu.be/3E1knT313tI)。

