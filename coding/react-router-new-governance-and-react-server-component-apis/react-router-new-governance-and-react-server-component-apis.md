<!--
title: React Router：新治理模式与 React 服务端组件 API
cover: https://cdn.thenewstack.io/media/2025/07/c002c95d-react_router_v7.jpg
summary: 本文讨论了 React Router 的未来发展，重点是其对 React Server Components (RSC) 的支持、新的治理模式以及与 Remix 的融合。React Router 将提供三种模式：声明式、框架式和数据模式。
-->

本文讨论了 React Router 的未来发展，重点是其对 React Server Components (RSC) 的支持、新的治理模式以及与 Remix 的融合。React Router 将提供三种模式：声明式、框架式和数据模式。

> 译自：[React Router: New Governance and React Server Component APIs](https://thenewstack.io/react-router-new-governance-and-react-server-component-apis/)
> 
> 作者：Loraine Lawson

关于 [Remix 的声明](https://remix.run/blog/wake-up-remix)，它将朝着不同的方向发展，这引起了很多关注，但在喧嚣中，关于 React Router 的消息有点……被埋没了。

[React Router](https://github.com/remix-run/react-router) 现在可能是 Shopify 的 React 框架，但它仍然是 [前端](https://thenewstack.io/introduction-to-frontend-development) 的路由器。计划是继续发展该产品，同时管理新的框架“模式”。

React Router 团队一直忙于新的治理模型，并推出对 [React Server Components (RSC)](https://thenewstack.io/react-server-components-in-a-nutshell/) 的支持，这些组件是 [React](https://thenewstack.io/react-adds-new-experimental-animation-feature/) 组件，在服务器而不是客户端上运行。

The New Stack 采访了 Shopify 电子商务平台的开发者关系经理兼 React Router 指导委员会成员 [Brooks Lybrand](https://www.linkedin.com/in/brooks-lybrand/)。我们询问了 Lybrand 成为框架对 React Router 意味着什么，以及该开源项目的下一步计划。

他说：“在 React Router 方面，我们仍在发布大量新内容。最重要、最令人兴奋的事情是我们对 React Server Component 的支持。”

该团队已经发布了 RSC 支持的预览版，本周将发布特定于 RSC 的 API。Lybrand 说，目标是演示 React Router API 如何实现 [React Server Components](https://thenewstack.io/react-panel-frontend-should-embrace-react-server-components/)。

他说：“这是您在 React Router 应用程序中实际启用 React Server Components 的方式”，并补充说，最初它也将是不稳定的。

## Remix 和 React Router 的融合：接下来会怎样？

React Router 和 Remix 都是 Ryan Florence 和 Michael Jackson 的作品，他们现在在 Shopify 工作。去年在 React Conference 2024 上，创建者宣布 Remix 和 React Router 将合并。Remix 将不再与 React Router 分开开发。

实际上，该团队已将框架功能整合到 React Router 插件中，该插件现在是框架。

自那时以来，Jackson 和 Florence 宣布他们计划创建一个 [新框架](https://remix.run/blog/wake-up-remix)，该框架与基于 React 的 Remix 不同。关于这意味着什么有很多猜测，但这对开发人员写道，这将是“对 [Web 框架](https://thenewstack.io/solidjs-creator-on-confronting-web-framework-complexity/) 的重新构想——一个由数十年的 Web 构建经验塑造的全新基础。”

“这不仅仅是一个新版本，而是一个新的方向。一个更快、更简单、更接近 Web 本身的方向，”Jackson 和 Florence 在 5 月的一篇博文中写道。“为此，我们需要拥有完整的技术栈——而无需依赖我们无法控制的抽象层。这意味着没有关键依赖项，甚至没有 React。”

他们补充说，他们从 Preact 的一个分支开始，Preact 是一个成熟的虚拟 [DOM (文档对象模型)](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) 库，已在 Shopify 和 Google 广泛使用。

在讨论中迷失的是，这一切对今年已有 11 年历史的 React Router 意味着什么。

> “我们正在努力支持所有这些人，所以 [...] 框架模式是完全可选的。”
> **– Brooks Lybrand，Shopify 开发者关系经理**

React Router 和 Remix 框架的融合引起了 [一些 Reddit 的批评](https://thenewstack.io/why-some-developers-are-unhappy-with-react-router/)，但 Lybrand 表示下载量有所增加。

他说：“我们宣布我们正在 [将 React Router 合并到 Remix](https://thenewstack.io/remix-react-router-merge-jetbrains-ide-for-test-automation/)，并且原始 React Router 的使用量大大增加，至少从 NPM 下载量来看是这样。”“这不是框架模式用户。这就像你熟悉和喜爱的常规旧 React Router，而不是框架功能。”

他指出 React Router 的第 5 版，该版本于五年前发布，每周仍收到数百万次的下载。

他说：“我们正在努力支持所有这些人，因此我们所做的是框架模式是完全可选的。”“归根结底，它是一个 [Vite](https://thenewstack.io/development-server-vite-gets-independent-team-and-rust-ifies/) 插件。”

Vite 是一个前端构建工具和开发服务器，已成为元框架的流行基础，包括 [SvelteKit](https://thenewstack.io/rich-harris-talks-sveltekit-and-whats-next-for-svelte/)、[Nuxt.js 3](https://thenewstack.io/dev-news-react-19-nuxt-3-11-a-python-gui-tabnine-llms/)、[Astro](https://thenewstack.io/new-astro-releases-incorporates-sessions-new-astro-actions-tools/) 和 [SolidStart](https://thenewstack.io/how-js-meta-framework-solidstart-became-router-agnostic/)。

Lybrand 说，开发人员可以添加框架插件，也可以选择像自第 5 版以来一直使用 React Router 一样使用它。它基本上是相同的 API。

他说：“随着 React 本身的变化，我们不得不改变一些小事情，因为我们一直在努力支持最新版本的 React，并以 React 希望我们构建的方式进行构建。”

## React Router 的三种模式

Lybrand 将新的 React Router 描述为以 [三种模式之一](https://reactrouter.com/home) 运行：

1. 声明式模式，即自 v5 以来 React Router 的模式；
2. 框架模式，它结合了 Remix 功能；以及
3. 数据模式或数据路由，这是 Shopify 需要但决定共享的 API。他解释说，它允许你将路由器和数据连接在一起，但可以自由地使用任何特定框架。

他说：“这实际上是我们试图给人们的第一个切入点——这是使用你选择的捆绑器或任何东西启用 RSC 所需的所有组件。”“我们将为我们自己的框架模式构建在这些之上，但我们也给你这些乐高积木。”

他补充说，数据模式是从对 RSC 的支持中产生的。

“你的服务器上发生了什么，然后你实际发送到客户端的内容是什么？这种对话必须包括路由器，”Lybrand 解释说。“它决定了向用户显示什么，但也决定了为用户加载什么。这就是为什么我们有数据模式，因为它实际上可以将你的加载和你的操作结合起来。”

他补充说，RSC 也关心数据以及要向用户呈现的内容。

“这对于 React Server Components 来说非常重要，因为你可以使用你的客户端指令来说，‘好吧，这一小部分，它获得了一些 JavaScript，但其余的东西没有获得 JavaScript，’”他说。“有了所有这些细节，React Router 是这些类型的组件的协调者——说，‘这是你的 React Server Components [和] 这是我们应该呈现这些东西的地方，这是所有这些组件。’”

他补充说，在数据模式下，开发人员可以使用 Webpack 或基本上构建他们自己的框架，许多公司都是这样做的。

## 支持 React Server Components

[React Server Components 于 2020 年正式推出](https://dzone.com/articles/react-server-components-rsc-the-future-of-react)，但第一个稳定版本直到去年 React 19 发布时才推出。Lybrand 解释说，如果你想实现 RSC，这意味着使用 Next.js 或进行自定义工作。

这是因为 [Next.js 构建](https://thenewstack.io/how-to-build-a-carbon-aware-website-using-react-and-next-js/) 在最新版本的 React 之上。

“我们从来不喜欢这种策略，”Lybrand 说。“我们一直认为，你可以尽可能多地拥有你的依赖项。”

React Router 主要用于构建单页应用程序 (SPA)，这些应用程序在客户端加载。通过支持 RSC，它将能够提供完整的技术栈 SSR（服务器端渲染）应用程序。（开发者和教育家 [Josh Comeau](https://www.linkedin.com/in/joshwcomeau/?originalSubdomain=ca) 对 [RSC 如何做到这一点以及它与 SSR 的区别](https://www.joshwcomeau.com/react/server-components/) 有很好的解释。）

本周，React Router 团队计划发布 API，以展示其对 RSC 的支持如何工作。

他说：“我们不只是将其提供给框架。我们实际上是在此数据模式下提供它，以便许多 React Router 用户可以使用它。”“你不需要购买我们的 Vite 框架。你不需要购买我们如何进行基于文件的路由以及所有这些废话。你只需在你的数据路由器中使用它，并通过 React Router 启用 React Server Components，这非常令人兴奋。”

他补充说，还将有模板来帮助人们开始使用 React Server Components。（截至发布时，它是 [拉取请求](https://github.com/remix-run/react-router-templates/pull/139)，但他表示很快将被合并。）

## 开放治理

对 RSC 的支持并不是 React Router 的唯一新发展。5 月，Jackson 宣布转向 [开放治理模型](https://github.com/remix-run/react-router/blob/main/GOVERNANCE.md)。

“React Router 不再只是我和 Ryan 的孩子了。它是一个成熟的 OSS 项目，有数百万的依赖者。我们希望每个人都能对项目的未来发展方向发表意见，”[Jackson 在 X 上写道](https://x.com/mjackson/status/1927739177149382991)。“为此，我们正在为 React Router 引入一个开放治理模型。我们希望这将有助于项目继续蓬勃发展，并为任何在 React 上构建的人提供一个稳定的基础。”

五人指导委员会目前全部来自 Remix 团队——包括 Lybrand。他和开发者 Matt Brophy（指导委员会的另一位成员）写道，[该团队希望获得更多反馈](https://remix.run/blog/rr-governance) 以及来自更广泛的 React Router 社区的贡献。

Lybrand 和 Brophy 写道：“这些对 React Router 开发方式的改变只是对我们多年来工作方式的略微调整，并将确保 React Router 在未来几年继续发展。”