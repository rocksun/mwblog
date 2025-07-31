
<!--
title: 厌倦了 JavaScript 框架的复杂性？认识一下 Still.js
cover: https://cdn.thenewstack.io/media/2025/07/46ac1d7e-still_framework.jpg
summary: Nakassony Bernardo 创建了 Still.js 框架，旨在简化遗留 Web 应用程序的现代化，它允许引入 React、Angular 或 Vue.js 等框架的功能，而无需重写代码。Still.js 适用于企业级应用，支持模块化、用户权限管理、组件路由等功能，且不依赖打包器。
-->

Nakassony Bernardo 创建了 Still.js 框架，旨在简化遗留 Web 应用程序的现代化，它允许引入 React、Angular 或 Vue.js 等框架的功能，而无需重写代码。Still.js 适用于企业级应用，支持模块化、用户权限管理、组件路由等功能，且不依赖打包器。

> 译自：[Tired of JavaScript Framework Complexity? Meet Still.js](https://thenewstack.io/tired-of-javascript-framework-complexity-meet-still-js/)
> 
> 作者：Loraine Lawson

开发者 [Nakassony Bernardo](https://www.linkedin.com/in/nakassony-bernardo-8392879a/) 面临着一个在企业中很常见的问题，无论哪个行业：现代化一个遗留的 Web 应用程序。许多较旧的 Web 界面没有使用 [JavaScript](https://thenewstack.io/introduction-to-javascript/) 框架，并且缺乏当今开发者拥有的能力。

“迁移那些遗留应用程序真的很难，因为它们确实解决了他们过去遇到的问题，并且在某种程度上，对于他们今天的一些问题仍然可用，”Bernardo 说。“你不能只是说，‘我要摆脱他们当时使用的任何东西，开始使用一个新的、现代的框架。’这根本行不通，因为你必须破坏现有的东西，而且还必须从头开始重建一切。”

## 更新遗留应用程序的挑战

必须使用 [TypeScript](https://thenewstack.io/typescript-5-5-faster-smarter-and-more-powerful/) 进一步增加了复杂性，因为它必须被转译为 JavaScript。

“这就是事情变得非常困难的时候，特别是当你处理那些遗留系统时，”他说。“现代化这些应用程序需要你**不**使用那些新的 JavaScript 方法，这意味着你需要坚持使用纯 JavaScript。但你需要引入所有新的 JavaScript 工具正在提供的那些功能——例如状态管理。”

例如，他有一个可以追溯到 2003 年的应用程序，但它仍然解决了组织的问题。因此，该公司希望添加一些新功能，而不会破坏核心。

Bernardo 在 vanilla JavaScript 中找到了答案，他用它创建了一个名为 [Still.js](https://github.com/still-js/core) 的新开源框架（*编者注：Still.js 也是一个基于 React 的 [静态站点生成器](https://thenewstack.io/nue-a-new-static-site-generator-taking-on-next-js/) 的名称，现在已被存档。*）。该框架允许他引入像 [React](https://thenewstack.io/remix-3-and-the-end-of-react-centric-architectures/)、[Angular](https://thenewstack.io/angular-v20-advances-zoneless-adds-support-for-ai-development/) 或 [Vue.js](https://thenewstack.io/a-peek-at-whats-next-for-vue/) 启用的功能，而无需重写代码。Still.js 只有大约一年的历史，但它提供了一个模块化和基于组件的架构，类似于那些流行的框架，他说。

”它提供了一种轻量级但功能强大的方法来构建应用程序，从而可以在不引入复杂抽象层的情况下实现更好的可维护性和可扩展性，“Bernado 在一篇关于 Still.js 的 [Medium 帖子](https://medium.com/@sonybernardo/still-js-a-way-to-leverage-vanilla-javascript-for-complex-and-enterprise-level-web-development-34cd1c555061) 中写道。“通过 Still.js，你可以获得原始 JavaScript 的灵活性，同时受益于有组织且高效的开发工作流程。”

## Still.js 用例

Still.js 还有其他应用程序。例如，它可以用于现代化一个较旧的 React 或 Angular 应用程序，同样不会破坏遗留代码。

虽然你不能轻易地组合像 React、Angular 和 Vue.js 这样的框架，但你可以将它们与 Still.js 集成。Bernardo 解释说，这是因为 Still.js 直接利用浏览器的原生功能，避免了复杂的工具和抽象层，这些工具和抽象层在混合其他主要框架时经常导致冲突。

“如果你正在使用 React 并尝试将其与 Angular 组合，你还必须找到一种方法来组合它们背后运行这些应用程序的工具，但 Still.js 不会告诉你这些，”Bernardo 说。“你不需要使用任何工具，因为它是 vanilla JavaScript。”

它还可以与其他技术栈组合，包括利用 [Java](https://thenewstack.io/introduction-to-java-programming-language/)、经典 [ASP](https://dotnet.microsoft.com/en-us/apps/aspnet) 甚至 [PHP](https://thenewstack.io/the-herd-is-strong-php-and-its-developer-ecosystem-at-30/) 的应用程序，他补充说。

## 架构和其他 Still.js 详细信息

Still.js 使用其自己的架构方法，称为服务、控制器和视图，因为“它在处理和处理组件的方式上非常世俗[在]的方式，因为它没有捆绑/构建过程”，根据 [Still.js 文档](https://still-js.github.io/stilljs-site/architecture/)。

[![Still.js 使用名为服务、控制器和视图的架构。](https://cdn.thenewstack.io/media/2025/07/394b5b87-scv-architecture.png)](https://cdn.thenewstack.io/media/2025/07/394b5b87-scv-architecture.png)

*Still.js 使用名为服务、控制器和视图的架构。图片来自 [Still.js 网站](https://still-js.github.io/stilljs-site/)。*

服务向视图提供数据并处理诸如 HTTP 请求之类的事务。控制器为视图提供不同的行为和 DOM 实现。视图显示需要向用户显示的任何内容。

Still.js 依赖于面向对象的原则，Bernardo 告诉 The New Stack。在状态管理方面，它提供本地状态管理和 [全局状态管理](https://thenewstack.io/how-to-simplify-global-state-management-in-react-using-jotai/)。

“在 Still.js 中，你为你的组件拥有那些状态属性或状态变量，这与组件本身有关，本地地，它将如何工作，”Bernardo 解释说。

React 引入了虚拟 DOM 作为实际 DOM 的轻量级、内存中的表示。它提供了一种以反应方式更新 UI 的方法，但 Still.js 避免了这种人为的层，他说。

“如果你开始引入越来越多的层，那么在某种程度上，你会影响性能，”他说。“我并不是说他们没有解决 React 中的性能问题，但我想说的是：当以反应方式更新用户界面时，是否需要它？因为它不需要，让我们尽量避免这些类型的实现。”

## Still.js 的其他不同之处

其他框架具有构建或编译过程，特别是如果需要将 TypeScript 转译为 JavaScript。

“他们获得了这个处理时间，将你编写的所有内容转换为浏览器需要渲染的内容，”他说。“我们在 Still.js 上没有这个，所以这是一种运行时渲染方法。每当这个组件被访问或请求时，渲染过程就开始了。”

该框架使用正则表达式来查找模板。模板中 80% 的内容将是 vanilla JavaScript，他补充说。但是，对于 HTML，有一些特殊的指令。Still.js 解释器将这些指令转换为浏览器可以理解的内容，他解释说。

“这就是渲染过程的工作方式，但它的一切都在 Still.js 本身之上，”他说。“没有其他框架用于渲染目的。”

> Still.js 模板中 80% 的内容将是 vanilla JavaScript。
> 
> **– Nakassony Bernardo, Still.js 的创建者**

根据 Bernardo 的说法，Still.js 也不需要预处理，也不依赖于像 WebPack 或 Vite 这样的打包器。他写道，这使得它“非常适合喜欢直接、不妥协地访问原生 Web 技术以及 Web 框架提供的那些现代功能的团队和开发者。”

毫不奇怪，考虑到它被创建的原因，Still.js 适用于企业和复杂的应用程序。

“企业级 Web 应用程序需要的不仅仅是丰富的 UI 功能。它们需要：模块化、用户权限管理、组件路由、验证、关注点分离、通信管理、微前端架构（例如，前端嵌入和交互）等等，”他写道。“Still.js 本地支持所有这些功能，而无需打包器增加构建时间和潜在的复杂性，甚至工具开销。”

正如他提到的，Still.js 也可以用于在 React 中创建微前端。该框架允许开发者将 Still.js 组件嵌入到现有应用程序中，但以这样一种方式，即该组件可以是一个完整的前端，从而可以访问诸如导航之类的功能，他在另一篇 [Still.js Medium 帖子](https://medium.com/@sonybernardo/rethinking-microfrontend-architecture-combining-still-js-f24862358847) 中写道。Bernardo 还在 [YouTube 教学视频](https://www.youtube.com/watch?v=8dPNkNhpbkc) 中详细阐述了微前端。

## Still.js 供应商组件

Still.js 提供基于组件的 UI 和基于 HTML 的模板。它具有内置的符号/指令、用户权限流程、组件状态管理、全局状态管理、路由和表单验证。

它甚至提供了一些 React 没有的东西。

“如果你在 React 中提出路由，你不能在路由时添加那些类型的数据传输，你需要依赖状态管理，”Bernardo 说。“你将把这些数据推送到，比如说，某种 [Redux 状态管理库](https://redux.js.org/)，然后一个兄弟工具需要去 Redux 检查那里有什么，然后从那里开始处理数据。”

Still.js 可以发送数据，无论多大，他补充说。

它还提供了一个名为供应商组件的功能，即当 Web 开发者需要一个不属于框架核心的功能时。到目前为止，只有少数这些功能，但供应商组件允许开发者使用新组件创建功能——然后该组件可以被重用。

Still.js 还提供了一种独特的内置注释方法，通过利用 JSDoc 和 JavaScript 注释，不是用于文档，而是用于在运行时动态添加功能，他在 [Still.js 网站](https://still-js.github.io/stilljs-site/) 上解释说。JSDoc 也用于类型和类型提示，启用大多数 TypeScript 功能，尽管他补充说“类型通常是可选的，除非在需要它的特定情况下。”

在 Still.js 中，开发者会找到一个完整的框架，但它仍然是一个年轻的框架，因此开发者可能会遇到可以改进的地方，Bernardo 说，并补充说他乐于接受贡献和建议。

“这是一个非常成熟的框架，但仍然是一个年轻的框架，尽管你可以构建非常庞大和复杂的东西，”他说。“我们对任何想法、任何贡献都非常开放。”