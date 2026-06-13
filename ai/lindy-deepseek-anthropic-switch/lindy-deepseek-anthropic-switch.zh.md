**实现可持续AI部署的最大阻碍**已演变为[推理成本](https://thenewstack.io/confronting-ais-next-big-challenge-inference-compute/)。GitHub[最近放弃了](https://thenewstack.io/github-copilot-token-billing/)其Copilot的固定费率订阅，转而采用按需计费，原因是代理化编程会话导致的成本超出了固定月费所能承受的范围——一些订阅者醒来后发现账单比以往高出了数倍。与此同时，Uber在短短四个月内就[耗尽了其整个2026年的AI预算](https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/)，主要花在了Claude Code上，这让其首席运营官（COO）开始质疑这些回报是否值得如此投入。

为了应对这一广泛的清算，[Linux基金会启动了Tokenomics基金会](https://thenewstack.io/tokenomics-foundation/)——得到了Google、Microsoft、IBM、Salesforce等公司的支持——旨在围绕AI Token成本建立开放标准，这默认了企业目前缺乏衡量或控制欠费的统一方法。

## 切换开关

对于大规模运行AI代理的公司来说，前沿模型的经济学已几乎变成一个关乎生存的问题。

[Flo Crivello](https://www.linkedin.com/in/florentcrivello/)曾是Uber的工程师和产品负责人，现在是Lindy的创始人兼CEO。Lindy是一个无代码AI代理平台，能够自动处理日常工作任务——从邮件分拣、会议安排到CRM管理。Crivello在2023年创立了Lindy，这是从他之前的虚拟办公室初创公司Teamflow转型而来的，此前他已为Teamflow筹集了[5200万美元](https://www.teamflowhq.com/blog/teamflow-raises-35m-series-b)的资金——这笔资金现在正支持着[Lindy的发展](https://ff.co/flo-crivello-lindy/)。

![Lindy](https://cdn.thenewstack.io/media/2026/06/5d9a3984-lindya-1024x729.png)

*Lindy*

Crivello上周在社交媒体上[宣布](https://x.com/Altimor/status/2062389885437366342)，Lindy已将其整个模型基础设施从Anthropic切换到了DeepSeek。

> “为我们节省了数百万美元，而且我们实际上在许多核心用例中看到了性能的提升。”

“今天按下了开关，将Lindy 100%的流量切换到了DeepSeek v4，从Anthropic模型中流失，”Crivello在X上写道。“为我们节省了数百万美元，而且我们实际上在许多核心用例中看到了性能的\*提升\*。这对业务具有变革意义。”

事实上，Crivello在几个月前就[表达过他的意图](https://x.com/Altimor/status/2024166557107311057)。他在4月的[X贴文](https://x.com/Altimor/status/2044108104816832576?s=20)中写道，推理是Lindy最大的单项成本——甚至超过了员工薪资——而且开源模型在一年时间内已经从“完全比不上”发展到了在大多数用例中“处于前沿水平”。当时，他表示Lindy曾接近将[Kimi K2.5](https://www.kimi.com/ai-models/kimi-k2-5)（来自中国AI公司[月之暗面](https://www.moonshot.ai/)的模型）作为默认选项，之后又转向了由北京智谱AI开发的[GLM-5.1](https://z.ai/blog/glm-5.1)。

最终，该公司选择了[DeepSeek v4](https://deepseek.ai/deepseek-v4)，这是来自中国AI研究公司DeepSeek的一款旗舰开源模型。

当然，在全量生产环境下从一家模型提供商切换到另一家并非易事。Crivello告诉*The New Stack*，完成迁移的时间取决于从什么时候开始算起——但无论如何，这都是一项重大任务。

> “我们已经考虑进行这种切换并评估新的开源模型有6到9个月了。”

“我们已经考虑进行这种切换并评估新的开源模型有6到9个月了，而对DeepSeek的评估是从它发布起开始的，大约是2个月前，”Crivello解释道。

值得注意的是，这次迁移被证明比Crivello最初预想的要苛刻得多——正如他所说，“工作量比我们预想的大100倍”。评估工作是其中的主要部分，即在真实任务中系统地测试新模型，以验证它是否能达到或超过Anthropic模型之前的表现。

![](https://cdn.thenewstack.io/media/2026/06/a8724953-1776918947306.jpg)

Flo Crivello，Lindy创始人兼CEO

“为了评估模型做了大量工作，包括线上评估、线下评估以及海量的‘氛围评估’，”Crivello说。“[然后我们]进行了分阶段推广，既是为了线上评估，也是为了观察对留存率的影响；并且[随后]让我们的提示词去适配这个新模型。”

如果仅仅是为了节省成本，这种努力可能很难证明其合理性——但性能结果给了Crivello额外的信心，尤其是在其核心用例中，包括电子邮件收件箱分拣和基于用户语气的回复预草拟。

“这正是我们在DeepSeek上看到令人惊讶的性能提升的地方，”Crivello解释道，并补充说DeepSeek在某些复杂的自动化任务上仍然落后于Anthropic。

“在‘工作流自动化’方面，它仍然不如[Sonnet](https://thenewstack.io/claude-sonnet-46-launch/)，但这由于我们来说是次要的，”他说。

## DeepSeek时刻

要理解为什么Lindy的切换如此重要，有助于了解DeepSeek在AI行业中代表了什么。

DeepSeek在[2025年1月](https://www.forkable.io/i/155825266/the-open-source-ai-debate-deepens-a-sputnik-or-google-moment)给硅谷带来了震动，当时其R1模型以极低的成本达到了美国领先前沿模型的性能——这引发了Nvidia股票的短暂但剧烈的[抛售](https://www.bbc.co.uk/news/articles/c0qw7z2v1pgo)，因为投资者开始质疑关于AI算力需求的假设。随后是一连串的发布，不断缩小与前沿领域的差距。

DeepSeek v4在[2026年4月发布预览版](https://api-docs.deepseek.com/news/news260424)，标志着进一步的跨越——不仅仅是在价格上。瑞士洛桑联邦理工学院（EPFL）教授、EPFL AI中心联席主任[Marcel Salathe](https://www.linkedin.com/in/salathe/)在[LinkedIn上指出](https://www.linkedin.com/posts/salathe_deepseek-v4-for-the-first-time-a-frontier-class-activity-7453409089885429760-zJir/)，v4从地缘政治角度来看更具意义：第一次出现了一个从芯片、框架到模型完全由中国自主研发的前沿级AI技术栈。DeepSeek似乎[花费了数月时间重写](https://www.scmp.com/tech/big-tech/article/3351349/huawei-deepseek-strengthen-chinas-ai-self-reliance-collaboration-v4-model)v4，使其运行在[CANN](https://developer.huawei.com/consumer/en/doc/hiai-guides/introduction-0000001051486804)（华为对标Nvidia CUDA的架构）上，从而[减少了其对美国芯片基础设施的依赖](https://www.reuters.com/technology/chinas-deepseek-returns-with-new-model-year-after-viral-rise-2026-04-24/)。

这种地缘政治转变具有直接的商业后果。正如*The New Stack*[此前报道](https://thenewstack.io/disappearing-ai-middle-class/)的那样，主要来自中国AI实验室的廉价开放权重模型的出现，已将AI模型市场分成了两个集群：来自OpenAI和Anthropic等的超高端前沿模型，以及价格大幅降低的开放权重替代方案——中间地带正在变薄。数据证明了这一点：在应用和AI提供商之间路由流量的Vercel AI Gateway记录到，DeepSeek的Token流量份额在5月份的单月内[从不到1%飙升至17%](https://vercel.com/blog/ai-gateway-production-index-june-2026)，而其在实际支出中的份额仍维持在1%左右，这反映出这些Token的供应价格是多么低廉。

对于像Lindy这样大规模运行代理的公司来说，这种两极分化迫使他们必须权衡选择哪种经济模式。对于Lindy的创始人来说，当推理账单已经超过了员工薪资时，这个问题其实只是时间问题。

Lindy最终选择了[Atlas Cloud](https://www.atlascloud.ai/)，这是一家总部位于美国的推理供应商，它在美国本土[托管DeepSeek v4](https://www.atlascloud.ai/models/deepseek)——考虑到围绕中国开发模型的常见数据主权问题，这是一个重要的细节。Crivello在回应[X上的一位评论者](https://x.com/parenth_/status/2062559294101524603?s=20)时[直接提到了这一点](https://x.com/Altimor/status/2062565063312199867?s=20)，指出该模型由一家美国供应商在美国境内托管——而且在评估了“所有主要玩家”之后，[Atlas脱颖而出](https://x.com/Altimor/status/2062423820636672069?s=20)。值得一提的是，自建托管从未在考虑范围内。

“我们没有认真考虑过[自建托管]，没有——那看起来会是一个巨大的干扰，”他说。

> “我们没有认真考虑过自建托管……那看起来会是一个巨大的干扰。”

## 跑道与未来计划

虽然Crivello表示这次切换最终将为Lindy节省数百万美元，但对于一家风险投资支持的公司来说，这对资金跑道的影响是巨大的。

具体节省了多少？“非常多，”这是Crivello愿意透露的全部。
  
至于此举是否是永久性的，Crivello没有给出定论。“生活中没有什么事是永久的，”他说。“如果Anthropic的下一次发布赢回了我们的业务，我不会感到惊讶，但他们需要大幅降价。”

> “如果Anthropic的下一次发布赢回了我们的业务，我不会感到惊讶，但他们需要大幅降价。”

同样值得注意的是，Lindy仍然是Anthropic的客户——只是不再将其用于核心产品。该公司在内部仍在使用Claude，因为订阅模式的经济性使其可行。

“我们的内部使用主要是基于[Max计划](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)——如果不是因为这个计划，如果我们必须支付全额Token费用，我们就会换成别的，”Crivello说。

在回答Amp CEO兼创始人[Quinn Slack](http://linkedin.com/in/quinnslack)[提出的关于](https://x.com/sqs/status/2062393582091424058?s=20)Lindy最终是否可能被迫在其外部产品中换回Anthropic模型的问题时，Crivello暗示大门并未完全关闭。“当我们检测到Lindy在某项任务中失败时，我们可能仍会升级到Opus，”他[写道](https://x.com/Altimor/status/2062398729349628162?s=20)，“但那将是边际性的。”

Crivello的观点是，处于Lindy这种位置的公司——Token的大量消耗者——除了采取行动外别无选择。“像我们这样在Token上花费巨大的公司，100%会这样做——不这样做就是不负责任，”他说。“其他公司则取决于情况，但我认为很多人只是坚持使用品牌知名度高的产品。”