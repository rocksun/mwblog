在 AI 世界中，“在我机器上能跑”是开发者能说出的最危险的一句话。从 Notebook 转向生产环境不仅仅是迁移代码，构建者必须预见到规模化带来的混乱。

在本地部署中，500 毫秒的延迟只是个小打嗝；但在生产环境中，同样的延迟在数千名用户中产生连锁反应，那就是一场灾难。在设计高性能 AI 系统时，理想的结果是确定性的可预测性。

为了实现这一目标，我们将两个在各自领域最专业的语言结合起来。Python 担任大脑的角色，而 Rust 扮演体力的角色。

核心逻辑是：Python 是 AI 生态系统无可争议的王者，其优势在于抽象，这使其成为系统“智能”部分的完美工具。

Rust 是基础设施的巨无霸，能够处理高风险的网络任务，同时通过保证内存安全的并发性来提升稳定性。

Python 提供智能，但 Rust 提供财务和运营上的责任感。通过本指南，你将了解如何构建一个生产级引擎，它不仅能返回预测结果，而且能以企业级规模所需的精确度和可靠性来完成。

> “Python 提供智能，但 Rust 提供财务和运营上的责任感。”

为了说明这一点，让我们探索如何构建一个在压力下仍能保持高性能，并展现人类智慧以确保系统正常运行的架构。在这种场景下，人类决定什么在何处运行、何时停止生产，以及如何从概率模型中产生确定性。

**边车（Sidecar）：** 我们实现了一个高性能的 WebSocket 网关，作为 Kafka 驱动的后端与多用户之间的实时桥梁。这确保了当 AI 完成分析或工具运行时，用户能立即在浏览器或 Slack 窗口中看到输出。

![智能体工作流设计的视觉艺术](https://cdn.thenewstack.io/media/2026/05/a0b9278a-unnamed-1024x694.jpg)

---

## 高级概述：扇出模式中的 Rust

这段代码解决的核心问题是**高效分发**。与其让每个用户都向 Kafka 集群创建单独且昂贵的连接（这会在负载下使代理崩溃），此代码创建了一个**单一**的主要 Kafka 消费者，并通过内部高速广播通道将消息“扇出”到数千个 WebSocket。

```rust

struct AppState {
    // tx 是“发射器”。我们使用它向每个活动的 WebSocket 连接
    // 广播 Kafka 消息。
    tx: broadcast::Sender<(String, String)>, // 元组: (SessionID, 内容)
}

#[tokio::main]
async fn main() {
    // 使用特定的组 ID 初始化 Kafka 消费者
    let consumer: StreamConsumer = ClientConfig::new()
        .set("bootstrap.servers", "localhost:9092")
        .set("group.id", "githouse-gateway-v1")
        .create()
        .expect("Consumer creation failed");

    // 创建一个带有 1000 条消息缓冲区的广播通道
    let (tx, _rx) = broadcast::channel(1000);
    let tx_clone = tx.clone();

    // ... 路由和服务器设置 ...
}

```

让我们扩展我们的 `AppState` 来管理会话生命周期和控制流。我们使用并发 `DashMap` 来跟踪每个会话的状态，包括其状态、最后活动时间戳和生存时间（TTL）。这允许系统强制执行过期策略，支持多阶段工作流，并在并发情况下保持有界的、可观测的会话状态。

```rust

use dashmap::DashMap;
use std::sync::Arc;
use std::time::{Duration, Instant};
enum SessionStatus {
    Active,
    WaitingForHuman,
    Completed,
    Failed,
}

struct SessionState {
    status: SessionStatus,
    last_seen: Instant,
    ttl: Duration,
}

struct AppState {
    tx: broadcast::Sender<(String, String)>,
    active_sessions: Arc<DashMap<String, SessionState>>,
}

```

```rust

async fn handle_socket(
    mut socket: WebSocket,
    tx: broadcast::Sender<(String, String)>,
    sessions: Arc<DashMap<String, SessionState>>,
    session_id: String,
) {
    let mut rx = tx.subscribe();
    sessions.insert(
        session_id.clone(),
        SessionState {
            status: SessionStatus::Active,
            last_seen: Instant::now(),
            ttl: Duration::from_secs(300),
        },
};

```

```rust

info!(%session_id, "session started");

let mut heartbeat = interval(Duration::from_secs(30));

loop {
tokio::select! {
_ = heartbeat.tick() => {
if socket.send(Message::Ping(vec![])).await.is_err() {
break;
}
}

```

```rust

            result = timeout(Duration::from_secs(300), rx.recv()) => {
                match result {
                    Ok(Ok((key, payload))) if key == session_id => {
                        match serde_json::from_str::<Event>(&payload) {
                            Ok(Event::Resolved { .. }) => {
                                info!(%session_id, "session resolved");
                                if let Some(mut entry) = sessions.get_mut(&session_id) {
                                    entry.status = SessionStatus::Completed;
                                    entry.last_seen = Instant::now();
                                }
                                let sid_clone = session_id.clone();
                                tokio::spawn(
                                    async move {
                                        if let Err(e) = initiate_after_runner(sid_clone.clone()).await {
                                            error!(error = %e, "after-runner failed");
                                        }
                                    }
                                    .instrument(info_span!("after_runner", session_id = %sid_clone))
                                );
                                let _ = socket.send(Message::Text(
                                    "Issue resolved. Closing stream...".into()
                                )).await;
                                break;
                            }
                            Ok(Event::Message { content }) => {
                                if socket.send(Message::Text(content)).await.is_err() {
                                    break;
                                }
                                if let Some(mut entry) = sessions.get_mut(&session_id) {
                                    entry.last_seen = Instant::now();
                                }
                            }
                            Err(e) => {
                                warn!(%session_id, "invalid payload: {}", e);
                                continue;
                            }
                        }
                    }
                    Ok(Ok(_)) => continue,
                 
                    Ok(Err(_)) => break,
                   
                    Err(_) => {
                        info!(%session_id, "session timeout");
                        if let Some(mut entry) = sessions.get_mut(&session_id) {
                            entry.status = SessionStatus::TimedOut;
                        }
                        break;
                    }
                }
            }
        }
    }
    sessions.remove(&session_id);
    info!(%session_id, "session closed");
}

```

```rust

async fn initiate_after_runner(state: Arc<AppState>, session_id: String) {
    // 六西格玛护栏：等待 10 分钟以确保“修复”生效
    println!("After-runner started for session: {}", session_id);
    sleep(Duration::from_secs(600)).await;

    // 模拟工具调用以检查 Githouse CI/CD 状态
    let check_success = verify_githouse_service_health(&session_id).await;

    if check_success {
        println!("Verification successful for {}. Closing ticket permanently.", session_id);
    } else {
        // 确定性重新开启：如果失败，向 Kafka 的 "alerts" 主题发送警报
        eprintln!("Verification FAILED for {}. Re-escalating to human.", session_id);
        // (将重新升级事件发回 Python 的生产者逻辑)
    }
}

```

这是初始化“边车”的入口点。它设置了 Kafka 连接和 HTTP 服务器：

```rust

#[tokio::main]
async fn main() {
    // 使用特定的组 ID 初始化 Kafka 消费者
    let consumer: StreamConsumer = ClientConfig::new()
        .set("bootstrap.servers", "localhost:9092")
        .set("group.id", "githouse-gateway-v1")
        .create()
        .expect("Consumer creation failed");

    // 创建一个带有 1000 条消息缓冲区的广播通道
    let (tx, _rx) = broadcast::channel(1000);
    let tx_clone = tx.clone();

    // ... 路由和服务器设置 ...
}

```

`StreamConsumer` 是一个高级 Kafka 消费者，原生支持 Rust 的 async/await `group.id`；这有助于确保即使你将此网关扩展到多台服务器，Kafka 也会知道它们属于同一个“GitHouse 舰队”。

边车摄取器（sidecar ingestor）是性能最关键的部分，因为它运行在自己的专用线程上且永不停止。

```rust

fn extract_message(msg: &BorrowedMessage) -> Result<(String, String)> {

let key_bytes = msg.key()
.ok_or_else(|| anyhow!(
"missing key | topic={} partition={} offset={}",
msg.topic(),
msg.partition(),
msg.offset()
))?;

let payload_bytes = msg.payload()
.ok_or_else(|| anyhow!(
"missing payload | topic={} partition={} offset={}",
msg.topic(),
msg.partition(),
msg.offset()
))?;
let key = String::from_utf8(key_bytes.to_vec())?;
let payload = String::from_utf8(payload_bytes.to_vec())?;
Ok((key, payload))
}
fn process_message(
    consumer: &impl rdkafka::consumer::Consumer,
    tx: &tokio::sync::broadcast::Sender<(String, String)>,
    msg: rdkafka::message::BorrowedMessage,
) -> Result<()> {

    let (key, payload) = extract_message(&msg)?;
    let _ = tx.send((key, payload));
    consumer.commit_message(
        &msg,
        rdkafka::consumer::CommitMode::Async
    )?;
    Ok(())
}

```

```rust

fn reset_failure_state(backoff: &mut u64, failures: &mut u32) {
    *backoff = 1;
    *failures = 0;
}

async fn handle_kafka_error(
    e: impl std::fmt::Display,
    failures: &mut u32,
    backoff: &mut u64,
) -> bool {
    eprintln!("Kafka error: {}", e);

    *failures += 1;

    // 断路器
    if *failures > 10 {
        eprintln!("Too many Kafka failures, stopping consumer loop");
        return true; // 发出中断信号
    }

    // 指数退避
    sleep(Duration::from_secs(*backoff)).await;
    *backoff = (*backoff * 2).min(30);

    false
}

```

```rust

use anyhow::{anyhow, Result};
use tokio::time::{sleep, Duration};

tokio::spawn(async move {
    if let Err(e) = consumer.subscribe(&["agent-output-topic"]) {
        eprintln!("Kafka subscribe error: {}", e);
        return;
    }

    let mut backoff = 1u64;
    let mut failures = 0u32;

    loop {
        match consumer.recv().await {
            Ok(msg) => {
                reset_failure_state(&mut backoff, &mut failures);

                if let Err(e) = process_message(&consumer, &tx_clone, msg) {
                    eprintln!("Message processing error: {}", e);
                    continue;
                }
            }

            Err(e) => {
                if handle_kafka_error(e, &mut failures, &mut backoff).await {
                    break;
                }
            }
        }
    }
});

```

`Tokio::spawn` 卸载了 Kafka 循环，防止其阻塞 HTTP 服务器。`String::from_utf8_lossy` 安全地处理可能格式错误的数据，而不会导致服务器崩溃。

WebSocket 握手 —— 此函数处理初始 HTTP 请求并将其升级为永久的 WebSocket 连接：

```rust

async fn ws_handler(
    ws: WebSocketUpgrade,
    State(state): State<Arc<AppState>>,
    axum::extract::Path(session_id): axum::extract::Path<String>,
) -> impl IntoResponse {
    // 升级连接并将 session_id 传递给处理程序
    ws.on_upgrade(move |socket| handle_socket(socket, state, session_id))
}

```

由于我们不能依赖 WebSocket URL 是秘密的，我们必须验证请求者具有查看特定 `session_id` 日志的加密权限。

为了使其更加安全，让我们实现 JWT 和 Axum 的 `TypedHeader`。

由于 WebSocket 是通过 GET 请求启动的，我们通常在查询字符串中传递 JWT。然后 Rust 将拦截升级请求，验证签名，交叉引用主体和事件，并根据 URL 中的 `session_id` 验证令牌。

通过将身份验证放在 Rust 网关而不是 AI 智能体中，我们卸载了计算（正如我们所知，Rust 可以处理显著更高的吞吐量）。这确保了大脑可以简单地向 Kafka 发送消息，同时信任边车始终处于警戒状态。

```rust

use axum::{
    extract::{Path, State, WebSocketUpgrade},
    http::StatusCode,
    response::IntoResponse,
};
use axum_extra::{
    headers::{authorization::Bearer, Authorization},
    TypedHeader,
};
use jsonwebtoken::{decode, Algorithm, DecodingKey, Validation};
use serde::{Deserialize, Serialize};
use std::sync::Arc;


#[derive(Debug, Serialize, Deserialize)]
struct Claims {
    sub: String,
    incident_id: String,
    exp: u64,
    aud: String,
    iss: String,
    jti: String,
}

```

```rust

async fn ws_handler(
    ws: WebSocketUpgrade,
    State(state): State<Arc<AppState>>,
    Path(session_id): Path<String>,

    TypedHeader(auth): TypedHeader<Authorization<Bearer>>,
) -> impl IntoResponse {
    let token = auth.token();
    let secret = std::env::var("JWT_SECRET")
.expect("JWT_SECRET must be set; refusing to start without it");

let decoding_key = DecodingKey::from_secret(secret.as_bytes());

let mut validation = Validation::new(Algorithm::HS256);
validation.validate_exp = true;
validation.leeway = 10;
validation.set_audience(&["githouse_websocket_api"]);
validation.set_issuer(&["githouse_auth_service"]);

match decode::<Claims>(token, &decoding_key, &validation) {
Ok(token_data) => {
if token_data.claims.incident_id != session_id {
tracing::warn!(
user_id = %token_data.claims.sub,
attempted_session = %session_id,
"Unauthorized session access"
);

return (
StatusCode::FORBIDDEN,
"Token not valid for this Session",
)
.into_response();
}

ws.on_upgrade(move |socket| handle_socket(socket, state, session_id))
}
Err(_) => {
tracing::warn!("JWT validation failed");
(StatusCode::UNAUTHORIZED, "Invalid Token").into_response()
}
}

```

---

## 高级概述：大脑部分

让我们构建一个专门的智能体网格，由中央路由器驱动，将查询路由到深度集成特定工具集的领域专家。

在“GitHouse”，支持不是铁板一块；它是专业领域的集合。

| 子团队领域 | 专长 | 智能体的主要“工具” |
| --- | --- | --- |
| 账户与安全 (A&S) | 身份、2FA、账户接管 (ATO)、垃圾邮件和条款 (ToS) 违规。 | 审计日志 API、IP 声誉数据库、设备指纹、GitHouse CLI |
| 计费与营收 | 支付、优惠券、计量使用 (Actions/LFS) 和退款。 | Stripe/Braintree、Actions 使用计量器、订阅 API。 |
| 企业支持 | GitHouse Enterprise Cloud (GHEC) & Server (GHES)、SAML/SSO 和 SCIM。 | IdP 日志、XML 握手调试器、企业管理 API。 |
| 开发者支持 | Git 命令、存储库管理、API 和 Webhooks。 | Git Trace 日志、API 速率限制标头、后端状态。 |
| GitHouse Workers & Packages | CI/CD 工作流、运行器（托管/自托管）和容器注册表。 | 工作流 YAML 解析器、运行器遥测、作业日志。 |
| GitHouse ShotGun | 商业版 ShotGun、IDE 扩展和安全性。 | 许可证管理、遥测日志、IDE 版本控制。 |
| GitHouse Discourse | 文档反馈、GitHub 社区论坛和 GitHub Stars。 | Markdown 解析器、GitHouse Discourse API、站点搜索。 |

在构建子团队智能体之前，我们需要一个路由器。它负责识别用户的意图、语气、紧迫性和主题：

```python

from typing import Literal, Optional
from langchain_core.pydantic_v1 import BaseModel, Field

class QueryAnalysis(BaseModel):
    intent: str = Field(description="用户想要采取的主要操作。")
    urgency: Literal["low", "medium", "high", "critical"] = Field(description="优先级。")
    tone: Literal["neutral", "frustrated", "polite", "urgent"] = Field(description="用户的情绪状态。")
    topic: Literal["A&S", "Billing", "Enterprise", "DevSupport", "Workers", "ShotGun", "Discourse", "unknown"] = Field(
        description="GitHouse 子团队领域。如果不符合任何一项，请使用 'unknown'。"
    )
    is_sensitive: bool = Field(description="如果查询涉及密码、令牌或法律威胁，则为 True。")

```

```python

# 此组件处理路由器的“思考”部分。
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 初始化 LLM，并在环境中启用 LangSmith 追踪
llm = ChatOpenAI(model="gpt-4o", temperature=0)
structured_llm = llm.with_structured_output(QueryAnalysis)

router_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是 GitHouse 智能路由器。分析用户的支持查询。"),
    ("human", "{query}")
])

# 链式调用
router_chain = router_prompt | structured_llm

```

让我们将人类支持和安全协议定义为不同的节点和边。

当工作流在中断后恢复时，它将从执行停止的节点开头开始。如果你将多个操作合并到一个大节点中，靠近结尾的故障将需要重新执行该节点的所有操作。另一个考虑因素是，当我们有不同的节点定义和执行时，我们可以监控和检查每个节点。LangGraph 的持久执行在节点边界处创建检查点。

最后，因为节点完成不同的工作，它们的故障将需要配置不同的故障策略，这些策略不能合并。它们还有你可能希望以不同方式实现的重试策略。

```python

import operator
from typing import Annotated, TypedDict, Union
from langgraph.graph import StateGraph, END

# 1. 定义状态
class RouterState(TypedDict):
    query: str
    analysis: Optional[QueryAnalysis]
    destination: str

# 2. 定义节点
def classify_query(state: RouterState):
    """分析意图、语气和主题。"""
    analysis = router_chain.invoke({"query": state["query"]})
    return {"analysis": analysis}

def sensitivity_filter(state: RouterState):
    """检查安全协议。"""
    analysis = state["analysis"]
    if analysis.is_sensitive or analysis.urgency == "critical":
        return {"destination": "HIGH_SECURITY_QUEUE"}
    return {"destination": "STANDARD_QUEUE"}

def human_escalation(state: RouterState):
    """回退节点。"""
    return {"destination": "HUMAN_SUPPORT_LIVE"}

# 3. 定义条件逻辑（路由器）
def route_decision(state: RouterState):
    analysis = state["analysis"]

    # 逻辑：未找到领域 -> 人类
    if analysis.topic == "unknown":
        return "human"

    # 逻辑：继续进行敏感性检查
    return "security"

# 4. 构建图
workflow = StateGraph(RouterState)

workflow.add_node("classifier", classify_query)
workflow.add_node("security_check", sensitivity_filter)
workflow.add_node("human_support", human_escalation)

workflow.set_entry_point("classifier")

# 条件边
workflow.add_conditional_edges(
    "classifier",
    route_decision,
    {
        "human": "human_support",
        "security": "security_check"
    }
)

workflow.add_edge("security_check", END)
workflow.add_edge("human_support", END)

app = workflow.compile()

```

在分类器将其映射到正确的子团队后。如果未找到子团队映射，分类器会将其升级到人工智能体。

分类完成后，我们使用特定的、预定义的安全协议运行敏感性过滤器。我们通过创建一个触发安全协议节点的条件分支来实现这一点，该节点反过来在人类看到消息之前执行预定义的检查，如 IP 声誉检查和日志审计。

为了信任 LLM，检查其置信度分数很重要。如果它不确定（<=0.5），我们将其发送给人类；如果它（>0.85），我们触发协议。

安全节点首先执行后台操作（如审计日志）。然后它可以合成到一个状态中，以根据发现的结果告知后续智能体或人类应采取的方法。

我们用严格的模式定义这些工具。这确保了路由器确切地知道要传递什么数据。

```python

# 我们需要 LLM 识别其敏感的原因，以便协议知道启动哪些工具。
class SecurityMetadata(BaseModel):
    is_sensitive: bool
    risk_category: Literal["none", "ATO", "PII_LEAK", "TOKEN_EXPOSURE", "LEGAL_THREAT"]
    confidence_score: float = Field(description="我们确定这是威胁的 0 到 1 分数")
    extracted_entities: list[str] = Field(description="发现的泄露令牌、IP 或电子邮件列表")

class RouterState(TypedDict):
    query: str
    analysis: QueryAnalysis
    security_metadata: Optional[SecurityMetadata]
    protocol_active: bool
    audit_log_id: str

```

```python

from langchain_core.tools import tool
from typing import List, Dict


@tool
async def revoke_githouse_tokens(tokens: List[str]) -> str:
"""
撤销 GitHouse 个人访问令牌 (PAT)。
绝不返回完整的令牌值。
"""

masked = [f"{t[:4]}…{t[-4:]}" for t in tokens if len(t) >= 8]

return f"成功撤销了 {len(tokens)} 个令牌: {', '.join(masked)}"



@tool
async def check_ip_reputation(ip: str) -> Dict:
    """查询全球 IP 声誉数据库，获取风险评分、VPN 检测和地理位置。"""
    # 逻辑: reputation_provider.get_score(ip)
    return {"ip": ip, "risk_score": 95, "type": "Tor 出口节点", "action": "已标记"}

@tool
async def get_user_audit_logs(username: str) -> List[str]:
    """检索特定 GitHouse 用户的最后 5 个安全关键事件。"""
    # 逻辑: githouse_db.audit_logs.filter(user=username).limit(5)
    return ["SSH 密钥已添加 (2分钟前)", "MFA 已禁用 (10分钟前)", "从新 IP 登录 (11分钟前)"]

# 为 LangGraph 封装它们
security_tools = [revoke_githouse_tokens, check_ip_reputation, get_user_audit_logs]

```

在这个阶段，我们不需要任何额外的输入，所以让我们并行运行工具：

```python

from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI

# 1. 设置专门的安全 LLM
# 我们绑定工具，以便 LLM 知道它有“武器”可以使用。
llm = ChatOpenAI(model="gpt-4o", temperature=0)
security_agent_llm = llm.bind_tools(security_tools)

# 2. 定义“调用”工具的逻辑
async def security_expert_node(state: RouterState):
    """决定启动哪些安全工具的智能体节点。"""
    # 我们将查询 + 任何先前的分析传递给 LLM
    prompt = f"SYSTEM: 检测到安全威胁。执行所有必要协议。查询: {state['query']}"
    response = await security_expert_node_llm.ainvoke(prompt)
    return {"messages": [response]}

# 3. 定义工具执行节点（并行引擎）
tool_node = ToolNode(security_tools)

```

工具返回后，让我们将数据合成到图状态和长期记忆中：

```python

async def synthesize_and_store(state: RouterState):
    """总结工具输出并将事件持久化到长期记忆中。"""
    # 最后一条消息包含工具输出
    tool_outputs = state["messages"][-1].content

    summary_prompt = f"为支持团队合成这些安全工具结果: {tool_outputs}"
    summary = await llm.ainvoke(summary_prompt)

    # --- 长期记忆 (持久化) ---
    # 我们将其存储在 'SecurityIncidents' 表中，以便将来进行 ATO 模式匹配
    # db.save_incident(user_id=state['user_id'], report=summary.content)

    return {
        "security_brief": summary.content,
        "destination": "SECURE_HUMAN_QUEUE"
    }

```

这种设置确保工具并行运行，并且流程仅在所有调用的工具完成后才继续。

```python

workflow = StateGraph(RouterState)

workflow.add_node("agent", security_expert_node)
workflow.add_node("action", tool_node) # 标准 ToolNode 并行运行工具
workflow.add_node("summarize", synthesize_and_store)

workflow.set_entry_point("agent")

# 在此协议中，'action' 节点始终返回到 'summarize' 节点
workflow.add_edge("agent", "action")
workflow.add_edge("action", "summarize")
workflow.add_edge("summarize", END)

app = workflow.compile()

```

---

## 构建领域特定的智能体

为了[指导我们构建智能体](https://thenewstack.io/a-guide-to-building-scalable-ai-agents/)，让我们使用从 GitHouse 的一家企业客户那里收到的查询：

*“嘿，听着，这太荒谬了。我们的整个 CI/CD 管道已经挂了三个小时，我的团队一直在催我。我甚至没法进去修复它，因为我被困在了 2FA 锁定循环里。我该如何给我的首席开发人员权限来增加预算并让这些运行器恢复在线？只要这东西还是坏的，我们[每一分钟都在损失开发时间](https://thenewstack.io/case-study-ai-agent-cuts-api-connector-dev-time-to-minutes/)。”*

接下来，让我们来看看流水线以及这将如何处理。

在这一步中，分类器已经运行并将此查询分类为 8/10 的紧急程度，标记了账户、安全和计费主题。

路由器检查了可用的智能体，并确定我们可以运行账户和计费智能体。结果：安全智能体缺失，因此将升级给人工处理。

从那里，我们将构建账户和计费智能体来解决用户的查询。

SOP（标准作业程序）充当“护栏”和“蓝图”，将通用的 LLM 转变为可靠的领域特定专业人员。如果没有 SOP，智能体只能根据其训练数据进行猜测。SOP 遵循组织的特定逻辑。

> “如果没有 SOP，智能体只能根据其训练数据进行猜测。”

在我们的账户智能体中，SOP 强制执行交易 ID 检查和验证，而不是让智能体猜测如何处理退款请求（这使其容易受到恶意提示词注入的影响）。相反，如果验证失败，它会拒绝请求或将其转发给人工进行澄清。通过消除猜测，我们确保为概率模型提供了确定性的护栏。

SOP 还定义了工作流逻辑和要使用的工具。在执行验证检查之前，你不能让智能体退款。

将 LLM 视为多才多艺的实习生。SOP 就像你在他们入职第一天交给他们的员工手册。没有它，事情会变糟；有了它，他们就是资产。

让我们创建一个账户智能体并启用中间件，该中间件将清理工具提供的所有 PII（个人身份信息）。这一步至关重要，因为我们需要遵守隐私规则和法规。我建议脱敏我们可能从工具中获得的 PII。

```python

from langchain.agents.middleware import PIIMiddleware
from langchain_openai import ChatOpenAI


# 护栏配置
# 策略: 'redact' (已脱敏邮箱), 'mask' (****@****.com),
# 'hash' (确定性匿名)
pii_guardrail = PIIMiddleware(
    pii_types=["email", "credit_card", "ip", "phone"],
    strategy="redact",
    apply_to_input=True,   # 保护提示词
    apply_to_output=True,
)

# 将中间件绑定到我们的聊天模型
# 此模型现在将自动清理它接收到的任何输入
model = ChatOpenAI(model="gpt-4o").with_middleware([pii_guardrail])

```

让我们定义智能体要使用的状态和工具：

```python

from typing import TypedDict, Optional, List
from langgraph.types import interrupt, Command

class ASState(TypedDict):
    query: str
    sop_content: Optional[str]
    audit_logs: List[str]
    messages: list
    user_id: str

@tool
def githouse_grep_logs(pattern: str):
    """安全 grep 工具：仅搜索 /var/log/githouse/audit/ 目录。"""
    # 在此强制执行最小权限逻辑
    return f"LOG_MATCH: 在 14:02 UTC 发现 {pattern} 的 PAT 活动"

```

让智能体执行一次[向量库搜索](https://thenewstack.io/how-to-store-embeddings-in-vector-search-and-implement-rag/)。如果由于任何原因缺失，我们应该中断并允许人类在恢复之前提供 SOP。在这种情况下，智能体将使用 SOP 绑定工具并执行查询。

```python

from langgraph.graph import StateGraph, START, END

async def retrieve_sop_or_ask_human(state: ASState):
    """
    尝试在向量库中查找 SOP。
    如果缺失，使用 interrupt() 等待支持经理提供它。
    """
    # 1. RAG 查找
    sop = vector_db.similarity_search(state["query"], k=1)

    if not sop:
        # 暂停图：这将控制权交还给 UI/人类
        human_input = interrupt({
            "status": "SOP_MISSING",
            "message": "未找到此查询的标准作业程序。请上传/提供 SOP。",
            "context": state["query"]
        })
        # 使用人类提供的文本恢复
        return {"sop_content": human_input["sop_text"]}

    return {"sop_content": sop[0].page_content}

async def execute_as_forensics(state: ASState):
    """智能体使用 SOP 作为其指令和工具进行调查。"""
    system_prompt = f"严格遵守此 SOP: {state['sop_content']}"

    # 已经附加了 PII 中间件的模型
    agent = model.bind_tools([githouse_grep_logs])
    response = await agent.ainvoke([
        ("system", system_prompt),
        ("human", state["query"])
    ])

    return {"messages": [response]}

```

然后，让我们编译图：

```python

workflow = StateGraph(ASState)

workflow.add_node("sop_check", retrieve_sop_or_ask_human)
workflow.add_node("investigate", execute_as_forensics)

workflow.add_edge(START, "sop_check")
workflow.add_edge("sop_check", "investigate")
workflow.add_edge("investigate", END)

# 中断正常工作需要持久化检查点
from langgraph.checkpoint.memory import InMemorySaver
checkpointer = InMemorySaver()

as_app = workflow.compile(checkpointer=checkpointer)

```

现在，是时候起草给客户的回应了。

你可以使用手头的草稿回应智能体来完成此操作。但重要的是要记住，这一步尚未获得管理层批准以自主与客户沟通。因此，每个回应在继续之前都必须经过人工核实。

```python

from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware, AgentMiddleware, AgentState, hook_config
from langgraph.runtime import Runtime
from typing import Any

class GitHousePolicyGuardrail(AgentMiddleware):
    """确定性护栏：防止智能体提到“绕过”或“变通方法”。"""

    @hook_config(can_jump_to=["end"])
    def before_agent(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
if not state["messages"]:
return None

content = state["messages"][-1].content.lower()

if self.is_policy_violation(content):
runtime.logger.warning(
"检测到违反政策",
extra={"content_preview": content[:200]}
)

return {
"messages": [{
"role": "assistant",
"content": "错误：建议的草案违反了安全 SOP。正在重定向到人工。"
}],
"jump_to": "end"
}

return None

def is_policy_violation(self, text: str) -> bool:
patterns = [
"bypass",
"circumvent",
"work around",
"skip verification",
"ignore policy",
"disable security",
"绕过",
"规避",
"跳过验证",
"忽略政策",
]
return any(p in text for p in patterns)

# 组合中间件栈
middleware_stack = [
    PIIMiddleware("email", strategy="redact", apply_to_input=True),
    PIIMiddleware("credit_card", strategy="mask", apply_to_input=True),
    GitHousePolicyGuardrail()
]

```

```python

from dataclasses import dataclass
from langgraph.store.memory import InMemoryStore

@dataclass
class SupportContext:
    user_id: str
    ticket_urgency: str

store = InMemoryStore()

# 专门的草稿智能体
draft_agent = create_agent(
    model="claude-3-5-sonnet", # 高质量的文字和推理能力
    tools=[], # 草稿智能体的“工具”是其从存储中读取的能力
    middleware=middleware_stack,
    store=store,
    context_schema=SupportContext,
    system_prompt=(
        "你是 GitHouse 首席沟通官。合成 A&S 和计费的调查结果。"
        "结构：1. 同理心, 2. 安全要求, 3. 计费解决方案。"
        "严格遵循消息中提供的检索到的 SOP 上下文。"
    )
)

```

草稿智能体的输出使用 `interrupt()` 来暂停系统。人类必须提供一个命令来恢复。

```python

from langgraph.types import interrupt, Command

async def human_review_node(state: GitHouseState):
    """暂停图以允许人类批准或编辑 AI 的草稿。"""
    ai_draft = state["messages"][-1].content

    # 这会物理上停止执行并将状态保存到检查点
    print("--- [等待人工批准] ---")
    review_result = interrupt({
        "proposed_draft": ai_draft,
        "urgency": state["analysis"].urgency,
        "instructions": "批准以发送，或编辑下面的文本。"
    })

    # 处理人类的决定
    if review_result["action"] == "approve":
        return {"final_output": ai_draft, "status": "sent"}
    elif review_result["action"] == "edit":
        return {"final_output": review_result["edited_text"], "status": "sent_with_edits"}

    # 如果拒绝，我们循环回到 'synthesizer' 以尝试不同的方法
    return Command(goto="synthesizer")

```

最后，与所有支持事件一样，反馈对于确保下次提供更好的服务至关重要。

因此，让我们创建一个反馈智能体，它将收集客户的反馈并确定问题是否按照他们的预期得到了解决。

```python

from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware

# 中断件确保反馈不会将账户 ID 泄露到日志中
feedback_middleware = [
    PIIMiddleware("email", strategy="redact", apply_to_input=True),
    PIIMiddleware("api_key", strategy="block", apply_to_input=True)
]

feedback_agent = create_agent(
    model="claude-3-5-sonnet",
    tools=[save_user_info, update_security_checkpoint], # 重用我们的工具
    middleware=feedback_middleware,
    store=store,
    context_schema=SupportContext,
    system_prompt=(
        "你是 GitHouse 体验研究员。你的目标是收集反馈"
        "并确定技术阻碍是否已解决。使用乐于助人、非侵入性的语气。"
    )
)

```

```python

async def consolidate_memory_node(state: GitHouseState):
    """
    在用户提供反馈后运行的最终节点。
    它将交互保存到长期记忆 (LTM)。
    """
    user_id = state["context"].user_id

    # 定义“事件记忆”对象
    incident_summary = {
        "incident_id": state.get("ticket_id"),
        "resolution": state.get("final_response"),
        "sentiment": state.get("user_feedback_sentiment"),
        "sop_used": state.get("sop_content"),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    # 1. 存储在用户特定记忆中
    # 这允许智能体下次说：“我看到上个月我们帮你处理了 2FA 锁定……”
    store.put(("user_history",), user_id, incident_summary)

    # 2. 存储在组织记忆中（模式）
    # 如果来自同一组织的 10 个用户都有此问题，“企业智能体”会收到警报。
    org_id = state["context"].org_id
    store.put(("org_analytics",), org_id, {"last_incident": "2FA_Lockout_Budget_Exceeded"})

    return {"status": "ARCHIVED"}

```

我们的多智能体流水线现在将查询转化为结构化的、符合政策的解决方案。它从摄取查询开始，触发相关节点对查询进行分类并隔离特定主题和工具。然后，在发送之前使用 RAG 人机回环 (HITL) 审批。该循环以反馈智能体确认解决并保存来自客户和工作流的反馈到长期记忆中而告终，以此优化未来的系统流程。