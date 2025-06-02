<!--
title: 让前端开发者一次构建，部署Web和原生应用
cover: https://cdn.thenewstack.io/media/2025/04/9157e63c-one_framework_react.jpg
summary: 前端福音！One框架横空出世，基于Vite插件，一次构建同时搞定Web和原生应用！支持SPA、SSG、SSR，集成React Native和React，更有文件系统路由、CLI和Hono加持。年底Ready，云原生时代效率🚀！
-->

前端福音！One框架横空出世，基于Vite插件，一次构建同时搞定Web和原生应用！支持SPA、SSG、SSR，集成React Native和React，更有文件系统路由、CLI和Hono加持。年底Ready，云原生时代效率🚀！

> 译自：[One Lets Frontend Devs Build Once, Deploy Web and Native Apps](https://thenewstack.io/one-lets-frontend-devs-build-once-deploy-web-and-native-apps/)
> 
> 作者：Loraine Lawson

一个新的 React 框架使开发者能够创建 Web 和原生平台应用程序。它被诗意地称为 One，它与其他选项的不同之处在于，它将生成 [单页应用程序 (SPA](https://thenewstack.io/secure-single-page-apps-with-cookies-and-token-handlers/))、[静态站点生成](https://thenewstack.io/nue-a-new-static-site-generator-taking-on-next-js/) (SSG) 和服务器端渲染 (SSR) 网页。

它运行在 [Vite](https://thenewstack.io/vites-new-rust-based-javascript-bundler-available-in-beta/) 上，是 [Nate Wienert](https://www.linkedin.com/in/nathan-wienert-89091945/) 的创意，他是一位软件开发者，曾在 Vercel 工作，现在是软件开发公司 Uniswap Labs 的一名 Staff Engineer。[Wienert](https://www.linkedin.com/in/nathan-wienert-89091945/) 还创建了基于 React 的 UI 库 [Tamagui](https://tamagui.dev/) 和 [Takeout](https://tamagui.dev/takeout)，它是 Tamagui 的一个入门工具包。

## 一个打包为 Vite 插件的框架

One 通过 [单个 Vite 插件](https://github.com/onejs/one) 面向 Web 和原生平台。[开发者](https://roadmap.sh/roadmaps?g=Web+Development) 可以使用 One 进行创建，然后输出用于移动设备的 [React Native](https://thenewstack.io/cross-platform-ui-framework-lynx-competes-with-react-native/) 和用于 Web 的 [React](https://thenewstack.io/new-york-public-library-on-choosing-react-to-rebuild-website/) 代码。它还添加了文件系统路由、渲染模式、加载器、中间件、命令行界面 (CLI) 和 [Hono](https://hono.dev/)。

“[如果你]确实想构建一个原生应用程序，并且想构建一个 Web 应用程序，那么它就能真正发挥作用，”[Wienert](https://www.linkedin.com/in/nathan-wienert-89091945/) 告诉 The New Stack，“你可以共享代码，这样你就可以编写更少的代码，并且可以面向这两个平台，并且仍然可以获得相当不错的——老实说，非常棒的——用户体验和性能。”

也就是说，开发者也可以将其用作创建两者的开发工具。

“我确实认为，我们如此专注于提供真正好的体验，使得它对两者都有好处，但真正闪光的使用场景绝对是在两者之间共享代码，”他说。

## 为简单性而开发

[Wienert](https://www.linkedin.com/in/nathan-wienert-89091945/) 是一位重视简单性的程序员。他记得小时候 [Ruby on Rails](https://thenewstack.io/dhh-wants-to-make-web-dev-easy-again-with-ruby-on-rails/) 如何让他创建东西变得容易 10 倍。

“小时候，我几乎什么都做不了，但突然之间就能实现我所有的想法，”他说。“Rails 做的最重要的事情是：所有那些与你试图构建的东西没有真正直接关系的烦人事情，[它]让它们变得非常容易。”

但在开发中情况并非总是如此。他说，有时开发者似乎想以“奇怪”的方式让开发变得有趣。

“我不在乎学习你为身份验证提出的疯狂的、深奥的、天才的解决方案，”他说。“我只想尽可能简单地让我的身份验证工作，因为 99% 的身份验证系统都是相同的。”

在疫情期间，[Wienert](https://www.linkedin.com/in/nathan-wienert-89091945/) 创建了 Tamagui，因为他正在开发一个大型应用程序，他希望该应用程序能够跨平台工作，同时支持 Web 和原生平台。

> “灵感更多的是来自于类似 Rails 的体验，它非常简单；它非常清晰，你不会重复做事情。”
>
> — [Nate Wiener](https://www.linkedin.com/in/nathan-wienert-89091945/)，One 和 Tamagui 的创建者

“在构建它时，我注意到没有什么好的方法可以在原生和 Web 之间共享 UI——一切都有很大的问题，”他说。“我构建 Tamagui 来解决这些问题，我认为这非常成功。”

当时，他认为最好的解决方案是采用 [Next.js 应用程序](https://thenewstack.io/build-a-real-time-bidding-system-with-next-js-and-stream/) 和 [Expo](https://thenewstack.io/expo-vs-flutter-how-to-choose-the-right-mobile-framework/) 应用程序，然后使用 [Solito](https://github.com/nandorojo/solito) 将它们粘合在一起，[Solito](https://github.com/nandorojo/solito) 是他的朋友 [Fernando Rojo](https://github.com/nandorojo/solito) 创建的一个库，他现在是 Vercel 的移动部门负责人。它奏效了，但令人沮丧。

“我们拥有所有这些令人惊叹的新事物，它们更强大，我们可以构建更好的体验，但[作为开发者的实际体验](https://thenewstack.io/developer-experience-devs-shouldnt-have-to-figure-it-out/)太糟糕了，”他说。“代码量要多得多，优雅性要差得多，而且当时没有更好的选择。”

这成为他创建框架的动力，该框架可以以更简单的方式统一所有这些，同时编写一次代码，他说：“灵感更多的是来自于类似 Rails 的体验，它非常简单；它非常清晰，你不会重复做事情。”

## 为什么选择 Vite 而不是 Metro

One 最初是一个实验，通过 fork [Expo Router](https://docs.expo.dev/router/introduction/) 开始的，它是一个基于文件的 React Native 和 Web 应用程序路由库，构建于 [React Navigation](https://reactnavigation.org/) 之上用于导航。但它使用 [Metro 作为打包器](https://metrobundler.dev/)，他发现这“有点乱”，使用起来很痛苦。而且这种组合在 Web 方面表现不佳。

他更喜欢 Vite，它在 Web 方面表现良好，但不输出与 React Native 兼容的 JavaScript 包。他补充说，让它在 Native 方面表现良好比让 Metro 在 Web 方面表现良好更容易。

“我们也花了很多时间，让很多不同的包与更现代、更像有效的语法一起工作，”他说。“Vite 在很多方面都是最好的。它非常干净，设计非常精美。”

虽然 One 是一个框架，但它被打包为一个 Vite 插件，他补充说。他还说，它还可以检测 [CommonJS](https://www.freecodecamp.com/news/modules-in-javascript/) 包并自动支持它们。

One 的另一个区别在于它与 [Zero](https://zero.rocicorp.dev/) 一起开发，Zero 是 [一种新型的同步引擎](https://thenewstack.io/how-a-new-breed-of-sync-engines-solves-frontend-problems/)，目前处于公开 alpha 阶段。Wienert 是 Zero 的创建者 Aaron Boodman 的朋友。

## 年底准备就绪

Wienert 说，One 和 Zero 都“有点早”，但他相信它们代表了 [前端开发](https://thenewstack.io/introduction-to-frontend-development) 的未来。

“我非常相信这就是未来——不仅仅是 Zero——而是通用的同步引擎，”他说。“我认为这种风格的软件将是未来 10 年大多数人编写大多数应用程序和网站的方式。”

欢迎开发人员现在尝试 One，但他警告说，它还没有完全准备好投入使用。Test Flight 上有一个 [演示应用程序](https://testflight.apple.com/join/aNcDUHZY)，但目前不接受新的测试人员。该团队还在构建一个复杂的跨平台聊天应用程序，类似于 Discord，以便开发人员可以看到它的功能。该团队计划添加工具和一种托管方式。

他补充说，One 应该在今年年底准备好进行实际部署。

“我们的目标是使其稳定、可靠且运行良好，然后 Zero 集成对我们来说非常重要，”他说。“如果我们专注于任何事情，那就是使其尽可能简单、美观和干净。”

了解 One 如何与其他跨平台框架相抗衡：

## 跨平台开发框架比较

| 名称 | 定义 | 创建者 | 构建技术 | 适用场景 | 开源？ | 其他说明 |
|------|------|--------|----------|----------|--------|----------|
| .NET MAUI (前身为Xamarin) | 跨平台框架 | 微软 | C#和.NET | 它演变并统一了Xamarin.Forms，允许开发者使用单一代码库创建可在iOS、Android、macOS和Windows上运行的应用程序。 | 是，MIT许可证 | 该框架提供一套UI控件和API，用于访问原生平台功能。 |
| Flutter | 开源UI开发套件 | 谷歌 | Dart | 从单一代码库为移动端、网页和桌面应用生成原生编译的应用程序。 | 是，BSD 3-Clause许可证 | 以其快速开发的特性如热重载、富有表现力且灵活的UI与丰富的组件库而闻名，能够提供在不同平台上看起来和感觉都像原生应用的高性能应用。 |
| Iconic | UI工具包 | Max Lynch、Ben Sperry和Adam Bradley（Drifty Co.成员），2013年创建 | JavaScript —— 包括Angular、Vue和React —— 及其变体（如TypeScript），以及HTML和CSS | 使用网页技术如HTML、CSS和JavaScript（通常搭配Angular、React或Vue.js）开发混合移动应用、渐进式网页应用（PWAs）和桌面应用。 | 是，MIT许可证 | 提供Iconic CLI；在WebView中渲染UI。 |
| Kotlin | 通用跨平台编程语言 | JetBrains | Java | Android开发和基于Java虚拟机（JVM）的后端开发。编译成JavaScript（Kotlin/JS）用于前端网页开发，编译成原生代码（Kotlin/Native）用于iOS、macOS、Windows、Linux和WebAssembly。 | 是，Apache 2.0许可证 | 可在不同平台间共享代码。 |
| Lynx | 跨平台UI框架 | 字节跳动（拥有TikTok） | 核心引擎用Rust编写，但开发者主要使用JavaScript和TypeScript构建应用 | 用于创建适用于跨平台应用和网页的单一代码库。 | 是，Apache 2许可证 | 允许开发者使用CSS，尽管它是原生的。一些UI组件和高级内置图形功能尚未在Apache 2许可证下发布。 |
| NativeScript | 用JavaScript、TypeScript或Angular构建移动原生iOS和Android应用的框架 | Telerik（现为Progress Software所有）。现归OpenJS基金会所有。 | JavaScript、TypeScript和Angular | 使用JavaScript、TypeScript或Angular构建原生iOS和Android应用。 | 是，Apache许可证2.0 | 直接使用原生UI组件。开发者可以访问原生设备API的全部功能。NativeScript不尝试模拟原生UI或在浏览器容器中运行。相反，它充当JavaScript/TypeScript/Angular到原生的桥梁，允许你用这些熟悉的语言编写直接操作和利用底层原生平台功能和UI组件的代码。 |
| One | 跨平台框架 | Nate Weinert | React JavaScript | 使用React创建网页和使用React Native创建原生平台应用。 | 是，MIT许可证 | 将任何页面渲染为SPA、SSR或SSG，控制全局默认设置。提供CLI。 |
| QT | 用于桌面开发的跨平台框架，支持移动端（Qt for Mobile）和网页（Qt for WebAssembly） | Trolltech的Haavard Nord和Eirik Chambe-Eng（经过一系列收购后最终成为Qt公司） | C++ | 高性能桌面应用、移动端和网页。 | 是，LGPL和GPL许可证，也提供商业许可证 | Qt提供一套用于网络、数据库访问、多媒体、XML处理等功能的库，因此可以用于从单一代码库构建跨平台的复杂应用程序。 |
| React Native | 创建原生移动应用的框架 | Meta | React JavaScript | 从单一代码库开发iOS和Android应用。 | 是，MIT许可证 | |
| Swift | 使用UIKit或SwiftUI作为框架的跨平台语言 | 苹果 | Swift | 构建iOS应用，以及使用Swift for Android构建Android应用。可以编译成WebAssembly，用于构建Linux服务器端应用、命令行工具等。对Windows平台上的Swift开发支持也在增长，允许开发者为该平台构建应用。 | 是 | 构建为网页应用提供动力和生成初始HTML的服务器端组件。Vapor、Kitura和Perfect等框架使用Swift实现这种服务器端网页开发。 |