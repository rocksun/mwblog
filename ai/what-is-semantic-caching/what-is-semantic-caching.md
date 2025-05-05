
<!--
title: 什么是语义缓存？
cover: https://cdn.thenewstack.io/media/2025/05/c614771a-semantic-caching-2.jpg
summary: AI成本高企？试试语义缓存！通过存储LLM的提示和响应，减少API调用，降低延迟，提升性能。类似CDN，核心在于语义相似性引擎。Redis等已推出相关工具如LangCache。结合RAG、多Agent等优化策略，或将改变AI开发格局！
-->

AI成本高企？试试语义缓存！通过存储LLM的提示和响应，减少API调用，降低延迟，提升性能。类似CDN，核心在于语义相似性引擎。Redis等已推出相关工具如LangCache。结合RAG、多Agent等优化策略，或将改变AI开发格局！

> 译自：[What Is Semantic Caching?](https://thenewstack.io/what-is-semantic-caching/)
> 
> 作者：Bill Doerrfeld

对 AI 提供商的 API 请求可能会产生相当可观的费用。Barclay 的分析师发现，根据 Business Insider 的报道，OpenAI 的 o3-high 模型的单个提示产生了 3,500 美元的费用，比其前代模型需要多 1,000 个 token。

大多数开发人员都知道[缓存](https://thenewstack.io/is-a-database-caching-layer-still-necessary/)是什么。但语义缓存是 AI 的新事物。随着 AI 成本的上升，以及开发人员寻求更简洁的设计以避免一遍又一遍地 ping AI 服务器来处理冗余查询，它将变得更加重要。

[Fastly](https://www.fastly.com/) 技术研究和孵化副总裁 [Randy Reddig](https://www.linkedin.com/in/ydnar/) 告诉 The New Stack：“每个人都会关注他们的 AI 成本结构、延迟和性能。OpenAI 甚至建议您对其输出执行某种缓存。”

好处是显而易见的：[2024 年的一项研究](https://arxiv.org/pdf/2411.05276)发现，语义嵌入缓存可以显著减少延迟，并在各种查询类别中将 API 调用减少高达 68.8%。

但究竟什么是语义缓存，又该如何实现它呢？下面，我们将在[大型语言模型 (LLM)](https://thenewstack.io/llm/) 和 API 的背景下，探讨语义缓存、它的优点和可能的缺点，以及它如何融入更广泛的 AI 开发实践中。

## 语义缓存建立在标准缓存之上

缓存是存储频繁访问的信息以避免加载时间过长、减少服务器请求并改善用户体验的过程。服务器端和浏览器端缓存是设计 [Web 应用程序和 API](https://thenewstack.io/why-http-caching-matters-for-apis/) 时的基本策略。

语义缓存和您典型的 Web 缓存非常相似。两者都访问存储的数据以减少不必要的调用。不同之处在于，语义缓存存储和检索对 AI 服务器的提示和响应，例如来自 [OpenAI](https://thenewstack.io/introduction-to-the-openai-agents-sdk-and-responses-api/)、[Google](https://cloud.google.com/?utm_content=inline+mention) [Gemini](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/)、[Anthropic](https://www.anthropic.com/) 等的 LLM。

语义缓存的工作原理：

- 用户向基于 LLM 的 AI 代理发送聊天。
- 一层拦截请求并执行语义分析，以确定该请求是否与之前发出的任何提示匹配。
- 如果系统找到合适的提示，它会快速返回缓存的响应。
- 如果不存在类似的提示，它会将请求传递到 AI 服务器进行处理。

虽然检索增强生成 (RAG) 通过访问外部数据来补充 LLM 查询，但语义缓存的独特之处在于，它通过从数据库（可以是本地存储或外部存储）中提取数据来完全避免进一步的查找。

根据 Fastly 的 Reddig 的说法，语义缓存与[内容分发网络 (CDN)](https://thenewstack.io/the-modern-cdn-means-complex-decisions-for-developers/) 或网关的工作方式没有太大区别。秘诀在于确定语义相似性的引擎。

Fastly 的 Reddig 说：“许多请求的措辞略有不同，但它们的响应应该相对相同。”例如，他说，不同的用户经常提出类似的要求，例如比较咖啡类型或询问为四口之家推荐的最佳汽车。

在 Fastly 的案例中，其 AI Accelerator 会解析新请求，并将每个请求与 Fastly 托管在其分布式、低延迟边缘网络上的 LLM 交互的大型向量数据库进行比较。然后，它会返回具有高置信度级别的响应，以将类似的查询发送到客户端应用程序。不匹配的查询将转发到 LLM API。

其他平台也在解决 AI 缓存问题。例如，内存数据存储和缓存系统 [Redis](https://redis.com/?utm_content=inline+mention) [最近推出了](https://thenewstack.io/redis-launches-vector-sets-and-a-new-tool-for-semantic-caching-of-llm-responses/) LangCache，用于缓存 LLM 响应，以及一种用于存储和查询向量嵌入的新数据类型。

## 结果：更低的成本和更好的性能

迄今为止，AI 需要大量的基于 GPU 的处理。根据 [McKinsey & Company](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/ai-power-expanding-data-center-capacity-to-meet-growing-demand) 的数据，到 2030 年，AI 可能会使全球数据中心容量需求增加两倍。
Reddig 认为高成本源于与 AI 模型交互的低效率。当 LLM 处理提示时，它必须对请求进行分词，以及其他上下文，例如项目提示、文件和从 RAG 中提取的数据，并将其发送到 LLM 以合成和生成响应。后续请求然后在内存中使用此上下文，并在每次请求时重新对其进行分词。

“提示的总成本与 token 的数量有关，并且重复地顺序处理这些 token 最终会消耗大量资源，”Reddig 说。“对于非常长的查询，或者带有大量上下文的短查询，在成本、CPU、功耗和时间方面，这将是一个更昂贵的查询处理过程。”

语义缓存可以完全避免启动对 AI 服务器的新 LLM 调用，从而避免繁重的 CPU 需求。通过调用更多本地数据，您可以避免长时间的等待并减少往返调用，从而提高吞吐量。

根据 [Fastly’s benchmarks](https://www.businesswire.com/news/home/20241216172993/en/Fastly-AI-Accelerator-Helps-Developers-Unleash-the-Power-of-Generative-AI)（Fastly 的基准测试），与直接 OpenAI 服务器调用相比，语义缓存设置可将服务器响应时间提高 9 倍。该公司表示，这也是一种低成本的迁移，只需要应用程序开发人员指向一个新的端点来重新路由 API 调用。

## 语义缓存：AI 代理的好帮手

语义缓存是一个新兴领域，确切的用例仍在制定中。也就是说，它在对话式或基于提示的用例中表现最佳。

“产生自然语言输出的自然语言输入是一个很好的用例，”Reddig 说。他补充说，尽管相同的过程可以支持其他内容类型，如视频和图像。

语义缓存在超特定领域也显示出前景。“如果语义空间狭窄，并且您看到很多常见问题或提示，那么这可能非常合适，”他说。

这些因素使其非常适合在特定上下文中向面向用户的 AI 代理发出查询，例如零售、客户服务或在线购物。在这种情况下，实时响应对于客户体验至关重要，从而提高了对高质量性能的需求。

对于在企业环境中工作的代理来说，响应能力也至关重要。[Archana Kannan](https://www.linkedin.com/in/archkan/)，[Slack product at Salesforce](https://api.slack.com/?utm_content=inline+mention)（Salesforce 的 Slack 产品）高级副总裁告诉 The New Stack：“代理对高质量数据有很大的依赖性，因此他们可以根据准确、及时和上下文相关的信息采取行动。正确的数据和上下文是代理为员工和组织提供真正价值的基础。”

其他人也认为，快速、可靠的数据访问是代理 AI 的基础。[Andre Zayarni](https://www.linkedin.com/in/zayarni)，向量数据库公司 [Qdrant](https://qdrant.tech/) 的联合创始人兼首席执行官告诉 The New Stack：“代理 AI 需要更好的上下文集成、更快的反馈循环和可扩展的编排。当检索速度慢或上下文更新滞后于实时需求时，AI 代理就会遇到瓶颈。”

Zayarni 将语义缓存视为减少冗余查找的一种策略：“如果已经回答了类似的查询，则重用它而不是重新计算。”

## 更广泛的优化策略的一部分

围绕语义缓存还需要进一步创新。Reddig 说，其中之一是改进模型，以避免错误地连接语义相似的提示。不过，他补充说，可以通过提示工程和其他保障措施来缓解这种情况。

从更广阔的角度来看，语义缓存只是难题的一部分——它本身并不能解决幻觉问题和其他低效率问题。因此，需要集思广益（精明的策略）来优化代理 AI。

Zayarni 说：“关键的进步包括用于实时向量摄取的 GPU 加速索引构建、用于减少冗余查找的语义缓存以及混合搜索模型，这些模型融合了密集向量、稀疏术语和元数据过滤器。”他还提到使用多代理系统将某些职责委派给各种代理。

其他人也同意，数据处理和多代理方法的进步对于优化代理 AI 是必要的。Salesforce 的 Kannan 说：“最关键的进步将集中在数据集成、元数据管理和多代理协作方面的改进。”

她补充说：“采用多代理方法可以显着增强优化。专业的环境代理团队可以在幕后进行协作，自主处理复杂的工作流程，集成不同的系统并简化多步骤流程。”
可以说，多代理架构与语义缓存非常互补，因为专用代理可以审查用户查询，以确定语义上相似的查询，并将更深层次的元素交给其他代理来处理。这种移交甚至可以在查询内的语义分割中进行，例如分解用户请求的各个部分并分别路由它们。

最后，有人认为，随着未来模型的发展和 GPU 效率的提高，LLM 的成本将会降低，从而减少对效率提升的需求。但是，随着摩尔定律趋于平缓且推理成本攀升，语义缓存正逐渐成为一种减少冗余的有用方法。

## 语义缓存改变游戏规则

正如 CDN 成为优化 Web 性能的标准实践一样，Reddig 预测客户端和 LLM API 之间的缓存层将成为新 AI 开发的默认设置。

迄今为止，高计算需求阻碍了中小型公司在公平的竞争环境中竞争。但他希望语义缓存能够降低 AI 开发的成本，以与[台积电 (TSMC)](https://www.tsmc.com/) 曾经通过处理昂贵的制造来为芯片设计师实现民主化的方式相同，实现访问的民主化。

正如过去的突破降低了门槛一样，语义缓存可能会对新兴市场产生类似的连锁反应。正如 Reddig 所说，“在使用现有成本结构不可能实现的使用现在变得更有可能。”