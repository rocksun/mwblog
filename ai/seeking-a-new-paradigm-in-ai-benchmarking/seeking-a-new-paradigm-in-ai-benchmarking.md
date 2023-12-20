<!--
title:  寻求人工智能基准测试的新范式
cover: https://cdn.thenewstack.io/media/2023/12/d785cca0-model-1024x683.jpg
-->

Chakra执行追踪是人工智能/机器学习工作负载的基于图形的表示，旨在统一各种执行追踪模式。

> 译自 [Seeking a New Paradigm in AI Benchmarking](https://thenewstack.io/seeking-a-new-paradigm-in-ai-benchmarking/)，作者 Shashi Gandham 是Meta的软件工程总监，他支持Meta的网络AI团队。他拥有计算机科学博士学位，在行业内有大约20年的经验，涵盖大规模网络、分析等领域...

AI开发潜在地为解决全球一些最紧迫的问题提供了解决方案，并可能有助于为所有人创造更美好的未来。为了构建[AI模型](https://roadmap.sh/guides/introduction-to-llms)并解决这些问题，我们需要尖端的基础设施，而网络是这种基础设施的重要组成部分。这项重要的工作包括优化这些支持[AI/ML计算](https://thenewstack.io/ai/)的广泛网络，推动技术为每个人取得进展。随着规模的增长，性能、部署和运营复杂性都带来了管理网络解决方案的挑战。

例如，基准测试不仅改进当前的AI系统，而且有助于规划未来的网络。我们在 Meta 开发的新基准测试系统可以在其中发挥重要作用，我们认为这是另一个机会，可以请全球的AI技术专业人员共同推动提高AI效率分析和基准测试工具的发展。

作为基准测试的一部分，执行跟踪还提供了其他重要的功能，包括[可视化](https://thenewstack.io/how-opensearch-visualizes-jaegars-distributed-tracing/)和性能优化。在 Meta，我们的[新 Chakra 执行跟踪](https://engineering.fb.com/2023/09/07/networking-traffic/chakra-execution-traces-benchmarking-network-performance-optimization/)是AI/ML工作负载的基于图形的表示，旨在统一各种执行跟踪模式。除了捕捉通信、内存和计算等核心操作外，它还可以捕捉元数据、依赖关系和时间。

我们相信，鼓励并寻求全行业采用可以增强AI效率分析工具，并实现整体性性能基准测试。作为与开放工程联盟MLCommons合作的一部分，Meta已经开源了一个工具包，其中包括各种模拟器、仿真器和重放工具，以便收集、分析、生成和采用Chakra执行跟踪。

## 超越传统基准测试的限制

在很大程度上，[基准测试AI系统意味着运行完整的机器学习工作负载](https://thenewstack.io/what-we-learned-benchmarking-petabyte-scale-workloads-with-scylladb/)。MLCommons的MLPerf和其他已建立的基准测试方法可以提供有用的见解，例如对AI工作负载和系统性能行为的了解。MLPerf已成为在各种加速器上（包括GPU（图形处理单元）、ASIC（专用集成电路）和其他芯片）进行AI应用基准测试的[领先标准](https://thenewstack.io/us-gets-bragging-rights-for-worlds-first-exascale-system/)之一。

然而，在这种完整工作负载基准测试中存在一些固有的挑战。其中包括高计算成本、预测未来系统性能的障碍以及无法适应不断演变的工作负载。

Chakra执行跟踪是建立在我们对传统基准测试限制的深刻认识之上的。通过与MLCommons合作，我们希望推动如此重要的AI工作基准测试的一个关键领域。

![](https://cdn.thenewstack.io/media/2023/12/48c5f497-meta2.jpg)

Chakra工作组，例如，正在策划一个“Chakra跟踪基准套件” —— 收集来自其他贡献者的执行跟踪。此外，该工作组正在帮助解决一种约束，即来自一个系统的跟踪可能无法准确模拟在具有不同网络拓扑、GPU和带宽的系统上。其目标是在多个阶段收集跟踪，包括优化前和优化后，以在任何目标系统上使用。

## Meta、MLCommons和通往未来创新的道路

Chakra工作组只是我们与MLCommons合作的[一个例子](https://www.linkedin.com/posts/aiatmeta_mlcommons-announces-the-formation-of-ai-safety-activity-7127348316362706944-dRfJ?utm_source=share&utm_medium=member_desktop)。我们还是一个新的跨学科团队的一部分，致力于AI安全基准的研究。

为了使AI生态系统繁荣发展，产业共识至关重要。在MLCommons下的Chakra工作组将专注于一系列项目，这些项目有助于打造一个敏捷、可重复的AI基准测试和协同设计系统。无论是开发从各种框架捕获和转换执行跟踪，还是基于MLCommons/MLPerf指南定义具有Chakra执行跟踪的全面基准，我们邀请有兴趣的个人和公司加入我们。

