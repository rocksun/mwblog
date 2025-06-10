# 构建原生移动和 Web 的 10 个跨平台选项

![Featued image for: 10 Cross-Platform Options for Building Native Mobile and Web](https://cdn.thenewstack.io/media/2025/05/8ec7897a-skyscraper-building-apps-2-1024x576.jpg)

## 1. Flutter

[Google](https://cloud.google.com/?utm_content=inline+mention) 的开源移动 [UI 工具包 Flutter](https://github.com/flutter) 通过单个代码库，为移动、Web 和桌面应用程序提供具有原生外观和感觉的高性能应用程序。它构建于 [Dart 编程语言](https://thenewstack.io/week-programming-ashes-arises-dart-2/)之上，以 [hot reload](https://docs.flutter.dev/tools/hot-reload)、可自定义的用户界面和丰富的 Widget 集而闻名。[Flutter](https://thenewstack.io/flutter-fever-adoption-grows-and-spreads-to-embedded-devices/) 在 Google 内部使用，但也已被 BMW 和 [Toyota](https://thenewstack.io/how-toyota-drove-agile-load-testing-to-the-cloud/) 等公司使用。

## 2. Iconic

[Iconic](https://github.com/iconic) 是一个开源移动 UI 工具包，用于使用 HTML、CSS 和 JavaScript 构建高质量的跨平台混合和 [渐进式 Web 应用程序 (PWA)](https://thenewstack.io/growth-of-progressive-web-apps/)。开发人员使用它来创建可以在 Web、iOS、Android 和桌面平台上运行的应用程序。

虽然过去版本的 Ionic 与 [Angular](https://thenewstack.io/angular-shares-potential-ideas-for-2025-improvements/) 紧密耦合，但该框架的 4.x 版本经过重新设计，可以作为独立的 [Web Component](https://thenewstack.io/introduction-to-web-components-and-how-to-start-using-them/) 库工作，因此可以在大多数前端框架中使用，包括 [React](https://thenewstack.io/react-adds-new-experimental-animation-feature/) 和 [Vue](https://thenewstack.io/a-peek-at-whats-next-for-vue/)。某些 JavaScript 框架需要一个 shim，它是一种代码（通常是一个库），充当中间层，以实现完整的 Web Component 支持。

## 3. Kotlin

[Kotlin](https://thenewstack.io/how-to-handle-platform-specific-dependencies-in-kotlin-multiplatform/) 是一种通用的多平台编程语言，由 [集成开发环境 (IDE)](https://thenewstack.io/agentic-ides-next-frontier-in-intelligent-coding/) 提供商 [JetBrains](https://thenewstack.io/jetbrains-agentic-ai-assistant-helps-automate-coding-tasks/) 开发。Kotlin 可以编译为 JVM、[用于 Web 开发的 JavaScript](https://thenewstack.io/javascript-framework-reality-check-whats-actually-working/) 以及用于构建面向 Android、iOS、macOS、Windows、[Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 和 [WebAssembly](https://thenewstack.io/top-5-uses-of-webassembly-for-web-developers/) 的跨平台应用程序的本机代码。Kotlin 与 UI 框架（如 [Compose Multiplatform](https://github.com/JetBrains/compose-multiplatform)）一起使用，Compose Multiplatform 是一个基于 Kotlin 的框架，用于在 Android、iOS、桌面和（实验性地）Web 的多个平台之间共享声明式 UI。

该公司还拥有 [Kotlin Multiplatform Mobile](https://www.jetbrains.com/kotlin-multiplatform/)，这是一个构建在 Kotlin 语言之上的移动开发框架。它允许开发人员编写一次平台无关的业务逻辑，然后通过 Kotlin/Native 将其编译为 Android 的 Kotlin 库和 iOS 的本机 Universal Framework。Netflix 使用该工具创建了 Prodicle，这是一个用于电视节目和电影制作的移动应用程序。

## 4. Lynx

[Lynx](https://github.com/lynx-family) 是一系列技术，其中 [LynxJS](https://github.com/lynx-family/lynx) 是 ByteDance（TikTok 的所有者）创建的 [跨平台 UI 框架](https://thenewstack.io/cross-platform-ui-framework-lynx-competes-with-react-native/)。它使开发人员能够使用单个代码库为跨平台应用程序（包括 Web、Android 和 iOS）创建原生用户界面 (UI)。它于 3 月 5 日推出，并且已经获得了积极的评价，并与 React Native 进行了比较。

## 5. NativeScript

[NativeScript](https://github.com/nativescript) 是一个开源的、基于 JavaScript 的框架，用于使用 JavaScript、TypeScript 或 Angular 构建移动原生 iOS 和 Android 应用程序。与在 WebView 中呈现 UI 的混合框架不同，NativeScript 直接编译为原生 UI 组件，从而实现性能和用户体验，与使用 Swift 或 Kotlin 等平台特定语言构建的应用程序非常匹配。这使 Web 开发人员能够利用他们现有的技能来创建高性能的 [移动应用程序，同时仍然可以访问原生](https://thenewstack.io/beta-solution-helps-frontend-developers-make-native-mobile-apps/) 设备 API。

## 6. .NET MAUI
[.NET MAUI](https://github.com/dotnet/maui)，之前称为 Xamarin，代表 NET 多平台应用 UI。由 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 开发，它允许 .[NET 开发人员使用](https://thenewstack.io/what-net-maui-can-do-for-frontend-and-web-developers/) 单个代码库构建原生移动和桌面应用程序。它利用 C# 和 .NET 生态系统，提供统一的 API 来访问平台特定的[功能并创建](https://thenewstack.io/using-apis-with-low-code-tools-9-best-practices/)可在 iOS、Android、macOS 和 Windows 上运行的用户界面。Progress Software 正在使用它。[Xamarin 仍然可用](https://github.com/xamarin)。

## 7. One

[One 是一个基于 React 的框架](https://thenewstack.io/one-lets-frontend-devs-build-once-deploy-web-and-native-apps)，允许开发人员编写一次并部署到 Web 或 React Native 以用于移动设备。根据创建者 Nate Wienert 的说法，它目前处于 beta 阶段，Nate Wienert 也构建了 UI 库 [Tamagui](https://github.com/tamagui/tamagui)。[One 以 Web 和原生为目标](https://thenewstack.io/one-lets-frontend-devs-build-once-deploy-web-and-native-apps/)，带有一个 [Vite](https://thenewstack.io/vites-new-rust-based-javascript-bundler-available-in-beta/) 插件，允许开发人员创建 Web 和原生平台应用程序。它将生成单页应用程序、静态站点生成和服务器端渲染的网页，这是这个新框架的关键区别。

## 8. Qt

[Qt](https://www.qt.io/download-dev) 是一个成熟的跨平台框架，主要用 [C++](https://thenewstack.io/bjarne-stroustrup-on-how-he-sees-c-evolving/) 编写。它用于桌面开发（Windows、MacOS 和 Linux），但也支持嵌入式系统、带有 Qt for Mobile 的移动设备和带有 Qt for WebAssembly 的 Web。它提供了一组丰富的 UI 小部件和工具。
除了 UI 开发之外，Qt 还提供了一组用于网络、数据库访问、多媒体和 XML 处理等功能的库，因此它可以用于从单个代码库构建跨平台的复杂应用程序。与此列表中的其他选项不同，QT 可通过 [LGPL 和 GPL 许可](https://www.qt.io/licensing/open-source-lgpl-obligations)获得，但也有商业许可选项。

## 9. React Native

[React Native](https://github.com/facebook/react-native) 是一个开源框架，使开发人员能够使用 JavaScript 和 React 构建适用于 iOS 和 Android 的原生移动应用程序。它允许跨平台代码重用，从而加速开发，同时仍然提供对原生设备功能和性能的访问。[JavaScript Web 开发人员](https://thenewstack.io/web-development-in-2023-javascript-still-rules-ai-emerges/)使用它来构建移动应用程序。利用 React Native 的一种方法是使用 [Expo，一个构建在 React Native 之上的框架和平台](https://github.com/expo/expo)。

## 10. Swift

[Swift](https://github.com/swiftlang/swift) 由 Apple 为其自身平台设计，现已发展成为一种跨平台编程语言。它可在 Linux 和 Windows 上用于服务器端开发、命令行工具和桌面应用程序。[SwiftUI](https://developer.apple.com/xcode/swiftui/) 是一个基于 Swift 的专有框架，用于构建跨 Apple 平台（iOS、macOS、watchOS、tvOS 和 visionOS）的应用程序。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。