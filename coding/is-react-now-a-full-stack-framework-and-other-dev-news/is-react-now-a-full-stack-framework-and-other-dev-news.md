
<!--
title: React现在是全栈框架吗？
cover: https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2.png
-->

本周我们将探讨 React 理论、Claude 如何为开发者生成工件、最新 TypeScript 版本以及 Project IDX。

> 译自 [Is React Now a Full Stack Framework? And Other Dev News](https://thenewstack.io/is-react-now-a-full-stack-framework-and-other-dev-news/)，作者 Loraine Lawson。

也许我们并没有生活在[后 React 世界](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)，而是生活在一个新的 React 范式中：[React 正在成为一个全栈框架](https://www.robinwieruch.de/react-full-stack-framework)，软件工程师和自由开发者[Robin Wieruch](https://www.linkedin.com/company/rwieruch/) 最近争论道。

“这仅仅是 React 全栈开发的开始，”Wieruch 写道。“随着开发者开始通过 Server Components 和 Server Actions 直接访问数据库，在超越简单 CRUD 应用程序的复杂性方面，将会有一个学习曲线。”

Wieruch 补充说，这将使前端开发者能够快速掌握实现具有层级、设计模式和最佳实践的后端架构。

## Claude 现在可以生成工件

[工件为 Claude AI 用户提供了一个专用窗口](https://www.anthropic.com/news/artifacts) 来查看、迭代和构建在 Claude 中创建的任何工作。对于开发者来说，这提供了一个单独的窗口来查看代码或从代码库创建架构图，据 Claude 团队称。

“工件将与 Claude 的对话变成了更具创造力和协作性的体验，”Claude 博客指出。“有了工件，您将拥有一个专用窗口，可以立即查看、迭代和构建您使用 Claude 创建的工作。”

![Claude 的屏幕截图，显示了带有 Python 代码的工件界面。](https://cdn.thenewstack.io/media/2024/08/234c2f0e-artifacts_claude.jpg)

*Claude.ai 的屏幕截图*

工件现在可供所有[Claude.ai](https://claude.ai/new) 用户在平台的免费、专业版和团队计划中使用。工件也可以在 Claude 的 iOS 和 Android 模型上创建和查看。它还可以创建：

- 代码片段
- 流程图
- SVG 图形
- 单页 React 或 HTML 网站
- 交互式仪表板
- 插入图片

Anthropic 的帖子包含一个视频，描述了此功能是如何创建的，并探讨了开发之外的其他用例，但要更深入地了解如何使用它来构建 Web 应用程序，请查看[Pragmatic Engineer 的这篇帖子](https://newsletter.pragmaticengineer.com/p/how-anthropic-built-artifacts)，它深入探讨了工件的功能和创建。

“虽然这个功能很小，但感觉它可能是使用 LLM 进行协作工作的一大飞跃——因为每个工件都可以共享、供其他人使用和重新组合，”[Gergely Orosz](https://www.linkedin.com/in/gergelyorosz/?originalSubdomain=nl) 解释道，他撰写了 Pragmatic Engineer。

## 使用 TypeScript 捕获更多错误

[TypeScript 5.6 的候选版本](https://devblogs.microsoft.com/typescript/announcing-typescript-5-6-rc/) 已经发布，[Microsoft TypeScript 产品经理 Daniel Rosenwasser](https://www.linkedin.com/in/daniel-rosenwasser-b56b7837/) 提供了新功能的汇总，包括禁止空值和真值检查以捕获更多错误。Rosenwasser 列出了几个代码示例，这些代码没有按照作者的意图执行，但仍然是有效的 JavaScript 代码。他写道，以前 TypeScript 只是接受这些示例。现在不再了。

“但通过一些实验，我们发现可以从标记上面这些可疑示例来捕获许多错误，”他写道。“在 TypeScript 5.6 中，当编译器能够语法上确定真值或空值检查将始终以特定方式评估时，它现在会报错。”

> “但通过一些实验，我们发现可以从标记上面这些可疑示例来捕获许多错误。”
>
> — Daniel Rosenwasser，Microsoft TypeScript 产品经理

TypeScript 5.6 还引入了一种名为 IteratorObject 的新类型，并且该帖子提供了关于如何定义它的代码示例。

Rosenwasser 写道，有一个 AsyncIteratorObject 类型用于奇偶校验。

“AsyncIterator 尚未作为 JavaScript 中的运行时值存在，它为 AsyncIterables 带来了相同的方法，但它是一个积极的提案，这种新类型为此做好了准备，”他解释道。

## Project IDX 将代码编辑器与语言和工具相结合

[Project IDX](https://thenewstack.io/project-idx-googles-new-web-and-mobile-app-development-ide/) 是一种基于浏览器的开发体验，它建立在 Google Cloud Workstations 之上，并由[Codey](https://lablab.ai/tech/google/codey) 提供支持，Codey 是一种基于代码训练的、建立在 PaLM 2 之上的基础 AI 模型。它的目标是简化构建、管理和部署全栈 Web 和跨平台应用程序，并使用流行的框架和语言。

Project IDX 项目旨在统一开发环境的两个主要部分：代码编辑器以及构建及运行代码所需的语言和工具，该团队在最近一篇有关过去一年 Project IDX 开发历程的反思文章中写道。

“Project IDX 的核心是我们坚信你应该能够在任何地方、任何设备上进行开发，并且能充分利用本地开发的高保真度。”Project IDX 团队在去年介绍该项目时写道。“每个 Project IDX 工作空间都具备基于 Linux 的虚拟机的全部功能，以及托管在云中（在你附近的某个数据中心中）带来的通用访问优势。”

今年的更新指出，Project IDX 团队关注三个领域：

- 利用 Gemini 支持的生成式人工智能工具来提高开发人员的工作效率。
- 通过项目模板和集成来重新定义“快速入门”的含义。
- 使用 Flutter、React Native 以及即将推出的 Android Studio 将原生移动应用程序开发引入浏览器。

该团队已将 Gemini 提供的生成式人工智能功能集成到了代码中。

今年的更新指出，Project IDX 团队关注三个领域：利用 Gemini 支持的生成式人工智能工具来提高开发人员的工作效率。通过项目模板和集成来重新定义“快速入门”的含义。使用 Flutter、React Native 以及即将推出的 Android Studio 将原生移动应用程序开发引入浏览器。该团队已将 Gemini 提供的生成式人工智能功能集成到了代码中。