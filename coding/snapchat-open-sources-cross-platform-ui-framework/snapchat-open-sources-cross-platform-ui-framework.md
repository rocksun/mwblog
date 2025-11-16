
<!--
title: Snapchat 开源跨平台UI框架，助力开发者
cover: https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2.png
summary: Snapchat 开源了跨平台 UI 框架 Valdi；Nuxt 发布了 MCP 服务器；Next.js 部署更灵活；React Native 在 Bitrise 采用率上升；Web 开发者发布了 Wiggle UI 小部件库；一款名为 Poopetti 的库可为 Web 应用添加动画便便表情。
-->

Snapchat 开源了跨平台 UI 框架 Valdi；Nuxt 发布了 MCP 服务器；Next.js 部署更灵活；React Native 在 Bitrise 采用率上升；Web 开发者发布了 Wiggle UI 小部件库；一款名为 Poopetti 的库可为 Web 应用添加动画便便表情。

> 译自：[Snapchat Open Sources Cross-Platform UI Framework](https://thenewstack.io/snapchat-open-sources-cross-platform-ui-framework/)
> 
> 作者：Loraine Lawson

八年来，Snapchat 一直在内部使用 [Valdi](https://github.com/Snapchat/Valdi) 这个跨平台 UI 框架。现在，它已将该框架开源。

Valdi 的设计初衷是为了解决跨平台开发的一个根本性问题：**速度与运行时性能的权衡**，该项目的 Readme 文件中提到。

尽管该框架在内部已经使用了近十年，但这次发布被定为 beta 版，因为“工具和文档还需要在开源世界中经过更多的实战检验”，根据该项目的仓库说明。其目标是在将其移出 beta 版之前，**改善开发者体验**。

“Valdi 是一个跨平台 UI 框架，可以在不牺牲开发者速度的情况下提供原生性能，”该项目仓库表示。“用声明式的 TypeScript 编写你的 UI，它会直接编译成 iOS、Android 和 macOS 的原生视图——无需 Web 视图，也无需 JavaScript 桥接。”

它加入了众多 [跨平台框架](https://thenewstack.io/10-cross-platform-options-for-building-native-mobile-and-web/) 的行列，但根据该项目仓库的说法，它与众不同之处在于其真正的原生性能。

“与依赖 Web 视图或 JavaScript 桥接的框架不同，Valdi 将声明式渲染的 TypeScript 组件编译成平台原生视图，”该项目仓库补充道。

它还提供了许多性能优势，例如：

*   自动视图回收，这可以减少视图加载延迟；
*   优化的组件渲染，允许组件独立重新渲染，而不会触发父组件的重新渲染；
*   一个运行在主线程上的 C++ 布局引擎，具有最小的序列化开销；
*   视口感知渲染，只加载可见视图，从而使无限滚动默认就具有高性能。

它包含自动代码生成功能，可以将 [TypeScript](https://thenewstack.io/typescript-5-9-brings-less-friction-more-features/) 接口转换为 Kotlin、Objective-C 和 Swift 绑定。

## Nuxt 发布 MCP 服务器

渐进式 Web 框架 Nuxt 发布了一个 [模型上下文协议 (MCP) 服务器](https://nuxt.com/blog/building-nuxt-mcp)，该服务器以 AI 助手能够理解的方式暴露其文档、博客文章和部署指南。

包括 [Angular](https://angular.love/angular-cli-mcp-server-keep-your-ai-up-to-date) 和 [React](https://github.com/kalivaraprasad-gonapa/react-mcp) 在内的许多框架，在最近几个月都发布了 MCP 服务器。

这次发布与众不同之处在于，团队成员 [Hugo Richard](https://x.com/HugoRCD__) 和 [Sébastien Chopin](https://www.linkedin.com/in/atinux/?originalSubdomain=fr) 不仅仅是发布了 Nuxt 的 MCP 服务器——他们做得更酷。他们解释了如何构建它，以便其他开发者可以效仿，[部署自己的 MCP 服务器](https://thenewstack.io/tutorial-build-a-simple-mcp-server-with-claude-desktop/)。

该公告还解释了如何在 Cursor 和其他 AI 工具中部署它。

## Next.js 在 Vercel 之外更易于部署

据 Appwrite（一个 Vercel 的开源替代品）的工程负责人 [Matej Bačo](https://github.com/meldiron) 称，[Next.js 在非 Vercel 环境中部署更加容易](https://appwrite.io/blog/post/everything-new-in-nextjs16)。

根据 Bačo 的说法，使之成为可能的一个重大变化是 [Adapters API](https://nextjs.org/blog/next-16#build-adapters-api-alpha)。

“如果你曾经不得不在不寻常的环境中部署 Next.js 应用，比如在 [Vercel](https://thenewstack.io/next-js-in-chatgpt-vercel-brings-the-dynamic-web-to-ai-chat/) 之外，那么这个功能就是为你准备的，”他写道。“Build Adapters（目前处于 alpha 阶段）允许你钩入构建过程并对其进行修改，而无需分叉框架。这对于自托管或构建自定义管道的团队尤其有用。”

他补充说，这表明“Next.js 开始认真对待在不同环境中运行框架的开发者的灵活性。”

他还指出了 Next.js 16 中其他有用的变化，包括 [DevTools MCP](https://github.com/vercel/next-devtools-mcp)。它将允许 AI 工具理解项目的上下文、路由、缓存和渲染行为。

> “这些中间件不是你典型的中间件。你在这些中间件中进行的任何网络调用都会让你处于被动，因为一次缓慢的网络调用可能会阻塞整个网页的初始加载，这并不理想。”
> 
> **— Matej Bačo，Appwrite 的工程负责人**

他还指出了一个看似微小的变化，但对他来说，这对 [Next.js 开发者](https://roadmap.sh/nextjs)很重要——旧的 `middleware.ts` 文件现在被命名为 `proxy.ts`。

“就是这样。行为相同，名字更好，”他写道。

但他表示，中间件的命名引起了关于其在 Next.js 中工作方式的许多困惑。

“这些中间件不是你典型的中间件，”Bačo 写道。“你在这些中间件中进行的任何网络调用都会让你处于被动，因为一次缓慢的网络调用可能会阻塞整个网页的初始加载，这并不理想。”

他补充说，Next.js 中的中间件用于执行轻量级任务，例如根据存储的身份验证 Cookie 重定向用户。这使得该术语令人困惑，因此 Next.js 团队将其重命名为“proxy”，以便更清楚地表明其用途。

他指出了其他更新，例如改进的日志以及 TurboPack 从 beta 版毕业并成为所有新 Next.js 项目的默认打包器。

“构建和开发日志现在显示时间花费在哪里，细分了编译、渲染和优化步骤，”Bačo 写道。“如果你的构建突然感觉变慢了，你可以立即知道是哪些部分出了问题。”

他还提到了更精炼的缓存 API，他认为这些 API 已经得到了清理和明确化。

“Next.js 16 不是一个改变你构建方式的发布，”Bačo 写道。“它是一个改变你的构建体验的发布。缓存现在是可预测的。构建更快。路由更精简。日志更清晰。”

## React Native 在 Bitrise 部署中的采用率上升

Bitrise 发布了其首份 [Mobile Insights 报告](http://www.bitrise.io/insights)，分析了其基于云的移动 [DevOps](https://thenewstack.io/go-beyond-devops-with-autonomous-full-stack-optimization/) 和 [CI/CD 平台](https://thenewstack.io/beyond-ci-cd-why-your-infrastructure-is-your-new-bottleneck/) 上超过 1000 万次构建。

在该数据集中，它发现跨平台框架正在兴起，其中 React Native 成为领导者。报告显示，React Native 的部署量从 2022 年占所有平台构建的 63% 上升到 2025 年的 83%。

它还揭示了一个有趣的悖论：虽然移动 CI 流水线复杂性增加了 23%，但领先的团队却将构建时间缩短了 28%。

“移动开发变得越来越复杂和要求高，”Bitrise 工程和基础设施副总裁 [Arpad Kun](https://www.linkedin.com/in/arpadkun/) 在一份准备好的声明中说。“这些见解为工程团队提供了他们所需的基准，以了解他们的现状以及他们应该在哪里努力以提升水平。”

## Wiggle UI：Web 的开源小部件

Web 开发者 [Henil Shah](https://henilshah.vercel.app/) 发布了他声称是首个开源的 Web 小部件集合。

[![Wiggle UI 主页](https://cdn.thenewstack.io/media/2025/11/9f189f23-wiggleui.png)](https://cdn.thenewstack.io/media/2025/11/9f189f23-wiggleui.png)

*一个开源的小部件库。截图来自 [Wiggle UI 网站](https://wigggle-ui.vercel.app/)。*

名为 [Wiggle UI](https://wigggle-ui.vercel.app/)，它包含了日历、时钟、仪表板、体育、股票和天气等小部件，所有这些都可根据 MIT 许可证使用。开发者也可以在 [Github](https://github.com/wigggle-ui/ui) 上找到它。

## 这个库让“便便”下雨……？

有趣的消息是，自称独立开发者的 Alex Enes Zorlu 创建了一个开源的“轻量级、充满乐趣的库”，旨在为 Web 应用程序带来动画便便表情符号。

恰如其分地命名为 [Poopetti](https://poopetti.com/)，它将实现两个功能：让便便表情符号像下雨一样落下，或者创建一个大的便便表情符号，当被选中时会弹出，然后——你猜对了——落下便便表情符号。

我们八岁的内心对此很喜欢。

“你是否被用户的不称职所困扰？Poopetti 来救援！💩，”该页面吹嘘道。“为什么要使用无聊的错误消息，而你可以字面意思上用 💩 来“洗礼”你的用户？”

到目前为止，它在 [GitHub](https://github.com/enszrlu/poopetti) 上有 35 个星和 1 个 fork。