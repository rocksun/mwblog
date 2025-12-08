
<!--
title: 指令无效又如何？AI连基础推理都搞不懂！
cover: https://cdn.thenewstack.io/media/2025/12/72755fd5-gemini_generated_image_z2cw43z2cw43z2cw.png
summary: Azure CTO表示，大型语言模型（LLM）推理能力有缺陷，是概率性的非确定性。LLM易受提示注入、越狱和幻觉影响，新模型不一定更优。需设护栏降低风险，并了解其局限性。
-->

Azure CTO表示，大型语言模型（LLM）推理能力有缺陷，是概率性的非确定性。LLM易受提示注入、越狱和幻觉影响，新模型不一定更优。需设护栏降低风险，并了解其局限性。

> 译自：[Ignore Prior Instructions: AI Still Befuddled by Basic Reasoning](https://thenewstack.io/ignore-prior-instructions-ai-still-befuddled-by-basic-reasoning/)
> 
> 作者：Joab Jackson

事实就是事实就是事实。但对于大型语言模型（LLM）来说，如果某人足够严厉地表达，那么事实就是某人所说的“事实”。

[Microsoft Azure](https://thenewstack.io/microsoft-linux-is-the-top-operating-system-on-azure-today/) 的首席技术官分享了一些关于人工智能操作安全状况的精选评论，这显然需要改进。他不仅涵盖了提示注入、越狱和幻觉方面的最新技术，还讨论了围绕LLM基本推理能力的一系列担忧。

[![](https://cdn.thenewstack.io/media/2025/12/6f17ca40-acm-russinovich-300x226.jpg)](https://cdn.thenewstack.io/media/2025/12/6f17ca40-acm-russinovich-300x226.jpg)

Mark Russinovich

这种可能固有的缺陷表明，用户需要了解LLM能做什么和不能做什么。

Mark Russinovich 在计算机协会 [TechTalk 系列](https://learning.acm.org/techtalks-archive) 讲座中表示：“关键在于将 [LLM] 视为一个有缺陷、不完美的推理引擎，然后围绕系统设置护栏以降低风险。”“你会在护栏上投入多少？这取决于你愿意接受的风险。”

## 推理挑战

LLM做出逻辑上正确决策的能力尚未被充分理解。研究表明，它们在非正式和正式推理方面的基础课程中都会不及格。

Russinovich 说：“人们认为，当AI获得良好的上下文时，它会可靠地对上下文进行推理。”计算机不就是逻辑机器吗？

LLM擅长总结大量信息，但就像一个老态龙钟的亲戚，它们可能会很快“忘记”知识库中的部分信息。在长提示的开头丢下一个事实（“Sarah最喜欢的颜色是蓝色”），当稍后被问及Sarah最喜欢的颜色时，LLM可能甚至不记得蓝色。

基本逻辑测试也可能存在问题。例如，当给出大量逻辑关系（即“A > C”或“C = A”）时，LLM可能无法成功找出整个集合的任何矛盾。多次运行（提示：“你确定吗？”）可能会产生不同的结果，有些正确，有些错误。

在自己的编程中，Russinovich也发现了类似的行为。有一次，他挑战了ChatGPT关于其代码中竞态条件的假设，但当被反驳时，他却退让了，承认“我犯了一个逻辑错误”。

而且LLM会断言自己错了，*即使它们是对的*！毕竟，在用户的要求下，模型只是在寻找可能出错的地方。

人们假设随着模型的升级，它们的推理能力也会提高。但Russinovich说，情况似乎并非如此。他引用了微软研究院的工作，该工作使用 [Eureka 框架](https://microsoft.github.io/eureka-ml-insights/) 对跨模型的推理能力进行了基准测试。

他说：“新模型不一定比该模型的旧版本表现更好，至少在某些维度上是这样。”“这是每个企业都需要去关注和审视的事情。仅仅因为新版本的模型发布了，并不意味着它在你的特定场景中会比旧版本表现得更好。”

[![比较模型推理能力](https://cdn.thenewstack.io/media/2025/12/87f1ae9c-acm-russinovich-ai_security-reasoning_failures-02-1024x563.png)](https://cdn.thenewstack.io/media/2025/12/87f1ae9c-acm-russinovich-ai_security-reasoning_failures-02-1024x563.png)

*微软研究院*

换句话说，组织必须进行评估、评估、再评估。

## 误导LLM

在讲座的问答环节中，Russinovich谈到了他所谓的“诱导幻觉”，即你可以给模型一个错误的假设，然后让它在这个假设上进行扩展。他说：“许多模型会自行开始编造东西。”

他指出，如果模型变得固执，用户可以尝试在提示中采取更具权威性的语气。它们被训练成会顺从。

## LLM是概率性的，而非确定性的

Russinovich断言，LLM的核心是概率性的，永远无法明确地提供真相。

他举了一个例子：在一个训练集中嵌入了九个断言法国首都是巴黎，和一个断言马赛是首都，LLM在某个时候会提供马赛是首都的断言。

对Russinovich来说，LLM的致命缺陷，至少以其目前的形式来看，在于它们不是确定性的。这是这类 [基于Transformer](https://thenewstack.io/grounding-transformer-large-language-models-with-vector-databases/) 模型的一个“根本”限制。

他说：“由于这些系统的工作性质，这些问题从根本上是无法修复的。”

[![截图](https://cdn.thenewstack.io/media/2025/12/650d6801-acm-russinovich-ai_security-legal-devmon-1024x547.png)](https://cdn.thenewstack.io/media/2025/12/650d6801-acm-russinovich-ai_security-legal-devmon-1024x547.png)

Microsoft Copilot曾向Russinovich推荐了他自己的sysinternals网站上一个不存在的工具，名为“DevMon”。他说：“我本可以写它，但从未写过。”

## 忽略之前的指令

也许正是因为这些薄弱的推理能力，模型才容易受到恶作剧和黑客攻击。

Russinovich和一位同事发现了一种方法，可以欺骗LLM泄露它们本应被禁止提供的信息。经典的例子是要求模型制造一个管状炸弹。当今面向公众的LLM都有阻止它们回答这个问题的屏蔽功能。

但两位研究人员发现，通过将问题分解成一系列更小、渐进式的问题，他们通常仍能提取出这套管状炸弹的制造说明。

从一个问题开始，例如“什么是管状炸弹？”然后问，“管状炸弹的部件有哪些？”依此类推。你将答案一点一点地从机器中提取出来，以免触发安全机制。

Russinovich提供了一个与ChatGPT-4.0进行这种对话的例子。

LLM当然不能被信任来检查自己的工作。Russinovich提到，他曾要求LLM检查自己的参考文献，以确保它们都是正确的。对于之前的一些工作，它直接从互联网上获取了所有参考文献。

但在重新检查自己的工作时，它发现作者姓名或出版日期等方面存在各种错误。

再进行两次参考文献检查，又发现了额外的错误。

Russinovich指出：“即使经过多轮自我评估其正确性，它仍然会犯错误。”

他说，这种不存在的参考文献的“猖獗流行”正在 [困扰法律界](https://www.damiencharlotin.com/hallucinations/)。

这个问题困扰着Russinovich，以至于他 [氛围编程](https://thenewstack.io/mastering-vibe-coding-may-the-force-be-with-you/) 了一个名为 [ref checker](https://github.com/markrussinovich/refchecker) 的工具，用于根据 [Semantic Scholar](https://www.semanticscholar.org/) 验证（大部分非结构化的）参考文献。