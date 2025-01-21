
<!--
title: Vite 的基于 Rust 的新 JavaScript 打包器 Beta 版可用
cover: https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2.png
-->

在其他开发者新闻方面，Flutter 和 React Native 在采用率调查中不相上下，而 Nue 成为一个基于标准的 Web 框架。

> 译自 [Vite’s New Rust-Based JavaScript Bundler Available in Beta](https://thenewstack.io/vites-new-rust-based-javascript-bundler-available-in-beta/)，作者 Loraine Lawson; Lawrence E Hecht。

[Rolldown，一个用 Rust 编写的 JavaScript 打包器](https://rolldown.rs/about)，由 void(0) 公司创建——该公司也负责 Vite——现已推出 Beta 版。Rolldown 团队在介绍这款打包器时表示，这款新的打包器提供了与 Rollup 兼容的 API 和插件接口，但在范围上更类似于 esbuild。

其目标是用一个统一的构建工具替换 Vite 中当前使用的 esbuild 和 Rollup [Vite](https://thenewstack.io/development-server-vite-gets-independent-team-and-rust-ifies/)。因为它是用 Rust 编写的，所以它的性能与 esbuild 相当，并且比 Rollup 快 10 到 30 倍。

“它的 [WASM](https://thenewstack.io/introduction-to-moonbit-a-new-language-toolchain-for-wasm/) 构建也比 esbuild 的构建速度快得多（因为 Go 的 WASM 编译效率不高）”，团队补充道。

团队写道，尽管它是为 Vite 设计的，但 Rolldown 可以用作独立的通用打包器。

根据 [Rolldown 介绍页面](https://rolldown.rs/guide/)，它可以在大多数情况下作为 Rollup 的直接替代品，也可以在需要更好的代码块控制时用作 esbuild 的替代品。

如果您想了解更多信息，JavaScript [YouTuber Theo Browne 也对 Rolldown 进行了深入探讨](https://www.youtube.com/watch?v=IDe1zVWoX94)。

## React Native 与 Flutter：使用率不相上下

尽管 Flutter 在一小部分移动开发者中占据主导地位，但[React Native 在更广泛使用跨平台移动框架的开发者群体中胜过 Flutter](https://thenewstack.io/googles-flutter-beefs-up-web-support-so-how-does-it-compare-to-react-native-now/)。

根据 TNS 对[最新 Stack Overflow 调查](https://survey.stackoverflow.co/2024/technology)的分析，工作重点是移动开发的开发者使用 Flutter 的可能性是使用 React Native 的两倍（41% 对 20%）。移动开发者仅占调查的 3%。在所有专业开发者中，Flutter 略微领先（9% 对 8%）。

许多 Web 首选开发者使用 JavaScript，但只有 37% 的专业雇佣移动开发者定期使用 JavaScript。然而，在 JavaScript 用户中，React Native 略微领先于 Flutter（14% 对 13%）。

[最新的 JetBrains 调查](https://www.jetbrains.com/lp/devecosystem-2024/)发现，30% 的开发者将应用程序部署到移动平台，但只有 54% 的这部分开发者实际使用了跨平台移动框架。在这部分开发者中，39% 使用 React Native，38% 使用 Flutter。

根据 JetBrains 的研究，在北欧和美国等移动优先开发不太常见的地区，React Native 的采用率超过了 Flutter。

## Nue Web 框架转向“标准优先”

前端/UX 开发者 [Teri Piirainen](https://www.linkedin.com/in/tipiirai/)，Web 框架 [Nue](https://github.com/nuejs/nue) 的创建者，对 JavaScript 及其在现代 Web 开发中的地位有很多话要说。

“我们已经将简单的任务需要大量 JavaScript 的想法视为常态，”Piirainen 在 [Nue JS 文档](https://nuejs.org/docs/)中写道。“基本的样式需要数千个实用程序类。设计更改意味着更新无数组件。虽然这种方法最初看起来可能很有效率，但它会产生难以改变且随着时间的推移越来越难以维护的僵化系统。”

正如您可能想象的那样，Nue 试图纠正这种情况。它是一个极小的 (2.3kb minzipped) 用于构建用户界面的 JavaScript 库。

虽然 Nue 已经开发了一段时间，但本月，Piirainen 宣布 [它现在将成为一个“标准优先”的 Web 框架](https://nuejs.org/blog/standards-first-web-framework/)。“

重点一直是去除人工层，帮助开发者将现代 HTML、CSS 和 JavaScript 提升到极致，”Piirainen 写道。他补充说，这一转变将使他能够专注于两个问题：

1. 他认为是复杂性常态化的前端工程问题。“最初是 HTML、CSS 和 JavaScript 的东西已经发展成为复杂的构建编排，即使对于一个简单的页面也需要数百个依赖项，”他解释道。
2. 设计工程问题，即 Web 设计应该重新关注设计而不是 JavaScript。“首先，JavaScript 工程师已经控制了讨论，”他写道。“你上次看到工程师讨论 Perfect Fifth 排版比例的优点或 Dieter Rams 系统方法背后的原则是什么时候？”

但他写道“标准优先”是什么意思呢？

“浏览器在过去十年中发展显著，”他写道。“通过遵循而不是对抗标准，我们能够用更少的代码创建更好的产品。”

这也意味着将语义化HTML作为一切的基础，并优先考虑内容。

“内容存在于简洁易访问的文件中——而不是JavaScript中，”他补充道。

他还强调了使用现代、系统化CSS的设计系统。他认为，其结果是更快的工具、更简洁的代码和更快的页面。

“最快的页面加载只需要一个请求。没有框架初始化，没有累积布局偏移，也没有等待JavaScript，”他写道。“当内容和样式一起到达时，页面就会立即显示。”
