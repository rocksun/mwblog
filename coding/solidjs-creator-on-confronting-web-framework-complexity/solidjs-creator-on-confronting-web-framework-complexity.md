
<!--
title: SolidJS创建者谈Web框架复杂性
cover: https://cdn.thenewstack.io/media/2025/01/ef80dc2f-reactcode.jpg
-->

Ryan Carniato，SolidJS 和 SolidStart 的创建者，表示 Angular 和 Vue 将是 2025 年值得关注的 JavaScript 框架。

> 译自 [SolidJS Creator on Confronting Web Framework Complexity](https://thenewstack.io/solidjs-creator-on-confronting-web-framework-complexity/)，作者 Loraine Lawson。

前端专家、Solid.js 创建者近日预测，Angular 和 Vue 将是今年值得关注的框架。

“[在 1 月 6 日的一篇博客文章中](https://dev.to/this-is-learning/javascript-frameworks-heading-into-2025-hkb)，[Carniato 写道](https://github.com/ryansolid)：“Vue 和 Angular 是我明年会关注的框架。这并非因为我期待它们带来什么惊人的创新，而是因为这些工具在让开发者感到满意方面做得更出色。有时候，最好的工具并非‘最佳’工具。”

事实上，Google 的产品和开发者关系负责人最近宣布，[提升开发者体验将是 Angular 2025 年的重点](https://blog.angular.dev/angular-2025-strategy-9ca333dfc334)。

如果您不熟悉 Carniato，他是 [SolidJS 框架](https://github.com/solidjs) 和 2024 年推出的元框架 [SolidStart](https://thenewstack.io/how-js-meta-framework-solidstart-became-router-agnostic/) 的创建者。

像许多框架作者一样，他也是 JavaScript 领域的思想领袖——这一荣誉称号源于他对 JavaScript 的深入演讲和写作。他经常被其他框架创建者和 JavaScript 行业的领导者引用。

Carniato 预计前端框架领域将会是平静的一年——这段反思期可能是一件好事，因为社区正在努力应对其自身创造的复杂性。

Carniato 写道：“追求简洁并没有让 Web 开发变得更简单。我们有很多复杂性需要解决。我们需要做出许多艰难的决定，来判断哪些技术值得我们投资和付出努力。”

虽然“下一代解决方案的原始能力已经存在”，但 Carniato 不确定是否已经找到了合适的组合来创建一个“易于使用的”解决方案。

他写道：“但至少我们开始承认，在我们追求简洁的过程中，我们走上了一条以新的方式增加复杂性的道路。”

在他的博客文章和最近的 [五小时直播](https://www.youtube.com/watch?v=D1XN8j77Ntk)（我们观看了其中两小时）中，他解释了一些造成复杂性的原因。

## 同构 SPA 与 分离执行 MPA

据 Carniato 称，JavaScript 中出现了一种分歧，即使用分离执行的多页面应用程序（例如 Astro 中的 [Islands](https://thenewstack.io/astro-launches-new-server-islands-and-partners-with-netlify/) 或服务器组件）和本质上是同构的服务器优先单页面应用程序 (SPA)。

![Solid.js 创建者 在最近的直播中展示了同构框架和分离执行框架之间的区别](https://cdn.thenewstack.io/media/2025/01/a1c19542-ryancarniatoisomorphicvssplit-2.png)

*Ryan Carniato 在最近的一次直播中分享了一张关于同构框架和分离执行框架之间差异的幻灯片。*

同构 JavaScript 或通用 JavaScript 涉及使用可以在浏览器（客户端）和服务器端运行的 JavaScript 代码编写应用程序。

根据 [Sanity.io 的词汇表](https://www.sanity.io/glossary/isomorphic-javascript)，“使用同构 JavaScript，服务器会生成网页的初始视图并将其几乎立即发送到客户端进行渲染，同时在后台下载完整的应用程序。”“这种方法减少了服务器负载，并通过加快页面加载速度来显著提升用户体验。”

采用同构方法的框架包括 [Next.js](https://thenewstack.io/vercel-makes-changes-to-next-js-to-simplify-self-hosting/)、[Nuxt](https://thenewstack.io/dev-news-react-19-nuxt-3-11-a-python-gui-tabnine-llms/) 和 [Sveltekit](https://thenewstack.io/rich-harris-talks-sveltekit-and-whats-next-for-svelte/)。

Sanity.io 解释说，它们允许 [开发者“优化 Web 应用程序性能](https://thenewstack.io/how-to-master-javascript-performance-optimization/)，同时保持跨不同环境的兼容性”。使用同构 JavaScript 完成大型项目的公司包括 Airbnb、Facebook 和 Netflix。

依赖分离执行的框架包括 [Astro](https://thenewstack.io/new-astro-releases-incorporates-sessions-new-astro-actions-tools/)、[Fresh](https://thenewstack.io/denos-fresh-uses-server-side-rendering-for-faster-apps/) 和 [Next.js 的 App 目录](https://nextjs.org/docs/app)。
过去五年中，对服务器优先的追求导致了服务器优先元框架的兴起，特别是SelveKit、Astro、[Remix](https://thenewstack.io/remix-takes-on-next-js-in-battle-of-the-react-frameworks/)、[SolidStart](https://thenewstack.io/solidstart-launches-next-js-15-releases-with-dx-questions/)、[Qwik](https://thenewstack.io/javascript-on-demand-how-qwik-differs-from-react-hydration/)、Fresh和[Analog](https://analogjs.org/)，Carniato写道。他还补充说，这也导致了“对Next和Nuxt等现有框架的重大升级”。

> “这是一种尝试在中间相互接近的两个对立面的练习。”
>
> ——Ryan Carniato，JavaScript框架SolidJS的创建者

“过去几年中，受SPA影响的[同构](https://thenewstack.io/doordash-building-isomorphic-javascript-libraries/)（相同的代码在客户端/服务器端运行方式不同）方法与受MPA影响的分裂执行（Islands/服务器组件）方法对抗，以寻求一种通用的解决方案，”Carniato写道。“这是一种尝试在中间相互接近的两个对立面的练习。”

这导致了路由[例如Next App Router的开发](https://thenewstack.io/why-developers-should-give-next-js-app-router-another-chance/)和视图转换路由，他写道。他还提到了其他发展，例如乱序流、服务器函数、乐观更新、服务器岛和单次飞行突变。

但这同时也带来了复杂性。

“当你组合所有这些功能时，事情就不那么简单了，”他写道。“如果2021/22年是对更简单基础的重置，是对我们服务器端起源的回归，那么2024年提醒我们，简单并不总是足够的。”

## 通过编译器处理复杂性

他补充说，框架处理这种复杂性的一种方法是使用编译器。2024年，开发人员看到了[React编译器](https://thenewstack.io/meta-releases-open-source-react-compiler/)和[Svelte 5 Runes](https://svelte.dev/blog/runes)的发布。React编译器是一个“自动优化编译器，它以减少不必要的重新执行而无需手动干预的方式转换代码，”他指出。

另一方面，Svelte 5 Runes“在细粒度的Signals渲染器上提供语法糖，”他写道。简单来说，signals通过充当反应式变量来管理应用程序状态——当它们的值发生变化时，它们会自动更新任何依赖它们的UI部分。

他补充说，这些编译器采用了截然不同的方法。

“React承认重新渲染确实很重要，需要围绕它进行优化，”他说。“Svelte放弃了其最小的语法，转而使用更具表现力的语言，具有增强的功能和更好的性能基础。具有讽刺意味的是，这些立场都与其最初的卖点完全相反。”

## 前端框架预测

鉴于所有这些，Carniato对2025年的发展做出了两个预测：

- **服务器第二种方法。**“我们已经开始看到2024年中期钟摆向中间摆动的一些迹象，Sveltekit、SolidStart和Remix中都出现了SPA模式。[Remix将其非服务器功能移植回React Router](https://thenewstack.io/remix-react-router-merge-jetbrains-ide-for-test-automation/)，”他写道。“SolidStart对服务器函数和单次飞行突变的增量方法为[TanStack Start](https://thenewstack.io/tanstack-introduces-new-meta-framework-based-on-its-router/)奠定了最终的基础，这是一个基于相同原则构建的[React](https://thenewstack.io/redwood-framework-all-in-on-react-server-components/)框架。”
- **成长的烦恼**“毫无疑问，几乎所有非React框架现在都使用Signals，”他写道。“但一段时间过去了，开发人员开始了解其中存在的权衡取舍的深度。”虽然他认为这些问题很小，但他表示它们可能会导致人们对React产生新的尊重。[Signals](https://thenewstack.io/javascript-in-2023-signals-reacts-rsc-and-full-stack-js/)。
