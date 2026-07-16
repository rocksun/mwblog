<!--
title: 24小时内：OpenAI、SpaceXAI与Meta将AI竞争拖入价格战泥潭
cover: https://cdn.thenewstack.io/media/2026/07/2b69987a-wahyu-setyanto-0qhkmuoy8oo-unsplash-1024x819.png
summary: 本文分析了OpenAI、SpaceXAI和Meta等大模型厂商在短期内集中发布新模型并主打低价策略的现象，指出AI行业正进入残酷的价格战。作者建议企业应构建模型组合，通过将任务分流至最适宜的成本与性能区间，以实现性价比最优，而非盲目忠诚于单一模型。
-->

本文分析了OpenAI、SpaceXAI和Meta等大模型厂商在短期内集中发布新模型并主打低价策略的现象，指出AI行业正进入残酷的价格战。作者建议企业应构建模型组合，通过将任务分流至最适宜的成本与性能区间，以实现性价比最优，而非盲目忠诚于单一模型。

> 译自：[In 24 hours, OpenAI, SpaceXAI, and Meta turned AI into a race to the bottom on price](https://thenewstack.io/openai-spacexai-meta-price-war/)
> 
> 作者：Matthew Burns

*我是Matt Burns，Insight Media Group的内容总监。每周，我都会汇总最重要的AI进展，并解释它们对那些将这项技术投入使用的人员和组织意味着什么。核心观点很简单：学会使用AI的从业者将定义各自行业的下一个时代，而本简报旨在帮助你成为其中一员。*

上周我正在露营、阅读，并与蚊子进行一场一边倒的搏斗。这周，AI新闻的节奏似乎比以前更快了。我很难跟上，我知道我并不孤单。

周三是Grok 4.5。周四是GPT-5.6。Meta发布了其首款付费模型，Anthropic则在订阅计划中扩大了对Fable的使用权限。这周我真实的反应不是兴奋，而是疲惫。

我花了20年时间报道产品发布，从iPhone到CES、IFA和MWC的展会狂热。我知道真正的突破节奏和营销作秀的区别，而我们现在正处于作秀的漩涡中。发布会变得越来越频繁。每次发布都标榜为前沿事件，但它们共同的突破在于经济性：用更少的Token（以及更少的美元）完成相似的工作。模型本身各不相同，但价格是每个实验室都在强调的论点。当整个前沿领域都在竞逐价格时，那些投入最多资金才达到这一高度的公司，损失也最惨重。

## 新模型各异，但共同的卖点是价格

周三，Elon Musk旗下的[SpaceXAI推出了Grok 4.5](https://thenewstack.io/grok-45-opus-killer-launch/)，这是该公司上市并吞并代码初创公司Cursor以来的首款模型。一天后，OpenAI[将GPT-5.6推向通用可用状态](https://openai.com/index/gpt-5-6/)，采用了类似于Anthropic的模型族架构：顶部的Sol、中间的Terra以及底部的Luna。同样不能被忽视的是，Meta在同一时间窗口发布了其[有史以来首个付费模型](https://thenewstack.io/meta-muse-spark-api)。

这些并非同一类型的模型。OpenAI以新的前沿基准测试领先。Musk称Grok 4.5是xAI迄今为止最聪明的模型。Meta将Muse Spark推销为一个具有广泛多模态能力的编程和智能体系统。它们的功能各不相同，但扫描一下发布文案，就会发现一个共同的论点：价格。OpenAI推销GPT-5.6时强调“每个Token带来更多智能”，并吹嘘Luna以大约四分之一的成本击败了Anthropic的Opus 4.6。Musk则将Grok宣传为Opus级别的模型，“但速度更快、Token利用率更高、成本更低”。[Sam Altman在CNBC上接受采访时](https://www.cnbc.com/2026/07/09/open-ai-sam-altman-chatgpt-5-6-sol.html)开篇提到的数字与智能无关：Sol在智能体编程方面的Token效率提高了54%，因为“每家企业现在都在考虑支出”。

这与几个月前的论调截然不同，那时新的前沿模型重新定义了可能性的边界，而价格只是事后考虑的问题。工程上的进步是真实的，但每个实验室这周在头条中强调的唯一突破却是账单。这些公司显然是在回应最近关于“AI可能无法提供足够的投资回报”的头条新闻。

## 逐底竞争的目标是参与者们

从下表可以看出这周真正发生了什么：

2026年7月8-10日，前沿模型价格概览

| 模型 | 价格 (输入 / 输出) | 价格定位 |
| --- | --- | --- |
| **GPT-5.6 Luna** (OpenAI) | $1 / $6 | OpenAI低成本层级 |
| **Muse Spark 1.1** (Meta) | $1.25 / $4.25 | Meta的激进切入 |
| **Grok 4.5** (SpaceXAI) | $2 / $6 | 对标Opus，但采取闪电模型定价 |
| **GPT-5.6 Sol** (OpenAI) | $5 / $30 | OpenAI旗舰款 |
| **Claude Opus 4.8** (Anthropic) | $5 / $25 | Anthropic旗舰款 |
| **Claude Fable 5** (Anthropic) | $10 / $50 | 高级编程层级 |

数据来源：截至2026年7月10日的公开API定价（每百万Token，输入/输出）。

Meta的信号最明确，因为它曾经是免费提供模型的。这周它首次开始收费，我们的同事Amanda Caswell捕捉到了Mark Zuckerberg的说法：Muse Spark 1.1的运行成本大约是OpenAI和Anthropic顶级模型收费的四分之一，而且“其他一些实验室的定价非常极端，利润率非常高”。这是一位前沿领域CEO公开抨击竞争对手的利润率。这不仅仅是产品发布，这是一场价格战。

那么，谁在为这一切买单？有人必须消化掉Fable每百万Token输出50美元与Grok每百万Token输出6美元之间不断扩大的经济鸿沟。目前，消费者正在受益。仅在SpaceXAI的基础设施业务中就能看到这种规模：Google是最近向Space支付算力费用的公司，[同意从10月开始每月支付9.2亿美元](https://techcrunch.com/2026/06/05/google-will-pay-spacex-920m-per-month-for-compute/)，以获取约11万个GPU及相关算力。

投资者也在问类似的问题。Meta在4月财报发布后[股价下跌](https://fortune.com/2026/04/29/meta-zuckerberg-145-billion-ai-spending-roi/)，当时该公司将其2026年的资本支出预期提高到了1450亿美元。而这周，由于Muse Spark的发布以及Meta新兴的API和基础设施业务让投资者更清楚地看到了这些支出可能带来的回报，[股价出现上涨](https://invezz.com/za/news/2026/07/09/meta-stock-rises-as-ai-chip-plans-and-muse-spark-11-rollout-take-focus/)。《华尔街日报》[报道称，OpenAI正在考虑](https://www.cnbc.com/2026/06/11/openai-mulls-slashing-prices-ahead-of-competition-from-anthropic-wsj.html)在面临Anthropic竞争之前进行“大幅”的Token定价削减，因为两家公司都在为可能的首次私募发行做准备。[Altman本人也表示](https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-ceo-sam-altman-admits-ai-token-costs-are-becoming-a-huge-issue-company-seeks-improved-value-as-overspending-becomes-a-meme)，在第一季度就烧光年度AI预算“几乎成了一个梗”。

这不是市场崩盘。但一家不断削减其耗资数十亿美元构建的产品价格的公司，并不一定在赢得胜利。它可能只是在参与一场它无法承受停下来的竞赛。

Anthropic似乎正在进行相反的押注：其最好的编程模型Fable 5现在的价格是每百万输入Token 10美元，每百万输出Token 50美元，是Opus价格的两倍，也是其有史以来定价最高的模型。底部正在向1美元滑落，而顶部正在升至50美元以上。中间地带正在被挤压。

## 优势属于那些能够灵活切换的人

价格战对买家有利，但前提是他们能够在不同模型之间进行切换。如果一个智能体消耗了五倍的Token、反复重试失败的任务，并将工作移交给另外六个智能体，那么1美元的模型并不便宜。正如Amanda Caswell在TNS上所言，[单个智能体任务可能运行15万到20万个Token](https://thenewstack.io/agentic-ai-token-costs/)，是普通对话成本的一千倍。我在几周前也指出了[同样的教训](https://thenewstack.io/claude-fable-cost-model-triage/)：在一次对比测试中，一个在GPT-5.5上花费1.5美元的工作，在Fable上运行成本高达9美元。

当一个50美元的模型能够一次性解决高成本问题时，它依然可能是经济的选择。重要的单位不再是单价（Price per token），而是完成任务的单价（Price per finished task）。

这要求技能从“找到最好的模型”转向“构建一个模型组合”。将大批量的工作路由到廉价模型；在测试证明确实物有所值的地方，支付高昂的推理费用；保留一个开放权重选项，用于敏感、高容量或对连续性要求极高的工作。并保持你的提示词、上下文和工作流的可移植性，以便在模型之间切换时不需要完全重写代码。

这些实验室在告诉我们不要产生品牌忠诚度。OpenAI一次性发布了三个性价比层级，Meta则通过压低竞争对手的价格入场。与此同时，SpaceXAI的卖点是它用更少的Token完成相当的工作。而Anthropic则押注编程工作值得支付溢价。

这些并不是同一个商业模式的四个版本。它们是让你在它们之间路由工作的邀请函。

现在判定这场价格战的赢家还为时过早。实验室将继续发布在定价、能力和推理方面相互超越的模型。

所以我将继续提醒你不要成为任何一方的狂热粉丝。

最好的模型会不断变化。持久的优势属于那些能够随之改变的人和组织。