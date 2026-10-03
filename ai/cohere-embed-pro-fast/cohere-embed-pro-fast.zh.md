**Cohere于周三发布了Embed 5**，为团队提供了使用 Embed 5 Pro 索引数据、并使用更快且更便宜的 Embed 5 Fast 查询相同向量的选项，而无需创建第二个索引。

该公司建议将 Pro 用于索引，将 Fast 用于查询，特别是在 RAG 和智能体会叠加[延迟累积](https://thenewstack.io/agentic-ai-latency-infrastructure/)的智能体工作负载中，因为需要重复搜索相同的数据。

检索质量存在一定的权衡，尽管 Cohere 的测试表明这种权衡相当小。在涵盖文本、图像、融合文档和解析文档的 40 个数据集上，使用 Fast 对 Pro 索引进行查询的得分为 98.4（相对于 Pro 对 Pro 基准的 100）。同时将 Fast 用于索引和查询，该得分会下降至 96.6。Cohere 表示，当 Pro 和 Fast 结合使用时，没有一个单独的数据集出现大幅下降。

## 一个嵌入空间，两个模型

由于 Pro 和 Fast 共享一个嵌入空间，团队可以在它们之间切换，而无需重新对语料库进行嵌入。两者产生相同维度的兼容向量，并且 Cohere 表示，在使用 Matryoshka 截断或 int8 量化时，团队仍然可以混合使用这两者。

> 由于 Pro 和 Fast 共享一个嵌入空间，团队可以在它们之间切换，而无需重新对语料库进行嵌入。

Pro 的价格为每百万个 Token 0.12 美元，而 Fast 的价格为 0.08 美元，在 Cohere 的测试中，平均文档吞吐量是前者的 2.4 倍。对于文档摄入频率低于搜索频率的 RAG 系统，Pro 可以处理进入索引的文档，而 Fast 则可以处理负载大得多的查询流量。

## 用 Matryoshka 缩减向量

这两个模型都支持从 256 到 2,048 的六种向量维度，并提供 float32、int8 和 binary 格式。随着规模的扩大，存储空间的差异变得显着，特别是对于那些已经在[重新思考向量存储位置](https://thenewstack.io/spark-4-2-ai-workloads/)的团队而言。

Cohere 将 2,048 维的 float32 向量大小定为 8 KB，对于 1 亿个分块来说大约是 819 GB。1,024 维的 int8 向量将其缩减至约 102 GB，而 256 维的 binary 向量则将同一语料库缩减至约 3.2 GB。

对于大多数部署，Cohere 推荐使用 1,024 维的 int8，这可以在减少内存和存储的同时，保持接近全精度的检索质量。二进制表示提供了更重的压缩但会有一些精度损失，更适合在更高精度的重排序之前的初始检索阶段。

> 这两个模型都支持从 256 到 2,048 的六种向量维度，并提供 float32、int8 和 binary 格式。

## 超越纯文本的检索

Embed 5 支持跨 100 多种语言的文本、图像和融合的文本-图像输入，并具有 128K-token 的上下文窗口。它可以直接嵌入页面图像，或在单个向量中组合图像和文本输入。

Cohere [报道称](https://docs.cohere.com/changelog/embed-v5)，在其五个数据集的融合文本-图像评估中，Pro 的平均得分为 82.3，而 Fast 为 81.2，Google 的 Gemini Embedding 2 为 61.3。在其解析的 PDF 评估中，Pro 得分为 84.8，其次是 Voyage 4 Large（83.6）、Fast（83.4）和 Gemini Embedding 2（80.8）。

在 ViDoRe V3 上（Cohere 使用基准测试作者策划的解析文本输出而非页面图像进行评估），Pro 的平均得分为 85.8，Fast 为 84.5，相比之下 Voyage 4 Large 为 83.7，Gemini Embedding 2 为 83.2，Cohere 先前的 Embed 4 为 77。

Cohere 的多语言结果并非一边倒，鉴于该公司[最近向机器翻译领域的推进](https://thenewstack.io/cohere-north-translate-sovereignty/)，这一点尤为引人注目。Pro 在其五个语言的欧洲平均测试中以 77 分领先（Voyage 4 Large 为 76 分，Gemini Embedding 2 为 73 分），但在九项测试中落后于 Gemini Embedding 2。

## 解读基准测试的细则

基准测试结果需要一些背景信息，因为 Embed 5 是 Cohere 第一个使用 RCP-nDCG@10 进行评估的模型系列，该系列使用特定于查询的相关性标准，而不是固定的相关性标签。

Cohere 表示，这种方法可以捕捉到原始基准测试标签遗漏的相关结果，但 RCP-nDCG@10 衡量的是固定候选集上的重排序，而不是来自完整语料库的第一阶段检索。

第一阶段检索使用标准的 nDCG 和 Recall 进行单独评估，而融合文本-图像、页面图像和跨模型测试使用标准的 nDCG@10，因此报告的得分在不同的评估之间无法直接进行比较。

## 将索引与服务分离

Embed 5 中更重要的改变是将索引和服务视为[独立的架构决策](https://thenewstack.io/ai-agent-retrieval-infrastructure/)的能力。可以对相同的语料库进行索引以获得检索质量，同时将查询路径优化为高吞吐量和低延迟，而无需维护两个数据表示。

Cohere 的 98.4 分表明，Pro-to-Fast 设置在其测试中牺牲的检索质量相对较小，尽管该数字是跨 Cohere 自己的评估套件取平均值。生产环境中的 RAG 和智能体系统仍然需要在其自己的语料库和查询分布上对 Pro-to-Fast 与 Pro-to-Pro 进行基准测试，特别是当检索错误可能会贯穿智能体工作流的多步时。

Embed 5 Pro 和 Fast 通过 Cohere 的 API 和 Model Vault、Microsoft Foundry 以及 Amazon SageMaker 提供，并通过 vLLM 支持私有 VPC 和本地部署。

> 生产环境中的 RAG 和智能体系统仍然需要在其自己的语料库和查询分布上对 Pro-to-Fast 与 Pro-to-Pro 进行基准测试，特别是当检索错误可能会贯穿智能体工作流的多步时。