<!--
title: 为什么红帽认为人工智能的未来是小语言模型
cover: https://cdn.thenewstack.io/media/2025/03/02841b58-smallai.jpg
summary: Red Hat 认为 AI 未来在于小型化！企业应拥抱定制化、低成本的 LLM 和 AI Agent。InstructLab 开源项目助力 GenAI 应用，通过指令调优和合成数据，简化 LLM 创建。vLLM 推理服务器和 PyTorch FSDP 加持，让 AI 在 OpenShift 上跑得飞起！
-->

Red Hat 认为 AI 未来在于小型化！企业应拥抱定制化、低成本的 LLM 和 AI Agent。InstructLab 开源项目助力 GenAI 应用，通过指令调优和合成数据，简化 LLM 创建。vLLM 推理服务器和 PyTorch FSDP 加持，让 AI 在 OpenShift 上跑得飞起！

> 译自：[Why Red Hat Thinks AI’s Future Is Small Language Models](https://thenewstack.io/why-red-hat-thinks-ais-future-is-small-language-models/)
> 
> 作者：Loraine Lawson

没有一个能做所有事情的独角兽应用程序，那么为什么应该有一个大型语言模型（LLM）来满足所有需求呢？

[Tushar Katarki](https://www.linkedin.com/in/katarki/)认为不应该这样，他是[Red Hat](https://www.openshift.com/try?utm_content=inline+mention)公司 GenAI 基础模型平台的高级产品总监。他告诉 The New Stack，流行的 LLM 对于大多数组织，甚至企业来说，可能都是过度配置。

“如果你有一个大型模型，当然它非常强大，但同时也伴随着很多东西，”Katarki 说。“[一个]企业不需要一个可以做世界上所有事情的单一模型。事实上，如果有什么需要的话，他们需要可以定制并用于其用例的模型。”

[大型语言模型](https://thenewstack.io/top-5-large-language-models-and-how-to-use-them-effectively/)是 ChatGPT 等流行的 Gen AI 解决方案的基础，需要服务于数百万客户，满足各种语言和知识需求，但他指出，[企业 AI](https://thenewstack.io/how-ai-agents-are-starting-to-automate-the-enterprise/) 可以更加专注。

“企业面临着不同的问题，”他说。“他们实际上有很多不同的用例。”

## 为什么开发者应该拥抱小型模型

组织想要小型 LLM 有两个主要原因。首先，他说，小型模型在运营和运行方面更具成本效益。其次，企业希望能够从 AI 内部访问其私有数据。

“猜猜怎么着？任何大型模型，尤其是他们从 ChatGPT 或其他任何地方获得的模型，都不包含你企业的私有数据，”Katarki 说。

但对于开发者来说，还有第三个原因可以利用小型模型和 [AI 代理](https://thenewstack.io/the-rise-of-ai-agents-how-arazzo-is-defining-the-future-of-api-workflows/)：它们可以用作工作流程中的“构建块”，就像开发者利用微服务来处理多个应用程序中的不同功能一样，Katarki 补充道。

“AI 代理只不过是这些小型的、适合用途的 AI 系统，所有这些都需要可以为企业用例定制的小型模型，”他说。“一旦你开发了一个代理，……你就可以混合搭配不同的东西并创建一个不同的终端系统。”

## 小型模型的骨架

当然，[小型语言模型](https://thenewstack.io/the-rise-of-small-language-models/)不一定很小——它们只是相对于其他模型而言较小。例如，LLaMA 有一个 4050 亿参数的模型（目前最大的模型），但也有一个 700 亿参数的模型、一个 80 亿参数的模型和一个 30 亿参数的模型。

“我们只是简单地说，80 亿和 30 亿的模型可能更小，”Katarki 说。“没有这些的正式定义。但这就是想法。否则，它们都是 LLaMA 模型。”

小型[语言模型也应该仍然由 Transformer 模型生成](https://thenewstack.io/grounding-transformer-large-language-models-with-vector-databases/)，这是一种神经网络架构，他说。Transformer 模型包括：

*   [OpenAI 的 GPT](https://thenewstack.io/openai-launches-new-chatgpt-interface-designed-for-coding/)(Generative Pre-trained Transformer) 系列；
*   [Google](https://cloud.google.com/?utm_content=inline+mention)的[BERT](https://research.google/pubs/bert-pre-training-of-deep-bidirectional-transformers-for-language-understanding/)(Bidirectional Encoder Representations from Transformers) 和 T5 (Text-to-Text Transfer Transformer)；
*   Meta 的[LLaMA](https://thenewstack.io/get-started-with-metas-llama-stack-using-conda-and-ollama/)(Large Language Model Meta AI) 和 RoBERTa (Robustly Optimized BERT Pretraining Approach)；
*   以及 [IBM](https://www.ibm.com?utm_content=inline+mention)的 Granite 模型。

“当我们说小型模型时，它们不是新的——它们仍然基于这种 Transformer [范式]，因此它们肯定需要具有基本的语言能力，包括代码等，”Katarki 说。

## 创建小型语言模型

有几种生成小型模型的选项。最著名的是[检索增强生成 (RAG)](https://thenewstack.io/rag-and-model-optimization-a-practical-guide-to-ai/)，它作为一种使用专有数据集改进模型的工具而备受关注。

“RAG…允许你引入自己的数据集，并对其进行向量化处理，然后放入向量数据库，”Katarki说。“当查询到来时，你会查找向量数据库，看看文档中最相关的部分是什么，然后将其作为提示发送给[大型语言模型](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/)，说明你将其用作问题的提示。”

但他补充说，RAG也有缺点。首先，它可能会遇到检索方面的挑战。其次，它需要创建另一个数据库，“随着数据集的增加，这会带来自身的规模问题，”他补充说。

他继续说，虽然RAG确实提高了准确性，但也有局限性。

“如果你想不断提高AI系统的准确性，那么你需要对知识进行微调，使其融入模型中，”他说。

他补充说，这就是Red Hat用于创建小型模型的工具可以发挥作用的地方。

## InstructLab如何生成小型模型

[InstructLab](https://www.redhat.com/en/topics/ai/what-is-instructlab)是一个开源项目，用于增强Gen AI应用中使用的LLM。InstructLab由IBM和Red Hat创建，Instruct代表“instruction tuning（指令调优）”，这是一个行业术语。LAB代表[Large-scale Alignment for chatBots](https://research.ibm.com/blog/LLM-generated-data)，它来自[IBM的相关研究论文](https://arxiv.org/abs/2403.01081)。

InstructLab使用监督式微调，也称为指令对齐。这种方法基本上是通过标记来训练AI。例如，对于[计算机视觉模型](https://thenewstack.io/computer-vision-modeling-unlocks-new-use-cases/)，训练员会指示或标记AI，一张图片是狗，另一张是猫，直到它学会区分。

“我将告诉你下一个词是什么，以及正确的下一个词是什么，所以如果你预测的东西不是这个，那么你必须给你的预测打很低的分数。如果你预测的和我告诉你的完全一样，那么你可以给自己打高分，”他解释说，“这基本上在监督式微调中重复了无数次，所以你需要的是标签数据。”

> “一个企业不需要一个可以做世界上所有事情的单一模型。事实上，如果有什么需要的话，他们需要可以定制并用于其用例的模型。”
>
> — Tushar Katarki, Red Hat

Katarki说，使用InstructLab，只需“几个CLI命令”即可完成该过程。

“如果你让别人做监督式微调，那是一个非常繁琐的过程。你需要数据科学家来做，”他说。“我们使它变得非常简单，并且对非数据科学家或‘公民数据科学家’来说也很容易访问。”

标记数据也很昂贵。因此，InstructLabs获取一个数据集，使用合成数据生成对其进行放大，然后使用合成数据进一步训练模型。

Katarki提供了一个例子。一家银行可能希望训练一个模型，了解如何在消费者来电时批准信用额度增加。为此，银行需要创建一个具有代表性的问答，其中包含该场景可能产生的各种问题，例如客户是谁，他们的信用评级是什么，他们在银行的时间是否足够长。

“合成数据生成将采用这些具有代表性的问题，并以1,000种不同的方式应用这些问题，”他说。“它使用生成式AI来做到这一点，然后它会有一个你已经提供的数据语料库，因为那是答案。现在它有了一个非常大的数据集。”

该模型学习了更多关于如何进行问题和答案的排列组合，这使其在回答问题时更加有效。

他补充说，该平台还支持用于完全共享数据并行（FSDP）的PyTorch，这是一种用于LLM分布式训练的技术。

## 为什么AI需要开源

Katarki认为，组织选择开源，尤其是在AI领域，也非常重要。尽管InstructLab可以训练任何LLM，但Katarki指出[IBM Research的Granite](https://www.ibm.com/granite)是一个开源选项。

这提供了两个好处。首先，它可以为可能出现的任何知识产权索赔创建保障。其次，它提供了许可优势。

“如果我是一家公司，特别是如果我是一家需要发布这些模型的公司，那么如果它是Apache 2.0许可，我就不必再来找你，”他说。“假设我们使用LLaMA，例如，它不是Apache 2.0许可……你不想发现——在7亿用户之后，现在我是一个非常成功的企业——我现在必须回到[Meta]为我的第7亿零一个用户付费。”
Red Hat 最近还增加了一个推理服务器，这是运行任何 LLM 所必需的。Red Hat 收购了 Neural Magic，该公司是流行的开源推理服务器 [vLLM](https://github.com/vllm-project/vllm) 的主要商业贡献者，收购于 1 月份完成。[Red Hat 收购 Neural Magic](https://www.redhat.com/zh/about/press-releases/red-hat-completes-acquisition-neural-magic-fuel-optimized-generative-ai-innovation-across-hybrid-cloud)。

“所有这些大型语言模型都需要一个运行时来运行它们，而 vLLM 是事实上的运行时，”他说。

InstructLab 可用于 Red Hat [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 或 [OpenShift](https://thenewstack.io/docker-testcontainers-now-available-on-red-hats-openshift/)。它允许 AI 在本地 [数据中心或公共云或私有云中运行](https://thenewstack.io/choosing-the-right-database-strategy-on-premises-or-cloud/)。