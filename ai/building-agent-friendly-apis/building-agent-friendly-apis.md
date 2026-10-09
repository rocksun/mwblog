<!--
title: 为AI应用构建可扩展、智能体友好的API
cover: https://cdn.thenewstack.io/media/2026/10/ee1a9e41-resource-database-joz4ohpe8f4-unsplash.jpg
summary: 本文探讨了AI智能体流量与传统网页流量的区别，指出传统单体API在处理智能体多轮对话时容易丢失上下文。通过借鉴2010年代的微服务原则（如无状态、舱壁隔离），结合Oracle AI Database Free实现数据收敛，文章提出了一种可扩展、支持智能体的API架构设计方案。
-->

本文探讨了AI智能体流量与传统网页流量的区别，指出传统单体API在处理智能体多轮对话时容易丢失上下文。通过借鉴2010年代的微服务原则（如无状态、舱壁隔离），结合Oracle AI Database Free实现数据收敛，文章提出了一种可扩展、支持智能体的API架构设计方案。

> 译自：[Building scalable, agent-friendly APIs for AI applications](https://thenewstack.io/building-agent-friendly-apis/)
> 
> 作者：Nacho Martínez

如今，我们大多数人都在以结构化的方式与前沿AI模型进行交互，尽管我们并不总是这样认为。大多数系统已经建立在协议之上，这些协议通常由模型提供者自己创建。例如，[OpenAI和Anthropic](https://thenewstack.io/ai-agent-harness-pricing-split/)各自提供API来与其推理系统进行通信。

在实践中，一种方法是使用兼容OpenAI的API，该API可以为多轮智能体提供服务。我们可以将官方的OpenAI SDK指向兼容的推理端点，与智能体保持对话，并在多轮对话中使用相同的接口。

这些系统以一种特定且巧妙的方式构建，使它们能够扩展。当流量增长或子智能体衍生时，需要对这些系统进行扩展，以便我们作为工程师能够在用户无感的情况下进行必要的调整。例如，当我们需要额外的流量支持时，我们可能会在负载均衡器后面将单副本系统扩展为三个副本，同时仍保留正确的对话上下文和之前的轮次。

> “五年前大家不再讨论的微服务原则，恰恰成了智能体流量所需要的东西。”

我们将探讨在AI流量突发时会发生什么。

在开发这些系统之前我们需要自问的许多问题，2010年代的微服务文献中已经探讨过了。我们将展示如何根据这些原则重建一个对智能体友好的API，并以[Oracle AI Database Free](https://www.oracle.com/database/free/?source=:ex:pw:::::TNS_SAFA_A&SC=:ex:pw:::::TNS_SAFA_A&pcode=)作为后端，同时测量所发生的变化。

## 为什么智能体流量不同于网页流量

**核心见解：** 负载形态是不同的，而这种差异正是状态化设计难以承受的。

区分智能体客户端与浏览器的四个属性：

1. **对话是长期的且有状态的，但请求不是。** 一个包含40轮的智能体循环会产生40个独立的HTTP请求。协议中的任何内容都不会将它们绑定到一台服务器。每次工具调用在HTTP层都是无状态的：端点随着时间接收单独的请求和响应，因此应用程序需要确定请求属于哪个对话以及其状态驻留在何处。
2. **工具调用会不可预测地发散。** 一个聊天请求可能会触发零个下游调用，也可能触发六个，其中一个会命中向量索引并花费400毫秒。由于模型输出和工具选择路径可能不同，即使相同的输入也可能触发不同序列和数量的工具调用。
3. **智能体进行激进的重试。** AI智能体通常被包装在一个带有自身控制循环、错误处理和重试策略的智能体套件中。当发生超时或错误时，系统可能会收到来自同一工作负载的快速连续重试。这对于弹性很有帮助，但它也会放大对本来就已经苦苦挣扎的依赖项的压力。
4. **负载具有突发性且由机器驱动。** 轮次之间几乎没有或根本没有思考时间。当AI智能体在运行时，它可以产生连续的工作爆发，主要受其周围的硬件和并发限制所约束。

第1点是人们通常理解的一点：由于粘性和人类思考时间，浏览器会话在一台服务器上存活。而智能体可以连续快速发出多个请求，如果没有持久的共享状态，跨副本分发的请求可能会丢失所需的上下文，从而给用户造成摩擦。

## 每个人构建的第一个版本

这里展示了整个故障，在一个端点中：

```python
SESSIONS: dict[str, list] = {}
SLOTS = asyncio.Semaphore(int(os.environ.get("CONCURRENCY", "32")))  # 一组池

@app.post("/v1/chat/completions")
async def chat(req: Request):
    body = await req.json()
    sid = req.headers.get("x-session-id") or body.get("user")
    async with SLOTS:                                 # 一切共享它
        history = SESSIONS.setdefault(sid, [])
        history.append({"role": "user", "content": body["messages"][-1]["content"]})
        if body.get("tools"):
            await TOOLS[body["tools"][0]["function"]["name"]]()   # 内联、在路径中
        ...
```

这是一个正确、可运行且极简的兼容OpenAI的API。装饰器确立了当调用端点时，以下函数将异步运行。

这个极简的端点通过了所有测试，但有一个根本性的缺陷。你能发现它吗？

在我们的POC基准测试中，我们驱动了200个对话，每个对话四轮，将每一轮发送到轮换中的下一个可用副本——这就是当未正确配置粘性参数时可以看到的那种分发：

| 部署 | 轮次 | 丢失的上下文 | 丢失率 |
| --- | --- | --- | --- |
| 单体，**1台机器** | 800 | 0 | **0.0%** |
| 单体，**3台机器** | 800 | 600 | **75.0%** |
| 解耦，1台机器 | 800 | 0 | 0.0% |
| 解耦，3台机器 | 800 | 0 | **0.0%** |

看看单机部署与三机部署的对比。设计并未损坏；它是条件正确的。条件是每一轮都到达同一台机器，而这正是当你进行扩展时放弃的条件。

> “失败是无声的。模型仍然会回答，但它可能在没有正确上下文的情况下回答，因为请求落在了没有先前聊天历史记录的其他机器上。”

失败是无声的。模型仍然会回答，但它可能在没有正确上下文的情况下回答，因为请求落在了没有先前聊天历史记录的其他机器上。可观测性可能仍然显示HTTP 200响应，但从用户的角度来看，系统表现并不正确。这就是我们在[为AI应用设计API](https://thenewstack.io/why-databases-need-apis/)时需要考虑的差异。

## 回归原则

**Key insight:** 修复方案中的任何内容都不是新的。它是刘易斯和福勒（Lewis and Fowler）的[微服务特征](https://martinfowler.com/articles/microservices.html)（2014年）以及迈克尔·尼加德（Michael Nygard）在《Release It!》中的舱壁模式，被应用于编写时并不存在的请求形态。

有三个原则起到了关键作用：

**无状态性：** 对话状态移出进程并进入共享存储。任何副本都可以为任何对话的任何轮次提供服务。这一单项改变使先前的端点能够跨副本扩展，而不依赖于进程局部的对话状态：如果智能体可以从集中式位置检索其所需的内容，我们就不需要在每个请求中来回发送完整的聊天历史记录。

**舱壁（又称隔离）：** 其理念是隔离系统的不同部分[以防止级联故障](https://thenewstack.io/acm-vibe-coding-ai-agent/)。在这种情况下，我们按*依赖关系*进行隔离，而不是全局隔离。

**智能端点，愚蠢管道：** OpenAI聊天补全协议是一个异常有用的传输层：相对较小、稳定、已被许多智能体框架支持，并且为AI开发者所熟悉。我们将智能（路由、预算、记忆工程、上下文工程、工具调用策略）置于其之上，而不是内部。保持管道简单。

## POC：四个服务，一个协议

![展示单体和网关+服务架构的图片](https://cdn.thenewstack.io/media/2026/10/e309ac0a-image.png)

*架构*

解耦的技术栈按照故障域划分，而不是按照名词：

* **网关（gateway）** — 使用OpenAI协议，不持有任何内容，并且可水平扩展
* **记忆（memory）** — 拥有对话状态和工具审计跟踪；其他任何东西都不得持有消息列表
* **工具（tools）** — 在其自己的进程中执行工具，拥有自己的并发预算和超时时间
* **Oracle AI Database Free** — 所有这些之下的共享基底

正如架构所示，关键在于尽可能多地隔离，同时使每个组件专注于一项工作。这可以使组件更容易独立演进。它还为我们留出了空间，可以为每个依赖项设置单独的并发预算、超时和其他配置参数。

你可以用信号量来实现这一点：它们让我们能够控制对共享资源的访问，这正是我们所需要的。

```python
CHAT_SLOTS = asyncio.Semaphore(int(os.environ.get("CHAT_CONCURRENCY", "24")))
TOOL_SLOTS = asyncio.Semaphore(int(os.environ.get("GW_TOOL_CONCURRENCY", "8")))
```

由于协议保持不变，官方SDK可以与此兼容OpenAI的端点通信，而无需修改SDK本身：

```python
from openai import OpenAI
c = OpenAI(base_url="http://127.0.0.1:8110/v1", api_key="")

c.models.list()          # ['agent-gateway/router-v1']
r1 = c.chat.completions.create(model="agent-gateway/router-v1",
        messages=[{"role": "user", "content": "hello"}], user="demo-1")
r2 = c.chat.completions.create(model="agent-gateway/router-v1",
        messages=[{"role": "user", "content": "and again"}], user="demo-1")
# r1 -> "turn 1"   r2 -> "turn 3"   (状态存活，在不同的副本上)
```

由于网关独立地向记忆组件写入数据，并且通过信号量控制并发，该设计避免了跨副本依赖本地文件系统状态。

## 舱壁值得拥有吗？

舱壁隔离了我们应用程序的不同组件，以防止故障在它们之间传播。例如，我们可以将工具调用路径与标准聊天补全路径分开。

想象一下，我们有一个系统，能够正确划分组件并将工具调用请求与标准聊天补全分离开来，如图所示：

![比较舱壁请求时间的图片](https://cdn.thenewstack.io/media/2026/10/b9d9bc85-image.png)

*来自我们POC的舱壁比较*

两个栈每个副本都获得32个准入槽位。单体方法从一个请求池中消耗它们。网关将其拆分：24个用于纯聊天，8个用于带工具的请求。基准测试驱动每秒120个聊天请求，同时有300个并发调用者猛击400毫秒的工具。

> “如果没有舱壁，进行标准聊天请求的用户最终可能会在缓慢的工具调用后面等待，因为每个请求都在争夺同一个池。”

如果没有舱壁，进行标准聊天请求的用户最终可能会在缓慢的工具调用后面等待，因为每个请求都在争夺同一个池。通过隔离，工具压力可以与标准聊天池隔离，从而有助于为标准聊天流量保留容量。

## Oracle AI Database Free的契合点

**核心见解：** “每个服务一个数据库”可能是你在AI应用中不希望统一应用的微服务原则。

2014年盛行的建议是给每个服务提供自己的数据存储，因为共享模式的耦合成本超过了最终一致性的协调成本。

对于智能体来说，这种计算可能会颠倒，因为单个智能体轮次会写入必须一致的四件事：

* 对话状态
* 工具调用记录（及顺序）
* 从轮次中提取的语义、情景和工作流记忆事实
* 阻止重试重新执行付费工具的幂等性分类账条目

如果你决定将这些拆分到不同的数据存储中——一个在Postgres中，一个在向量存储中，另一个在Redis中——你就会得到一个应用程序现在必须管理的一致性问题。数据库几十年来一直在解决事务一致性，因此该架构可以利用数据库事务能力来共同管理这些相关的写入。

将它们放在一个数据库中使其成为一个事务提交：

```sql
CREATE TABLE agent_sessions (
  session_id   VARCHAR2(64) PRIMARY KEY,
  messages     JSON NOT NULL,                 -- 原生JSON，而不是你要解析的CLOB
  version      NUMBER DEFAULT 1 NOT NULL,     -- 乐观并发
  updated_at   TIMESTAMP WITH TIME ZONE DEFAULT SYSTIMESTAMP NOT NULL
);

CREATE TABLE agent_memory (
  memory_id    VARCHAR2(64) PRIMARY KEY,
  session_id   VARCHAR2(64),
  content      CLOB NOT NULL,
  embedding    VECTOR(1024, FLOAT32)          -- 同一行，同一事务
);

CREATE VECTOR INDEX ix_memory_vec ON agent_memory (embedding)
  ORGANIZATION NEIGHBOR PARTITIONS DISTANCE COSINE WITH TARGET ACCURACY 95;
```

关系型、JSON和向量数据在一个引擎、一个事务、一个备份、一套凭据中。[Oracle AI Database混合向量搜索](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/understand-hybrid-vector-indexes.html?source=:ex:pw:::::TNS_SAFA_B&SC=:ex:pw:::::TNS_SAFA_B&pcode=)允许检索查询在单个语句中检索所需内容、关联工具历史记录并按余弦距离排序——而不是在Python中跨三个系统进行关联，否则可能需要跨多个系统进行应用级别的协调。

数据库为水平扩展的API做的另一件事是帮助协调并发轮次。为同一对话的轮次提供服务的两个副本是正常的，而不是例外的。SELECT … FOR UPDATE加上版本列可以串行化冲突的更新并实现重试处理，而不是让竞争的更新覆盖对话状态。

## 反直觉的部分：解耦计算，收敛数据

每个人都求助于微服务来扩展AI应用，但统一应用该原则可能会在智能体的记忆、审计日志和向量索引之间产生一致性挑战。

> “有用的拆分是不对称的：解耦计算，收敛数据。”

有用的拆分是不对称的：解耦计算，收敛数据。

2014年的原则依然适用。我们只需要使它们适应AI智能体的新时代。

*准备好尝试该架构了吗？下载* [*Oracle AI Database Free*](https://www.oracle.com/database/free/?source=:ex:pw:::::TNS_SAFA_A&SC=:ex:pw:::::TNS_SAFA_A&pcode=)*，安装* [*Oracle AI Agent Memory Python包*](https://pypi.org/project/oracleagentmemory/)*，并按照本地快速入门指南为你的智能体API添加持久状态和持久记忆。更多示例请访问* [*Oracle AI开发者中心*](https://github.com/oracle-devrel/oracle-ai-developer-hub)*。*