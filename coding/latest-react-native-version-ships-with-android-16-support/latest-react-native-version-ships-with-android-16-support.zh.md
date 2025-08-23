上周 [React Native 0.81 发布了](https://reactnative.dev/blog/2025/08/12/react-native-0.81)，支持 Android 16 (API level 36)，并实验性地支持使用重新编译来加速 iOS 构建。

React Native 团队写道：“正如 [Google](https://thenewstack.io/googles-gemini-cli-agent-comes-to-github/) 先前宣布的那样，Android 16 要求应用程序以 edge-to-edge 方式显示，不支持退出”。为了做到这一点，他们已经弃用了 `SafeAreaView`。

该团队警告说，如果你的应用程序使用了它，你将在 React Native DevTools 中看到警告。

他们补充说：“它将在 React Native 的未来版本中被移除。我们建议你迁移到 `react-native-safe-area-context` 或类似的库，以确保你的应用程序在所有平台上看起来都是最佳的。”

他们还添加了一个新的 Gradle 属性 `edgeToEdgeEnabled`，让开发者可以决定是否在所有 16 以上的受支持 Android 版本上启用 edge-to-edge。

此外，对 JavaScriptCore (JSC) 引擎的支持现在将转移到一个由社区维护的软件包，该软件包与 React Native 本身分开发布。因此，React Native 0.81 移除了内置的 JavaScriptCore 版本。该博客文章补充说，任何需要 JavaScriptCore 的应用程序现在都应该迁移到社区软件包，以便升级到 0.81。

此更新中还有一个开发者需要审查的重大更改列表，其中包括现在需要 Node.js 版本 20.19.4 或更高版本，这是撰写本文时最新的维护 LTS 版本。

React Native 0.81 还发布了各种其他稳定性改进和错误修复。

## 为 React Native 新架构重写的 FlashList v.2

说到 React Native，[FlashList](https://shopify.github.io/flash-list/) 是一个用于 React Native 的高性能列表组件。它的创建是为了解决标准 FlatList 组件中常见的性能问题。两者都用于显示长列表数据。自 2022 年发布以来，FlashList 在 React Native 社区中广受欢迎，每月下载量超过 200 万次。

现在 React Native 有了一个新的架构，[Shopify 已经从头开始重写了 FlashList v.2](https://shopify.engineering/flashlist-v2?ck_subscriber_id=2264736565)，使其更快、更精确、更易于使用，该团队写道。

该文章阐述了通过重写解决的 FlashList 问题，包括一个新的滚动系统、一个精度问题的解决方案和改进的水平列表。该博客文章详细介绍了此次改进所包含的所有更改。

## Turbopack 构建现在在 Next.js 15.5 版本中为 Beta 版

[Next.js 15.5 于周一发布](https://nextjs.org/blog/next-15-5)，它使生产 Turbopack 构建作为 Beta 功能提供。Next.js 团队在最近的一篇文章中写道，这带来了更快的站点构建。

TurboPack 现在为 Vercel 网站提供支持，包括 [Vercel.com](https://vercel.com/)、[v0.app](https://v0.app/) 和 [nextjs.org](https://nextjs.org/)，该团队补充说。

该文章指出：“这些由 Turbopack 提供支持的应用程序已经过实战检验，自推出以来已处理超过 12 亿个请求。”

Turbopack 旨在利用构建的所有阶段中的多个 CPU 核心，从而使开发人员能够随着应用程序的增长扩展构建性能。使用 Turbopack 带来了“编译时间的持续改进”。这里有几个匿名示例，包括一个包含 7 万个模块的大型站点，现在在 30 核机器上速度提高了五倍。

该团队写道：“与 Webpack 相比，我们的生产指标监控显示，使用 Turbopack 构建的站点以更少的请求提供相似或更少数量的 JavaScript 和 CSS，从而带来相当或更好的 FCP、LCP 和 TTFB 指标。”

Next.js 团队要求在 [GitHub for Next.js](https://github.com/vercel/next.js/discussions/77721) 上报告有关 Turbopack 的任何问题。此版本还包括将 Node.js 中间件作为稳定版本引入。

Node.js 运行时不会是 Next.js 16 中的默认设置，但他们正在考虑将其设为 Next.js 17 中的默认设置，具体取决于社区反馈和使用模式。

此版本还包括对 App Router 的主要 Typescript 改进和稳定的类型化路由。还有一个针对 Next.js 16 发布的弃用警告列表，包括：

* next/link 的 legacyBehavior 属性；
* AMP 支持；
* next/image 的质量设置，默认情况下将限制为 75，以及
* 带有本地图像 src 路径的查询字符串将需要在 images.localPatterns 中进行显式配置。

## SvelteKit 现在可以在边缘环境中工作

本月早些时候，Svelte 团队发布了 Svelte 和 SvelteKit 的更新列表。其中一项更改是：SvelteKit 的读取现在可以在 `fs.readFile` 不可用的边缘环境中工作。这包括 Cloudflare 的 Workers 以及 Netlify 和 Vercel 的边缘函数。

此外，远程函数现在可以在应用程序中的任何位置调用，但始终在服务器上运行。这使开发人员可以安全地访问仅服务器模块，其中包含例如环境变量和数据库客户端。

最后，[vite-plugin-svelte](https://github.com/sveltejs/vite-plugin-svelte/blob/main/packages/vite-plugin-svelte/CHANGELOG.md) 现在支持 Vite7 和 rolldown-vite。在[完整文章](https://svelte.dev/blog/whats-new-in-svelte-august-2025) 中还有更多更改，以及社区展示、学习资源、库、工具和组件链接。