# 机器遗忘：为什么教会 AI 遗忘至关重要

![机器遗忘：为什么教会 AI 遗忘至关重要的特色图片](https://cdn.thenewstack.io/media/2024/08/85a00206-kim-leary-2zl80uqruuu-unsplash-1024x683.jpg)

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

###  精确遗忘 

精确遗忘的目标是完全删除模型中与特定数据点相关的知识。这就像从模型的记忆中完全擦除一个特定的数据点。

###  近似遗忘 

近似遗忘的目标是减少模型对特定数据点的依赖性，而不是完全删除它。这就像让模型“忘记”特定数据点的大部分信息，但仍然保留一些关于它的模糊记忆。

这两种方法都有其优缺点，选择哪种方法取决于具体的应用场景。

## 机器遗忘的挑战

机器遗忘面临着许多挑战，包括：

* **模型复杂性：** 大型语言模型非常复杂，难以理解它们是如何工作的，更难以控制它们的行为。
* **数据依赖性：** 模型通常依赖于大量数据进行训练，删除部分数据可能会影响模型的性能。
* **隐私和安全：** 遗忘机制需要确保数据被安全地删除，并且不会被恶意使用。

## 机器遗忘的未来

机器遗忘是一个新兴的研究领域，还有很多问题需要解决。然而，它具有巨大的潜力，可以帮助我们构建更安全、更公平、更值得信赖的 AI 系统。

随着 AI 技术的不断发展，机器遗忘将变得越来越重要。它将帮助我们解决 AI 发展中面临的伦理和社会问题，并确保 AI 技术能够造福人类。
**精确遗忘：** 也称为完美遗忘，它需要从头开始重新训练 AI 模型，但不需要删除需要删除的数据。这种方法的优点是，它确保删除特定数据点不会损害模型的性能，缺点是它通常需要大量的计算资源，最适合不太复杂的 AI 模型。[精确遗忘](https://www.xda-developers.com/what-is-machine-unlearning/) 的示例包括反向最近邻 (RNN) 等技术，它通过调整与其相邻的其他数据点来弥补数据点删除的影响。K 最近邻是一种类似的技术，但根据目标数据点的接近程度删除数据点，而不是调整它们。

另一种精确遗忘方法是将数据集分成两个独立的子集，然后训练两个可以稍后合并的局部模型，这个过程称为[分片](https://softteco.com/blog/what-is-sharding)。如果需要消除集合中的特定数据点，则可以修改该特定数据集并用于重新训练局部模型，然后再进行分片。

**近似遗忘：** 也称为有界遗忘或认证遗忘，它旨在将未学习数据的影響最小化，而不是完全消除，使其达到可接受的水平。在计算资源和存储成本有限的情况下，或者需要更灵活的解决方案时，近似遗忘方法可能更可取。近似遗忘方法的缺点是它们不能完全消除所有未学习数据的痕迹，并且可能难以验证或证明遗忘过程的有效性。
[局部离群因子](https://towardsdatascience.com/local-outlier-factor-lof-algorithm-for-outlier-identification-8efb887d9843) (LOF) 技术就是一个近似遗忘的例子，它识别并清除数据集中的离群数据点，以提高模型性能。

类似地，[隔离森林](https://www.analyticsvidhya.com/blog/2021/07/anomaly-detection-using-isolation-forest-a-complete-guide/) (IF) 等算法可用于创建具有随机子采样数据的决策树，这些数据基于随机选择的特征进行处理，目的是评估任何明显的异常，然后可以将其丢弃。与精确遗忘方法相比，这些近似遗忘方法更容易适应更大的模型，如 LLM。

## 遗忘并非万能药 - 至少现在还不是
目前，还没有一种万能的解决方案可以解决机器遗忘的不同应用，尽管像 Kurmanji 这样的研究人员正在努力开发更通用的遗忘工具。

在 Kurmanji 的案例中，他和沃里克大学和谷歌 DeepMind 的研究人员团队创建了一个[名为 SCRUB 的工具](https://arxiv.org/pdf/2302.09880)，它有可能解决各种问题，从消除偏差，保护用户隐私到解决模型中由于数据标记错误而导致的混淆。

“SCRUB 的设计基于机器学习中的一种方法，称为[‘师生’框架](https://amit-s.medium.com/everything-you-need-to-know-about-knowledge-distillation-aka-teacher-student-model-d6ee10fe7276),” Kurmanji 说。“它的工作原理如下：一个预训练模型（‘老师’）指导新模型（‘学生’）的训练。SCRUB 将这个概念更进一步。在训练新模型时，SCRUB 使其对我们想要遗忘的数据‘不服从’老师模型，而对其他数据‘服从’老师。这种相互作用是通过最小化或最大化模型输出之间的相似性度量来管理的。但是，SCRUB 有时会过度遗忘数据点，使其变得明显。这就是[算法] SCRUB+R 的用武之地，它对遗忘过程进行微调，以控制遗忘的程度。”

机器遗忘仍然面临着许多挑战，无论是缺乏标准的评估指标，还是与兼容性和可扩展性相关的潜在问题。但随着更大、更复杂的 AI 模型出现在地平线上，机器遗忘的概念将成为该过程越来越不可或缺的一部分。也许这将促使 AI 专家与法律、数据隐私和伦理领域的专业人士更紧密地合作，以更好地定义未来的[负责任的 AI](https://thenewstack.io/responsible-ai-at-amazon-web-services-qa-with-diya-wynn/) 实践和工具可能是什么样子。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)