
<!--
title: 自我感知AI：构建自适应LLM决策代理
cover: https://cdn.thenewstack.io/media/2025/05/d6ced13c-agents-1024x576.jpg
summary: 人工智能不再仅仅是处理数字或完成任务。我们正在步入智能体AI时代，系统不仅会按照指示行事，还会独立思考、学习和适应。
-->

人工智能不再仅仅是处理数字或完成任务。我们正在步入[智能体AI](https://thenewstack.io/agentic-ai-the-next-frontier-of-ai-power/)时代，系统不仅会按照指示行事，还会独立思考、学习和适应。

> 译自：[Self-Aware AI: Building Adaptive LLM Decision Agents](https://thenewstack.io/self-aware-ai-building-adaptive-llm-decision-agents/)
> 
> 作者：Oladimeji Sowole

这些人工智能无需持续的人工输入，就可以反思自己的行为，找出哪些有效（哪些无效），并随着时间的推移不断改进。诸如[GPT-4](https://thenewstack.io/openais-gpt-4-can-analyze-visual-images-pass-bar-exam/)和[Claude](https://claude.ai)之类的工具已经扩展了我们对它们能力的认知——无论是回答棘手的问题还是编写可靠的代码——但真正的变革在于创建能够实时成长和适应的人工智能系统。

让我们来探讨如何构建自我反思的[AI智能体](https://thenewstack.io/the-architects-guide-to-understanding-agentic-ai/)，这些智能体可以观察自己的行为，调整自己的策略，并使用[LangGraph](https://www.langchain.com/langgraph)、[OpenAI](https://openai.com)和反馈循环来构建更智能、更具适应性的系统，从而全面提升自己。

## 什么是涌现式智能体AI系统？

涌现式[智能体AI系统](https://thenewstack.io/building-autonomous-systems-in-python-with-agentic-workflows/)正在改变人工智能领域的游戏规则。它们的构建目标是自主、适应性强，并且能够在没有人为持续干预的情况下学习和改进。与传统人工智能受限于单一用途任务不同，这些系统依靠独立性和进化来处理复杂、不可预测的挑战。

以下是它们的工作方式：

*   **自主性**：这些AI系统可以自行做出决策，使用其内部逻辑来确定下一步的最佳步骤，而无需持续的指导。
*   **记忆**：它们会记住过去的行动、结果和经验。这种记忆有助于它们根据随着时间的推移所学到的知识做出更明智的决策。
*   **反思**：它们会分析自己的表现，从而在每个任务中变得更好、更有效率。
*   **适应**：当事情发生变化或它们犯错时，它们会从中学习。它们会进行调整和改进，以便下次表现得更好。

这种先进的设计使涌现式智能体AI系统能够摆脱重复的、特定于任务的编程，而是像人类一样通过内省来学习和成长。通过结合这些原则，它们正在为智能和自给自足的AI智能体铺平道路，这些智能体可以在不可预测的环境中蓬勃发展。

## 用例：自我改进的研究助理

假设一个[研究助理智能体](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/)的任务是编写一份关于某个主题的简短报告。其过程是检索信息，对其进行总结，评估其总结的质量并对其进行改进，直到达到质量阈值，所有这些都是自主完成的。

**系统概述**

1. **用户输入**：初始查询（“撰写一份关于聚变能的报告”）。
2. **智能体循环**：
    *   **计划**：定义子目标。
    *   **执行**：执行子目标（检索、总结）。
    *   **反思**：批判性地评价输出。
    *   **修改**：如果需要，重新尝试。
3. **记忆模块**：存储输出和自我评估。
4. **终止条件**：当反思认为输出足够时停止。

## 构建智能体

**步骤1：安装依赖项**

```
pip install langchain langgraph openai llama-index tiktoken
```

**步骤2：定义智能体核心组件**

```python
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.prompts import PromptTemplate
from llama_index import VectorStoreIndex, SimpleDirectoryReader

llm = ChatOpenAI(model="gpt-4", temperature=0)
```

**步骤3：加载知识库以进行上下文RAG（检索增强生成）**

```python
documents = SimpleDirectoryReader("./knowledge_base").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

def retrieve_info(topic):
    return query_engine.query(topic).response
```

**步骤4：定义计划函数**

```python
def plan_objectives(task):
    response = llm.predict(f"Break down the task '{task}' into 2-4 sub-objectives.")
    return response.split("\n")
```

**步骤5：定义执行函数**

```python
def execute_objective(objective):
    context = retrieve_info(objective)
    prompt = f"Using this context: {context}, write a paragraph about: {objective}"
    return llm.predict(prompt)
```

**步骤6：反思智能体**

```python
def reflect(output_text):
    prompt = f"Evaluate the quality of the following response. Be critical but constructive:\n\n{output_text}\n\nIs it accurate, clear, and complete? Suggest improvements if needed."
    return llm.predict(prompt)
```

**步骤7：自适应循环控制器**

```python
def self_improve(task):
    objectives = plan_objectives(task)
    report = ""
    for obj in objectives:
        result = execute_objective(obj)
        feedback = reflect(result)
        if "needs improvement" in feedback.lower() or "rewrite" in feedback.lower():
            print(f"Retrying: {obj}")
            result = execute_objective(obj)
        report += f"\n\n### {obj}\n{result}"
    return report

query = "Write a 2-paragraph overview on fusion energy."
final_report = self_improve(query)
print("Generated Report:\n", final_report)
```

**第 8 步：运行完整的 Agent 循环**

```py
query = "Write a 2-paragraph overview on fusion energy."
final_report = self_improve(query)
print("Generated Report:\n", final_report)
```

**此 Agentic 系统的主要特性**

- **涌现式规划**： LLM 动态分解任务。
- **基于 RAG 的推理**： 从知识库中提取上下文。
- **自我批判**： 反思循环迭代地改进内容。
- **适应性**： Agent 根据反馈重试子任务。
- **低代码/无代码定制**： 轻松修改任务结构和行为。

**高级附加组件**

1. **多 Agent 协作**： 在 Agent 之间分配职责（研究员、作者、编辑）。
2. **LangGraph 流程控制**： 使用 LangGraph 创建具有条件分支的基于节点的任务流程。
3. **工具增强操作**： 添加搜索 API、计算器或数据解析器等工具。
4. **人机协作 (HITL)**： 仅当 LLM 置信度下降时才提醒人工。
5. **元反思**： 添加一个最终 Agent，审查完整报告的连贯性和语气。

## 为什么这很重要

自我反思的 [agentic AI 系统正在赋能 LLM（大型语言模型）驱动的下一代演进](https://thenewstack.io/agentic-ai-is-the-next-frontier-in-enterprise-operations/) 工具。这些 Agent 不再是被动的引擎，而是表现出涌现智能的迹象，模仿人类般的执行和改进周期。对于全球组织，这些 Agent 可用于：

- 研究和总结
- 客户支持分流
- 法律或合规文档审查
- 个性化辅导系统

它们减轻了提示工程的负担，并为可扩展、可靠和可解释的 AI 应用程序创造了机会。

## 结论

随着 LangGraph 和 LlamaIndex 等工具的不断发展和完善，构建这些高级 Agent 比以往任何时候都容易。从小处着手，给你的 Agent 留出反思的空间，然后见证奇迹的发生。

Agentic AI 系统正在重塑行业并推动创新。了解 agentic AI 工作流程如何在 Andela 的指南中改变您的业务，[使用 Agentic 工作流程在 Python 中构建自主系统。](https://www.andela.com/blog-posts/building-autonomous-systems-in-python-with-agentic-workflows/?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack&utm_content=agentic-ai&utm_term=writers-room)