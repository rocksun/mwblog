<!--
title: StyleX 对决 Tailwind：Meta 如何解决 CSS-in-JS 可维护性难题
cover: https://cdn.thenewstack.io/media/2026/01/b24238ed-a-c-isuawotupey-unsplashc.jpg
summary: 文章对比了Meta的StyleX和Tailwind，强调StyleX在大规模应用中的可维护性优势。它通过静态编译解决CSS全局性问题，更适合巨型项目。
-->

文章对比了Meta的StyleX和Tailwind，强调StyleX在大规模应用中的可维护性优势。它通过静态编译解决CSS全局性问题，更适合巨型项目。

> 译自：[StyleX vs. Tailwind: Meta's Take on CSS-in-JS Maintainability](https://thenewstack.io/stylex-vs-tailwind-metas-take-on-css-in-js-maintainability/)
> 
> 作者：Richard MacManus

最近，随着 [Tailwind](https://thenewstack.io/tailwind-creator-says-ai-played-a-role-in-downsizing/) 在人工智能时代努力维持运营，它登上了新闻头条。但它并非唯一一个争夺开发者关注的“CSS-in-JS”解决方案。最近，Meta一直在推广其开源的、基于React的样式项目 [StyleX](https://stylexjs.com/)。与Tailwind不同，它不是一个框架——Meta称其为 [JavaScript 库](https://github.com/facebook/stylex)，更广泛地说，是一个“系统”。但无论如何，StyleX是直接使用样式表语言CSS（层叠样式表）的又一个替代方案。

在去年年底的 [一篇博客文章](https://engineering.fb.com/2025/11/11/web/stylex-a-styling-library-for-css-at-scale/) 中，Meta 的 Melissa Liu 将 StyleX 称为“大规模应用程序的样式系统”。Liu 是一名 React 组件软件工程师，也是 Meta StyleX 项目的核心成员。她在博客文章中指出，StyleX 已成为“Meta 产品（如 Facebook、Instagram、WhatsApp、Messenger 和 Threads）以及外部公司（如 Figma 和 Snowflake）的标准化样式系统。”

关于 CSS-in-JS 的简要说明：这些解决方案允许开发者使用 JavaScript 而不是 CSS 来定义样式。但是，在 CSS 本身变得 [越来越复杂](https://thenewstack.io/web-development-in-2025-ais-react-bias-vs-native-web/) 的时代——Google 的 [CSS Wrapped 2025](https://chrome.dev/css-wrapped-2025/) 去年列出了 Chrome 中的 22 个新 CSS 功能——为什么还需要基于 JavaScript 的样式系统呢？

至少对 Meta 而言，答案是：规模和代码可维护性。

## 大规模样式设计的挑战

本周，Liu [参加了 Meta 技术播客](https://engineering.fb.com/2026/01/12/web/css-at-scale-with-stylex/)，与她的同事 Pascal Hartig 讨论 StyleX。她指出，Facebook 的网站由“数千个组件”组成——其中无疑包括大量的样式组件——并且每天必须应对“数亿用户”。她解释说，这种复杂性和规模要求更好的方式来管理样式。

她说：“我们还需要从开发者的角度考虑什么是可维护的。” “能够拥有如此庞大的代码库并使其保持可维护性……如果广告团队的某个人正在构建一个组件，他们在那里声明了一个按钮类；然后，Instagram 的某个人也在创建一个按钮类……因此我们需要一个系统……来使其保持可维护性。”

这意味着，对于像 facebook.com 这样的大型网站，单独编写 CSS 代码是不够的，更不用说当它与 Instagram 或 Threads 等其他应用程序集成时。这里的问题是 CSS 是全局的；如果，正如 Liu 所说，Meta 广告团队的某个人更改了 CSS 中的一个按钮类，它可能会无意中覆盖或与 Instagram 的按钮类冲突。

在她的博客文章中，Liu 解释了在 StyleX（以及一个名为 cx 的前身）出现之前直接使用 CSS 的问题：

“在如此大的规模下提供 CSS 导致了捆绑包之间的冲突，管理样式表之间的依赖关系变得困难，并且在协调经常导致特异性冲突的竞争规则方面面临挑战。”

## StyleX 与 Tailwind 的比较

那么 StyleX 是如何工作的呢？如上所述，它是一个 JavaScript 库——因此你编写的是 JavaScript 代码而不是 CSS 语言。由于这是 Meta 的项目，StyleX 已针对 React 进行了优化，但在 [一份 FAQ](https://stylexjs.com/docs/learn/thinking-in-stylex/) 中，Meta 坚称它与框架无关：

“StyleX 是一种 CSS-in-JS 解决方案，而不是 CSS-in-React 解决方案。尽管 StyleX 目前已针对 React 进行了优化，但它被设计为可与任何允许在 JavaScript 中编写标记的 JavaScript 框架一起使用。”

> “StyleX 的核心是一个编译器，它在构建时提取样式并生成静态样式表。”  
> **— Melissa Liu，Meta StyleX 核心开发者**

Liu 在她的博客文章中指出，“StyleX 的核心是一个编译器，它在构建时提取样式并生成静态样式表。”因此，最终结果是 CSS，但它是通过 JavaScript 生成的，并且处理（转换为 CSS）是在构建时完成的。

Tailwind 也是一个 CSS-in-JS 解决方案，与 StyleX 有一些相似之处。Tailwind 允许开发者在 HTML 文件中创建“实用工具类”，这些类在构建时被转换为静态 CSS 文件。主要区别在于语法：Tailwind 使用其自己的特殊 `classNames`，而 StyleX 使用 JavaScript 对象。

主要由于其独特的语法，可维护性一直是 Tailwind 的一个争议问题。在 [2023 年的一篇文章](https://thenewstack.io/tailwind-css-debate-another-cool-tool-dissed-by-web-purists/) 中，我指出许多开发者不喜欢 Tailwind 强加给 HTML 的丑陋标记，这反过来使代码库更难以维护。

尽管 Liu 在 Meta 技术播客上只是简要提及了 Tailwind，但她似乎对可维护性也有同样的担忧。她承认开发者喜欢它的快速工作方式，但补充说：“使用像 Tailwind 这样的系统，你会牺牲可维护性。”

> “虽然 Tailwind 很大程度上是 CSS-in-JS，但作为一种语法，它在作为 CSS-in-JS 方面表现不佳。”  
> **— Naman Goel，Meta StyleX 核心开发者**

StyleX 团队的其他成员则更为 kritisch。StyleX 的联合创始人之一（也是核心开发者） [Naman Goel](https://www.linkedin.com/in/naman-goel-66747242/) 去年 9 月在 [他的个人博客](https://nmn.sh/blog/2025-09-14-tailwind-is-css-in-js) 上发表了一篇文章，认为 Tailwind 因其语法而“不擅长作为 CSS-in-JS”：

“虽然 `className` 抽象非常适合快速原型设计样式，但在常见用例之外它就崩溃了。编写 CSS 关键帧、视图转换、锚点定位以及任何不寻常的样式都意味着需要使用实际的 CSS 文件。”

当然，Web 标准倡导者会说 [回归源代码](https://thenewstack.io/css-frameworks-in-vogue-but-dont-forget-style-fundamentals/)：CSS 并没有错。但 Goel 的观点是，使用 StyleX，你可以（显然）用 JavaScript 满足所有的样式需求。

## 原子化 CSS 的兴起

正如 Goel 在 [后续文章](https://nmn.sh/blog/2025-09-16-serving-atomic-styles) 中指出的，StyleX 和 Tailwind 都是“原子化 CSS”样式设计的例子。根据另一个名为 [Compiled](https://compiledcssinjs.com/) 的 CSS-in-JS 解决方案的文档，[原子化 CSS](https://compiledcssinjs.com/docs/atomic-css) 是一种“通过为每个声明创建一个单一规则（进而创建一个唯一的类名）来减少定义的规则总数的方法——从而实现大规模样式重用。”

> “StyleX 的核心是将其静态编译为原子化 CSS。”  
> **— Liu**

对于 StyleX 而言，原子化 CSS 是其解决方案的关键部分。根据 Liu 的博客文章：

“StyleX 的核心是将其静态编译为原子化 CSS。样式被转换为包含单个样式声明的类，以便在整个代码库中重用，从而使 CSS 大小随着应用程序的增长而趋于稳定。”

在他关于原子化 CSS 的文章中，Goel 指出“捆绑和提供原子化 CSS”有多种方法。但同样，这似乎只适用于具有某种非常罕见规模的网站或应用程序。即使 Goel 也承认，通常单个 CSS 文件效果最好：

“为整个 Web 应用程序拥有一个单一的 CSS 捆绑包几乎总是一个不错的解决方案。如果 Facebook.com 都能搞定，那它可能就足够快了。”

## StyleX 的下一步是什么？

在 2025 年底，StyleX 推出了一个新网站。随之而来的是 [一篇博客文章](https://stylexjs.com/blog/a-new-year-2026)，作者是 Goel 和 Liu。他们写道，“新网站是使用 Waku 构建的，Waku 是一个最小的 React 框架，它让我们能够受益并展示 StyleX 与 React Server Components 的兼容性。” （[The New Stack 在几年前 Waku 刚发布时就对其进行了介绍](https://thenewstack.io/new-framework-lets-devs-explore-react-server-components/)。）

两人补充说，在 2026 年，StyleX 将获得“更好的用户体验、新功能开发和开发者工具”。

StyleX 是一个值得关注的 CSS-in-JS 系统，特别是如果你深入 React 生态系统。但除非你正在运行一个像 Facebook.com 那样规模的网站或应用程序，否则你可能最好还是坚持使用 Tailwind，或者（甚至更好）直接处理 CSS 语言。