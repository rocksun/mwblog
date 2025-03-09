# 为移动可观测性选择手动或自动埋点

![Featued image for: Choosing Manual or Auto-Instrumentation for Mobile Observability](https://cdn.thenewstack.io/media/2025/03/e1131f83-embrace-1024x576.jpg)

当应用程序在生产环境中运行时，你需要找出发生了什么。你可能想知道你是否使硬件过载，在 A/B 测试中移动到错误的功能，或者在移动端，甚至像电池电量耗尽这样简单的意外情况。

开发一个应用程序来发送关于自身的信息意味着添加埋点。应用程序可以发送诸如[指标、日志和追踪](https://opentelemetry.io/docs/concepts/signals/)之类的遥测数据，以允许团队解释应用程序的内部状态。这个概念是可观测性中收集的基础。

[标准化这些信号的收集](https://thenewstack.io/sending-mobile-signals-to-the-opentelemetry-collector/)和格式在很大程度上是 [OpenTelemetry](http://opentelemetry.io) (OTel) 项目的目标。一个额外的好处是，如果给定语言中的大多数应用程序需要观察相同类型的操作和工作流程，那么基于 OTel 标准构建的开发人员可以识别并构建[自动埋点](https://opentelemetry.io/docs/concepts/instrumentation/zero-code/)来为他们完成这项工作。

## 自动埋点的乐趣

如果你可以在不做任何额外工作的情况下了解你需要了解的关于应用程序的一切，那当然很好。例如，想象一下，你可以了解你高度定制的构建中的哪些服务耗尽了资源。或者，你可能会看到[网络请求在应用程序流程的关键部分重复失败](https://thenewstack.io/why-your-mobile-app-needs-client-side-network-monitoring/)。

移动应用程序在特定的设备和操作系统上运行，这意味着某些操作在每个应用程序实例中都是标准的。例如，在基于 [UIKit](https://developer.apple.com/documentation/uikit/) 构建的 iOS 应用程序中，[didFinishLaunchingWithOptions](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:)) 方法通知应用程序开发人员，新启动的应用程序几乎已准备好运行。在任何应用程序中监听此方法反过来可以让你自动观察和了解有关应用程序启动完成的更多信息。

像这样快速、开箱即用的埋点易于使用。通过将自动埋点库导入到你的应用程序中，你无需编写自定义代码即可连接到应用程序的活动。

使用自动埋点为应该以规定方式识别的操作提供标准化信号。你可以监听应用程序启动（如上所述），还可以监听视图的加载、[网络请求的开始和结束](https://thenewstack.io/best-practices-for-monitoring-network-conditions-in-mobile/)、崩溃等等。如果导入的库完成了所有工作，那么可观测性将非常棒。

## 移动应用工作流程以及你可以控制的内容

但是，要理解你的移动应用程序，需要的不仅仅是监控移动应用程序开发中普遍存在的信号。首先，移动遥测数据的收集和传输可能会受到应用程序用户选择的[操作系统的限制](https://get.embrace.io/mobile-observability-guide?utm_source=the-new-stack&utm_medium=paid&utm_campaign=manual-or-auto-instrumentation)，该操作系统并非旨在传输其自身的每个信号。此外，用于常见用例（如网络和 UI 渲染）的第三方库通常是闭源的，并且在设计时没有考虑到自动埋点。

最后，也是最重要的一点，应用程序的特定流程来自应用程序开发人员的意图，只有他们才能为此提供埋点。换句话说，应用程序的构建方式完全是为用户的预期用途而定制的。这就是构建新应用程序的意义所在。

例如，使用正在进行的网络请求导航屏幕以及跨线程发生的缓存是一组常见的同步活动。自动埋点可能会将导航和网络捕获为在应用程序生命周期中发生的单独信号。要在同一[用户流程](https://thenewstack.io/5-user-flows-to-trace-in-your-mobile-app/)中理解这些活动，甚至理解它们在用户旅程中何时发生，都需要应用程序开发人员的输入。

## 手动埋点，以用户为中心

[移动埋点与后端系统埋点之间](https://thenewstack.io/why-good-p99s-arent-good-enough-on-mobile/)的一个关键区别是用户。后端流程的构建遵循命令式框架，即“如果发生这种情况，就执行该操作”以响应操作。移动应用程序则不然。用户正在以他们喜欢的顺序触摸屏幕、滚动和点击按钮，而不是服务和程序的预定例程。
作为起点，移动端检测需要将[用户触及范围内的事件联系起来](https://dzone.com/articles/beyond-sessions-centering-users-in-mobile-app)，置于其特定的上下文中。这不一定是可观测性工程师所熟悉的[服务内部上下文](https://opentelemetry.io/docs/concepts/context-propagation/#context)。相反，它更人性化：检测需要反映用户在[会话](https://opentelemetry.io/docs/specs/semconv/general/session/)（即应用程序的一次使用）中的旅程。

以电子商务应用程序中[完成结账流程](https://get.embrace.io/ios-shopping-app-performance?utm_source=the-new-stack&utm_medium=paid&utm_campaign=manual-or-auto-instrumentation)为例。从一个屏幕导航到另一个屏幕需要网络请求来获取购物车可用性、支付信息和购买尝试，以及在屏幕之间传递这些信息。这些屏幕的正确排序显然很重要，因为没有开发人员应该构建一个从购买请求开始的结账流程。

在此会话中，可能还需要考虑在流程之外发生的其他因素。用户的地理位置可能会限制特定国家/地区的某些类型的购买。您需要知道糟糕的Wi-Fi是否在流程中途停止了流程。即使拥有世界上最好的用户体验，应用程序的软件本身也是由其他人操作的，因此捕获他们体验的详细信息是理解它的最佳方式。

## 检测混合

某些信号可以在应用程序中自动捕获并且无处不在，而另一些信号则需要手动检测才能深入了解其意图。将它们放在一起可能是最好的目标，因为将所有信号与正确的上下文信息放在一起可以最广泛地了解应用程序活动。

在手动[追踪](https://thenewstack.io/spans-what-are-they-and-why-should-mobile-engineers-care/)导航时，您可以使用自动网络检测来查看是否触发了错误的网络请求。然后，您可以向后工作，以了解导致此不正确活动的用户活动。

更广泛地说，对于任何工作流程，您可能需要添加自定义数据，以便您可以跟踪特定于您的应用程序的子工作流程。生成自动检测的SDK需要提供此功能，以允许自定义和自动捕获的数据“混合”。

## 找到合适的工具

最终，应用程序将需要通过手动和自动检测的混合来实现其检测。理想情况下，移动应用程序应依赖自动检测来捕获常见工作流程，并依赖手动检测来捕获自定义工作流程，但它们还应增强自动检测的遥测数据，以便可以将自定义上下文与自动捕获的内容混合在一起。

添加手动检测的难易程度将取决于您使用的SDK公开的API。这就是为什么像Embrace的[Android](https://github.com/embrace-io/embrace-android-sdk/)和[Apple](https://github.com/embrace-io/embrace-apple-sdk) SDK这样的SDK存在的原因：为大多数移动应用程序所需的平台和常见的特定于库的工作流程提供开箱即用的检测。Embrace的SDK经过定制，可以将移动上下文构建到可观测性中，因此移动开发人员不必一遍又一遍地面临相同的挑战。

在[Embrace](https://embrace.io/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=manual-or-auto-instrumentation)，我们正在寻求扩展在移动设备上捕获的信息的功能，以便轻松了解哪些因素会影响用户体验。加入我们的[社区Slack](http://community.embrace.io/)，提出问题并了解更多关于如何使用[基于OpenTelemetry构建的移动可观测性](https://embrace.io/blog/why-embrace-opentelemetry-mobile/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=manual-or-auto-instrumentation)的信息。

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)