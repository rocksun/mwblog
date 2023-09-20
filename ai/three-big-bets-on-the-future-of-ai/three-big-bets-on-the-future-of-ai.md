<!--
# 对 AI 未来的三大预测
https://cdn.thenewstack.io/media/2023/09/688e57f8-singlestore-1024x560.png
Feature image via SingleStore
-->


SingleStore 即将举办 Now 大会，开发者将参与如何构建和扩展引人注目的企业级通用 AI 应用的动手实践课程。

译自 [Three Big Bets on the Future of AI](https://thenewstack.io/three-big-bets-on-the-future-of-ai/) 。

Goldman Sachs 在 4 月发布的一份[报告](https://www.goldmansachs.com/intelligence/pages/generative-ai-could-raise-global-gdp-by-7-percent.html)估计，通用 AI 的进步有可能在 10 年内带来约 7 万亿美元(或 7%)的全球 GDP 增加，并将生产率增长提高 1.5 个百分点。这一前景如此清晰地凸显了为通用 AI 的未来做正确抉择的重要性，特别是与数据相关的部分——这无疑是这项技术的核心。

那么，通用 AI 的未来会是什么样的呢？其中很大一部分将是对多个数据源和类型进行秒级整合、汇总和提供上下文。为了发挥最佳效果，通用 AI 将需要获取新鲜、整合后的用于特定应用场景的数据和上下文，而所有这一切都需要在毫秒级的实时快照中完成。让我们更深入地探讨一下我对 AI 未来的三大预测。

## 1. LLM 合体

LLM 或大型语言模型[是](https://www.nvidia.com/en-us/glossary/data-science/large-language-models/)“可以使用非常大的数据集识别、总结、翻译、预测和生成内容的深度学习算法”。LLM 是通用 AI 的[支柱](https://www.computerworld.com/article/3697649/what-are-large-language-models-and-how-are-they-used-in-generative-ai.html)。随着这项技术的不断发展，不会有一个主导市场的通用 LLM。相反，组织将利用 LLM 组合来驱动用例，这在今天已经开始出现。例如，有传言 GPT4 不仅是一个巨大的模型，而是一个由 10 多个不同的模型组成的集合，每个模型具有 1000 亿个参数，全部缝合在一起。因此，企业将必须拥有 LLM 或基础模型的组合来利用。我相信企业将通过利用完成特定任务效果较好的多个基础模型来分散风险和成本。这包括 [Llama 2](https://ai.meta.com/llama/) 和 [Hugging Face](https://huggingface.co/) 等开源 LLM，以及 [OpenAI](https://openai.com/)、[Anthropic](https://www.anthropic.com/) 和 [Cohere](https://cohere.com/?utm_term=cohere&utm_campaign=Cohere+Brand+%26+Industry+Terms&utm_source=adwords&utm_medium=ppc&hsa_acc=4946693046&hsa_cam=20368816223&hsa_grp=150847156266&hsa_ad=665675022865&hsa_src=g&hsa_tgt=kwd-322268544642&hsa_kw=cohere&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gad=1&gclid=EAIaIQobChMIobC6nd3-gAMVRb2GCh14HwGOEAAYASAAEgLiPPD_BwE) 等私有 LLM。

### 2. AI 数据平面出现 

对于企业来说，我认为会出现一个 AI 数据平面，它位于 LLM 组合与企业数据之间。加入 AI 数据平面可为 LLM 组合提供企业防火墙内数据的额外上下文和清洁数据，以便根据企业内部数据进行即时响应。这些数据平面将需要能够摄取、存储和处理向量嵌入，以及其他数据类型和结构，包括混合搜索。这包括管理数据访问、安全性和治理，以及一层轻薄的智能层，可帮助快速轻松地原型设计和构建应用程序。

### 3. 实时 AI 将日益成为常态

随着 AI 的普及，以及我们开始与更多启用音频和视频的 AI 进行交互，企业将要求实时(毫秒级)访问新鲜数据，以为基础模型提供正确的上下文。LLM和其他多结构基础模型将需要实时响应请求，反过来，它们的数据平面将需要具备实时处理和分析各种格式数据的功能。要实施实时 AI，企业需要在摄取数据流时持续向量化数据，并将其用于 AI 应用程序。因此，组织将越来越多地采用零 [ETL](https://www.ibm.com/topics/etl#:~:text=ETL%2C%20which%20stands%20for%20extract,warehouse%20or%20other%20target%20system.) 理念，以最小化数据移动、复杂性和延迟，以驱动其 AI 应用程序。

### 结论

AI 和通用 AI 世界正在迅速发展。新的应用程序、基础和业务模型以及支持技术正在快速出现。[SingleStore](https://www.singlestore.com/blog/how-to-bulk-load-vectors-into-singlestoredb-/) 一直处于这场通用 AI 革命的前沿，其内置的向量和多模型功能可用于驱动快速的实时 AI 应用程序。了解组成更大困惑的小碎片对于正确推进通用AI革命至关重要——并创造一个可以将这项技术用于提升人类生活的未来。

在即将举办的 [SingleStore Now](https://singlestorenowtherealtimeaicon.splashthat.com/) 大会上，我们将演示如何构建和扩展引人注目的企业级通用 AI 应用程序的动手课程。活动将邀请客户、合作伙伴、行业领导者和从业者，如 LangChain 的联合创始人兼 CEO Harrison Chase。要了解更多信息并注册 SingleStore Now 大会，请访问 [singlestore.com/now](https://www.singlestore.com/resources/singlestore-now-the-real-time-ai-conference/)。