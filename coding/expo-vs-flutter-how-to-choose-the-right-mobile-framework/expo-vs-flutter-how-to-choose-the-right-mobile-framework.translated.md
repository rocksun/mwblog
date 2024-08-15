# Expo 与 Flutter：如何选择合适的移动框架

![Featued image for: Expo vs. Flutter: How to Choose the Right Mobile Framework](https://cdn.thenewstack.io/media/2024/08/4f1340e6-computer-chip-6054331_1280-1024x576.jpg)

您希望为公司下一个移动项目做出正确的选择，但在这场辩论中很难找到实用的信息。几乎每篇文章都指向一个 [Flutter](https://thenewstack.io/flutter-fever-adoption-grows-and-spreads-to-embedded-devices/) 或 [React Native](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/) 开发工作室，试图说服您他们的技术是最好的。我向您保证，这篇文章不同。

在本文中，我将提出并回答十个可操作的问题，这些问题将帮助您确定适合您特定用例的技术，以便您自信地说：“*我选择 Expo/Flutter 是因为 X、Y 和 Z。*”

首先，让我们快速了解一下 Expo 和 Flutter 的基础知识，然后我们可以深入探讨这十个问题，帮助您在它们之间做出选择。

## 什么是 Flutter？什么是 Expo？

首先，[Expo 现在是推荐的框架](https://reactnative.dev/docs/environment-setup) 用于 [React Native](https://reactnative.dev/)。因此，我们将比较 Expo 和 Flutter，因为 Expo 是构建 React Native 应用程序最流行的方式。

简单的事实是，Expo 和 Flutter 都是很棒的技术！

Google 在 2017 年推出了 [Flutter](https://flutter.dev/)。它使用 [Dart](https://dart.dev/) 编程语言。Flutter 是一个完整的框架，允许您从单个代码库构建移动、Web 和桌面应用程序。它以其高性能和平台一致的设计而闻名。

[Expo](https://expo.dev/) 是一套围绕 React Native 构建的工具和服务，React Native 由 [Meta](https://www.meta.com/de/en/) 创建。Expo 允许您通过编写 JavaScript/TypeScript 和 JSX 来更快地构建移动应用程序。它以其完整的服务生态系统而闻名，这些服务可以帮助公司更快地发布和迭代。

Flutter 和 React Native 是开源技术，拥有庞大的社区和工具和库生态系统。

Flutter 遵循“一次编写，随处运行”的方法，而 Expo 遵循“一次学习，随处编写”的方法。

这些理念之间有什么区别？

- 对于 Flutter，这个概念意味着您的 UI 代码是平台无关的，并且在所有平台上看起来都一样。理论上，应用程序可以在所有平台上运行，例如嵌入式设备。
- 对于 Expo，这意味着每个了解 React 的开发人员都可以使用 React Native 创建平台原生应用程序，而无需学习新的编程语言。

所以您会看到，两者从外部看起来都很棒，但魔鬼在于细节。

这就是为什么我们需要提出正确的问题来为您的项目选择合适的技术。

## 选择 Expo 和 Flutter 的 10 个问题

### 1. 您是否拥有 React/Dart 知识？

如果您是拥有 React 知识的 Web 开发人员，您会对 Expo 感到宾至如归。Expo 使用 React Native，React Native 使用 React，因此您可以利用您现有的知识来构建移动应用程序。

如果您想快速入门并避免学习像 Dart 这样的新语言，或者您已经拥有想要在移动应用程序中使用的 React 包，这是一个重大优势。

另一方面，如果您是 Dart 开发人员或对 Flutter 比 React 更熟悉，您会对 Flutter 感到更舒适。

除了回答这个问题本身之外，还需要更多信息才能做出决定，但这可以帮助您在启动新项目或处理具有挑战性的要求时节省时间和资源。

### 2. 您是否希望直接访问原生平台 API？

Flutter 和 Expo 允许您构建移动应用程序，而无需接触原生代码。但是，它们对访问和使用原生平台 API 采取了不同的方法。

以相机为例。

在 Flutter 中，带有其控件的叠加层由 Flutter 框架本身渲染，而不是底层操作系统。

在 Expo 中，相机被抽象化，您可以使用 `expo-camera` 包来渲染原生 iOS 和 Android 相机视图。

虽然看起来是一个很小的区别，但它会影响某些项目的关键要求。您应该问问自己，您是想访问 Google 和 Apple 团队提供的用户体验，还是需要用户界面在所有平台上保持一致。

除了使用现有库之外，您还可以编写原生 [Expo 模块](https://docs.expo.dev/modules/native-module-tutorial/) 或 [Flutter 插件](https://docs.flutter.dev/platform-integration/platform-channels) 来直接访问原生 API。

但是，管理 Flutter 通道可能比编写 Expo 模块更复杂，因为您需要设置许多文件和处理程序（这也会变得很混乱），并且 [Expo 模块可以使用 CLI 轻松引导。](https://docs.expo.dev/modules/native-module-tutorial/)
Flutter 的插件生态系统不如 React Native 社区那么广泛，因此您可能难以找到适合您的软件包。

因此，如果您希望使用利基原生 API 或希望在发布后立即访问新的平台功能，您可能需要选择 Expo。

### 3. 您是否希望跨平台拥有视觉上相同的界面？

Flutter 应用程序在所有平台上的外观和感觉都相同。这是因为 Flutter 使用自己的 [渲染引擎](https://docs.flutter.dev/resources/architectural-overview) Skia（过去），现在在 iOS 上使用 [Impeller](https://docs.flutter.dev/perf/impeller) 和小部件来绘制 UI。如果您希望跨平台拥有统一的品牌外观和感觉，这可能是一件好事，但它以无法在每个平台上完全呈现原生外观和感觉为代价。

为什么？

因为所有 Flutter 组件（或小部件）都具有特定的预定义样式，当 Apple 更新 iOS 版本和控件时，Flutter 组件仍然呈现相同的 UI，直到 Flutter SDK 和您的应用程序在几周/几个月后更新。

另一方面，Expo 使用平台的原生组件。这意味着组件由平台本身渲染，您的应用程序将在每个平台上都是原生的。如果您希望采用每个平台的设计指南和行为，这可能是一件好事。

此外，使用平台原生组件意味着拥有开箱即用的内置可访问性，这对 Expo 来说是一个很大的优势。毕竟，Google 和 Apple 的工程师花了数年时间完善他们的组件。

如果您希望跨平台拥有相同的设计，请选择 Flutter。如果您希望采用自适应样式，让您的用户在使用您的应用程序时感到宾至如归，您应该选择 Expo。

### 4. 您是否希望拥有应用程序的 Web 版本？

虽然 Flutter 从技术上讲允许定位 [Web](https://flutter.dev/multi-platform/web)，但它不如移动版本成熟。

您的整个应用程序都在一个 `canvas` 中渲染，这给 SEO 和可访问性带来了障碍，因为屏幕阅读器将难以理解画布中所有元素的含义。

此外，您的应用程序的 Web 版本看起来和感觉不像真正的 Web 应用程序，更像是运行在浏览器中的移动应用程序。通常，即使 [Flutter 开发人员也不喜欢这种方法](https://www.reddit.com/r/FlutterDev/comments/180h020/why_is_flutter_not_as_popular_for_web_its_a_great/)。

另一方面，Expo 可以提供使用 DOM 的应用程序的 Web 版本。这意味着您可以构建一个移动应用程序，并通过最少的努力获得一个 Web 版本。

使用 [Expo Router](https://docs.expo.dev/router/introduction/)，您可以获得基于文件的路由，并可以使用相同的组件来构建您的移动应用程序和 Web 应用程序，从而实现通用应用程序。

这意味着您可以同时获得两全其美：一个在每个平台上看起来和感觉都像原生应用程序的移动应用程序，以及一个看起来和感觉都像真正的 Web 应用程序的 Web 应用程序。

如果您希望拥有应用程序的 Web 版本，您应该选择 Expo。

### 5. 您是否希望快速构建原型？

Flutter 的内置 UI 组件允许您快速构建出色的 UI。如果您是独立开发者，这尤其宝贵，因为您可以快速构建一个看起来像您雇佣了设计师的 MVP。

唯一的缺点是，在构建看起来像原生 iOS 应用程序的应用程序时，使用 [Material Design 组件](https://docs.flutter.dev/ui/widgets/material) 比较困难（尤其是针对两个平台的自适应样式）。

人们还抱怨 React Native 缺少 UI 组件。如果您想构建自定义 UI，您必须使用 [StyleSheet API](https://reactnative.dev/docs/stylesheet) 自己构建，或者添加像 [NativeWind](https://www.nativewind.dev/) 这样的库，将 [TailwindCSS](https://tailwindcss.com/) 带入 React Native 或将 [Tamagui](https://tamagui.dev/) 带入您的项目。

总的来说，您在 React Native 中构建 UI 所花费的时间要比在 Flutter 中多得多。

如果您需要快速发布原型，您应该选择 Flutter。

### 6. 您是否希望使用无线更新？

应用商店审核流程存在摩擦。您的应用程序可能需要几天甚至几周才能完成审核和发布。如果您需要修复严重错误或希望快速推出新功能，这可能是一个问题。

使用 Expo，您可以使用 [EAS Update](https://docs.expo.dev/eas-update/introduction/) 将 JS 更新直接发送到应用程序的最终用户。此服务允许您替换应用程序中的非原生部分（JS、样式代码和资产），而无需向商店提交新版本。

这对拥有众多用户的知名公司来说是一个绝对的改变游戏规则。您可以快速修复错误并推出新功能，而无需等待外部审核流程的等待时间和不确定性。
Flutter 没有内置的无线更新功能，因为 Flutter 应用程序被编译成二进制文件，无法轻松替换。但是，[Shorebird](https://shorebird.dev/) 是一项新服务，它承诺在早期阶段为 Flutter 应用程序提供相同的功能。

此外，其他无线更新服务的未来尚不明朗，因为微软宣布将 [App Center](https://appcenter.ms/) 退役。

如果您计划频繁地向用户推送更新或希望快速修复生产中的错误，请为您的下一个项目选择 Expo。

### 7. 您是否计划组建一个开发人员团队？
找到或提升一名开发人员很容易，但如果您想扩展您的应用程序并需要一个团队来支持它怎么办？

由于 React 主导着 Web，几乎每个 Web 开发人员都有一些 React 经验。这意味着您可以轻松找到可以参与您的 Expo 项目的开发人员，并且学习时间最短。

另一方面，Flutter 是一种更利基的技术，仅仅因为 Dart 是一种利基语言，而 JavaScript 则更通用。Flutter 的普及率正在上升，但由于语言限制，它仍然没有像 React 那样被广泛采用。您需要帮助找到可以参与您的 Flutter 项目的开发人员，因为 Dart 实际上只用于 Flutter 项目。

如果您想组建一个开发人员团队来支持您的应用程序多年，请选择 Expo。

PS：如果您想学习 React Native 或提升您的团队技能，请查看 [Galaxies. Dev 的深入 React Native 视频课程](https://galaxies.dev/)。

### 8. 您是否想要最佳性能？
您阅读的几乎每篇文章都告诉您 Flutter 比 React Native 更快。

而且，有时，这是真的。这取决于应用程序。

由于 Flutter 使用其渲染引擎，因此它可以实现出色的性能。但他们正在从 Skia（一个成熟的渲染引擎）迁移到 Impeller。目前尚不清楚这对性能的影响。

过去，React Native 由于 JavaScript 和原生代码之间的 [桥接](https://reactnative.dev/docs/communication-ios) 而比 Flutter 慢。但是，随着 [TurboModules](https://reactnative.dev/blog/2021/09/13/turbomodules) 和 [新架构](https://reactnative.dev/docs/the-new-architecture/landing-page) 的引入，React Native 变得快得多（看看这些 [性能基准](https://github.com/reactwg/react-native-new-architecture/discussions/123) 来自 2023 年）。

在撰写本文时，[React Native](https://reactnative.dev/docs/the-new-architecture/landing-page) 中的新架构尚未成为标准，并非所有库都与之兼容。

最重要的是，您现在还可以使用 [[React Native Skia](https://shopify.github.io/react-native-skia/) 在您的应用程序中使用 Skia 作为渲染引擎，这可以使 Expo 的性能与 Flutter 相媲美。

不过，还有一个问题：您是否需要最佳性能？

如果您构建一个标准应用程序，Flutter 和 Expo 之间的性能差异对最终用户来说是不可察觉的。两种技术都足够快，并提供出色的用户体验。

但是，在构建具有大量动画的复杂应用程序（例如 [Wonderous](https://flutter.gskinner.com/wonderous/)）时，您可能希望选择 Flutter 以获得最佳性能。话虽如此，Skia 的创建者 William Candillon 最近 [展示了使用 React Native 构建的强大应用程序动画](https://youtu.be/Pu-Zngp0JUU?si=9r_-oPHsH70pNidT)。

要确定哪种技术在性能方面“获胜”，我们必须定义如何衡量性能。仅仅是速度吗？是滚动的外观和感觉吗？崩溃率？CPU 使用率？

然后，您必须决定哪种性能对您的用例最重要。

如果您在 Google 上搜索“Flutter vs. React Native 性能”，您会看到很多偏爱 Flutter 的博客。我的建议是更细致入微地考虑您如何评估性能。如果没有当前的和客观的公共基准，就无法以二进制方式进行评估。根据您团队的技能和您的用例做出决定。

### 9. 您是否想要一个工具生态系统来创建、审查和提交您的应用程序？
Expo 不仅是 React Native 的推荐框架，而且还附带各种工具，供团队和公司构建、测试和部署他们的应用程序。

迭代速度在构建移动应用程序时至关重要。Expo 提供了 [Expo Go](https://expo.dev/go) 等工具来在您的手机上测试您的应用程序，[Expo CLI](https://docs.expo.dev/more/expo-cli/) 来管理您的项目，以及 [Expo Orbit](https://expo.dev/orbit) 来使用一键式构建启动和模拟器管理与您的团队协作。

除此之外，您还可以选择使用 Expo 应用程序服务 (EAS)：
[EAS Build](https://docs.expo.dev/build/introduction/) 在云端构建您的应用程序，因此您无需担心为 iOS 和 Android 设置构建环境。[EAS Submit](https://docs.expo.dev/submit/introduction/) 将您的应用程序提交到应用商店，无需使用 Xcode 或 Android Studio。[EAS Update](https://docs.expo.dev/eas-update/introduction/) 将 JS 更新直接推送到您的最终用户。
对于 Flutter，您可以使用像 [Codemagic](https://codemagic.io/) 这样的服务来构建、测试和部署您的应用程序。但是，它不像 Expo 生态系统那样集成，需要更多设置和配置。

如果您希望获得最佳支持来构建、测试和部署您的应用程序，并使用与 GitHub 等工具集成的强大自动化功能，您应该选择 Expo。

### 10. 您是否想要一项具有活跃社区的未来安全技术？
Flutter 的开发由 Google 提供支持，Google 拥有 [结束项目](https://killedbygoogle.com/) 的 [声誉](https://killedbygoogle.com/)。但是，Google 一直积极开发和使用 Flutter 在其应用程序中，这是一个好兆头。

这意味着 Flutter 拥有清晰的路线图，并且主要由 Google 工程师积极开发。虽然 Flutter 社区正在不断壮大，但它仍然不如 React Native 社区大。

如果 Google 决定停止开发 Flutter 会怎样？社区会继续开发和维护 Flutter 吗？在选择 Flutter 时，您应该问问自己这些问题。

另一方面，React Native 由社区提供支持。这意味着社区推动 React Native 的开发，并添加新功能和更新。

虽然 Meta 仍在积极开发 React Native，但社区在 React Native 的开发中发挥着重要作用。像 [Microsoft](https://microsoft.github.io/react-native-windows/) 和 [Shopify](https://shopify.github.io/flash-list/) 这样的公司正在积极为 React Native 做出贡献，而像 [Software Mansion](https://swmansion.com/)、[Margelo](https://margelo.io/)、[Infinite Red](https://infinite.red/) 和 [Callstack](https://www.callstack.com/) 这样的大型机构正在与 [Expo](https://expo.dev/) 的支持相结合，为 React Native 构建工具和库。

即使 Meta 停止开发 React Native，社区也会继续开发和维护 React Native。

如果您想选择一项具有活跃社区的未来安全技术，请选择 Expo。

## 做出您的选择
现在您已经回答了十个问题，您应该更好地了解为下一个项目选择哪种技术。

没有人说选择很容易，对吧？

如果您仍然不确定，让我帮助您快速了解一下：

**如果您：**
- 已经拥有 React 经验或代码
- 想要使用一个代码库构建 Web 和移动应用程序
- 想要使用原生平台组件
- 需要访问最新的原生平台 API
- 想要代码推送
- 计划使用大型团队构建一个面向未来的应用程序
**您应该选择 Expo。**
**如果您：**
- 拥有现有的 Dart 开发人员或知识
- 需要非常快地制作原型界面
- 想要跨平台的视觉上相同的界面设计
- 想要创建更接近游戏的“自定义”应用程序体验
- 也关注桌面或嵌入式设备应用程序
**您应该选择 Flutter。**
请记住，这两种技术都很棒，您可以构建出色的应用程序。最重要的是选择最适合您的用例、利益相关者和团队的技术。

## Flutter 和 Expo 的未来
Flutter 和 Expo 的未来一片光明。这两种技术都由各自的社区和公司积极开发和维护，并且定期添加新功能和更新。

Flutter 的普及率正在上升，并被 Google、[阿里巴巴](https://flutter.dev/showcase/alibaba-group) 和 [宝马](https://flutter.dev/showcase/bmw) 等公司用于构建移动、Web 和桌面应用程序，这些应用程序提供自定义应用程序体验。

Expo 被 [Meta](https://reactnative.dev/showcase)、[Microsoft](https://devblogs.microsoft.com/react-native/) 和 [Coinbase](https://www.coinbase.com/en-de/blog/optimizing-react-native) 等公司用于构建移动应用程序，这些应用程序在每个平台上看起来和感觉都像原生应用程序。

Evan Bacon 的博客还包含一个 [使用 React Native 和 Flutter 构建的应用程序](https://evanbacon.dev/blog/expo-2024/) 的广泛列表。

总的来说，越来越多的大型公司选择 Expo 而不是 Flutter。我观察到的趋势是，公司使用 Flutter 来构建员工体验，在这种体验中，在多个设备上拥有视觉上相同的体验对于内部应用程序来说是有意义的，而公司使用 Expo 来构建消费者体验。这些显然不是绝对的。有很多面向消费者的 Flutter 应用程序和内部 Expo 应用程序。

但是，如果您正在构建一个您认为可以扩展到大众市场的应用程序，那么您最好使用 Expo，因为您可以使用 [Expo](https://www.youtube.com/@galaxies_dev) 快速扩展您的应用程序和团队。

[
YOUTUBE.COM/THENEWSTACK
科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看所有播客、访谈、演示等。

[https://youtube.com/thenewstack?sub_confirmation=1](https://youtube.com/thenewstack?sub_confirmation=1)