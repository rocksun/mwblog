# 如何为 AI 智能体添加 RAG 以实现上下文理解

![关于如何为 AI 智能体添加 RAG 以实现上下文理解的特色图片](https://cdn.thenewstack.io/media/2024/12/940a6b89-alexander-mils-ctpwqeem46s-unsplashb-1024x576.jpg)

[GitHub](https://github.com/janakiramm/agent-framework)

- 概述：

[AI 智能体：面向开发人员的全面介绍](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)

- 步骤 1：

[如何通过调整 LLM 提示来定义 AI 智能体角色](https://thenewstack.io/how-to-define-an-ai-agent-persona-by-tweaking-llm-prompts/)

- 步骤 2：

[增强 AI 智能体：添加指令、任务和内存](https://thenewstack.io/enhancing-ai-agents-adding-instructions-tasks-and-memory/)

- 步骤 3：

[增强 AI 智能体：通过提示工程实现推理](https://thenewstack.io/how-to-add-reasoning-to-ai-agents-via-prompt-engineering/)

- 步骤 4：

[如何为 AI 智能体添加持久性和长期记忆](https://thenewstack.io/how-to-add-persistence-and-long-term-memory-to-ai-agents/)

- 步骤 5：如何为 AI 智能体添加 RAG 以实现上下文理解

在我们关于构建企业级 AI 智能体的系列文章中，我们已经探讨了各种关键组件——包括角色、指令、任务、会话记忆和持久性（参见上面的链接）。这些基础知识已经阐明了智能体如何保持其身份、遵循指南、执行任务以及跨会话保持其状态。

现在，让我们深入探讨另一种关键能力，它将智能体提升到真正的企业就绪水平：[检索增强生成](https://thenewstack.io/retrieval-augmented-generation-for-llms/) (RAG) 和上下文管理。

## 企业智能体对上下文的需要

企业环境中充斥着特定领域的知识、专有信息和标准语言模型无法访问的专业文档。虽然我们之前的实现使智能体能够维护会话历史并保持其状态，但它们仍然缺乏将响应建立在组织特定知识基础上的能力。当智能体需要处理有关内部流程、产品或策略（这些不在其训练数据中）的查询时，这种限制尤其明显。

通过 RAG 进行上下文管理解决了这一关键差距，它允许智能体动态地访问和整合组织文档库中的相关信息到其响应中。此功能将智能体从通用助手转变为能够提供准确、上下文感知的响应并同时遵守组织准则的专用企业工具。

## 实现上下文管理

上下文管理系统使用[向量数据库](https://thenewstack.io/top-5-vector-database-solutions-for-your-ai-project/)（在本例中为 ChromaDB）来实现高效的相似性搜索和检索。以下是我们上下文管理实现的核心结构：

```python
class ContextManager:
    def __init__(self, collection_name: str, persist_dir: str = "context_db", chunk_size: int = 1000, chunk_overlap: int = 200):
        self.persist_dir = persist_dir
        self.collection_name = collection_name
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        # Initialize ChromaDB
        self.client = chromadb.PersistentClient(path=persist_dir)
        self.collection = self.client.get_or_create_collection(
            name=collection_name, metadata={"hnsw:space": "cosine"}
        )
```

此实现提供了几个关键功能：

### 1. 文档处理和索引

上下文管理器实现了复杂的文档处理功能，这些功能可为高效检索准备组织内容。文档通过包括文本提取、分块和嵌入生成的管道进行处理。分块策略尤其重要，因为它决定了文档如何被分割成可管理的片段，同时保持语义连贯性：

```python
# ... (Code for document processing and indexing would go here) ...
```
```python
def index_document(self, pdf_path: str, metadata: Optional[Union[Dict[str, Any], DocumentMetadata]] = None) -> bool:
    """将PDF文档索引到向量数据库中。"""
    try:
        # 如果元数据是字典，则将其转换为DocumentMetadata
        if isinstance(metadata, dict):
            metadata = DocumentMetadata.from_dict(metadata)
        elif metadata is None:
            metadata = DocumentMetadata(source=os.path.basename(pdf_path))
        # 从PDF中提取文本
        text = self._extract_text_from_pdf(pdf_path)
        # 将文本分割成块
        chunks = self._text_splitter.split_text(text)
        # 生成唯一ID并准备元数据
        ids = [self._generate_document_id(chunk, metadata.to_dict()) for chunk in chunks]
        metadatas = [metadata.to_dict() for _ in chunks]
        # 添加到ChromaDB
        self.collection.add(documents=chunks, ids=ids, metadatas=metadatas)
        return True
    except Exception as e:
        logger.error(f"索引文档{pdf_path}出错：{str(e)}")
        return False

```

```python
def query(self, query: str, num_results: int = 3, filter_metadata: Optional[Dict[str, Any]] = None) -> str:
    """查询上下文并返回相关信息。"""
    try:
        self._current_query = query
        # 准备查询参数
        query_params = {
            "query_texts": [query],
            "n_results": num_results
        }
        if filter_metadata:
            query_params["where"] = filter_metadata
        # 执行查询
        results = self.collection.query(**query_params)
        # 使用元数据格式化上下文
        context_parts = []
        for i, (doc, metadata) in enumerate(zip(results['documents'][0], results['metadatas'][0]), 1):
            source = metadata.get('source', 'Unknown source')
            context_parts.append(f"相关上下文 {i} (来自 {source}):\n{doc}\n")
        self._current_context = "\n".join(context_parts)
        return self._current_context
    except Exception as e:
        logger.error(f"执行查询出错：{str(e)}")
        self._current_context = ""
        return ""

```

```python
class Agent:
    def __init__(self, name: str, context: Optional[ContextManager] = None, persistence: Optional[AgentPersistence] = None):
        self._name = name
        self._persona = ""
        self._instruction = ""
        self._task = ""
        self._context = context
        self._persistence = persistence or AgentPersistence()
        self._history: List[Dict[str, str]] = []

```

```python
# 1. 初始化上下文并索引PDF
print("\n步骤 1：初始化上下文并索引文档...")
context = ContextManager.initialize(collection_name="simple_docs", persist_dir="context_db")
pdf_path = "quantum_computing.pdf"
metadata = DocumentMetadata(
    source=os.path.basename(pdf_path),
    doc_type="pdf",
    author="Demo Author",
    created_at=datetime.now(),
    tags="technical,quantum,computing"
)
success = context.index_document(pdf_path, metadata)

# 2. 使用上下文创建和配置代理
print("\n步骤 2：使用上下文创建代理...")
agent = Agent("rag_agent", context=context)

# 设置代理角色和指令
agent.persona = """我是一个乐于助人的AI助手，根据给定的上下文提供准确的信息。我分析文档并以清晰易懂的方式解释复杂主题。"""
agent.instruction = """解释文档中的概念时：1. 重点关注关键原则和基本原理2. 使用清晰简洁的语言3. 在适用情况下提供相关示例"""

# 3. 使用上下文查询并获取响应
print("\n步骤 3：设置上下文并执行任务...")
context_query = "量子计算的主要原理是什么？"
agent.set_context_query(context_query)
agent.task = """根据提供的上下文：1. 识别并解释量子计算的关键原理"""
response = agent.execute()

```
添加RAG功能将我们的代理转变为企业级解决方案，带来三大关键优势：

**1. 知识基础**

增强RAG功能的代理可以将其响应建立在组织特定的知识基础上，确保准确性和相关性。对于企业环境而言，此功能至关重要，因为响应必须符合内部策略、程序和特定领域的知识。系统维护文档元数据和版本控制，从而能够追溯信息来源并支持合规性要求。

**2. 动态信息更新**

上下文管理系统支持对知识库进行动态更新。可以对新文档进行索引并立即提供给代理，确保它们始终使用最新信息。此功能在策略、产品或程序频繁变化的环境中尤其宝贵。

**3. 合规性和审计支持**

通过维护响应和源文档之间的清晰链接，系统支持合规性要求并能够对代理响应进行审计。元数据系统跟踪文档来源、版本和使用情况，为审计目的提供清晰的线索。这种透明度对于需要记录决策来源的受监管行业至关重要。

## RAG实施最佳实践

在代理系统中实施RAG功能时，需要考虑以下几个关键因素：

**1. 文档处理**

有效的文档处理对于RAG的成功至关重要。分块策略应在粒度和上下文保留之间取得平衡，确保检索到的块包含足够的上下文，同时保持重点。元数据管理应全面，捕获所有可能需要用于过滤或审计的相关文档属性。系统应处理各种文档格式和结构，在整个处理流程中保持语义一致性。

**2. 上下文检索**

检索系统应针对相关性和性能进行优化。应仔细调整相似度阈值，以平衡精度和召回率，确保检索到的上下文既相关又全面。系统应实施高效的缓存策略以优化对频繁访问内容的性能。查询处理应同时考虑语义相似性和元数据过滤器，从而实现精确的上下文检索。

**3. 集成策略**

与现有代理功能的集成应无缝且高效。上下文系统应与代理的角色、指令、任务执行和推理能力和谐地协同工作。状态管理应包含与上下文相关的信息，从而能够在会话之间保持持续的上下文感知。系统应提供清晰的上下文更新和维护接口。

## 未来展望

随着企业AI的不断发展，RAG和上下文管理的作用将变得越来越重要。未来的增强功能可能包括更复杂的文档理解能力、改进的上下文相关性排名和高级元数据管理系统。与企业知识图谱的集成可以提供额外的上下文结构，而改进的分块策略可以更好地保留文档语义。

RAG功能与我们之前实施的功能（角色、指令、任务、会话记忆和持久性）相结合，为企业级AI代理创建了一个强大的框架。这些代理现在可以维护其身份、遵循指南、执行任务、持久化其状态，并将它们的响应建立在组织特定的知识基础上，使它们成为企业自动化和辅助的强大工具。

在本系列的最后一部分，我们将添加代理最重要的构建块：一个工具。敬请期待。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)