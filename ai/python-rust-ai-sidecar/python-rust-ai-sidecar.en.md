In the world of AI, “it works on my machine” is the most dangerous phrase a developer can muster. Transitioning from a notebook to a production environment is about more than moving code. Builders must anticipate the chaos of scale.

In a local deployment, a 500ms delay is a hiccup; in production, the same delay, cascading across thousands of users, is a disaster. When designing high-performance AI systems, the ideal outcome is deterministic predictability.

To achieve this, we marry the two most specialized languages for their domains. Python serves as the brain, and Rust plays the role of brawn.

The breakdown: Python is the undisputed King of the AI ecosystem; its strength lies in abstraction, which makes it the perfect tool for the “intelligence” part of the system.

Rust is the infrastructure juggernaut; handling high-stakes networking while boosting stability with concurrency that guarantees memory safety.

Python provides the intelligence, but Rust provides the fiscal and operational responsibility. By the end of this guide, you will understand how to build a production-grade engine that doesn’t just return a prediction, but does so with the precision and reliability that enterprise scale demands.

> “Python provides the intelligence, but Rust provides the fiscal and operational responsibility.”

To put this in context, let’s explore how to architect a system that remains performant under pressure and displays the human intelligence that keeps the train on its tracks. In this scenario, humans make the call on what runs where, when production stops, and how to generate determinism from a probabilistic model.

The sidecar: We implement a high-performance WebSocket Gateway that serves as the real-time bridge between the Kafka-driven backend and multiple users. This ensures that when the AI finishes an analysis or a tool run, the user sees the output instantly in their browser or Slack window.

![Visual art of agentic workflow design](https://cdn.thenewstack.io/media/2026/05/a0b9278a-unnamed-1024x694.jpg)


---

## High-level overview: Rust in the fan-out pattern

The core problem this code solves is **Efficient Distribution**. Instead of every single user creating a separate, expensive connection to your Kafka cluster (which would crash the broker under load), this code creates a **single** primary Kafka consumer and “fans out” messages to thousands of WebSockets via an internal high-speed broadcast channel.

```

struct AppState {
    // tx is the 'transmitter'. We use it to blast Kafka messages
    // to every active WebSocket connection.
    tx: broadcast::Sender&lt;(String, String)>, // Tuple: (SessionID, Content)
}

#[tokio::main]
async fn main() {
    // Initialize the Kafka Consumer with a specific group ID
    let consumer: StreamConsumer = ClientConfig::new()
        .set("bootstrap.servers", "localhost:9092")
        .set("group.id", "githouse-gateway-v1")
        .create()
        .expect("Consumer creation failed");

    // Create a broadcast channel with a buffer of 1000 messages
    let (tx, _rx) = broadcast::channel(1000);
    let tx_clone = tx.clone();

    // ... Router and Server setup ...
}

```

Let’s extend our AppState to manage session lifecycle and control flow. We use a concurrent DashMap to track each session’s state, including its status, last activity timestamp, and time to live. This allows the system to enforce expiration, support multi-stage workflows, and maintain bounded observable session state under concurrency.

```

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
    tx: broadcast::Sender&lt;(String, String)>,
    active_sessions: Arc&lt;DashMap&lt;String, SessionState>>,
}

```

```

async fn handle_socket(
    mut socket: WebSocket,
    tx: broadcast::Sender&lt;(String, String)>,
    sessions: Arc&lt;DashMap&lt;String, SessionState>>,
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

```

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

```

            result = timeout(Duration::from_secs(300), rx.recv()) => {
                match result {
                    Ok(Ok((key, payload))) if key == session_id => {
                        match serde_json::from_str::&lt;Event>(&amp;payload) {
                            Ok(Event::Resolved { .. }) => {
                                info!(%session_id, "session resolved");
                                if let Some(mut entry) = sessions.get_mut(&amp;session_id) {
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
                                if let Some(mut entry) = sessions.get_mut(&amp;session_id) {
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
                        if let Some(mut entry) = sessions.get_mut(&amp;session_id) {
                            entry.status = SessionStatus::TimedOut;
                        }
                        break;
                    }
                }
            }
        }
    }
    sessions.remove(&amp;session_id);
    info!(%session_id, "session closed");
}

```

```

async fn initiate_after_runner(state: Arc&lt;AppState>, session_id: String) {
    // 6-Sigma Guardrail: Wait 10 minutes to ensure the "fix" holds
    println!("After-runner started for session: {}", session_id);
    sleep(Duration::from_secs(600)).await;

    // Simulation of a tool call to check Githouse CI/CD status
    let check_success = verify_githouse_service_health(&amp;session_id).await;

    if check_success {
        println!("Verification successful for {}. Closing ticket permanently.", session_id);
    } else {
        // Deterministic Re-opening: If it failed, alert the Kafka "alerts" topic
        eprintln!("Verification FAILED for {}. Re-escalating to human.", session_id);
        // (Producer logic to send re-escalation event back to Python)
    }
}

```

This is the entry point where the “Sidecar” is initialized. It sets up the Kafka connection and the HTTP server:

```

#[tokio::main]
async fn main() {
    // Initialize the Kafka Consumer with a specific group ID
    let consumer: StreamConsumer = ClientConfig::new()
        .set("bootstrap.servers", "localhost:9092")
        .set("group.id", "githouse-gateway-v1")
        .create()
        .expect("Consumer creation failed");

    // Create a broadcast channel with a buffer of 1000 messages
    let (tx, _rx) = broadcast::channel(1000);
    let tx_clone = tx.clone();

    // ... Router and Server setup ...
}

```

`StreamConsumer` is a high-level Kafka consumer that works natively with Rust’s async/await `group.id`; helpful for ensuring that, even if you scale this gateway to multiple servers, Kafka knows they are part of the same “GitHouse Fleet.”

The sidecar ingestor is the most critical part of the performance because it runs its own dedicated thread and never stops.

```

fn extract_message(msg: &amp;BorrowedMessage) -> Result&lt;(String, String)> {

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
    consumer: &amp;impl rdkafka::consumer::Consumer,
    tx: &amp;tokio::sync::broadcast::Sender&lt;(String, String)>,
    msg: rdkafka::message::BorrowedMessage,
) -> Result&lt;()> {

    let (key, payload) = extract_message(&amp;msg)?;
    let _ = tx.send((key, payload));
    consumer.commit_message(
        &amp;msg,
        rdkafka::consumer::CommitMode::Async
    )?;
    Ok(())
}

```

```

fn reset_failure_state(backoff: &amp;mut u64, failures: &amp;mut u32) {
    *backoff = 1;
    *failures = 0;
}

async fn handle_kafka_error(
    e: impl std::fmt::Display,
    failures: &amp;mut u32,
    backoff: &amp;mut u64,
) -> bool {
    eprintln!("Kafka error: {}", e);

    *failures += 1;

    // Circuit breaker
    if *failures > 10 {
        eprintln!("Too many Kafka failures, stopping consumer loop");
        return true; // signal break
    }

    // Backoff
    sleep(Duration::from_secs(*backoff)).await;
    *backoff = (*backoff * 2).min(30);

    false
}

```

```

use anyhow::{anyhow, Result};
use tokio::time::{sleep, Duration};

tokio::spawn(async move {
    if let Err(e) = consumer.subscribe(&amp;["agent-output-topic"]) {
        eprintln!("Kafka subscribe error: {}", e);
        return;
    }

    let mut backoff = 1u64;
    let mut failures = 0u32;

    loop {
        match consumer.recv().await {
            Ok(msg) => {
                reset_failure_state(&amp;mut backoff, &amp;mut failures);

                if let Err(e) = process_message(&amp;consumer, &amp;tx_clone, msg) {
                    eprintln!("Message processing error: {}", e);
                    continue;
                }
            }

            Err(e) => {
                if handle_kafka_error(e, &amp;mut failures, &amp;mut backoff).await {
                    break;
                }
            }
        }
    }
});

```

`Tokio::spawn` offloads the Kafka loop, preventing it from blocking the HTTP server. `String::from_utf8_lossy` handles potentially malformed data safely without crashing the server:

The Websocket Handshake — This function handles the initial HTTP request and upgrades it to a permanent WebSocket connection:

```

async fn ws_handler(
    ws: WebSocketUpgrade,
    State(state): State&lt;Arc&lt;AppState>>,
    axum::extract::Path(session_id): axum::extract::Path&lt;String>,
) -> impl IntoResponse {
    // Upgrade the connection and pass the session_id to the handler
    ws.on_upgrade(move |socket| handle_socket(socket, state, session_id))
}

```

Since we cannot rely on the WebSocket URL being secret, we must verify that the requester has the cryptographic authority to view the logs for a specific session\_id.

To make it even more secure, let’s implement JWT and Axum’s TypedHeader.

Since websockets are initiated via a GET request, we typically pass a JWT in the query string. Rust will then intercept the upgrade request, validate the signature, cross-reference the subject and the incident, and claim the token against the session\_id in the URL.

By placing the auth in the Rust gateway rather than the AI agent, we offload the compute (which as we know, Rust can handle significantly higher throughput). This ensures that the brain can simply emit to Kafka while trusting the sidecar is always on the lookout.

```

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

```

async fn ws_handler(
    ws: WebSocketUpgrade,
    State(state): State&lt;Arc&lt;AppState>>,
    Path(session_id): Path&lt;String>,

    TypedHeader(auth): TypedHeader&lt;Authorization&lt;Bearer>>,
) -> impl IntoResponse {
    let token = auth.token();
    let secret = std::env::var("JWT_SECRET")
.expect("JWT_SECRET must be set; refusing to start without it");

let decoding_key = DecodingKey::from_secret(secret.as_bytes());

let mut validation = Validation::new(Algorithm::HS256);
validation.validate_exp = true;
validation.leeway = 10;
validation.set_audience(&amp;["githouse_websocket_api"]);
validation.set_issuer(&amp;["githouse_auth_service"]);

match decode::&lt;Claims>(token, &amp;decoding_key, &amp;validation) {
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

## High-level overview: the brains

Let’s build a specialized agentic mesh powered by a central router that routes queries to domain experts with deep integration into specific toolsets.

At “GitHouse,” support isn’t a monolith; it’s a collection of specialized domains.

|  |  |  |
| --- | --- | --- |
| **Sub-Team Domain** | **Specialty** | **Primary “Tools” for the Agent** |
| Account & Security (A&S) | Identity, 2FA, ATO, Spam, and Terms of Service (ToS) violations. | Audit Log API, IP Reputation DB, Device Fingerprinting, GitHouse CLI |
| Billing & Revenue | Payments, Coupons, Metered Usage (Actions/LFS), and Refunds. | Stripe/Braintree, Actions Usage Meters, Subs API. |
| Enterprise Support | GitHouse Enterprise Cloud (GHEC) & Server (GHES), SAML/SSO, and SCIM. | IdP Logs, XML Handshake debuggers, Enterprise Admin API. |
| Dev Support | Git commands, Repository management, API, and Webhooks. | Git Trace logs, API Rate-Limit Headers, Backend status. |
| GitHouse Workers & Packages | CI/CD Workflows, Runners (Hosted/Self), and Container Registry. | Workflow YAML Parser, Runner Telemetry, Job Logs. |
| GitHouse ShotGun | ShotGun for Business, IDE Extensions, and Safety. | License Management, Telemetry Logs, IDE versioning. |
| GitHouse Discourse | Documentation feedback, GitHub Community Forum, and GitHub Stars. | Markdown parsers, GitHouse Discourse API, Site Search. |

Before we build the sub-team agents, we need a router. This identifies the users’ intent, tone,  urgency, and topic:

```

from typing import Literal, Optional
from langchain_core.pydantic_v1 import BaseModel, Field

class QueryAnalysis(BaseModel):
    intent: str = Field(description="The primary action the user wants to take.")
    urgency: Literal["low", "medium", "high", "critical"] = Field(description="Priority level.")
    tone: Literal["neutral", "frustrated", "polite", "urgent"] = Field(description="User's emotional state.")
    topic: Literal["A&S", "Billing", "Enterprise", "DevSupport", "Workers", "ShotGun", "Discourse", "unknown"] = Field(
        description="The GitHouse sub-team domain. Use 'unknown' if it doesn't fit any."
    )
    is_sensitive: bool = Field(description="True if query involves passwords, tokens, or legal threats.")

```

```

#This component handles the "thinking" part of the router.
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Initialize LLM with LangSmith tracing enabled in environment
llm = ChatOpenAI(model="gpt-4o", temperature=0)
structured_llm = llm.with_structured_output(QueryAnalysis)

router_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are the GitHouse Intelligent Router. Analyze the user query for support."),
    ("human", "{query}")
])

# The Chain
router_chain = router_prompt | structured_llm

```

Let’s define the Human Support and Security protocol as distinct nodes and edges.

When a workflow resumes after an interruption, it will start from the beginning of the node where the execution stopped. If you combine multiple operations into a single large node, a failure near the end will require re-executing everything from that node. Another consideration is that when we have distinct node definitions and executions, we can monitor and inspect each node. LangGraphs durable execution creates checkpoints at node boundaries.

Lastly, because nodes do different jobs, their failures will require the configuration of distinct failure strategies that cannot be combined. They also have different retry strategies that you may want to implement differently.

```

import operator
from typing import Annotated, TypedDict, Union
from langgraph.graph import StateGraph, END

# 1. Define the State
class RouterState(TypedDict):
    query: str
    analysis: Optional[QueryAnalysis]
    destination: str

# 2. Define the Nodes
def classify_query(state: RouterState):
    """Analyze intent, tone, and topic."""
    analysis = router_chain.invoke({"query": state["query"]})
    return {"analysis": analysis}

def sensitivity_filter(state: RouterState):
    """Checks for security protocols."""
    analysis = state["analysis"]
    if analysis.is_sensitive or analysis.urgency == "critical":
        return {"destination": "HIGH_SECURITY_QUEUE"}
    return {"destination": "STANDARD_QUEUE"}

def human_escalation(state: RouterState):
    """Fallback node."""
    return {"destination": "HUMAN_SUPPORT_LIVE"}

# 3. Define Conditional Logic (The Router)
def route_decision(state: RouterState):
    analysis = state["analysis"]

    # Logic: No domain found -> Human
    if analysis.topic == "unknown":
        return "human"

    # Logic: Proceed to sensitivity check
    return "security"

# 4. Build the Graph
workflow = StateGraph(RouterState)

workflow.add_node("classifier", classify_query)
workflow.add_node("security_check", sensitivity_filter)
workflow.add_node("human_support", human_escalation)

workflow.set_entry_point("classifier")

# Conditional Edges
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

After the classifier maps it to the correct sub-team. If a sub-team map isn’t found, the classifier escalates to a human agent.

Once the classification is done, we run a sensitivity filter with specific, predefined security protocols. We achieve this by creating a conditional branch that triggers a security protocol node, which, in turn, executes predefined checks such as IP reputation checks and log audits before a human sees the message.

To trust the LLM, it’s important to check its confidence score. If it is uncertain <=0.5, we send it to a human; if it is >0.85, we trigger the protocol.

The security node performs background actions (such as audit logs) first. And then it can be synthesized into a state to inform subsequent agents or a human about the approach to take based on the findings.

We define these tools with strict schemas. This ensures the router knows exactly what data to pass.

```

# We need the LLM to identify why it's sensitive so the protocol
# knows which tools to spin up.
class SecurityMetadata(BaseModel):
    is_sensitive: bool
    risk_category: Literal["none", "ATO", "PII_LEAK", "TOKEN_EXPOSURE", "LEGAL_THREAT"]
    confidence_score: float = Field(description="0 to 1 score of how certain we are this is a threat")
    extracted_entities: list[str] = Field(description="List of leaked tokens, IPs, or emails found")

class RouterState(TypedDict):
    query: str
    analysis: QueryAnalysis
    security_metadata: Optional[SecurityMetadata]
    protocol_active: bool
    audit_log_id: str

```

```

from langchain_core.tools import tool
from typing import List, Dict


@tool
async def revoke_githouse_tokens(tokens: List[str]) -> str:
"""
Revokes GitHouse Personal Access Tokens.
Never returns full token values.
"""

masked = [f"{t[:4]}…{t[-4:]}" for t in tokens if len(t) >= 8]

return f"Successfully revoked {len(tokens)} tokens: {', '.join(masked)}"



@tool
async def check_ip_reputation(ip: str) -> Dict:
    """Queries the Global IP Reputation DB for risk scores, VPN detection, and geolocation."""
    # Logic: reputation_provider.get_score(ip)
    return {"ip": ip, "risk_score": 95, "type": "Tor Exit Node", "action": "Flagged"}

@tool
async def get_user_audit_logs(username: str) -> List[str]:
    """Retrieves the last 5 security-critical events for a specific GitHouse user."""
    # Logic: githouse_db.audit_logs.filter(user=username).limit(5)
    return ["SSH Key Added (2m ago)", "MFA Disabled (10m ago)", "Login from New IP (11m ago)"]

# Wrap them for LangGraph
security_tools = [revoke_githouse_tokens, check_ip_reputation, get_user_audit_logs]

```

At this stage, we do not require any additional input, so let’s run the tools in parallel:

```

from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI

# 1. Setup the Specialized Security LLM
# We bind the tools so the LLM knows it has 'weapons' to use.
llm = ChatOpenAI(model="gpt-4o", temperature=0)
security_agent_llm = llm.bind_tools(security_tools)

# 2. Define the Logic to "Call" the tools
async def security_expert_node(state: RouterState):
    """The Agent node that decides which security tools to fire."""
    # We pass the query + any previous analysis to the LLM
    prompt = f"SYSTEM: A security threat was detected. Execute all necessary protocols. Query: {state['query']}"
    response = await security_agent_llm.ainvoke(prompt)
    return {"messages": [response]}

# 3. Define the Tool Execution Node (The Parallel Engine)
tool_node = ToolNode(security_tools)

```

Once the tools return, let’s synthesize the data into the graph state and long-term memory:

```

async def synthesize_and_store(state: RouterState):
    """Summarizes tool outputs and persists the incident to Long-Term Memory."""
    # Last message contains the tool outputs
    tool_outputs = state["messages"][-1].content

    summary_prompt = f"Synthesize these security tool results for the Support Team: {tool_outputs}"
    summary = await llm.ainvoke(summary_prompt)

    # --- LONG TERM MEMORY (Persistent) ---
    # We store this in a 'SecurityIncidents' table for future ATO pattern matching
    # db.save_incident(user_id=state['user_id'], report=summary.content)

    return {
        "security_brief": summary.content,
        "destination": "SECURE_HUMAN_QUEUE"
    }

```

This setup ensures that tools run in parallel and that the flow continues only after all called tools finish.

```

workflow = StateGraph(RouterState)

workflow.add_node("agent", security_expert_node)
workflow.add_node("action", tool_node) # Standard ToolNode runs tools in parallel
workflow.add_node("summarize", synthesize_and_store)

workflow.set_entry_point("agent")

# The 'action' node always returns to the 'summarize' node in this protocol
workflow.add_edge("agent", "action")
workflow.add_edge("action", "summarize")
workflow.add_edge("summarize", END)

app = workflow.compile()

```

---

## Building domain-specific agents

To [guide us through the building of the agents](https://thenewstack.io/a-guide-to-building-scalable-ai-agents/), let’s use a query received from one of GitHouse’s enterprise clients:

*“Hey, look, this is getting ridiculous. Our entire CI/CD pipeline has been dead for three hours, and my team is breathing down my neck. I can’t even get in to fix it because I’m stuck in a 2FA lockout loop. How do I give my Lead Dev the permissions to increase the budget and get these runners back online? We’re losing [dev time every minute](https://thenewstack.io/case-study-ai-agent-cuts-api-connector-dev-time-to-minutes/) this stays broken.*

Next, let’s go through the pipeline and how this will be handled.

At this step, the classifier has run and classified this query with an urgency of 8/10, flagging the topics of account, security, and billing.

The router has checked the available agents and determined that we can run the account and the billing agent. Outcome: the security agent is missing and will therefore be escalated to a human.

From there, we’ll build the account and the billing agent that will resolve the user’s query.

SOPs (Standard Operating Procedures) act as the “guardrails” and “blueprints” that transform a generic LLM into a reliable, domain-specific pro. Without SOPs, an agent is guessing based on its training data. The SOPs follow the organization’s specific logic.

> “Without SOPs, an agent is guessing based on its training data.”

In our account agent, instead of the agent guessing how to handle a refund request (which makes it susceptible to malicious prompt injection), the SOP mandates a transaction ID check and verification. Conversely, if verification fails, it rejects the request or forwards it to a human for clarification. By removing guesswork, we ensure a deterministic guardrail to the probabilistic model.

The SOPs also define the workflow logic and which tools to use. You cannot get an agent to refund before it performs a validation check.

Think of LLMs as multi-talented interns. The SOPs serve as an employee handbook that you give them on their first day. Without it, things go south; with it, they are an asset.

Let’s create an account agent and enable a middleware that will scrub all PII provided by the tools. This step is crucial because we need to be compliant to privacy rules and regulations. I recommend redacting the PII we may obtain from the tools.

```

from langchain.agents.middleware import PIIMiddleware
from langchain_openai import ChatOpenAI


# Configuration for the Guardrail
# Strategies: 'redact' [REDACTED_EMAIL], 'mask' (****@****.com),
# 'hash' (deterministically anonymous)
pii_guardrail = PIIMiddleware(
    pii_types=["email", "credit_card", "ip", "phone"],
    strategy="redact",
    apply_to_input=True,   # Protect the prompt
    apply_to_output=True,
)

# Bind the middleware to our Chat Model
# This model will now automatically clean any input it receives
model = ChatOpenAI(model="gpt-4o").with_middleware([pii_guardrail])

```

Let’s define the state and tools to be used by the agent:

```

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
    """Secure grep tool: Only searches the /var/log/githouse/audit/ directory."""
    # Enforced Least Privilege logic here
    return f"LOG_MATCH: Found PAT activity for {pattern} at 14:02 UTC"

```

Let’s have the agent perform a [vector store search](https://thenewstack.io/how-to-store-embeddings-in-vector-search-and-implement-rag/). If it is missing for any reason, we should interrupt and allow the human to provide the SOP before we resume. In this case, the agent would use the SOP to bind the tools and perform the query.

```

from langgraph.graph import StateGraph, START, END

async def retrieve_sop_or_ask_human(state: ASState):
    """
    Attempt to find the SOP in Vector Store.
    If missing, use interrupt() to wait for a Support Manager to provide it.
    """
    # 1. RAG lookup
    sop = vector_db.similarity_search(state["query"], k=1)

    if not sop:
        # PAUSE GRAPH: This returns control to the UI/Human
        human_input = interrupt({
            "status": "SOP_MISSING",
            "message": "No Standard Operating Procedure found for this query. Please upload/provide the SOP.",
            "context": state["query"]
        })
        # Resume with the human's provided text
        return {"sop_content": human_input["sop_text"]}

    return {"sop_content": sop[0].page_content}

async def execute_as_forensics(state: ASState):
    """Agent uses the SOP as its directive and tools for the investigation."""
    system_prompt = f"Follow this SOP strictly: {state['sop_content']}"

    # Model with PII Middleware already attached
    agent = model.bind_tools([githouse_grep_logs])
    response = await agent.ainvoke([
        ("system", system_prompt),
        ("human", state["query"])
    ])

    return {"messages": [response]}

```

Then, let’s compile the graph:

```

workflow = StateGraph(ASState)

workflow.add_node("sop_check", retrieve_sop_or_ask_human)
workflow.add_node("investigate", execute_as_forensics)

workflow.add_edge(START, "sop_check")
workflow.add_edge("sop_check", "investigate")
workflow.add_edge("investigate", END)

# Persistent checkpointer is REQUIRED for interrupts to work
from langgraph.checkpoint.memory import InMemorySaver
checkpointer = InMemorySaver()

as_app = workflow.compile(checkpointer=checkpointer)

```

Now, it’s time to draft a response to the client.

You can use the draft response agent at hand for this. But it’s important to remember that this step has not been approved by management to communicate with clients autonomously. Consequently, every response must be verified by a human before proceeding.

```

from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware, AgentMiddleware, AgentState, hook_config
from langgraph.runtime import Runtime
from typing import Any

class GitHousePolicyGuardrail(AgentMiddleware):
    """Deterministic guardrail: Prevent the agent from mentioning 'bypass' or 'workaround'."""

    @hook_config(can_jump_to=["end"])
    def before_agent(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
if not state["messages"]:
return None

content = state["messages"][-1].content.lower()

if self.is_policy_violation(content):
runtime.logger.warning(
"Policy violation detected",
extra={"content_preview": content[:200]}
)

return {
"messages": [{
"role": "assistant",
"content": "Error: Proposed draft violates Security SOP. Redirecting to Human."
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
]
return any(p in text for p in patterns)

# Combined Middleware Stack
middleware_stack = [
    PIIMiddleware("email", strategy="redact", apply_to_input=True),
    PIIMiddleware("credit_card", strategy="mask", apply_to_input=True),
    GitHousePolicyGuardrail()
]

```

```

from dataclasses import dataclass
from langgraph.store.memory import InMemoryStore

@dataclass
class SupportContext:
    user_id: str
    ticket_urgency: str

store = InMemoryStore()

# The specialized Drafting Agent
draft_agent = create_agent(
    model="claude-3-5-sonnet", # High-quality prose and reasoning
    tools=[], # The draft agent's 'tools' are its ability to read from the store
    middleware=middleware_stack,
    store=store,
    context_schema=SupportContext,
    system_prompt=(
        "You are the GitHouse Lead Communicator. Synthesize the A&S and Billing findings. "
        "Structure: 1. Empathy, 2. Security Requirement, 3. Billing Solution. "
        "Strictly follow the retrieved SOP context provided in the messages."
    )
)

```

The Draft Agent’s output uses the `interrupt()` to pause the system. A human must provide a command to resume.

```

from langgraph.types import interrupt, Command

async def human_review_node(state: GitHouseState):
    """Pauses the graph to allow a human to approve or edit the AI's draft."""
    ai_draft = state["messages"][-1].content

    # This physically stops the execution and saves state to a checkpointer
    print("--- [WAITING FOR HUMAN APPROVAL] ---")
    review_result = interrupt({
        "proposed_draft": ai_draft,
        "urgency": state["analysis"].urgency,
        "instructions": "Approve to send, or edit the text below."
    })

    # Process the human's decision
    if review_result["action"] == "approve":
        return {"final_output": ai_draft, "status": "sent"}
    elif review_result["action"] == "edit":
        return {"final_output": review_result["edited_text"], "status": "sent_with_edits"}

    # If rejected, we loop back to the 'synthesizer' to try a different approach
    return Command(goto="synthesizer")

```

Finally, as with all support incidents, feedback is crucial to ensuring better service provision next time.

So, let’s create a feedback agent that will gather feedback from the client and determine whether an issue is resolved in accordance with their expectations.

```

from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware

# Middleware ensures feedback doesn't leak account IDs into the logs
feedback_middleware = [
    PIIMiddleware("email", strategy="redact", apply_to_input=True),
    PIIMiddleware("api_key", strategy="block", apply_to_input=True)
]

feedback_agent = create_agent(
    model="claude-3-5-sonnet",
    tools=[save_user_info, update_security_checkpoint], # Reusing our tools
    middleware=feedback_middleware,
    store=store,
    context_schema=SupportContext,
    system_prompt=(
        "You are the GitHouse Experience Researcher. Your goal is to collect feedback "
        "and determine if the technical blocker was resolved. Use a helpful, non-intrusive tone."
    )
)

```

```

async def consolidate_memory_node(state: GitHouseState):
    """
    Final node that runs after the user provides feedback.
    It saves the interaction to Long-Term Memory (LTM).
    """
    user_id = state["context"].user_id

    # Define the "Incident Memory" object
    incident_summary = {
        "incident_id": state.get("ticket_id"),
        "resolution": state.get("final_response"),
        "sentiment": state.get("user_feedback_sentiment"),
        "sop_used": state.get("sop_content"),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    # 1. Store in User-Specific Memory
    # This allows the agent to say next time: "I see we helped you with a 2FA lockout last month..."
    store.put(("user_history",), user_id, incident_summary)

    # 2. Store in Organizational Memory (Patterns)
    # If 10 users from the same Org have this issue, the 'Enterprise Agent' gets an alert.
    org_id = state["context"].org_id
    store.put(("org_analytics",), org_id, {"last_incident": "2FA_Lockout_Budget_Exceeded"})

    return {"status": "ARCHIVED"}

```

Our multi-agent pipeline now transforms queries into a structured policy-compliant resolution. It begins by ingesting queries, triggering relevant nodes to classify them and isolate specific topics and tools. Then it uses RAG human-in-the-loop (HITL) approvals before it is sent. The cycle concludes with a feedback agent confirming the resolution and saving feedback from both the clients and the workflow into long-term memory to refine future system processes.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/65126d72-borisheadshot-1-600x600.png)

Boris Chabeda is a systems engineer focused on the intersection of high-concurrency infrastructure and intelligent automation. His work centers on architecting resilient environments that bridge the gap between experimental development and production-grade reliability. By integrating specialized languages and agentic frameworks,...

Read more from Boris Chabeda](https://thenewstack.io/author/boris-chabeda/)