
<!--
title: React 诞生十年后，前端是否已进入后 React 时代？
cover: https://cdn.thenewstack.io/media/2024/07/29ba2c30-getty-images-hfoa7gkx1bq-unsplash.jpg
-->

在 2014 年 Oscon 大会上 React 发表了一场有影响力的演讲，十年后，我们重新审视 React 背后的概念，看看它们在 2024 年是否仍然适用。

> 译自 [After a Decade of React, Is Frontend a Post-React World Now?](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)，作者 Richard MacManus。

十年前，Facebook 开发者 Christopher Chedeau 在 [Oscon](https://www.youtube.com/watch?v=tXeBZ3WujTs)（O’Reilly 开源大会）上做了一场关于一个名为 React 的相对较新的 JavaScript 框架的演讲。正如 The New Stack 的 Chris Dawson [当时所指出的](https://thenewstack.io/javascripts-history-and-how-it-led-to-reactjs/)，这场演讲非常引人入胜，因为它解释了 React 背后的概念——不仅仅是 *如何* 工作，而是 *为什么* 被创建。

鉴于 React 自 2014 年 Oscon 以来在前端开发生态系统中的主导地位，在这篇文章中，我将重新审视 React 背后的概念，并确定它们在多大程度上经受住了时间的考验。这在 2024 年尤其重要，因为像 [Microsoft Edge](https://thenewstack.io/from-react-to-html-first-microsoft-edge-debuts-webui-2-0/) 这样的主要软件产品已经开始探索我称之为 [后 React 方法](https://thenewstack.io/pivoting-from-react-to-native-dom-apis-a-real-world-example/) 的 Web 开发（Microsoft Edge 团队称之为“HTML-first”）。此外，像 Svelte 和 Solid 这样的非 React 框架为前端开发人员提供了越来越可行的替代方案。

## 为什么 React 在 2014 年席卷 Web 开发

在 2014 年的演讲中，Chedeau 解释说，React 的起源来自 Facebook 在 2010 年 2 月作为开源软件发布的 PHP 扩展，名为 XHP。“我们扩展了 PHP 语法，以便在其中放入 XML，”Chedeau 说。这样做主要是出于安全原因，但也导致了“非常快的迭代周期”。

然而，由于它是 PHP——一种服务器端语言——每次发生更改时，页面都需要完全重新渲染。因此，Facebook 团队决定将 XHP 的许多应用程序逻辑迁移到 JavaScript，即浏览器的原生脚本语言，因为他们希望避免往返——从服务器到客户端，再回到服务器，再回到客户端，等等。然后，他们寻找优化 JavaScript 使用方式的方法。

> “我倾向于将 React 视为 DOM 的版本控制”
>
> – Christopher Chedeau，2014（来自 AdonisSMU）

长话短说，他们最终创建了一个名为 React 的 JavaScript 库：关键创新是创建了一个“虚拟 DOM”。DOM（文档对象模型），正如维基百科 [很好地解释](https://en.wikipedia.org/wiki/Document_Object_Model) 的那样，是“HTML 文档的面向对象表示，充当 JavaScript 和文档本身之间的接口”。

正如 Chedeau 所解释的，React 为您提供了 DOM 的两个“虚拟”副本（每次交互的之前和之后），您可以从中运行“差异”过程来确定到底发生了什么变化。然后，React 将这些更改应用于实际的 DOM——这意味着只有 DOM 的一部分发生了更改，而其余部分保持原样。反过来，这意味着网页的只有一部分需要为最终用户重新渲染。

![](https://cdn.thenewstack.io/media/2024/07/06976199-react_2014_oscon.jpg)

*Facebook 开发者 Christopher Chedeau 在 Oscon 2014 上讲解 React。*

Chedeau 有一个简洁的引言概括了 React 的优势：“我倾向于将 React 视为 DOM 的版本控制”（归功于 AdonisSMU）。因此，在这个框架中，React 就像前端的 Git。

另一个创新是创建了 JSX（JavaScript XML，正式名称为 JavaScript 语法扩展），一种类似 XML 的 JavaScript 语法扩展。早在 2013 年，Facebook 的 Pete Hunt [就描述了它](https://tr.legacy.reactjs.org/blog/2013/06/05/why-react.html) 为“一种可选的语法扩展，如果你更喜欢 HTML 的可读性而不是原始 JavaScript”。

React 背后的一个重要理念是它不是基于模板的，不像以前的流行框架（如 Ruby on Rails 和 Django）。正如 Hunt 所指出的，“React 通过将用户界面分解为组件来采用不同的方式构建用户界面 [这] 意味着 React 使用真正的、功能齐全的编程语言来渲染视图”。

React 确实提供了一种革命性的 Web 应用程序开发方法——它特别适合数据变化很大的大型应用程序。有影响力的开发人员开始注意到这一点，React 的采用在 2014 年增长。James Long，当时是 Mozilla 的一名开发者，用 2014 年 5 月的一篇名为：[消除用户界面复杂性，或 React 为什么很棒](https://archive.jlongster.com/Removing-User-Interface-Complexity,-or-Why-React-is-Awesome) 的帖子总结了围绕 React 的乐观情绪（如果你想了解技术细节，请阅读这篇文章，但就我们这里而言，标题已经说明了一切！）。

## React 的批评者
尽管 React 很受欢迎，但关于它的抱怨很快就出现了。到 2015 年底，一些开发者开始抱怨 React 的“疲劳”，因为它的学习曲线太陡峭了。[2015 年 12 月](https://medium.com/@ericclemmons/javascript-fatigue-48d4011b6fc4#.vw6jw7oxw)，Eric Clemmons 写道：

“最终，问题在于，选择 React（以及内在的 JSX），你就无意中选择了混乱的构建工具、样板代码、代码风格检查器和时间消耗，你需要在开始创建任何东西之前处理这些问题。”

开发者也对 React 处理状态管理的方式存在问题。以下是 Charlie Crawford 在 The New Stack 上[2016 年 8 月](https://thenewstack.io/flux-overview-react-state-management-ecosystem/) 的说法：

“当组件树变得很高，并且树上彼此相距很远的组件，以及一个组件不是另一个组件的后代，而且这两个组件都依赖于相同的状态时，问题就会开始出现。”

到 2017 年，一些有影响力的开发者开始定期表达对 React 的抱怨。[2017 年 8 月](https://x.com/slightlylate/status/901580389759696897)，Alex Russell——当时在 Google 的 Chrome 团队工作——反驳了虚拟 DOM 很快的说法：

“[…] 实际上，VDOM 很快的说法从来没有任何事实依据，现在仍然没有。它是在用空间换取*便利性*，而不是速度。”

![](https://cdn.thenewstack.io/media/2024/07/d39221bc-russell-react-2021.png)

另一次，[2019 年 6 月](https://x.com/slightlylate/status/1135350142364659713)，Russell 指出“差异化”实际上比其他框架慢：

“事实证明，差异化很慢！其他框架（Svelte、Lit、Vue 等）通过采用不同的方法运行得更快，但它们获得了类似的表面语法，而且它们*小得多*。

## React 的捍卫者
开发者在过去十年中抱怨的一些 React 问题要么已经消散，要么已经得到解决。例如，学习曲线现在已经不是什么大问题了——自 2014 年以来，许多新的前端开发者涌现，许多人都是从学习 React 开始的。状态管理问题也有一些很好的解决方案，比如 Redux 或 React 的 Context API。

即使存在性能问题，React 也有它的捍卫者。其中最主要的是 Vercel 公司，该公司运行着业界领先的 React 框架 Next.js。2023 年 7 月，Vercel 发布了[一篇关于 React 18 的长篇博文](https://vercel.com/blog/how-react-18-improves-application-performance)，这是当前的稳定版本。这篇文章概述了“并发功能（如 Transitions、Suspense 和 React Server Components）如何提高应用程序性能”。

但即使这些功能确实提高了性能，它们是否是以复杂性为代价的呢？有些人，包括 Netlify 首席执行官 Matt Biilmann，认为是这样。[今年 1 月](https://thenewstack.io/keep-it-simple-frameworks-netlify-ceo-praises-astro-remix/)，Biilmann 使用了 Vercel 首席执行官 Guillermo Rauch 的一条推文来嘲笑 Vercel（以及扩展的 React）的复杂性。

![](https://cdn.thenewstack.io/media/2024/01/c73439b4-thejamdev1-1024x525.jpg)

需要注意的是，Netlify 是 Vercel 的直接竞争对手！在这次演讲中，Biilmann 推出了 Astro，作为 Next.js 的一个更简单的框架替代方案。虽然 Astro 允许用户集成 React，但他们也可以选择其他 UI 框架，比如 Vue、Svelte 和 Solid。

就在本周，Netlify 和 Astro [宣布](https://www.netlify.com/blog/netlify-astro-are-partnering/) 建立正式合作伙伴关系——因此我们可以期待 Netlify 更多地宣传“保持简单”的理念。

## 结论：后 React 时代还是否存在？
现在断言我们已经进入后 React 前端时代还为时过早，因为 React——以及 Next.js 等相关框架——仍然非常流行。但有一种感觉是，开发者现在可以选择其他可行的替代方法。Astro 和 Svelte 都没有使用虚拟 DOM 方法，因此开发者现在可以选择不依赖 React 的 Web 框架（尽管 Astro 仍然可以选择 React）。

微软 Edge 正在推行的“HTML 优先”方法，Alex Russell（该团队成员）将其描述为“现代 Web Components + HTML 优先架构”。

无论哪种方式，前端开发不再像几年前那样依赖 React 了。如果你是一名进入该行业的新 Web 开发者，你甚至可以考虑完全放弃 React——尽管承认，这会降低你的短期工作机会。但至少这是一个需要认真考虑的选择，甚至可能帮助你找到一家有远见的雇主。
