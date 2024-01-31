<!--
title: 自然语言处理和AI中的温度
cover: https://cdn.thenewstack.io/media/2024/01/db989bc8-temperature-ai-2-1024x576.jpg
-->

在生成式人工智能中，所谓的“温度（Temperature）”是指提高的熵。下面解释了这是什么意思，以及为什么提高温度可能导致更多的幻觉。

> 译自 [What Temperature Means in Natural Language Processing and AI](https://thenewstack.io/what-temperature-means-in-natural-language-processing-and-ai/)，作者 David Eastman。

使用 ChatGPT 的增加使得一个问题不断浮出水面，即在回答中偶尔包含明显错误的信息，这些信息已被准确描述为**幻觉**。为什么会发生这种情况，能否加以控制？

当我们研究一个简单的 [OpenAI API 查询](https://thenewstack.io/the-promise-of-riches-from-ai-wrappers/)时，我们遇到了变量**温度**。除了它可以在 0 到 1 之间，我们仅仅注意到它控制着 "响应的创造力"。以下是对这一概念的轻度技术性解释。

在继续之前，我们最好简要地记住，当一个工程思维认为 "温度" 时，他们不是在想 "这里变热了"，而更多地是在想 "熵增加"。考虑到兴奋分子额外的扭动会导致（随机的）可能性增加。

温度并不是特定于 [OpenAI](https://thenewstack.io/beyond-chatgpt-exploring-the-openai-platform/)；它更属于[自然语言处理（NLP）](https://thenewstack.io/top-5-nlp-tools-in-python-for-text-analysis-applications/)的思想。虽然[大型语言模型](https://thenewstack.io/what-is-a-large-language-model/)（LLM）代表了在给定上下文中文本生成的当前顶峰，但这种基本的能力，即推断出下一个词，几十年来一直存在于手机预测文本上。

为了理解变化的根源，让我们考虑一个简单模型如何从示例中学习。

考虑一个模型首次接收到的句子：

![Zoom](https://cdn.thenewstack.io/media/2024/01/b5a8a885-untitled-1024x111.png)

*To be or not to be.*

它理解这个句子是一串有序的单词，句号表示结束。如果这是它唯一知道的句子，它将不会做出任何合理的预测。如果你碰巧输入 "To be … "，它只会建议哈姆雷特的著名台词。

所以我们将在模型中添加一行：

![Zoom](https://cdn.thenewstack.io/media/2024/01/7fffcd25-untitled-1-1024x124.png)

*To be young again.*

将两者结合起来，我们有可能在第一个 "To be" 之后产生任何一行。我们将句号视为短语的结束，因此它可以被任一选项共享，就像前两个单词一样。

![Zoom](https://cdn.thenewstack.io/media/2024/01/1423ddf6-untitled-2-1024x244.png)

*基于前两个输入可能产生的选项。*

因此，橙色线代表一种变化。我们的模型现在理解两行。

我们必须注意，我将每个单词都视为一个可消耗的token或单元，包括句号。但单词并不是真正的离散实体；我们知道单词 "doing" 和 "done" 是相同的单词，只是在不同的时态，或者 "ships" 是 "ship" 的复数。我们还知道单词 "disengage" 是以前缀开头的 "engage"。

简而言之，单词似乎是由token组成的。在以英语为基础的模型中，[每个单词大约有 1.3 个token](https://gptforwork.com/guides/openai-gpt3-tokens)。而这对于不同的语言会有所不同。我们需要了解token的原因之一是 GPT 模型是按token计费的。因此，每个token的价格是你需要了解的事情。

## 机会有多大？

培训是一个学习token和上下文的过程，直到出现具有不同发生概率的多个选项。如果我们假设上面的简单模型已经从文本中吸收了数百个示例，它将知道 "To be frank" 和 "To be continued" 比莎士比亚 400 年前的独白更有可能发生。

如果我们围绕 "To be …" 后面的下一个词创建一个钟形曲线，我们自然会期望有些词是非常可能的，而有些词则可能性较小。在下面的图表中，一个方块代表了大量的示例。因此，不出现为选项的可能词有太少的示例参考。

让我们考虑可能的前五个选项：

![Zoom](https://cdn.thenewstack.io/media/2024/01/47b66d38-untitled-3.png)

*基于输入 "To be … " 的可能选项块*

如果我们将所有块的值相加，我们可以简单地表达任何单词被随机选中的机会。因此，“continued” 出现的机会为 14 次中的 6 次，即 42% 的可能性，而 "or" 只有 14 次中的约 1 次，即 7%。但已经很明显，有些词更不可能出现。

如果我们使曲线变平？这显然仍然会表达可能的响应为更高的概率，但它使不太常见的选项更有机会被选择：

![Zoom](https://cdn.thenewstack.io/media/2024/01/eb211601-untitled-4.png)

*更平坦的曲线显示了 "To be … " 输入后可能的选项*

这将 "continued" 的可能性改变为 36%，将 "or" 提高到 9%。因此，围绕更多种类的词被选择，赔率变得更短了。

这实际上就是增加温度所做的。它使曲线变平，给予不太可能的响应一个提升。如果温度为零，那么模型可能只会选择最高概率的token。作为提醒，当直接调用 OpenAI API 时，您可以直接输入温度范围：

```bash
curl https://api.openai.com/v1/chat/completions
  -H "Content-Type: application/json"
  -H "Authorization: Bearer xx-xxxxXX"
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "What is TheNewStack?"}],
     "temperature": 0.7
   }'
```

因为我们可能正在寻找有趣且原创性的回答，所以温度值接近1是合理的。

现在你可能会说，“但是这不会增加模型回复不真实的可能性吗？” 针对这个问题，我们需要根据任务将温度值匹配到适当的范围。这是通过区分“创造性”输出和[“事实性”输出来完成的。如果在事实性材料上使用过高的温度，我们很可能会产生可怕的幻觉](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/)。

## 温度掩盖了聊天机器人回应的来源

ChatGPT的伟大任务是让你误以为AI已经“思考”出了一个答案。实际上没有。它正在进行上述操作的更复杂版本，有着数百万个摄入的token，但仍然完全受预先构建的LLMs的指导。这就是为什么它既可以看起来很有权威，又可能是彻头彻尾的胡言乱语。

然而，正如我们在日常使用中所看到的，ChatGPT在大多数情况下表现得非常好。这是因为对于你可能有的每个问题，有人在互联网的某个地方已经直接或间接地回答过它。ChatGPT的真正任务是理解问题的上下文，并在回应中反映出来。

阅读本地报纸上的天气预报时，如果随后我利用这些信息回答一位想知道明天是否晴朗的朋友，我并不是在“剽窃”他们。报纸（或曾经是）旨在成为有效的信息来源。但显然，如果我从专家报告中摘取大段文字并将其标榜为自己的，这可能构成欺诈。

对于模型来说，将法律压力越来越多，不允许其大声回应，[使得源材料明显可见](https://arstechnica.com/tech-policy/2023/12/ny-times-sues-open-ai-microsoft-over-copyright-infringement/?utm_source=thenewstack&utm_medium=website&utm_content=inline-mention&utm_campaign=platform)。这就是为什么幻觉可能会持续存在的原因，因为温度被用于改变响应并掩盖它们的来源。奇怪的是，最初使用相同原理来打败垃圾邮件检测——通过在垃圾邮件中添加错误，最初很难将其列入黑名单。Gmail通过其庞大的规模和理解分布模式的能力克服了这一问题。

总体而言，我们认识到LLMs在社会上是积极的。最终，法律将会在培训过程的做与不做方面形成正式规范。但在那之前，将有足够的机会让温度上升，导致LLMs侵占其他创作者内容。
