
<!--
title: 再见Create React App，你好TanStack Create React App
cover: https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2.png
-->

> 译自：[Goodbye Create React App, Hello TanStack Create React App](https://thenewstack.io/goodbye-create-react-app-hello-tanstack-create-react-app/)
> 
> 作者：Loraine Lawson

其他开发者新闻：Anaconda 提供了一个新的自然语言 AI 数据工具；Vercel增加了对 React Router v7 应用的支持。

[Create React App 已被弃用](https://react.dev/blog/2025/02/14/sunsetting-create-react-app) ，在近十年的使用中构建 React 应用之后，于 2月14日被弃用。它将继续以维护模式运行。Meta 的团队写道：“今天，我们不再建议将 Create React App 用于新应用，并鼓励现有应用迁移到一个框架，或迁移到一个构建工具，例如 [Vite](https://thenewstack.io/vites-new-rust-based-javascript-bundler-available-in-beta/)、[Parcel](https://parceljs.org/) 或 [Rsbuild](https://rsbuild.dev/)。”

Create React App (CRA) 库于 2016 年发布，当时没有明确的方法来构建新的 [React](https://thenewstack.io/new-york-public-library-on-choosing-react-to-rebuild-website/) 应用，他们写道。它将多个工具组合成一个推荐的配置来 [简化应用开发](https://thenewstack.io/datastax-aims-to-simplify-building-ai-apps-with-ragstack/)，允许开发人员快速启动一个 React 项目。它包括网站的基本文件结构和一个开发服务器，用于在本地运行网站以方便开发。

他们写道：“这允许应用以简单的方式升级到新的工具功能，并允许 React 团队将非平凡的工具更改（快速刷新支持、React Hooks lint 规则）部署到尽可能广泛的受众。”“这种模式变得如此流行，以至于今天有一整类工具都在以这种方式工作。”

那么……为什么终止一个流行的工具？

博客文章概述了 CRA 的问题，包括难以构建高性能的生产应用。它还指出，Create React App 没有提供路由、数据获取或代码分割的特定选项。

他们写道：“原则上，我们可以通过将其发展成一个框架来解决这些问题。”

但这带来了 CRA 可能面临的最大挑战：它有 `null` 活跃维护者。

因此，团队建议开发人员使用框架创建新的 React 应用。

他们补充道：“我们推荐的所有框架都支持客户端渲染 (CSR) 和单页应用 (SPA)，并且可以部署到 CDN 或静态托管服务而无需服务器。”

他们提供了迁移指南的链接，用于 [Next.js](https://nextjs.org/docs/app/building-your-application/upgrading/from-create-react-app)、[React Router](https://reactrouter.com/upgrading/component-routes) 和 [Expo web pack 到 Expo Router](https://docs.expo.dev/router/migrate/from-expo-webpack/)。

他们补充道：“如果您的应用有特殊约束，或者您更喜欢通过构建自己的框架来解决这些问题，或者您只想从头开始学习 React 的工作原理，您可以使用 [Vite](https://www.robinwieruch.de/vite-create-react-app/)、[Parcel](https://parceljs.org/migration/cra/) 或 [Rsbuild](https://rsbuild.dev/guide/migration/cra) 使用 React 滚动您自己的自定义设置。”

最近发布的 [2024 React 现状](https://2024.stateofreact.com/en-US/) 将 CRA 排名第三，仅次于 [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) 和 [useState](https://react.dev/reference/react/useState)。[对 CRA 作出回应的 6240 名开发人员中有 89%](https://2024.stateofreact.com/en-US/libraries/) 使用过该工具，但从该组中，近 30% 的人对它表达了负面情绪。只有 15% 的人表达了积极情绪。44% 的前端开发人员没有表达任何情绪。

## TanStack Router 的新 Create React App

相关新闻是，TanStack 最近添加了一个开源的 [TanStack Router 的 Create React App](https://github.com/TanStack/create-tsrouter-app)。它旨在作为 [Create React App](https://create-react-app.dev/) 的直接替代品。这将允许开发人员基于他们的 Router 构建 SPA 应用程序。

为了帮助加快从 create-react-app 的迁移，团队创建了 create-tsrouter-app CLI，它是 CRA 的即插即用替代品。

项目说明指出：“您将获得一个使用 TanStack Router 的 Vite 应用程序。”“create-tsrouter-app 拥有您对 CR 的所有喜爱之处，但它是使用现代工具和最佳实践实现的，建立在流行的 TanStack 库之上。”

这包括 [Tanstack Query](https://tanstack.com/query/latest)，一个用于 TS/JS、React、Solid、Vue、Svelte 和 Angular 的异步状态管理，以及用于 React 和 Solid 应用程序的 [Tanstack Router](https://tanstack.com/router/latest)。

它在 MIT 许可下可用。

## Anaconda 提供新的开源 AI 工具
Anaconda周三推出了一款新的开源AI数据工具[Anaconda发布Lumen AI](https://www.anaconda.com/blog/anaconda-launches-lumen-ai)，允许数据科学和开发团队使用自然语言探索、转换和可视化数据。它被称为[Lumen AI](https://github.com/holoviz/lumen)，是一个基于代理的框架，用于“与数据聊天”和[检索增强生成 (RAG)](https://thenewstack.io/solving-the-rag-vs-long-context-model-dilemma/)。根据发布该消息的帖子，其目标是使高级数据工作流程更直观且更具可扩展性。

高级市场传播经理Kodie Dower写道：“基于AI的代理系统正在迅速改变企业的运营方式，但许多组织仍在努力克服技术障碍、碎片化的工具以及缓慢的手动流程。”“Lumen通过为用户提供一个AI驱动的环境来消除这些障碍，从而快速生成SQL查询、分析数据集和构建交互式仪表板——所有这些都无需编写代码。”

Dower补充说，Lumen可以：

- 无需编码即可创建图表、表格和仪表板等可视化效果；
- 生成SQL查询并在本地文件、数据库和云数据湖中转换数据；
- 支持具有序列化和共享工作流的协作；
- 检查、验证和编辑AI生成的输出，以确保[数据准确性和清晰度](https://thenewstack.io/from-chaos-to-clarity-master-the-first-mile-of-observability/)；
- 支持自定义工具和AI代理。

代码库解释说：“Lumen的[数据模型的声明性使得大型语言模型 (LLM)](https://thenewstack.io/use-your-data-in-llms-with-the-vector-database-you-already-have/)能够轻松生成整个数据转换管道、可视化效果和许多其他类型的输出。”“生成后，[数据管道和可视化](https://thenewstack.io/apache-hop-harnesses-metadata-to-create-visual-data-pipelines/)输出可以轻松序列化，从而可以共享它们，以便在笔记本中继续分析和/或构建整个仪表板。”


## Vercel添加对React Router v7应用程序的支持

React Router版本7与其之前的迭代略有不同，因为它也是一个[与Remix合并后的框架](https://thenewstack.io/why-some-developers-are-unhappy-with-react-router/)。本周，Vercel宣布它将支持[用作框架的React Router v7应用程序](https://vercel.com/changelog/support-for-eact-router-v7)。这包括使用[Vercel的Fluid计算](https://thenewstack.io/vercel-rolls-out-more-cost-effective-infrastructure-model/)支持服务器端渲染的React Router应用程序。
