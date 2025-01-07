# 通用多模态AI模型的兴起

![通用多模态AI模型特色图片](https://cdn.thenewstack.io/media/2025/01/cfb521f4-google-deepmind-3pukewjvszw-unsplashb-1024x576.jpg)

过去一年左右，人们对[多模态大型语言模型](https://thenewstack.io/top-7-tools-for-building-multimodal-ai-applications/) (MLLMs) 的兴趣激增，这要归功于它们在处理多种类型数据（文本、图像和视频，以及时间序列和图数据）的任务中的多功能能力。

由于MLLMs旨在学习、推理并根据上下文信息调整其行为——这与人类智力的运作方式非常相似——一些专家也认为，进一步发展多模态AI是迈向[人工通用智能](https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-artificial-general-intelligence-agi) (AGI) 的关键一步。

正是由于多模态AI潜在的下游影响，现在人们更加关注构建真正“通用”的多模态AI模型。这种通用多模态模型 (GMMs) 能够轻松地跨不同模态学习，并在面对不同类型任务时适应并表现良好。

当前通用多模态AI模型的示例包括：

## 基础模型铺平道路

当前通向通用多模态模型的轨迹源于预训练的深度学习[基础模型](https://www.datacamp.com/blog/what-are-foundation-models) 的发展，这些模型用于处理自然语言、视觉、时间序列和图结构数据。

最值得注意的是，2018年引入的基础语言模型 (FLMs)，例如[BERT](https://www.datacamp.com/blog/what-is-bert-an-intro-to-bert-models)（来自Transformer的双向编码器表示），在为能够使用基于注意力的架构在海量文本数据集上进行预训练的模型奠定基础方面具有关键作用。这些Transformer模型最终为后来的大型语言模型铺平了道路，例如OpenAI的[GPT系列](https://thenewstack.io/openais-gpt-3-makes-big-leap-forward-for-natural-language-processing/)。

同样，基础视觉模型 (FVMs)，例如[视觉Transformer (ViT)](https://huggingface.co/docs/transformers/en/model_doc/vit) 和视觉语言对齐模型，例如[CLIP](https://medium.com/@melgor89/foundation-models-for-computer-vision-42574d13f6a6) 和[LLaVA](https://thenewstack.io/5-multimodal-ai-models-that-are-actually-open-source/)，帮助推动了多模态AI模型的跨模态能力。

虽然语言和视觉领域的基础模型发展迅速，但由于此类模型的特殊性和它们在不同数据集之间的有限可迁移性，开发基础时间序列模型 (FTMs) 和基础图模型 (FGMs) 的工作进展较慢。

尽管如此，诸如[Informer](https://arxiv.org/abs/2012.07436) 和[TimeGPT](https://towardsdatascience.com/timegpt-the-first-foundation-model-for-time-series-forecasting-bf0a75e63b3a) 之类的时间序列模型以及[图神经网络](https://www.assemblyai.com/blog/ai-trends-graph-neural-networks/) (GNNs)，例如[GROVER](https://arxiv.org/abs/2007.02835)，的功能可能会转化为通用多模态模型——从而允许GMMs轻松地根据历史时间戳数据（即[时间序列预测](https://www.datacamp.com/blog/ai-time-series-forecasting)）进行未来预测，或分析各种实体及其相互作用（即[图数据](https://www.assemblyai.com/blog/ai-trends-graph-neural-networks/)）。

## 典型的模型流程

根据最近[太平洋西北国家实验室](https://www.pnnl.gov/)的一项[调查](https://arxiv.org/pdf/2406.05496)，该调查考察了GMMs 的发展，一个具有通用能力的多模态模型通常具有以下组件：

- 输入数据预处理器；
- 通用学习模块（编码器、解码器）；以及
- 输出数据后处理器。

![](https://cdn.thenewstack.io/media/2024/12/7890f219-generalist-multimodal-ai-survey-munikoti-et-al.png)

来自Munikoti等人的“通用多模态AI：架构、挑战和机遇综述”

不同模态的原始数据由输入数据预处理器预处理，将其转换为通用学习模块可以使用的一种形式。这可以通过序列化或标记化来实现，其中文本、音频或图像被转换为数字“标记”格式，以便可以将其馈送到通用学习模块的编码器中——该编码器充当学习和推理的“主干”。
编码器将输入令牌转换为位于高维语义空间中的表征嵌入，用于通用学习。例如，基于文本的数据可以由任何大型语言模型处理，而图像可以由像CLIP这样的模型编码，或者各种模态可以由像[ImageBind](https://thenewstack.io/top-7-tools-for-building-multimodal-ai-applications/)这样的多模态模型编码。

此外，可能需要一个[投影器](https://www.tandfonline.com/doi/full/10.1080/0952813X.2022.2078889#abstract)来转换或“投影”编码器的表征嵌入，使其能够被通用学习模块理解。

解码器然后将多模态表征嵌入转换为与任务相关的输出，并根据从先前步骤收集的跨模态上下文进行信息告知。

## 挑战

虽然通用多模态人工智能领域仍在不断发展，但仍有一些潜在问题需要考虑。

这些问题包括多模态数据集的短缺，相对于丰富的单模态、基于文本和基于图像的数据集而言。这是由于成本和对数据隐私的合理担忧，以及生成真正全面的多模态数据集的巨大计算和人力成本，这些数据集需要将海量文本数据与音频和图像数据（例如）准确匹配。

其他障碍包括缺乏足够复杂的基准来评估通用多模态模型（GMMs），而通常的基准主要针对文本和图像。

另一个障碍是当前的多模态学习严重偏向于跨模态学习，这往往偏向于图像和文本而不是其他模态。需要更多的研究来探索和创新，以捕捉代表性不足的模态——例如红外图像中的热信息——然后可以利用这些信息来进一步开发用于医疗应用的通用多模态人工智能模型。

尽管存在这些挑战，但进一步发展真正通用的多模态人工智能是一个至关重要的任务，尤其是在建立AGI必要基础方面。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。