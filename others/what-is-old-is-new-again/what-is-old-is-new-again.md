
<!--
title: 旧瓶新酒
cover: https://substackcdn.com/image/fetch/w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ef76fc9-c27f-439b-a15b-5ebded516cfb_5463x3642.jpeg
-->

过去 18 个月，科技行业发生了重大变化。这对企业、开发团队意味着什么？未来务实的软件工程方法会是什么样子？

> 译自 [What is Old is New Again](https://newsletter.pragmaticengineer.com/p/what-is-old-is-new-again)，作者 Gergely Orosz。

过去 18 个月，科技行业经历了重塑。这对企业、开发团队意味着什么？未来务实的软件工程方法会是什么样的？

是什么导致了整个科技行业的突然变化？软件工程行业可能会因此发生怎样的变化？我在 2024 年 5 月在匈牙利布达佩斯举行的 [Craft Conference](https://craft-conf.com/) 上的年度会议演讲“旧事重提”中探讨了这些迫切的问题。如果您当时在场，希望您喜欢！本文包含完整的演讲内容、幻灯片和摘要。*我每年只做一次会议演讲，这是 2024 年的演讲。*

如果您有时间，可以查看下面刚刚发布的编辑后的录音。感谢 Craft Conference 团队的出色视频制作和活动组织！

[点击此处查看幻灯片](https://docs.google.com/presentation/d/1EHrQqQIA6pb8t1K8G6oJWED1rwa8F_lVJyWkOcXcubU/edit?usp=sharing)，[点击此处观看问答](https://www.youtube.com/watch?v=qYEhdZmPjsU)。

## 1. 发生了什么？

在过去两年中，科技行业的就业市场、风险投资资金、IPO 和大科技公司都受到了变化之风的强烈影响。

### 就业市场

2021 年底是史上最火热的科技招聘市场，正如 [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/perfect-storm-causing-a-hot-tech-hiring-market) 中所述：

> “如果您是需要招聘的招聘经理，您就会明白我的意思。申请的数量只有往常的一小部分，招聘难度更大，候选人要求的薪酬超出目标范围。您可能遇到过有人口头接受了工作，然后又因为更好的机会而拒绝的情况。一位市场上的招聘经理说：
>
> “以前从未如此困难，而且在所有地区都是如此。我记得几年前在印度看到过一个火热的市场。然而，目前的环境要强烈得多。我们在美国、英国、欧盟、东欧、南美洲……几乎所有地方都看到了同样类型的激烈竞争。我们预计这种情况会持续到今年年底。” – 一家在大多数大陆设有办事处的科技公司。

当时分析这种情况时，我概述了导致 [“完美风暴”](https://newsletter.pragmaticengineer.com/p/perfect-storm-causing-a-hot-tech-hiring-market) 的六个因素，这些因素将就业市场变成了求职者的天堂。

六个月后，即 2022 年 2 月，《纽约时报》（NYT）发表了一篇文章 [得出了类似的结论](https://www.nytimes.com/2022/02/16/magazine/tech-company-recruiters.html)，即科技公司面临着招聘危机。然而，当 NYT 意识到这一点时，就业市场已经开始快速变化……

2022 年 4 月和 5 月出现了意外的裁员：

- [一键结账初创公司 Fast 在一夜之间破产](https://newsletter.pragmaticengineer.com/p/the-scoop-fast)，在筹集了 1 亿美元资金后一年
- [Klarna 解雇了 10% 的员工](https://newsletter.pragmaticengineer.com/p/the-scoop-12)，这是一次意外的大规模裁员其他几家公司
- [随后](https://newsletter.pragmaticengineer.com/p/the-scoop-12)也进行了裁员：Gorillas、Getir、Zapp（即时配送）、PayPal、SumUp、Kontist、Nuri（金融科技）、Lacework（网络安全）等等。

2022 年秋季，大规模裁员仍在继续，Lyft、Stripe、CloudKitchens、Delivery Hero、OpenDoor、Chime、MessageBird 等公司 [裁员 10% 或更多](https://newsletter.pragmaticengineer.com/i/82363041/a-large-spike-in-layoffs)。

许多裁员都与一个共同点有关：它们发生在亏损的公司，因此比在盈利公司更容易被证明是合理的。

但随后，盈利公司也开始裁员。2022 年 11 月，Meta [解雇](https://newsletter.pragmaticengineer.com/p/the-scoop-32) 了 11,000 人（占员工总数的 13%），这是这家社交媒体巨头有史以来的首次裁员。几个月后，[谷歌](https://newsletter.pragmaticengineer.com/p/the-scoop-39)、[微软和亚马逊也纷纷效仿](https://newsletter.pragmaticengineer.com/p/google-job-cuts?)；造成了迄今为止最大规模的裁员潮。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f202c5b-a4d4-4146-a7b7-02e2dc2aa684_1600x670.png)

*2022 年底至 2023 年初科技行业裁员规模创下多年来新高。来源：[Layoffs.fyi](http://layoffs.fyi)*

### 风险投资资金

2020 年之前，风险投资对初创企业的投资一直在稳步增长。然后在 2021 年，投资速度爆炸式增长，几乎翻了一番：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9fb6f4c-d23e-4e7d-8f84-ea597ce58c1d_1600x730.png)

*风险投资年度投资额。来源：[Pitchbook](https://nvca.org/pitchbook-nvca-venture-monitor/)*


从那时起，风险投资一直在稳步下降。今年第一季度，风险投资水平与 2018 年持平！

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F295c357e-79f8-44ae-8b35-453c5fdb6823_1600x1066.jpeg)

### 首次公开募股

2021 年是科技公司上市的突出年份，因为相对大量的科技公司在股市上市。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff65f96ee-b098-4d93-95ad-100fdc629008_1210x906.png)

*2021 年 IPO 数量激增。来源：[Pitchbook](https://nvca.org/pitchbook-nvca-venture-monitor/)*

为了了解那一年有多少 IPO，这里列举了一些值得注意的 IPO：

GitLab（版本控制）、Rivian（电动汽车）、Couchbase（NoSQL 数据库）、Affirm（先买后付）、Bumble（约会）、Duolingo（语言学习）、Robinhood（交易）、Expensify（费用报销）、Nubank（金融科技）、Roblox（游戏）、Coinbase（加密货币）、Squarespace（域名）、Coupang（电子商务）、DigitalOcean（托管）、Toast（餐厅科技）、Coursera（教育科技）、Udemy（教育科技）、Amplitude（分析）、AppLovin（移动分析）、UiPath（自动化）、Monday.com（项目管理）、Confluent（数据流）、滴滴出行（网约车）、Outbrain（广告）、Nerdwallet（个人理财）。

相比之下，2022 年没有科技公司 IPO，[2023 年只有三家](https://newsletter.pragmaticengineer.com/p/the-pulse-62)（ARM、Instacart 和 Klaviyo）。当时我们并不知道，HashiCorp 在 2021 年 12 月的 IPO 是 18 个月以来的最后一次。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F68097da2-ac10-4f2f-b7b4-5668eafc23f2_1490x1012.png)

*自 2021 年以来，IPO 寒冬。来源：[Pitchbook](https://nvca.org/pitchbook-nvca-venture-monitor/)*

### 科技巨头

科技巨头在 2023 年初进行了大规模裁员，他们声称这是因为他们在 2020 年至 2022 年的疫情期间过度招聘。然而，到今年年初，科技巨头[仍在进行大规模裁员](https://newsletter.pragmaticengineer.com/p/the-pulse-76)，尽管他们没有过度招聘，并且利润创下历史新高。谷歌就是一个典型案例；该公司成立于 1998 年，在 2008 年之前只进行过一次大规模裁员，当时裁掉了 2% 的员工（300 人）。然后在 2023 年 1 月，大约 6% 的员工被裁掉了。在 2024 年 1 月，在收入和利润创下历史新高的背景下，这家搜索巨头再次裁员：

谷歌的做法似乎很典型；无论收入和利润如何创下历史新高，科技巨头似乎都习惯了定期裁员。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59131ad2-d8fc-4739-9542-eb8abd3d89fb_1600x949.png)

*谷歌在 2023 年和 2024 年连续裁员，尽管利润创下历史新高。舞台上图像来源：[谷歌是“新 IBM”吗？](https://newsletter.pragmaticengineer.com/i/141043954/is-google-the-new-ibm) *

我分析了当时这些裁员背后的原因，[写道](https://newsletter.pragmaticengineer.com/p/the-pulse-76)：

> “Meta、谷歌和亚马逊，并不是在无意义地裁员；他们似乎正在战略性地削减其[成本中心]和严重亏损的部门。此外，他们很可能正在淘汰表现不佳的员工。”
> 
### 总结

以下是我们正在看到的变化：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F96870e71-02c1-4df3-a682-799213dbfc9d_1364x592.png)

## 2. 为什么今天会发生这种情况？

大约在 2022-2023 年左右，有些事情发生了变化。但究竟是什么？

一个明显的候选原因是 2020-2021 年的疫情和封锁的结束，因为世界正在慢慢恢复正常。

当时，创始人、首席技术官告诉我他们的公司为什么裁员，以及他们的业务为什么突然面临增长挑战。“宏观经济环境”被反复提及，并在公司发布的裁员公告中得到呼应。很明显，利率的变化起到了比预期更大的作用。

2022 年年中，美联储（FED）做了一件几十年来从未做过的事情，大幅加息：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6059eb92-9223-413f-8b23-3017f4bd0f8d_1366x864.png)
*2022 年年中重大金融新闻。来源：[NPR](https://www.npr.org/transcripts/1105026915)*


#### 什么是利率，为什么利率会上涨？


我们需要稍微绕一下，才能理解利率。

我指的是国家中央银行设定的利率。在美国，这是美联储（美联储），在英国是英格兰银行，在欧盟是欧洲中央银行（ECB）。这些机构的目标是维护金融稳定，并执行政府财政政策，这可能是增加或减少消费者支出，增加或减少通货膨胀等。中央银行最强大的“杠杆”之一是设定适用于存款和债务的利率。

2022 年，通货膨胀率达到 40 年来的最高水平 [在美国](https://www.wsj.com/articles/us-inflation-june-2022-consumer-price-index-11657664129)（2022 年 7 月为 9.1%），30 年来的最高水平 [在英国](https://www.ons.gov.uk/economy/inflationandpriceindices/articles/newestimatesofcoreinflationuk/2022)（8 月为 8.6%），以及有史以来的最高水平 [在欧盟](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20230309-2)（2022 年为 9.2%）。这些地方的政府制定了财政政策，试图将通货膨胀率拉低至 2-3% 左右。美联储、英格兰银行和（ECB）都采取了相同的行动：他们提高了利率。

更高的利率如何减缓通货膨胀率？以下是 [BBC](https://www.bbc.com/news/business-57764601) 的解释：

> “英格兰银行上下调整利率以控制英国通货膨胀——即某物价格随时间推移的增长。
> 
> 当通货膨胀率很高时，英格兰银行（其目标是将通货膨胀率保持在 2%）可能会决定提高利率。这样做是为了鼓励人们减少支出，通过减少需求来帮助降低通货膨胀。一旦这种情况开始发生，英格兰银行可能会保持利率不变，或降低利率。
>
> 英格兰银行必须在减缓价格上涨的必要性与损害经济的风险之间取得平衡。”

将“英格兰银行”替换为“美联储”或“ECB”，道理是一样的。提高利率是全球范围内应对通货膨胀的久经考验的方法。

### 为什么更高的利率很重要？

在美国，利率在不到一年的时间里从几乎 0% 上升到 5% 左右：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5c003be9-555a-419a-9e4a-a01f124b82c4_1596x694.png)

*2021 年以来的美国利率。来源：[FRED](https://fred.stlouisfed.org/series/FEDFUNDS)*

为了了解这种利率变化是否属于“正常情况”，让我们回顾一下过去 15 年左右的情况：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc2fa7c6-cf9f-40aa-910c-afa071191247_1600x754.png)
*2009 年以来的美联储利率。来源：[FRED](https://fred.stlouisfed.org/series/FEDFUNDS)*

这张图表令人大开眼界。从 2009 年开始，利率接近 0%，然后在 2017 年至 2019 年间攀升至约 2%。之后，由于疫情，利率迅速降至零，因为美联储试图抑制储蓄，鼓励消费，以刺激经济并避免衰退。

现在让我们将时间轴拉回到 1955 年，看看随着时间的推移，“正常”利率通常是多少：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2b9efeb-948d-492f-a896-ffadb2890651_1600x660.png)

*美国利率自 1955 年起。来源:[FRED](https://fred.stlouisfed.org/series/FEDFUNDS)*

上图中一个“哇”点表明，超低利率在历史上并不常见。让我们标记利率在 1% 或以下的时期：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d95b485-0204-4d3c-8c9f-9c5efdc07883_1600x894.png)

*美国利率为 1% 或更低时的时期*

自 1955 年以来，共有 11.5 年的超低“接近零”利率，其中 11 年发生在 2009 年之后。这就是为什么它被称为零利率时期 (ZIRP)。

有趣的是，这种 ZIRP 并非美国独有。由于 2007-2008 年的全球金融危机 (GFC)，金融体系经历了濒临死亡的体验，加拿大、英国和欧盟也发生了非常类似的事件。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43816d92-9dd0-4e3b-9f50-d1d6c0178e50_1456x1009.png)

*自 2000 年以来，美国、加拿大、欧盟和英国央行隔夜借贷利率。来源:[0% 利率的终结及其对科技行业的影响](https://newsletter.pragmaticengineer.com/p/zirp)*


## 3. 利率对科技初创企业的影响
人们很容易认为科技与金融和利率无关，但事实恰恰相反。这不是我说的，而是彭博分析师和专栏作家 [Matt Levine](https://mattlevine.co/)，他对科技行业充满热情，并解释了财政政策如何影响行业。在 2023 年，[他分析了](https://www.bloomberg.com/opinion/articles/2023-03-10/startup-bank-had-a-startup-bank-run)硅谷银行的倒闭：

> “初创企业是低利率现象。当利率普遍较低时，20 年后的 1 美元与今天的 1 美元价值相当，因此，一家商业模式为“我们将损失 10 年的资金来开发人工智能，然后在未来获得大量资金”的初创企业听起来相当不错。
>
> 当利率较高时，今天的 1 美元比明天的 1 美元更有价值，因此投资者希望获得现金流。(...)
>
> 如果一些有魅力的科技创始人曾在 2021 年来到你 [银行] 那里，并说“我将通过 [人工智能][机器人出租车][飞行出租车][太空出租车][区块链] 来改变世界”，你可能会觉得回答“不，但如果美联储将利率提高 0.25% 会怎么样？”很不自然。这是一个对人类未来的愿景充满激情的行业，而不是对利率的押注。
> 
> 事实证明，这确实是对利率的押注。”

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf161baa-9a86-496e-bdf1-888ccae960cd_1600x1066.jpeg)

*在 Matt Levine 的引言在大屏幕上的舞台上*

当我读到这篇分析时，我的本能是反驳。利率和科技初创企业之间不可能有如此基本的联系？然而，我越想越觉得莱文说得有道理。

让我们分析一下当利率从 0% 迅速上升到 5% 时会发生什么，就像现在一样：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb395d4d2-4940-4505-b6dc-c0db8bb68a7d_1600x726.png)

*在突然上调利率后会发生什么？*

让我们也看看本通讯涵盖的主题，如风险投资资金、IPO、大型科技公司和就业市场，以及利率如何影响它们：

- **风险投资资金减少**：风险投资是一种高风险/高回报的投资类型，大型养老基金和超高净值人士会投资这种类型。其理念是将一大笔资金（例如 1 亿美元）投入风险投资基金，等待大约 10 年获得丰厚的回报。投资可能会变成 1.5 亿美元、2 亿美元等等。另一种选择是将其存入银行，但这会侵蚀其价值，因为年度通货膨胀（例如 2%）会逐年降低美元的购买力。但以 5% 的利率，你几乎可以无风险地将 1 亿美元变成 1.5 亿美元；那么为什么还要投资风险较高的科技初创公司——其中一些会成功，一些会失败——并冒着在十年后获得的资金少于初始投资总额的风险呢？
- **科技公司 IPO 减少**：科技公司上市通常处于亏损状态，因为它们仍处于增长阶段；2021 年上市的大多数科技公司都属于此类。在高利率环境下，投资它们不太诱人，因为除非它们有*明确*的盈利路径：否则它们可能会资金耗尽，从而贬值你的投资。*Rivian 的市值*相比之下，投资者只需将资金存入银行，就可以获得有吸引力的利率。[从 2021 年的 1500 亿美元跌至 2024 年的 100 亿美元](https://newsletter.pragmaticengineer.com/i/143712983/rivian-in-trouble)——部分原因是资金耗尽的风险——就是一个这样的警示案例。
- **大型科技公司利润推动**：在零利率时期，“基准”回报率为 0%。当该基准上升到 5% 时，盈利公司需要更高的利润率才能维持其估值。这意味着大型科技公司更积极地削减成本，以使他们的利润看起来更好，即使已经非常盈利。
- **就业市场恶化**：这是由于大型科技公司裁员以及初创公司招聘减少，因为可用的风险投资资金减少。

让我们将这些与本文第 1 部分中描述的过去两年的变化进行比较；“到底发生了什么？”

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa906074b-6d7e-4188-96f8-f5b71f747d55_1182x530.png)

*利率突然上涨时，科技行业在逻辑上应该发生的事件*

比较我们逻辑上应该随着利率上升而发生的事情，以及我们目前看到的事情：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa03669d0-a25e-4b3b-8b35-d8486ee33cb3_1980x684.png)

*预期与实际。它们几乎相同！*

这可能出乎意料，但利率上升解释了科技市场中的许多趋势。

## 4. 智能手机和云革命

从 2009 年左右开始的利率下降推动了更多风险投资进入初创公司，因为当利率处于历史低点且政府债券的回报率很低时，风险投资更具吸引力。在全球金融危机发生时，另外两个因素也开始产生影响。

### 智能手机革命

iPhone 于 2007 年推出，现已停产的 Windows Phone 两年后推出。智能手机改变了消费科技，并成为移动优先科技公司的催化剂，例如 Spotify（成立于 2006 年）、WhatsApp（2009 年）、Instagram（2010 年）、Uber（2010 年）、Snap（2011 年）等等。

### 云革命

大约在智能手机出现的同时，第一批云提供商也推出了：

- 2006 年：AWS
- 2008 年：Azure
- 2008 年：Google Cloud

云提供商使初创公司更快、更便宜地构建产品。他们无需购买和运营本地服务器，只需租用虚拟服务器即可。如果他们需要更多容量，他们只需付费并立即扩展。亚马逊早期员工 Joshua Burgin（现任 VMWare 工程副总裁）在[现代后端实践的过去和未来](https://newsletter.pragmaticengineer.com/p/the-past-and-future-of-backend-practices)中描述了这一点：

> “这种[云]转变使 Netflix、Lyft 和 Airbnb 等早期 AWS 客户能够获得与成熟科技巨头相同的计算能力，即使这些初创公司还处于起步阶段。你只需要一张信用卡，就可以立即开始，而无需采购订单 (PO)、数月的交付周期以及庞大的 IT 部门或托管服务提供商。”

如今，一些最知名的 AWS 客户包括 Netflix、Airbnb、Stripe 和 Twitch。所有这些公司都通过利用云技术实现了更快的增长——并且可能需要更少的资金。

### 重叠

智能手机和云革命几乎与利率降至零并在此后十年保持在冰点的时间完全一致：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8b298810-85a4-4df5-9ebf-acbc7a18c0c9_1600x961.png)

*智能手机和云革命中与利率相关的关键事件*

这些发展给了风险投资家更多理由投资初创公司：


- 出现了新的移动优先初创公司类别，如果它们快速发展，就有可能成为价值数十亿美元的公司。筹集大量资金对于赢得市场至关重要；Uber 和 Spotify 通过这种策略取得了成功。
- 初创公司可以通过将资金投入云技术来解决扩展问题，而不是花费数年时间构建自己的基础设施，从而更有效地将投资转化为增长。这是风险投资帮助初创公司赢得各自市场的另一种方式。

由于0%利率持续时间最长且两个技术革命在那时开启，2010年代很可能是科技初创企业的黄金时期。

今天，另一场潜在的技术革命正在升温：生成式 AI 和大型语言模型 (LLM)。AI 革命与云革命有相似之处，因为 AI 也可能带来效率提升（一旦 AI 成本从现在的水平下降）。然而，AI 革命在本质上与智能手机革命截然不同：这是因为 AI 似乎没有像智能手机那样为应用开发者提供一个新的、最初免费的、广泛的传播渠道。而且，GenAI 革命也始于高利率环境：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febfc322d-9500-488c-ac05-fe9973dc46f4_1600x944.png)

*GenAI革命（ChatGPT发布等）发生在高利率环境中。*

我们在以下文章中更详细地介绍了 GenAI 的“如何”：

- [Inside OpenAI: how does ChatGPT ship so quickly?](https://newsletter.pragmaticengineer.com/p/inside-openai-how-does-chatgpt-ship)
- [Scaling ChatGPT: five real-world engineering challenges](https://newsletter.pragmaticengineer.com/p/scaling-chatgpt)
- [Applied AI software engineering: RAG](https://newsletter.pragmaticengineer.com/p/rag)

## 5. 新现实

那么，我们所处的“新现实”是什么？[查看演示文稿的这一部分](https://youtu.be/VpPPHDxR9aM?si=F87B-4mKuikca9qc&t=1257)了解我对软件工程师和工程实践意味着什么的看法。

基本上，对于软件工程师来说，找到工作更难，职业发展也更慢。对于工程实践，我们可能会看到一种趋势，即选择“无聊”的技术，单体架构变得更加流行，“全栈”和 Typescript 获得更多动力，以及更多责任“左移”到开发人员身上。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff21e152c-8101-41d9-ab67-be425725ead2_1600x1066.jpeg)

*软件工程实践将如何改变？观看[此处完整片段](https://youtu.be/VpPPHDxR9aM?si=Xt2aZd6Nz7VykiV7&t=1558)*


之前的通讯更深入地介绍了这一点：

- [What the end of 0% rates means for software engineers](https://newsletter.pragmaticengineer.com/p/zirp-software-engineers)
- [What it means for software engineering practices](https://newsletter.pragmaticengineer.com/p/zirp-engineering-practices)

## 6. 历史重演？

变化往往陌生而意外。那些经历过 2001 年互联网泡沫破裂的人一定能看到今天与当年科技泡沫破裂带来的突然变化之间的相似之处。在那段时间工作的软件工程师提供了关于如何在工作保障感难以控制的情况下优先考虑职业安全的视角和战术建议。

## 7. 问答、幻灯片和进一步阅读

要回顾演讲后的问答，[请查看此录音](https://www.youtube.com/watch?v=qYEhdZmPjsU)。

[访问演示文稿幻灯片。](https://docs.google.com/presentation/d/1EHrQqQIA6pb8t1K8G6oJWED1rwa8F_lVJyWkOcXcubU/edit?usp=sharing)

我已经在单独的分析文章中详细介绍了演讲中的几个主题。更多内容，请查看：

- [What the end of 0% interest rated means for the tech ](https://newsletter.pragmaticengineer.com/p/zirp)industry
- [What it means for engineering managers](https://newsletter.pragmaticengineer.com/p/zirp-engineering-managers)
- [For software engineers](https://newsletter.pragmaticengineer.com/p/zirp-software-engineers)
- [For software engineering practices](https://newsletter.pragmaticengineer.com/p/zirp-engineering-practices)

## 结论

有时，从“放大”的角度来看待技术领域正在发生的变革，以便更好地理解它，这是很有帮助的。0% 利率的消亡是一个重大事件，对科技行业产生了显著影响。很难预测未来——尤其是在技术领域，事物变化很快——但我发现，了解影响该行业发展方向的潜在力量很有用。

从一个角度来看，科技行业的历史就是周期性繁荣和萧条的历史。创新是新商业机会的沃土，我毫不怀疑未来会有很多繁荣时期；我们只需要在它们发生时认清它们！

在主题演讲之后，有几个人告诉我，它让他们“豁然开朗”，包括他们在工作中、朋友的工作场所以及在就业市场上的经历。一位参与者说，他们正在计划自己的下一个职业步骤，了解正在发生的变化趋势有助于他们做出更明智的决定：

> “用足球的比喻来说：我想跑到球将被射向的地方，而不是大多数球员正在看的地方（球目前所在的地方）。我觉得我对科技行业‘球’在未来几年的走向有了更多信息，所以我可以更好地定位自己。”

我希望您发现这篇分析有见地，并且[演讲很有趣](https://www.youtube.com/watch?v=VpPPHDxR9aM)！

最后，非常感谢[Craft 大会](https://craft-conf.com/)邀请我。我问组织者今年大会的情况如何，他们分享了一些有趣的统计数据：

- **2,000 名与会者**：约 1,500 人现场参加，其余在线参加。
- **80 位演讲者**：其中 95% 来自国外。这个国际阵容吸引了我参加这个活动。
- **49 个国家**的参与者，包括德国、罗马尼亚、挪威、奥地利、荷兰、美国和塞尔维亚，以及当地专业人士。
- **60% 的参与者是软件工程师**，13% 是工程经理/团队负责人，10% 是架构师。
- **Javascript 和 Typescript**是与会者中最受欢迎的编程语言。Java、Python、C#、C+++、PHP、C、Go 和 Kotlin 的受欢迎程度紧随其后。

该活动是年度活动，下一届将于 2025 年春季举行。