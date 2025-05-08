<!--
title: MCP如何实现Agentic AI工作流
cover: https://cdn.thenewstack.io/media/2025/05/c924d026-how-mcp-enables-agentic-ai-workflows2.jpg
summary: Agentic AI工作流涌现！本文揭秘如何用 Anthropic 的 MCP 赋能 LLM，实现自主决策。通过 `Todo List MCP Server` 和 `Calendar MCP Server` 演示，展示 MCP 客户端如何协调工具和动态提示，构建模块化、可组合的智能自动化流程。MCP 嵌套实现类似微服务的代理委托，`dev-scaffolding` 服务器联动 `spec-writer`、`code-gen`、`test-writer`，构建强大工具系统。
-->

Agentic AI工作流涌现！本文揭秘如何用 Anthropic 的 MCP 赋能 LLM，实现自主决策。通过 `Todo List MCP Server` 和 `Calendar MCP Server` 演示，展示 MCP 客户端如何协调工具和动态提示，构建模块化、可组合的智能自动化流程。MCP 嵌套实现类似微服务的代理委托，`dev-scaffolding` 服务器联动 `spec-writer`、`code-gen`、`test-writer`，构建强大工具系统。

> 译自：[How MCP Enables Agentic AI Workflows](https://thenewstack.io/how-mcp-enables-agentic-ai-workflows/)
> 
> 作者：Michael Field

人们对 Anthropic 的 [模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) 的兴趣与对它是什么以及为什么要使用它的困惑一样高。在本系列文章的第 1 部分中，我深入 [探讨了 MCP](https://thenewstack.io/what-is-mcp-game-changer-or-just-more-hype)——它是什么，以及它不是什么。在本文中，我将探讨围绕它如此多讨论的主要原因：赋能 agentic AI 工作流。

## 用于 Agentic 工作流的 MCP

原始的 [大型语言模型 (LLM)](https://thenewstack.io/category/llm/) 只是将输入映射到输出。一个 agentic LLM 系统赋予 LLM：

- 行动的工具
- 对过去步骤的记忆
- 迭代循环和推理的方式
- 可选的目标或任务

因此，当你将 LLM 与工具连接起来，让它决定调用哪些工具，让它反思结果并让它计划下一步——你就使它具有了 agentic 能力。它现在可以决定下一步做什么，而无需被告知每一步。

那么这与 MCP 有什么关系呢？嗯，正如我们所提到的，MCP 可以提供超出工具的上下文。MCP 服务器还可以提供参数化的提示，从而有效地允许 MCP 服务器向 LLM 提供下一个指令。这种提示链可以打开一些非常有趣的大门。

更引人注目的是 MCP 如何在正确的时间呈现相关的工具，而无需将每个选项都塞进提示上下文中。MCP 允许一种更模块化的方法，而不是过度设计提示描述以考虑每一种可能性并迫使 LLM 进入确定性的工作流程：“这是来自此工具调用的响应，如果事情变得更复杂，这里有一些可能有帮助的工具。”这使得系统更具适应性和可扩展性，同时仍然让 LLM 能够灵活地探索新的路径，如果最初的指令不是完全确定性的。

事实上，有了这些能力，我们就拥有了一些类似于 agent 的东西，它从以下几个方面的相互作用中产生：

- LLM（推理和决策）
- MCP 服务器（提供工具和链接提示）
- MCP 客户端（管理循环和执行）
- 用户（提供目标）

让我们来看看实际情况。我将演示一个非常简单的 agentic 工作流，其中 LLM 根据返回的提示调用来自多个 MCP 服务器的工具。以下是我正在使用的服务器：

**Todo List MCP Server**

```
[[tool]]
name = "add_task"
description = "Adds a new task to your todo list."
input_parameters = [
  { name = "task_description", type = "string", description = "The task to add to your todo list." }
]

[[prompt]]
name = "plan_daily_tasks"
description = "Plans the day by breaking down a user goal into actionable tasks."
input_parameters = [
  { name = "user_goal", type = "string", description = "The user's goal for the day." }
]
template = """Based on the user's goal: '{user_goal}', generate 2-3 specific, actionable tasks that would help the user achieve it.
For each task, call the `add_task` tool with a helpful task description."""
```

**Calendar MCP Server**

```
[[tool]]
name = "schedule_event"
description = "Schedules an event in your calendar."
input_parameters = [
  { name = "task_description", type = "string", description = "The task or event to be scheduled." },
  { name = "time", type = "string", description = "The time when the event should be scheduled (e.g., '2pm today')." }
]

[[prompt]]
name = "schedule_todo_task"
description = "Schedules a task from the todo list into your calendar."
input_parameters = [
  { name = "task_description", type = "string", description = "The task to schedule." }
]
template = """The user wants to schedule the task: '{task_description}'.
Suggest a good time for today and call the `schedule_event` tool to add it to the calendar."""
```

好的，现在想象你有一个聊天机器人，可以访问这些 MCP 服务器提供的上下文。当用户提供一个高级目标，例如“我今天想专注于深度工作”时，MCP 客户端会协调一个模块化的、多服务器的工作流程来满足请求。它将用户消息与来自所有连接的 MCP 服务器的工具元数据和提示指令打包在一起，并将其发送到 LLM。LLM 首先从 Todo Server 中选择一个高级规划工具 `plan_daily_tasks`，该工具返回一个提示，指示 LLM 使用 `add_task` 将目标分解为可操作的任务。

随着任务的创建和 LLM 收到通知，LLM 会进一步推理并决定通过调用 `schedule_todo_task` 来安排任务，从而触发 Calendar Server。该服务器使用新的提示指导来使用 `schedule_event` 做出响应，此时 LLM 会以特定时间最终确定当天的计划。

每个工具交互都由 MCP 客户端路由和协调，该客户端管理推理循环，协调工具执行并跟踪整个会话的交互状态。这形成了一个完全自主的工作流程：用户**设定目标**，LLM **推理和决策**，MCP 服务器**公开工具和动态提示**，MCP 客户端**协调流程**，从而在各个领域实现智能、可组合的自动化。

![](https://cdn.thenewstack.io/media/2025/05/ea173846-mcp-agent-architecture.png)

从一个非常基础和高级的提示开始，你现在有了一个代理，它可以自行做出多个决策以达到最终目标。当然，如果不了解用户希望将精力集中在哪些深度工作上，那么生成这些任务的价值就微乎其微了，但是改进这一点只需要修改 MCP 服务器，使其具有更全面和周到的提示。

## MCP 嵌套

当你开始关注单层 MCP 客户端和服务器之外的东西时，事情开始变得非常有趣。MCP 服务器也可以是其他 MCP 服务器的客户端。这种嵌套实现了模块化、组合和类似代理的委托，其中一个服务器可以将部分推理或功能“委托”给另一个服务器。

这就像代理的 [微服务](https://thenewstack.io/microservices/)。正如我们从后端应用程序的 [单体架构转向微服务架构](https://thenewstack.io/microservices/microservices-vs-monoliths-an-operational-comparison/) 一样，我们现在正在使用 MCP 服务器将工具逻辑与代理运行时解耦。基于新 MCP 服务器的快速添加，很容易想象一个庞大且高度可组合的工具系统，可以像乐高积木一样用于构建全面的工作流程。

例如，你可以拥有一个 `dev-scaffolding` MCP 服务器，它充当高级协调器，专注于通过协调几个专门的上游 MCP 服务器来帮助开发人员将想法转化为可工作的代码。当用户请求新的应用程序功能（例如，“添加登录功能”）时，协调器服务器使用上游服务器——`spec-writer` 生成 API 规范，`code-gen` 从该规范搭建代码，以及 `test-writer` 生成相应的测试用例。

这些集体的 MCP 服务器也可以用于特定于环境的功能。换句话说，它们公开相同的接口（例如，`query_database` ），但配置用于不同的环境。这将允许你拥有一个 `dev-app-server` ，其中包括上游 MCP 服务器，例如使用 SQlite 数据库的 `dev-db-server` 、返回模拟身份验证响应的 `dev-auth-server` 以及包装本地命令行界面 (CLI) 工具的 `dev-deploy-server` 。然后，`prod-app-server` 将指向与基于云的部署相关的相关上游服务器。

像 mcp.run 这样的平台已经大量利用了这种可组合性。Mcp.run 允许你安装一个可扩展的、动态可更新的服务器，该服务器利用它称为 servlet 的 MCP 服务器的上游注册表。这些 servlet *不需要* 本地安装，但可以在 mcp.run 基础设施上远程运行。

由于多种原因，这非常强大，但就本文而言，它突出了 MCP 生态系统中正在发生的一个重要转变：远程 MCP 服务器。这就是本系列第三篇也是最后一篇文章的主题。

*想了解更多？了解 Kong 今天如何解决现实世界中的 MCP 服务器挑战。*