<!--
title: JavaScript新框架？这经济还敢搞？
cover: https://cdn.thenewstack.io/media/2026/01/fc690a66-sigment_js_-framework.jpg
summary: Yaniv Soussana开发Sigment框架，简化JS开发。它摒弃JSX、不混合HTML/JS、无虚拟DOM，采用Signals提升性能和响应性。适合厌倦React者。
-->

Yaniv Soussana开发Sigment框架，简化JS开发。它摒弃JSX、不混合HTML/JS、无虚拟DOM，采用Signals提升性能和响应性。适合厌倦React者。

> 译自：[A New JavaScript Framework? In this Economy?](https://thenewstack.io/a-new-javascript-framework-in-this-economy/)
> 
> 作者：Loraine Lawson

经过 20 年的软件开发经验，全栈开发者 [Yaniv Soussana](https://www.linkedin.com/in/yaniv-soussana-408a4a137/?originalSubdomain=il) 已经厌倦了基于 React 的 JavaScript 框架的复杂性。因此，作为应用转换工具 [Wappaa](https://wappaa.com/) 的创建者，他做了开发者们常做的事：他构建了一个新的框架，名为 [Sigment](https://sigment.dev/)。

他表示：“我想创造一些比 [React](https://thenewstack.io/web-development-in-2025-ais-react-bias-vs-native-web/) 和 [Angular](https://thenewstack.io/angular-v21-adds-signal-forms-new-mcp-server/) 更好的东西，因为我已经厌倦了这一切——我想为开发者创造一些简单的东西。”

Sigment 通过豁免来简化，这意味着它**不**会：

* 将 HTML 与 JavaScript 结合；
* 使用 JSX；或
* 创建虚拟 DOM。

那么，你会在什么时候使用 Sigment 呢？

首先，如果你[厌倦了基于 React 的框架](https://sigment.dev/blogs/sigment-vs-react/)或者不想学习 React，它可能是一个不错的选择。这个[开源框架](https://github.com/sigmentjs)声称以最小开销实现最大运行时性能、通过 API 对渲染进行完全控制、零配置开发无需转译，以及细粒度响应性。

让我们深入了解一下。

## HTML 和 JavaScript 混合的问题

React 将 JavaScript 与 HTML 语法 (JSX) 混合使用，坦率地说，Soussana 并不喜欢。Sigment 不混合两者，他表示这使得语法更短、更容易。这使得该框架对那些了解原生 JavaScript 但不想学习 React（React 创建并使用了 JSX）的人更易于访问。

他表示，这使得该框架不仅可以构建单页应用；它还支持 HTML 优先架构。此外，Sigment 支持动态或增量渲染。

他解释说：“开发者可以创建一个小型网站，然后当用户开始移动时，它会及时地、即时地创建新的元素和一切。”他还补充说，它会将该元素放入缓存中以获得更好的性能。

## 为什么 Sigment 不使用 JSX

JSX 代表 JavaScript XML。它是一种语法扩展，允许开发者直接在 JavaScript 中编写类似 HTML 的代码。

就上下文而言，React 依赖于 JSX 语法，其他基于 React 的框架也是如此。Preact、Qwik 和 Solid JS 也使用 JSX。使用 JSX，开发者编写生成 HTML 的 JavaScript。

JSX 的问题在于它需要代码的转译或转换，以及额外的工具，如 Babel、Webpack 或 Vite。Soussana 表示，虽然这感觉像是声明性的，但它增加了构建过程的复杂性。

Sigment 依赖于模板，这意味着 UI 是以框架引擎可理解的 HTML 的专业版本编写的。顺便说一下，Svelte 也[相当出名地使用了这种方法](https://svelte.dev/blog/virtual-dom-is-pure-overhead)，Angular 和 Vue 也是如此。

Sigment 不使用 JSX，而是依赖于 JavaScript 标签函数。与其写成：

`<div class="container">`,

……开发者可能会写成：`div({ class: 'container' })`。

根据 Sigment 网站的说法，这带来了“闪电般快速”的性能和更快的迭代，因为代码已经是有效的 JavaScript。Soussana 告诉 The New Stack，此外，由于 Sigment 不使用 JSX，开发者可以创建纯 HTML 和简单语法的网站。他还解释说，这也意味着该框架无需创建虚拟 DOM 即可工作。

## 没有虚拟 DOM

我问 Soussana 为什么他决定不使用虚拟 DOM，虚拟 DOM 是“真实”DOM（即屏幕上的实际 HTML 元素）的轻量级、简化副本。虚拟 DOM 在开发者代码和实际浏览器之间充当“草稿板”。

Soussana 指出，Svelte 和 SolidJS 也不使用虚拟 DOM。

“我们正处于新一代，”他说，“我们不再需要虚拟 DOM 了。它只会增加更多的复杂性和重量，而且编译需要更多时间。”

相反，Sigment 使用 Signals。Angular 和 Qwik 的创建者 [Miško Hevery](https://github.com/mhevery) 曾将 [Signals 解释为放入桶中的值](https://thenewstack.io/angular-qwik-creator-on-how-js-frameworks-handle-reactivity/)。他将其比作一个交通警察，告知框架何时有访问发生。当读取一个 Signal 时，框架会发送一条消息，表示有人读取了该值，然后它会继续处理下一个值。

Soussana 解释说，这使得性能轻量化，他还补充说，Sigment 首次运行时，在运行时，当用户需要某些东西时，它会渲染它并将其保存到缓存中。下次用户需要时，可以直接从缓存中获取。

Soussana 说，没有虚拟 DOM 和没有 JSX 也意味着更小的包大小，他补充说，这为用户和开发者创造了更好的性能和更好的体验。