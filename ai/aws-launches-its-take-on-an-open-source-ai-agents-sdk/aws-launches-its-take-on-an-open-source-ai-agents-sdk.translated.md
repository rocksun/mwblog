# AWS 发布其开源 AI Agent SDK

![Featured image for: AWS 发布其开源 AI Agent SDK](https://cdn.thenewstack.io/media/2025/05/da2ae77f-img_6899-edit.7fa451fddc234945b82d58b2daf091ed-1024x576.jpg)

[AWS](https://aws.amazon.com/?utm_content=inline+mention) 今天[发布了](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/) [Strands Agents](https://strandsagents.com)，这是一个[开源](https://github.com/strands-agents/sdk-python) AI agent SDK，是 AWS 内部构建企业级 agent 的成果。
Accenture, Anthropic, Langfuse, mem0.ai, Meta, PwC, Ragas.io, 和 Tavily 正在加入 AWS 的行列。

随着 LangChain、CrewAI、OpenAI 的 Swarm 和市场上大量的其他框架的出现，选择使用哪个 agent 框架几乎变得和选择用哪个模型来驱动这些 agent 一样困难。但 AWS 表示，它对 agent 的看法使得开发者体验更简单，因为它更多地依赖于模型本身。这里的论点是，模型在过去几年里变得更加智能，这意味着它们需要更少的指导来弄清楚如何使用工具，例如。

Strands 支持各种各样的模型，包括来自 Amazon 自己的 Bedrock 服务和 LiteLLM，以及在 Ollama 的帮助下的本地模型。它将开箱即用地提供许多内置工具，允许 agent 从 Amazon Bedrock 的知识库中检索数据、调用 API 和运行 Python 逻辑，例如。当然，也支持模型上下文协议 (MCP) 服务器。

AWS 开发者 Agent 和体验总监 Neha Goswami 告诉我：“[The] Strands SDK 将通过实际使用模型的力量来帮助你构建 agent。这确实是我们在过去两年中看到的演变。Strands 现在允许你通过真正使用模型的推理能力来构建 agent，而工具的使用实际上现在已经融入到模型本身中。因此，我们使用它，然后我们还使用模型自己的反思和思维链能力来真正弄清楚如何构建正确的 agent。”

因此，Strands 还配备了一个思维工具，该工具提示模型使用多个周期进行思维处理和自我反思。AWS 首席工程师 Clare Liguori 在今天的公告中写道：“在模型驱动的方法中，将思维建模为一种工具使模型能够推理任务是否以及何时需要深入分析。”

还支持多 agent 工具，如 [workflow, graph, and swarm](https://github.com/strands-agents)，尽管今天的公告对此有所淡化。然而，Strands 将能够协调多个 agent 之间的任务并管理 agent 群。

在大多数情况下，使用 Strands 构建 agent 确实非常简单，并且与类似的框架一样，大部分工作都在于编写工具和正确的提示，因为运行 agent 的大部分代码都是样板代码。

Goswami 说：“作为一名现在正在构建 agent 的开发者，即使是我自己的团队，我们做事的方式，我们只是编写一些提示，现在我们非常关注适合这项工作的正确工具。因此，我们将此引入 SDK，然后我们通过结合使用这些提示、这些工具来构建我们的 agent，然后我们基本上进入一个 agent 循环，模型在其中指导自己如何正确构建 agent。”

展望未来，Goswami 指出，仍然缺乏工具的一个领域是遥测。我们很可能会在未来看到 Strands（或不同的 AWS 项目）解决这个问题。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，即可观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)