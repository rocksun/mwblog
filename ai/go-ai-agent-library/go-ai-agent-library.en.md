# Introduction

LangGraph tries to reinvent programming language control flow by implementing graphs for AI agent development. But here's the fundamental issue: programming languages already are graphs with compile-time validation and control flow management.

During my research into AI agent development, I built agents using Python and LangGraph for cybersecurity scanning, documented in these articles:

The key insight I discovered is that an AI agent is fundamentally just a pattern of using LLMs that looks like this:

```


```
1for {
2    res := callLLM(ctx)
3    if res.ToolsCalling {
4        ctx = executeTools(res.ToolsCalling)
5    }
6    if res.End {
7        return
8    }
9}
```


```

This is simply calling an LLM in a loop and allowing the LLM to make decisions for the next step.

# The LangGraph Problem

LangGraph proposes using graph structures to implement application flow:

![go-ai-agent-library-graph-flow.png](/_next/image?url=%2Fblog%2Fgo-ai-agent-library%2Fgo-ai-agent-library-graph-flow.png&w=1080&q=75)

This introduces unnecessary complexity because programming languages already implement graph structures with compile-time flow validation. In LangGraph:

* **Vertices** specify business logic
* **Edges** specify control flow

In any programming language, the same functionality is achieved with standard language constructs:

* **Operators** specify business logic
* **Conditions** (if/else) specify control flow

The agent code example demonstrates this natural graph structure:

```


```
1for {
2    res := callLLM(ctx)     // vertex (business logic)
3    if res.ToolsCalling {   // edge (control flow)
4        ctx = executeTools(res.ToolsCalling) // vertex (business logic)
5    }
6    if res.End {            // edge (control flow)
7        return
8    }
9}
```


```

LangGraph compiles graphs and performs validation, which adds little value in compiled programming languages that already provide these guarantees. This observation led me to develop my own AI agent library that leverages existing language features instead of reimplementing them.

# The go-agent Library

**Current Status:** Active development, not production-ready  
**GitHub:** <https://github.com/vitalii-honchar/go-agent>  
**Features:**

* ReAct Agent support
* OpenAI API integration
* Type-safe AI agent development

I chose Go for several technical advantages over Python:

* **Strict compilation checks** catch errors at build time
* **True parallelism** with goroutines vs Python's GIL limitations
* **Superior performance** for infrastructure workloads
* **Better suited for engineering tasks** rather than data science experiments

Instead of implementing graph abstractions, I focused on agent patterns. The first implementation targets the ReAct pattern:

```


```
1// Define tool parameters with JSON schema validation
2type AddToolParams struct {
3    Num1 float64 `json:"num1" jsonschema_description:"First number to add"`
4    Num2 float64 `json:"num2" jsonschema_description:"Second number to add"`
5}
6
7type AddResult struct {
8    llm.BaseLLMToolResult
9    Sum float64 `json:"sum" jsonschema_description:"Sum of the two numbers"`
10}
11
12// Create type-safe tool with validation
13addTool := llm.NewLLMTool(
14    llm.WithLLMToolName("add"),
15    llm.WithLLMToolDescription("Adds two numbers together"),
16    llm.WithLLMToolParametersSchema[AddToolParams](),
17    llm.WithLLMToolCall(func(callID string, params AddToolParams) (AddResult, error) {
18        return AddResult{
19            BaseLLMToolResult: llm.BaseLLMToolResult{ID: callID},
20            Sum:              params.Num1 + params.Num2,
21        }, nil
22    }),
23)
24
25// Configure agent with usage limits and behavior
26calculatorAgent, err := agent.NewAgent(
27    agent.WithName[CalculatorResult]("calculator"),
28    agent.WithLLMConfig[CalculatorResult](llmConfig),
29    agent.WithBehavior[CalculatorResult]("Use the add tool to calculate sums. Do not calculate manually."),
30    agent.WithTool[CalculatorResult]("add", addTool),
31    agent.WithToolLimit[CalculatorResult]("add", 5), // Maximum 5 calls
32)
```


```

## Developer Experience Advantages

The library requires developers to specify only:

* **Tools** that the agent can use
* **Behavior prompts** focused on domain-specific tasks

The system prompt for ReAct pattern implementation is handled automatically ([source](https://github.com/vitalii-honchar/go-agent/blob/main/pkg/goagent/agent/agent.go#L33C1-L61C3)):

```


```
1var systemPromptTemplate = NewPrompt(`You are an agent that implements the ReAct ` +
2    `(Reasoning-Action-Observation) pattern to solve tasks through systematic thinking and tool usage.
3
4## REASONING PROTOCOL
5
6Before EVERY action:
71. **THINK**: State your reasoning for the next step
82. **ACT**: Execute the appropriate tool with complete parameters
93. **OBSERVE**: Analyze the results and their implications
10
11Always maintain explicit reasoning chains. Your thoughts should be visible and logical.
12
13## EXECUTION CONTEXT
14
15TOOLS AVAILABLE TO USE:
16{{.tools}}
17
18CURRENT TOOLS USAGE:
19{{.tools_usage}}
20
21TOOLS USAGE LIMITS:
22{{.calling_limits}}
23
24## AGENT BEHAVIOR
25
26<BEHAVIOR>
27{{.behavior}}
28</BEHAVIOR>
29`)
```


```

This abstraction allows developers to focus on business logic rather than ReAct implementation details.

## Flexible LLM Configuration

The library supports flexible LLM configuration with a simple interface:

```


```
1agent.WithLLMConfig[HashResult](llm.LLMConfig{
2    Type:        llm.LLMTypeOpenAI,
3    APIKey:      apiKey,
4    Model:       "gpt-4o",
5    Temperature: 0.0,
6})
```


```

Currently supporting OpenAI API with planned expansion to other providers.

# Development Roadmap

The [go-agent](https://github.com/vitalii-honchar/go-agent/tree/main) library is in early development. I'm building real AI agents with it to refine the API before releasing version `1.0.0`. Planned features include:

* **Memory support** for persistent agent state
* **Ollama integration** for local LLM deployment
* **Multi-agent orchestration** capabilities
* **Concurrent tool execution** leveraging Go's parallelism
* **Advanced error handling** patterns

# Technical Philosophy

I built go-agent because I see AI agents becoming critical infrastructure components that require:

* **High performance** for production workloads
* **Strong guarantees** through type safety
* **Maintainability** by software engineering teams

The separation of concerns should be:

* **Software engineers** build and maintain the agent infrastructure layer
* **Data scientists/prompt engineers** develop domain-specific prompts and behavior

This division of responsibility makes LangGraph's approach problematic due to Python's performance limitations and the unnecessary complexity of reimplementing control flow that programming languages already provide efficiently.

# Conclusion

LangGraph attempts to solve problems that don't exist in compiled languages while introducing complexity that hinders development velocity. The [go-agent](https://github.com/vitalii-honchar/go-agent) library demonstrates that AI agents can be built more efficiently by leveraging existing language features rather than creating new abstractions.

By focusing on what actually matters—type safety, performance, and developer productivity—we can build more reliable AI agent systems that scale with real-world infrastructure demands.