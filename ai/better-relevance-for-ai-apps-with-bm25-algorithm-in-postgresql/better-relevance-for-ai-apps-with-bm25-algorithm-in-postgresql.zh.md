Tiger Data，原名Timescale，最近开源了[pg\_textsearch](https://github.com/timescale/pg_textsearch)的预览版，该工具使用[最佳匹配25 (BM25) 算法](https://www.geeksforgeeks.org/nlp/what-is-bm25-best-matching-25-algorithm/)对PostgreSQL进行排名文本搜索。

其创建者发现反响惊人。几天之内，它在GitHub上获得了1,000颗星，截至上次统计已达1,800颗。

该公司之所以更名，是因为尽管最初专注于创建时序数据库，但他们发现开发者将其Postgres实现用于与时序数据无关的用例。正如创始人兼首席技术官Mike Freedman在采访中解释的那样，随着公司扩大业务范围——如今它提供自己的云服务以及Postgres for Agents——旧名称造成了混淆。

最近，它一直致力于改进Postgres中的搜索功能，以应用于AI应用。

“我们从想要开始探索AI搜索的客户那里得知，他们需要这种通用搜索原语。实际上，当时市场上我们没有可以提供给他们的东西，所以我们最终自己构建并将其开源了，”他解释道。

pg\_textsearch的预览版是一个Postgres扩展，旨在提高这个拥有30多年历史的数据库中搜索的相关性和性能。

## AI时代对更好关键词搜索的需求

我们一直在听到很多关于[人们对“无聊”而可靠的Postgres重新产生了浓厚兴趣](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/)，特别是[自从AI兴起以来](https://thenewstack.io/why-a-boring-database-is-your-secret-ai-superpower/)。 Freedman说，尽管最初所有的讨论似乎都围绕着[向量数据库](https://thenewstack.io/vector-databases-where-geometry-meets-machine-learning/)，但一种新兴模式正在融合[向量](https://thenewstack.io/vector-processing-understand-this-new-revolution-in-search/)和[关键词搜索](https://thenewstack.io/combining-the-power-of-text-based-keyword-and-vector-search/)。

虽然Apache Lucene和Elasticsearch等搜索引擎——以及原生Postgres——多年来一直提供关键词搜索，但AI加速了改进其输出相关性的需求。

高级软件工程师TJ (Todd) Green在博客文章中解释说：“AI原生应用、RAG [检索增强生成] 系统、聊天代理和代理工作流需要搜索，这并非为了人类浏览目录或工程师查询日志，而是为了LLM [大型语言模型][检索上下文](https://www.tigerdata.com/blog/introducing-pg_textsearch-true-bm25-ranking-hybrid-retrieval-postgres)。”

“语料库的变化不像流日志那样迅速，但结果质量至关重要：这些系统既需要向量搜索的语义理解，也需要关键词匹配的精确度。这两种方法是深度互补的：向量捕捉概念相似性，而关键词确保不会遗漏确切的术语。”

他补充道：“挑战在于Postgres原生全文搜索缺乏一致地显示最相关结果所需的排名信号。”

## 什么是BM25算法？

BM25（最佳匹配25）是一种在信息检索系统中[用于对相关性进行排名](https://www.tigerdata.com/docs/use-timescale/latest/extensions/pg-textsearch)的算法。它被认为是传统搜索引擎使用的[TF-IDF（词频-逆文档频率）](https://www.geeksforgeeks.org/machine-learning/understanding-tf-idf-term-frequency-inverse-document-frequency/)方法的改进。

pg\_textsearch使用内存表架构来索引和排名信息：

*   使用逆文档频率对稀有词语进行更高权重。
*   使用词频饱和度防止重复使用的词语主导结果。
*   阻止长文档主导。
*   采用相对排名，侧重排名顺序而非绝对分数。

它支持PostgreSQL 17和PostgreSQL 18。

使用Postgres的原生搜索时，随着语料库大小的增长，性能会急剧下降，因为它必须查询每个匹配文档的tsvector。使用pg\_textsearch，您可以为您正在使用的语料库设置内存大小，并使用分数阈值来过滤掉低相关性结果，从而提高性能。

该公司表示，结合[pg\_vector](https://github.com/pgvector/pgvector?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)和[pg\_vectorscale](https://thenewstack.io/make-pgvector-faster-than-pinecone-and-75-cheaper-with-this-new-open-source-extension/)（后者在与pg\_vector相同的数据类型上添加了更高级的算法），开发者可以通过单个SQL查询将关键词搜索与向量搜索结合在Postgres中，避免了从多个数据源调用数据的延迟和复杂性。

Freedman在谈到开源公告的反响时说：“我认为最棒的类比是pg\_vector。”“你知道，所有这些向量数据库都大幅崛起，然后pg\_vector出现了……并得到了广泛采用。而对于现代AI搜索来说，缺失的部分就是关键词方面。”

“我们看到很多供应商都推出了自己的专有实现，但这并没有真正解决开发者更广泛的需求，即‘嘿，我们想要这种更生态系统友好的软件，可以随处使用。’我认为当有这么多专有实现时，这种碎片化对任何人都无益。”

Freedman表示，他们选择在开放源代码促进会（OSI）批准的宽松[PostgreSQL许可](https://opensource.org/license/postgresql)下发布，因为他们希望它能够被广泛使用和采纳。

与此同时，越来越多的供应商和开源项目正在添加BM25排名功能，包括Elasticsearch、Apache Solr和Neon，尽管Freedman表示，这些替代方案的许可通常较为不宽松。

## pg\_textsearch是如何构建的

在经过几个月的规划后，Green于十月开始着手pg\_textsearch，公司于十二月中旬宣布了开源预览版。

Green在采访中说：“我认为我们最难决定的就是承诺投入，因为世界正在变化，对吧？”“像这样的项目，在AI工具出现之前，一个小团队需要花费大量时间，而且对我们来说会太长、太昂贵，所以我们决定尝试以不同的方式开发这个项目。”

根据Green的说法，这种不同的方式“本质上是我和机器人”。Green此前曾在RelationalAI担任计算机科学家，并在AWS和Pinecone从事数据库工作。这个机器人是[Claude Cloud Opus](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/)。

他说：“是的，我就是那些愿意支付Opus 4.1高昂费用的人之一，因为我发现它比其他替代方案能力更强，更符合我的工作流程。而现在我们有了[Opus 4.5](https://thenewstack.io/anthropics-new-claude-opus-4-5-reclaims-the-coding-crown-from-gemini-3/)，它功能更强大，价格也显著降低。所以，这基本上就是我内部的工作流程，同时还使用[Cursor](cursor)作为编辑器。”

事情进展迅速，他预计生产就绪版本将在新年伊始（可能是一月份）推出。

“这也将取决于我们从本周刚刚开始使用该产品的人那里得到的反馈。我们已经收到了一些非常有用的报告，而且，你知道，一旦它在实际使用中经受了考验，它的实际稳健程度将决定发布时间，”他说。

Freedman指出，由于公司运营自己的云服务，其仪表工具将使其能够发现人们遇到的问题，而不仅仅依赖报告，这应该会加快时间线。

“Postgres基本上赢得了开发者的心智。它几乎是当今所有开发者的首选数据库……有了AI，我们如何继续扩展它，以便开发者能够越来越多地使用它，从而最终获得更简单、易于使用的数据架构，而不是拥有五个不同的数据库，数据分散在所有这些不同的地方，他们还必须担心同步和管理，”Freedman说。“相反，我们可以将其中很多东西整合到Postgres中，特别是[我]喜欢称之为为99%的用户构建的产品。它是为市面上99%的项目而构建的。”

他说：“我们对AI如何改变开发者的构建方式非常看好，我们正处于重新思考开发者体验会是怎样以及我们的数据基础设施如何支持这一点的过程中。”