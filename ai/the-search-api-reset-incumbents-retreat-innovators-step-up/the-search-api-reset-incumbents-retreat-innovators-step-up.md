
<!--
title: 搜索API大洗牌：巨头退守，创新者崛起
cover: https://cdn.thenewstack.io/media/2025/11/8e80d61d-search.jpg
summary: 搜索API格局变化，谷歌微软限制访问，旨在引导AI生态内检索。Perplexity等新玩家涌现，提供AI原生搜索API，市场围绕AI重建搜索。
-->

搜索API格局变化，谷歌微软限制访问，旨在引导AI生态内检索。Perplexity等新玩家涌现，提供AI原生搜索API，市场围绕AI重建搜索。

> 译自：[The Search API Reset: Incumbents Retreat, Innovators Step Up](https://thenewstack.io/the-search-api-reset-incumbents-retreat-innovators-step-up/)
> 
> 作者：Tim Young

[搜索格局](https://thenewstack.io/why-ai-search-platforms-are-gaining-attention/)正在发生变化。近几个月来，微软宣布Bing搜索API退役，而谷歌则将其API限制为每次查询最多10个结果。这些举动标志着网络主导搜索提供商在看待数据访问方式以及谁可以在其基础上进行构建方面发生了显著变化。

十多年来，像Bing和Google自定义搜索这样的[搜索API](https://thenewstack.io/why-api-first-matters-in-an-ai-driven-world/)一直是网络基础设施的一部分。开发者利用它们检索网页结果、图片和新闻，而无需维护自己的索引。企业已将它们嵌入到客户支持、知识库和市场情报等应用程序中，以提供外部上下文。初创公司和研究团队利用它们收集训练数据、为语言模型提供基础或进行竞品分析，而无需运行自己的爬虫。

简而言之，搜索API提供了一种以编程方式访问开放网络的简单方法，弥合了消费者搜索和企业信息检索之间的鸿沟。

## AI转型

生成式AI的兴起改变了[搜索基础设施需要提供什么](https://thenewstack.io/enterprise-ai-search-vs-the-real-needs-of-customer-facing-apps/)。随着[检索增强生成（RAG）](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/)在AI系统中变得核心，开发者现在需要在AI管道内拥有灵活的检索层，而不仅仅是返回链接。

在此背景下，微软和谷歌的决定时机显得尤为突出。微软已通过其针对AI代理的“Bing搜索基础功能”（Grounding with Bing Search）将搜索访问集成到Azure的AI堆栈中，而谷歌则继续减少对其自身搜索结果的外部可见性。将每次调用查询限制为10个结果，符合其长期以来最小化批量数据提取和自动化抓取的目标。

其商业考量很明确：两家公司都在引导开发者从大规模、开放的检索转向在其自身生态系统内通过AI介导的访问。提供完整的结果集成本高昂，且通常被SEO平台、数据挖掘工具或研究爬虫等自动化系统使用，而非交互式用户。限制API有助于控制这些成本，同时将网络数据重新定位为更高级AI服务的受控资源。

## 重置而非撤退

这并非搜索的崩溃，而是控制权的重新调整。过去开放的、基于列表的API属于一个以原始结果为产品的时代。在生成式AI时代，现有巨头正在围绕答案、基础和上下文重新定义搜索，并与他们的云生态系统紧密结合。

但随着大型提供商的退出，新玩家正在涌入。Perplexity和Parallel代表了为AI工作负载设计的新一代搜索API。它们发布基准测试，开放API，并强调检索质量和低延迟，这些是在RAG和代理系统中最关键的性能特征。你可以在[这里](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-search-api)阅读更多关于Perplexity搜索API的信息。

Perplexity还展示了它在RAG式任务的[相关性方面优于谷歌](https://medium.com/@evolutionaihub/whats-new-in-perplexity-s-search-api-that-just-killed-google-s-edge-b95047ada22e)。为了不甘落后，由Twitter前首席执行官Parag Agrawal创立的Parallel，最近利用Perplexity自己的评估工具[报告了优于Perplexity的结果](https://x.com/paraga/status/1971650814705127438)。

## 市场火爆，新基础涌现

搜索API市场再次升温，这次围绕着AI原生基础设施。Perplexity和Parallel的底层都有一个共同组件：Vespa，一个为大规模检索、排名和机器学习推理而构建的开源引擎。

Vespa在这些系统中的作用反映了架构上的一个更广泛的转变：搜索基础设施现在已成为AI堆栈本身的一部分。随着模型越来越依赖检索，性能、可扩展性以及结合[结构化和非结构化数据](https://thenewstack.io/automating-context-in-structured-data-for-llms/)的能力等因素已成为关键的差异化因素。

现有巨头正在收窄访问权限；创新者则正在扩展它。无论如何，搜索再次成为网络组织方式的中心，只不过这一次，它是为AI而重建的。