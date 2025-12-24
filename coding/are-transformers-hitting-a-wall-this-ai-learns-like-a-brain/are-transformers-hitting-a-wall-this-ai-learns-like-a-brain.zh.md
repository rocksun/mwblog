[Pathway](https://pathway.com/) 团队认为，八年前开发的 Transformer 架构已经达到了极限，任何计算量都无法逾越。而且，目前也没有可持续其运行的计算能力。此外，它还缺乏时间推理和持续学习的能力。

因此，正如 [Pathway 在 9 月份发表的一篇研究论文](https://arxiv.org/abs/2509.26507)以及我们在 [AWS re:Invent](https://reinvent.awsevents.com/on-demand) 采访中所讨论的，该公司正在构建一个基于神经元动力学的后 Transformer 时代前沿模型，并以龙为灵感——一个名为“雏龙（Dragon Hatchling）”的架构，其灵感来源于 20 瓦特的人脑。

Pathway 首席执行官 Zuzanna Stamirowska 表示：“神经元彼此连接并相互交流。一旦有新的信息进入系统——并且它可能像人类一样随着时间持续流动——感兴趣的神经元就会被激活，而与它们连接的神经元也可能随之一起激活。”

神经元一起激活，整合了赫布学习——即“一起激活的神经元会连接在一起”的概念。而那一点点信息是什么？Pathway 称之为稀疏激活；这是理解该公司方法的关键。根据我之前引用的研究论文，这意味着在雏龙模型中，大约 5% 的神经连接会被激活。其余 95% 保持静默。

## Transformer 架构的统治地位和局限性

Transformer 架构通过[注意力机制](https://thenewstack.io/introduction-to-llms/)为从 [GPT](https://thenewstack.io/gpt-5-a-choose-your-own-adventure-for-frontend-developers/) 到 [Claude](https://thenewstack.io/anthropics-new-claude-opus-4-5-reclaims-the-coding-crown-from-gemini-3/) 的大型语言模型提供支持。这些机制允许模型权衡句子或文档中不同词语的重要性，有助于处理和管理词语之间的上下文和关系。

Transformer 技术取得了巨大成就，影响着我们的生活和工作方式。只是它的功耗是不可持续的，而且其性能提升也日益减弱。

考虑 Transformer 在训练过程中学习的方式。它使用[梯度下降](https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent)法，看到模式数千甚至数百万次。这个过程需要一遍又一遍的重复，直到系统理解一个小孩子或任何人类只需一次经验就能学会的东西。

“你小时候需要尝多少次肥皂？” Stamirowska 问道，“一次，最多两次。但对于 Transformer 模型来说，要尝到肥皂的味道，它真的需要成千上万次，甚至数百万次地改变模型中的权重，才能说‘哦，肥皂是这个味道。’”

## Transformer 的时间盲点问题

Stamirowska 表示，当前的架构存在扩展无法解决的局限性。

其中一个问题是时间盲点。“从定义上讲，Transformer 没有时间概念，”她说，“它们看不到事件序列，而这些序列通常会引导我们得出结论，比如，某件事是好的，某件事是坏的。”

例如，在训练模型时，会收集大量数据，然后数据会经历一个类似于搅拌机的处理过程，然后才进行训练。

这就是棘手的地方。训练是并行完成的。所有时间数据都被移除。没有排序，只有并行。所有标记（token）都是同时被查看的，而不是按时间顺序。目标是：最大化吞吐量。缺点是：为了速度，时间的概念成为模型不考虑的一个维度。

Stamirowska 说：“对于任何涉及时间推理的应用——从市场预测到系统监控——这都是一个根本性的缺陷。”

## 记忆和持续学习如何挑战大型语言模型

然后是记忆问题。持续学习不像人类学习那样受到支持。你知道热炉会烫伤你吗？为什么？我的生物系统告诉我。

“LLM Transformer 无法整合记忆和时间。就像，无法随着时间学习和泛化。它们想这么做。”

而且这一切都效率极低。

Transformer 模型通过梯度下降学习。每一次学习都是渐进的。一个孩子只需学习一次就能理解的事情，它可能需要 10,000 份文档才能学会。

Pathway 的方法结合神经科学的背景来使用记忆。这与 Transformer 模型的学习形式不同。

Stamirowska 说：“如果两个神经元被激活，它们之间的连接就会变得更强，对吗？而这些连接实际上就是系统的记忆。”

时间结构被保留而不是丢弃。结果是一个类似于大脑的系统，被称为后 Transformer 架构，它在 GPU 规模上运行，并且正如 Stamirowska 所说，其性能“实际上达到了 Transformer 的水平”。

## Pathway 雏龙架构介绍

Pathway 拥有一支具有成熟人工智能血统的团队。首席技术官 Jan Chorowski 曾与诺贝尔奖获得者 Geoffrey Hinton 合作。Chorowski 是最早将注意力机制应用于语音识别的人之一，他的研究与注意力机制的兴起以及该领域的后续发展不谋而合。

Adrian Kosowski 领导 Pathway 的研发工作。Kosowski 是一位量子物理学家、计算机科学家和数学家，在复杂系统方面拥有专业知识。

Stamirowska 曾在巴黎复杂系统研究所工作，将粒子动力学应用于预测问题，这与他们通过学习机制所追求的方法相吻合。

Pathway 构建了一个流处理框架，在 GitHub 上获得了超过 10 万颗星。Stamirowska 表示，WhatsApp 和 NATO 等组织都在使用该人工智能平台。

Pathway 的模型名称以“龙”命名。该公司将其架构称为“雏龙（Dragon Hatchlings）”，因为龙需要一个巢穴。Pathway 的龙巢拥有所有“雏龙”的连接器。

雏龙的巢穴由 [Pathway 的实时数据框架](https://github.com/pathwaycom/pathway)提供支持，这是一个用于流处理、实时分析、大型语言模型 (LLM) 管道和检索增强生成 (RAG) 的 Python ETL（提取、转换、加载）框架。Stamirowska 表示，它是一个使用 [Apache Spark](https://thenewstack.io/is-apache-spark-too-costly-an-aws-engineer-tells-his-story/) 的增量数据处理引擎，可以使用相同的 Python API 处理低延迟流。

数据科学家可以用 Python 编写代码，无论数据以何种速度流入系统，这些代码都会在增量数据处理引擎上被翻译成 Rust。

她表示，它堪比 [Apache Flink](https://thenewstack.io/building-real-enterprise-ai-agents-with-apache-flink/)，但更像是加强版 Apache Spark。这也是他们的平台将在企业环境中获得认可的方式。

巢穴已备。现在是雏龙孵化的时候了。

雏龙架构将记忆作为模型的一部分。相比之下，Transformer 架构将记忆分离。整个模型不会被遍历，只有适用的神经连接器会被遍历。而且它不会遗忘：例如，添加一个电子表格，模型就会记住它。

Pathway 的架构反映了过去十年中出现的内存架构创新。[Victor Szczerba](https://www.linkedin.com/in/victorszczerba/) 现为 Pathway 团队成员，他曾领导 [SAP](https://www.sap.com/index.html?utm_content=inline+mention) HANA 内存数据库的市场推广。

Stamirowska 说：“状态实际上内置在平台中……它内置于学习本身的地图中，因为它保存在突触连接上。所以，就像 Transformer 从定义上就具有记忆一样。我们天生就拥有这种能力。”

## 受神经科学启发的节能数据处理方法

在我们的采访中，Stamirowska 还提到了其他一些概念，关于传统 Transformer 如何通过不断激活数百万和数十亿参数来消耗大量能量。

Pathway 的处理方式略有不同。它依赖神经连接，通过其内存能力实现效率。

她说：“因此，当你激活你需要的连接和神经元时，你不会总是激活巨大的、密集的矩阵。你可能拥有一个相当大的模型，因为你可以在结构中存储相当多的信息，但你只使用其中非常微小的一部分。”

Pathway 的方法将人工智能的进展思维推向超越其 Transformer 根源的境界。

总而言之，Pathway 的方法是数据高效的。它提供时间推理并使用极低的能耗（想想神经元激活与数据中心兆瓦的对比）。模型即记忆。它还可以根据为特定概念建立的连接进行解释。

那么权衡呢？有很多。首先，Transformer 凭借其八年的历史确实具有优势。关于基础设施、模型和工具生态系统，可以写很多东西。相比之下，雏龙技术是一种与基于 Transformer 的系统不同类型的架构。

## Transformer 时代之后的人工智能未来

Transformer 可能浪费，但模式匹配有着成功的记录。直到最近，关于不仅仅是 Transformer 的话题才开始转变。

人们是否有改变的意愿？有一些迹象表明。正如 Stamirowska 所说，“对于一位人工智能研究员来说，说他或她不研究 Transformer 是非常困难的……直到大约两个月前，这确实不流行。”

在这一点上，这更多地成为了一个哲学问题。如果基于 Transformer 的方法真的不可持续，那么人工智能的未来又将如何？

Transformer 时代带来了巨大的进步，但也创造了一场永不满足的熊熊烈火。或许我们真的需要驾驭雏龙，翱翔于熔岩景观之上。