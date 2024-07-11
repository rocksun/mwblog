
<!--
title: 2024年云端AI工程的三大趋势
cover: https://cdn.thenewstack.io/media/2024/07/8a745e85-george-c-hsyq2hk91lo-unsplash.jpg
-->

AI 工程师的三大关键趋势包括：使用低代码或无代码工具构建 AI 代理，以及结合 AI 模态。

> 译自 [3 Key Trends for AI Engineering in the Cloud in 2024](https://thenewstack.io/3-key-trends-for-ai-engineering-in-the-cloud-in-2024/)，作者 Dan Rowinski。

过去 20 年的创新为我们带来了转折点，创造了全新的工作类别。想想 2006 年 AWS 推出后云架构师和开发人员的兴起，iPhone 和 Android 兴起后的移动开发人员，当我们终于拥有足够的数据和计算能力来使神经网络发挥作用时，机器学习工程师的出现，以及这三种趋势融合后数据科学家的出现。

> “如果你想在 18 个月前成为一名 AI 开发人员，你需要克服很大的障碍。[...] 现在我们已经到了一个阶段，只要有一个想法，你就可以在午餐时间实现它。”
>
> – Simon Margolis，SADA 的 AI 和 ML 副 CTO

沿着这条演变路径，我们可能已经到达了另一个转折点：AI 工程师。AI 工程师在过去几年中开始流行，并且处于使用 [大型语言模型和相关工具](https://thenewstack.io/top-5-ai-engineering-trends-of-2023/) 来构建生成式 AI 聊天机器人、代理和其他功能的最前沿。

随着基础模型和 AI 工程的成熟，一些趋势开始出现。我们与 [Simon Margolis](https://www.linkedin.com/in/smargolis/)，[SADA](https://sada.com/) 的 AI 和 ML 副 CTO（一家 Google Cloud 供应商）进行了交谈，了解他们在当前 AI 工程领域看到了什么，以及我们接下来可能会看到什么。

“这取决于你在生成式 AI 的整体采用曲线上处于什么位置，”Margolis 说。“有些人还在试用，刚开始接触，而有些人早在 ChatGPT 成为家喻户晓的名字之前就在做生成式 AI 工作。我认为，人们在这个范围内的位置与他们的主要趋势有很大关系。”

总的来说，Margolis 确定了 2024 年年中 AI 工程师的三个关键趋势：1) 能够使用低代码或无代码或技术知识构建 [AI 代理](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/)；2) 结合 AI 模式，例如机器学习和生成式 AI；3) 使用生成式 AI 来帮助构建生成式 AI 代理。

## 无需代码构建 AI 代理

两个主要的生成式 AI 平台，Google Cloud 和 OpenAI，一直在努力让 AI 工程师更容易构建 AI 代理，而无需过多地关注基础模型或向量数据库本身。两者都推出了构建代理的工具，包括 Google Cloud 的 [Vertex AI](https://thenewstack.io/an-introduction-to-google-vertex-ai-automl-training-and-inference/) 中的 Agent Builder 和 OpenAI 的 [GPTs](https://thenewstack.io/getting-started-with-openais-gpt-builder-and-how-it-uses-rag/)。

“在早期采用者方面，我们看到的一个最大增长点是能够构建生成式代理，而无需具备深厚的技术知识，”Margolis 说。“而两年前，你需要对诸如 Transformer 和 RAG [[检索增强生成](https://thenewstack.io/freshen-up-llms-with-retrieval-augmented-generation/)] 之类的东西非常了解，并且需要进行大量深奥的技术工作。”

Margolis 指出，虽然在构建代理方面存在一些边缘玩家，但他主要只在野外看到了 Agent Builder 和 GPTs。

> “有了像 Agent Builder 和 GPTs 这样的东西，你不需要是 AI 工程师才能做到这一点。”

能够使用较少的技术知识构建代理的净效应是，将创建代理的想法，以及一些执行工作，推向了业务线人员，而不是仅仅依赖开发人员。

“在高级别上，你从某个系统中获取信息——一个专有系统、互联网或它们的组合——然后使用它来告知一个 AI 工具、一个代理或某种类型的生成式助手，”Margolis 说。“这与我们一两年前在 LangChain 中看到的模式相同，你拥有这些逻辑和推理循环，并且不断增强输出，直到它最终为你提供你想要的东西。它只是变得不那么微妙了。”

“有了像 Agent Builder 和 GPTs 这样的东西，你不需要是 AI 工程师才能做到这一点。你可以是一个外行人来做到这一点。你可以使用纯文本或 ClickOps 之类的东西来做到这一点。在解决方案空间方面，它更具可预测性。”

## 结合 AI 模式
将 AI 模式结合起来的想法可能对 AI 工程师更具实际意义。需要注意的是，当 Margolis 在这种情况下谈论模式时，他指的是我们可能认为的“传统”机器学习，例如用于推理和预测的机器学习，以及基础模型和生成式 AI 的更新模式之间的区别。这与生成式 AI 中的模式概念不同，在生成式 AI 中，输入和输出取决于媒体，例如文本、音频、视频或翻译。

“以前你会看到有些人要么在生成式 AI 世界中玩耍，要么在更传统的 ML 世界中玩耍，围绕推理和预测之类的东西，现在你开始看到这两种东西的融合。”

> “这不是一个无代码解决方案，而是一个相对低代码的解决方案。我不是从头开始构建模型。我没有用 TensorFlow 编写代码。”

Margolis 指出，这就是我们可以看到生成式 AI 的使用，而无需构建特定的 AI 代理或聊天机器人。他以使用 AI 工具在医疗保健系统中呈现数据的例子为例，在医疗保健系统中，护士或医生或管理员可能会输入有关患者的多个数据字段，这些数据字段由生成式工具编写。然后在同一个系统中，有 ML 工具带有推理引擎，这些工具可能会说这是一个高风险患者等等。

“几年前，如果我想构建一个像 [医疗保健示例] 这样的应用程序，我可能需要征求一些精通模型创建的 ML 同事，他们可能需要使用 JAX 或 TensorFlow 为我构建一个倾向模型，”Margolis 说。“他们可能需要真正地进入物理 GPU。这需要大量的 ML 工程和数据科学工作。然后在生成方面，也许我可以直接将该输出输入到我最喜欢的生成模型的上下文窗口中。但这些是两种截然不同的技能。”

Margolis 说，像 Google Cloud 的 Vertex 套件（SADA 是 Google Cloud 生成式 AI 的首选合作伙伴）这样的工具可以帮助弥合机器学习工具和生成式 AI 工具之间的差距。

“现在同一个工程师可以去 Vertex 创建一个 AutoML 模型，”Margolis 说。“这不是一个无代码解决方案，而是一个相对低代码的解决方案。我不是从头开始构建模型。我没有用 TensorFlow 编写代码。我没有用 JAX 编写代码。我不处理 GPU。我不处理任何虚拟或系统组件。”

有关将生成式 AI 与结构化数据结合使用的更多信息，Margolis 最近在 Medium 上发表了一篇 [关于该主题的有趣文章](https://medium.com/google-cloud/generative-agents-with-structured-data-c4947603f600)。

## 生成式 AI 帮助构建生成式 AI

> “进入的门槛真的降低了，我认为这对每个人都有好处。”

我们还没有进入一个计算机自主构建自己的婴儿计算机并编写自己的代码的世界。然而，AI 工程中一个有趣的发展是使用生成式 AI 来帮助构建更多生成式 AI 代理、机器人和应用程序。

“我认为这是一个强大的模式，它使许多人能够参与到这个领域，”Margolis 说。

他将这种趋势比作过去 10-15 年的拐点，当时开发人员可以轻松地在云中启动虚拟机（大约在 2010 年），或者当构建移动应用程序的门槛在 2014 年左右降低时。

“我觉得这和我们在公共云中遇到的‘哦，天哪’时刻一样，当时我们意识到，每个刚开始学习计算机科学或系统设计的学生，你知道，在 2010 年，突然之间就可以启动服务器和数据库，”Margolis 说。“如果你想在 18 个月前成为一名 AI 开发人员，你需要克服一个很大的障碍。要达到能够真正实现你的想法的程度，需要做很多工作。现在我们已经到了有了一个想法并实现它，你可能可以在午餐时间完成。”

“进入的门槛真的降低了，我认为这对每个人都有好处。”
