
<!--
title: 停止支付OpenAI税：新兴的开源AI技术栈
cover: ./cover.png
-->

以下是我们挑选的开源AI技术栈最佳组件。

> 译自 [Stop Paying the OpenAI Tax: The Emerging Open-Source AI Stack](https://medium.com/timescale/stop-paying-the-openai-tax-the-emerging-open-source-ai-stack-5e8b4422b411)，作者 Team Timescale。译者对这个技术栈都有涉猎，有没有朋友想要一起做点事情？

*一套开源模型和工具，使任何开发者都能构建最先进的AI应用程序。*

如果我们能够回到过去，告诉软件工程师他们的应用程序将由神秘的AI驱动，我们对其内部运作一无所知，并且他们为了体验的便利性而将最敏感的数据交给影子第三方，他们可能会难以置信地摇头。但这就是我们现在所处的境地。

如今，全球的开发者正在围绕AI重新构想他们的应用程序，默认情况下，这意味着将专有的大型语言模型（LLM）集成到各个方面。但是，虽然来自OpenAI和Anthropic等公司的专有LLM引发了AI革命，但它们也存在明显的缺点：惊人的成本、数据隐私问题、供应商锁定以及缺乏可定制性。最初，为了革命性的功能而牺牲性能和控制权似乎是一笔值得做的交易，但如今许多开发者想要一种不同的方式。

但是，革命总能使曾经独有的东西民主化。虽然最初的AI热潮集中在专有模型上，但真正的革命是开源LLM作为专有模型（如OpenAI的模型）的可行替代方案的迅速兴起。开源AI工具的创新也悄然爆发，使开发人员能够利用开源LLM增强的推理能力，并将它们转化为有用的应用程序——从模型部署和托管工具到数据存储和检索，再到前端和后端Web框架，无所不包。

为了帮助您了解这个新的领域，并基于与数百名开发人员和其他AI工具构建者的对话，我们正在分享我们选择的**“简单模式”开源AI技术栈**——最适合开发人员构建AI应用程序的模型和工具。以下是该技术栈的组件如何协同工作以增强开发人员能力并重塑AI未来的：

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*nHEqU8pCTFJvwAb9)

*“简单模式”开源AI技术栈。精选的顶级模型和工具，使开发人员能够轻松构建AI应用程序，从而最大限度地控制数据隐私、成本和性能。*

这套开源AI工具将部署、隐私和性能的完全控制权交还给开发人员，而不会牺牲其应用程序的智能性。开发人员现在可以使用这些工具以任何他们想要的方式构建和部署AI解决方案——本地、云端或边缘。他们保留对其数据的100%控制权，并且不必担心“值得信赖的”第三方可能会如何处理潜在的敏感信息。这不仅仅是技术上的转变；它也是文化上的转变，标志着开发者自主性和创新的核心价值观的回归。

这就是开源AI技术栈的承诺——一套使任何开发者都能构建最先进AI应用程序的模型和工具。它不仅仅是一套技术；它更是一场旨在使创新惠及每位开发者的运动。

## 开源AI技术栈的关键组件

### 1. LLMs：开源模型

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*yyUspFz570UrEVNU)

*精选的顶级开源免费LLM，可与OpenAI、Anthropic和Google的专有模型相媲美。其中包括Meta的Llama 3.3、Mistral模型系列、Qwen模型系列、微软的Phi 3以及DeepMind的Gemma 2。*

开源大型语言模型正处于AI民主化的最前沿。诸如Meta的[Llama 3系列](https://www.llama.com/?ref=timescale.ghost.io)、[Mistral 7B和Pixtral 12B](https://mistral.ai/technology/?ref=timescale.ghost.io#models)、阿里云的[Qwen 2.5](https://github.com/QwenLM/Qwen2.5?ref=timescale.ghost.io)、微软的[Phi 3](https://azure.microsoft.com/en-us/blog/introducing-phi-3-redefining-whats-possible-with-slms/?ref=timescale.ghost.io)和DeepMind的[Gemma 2](https://blog.google/technology/developers/google-gemma-2/?ref=timescale.ghost.io)等模型都可以免费下载和使用，任何拥有足够硬件的开发者都可以运行。

这些开源模型可与专有解决方案相媲美，并提供以下优势：

- **更强大的数据控制**： 使用开源模型可以保证所有数据私密性，避免依赖第三方，并为开发者提供更强大的安全性和合规性保障。
- **具有竞争力的推理性能**： 开源模型在[MMLU](https://paperswithcode.com/dataset/mmlu?ref=timescale.ghost.io)、[HumanEval](https://github.com/openai/human-eval?ref=timescale.ghost.io)和[MATH Reasoning](https://paperswithcode.com/sota/math-word-problem-solving-on-math?ref=timescale.ghost.io)等基准测试中日益具有竞争力，表明开源模型和专有模型之间的推理差距正在缩小。
- **灵活的部署和可定制性**： 您可以通过自行微调或访问公开可用的模型微调和变体来适应利基用例，而无需受供应商约束。
- **小型模型的效率和可扩展性**： 较小的开源模型通常需要较少的计算能力，使其具有成本效益，并且易于在资源受限的设备或环境中部署，同时仍能为特定任务提供强大的性能。

### 2. 嵌入模型：开源嵌入模型

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*yP4Ef2JcuUHbyb1H)

*一些顶级的开源嵌入模型包括Nomic、来自BAAI的BGE、Sentence Transformers系列以及来自Jina AI的模型等。向量嵌入在现代AI应用中极其有用。它们为搜索和RAG（检索增强生成）功能提供支持，使LLM应用程序能够以更可靠、更符合上下文的相关答案进行响应。*

就像开源LLM一样，开源嵌入模型也取得了显著进展，可以与OpenAI的text-embedding-3模型系列和Cohere的embed-multilingual-v3.0等专有解决方案相媲美。领先的开源嵌入模型包括：

包含各种尺寸和专业化功能的开源嵌入模型系列，从轻量级的all-minilm到多语言模型。

- **Sentence Transformers / SBERT**： 开源的嵌入模型家族，包含各种大小和专业化的模型，从轻量级的all-minilm到多语言模型。
- **Nomic**： Nomic Embed Text V1.5支持多种嵌入尺寸（768、512、256、128、64），专门用于检索、相似性、聚类和分类任务。它可以处理多达8,192个标记的序列，并为文本和图像数据提供多模态能力。
- **BGE (BAAI)**： BGE（BAAI通用嵌入）模型将文本映射到密集向量，用于检索、分类和语义搜索任务。最新的BGE-M3模型支持100多种语言，可以处理最多8192个token的文档。它具有多功能性（密集检索、多向量检索、稀疏检索）能力。
- **Jina AI**：Jina AI的jina-embeddings-v3是一个拥有5.7亿参数的模型，支持89种语言，在30种核心语言中表现出色。它具有8192个token的输入长度、可配置的最高1024维输出以及针对查询文档检索、聚类、分类和文本匹配的专业功能。

### 3. 模型访问和部署：Ollama

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*SFnpbK5kZXG4EHBh)

*Ollama已成为开发者访问和使用开源LLM和嵌入模型的默认工具。*

部署AI模型曾经就像试图从你的车库发射航天飞机一样。这需要令人望而生畏的专业知识组合：由博士组成的团队、复杂的架构以及会让大多数组织望而却步的资源。[Ollama](https://ollama.com/?ref=timescale.ghost.io)彻底改变了游戏规则，允许开发者使用单个命令运行最先进的模型：

```
ollama run llama3.2
```

通过单个工具访问数百个LLM和嵌入模型，抽象化基础设施挑战并简化部署，Ollama将曾经看似难以逾越的障碍转变为无缝、直观的流程。它使开发人员能够专注于解决现实世界的问题，弥合个人和企业项目创新与实用性之间的差距。

借助开源模型和Ollama的简洁性，开发人员可以以前所未有的自由度来部署AI。例如：上述开源LLM和嵌入模型部分中提到的所有模型都可通过Ollama获得！

### 4. 数据存储和检索：PostgreSQL、pgvector和pgai

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*GRjh3qXMwoduL-10)

*开源数据库PostgreSQL及其用于AI用例（如pgvector和pgai）的开源扩展生态系统，是希望构建AI应用程序的开发者的理想选择。*

良好的数据和良好的检索是AI中RAG革命的核心，使开发人员能够创建LLM应用程序，为用户提供高度准确、符合上下文、无幻觉的答案。

但是，最好的AI应用程序不仅仅是使用向量数据库——它们涉及非结构化数据、结构化数据和应用程序数据的组合，以及对具有复杂过滤器的庞大数据集进行向量搜索。此类检索系统可确保您的用户获得最符合上下文的答案，但构建它们可能很复杂，在某些情况下，可能需要多个数据库系统和自定义数据管道：

- 您需要存储文档和其他源数据以创建要搜索的知识库。
- 你需要一种方法来预处理数据，从中创建向量嵌入，并在知识库发生变化时保持这些嵌入同步。
- 你还需要能够存储和搜索向量嵌入，通常是大规模的，并且对元数据和其他用户数据进行复杂的过滤。更不用说处理多租户、权限和访问控制以及高可用性等实际问题了。

好消息是，PostgreSQL（[世界上最受欢迎的数据库](https://survey.stackoverflow.co/2024/technology?ref=timescale.ghost.io#1-databases)）正在从可靠的关系型数据库转变为为 AI 应用程序提供支持的数据层，支持结构化数据、非结构化数据以及快速、准确的向量搜索。

PostgreSQL 是开源的，并且拥有一个开源扩展生态系统，这使其成为为 AI 应用程序提供存储和检索功能的首选数据库：

- **向量搜索**：诸如 [pgvector](https://github.com/pgvector/pgvector?ref=timescale.ghost.io) 和 [pgvectorscale](https://github.com/timescale/pgvectorscale/?utm_source=blog&utm_medium=website&utm_campaign=december-AI-launch&utm_content=pgaivectorizer-github) 之类的扩展程序支持向量存储和相似性搜索，[其性能优于专门的向量数据库](https://www.timescale.com/blog/pgvector-vs-pinecone/?ref=timescale.ghost.io)。
- **易用性**：诸如 [pgai](https://github.com/timescale/pgai/?utm_source=blog&utm_medium=website&utm_campaign=december-AI-launch&utm_content=pgai-github) 之类的扩展程序简化了访问 LLM 以对 PostgreSQL 中的数据进行推理的过程，并且诸如 [pgai Vectorizer](https://github.com/timescale/pgai/blob/main/docs/vectorizer-quick-start.md/?utm_source=blog&utm_medium=website&utm_campaign=december-AI-launch&utm_content=pgaivectorizer-github) 之类的功能使嵌入创建和同步与传统的数据库索引一样直观。
- **集成和生态系统**：Pgai 对 Ollama 的支持使得轻松访问最先进的开源模型以进行嵌入创建或推理成为可能。

**示例**：使用几行 SQL 执行语义搜索：

```sql
CREATE TABLE IF NOT EXISTS blog (
            id SERIAL PRIMARY KEY,
            title TEXT,
            authors TEXT,
            contents TEXT,
            metadata JSONB
 );

INSERT INTO blog (title, authors, contents, metadata) VALUES ('The Future of Artificial Intelligence', 'Dr. Alan Turing', 'As we look towards the future, artificial intelligence continues to evolve...', '{"tags": ["AI", "technology", "future"], "read_time": 12, "published_date": "2024-04-01"}');

--insert more data here

--Vectorize data in the contents column using models from Ollama
SELECT ai.create_vectorizer(
            'blog'::regclass,
            destination => 'blog_contents_embeddings',
            embedding => ai.embedding_ollama('nomic-embed-text', 768),
            chunking => 
ai.chunking_recursive_character_text_splitter('contents')
);

-- Perform semantic search
SELECT
            b.title,
            b.contents,
            be.chunk,
            be.embedding <=> ai.ollama_embed('nomic-embed-text', 'What comes next in AI') as distance
        FROM blog_contents_embeddings be
        JOIN blog b ON b.id = be.id
        ORDER BY distance
        LIMIT 3;
```

### 5. 后端：FastAPI

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*VjIWnItK8czoe0OA)

你的应用程序后端将智能模型连接到面向用户的应用程序，而 FastAPI 已成为开发人员的首选框架。它提供：

- **速度和简洁性**：异步编程确保低延迟和高吞吐量。
- **面向开发人员的设计**：自动 API 文档和类型提示能够快速迭代。
- **无缝集成**：非常适合实时应用程序，例如聊天机器人、推荐引擎和预测分析。

FastAPI 消除了后端瓶颈，使开发人员能够轻松地将 AI 应用程序从原型扩展到生产环境。想象一下部署一个由开源模型驱动的推荐系统。FastAPI 的异步功能确保用户请求立即得到处理，而其自动文档使协作保持无缝。这些功能共同将复杂的后端工作流程转变为可管理、高效的系统。

### 6. 前端：NextJS

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*sHeuqCnMIc0k0RYZ)

AI 应用程序的前端需要处理复杂的状态管理和动态更新，而 [NextJS](https://nextjs.org/?ref=timescale.ghost.io) 已成为用于生产部署的首选 React 框架。

它提供许多有用的功能：

- **混合渲染:** 服务器端渲染 (SSR) 和客户端静态渲染为您提供了灵活的每个页面渲染和缓存选项。Next.js 提供强大的服务器端功能，这对于 AI 应用程序尤其有利。该框架的 SSR 有助于有效地管理计算密集型 AI 任务，同时减少客户端设备的负载。这在处理复杂的 AI 模型交互和数据处理时尤其重要。
- **实时流和更新:** 它与各种实时解决方案无缝集成，以支持流畅的动态交互，这对于 AI 聊天和其他显示动态内容的 UI 尤其重要。
- **与 Vercel AI SDK 集成:** Vercel AI SDK（也是开源的）专为使用 Next.js 创建 AI 应用程序而构建，并支持客户端和服务器端的 AI 功能。它与[Ollama](https://sdk.vercel.ai/providers/community-providers/ollama?ref=timescale.ghost.io)很好地集成，并提供用于处理 AI 模型推理、流式响应和连接提供商的实用程序。

### 7. 缺失的部分：评估和验证

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*hzaS9ml-asVE6yf0)

虽然开源 AI 技术栈已经成熟，但评估仍然是一个关键挑战。像 [LangFuse](https://langfuse.com/?ref=timescale.ghost.io) 和 [Arize 的 Phoenix](https://github.com/Arize-ai/phoenix?ref=timescale.ghost.io) 这样的项目提供了希望，但生态系统仍然缺乏一个用于测试和验证 AI 模型的全面框架。这一差距代表了一个创新的机会——一个让社区定义可靠的、现实世界的 AI 应用程序的机会。

**这为什么重要**： 与传统应用程序不同，LLM 是非确定性的，这意味着如果您在没有评估和验证的情况下部署 AI 应用程序，您将无法判断应用程序的性能。强大的评估系统对于确保您的应用程序现在和系统发展过程中都能良好运行至关重要。

我们应该说，鉴于开源社区在创建可观察性和监控工具方面的强大记录，我们发现这种能力差距特别有趣。我们认为，总的来说，评估生态系统还处于起步阶段，尚未找到正确的方法。我们怀疑目前的系统过于千篇一律，并且低估了不同项目之间评估需求的多样性。需要的是一种类似于 DevOps 中**GitOps 革命**的视角转变，这就是为什么我们特别高兴看到开源驱动的创新在这个领域蓬勃发展。

## 开放获取创新：你将构建什么？

开源 AI 技术栈不仅仅是一组工具——它是一场运动。开发人员现在可以自由地构建、创新和控制他们的 AI 应用程序，而无需担心供应商锁定或隐私问题。

使用开源 AI，您可以获得：

- 自由部署在任何地方——本地、云端或边缘。
- 完全控制数据——无需第三方共享。
- 可定制性以满足您的需求。
- 与全球社区合作。

这不仅仅关乎技术；它关乎创造属于你自己的东西。无论您是部署模型、构建 RAG 应用程序还是启动新的 AI 服务，开源技术栈都让您可以按照自己的方式进行操作。

立即开始：

- 使用 Ollama [部署](https://ollama.com/?ref=timescale.ghost.io) 开源模型。
- 使用 PostgreSQL [构建 RAG 应用程序](https://github.com/timescale/pgai/?utm_source=blog&utm_medium=website&utm_campaign=december-AI-launch&utm_content=pgai-github)。
- 使用 FastAPI [创建](https://fastapi.tiangolo.com/?ref=timescale.ghost.io)您的后端。

实验、迭代和贡献。开源 AI 革命已经到来——你将构建什么？

*本文由 Matvey Arye 和 Avthar Sewrathan 撰写，并于 2024 年 12 月 16 日在 Timescale 官方博客上首次发布*。