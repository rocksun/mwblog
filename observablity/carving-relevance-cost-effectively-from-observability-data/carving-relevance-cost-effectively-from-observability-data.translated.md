# 从可观测性数据中经济高效地挖掘相关性

![从可观测性数据中经济高效地挖掘相关性的特色图片](https://cdn.thenewstack.io/media/2025/02/ecd12a95-sculpture-1024x576.jpg)

随着可观测性数据以惊人的速度增长，总部位于旧金山的初创公司[Sawmills](https://www.sawmills.ai/)认为，一个新的类别正在出现，以管理数据量并使其更有用。

“团队淹没在遥测数据中，耗尽了预算，但仍然难以获得真正的见解。我们构建 Sawmills 来解决这个问题——智能遥测管理，可以在数据到达您的可观测性堆栈之前对其进行过滤、丰富和路由，”联合创始人兼首席产品官 Erez Rusovsky 在 [LinkedIn 帖子](https://www.linkedin.com/feed/update/urn:li:activity:7298011381256138752/)中写道。

该公司强调，它不是可观测性供应商，而是位于数据摄取和可观测性产品之间。它在 [OpenTelemetry Collector](https://thenewstack.io/how-the-opentelemetry-collector-scales-observability/) 之上使用 AI，OpenTelemetry Collector 是一种可观测性管道中间件，可以大规模接收、处理和导出数据，然后添加功能以消除无用或重复的数据，设置发送给所选供应商的数据量的护栏，并推荐更有效地使用遥测数据的方法。

![Sawmills 联合创始人 Amir Jakoby, Ronit Belson and Erez Rusovsky](https://cdn.thenewstack.io/media/2025/02/9aeff040-sawmills-team2-300x169.jpg)

Sawmills 联合创始人 Amir Jakoby, Ronit Belson and Erez Rusovsky

“让我们相信我们想要进入这一领域的一个重要点是……我们了解到新技术，AI 等，创造了一个新的机会，以我们认为我们的目标受众真正想要的方式来解决问题。DevOps 不想要另一个他们需要配置的工具，因此以智能方式执行此操作的能力是解决方案的重要组成部分，”Sawmills 首席执行官 Ronit Belson 说。

**太多太多的数据**

特别是微服务架构正在产生大量数据，但可观测性供应商按摄取的数据量收费，导致巨额账单——例如，一位毫无戒心的客户向 [Datadog 支付了 6500 万美元](https://thenewstack.io/datadogs-65m-bill-and-why-developers-should-care/)。

[日志数据平均同比增长](https://chronosphere.io/learn/observability-log-data-trends/) 250%，2024 年 [Chronosphere](https://chronosphere.io/?utm_content=inline+mention) 调查的受访者报告说，22% 的人表示他们每天创建 1 TB 或更多的日志。加上事件、跟踪和其他指标的数据，数据量显然变得不可持续。然而，这些调查受访者坚持认为，他们正在努力从这些数据中获得有用的见解。
虽然从历史上看，存储所有数据一直是可行的方法，以免将来出现问题并且需要它来查明原因，但即使采用经济高效的存储，数据量也使其变得不可行。

Honeycomb 联合创始人兼首席执行官 Christine Yen 在最近一期的 [The New Stack Makers](https://thenewstack.io/whats-driving-the-rising-cost-of-observability/) 中解释说：“如今，许多工程团队都拥有混合存储和微服务，其中不同的组件以不同的语言和不同的框架编写。对于一种神奇的方法来说，越来越难以涵盖我们在现代基础设施中看到的广度。”

Gartner 的一份报告显示，因此，大型组织正在转向[遥测管道](https://thenewstack.io/observability-can-get-expensive-heres-how-to-trim-costs/)，以聚合和处理来自多个来源的数据，该报告建议关注这种策略的价值和投资回报率。

**解决海量数据量的痛点**

Sawmill 的联合创始人 Belson, Rusovsky 和 Amir Jakoby 都在 DevOps 方面拥有丰富的经验，他们最初的目标是建立一家基于工具的初创公司。但在与潜在公司的对话中，他们被告知数据量是最大的问题。他们震惊地得知只有大约 10% 的数据是有用的。数据质量（例如缺少数据点、格式不一致和重复数据）也是一个痛点。

Rusovsky 说：“很多数据是重复数据。想想一条重复了 1000 万次的出错消息。你需要 1000 万条消息吗？可能不需要。你可能需要一条消息来说，‘哦，这条消息重复了 1000 万次’，对吗？”

Belson 解释说，当你发送大量不需要的数据时，也会影响可观测性解决方案的有效性。
“使用大量质量不高的数据进行根本原因分析确实更加困难。因此，数据发送量以及您不一定需要的数据会产生很多问题，”Belson说。

OpenTelemetry Collector是“允许我们处理流中数据的引擎，我们在其之上构建了一个管理层，并在其之上构建了洞察力和智能层，”Rusovsky说。

该公司与客户合作，在他们自己的遥测管道上安装代理，将数据发送到[Datadog](https://www.datadoghq.com/?utm_content=inline+mention), [New Relic](http://newrelic.com/?utm_content=inline+mention), [Elastic](https://www.elastic.co/observability?utm_content=inline+mention)或任何地方。这些代理使用SaaS产品中的AI模型处理数据，自动识别减少支出和提高数据质量的机会，但Jakoby指出，Sawmills无法访问这些数据。客户完全控制数据的存储位置，并决定发送哪些数据。

“客户不需要支付出口费用，我们也不需要处理数据，花费CPU等……因此，对于任何浪费的东西，都不会产生额外的成本，”Jakoby说。

AI和机器学习被用于流数据和推荐引擎中。该引擎使用OpenAI或AWS Bedrock等专有工具，以及客户自己的基于云的大型语言模型。虽然AI/ML可以识别模式，但有些数据是公司开发的应用程序特有的，因此客户可以决定哪些数据是相关的。

客户可以设置数据发送量的警戒线，并在接近这些限制时收到警报。他们还可以一键应用Sawmills的建议，并设置自动策略来防止意外的超额使用和可用性问题。该架构还允许客户灵活地无缝切换可观测性供应商。

Rusovsky表示，当收到有关接近其中一个限制的警报时，可以采取多种措施：抽样、聚合或只是将数据发送到低成本存储，并通知团队决定如何处理。

“我认为人们越来越认识到客户想要拥有这些数据，”Belson说。“他们不希望可观测性解决方案拥有这些数据。”

## 抓住机遇
这家拥有10名员工的公司成立大约一年。CEO Belson之前曾担任Testim.io（被Tricentis收购）、Rollout.io（被CloudBees收购）和Cloudmeter（被Splunk收购）的首席运营官。CTO Jakoby之前曾担任New Relic的软件工程副总裁、SignifAI的工程总监、Preempt Security的首席安全工程师和以色列军事情报8200部队的软件工程经理。Rusovsky曾担任CloudBees的产品总监以及Rollout.io的CEO兼联合创始人。

Belson表示，该公司刚刚筹集了1000万美元的种子资金，预计在未来六个月内员工人数将翻一番。

它面临着来自SigNoz、Kloudfuse和Edge Delta等初创公司的竞争，以及[Cribl.io](https://cribl.io/?utm_content=inline+mention)，更不用说Datadog、New Relic、Elastic和[Splunk](https://www.splunk.com/en_us/products/observability.html?utm_content=inline+mention)等主要供应商也在加倍投入OpenTelemetry Collector数据。

“所有这些数据都不可能像这样不受管理，”Rusovsky说。“与此相关的有太多的问题，因此我们坚信现在正在形成一个管理这些数据的类别，我们希望抓住这方面的机会。”

最近领导种子轮融资的Team8的管理合伙人[Liran Grinberg](https://www.linkedin.com/in/lirangr/?originalSubdomain=il)称[遥测数据管理](https://team8.vc/rethink/cyber/sawmills-the-future-of-intelligent-telemetry-management)是一个快速出现、至关重要的新类别。
他在一篇博客文章中说：“解决成本很重要，但真正的挑战是治理、灵活性以及从收集的数据中获得可操作的见解的能力。Sawmills正在正面应对这一挑战。Sawmills团队对这个问题有着深刻的理解和全面的愿景，这使他们能够完美地拥有这个新类别。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)