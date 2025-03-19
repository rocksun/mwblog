
<!--
title: Pagoda：Go 程序员的 Web 开发入门套件
cover: https://cdn.thenewstack.io/media/2025/03/ca27c39e-andre-frueh-ldoxcohl7fw-unsplashb.jpg
summary: Go 开发者福音！Pagoda 并非框架，而是 Web 开发启动套件，集成 HTMX、Alpine.js、Bulma 等前端库，后端选用 Echo、Ent、Gomponents。告别 JavaScript 困扰，快速构建现代 Web 应用，亦可灵活替换 Postgres、Redis 等组件，更有 GoShip 衍生，拥抱 SaaS 和 AI。
-->

Go 开发者福音！Pagoda 并非框架，而是 Web 开发启动套件，集成 HTMX、Alpine.js、Bulma 等前端库，后端选用 Echo、Ent、Gomponents。告别 JavaScript 困扰，快速构建现代 Web 应用，亦可灵活替换 Postgres、Redis 等组件，更有 GoShip 衍生，拥抱 SaaS 和 AI。

> 译自：[Pagoda: A Web Development Starter Kit for Go Programmers](https://thenewstack.io/pagoda-a-web-development-starter-kit-for-go-programmers/)
> 
> 作者：Loraine Lawson

2020 年，[Mike Stefanello](https://github.com/mikestefanello) 爱上了 [Go](https://thenewstack.io/introduction-to-go-programming-language/)。

这位软件工程师说：“这是我第一次说我爱上了一种编程语言，甚至是某种技术或工具，但确实是那种反应 —— 我真的非常非常喜欢它。我知道我想用它工作。”

Stefanello 还以个人项目的形式做了很多 [web 开发](https://thenewstack.io/web-development-trends-in-2024-a-shift-back-to-simplicity/)，当时，大多数 web 开发都是基于 [PHP](https://thenewstack.io/why-php-usage-has-declined-by-40-in-just-over-2-years/) 的。有一天，他看到一篇 Hacker News 的帖子，询问开发者他们个人项目的首选 web 技术栈是什么。

他说：“我坐在那里思考，‘我实际上没有这个问题的答案’。我不想回到以前使用的 PHP 中的所有东西。我喜欢 Go。我非常执着，我不能没有这个问题的答案。”

出于这种挫败感和探索，[Pagoda](https://github.com/mikestefanello/pagoda) 诞生了。

他说：“更多的是对 Go 和对 web 开发的热爱。这不像我在考虑应该使用哪种语言来进入 web —— 我是从 web 开发开始的。”

## Pagoda：Go 的启动套件

Pagoda 不是一个框架 —— Stefanello 多次强调这一点。它是一个 web 开发的启动套件，提供了由 Go 代码粘合在一起的前端和后端库。Go 生成服务器端的 [HTML](https://thenewstack.io/why-html-actions-are-suddenly-a-javascript-trend/) 来创建网页。

对于习惯于 [JavaScript 框架](https://thenewstack.io/google-angular-lead-sees-convergence-in-javascript-frameworks/) 世界的前端开发者来说，启动包方法可能看起来很奇怪，但 Stefanello 告诉 The New Stack，后端开发者如果必须使用前端，则希望保持简单。

他说：“我们大多数人不想切换语言，特别是如果你不在后端使用 [JavaScript](https://thenewstack.io/three-javascript-proposals-advance-to-stage-4/) 的话。我可以理解如果你使用 JavaScript，那么你已经习惯了那个生态系统。但如果你不习惯它 —— 而我真的不习惯，我已经很长时间没有真正接触过 JavaScript 了 —— 它感觉像一个有点混乱的生态系统，而且真的很难掌握。”

但这让他陷入了一个困境，即如何在不 [打开 JavaScript](https://thenewstack.io/web-development-in-2023-javascript-still-rules-ai-emerges/) 并致力于大型框架（如 React 和 Vue）的情况下构建一个现代、时尚的 web 应用程序。

他补充说：“完全没有反对它们的意思。显然，它们都是很棒的项目，但这只是个人选择的问题。如果你是后端开发者，你希望尽可能少地关注前端。”

但是为什么不将 Pagoda 制作成 Go 框架呢？他说，因为 Go 社区似乎对此不感兴趣。他说，虽然在 PHP 中有一个大型的单一框架 —— Laravel —— 但在 Go 中并没有真正的等价物。

![Pagoda 创建的主页](https://cdn.thenewstack.io/media/2025/03/9ff64751-pagoda_sample.png)

*Mike Stefanello 在 Pagoda 中制作的示例主页。该功能性网站包含在 repo 中。*

Stefanello 说：“如果你是 Go 的新手，这会让人感到困惑：为什么没有一个框架，为什么人们不喜欢它？但我认为你使用 Go 的次数越多，你就越开始欣赏它。”

[Pushup 是一个例外](https://thenewstack.io/pushup-offers-speed-of-go-in-web-development-framework/)，因为它是一个 Go web 开发框架。还有 [GoBuffalo](https://gobuffalo.io/)，它在其网站上指出它可能是一个框架，但相反，它将自己描述为一个“Go web 开发生态系统”，它“主要是 Go 和 JavaScript 库的生态系统，这些库经过精心设计以协同工作。”
Stefanello 早在早期就做出了不创建框架的选择，因为他不喜欢被单一的大型框架束缚的想法。

他说：“它们往往过于臃肿。它们往往会强制你必须遵循的模式。”

他还补充说，开发者往往会超越框架，但随后会被框架锁定。然后存在框架作者将停止维护它的风险。

相比之下，他补充说，启动套件可以让 web 开发者 [快速启动 web 开发](https://thenewstack.io/pushup-offers-speed-of-go-in-web-development-framework/)，而没有完整框架的缺点。
“这个启动套件的好处在于它解决了所有这些问题，”他说。“没有严格的模式需要遵循。我提供了一些想法和模式，并将它们粘合在一起，只是为了让事情变得简单，让你快速启动并运行。但这些都不是强制性的。没有任何严格的要求。”

即使他停止维护 Pagoda，[Web 开发者也能拥有他们所需的一切](https://thenewstack.io/web3-stack-what-web-2-0-developers-need-to-know/)，以便继续。

“我基本上只是为你做了很多工作，然后你可以从那里接手，”他说。“你不必担心我是否停止维护它，因为一旦你复制了启动套件，它就是你的了——100% 是你的。”

## Pagoda 前端

Pagoda 包括三个用于前端的库：

1. HTMX，它直接在 HTML 中提供对 AJAX、CSS 转换、WebSockets 和服务器事件的访问。“HTMX 的美妙之处在于它使你能够拥有 Ajax 类型的行为，而无需进行整页重新加载，”他说。“这是你在 JavaScript 驱动的 [单页应用程序](https://thenewstack.io/secure-single-page-apps-with-cookies-and-token-handlers/) 中期望或看到的很多功能。你可以根据需要使用任意数量的功能，而无需编写一行 JavaScript，你可以使用常规 HTML 并在你的网站上创建非常好的交互性。”
2. Alpine.js，Stefanello 说它很像 JQuery，但适用于现代 Web。它是一个最小的工具，用于直接在标记中组合行为。“真正好的是，它在很大程度上都在你的 HTML 中工作，所以你甚至不必实际编写独立的 JavaScript，”他说。“你可以只添加一堆 Alpine 标签和一些声明，并告诉 HTML 该怎么做。而且你可以用它做到的程度非常显著。这是一个我非常喜欢使用的项目。”
3. Bulma，一个易于使用的 CSS 框架。“它非常容易——你只需扔一些类，你就会得到一个相当不错的 UI，”他说。

如果你不喜欢这些库，你可以将它们换掉。例如，Tailwind 可以取代 Bulma，他说，并且可以在几分钟内完成。

## Pagoda 后端

在后端，Pagoda 包括：

1. Echo：一个高性能、可扩展、极简的 Go Web 框架。
2. Ent：一个强大的 ORM，用于[建模和查询数据](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/)。
3. [Gomponents](https://www.gomponents.com/)：用纯 Go 编写的 HTML 组件。它们渲染为 HTML 5，并且可以轻松构建可重用的组件。

Stefanello 再次强调，这些库中的任何一个都可以被替换——事实上，本月，他用 Gomponents 替换了 Go 模板。

“如果你浏览任何 Go 社区，无论是 Reddit、Slack 还是 Discord，或者其他任何地方，都会发现很多人对模板感到沮丧——尤其是在 HTML 方面，它们确实有很多不足之处，”他说。

他列举了这些问题：它们不是类型安全的；如果代码有错误，你必须运行应用程序才能发现；在不同的模板之间传递数据很困难；最后，很难以一种易于在 Web 应用程序中使用的方式编译它们。

Gomponents 是由 [Markus Wüstenberg](https://github.com/maragudk) 创建的库，它渲染为 HTML 5，可以轻松构建可重用的组件。

“这可能是我自项目启动以来，在该项目中做出的最大的代码更改 […]，”他说。“这是一个很大的根本性变化，即从 Go 标准库模板转向使用第三方解决方案。”

根据文档，SQLite 提供了主要的数据存储以及持久的后台任务队列。但是，如果[开发人员更喜欢使用 Postgres 或 Redis](https://thenewstack.io/vercel-offers-postgres-redis-options-for-frontend-developers/)，则可以将其换掉。

该项目甚至被 Fork 以创建 [GoShip](https://github.com/leomorpho/GoShip)，这是一个 Go 加 HTMX 样板，包含 SaaS、AI 工具或 Web 应用程序的所有必需品。