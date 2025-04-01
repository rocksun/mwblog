<!--
title: NVIDIA开源KAI调度器，助力AI团队优化GPU利用率
cover: https://cdn.thenewstack.io/media/2025/03/38e95859-nvidia-gtp-logo-scaled.jpg
summary: NVIDIA开源KAI Scheduler，专为AI工作负载优化GPU资源！支持Kubernetes，集成Kubeflow、Ray、Argo等云原生框架，实现GPU共享、动态配额调整。实时调度策略如组调度、分层排队提升GPU利用率，解决AI模型训练和推理难题！
-->

NVIDIA开源KAI Scheduler，专为AI工作负载优化GPU资源！支持Kubernetes，集成Kubeflow、Ray、Argo等云原生框架，实现GPU共享、动态配额调整。实时调度策略如组调度、分层排队提升GPU利用率，解决AI模型训练和推理难题！

> 译自：[NVIDIA Open Sources KAI Scheduler To Help AI Teams Optimize GPU Utilization](https://thenewstack.io/nvidia-open-sources-kai-scheduler-to-help-ai-teams-optimize-gpu-utilization/)
> 
> 作者：Frederic Lardinois

在KubeCon Europe上，NVIDIA今天宣布开源[KAI Scheduler](https://github.com/NVIDIA/KAI-scheduler)，这是一个以GPU为中心的Kubernetes调度器，最初由Run:ai开发，该公司去年被NVIDIA收购。KAI Scheduler在Apache 2.0许可下发布，可帮助其用户优化GPU集群中AI和机器学习工作负载的GPU资源分配。

NVIDIA认为，传统的资源调度器不太适合管理AI工作负载，因为GPU需求可能会发生很大变化，包括突发推理工作负载和可持续数天的模型训练运行。

KAI Scheduler承诺为这些团队提供更好的工具来管理这些工作负载，其中包括实时动态调整配额和限制，同时还提供各种调度策略——组调度、分层排队、装箱、分散和GPU共享——以避免长时间等待访问GPU。

GPU共享看起来将是一个特别有用的功能。例如，这允许多个Pod使用同一个GPU。值得注意的是，NVIDIA已经提供了一个名为[GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html)的工具，这是一个用于配置GPU的Kubernetes框架，其中还包括GPU时间分片功能。

然而，GPU Operator非常注重与NVIDIA硬件和大型集群（包括NVIDIA自己的DGX机架）配合使用，而KAI Scheduler更具供应商不可知性，并且还支持CPU上的AI工作负载。

除了GPU共享之外，KAI Scheduler的方法侧重于单个GPU及其可用的内存。开发人员可以在这里预留一部分内存。但是，没有内存隔离。

默认情况下，KAI Scheduler与流行的AI工具和云原生框架集成，如Kubeflow的Training Operator、Ray和Argo。

KAI Scheduler的代码和文档现在已[在GitHub上提供](https://github.com/NVIDIA/KAI-Scheduler)。Run:ai的很多其他部分也已经是开源的，包括有些相关的[Genv](https://github.com/run-ai/genv) GPU环境和集群管理工具。