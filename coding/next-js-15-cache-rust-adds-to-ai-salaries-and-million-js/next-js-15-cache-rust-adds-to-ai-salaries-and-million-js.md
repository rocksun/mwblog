
<!--
title: Next.js 15的缓存、Rust和AI提升薪资，以及 Million.js
cover: https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2.png
-->

Vercel 对 Next.js 和缓存的最终目标，以及 Rust、Go 和 JavaScript 技能如何为 AI 工作增添价值，以及对 Million.js 的回顾。

> 译自 [Next.js 15 Cache, Rust Adds to AI Salaries, and Million.js](https://thenewstack.io/next-js-15-cache-rust-adds-to-ai-salaries-and-million-js/)，作者 Loraine Lawson。

开发者一直对上个月发布的 Next.js 发布候选版本如何处理缓存有疑问。Vercel 的产品营销副总裁 [Lee Robinson](https://www.linkedin.com/in/leeerob/) 在最近一篇关于 [Vercel 打算在 Next.js 中如何处理缓存和数据](https://threadreaderapp.com/thread/1803824227704877236.html) 的文章中试图解答这些问题。

他在文章中写道，在 [Next.js](https://thenewstack.io/solidstart-launches-next-js-15-releases-with-dx-questions/) 15 的发布候选版本中，许多部分不再默认缓存。

“在 Next.js 15 中，如果我向某个 API 发起请求，或进行数据库查询，结果不会被缓存。这是动态的。如果你想缓存数据，你可以选择这种行为。你需要明确。”

“我们认为本地开发体验应该尽可能‘懒惰’。”——Vercel 产品营销副总裁 Lee Robinson

首先，他解释了预渲染，它与缓存 [数据获取或数据库查询](https://thenewstack.io/best-practices-collect-and-query-data-from-multiple-sources/) 不同，他写道。它是框架在“next build”期间尝试生成静态 HTML 页面的地方。”然后他回答了一系列相关问题，例如为什么预渲染在本地开发和生产环境中的行为不同。

“我们认为本地开发体验应该尽可能‘懒惰’。页面应该按需编译；你不会想在开始之前等待每条路由都编译，”他说。“在保存时预渲染每条路由会很慢，这与我们不断改进快速刷新时间的目标相悖。”

长话短说：他们正在添加一个图标，让你知道页面是否会被预渲染。

从长远来看，他们的目标是让所有异步操作都选择动态渲染。

“我们相信 [部分预渲染](https://thenewstack.io/vercels-next-js-14-introduces-partial-pre-rendering/) 将成为构建 Next.js 应用程序的默认方式。在这个世界里，路由可以是静态的，也可以是动态的，”Robinson 写道。

然后，即使应用程序的大部分是动态的，开发人员仍然会立即在浏览器中获得应用程序的 shell，然后动态部分会并行流入。

“如果你想让更多路由包含在预渲染中，你可以将页面动态部分包装在 React Suspense 中以定义一个回退状态，”他补充道。“Next.js 然后可以在构建过程中将预渲染到 Suspense 边界。在提供页面时，用户会立即看到预渲染的 HTML，同时流式传输路由的动态部分。”

他以一个关于 Next.js 15 的含义列表结束：

- `fetch` 请求不再默认缓存；- 路由处理程序不再默认缓存；
- 当使用 `<Link>`或 `useRouter` 时，客户端导航将不再保留上一个页面的缓存版本 30 秒。

## Rust + AI = 更多薪资

根据内容运营软件 [StoryChief.io](https://www.storychief.io/) 的研究，[Rust](https://thenewstack.io/rust-the-future-of-fail-safe-software-development/) 或 [Golang](https://thenewstack.io/how-golang-range-simplifies-data-structure-iteration/) 可以将与 [人工智能](https://thenewstack.io/ai-for-developers-how-can-programmers-use-artificial-intelligence/) 相关的职位薪资提高多达 30,000 美元。

该公司分析了 Glassdoor 上 12,643 个提及 AI 并显示任何薪资信息的职位列表。它如何得出这些数字有点复杂，但基本上它识别了与技能、教育和经验相关的最常见关键词，然后根据职位所在的州和其他标准估计每个关键词的薪资价值。

根据他们的计算，Rust 平均增加了 29,480 美元的薪资，Go 增加了 21,080 美元。[Python](https://thenewstack.io/python-mulls-a-change-in-version-numbering/) 将意味着额外增加 13,100 美元，而 [PyTorch](https://thenewstack.io/pytorch-docker-and-ai-openness-highlight-ai_dev-europe/) 则转化为 7,223 美元。[JavaScript](https://thenewstack.io/javascript-framework-maintainers-on-unification-potential/) 平均增加了 5,952 美元。

奇怪的是，R——通常用于数据工作——评级为负 6,000 美元，这并不意味着它降低了薪资，而是表明该语言的薪资往往低于平均水平，该公司表示。

## 了解 Million.js，一个极简的 JS 编译器
Million.js 是一个开源的 JavaScript 编译器，它采用极简主义的方法。我们没有看到太多关于它的信息，创建者 Aiden Bai 也没有回复我们的采访请求。但本周我们发现了一篇由程序员和 LogRocket 技术作家 Isaac Okoro 撰写的 [关于 Million.js 的深入评论](https://blog.logrocket.com/million-js-adoption-guide)。

“它允许你像 React 一样编写 JSX 代码，但编译你的代码，这样你就可以向浏览器发送更少的 JavaScript 代码，”Okoro 写道。“Million 在更新 DOM 时采用了一种细粒度的方法。这与 React 处理 DOM 更新的方式不同，React 会更新整个 DOM 树。Million 的方法减少了内存使用，提高了渲染速度和性能，而不会牺牲灵活性。”

Okoro 写道，Million.js 通过使用块来实现这一点，块是轻量级且高性能的高阶组件，“针对渲染速度进行了优化，你可以将其用作 React 组件”。

根据 Okoro 的说法，Million.js 拥有以下优势：

- “极快”的速度；
- 低内存使用；
- 易于使用；
- [与 React 和 React 框架（如 Astro）集成](https://thenewstack.io/how-quiks-astro-integration-beats-both-react-and-vanilla-js/)、Gatsby、Next.js；
- 文档。

然而，Okoro 指出学习曲线、缺乏社区和生态系统以及对其未来的疑问是缺点。
