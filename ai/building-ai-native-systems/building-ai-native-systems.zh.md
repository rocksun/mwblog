### 核心问题： “脆弱的”企业

传统企业软件是确定性的；由一系列“If-Then”语句组成，当业务条件发生变化时，这些语句就会失效。历史上，组织通过在手动数据对账和分析上花费数千小时的人力来填补这一“逻辑鸿沟”。

AI 原生系统的特权是从软件 1.0（固定逻辑）转向软件 2.0（学习逻辑）。我们不仅仅是像实现聊天机器人那样“插入” AI。事实上，我们正在围绕它从根本上重建企业，使其能够：

*   **处理不确定性的推理：** 使用概率模型来处理用户请求。
*   **安全扩展：** 使用“屏蔽”架构，防止 AI 做出未经审核的高风险举动。
*   **保持问责制：** 确保 AI 的每一个“想法”都被记录下来以供审计。

本博客将借助分层架构来穿越这一迷宫，展示企业如何在不牺牲合规性或安全性的情况下构建 AI 原生应用。

![构建 AI 原生系统所涉及的所有移动部件的矢量图](https://cdn.thenewstack.io/media/2026/05/d1830de9-1-1024x789.png)

## 第 0 层：确定性屏蔽（治理与身份）：AIMS

目标：确保无论 LLM “决定”什么，AI 都永远不会违反公司政策。

治理必须是模型无关的。如果你从 Claude 切换到 Gemini，你的 PII（个人身份信息）规则不应该改变。通过拥有“预处理”和“后处理”网关，可以确保敏感数据永远不会接触第三方 API（入站），并且 AI 永远不会泄露内部秘密（出站）。

> “治理必须是模型无关的。如果你从 Claude 切换到 Gemini，你的 PII 规则不应该改变。”

```python

# 入站网关
@app.post("/gateway/query")
async def inbound_shield(
request: UserRequest,
principal: Principal = Depends(verify_jwt)
):
	user_id = principal.sub
	user_role = await asyncio.to_thread(ldap.get_role, user_id)
	clean_query = scrubber.redact(request.text)
	trace_id = generate_otel_trace()

try:
await kafka.produce_and_flush(
"inbound_queries",
{
"trace_id": trace_id,
"query": clean_query,
"role": user_role,
},
timeout=5
)
except Exception as e:
logger.error("Kafka enqueue failed | trace=%s err=%s", trace_id, e)
raise HTTPException(status_code=503, detail="Queue unavailable")

return {"status": "queued", "trace_id": trace_id}

```

*   在企业中，LDAP “身份”是最昂贵的资产，因为它被用来强制执行最小权限。如果 AI 被询问“CEO 工资数据”，AIMS 层会在请求到达编排器 *之前* 检查用户的 LDAP 角色。这可以防止“提示词注入”绕过你的安全设置。

## 第 1 层：编排层

目标：从“无状态聊天”转向“有状态业务流程”。

与逻辑硬编码的传统应用不同，AI 原生系统使用像 LangChain 这样的编排层来管理“思维链”。

*   **解耦逻辑：** “大脑”（LLM/模型）与“工具”（API、数据库）分离。这允许企业在不重写应用的情况下更换模型（例如，从 GPT-4 迁移到微调后的 Llama-3）。

为了实现这一点，它必须首先使用分类器：高端模型（如 Claude 3.5 Opus）昂贵且缓慢。一个[小语言模型](https://thenewstack.io/why-upstage-builds-small-language-models/) (SLM) 充当“分诊护士”。它确定查询是简单的（确定性脚本）、复杂的（生成式 AI），还是需要人工介入。通过将简单任务路由到更便宜的计算资源，这可以节省高达 80% 的推理成本。

*   **RAG 模式（检索增强生成）：** 通过从[向量数据库检索专有数据](https://thenewstack.io/vectors-tensors-ai-search-explained/)并将其作为“上下文”反馈到模型提示词中，防止“幻觉”。
*   AI 原生系统必须在跨多天的流水线中记住上下文。
*   编排器使用“检查点”来保存对话或任务的状态。

> “小语言模型 (SLM) 充当‘分诊护士’。它确定查询是简单的、复杂的，还是需要人工介入。”

为了真正做到审计就绪，请使用自定义检查点。与其仅仅保存到内存中，这种逻辑确保每一次轮换都镜像到你的永久数据库中。

```python

import json
import os
from langgraph.checkpoint.base import BaseCheckpointSaver

class EnterpriseAuditSaver(BaseCheckpointSaver):
def put(self, config, checkpoint, metadata):
"""
确保每个检查点写入在允许图运行之前被持久化
（审计完整性的失败关闭机制）。
"""

thread_id = config["configurable"]["thread_id"]
checkpoint_id = checkpoint["id"]

try:
s3.put_object(
Bucket=os.getenv("AUDIT_BUCKET"),
Key=f"{thread_id}/{checkpoint_id}.json",
Body=json.dumps(checkpoint, default=str),
ServerSideEncryption="aws:kms",
)

db.execute(
"""
INSERT INTO traces (thread_id, checkpoint_id, state_blob)
VALUES (%s, %s, %s)
""",
(thread_id, checkpoint_id, json.dumps(checkpoint, default=str))
)

except Exception as e:
logger.exception(
"Audit write failed | thread=%s checkpoint=%s error=%s",
thread_id,
checkpoint_id,
str(e)
)
raise

return super().put(config, checkpoint, metadata)


# 编译图
# checkpointer = EnterpriseAuditSaver()
# app = workflow.compile(checkpointer=checkpointer)

```

*   **工具/函数调用：** 编排器被授予“工具”（API 或内部数据库）。编排器确保 MCP 使用严格定义的模式调用这些工具，以防止“虚假”的 API 调用。
*   传统的 AI “链”是单行道。如果一个工具失败了（例如，SQL 数据库宕机），简单的链就会崩溃。LangGraph 允许系统“对错误进行推理”。它可以捕获异常，查看错误日志，并决定是尝试不同的工具还是通知人工。
*   **人机协作 (HITL)：** 最佳实践规定，对于高风险决策（如信贷审批），编排器必须暂停 Agent 并在继续之前等待人工“确认”。

```python

import os

COMPLEXITY_THRESHOLD = int(os.getenv("COMPLEXITY_THRESHOLD", "7"))
CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", "0.95"))

MODEL_REGISTRY = {
"high": "claude-sonnet-4-5",
"low": "gpt-4o-mini"
}

def estimate_confidence(response):
"""
置信度必须是推导出来的，而不是假设的。
生产环境中的选项：
- logprob 聚合
- 自我批评模型
- 外部评估模型
"""
return getattr(response, "logprob_score", 0.8)


def call_model(state: GraphState):

if state["complexity"] > COMPLEXITY_THRESHOLD:
model = MODEL_REGISTRY["high"]
else:
model = MODEL_REGISTRY["low"]


response = llm.invoke(state["prompt"], model=model)

confidence = estimate_confidence(response)

if confidence < CONFIDENCE_THRESHOLD:
return "trigger_dehydration"

return "finalize_result”


# 定义图
workflow = StateGraph(GraphState)
workflow.add_node("reasoning", call_model)
workflow.add_edge("reasoning", "tools")

```

## 第 2 层：持久化中枢

目标：使 AI 原生系统“异步且持久”。

如果你的 AI 编排器容器在思考中途崩溃，消息仍会保留在 Kafka 主题中。当容器重启时，它会从上次中断的地方精确继续。这种“神经系统”提供了零数据丢失。

*   **事件驱动触发：** 系统不再仅仅是“提示-响应”。它们使用工具在数据库记录更改或事件发生时自动触发 AI Agent。
*   AI 推理成本昂贵。如果一个流程需要人工审批，你不希望一个容器在内存中坐等 4 小时来等待点击。建议：实施 **水合/脱水 (Hydration/Dehydration)** 机制。
*   **脱水** 将“大脑状态”序列化并移动到廉价存储（RDBMS/S3）。
*   Step Functions 处理“休眠”逻辑。
*   **再水合** 仅在需要时唤醒系统，从而最小化[云成本并最大化资源](https://thenewstack.io/engineers-guide-to-cloud-cost-optimization-engineering-resources-in-the-cloud/)可用性。

```python

import json
import os
import re
import boto3

s3_client = boto3.client("s3")

THREAD_ID_PATTERN = re.compile(r"[A-Za-z0-9_-]{1,64}")


def _validate_thread_id(thread_id: str) -> str:
if not isinstance(thread_id, str) or not THREAD_ID_PATTERN.fullmatch(thread_id):
raise ValueError(f"Invalid thread_id: {thread_id!r}")
return thread_id

def dehydrate_to_s3(state, task_token, thread_id):
"""
序列化 AI 状态并暂停执行。
安全性：
- 验证 thread_id 以防止路径遍历 / 租户逃逸
- 对存储状态进行加密
"""
thread_id = _validate_thread_id(thread_id)

bucket = os.environ["AI_STATE_BUCKET"]
checkpoint_key = f"checkpoints/{thread_id}/state.json"

try:
s3_client.put_object(
Bucket=bucket,
Key=checkpoint_key,
Body=json.dumps(state, default=str),
ServerSideEncryption="aws:kms",
)

# db.update_metadata(thread_id, status="WAITING_FOR_HUMAN", #s3_ptr=checkpoint_key)

print(f"Pausing workflow. Task Token: {task_token}")

except Exception as e:
logger.exception("Dehydration failed | thread=%s err=%s", thread_id, e)
raise

return {"status": "DEHYDRATED", "s3_ptr": checkpoint_key}

```

## 为什么要采用这种“分层”策略 (S3 + RDBMS)?

| 存储类型 | 用途 | 原因 |
| --- | --- | --- |
| RDBMS / DynamoDB | 元数据与索引 | 用于控制面板显示“待办任务”列表。它存储 thread\_id、时间戳和指针。对于像 *“显示所有等待 HR 审批的任务”* 这样的查询非常快。 |
| Amazon S3 | 大型状态对象 | LangGraph 状态可能会变得非常庞大（聊天历史、检索到的文档）。随着时间的推移，RDBMS 数据库处理大型 JSON 对象会变得吃力。S3 以极低的成本处理 10MB+ 的状态，并保留它们用于监管审计。 |

当 HITL 交互并点击“批准”时，应用会调用此 Lambda 来重新唤醒 AI，即“再水合”。

```python

import json
import os
import re
import boto3

s3_client = boto3.client("s3")
sfn_client = boto3.client("stepfunctions")

THREAD_ID_PATTERN = re.compile(r"[A-Za-z0-9_-]{1,64}")

def _validate_thread_id(thread_id: str) -> str:
    if not isinstance(thread_id, str) or not THREAD_ID_PATTERN.fullmatch(thread_id):
        raise ValueError(f"Invalid thread_id: {thread_id!r}")
    return thread_id


def rehydrate_and_resume(event, context):
    """
    由人工 UI 触发（通过身份验证的 API）。
    安全性：
      - 验证输入
      - 授权审批人
      - 防止令牌重放
      - 使用加密状态
    """
    try:
        task_token = event["task_token"]
        human_input = event["human_decision"]
        thread_id = _validate_thread_id(event["thread_id"])
        approver_id = event["approver_id"]  
    except KeyError as e:
        return {"statusCode": 400, "body": f"Missing field: {e}"}
    except ValueError as e:
        return {"statusCode": 400, "body": str(e)}

    
    if not authz.can_approve(approver_id, thread_id):
        logger.warning(
            "Unauthorized approval attempt | approver=%s thread=%s",
            approver_id,
            thread_id,
        )
        return {"statusCode": 403, "body": "Not authorized"}

    
    if not token_store.matches(thread_id, task_token):
        return {"statusCode": 409, "body": "Stale or invalid task token"}

    bucket = os.environ["AI_STATE_BUCKET"]
    key = f"checkpoints/{thread_id}/state.json"

    try:
        
        obj = s3_client.get_object(Bucket=bucket, Key=key)
        frozen_state = json.loads(obj["Body"].read())

        
        frozen_state.setdefault("messages", []).append(
            {"role": "human", "content": human_input}
        )
        frozen_state["status"] = "RESUMED"
        frozen_state["approved_by"] = approver_id

        token_store.invalidate(thread_id, task_token)

        sfn_client.send_task_success(
            taskToken=task_token,
            output=json.dumps(frozen_state, default=str),
        )

    except Exception as e:
        logger.exception("Rehydration failed | thread=%s err=%s", thread_id, e)
        return {"statusCode": 500, "body": "Rehydration failed"}

    return {"statusCode": 200, "body": "AI rehydrated and processing"}

```

*   LangGraph 命中“需要人工”节点。
*   Worker 将 JSON 保存到 S3，并将 task\_token 发送到控制面板。
*   Step Functions 冻结工作流。
*   人工审阅并提交答案。
*   API 发回令牌；Step Functions 将 S3 数据再水合到新的 Worker 中。
*   AI 将人工的回答作为其“记忆”的一部分恢复运行。

## 第 3 层：审计与可观测性

目标：将 AI 的“黑盒”转变为透明的业务指标。

*   我建议使用 Arize Phoenix，因为它充当“模型裁判”。在实践中，它通过使用一个 LLM 来评估另一个 LLM 的性能来实现这一点。它会寻找“幻觉分数”，或者 AI 开始凭空捏造的证据。一旦发生这种情况，Phoenix 就会在用户看到它 *之前* 标记出来。
*   LangSmith 帮助连接各个环节。它允许 IT 部门说：*“这一特定响应耗时 4 秒，成本 0.05 美元，并由人工代理 X 批准。”* 这是 SOC2 和 GDPR 合规性所需的审计追踪。

虽然标准的 LangGraph 检查点保存状态是为了 *恢复*，但审计就绪的检查点会在每一个“超步”将该状态连同丰富的元数据（谁、何时、为什么）一起镜像到 S3 或 RDS。

```python

from typing import Annotated, TypedDict, List
from operator import add

class AuditEntry(TypedDict):
    node: str
    thought: str
    timestamp: str
    metadata: dict

class AgentState(TypedDict):
    # 'add' 确保我们追加到历史记录而不是覆盖
    messages: Annotated[List[dict], add]
    audit_log: Annotated[List[AuditEntry], add]
    internal_monologue: List[str] # 当前思维过程
    status: str

```

## 带有审计节点的 LangGraph 实现

添加专门的“观察者”模式，其中节点在执行前后报告其“想法”：

```python

import datetime
from langgraph.graph import StateGraph, START, END

def reasoning_node(state: AgentState):
    # 逻辑：AI 在行动前先“思考”
    thought = "在批准 CEO 的请求之前，我需要检查库存水平。"
    
    # 审计日志条目
    audit = {
        "node": "reasoning_node",
        "thought": thought,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "metadata": {"model": "claude-3-5-sonnet", "tokens": 450}
    }
    
    # 执行实际逻辑...
    result = "正在搜索数据库..."
    
    return {
        "internal_monologue": [thought],
        "audit_log": [audit],
        "messages": [{"role": "assistant", "content": result}]
    }

# “审计钩子”节点
def audit_persistence_node(state: AgentState):
    """
    此节点充当长期存储的网关。
    它将当前的审计追踪“脱水”到 S3。
    """
    latest_audit = state["audit_log"][-1]
    # 在实践中，在此处调用你的 S3/RDS 逻辑
    # s3.upload_json(latest_audit, key=f"audits/{trace_id}/{step}.json")
    print(f"[AUDIT LOGGED]: Node {latest_audit['node']} completed.")
    return state

```

LangSmith 原生集成在 LangChain 中。我建议使用自定义注释来标记思维链，使其可搜索。

```python

from langsmith import traceable
from langchain_openai import ChatOpenAI
from config import settings  # 你的集中式配置


@traceable(
    run_type="chain",
    name="Inventory_Reasoning_Step",
    metadata={
        "department": "logistics",
        "priority": "high"
    }
)
def reasoning_node(state):
    """
    生产级安全推理节点：
    - 无环境变更
    - 无思维链泄露
    - 取而代之的是结构化的推理上下文
    """
    reasoning_context = {
        "intent": "inventory_analysis",
        "data_source": "s3+rds",
        "request_origin": "ceo_query"
    }

    data = state.get("data", "")
    if not isinstance(data, str):
        data = str(data)

    safe_data = data[:5000]  # 防止过多的 token 使用

    llm = ChatOpenAI(model="gpt-4o")

    response = llm.invoke(
        f"Analyze the following structured data:\n{safe_data}"
    )

    return {
        "messages": [response],
        "reasoning_context": reasoning_context
    }

```

Arize Phoenix 充当你的自动化合规官。它追踪并运行“判定”以查看 AI 是否产生了幻觉。

```python

import phoenix as px
from phoenix.otel import register
from openinference.instrumentation.langchain import LangChainInstrumentor

# 1. 启动 Phoenix (本地或云端)
session = px.launch_app()

# 2. 注册 OTel 追踪器 (这是你的 OTel 中枢)
tracer_provider = register(
    project_name="AI-Native-Enterprise",
    endpoint="http://localhost:6006/v1/traces" # 你的 Phoenix 收集器
)

# 3. 仪表化 LangChain/LangGraph
# 现在每个节点的执行都会自动流向 Phoenix
LangChainInstrumentor().instrument(tracer_provider=tracer_provider)

# 4. 示例：LLM 即评审员 (幻觉检测)
from phoenix.evals import HallucinationEvaluator, OpenAIModel, run_evals

# 我们按计划或在 HITL 再水合事件后运行此程序
evaluator = HallucinationEvaluator(model=OpenAIModel(model="gpt-4o"))
results = run_evals(
    dataframe=px.active_session().get_spans_dataframe(),
    evaluators=[evaluator],
    provide_explanation=True
)

```

### 组织影响

实施过程将劳动力从任务执行者转变为 AI 原生系统的管理者。

*   **数据科学** 构建“大脑”（模型）。
*   **工程** 构建“神经系统”。
*   **业务部门** 管理“异常”（HITL）。

其结果是一个 95% 的任务以 AI 速度运行，同时在涉及高风险的 5% 任务中保持 100% 合规且经过人工验证的组织。