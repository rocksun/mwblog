在前端引入更好的可观测性实践方面，有很多发展势头，OpenTelemetry 项目中专门的[浏览器特别兴趣小组（SIG）](https://opentelemetry.io/docs/community/special-interest-groups/#browser-sig)的成立就是一个很好的例子。虽然 OpenTelemetry 最初是作为解决分布式追踪后端可观测性挑战的方案而创立的，但工程团队和组织正越来越多地将其作为整个技术栈可观测性的开放标准。

尽管 OpenTelemetry [支持在 JavaScript](https://thenewstack.io/building-an-ergonomic-opentelemetry-for-javascript/) 语言中收集遥测数据，但其 API 和 SDK 是为服务器运行时 Node.js 设计的。为了更好地支持浏览器运行时的细微之处，OpenTelemetry 项目创建了浏览器 SIG，旨在为前端 Web 应用中运行 JavaScript 建立更好的仪表化、工具和语义约定。

我与浏览器 SIG 的几位关键成员进行了一场[有趣的、电影主题的小组讨论](https://get.embrace.io/web-otel-panel-typ?utm_source=the-new-stack&utm_medium=paid&utm_campaign=web-otel-panel)，内容涉及[浏览器可观测性](https://thenewstack.io/setting-up-opentelemetry-on-the-frontend-because-i-hate-myself/)的一些关键挑战、该小组将要开展的工作以及 Web 开发者如何开始使用 OpenTelemetry。小组成员包括：

* [Ted Young](https://www.linkedin.com/in/ted-young/)，[Grafana Labs](https://grafana.com/) 开发者项目总监，OpenTelemetry 联合创始人。
* [Purvi Kanal](https://www.linkedin.com/in/purvi-kanal/)，[Honeycomb](https://www.honeycomb.io/) 高级软件工程师，OpenTelemetry JavaScript 审批人兼浏览器实现工程师。
* [Martin Kuba](https://www.linkedin.com/in/kubamartin/)，Grafana Labs 资深软件工程师，OpenTelemetry 贡献者兼 JavaScript SDK 审批人。
* [Jared Freeze](https://www.linkedin.com/in/jaredfreeze/)，[Embrace](https://embrace.io/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=web-otel-panel) 高级软件工程师，OpenTelemetry 浏览器 SIG 贡献者。

## 浏览器可观测性中的关键挑战

OpenTelemetry 早已有了[JavaScript 实现](https://thenewstack.io/javascript/ "JavaScript 实现")，并且可以在浏览器中运行。然而，该实现主要侧重于在 Node.js 中运行的生产环境。

正如 Young 所解释的：“这并不是我们认为的能够与市面上其他产品相媲美的专业产品。但它确实有效。但就资源管理而言，浏览器、移动设备等与服务器端的东西截然不同。我们知道我们需要非常刻意地解决这个问题。”

浏览器需要与后端系统不同的方法的一个原因是，浏览器运行时是事件驱动的，而不是请求驱动的。Kanal 解释了分布式追踪的[可观测性方法](https://thenewstack.io/a-user-focused-approach-to-core-web-vitals-via-opentelemetry/)在浏览器中为何不太适用。

她说：“浏览器面临的挑战是，它不是从分布式追踪系统出发，而是转向了一个具有多个输入的事件驱动系统。所以这里我们不只有一个输入。你会有多个输入。用户会做一些事情。你会在浏览器中点击。你会滚动。用户会创建成百上千的事件，甚至每秒数百个事件。如今的浏览器应用相当复杂。”

“所以用户输入，你有你的应用代码输入。当用户做事情时，应用可能会对其中一些事情做出反应，但也可能在做其他事情，比如在后台获取资源或执行其他类型的后台任务，预取其他资源。”

浏览器都像一个事件循环，响应来自任意数量输入源的事件监听器。它们并没有很好地设计成能够被完美追踪，甚至很难决定在浏览器中从哪里开始和结束追踪。因此，与其仅仅衡量单个请求或追踪，不如通过[用户会话的视角](https://thenewstack.io/5-user-flows-to-trace-in-your-mobile-app/)来观察前端应用更有帮助。不幸的是，OpenTelemetry 并没有定义良好的会话数据模型。

## 浏览器SIG正在做什么？

最初，浏览器 SIG 并不专注于为浏览器创建新的 JavaScript SDK。相反，它正在为浏览器运行时研究 OpenTelemetry API、仪表化和数据模型。

正如 Kuba 所说：“我们知道现有仪表化存在挑战。所以也许我们应该退一步，审视 API 和 SDK，以及它与市面上其他解决方案的比较。”

例如，存在一些缺失或需要重新评估的核心仪表化，例如页面加载/卸载、用户事件、资源计时、核心 Web 生命指标和错误。此外，还需要解决浏览器数据模型中的空白，例如定义会话的概念。

Kuba 说：“会话是将许多不同事件和许多不同追踪或跨度（span）联系在一起的东西。所以我们希望将会话视为一种资源。它也很有趣，因为会话会跨越页面加载。”

用户启动网站后，可以在一次体验中浏览多个页面。Freeze 解释了在这种情况下建模用户会话的一些挑战。

“我喜欢用电子商务的例子，对吧？我在主页上，有很多产品，我正在新标签页中打开产品，对吧？但我还没有访问那个页面。它在后台发生了。……然后我去了产品一。我说，‘这真的很酷。’把它放进购物车。追踪所有这些事件，然后回到主页。我仍然拥有相同的体验。那么，你是否包括那个？有哪些选项？”

Web 应用的种类繁多也意味着工程团队根据其业务需求具有不同的可观测性要求。[OpenTelemetry JavaScript SDK 尚未针对浏览器进行优化](https://thenewstack.io/how-to-make-opentelemetry-better-in-the-browser/)，浏览器 SIG 正在更新现有版本。

正如 Kuba 所说：“有些应用只关心尽可能小的打包大小，因为页面加载速度是最重要的。……我们正稍微从基于跨度（span）的仪表化转向基于事件的仪表化，我希望这能使打包大小更小。或者至少给用户一个选项，如果他们只想收集某些事件，他们就不必包含追踪 SDK。他们可以只包含日志 SDK。就打包大小而言，追踪具有挑战性，因为 API 和 SDK 更大、更复杂。”

为开发者提供选择他们想要包含在打包中的内容的灵活性，以及更新现有 JavaScript SDK 以更好地进行摇树优化，是浏览器 SIG 的关键工作。

## Web开发者如何开始使用OpenTelemetry

Web 开发者现在可以在他们的 Web 应用中使用现有的 OpenTelemetry JavaScript SDK，但有一些注意事项，最大的问题是它不是以浏览器优先的心态构建的。例如，想要使用追踪的 Web 开发者在上下文传播方面会遇到一些障碍。

正如 Kanal 所说：“如果你正在考虑跨异步边界进行上下文传播，你将不得不使用一个名为 zone.js 的库来完成，我认为这很难推广，因为它非常大。它本身就有大约一兆字节。而且维护得也不是很好。它也不适用于 async-await。所以，也许最好放弃它，转而通过会话将事物联系起来，而不是这些涵盖整个会话的完美追踪，这正是我们无论如何都想迈向的世界。”

正如 Kuba 指出的那样：“现在当然可以只包含日志 SDK 并从应用程序的不同部分生成自己的事件。有些事件不难捕获。你可以从那里开始。然后，当我们构建官方仪表化时，你可以轻松替换。我们现在正在为其中一些事件制定语义约定。所以我想你可以通过使用这些语义约定生成自定义事件来开始，然后在官方仪表化可用时替换它。”

OpenTelemetry JavaScript SDK 已经有一些有用的浏览器仪表化，例如用于网络请求、文档加载和用户交互的仪表化。

小组成员一致认为，Web 开发者了解 OpenTelemetry 的最佳地点是访问 [OpenTelemetry 网站](https://opentelemetry.io/)并尝试 [OpenTelemetry 演示应用](https://opentelemetry.io/docs/demo/)。它包含了许多不同类型的仪表化，例如语言和 SDK，包括浏览器。

Young 说：“OpenTelemetry 演示应用是一个非常好的起点，因为在你尝试进行仪表化和搭建所有东西之前，能够直接在你将查看数据的产品中看到数据会非常有帮助。它是一个良好仪表化的应用，并带有一个负载测试器，可以生成所有负载，让你实际尝试并了解它应该是什么样子，然后再自己动手。这真的很有帮助。”

Freeze 提到了另一件帮助他熟悉 OpenTelemetry 的事情是[控制台导出器](https://opentelemetry.io/docs/languages/js/exporters/#console)。

“你可以运行这些库而不需要端点。你不必从那里开始。你可以在浏览器中运行。你可以以结构良好的方式看到所有发出的内容，并说，‘好的，太棒了，我有正确的属性。我做对了。我正确命名了它。或者我正确使用了标点符号来命名键，无论是何种情况。’”

Web 开发者还可以选择使用 [Embrace Web SDK](https://github.com/embrace-io/embrace-web-sdk/)。它是开源的，基于 OpenTelemetry 构建，并连接到任何 OpenTelemetry 兼容工具，因此它是 Web 应用使用 OpenTelemetry JavaScript SDK 的替代方案。

要了解更多信息，您可以观看下方完整的小组讨论。

视频

[YOUTUBE.COM/THENEWSTACK

科技发展迅猛，不要错过任何一集。订阅我们的 YouTube 频道，观看所有播客、访谈、演示等内容。

订阅](https://youtube.com/thenewstack?sub_confirmation=1)