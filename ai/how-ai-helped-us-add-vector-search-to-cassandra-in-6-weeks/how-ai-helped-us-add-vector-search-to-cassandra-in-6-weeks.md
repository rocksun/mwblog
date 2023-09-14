<!-- 
AI 如何助力 Cassandra 六周添加向量搜索功能
https://cdn.thenewstack.io/media/2023/09/6f6c887c-aiandcoding-1024x683.
Image from Thapana_Studio on Shutterstock.jpg
-->

DataStax 必须迅速行动，添加这个基础的 AI 赋能功能。以下是 ChatGPT、Copilot 和其他 AI 工具如何帮助我们构建代码的情况。

DataStax 面临着巨大的[需求](https://hackernoon.com/how-llms-and-vector-search-have-revolutionized-building-ai-applications)，需要添加[向量搜索](https://www.datastax.com/guides/what-is-vector-search?utm_source=thenewstack&utm_medium=byline&utm_campaign=vector-search&utm_term=all-plays&utm_content=how-we-built-vector)功能来支持生成式 AI 应用程序。我们为 Cassandra 和基于 Cassandra 构建的托管服务 Astra DB 添加这一功能制定了一个非常雄心勃勃的目标。

早在 4 月份，当我问我们的产品负责人首席副总裁谁会去构建它时，他说：“为什么你不做呢？”

我和其他两名工程师着手在 6 周内，也就是 6 月 7 日[交付一个新的向量搜索实现](https://www.datastax.com/blog/introducing-vector-search-empowering-cassandra-astra-db-developers-to-build-generative-ai-applications?utm_source=thenewstack&utm_medium=byline&utm_campaign=vector-search&utm_term=all-plays&utm_content=how-we-built-vector)。

在这个关键项目中尝试过这些工具后，我确信这些工具确实极大地提高了生产力。事实上，我再也不会全部手写代码了。以下是我在使用 ChatGPT、GitHub Copilot 和其他 AI 工具进行编码时获得的经验。

## Copilot

[Copilot](https://github.com/features/copilot) 很简单：它是增强的自动完成功能。大多数时候，它会为你完成一行，或者根据上下文模式匹配完成几行。在这里，我写了一个注释，然后在新行上开始写“neighbors”。Copilot提供完成其余部分，正确地补全了第二行“neighbors”后的文本。

![](https://cdn.thenewstack.io/media/2023/09/48be07e6-image1a-e1693939176744.png)

这里有一个稍微复杂一点的测试代码示例，我开始用 mapToLong 编写循环，然后改变了数据结构，以便使用 forEach 调用方法更清晰。Copilot 照顾了我：

![](https://cdn.thenewstack.io/media/2023/09/39148475-image2a.png)

有时(这更是例外而不是规则)，它通过提供完成整个方法而让我感到惊讶：

![](https://cdn.thenewstack.io/media/2023/09/3b6e0053-image3a.png)

Copilot 有用，但由于两个原因受到限制。首先，它经调优以保守地(正确地)犯错误。它仍可能产生幻觉，但很少见；当它不知道做什么时，它不会提供完成选项。其次，它受限于需要快速地无缝集成到人类键入的短暂停顿中，这暂时排除了使用像 GPT-4 这样的重量级模型。

([另见 Max Krieger 的此推文，了解“Copilot 极致主义者”的观点](https://twitter.com/maxkriegers/status/1648036999650230272)。)

## ChatGPT

你可以尝试让 Copilot 通过注释生成代码，但对于这种用例，你几乎总是能从 [GPT-4](https://openai.com/research/gpt-4)(通过付费的 ChatGPT 或 API 访问)获得更好的结果。

如果你还没有尝试过 GPT-4，你绝对应该尝试。确实，它有时会产生幻觉，但远少于 GPT-3.5 或 [Claude](https://claude.ai/login)。确实，有时它无法解决简单的问题([这里我正在努力让它理解简单的二分查找](https://chat.openai.com/share/5b559fb8-6068-4323-bfba-3578843e2256))。但其他时候，它的表现令人震惊地好，就像这个时候，[它在第一次尝试中就找到了我的竞争条件](https://chat.openai.com/share/8ce78037-8788-4ec1-9ea2-5cd124a97a2f)。即使当它表现不佳时，拥有一个可以用貌似智能的方式响应的[橡皮鸭调试伙伴](https://en.wikipedia.org/wiki/Rubber_duck_debugging)也非常宝贵，可以保持思维状态，保持动力。

你可以用它做任何事情。或者至少是你能用文字描述的任何事情，在编程背景下，这几乎涵盖了一切。

以下是我使用 GPT-4 的一些地方:

- [关于 API 的随机问题，否则我不得不潜入源码](https://chat.openai.com/share/f6ac4b9e-0cc8-4e6b-81c4-49930c54a0a1)。这类问题最有可能产生幻觉，对于这种用例，我已经大部分切换到 [Phind](https://www.phind.com/)(见下文)。
- [微优化](https://chat.openai.com/share/90e8877f-fca8-4b18-acc3-431f29848649)。这像 Copilot，但匹配全部 Stack Overflow 内容，因为那就是(部分)它的训练数据。
- 复杂的 [Stream 流水线](https://chat.openai.com/share/89df703b-4928-44ca-baf3-fdac33c4cfaa)，因为我还不太善于把头脑中的逻辑转化为 Stream 方法调用的功能链。有时，像这个例子一样，最终结果比我们开始的要差，但这在编程中经常发生。用 GPT 探索要比一步一步打字快得多，而且更容易。缩短结果周期可以提高尝试新想法的可能性，因为实验成本更低。
- 当然，GPT 也知道 [git](https://chat.openai.com/share/4a4d2047-57fc-4b94-848e-0e7bc0eef0ba)，但你可能没有意识到它在使用 git 构建[自定义工具](https://chat.openai.com/share/ed9da883-473b-4cf1-a4b6-3aa2f7d92341)方面有多强大。与列表中的其他内容一样，这是我以前可以手动完成的事情，但有了 GPT 加速意味着现在我会创建这样的工具(以前，我通常会采用第二好的解决方案，而不是在一次性脚本上花一个小时)。

[这里是与 GPT-4 的协作中最喜欢的部分](https://chat.openai.com/share/24bc6f9f-1380-4e0d-abe9-489c1378c992)。我需要编写一个自定义类来避免 `ConcurrentHashMap<Integer，Integer>` 的盒装/拆箱造成的垃圾回收开销，而这是为 Lucene 编写的，它有严格的无外部依赖项的政策，所以我不能简单地使用像 [fastutil-concurrent-wrapper](https://github.com/trivago/fastutil-concurrent-wrapper) 这样的并发基元映射。

我与 GPT 反复多次交流，改进了它的解决方案。这段对话说明了我认为 2023 年年中使用 GPT 的几个最佳实践：

1. 在编写代码时，GPT 在封装良好的问题上表现最佳。相比之下，我在试图让它执行涉及一个类多个部分的重构时大多不成功，即使是一个小类。
2. 将建议提出为问题。“是否会更有效......?” GPT(甚至更多的是 Claude)不愿直接反驳用户。留出空间让它表示不同意见，否则可能会无意中强迫它开始产生幻觉。
3. 不要试图在大语言模型(LLM)中做每一件事。来自这次对话的最终输出仍需一些调整，但已经足够接近我想要的，手动完成会更简单快速，而不是试图让 GPT 完全正确。
4. 我通常不相信神奇的提示词 —— 最好使用直接的提示，如果 GPT 朝错误方向发展，进行纠正——但在某些地方，正确的提示词确实可以提供很大帮助。Java 中的并发编程就是这样的地方之一。GPT 的首选解决方案是简单地在所有内容上加上 synchronized 并结束。我发现，告诉它按照并发大师 [Cliff Click](https://twitter.com/cliff_click) 的风格思考会有很大帮助。最近，我也切换到使用 [Jeremy Howard 的系统提示](https://twitter.com/jeremyphoward/status/1689464587077509120)的略加编辑的版本。

看这个列表，它非常符合使用 AI 就像有无限的实习生为你效劳的经验法则。实习生在自包含的问题上表现最好，通常不愿与团队负责人相矛盾，而你自己完成这项工作通常比解释你想要的每一个细节以便实习生能做到要简单得多。(尽管我建议抵制在真实实习生身上这样做的诱惑，但对 GPT 不重要。)

## 高级数据分析

高级数据分析（Advanced Data Analysis，ADA），以前称为[代码解释器](https://openai.com/blog/chatgpt-plugins#code-interpreter)，也是 ChatGPT 的一部分，是另一个层次的，我希望它能在昨天就用于 Java。它将 GPT-4 Python 代码生成封装到类似 Jupyter 的沙盒中，并进行循环以纠正自己的错误。这里有一个例子，当我正在调查为什么我的索引代码构建了一个分区图时。

需要注意的主要问题是，当遇到意外输入时，ADA 倾向于“解决”问题是抛弃冒犯的行，这通常不是你想要的。一旦代码顺利运行到完成，它通常对自己的努力感到满意 - 你需要明确要求它包含的正常检查。一旦你告诉它要查找什么，它就会将其添加到“迭代直到成功”循环中，你就不必一遍又一遍地重复自己了。

同样值得一提的是，谣言暗示 ADA 现在正在运行比常规 GPT-4 更高级的模型，至少具有更长的上下文窗口。我现在默认使用 ADA 进行所有操作，它确实看起来有改进；唯一的缺点是有时它会在我想要 Java 时开始为我编写 Python。

## Claude

Claude 是 Anthropic 的 GPT 竞争者。在编写代码方面，Claude 大约处于 GPT 3.5 水平，明显差于GPT-4。

但是，Claude 具有 10 万 token 的上下文窗口，是 GPT-4 的 10 倍以上。(OpenAI 刚刚宣布企业版 ChatGPT 将 GPT-4 的上下文窗口增加到 32，000 个 token，仍然只有 Claude 的三分之一。)

我使用Claude进行了三件事:

1. 粘贴整个 Cassandra 代码类来帮助弄清它们的作用。
2. 上传研究论文并提出问题。
3. 同时进行两者：这是一篇研究论文；这是我的Java实现。它们有什么不同？考虑到约束 X 和 Y，这些差异是否有意义？

## Bing 和 Phind

Bing Chat 在今年早些时候推出时引起了一定关注，它仍然是免费的 GPT-4 来源(选择 “Creative” 设置)，但就这样了。我几乎完全停止使用它。微软对 Bing 的 GPT-4 版本所做的事情，使其编写代码的能力比 ChatGPT 中的版本差得多。

相反，当我需要 AI 风格的搜索时，我使用 Phind。这应该是 Bing 的样子，但出于某种原因，一个微小的创业公司在微软的旗舰项目之一上实现了执行力。Phind 已经完全取代了我在 Java、Python、git 等中的“我该如何做 X”类问题的 Google 搜索。这里是一个使用不熟悉库解决问题的[好例子](https://www.phind.com/search?cache=erlkvj4t5iznhpe1wthuv9xg)。对于这种查询， Phind 几乎总能命中要点 - 而且还有相关的来源。相比之下，Bing 至少会引用一个声称与实际不同的来源。

## Bard

我还没有找到 Bard 擅长的东西。它既不具备 GPT-4 编写代码的技能，也没有 Claude 的大上下文窗口。与此同时，它的幻觉比两者都多。

## 使编码更具生产力 - 并且更有趣

Cassandra 是一个大型且成熟的代码库，这对希望添加新功能的新人来说可能很吓人 - 即使对我来说也是如此，在管理方面花了 10 年时间。如果 AI  可以帮助我们中的任何一个人更快地行动，那就是了。ChatGPT 和相关的 AI 工具善于编写代码以解决明确定义的问题，无论是作为人类工程师设计的更大项目的一部分，还是用于一次性工具。它们在调试、绘制原型和探索不熟悉的代码方面也很有用。

简而言之，ChatGPT 和 Copilot 对于达到最后期限至关重要。根据任务的不同，这些工具使我的生产力提高 50% 至 100%。它们确实有局限性，但在不知疲倦地迭代更小的任务方面表现突出，并通过充当不知疲倦的无怨无悔的伙伴来弹出想法，帮助人类管理者保持思路。即使你有多年的编程经验，你也需要做到这一点。

最后，甚至在不考虑生产力方面的情况下，使用 AI 帮助重复部分的编码只是更有趣。这给了我继续前进的动力和新的兴奋来构建很酷的东西。我期待着使用这些工具的更高级版本，随着它们的发展和成熟。
