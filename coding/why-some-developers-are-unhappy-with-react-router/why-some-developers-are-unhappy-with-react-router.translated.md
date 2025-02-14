# Remix/React Router 合并后，一些开发者转向 TanStack

![Featued image for: Some Devs Turn to TanStack After Remix/React Router Merger](https://cdn.thenewstack.io/media/2025/02/e7791ff0-remix-becomes-react-router-1024x683.jpg)

像 SolidStart、SvelteKit 和 [Analog](https://thenewstack.io/google-engineer-outlines-whats-next-for-angular/) 这样的元框架与路由器紧密结合，实际上它们就是一体的。以 Remix 为例，情况确实如此，因为它在 11 月与 [React Router v7](https://remix.run/blog/react-router-v7) 合并了。这是维护 Remix 和 [React Router](https://www.travis-ci.com/blog/react-router-demystified-a-developers-guide-to-efficient-routing/) 的团队在去年春天选择将路由器集成到框架中后的首次发布。

然而，并非所有人都对这一变化感到满意，正如最近的 Reddit 帖子所显示的那样。事实上，帖子中的许多开发者表示，他们正在离开该框架/路由器，转而拥抱 [TanStack 路由器及其框架 TanStack](https://thenewstack.io/tanstack-introduces-new-meta-framework-based-on-its-router/)。

## 路由器和框架

元框架是一种位于前端框架（如 React、[Vue](https://thenewstack.io/want-out-of-react-complexity-try-vues-progressive-framework/) 或 Angular）之上或与之并行的工具，用于为构建复杂的 Web 应用程序提供额外的功能和结构。

在前端，路由器管理 Web 应用程序中的导航和 URL，而无需重新加载整个页面。通常，它们作为元框架的一部分发布。

正如 Solid 框架的创建者和元框架 SolidStart 的联合创建者 Ryan Carniato 之前告诉 The New Stack 的那样，[路由器是该软件包的关键组成部分](https://thenewstack.io/how-js-meta-framework-solidstart-became-router-agnostic/)。SolidStart 去年成为第一个出现路由器不可知的框架，部分原因是 [Vite](https://thenewstack.io/vites-new-rust-based-javascript-bundler-available-in-beta/) 和 Vinxi，Vinxi 是一个包装器，它接受多个 Vite 配置并将它们组合在一起，以创建开发者期望的所有高级功能，如服务器组件和服务器操作。

## 路由器如何成为元框架？

Remix + React Router 核心团队成员 [Mark Dalgleish](https://github.com/markdalgleish) 在 React Advanced 2024 的一次演讲中解释说，Vite（一种现代前端构建工具，既充当服务器又充当打包器）承担了构建器和框架曾经执行的更多繁重工作，这次演讲的标题简洁明了，名为“[React Router 如何成为框架](https://www.youtube.com/watch?v=BKi4YwLaMBI)”。

该演示深入探讨了关于这种转变的元框架细节，但简而言之，Remix 和 React Router 长期以来一直深度集成，这很容易实现，因为同一个团队支持两者。他说，对一个的更改通常会导致对另一个的更改。

“React Router 是一个库。说这个没什么争议，”他告诉观众。Remix 在此基础上添加了“一堆东西，但这意味着 Remix 的核心 DNA 实际上是 React Router 框架，”他继续说道。

他详细解释了这是如何发生的，但这在很大程度上归功于 Vite 的发展，特别是即将推出的 [Vite 的环境 API](https://vite.dev/guide/api-environment)。

“Vite 对于 JavaScript 开发者来说是非常棒的工具，但今天我想反过来说，强调它的另一方面，即作为框架维护者，它是一个非常棒的框架平台，这就是为什么我们今天看到这么多框架构建在 Vite 之上，”Dalgleish 说。“因此，当我们开始走这条路时，我们真的想倾向于这种理念，即 Remix 只是一个 Vite 插件。”

这种插件理念并没有完全奏效，因此他们现在切换到的是开源 Remix“主要是一个 Vite 插件”，他补充道。

> “React Router 是一个库。说这个没什么争议。”
>
> – Mark Dalgleish, React Router 核心团队成员

“如果绝大多数特定于打包器的东西都由 Vite 插件完成，并且 Remix 是什么和 React Router 是什么之间的差距继续缩小，那么 Remix 到底是什么？” Dalgleish 质疑道。“为什么不直接消除间接性，让消费者直接从底层库 React Router 导入这些东西呢？”

与此同时，[React Router](https://remix.run/blog/merging-remix-and-react-router) 正在“管理应用程序的入口点，包括你必须运行的命令，”Dalgleish 说。“它现在为你提供了我们在 Remix 中获得的路由模块 API 的官方版本。”

他继续说，它包括文件系统路由、服务器和客户端渲染约定，以及 SPA（单页应用程序）模式和预渲染。

## 可观测性
“这里有一套非常完整的功能集，所以现在可以公平地看待它，并说 React Router 现在是一个框架了，”Dalgleish 说。

前端开发者和 Epic Stack 的创建者 Kent Dodds 也在 2023 年 ViteConf 大会上探讨了 [Vite 和 React Router 之间的联系](https://www.youtube.com/watch?v=rPjj6s7VPQM)，使其成为一个框架。

[React Router 是开源的](https://github.com/remix-run/react-router)，自 2022 年以来一直归 Shopify 所有。The New Stack 试图通过 X 联系该框架的创建者兼 CEO Michael Jackson，但没有收到回复。

## React Router 的影响范围

在 [2024 年 JavaScript 状态调查中，只有 3% 的受访者表示使用 Remix](https://2024.stateofjs.com/en-US/libraries/front-end-frameworks/)。但是 JavaScript 社区影响者和前 Twitch 开发者 Theo Browne，又名 t3dotgg 指出，现在大多数 React 应用程序都使用 React Router 的方法。

“很高兴看到他们承认这一点，并成为将新的 React 构建中的最佳实践引入到每个使用 React 的代码库的途径，”他在他的 [大部分是积极的评论](https://www.youtube.com/watch?v=5B1LScZtrb4) 中说。“我会在这里保持现实。在 Twitch 投入了大量精力到当前网站之后，实际上不可能迁移到 [Next.js](https://thenewstack.io/why-developers-should-give-next-js-app-router-another-chance/)。这使得 [React 19](https://thenewstack.io/react-19-change-angers-some-devs-vector-database-use-jumps/) 的优势能够到达 Twitch 代码库和其他大型代码库。”

## 一些开发者拒绝这种范式

一位 Reddit 用户 MustyMustelidae 在 1 月份发起了一场关于这一变化的讨论，标题颇具讽刺意味：“[React Router v7 必须是一种心理战](https://www.reddit.com/r/reactjs/comments/1iatblk/react_router_v7_has_to_be_a_psyop/)。”

MustyMustelidae 写道：“我拒绝相信 Remix 团队会把他们框架的所有势头都扔到墙上。我认为这个团队由非常聪明的人组成，他们很好地掌握了 JS (JavaScript) 开发的时代精神，我拒绝相信他们不知道更好。”

这位发帖者继续称这种改变是自我破坏。

MustyMustelidae 声明说：“框架不会因为非常明显的原因而这样做。这就像 [Svelte](https://thenewstack.io/youll-write-less-code-with-svelte-5-0-promises-rich-harris/) 用 [SvelteKit](https://thenewstack.io/dev-news-sveltekit-2-0-state-of-rust-survey-and-ai-on-apple/) 扁平化他们的文档，并将其标记为‘作为库’/‘作为框架’。或者如果 [TanStack Start](https://tanstack.com/start/latest) 变成 TanStack Router。在任何情况下，这都不是严格意义上的更糟：为了文档目的，为了品牌目的，为了 SEO 目的，为了支持目的。”

至少有一位发帖者说，他们的整个“非常大的公司”已经切换到 [TanStack Router](https://github.com/TanStack/router)。

一些评论者确实指出 TanStack 仍然存在错误和缺陷，尽管他们对解决这些问题的速度存在分歧。一位发帖者 Veranova 认为 TanStack 应该对问题进行分类。但 Veranova 和其他人仍然推荐它而不是 React Router。

Veranova 写道：“这是我们拥有的公共 API 上设计最好的路由器，所以我相信它会到达那里，但现在底层存在一些严重的缺陷。”

## TanStack Router 创建者的看法

创建 TanStack 的 Tanner Linsley 加入了讨论，指出 TanStack Start 仍处于 beta 阶段，用户可以预期它会发生一些变化。值得注意的是，TanStack Start 也利用了 Vite。（*编者注：TNS 通过 Bluesky 确认是 Linsley 发表了上述言论*。）

他指出，他的元框架 TanStack Start 是一个插件和运行时集合，用于服务器功能（远程过程调用）、服务器中间件、React 服务器组件、流式传输和序列化。他继续说，这是 TanStack Router 的 [服务器端渲染 (SSR)](https://thenewstack.io/how-to-build-a-server-side-react-app-using-vite-and-express/) 的一种“风格”。

他写道：“Start 添加了一个完整的堆栈构建系统，目前它有自己的 CLI，但很快就会变成一个 Vite 插件或类似的东西。这使用 Nitro 将服务器内容部署到基本上任何地方，并编写可在任何地方使用的可移植服务器代码。”

他还提供了一个 [图表，将 TanStack Router 和 TanStack Start](https://tanstack.com/router/latest/docs/framework/react/comparison) 与 Next.js 和 React Router/Remix 进行比较。

## 结论

Vite 正在改变框架；这一点很清楚。Vite 的环境 API 于 1 月份以实验性形式发布。
虽然它主要是为框架创建者设计的，但它可能会导致更多利用 Vite 的元框架发生变化，其中包括 Nuxt、TanStack Start、SvelteKit、SolidStart、[Astro（新 Astro 版本整合了会话、新 Astro Actions 工具）](https://thenewstack.io/new-astro-releases-incorporates-sessions-new-astro-actions-tools/) 和 [Angular 的 Analog.js](https://analogjs.org/)。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。