<!--
title: Remix挑战Next.js成为React框架新宠
cover: https://cdn.thenewstack.io/media/2024/02/624b8b7a-20221207_chello_shopify_incu0382-1b-1024x683.jpg
-->

Remix 是一款崛起中的 JavaScript 框架，正在与 Next.js 展开竞争，但其起源竟可追溯到 10 年前。我们与 Remix CEO Michael Jackson 进行了交谈。

> 译自 [Remix Takes on Next.js in Battle of the React Frameworks](https://thenewstack.io/remix-takes-on-next-js-in-battle-of-the-react-frameworks/)，作者 Richard MacManus 是 The New Stack 的高级编辑，并撰写有关 Web 和应用程序开发趋势的文章。此前他于 2003 年创立了 ReadWriteWeb，并将其打造成为世界上最有影响力的科技新闻网站之一。

JavaScript 框架 Remix 和 Astro 当前[获得了大量关注](https://thenewstack.io/keep-it-simple-frameworks-netlify-ceo-praises-astro-remix/)，作为 Next.js 的更简单替代方案，Next.js 是 React 时代占主导地位的框架。 在这两款新兴框架中，[Remix](https://thenewstack.io/im-in-an-open-relationship-with-remix/) 是 [Next.js](https://thenewstack.io/vercels-next-js-14-introduces-partial-pre-rendering/) 的更直接竞争对手，因为它们都基于 React 库([Astro](https://thenewstack.io/how-to-use-astro-with-a-sprinkling-of-react/) 是框架无关的，用户不仅可以与 React 一起使用，还可以与 Vue、Svelte 等一起使用)。

Next.js 和 Remix 有另一个共同点是它们的企业支持。Next.js 由风险投资支持的公司 Vercel 赞助，而 Remix 在 2022 年 10 月[被 Shopify 收购](https://shopify.engineering/remix-joins-shopify)。

因此，Remix 和 Next.js 似乎有很多共同点，但你可能没有意识到的是，Remix 的起源可以追溯到 Next.js 几年前。所以，为了更多了解 Remix 的历史(和未来)，我采访了它的共同创始人兼 CEO [Michael Jackson](https://www.linkedin.com/in/mjijackson/)。

## React Router 和 Remix 的起源

Remix 的最大不同点可能是它的服务端渲染方式。Remix [将自己描述为](https://remix.run/)“无缝的服务端和浏览器运行时”，利用“分布式系统和原生浏览器功能而不是笨重的静态构建”。它建立在 Web Fetch API 而不是 Node 之上，并且“可以在任何地方运行”。

Remix 的服务器方法的核心可以追溯到 2014 年，当时其创建者发布了 React Router。事实上，Remix 文档声明“90% 的 Remix 实际上只是 React Router”，它称之为“一个非常老的、非常稳定的库，可能是 React 生态系统中最大的依赖项”。

“React Router 是我们在 React 本身还在努力获得普及的时候启动的一个项目，”Jackson 告诉我，“现在回头看通用的网络格局，React 是王者，这很难相信。”

React Router 创建于 2014 年，由当时 Twitter 的工程师 Jackson 和一家名为 Instructure 的公司的工程师 [Ryan Florence](https://www.linkedin.com/in/ryanflorence/) 创建。这对搭档之所以创建 React Router，是因为这样的库在 React 本身还不存在。简单来说，React Router [实现了](https://reactrouter.com/en/main/start/overview)“客户端路由”—— 意味着可以在不完全重载页面的情况下加载新的 JavaScript 组件。

Jackson 和 Florence 在 React Router 周围建立了咨询公司，但多年来他们没有提供自己的 React 整体使用方案。Guillermo Rauch 用 Next.js 打败了他们，Next.js 在 2016 年 10 月首次亮相。但是直到 2020 年，Rauch 的公司，最初叫 ZEIT 但[在 2020 年 4 月改名为 Vercel](https://thenewstack.io/vercels-frontend-and-the-rise-of-the-hybrid-developer/)，才开始认真商业化 Next.js。就在这时，Remix 诞生了。

“2020 年，我们决定接管其余的技术栈，看看我们是否可以搭建一些从端到端更完整的东西，在 React Router 之上构建一个功能齐全的框架，”Jackson 说，“所以这就是 Remix。Remix 基本上是我们对 Web 开发的所有见解，建立在 React Router 的基础上。”

他补充说，Remix 的许多灵感来自老式 PHP 框架，以及 Web 2.0 时代最流行的 Web 框架之一 Ruby on Rails。

## Remix 如何在 Shopify 的技术栈中使用

Jackson 在我们的访谈中提到过几次，多年来许多“大型企业公司”都在 React Router 之上开发——其中之一就是 Shopify。“所以他们已经认识我们，”他说，“并且在收购 Remix 之前就已经使用我们的软件了。”

事实上，Shopify 曾试图构建类似 Next.js 的框架。就在收购 Remix 前的不到一年的 2021 年 11 月，Shopify 发布了一个基于 React 的 Web 开发框架，[称为 Hydrogen](https://thenewstack.io/dynamic-by-default-shopifys-hydrogen-a-new-take-on-react/)。当时，Shopify 的首席工程师 Ilya Grigorik 告诉我，公司的目标是“使服务器端渲染和动态商务很好地协同工作”。Hydrogen 是他们为此定制的解决方案。

但是当 Remix 在 2022 年 10 月被收购时，它很快成为了 Shopify 的新默认框架。Jackson 告诉我，Shopify.com 使用 Remix 重建。公司的 iOS 和 Android 应用 Shop.app 也使用 Remix 重建。但是等等，还有更多。Jackson 说，Hydrogen 现在“完全建立在 Remix 之上”。

“所以现在，Hydrogen 在很大程度上起着 Remix 之上的库的作用，”他说，“Remix 是 Hydrogen v2 的所有基础。”

Shopify 当前的项目之一是重建所有电子商务客户使用的控制面板。Jackson 说这是该公司最大的软件项目(“数百万行代码”)。这个项目有趣的一个方面是，他们在 Remix 中使用 [Vite](https://thenewstack.io/dev-news-babylon-js-6-0-vite-update-and-the-perils-of-ai/) 作为编译器，这是来自 [Vue 社区](https://thenewstack.io/vue-2023/)而不是 React 社区的软件。Jackson 将 Vite 描述为“类似于 Webpack”的 JavaScript 模块打包器。

Jackson 还指出也在鼓励第三方开发者使用 Remix。

“我们发布了一个模板，允许在第三方应用上开发的开发者实际上也用 Remix 构建他们的应用，并且，你知道的，与 Shopify 认证并做所有的这些事情。所以 [...] Remix 不仅是我们向商户推荐的，也是我们向与 Shopify 集成的开发者推荐的。”

## Remix 如何应对 React 的复杂性

去年前端开发的一个主题是 React 生态系统日益复杂。我问 Jackson 是否同意 React [变得太复杂](https://thenewstack.io/web-development-in-2023-javascript-still-rules-ai-emerges/)了。

“是的，我看到了反对的声音，”他承认，“有很多人说，哦，天哪，React 过去感觉更简单。我对 React 社区的恳求是，要意识到这里有很多好的想法。目前许多这些前沿的 React 想法的实现 [...] 是 Next.js。这些想法首次在 Next.js 中发布和讨论。”

Jackson 的观点是，Remix 对新的 React 特性有自己的实现，所以值得开发者检查它们。

“Ryan 和我构建 Remix 的全部意义——当我第一次看 Next 时，我甚至无法让它返回适当的状态码。对我来说，非常早期，[...] 就很明显，我们非常非常重视不同的事物。”

他列出渐进增强作为 Next.js 似乎不重视但 Remix 重视的事情之一。

“对我们这些做了一段时间 Web 的人来说，这个术语[渐进增强]传达了很多理解和对用户的价值。这是我们真的非常关心的东西，当你使用 Remix 构建时，这是你总能得到的。”
