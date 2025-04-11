<!--
title: 如何构建自己的简单AI代理来排除Kubernetes故障
cover: https://cdn.prod.website-files.com/635e4ccf77408db6bd802ae6/67f6263da6941ce2cca27631_Group%201000001800%20(1).png
summary: AutoGen v0.4 发布！用 AgentChat 轻松构建 Kubernetes 故障排除助手 Kaia。利用 Ollama 免费 LLM (如 qwen2) 创建 AssistantAgent，结合 kubectl 工具，构建单人 RoundRobinGroupChat 团队。加入 UserProxyAgent 实现人工干预，定义停止词，体验 AI 驱动的云原生运维！
-->

AutoGen v0.4 发布！用 AgentChat 轻松构建 Kubernetes 故障排除助手 Kaia。利用 Ollama 免费 LLM (如 qwen2) 创建 AssistantAgent，结合 kubectl 工具，构建单人 RoundRobinGroupChat 团队。加入 UserProxyAgent 实现人工干预，定义停止词，体验 AI 驱动的云原生运维！

> 译自：[How to build your own simple AI agent to troubleshoot Kubernetes](https://www.perfectscale.io/blog/build-simple-ai-agent-to-troubleshoot-kubernetes)
> 
> 作者：Anton Weiss



终于来了！AI 助手可以帮助我们与机器对话了。当然，它们也可以帮助我们处理 Kubernetes。

下面介绍如何使用最近发布的 AutoGen v0.4 AgentChat 功能构建你自己的（虽然非常基础）Kubernetes 故障排除助手。

## AutoGen v0.4

**AutoGen** 是一个领先的开源代理软件框架，刚刚通过 0.4 版本的发布进行了重大改进。新版本中的一项更改是增加了 **AgentChat** 层，这使得构建有用的助手变得更加容易。以下是新的 AutoGen 0.4 分层架构图：

![autogen v0.4](https://cdn.prod.website-files.com/635e4ccf77408db6bd802ae6/67f61be9a6941ce2cc996f90_AD_4nXfM9r3ycxjRYfWdOXtkGrQNYmaeG1FZ9kf4_9JXkl9ILRZFe7Tshj9nlIyBY49vrCMF7VjFFncV_ezlW1DMXeXB7nDNeHXME7e2hyEGY8lu091UCGkJ1sb52hntI9k3UcBZG7SwSg.png)

## 构建一个 Agent 团队

AgentChat 为我们提供了用户友好的抽象，可以帮助创建 AI agent 并将它们分组到团队中，以便它们可以共同朝着一个共同的目标努力。

创建一个 agent 非常简单：

```python
agent = AssistantAgent(name="my_agent",llm_client=llm_client)
```

将 agent 放入团队中可以这样操作：

```python
team = RoundRobinGroupChat([agent1,agent2],
termination_condition=termination)
stream = team.run_stream(task="Do something useful.")
```

## 使用 LLM

Agent 的基本工作方式是将任务发送到模型，并提供可以帮助完成任务的工具。LLM 预测完成任务的正确工具命令，agent 调用这些工具，将输出返回给 LLM，然后模型预测任务的正确解决方案。

![LLMs](https://cdn.prod.website-files.com/635e4ccf77408db6bd802ae6/67f61be9b1bafb58f0b09c5c_AD_4nXduCyh0C9xzprdD8MiwxZ-arzHTn9uWKft-bf666tj89I5sPL0jnE1X17kNc5dxWAA3AiHLVDK7Mr134Mr3-hQqQcCf29OisUjuu-hY6fFRNX0n3CgXRgMgN_jIQOVMadt31Rf4qA.png)

因此，我们需要将我们的 agent 连接到一个模型。我们当然可以使用 OpenAI、Claude 或其他知名模型，但这通常意味着注册并最终付费。仅仅为了玩开源？！当然不是！相反，我们将使用带有开源、免费使用的模型的 [Ollama](https://ollama.com/)。幸运的是，现在不乏轻量级模型，即使没有 GPU 也可以运行推理。在本示例中，我使用的是“qwen2”模型，但你可以使用你选择的任何其他模型。是的，如果你不介意联系 Google 进行简单的 Kubernetes 故障排除，你也可以免费使用 Gemini。AutoGen 支持所有 [主要的 LLM 提供商](https://microsoft.github.io/autogen/stable//user-guide/agentchat-user-guide/tutorial/models.html)：

## AgentChat 与 Ollama

通过运行 `brew install ollama` 安装 Ollama（如果你使用的是 Mac），或者按照你选择的 OS 的 [官方安装说明](https://ollama.com/download) 进行安装。

安装完成后，拉取模型：`ollama pull qwen2`
然后通过运行以下命令来提供服务：`ollama serve`

为了从我们的代码中实例化一个模型，我们将使用 [OllamaChatCompletionClient](https://microsoft.github.io/autogen/stable/reference/python/autogen_ext.models.ollama.html#autogen_ext.models.ollama.OllamaChatCompletionClient) 对象，并使用以下参数：

```python
model_client = OllamaChatCompletionClient(model="qwen2",
keep_alive="60m", response_format=StructuredOutput)
```

## 创建 Agent

一旦我们有了可用的模型，我们就可以使用 AgentChat 的 AssistantAgent（内置 agent，它使用语言模型并具有使用工具的能力）来创建我们有用的助手。

```python
agent = AssistantAgent(
   name="kaia",
   model_client=model_client,
   tools=[tool],
   system_message="""You are a Kubernetes troubleshooting agent.
     When asked about a resource but no namespace is specified - you can run kubectl get resource_type -A and then analyze the output to find the resource name.
     That's how you find the namespace where a resource is located.
     If the resource is a pod -  you MUST inspect the pod's logs for issues.
     The correct command to do that is: kubectl logs <pod_name> -n <namespace>.
     If a resource is not found in any namespace, inform me that it was not found.
""",
   reflect_on_tool_use=True,
  )
```

在这里，我创建了一个名为 **kaia** (**K**ubernetes** AI A**gent) 的 agent，它使用我之前创建的基于 Ollama 的 LLM 客户端，并接收到一个非常详细的系统提示，解释了应该如何排除 Kubernetes pod 的故障。（我花了大约 20 次迭代才想出一个提示，可以最大限度地减少幻觉）。我还告诉它 reflect_on_tool_use，这会导致它使用工具调用和结果进行另一次模型推理，以生成响应。

我想修改其他 agent 参数可以产生更好的结果，但对于本示例，我坚持使用基本知识。

## 提供工具

正如已经讨论过的，agent 需要工具来完成其工作。在这个简单的例子中，我只是让它访问我的 kubectl。对于更高级的用例，绝对要看看过去几个月创建的众多 Kubernetes [MCP](https://www.anthropic.com/news/model-context-protocol) 服务器之一。这是 Alexey Ledenev 创建的此类服务器的一个例子：[https://github.com/alexei-led/k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server)。

但在这里，我只是定义一个调用 `kubectl` 的函数并将其包装在 AutoGen FunctionTool 中：

```python
def call_kubectl(command: str) -> str:
   """Call any kubectl command in the current cluster context"""
   if command == '':
       return subprocess.check_output(['kubectl', ''])
   if command.split()[0] != 'kubectl':
       command = 'kubectl ' + command
   return (subprocess.check_output(command.split()))

tool = FunctionTool(call_kubectl, description="Kubernetes Command Execution", strict=True)
```

## 单人团队

现在互联网上有很多关于在 GenAI 的帮助下，一个人如何取代整个团队的讨论。不确定这对人类来说是否真实，毕竟我们组建团队不仅仅是为了提高生产力。

但对于 AI agent 来说，这绝对可行。（即使也有这样一种概念，即高度专业化的 AI agent 比处理所有工作的通用 agent 交付更好的结果）。无论如何，对于 Kaia 来说，单 agent 团队已经足够了，Kaia 的唯一目的是对 Kubernetes 进行故障排除。在 AgentChat 中创建这样一个单人团队的最简单方法是使用 [RoundRobinGroupChat](https://microsoft.github.io/autogen/stable/reference/python/autogen_agentchat.teams.html#autogen_agentchat.teams.RoundRobinGroupChat) - 一种简单而有效的团队配置，其中所有 agent 共享相同的上下文，并以循环方式轮流响应。

## 在循环中添加人工

当然，我们都设想一个未来，机器不仅会发现问题，还会无需询问我们即可修复它们。然而，现在 AI 容易产生幻觉，因此我们非常希望审查它决定做的任何事情。在 agent 团队中添加人工审查员的方法是创建一个 [UserProxyAgent](https://microsoft.github.io/autogen/stable/reference/python/autogen_agentchat.agents.html#autogen_agentchat.agents.UserProxyAgent)：

```python
user_proxy = UserProxyAgent("user_proxy", input_func=input)
```

## 停止词

我们的 agent 将继续工作，直到任务完成。但什么时候才算完成？AgentChat 团队允许我们定义终止条件，允许 agent 相互告知何时停止聊天和调用工具。在 Kaia 的例子中，我认为在团队合作中保持感恩和礼貌总是好的，所以我的终止消息是“Thanks!”。还有其他可能的方式来终止 agent 群聊：[TerminationCondition](https://microsoft.github.io/autogen/stable//reference/python/autogen_agentchat.base.html#autogen_agentchat.base.TerminationCondition)。请注意，我们还可以定义 `max_turns` 参数来限制 agent 交互的总次数。

所以最后，让我们创建我们的团队：

```python
termination_condition = TextMentionTermination("Thanks!")
team = RoundRobinGroupChat(
    [agent, user_proxy],
    termination_condition=termination_condition,
    # max_turns=10
)
```

## 让我们开始工作！

我们现在需要做的就是获取用户的输入，即 Kubernetes 故障排除的请求，并运行团队直到找到答案：

```python
async def ainput(string: str) -> str:
   await asyncio.to_thread(sys.stdout.write, f'{string}')
   return await asyncio.to_thread(sys.stdin.readline)


async def main():
 print("What do you want to know?");
 prompt = await ainput("Prompt:\n")
 # Ignoring warnings to clean up the output.
 with warnings.catch_warnings():
   warnings.simplefilter("ignore")
   async for message in team.run_stream(task=prompt):  # type: ignore
     if type(message).__name__ == "TextMessage" or type(message).__name__ == "UserInputRequestedEvent":
       if message.source not in ["user_proxy", "user"]:
         print(message.content)
         print("Type 'Thanks!' if you're done.\n")

asyncio.run(main())
```

请注意，我正在进行一些消息清理，以防止 AgentChat 向控制台打印太多内容。

## 使用 AI 对 Kubernetes 进行故障排除

要运行我编写的代码，请执行以下操作：

```bash
git clone https://github.com/otomato-gh/kaia
cd kaia
pip install -r requirements.txt
python3 kaia.py
```

然后使用类似以下内容提示它：“pod **dummy** 有什么问题？”

[观看以下视频以了解 kaia 的实际应用](https://youtu.be/85RZcMAPAeE?feature=shared)。然后单击[此处](https://github.com/otomato-gh/kaia)获取此简单基本 AI agent 的完整代码。然后在您自己的环境中运行它，让我知道结果如何。您想添加什么？它产生多少幻觉？哪个 LLM 对您来说效果最好？
接下来是什么？我将把Kaia连接到语音识别，最终能够真正地对我的集群低语。太激动了！

期待您的回音。