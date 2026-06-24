最近，我们的一家企业客户使用的关键 RAG 流水线开始对财务数据产生幻觉，但并没有通知我们任何错误或故障。我们的监控面板显示系统运行状况良好（绿色）；所有测试均顺利通过。然而，该系统自信地向用户建议投资某些股票，理由是其收益将大幅增长。遗憾的是，那份报告完全是虚构的。

我们花了极其痛苦的三天时间才查明问题所在：提示词模板的一个微小改动导致大语言模型完全忽略了上下文，仅依赖其预训练权重进行输出。

这次经历揭示了现代 AI 系统对传统调试方法的兼容性有多么糟糕。

如果你在处理传统软件时遇到任何问题，你会确切地知道代码哪里出了错：你会看到行号、错误消息、堆栈跟踪，甚至可能是一个 *NullReferenceException*。

> “你无法通过 console.logging 摆脱概率性错误，也没有断点来调试神经网络的内部状态。”

如果你在使用 AI 驱动的解决方案时遇到问题，你不会在那里找到任何 bug，系统依然运行得完美无缺。相反，它会产生彻底的捏造，跳过推理的关键部分，提取无关的来源，并基于虚假信息构建出完美的论点。你无法通过 *console.logging* 摆脱概率性错误，也没有断点来调试神经网络的内部状态。

为了在生成式 AI 时代生存，我们需要一种新的调试概念。

## 范式转换：确定性 bug vs. 概率性 bug

要理解为什么我们当前的工具失败了，我们必须首先了解 bug 的本质发生了怎样的变化。

| 特性 | 传统调试 | Gen AI 调试 |
| --- | --- | --- |
| 故障模式 | 二进制（通过/失败，崩溃，异常） | 错误的梯度（幻觉、漂移、遗漏） |
| 根本原因 | 逻辑缺陷、语法错误、状态错误 | 检索效果差、提示词歧义、模型漂移 |
| 可重现性 | 高（给定精确输入，输出一致） | 低（相同输入可能产生不同输出） |
| 主要工具 | 断点、堆栈跟踪、单元测试 | 执行跟踪、评估、负载日志记录 |

> “在传统软件中，bug 是指令中的缺陷。在生成式 AI 中，bug 是你提供给模型的上下文环境中的缺陷。”

在传统软件中，bug 是指令中的缺陷。在生成式 AI 中，bug 是你提供给模型的上下文环境中的缺陷。如果你把大语言模型的故障当作逻辑 bug 来处理，当你重写外层代码时就会浪费数小时，而真正的问题其实是向量数据库中切片处理不当的 PDF。

## 生成式 AI 系统调试与监控的现代方法

那些能够通过生产验证的系统，不会将 AI 系统视为某种神奇的函数调用，而是将其视为一个受 I/O 限制的外部子系统，并接受其所有的随机性和不可预测性。让我们看看现代工程师是如何解决概率性代码调试挑战的。

### 停止单步执行，转向异步处理

在[多步智能体工作流](https://thenewstack.io/groundcover-ai-observability-agents/)（例如：查询 → 检索 → 工具调用 → 合成）期间，合成阶段发生的任何故障，很可能都是因为三步之前的检索错误导致的。

单步执行代码在这里无济于事；相反，你应该创建跟踪图（trace graphs）。所有的交互都需要捕获完整的载荷（payload）。由于大语言模型调用受网络限制且需要几秒钟才能解析，因此你的跟踪必须异步进行，以避免阻塞你的事件循环。

下面是一个示例，展示了如何将你的系统包装到现代异步跟踪中，而不会破坏 FastAPI 应用程序，同时向 `stdout` 输出结构良好的 JSON，以便 Datadog、CloudWatch 或 OpenTelemetry 进行后续消费。

```python
import time
import json
import logging
from string import Template 
from typing import Callable, Dict, Any, List

# 为生产环境注入配置结构化日志
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def trace_llm_execution(
    step_name: str, 
    async_llm_callable: Callable, 
    prompt_template: str, 
    context: List[str], 
    user_query: str
) -> Dict[str, Any]:
    
# 1. 使用 string.Template 进行更安全的填充，避免用户输入包含 '{}' 时出现 KeyError
template = Template(prompt_template)
hydrated_prompt = template.safe_substitute(
context="\n".join(context),
query=user_query
) 
    
    start_time = time.perf_counter()
    error = None
    raw_response = None
    
    try:
        # 2. 等待概率性调用以保持线程不被阻塞
        raw_response = await async_llm_callable(hydrated_prompt)
    except Exception as e:
        error = str(e)
        
    latency_ms = round((time.perf_counter() - start_time) * 1000, 2)
    
    # 3. 创建精确状态的不可变工件
    trace_artifact = {
        "event": "llm_trace",
        "step": step_name,
        "latency_ms": latency_ms,
        "hydrated_prompt": hydrated_prompt, # 关键：模型实际上看到了什么？
        "raw_context_chunks": context,      # 关键：数据库返回了垃圾信息吗？
        "raw_response": raw_response,
        "error": error
    }
    
    # 4. 输出到 stdout 以供可观测性平台使用
    logger.info(json.dumps(trace_artifact))
        
    if error:
        raise RuntimeError(f"Step {step_name} failed: {error}")
        
    return raw_response
```

通过将结构化跟踪转储到标准输出，你可以让你的可观测性栈索引精确的 `hydrated_prompt`。如果输出错误，你不需要猜测；你可以查询你的日志。90% 的情况下，bug 就在那里：模型被喂入了[错误的上下文](https://thenewstack.io/context-rot-enterprise-ai-llms/)。

### 区分“上下文 bug”与“推理 bug”

一旦 AI 流水线开始产生幻觉，开发人员就会急于修改提示词。这是一种懒惰的方法。你需要首先确定问题来自哪里：

**上下文 bug**：向量数据库返回了不相关的切片。答案错误是因为模型缺乏适当的上下文（解决方案：调整你的嵌入和切片大小，使用混合 BM25 检索）。

**推理 bug**：向量数据库返回了最相关的切片，但模型要么没有正确使用它们，要么误解了它们，或者是遭受了格式漂移（解决方案：升级模型，降低温度参数，使用少样本提示）。

对大语言模型大喊大叫要求其遵守系统提示词（“你必须只使用上下文！！！”）并试图以此修复推理 bug 是永远不会奏效的。

### 使用 Pydantic 进行现代数据类型模式验证

你的企业系统离不开验证。仅仅依靠手动正则表达式和 `json.loads()` 是行不通的。概率性输出需要符合某种模式。对于 Python 而言，Pydantic 优雅地解决了这个问题。

（代码示例省略，同上文逻辑）

### 通过“LLM-as-a-Judge”实现自动化评估

由于生成式 AI 不支持输出的字符串相等断言测试，单元测试需要转变其方法。

在过去，你制作的是脆弱的断言，而现在，你需要依赖一个轻量级且廉价的模型（GPT-4o-mini、Gemini 1.5 Flash 或 Claude 3 Haiku），让它根据严格的标准来判断主模型的输出。

评估提示词的一个例子是将答案和来源传递给判别模型，并要求：“仅根据是否提到了以下上下文，以 1-5 分的等级对该答案进行评分。”这样，你就可以在你的 [CI/CD 流程](https://thenewstack.io/introduction-to-ci-cd/)中持续监控幻觉率。

## 工程是驾驭混乱的艺术

虽然早期一代的 AI 工具几乎是神奇的，因为我们在纸上对它们进行了实验，但企业软件并不遵循魔法原则；它遵循可观测性、可预测性和清晰边界的原则。

> “虽然早期一代的 AI 工具几乎是神奇的，但企业软件并不遵循魔法原则；它遵循可观测性、可预测性和清晰边界的原则。”

目前调试代码的挑战不在于代码变得更复杂或更难理解，而在于代码运行的环境变得不可预测。通过将注意力从断点转向创建异步跟踪、使用 Pydantic 严格验证模式以及自动运行评估器，我们可以揭开 AI 的神秘面纱，并将其回归到软件工程中。