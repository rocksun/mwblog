
<!--
title: Hono：后React时代微框架的新思路
cover: https://cdn.thenewstack.io/media/2025/07/35aaa471-josh-hild-3b4c_eydwd4-unsplashb.jpg
summary: Hono是一个轻量级的Web框架，构建于Web标准之上，适用于边缘计算和API服务。它由日本开发者创建，旨在成为全栈框架，但目前仍处于早期阶段。Hono与Next.js等重量级框架不同，更注重灵活性和性能。
-->

Hono是一个轻量级的Web框架，构建于Web标准之上，适用于边缘计算和API服务。它由日本开发者创建，旨在成为全栈框架，但目前仍处于早期阶段。Hono与Next.js等重量级框架不同，更注重灵活性和性能。

> 译自：[Hono Shows the Way for Microframeworks in a Post-React World](https://thenewstack.io/hono-shows-the-way-for-microframeworks-in-a-post-react-world/)
> 
> 作者：Richard MacManus

本周，一个名为 Hono 的 Web 框架在 X 上[宣布](https://x.com/honojs/status/1942207883879530525)它“终于”达到了 25,000 个 GitHub 星星。虽然 25,000 名粉丝不算默默无闻，但 Hono 也没有得到它应得的关注。鉴于它构建在 Web 标准之上，而不是（例如）React，Hono 似乎表明了框架在 [后 React 时代](https://thenewstack.io/why-react-is-no-longer-the-undisputed-champion-of-javascript/)的发展方向。

Hono 由日本开发者 Yusuke Wada 于 2021 年 12 月创建。根据其 GitHub 仓库，Hono 在日语中意为“火焰”，是一个“基于 Web 标准的小巧、简单且超快的 Web 框架”。它最初是为 Cloudflare Workers 构建的，但现在可以在“任何 JavaScript 运行时”上运行，包括 Node.js、Deno、Bun 和 Vercel（尽管 Node 支持需要适配器和 Node ≥ 18）。

Wada 于 2023 年被 Cloudflare 聘用，他的一些工作时间花在了 Hono 上。根据他在 Cloudflare 博客上 [2024 年 10 月的一篇文章](https://blog.cloudflare.com/the-story-of-web-framework-hono-from-the-creator-of-hono/)中的说法，他对该项目抱有很大的雄心：

“与 Next.js 框架从客户端的 React 开始不同，Hono 正试图从服务器端开始成为一个全栈框架。”

## 使用案例

那么 Hono 可以用来做什么呢？在去年 10 月 Cloudflare Developers YouTube 频道上 [的一次采访](https://www.youtube.com/watch?v=yoqtk85HITM) 中，Wada 表示他对使用案例的多样性感到惊讶。

“有些人构建经典的 Web API，另一些人制作全栈应用程序，有些人运行文档站点，我甚至看到它被用来在 Next.js 内部实现 API 层，”他说。“用户不断提出我从未想象过的用例，这是最令人兴奋的部分。”

根据该项目的[文档](https://hono.dev/docs/)，在 Cloudflare 内部，Hono 用于三个不同的 API 服务器。其中两个（KV 和 D1）是内部的，一个（cdnjs）是公共的。

[![Hono 截图](https://cdn.thenewstack.io/media/2025/07/dcbce603-hono-screenshot-july2025.png)](https://cdn.thenewstack.io/media/2025/07/dcbce603-hono-screenshot-july2025.png)

*Hono 主页*

在直接比较方面，Hono 最好被认为是 Express 的现代替代品，Express 是 Node.js 的中间件 Web 框架。使用 Hono 的主要好处是它不仅仅可以在 Node.js 上运行；即使在 Node.js 上，Hono 的基准测试也通常比 Express 快一点。

Hono 与 Express 的区别在于它构建在 Fetch API 之上，Fetch API 是一个 [WHATWG 标准](https://fetch.spec.whatwg.org/)，它“定义了请求、响应以及将它们绑定的过程：获取”。

因此，对于那些希望从 Node.js 和 Express 迁移的开发人员来说，Hono 可能是解决方案的一部分。

“我一直在使用 Hono + Bun + SQLite 来完成我所有的个人项目，我真的很喜欢它，”一位开发人员在 [Hacker News 上](https://news.ycombinator.com/item?id=40049320)说道。“基本上，我已经用它取代了 Express 和 Node。”

## 与 Next.js 比较

当 Wada 说 Hono 正在构建一个全栈框架时，他主要指的是 [HonoX](https://github.com/honojs/honox)，这是一个构建在 Hono 之上的元框架，包括基于文件的路由。

“当您使用 HonoX 时，您会自动使用底层的 Hono，这使您可以创建完整的全栈应用程序，”他解释说。HonoX 也构建在流行的前端构建工具 Vite 之上。

在撰写本文时，HonoX GitHub 项目有 2,300 个星星，并被描述为处于“alpha 阶段”。因此，作为一种全栈解决方案，Hono 仍处于早期阶段。

即使 Wada 将 Hono 与 Next.js 进行比较，这就像将自行车与闪电跑车进行比较一样。

Hono 非常轻量级，专注于服务器/运行时层（路由、中间件、响应）。它特意保持 UI 不可知；您可以返回 JSON、流式传输 HTML 或仅在需要时通过 HonoX 添加您自己的模板或 JSX/SSR。

> 作为一种全栈解决方案，Hono 仍处于早期阶段。

相比之下，Next.js 是一个大型、有主见的端到端 React 栈。它包括基于文件的路由、服务器组件、数据获取、使用 Turbopack 打包、图像优化等等。它既有 UI 组件，也有后端组件。

也许 Hono 最大的优势在于它专注于[边缘网络](https://thenewstack.io/why-devs-must-rethink-their-role-in-modern-cdns-and-the-edge/)。它专为所有运行时设计，非常适合需要在边缘运行的 API 或微服务。

[Cloudflare 的文档](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/hono/) 将 Hono 描述为“一个超快、轻量级的 Web 应用程序构建框架”。Cloudflare 建议 Hono 与 Cloudflare Workers 结合使用是一种有效的全栈解决方案。“借助 Workers Assets，您可以轻松地将运行在 Workers 上的 Hono API 与 [React] SPA 结合起来，从而创建一个全栈应用程序。”

事实上，如果您已经生活在 Cloudflare 的生态系统中，那么 Hono 与 Cloudflare 产品（如 KV、R2、D1、Durable Objects 和 Queues）非常匹配。

## Hono 在后 React 世界中的地位

虽然将自己与 Next.js 进行比较有点雄心勃勃（特别是考虑到 HonoX 仍处于 alpha 模式），但 Hono 似乎确实表明了事物的发展方向。与 Next.js 或 Remix 不同，Hono 不内置 React。您可以返回 JSON、流式传输 HTML 或仅在需要时分层 HonoX 以实现 JSX islands。这种“选择加入 UI”反映了 Web 开发生态系统开始 [远离一体化巨石](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)。

像 Next.js 这样的“超级框架”的时代开始消散。相反，开发人员越来越多地转向更适度的框架，这些框架使用 Web 标准，例如 [Astro 用于更大的项目](https://thenewstack.io/how-astro-and-its-server-islands-compare-to-react-frameworks/)，以及现在的 Hono 用于特定于边缘的使用案例。

Hono 更像是“微框架”阵营，因此它实际上无法与 Next.js（或 Astro）相提并论。但它与那些更大的框架一样值得您关注。