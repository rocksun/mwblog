
<!--
title: 2024年度JavaScript回顾：热点新闻
cover: https://cdn.thenewstack.io/media/2023/12/88ad96d3-year-wrapup-1.png
-->

The New Stack 回顾了 JavaScript 在其 29 年发展历程中取得的胜利和留下的伤痕。

> 译自 [The Year in JavaScript: Top JS News Stories of 2024](https://thenewstack.io/the-year-in-javascript-top-js-news-stories-of-2024/)，作者 Loraine Lawson。

[JavaScript](https://thenewstack.io/5-javascript-libraries-you-should-say-goodbye-to-in-2025/) 语言明年将迎来 30 岁生日——但它仍在以新的、有时意想不到的方式不断变化和发展。

今年很好地展现了这门语言的动态性。我们看到了两个新的 JavaScript 元框架的发布，Vue 创建者 [Evan You](https://evanyou.me/) 另一个 JavaScript 工具链的计划，一个新的开源 [React 编译器](https://github.com/facebook/react/tree/main/compiler) 以及 Angular 引入的部分水合——所有这些都表明这门用于 [Web 开发](https://roadmap.sh/roadmaps?g=Web+Development) 的语言蓬勃发展。

但 2024 年也暴露出这门语言中的一些压力和磨损迹象，例如 Google 提出的将这门语言一分为二的提案以及对 JavaScript 代码膨胀的抱怨。

总而言之，对于 JavaScript 来说，这是忙碌的一年。以下是 The New Stack 评选的 2024 年 JavaScript 热门新闻。

## 蓬勃发展的语言：更多选择

有一个流传的笑话是，每个月都会出现一个新的 JavaScript 框架。哎呀，一位开发者甚至建议 [每个开发者都尝试编写自己的框架](https://thenewstack.io/learn-more-by-building-your-own-custom-javascript-framework/)。

然而，有些框架比其他的更重要。

元框架领域一个有趣的参与者是 [TanStack Start，一个基于流行的 TanStack Router 的全栈 React 框架](https://thenewstack.io/tanstack-introduces-new-meta-framework-based-on-its-router/)，其创建者 Tanner Linsley 如是说。该路由器直接与来自 [React](https://thenewstack.io/remix-react-router-merge-jetbrains-ide-for-test-automation/)、Next.js 和 Redwood 的路由器竞争。

此外，JavaScript 框架 Solid 今年也推出了自己的 [元框架 SolidStart](https://thenewstack.io/how-js-meta-framework-solidstart-became-router-agnostic/)。元框架为路由、服务器端 [渲染和构建](https://thenewstack.io/slow-jamstack-builds-netlifys-solution-is-distributed-persistent-rendering/) 等任务添加了额外的功能，尽管 SolidStart 故意与特定路由器解耦。

[Solid](https://thenewstack.io/solid-js-creator-outlines-options-to-reduce-javascript-code/) 的创建者 Ryan Carniato 三年前开始着手 SolidStart 的工作，因为他看到服务器端渲染将促使人们“真正想要一个元框架”，他告诉 The New Stack。

“现在人们期望你有一些可以处理它的启动器，所以我最初就是出于这个原因构建 SolidStart 的。”

最后，Vite 和 JS 框架 Vue 的创建者 Evan You 宣布成立一家名为 VoidZero, Inc. 的新公司，该公司将致力于构建一个 [统一的 JavaScript 工具链](https://thenewstack.io/vite-creator-launches-company-to-build-javascript-toolchain/)。这源于他在一个名为 Rolldown 的新捆绑器上的工作，当时他意识到他在 Vite 中遇到的挑战反映了 JavaScript 生态系统支离破碎的现状。

“这样的工具链不仅会增强 Vite，还会推动整个 JavaScript 生态系统的显著改进，”Vue 在一篇 [关于此举的博客文章](https://voidzero.dev/posts/announcing-voidzero-inc) 中写道。

## Angular 引入增量水合

[Angular 对各个框架](https://thenewstack.io/angular-vs-react-how-to-choose-the-right-framework-for-you/) 提供的部分水合功能进行了调查，发现尽管有很多讨论，但实际的实现却很少。例外的是 Astro，它在其 [Island 水合方法](https://thenewstack.io/astros-journey-from-static-site-generator-to-next-js-rival/)（去年推出）中。该框架在 [Angular 19 中发布了增量水合](https://thenewstack.io/angulars-approach-to-partial-hydration/)。

创建 Angular 的增量水合耗时数年，始于 15 版本中可延迟视图的发布。可延迟视图是 [Angular 的原生延迟加载](https://thenewstack.io/deferable-views-page-load-improvements-coming-to-angular/) 内置框架原语，用于能够延迟加载块并指定加载时间。

事件重播（在 Angular 18 中发布）和延迟块也发挥着作用。Angular 中的延迟块用于延迟执行组件模板的某些部分，直到需要它们为止。开发者可以指定触发交互的内容。

## JavaScript 在 2024 年遇到的问题

但 JavaScript 世界并非尽善尽美，并且这门 29 岁的语言也显现出一些压力迹象。

例如，并非所有人都喜欢众多框架。一些人[提倡回归原生JavaScript](https://thenewstack.io/frontend-strategies-frameworks-or-pure-javascript/)。TNS高级编辑Richard MacManus探讨了[我们是否身处后React时代](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)。事实证明，今年的JavaScript现状调查确实显示出React使用人数略微下降——2%。然而，总的来说，它仍然是[受访者中最常用的框架](https://thenewstack.io/javascript-python-and-java-among-tops-in-language-rankings/)。

![](https://cdn.thenewstack.io/media/2024/12/4c96533c-front_end_frameworks_ratios.png)

但今年的调查确实显示[TypeScript的使用超过了JavaScript的使用](https://2024.stateofjs.com/en-US/usage/)。本月发布的调查发现，67%的受访者表示他们编写TypeScript代码多于JavaScript代码。TypeScript是带有类型语法的JavaScript。

然而，这并非唯一表明对该语言不满的指标。十月，[Google提议将该语言拆分为两部分](https://app.daily.dev/posts/the-proposal-to-split-javascript-into-two-languages-an-overview-mdlmsjvsq)：

1. JS0将只包含基本功能，但仍直接在浏览器中实现。
2. JSSugar将提供附加功能、扩展功能和语法。但它需要使用类似Webpack的工具编译成JS0。

鉴于一些著名的[开发者今年对JavaScript的复杂性和膨胀提出了批评](https://thenewstack.io/developers-rail-against-javascript-merchants-of-complexity/)，这可能是对公众反弹的回应。但是——我们知道这可能会让一些人[感到震惊](https://www.youtube.com/watch?v=HMIyDf3gBoY)——它也[在程序员中引发了辩论](https://leaddev.com/technical-direction/should-javascript-really-be-split-in-two)，一些人[对谁将从中受益表示担忧](https://www.reddit.com/r/programming/comments/1ggaljn/who_stands_to_benefit_from_a_proposed_split_of/)，另一些人质疑这是否会毁掉这门语言，还有一些人[建议使用WebAssembly](https://medium.com/@phillipgimmi/javascript-vs-jssugar-vs-webassembly-6fd4bd41fe1f)来达到相同的结果。

一位[开发者](https://news.ycombinator.com/user?id=sshine)指出JavaScript是两种语言：

1. “JavaScript，互联网最初的汇编语言，不需要新的语言特性。”
2. “JavaScript，前端Web开发语言，是无限多个编译回ES5的子语言的分形。”

说到分裂，让我们不要忘记今年围绕谁应该拥有“JavaScript”名称的实际斗争。2024年，Deno向美国专利商标局(USPTO)请愿，要求[USPTO取消Oracle对JavaScript的商标](https://thenewstack.io/deno-petitions-to-cancel-oracles-javascript-trademark/)。

最终，所有这些都为JavaScript的30岁生日设定了一个引人入胜，甚至可能令人暴躁的基调。
