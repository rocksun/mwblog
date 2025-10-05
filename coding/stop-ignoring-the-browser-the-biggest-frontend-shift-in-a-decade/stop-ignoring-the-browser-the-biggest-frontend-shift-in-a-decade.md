<!--
title: 别再忽视浏览器：十年前端巨变的序幕
cover: https://cdn.thenewstack.io/media/2025/10/c4c7c542-mohammad-mardani-p0dniqi1upw-unsplashb.jpg
summary: 浏览器整合框架功能，动摇其主导地位。框架仍提供约定与生态，但已从必需品变为偏好，开发者应关注原生平台。
-->

浏览器整合框架功能，动摇其主导地位。框架仍提供约定与生态，但已从必需品变为偏好，开发者应关注原生平台。

> 译自：[Stop Ignoring the Browser: The Biggest Frontend Shift in a Decade](https://thenewstack.io/stop-ignoring-the-browser-the-biggest-frontend-shift-in-a-decade/)
> 
> 作者：Alexander T. Williams

网页曾经感觉像是一个充斥着相互竞争的想法、半残废的库和伪装成标准的“胶带”解决方案的混乱集市。然后，框架像救世主一样大摇大摆地出现，承诺带来秩序。

但现在发生了一些奇怪的事情：浏览器本身正在将这些框架的许多“超能力”直接 [吸收到平台中](https://goodinternetmagazine.com/close-to-the-metal-web-design-and-the-browser/)。

框架并未消亡，但它们在开发者体验上的垄断地位正在瓦解，而且标准运动比十年来任何时候都更加尖锐。这场战斗不再是 React 和 Angular 之间，因为两者已联手对抗一个新敌人：浏览器。

## 框架始终是补丁，而非治愈良方

框架之所以能够占据主导地位，是因为网页坦率地说并未为现代应用开发做好准备。开发者需要路由、状态管理、模板、组件隔离——而这些浏览器都未能提供。

React 和 [Angular 不仅仅是靠炒作而流行起来的](https://blog.logrocket.com/angular-has-grown-up/)；它们填补了标准长期以来忽视的巨大空白。但老实说：它们始终是权宜之计。它们的 API 将网页改造得可行，但往往以牺牲性能和复杂性为代价。

想想 [React 的虚拟 DOM](https://legacy.reactjs.org/docs/faq-internals.html)：一个巧妙的技巧，让 DOM 操作不那么痛苦。或者 Angular 的双向绑定，看起来很神奇，直到你看到它在大规模应用中造成的混乱。这些想法之所以兴盛，是因为平台滞后了。

> 框架的肮脏秘密在于它们将城堡建在沙子上，而浏览器终于在它们下方铺设了坚实的地基。

然而，到了 2025 年，当平台本身提供了模板字面量、Shadow DOM 或新的 Web Components API 等解决方案时，我们真的还需要那些间接层吗？框架的肮脏秘密在于它们将城堡建在沙子上，而浏览器终于在它们下方铺设了坚实的地基。这一转变有潜力 [改善发布管理](https://octopus.com/devops/software-deployments/release-management/)、代码维护以及更多方面。

## 原生平台功能的崛起

标准正在“蚕食”那些曾是框架专属的功能，而且其速度之快超出了许多人的想象。Shadow DOM 现在提供了真正的组件封装，无需第三方库。ES 模块终结了 `script` 标签的依赖混乱，为我们带来了原生的导入和导出。再加上 fetch、async/await 和 streams——这些曾需要 polyfills 或完整库的功能——现在的平台与十年前相比判若两样。

以路由为例，它长期以来一直是框架的“皇冠上的明珠”。Navigation API 和 View Transitions API 允许开发者用最少的代码 [创建流畅、类似原生的导航效果](https://css- tricks.com/toe-dipping-into-view-transitions/)。状态管理呢？

> 信息很明确：框架不再是现代网页构建块的看门人。

信号（Signals）和响应式原语（reactive primitives）正直接进入标准讨论，框架普及的相同理念正在被重写进浏览器的 DNA 中。当你将所有这些与 Web Animations API、[CSS 容器查询](https://www.joshwcomeau.com/css/container-queries-introduction/) 以及性能 API 的稳步发展结合起来时，Web 平台开始感觉不再像一个半成品，而更像一个一流的操作系统。

这并非理论。主要的应用程序已经开始依赖这些原生功能，从而减少了打包大小和维护债务。信息很明确：框架不再是现代网页构建块的看门人。

## 为什么框架仍不会消失

声称框架已走到尽头是偷懒的说法。它们仍然解决着难题，尤其是在开发者人体工程学、大型团队扩展以及有主见的架构方面。

框架提供了约定，而这些约定节省了代码审查中数小时的争论。标准，尽管取得了所有进展，但被设计为灵活和最小化的——它们很少规定如何实际组织你的代码。

考虑一下 React 的生态系统：库、工具、状态管理约定及其庞大的开发者基础。即使 [浏览器提供了与 Hooks 或 Context 等价的功能](https://react.dev/learn/reusing-logic-with-custom-hooks)，单纯的熟悉感也让 React 具有粘性。Angular 在企业中依然蓬勃发展，因为它是一个完整的“电池全包”解决方案。而像 Svelte 或 SolidJS 这样的新框架则不断在人体工程学上创新，而非仅仅与标准实现原始的功能对等。

> 真正的转变并非框架的消失。相反，是框架被迫为自身的存在寻找理由。

十年前，你需要一个框架来构建一个严肃的应用程序。今天，如果你想要严格的约定、生态系统锁定，或者你的团队重视某些人体工程学特性，你才需要一个框架。这是一个根本性的区别：[框架正在从必需品转向偏好](https://www.repindia.com/blog/why-framework-choice-can-make-or-break-your-web-project/)。

## 性能之争：原生 vs. 框架

多年来，框架都以网页过于混乱为借口，声称性能上的权衡是值得的。开发者容忍臃肿的捆绑包、hydration（水合）问题和运行时 hack，因为开发者体验似乎值得。现在，这个论点变得站不住脚了。

原生解决方案通常优于框架的等价物。原因很简单：

* 自定义元素 [渲染速度快于许多虚拟 DOM 抽象](https://news.ycombinator.com/item?id=31577389)。
* CSS 容器查询消除了曾用脆弱 JavaScript 处理的一整类布局 hack。
* Navigation API 取代了笨重的客户端路由器，后者仅为模拟原生导航就需要数 KB 的代码。

更残酷的是对性能敏感环境的影响。移动优先应用、新兴市场连接和边缘计算都要求效率。[一个臃肿着各种依赖的 React SPA](https://programmers.io/blog/react-single-page-application/)，在一个即时加载、流畅运行的精简、基于标准的应用程序面前显得愚蠢。

浏览器厂商几乎是在挑战开发者，要求他们 [停止交付数兆字节的 JavaScript](https://thenewstack.io/introduction-to-javascript/)，转而使用已内置的工具。在这种背景下，框架看起来更像是性能负担，而非生产力工具。

## 开发者心智份额的政治博弈

这场斗争并非纯粹的技术之争——它关乎政治。框架拥有庞大的营销机器，背后有既得利益的公司的支持。Meta 支持 React，因为它是其帝国的基石。

谷歌 [支持 Angular，因为它将开发者绑定到其生态系统](https://thenewstack.io/google-angular-lead-sees-convergence-in-javascript-frameworks/)。相比之下，标准是缓慢推进的委员会和工作组。它们缺乏框架赖以生存的品牌效应和炒作周期。

但情况正在发生变化：浏览器厂商越来越意识到，不能允许框架永远主导网络的发展方向。

> 正在设计的标准旨在直接与框架功能竞争，而不是落后于它们。

正在设计的标准旨在直接与框架功能竞争，而不是落后于它们。而 [Open Web Components 等社区的崛起](https://developer.mozilla.org/en-US/docs/Web/API/Web_components) 表明，人们渴望在没有企业把关者的情况下进行协作。

尽管如此，文化惯性确实存在。大学教授 React，训练营推广 Angular，招聘信息用框架特有的语言编写。标准存在公关问题。

它们需要布道者，愿意向开发者展示现代平台足够强大，无需额外臃肿的层面。在此之前，即使框架的技术护城河正在缩小，它们仍将凭借纯粹的心智份额而得以维持。

## 最终思考

框架曾将网页从自身的无能中拯救出来。如今，它们开始看起来像浏览器现在主办的派对上的中间人。如果你仍然像浏览器无法处理一样编写代码，那么你正在忽略前端开发二十年来最重要的转变。

框架不会明天就消失，[但它们的统治地位已在逐步瓦解](https://thenewstack.io/javascript-framework-reality-check-whats-actually-working/)。标准运动正处于几十年来最强劲的时期，浏览器正在一块一块地蚕食框架的“蛋糕”。

盲目依恋框架的开发者，面临着交付臃肿、过时应用的风险，而网络的其他部分正在加速前进。信息很简单：是时候再次认真对待浏览器了。