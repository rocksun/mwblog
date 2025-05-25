# Tiny Agents in Python：一个由 MCP 驱动的 Agent，代码量约为 70 行

[在 GitHub 上更新](https://github.com/huggingface/blog/blob/main/python-tiny-agents.md)

灵感来自 [JS 中的 Tiny Agents](https://huggingface.co/blog/tiny-agents)，我们将这个想法移植到了 Python 🐍，并扩展了 `huggingface_hub` [客户端 SDK，使其可以充当 MCP 客户端，从而可以从 MCP 服务器拉取工具，并在推理期间将其传递给 LLM。](https://github.com/huggingface/huggingface_hub/)

MCP ([模型上下文协议](https://modelcontextprotocol.io/)) 是一个开放协议，用于标准化大型语言模型 (LLM) 与外部工具和 API 的交互方式。从本质上讲，它消除了为每个工具编写自定义集成的需要，从而可以更轻松地将新功能插入到 LLM 中。

在这篇博文中，我们将向您展示如何开始使用 Python 中的 Tiny Agent，该 Agent 连接到 MCP 服务器以解锁强大的工具功能。您将看到启动自己的 Agent 并开始构建是多么容易！

剧透：Agent 本质上是一个构建在 MCP 客户端之上的 while 循环！

## 如何运行演示

本节将引导您了解如何使用现有的 Tiny Agents。我们将介绍设置和运行 Agent 的命令。

首先，您需要安装最新版本的 `huggingface_hub`，并使用 `mcp` extra 来获取所有必要的组件。

```
pip install "huggingface_hub[mcp]>=0.32.0"
```

现在，让我们使用 CLI 运行一个 Agent！

最酷的部分是，您可以直接从 Hugging Face Hub [tiny-agents](https://huggingface.co/datasets/tiny-agents/tiny-agents) 数据集中加载 Agent，或者指定您自己的本地 Agent 配置的路径！

```
> tiny-agents run --help
Usage: tiny-agents run [OPTIONS] [PATH] COMMAND [ARGS]...
Run the Agent in the CLI
╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ path [PATH] Path to a local folder containing an agent.json file or a built-in agent stored in the 'tiny-agents/tiny-agents' Hugging Face dataset │
│ (https://huggingface.co/datasets/tiny-agents/tiny-agents) │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help Show this message and exit. │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

如果您没有提供特定 Agent 配置的路径，我们的 Tiny Agent 默认会连接到以下两个 MCP 服务器：

- “canonical”[文件系统服务器](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)，它可以访问您的桌面，以及
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) 服务器，它知道如何为您使用沙盒 Chromium 浏览器。

以下示例展示了一个配置为通过 Nebius 推理提供程序使用 [Qwen/Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) 模型的 Web 浏览 Agent，它配备了一个 playwright MCP 服务器，这使其可以使用 Web 浏览器！Agent 配置是通过指定 [其在 tiny-agents/tiny-agents](https://huggingface.co/datasets/tiny-agents/tiny-agents/tree/main/celinah/web-browser) Hugging Face 数据集中的路径来加载的。

当您运行 Agent 时，您会看到它加载，并列出它从其连接的 MCP 服务器中发现的工具。然后，它就可以接受您的提示了！

此演示中使用的提示：

```
do a Web Search for HF inference providers on Brave Search and open the first result and then give me the list of the inference providers supported on Hugging Face
```

您还可以使用 Gradio Spaces 作为 MCP 服务器！以下示例通过 Nebius 推理提供程序使用 [Qwen/Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) 模型，并连接到 `FLUX.1 [schnell]` 图像生成 HF Space 作为 MCP 服务器。该 Agent 是从 Hugging Face Hub 上的 [tiny-agents/tiny-agents](https://huggingface.co/datasets/tiny-agents/tiny-agents/tree/main/julien-c/flux-schnell-generator) 数据集中的配置加载的。

此演示中使用的提示：

```
Generate a 1024x1024 image of a tiny astronaut hatching from an egg on the surface of the moon.
```

现在您已经了解了如何运行现有的 Tiny Agents，以下各节将更深入地探讨它们的工作原理以及如何构建自己的 Agent。

### Agent 配置
每个代理的行为（其默认模型、推理提供者、要连接的 MCP 服务器以及其初始系统提示）由一个 `agent.json` 文件定义。您还可以在同一目录中提供自定义的 `PROMPT.md`，以获得更详细的系统提示。这是一个例子：

`agent.json`
`model` 和 `provider` 字段指定了代理使用的 LLM 和推理提供者。`servers` 数组定义了代理将连接的 MCP 服务器。在此示例中，配置了一个“stdio”MCP 服务器。这种类型的服务器作为本地进程运行。代理使用指定的 `command` 和 `args` 启动它，然后通过 stdin/stdout 与其通信，以发现和执行可用的工具。

```json
{
"model": "Qwen/Qwen2.5-72B-Instruct",
"provider": "nebius",
"servers": [
{
"type": "stdio",
"config": {
"command": "npx",
"args": ["@playwright/mcp@latest"]
}
}
]
}
```

`PROMPT.md`

```
You are an agent - please keep going until the user’s query is completely resolved [...]
```

您可以在[这里](https://huggingface.co)找到关于 Hugging Face 推理提供者的更多详细信息。

[
](#llms-can-use-tools)

## LLMs 可以使用工具

现代 LLM 是为函数调用（或工具使用）而构建的，这使用户能够轻松构建针对特定用例和实际任务量身定制的应用程序。

函数由其模式定义，该模式告知 LLM 它做什么以及它期望什么输入参数。LLM 决定何时使用工具，然后代理协调运行该工具并将结果反馈回来。

```json
tools = [
{
"type": "function",
"function": {
"name": "get_weather",
"description": "Get current temperature for a given location.",
"parameters": {
"type": "object",
"properties": {
"location": {
"type": "string",
"description": "City and country e.g. Paris, France"
}
},
"required": ["location"],
},
}
}
]
```

`InferenceClient` 实现了与 [OpenAI Chat Completions API](https://platform.openai.com/docs/guides/function-calling?api-mode=chat) 相同的工具调用接口，这是推理提供者和社区的既定标准。

[
](#building-our-python-mcp-client)

## 构建我们的 Python MCP 客户端

`MCPClient` 是我们工具使用功能的核心。它现在是 `huggingface_hub` 的一部分，并使用 `AsyncInferenceClient` 与 LLM 通信。

完整的 `MCPClient` 代码在[这里](https://huggingface.co)，如果您想使用实际代码来学习 🤓

`MCPClient` 的主要职责：

- 管理与一个或多个 MCP 服务器的异步连接。
- 从这些服务器发现工具。
- 为 LLM 格式化这些工具。
- 通过正确的 MCP 服务器执行工具调用。

以下是它如何连接到 MCP 服务器的简要介绍（`add_mcp_server` 方法）：

```python
# Lines 111-219 of `MCPClient.add_mcp_server`
# https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/inference/_mcp/mcp_client.py#L111:L219
class MCPClient:
...
async def add_mcp_server(self, type: ServerType, **params: Any):
# 'type' can be "stdio", "sse", or "http"
# 'params' are specific to the server type, e.g.:
# for "stdio": {"command": "my_tool_server_cmd", "args": ["--port", "1234"]}
# for "http": {"url": "http://my.tool.server/mcp"}
# 1. Establish connection based on type (stdio, sse, http)
# (Uses mcp.client.stdio_client, sse_client, or streamablehttp_client)
read, write = await self.exit_stack.enter_async_context(...)
# 2. Create an MCP ClientSession
session = await self.exit_stack.enter_async_context(
ClientSession(read_stream=read, write_stream=write, ...)
)
await session.initialize()
# 3. List tools from the server
response = await session.list_tools()
for tool in response.tools:
# Store session for this tool
self.sessions[tool.name] = session
# Add tool to the list of available tools and Format for LLM
self.available_tools.append({
"type": "function",
"function": {
"name": tool.name,
"description": tool.description,
"parameters": tool.input_schema,
},
})
```

它支持用于本地工具的 `stdio` 服务器（例如访问您的文件系统）和用于远程工具的 `http` 服务器！它还与 `sse` 兼容，`sse` 是以前的远程工具标准。

[
](#using-the-tools-streaming-and-processing)

## 使用工具：流式传输和处理

`MCPClient` 的 `process_single_turn_with_tools` 方法是 LLM 交互发生的地方。它通过 `AsyncInferenceClient.chat.completions.create(..., stream=True)` 将对话历史记录和可用工具发送到 LLM。

[
](#1-prepare-tools-and-calling-the-llm)

## 1. 准备工具并调用 LLM

首先，该方法确定 LLM 应该知道的当前回合的所有工具——这包括来自 MCP 服务器的工具和任何用于代理控制的特殊“退出循环”工具；然后，它对 LLM 进行流式调用：

```python
# Lines 241-251 of `MCPClient.process_single_turn_with_tools`
# https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/inference/_mcp/mcp_client.py#L241:L251
# Prepare tools list based on options
tools = self.available_tools
```
如果 `exit_loop_tools` 不是 `None`：

```python
tools = [*exit_loop_tools, *self.available_tools]
# Create the streaming request to the LLM
response = await self.client.chat.completions.create(
    messages=messages,
    tools=tools,
    tool_choice="auto",  # LLM decides if it needs a tool
    stream=True,
)
```

当从 LLM 接收到数据块时，该方法会遍历它们。每个数据块都会立即产生，然后我们重建完整的文本响应和任何工具调用。

```
# Lines 258-290 of `MCPClient.process_single_turn_with_tools`
# https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/inference/_mcp/mcp_client.py#L258:L290
# Read from stream
async for chunk in response:
    # Yield each chunk to caller
    yield chunk
    # Aggregate LLM's text response and parts of tool calls
    …
```

## 2. 执行工具

一旦流完成，如果 LLM 请求了任何工具调用（现在已在 `final_tool_calls` 中完全重建），该方法将处理每一个调用：

```
# Lines 293-313 of `MCPClient.process_single_turn_with_tools`
# https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/inference/_mcp/mcp_client.py#L293:L313
for tool_call in final_tool_calls.values():
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")
    # Prepare a message to store the tool's result
    tool_message = {"role": "tool", "tool_call_id": tool_call.id, "content": "", "name": function_name}
    # a. Is this a special "exit loop" tool?
    if exit_loop_tools and function_name in [t.function.name for t in exit_loop_tools]:
        # If so, yield a message and terminate this turn's processing
        messages.append(ChatCompletionInputMessage.parse_obj_as_instance(tool_message))
        yield ChatCompletionInputMessage.parse_obj_as_instance(tool_message)
        return  # The Agent's main loop will handle this signal
    # b. It's a regular tool: find the MCP session and execute it
    session = self.sessions.get(function_name)  # self.sessions maps tool names to MCP connections
    if session is not None:
        result = await session.call_tool(function_name, function_args)
        tool_message["content"] = format_result(result)  # format_result processes tool output
    else:
        tool_message["content"] = f"Error: No session found for tool: {function_name}"
    tool_message["content"] = error_msg
    # Add tool result to history and yield it
    ...
```

它首先检查调用的工具是否退出了循环（`exit_loop_tool`）。如果不是，它会找到负责该工具的正确 MCP 会话，并调用 `session.call_tool()`。然后，结果（或错误响应）会被格式化，添加到对话历史记录中，并产生，以便 Agent 知道工具的输出。

## 我们的小型 Python Agent：它（几乎）只是一个循环！

由于 `MCPClient` 完成了所有工具交互的工作，我们的 `Agent` 类变得非常简单。它继承自 `MCPClient` 并添加了对话管理逻辑。

Agent 类很小，专注于对话循环，代码可以在 [这里](https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/inference/_mcp/agent.py)找到。

## 1. 初始化 Agent

创建 Agent 时，它会获取 Agent 配置（模型、提供程序、要使用的 MCP 服务器、系统提示），并使用系统提示初始化对话历史记录。然后，`load_tools()` 方法会遍历服务器配置（在 agent.json 中定义），并为每个配置调用 `add_mcp_server`（来自父类 `MCPClient`），从而填充 Agent 的工具箱。

```
# Lines 12-54 of `Agent`
# https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/inference/_mcp/agent.py#L12:L54
class Agent(MCPClient):
    def __init__(
        self,
        *,
        model: str,
        servers: Iterable[Dict],  # Configuration for MCP servers
        provider: Optional[PROVIDER_OR_POLICY_T] = None,
        api_key: Optional[str] = None,
        prompt: Optional[str] = None,  # The system prompt
    ):
        # Initialize the underlying MCPClient with model, provider, etc.
        super().__init__(model=model, provider=provider, api_key=api_key)
        # Store server configurations to be loaded
        self._servers_cfg = list(servers)
        # Start the conversation with a system message
        self.messages: List[Union[Dict, ChatCompletionInputMessage]] = [
            {"role": "system", "content": prompt or DEFAULT_SYSTEM_PROMPT}
        ]

    async def load_tools(self) -> None:
        # Connect to all configured MCP servers and register their tools
        for cfg in self._servers_cfg:
            await self.add_mcp_server(cfg["type"], **cfg["config"])
```

## 2. Agent 的核心：循环

`Agent.run()` 方法是一个异步生成器，用于处理单个用户输入。它管理对话轮次，决定 Agent 当前的任务何时完成。

```
# Lines 56-99 of `Agent.run()`
# https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/inference/_mcp/agent.py#L56:L99
async def run(self, user_input: str, *, abort_event: Optional[asyncio.Event] = None, ...) -> AsyncGenerator[...]:
    ...
```

```python
while True: # Main loop for processing the user_input
...
# Delegate to MCPClient to interact with LLM and tools for one step.
# This streams back LLM text, tool call info, and tool results.
async for item in self.process_single_turn_with_tools(
self.messages,
...
):
    yield item
...
# Exit Conditions
# 1. Was an "exit" tool called?
if last.get("role") == "tool" and last.get("name") in {t.function.name for t in EXIT_LOOP_TOOLS}:
    return
# 2. Max turns reached or LLM gave a final text answer?
if last.get("role") != "tool" and num_turns > MAX_NUM_TURNS:
    return
if last.get("role") != "tool" and next_turn_should_call_tools:
    return
next_turn_should_call_tools = (last_message.get("role") != "tool")
```

在 `run()` 循环中：

- 首先，它将用户提示添加到对话中。
- 然后，它调用 `MCPClient.process_single_turn_with_tools(...)` 来获取 LLM 的响应并处理推理的每个步骤的任何工具执行。
- 每个项目都会立即产生，从而可以实时流式传输到调用者。
- 在每个步骤之后，它会检查退出条件：是否使用了特殊的“退出循环”工具，是否达到了最大轮数限制，或者 LLM 是否提供了对于当前请求来说似乎是最终的文本响应。

[
](#next-steps)

## 下一步

有很多很酷的方法可以探索和扩展 MCP Client 和 Tiny Agent 🔥 以下是一些帮助你入门的想法：

- 衡量不同的 LLM 模型和推理提供商如何影响 Agent 的性能：工具调用性能可能会有所不同，因为每个提供商可能会对其进行不同的优化。你可以在[此处](https://huggingface.co/docs/inference-providers/index#partners)找到支持的提供商列表。
- 使用本地 LLM 推理服务器（例如 [llama.cpp](https://github.com/ggerganov/llama.cpp) 或 [LM Studio](https://lmstudio.ai/)）运行微型 Agent。
- 当然，还可以做出贡献！在 Hugging Face Hub 上的 [tiny-agents/tiny-agents](https://huggingface.co/datasets/tiny-agents/tiny-agents) 数据集中分享你独特的微型 Agent 并打开 PR。

欢迎提出 Pull Request 和贡献！同样，这里的一切都是[开源](https://github.com/huggingface/huggingface_hub)的！💎❤️