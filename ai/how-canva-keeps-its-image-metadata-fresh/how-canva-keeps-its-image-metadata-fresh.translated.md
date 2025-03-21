# Canva 如何保持其图像元数据的新鲜度

![Featued image for: How Canva Keeps Its Image Metadata Fresh](https://cdn.thenewstack.io/media/2025/03/b94f2d61-canvas-monsterscale-1024x580.jpg)

在 2020 年之前，“[田园风 (cottagecore)](https://www.architecturaldigest.com/story/what-exactly-is-cottagecore)”这个词几乎不存在。但 Covid 疫情促使很多人开始让自己的家更舒适，并普遍浪漫化一种更简单、更乡村的生活。这个词在网上蓬勃发展，让人联想到装满干花的野餐篮、铸铁炉、装满水果的碗等等。

对于图形设计平台 [Canva](https://www.canva.com/) 的管理者来说，跟上这种语言趋势对于服务其用户群至关重要。趋势孕育商机，而企业需要推广。一旦出现像田园风这样的新词，图形设计师、营销人员和数百万其他月度用户都会希望在 Canva 上找到完美的图像，以美化他们的网站、营销和宣传材料。

那么 Canva 如何识别哪些图像适合像田园风这样的新类别呢？它管理着一个超过 400 亿张图像的库——这些图像要么来自图库照片服务，要么由其用户共享——并且每天摄取 5000 万到 1 亿张新图像。

显然，手动标记这些图像是无法扩展的。

Canva 首席机器学习工程师 [Kerry Halupka](https://www.linkedin.com/in/kerry-halupka/?originalSubdomain=au) 在为 [ScyllaDB](https://www.scylladb.com/?utm_content=inline+mention) 的 [Monster Scale Summit 2025](https://www.scylladb.com/monster-scale-summit/on-demand/) 上发表的 [演讲](https://www.scylladb.com/tech-talk/30b-images-and-counting-scaling-canvas-content-understanding-pipelines/) 中解释说：“我们需要大规模的准确实时标记。”该峰会于上周以虚拟方式举行。

而且，这种分类系统可能比人们最初想象的要复杂。

## 超越字面意义

以一张照片为例，照片中一位父亲穿着商务套装，似乎正在客厅里和他的小儿子玩耍，地板上散落着儿童玩具。

图像到文本服务可以轻松识别照片中的所有对象。但是，这张照片也可以在更抽象的类别下进行识别，例如“工作与生活的平衡”，或“父子情深”，甚至具有讽刺意味的是“专业父母”。

挑战在于，这些概念都无法在照片本身中识别出来。

Halupka 说：“这不仅仅是识别对象，而是要理解上下文和含义。”

而且这些术语不是静态的。每天都有新概念出现。并且，当试图使用 AI 进行任何类型的 [分类工作](https://thenewstack.io/graph-embeddings-101-key-terms-concepts-and-ai-applications/) 时，任何行业——不仅仅是图形设计——都会面临这个问题。

Halupka 解释说：“对用户重要的概念不是静态的。这是一个移动的目标，每天都会涌现出新的趋势。因此，我们需要一个可以处理数千个标签并可以轻松扩展到数千个标签的模型，以捕获这些更深层次的概念。”

Halupka 说：“我们的目标是推动机器超越识别简单对象，更接近对人类的细致理解。”

而且，鉴于 Canva 图像库的大小，分类系统必须快速。过于复杂的模型维护成本太高。而且它必须快速，以便它可以像用户自己一样快速地掌握新趋势。

## 一种“极端分类系统”

为了实现这些目标，该团队研究了典型的机器学习 [transformer-decoder architectures](https://thenewstack.io/how-liquid-ai-is-challenging-transformer-based-ai-models/) 之外的方法。Halupka 说，传统的分类架构的扩展“比线性更差”，这与要分类的标签数量有关。

相反，它选择了 [ML-Decoder](https://arxiv.org/abs/2111.12933) 架构，该架构起源于 [阿里巴巴](https://thenewstack.io/alibaba-github-repos-most-active-in-china/) 和 [达摩院](https://damo.alibaba.com/about?language=en)。开发团队发现，随着引入系统的概念数量的增加，ML-Decoder 的扩展“比线性更好”，Halupka 解释说。

“[ML-Decoder](https://arxiv.org/pdf/2111.12933) 通过查询预测类标签的存在，并且与全局平均池化相比，可以更好地利用空间数据。通过重新设计解码器架构并使用一种新颖的组解码方案，ML-Decoder 非常高效，并且可以很好地扩展到数千个类，”ML-Decoder 的创始人在一篇论文中解释说。

## 一个交互式数据标记管道

训练一个全新的术语——例如田园风——需要训练样本，并且最好事先不要手动标记数千张图像。
因此，该公司构建了一个交互式数据标注管道来定义新概念。一旦确定了一个新概念（“cottagecore”），该管道就会使用基于文本和基于图像的搜索相结合的方式，在一个小型训练集上找到与之紧密匹配的图像。然后检查整个图像库。在许多情况下，以前未标记的图像将被标记上新术语。在其他情况下，已经标记的图像也适合这个新术语。

![数据标注的屏幕截图。](https://cdn.thenewstack.io/media/2025/03/85d97064-monsterscale-canva-03.jpg)

“这是一个反馈循环。随着时间的推移，每个新概念都会扩展我们更准确地对图像进行分类的能力，” Kerry Halupka 解释说。

为了帮助理解单个搜索词的上下文，Canva 使用大型语言模型从单个短语生成更详细的描述。

例如，“Cottagecore”可能会衍生出：

- “一个舒适的农舍厨房”
- “一个拿着野花的年轻女子”
- “在树林里野餐”

Halupka 说，虽然不太明显，但这些都是人们仍然期望在“cottagecore”标签下看到的图像类型。

为了找到符合这些更详细描述的图像，Canva 使用 [CLIP](https://github.com/openai/CLIP) (Contrastive Language-Image Pretraining)，这是一个基于 [Python](https://thenewstack.io/what-is-python/) 的神经网络，经过训练可以在共享空间中查找图像/文本配对。

“由于 CLIP 比传统的关键词匹配更自然地理解概念，因此即使在没有明确标记的情况下，它也可以找到示例，”Halupka 解释说。

因此，诸如“带有复古装饰的舒适小屋厨房”之类的短语可能会出现符合此描述但以前未标记为“cottagecore”的图像，但确实通过[最接近的匹配向量](https://thenewstack.io/vector-processing-understand-this-new-revolution-in-search/)与该美学相匹配。

当新标签被引入模型时，它们仍然被评为“低置信度”，因此它们可以由 [VisualCritic LLM](https://arxiv.org/abs/2403.12806) 进一步检查以验证标签。

“结果是一个不断改进的训练集，它可以跟上不断发展的内容和词汇，并且可以用于训练可以在大规模运行的小型高效模型，”Halupka 说。

“这种方法的强大之处在于它既可扩展又可维护。当我们需要添加新概念时，无论是今天的 cottagecore 还是明天出现的任何趋势，这种自动化管道都可以找到多样化的、准确标记的示例，而无需大量的人工工作。因为每个步骤都针对质量进行了优化。即使在大规模的情况下，我们也可以保持高精度。”

在此处查看完整演示文稿：

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。 订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。