<!--
title: 为什么大多数AI项目在演示成功后却会失败？
cover: https://cdn.thenewstack.io/media/2026/03/13f1af2a-imhaf-maulana-ffuad9izkse-unsplash-scaled.jpg
summary: 大多数AI项目在演示成功后仍会失败，因为生产级AI系统是复杂的分布式系统，需要深思熟虑的架构、可观测性、成本控制和防护栏。文章提供了12步指南，强调将AI视为关键生产软件。
-->

大多数AI项目在演示成功后仍会失败，因为生产级AI系统是复杂的分布式系统，需要深思熟虑的架构、可观测性、成本控制和防护栏。文章提供了12步指南，强调将AI视为关键生产软件。

> 译自：[Why most AI projects fail after the demo actually works](https://thenewstack.io/ai-demo-to-production/)
> 
> 作者：Oladimeji Sowole

构建一个AI演示很容易。但要交付一个能够在生产环境中日复一日、负载下可靠运行、预算内且具有可观测性的AI系统，却很难。许多团队只有在令人印象深刻的概念验证在面对真实用户、真实数据和真实操作约束时崩溃之后，才发现这个差距。

> “构建一个AI演示很容易。但要交付一个能够在生产环境中可靠运行的AI系统……却很难。”

生产级AI系统不仅仅是模型。它们是必须处理故障、控制成本、安全演进并与现有基础设施集成的分布式系统。本指南展示了生产级AI系统背后的核心架构模式，以及一个简化的参考实现。

你将学习如何：

*   为生产环境构建AI服务
*   使用现代LLM编排
*   添加检索、防护栏和成本意识
*   以可扩展、可观测的方式部署

## 为什么AI在生产中会崩溃

大多数AI演示在生产中失败的原因相同：

*   推理、检索和执行之间没有明确分离
*   缺乏可观测性（你不知道模型在做什么）
*   没有成本控制或令牌限制
*   模型逻辑与应用逻辑之间的紧密耦合
*   除了“运行此脚本”之外没有部署策略

生产级AI系统必须像任何其他关键服务一样对待：它们必须进行版本控制、监控和可扩展，以实现弹性。

## 参考架构

一个生产级AI系统通常包括：

1.  API层：FastAPI或类似框架
2.  LLM编排层：LangChain
3.  知识层：向量数据库（FAISS, Qdrant, Pinecone）
4.  工具层：API、数据库、服务
5.  防护栏：模式验证、策略检查
6.  可观测性：日志、指标、追踪
7.  基础设施：容器、Kubernetes、IaC

在本指南中，我们将实现此技术栈的简化但现实的版本。

## 步骤1：安装依赖

```
pip install fastapi uvicorn \
  langchain langchain-openai langchain-community \
  pydantic faiss-cpu tiktoken
```

要点：

*   `langchain-openai`是OpenAI模型必需的
*   `langchain-community`提供向量存储和实用工具

## 步骤2：初始化LLM

```
import os
from langchain_openai import ChatOpenAI

openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY must be set")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    openai_api_key=openai_api_key
)
```

### 为什么这很重要

*   明确的API密钥验证[可防止静默故障](https://thenewstack.io/mastering-deadman-alerts-to-prevent-silent-failures/)
*   `'gpt-4o-mini'`通常是需要强大延迟和性价比的生产工作负载的经济高效选择，尽管模型选择应根据你的准确性和预算目标进行验证。

## 步骤3：构建知识层（向量存储）

生产级AI系统通常使用检索增强生成（RAG）将响应基于真实数据。

```
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document

embeddings = OpenAIEmbeddings(
model="text-embedding-3-small",
openai_api_key=openai_api_key
)

docs = &#91;
    Document(page_content="All customer data must be encrypted at rest."),
    Document(page_content="Refunds require manager approval above $500."),
]

vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
```

这使得能够：

*   企业知识基础
*   降低幻觉风险
*   与重新训练模型相比，更新更快

## 步骤4：将检索作为工具公开

当检索被视为工具而非硬编码逻辑时，代理系统表现最佳。

```
from langchain.tools import Tool

def retrieve_policy(query: str) -> str:
    docs = retriever.invoke(query)
    return "\n".join(d.page_content for d in docs)

tools = &#91;
    Tool(
        name="PolicyRetriever",
        func=retrieve_policy,
        description="Retrieve internal company policies."
    )
]
```

这种分离允许：

*   工具审计
*   权限控制
*   后续安全扩展

## 步骤5：明确管理对话状态

```
from typing import Dict, List
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage

# Demo-only in-memory store.
# In production, replace with Redis, Postgres, DynamoDB, etc.
conversation_store: Dict&#91;str, List&#91;BaseMessage]] = {}

def load_history(session_id: str) -> List&#91;BaseMessage]:
    return conversation_store.get(session_id, &#91;])

def append_user_message(session_id: str, content: str) -> None:
    history = conversation_store.setdefault(session_id, &#91;])
    history.append(HumanMessage(content=content))

def append_ai_message(session_id: str, content: str) -> None:
    history = conversation_store.setdefault(session_id, &#91;])
    history.append(AIMessage(content=content))
```

内存对于生产至关重要，原因如下：

*   对话连贯性
*   用户体验
*   有状态工作流

## 步骤6：初始化代理（生产安全）

```
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(&#91;
("system", "You are a helpful assistant that uses tools when needed."),
("human", "{input}"),
("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)
```

一旦初始化，此代理可以：

*   规划步骤
*   在需要时调用工具
*   生成有根据的响应

## 步骤7：验证和清理AI响应

生产系统绝不应直接将原始LLM输出返回给用户。相反，在离开服务边界之前，响应应进行验证、清理并转换为可预测的模式。这确保了下游系统接收到结构化、可靠的数据，并防止畸形输出在系统中传播。

``` python
from pydantic import BaseModel, Field
from typing import List

class AgentResponse(BaseModel):
answer: str = Field(description="Direct answer to the user")
sources: List&#91;str] = Field(default_factory=list, description="Supporting sources")

structured_llm = llm.with_structured_output(AgentResponse)

result = structured_llm.invoke(
"Answer the user question and include any relevant source identifiers."
)
```

> “生产级AI系统绝不应直接将原始LLM输出返回给用户。相反，响应应进行验证、清理并转换为可预测的模式。”

防护栏有助于减少几类运行时问题，包括：

*   意外的输出形状
*   模式违规
*   一些下游解析失败

然而，仅靠防护栏不足以防止提示注入或不安全的工具执行。生产系统还应实施额外的控制措施，例如工具允许列表、授权检查、输入过滤以及对高风险操作进行人工审查。

## 步骤8：将所有内容封装到FastAPI服务中

``` python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Production AI Service")

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_agent(payload: Query):
try:
result = agent_executor.invoke({"input": payload.question})
return {"answer": result&#91;"output"]}
except Exception:
raise HTTPException(status_code=500, detail="Internal server error")
```

为什么这很重要：

*   将AI逻辑与客户端解耦
*   实现扩展、认证、速率限制
*   完美融入微服务架构

本地运行：

`uvicorn main:app --host 0.0.0.0 --port 8080`

## 步骤9：添加成本意识（常被忽视）

成本控制是生产级AI的重要组成部分。

``` python
import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o-mini")

def estimate_tokens(messages: list&#91;dict]) -> int:
    """
    Rough token estimate for a list of chat messages.

    Note: This is only an approximation. Real request cost depends on
    system prompts, retrieved context, tool call arguments, and
    generated output tokens returned by the model provider.
    """
    total_tokens = 0

    for message in messages:
        content = message.get("content", "")
        total_tokens += len(encoder.encode(content))

    return total_tokens
```

在生产中：

*   记录每次请求的令牌使用量
*   设置每个用户或每个端点的预算
*   为常规任务路由廉价模型

## 步骤10：可观测性基础

至少记录：

*   输入
*   工具调用
*   令牌使用量
*   错误

``` python
import logging
logging.basicConfig(level=logging.INFO)

def log_event(event: str, data: dict):
    logging.info({"event": event, **data})
```

在成熟系统中，集成：

*   OpenTelemetry
*   Prometheus/Grafana
*   集中式日志存储

## 步骤11：容器化部署

在容器化之前，创建一个与指南中使用的包匹配的requirements.txt文件。

``` requirements.txt
fastapi
uvicorn
langchain
langchain-openai
langchain-community
pydantic
faiss-cpu
tiktoken
```

```
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD &#91;"uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```

这使得能够：

*   一致的环境
*   Kubernetes部署
*   CI/CD管道

## 步骤12：使用Kubernetes进行扩展（概念性）

在生产中，部署：

*   多个副本
*   水平Pod自动扩缩
*   通过环境变量管理密钥
*   用于成本控制的资源限制

AI系统扩展不可预测。Kubernetes通过设计来处理这种复杂性。

## 关键生产经验

1.  AI系统是[分布式](https://thenewstack.io/rethinking-system-architecture-the-rise-of-distributed-intelligence-with-ebpf/)系统
2.  可观测性不能是可选的
3.  必须控制成本，而不是抱有希望
4.  防护栏对于保护用户和系统都是必要的
5.  基础设施与模型同样重要

## 生产级AI的新方法

[将AI从演示推向生产](https://thenewstack.io/ai-prototype-to-production-postgres/)需要更好的系统和完全摒弃炒作。

可靠的AI系统需要深思熟虑的架构、明确的职责分离和生产纪律。通过结合现代LLM编排、检索、防护栏、可观测性和云原生部署，团队可以构建出不仅令人印象深刻，而且在生产中可靠且具有弹性的AI服务。

成功的组织将把AI视为生产软件，以与任何任务关键型系统相同的严谨性进行工程设计。