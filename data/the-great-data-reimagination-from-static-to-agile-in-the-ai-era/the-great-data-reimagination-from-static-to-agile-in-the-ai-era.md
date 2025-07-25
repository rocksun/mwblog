<!--
title: AI时代数据重构：从静态到敏捷
cover: https://cdn.thenewstack.io/media/2025/06/feff67d2-great-data-reimagination.jpg
summary: AI 时代数据架构面临身份危机，传统数据库和适应性平台融合。适应性平台更适合 AI 开发，因其开发者速度快、能作为智能数据伙伴。MongoDB 统一了搜索、向量搜索等功能，简化 AI 基础设施。未来，数据库将成为 AI 的一部分，企业应从小处着手，逐步采用适应性平台。
-->

AI 时代数据架构面临身份危机，传统数据库和适应性平台融合。适应性平台更适合 AI 开发，因其开发者速度快、能作为智能数据伙伴。MongoDB 统一了搜索、向量搜索等功能，简化 AI 基础设施。未来，数据库将成为 AI 的一部分，企业应从小处着手，逐步采用适应性平台。

> 译自：[The Great Data Reimagination: From Static to Agile in the AI Era](https://thenewstack.io/the-great-data-reimagination-from-static-to-agile-in-the-ai-era/)
> 
> 作者：Karin Lauria

仅仅五年前，为应用程序选择合适的数据库类型对许多开发者来说是一件复杂的事情：关系型还是 NoSQL？结构化还是非结构化？灵活还是可预测？他们不清楚六个月后他们的数据会是什么样子，但他们知道的是，数据肯定会发生变化。这导致许多人做出了一个反叛的选择，放弃了 [SQL 数据库](https://thenewstack.io/introduction-to-databases/) 的僵化结构，转而选择更灵活和适应性强的东西。

现在，随着 AI 以超出预期的速度迅猛发展，对话已经发生了根本性的转变。这不仅仅是关于在哪里存储数据，而是关于理解应用程序底层正在发生的事情，我们存储、处理数据并用数据做出决策的根本方式正在实时转变。

这些变化正在推动伟大的数据重构，公司必须将他们的数据视为智能平台中的积极参与者，而不是静态资产，这使他们能够以 AI 的速度进行创新。

## 数据架构的身份危机

各组织目前面临着 [1.52 万亿美元的技术债务](https://www.architectureandgovernance.com/elevating-ea/new-research-suggests-architectural-technical-debt-is-most-damaging-to-applications-amid-1-52-trillion-technical-debt-crisis/?utm_source=chatgpt.com)，根据 Gartner 的数据，到 2026 年，[80% 的技术债务](https://vfunction.com/blog/technical-debt-vs-architectural-technical-debt-what-to-know/?utm_source=chatgpt.com) 将归因于架构问题。对于开发者来说，技术债务占用了他们高达 [42% 的时间](https://thenewstack.io/technical-debt-continues-to-mount-heres-how-to-solve-it/)，损害了士气，导致人员流失并减缓了创新，所有这些都阻碍了在 AI、个性化和物联网 (IoT) 使用等领域的竞争力。

MongoDB 的 EMEA 生成式 AI 解决方案架构师 Han Heloir 表示：“今天的开发者正在构建需要记住对话、语义搜索数百万份文档并同时跨多个云扩展的 [AI 代理](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)。开发者面临的大部分架构债务源于对象和关系系统之间的不匹配，这扼杀了敏捷性、速度和性能。”

开发者早就知道，僵化的基础设施会减慢开发速度。允许快速迭代的 [模式灵活](https://www.mongodb.com/docs/manual/data-modeling/)（不要与无模式混淆）方法最适合现代应用程序。尽管如此，在对应用程序应如何满足 AI 的机遇这两种截然不同的说法之间左右为难的技术领导者中，数据架构的身份危机是真实存在的。

例如，[PostgreSQL](https://roadmap.sh/postgresql-dba) 因其可靠性和 [SQL 掌握](https://roadmap.sh/sql) 而受到工程师的推崇。相反，灵活的、集成了 AI 的平台使用文档模型，这些模型自然地映射到应用程序代码，并且不需要预先确定的模式。它们允许快速迭代，同时保持治理，使其成为需要实时数据的动态领域的理想选择。

然而，这两个平台正在融合，像 PostgreSQL 这样的经典数据库正在拥抱 JSON 支持和类似 NoSQL 的灵活性，并且一些 NoSQL 供应商正在添加事务、连接和向量搜索等功能，以支持灵活和结构化的用例，同时简化架构。

这里的关键是了解您的应用程序的竞争优势和客户的需求。金融交易平台、医疗记录系统和法规遵从性工具都需要模式优先的思考方式。在这些情况下，PostgreSQL 的“结构优先”理念至关重要。但是，当您的应用程序的竞争优势来自理解半结构化、动态或快速发展的数据时，“构建优先”理念可提供战略优势。开发者可以快速开始编写应用程序，而无需首先设计数据库模式。

诀窍是采用多语言持久性，使用 PostgreSQL 处理关系型工作负载，使用文档数据库处理 AI 工作负载。这关系到理解哪个平台在您的架构中承担哪些职责。

## 适应性方法：优先考虑开发者速度

请记住，虽然传统数据库和适应性平台之间的选择不是二元的，但适应性方法最适合 AI 开发，因为开发者速度对于竞争力来说是不可或缺的。

这是因为适应性方法将数据视为应用程序的智能和敏捷性中的积极参与者，从而改善决策制定和用户体验。适应性平台充当智能数据合作伙伴，可以存储、搜索、分析甚至推理信息，同时使应用程序能够从一个用户扩展到数百万用户，而开发者无需在开始构建之前考虑定义基础设施。这些平台对开发者来说具有变革性，使他们能够专注于使其应用程序独特的功能，而不是将五种不同的服务拼凑在一起以处理数据、搜索、分析和 AI。

从技术角度来看，适应性平台融合了三种功能：它们消除了阻抗失配，提供了用于水平扩展的分布式架构，并集成了运营和分析工作负载。这些平台随着新的 AI 工作负载而发展，并且可以充当 [检索增强生成 (RAG)](https://thenewstack.io/no-mcp-hasnt-killed-rag-in-fact-theyre-complementary/) 应用程序的运营数据库和向量存储。

例如，MongoDB 的 RAG 整合方法统一了搜索、向量搜索、运营数据和事件驱动的触发器。无需将客户数据保存在 MongoDB 中，将向量保存在 Pinecone 中，将搜索索引保存在 Elasticsearch 中，所有内容都位于一个平台中。这是一种 AI 原生方法，通过使运营数据、向量嵌入、搜索索引和分析系统保持一致，消除了与传统 AI 平台相关的开销。

当客户的个人资料更新时，向量嵌入会自动同步。当新知识添加到系统时，它会立即用于运营查询和语义搜索。换句话说，它使智能成为数据层本身的内在属性。

Heloir 说：“统一的 AI 原生平台的优势是深远的。我们看到公司将其 AI 基础设施从六个或七个组件减少到 MongoDB 及其 LLM [大型语言模型] 提供商。这不仅仅是节省成本。这是加速创新的架构简单性。”

## AI 原生平台是未来

我们正处于企业软件在未来十年内如何运作的根本性重构之中，您的数据库将成为您的 AI。随着着眼于未来的组织开始采用学习和进化的适应性平台，关于数据库的争论正在消退。

随着运营数据库和适应性平台之间的区别完全消失，数据将越来越多地成为基础设施中的协作伙伴，该基础设施充当智能生物，数据、意义和推理无缝共存。这不是科幻小说。这是朝着 AI 原生设计的自然发展。

与此同时，技术领导者可以通过从小处着手来应对关系型/适应性鸿沟带来的不确定性，例如，从一个用例和一个 AI 增强功能开始，而不是做出平台范围内的决策。然后衡量结果，让成功推动扩张。

*MongoDB 正在超越数据库发展。它现在是一个 AI 原生数据平台，不仅处理存储，还处理向量搜索、实时分析和多云扩展，使应用程序能够以 AI 的速度进行创新。[了解更多信息并试用一下](https://www.mongodb.com/products/platform/atlas-product-tour?utm_campaign=devrel&utm_source=third-party-content&utm_medium=cta&utm_content=the+new+stack&utm_term=tony.kim)。*