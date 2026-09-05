<!--
title: “Google仅领先了几小时”：Meta发布Muse Spark 1.3，AI编程能力实现重大突破并超越Gemini
cover: https://cdn.thenewstack.io/media/2026/07/6b0faf67-rizki-ardia-p-a6oda-mqu-unsplash-scaled.jpg
summary: Meta推出Muse Spark 1.3推理模型，在编码与智能体任务上取得显著进展。凭借高性价比和出色性能，该模型在基准测试中超越了刚发布不久的Google Gemini 3.8 Flash，再次引发业界关注。此次发布不仅展示了Meta在模型迭代上的快速响应，也通过Muse Code进一步完善了其开发者生态系统。
-->

Meta推出Muse Spark 1.3推理模型，在编码与智能体任务上取得显著进展。凭借高性价比和出色性能，该模型在基准测试中超越了刚发布不久的Google Gemini 3.8 Flash，再次引发业界关注。此次发布不仅展示了Meta在模型迭代上的快速响应，也通过Muse Code进一步完善了其开发者生态系统。

> 译自：[“Google was ahead only a few hours”: Muse Spark 1.3 edges out Gemini as Meta claims its biggest coding leap yet](https://thenewstack.io/muse-spark-1-3-gemini/)
> 
> 作者：Paul Sawers

对于Meta的AI领域来说，本周是重要的一周。Meta正式[结束了Muse Code编程代理的测试阶段](https://thenewstack.io/muse-code-sdk-pricing/)，并推出了三项新的订阅计划。随后在周三深夜，该公司[发布了Muse Spark 1.3](https://research.meta.ai/blog/introducing-muse-spark-1-3)，这是其低成本推理模型的最新版本，Meta称该版本在编码和智能体任务上取得了迄今为止最大的进步。

Muse Spark 1.3可通过Muse Code和[Meta Model API](https://developer.meta.com/ai/products/meta-model-api/)获得，它是Meta在4月首次[引入的推理模型](https://ai.meta.com/blog/introducing-muse-spark-msl/)的最新迭代版本，且距离[Muse Spark 1.2](https://thenewstack.io/meta-muse-code/)的发布还不到一个月。Meta首席执行官Mark Zuckerberg在社交媒体上对这一新版本进行了宣传，称其提供了“几乎便宜到无需计费的前沿性能”。

> “这是我们在编码和智能体工作方面取得的迄今为止最大的飞跃。”

“这是我们在编码和智能体工作方面取得的迄今为止最大的飞跃，”Zuckerberg[在X上写道](https://x.com/finkd/status/2095232032896946311)。

## 开放权重版本“即将推出”

Zuckerberg还证实，Muse Spark的开放权重版本将“即将推出”。此举可能允许开发者下载该模型并在自己的基础设施上运行，从而绕过Meta托管的API。

然而，这一版本将有多大的开放性尚不清楚，因为Meta尚未公布随该版本附带的许可条款。其之前的开放权重模型[带有](https://thenewstack.io/meta-open-source-models/)不同的使用限制，因此具体细节将决定Spark可以多自由地被修改、重新分发或部署。

值得注意的是，Zuckerberg还预告了Meta备受炒作的下一个模型，代号为Watermelon（西瓜），并使用了相当贴切的西瓜表情符号。

据报道，该模型被认为是一个比Spark大得多的系统，据《商业内幕》（Business Insider）当时的[报道](https://x.com/finkd/status/2095232032896946311?s=20)，该模型在7月时仍在训练中。目前还没有关于Watermelon何时问世的确切消息，尽管Zuckerberg的暗示表明时间不会太久。

不过目前，Meta正为Spark 1.3本身提出一些宏大的主张。Zuckerberg在他的帖子中附带了一张基准测试表，将该模型与OpenAI的[GPT-5.6 Sol](https://thenewstack.io/developers-review-gpt-56-sol/)和Anthropic的[Claude Opus 5](https://thenewstack.io/anthropics-opus-5-almost-fable-5/)在编码、智能体、计算机使用和长上下文测试中进行了对比。

在突出的数据中，Muse Spark 1.3在DeepSWE编码基准测试中得分为75.4%，在512K-1M版本的MRCR长上下文测试中得分为98.1%。

![Muse Spark 1.3: 基准测试](https://cdn.thenewstack.io/media/2026/09/93e7fb99-becnhamrk-1024x920.png)

*Muse Spark 1.3: 基准测试*

然而，这些结果是由Meta汇总的。该公司表示，其Spark 1.3的得分是通过Meta Model API生成的，而对比数字则取自Meta自己的评估、官方排行榜以及竞争对手模型提供商报告的结果。Meta[还将对其第三方模型的测试](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology)描述为“尽力而为”，这意味着该表格不应被解读为在相同条件下进行的单一独立对比测试。

这些结果还有另一个警示：Meta在头条对比中运行的是其新的“最大（max）”推理级别，而目前开发者普遍可用的最高推理级别是“xhigh”。在Meta完成额外的安全测试之前，“max”仍处于有限预览阶段。

## “全力以赴”：Spark 1.3的表现如何

*Artificial Analysis*进行的独立测试[确实提供了一个有用的外部视角](https://artificialanalysis.ai/articles/muse-spark-1-3)。这家位于旧金山的专门从事AI模型和提供商基准测试的公司，在其智能指数（Intelligence Index）上给公开可用的Muse Spark 1.3 xhigh打了61分，比Spark 1.2高出4分，与GPT-5.6 Sol max、Grok 4.6 high和Claude Opus 5 high持平。它还测试了有限预览版的max版本，得分为62分，在发布时的对比模型中仅次于Claude Fable 5.1和Claude Opus 5。

![Artificial Analysis 智能指数 (来源: Artificial Analysis)](https://cdn.thenewstack.io/media/2026/09/94865237-stuff-1024x404.png)

*Artificial Analysis 智能指数 (来源: Artificial Analysis)*

云基础设施公司CoreWeave的AI传道者[Alex Volkov](https://www.linkedin.com/in/alex-volkov-/)指出该图表证明了Meta缩小与领先模型差距的速度有多快。

“该死，全力以赴了（gloves are off）！”，Volkov[在X上写道](https://x.com/altryne/status/2095252967452737785)，称Meta的这一表现是“相当有力的声明”，并预测“未来几周我们将很忙！”

> “该死，全力以赴了！”

成本是Meta推广策略的另一部分。Artificial Analysis将Spark 1.3 xhigh描述为在其测量智能水平上“最具成本效益的模型”，其61分的智能指数得分与相对较低的任务成本相结合，使其处于该公司的帕累托前沿线上。

![智能指数 vs. 每个智能指数任务的成本 (来源: Artificial Analysis)](https://cdn.thenewstack.io/media/2026/09/42576232-acost-1024x484.png)

*智能指数 vs. 每个智能指数任务的成本 (来源: Artificial Analysis)*

Artificial Analysis计算得出，Spark 1.3 xhigh每个智能指数任务的成本约为0.55美元，在所有指数得分59或更高的模型中是最低的。与Spark并列61分的GPT-5.6 Sol max和Grok 4.6 high的成本分别为0.95美元和0.94美元。

Spark 1.3每个任务的成本仍比Spark 1.2的0.40美元要贵，Artificial Analysis将这种增加主要归因于较新的模型在智能体评估中多消耗了约57%的输入Token。

![每个智能指数任务的成本 (来源: Artificial Analysis)](https://cdn.thenewstack.io/media/2026/09/961395e5-bcost-1024x401.png)

*每个智能指数任务的成本 (来源: Artificial Analysis)*

## Muse邂逅Gemini：“操场上的打闹”

值得注意的是，在Meta发布Muse Spark 1.3之前不久，Google[发布了](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)其自己的新低成本模型：Gemini 3.8 Flash，这是其[在短短六周内的第三次Flash发布](https://thenewstack.io/google-ships-its-third-gemini-flash-model-in-six-weeks/)。Google也将该模型作为其迄今为止最优秀的推理和编码Flash模型进行宣传，同时保持了每百万输入Token 0.75美元和每百万输出Token 3.75美元的初始定价。

Artificial Analysis[最初将](https://artificialanalysis.ai/articles/gemini-3-8-flash)Gemini 3.8 Flash (high) 放在其智能对成本的帕累托前沿——本质上是一组没有替代品比其更强大且更便宜的模型。Gemini[在智能指数上得了59分](https://artificialanalysis.ai/models/gemini-3-8-flash)，每个任务成本为0.58美元。

然而，仅仅几个小时后，Muse Spark 1.3 xhigh就以61分和每任务0.55美元的成绩到来，在两项指标上都击败了Gemini 3.8 Flash，并将其挤出了该前沿位置。

> “Google仅领先了几个小时。”

这一点被AI社区的许多人注意到了。事实上，AI研究员[Benjamin Marie](https://www.linkedin.com/in/benjamin-marie-a992b816b/)[在X上](https://x.com/bnjmn_marie/status/2095251751737971190)指出，“Google仅领先了几个小时。”

AI基础设施和研究公司[Prime Intellect](https://www.primeintellect.ai/)的研究工程师[Florian Brand](https://www.linkedin.com/in/florianbrand-de/)也简洁地总结了这一转变。

“Gemini 3.8在帕累托前沿保持了一个位置长达……查下笔记……3.5小时，”Brand[在X上写道](https://x.com/xeophon/status/2095255269060006397)。

甚至Meta首席AI官本人[Alexandr Wang](https://www.linkedin.com/in/alexandrwang/)也参与进来，借Artificial Analysis的报告之机对Google进行了抨击。

然而，云和AI成本管理公司Duckbill的联合创始人兼首席云经济学家[Corey Quinn](https://www.linkedin.com/in/coquinn/)很快就嘲笑了这种交流，暗示Meta和Google都没有在AI军备竞赛中真正引领步伐。

“Meta在AI领域对Google进行抨击，就像在MMA冠军赛场外发生的操场打闹，”Quinn[在X上写道](https://x.com/QuinnyPig/status/2095287236397031558)。

## Muse Code登场

背景方面，Muse Spark 1.3是Meta自4月以来推出的第四个模型版本，紧随7月的[Muse Spark 1.1](https://thenewstack.io/meta-muse-spark-api/)和一个月后的1.2版本。不过，可以说Meta推动力中更重要的部分是它围绕模型构建的智能体工具。

这以[Muse Code](https://developer.meta.com/ai/products/muse-code/)的形式呈现，这是Meta基于终端的编程代理，于[8月初](https://thenewstack.io/meta-muse-code/)随Spark 1.2一起进入测试阶段。它于周二正式发布，配有起价仅为每月5美元的新订阅计划，一个新的SDK也进入了开发者预览阶段。

因此，虽然Meta显然正在通过Muse Spark系列的增长证明其试图在模型质量上与前沿实验室竞争，但它也在更高层面追赶它们，即Anthropic的Claude Code和OpenAI的Codex在开发者如何实际使用智能体进行日常工作方面所设定的步伐。

这就解释了为什么1.3版本的发布语言中很大一部分专门围绕编程和智能体工作。该模型是Meta正在大力推行的更广泛开发者平台的关键组成部分，该平台在价格上和能力上一样激进。