<!--
title: LangGraph 徒增复杂性？我的Go语言Agent方案更胜一筹
cover: https://vitaliihonchar.com/blog/go-ai-agent-library/go-ai-agent-library.jpg
summary: LangGraph试图用图结构重新定义控制流，但编程语言本身已是图结构。go-agent库利用Go语言特性，提供类型安全、高性能的AI代理开发，专注于业务逻辑而非重新实现控制流，更适合构建可靠的AI代理系统。
-->

LangGraph试图用图结构重新定义控制流，但编程语言本身已是图结构。go-agent库利用Go语言特性，提供类型安全、高性能的AI代理开发，专注于业务逻辑而非重新实现控制流，更适合构建可靠的AI代理系统。

> 译自：[Why LangGraph Overcomplicates AI Agents (And My Go Alternative)](https://vitaliihonchar.com/insights/go-ai-agent-library)
> 
> 作者：[no-author]

LangGraph 尝试通过为 AI 代理开发实现图结构来重新定义编程语言的控制流。但这里存在一个根本问题：编程语言本身已经是图结构，具有编译时验证和控制流管理。

在我对 AI 代理开发的研究过程中，我使用 Python 和 LangGraph 构建了用于网络安全扫描的代理，这些代理记录在以下文章中：

- [How to Build a ReAct AI Agent for Cybersecurity Scanning with Python and LangGraph](https://vitaliihonchar.com/insights/how-to-build-react-agent)
- [Pipeline of Agents Pattern: Building Maintainable AI Workflows with LangGraph](https://vitaliihonchar.com/insights/how-to-build-pipeline-of-agents)

我发现的关键洞察是，AI 代理从根本上来说只是 LLM 的一种使用模式，如下所示：


```go
for {
    res := callLLM(ctx)
    if res.ToolsCalling {
        ctx = executeTools(res.ToolsCalling)
    }
    if res.End {
        return
    }
}
```

这只是在一个循环中调用 LLM，并允许 LLM 决定下一步的操作。

### LangGraph 的问题

LangGraph 建议使用图结构来实现应用程序流程：

![go-ai-agent-library-graph-flow.png](https://vitaliihonchar.com/_next/image?url=%2Fblog%2Fgo-ai-agent-library%2Fgo-ai-agent-library-graph-flow.png&w=640&q=75)

这引入了不必要的复杂性，因为编程语言已经实现了具有编译时流程验证的图结构。在 LangGraph 中：

* **顶点 (Vertices)** 指定业务逻辑
* **边 (Edges)** 指定控制流

在任何编程语言中，相同的功能都可以通过标准语言结构来实现：

* **操作符 (Operators)** 指定业务逻辑
* **条件 (Conditions)** (if/else) 指定控制流

代理代码示例演示了这种自然的图结构：

```go
for {
    res := callLLM(ctx)     // vertex (business logic)
    if res.ToolsCalling {   // edge (control flow)
        ctx = executeTools(res.ToolsCalling) // vertex (business logic)
    }
    if res.End {            // edge (control flow)
        return
    }
}
```

LangGraph 编译图结构并执行验证，这在已经提供这些保证的已编译编程语言中几乎没有增加价值。这一观察结果促使我开发了自己的 AI 代理库，该库利用现有的语言特性，而不是重新实现它们。

## go-agent 库

**当前状态：** 积极开发中，尚未准备好用于生产环境
**GitHub：** <https://github.com/vitalii-honchar/go-agent>
**特性：**

* ReAct 代理支持
* OpenAI API 集成
* 类型安全的 AI 代理开发

我选择 Go 是因为其相对于 Python 的几个技术优势：

* **严格的编译检查** 在构建时捕获错误
* **真正的并行性** 使用 goroutine，而不是 Python 的 GIL 限制
* **卓越的性能** 适用于基础设施工作负载
* **更适合工程任务** 而不是数据科学实验

我没有实现图抽象，而是专注于代理模式。第一个实现针对 ReAct 模式：

```go
// Define tool parameters with JSON schema validation
type AddToolParams struct {
    Num1 float64 `json:"num1" jsonschema_description:"First number to add"`
    Num2 float64 `json:"num2" jsonschema_description:"Second number to add"`
}

type AddResult struct {
    llm.BaseLLMToolResult
    Sum float64 `json:"sum" jsonschema_description:"Sum of the two numbers"`
}

// Create type-safe tool with validation
addTool := llm.NewLLMTool(
    llm.WithLLMToolName("add"),
    llm.WithLLMToolDescription("Adds two numbers together"),
    llm.WithLLMToolParametersSchema[AddToolParams](),
    llm.WithLLMToolCall(func(callID string, params AddToolParams) (AddResult, error) {
        return AddResult{
            BaseLLMToolResult: llm.BaseLLMToolResult{ID: callID},
            Sum:              params.Num1 + params.Num2,
        }, nil
    }),
)

// Configure agent with usage limits and behavior
calculatorAgent, err := agent.NewAgent(
    agent.WithName[CalculatorResult]("calculator"),
    agent.WithLLMConfig[CalculatorResult](llmConfig),
    agent.WithBehavior[CalculatorResult]("Use the add tool to calculate sums. Do not calculate manually."),
    agent.WithTool[CalculatorResult]("add", addTool),
    agent.WithToolLimit[CalculatorResult]("add", 5), // Maximum 5 calls
)
```

### 开发者体验优势

该库要求开发人员仅指定：

* 代理可以使用的**工具 (Tools)**
* 专注于特定领域任务的**行为提示 (Behavior prompts)**

ReAct 模式实现的系统提示会自动处理 ([source](https://github.com/vitalii-honchar/go-agent/blob/main/pkg/goagent/agent/agent.go#L33C1-L61C3))：


```go
var systemPromptTemplate = NewPrompt(`You are an agent that implements the ReAct ` +
    `(Reasoning-Action-Observation) pattern to solve tasks through systematic thinking and tool usage.

### REASONING PROTOCOL

Before EVERY action:
1. **THINK**: State your reasoning for the next step
2. **ACT**: Execute the appropriate tool with complete parameters
3. **OBSERVE**: Analyze the results and their implications

Always maintain explicit reasoning chains. Your thoughts should be visible and logical.

### EXECUTION CONTEXT

TOOLS AVAILABLE TO USE:
{{.tools}}

CURRENT TOOLS USAGE:
{{.tools_usage}}

TOOLS USAGE LIMITS:
{{.calling_limits}}

### AGENT BEHAVIOR

<BEHAVIOR>
{{.behavior}}
</BEHAVIOR>
`)
```

这种抽象允许开发人员专注于业务逻辑，而不是 ReAct 实现细节。

### 灵活的 LLM 配置

该库支持通过一个简单的接口进行灵活的 LLM 配置：


```go
agent.WithLLMConfig[HashResult](llm.LLMConfig{
    Type:        llm.LLMTypeOpenAI,
    APIKey:      apiKey,
    Model:       "gpt-4o",
    Temperature: 0.0,
})
```

目前支持 OpenAI API，并计划扩展到其他提供商。

## 开发路线图

[go-agent](https://github.com/vitalii-honchar/go-agent/tree/main) 库正处于早期开发阶段。我正在使用它构建真正的 AI 代理，以便在发布 `1.0.0` 版本之前完善 API。计划的功能包括：

* **内存支持 (Memory support)** 用于持久化代理状态
* **Ollama 集成 (Ollama integration)** 用于本地 LLM 部署
* **多代理编排 (Multi-agent orchestration)** 功能
* **并发工具执行 (Concurrent tool execution)** 利用 Go 的并行性
* **高级错误处理 (Advanced error handling)** 模式

## 技术理念

我构建 go-agent 是因为我认为 AI 代理正在成为关键的基础设施组件，需要：

* **高性能 (High performance)** 用于生产工作负载
* 通过类型安全提供**强大的保证 (Strong guarantees)**
* 由软件工程团队实现**可维护性 (Maintainability)**

关注点分离应该是：

* **软件工程师** 构建和维护代理基础设施层
* **数据科学家/提示工程师** 开发特定领域的提示和行为

由于 Python 的性能限制以及重新实现编程语言已经有效提供的控制流的不必要复杂性，这种职责分工使得 LangGraph 的方法存在问题。

## 结论

LangGraph 试图解决编译语言中不存在的问题，同时引入了阻碍开发速度的复杂性。[go-agent](https://github.com/vitalii-honchar/go-agent) 库表明，通过利用现有的语言特性而不是创建新的抽象，可以更高效地构建 AI 代理。

通过专注于真正重要的事情——类型安全、性能和开发者生产力——我们可以构建更可靠的 AI 代理系统，以满足现实世界的基础设施需求。