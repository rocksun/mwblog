
<!--
title: 机器遗忘：为什么教人工智能忘记至关重要
cover: https://cdn.thenewstack.io/media/2024/08/85a00206-kim-leary-2zl80uqruuu-unsplash.jpg
-->

机器遗忘学习允许 AI 模型擦除选定的训练信息片段，而不会对模型性能产生负面影响。

> 译自 [Machine Unlearning: Why Teaching AI To Forget Is Crucial](https://thenewstack.io/machine-unlearning-why-teaching-ai-to-forget-is-crucial/)，作者 Kimberley Mok。

一旦你学会了某件事，就很难忘记它。可以想象，机器也是如此，尤其是那些在 [数十亿](https://thenewstack.io/large-language-models-open-source-llms-in-2023/) 个参数上训练的 [大型语言模型](https://thenewstack.io/what-is-a-large-language-model/) (LLM)。在一个大型语言模型在 [处理语言](https://thenewstack.io/the-building-blocks-of-llms-vectors-tokens-and-embeddings/) 或生成 [令人毛骨悚然](https://www.creativebloq.com/ai/viral-flux-ai-image-generator-images-show-were-out-of-the-uncanny-valley) 的图像（这些图像看起来越来越逼真）方面展现出强大力量的时代，许多未解决的 [伦理问题](https://thenewstack.io/the-power-and-ethical-dilemma-of-ai-image-generation-models/) 正在不断涌现。这些问题从 OpenAI 因使用受版权保护的新闻文章训练其 AI 模型而被起诉，到艺术家指责科技公司在未经许可的情况下 [非法使用他们的艺术作品作为训练数据](https://thenewstack.io/the-power-and-ethical-dilemma-of-ai-image-generation-models/)，不一而足。

当前的 AI 开发状况无疑是一个伦理雷区，这导致了人们对“机器遗忘”的兴趣激增。

“本质上，像 ChatGPT 这样的机器学习 (ML) 模型是在海量数据集上训练的，”[Meghdad Kurmanji](https://www.linkedin.com/in/meghdadk/)，华威大学机器学习和数据系统研究助理，博士候选人，向我们解释道。“机器遗忘就是让训练好的模型‘忘记’这些数据中的特定部分。这个概念有几个应用。例如，它可以帮助保护隐私，让个人在 AI 时代行使他们的‘[被遗忘权](https://www.weforum.org/agenda/2023/11/eu-right-to-be-forgotten-online-data/)’。想象一下，一个明星的肖像在未经许可的情况下被用于人脸识别系统，可以从模型的记忆中删除。此外，遗忘可以帮助保护版权和知识产权，正如最近涉及聊天机器人模型的诉讼所强调的那样，例如 [纽约时报与 OpenAI 之间的案件](https://theconversation.com/how-a-new-york-times-copyright-lawsuit-against-openai-could-potentially-transform-how-ai-and-copyright-work-221059)。最后，遗忘可以帮助解决 ML 模型中的偏差，引导我们走向更值得信赖的 AI 系统。”

## 为什么机器遗忘很重要——以及为什么它很难做到

自从 [2015 年的一篇论文首次提到](https://ieeexplore.ieee.org/document/7163042?arnumber=7163042&tag=1) 以来，这个日益重要的 AI 研究子领域旨在开发能够让 AI 模型有效地“忘记”选定的训练信息片段的方法，而不会对它们的性能产生负面影响——最重要的是，无需从头开始重新训练它们，因为这可能既昂贵又耗时。

但是，从 AI 模型中选择性地删除数据并不像从计算机硬盘中删除文件那样简单。许多模型的功能就像难以解释的、复杂的“[黑盒子](https://thenewstack.io/how-human-trust-varies-with-different-types-of-explainable-ai/)”，这使得机器遗忘就像 [从已经烤好的蛋糕中移除一种成分](https://www.microsoft.com/en-us/research/project/physics-of-agi/articles/whos-harry-potter-making-llms-forget-2/) 一样容易。

尽管如此，随着围绕人工智能的伦理考量和法规不断发展，这种“遗忘”功能将变得越来越重要，尤其是在涉及 [安全](https://thenewstack.io/the-security-risks-of-generative-ai-package-hallucinations/) 或 [隐私问题](https://thenewstack.io/llms-and-data-privacy-navigating-the-new-frontiers-of-ai/)、[有害偏差](https://thenewstack.io/big-questions-for-the-ethical-use-of-ai/)、过时或 [虚假信息](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/) 或不安全内容时。

为此，机器遗忘可以帮助 AI 满足未来数据隐私、公平性和合规性的目标，以及帮助减轻模型中的 [概念漂移](https://www.evidentlyai.com/ml-in-production/concept-drift)，在这些模型中，数据中的潜在模式可能会随着时间的推移而发生变化，从而导致预测精度降低。

## 机器遗忘的类型

总的来说，机器遗忘可以分为 [两种方法](https://arxiv.org/pdf/2209.02299)：精确遗忘和近似遗忘。

**精确忘却**：也称为完美忘却，它需要从头开始重新训练 AI 模型，但不需要删除的数据。这种方法的优点是它确保了特定数据点的移除不会损害模型的性能，缺点是它通常需要大量的计算资源，并且最适合不太复杂的 AI 模型。

精确忘却的例子包括反最近邻 (RNN) 等技术，它通过调整与要删除数据点相邻的数据点来补偿数据点的移除。K 近邻是一个类似的技术，但它基于数据点与其目标数据点的接近程度来删除数据点，而不是调整它们。

另一种精确的遗忘方法是将数据集分成两个单独的子集，然后训练两个部分模型，之后可以在称为分片（sharding）的过程中合并它们。如果需要从集合中删除特定的数据点，那么可以修改该特定数据集，并在再次分片之前使用它来重新训练部分模型。

**近似遗忘**：又称有界或经过认证的遗忘，其目的是将未学习过的数据的影响最小化（而不是完全消除）至可接受的程度。近似遗忘方法在以下使用场景中可能更可取：受到计算资源和存储成本的约束，或者需要更加灵活的解决方案。近似遗忘方法的缺点在于，它们并不会完全消除未学习过数据的所有痕迹，并且很难验证或证明遗忘过程的有效性。

近似遗忘的一个例子是局部离群因子 (LOF) 技术，该技术在数据集中识别并清除离群数据点以增强模型性能。

类似地，诸如隔离森林 (IF) 之类的算法可用于创建决策树，这些决策树具有随机子抽样数据，这些数据基于随机选择的特征进行处理，目的是评估可被丢弃的任何明显异常。与确切的遗忘方法相比，这些近似的遗忘方法更容易适应大型模型，如 LLM。

## 遗忘并非万能药 - 至少现在还不是

目前，还没有一种万能的解决方案可以解决机器遗忘的不同应用，尽管像 Kurmanji 这样的研究人员正在努力开发更通用的遗忘工具。

在 Kurmanji 的案例中，他和沃里克大学和谷歌 DeepMind 的研究人员团队创建了一个[名为 SCRUB 的工具](https://arxiv.org/pdf/2302.09880)，它有可能解决各种问题，从消除偏差，保护用户隐私到解决模型中由于数据标记错误而导致的混淆。

“SCRUB 的设计基于机器学习中的一种方法，称为[‘师生’框架](https://amit-s.medium.com/everything-you-need-to-know-about-knowledge-distillation-aka-teacher-student-model-d6ee10fe7276),” Kurmanji 说。“它的工作原理如下：一个预训练模型（‘老师’）指导新模型（‘学生’）的训练。SCRUB 将这个概念更进一步。在训练新模型时，SCRUB 使其对我们想要遗忘的数据‘不服从’老师模型，而对其他数据‘服从’老师。这种相互作用是通过最小化或最大化模型输出之间的相似性度量来管理的。但是，SCRUB 有时会过度遗忘数据点，使其变得明显。这就是[算法] SCRUB+R 的用武之地，它对遗忘过程进行微调，以控制遗忘的程度。”

机器遗忘仍然面临着许多挑战，无论是缺乏标准的评估指标，还是与兼容性和可扩展性相关的潜在问题。但随着更大、更复杂的 AI 模型出现在地平线上，机器遗忘的概念将成为该过程越来越不可或缺的一部分。也许这将促使 AI 专家与法律、数据隐私和伦理领域的专业人士更紧密地合作，以更好地定义未来的[负责任的 AI](https://thenewstack.io/responsible-ai-at-amazon-web-services-qa-with-diya-wynn/) 实践和工具可能是什么样子。
