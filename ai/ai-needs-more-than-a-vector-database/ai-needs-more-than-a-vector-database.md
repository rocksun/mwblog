
<!--
title: AI 需要更多，不仅仅是向量数据库
cover: https://cdn.thenewstack.io/media/2024/09/9f601520-vectors123.png
-->

AI 数据库是一个多功能平台，它管理结构化和非结构化数据，并将 AI 模型应用于各种数据格式。

> 译自 [AI Needs More Than a Vector Database](https://thenewstack.io/ai-needs-more-than-a-vector-database/)，作者 Tim Young。

正如 Google Trends [数据](https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=vector%20database&hl=en) 所示，人们对向量数据库的兴趣正在激增。在最新的报告“[向量数据库概览，2024 年第二季度](https://www.forrester.com/report/the-vector-databases-landscape-q2-2024/RES180797)”中，Forrester [强调](https://www.datanami.com/2024/05/14/forrester-slices-and-dices-the-vector-database-market/)了 20 多个向量数据库，并将它们分为两大类：专门的原生 [向量数据库](https://thenewstack.io/vector-databases-where-geometry-meets-machine-learning/) 和将向量存储集成到更广泛数据生态系统中的多模态数据库。

原生向量数据库旨在实现最佳规模和性能，而多模态数据库则提供处理多种数据类型的灵活性，从而降低了管理独立系统的复杂性。要深入了解领先的原生向量数据库，请参阅“[GigaOM 关于向量数据库的声纳报告](https://content.vespa.ai/gigaom-report-2024)”。

向量数据库是一种专门的数据库，旨在存储、管理和查询高维向量，这些向量对于通过语义相似性检索内容的应用程序至关重要。

向量数据库在 2010 年代后期出现，其兴趣的增长得益于 [生成式人工智能](https://thenewstack.io/ai/)，因为它们能够实现快速准确的相似性搜索，这对于推荐系统、自然语言处理和图像识别等任务至关重要，从而显着提高了人工智能应用程序的质量和多功能性。

虽然向量数据库被认为是生成式人工智能的关键，但向量本身只是更大拼图中的一块。在生成式人工智能中获得相关答案依赖于强大的综合搜索功能，该功能由机器学习算法提供支持，这些算法可以检测历史数据中的模式、预测结果、识别异常并推荐行动。

这必须在数十亿个快速变化的数据点上进行，结果必须在瞬间 (<100 毫秒) 内提供，同时支持大量用户群体，每秒可能执行数千个查询。虽然某些数据可能是向量，但大多数业务应用程序都需要集成和分析非结构化数据（例如 PDF），以及传统的 [结构化数据](https://thenewstack.io/automating-context-in-structured-data-for-llms/) 来生成向量。

鉴于这种复杂性，仅仅关注向量数据库可能会忽略更广泛的图景。根据 Forrester 的说法，您可以选择最佳的向量数据库，但随后必须集成必要的组件，例如机器学习、对非向量数据类型的支持以及用于性能和高并发的工作负载管理。或者，您可以选择一个至少提供更广泛数据类型的多模态数据库，但需要将其与它从未设计为支持的应用程序集相匹配。

## 人工智能数据库的出现

一种新型的数据库正在出现：人工智能数据库。人工智能数据库是一个多用途平台，除了向量之外，还管理结构化和非结构化数据。它将人工智能模型应用于各种数据格式，结合信号以获得更准确的输出。人工智能数据库通过整合模型和数据类型来提高计算效率并支持可扩展性。它通过将相似向量聚类到查询结果中来组织数据，并支持合规性，同时还搜索表格、文本和向量以查找特定值、文档匹配和相似性搜索，以使用人工智能模型生成推断。

人工智能数据库支持三种主要的人工智能模型类型：近似机器学习 (ML) 的函数、自然语言处理 (NLP) 和生成式人工智能。

- ML 模型在历史数据中查找模式以预测趋势、识别异常、对结果进行排名/评分并推荐行动。它们主要选择表格、文本或图像等数据以供进一步使用。
- NLP 模型解释和生成文本或语音，用于翻译或情感分析等任务，主要处理文本文件。
- 生成式人工智能模型根据现有数据生成文本、图像、音频或视频等内容，预测序列中的下一个元素。

这些模型通常在人工智能数据库中托管和运行，它们根据接收到的数据学习模式、进行推断并创建输出。如果您想了解更多关于人工智能数据库的信息，我建议您阅读 BARC 的 [这份报告](https://barc.com/research/multi-faceted-ai-databases/)，以深入了解人工智能数据库。

AI 数据库代表着重大进步，但由于缺乏应用逻辑和运行时管理，它仍然只是一个部分解决方案。为了满足生成式 AI 对规模和延迟的苛刻要求，需要付出大量努力来集成工具并优化运行时性能。最有效的方法是一个平台，它无缝地将数据、应用逻辑和大规模执行结合在一起，提供一个全面的解决方案，以解决所有这些关键需求。

## Vespa：一个开源的 AI 工程师平台

Vespa.ai 是一个开源平台，用于开发和运行针对搜索、推荐、个性化和检索增强生成 (RAG) 的实时 AI 驱动应用程序。Vespa 有效地管理数据、推理和逻辑，支持具有大量数据量和高并发查询率的应用程序。它以托管服务和开源形式提供。
