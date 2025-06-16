
<!--
title: Elixir：JavaScript Web开发的替代方案
cover: https://cdn.thenewstack.io/media/2025/06/24ea64d5-elixir.jpg
summary: 还在用 JavaScript？试试 Elixir + Phoenix！函数式编程语言 Elixir 通过其 Web 框架 Phoenix 和前端框架 Phoenix LiveView，解决 JavaScript 扩展难题，提升开发效率。更有 LiveView Native 构建原生应用，或成云原生 Web 开发新选择？
-->

还在用 JavaScript？试试 Elixir + Phoenix！函数式编程语言 Elixir 通过其 Web 框架 Phoenix 和前端框架 Phoenix LiveView，解决 JavaScript 扩展难题，提升开发效率。更有 LiveView Native 构建原生应用，或成云原生 Web 开发新选择？

> 译自：[Elixir: An Alternative to JavaScript-Based Web Development](https://thenewstack.io/elixir-an-alternative-to-javascript-based-web-development/)
> 
> 作者：Loraine Lawson

这听起来可能像是异端邪说，但一些开发人员后悔他们对 JavaScript 的承诺。[Brian Cardarella](https://www.linkedin.com/in/briancardarella/) 是 Web 和移动开发公司 [DockYard](https://dockyard.com/) 的创始人，他就是这样一位开发人员。

“[我从事软件开发已经超过 30 年了]，我多次看到这种情况，即你的技术决策最终会影响你的生产力，尤其是在应用程序的复杂性不断增加的情况下，” Cardarella 告诉 The New Stack。“在 JavaScript 中，它的本质决定了它很难正确地扩展。”

他补充说，尽管社区做出了努力。

“JavaScript 社区已经做了英雄般的工作，试图解决 JavaScript 的局限性，并且在过去 10 年中，这个生态系统发展和壮大，这令人印象深刻，”他说。“但根本问题是 JavaScript 管理内存的方式以及它在构建应用程序方面所做的事情——[它]真的会失控。”

Cardarella 已经看到企业抱怨开发需要数周或数月才能实现过去只需一两天就能实现的功能，这是由于扩展问题。与此同时，他补充说，交付量下降，而成本却上升。

Cardarella 通过切换到 Elixir 和基于 Elixir 的 Web 开发框架 [Phoenix](https://github.com/phoenixframework/phoenix)（它是开源的）解决了自己的 JavaScript 问题。

据 Cardarella 称，DockYard 是最大的 Elixir 咨询公司。其客户名单包括 [Netflix](https://thenewstack.io/netflix-engineers-rethink-mock-testing-for-graphql/)、纳斯达克和 [Adobe](https://thenewstack.io/adobe-developers-use-webassembly-to-improve-users-lives/)。Phoenix 是 [Chris McCord](https://www.linkedin.com/in/chris-mccord-98b47a37/) 在开始为 DockYard 工作之前创建的。他花了六年时间在 DockYard 的支持下开发了该框架和一个名为 Phoenix LiveView 的前端框架。

## Elixir：一种函数式语言

[JavaScript](https://thenewstack.io/javascript-framework-reality-check-whats-actually-working/) 是一种多范式编程模型，这意味着它支持多种编程风格——包括面向对象、函数式和事件驱动编程。
相比之下，Elixir 是一种函数式编程语言。它改变的是函数，而不是数据。函数式程序不是改变数据，而是简单地添加更多数据。当计算成本更高时，这更具挑战性。

“从历史上看，函数式编程的性能较差，” Cardarella 说。这是因为它会进行内存复制或内存分配，即在函数式编程中创建新内存。

“它表示传入的任何值都必须复制，然后你才能处理该原始值的副本，”他说。“因此，复制是有成本的，并且在计算速度较慢的时代，这种成本非常明显，因为程序运行速度会变慢，需要更多内存，因为你会有某些值的重复。”

> “Elixir 有大量数据表明，它需要更少的人，成本更低，可以轻松完成计算机科学中真正困难的事情，但它没有大公司的支持。”
>
> – Brian Cardarella, DockYard 创始人

它还以不同于 JavaScript 的方式处理[垃圾回收](https://www.cloudbees.com/blog/comparing-elixir-go)。每个 Elixir 进程都有自己独立的堆和垃圾回收器，而不是可能暂停整个应用程序的单个全局垃圾回收器。这意味着长时间运行的进程不会无限期地占用内存而不进行回收。

他说，结果是一个更干净的程序，副作用更少。这意味着开发人员可以更快地行动，并以更低的成本更快地解决问题。

“Elixir 有大量数据表明，它需要更少的人，成本更低，可以轻松完成计算机科学中真正困难的事情，但它没有大公司的支持，”他说。他提到了 [Bleacher Report 的案例研究](https://www.erlang-solutions.com/case-studies/bleacher-report-case-study/)。

Bleacher Report 是 Turner Sports 的一个部门，是全球第二大体育网站。它咨询了 [Erlang Solution](https://www.erlang-solutions.com/)，以从 [Rails](https://thenewstack.io/dhh-wants-to-make-web-dev-easy-again-with-ruby-on-rails/) 迁移到 Phoenix。

“他们基本上能够将他们的团队缩减到以前的 10%，因为他们不再需要那么多人了，” Cardarello 说。

根据案例研究，他们还将生产服务器从 150 台减少到只有 8 台，并看到了以下收益：
- 处理八倍的流量而无需自动扩容的能力；
- 第95百分位的延迟保持在100毫秒左右，并且没有因突发新闻或其他事件引起的流量高峰而受到明显影响；
- 将内容添加到所有流的时间从30-40秒减少到3-4秒；
- 以前需要积极横向扩展的资源密集型功能，现在只需大约1/10的服务器即可运行，且CPU利用率很低。

Warner Media 后来将 Bleacher Report 撤下了 Elixir，Cardarella（以及[这位 Reddit 评论员](https://www.reddit.com/r/erlang/comments/18f3kl3/bleacher_report_gutting_out_otp/)）将其归因于公司政治。

Cardella 说，对于那些习惯了 JavaScript 的人来说，Elixir 仍然会令人沮丧。首先，语法差异很大。相比之下，Rust 已经能够从 JavaScript 社区吸引很多人，因为它的语法中有一些方面让 JavaScript 开发人员感到熟悉，他补充道。

## Elixir 开发工具

除了用于 Web 开发的 Phoenix 框架之外，McCord 还创建了 [Phoenix LiveView](https://dockyard.com/blog/2018/12/12/phoenix-liveview-interactive-real-time-apps-no-need-to-write-javascript)，该框架于 [12 月发布了 1.0 版本](https://dockyard.com/blog/2024/12/03/phoenix-liveview-goes-1-0)。Phoenix LiveView 利用服务器渲染的 HTML 和 Phoenix 原生的 [WebSocket](https://thenewstack.io/the-challenge-of-scaling-websockets/) 工具来构建实时功能。

Cardarella 在一篇博客文章中承认，起初，他很难看到 LiveView 的价值。

“大约在那个时候，我已经在内部宣布了 DockYard 打算与 Ember.js 项目保持距离的意图，”他写道。当时，他们正在后端使用 Phoenix，但他的声明引起了公司内部对其前端专业化的一些担忧。”

“我看到了与我职业生涯中使用过的任何其他语言相比，编写 Elixir 带来的开发人员生产力方面的数量级提升，”他说。“所以当 Chris 就在我眼前构建它时，我正在寻找替代品。不幸的是，它离我的脸太近了，我太老了，看不清这么近的东西，所以我花了很多钱试图将 Elixir 编译为 WebAssembly。”

他继续说，让他信服 LiveView 的是，与基于 JavaScript 的 [前端开发](https://thenewstack.io/introduction-to-frontend-development) 相比，它使几个关键问题变得多么容易，包括：

- 管理应用程序状态；
- 服务器端渲染和应用程序启动时间的复杂性；
- 没有复杂的编译管道；以及
- 生态系统稳定性。（“诚然，JS 生态系统不像 2018 年那样不稳定了，”他补充道。）

还有 [LiveView Native](https://github.com/liveview-native/live_view_native)，这是一个跨平台的开源框架，用于使用与 Phoenix LiveView 相同的代码库构建原生应用程序。它允许开发人员使用一组 Elixir 代码创建原生 UI，从而简化开发过程并实现更快的发布周期。

如果您有兴趣，Elixirland 发布了一个 [Elixir 生态系统中的工具列表](https://elixirland.dev/ecosystem)。

## Web 开发的政治

Cardarello 声称，Elixir 是技术领域中一个伟大的未被讲述的故事。他说它被忽视是因为政治原因、营销原因、资金支持，或者仅仅是因为人们想复制大公司。

“一般来说，你认为软件开发人员在他们所做的事情中做出了最好的技术决策，但事实并非如此，”他说。“相反，我们倾向于看到的是，最终流行的语言和框架之所以流行，是因为它们的能力无关紧要，……而像 Elixir 这样的东西正在解决所有这些问题，并允许数量级的生产力提高，但它尚未被大规模采用。”