<!--
title: 阻止Token流失：构建Token高效型多智能体系统
cover: https://cdn.thenewstack.io/media/2026/08/0f8bbcaf-a-c-3ku2c_-fxqk-unsplash.jpg
summary: 本文探讨了多智能体系统中Token消耗的系统性问题，指出架构设计而非单纯的提示词工程是成本优化的关键。通过路由分流、语义缓存、统一检索、上下文限制及模型选择等技术手段，可显著降低生产环境的延迟与运营成本，实现高效的AI系统构建。
-->

本文探讨了多智能体系统中Token消耗的系统性问题，指出架构设计而非单纯的提示词工程是成本优化的关键。通过路由分流、语义缓存、统一检索、上下文限制及模型选择等技术手段，可显著降低生产环境的延迟与运营成本，实现高效的AI系统构建。

> 译自：[Stop the token bleed: building token-efficient multi-agent systems](https://thenewstack.io/building-token-efficient-agents/)
> 
> 作者：Oladimeji Sowole

每个部署 AI 智能体的工程团队最终都会发现一个令人不安的事实：模型本身并不是最大的支出。隐藏的成本在于它周围的一切：重复的检索、重复的提示词、不必要的工具调用、过大的上下文窗口、多个智能体对相同信息的反复推理。单独来看，这些架构决策似乎无伤大雅。但在生产规模下，它们会成为延迟、基础设施和云支出的沉重负担。

一个每天回答 50 个问题的概念验证智能体可以容忍低效率，但一个每分钟协调数千个请求的企业平台则不行。

本文探讨了在不牺牲输出质量的前提下，构建 Token 高效型 AI 系统的实用技术。我们不仅关注提示词压缩，还将从路由和检索到缓存和模型选择等整个工作流进行优化。

## 为什么 Token 优化是一个系统问题

大多数关于 Token 优化的讨论都始于并止步于提示词工程。实际上，架构才是驱动 Token 消耗的根本。

考虑一个典型的多智能体工作流：

```

User 
  ↓
Intent Agent
  ↓
Retriever
  ↓
Research Agent
  ↓
Planning Agent
  ↓
Writer Agent
  ↓
Reviewer Agent
  ↓
Final Response

```

在每个阶段，系统都可能检索相同的文档、重复相同的指令、调用相同的模型并重新发送整个对话历史。当响应到达用户时，架构可能已经处理了数万个不必要的 Token。

> “提高效率需要重新设计工作流，而不仅仅是缩短提示词。”

## 架构概述

一个生产就绪、Token 高效的架构会在每次昂贵的模型调用之前引入优化。

```

User Request
       │ 
       ▼
Intent Router 
       │ 
       ▼
Semantic Cache ───────► Cached Response
       │ 
       ▼
Context Budget Manager
       │ 
       ▼
Adaptive Retriever
       │ 
       ▼
Model Router
       │ 
       ▼
LLM
       │ 
       ▼
Validated Response

```

> “大语言模型不再是第一个组件，它是最后、最昂贵的操作。”

注意这个关键转变：大语言模型不再是第一个组件，它是最后、最昂贵的操作。

### 第 1 步：安装现代依赖项

使用最新的包结构以避免弃用的导入，并与当前的 LangChain 生态系统保持一致。

```

Bash
pip install \
   langchain \
   langchain-core \
   langchain-openai \
   langchain-community \
   fastapi \
   faiss-cpu \
   tiktoken \
   rank-bm25 \
   pydantic \
   python-dotenv

```

### 第 2 步：配置模型

生产系统必须通过环境变量配置重试、超时和凭据。

```

Python
import os
from langchain_openai import ChatOpenAI 

api_key = os.getenv("OPENAI_API_KEY") 
if not api_key: 
    raise ValueError("OPENAI_API_KEY must be configured.")

llm = ChatOpenAI( 
    model="gpt-4o-mini", 
    temperature=0, 
    api_key=api_key, 
    timeout=30.0, 
    max_retries=2, 
)

```

设置较低的温度系数 (temperature) 可以提高一致性，而显式的超时和重试限制有助于系统从暂时的 API 故障中优雅恢复。

### 第 3 步：生成前先路由

并非每个请求都需要大语言模型。确定性逻辑往往可以回答简单的问题。将廉价的请求从 LLM 中分流出来，是生产系统中[成本削减](https://thenewstack.io/btrfs-petabyte-cost-reduction/)最显著的手段。

```

Python
def classify_request(question: str) -> str:
    q = question.lower()

    if "status" in q:
        return "metrics"

    if "runbook" in q:
        return "retrieval"
   
    return "generation"

```

### 第 4 步：添加语义缓存

最简单且最有效的优化之一是精确匹配缓存，当针对相同的检索文档询问相同问题时，它会返回之前生成的响应，从而避免不必要的模型调用。

```

Python
import hashlib

# 使用精确匹配（词法）缓存
exact_match_cache = {}

def cache_key(question: str, sources: list[str]) -> str:
    """
    根据用户问题和检索到的文档标识符生成确定性缓存键。
    """
    fingerprint = question + "|" + "|".join(sorted(sources))
    return hashlib.sha256(fingerprint.encode()).hexdigest()

# 流水线中的使用示例：
# key = cache_key(question, source_ids)
# if key in semantic_cache:
#     return semantic_cache[key]

```

### 第 5 步：规划上下文预算

大多数检索流水线返回的文本远超模型实际需求。不要用检索到的每一份文档填充上下文窗口，而应建立严格的上下文预算。

```

Python
import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o-mini")
MAX_CONTEXT_TOKENS = 2500

def build_context(chunks):
    context = []
    used = 0

    for chunk in chunks:
        tokens = len(encoder.encode(chunk.page_content, disallowed_special=()))

        if used + tokens > MAX_CONTEXT_TOKENS:
            break 

        context.append(chunk.page_content)
        used += tokens

    return "\n\n".join(context)

```

### 第 6 步：一次检索

在多智能体系统中，重复检索是一个极其常见的缺陷。规则很简单：检索一次，随处复用。

```

Python
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

documents = [
    Document(
        page_content="Database latency often follows connection pool exhaustion.",
        metadata={"source": "db_runbook"},
    ),
    Document(
        page_content="Node pressure can increase API response times.",
        metadata={"source": "cluster_runbook"},
    ),
]

embeddings = OpenAIEmbeddings(api_key=api_key)
index = FAISS.from_documents(documents, embeddings)

retrieved_docs = index.similarity_search(question, k=4)
shared_context = build_context(retrieved_docs)

```

现在，每个下游智能体都消耗相同的优化上下文，而不是启动各自冗余的检索流水线。

### 第 7 步：智能路由模型

大模型应该解决复杂问题，其余任务属于更小、更快的模型。

```

Python
from langchain_openai import ChatOpenAI

small_model = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=api_key)
large_model = ChatOpenAI(model="gpt-4.1", temperature=0, api_key=api_key)

def choose_model(question: str):
    """根据复杂性将请求路由到最合适的模型。"""
    if len(question) < 200:
        return small_model
    return large_model

```

这种策略在不明显影响响应质量的前提下，大幅降低了运营成本。

### 第 8 步：发送前估算 Token

没有 Token 遥测，优化只是盲目猜测。监控使用量使效率可度量，并帮助工程师检测成本回升。

```

Python
import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o-mini")

def estimate_tokens(messages):
    """
    估算 OpenAI 风格聊天负载的输入 Token。
    注意：这是估算值，不是精确的计费计算。
    """
    tokens_per_message = 3
    tokens_per_name = 1
    total = 0

    for message in messages:
        total += tokens_per_message
        for key, value in message.items():
            if isinstance(value, str):
                total += len(encoder.encode(value))
            if key == "name":
                total += tokens_per_name

    # 每次回复都预置额外的助手 Token。
    total += 3
    return total

```

### 第 9 步：验证响应

生产系统必须返回结构化输出，以确保下游系统接收到可预测、格式良好的数据。

```

Python
from pydantic import BaseModel

class AgentResponse(BaseModel):
    answer: str
    sources: list[str]

def validate_response(answer: str, sources: list[str]):
    """使用结构化模式验证并序列化智能体响应。"""
    response = AgentResponse(
        answer=answer,
        sources=sources,
    )
    return response.model_dump()

```

### 第 10 步：构建优化后的流水线

最后，将架构组件组装成单个工作流。注意失败是如何优雅降级的，而不是导致服务崩溃。

```

Python
import logging

from langchain_core.prompts import ChatPromptTemplate

logger = logging.getLogger(__name__)

def run_pipeline(question: str):
    """执行带有优雅降级的 Token 高效 AI 工作流。"""
    try:
        route = classify_request(question)

        # 将确定性请求路由出 LLM。
        if route == "metrics":
            return {
                "answer": "Retrieve metrics directly from the monitoring system.",
                "sources": [],
            }

        # 一次性检索上下文。
        docs = index.similarity_search(question, k=4)

        context = build_context(docs)

        source_ids = [
            doc.metadata.get("source")
            for doc in docs
            if doc.metadata.get("source")
        ]

        # 检查精确匹配缓存。
        key = cache_key(question, source_ids)

        if key in exact_match_cache:
            return exact_match_cache[key]

        # 选择最合适的模型。
        model = choose_model(question)

        # 将受信任的指令与不受信任的用户输入分开。
        prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    (
                        "Answer the user's question using ONLY the provided context. "
                        "If the answer cannot be determined from the context, say so."
                        "\n\nContext:\n{context}"
                    ),
                ),
                ("user", "{question}"),
            ]
        )

        chain = prompt_template | model

        result = chain.invoke(
            {
                "context": context,
                "question": question,
            }
        )

        payload = validate_response(
            answer=result.content,
            sources=source_ids,
        )

        # 缓存已验证的响应。
        exact_match_cache[key] = payload

        return payload

    except Exception:
        logger.exception("Token-efficient pipeline failed.")

        # 优雅降级而不是崩溃。
        return {
            "answer": (
                "The AI pipeline encountered an error. "
                "Please continue using the standard operational workflow."
            ),
            "sources": [],
        }

```

## 真正减少 Token 使用的是什么？

当团队构建这样的架构时，最大的节省很少来自编辑提示词，而是来自消除不必要的工作。

最大的改进通常源于：

* 只检索一次文档，而不是多次。
* 缓存语义相同的请求。
* 将简单请求路由出 LLM。
* 通过显式的 Token 预算限制上下文。
* 选择最小的合适模型。

这些架构调整降低了成本和延迟，同时使系统行为更易于理解。

## 经验教训

在为生产环境优化 AI 系统时，几个核心原则始终适用：

* **像对待基础设施一样对待 Token：** Token 是有限资源，就像 CPU 周期或内存一样。监控它们、预算它们并优化它们。
* **检索通常是浪费的最大来源：** 重复检索通常比冗长的提示词产生更多不必要的 Token。尽可能共享上下文。
* **更大的模型并不总是更好：** 更小、更快的模型可以有效处理许多操作任务。为真正复杂的推理保留更大的模型。
* **缓存是一项工程功能：** [语义缓存](https://thenewstack.io/redis-launches-vector-sets-and-a-new-tool-for-semantic-caching-of-llm-responses/)不仅仅是一种性能优化，它是核心架构组件，可降低成本、延迟并减少对供应商的依赖。
* **优化前先测量：** 每次生产部署都必须伴随仪器化测量。

随着 AI 系统的成熟，成功将日益依赖于工程效率，而不是纯粹的模型规模。AI 智能体的隐藏税很少是单个昂贵的提示词；它是分布式工作流中冗余检索、过大上下文、不必要的模型调用和重复推理的累积。

> “最有效的生产 AI 系统不是那些生成 Token 最多的系统，而是那些只生成它们真正需要的 Token 的系统。”

通过将 Token 消耗视为[系统工程问题](https://thenewstack.io/ai-retrieval-at-scale/)，组织可以构建更快、更便宜且高度可扩展的 AI 平台。智能路由请求、规划上下文预算、共享检索结果、验证结构化输出以及引入语义缓存，这些都是在不影响质量的前提下保证效率的实用技术。

最有效的生产 AI 系统不是那些生成 Token 最多的系统，而是那些只生成它们真正需要的 Token 的系统。