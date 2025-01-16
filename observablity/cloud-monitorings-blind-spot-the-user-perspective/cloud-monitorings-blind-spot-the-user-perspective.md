
<!--
title: 云监控的盲点：用户视角
cover: https://cdn.thenewstack.io/media/2025/01/40b9c1d8-cloud-monitor-blind-spot-scaled.jpg
-->

监控云应用性能时，主干网、最后一公里和无线网络不仅仅是画面的一部分，它们就是画面本身。

> 译自 [Cloud Monitoring’s Blind Spot: The User Perspective](https://thenewstack.io/cloud-monitorings-blind-spot-the-user-perspective/)，作者 Brandon DeLap。

互联网中心化应用交付的演变加剧了IT对影响最终用户体验因素的可视性缺口。当这些缺口导致负面业务后果，例如收入损失或净推荐值 (NPS) 下降时，这个问题会更加严重。Gartner 最近发布了其首个[数字体验监控 (DEM) 魔力象限](https://www.catchpoint.com/asset/2024-gartner-magic-quadrant-for-digital-experience-monitoring)报告，进一步强调了解决日益恶化的可视性缺口问题的必要性。

了解真正应该具备的可视性，一个好方法是从第一英里监控与最后一英里监控的角度来看。

## 第一英里监控与最后一英里监控：监控位置的重要性

第一英里代表云网络和平台，例如[AWS](https://aws.amazon.com/?utm_content=inline+mention)、[Azure](https://news.microsoft.com/?utm_content=inline+mention)、[Google Cloud](https://cloud.google.com/?utm_content=inline+mention)，甚至“的网络机房”。这些环境稳定、优化良好，对于托管应用程序至关重要。第一英里监控侧重于确保应用程序的核心基础设施和代码按预期运行。

然而，最后一英里是真实用户连接到应用程序的地方；体验发生的地方。这包括骨干网络（例如，BT、AT&T 和 Comcast 等区域 ISP）、最后一英里提供商（光纤或无线，例如 Verizon、Sky 或 T-Mobile）和无线连接。[监控](https://thenewstack.io/whats-the-difference-between-observability-and-monitoring/)最后一英里可以揭示用户面临的现实挑战，例如延迟峰值、丢包和第一英里监控看不到的特定于互联网服务提供商 (ISP) 的问题。

可以把它想象成达美乐的“[为披萨铺路”](https://pavingforpizza.com/) 广告宣传活动——这不仅仅是确保披萨离开店面时完美无缺（第一英里）；而是要修补道路上的坑洼，以便披萨完好无损地送到顾客手中（最后一英里）。同样的原则也适用于数字体验：如果最后一英里没有交付，那么仅仅监控第一英里是不够的。从最后一英里进行监控可以最清晰地展现用户视角下的性能。

## 为什么仅靠第一英里监控就显得不足

您的应用程序很可能托管在云提供商的数据中心中，通常与您的监控工具位于同一个[边界网关协议](https://thenewstack.io/how-a-popular-combo-provides-ddos-protection/) (BGP) 自治系统 (AS) 中。这意味着如此靠近源头的监控只能验证基础设施的可用性。换句话说，这种“内部”设置只能有限地了解现实世界中的问题。

1. **用户视角丢失**：互联网性能监控 (IPM) 从用户的角度监控健康状况，而仅限云端的监控无法做到这一点。
2. **可观测性风险**：当第一英里出现故障——这种情况比许多人意识到的要频繁——您的[可观测性策略](https://thenewstack.io/observability-in-2025-opentelemetry-and-ai-to-fill-in-gaps/)也会随之失效。这不仅仅是理论上的风险；这是我们在现实世界中断中一次又一次看到的现象，例如 2024 年 8 月发生的[Lumen 和 AWS 微中断](https://www.catchpoint.com/blog/dont-get-caught-in-the-dark-lessons-from-a-lumen-aws-micro-outage)。在此事件中，关键系统中断，波及相互关联的生态系统，并使企业措手不及。

## 重新思考可观测性：可用性和可达性

在提供完美的数字体验方面，可观测性依赖于四个关键支柱：可用性、可达性、性能和可靠性。每一个都在理解应用程序的性能和用户体验方面发挥着关键作用。

我将重点关注前两个：可用性和可达性。可用性是指您的应用程序是否正在运行。另一方面，可达性衡量用户是否能够实际连接到您的应用程序，其中考虑了网络延迟、丢包以及他们与您的服务器之间的跳数。

我将说明从云端监控与从最终用户网络监控的区别，以及在云端看起来完美无缺的东西在现实世界中往往会崩溃的原因。

**可视化差异：跨网络类型的可用性**

云监控数据往往呈现过于乐观的景象。如下图所示，来自云端的监控（绿线）报告显示可用性接近完美，始终徘徊在99.99%左右。但这些数据只讲述了故事的一部分——它反映的是云基础设施的受控环境，而不是用户的真实体验。

![](https://cdn.thenewstack.io/media/2025/01/9dc5fc29-network-availability_catchpoint-1024x803.jpg)

现在，将其与骨干网（蓝线）、最后一公里（红线）和无线（紫线）数据进行比较。这些波动突显了用户每天面临的挑战，从区域ISP中断到最后一公里的不稳定性。要点是什么？虽然云监控数据可以让仪表盘看起来不错，但它并没有考虑到用户连接的真实网络环境。要真正了解可用性，您需要监控所有这些网络类型。

**云与最终用户网络地图**

这是另一个例子。上面的地图显示了来自云端的监控结果，下面的地图显示了最终用户的网络。

![](https://cdn.thenewstack.io/media/2025/01/60bb67f4-cloud-end-user_catchpoint-913x1024.png)

云端显示全绿，表明第一公里性能接近完美。下面的地图显示了从最终用户角度看到的现实；红色和黄色标记代表云端监控看不到的性能问题。

这种差异强调了在用户实际连接的地方进行监控的迫切需要。虽然云端可能看起来很完美，但最终用户的网络却讲述了一个截然不同的故事。

为什么会这样？

![](https://cdn.thenewstack.io/media/2025/01/225e5193-end-user-network_catchpoint-1024x325.png)

上图显示，用户从外部ISP连接到云端的路径比云端ISP（如下图所示）更不稳定。这是由于云托管应用程序和用户之间存在大量的BGP自治系统和跳数。每个AS网络代表一个不同的管理域。当流量遍历这些域时，它会经过多个网络跳数。这些跳数可能包括不同的路由策略、对等协议和拥塞点。

![](https://cdn.thenewstack.io/media/2025/01/d22aa98f-asn-hops_catchpoint-1024x294.png)

基于云的监控缺乏对这些中间跳数的洞察，尤其是在跨运营商和对等交换的情况下，导致对网络性能和真实用户体验的看法支离破碎。

相比之下，[骨干网](https://thenewstack.io/how-meta-is-reinforcing-its-global-network-for-ai-traffic/)监控通过捕获更接近互联网核心的数据，提供了更全面的视角，可以了解最终用户流量的路径和沿途的潜在瓶颈。

**平均响应时间：云与骨干网ISP**

知道您的应用程序是否正在运行是一回事，但连接质量如何呢？下图比较了骨干网和云网络之间的响应指标。

![](https://cdn.thenewstack.io/media/2025/01/d26092de-cloud-backbone_catchpoint-1024x790.png)

左侧，来自骨干网的监控显示关键指标（如**加载时间**和**等待时间**）存在显著差异。峰值代表用户在遍历真实网络时面临的挑战。将其与右侧的云进行比较，那里的一切看起来都稳定、流畅且可控。但是大多数用户并非从云端连接。如果没有来自骨干网和最后一公里网络的监控，您只能看到故事的一部分。

这是另一个例子，说明云监控数据如何使一切看起来都很完美，而实际情况却远非如此。下图显示了来自[AWS](https://aws.amazon.com/?utm_content=inline+mention)的监控，报告显示近乎即时的响应时间为44.79毫秒。

![](https://cdn.thenewstack.io/media/2025/01/a9a9f6bc-response-time_catchpoint-1024x489.png)

但是，当您将视角转移到骨干网ISP时会发生什么？在这个CenturyLink示例中，响应时间飙升至730.67毫秒。

这种差异并非异常值——这是用户每天通过不同网络连接到您的应用程序时面临的现实。除非您从这些网络进行监控，否则您将无法全面了解应用程序的可达性。

## 综合起来

这些图表中的数据讲述了一个清晰的故事。它显示了仅靠第一公里监控无法显示的内容：用户每天在骨干网、最后一公里和无线网络上遇到的可变性、不稳定性和挑战。

要点是什么？要真正了解您的应用程序的性能，您需要超越云端进行监控。骨干网、最后一公里和无线网络不仅仅是画面的一部分——它们就是画面本身。能够监控整个互联网堆栈，包括用户实际连接的那些“眼球”网络，是[Catchpoint互联网性能监控 (IPM)](https://www.catchpoint.com/internet-performance-monitoring)与众不同的原因。

![](https://cdn.thenewstack.io/media/2025/01/f5429666-internet-stack_catchpoint.webp)
