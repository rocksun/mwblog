<!--
title: 针对更快AI工作负载定制的Google Kubernetes Engine
cover: https://cdn.thenewstack.io/media/2025/04/5f20cb6b-google-next-25.png
summary: GKE重磅升级！🚀推出 Gateway API Inference Extension，智能路由LLM，吞吐量飙升40%，尾部延迟暴降60%！更有Cluster Director加持，打造AI超级计算，单作业可达65000个GPU/TPU！Gemini Cloud Assist Investigations 助你debug， Kubernetes已成AI超能力！
-->

GKE重磅升级！🚀推出 Gateway API Inference Extension，智能路由LLM，吞吐量飙升40%，尾部延迟暴降60%！更有Cluster Director加持，打造AI超级计算，单作业可达65000个GPU/TPU！Gemini Cloud Assist Investigations 助你debug， Kubernetes已成AI超能力！

> 译自：[Google Kubernetes Engine Customized for Faster AI Work](https://thenewstack.io/google-kubernetes-engine-customized-for-faster-ai-work/)
> 
> 作者：Joab Jackson

拉斯维加斯 - Google Cloud 正在[积极准备](https://thenewstack.io/kubecon-europe-how-google-will-evolve-kubernetes-in-ai-era/)大规模 AI 工作负载，并使用 Kubernetes 作为平台来实现这一目标。

本周，在该公司的 [Google Cloud Next](https://cloud.withgoogle.com/next/25) 大会上，[Google](https://cloud.google.com/?utm_content=inline+mention) 推出了一系列针对 [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine) (GKE) 的增强功能，所有这些功能都旨在简化 AI 工作负载。

该公司还推出了其基于 GKE 的托管超级计算服务，为 AI 工作负载提供特殊便利。

许多公司已经拥有一些 Kubernetes 专业知识，可以运行其基础设施，因此使用相同的人才来开始他们的 AI 之旅也是有意义的，Google 云运行时副总裁兼总经理 [Gabe Monroy](https://www.linkedin.com/in/gabemonroy/) 在 TNS 采访中表示。

“您的 Kubernetes 知识和专业知识不仅相关，而且是您的 AI 超能力，”Monroy 说。

它的许多客户已经开始走上这条道路。在过去的一年中，该公司面向 AI 的 GPU 和 TPU 的使用量增长了 900%。Monroy 自豪地说，其所有 15 家顶级 GKE 客户现在都在使用该服务进行 AI 和机器学习 (ML) 工作负载。

该公司预计，到 2028 年，仅 AI 每年将产生超过 2000 亿美元的基础设施云服务收入。

GKE 的增强功能包括支持新兴的 Kubernetes 标准，称为 [Gateway API Inference Extension](https://thenewstack.io/kubecon-europe-kgateway-aims-to-be-the-kubernetes-onramp/)，这将有助于更好地将 AI 工作负载与 Kubernetes 资源配对。

一种名为 Cluster Director 的新型 GKE 超级计算服务，还将 GKE 机器连接到巨型超级计算模式中，使它们能够处理大型 AI 建模作业。

为了防止出现问题，这家云计算公司在其 GKE 管理仪表板上安装了基于 Gemini AI 的聊天客户端 Gemini Cloud Assist Investigations，它可以在其中调试问题。

## 将负载均衡器设置为“AI”

GKE Inference Gateway 现已推出公开预览版，它使用正在开发中的 [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) (CNCF) 的 Gateway API Inference Extension，为 AI 推理工作负载提供智能路由和负载均衡。

CNCF 的 [Gateway API Inference Extension](https://gateway-api-inference-extension.sigs.k8s.io/faq/) 将任何 Kubernetes 网关变成“推理网关”，从而能够使用训练模型优化设置来更好地进行负载均衡。

对于使用 Kubernetes 运行其大型语言模型 (LLM) 的推理平台团队来说，这种扩展将特别令人感兴趣。

如今，他们必须与通用负载均衡器作斗争，这些均衡器在处理不可预测的推理流量方面表现不佳。罪魁祸首是什么？可变的响应时间。一些简短的问题需要很长的答案。或者反之亦然。或者两者都不是。它使负载均衡器的预测能力变得疯狂。

另一个挑战：多个模型。

在任何蓬勃发展的 AI 环境中，“您需要管理许多不同版本的模型，并且您必须实际管理跨所有这些不同模型的路由，”Monroy 说。“今天的负载均衡基础设施根本无法胜任这种工作。”

由于采用了标记方案，该网关具有“模型感知”能力，因此针对智能路由进行了优化，能够区分所托管模型的不同版本。

为了提高性能，该网关具有“请求调度算法”，可以跟踪节点利用率，并可以相应地调整工作负载，“避免随着负载增加而出现驱逐或排队”，正如 GitHub [文档](https://github.com/kubernetes-sigs/gateway-api-inference-extension) 中所述。

该扩展还添加了一些其他好处，例如端到端可观测性 (obserablity) 和工作负载隔离。

Monroy 声称 GKE 是第一个实现 CNCF 推理扩展的。相当雄心勃勃的是，截至发稿时，最新版本是 [0.40](https://github.com/kubernetes-sigs/gateway-api-inference-extension/releases/tag/v0.3.0)。

但在这种实现中，Google 估计，GKE 的推理网关可以将吞吐量提高 40%，将尾部延迟降低高达 60%，并将服务器成本降低高达 30%。

## 虚拟超级计算

对于 Google Next，该公司已正式推出其超级计算服务。

GKE 的 Cluster Director 是一个新的服务平台，它模仿[超级计算机](https://thenewstack.io/xs-colossus-supercomputer-changes-the-sc500-performance-game/)的运行方式（它以前被称为 [Hypercompute Cluster](https://cloud.google.com/ai-hypercomputer/docs/hypercompute-cluster)），允许用户将多个虚拟机（包括计算、存储和网络）作为一个单元进行部署。

用户可以在单个作业上放置最多 65,000 个 GPU 或 TPU 的集群。自动修复可以修复作业期间出现故障的任何节点。

Kubernetes 编排器可以感知到有故障的集群，并在必要时将工作负载移动到另一个实例。使用 Google Cloud 的 [NodeLabels](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeLabels)，它可以根据可用的最佳拓扑来调度工作负载。

最重要的是，超级计算机可以通过使用标准的 Kubernetes API 在 GKE 中完全运行。为了使用 GKE 构建一个 AI 优化的集群，Google 提供了一组可配置的蓝图。Google 本身使用 GKE 来支持其最近推出的 [Vertix AI](https://cloud.google.com/vertex-ai) 企业 ML 服务。

虽然该服务具有 AI 扩展，但 Google 将 Cluster Director 视为独立高性能计算机的通用替代品，即迄今为止[在很大程度上是](https://thenewstack.io/sc500-microsoft-now-has-the-third-fastest-computer-in-the-world/)[巨大的裸机机器](https://thenewstack.io/top500-chinas-supercomputing-silence-aggravates-tech-cold-war-with-u-s/)定制构建的。

这就是 Google 现在所说的[传统超级计算机市场](https://top500.org/)。这些客户需要数百万个内核，这些内核可以组合在一起以执行单个任务，例如金融服务运行大型蒙特卡罗模拟以进行风险计算。

该公司专注于“goodput”，即 HPC 为应用程序提供的有用内容的数量。用训练术语来说，goodput 等于“在训练运行中取得进展的时间百分比”，Monroy 说。

借助 Cluster Director，Google 的目标是 99%。