<!--
title: 云现实正在减缓人工智能的雄心
cover: https://cdn.thenewstack.io/media/2025/05/d0770791-firosnv-photography-z2c6ounf-ie-unsplash-scaled.jpg
summary: AI雄心受限于云现实！企业需重新审视云配置，应对Agentic AI对低延迟的严苛需求。理解AI工作负载特征，优化云基础设施至关重要。需关注多云、数据中心及网络连接，避免单点故障，提升流量路由多样性与冗余。性能效率是关键，优化云资源使用，迎接AI挑战！
-->

AI雄心受限于云现实！企业需重新审视云配置，应对Agentic AI对低延迟的严苛需求。理解AI工作负载特征，优化云基础设施至关重要。需关注多云、数据中心及网络连接，避免单点故障，提升流量路由多样性与冗余。性能效率是关键，优化云资源使用，迎接AI挑战！

> 译自：[Cloud Realities Are Slowing AI Ambitions](https://thenewstack.io/cloud-realities-are-slowing-ai-ambitions/)
> 
> 作者：Mike Hicks

如今，云运营在很大程度上已经成熟。企业对云感到满意：它具有明确的运营角色，并且通过架构最佳实践、社区、知识、可见性和自动化，有足够的支持来以最佳方式在公共、私有或混合云环境中运行大多数数字应用程序和工作负载。

此外，云技术已成为广泛访问 AI 的关键。在过去，只有少数几家私营公司能够获得运行生成式 AI 工作负载所需的高性能计算能力。云正在被证明是一个伟大的均衡器，使这种级别的计算能力以及使用它的 AI 服务可供所有希望使用它的人使用。

但这需要付出代价。不一定是经济上的，尽管它是决策中的一个因素。更大的代价是云优化方法。简而言之，广泛而深入的 AI 采用开始将组织推向云配置方面的舒适区之外。需要采取有针对性的行动才能再次对云感到满意。

## 了解 AI 特征

要了解为什么云[运营中的既定规范正在受到考验](https://thenewstack.io/who-should-run-tests-on-the-future-of-qa/)，首先必须了解云现在被要求驱动的 AI 工作负载的性质。

AI 工作负载非常强大，无论是在它们可以为企业带来的价值方面，还是在以规模运行它们所需的计算资源方面。

随着 Agentic AI 成为企业环境中遇到的主要 AI 类型，这种情况只会增加。[Agentic AI 标志着 AI 技术与业务流程更紧密的集成](https://thenewstack.io/agentic-ai-and-a2a-in-2025-from-prompts-to-processes/)，自主或半自主软件代理处理关键流程或这些流程的部分，以满足特定目标。这些系统可以做出快速决策、管理复杂任务并适应不断变化的环境，前提是底层系统性能良好，但我们稍后会讨论这一点。

企业需要了解的是，[Agentic AI](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/) 比其他形式的 AI 更具交互性——不断与源系统、数据存储库、外部工具、数据库和 API“对话”，这使其成为对延迟更敏感的人工智能技术演进。云或连接中断或故障可能导致代理主导的流程无法启动或实现其预期目标。

关于 AI 工作负载，需要理解的主要一点是，它们与用于[定义云运营](https://thenewstack.io/defining-low-data-loss-downtime-tolerances-in-kubernetes/)参数的工作负载具有不同的特征。这意味着过去为使[数字应用程序或工作负载在云中以最佳方式运行](https://thenewstack.io/driving-digital-experiences-via-cloud-native-applications/)而做出的决策并不总是适用于 AI。今天的云设置并非旨在满足一组非常不同的需求，也并非旨在如此。

对于企业而言，很明显，必须重复投入到为数字环境优化云设置的相同努力，才能为 AI 优化云设置。

企业有责任理解和捕获其不同 AI 工作负载的特征，以便可以对[支持云基础设施](https://thenewstack.io/terraform-beta-supports-multicloud-complex-environments/)进行架构设计和配置，以满足不断变化的性能需求。

## 这在云中会是什么样子

对于大多数企业而言，AI 及其利用的源系统在多个云、数据中心以及由自有和非自有连接链路组成的复杂网络中运行。

并非所有 AI 服务都将在本地区域或区域中可用，这可能是企业选择 AI 模型的一个首要因素。

从卓越运营的角度来看，企业需要确定支持 AI 服务的基础设施及其用户的位置，以了解云环境是否可以支持这些需求，或者是否需要进行更改。
这包括了解人工智能暴露于“通用”基础设施的程度，例如大量流量通过单条光纤链路传输，或者通过高密度数据中心内的存在点等单个聚合点传输，这些数据中心集中了大量人工智能服务提供商。鉴于人工智能日益关键的作用，这种集中风险和[单点故障](https://thenewstack.io/james-webb-space-telescope-and-344-single-points-of-failure/)可能超过内部风险承受能力。

企业必须了解其人工智能[服务交付链的运作方式](https://thenewstack.io/top-costly-cloud-mistakes-and-how-to-sidestep-them/)。提供商如何在某些传输或切换点优先处理流量？他们是否执行自己的负载均衡？这将如何影响人工智能服务交付？这些问题的答案可能会促使企业重新构建其云设置，以实现流量路由多样化并提高冗余选项。

这些决策将影响性能效率。对于基本生成式人工智能应用程序，例如用户提出问题并期望获得上下文响应，50 毫秒的往返响应时间可能是可以接受的。但是对于[繁忙的 Agentic AI 系统](https://thenewstack.io/system-two-ai-the-dawn-of-reasoning-agents-in-business/)，如果每个查询响应都需要 50 毫秒，那么速度会很快。用户可能会因此遇到过多的事务处理时间、超时或其他与拥塞和延迟相关的问题。

企业可以通过主动识别流量和云资源使用的优化机会来提高[性能效率](https://thenewstack.io/3-legs-of-cloud-efficiency-cost-performance-and-velocity/)。