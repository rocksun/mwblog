<!--
title: 为什么大语言模型不会取代人类程序员
cover: https://cdn.thenewstack.io/media/2024/02/179755fc-philipp-katzenberger-iijruoerocq-unsplash-1024x683.jpg
-->

对于软件开发界来说，大语言模型的前景是将编码者转变为架构师。不过，并非所有 LLM 都一样。

> 译自 [Why Large Language Models Won’t Replace Human Coders](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/)，作者 Peter Schneider 是芬兰埃斯波总部的全球软件公司 Qt Group 的高级产品经理。

生成式人工智能是否会取代人类程序员？可能不会。不过，使用 GenAI 的人可能会。但是，由于今天混合了如此多的大型语言模型（LLMs），结果会有所不同。

如果你在努力跟上所有LLMs的话，你并不是唯一一个。我们正在目睹对LLMs的热情武装竞赛。仅 Google 的 GenAI 产品就变得丰富多样——[其最新的开放模型称为 Gemma](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/)，是迅速发生的LLM缩小的最新例子（是时候把它们称为[小语言模型](https://thenewstack.io/the-rise-of-small-language-models/)了吗？）。

对于 DevOps 社区而言，更为相关的是我们正在看到其他专门针对代码生成的LLMs的快速发展，比如 [Meta](https://about.meta.com/?utm_content=inline-mention) [最近更新的 Code Llama 70B](https://ai.meta.com/blog/code-llama-large-language-model-coding/)。自然而然，GenAI 已经让不少开发者感到不安。[最近一项研究中近一半的](https://www.pluralsight.com/resource-center/guides/new-developer-research-paper?exp=2)开发者表达了对于在GenAI世界中成功的担忧，担心自己的当前技术技能是否足够。

但是，这种担忧是否真的有根据呢？人类程序员的死亡可能被夸大了。人类甚至可能有更多的时间来为GenAI主导的世界做准备，比他们意识到的要多。

事实上，一个开发者应该问的更合适的问题不是“GenAI会取代我的工作吗？”而是“我应该使用哪个LLM？”

## 对于编码而言太大而无法成功

对于软件开发世界而言，LLMs的承诺是将编码者转变为架构师。然而，并非所有的LLMs都是平等的，值得探讨的是为什么会出现更小型的LLMs。

越强大的主流模型，如 GPT-4 和 Claude 2，仍然几乎无法解决[不到 5% 的真实世界 GitHub 问题](https://arxiv.org/abs/2310.06770)。ChatGPT 仍然经常产生幻觉：虚假变量，甚至是已经淘汰了十多年的概念。此外，它使得胡言乱语看起来非常美好。你可以试着通过“提示工程”摆脱这种胡言乱语，但对于有益的上下文量存在一个甜蜜点——太多会导致更多混乱和随机的结果，以及更多的处理能力开销。

关于编码的 LLM 的更大的担忧在于信任。历史上，主流的 LLM 无差别地像一个大数字吸尘器一样吸取在线的一切，但并没有透明度说明它们的数据来源。如果公司发布的代码中有百分之一是另一个组织的受版权保护的代码，那就是一个问题。你可以想象一个噩梦般的召回情景，在这种情况下，发货的产品没有能力通过空中进行调整以排除可疑代码。

然而，LLM 的格局正在迅速改变。

## LLM 进行编码是否足够专业化？

当 Meta 在今年早些时候宣布更新其 [Code Llama 70B](https://venturebeat.com/ai/meta-releases-code-llama-70b-an-open-source-behemoth-to-rival-private-ai-development/) 时，这感觉像是对主流 LLM 在编码方面缺乏关注的一种受欢迎的尝试。它提供了三种不同的规模：70 亿、130 亿和340 亿参数。它还在 5000 亿个代码和与代码相关的数据上进行了训练，包含一个 100,000 个标记的大上下文窗口。

最令人兴奋的其中之一，在理论上是 Code Llama Python，这是 Code Llama 专为 Python 特化的版本，主要是因为它代表了 LLM 未来的演进。与 Meta 的大型科技同行一些模型不同，这个模型专注于编程一种特定语言，训练了大约 1000 亿个额外的 Python 代码标记。这种针对特定用例的定制模型水平正是行业所需要的。

需要强调的是 "在理论上令人兴奋"，因为目前还不清楚像 Code Llama 这样的东西实际上对开发人员有多大帮助。跳到 Reddit 上，[初步的评价](https://www.reddit.com/r/LocalLLaMA/comments/1agcji6/how_is_codellama_70b_for_you_guys/)似乎是该模型引起了对问题的不满，其中包括复杂的提示格式、过于严格的防护栏以及重要的幻觉。最后一点是另一个令人警醒的提醒，即任何模型只能像它所训练的数据一样好。

不管有缺陷与否，Meta 的定制 LLM 方法引起了重要关注，即大型语言模型并不是在 AI 辅助代码生成中成功的唯一途径。我们看到行业对专门用于编码的更小、更专注的 LLM 正在聚集动力，例如 BigCode、Codegen 和 CodeAlpaca。StarCoder 是另一个例子，尽管大小仅为 155 亿参数，[但在评估基准中被发现胜过了像 PaLM、LaMDA 和 LLaMA 这样的最大模型](https://huggingface.co/blog/starcoder)。

这些选项各有利弊，但最重要的是，相比较而言，规模较小的模型将会比较安全。如果你在使用 C++ 进行编码，你是否真的需要你的 LLM 充斥着无关紧要的知识，比如，“美国第三任总统是谁？” 数据池越小，保持相关性就越容易，模型的训练成本也就越低，你也越不可能无意中窃取他人的版权数据。

2024 年的 DevOps 团队最好彻底研究市场上所有可用的 LLM 选项，而不是默认选择最显眼的那些。甚至可能值得为不同的用例使用多个模型。

但回到眼前的根本问题...

## GenAI 会取代人类吗？

这些 GenAI 工具中，是否有可能成为真正程序员的替代品？除非模型提供的编码答案的准确性增加到可接受的误差范围内（即 98-100%），否则可能不会。

然而，就让我们举个假设来论证，假设 GenAI 真的达到了这个误差范围。这是否意味着软件工程的角色将会转变，你只需要审查和验证由人工智能生成的代码而不是编写它？如果参考[四目原则](https://www.openriskmanual.org/wiki/Four_Eyes_Principle)，这样的假设可能会被证明是错误的。四目原则是内部风险控制的最重要机制之一，要求任何具有实质性风险的活动（如软件发布）都必须由第二个、独立的、有能力的个体进行审查和双重检查。除非人工智能被重新分类为独立而有能力的生命形式，否则它不应该很快成为方程式中的一双眼睛。

如果有一天 GenAI 能够进行端到端的开发并构建人机界面，那不会是在不久的将来。大型语言模型可以对文本和图像的元素进行足够好的交互。甚至有一些[工具可以将网页设计转换为前端代码](https://thenewstack.io/locofy-launches-large-design-model-to-turn-designs-to-code/)。然而，与编码相比，AI 单独承担与图形和 UI/UX 工作流相关的设计要困难得多（尽管不是不可能的）。编码只是开发的一部分。其余部分是投资于某种新颖的东西，弄清楚受众是谁，将想法转化为可构建的东西，并进行打磨。这就是人类因素的作用所在。

无论 LLM 的表现如何出色，对程序员来说，一个原则应该始终如一：像对待自己的代码一样对待每一行代码。进行同行评审，并问问你的同事，“这是好代码吗？”永远不要盲目相信它。
