
<!--
title: 微软Edge如何用Web Components替换React
cover: https://cdn.thenewstack.io/media/2024/10/87a6c598-react-kick.jpg
-->

微软的 Edge 浏览器团队正在努力用原生 Web 平台组件替换 React UI 组件。我们与团队负责人进行了交谈。

> 译自 [How Microsoft Edge Is Replacing React With Web Components](https://thenewstack.io/how-microsoft-edge-is-replacing-react-with-web-components/)，作者 Richard MacManus。

当微软 Edge 浏览器团队 [发布 WebUI 2.0](https://thenewstack.io/from-react-to-html-first-microsoft-edge-debuts-webui-2-0/) 时，该项目旨在用原生 [web components](https://thenewstack.io/introduction-to-web-components-and-how-to-start-using-them/) 替换 React 组件，其主要目标是让 Edge 浏览器对最终用户来说更快。核心思想是采用“标记优先架构”将减少产品对 JavaScript 的依赖，这意味着客户端需要处理的代码更少，从而为用户提供更好的体验。

为了了解 WebUI 2.0 项目的进展，包括项目的灵感来源和最终目标，我采访了 [Andrew Ritz](https://www.linkedin.com/in/andrewritz/)，他是微软 Edge 基础团队的负责人。

但首先，让我们快速澄清一下什么是 web components。社区网站 WebComponents.org [将其描述为](https://www.webcomponents.org/introduction)“一组 Web 平台 API，允许您创建新的自定义、可重用、封装的 HTML 标签，以便在网页和 Web 应用程序中使用。” Ritz 在建议自己的团队如何处理这种 Web 开发范式时这样说：“任何时候你想做一个新的控件，并且发现自己正在编写 JavaScript 代码，请暂停，停止，与高级工程师交谈，并询问如何用 HTML 和 CSS 解决这个问题？”

## 为什么微软 Edge 决定放弃 React？

Ritz 表示，他的团队的目标是在今年年底之前将 Edge 中大约 50% 的现有基于 React 的 Web UI 转换为 web components。

但这个项目的动力是什么？为什么他们决定需要在 Web 界面中远离 React？Ritz 解释说，这源于他们观察到 Edge 浏览器“Web 桌面”团队收到的工作请求——“包括外部请求，以帮助改进 Chromium 项目，以及内部请求。”

> “…我们 [微软] 采用了 React 框架，并且我们可能以最糟糕的方式使用了 React。”
>
> – Andrew Ritz，微软 Edge 基础团队合作伙伴总经理

后者的一个例子是 Excel 网页应用程序，它使用 Canvas 元素。因此，他们必须考虑的一个问题是，“我们如何才能提高 Canvas 的性能？” HTML `<canvas>` 元素用于通过脚本动态绘制图形——通常使用 JavaScript 完成。

为了帮助 Web 桌面团队处理此类请求，Ritz 希望采用更“有主见的方法”，这也将解决 Web 应用程序速度慢等问题。

“因此，我们开始查看内部所有使用 Web 技术的地方——也就是我们所有的内部 Web UI——并意识到它们的速度真的慢得无法接受。”

为什么它们速度慢？答案是：React。

“我们意识到，我们的性能，尤其是在低端机器上，非常糟糕——这是因为我们采用了 React 框架，并且我们可能以最糟糕的方式使用了 React。”

随着越来越多的团队使用 React 来构建 UI，微软内部对 React 的使用随着时间的推移不断增加。因此，该公司最终得到了“一个巨大的捆绑包，每个人都依赖它”，Ritz 说。这是 Web 应用程序之间捆绑包依赖关系的一团糟。

“这是一种糟糕的体验，尤其是在低成本、低端机器上，”Ritz 说。“我们看到启动时间长达数秒，而这本该是本地化的。这真是，你知道，令人震惊。”

## Edge Web UI

Ritz 说，Edge 本身有 50 到 100 个 Web UI，“每个 UI 都像一个小的 Web 应用程序。” 在 Web UI 2.0 项目开始之前，大约三分之二的 Edge Web UI 是用 React 构建的。有趣的是，Edge 团队最初使用 React 的目的是为了与 Chrome 区分开来。

“该团队在将 Edge 移植到 Chromium 的过程中，决定，好吧，我们需要添加一些 UI 区别——与 Chrome 不同——因此，在这个过程中，他们进行了这种大规模的 React 转换。”

因此，当前的 Web UI 2.0 项目在某种程度上是对 Edge 上完成的原始开发工作的回溯。

Ritz 的工程团队负责其中一个 React Web UI：“浏览器扩展”。当您使用 Edge 时，它可以通过点击浏览器栏中的心形图标激活，这会打开一个侧边栏。然后，它成为测试平台，用于查看使用 web components 替换 React 组件可以为该 UI 带来哪些性能改进。

![](https://cdn.thenewstack.io/media/2024/10/3bf895bf-edge-browser-essentials.jpg)

*Edge 浏览器要点（右侧）*

## Web Components 太难了吗？

最近，社交媒体上又爆发了一场关于 Web 组件与框架组件的争论。SolidJS JavaScript 框架的创建者 [Ryan Carniato](https://x.com/RyanCarniato) 发表了一篇博文，标题颇具挑衅意味，名为“[Web 组件并非未来](https://dev.to/ryansolid/web-components-are-not-the-future-48bh)”。他的主要观点是，像 SolidJS 这样的框架在某些情况下比 Web 组件能做更多的事情，而且更容易实现。他将 Web 组件斥为“彻头彻尾的妥协”。

针对 Carniato 的观点，[Shoelace](https://thenewstack.io/shoelace-web-components-library-that-works-with-any-framework/) 的创建者 Cory LaViska 反驳道，[Web 组件提供了稳定性和互操作性](https://www.abeautifulsite.net/posts/web-components-are-not-the-future-they-re-the-present/)。

“真正发布软件的人已经厌倦了框架的不断变化，”LaViska 写道。“他们厌倦了上个月写的代码现在已经过时了。他们想要稳定性。他们希望知道他们今天构建的东西明天还能用。”

LaViska 还指出，Web 组件并非能做到框架组件的所有功能，“因为它们是互操作元素的更低级实现”。

这是一种在社交媒体上无休止地进行的开发者辩论——它现在已经从*每日信息流*中消失了，但你可以肯定它会在一个月或两个月后卷土重来。无论如何，我问 Andrew Ritz 他的工程团队是如何适应 Web 组件的，以及它们是否像一些批评者声称的那样难以部署。

“我们的方法实际上是说，让我们尽可能多地使用内置的结构，”他回答道。“所以尽可能多地使用浏览器中存在的内置元素，这样做并没有那么糟糕。”

> “……努力使 Web 组件表现良好确实是一个问题。”
>
> – Ritz

Ritz 指出，Edge 开发人员可以使用微软自己的 [Fluent UI 框架](https://developer.microsoft.com/en-us/fluentui#/)，该框架包含 React 组件和 Web 组件（以及其他类型的组件，例如针对 iOS 和 Android 的移动端组件）。但他承认，即使使用公司范围内的框架来实现 Web 组件也并非易事。

“有些情况下，[一个] 内置控件需要大量的工作——你知道，它在 polyfill 上很重，或者类似的东西——我们永远、永远不会需要。所以努力使它们表现良好确实是一个问题。”

在 Ritz 所谓的 Web 组件“开发敏捷性”（其他人可能称之为“[开发者体验](https://thenewstack.io/how-do-you-measure-developer-experience/)”）方面，他说“我们实际上看到了一些相当不错的改进”。例如，能够专注于 HTML 和 CSS 意味着开发人员和设计师之间能够更好地协调——因为他们使用的是相同的语言。

“通过我们[开发人员]专注于使用 HTML 和 CSS，我们实际上消除了整个翻译层，这样就不用有人[在开发团队中]去处理线框图并将其转换为其他东西。[…] 因此，这[曾经]是我们开发人员生产力的一个巨大障碍，而我们消除了整个循环。”

## 关于 Web 组件的广泛采用
可以公平地说，微软的浏览器团队比一般的 Web 开发团队更容易实现 Web 组件。除了可以使用微软的 Fluent UI 框架之外，Edge 团队还在构建一个软件产品，该产品只需要满足一个浏览器的需求：它自己的浏览器。而几乎所有其他 Web 开发团队都必须确保他们的产品可以在各种不同的浏览器上使用：从 Chrome 到 Edge，再到 Safari、Firefox 等等。

“我们可能更容易一些，因为我们可以说我们只依赖 Edge 来处理本地事务，”Ritz 这样解释道。“这可以看作是[现代]最新 Web 的真实体现。而网站所有者——天哪，他们可能被迫支持 Safari 或者其他不支持我们想要使用的一半结构的东西……这会带来复杂性。”

> “如果我们能说服微软内部一些较大的非 Web 组件网站迁移过来，那将是一个很好的证明。”
>
> – Ritz

也就是说，微软的意图是将一些 WebUI 2.0 包作为开源发布——以及一套“Web 平台模式”。然而，Ritz 指出，许多外部开发人员可能不想完全按照相同的方式做事——例如，许多开发人员会想要选择与 Fluent UI 不同的样式框架。但至少，Ritz 的团队将能够为其他人提供“学习模式”。

一个中间步骤可能是尝试说服其他微软 Web 产品迁移到 Web 组件。
“我不知道微软其他部门会怎么做，”Ritz 说。“我们（Edge 团队）想把我们的房子打扫干净，比如 […] 一个公共库等等。但我认为，如果我们能说服微软内部一些更大的非 Web 组件网站迁移过来，这将是一个很好的证明。”

但他补充说，他们对外部合作伙伴持开放态度，以帮助引领 [后 React 时代](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/) 的发展。

“如果我们能找到一个有意义的外部合作伙伴，他们愿意与我们合作——我们当然会很高兴。”
