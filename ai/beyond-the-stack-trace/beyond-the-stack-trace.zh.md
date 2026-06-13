长期以来，调试工作一直基于软件是确定性的这一假设。

人们认为，在相同的输入下，代码每次都应提供相同的输出。当出现问题时，你可以求助于熟悉的工具，如堆栈跟踪（stack traces）和断点，并一点一点地逐步执行代码，直到找到故障点。这个过程往往是系统化、可重复的，并基于“行为是可以重现的”这一理念。

AI系统打破了这一假设。

当你在应用程序中集成LLM时，你调用的不再是一个可预测的函数，而是一个概率系统。这意味着相同的输入每次可能提供略有不同的输出。措辞的微小变化、隐藏的上下文或温度（temperature）等模型参数都可能显著改变结果。当出现问题时，通常没有堆栈跟踪来指向明确的失败行。

看看这个简单的AI驱动功能：

```

const response = await ai.generate({
  prompt: userInput,
});

```

乍一看，它看起来和其他函数调用没什么两样，但实际上，底层的实际执行取决于多个不可见的因素，例如：

* 模型自身的概率推理
* 可能截断输入或输出的Token限制
* 模型配置
* 对话历史或注入的上下文
* 你可能无法明确看到的系统级指令

当输出错误、不完整或不一致时，传统的调试工具就会失效。日志可能显示输入和输出，但很少能捕获理解模型为何如此表现所需的完整上下文。

这就是解决这一混乱局面所需的新范式：提示词跟踪（prompt tracing）。

开发者不再仅仅依赖堆栈跟踪，而是需要捕获并分析AI请求的整个生命周期，从原始提示词（prompt）和系统指令到最终的响应和Token使用情况。正如堆栈跟踪彻底改变了传统应用程序的调试方式一样，提示词跟踪对于构建可靠的AI系统也变得至关重要。

在本文中，我们将探讨涉及AI时调试是如何变化的，以及为什么传统方法会失效。我们还将研究如何设计[使AI行为可观测的系统](https://thenewstack.io/debugging-observable-ai-systems/)，使其在实践中可重现且可调试。

## 传统调试的工作原理

在使用AI之前，调试建立在一套可靠且几乎不可见的保证之上。

其核心是确定性执行：在给定相同的输入和系统状态下，你的程序将遵循相同的执行路径并产生相同的输出。正是这种可预测性使得传统的调试工具如此有效。

## 堆栈跟踪：跟踪执行路径

当发生错误时，堆栈跟踪会为你提供调用链的精确快照。

看看下面的TypeScript代码：

```

function divide(a: number, b: number) {
  return a / b;
}

function calculate() {
  return divide(10, 0);
}

calculate();

```

这段代码的正常输出将是：

```

Error: Division by zero
    at divide (math.ts:2:10)
    at calculate (math.ts:6:10)

```

这准确地告诉你错误发生的位置、执行是如何到达该点的，以及是什么导致了失败。这使你可以一步步跟踪问题并始终如一地重现它。

## 日志：随时间观察状态

日志提供了对应用程序状态的可见性：

```

console.log("User input:", input);
console.log("Processed value:", result);

```

通过正确的日志记录，你可以跟踪变量值，识别意外的状态变化，并重建执行流程。

当与时间戳和请求ID结合使用时，日志甚至允许你调试分布式系统。

## 断点：实时检查执行

通过使用调试器，你可以暂停执行并检查程序的状态：

```

debugger;

const total = items.reduce((sum, item) => sum + item.price, 0);

```

这实现了逐步执行、检查内存中的变量，以及对逻辑错误的即时反馈。

传统调试之所以如此有效，是因为执行是可预测的：相同的输入产生相同的输出。

故障总是明确的：异常、崩溃、错误代码。一切都在完全控制之中，因为你的代码掌握着逻辑。

即使在复杂的系统中，这些原则仍然适用。你可以跟踪请求、重放它们并可靠地重现问题。

一旦你将AI引入其中，这个假设就开始崩溃，因为逻辑不再完全是你的代码，输出也不是严格可重现的，而且失败通常是隐式的，而不是显式的。

这就是传统调试开始失效的地方。

## 是什么让AI系统难以调试

当AI进入你的系统时，调试就不再仅仅是一种机械练习，而变成了一种概率调查。这意味着你不再是在跟踪一条固定的执行路径。相反，你是在分析在运行、环境甚至细微输入变化之间可能发生变化的各种行为。

这种转变引入了一种传统工具从未设计处理过的新型复杂性。

为了说明这一点，让我们看看下面的非确定性输出示例。

上面的代码只要输入相同，就应始终返回相同的结果。

```

generate("Explaincaching")

→ "Caching is a technique used to store..."
→ "Caching improves performance by storing..."
→ "It is a method of temporarily storing data..."

```

现在看看上面的代码。在上面的AI系统中，输入是相同的，但我们有多个输出。这受到模型版本变化、内部随机解码、采样策略等因素的影响。当出现问题时，情况并不总是很清楚。

## 你无法完全控制的隐藏上下文

你发送给模型的内容很少是全貌。

单个请求可能包括系统提示词、开发者指令、对话历史、检索到的上下文（RAG）和工具输出。

```

const response = await ai.generate({
  system: "You are a strict JSON generator",
  prompt: userInput,
  history: previousMessages,
});

```

即使输入完全相同，对话历史、注入的系统消息和检索到的文档的变化也会完全改变输出。

这里的问题在于，上下文在默认情况下通常不会出现在日志中。

## 外部依赖：模型是一个黑盒

与内部函数不同，LLM是托管在外部的，其版本不受你控制，由提供商静默更新，并且受到延迟和区域差异的影响。

因此，你通常不是在调试你的代码，而是在试图弄清楚一个远程概率系统在当下决定做什么。

这引入了诸如模型更新后突然出现行为变化、跨区域输出不一致或高负载下性能下降等故障模式。

## Token限制和静默截断

最容易被忽视的调试问题之一是上下文截断。

看看下面的代码：

```

const response = await ai.generate({
  prompt: largeDocument,
});

```

如果largeDocument超过了模型的上下文窗口：

* 输入的部分内容可能会被静默删除
* 系统或用户指令可能会被丢弃
* 模型可能会表现得“随机出错”
* 通常没有明确的错误，而只是输出质量下降。

最危险的AI错误不是崩溃，而是看似合理但实际上不正确的输出。

> “最危险的AI错误不是崩溃，而是看似合理但实际上不正确的输出。”

例如，忽略了关键信息的总结、虽然格式有效但在语义上错误的JSON响应，或者微妙地偏离策略的推荐系统。

这些失败不会抛出异常；它们不会出现在堆栈跟踪中，并且通常可以通过基本测试。这使得它们极难用传统工具检测出来。

## 理解“提示词跟踪”

一旦你接受了AI系统具有非确定性和高上下文依赖性的事实，接下来的问题就是如何以结构化的方式调试它们。

简单来说，答案是从执行跟踪转向交互跟踪。

提示词跟踪是对所有影响AI响应的因素的完整记录。它通常以一种可以检查、重放和比较的方式进行捕获。

但什么是提示词跟踪？它不仅仅是用户输入。它是AI请求生命周期的完整快照，包括：

* 用户输入
* 系统指令
* 开发者指令
* 对话历史
* 检索到的上下文
* 模型配置

用以下术语来理解：

* 堆栈跟踪：代码是如何执行的
* 提示词跟踪：为什么AI会产生这个输出

> “堆栈跟踪：代码是如何执行的。提示词跟踪：为什么AI会产生这个输出”

提示词跟踪的目标很简单：使AI行为像传统代码执行一样可观测。

有了适当的提示词跟踪，你可以重放确切的故障、比较不同模型版本的输出、检测提示词中的回归、优化成本和Token使用情况，并最终理解输出为何随时间发生变化。

话虽如此，提示词跟踪很难做到位。与堆栈跟踪不同，提示词跟踪不会自动生成。你必须明确设计你的系统来捕获它们。

最常见的挑战包括日志中缺少系统提示词、丢失对话历史、不完整的检索日志以及没有跟踪模型版本的变化。

如果没有结构化的跟踪，调试基本上就变成了猜测。

以下是AI请求生命周期的剖析。

```

json
{
  "input": "Write a summary of this article",
  "systemPrompt": "You are a concise technical assistant",
  "chatHistory": [
    "User: Explain caching",
    "Assistant: Caching is..."
  ],
  "retrievedContext": [
    "Article: Caching improves performance by..."
  ],
  "modelConfig": {
    "model": "gpt-4o-mini",
    "temperature": 0.7,
    "maxTokens": 500
  },
  "output": "Caching is a technique used to store..."
}

```

以上就是一个完整的提示词跟踪的样子。这种结构允许你回答关键的调试问题，例如：

* 检索是否返回了不相关的数据？
* 系统提示词是否错误地影响了输出？
* 相关的上下文是否缺失或被截断？

## 为什么提示词跟踪很难做到位

与堆栈跟踪不同，提示词跟踪不会自动生成。你必须明确设计你的系统来捕获它们。

常见挑战：

1. 日志中缺少系统提示词

2. 丢失对话历史

3. 不完整的检索日志

4. 未记录Token截断

如果没有结构化的跟踪，调试就变成了猜测。

## 提示词跟踪的目标

目标很简单：使AI行为像传统代码执行一样可观测。

有了适当的提示词跟踪，你可以：

* 重放确切的故障
* 比较不同模型版本的输出
* 检测提示词中的回归
* 优化成本和Token使用情况

## AI故障剖析

在传统系统中，故障通常是明显的：异常、崩溃、失败的请求。在AI系统中，故障通常是微妙的、静默的，并且更难分类。

为了有效地调试，你需要了解不同类型的AI故障以及它们如何在实际系统中表现出来。

### 错误输出 vs 意外输出

并非所有的故障都是平等的。

### 错误输出

模型产生了明显的错误结果：

输入：“2+2”

输出：“5”

容易检测。容易标记。

### 意外输出

模型产生了有效但非预期的结果：

输入：“用一句话总结这篇文章”

输出：“这篇文章讨论了缓存、性能和系统设计的多个方面”

从技术上讲，这是正确的，但它违反了约束，而大多数AI Bug都存在于这里。

### 静默失败

这些输出看起来是正确的，通过了基本验证，但在语义上是错误的。

输入：“将用户数据提取为JSON”

输出：

```

{
  "name": "John",
  "email": "john@example.com"
}

```

这个输出看起来没问题，但电子邮件地址可能是幻觉出来的，可能缺少必填字段，其他数据也可能与源不匹配。没有异常，没有错误，只是在生产环境中行为不当。

### 上下文失败（输入丢失或损坏）

AI对上下文极其敏感。

如果你的提示词跟踪看起来像这样，模型将被迫进行猜测：

```

{
  input: "Summarize the report",
  retrievedContext: []
}

```

常见原因包括检索（RAG）未返回任何内容、上下文超过Token限制而被截断，以及对话历史丢失。

### 提示词失调导致的指令漂移

提示词的微小变化会导致巨大的行为转变。

// 版本A

“你是一个乐于助人的助手”

// 版本B

“你是一个严格的JSON生成器”

如果这种变化是无意的，输出往往会失去结构、忽略约束，甚至改变语气或格式。

如果没有提示词跟踪，这极难检测。

### 延迟和超时故障

AI API引入了[网络和推理延迟](https://thenewstack.io/p99-conf-3-ways-to-squash-application-latency/)。这会减慢负载下的响应速度，并导致流式设置中的部分响应。

```

const controller = new AbortController();
const timeoutId = setTimeout(() => controller.abort(), 3000);

try {
const response = await ai.generate({
prompt,
signal: controller.signal
});
clearTimeout(timeoutId);
} catch (err) {
if (err.name === 'AbortError') {
// 处理超时
}
}

```

如果模型速度缓慢，你可能会得到回退响应。

### 在生产中捕获提示词跟踪

我们已经确定，AI[系统失败的方式](https://thenewstack.io/ai-agents-batch-size-gravity/)是传统调试工具无法完全解释的。自然的下一步不仅仅是理解提示词跟踪，而是以在生产系统中有效的方式捕获它们。没有被记录下来的提示词跟踪实际上就是丢失了。

目标是使AI调用具有可观测性。在典型的后端中，你可能会这样记录请求：

```

logger.info({
  endpoint: "/api/users",
  payload: req.body,
});

```

对于AI系统，这还不够。

你需要记录完整的提示词、系统指令、上下文、模型配置、输出、Token使用情况和延迟。

从上下文来看，这相当于从“我们收到了什么请求？”升级到“模型到底看到了什么并产生了什么？”

### 设计提示词跟踪模式

结构化跟踪至关重要。避免原始日志并使用一致的模式：

```

type PromptTrace = {
  id: string;
  timestamp: number;

  input: string;
  systemPrompt?: string;
  history?: string[];

  context?: string[];

  model: string;
  temperature: number;
  maxTokens: number;

  output: string;

  tokens?: {
    input: number;
    output: number;
    total: number;
  };

  latencyMs: number;
  cost?: number;
};

```

这使你可以查询跟踪、比较运行情况并系统地调试故障。

## 封装你的AI调用（中间件模式）

永远不要直接从业务逻辑中调用AI提供商。

相反，要包装它：

```

async function generateWithTrace(prompt: string): Promise&lt;string> {
  const start = Date.now();

  const response = await ai.generate({
    prompt,
  });

  const latency = Date.now() - start;

  const trace = {
    id: crypto.randomUUID(),
    timestamp: Date.now(),
    input: prompt,
    output: response.text,
    model: "gpt-4o-mini",
    temperature: 0.7,
    maxTokens: 500,
    latencyMs: latency,
  };

  await saveTrace(trace);

  return response.text;
}

```

现在，每个AI调用都被记录、可追踪且可重现。

## 捕获Token使用量和成本

成本可视化至关重要。

```

function estimateCost(tokens: number) {
  const pricePer1kTokens = 0.002;
  return (tokens / 1000) * pricePer1kTokens;
}

```

现在，让我们扩展跟踪：

```

interface PromptTrace {
  prompt: string;
  response: string;
  tokens: { prompt: number; completion: number; total: number };
  cost: number;
}
const trace: PromptTrace = {
  prompt: userInput,
  response: assistantReply,
  tokens: response.usage,
  cost: estimateCost(response.usage.total)// 使用estimateCost函数
};

```

在这一点上，你可以调试为什么成本在增加、哪些端点昂贵，以及哪些提示词效率低下。

## 构建可调试的AI系统

捕获提示词跟踪只是基础。作为开发者，你需要能够利用这些跟踪进行有效调试的系统。

可调试的AI系统侧重于：

* 可重现性：重放完整的提示词跟踪以调查故障
* 版本控制：像对待代码一样对待提示词并跟踪更改
* 比较：比较不同的输出以检测回归或行为变化
* 隔离：删除变量（历史记录、上下文和配置）以找到根本原因
* 验证：添加护栏以捕获静默或错误的输出
* 韧性：为故障实施回退和重试
* 控制：减少随机性

这里的核心思想是，虽然你无法消除AI的不确定性，但你可以使它变得可观测、可测试和可控。

> “虽然你无法消除AI的不确定性，但你可以使它变得可观测、可测试和可控。”

调试AI系统迫使我们从根本上转变对软件可靠性整体的思考方式。

多年来，我们一直依赖于确定性行为，例如明确的输入、可预测的输出以及直接指向失败源的堆栈跟踪。一旦引入AI，这些假设就不再成立了。失败不再仅仅是关于破碎的代码，而是更多地关于失调的上下文、隐藏的输入和概率行为。

这就是传统调试工具不足的原因，而引入提示词跟踪改变了这一点。通过从输入、上下文、配置和输出捕获AI请求的完整生命周期，你完全从盲目的猜测转变为具备可见性。你获得了重放故障、跨变更比较行为的能力，并能系统地改进你的系统，而不是盲目地调整提示词。