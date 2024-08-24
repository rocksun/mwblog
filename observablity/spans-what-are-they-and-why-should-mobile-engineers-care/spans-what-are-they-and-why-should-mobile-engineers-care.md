
<!--
title: SPAN：为什么移动工程师应该关心它？
cover: https://cdn.thenewstack.io/media/2024/08/969de6d9-embrace-featured-image-what-is-a-span.png
-->

SPAN 衡量应用程序中关键操作的性能，以便您可以快速解决应用程序挂起和缓慢等问题。

> 译自 [Spans: What Are They and Why Should Mobile Engineers Care?](https://thenewstack.io/spans-what-are-they-and-why-should-mobile-engineers-care/)，作者 Fredric Newberg。

移动工程师非常熟悉应用程序崩溃以及将崩溃率保持在可接受范围内的重要性。虽然不像崩溃那样严重和明显，但应用程序挂起和缓慢也会对长期用户参与产生同样负面的影响。

人们的耐心是有限的，大多数人只会容忍缓慢、令人沮丧的体验一段时间，然后才会删除应用程序，正如这些数据所示。

![用户删除应用程序的可能性，基于缓慢的行为。数据来自 Embrace 的移动体验状况报告。](https://cdn.thenewstack.io/media/2024/08/06bd8516-embrace-state-of-mobile-experience-results.png)

用户删除应用程序的可能性，基于缓慢的行为。数据来自 [移动体验状况](https://get.embrace.io/state-of-mobile-experience-2023/) 报告，由 [Embrace](https://embrace.io/) 提供。

那么，您如何才能了解您的应用程序在哪里运行缓慢呢？

这就是 SPAN 发挥作用的地方。它们帮助您衡量应用程序中关键操作的性能，以便您可以快速解决问题。

## 什么是 SPAN？

从概念上讲，SPAN非常简单，包含三个关键要素：

- 它们有开始时间和结束时间，因此可以衡量持续时间。这与崩溃和错误日志不同，崩溃和错误日志锚定在时间上的一个点。
- 它们有一个结果：您正在衡量的内容是成功还是失败？
- 它们可以与其他SPAN具有父子关系。

![父SPAN及其子SPAN的示例，用于衡量添加到购物车功能的性能。](https://cdn.thenewstack.io/media/2024/08/79f24c70-embrace-span-example-1024x536.png)

*父SPAN及其子SPAN的示例，用于衡量添加到购物车功能的性能。*

SPAN在用途上非常灵活。监控应用程序中更大功能的SPAN，例如用户在电子商务应用程序中花费在结账页面上的全部时间，通常由产品组织使用。但是，我将讨论 [性能SPAN](https://embrace.io/blog/what-is-performance-tracing/)，它专注于更细粒度的任务，通常对试图理解和解决性能问题的移动工程师更有帮助。

性能SPAN衡量应用程序中不直接依赖于用户交互的操作和流程的持续时间。换句话说，性能SPAN衡量完成给定操作（例如，添加到购物车）需要多长时间。

## 使用 SPAN 的优势是什么？

SPAN可以帮助 [移动工程师](https://thenewstack.io/intertwined-worlds-platform-and-mobile-app-engineering/) 以多种方式。

### 了解性能并识别缓慢

SPAN帮助您了解应用程序发布后的真实性能。在现代 iOS 或 Android 设备上使用快速网络连接测试应用程序的干净安装时，操作可能很快并且永远不会挂起。但它们对于您现实世界用户中的很大一部分可能表现得非常不同。

除非您对性能SPAN进行检测，否则您将不知道您的用户群真正体验了什么。也许由于新的广告 SDK 版本，某些设备上的平均 [启动持续时间](https://embrace.io/blog/top-5-factors-slow-down-app-startup/) 显着增加。也许某些国家/地区的用户的支付处理速度很慢。除非您衡量这些内容，否则您将不知道您用户群中很大一部分正在积累的挫败感。

![SPAN示例，显示了可接受和不可接受持续时间的组合。对于大约 65% 的用户来说，此SPAN持续时间是可以的，但对于剩下的 35% 的用户来说，持续时间过长。](https://cdn.thenewstack.io/media/2024/08/541ef2d7-embrace-span-durations-graph-1024x597.png)

*SPAN示例，显示了可接受和不可接受持续时间的组合。对于大约 65% 的用户来说，此SPAN持续时间是可以的，但对于剩下的 35% 的用户来说，持续时间过长。*

作为一名移动工程师，了解问题的程度非常有帮助。您的应用程序是否因为缓慢的行为而收到了一些差评，但问题没有影响到很大一部分用户？或者负面评价是否表明问题影响了更大比例的用户？

拥有SPAN数据可以更轻松地决定是否优先提高应用程序各个部分的性能。在上图示例中，大约 35% 的用户存在实际问题。

### 使用与您的 DevOps 团队共享的语言

您的后端团队已经使用 Span 来了解服务和基础设施的运行状况，而且您的 DevOps 团队知道如何分析和监控 Span。采用一种共享遥测语言能让您标准化移动端和 Web 应用组件的监测方式。使用一种共享语言还能简化将移动端应用中启动的 Span 与之交互的所有后端服务连接在一起的方式。

通过追踪关键操作和整个流程（从客户端到后端再回到客户端），您可以全面了解最终用户体验的缓慢程度的确切原因。

## 移动应用程序的哪些部分需要 SPAN？

SPAN非常通用，因此您如何最好地将它们用于您的应用程序将取决于您的业务和技术目标。我将以电子商务应用程序为例来了解哪些值得检测。一般来说，[枚举](https://embrace.io/product/performance-profiling-embrace/) 应用程序中对良好用户体验至关重要的部分或流程是决定在何处添加SPAN的良好起点。

大多数电子商务应用程序中的关键流程包括：

### 登录

虽然一些应用程序允许以访客身份购买，但在大多数情况下，买家必须登录。虽然这看起来像是一个简单的过程，但现代登录具有十年前并不常见的许多组件，例如生物识别输入和 [双因素身份验证 (2FA)](https://thenewstack.io/githubs-2fa-push-boosts-adoption-among-developers/)。您可以为登录设置一个根SPAN，并为各个组件设置子SPAN，例如访问生物识别数据和获取 2FA 的输入。

### 产品搜索
搜索结果需要多长时间才能出现？在具有挑战性的网络连接下，交付搜索结果的效果如何？渲染搜索结果需要多长时间？您可以使用一个根SPAN来表示搜索操作，并将其分解。

### 将商品添加到购物车
当用户点击按钮将商品添加到购物车时，需要多长时间才能成功？是否有网络调用？它是否可以在网络连接不良的情况下工作？

### 结账
电子商务应用程序最重要的部分是让用户能够成功进行购买，因此监控实际的订单提交过程非常重要。您可以添加一个SPAN来衡量从点击“提交订单”按钮到出现“订单确认屏幕”的时间。然后，您可以添加子SPAN来衡量该旅程中的各个步骤，例如向第三方支付提供商进行调用。

## 如何开始在移动应用程序中添加SPAN

手动检测几个SPAN通常不是一项具有挑战性的任务，当您使用像 [我们在 Embrace 中构建的](https://github.com/embrace-io/) 这样的可观察性 SDK 时，您还将获得对常见任务（例如网络请求）的自动检测SPAN。您可以从检测应用程序中的一个或两个关键流程开始，然后从那里扩展。您不需要在能够获得价值之前详尽地检测应用程序中的每个流程。

选择 [符合 OpenTelemetry (OTel)](https://embrace.io/opentelemetry-for-mobile/) 的可观察性 SDK 可以让您在收集和分析性能SPAN数据的方式上拥有很大的灵活性。Embrace 提供托管服务，但您也可以选择将数据发送到 [OTel](https://thenewstack.io/why-the-latest-advances-in-opentelemetry-are-significant/) 兼容的收集器。

要详细了解性能SPAN如何帮助您提供更好的最终用户体验，请随时 [查看 Embrace 的网站](https://embrace.io/) 或加入 [我们的 Slack 社区](https://community.embrace.io/)。
