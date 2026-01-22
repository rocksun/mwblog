代理AI已从玩具演示转向真实产品的前沿：自主研究助理、合规副驾驶、监控仪表盘和提交工单的运维机器人，以及与企业数据连接的[检索增强生成（RAG）](https://thenewstack.io/how-to-build-rag-applications-using-model-context-protocol/)副驾驶。

问题不是“我们能否让代理做一次巧妙的事情？”，而是“我们能否让代理每次都可靠、可观测、成本可控且安全？”

实现这一点需要一种全面、以生产为中心的方式来构建、保护和扩展[代理AI系统](https://thenewstack.io/ai-agents-vs-agentic-ai-a-kubernetes-developers-guide/)。

本教程将引导您了解将代理系统投入生产的实用蓝图。它实现了一个最小的、面向生产的技术栈，包括：

* 使用LangChain/LangGraph风格的循环进行推理和编排。
* RAG向量搜索和重新排名。
* 护栏，如模式验证和允许/拒绝。
* 成本和遥测，包括令牌计量和跟踪。
* 异步执行和超时，以防止不稳定的工具导致运行停滞。
* 一个API接口（FastAPI），您可以对其进行容器化并部署到任何地方。

该项目涵盖了从推理循环和RAG到护栏、遥测和成本控制的生产工作流，从而实现在真实环境中可靠、可观测且经济高效地部署自主AI工作流。

## 架构一览

1. API层 (FastAPI)：接收任务。
2. 代理循环：使用结构化工具进行推理-行动-观察。
3. RAG：嵌入 → 检索 → 重新排名 → 合成。
4. 护栏：Pydantic 模式，内容过滤器。
5. 成本和遥测：使用日志；OpenTelemetry 的钩子。
6. 异步工具：超时/重试。
7. 缓存（可选）：语义缓存以降低成本/延迟。

## 步骤0：安装必需品

*生产提示：* 可以将[FAISS库](https://github.com/facebookresearch/faiss)替换为Pinecone/Qdrant，并添加`opentelemetry-exporter-otlp`以实现完整跟踪。

## 步骤1：定义健壮的工具接口

工具应该是具有清晰输入/输出的纯函数（或异步函数）。添加超时和重试以防止代理挂起。

*为什么这很重要：* 它有助于隔离I/O，添加默认超时并提前截断以控制成本。

## 步骤2：使用FAISS设置RAG

以下步骤将一次性嵌入文档，然后在运行时检索top-k。添加简单的词汇重新排名以提高质量，而无需额外的模型调用。

*生产提示：* 在延迟预算允许的情况下，用学习型重新排名器（Cohere/Rerankers）替换词汇型。

## 步骤3：定义护栏（模式和内容过滤器）

确保代理的最终输出与模式匹配，并在将其返回给用户或下游系统之前通过基本的策略检查。

*为什么这很重要：* 模式验证捕获格式错误的输出；策略过滤器阻止明显的泄露。

## 步骤4：带成本计量的代理循环（推理 → 行动 → 观察）

以下实现了带有最大步骤预算、工具调用和令牌使用量核算的轻量级React风格循环。

*成本感知默认值：* 使用更便宜的模型（例如`gpt-4o-mini`）进行规划/工具使用，并将高级模型保留用于关键提示。如果您的软件开发工具包（SDK）提供`usage_metadata`，请跟踪它。否则，使用[tiktoken](https://github.com/openai/tiktoken)估算令牌。

## 步骤5：代理的FastAPI接口

使代理可以从前端、cron或其他服务调用。添加超时以防止请求挂起。

在本地运行：

```
uvicorn app:app --host 0.0.0.0 --port 8080
```

## 步骤6：添加简单的遥测和成本日志记录

从一个普通的日志文件开始；稍后接入OpenTelemetry/Prometheus。

在 `agent_run` / `app.py`中使用：

```
# ...after final answer
from telemetry import log_event
log_event("answer", tokens=obj.cost_tokens, sources=obj.sources)
```

*生产提示：* 导出跟踪（`opentelemetry-sdk`，OTLP），并按路由/用户/工作流仪表盘令牌成本。

## 步骤7：使其具有弹性：重试、回退、缓存

* 重试：使用指数退避包装工具调用。
* 回退：如果高级模型失败，降级到较小的模型并标记响应。
* 语义缓存：哈希查询和检索到的文档ID；如果最近出现过类似的查询-上下文对，则返回缓存的响应。

缓存骨架：

## 步骤8：发布前评估（代理评估）

为[保留数据集](https://towardsdatascience.com/when-training-a-model-you-will-need-training-validation-and-holdout-datasets-7566b2eaad80/)添加一个快速的、大型语言模型“LLM作为评委”的健全性检查。保持轻量级但可重复。

跟踪不同版本的分数；如果指标下降，则构建失败。

## 步骤9：生产注意事项：部署和扩展

* 使用小型基础镜像（例如`python:3.11-slim`）进行容器化，固定依赖项，并为Uvicorn设置`--workers`。
* Kubernetes:
  + CPU/RAM的请求/限制；基于CPU或自定义指标（请求/分钟）的水平Pod自动扩缩器。
  + 将配置作为 secrets/ConfigMaps 挂载（模型密钥、阈值）。
  + 用于[OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/)或[FluentBit](https://thenewstack.io/fluent-bit-core-concepts/)的Sidecar以发送日志。
* 成本控制：实施每个租户的预算，默认路由便宜的模型，开启缓存，限制最大令牌数，并提前截断输入。
* 安全性：实施内容过滤器（如上述的`policy_check`），对外发响应进行个人身份信息（PII）检测，并对关键操作进行人工干预。

## 为什么这个蓝图有效

* **关注点分离**：工具是独立的；代理循环对其进行编排。
* **确定性护栏**：模式和策略在输出逃逸之前对其进行把关。
* **从第一天起就具备可观测性**：现在采用基本遥测，稍后进行完整跟踪，无需重写。
* **成本感知默认值**：选择更便宜的模型进行规划、截断、缓存和计量，以防止费用失控。
* **可移植性**：FastAPI和容器使其与云无关。准备好扩展时添加Terraform/K8s。

## **总结思考**

让一个代理工作一次很容易。使其可预测、可观测且经济高效才是真正的工作。这种模式通过衡量工具使用、强制形态和安全的护栏、优先处理相关上下文的RAG以及可监控和扩展的API来实现这一点。

从这里您可以：

* 将FAISS替换为托管向量数据库；添加学习型重新排名。
* 连接OpenTelemetry并设置服务级别目标（p95延迟，答案正确性 > X）。
* 仅当单代理基线稳定时才添加多代理模式（规划器/执行器/评论者）。

现在构建缓慢变化的部分，以便细节稍后能够出彩。