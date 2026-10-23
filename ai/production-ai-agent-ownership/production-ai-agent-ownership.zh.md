凌晨 2:07，一个 AI 智能体开始出现故障。

应用程序仍在运行，但由于下游 API 返回错误，请求正在超时。该智能体已经重试了两次，消耗了比平时更多的 Token，其响应时间大约翻了一番。

第一个问题不应该是：

```

	“我们应该使用哪个模型？”

```

而应该是：

```

	“现在是谁在负责这个系统？”

```

在[构建 AI 智能体](https://thenewstack.io/how-to-build-ai-agents-with-lifelong-learning/)时，这个问题很容易被忽视。团队通常将大量精力投入到提示词、检索、工具和模型选择上，但生产环境的所有权决定了智能体究竟会成为一个可靠的服务，还是另一个运营风险的来源。

> “团队通常将大量精力投入到提示词、检索、工具和模型选择上，但生产环境的所有权决定了智能体究竟会成为一个可靠的服务，还是另一个运营风险的来源。”

一个生产级智能体需要拥有者、边界、遥测数据、故障策略、升级路径，以及对系统可自动执行与需要人工干预的内容的清晰区分。

![展示处理用户请求的智能体涉及的工作流循环的图表。](https://cdn.thenewstack.io/media/2026/10/c3d0706d-image-1024x406.png)

生产级智能体不应存在从推理到行动的直接路径。每个工具调用都应通过显式控制、保持可观测性，并具备明确的[人工介入路径](https://thenewstack.io/ai-sre-agent-autonomy-phases/)。

以下是构建这些控制措施的实用方法。

---

## 第一步：将智能体视为生产服务

智能体应该与任何其他生产服务具有相同的运维身份。

首先定义其所有权元数据。

```

Python
from pydantic import BaseModel


class AgentService(BaseModel):
    name: str
    owner_team: str
    service_tier: str
    escalation_channel: str


agent_service = AgentService(
    name="incident-command-agent",
    owner_team="platform-engineering",
    service_tier="critical",
    escalation_channel="#platform-oncall",
)

```

这看起来很简单，但它改变了对话的方式。

该智能体不再是运行在某个 Python 进程中的实验。它是一个拥有负责团队和升级路径的服务。

> “该智能体不再是运行在某个 Python 进程中的实验。它是一个拥有负责团队和升级路径的服务。”

随后，你可以将相同的元数据附加到日志、跟踪、仪表盘、警报和部署记录中。

---

## 第二步：定义智能体被允许做什么

所有权还意味着明确智能体被允许做什么。

一个只能读取遥测数据的智能体，其风险远低于一个可以重启生产服务、更改基础设施或部署代码的智能体。

这就是为什么我更喜欢显式的工具白名单，它将智能体限制在你刻意授予它的操作范围内。

```

Python
ALLOWED_TOOLS = {
    "get_service_health",
    "get_recent_deployments",
    "search_runbooks",
    "summarize_incident",
}


class ToolAuthorizationError(Exception):
    """当智能体尝试使用未批准的工具时引发。"""


def authorize_tool(tool_name: str) -> None:
    if tool_name not in ALLOWED_TOOLS:
        raise ToolAuthorizationError(
            f"Tool '{tool_name}' is not authorized."
        )

```

指导原则是**默认拒绝**。

添加新功能应该是一个刻意的工程决策，而不是因为某个工具对智能体变得可用而偶然发生的事情。

对于破坏性操作，授权应该更加严格。生产环境的重启或部署应该需要经过身份验证的人工批准，而不是智能体自身的判断。

---

## 第三步：为智能体执行设置预算

一个可以无限期推理的智能体很难进行运维。

每个生产工作流都应该围绕执行时间、模型调用、工具调用以及理想情况下的 Token 消耗设定限制。

```

Python
import os


class ExecutionBudget:
    def __init__(
        self,
        max_steps: int | None = None,
        max_tools: int | None = None,
    ):
        self.steps = 0
        self.tool_calls = 0

        self.max_steps = (
            max_steps
            if max_steps is not None
            else int(os.getenv("MAX_AGENT_STEPS", "5"))
        )

        self.max_tools = (
            max_tools
            if max_tools is not None
            else int(os.getenv("MAX_TOOL_CALLS", "8"))
        )

        if self.max_steps <= 0 or self.max_tools <= 0:
            raise ValueError(
                "Execution budget limits must be positive."
            )

    def check_step(self) -> None:
        if self.steps >= self.max_steps:
            raise RuntimeError(
                "Agent step budget exceeded."
            )

        self.steps += 1

    def check_tool_call(self) -> None:
        if self.tool_calls >= self.max_tools:
            raise RuntimeError(
                "Agent tool-call budget exceeded."
            )

        self.tool_calls += 1

```

执行限制应该是可配置的，而不是埋在应用代码中。通过在构造函数中传递这些限制，工程师可以在不改变全局设置的情况下，为不同的智能体分配不同的预算。诊断智能体可能只需要三个步骤，而更复杂的调研工作流可能需要相当多的步骤。当没有提供限制时，该类将退回到环境变量。重要的是，每个工作流都有一个确定的上限，并且在整个执行过程中强制执行相同的预算。

---

## 第四步：使模型调用具备可观测性

所有者无法运维他们看不见的东西。

至少要记录以下内容：

* 请求延迟；
* 使用的模型；
* 成功/失败；
* 工具调用；
* 可用的 Token 使用量；
* 关联或请求 ID；
* 升级事件。

一个简单的包装器提供了一个有用的边界。

```

Python
import logging
import time
import uuid

logger = logging.getLogger(__name__)


def invoke_model(model, messages):
    request_id = str(uuid.uuid4())
    started = time.perf_counter()

    # 跨不同的提供商库提取模型名称。
    model_name = (
        getattr(model, "model_name", None)
        or getattr(model, "model", None)
        or "unknown_model"
    )

    try:
        response = model.invoke(messages)

        elapsed = time.perf_counter() - started

        logger.info(
            "agent_model_call_success",
            extra={
                "request_id": request_id,
                "model": model_name,
                "latency_seconds": round(elapsed, 3),
            },
        )

        return response

    except Exception:
        elapsed = time.perf_counter() - started

        logger.exception(
            "agent_model_call_failed",
            extra={
                "request_id": request_id,
                "model": model_name,
                "latency_seconds": round(elapsed, 3),
            },
        )

        raise

```

当事故涉及多个服务时，请求 ID 会变得尤其有价值。

工程师应该能够从警报跳转到智能体请求，再跳转到底层的模型和工具调用。

在生产环境中，请用[分布式追踪和指标](https://thenewstack.io/agent-traces-application-data/)来补充这个日志记录层，以便更全面地了解系统行为和性能。

---

## 第五步：将失败与升级分离开来

模型调用失败并不一定意味着整个服务都应该失败。

同样，成功的模型调用并不意味着智能体的推荐应该自动执行。

这是不同的决策。

```

Python
def handle_agent_failure(error: Exception) -> dict:
    logger.error(
        "Agent execution failed; escalating to human.",
        exc_info=(
            type(error),
            error,
            error.__traceback__,
        ),
    )

    return {
        "status": "escalated",
        "message": (
            "The AI agent could not complete the operation. "
            "Human intervention is required."
        ),
        "error_type": type(error).__name__,
    }

```

这种区别在真实的事故中非常重要。

智能体可能会宕机，但工程团队仍然应该能够使用底层的工单和运维手册进行响应。这就是实践中的优雅降级。

---

## 第六步：将高风险操作交由人工把关

企业智能体中最有用的模式之一是将**推荐**与**执行**分离开来。

例如：

```

Telemetry
    ↓
AI Agent
    ↓
Diagnosis
    ↓
Recommended Action
    ↓
Risk Check
    ↓
Human Approval
    ↓
Production Change

```

智能体可能会推荐：

```

	“增加数据库连接池。”

```

但它不应该仅仅因为模型生成了该推荐，就将该更改推送到生产环境。

以下是一个简单的批准边界长什么样：

```

Python
def execute_action(
    action: str,
    approved_by: str | None,
) -> dict:
    if not approved_by:
        return {
            "status": "awaiting_approval",
            "action": action,
        }

    return {
        "status": "approved",
        "action": action,
        "approved_by": approved_by,
    }

```

真实系统需要更复杂的实现，但架构边界才是最重要的。

> “智能体可以拥有推理权，但无需拥有授权权。”

智能体可以拥有推理权，但无需拥有授权权。

---

## 第七步：为智能体提供健康检查

生产级智能体需要像任何其他服务一样拥有健康端点。

使用 FastAPI：

```

`Python
import os

import httpx
from fastapi import FastAPI, Response, status

app = FastAPI()

SERVICE_NAME = "incident-command-agent"


@app.get("/health/live")
async def liveness():
    """检查应用进程是否响应。"""
    return {
        "status": "alive",
        "service": SERVICE_NAME,
    }


async def check_provider() -> bool:
    """检查配置的提供商健康端点。"""
    health_url = os.getenv("MODEL_PROVIDER_HEALTH_URL")

    if not health_url:
        return False

    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            result = await client.get(health_url)
            return result.status_code == 200
    except httpx.RequestError:
        return False


@app.get("/health/ready")
async def readiness(response: Response):
    """检查所需的依赖项是否可用。"""
    if not await check_provider():
        response.status_code = (
            status.HTTP_503_SERVICE_UNAVAILABLE
        )
        return {
            "status": "unhealthy",
            "reason": "Model provider unavailable",
        }

    return {
        "status": "ready",
        "service": SERVICE_NAME,
    }

```

存活性（Liveness）和就绪性（Readiness）服务于不同的目的。存活性端点确认应用进程是有响应的，而就绪性则根据所需依赖项的可用性来检查服务是否可以处理请求。

在此示例中，就绪性端点检查配置的模型提供商健康 URL，并在检查失败时返回 HTTP 503。该检查刻意保持轻量级和限时，以避免引入不必要的延迟或成本。在生产环境中，团队应该根据其提供商支持的健康检查机制以及其他关键依赖项（例如向量数据库或配置服务）对其进行调整。

保持这些检查相互独立，可以让诸如 Kubernetes 之类的编排平台区分需要重启的应用和暂时无法提供流量的应用。

---

## 第八步：当安全控制失效时实行故障安全关闭

最糟糕的故障模式之一就是允许智能体在其安全机制宕掉后继续运行。

例如：

```

Python
def run_controlled_agent(
    tool_name: str,
    model,
    messages,
    budget: ExecutionBudget,
):
    try:
        authorize_tool(tool_name)

        # 在智能体步骤和工具调用之间复用预算。
        budget.check_step()
        budget.check_tool_call()

        return invoke_model(
            model,
            messages,
        )

    except ToolAuthorizationError:
        logger.exception(
            "Agent authorisation check failed."
        )

        return {
            "status": "blocked",
            "message": (
                "The requested operation is not authorised."
            ),
        }

    except RuntimeError:
        logger.exception(
            "Agent execution budget exceeded."
        )

        return {
            "status": "escalated",
            "message": (
                "The agent exceeded its execution budget. "
                "Human investigation is required."
            ),
        }

    except Exception as exc:
        return handle_agent_failure(exc)

```

请注意，不同的故障会产生不同的结果。授权失败应该阻止请求的操作，而耗尽的执行预算应该触发升级而不是再次重试。同时，临时的模型故障应该遵循系统定义的故障处理策略。

另一个重要细节是：执行预算必须在智能体的整个工作流中保持持久。为每次调用创建一个新预算将重置其计数器，从而允许重复调用绕过预期的限制。相反，应该创建一次预算并将其传递到后续的每次调用中，如下所示。

```

Python
# 为整个智能体工作流创建一个预算。
budget = ExecutionBudget(
    max_steps=5,
    max_tools=8,
)

# 在连续调用中复用相同的预算。
for tool_name in planned_tools:
    result = run_controlled_agent(
        tool_name=tool_name,
        model=model,
        messages=messages,
        budget=budget,
    )

    if isinstance(result, dict) and result.get(
        "status"
    ) in {"blocked", "escalated"}:
        break

```

通过在多次调用中共享相同的预算，每个计数的步骤和工具调用都会对工作流的总体限制做出贡献。一旦达到该限制，智能体就会停止，而不是带着新的预算继续运行。只有当这些控制在整个执行过程中保持有效时，它们才能发挥作用，特别是当智能体遇到连续故障时。

---

## 第九步：定义凌晨 2 点的运维手册

这就是运维所有权变得真实的地方。

假设智能体在凌晨 2 点开始出现故障。

值班工程师应该能够迅速回答五个问题：

1. **智能体本身是否健康？**
2. **模型提供商是否健康？**
3. **检索或工具依赖项是否发生故障？**
4. **智能体是否超出了其正常的成本或延迟范围？**
5. **如果我们禁用它会发生什么？**

最后一个问题最重要。

每个生产级 AI 系统都应该有清晰的降级路径。

对于一个事故响应智能体来说，这可能意味着：

```

AI Agent unavailable
        ↓
Incident still created
        ↓
Telemetry remains available
        ↓
Standard runbook activated
        ↓
Human engineer continues investigation

```

AI 系统应该加速运营，而不是成为组织离开它就无法运转的东西。

---

## 那么，谁拥有这个智能体？

答案绝不能简单地是：

生产环境的所有权必须是明确的。

总有人拥有：

* 部署；
* 基础设施；
* 模型配置；
* 工具权限；
* 监控；
* 事故响应；
* 成本；
* 安全；
* 回滚；
* 禁用智能体的决策。

这并不意味着一个人必须处理所有事情。这意味着每个人都足够清楚自己的角色，当事故发生时，团队不会浪费时间去弄清楚谁应该负责人。

---

## AI 智能体的真正考验

运营 AI 智能体最轻松的时候是在一切正常的工作时间内。

真正的考验在凌晨 2 点到来。

一个生产就绪的智能体应该拥有一个可以被呼叫的负责人、一个防止失控行为的执行预算、一个解释发生了什么的观测性、一个约束其行为的授权边界，以及一个允许工程师在没有它时继续运行的兜底方案。

我们的目标不是把人类排除在环路之外。

> “一个生产就绪的智能体应该拥有一个可以被呼叫的负责人、一个执行预算、一个解释发生了什么的观测性、一个授权边界，以及一个允许工程师在没有它时继续运行的兜底方案。”

而是要明确智能体的责任在哪里结束，人类在哪个环节需要介入。

因为当凌晨 2 点出现问题时，问题不在于模型是否足够聪明。

而在于系统的设计是否足够完善，以至于值班人员知道发生了什么、智能体做了什么以及接下来该做什麽。