
<!--
title: AutoGen AI 智能体框架开发者指南
cover: https://cdn.thenewstack.io/media/2024/12/5192e547-developers-guide-to-autogen-2.jpg
-->

AutoGen在Python开发者中很受欢迎，因为它可以用来构建多智能体AI系统。以下是入门方法。

> 译自 [A Developer's Guide to the AutoGen AI Agent Framework](https://thenewstack.io/a-developers-guide-to-the-autogen-ai-agent-framework/)，作者 Janakiram MSV。

[AutoGen](https://microsoft.github.io/autogen/0.2/) 是 Python 开发者中流行的框架，用于通过复杂的、对话驱动的协作和人机交互功能构建多智能体 AI 系统。由[Microsoft Research](https://news.microsoft.com/?utm_content=inline+mention)开发的开源 AutoGen 以其灵活的代理架构、高级对话管理和安全代码执行功能而脱颖而出。该框架使开发人员能够创建复杂的多个代理系统，其中代理可以参与动态对话，在安全环境中执行代码，并将人工反馈无缝集成到其工作流程中。

类似于我[介绍 CrewAI 的方式](https://yylives.cc/2024/12/23/developer-guide-to-the-crewai-agent-framework-for-python-2/)，我将使用我在之前的文章中定义的[AI 代理结构](https://yylives.cc/2024/10/22/ai-agents-a-comprehensive-introduction-for-developers/)。

![](https://cdn.thenewstack.io/media/2024/12/91d73a9e-agents-1-1-1024x681-1.png)

## AutoGen 和 AI 代理的结构

AutoGen 通过其复杂的架构实现了 AI 代理结构的关键组件，从而能够创建多功能且强大的多智能体系统。让我们探讨 AutoGen 如何结合每个基本要素：

### 角色

AutoGen 允许开发人员通过其灵活的代理配置系统创建不同的代理角色。每个代理都可以定义特定的角色、能力和个性特征，这些特征会影响其行为和决策过程。例如：

```python
coding_agent = AssistantAgent(
    name="Python Developer",
    system_message="Expert Python developer with focus on code quality and optimization",
    llm_config={"temperature": 0.7}
)
 
reviewer_agent = AssistantAgent(
    name="Code Reviewer",
    system_message="Senior developer specialized in code review and best practices",
    llm_config={"temperature": 0.2}
)
```

请注意`system_message`如何用于定义代理的角色。这些角色为多智能体系统中的专业行为和专业知识奠定了基础。

### 指令

AutoGen 通过其复杂的报文传递系统实现指令处理。代理可以接收、解释和执行复杂的指令，同时在整个对话流程中保持上下文：

```python
user_proxy = UserProxyAgent(
    name="User_Proxy",
    system_message="A proxy for human user, providing project requirements and feedback.",
    human_input_mode="TERMINATE",
    code_execution_config={"work_dir": "coding_project"}
)
 
coding_agent = AssistantAgent(
    name="Coding_Assistant",
    system_message="You are a helpful AI assistant specialized in writing Python scripts with robust error handling.",
    llm_config={"config_list": [{"model": "gpt-4o"}]}
)
 
# Initiate the chat with the task
user_proxy.initiate_chat(
    recipient=coding_agent, 
    message="Develop a Python script for processing CSV files with error handling"
)
```

### 任务

AutoGen 中的任务通过其对话驱动的架构进行管理。代理可以通过多轮对话和嵌套工作流程来处理复杂的任务。

```python
async def development_workflow():
    # Initial code development
    code_response = await coding_agent.generate_response(task_message)
    # Code review phase
    review_response = await reviewer_agent.review_code(code_response)
    # Iterative improvement based on review
    if review_response.has_feedback:
        improved_code = await coding_agent.update_code(review_response.feedback)
```

AutoGen 的任务管理系统支持同步和异步执行模式。

### 规划

AutoGen 通过多种方法实现复杂的规划能力：[ReAct](https://microsoft.github.io/autogen/0.2/docs/topics/prompting-and-reasoning/react)（推理和行动）模式和[基于反思的](https://microsoft.github.io/autogen/0.2/docs/topics/prompting-and-reasoning/reflection)决策。开发人员可以选择与用例一致的特定提示工程技术，并将其与代理一起使用。

下面的代码片段演示了 AutoGen 代理如何使用 ReAct 提示来解决问题。

```python
#  (Example code for ReAct would go here)
```

```python
ReAct_prompt = """
Answer the following questions as best you can. You have access to tools provided.
 
Use the following format:
 
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take
Action Input: the input to the action
Observation: the result of the action
... (this process can repeat multiple times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question
 
Begin!
Question: {input}
"""
 
# Define the ReAct prompt message. Assuming a "question" field is present in the context
 
 
def react_prompt_message(sender, recipient, context):
    return ReAct_prompt.format(input=context["question"])
 
 user_proxy.initiate_chat(
        assistant,
        message=react_prompt_message,
        question="What is the result of super bowl 2024?",
    )
```

**缓存和内存**

AutoGen 提供强大的缓存和内存功能，可增强代理性能和上下文感知能力。该框架支持多种内存类型，包括短期内存、长期内存、语义内存和情景记忆，使代理能够保持上下文并从之前的交互中学习。其缓存机制允许重用 API 请求，从而提高可重复性和降低计算成本。

AutoGen 通过与 [Zep](https://www.getzep.com) 和 [Mem0](https://www.mem0.ai/) 等高级内存管理平台的无缝集成，提供灵活的长期内存支持。通过利用这些外部内存系统，AutoGen 代理可以维护持久上下文，检索相关的历史信息，并增强长期推理能力。

Zep 的时间知识图谱和 Mem0 的混合数据库方法可以直接插入 AutoGen 的代理架构中，从而实现超越传统上下文窗口限制的复杂内存管理。这种方法使开发人员能够创建更具上下文感知能力和自适应能力的 AI 代理，以便在复杂的交互场景中学习、记忆和推理。

以下代码片段演示了 Mem0 如何与 AutoGen 集成：

```python
memory = MemoryClient(api_key="mem0_key")  # Initialize Mem0 memory client
memory.add(messages=[{"role": "user", "content": "Query about TV issue"}], user_id="case_123")  # Store memory
memories = memory.search("TV issue", user_id="case_123")  # Retrieve relevant memories
agent.generate_reply(messages=[{"content": f"Context: {memories}", "role": "user"}])  # Use in agent response
```

### 工具

AutoGen 提供强大的[工具集成](https://microsoft.github.io/autogen/0.2/docs/tutorial/tool-use)功能，使代理能够与外部工具、API 和自定义函数无缝交互。开发人员可以直接将[Python 函数](https://thenewstack.io/how-to-define-and-use-your-own-functions-in-python/)、命令行工具或外部 API 注册到代理的配置中，从而允许在对话期间动态调用工具。该框架支持自动工具选择、参数推断和结果解释，使复杂的多步骤任务更易于管理。

```python
def calculator(operation, x, y):
    if operation == 'add':
        return x + y
    if operation == 'subtract':
        return x - y
    if operation == 'multiply':
        return x * y

assistant = AssistantAgent(
    name="Math_Assistant",
    llm_config={
        "config_list": [{"model": "gpt-4"}],
        "tools": [
            {"function": calculator, "name": "math_operations"}
        ]
    }
)
```

此示例演示了开发人员如何轻松地将自定义函数集成到工具中，使代理能够在各种领域中以最小的配置开销动态执行复杂任务。

### 委托

AutoGen 的委托机制通过智能任务路由和动态角色分配，实现了复杂的多代理协作。代理可以根据专业知识、当前上下文和任务复杂性，自主地将任务委托给最合适的团队成员。该框架支持显式和隐式委托策略，允许代理移交子任务、请求专业知识或协作解决复杂问题。委托通过智能路由机制进行，该机制评估代理能力、系统消息和之前的交互历史。

```python
coding_agent = AssistantAgent(
    name="Python_Developer",
    system_message="Expert in writing Python code with strong algorithmic skills",
    llm_config={"config_list": [{"model": "gpt-4"}]}
)
reviewer_agent = AssistantAgent(
    name="Code_Reviewer",
    system_message="Specialized in code quality assessment and optimization",
    llm_config={"config_list": [{"model": "gpt-4"}]}
)
group_chat = GroupChat(
    agents=[coding_agent, reviewer_agent],
    messages=[],
    max_round=5,
    speaker_selection_method="auto"
)
manager = GroupChatManager(groupchat=group_chat)
```

以上代码片段说明了 AutoGen 的委托框架，其中代理可以根据其专业角色和系统消息动态交互、委托任务和协作。

## AutoGen框架的独特特性

**对话驱动架构**

AutoGen的核心在于其复杂的对话驱动架构，该架构能够实现代理之间自然而动态的交互。该框架支持多轮对话并持久保留上下文，允许代理保持连贯的讨论并在之前的交互基础上进行构建。代理可以根据对话上下文和代理能力动态路由消息并选择合适的响应者。

**人机协同集成**

AutoGen提供了复杂的人机协同功能，能够将人工监督和反馈无缝集成到AI工作流程中。该框架提供多种交互模式（TERMINATE、NEVER、VERIFY）和可配置的干预点，允许开发者设计具有适当人工监督级别的系统。

**基于Docker的代码执行**

AutoGen提供了一个复杂的基于[Docker](https://www.docker.com/?utm_content=inline+mention)的[代码执行](https://microsoft.github.io/autogen/0.2/docs/tutorial/code-executors)环境，它结合了安全、灵活性和强大的执行能力。此系统允许代理在隔离的容器中安全地执行代码，同时保持对运行时环境的完全控制。

**复杂的对话结构**

AutoGen通过其GroupChat和嵌套对话功能支持复杂的[对话模式](https://microsoft.github.io/autogen/0.2/docs/tutorial/conversation-patterns)。该框架支持具有动态发言者选择和分层对话管理的复杂多代理交互。

## 结论

AutoGen代表了AI代理解剖学的复杂实现，它通过高级功能扩展了传统概念，使其适用于现实世界的应用。其对话驱动架构、人机协同功能和安全的代码执行环境使其成为构建复杂多代理系统的强大框架。

通过提供强大的代理交互、任务管理和工作流编排工具，AutoGen使开发人员能够创建智能、适应性和安全的AI应用程序。
