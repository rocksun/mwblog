<!--
title: 使用Ollama和Llama 2设置和运行本地LLM
cover: https://cdn.thenewstack.io/media/2024/02/4efb5fd7-monica-cisneros-parasi-_zsjafeahr8-unsplash-1024x683.jpg
-->

上周我发表了关于摆脱云端的文章，本周我将关注在我的 Mac 本地运行开源 LLM。如果这让人觉得像是某种“云端回归”项目的一部分，那不对：我只是对可以控制的工具感兴趣，以便添加到任何潜在的工作流中。

> 译自 [How to Set up and Run a Local LLM with Ollama and Llama 2](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/)，作者 David Eastman。

假设你的机器有足够的空间和内存，这样做的理由是什么？除了不必支付他人服务器的运行成本外，你还可以在不担心安全问题的情况下运行对私有数据的查询。

为此，我使用的是 Ollama。这是“一个允许你在本地机器上运行开源大型语言模型 (LLM) 的工具”。它们可以访问完整的开源模型列表，这些模型具有不同的专业化特点 —— 比如双语模型、紧凑型模型或代码生成模型。这起初是一个基于 Mac 的工具，但现在也可以在 Windows 上进行预览。它也可以通过 Docker 使用。

如果你正在寻找作为测试工作流一部分的 LLM，那么 Ollama 就是适合的选择：

Zoom

@patrickdubois 的 GenAI 测试演示

对于测试来说，从 Ollama 控制的本地 LLM 是很好的自包含系统，但它们的质量和速度与云端选项相比会有所降低。构建一个模拟框架将导致更快的测试，但设置这些可能会很繁琐。

我安装了 Ollama，打开了我的 Warp 终端，然后被提示尝试 Llama 2 模型（暂时我会忽略这个不是真正开源的论点）。我假设我需要先安装该模型，但运行命令已经搞定了：

Zoom

看着 llama2 7b 模型的规格，我远非肯定我的古老的 M1 之前的 MacBook，只有 8 GB 内存，甚至能否运行它。但它确实运行了，只是非常缓慢。

你可以看到，已经有了一个内置终端，所以我进行了一个快速的测试查询：

Zoom

这并不快，但模型显然还在运行。当我说“运行”时，我并不是完全的意思，因为模型在时间上被困在构建它的时刻：

Zoom

如果你在想，算术问题的正确答案实际上是 1,223,834,880。即使是粗略地看，也可以看出它不可能以六结束 —— 如果我再做一次，毫无疑问会不同。请记住，LLM 并不聪明，它们只是非常擅长从模型中提取语言含义。但你当然知道这一点。

方便的控制台很好用，但我想使用可用的 API。Ollama 将自己设置为本地服务器，端口为 11434。我们可以通过一个快速的 curl 命令来检查 API 是否响应。以下是一个非流式（即非交互式）REST 调用，通过 Warp 发送一个 JSON 风格的负载：

```bash
curl http://localhost:11434/api/generate -d '
{ 
 "model": "llama2", 
 "prompt": "为什么天空是蓝色的？", 
 "stream": false 
}'
```

响应是：

```json
{ 
 "model":"llama2", 
 "created_at":"2024-02-14T13:48:17.751003Z", 
 "response": "天空呈现蓝色是因为一种叫做瑞利散射的现象。", 
 "done":true, 
 "context":[518,25580,29962,..], 
 "total_duration":347735712609, 
 "load_duration":6372308, 
 "prompt_eval_duration":6193512000, 
 "eval_count":368, 
 "eval_duration":341521220000 
}
```

完整的响应行 —— 涵盖了瑞利散射、光的波长和太阳的角度 —— 在我看来都是正确的。

获得编程控制的常见途径是使用 Python，也许还有 Jupyter Notebook。但这些不是我首选的工具，所以我将尝试使用一些 C# 绑定。我在这里找到了一些。幸运的是，OllamaSharp 也可以通过 NuGet 作为一个包使用。

我对 Visual Studio Code 不是太感兴趣，但是一旦你设置了一个带有 NuGet 支持的 C# 控制台项目，启动速度就会很快。以下是与 Ollama 联系并发送查询的代码：

```csharp
using OllamaSharp; 

var uri = new Uri("http://localhost:11434"); 
var ollama = new OllamaApiClient(uri); 

// 选择一个模型用于进一步操作
ollama.SelectedModel = "llama2"; 
ConversationContext context = null; 
context = await ollama.StreamCompletion( 
 "你今天好吗？", 
 context, stream => Console.Write(stream.Response)
);
```

最终我们在调试控制台直接获得了响应（蓝色部分）：

Zoom

这很不错。
```

好的，现在我们准备问一些更具体的问题。我曾看到有人要求对其银行账户进行分类总结，但在我将其委托给它之前，让我先尝试一些更普通的事情。我将根据我冰箱里的食材询问一个食谱：

```csharp
string question = 
"我冰箱里有以下食材：茄子、牛奶、奶酪、彩椒。 
我可以用这些和其他基本食材做什么菜？"; 
context = await ollama.StreamCompletion(
 question, 
 context, stream => Console.Write(stream.Response)
);
```

这花了很长时间（实际上是几个小时；我有时间去购物了！），首次令牌生成（TTFT）需要几分钟。结果在这里：

Zoom

考虑到我们没有对 LLM 进行训练，并且也没有通过检索增强生成（RAG）添加任何食谱文本来通过补充 LLM 的内部表示来提高质量，我认为这个答案非常令人印象深刻。它理解了“基本食材”的含义，每个食谱都涵盖了不同的风格。它还直觉地意识到我并不需要使用我所有的食材，并且正确地确定了茄子是与众不同的食材。

我肯定有信心让它总结一个带有固定类别的银行账户，如果那是我重视的任务。Ollama 的可控性在我的 MacBook 上也令人印象深刻。作为一个额外的视角，我和历史学家/工程师 Ian Miell 谈到了他如何在一个稍微庞大一些的 128GB 机器上使用更大的 Llama2 70b 模型从提取的来源中写出历史文本。即使出现了一些非历史性的幻觉，他也觉得它令人印象深刻。

虽然开源 LLM 目前仍处于不断变化的状态，特别是在训练数据和偏见等问题上，但解决方案的成熟度显然在提高，给人们带来了对未来能力在考虑条件下的合理希望。

David 是一位常驻伦敦的专业软件开发人员，曾在 Oracle Corp. 和英国电信公司工作，并担任顾问，帮助团队以更敏捷的方式工作。他写过一本关于 UI 设计的书，自那以后一直在撰写技术文章...
阅读更多关于 David Eastman 的内容
