
<!--
title: 云金丝雀助力可观测性腾飞
cover: https://cdn.thenewstack.io/media/2024/07/5841b1b9-bird-3386323_1280.jpg
-->

这家初创公司刚刚走出隐身状态，提供轻量级代理、神经网络和开放平台，作为现有工具提供商更便宜、更快、更高效的替代方案。

> 译自 [Observability Takes Flight With Cloud Canaries](https://thenewstack.io/observability-takes-flight-with-cloud-canaries/)，作者 Jeffrey Burt。


# 云金丝雀让可观测性腾飞

![云金丝雀可观测性功能图片](https://cdn.thenewstack.io/media/2024/07/5841b1b9-bird-3386323_1280-1024x682.jpg)

[可观测性](https://thenewstack.io/observability/) 平台对于 [DevOps](https://thenewstack.io/devops/) 团队来说越来越重要，他们正在努力应对部署频率的加速和对从 [安全和合规性](https://thenewstack.io/chef-extends-security-and-compliance-across-hybrid-cloud/) 到 [治理和风险](https://thenewstack.io/governance-risk-and-compliance-with-kubernetes/) 的一切的扩展关注。这些平台为软件工程师提供了对其软件系统健康状况和性能的洞察，为他们提供了理解哪些有效——同样重要的是，哪些无效——修复问题并相应地调整其应用程序和服务的工具。但它们并不便宜，它们很复杂，并且被锁定在销售它们的供应商手中。

[Mark Callahan](https://www.linkedin.com/in/mark-callahan-1945b53/) 三年前创立了 [Cloud Canaries](https://cloudcanaries.ai/)，旨在开发一种开放的、基于人工智能的服务，可以像这些大型平台一样做同样的事情，只是更快、更便宜、更高效。该公司本月从隐身状态中脱颖而出，提供轻量级代理——称为智能金丝雀——可以轻松地启动并发送到云或互联网中，以收集这些大型平台收集的相同信息，以检测软件系统中的问题，提供实时性能监控、预测问题并确定解决问题的方法。

这些金丝雀利用该初创公司的 [神经网络](https://thenewstack.io/airbnb-builds-a-second-neural-network-to-diversify-listings/)，并且可以通过 Cloud Canaries 的 [Aviary 平台](https://cloudcanaries.ai/features/) 创建、安排、部署和管理，该平台收集传入数据并包含用于评估端点、服务和 [API](https://thenewstack.io/api-management/) 健康状况的仪表板，以及对 SLA 的合规性和预测，使用五天滚动复合、服务和金丝雀预测，使软件工程师能够主动解决问题。

开发人员可以将他们的金丝雀在组织内部与其他人共享，或者将金丝雀公开并与公司外部的其他人共享。他们还可以将他们的金丝雀上传到 Cloud Canaries 的系统中，创建所谓的“模板金丝雀”。

“我们提供的平台可以做几件事，”Callahan 告诉 The New Stack。“如果你有金丝雀或共享金丝雀，你可以真正实现主要供应商提供的相同解决方案，但你可以非常快地做到这一点。你可以在几分钟内创建一只金丝雀。……你可以分配环境变量，你可以分配阈值，你可以发送通知，你可以分配时间表，然后你可以将它放在 [Kubernetes](https://thenewstack.io/kubernetes/) 集群中，或者你可以将其变成一个‘金丝雀代理’，它可以在你编译它的任何地方执行，你把它放在任何你想放的地方，它只是收集数据。”

## 将数据馈送到 AI 模型

这些数据可以被馈送到该公司的 [神经网络](https://thenewstack.io/airbnb-builds-a-second-neural-network-to-diversify-listings/) 中，或者被保存到来自 [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) 等供应商的第三方 AI 模型中，例如 Snowflake 的 Cortex，这是一套基于其大型语言模型的 AI 工具，或者来自 Databricks、New Relic、DataDog 和其他供应商的 AI 模型。

Cloud Canaries 为“公司和企业提供了两全其美的选择——能够构建这些金丝雀并快速共享它们……以及以某种订阅价格获得更复杂的金丝雀，并拥有一个可以管理它们并最重要的是收集数据的平台，”他说。

Callahan 在他在 [Oracle](https://developer.oracle.com/?utm_content=inline+mention) 的 17 年多时间里最后三年中熟悉了金丝雀的概念，当时他是 [Oracle 云基础设施](https://thenewstack.io/oracle-touts-new-appdev-tools-distributed-cloud-support/) 的开发经理。金丝雀是用 Python、Java 或其他编程语言编写的，模拟用户工作负载并分派到软件系统中，以帮助 DevOps 团队和开发人员从用户的角度了解正在发生的事情。
他带着这个想法加入了 Cloud Canaries，与一众提供 [可观测性平台和工具](https://thenewstack.io/next-gen-observability-monitoring-and-analytics-in-platform-engineering/) 的老牌公司展开竞争，包括 [IBM](https://www.ibm.com?utm_content=inline+mention)、Splunk、Datadog、[亚马逊](https://aws.amazon.com/?utm_content=inline+mention)、Sumo Logic 和 [思科](http://cisco.com/?utm_content=inline+mention) 的 AppDynamics。这是一个庞大且不断增长的市场，MarketsandMarkets 预测该市场将从去年的 24 亿美元增长到 [2028 年的 41 亿美元](https://www.marketsandmarkets.com/Market-Reports/observability-tools-and-platforms-market-69804486.html)。

## 对速度的需求
Callahan 表示，Cloud Canaries 的竞争优势包括速度——金丝雀可以在几分钟内创建——开放平台，以及基于订阅的计划，他表示该计划将以可观测性平台成本的 10% 解决最常见的用例，这些平台需要针对其环境进行调整，并收集、存储和分析来自日志、指标和跟踪的数据，所有这些都是为了获得对软件系统操作的视图。对系统性能的洞察来自基于数据的事件和 KPI 测量。

“我和客户谈过，”他说。“Oracle 为一个席位花费了 10 万美元，而你可以在我的平台上用一些金丝雀做到这一点。一旦平台开发完成，每个人都在为计算建模付费，所以我现在可以做到 10%。我们从许多不同的开源软件平台获取诊断信息，[[Python 的] Django](https://thenewstack.io/what-is-pythons-django/) 和 Kubernetes，并且我们可以通过开放的 API 架构生成金丝雀。”

使用 Cloud Canaries 的开发人员可以快速创建自己的金丝雀，或者进入金丝雀模板库，找到他们想要使用的金丝雀并进行剪切粘贴。Callahan 说，这很容易做到。他们还可以从 Canary Marketplace 获取金丝雀——类似于 Apple 的 App Store 和 Google 的 Play 等移动应用市场——其中包含由 Cloud Canaries、客户的 DevOps 团队或第三方开发人员创建的金丝雀。

## 基于订阅的金丝雀
Cloud Canaries 提供多种订阅模式，包括前三个月免费提供三个 Canary 模型，之后将纳入付费订阅。下一级是每月 49 美元提供 15 个许可证——任何时候都可以运行 15 个金丝雀——以及每月 79 美元提供 45 个许可证（任何时候都可以运行 45 个金丝雀）。大型企业和服务提供商支付 5000 美元将技术安装在其防火墙或隔离区后面。

市场上的金丝雀将通过 1 美元到 10 美元的订阅免费提供。

“这里的关键是你获得了许可证，并且你获得了所有东西，”Callahan 说。“你不必回到你的首席财务官那里获得许可才能获得更多东西，你只需要运行一个金丝雀。这就是财务方面的魔力。我们之所以采用这种定价模式，是因为我希望在任何时候都有数万个金丝雀在运行。这就是愿景——大量企业在 Aviary 平台上运行数千个金丝雀，生成数据。”

他说，随着越来越多的公司使用更多金丝雀来引入更多数据，可能性开始增长并带来更多收入。如果组织同意，Cloud Canaries 将能够对一些数据进行众包，并将其通过 AI 模型运行。这可以带来更多付费仪表板，以及成为企业更紧密合作伙伴的机会，向他们展示哪些步骤有意义，或者向他们提供他们以前从未接触过的见解。

随着更多数据被收集并通过 AI 模型运行，该平台将能够对预测和预测进行更细粒度的运行，直到金丝雀不仅能够识别解决问题的方法，而且能够减轻问题。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)