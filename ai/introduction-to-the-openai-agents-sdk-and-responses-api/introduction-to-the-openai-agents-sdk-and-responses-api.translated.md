# OpenAI Agents SDK 和 Responses API 简介

![Featured image for: Introduction to the OpenAI Agents SDK and Responses API](https://cdn.thenewstack.io/media/2025/03/9c5be4c1-yasa-design-studio-yoh9dcqndii-unsplashb-1024x576.jpg)

当 OpenAI 推出被其他人称为 [Agents SDK](https://openai.com/index/new-tools-for-building-agents/) 的东西时，它承认以联合的方式使用现有功能“可能具有挑战性，通常需要大量的提示迭代和自定义编排逻辑，而没有足够的可观测性或内置支持”。简而言之，使用 [agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) 需要相当多的编程，这不是任何 AI 提供商想要推销的故事。

为了将叙述拉回到在 AI 上花钱最终将消除对昂贵的人工软件开发（或者实际上是人类）的需求的观点，OpenAI 正在实施一种结构以允许简单的编排。

让我们首先总结一下问题是什么。Agentic 任务意味着至少有两个进程独立工作，一个任务启动另一个任务，结果最终报告回最终报告进程——希望在相似的时间。 “结果”也必须采用已知格式（例如，句子、文件、图像、数据库），但这不容易概括。即使是顺利的情况也是一种微妙的平衡——处理和解释错误是另一个问题。这些都是熟悉的编排问题。但作为一个行业，没有人相信编排是一个“已解决”的问题。大量使用 LLM 也增加了控制 token 使用的需求；[tokens](https://thenewstack.io/what-is-an-llm-token-beginner-friendly-guide-for-developers/) 成为新的黑金。

为了开始编排之旅，OpenAI 向其核心平台添加了一些新的 API。值得注意的是，它引入了一个基本的 **Responses API**，它清理了聊天代理所做的一些假设。

从最简单的意义上讲，这可以捕获输出：

```python
from openai import OpenAI
client = OpenAI()
response = client.responses.create(
    model="gpt-4o",
    input="Write a one-sentence bedtime story about a unicorn."
)
print(response.output_text)
```

您可以在此级别分析图像；并添加以下工具之一。注意：新模型可能会停止支持现有的 Chat Completions API——许多新功能仅支持新的 Responses API。
让我们看看这些新工具。**Web search** 允许代理抓取网络以执行简单的任务。下面的简短 Python 脚本显示了如何为模型提供使用此工具的选项：

```python
from openai import OpenAI
client = OpenAI()
response = client.responses.create(
    model="gpt-4o",
    tools=[{"type": "web_search_preview"}],
    input="What Kubernetes news story appeared today?"
)
print(response.output_text)
```

`reesponse`
还将包含对任何引用的文章的引用。这些查询可以按时间或位置定义。您还可以权衡成本、质量和延迟。
**File Search** 实际上是一个托管的向量存储。您表明文件搜索是一个可用的工具，并标识您的向量存储：
```python
from openai import OpenAI
client = OpenAI()
response = client.responses.create(
    model="gpt-4o-mini",
    input="What is deep research by OpenAI?",
    tools=[
        {
            "type": "file_search",
            "vector_store_ids": ["<vector_store_id>"]
        }
    ]
)
print(response)
```
如果需要，代理将使用它。响应将引用响应中使用的文档。您可以限制响应以控制 token 使用和延迟。 [对总文件大小](https://platform.openai.com/docs/guides/tools-file-search#limitations)、搜索的文件和向量存储的大小有限制。可搜索的文档类型（按文件类型）[似乎很广泛](https://platform.openai.com/docs/guides/tools-file-search#supported-files)。
**Computer Use** 工具很有趣：

“计算机使用工具在一个连续的循环中运行。它发送计算机操作，例如 `click(x,y)`
或 `type(text)`
，您的代码在计算机或浏览器环境中执行这些操作，然后将结果的屏幕截图返回给模型。”

这听起来像是它在假装是 [Selenium](https://www.selenium.dev/)，我们过去常使用该工具通过脚本测试 Web 界面。显然，这承认我们尚未进入 AI 仅与其他 AI 对话的世界。但这至少是对并非所有内容都是网站这一想法的认可。

## 尝试 Agents
我将使用 Python 示例（它绝对是 Python 优先的产品，但文档也显示了 JavaScript 等效脚本）。我在我的帖子中运行了几次 Python，但在我的新 MacBook 上，我将检查是否已安装 Python：

结果是 python@3.13 3.13.2 已经安装并且是最新的。

我的 pip 也在那里（作为 pip3）。

所以现在我可以安装 OpenAI 包：

啊，我记得这个。我们需要一个虚拟环境：

然后我激活虚拟环境：
我们准备好继续了。

当然，现在你需要使用并设置一个 `OPENAI_API_KEY`。 我在我的[帐户页面](https://platform.openai.com/settings/organization/api-keys)上创建了一个新的密钥，并设置了 `OPANAI_API_KEY`（别担心，它比这长得多）：

你还需要确保你有一些黑金——[我的意思是 tokens](https://platform.openai.com/settings/organization/billing/overview)。 我已经介绍了一些通过使用[本地模型](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/)来避免向 OpenAI 付费的方法，但在这篇文章中，我假设你正在为 tokens 付费。

按照惯例，让我们从一个简单的请求开始，检查上述基础是否到位，使用以下 **haiku.py**：

```python
from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are a helpful assistant")
result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)
```

我们得到了一个很好的回应：
（一首好的传统俳句应该提到季节的流逝，但这不是我们在这里的原因。）通常，我也会检查我的余额——但它没有受到干扰。

## 代理的巢穴

正如你所看到的，我们已经使用了一个 [agent](https://github.com/openai/openai-agents-python)。 并不是说它以任何方式介入，但我们稍后会讨论这个问题。

OpenAI 通过一些简单的术语简化了编排过程。 **handoff** 是对异步世界的介绍，其中某些东西必须等待其他东西。 让我们分解一下他们的例子，我将以 **hola.py** 运行它：

```python
from agents import Agent, Runner
import asyncio

spanish_agent = Agent(
    name="Spanish agent",
    instructions="You only speak Spanish.",
)
english_agent = Agent(
    name="English agent",
    instructions="You only speak English",
)
triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[spanish_agent, english_agent],
)

async def main():
    result = await Runner.run(triage_agent, input="Hola, ¿cómo estás?")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
```

这显示了两个基本的事情。 首先，我们习惯的纯英文的代理角色设置，以及代理之间的相互作用设置。 handoff 代理保留一个可用代理列表来回答响应。
现在，这意味着我的德语请求不会得到正确的响应。 因此，如果我们在 **hola.py** 中更改查询：

```python
...
async def main():
    result = await Runner.run(triage_agent, input="Wie geht es ihnen?")
...
```

并运行我们的代理巢穴：
因此，虽然 OpenAI 在翻译德语方面没有问题，但 triage 代理没有相关的语言代理可以移交，因此它完成了工作并以英语回复。 我们的德国客户不太可能感到不安，但我们可以改进。

因此，如果我们最终添加德语代理并将其放入 **hola.py** 的 handoffs 列表中：

```python
...
german_agent = Agent(
    name="German agent",
    instructions="You only speak German",
)
triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[spanish_agent, english_agent, german_agent],
)
...
```

我们可以再次尝试德语请求：
这次调用了正确的代理并做出响应。 我们的德国客户现在更高兴了——ausgezeichnet！ 不要忘记 [我的 Warp 终端](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) 也在为您提供这些响应的时间。

## 结论

我们首先研究了响应循环，其中可能包括进一步的工具调用。 如果响应有 handoff，我们将代理设置为新代理并返回到开始。

下面有一些日志记录选项，但与往常一样，OpenAI 在此阶段提供了相当高级别的 API——这应该鼓励实验，而无需过多地参与编排。

虽然我在这里介绍了代理，但在以后的文章中，我将研究 SDK 的更多部分。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。 订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)