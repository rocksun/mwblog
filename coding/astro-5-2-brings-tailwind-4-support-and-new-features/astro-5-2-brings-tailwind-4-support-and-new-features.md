
<!--
title: Astro 5.2带来了Tailwind 4支持和新功能
cover: https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2.png
-->

本周开发者新闻：一个用于 Flutter 的服务器驱动 UI 应用程序框架、Android 16，以及 Vercel 收购了开源库 Tremor。

> 译自 [Astro 5.2 Brings Tailwind 4 Support and New Features](https://thenewstack.io/astro-5-2-brings-tailwind-4-support-and-new-features/)，作者 Loraine Lawson。

Web 框架 [Astro 发布了 5.2 版本](https://astro.build/blog/astro-520/)，支持 Tailwind 4。

该团队撰写了关于新版本的文章，指出 [Tailwind CSS](https://thenewstack.io/tailwind-css-for-developers-style-without-using-css-code/) 现在提供了一个 @tailwindcss/vite 插件，可以直接添加到 Astro 项目中。

“这简化了 Astro 中的 Tailwind 体验，并且现在是在 [Astro](https://thenewstack.io/new-astro-releases-incorporates-sessions-new-astro-actions-tools/) 中使用 Tailwind 4 的推荐方式，”该团队写道。“Astro 5.2 增加了对这个 Vite 插件的原生支持，并且 Astro add tailwind 命令现在会将该插件添加到你的 Astro 配置中，并创建一个导入 Tailwind 样式的默认 CSS 文件。”

Astro 5.2 还包括一种在页面中访问配置值的新方法、更好的尾部斜杠处理以及对外部重定向的支持，该团队在一篇介绍新版本的博客文章中写道。

此外，此版本还引入了以下实验性功能：

- astro:config，它提供了一种从项目中的任何位置读取最有用的配置选项的单一方法；以及
- disable React streaming，它禁用了 React 流式传输，如果开发人员使用的库与流式传输不兼容（例如在许多 CSS-in-JS 库中），则此操作可能很有用。

## Mirai：一个用于 Flutter 的服务器驱动 UI 框架

[Mirai 是一个用于 Flutter 的新的服务器驱动 UI 框架](https://medium.com/buildmirai/introducing-mirai-a-server-driven-ui-framework-for-flutter-d020fd0c387d)，由专注于 Flutter 开发的开发者 Divyanshu Bhargava 最近推出。

Bhargava 写道，服务器驱动 UI (SDUI) 将 UI 与代码库和客户端分离。他解释说，UI 不是硬编码到应用程序中，而是由服务器驱动 UI。

“可以把它想象成浏览器渲染网站，”他写道。“你的浏览器事先不知道它要显示什么内容——它只知道如何解释和渲染标签。类似地，在 SDUI 中，应用程序能够渲染服务器发送的 widget 或组件，从而使 UI 具有动态性、灵活性和完全的服务器控制。”

他继续说，这样做的好处是开发人员可以即时发送更新，而无需延迟和批准。在服务器驱动的 UI 中，服务器定义应用程序的 UI，通常采用轻量级格式，如 [JSON](https://thenewstack.io/how-to-use-json-in-your-python-code/)。他继续说，客户端或应用程序接收这些定义并动态渲染 UI。但他警告说，构建服务器驱动的 UI 很难，这就是开源框架 [Mirai](https://github.com/BuildMirai/mirai) 的用武之地。

“使用 Mirai，你可以使用 JSON 实时定义你的 UI，从而动态地构建出色的跨平台应用程序，”他写道。他写道，Mirai 使个性化 UI 变得更容易，并简化了维护。

它还支持 [A/B 测试](https://thenewstack.io/a-perfect-match-a-b-testing-and-business-success/)，因为开发人员可以通过直接从服务器提供变体有效负载来实时试验多个 UI 版本，他补充说。

## Android 16 Beta 版可用

[Android 上周四发布了 Android 16 的 Beta 版](https://android-developers.googleblog.com/2025/01/first-beta-android16.html?m=1)。根据 Android Developer 博客，它具有对未来应用程序适应性、实时更新和高级专业视频格式的支持，该格式旨在用于专业级高质量视频录制和后期制作。

一个有趣的变化是，Android 16 正在逐步取消应用程序限制大屏幕上的屏幕方向和可调整大小的能力。

“这类似于 OEM 在过去几年中添加到大屏幕设备中的功能，允许用户以任何窗口大小和宽高比运行应用程序，”该博客文章指出。“在宽度大于 600dp 的屏幕上，以 [API level 36](https://apilevels.com/) 为目标的应用程序将具有可调整大小的应用程序窗口；你应该检查你的应用程序，以确保你现有的 UI 可以无缝缩放，并在纵向和横向宽高比下都能很好地工作。”

他们补充说，限制方向和调整大小的 Manifest 属性和 API 将被忽略，但游戏除外。

Android 提供了 [框架、工具和库](https://developer.android.com/develop/ui/compose/layouts/adaptive) 来帮助解决这个问题。

## Vercel 收购 Tremor
Vercel 上周宣布[已收购 Tremor](https://vercel.com/blog/vercel-acquires-tremor)，这是一个构建于 [React](https://thenewstack.io/new-york-public-library-on-choosing-react-to-rebuild-website/)、Tailwind CSS 和 [Radix](https://www.radix-ui.com/) 之上的开源库。根据 Vercel 首席产品官 Tom Occhino 的说法，这是该公司投资开源 React 组件的一种方式。

Occhino 写道，Tremor 包括 35 个独特的组件和 300 个可以复制粘贴以构建视觉丰富且交互式仪表板的块。

Tremor 的员工及其联合创始人 Severin Landolt 和 Christopher Kindl 将加入 Vercel 的设计工程团队，他们将在该团队中为 Vercel Dashboard、v0 和其他项目开发 UI 组件。
