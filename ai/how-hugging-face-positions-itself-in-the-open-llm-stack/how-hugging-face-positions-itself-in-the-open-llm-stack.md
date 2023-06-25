# Hugging Face 在开放 LLM 堆栈中的定位是什么？

翻译自 [How Hugging Face Positions Itself in the Open LLM Stack](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) 。

Hugging Face 在生成式人工智能开发者生态系统中扮演什么角色？我们来看一下该公司精明的开源品牌定位。译者在前不久确实成了 Hugging Face 的粉丝，也有幸参加了一次 Hugging Face 联合 Google 举办的一次开发者活动。

![](https://cdn.thenewstack.io/media/2023/06/5b642950-huggingface_feature2-1024x568.jpg)

Hugging Face 在生成式人工智能开发者生态系统中扮演着什么角色？我们来看一下该公司精明的开源品牌定位。

忘记 LAMP 堆栈，现在一切都是关于 LLM 堆栈。在过去的一年中，诸如 [LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/) 和 [Anyscale 的 Aviary](https://thenewstack.io/a-new-tool-for-the-open-source-llm-developer-stack-aviary/) 等工具已经推出，帮助开发者基于或连接到大型语言模型（LLMs）构建应用程序。尽管现在还处于初期阶段，[Hugging Face](https://huggingface.co/) 已经迅速成为这个新兴堆栈的关键组成部分。它已经成为选择 LLMs 和其他机器学习模型和数据集的首选存储库。

在最近在瑞典 PyCon 的[演讲](https://youtu.be/fckyXntHy1s)中， Hugging Face 首席传道者 Julien Simon 解释了 Hugging Face 在生成式人工智能开发者生态系统中的角色，以及其近期的计划。

## Hugging Face 如何成为开源冠军？

具有讽刺意味的是， Hugging Face 是一家商业公司，其存储库实际上并不是一个开源平台。但是，它最接近的 “Web 2.0” 等价物 GitHub（当然是由 Microsoft 拥有）也不是开源平台。在这两种情况下，重要的是托管的文件是开源的。

在其作为开放平台的品牌定位中， Hugging Face 最初是开源 transformer 库的提供者。

“所以 Hugging Face 是一家成立于 2016 年的公司，我们开始在 2018 年左右构建 transformer 的开源库，” Julien Simon 在他在瑞典 PyCon 的主题演讲中说道。“结果发现，我们是发展最快的开源项目之一。”

![](https://cdn.thenewstack.io/media/2023/06/7f4fae4b-hf_growth2-scaled.jpg)


那么为什么 Hugging Face 会如此迅速地变得如此受欢迎呢？Simon 列举了几个因素，包括处理早期神经网络的困难和运行它们所需的昂贵的 GPU 。但是他说，最大的问题是缺乏“专家工具”。

“所以，如果你想从神经网络和深度学习模型中获得你所期望的准确性，你需要深入研究 PyTorch 代码、 TensorFlow 代码[...]，你需要有计算机科学、统计学和机器学习的背景，而不是每个人都有这个背景，对吧。”

![](https://cdn.thenewstack.io/media/2023/06/c0ae0f6a-hf_expert_tools2-scaled.jpg)

Hugging Face 试图做的，他继续说，是使 AI 开发“更快、更简单、更高效”。他将这一努力比作敏捷方法在软件工程项目管理中取代瀑布模型的过程。

![没有命运](https://cdn.thenewstack.io/media/2023/06/4df21d3f-hf_agile2.jpg)

他称之为（当然是）深度学习 2.0 的这个新过程的关键是使用 transformers ，即 OpenAI 的 GPT 和几乎所有后来的模型都是基于该技术构建的。

“最重要的是，我们不再需要使用一系列复杂的深度学习架构，而是越来越多地使用 transformers 模型，”他说。

![](https://cdn.thenewstack.io/media/2023/06/c4afcfe7-hf_dl2.02-scaled.jpg)

同样重要的是，开发者工具要比上述的“专家工具”更简单。正如 Simon 所说，“如果你能写几行 Python 代码，你就可以开始了。”

在 2023 年，没有 Marc Andreessen 在 2011 年著名的“软件正在吞噬世界”这句话，就不完整了。在 Hugging Face 的世界中，这句话变成了“ transformers 正在吞噬深度学习”。

![](https://cdn.thenewstack.io/media/2023/06/7bd2f752-eating2-scaled.jpg)

## Hugging Face Hub

除了其 transformer 库外，Hugging Face 还以其 “Hub” 而闻名，这是一个平台，“拥有超过 12 万个模型、 2 万个数据集和 5 万个演示应用程序（Spaces），全部都是开源和公开可用的。”在他的演讲中， Simon 称其为“机器学习的 GitHub ”。他还表示，Hub 拥有超过 10 万个“活跃用户”，每天下载量超过 100 万次。

![Hugging Face](https://cdn.thenewstack.io/media/2023/06/725d50a0-hf-hub2-scaled.jpg)

回到敏捷方法的比较上，Simon 随后提供了开发者在 Hugging Face 上可能遵循的流程图。

![Hugging Face流程](https://cdn.thenewstack.io/media/2023/06/88073fbe-hf-flow-chart2-scaled.jpg)

“所以你可以从 Hub 上的现有数据集和预训练模型开始。然后，你可以直接使用它们——[...]在 Transformers 库中编写几行代码，然后在你的数据上测试这些模型。如果它们效果不错，如果你获得了所需的准确性，那就完成了[...]，你可以称自己为机器学习工程师。”

这只是开发者可以做的一小部分。他提到，你可能希望对自己的数据进行微调，或者使用 Optimum 进行硬件加速。

他补充说，Hugging Face 与 Amazon（SageMaker） 和 Azure 都有集成，因此开发者也可以使用这些工具。目前还没有与 Google 的集成。

## 开放和闭源的混合

在本文的开头，我有点轻率。新的 LLM 堆栈与上世纪 90 年代末和本世纪初的 LAMP 堆栈并不直接可比——首先，在 LLM 堆栈中没有操作系统组件。但是，有一套工具，包括出色的开源版本，开发者在使用 LLMs 时开始青睐。例如，对于向量数据库，既有商业版（例如 [Pinecone](https://thenewstack.io/vector-databases-are-having-a-moment-a-chat-with-pinecone/) ），也有开源版本（例如 Chroma ）[可供选择](https://thenewstack.io/top-5-vector-database-solutions-for-your-ai-project/)。

Hugging Face 是开源产品和典型的 [SaaS 商业产品](https://huggingface.co/pricing)的混合体。在 2022 年，它发布了一个名为 [BLOOM](https://huggingface.co/docs/transformers/model_doc/bloom) 的 LLM ，并在今年发布了一个名为 [HuggingChat](https://twitter.com/ClementDelangue/status/1650908484936908808) 的 ChatGPT 竞品。在 SaaS 方面，它的许多产品之一是 Inference Endpoints ，这是一个“完全托管的基础设施”，用于部署模型，起价为每小时 0.06 美元。考虑到商业设置和风险投资，有可能（甚至很有可能）有一家大型科技公司收购 Hugging Face ，就像 Microsoft 收购 GitHub 一样。但目前，开发者没有什么可以抱怨的。

Simon 在[最近接受英特尔采访](https://www.intel.com/content/www/us/en/developer/articles/community/democratized-language-models-boost-ai-development.html)时表示：“我告诉客户，如果他们相信 AI 具有变革性，它可能比云计算的变革性还要大，你怎么能不拥有它呢？你不希望别人掌控你的未来。你希望自己掌控自己的未来。”

最终，这是一个聪明的定位，与 OpenAI 领导的专有 LLM 阵营截然相反。此外，在人工智能时代， Hugging Face 将自己称为“机器学习的 GitHub ”无疑吸引了开发者们的注意。