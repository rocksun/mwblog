<!--
title: 目视检查的艺术：在图表中发现隐藏的故事
cover: https://cdn.thenewstack.io/media/2026/01/2536ece5-acm-luca-data_storytelling.png
summary: Angelica Lo Duca分享了通过目视检查从数据中提取洞察的方法，重点分析时间、空间和类别，强调发现数据背后的故事，利用峰值、趋势和阈值。
-->

Angelica Lo Duca分享了通过目视检查从数据中提取洞察的方法，重点分析时间、空间和类别，强调发现数据背后的故事，利用峰值、趋势和阈值。

> 译自：[The art of visual inspection: Spot the hidden story in your charts](https://thenewstack.io/art-of-visual-inspection-spot-the-hidden-story-in-your-charts/)
> 
> 作者：Joab Jackson

你有一组漂亮的数据，但如何将其意义传达给受众？

在最新一期的[免费技术讲座系列](https://learning.acm.org/techtalks-archive)中，计算机协会（ACM）邀请了[知名](https://scholar.google.com/citations?user=uAsnKo0AAAAJ&hl=it)研究员兼作家 [Angelica Lo Duca](https://alod83.medium.com/) 讨论“如何从数据中提取有意义的洞察”。

如果这个主题对于一个一小时的教程来说显得过于宽泛，你会被她如何有效地将其归结为几个关键原则而惊喜，这些原则可以用来为任何数据集赋予叙述性。

Lo Duca 提供了几种“启发式技术”来从数据中提取洞察。她告诉线上观众，在本次演讲中，她没有过多关注统计学基础；而是专注于通过目视图表（“目视检查”）可以学到的东西。她通过教授数据新闻学学生开发了这些技术。

Lo Duca 是意大利国家研究委员会信息与远程信息处理研究所的研究员，也是[《成为一名优秀的数据讲故事者：学习如何用数据推动变革》](https://www.wiley.com/Become+a+Great+Data+Storyteller%3A+Learn+How+You+Can+Drive+Change+with+Data-p-9781394283323)以及即将出版的[《学习Excel生成式AI工具：使用Microsoft Excel、Copilot、ChatGPT及其他工具加速日常任务》](https://www.oreilly.com/library/view/learning-generative-ai/9781098190163/)的作者。

她说，你在数据中发现的任何事物都是一个洞察。数据可以包含多个洞察，具体取决于你执行的分析。但在思考这些问题时，你希望一次只关注一个洞察。

她提供了三种数据分析方式：时间、空间和类别。

## 时间分析

时间分析研究[随时间变化的数据模式](https://thenewstack.io/how-time-plays-a-crucial-role-in-aggregating-mobile-data/)。在一个简单的X/Y分析中，时间段可以沿着水平Y轴流逝，而所有[在特定时间点捕获的事件](https://thenewstack.io/fluent-bit-a-specialized-event-capture-and-distribution-tool/)的聚合则在X轴上。

![截图](https://cdn.thenewstack.io/media/2026/01/a4393d7d-acm-lo_duca-01.png)

该图表显示了每年事件发生的次数，其中事件数量在2021年达到峰值。

然而，这里的洞察并非来自峰值点，而是来自事件每年开始增加的点（2014年）与开始下降的年份（2021年）之间的范围。故事就在这里。

一种方法是解释[启动这一趋势的起始事件](https://thenewstack.io/what-happens-to-relicensed-open-source-projects-and-their-forks/)发生了什么，然后解释结束事件发生了什么来终止这一趋势。

Lo Duca 建议，要找到这个故事，你通常需要跳出数据本身。解释可能存在于公共领域，例如在这些拐点发生的有趣新闻事件。也可能是公司内部发生的事件。

例如，在上面的图表中，数据可能与产品销售有关。因此，2016年可能是新销售活动的开始，而2021年则是新竞争对手进入市场的一年。

同样的分析也可以应用于负峰值，或图表中的最低点。

如果没有峰值，则比较线的起点和终点，计算两者之间的差异。故事就在那里；产品销售额可能增加了186%，或者下降了50%。

### 一切尽在掌握

但如果你的数据没有任何变化呢？你的时间线既没有上升也没有下降？如果它只是在波动呢？

这里面也有故事。

在这些情况下，Lo Duca 建议，你需要设置一个“阈值”，高于或低于所有数据。

如果数据线低于阈值，那么洞察就是“情况尽在掌握”。

日志系统就是基于这个理念运作的，只有当数据线突破阈值时，用户才会收到警报。此时情况就不再受控。

超过阈值？情况仍然失控。

## 空间分析

借助空间分析，你是在空间而不是时间中绘制点。

尽管时间分析寻找随时间变化，空间分析则[探索数据](https://thenewstack.io/the-rise-of-community-driven-data-analysis-in-the-age-of-ai/)如何在空间中移动。两者逻辑相同，但维度不同。两者都寻找峰值、趋势和稳定性。

在一个例子中，Lo Duca 展示了一张布满了数据点的欧洲地图。

拥有许多点的位置可以被称为“热点”。

通过比较不同位置可以获得洞察。为什么意大利的点比法国或德国多？这里的故事是什么？

![布满散布点的欧洲地图。](https://cdn.thenewstack.io/media/2026/01/86716dc7-acm-luca-data_storytelling-2.png)

你也可以通过[比较相邻区域](https://thenewstack.io/cloud-pue-comparing-aws-azure-and-gcp-global-regions/)来发现洞察。为什么意大利有这种特点，而西班牙却不那么明显？

她说，具有其他共性的位置也可以进行比较：“如果我分析天气，我可以查看具有相同气候的位置。”

对于没有热点的地图，你可以寻找梯度，它突出了特定方向的趋势。

可以从南到北穿过欧洲绘制一个梯度，这将使你能够测量极端值。（在这些情况下，请确保与比较区域相关的所有其他变量，例如[数据采样时间](https://thenewstack.io/how-time-series-data-empowers-telcos-to-stay-competitive/)，都相对相等。）

![一张欧洲地图](https://cdn.thenewstack.io/media/2026/01/a64bffa9-acm-luca-data_storytelling-3.png)

穿过欧洲的梯度。

没有梯度？没问题。使用前面描述的阈值。阈值可以从[历史模型数据](https://thenewstack.io/historical-data-and-streaming-friends-not-foes/)中导出，由法律或标准或其他外部因素定义。

## 比较类别

另一种数据比较形式是分类。不同类型的事物可以产生不同的数据点，这些数据点可以进行比较。

那么，洞察可能来自查看领先类别，并观察它与其他类别之间的差距。

![柱状图。](https://cdn.thenewstack.io/media/2026/01/35de2a8b-acm-luca-data_storytelling-4.png)

一组类别，其中有一个明确的领先类别。

在其他情况下，你可能没有一个显著领先的类别。但在这里，你可以通过查看类别的分布来获得洞察。每个类别之间的数值差异是什么？是否存在一组类别其值超过了其余类别？也许前五个类别占了90%的值。这就是一个洞察。

或者，你也可以使用你的老朋友——阈值，例如，将表现良好的类别与表现不佳的类别分开。

## 其他技巧

时间、空间和类别是Lo Duca在她的演讲中重点关注的三种分析类型。一旦她解释了它们，你就会发现它们是多么相似：

| 时间分析 | 空间分析 | 多类别分析 |
| --- | --- | --- |
| 峰值 | 热点 | 领先类别 |
| 趋势 | 梯度 | 排名 |
| 稳定性 | 均匀性 | 稳定 |

在演讲中，她还讨论了其他几种分析形式以及如何处理异常情况。与所有ACM技术讲座一样，本次讲座也是免费的，如果你想了解更多，可以听完整场讲座。

而且，如果你想让你的故事更精彩，还可以查看 Lo Duca 今年早些时候的演讲，[“将电影技术应用于数据叙事。”](https://learning.acm.org/techtalks/datastorytelling)