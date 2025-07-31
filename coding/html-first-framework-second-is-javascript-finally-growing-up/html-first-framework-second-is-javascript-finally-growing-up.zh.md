长期以来，[JavaScript 一直是现代网络的英雄](https://thenewstack.io/javascript-framework-reality-check-whats-actually-working/)，它突然出现并在浏览器中构建全面的应用程序。 但最近，[一场悄无声息的叛乱正在酝酿之中](https://thenewstack.io/why-react-is-no-longer-the-undisputed-champion-of-javascript/)。 开发人员正在回归[HTML优先的方法](https://thenewstack.io/how-astro-and-its-server-islands-compare-to-react-frameworks/)——更快、更简单、更具弹性。

越来越多的团队不再默认使用框架，而是[再次将 HTML 和 CSS 视为一等公民](https://news.ycombinator.com/item?id=34618628)，仅在 JavaScript 真正增强体验时才依赖它。 这不是怀旧，而是一种经过计算的修正。 现在真正的问题是：这种转变是 JavaScript 成熟的标志，还是更扎实的 Web 开发理念的出现？

## 框架后遗症

10 多年来，Web 开发一直深陷 JavaScript 优先的思维方式。 随着单页应用程序 (SPA) 的兴起，JavaScript 不再只是一种脚本语言，而是[成为整个前端的基础](https://thenewstack.io/30-years-of-javascript-10-milestones-that-changed-the-web/)——以至于 HTML 和 CSS 通常由 JavaScript 生成、由 JavaScript 操作，甚至完全被 JavaScript 抽象所取代。 我们告诉自己这是一个进步，开发者体验证明了这种权衡是合理的。

在某些方面，确实如此。 SPA 让我们构建动态的交互式界面。 像 React 这样的框架为我们提供了比静态 HTML 模板强大得多的组件模型。 但钟摆摆动得太远了。 应用程序在没有 JavaScript 的情况下开始崩溃。 页面在完成 hydration 之前呈现空白。 内容的整个部分[无法被爬虫或屏幕阅读器访问](https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript)。 曾经旨在增强用户体验的东西已经变成了一种可能会破坏它的依赖。

> 潜在的问题变得越来越难以忽视：我们是在解决正确的问题，还是仅仅在构建更复杂的解决方案？

开发人员变成了运维工程师——与构建管道、webpack 配置、打包器、tree-shaking 和 hydration 策略作斗争。 曾经是一个简单的网站，现在却变成了一台基于 JS 的机器，拥有数十个移动部件。 结果呢？ 性能变慢，学习曲线变陡峭，并且 Web 越来越多地[迎合开发人员而不是用户](https://thenewstack.io/from-react-to-html-first-microsoft-edge-debuts-webui-2-0/)。 潜在的问题变得越来越难以忽视：我们是在解决正确的问题，还是仅仅在构建更复杂的解决方案？

好吧，除了像 Elixir 这样的[创新解决方案](https://thenewstack.io/elixir-an-alternative-to-javascript-based-web-development/)之外，许多开发人员现在正在回归可靠的旧方法：HTML。

## HTML 优先工具的兴起

像 [Astro](https://thenewstack.io/astros-journey-from-static-site-generator-to-next-js-rival/)、[HTMX](https://thenewstack.io/htmx-html-approach-to-interactivity-in-a-javascript-world/)、[Enhance](https://enhance.dev/) 和 [MarkoJS](https://github.com/marko-js/marko) 这样的新工具和理念正在颠覆传统的前端范例。 他们不是从框架开始并在其中加入 HTML，而是从干净、语义化的 HTML 开始，并通过 JavaScript 逐步增强它。 重点是速度、可访问性和简单性。

以 Astro 为例。 默认情况下，它[不附带任何 JavaScript](https://thenewstack.io/how-to-build-and-deploy-a-basic-site-using-astro-and-netlify/)，让开发人员仅在需要时才选择加入。 你主要编写 HTML 和 CSS，并且仅在交互性需要时才在客户端 hydrate 组件。 这不是回归静态站点，而是一种更深思熟虑的、性能优先的架构。

> Web 的基础语言 HTML 仍然值得占据首位。

同时，HTMX 允许你通过网络发送 HTML，并使用属性以声明方式附加行为。 它优雅、简洁，并且对于构建交互式应用程序而无需启动完整的 JS 框架非常有效。

这些工具不仅仅代表新的选择。 它们标志着更深层次的文化转变，一种对 Web 的基础语言 HTML 仍然值得占据首位的认识。

## JavaScript 的成熟时刻

JavaScript 没有消失，而是在不断发展。 它的角色正在从“一直渲染一切”重新定义为“在重要的地方增强”。 在许多方面，这都是成熟的标志。 JS 没有被抛弃，只是（终于）被要求表现得像个成年人。

例如，在 Next.js 和 SvelteKit 等工具的推动下，[服务器端渲染 (SSR) 已经卷土重来](https://thenewstack.io/spas-and-react-you-dont-always-need-server-side-rendering/)。 即使是传统的 JS 繁重的框架也在适应：React 服务器组件、[Remix 对服务器的强调](https://thenewstack.io/remix-3-and-the-end-of-react-centric-architectures/) 和 [Vue 更精简的生态系统](https://thenewstack.io/want-out-of-react-complexity-try-vues-progressive-framework/) 反映了更广泛的控制客户端过剩的愿望。

> HTML 用于内容，CSS 用于样式，JavaScript 用于交互（仅在必要时）。

随着人们越来越关注[分布式拒绝服务 (DDoS) 攻击](https://www.imperva.com/learn/ddos/anti-ddos-protection/)，现代 JavaScript 生态系统正在拥抱 SSR 和[边缘计算](https://thenewstack.io/why-devs-must-rethink-their-role-in-modern-cdns-and-the-edge/)，以减少攻击面，分散工作负载瓶颈并减轻客户端漏洞。

正在改变的是默认的思维方式。 鼓励开发人员首先使用本机浏览器功能：HTML 用于内容，CSS 用于样式，JavaScript 用于交互（仅在必要时）。 这种进步与许多现代开发人员在框架热潮中忽略的渐进增强和可访问性的精神相呼应。

## 为什么这种转变很重要

这不仅仅是关于开发人员偏好的书呆子式辩论。 这是一个直接影响用户的对话。 HTML 优先的设计加载速度更快，降级效果更好，并且与搜索引擎和辅助技术配合得更好。 站点变得更具弹性、更易于维护，并且通常更易于构建。

同样，你还必须考虑[核心 Web 指标的兴起](https://developers.google.com/search/docs/appearance/core-web-vitals)作为排名因素。 或者移动优先性能预算的普遍存在。 评判开发人员的标准不再仅仅是功能，而是这些功能到达和运行的效率。 HTML 优先的方法与这种现实完美契合。

它还降低了入门门槛。 新开发人员可以学习 Web 的构建块，而不会被 webpack 配置或 JSX 语法树所淹没。 通过这种方式，HTML 优先不仅是性能上的胜利，[也是教学上的胜利](https://html-first.com/guidelines)。

### 但它能扩展吗？

自然而然的问题是，HTML 优先的架构是否可以支持复杂、动态的应用程序。 答案越来越像是肯定的。

像 Enhance 和 Qwik 这样的项目正在证明，渐进增强[可以与可扩展性共存](https://outshift.cisco.com/blog/qwik-vs-nextjs)。 他们没有重新发明轮子，而是使用了平台原生功能，如 Web Components 和 DOM 本身。 并且他们这样做，同时允许延迟加载、hydration 和动态更新，只是没有传统框架的 all-or-nothing 方法。

> 当你停止将浏览器视为一个愚蠢的画布并开始利用其本机行为时，你可以走得很远。

即使是像 Google、Netlify 和 Shopify 这样的大型公司的团队也在探索 HTML 优先或[基于岛屿的架构](https://thenewstack.io/how-astro-and-its-server-islands-compare-to-react-frameworks/)，以驯服他们不断增长的前端代码库。 事实证明，当你停止将浏览器视为一个愚蠢的画布并开始利用其本机行为时，你可以走得很远。

复杂性并没有消失。 但它变得更加审慎、更加模块化，并且与单个框架的生命周期或状态模型的相关性更小。 这很重要。

## 开发人员需要重新学习什么

如果你在过去五年中一直以 props、状态和客户端路由来思考，那么 HTML 优先的转变可能会让人感到不适应。 但这并不是要放弃你辛辛苦苦学来的技能。 而是要重新发现 Web 的最初意图。

因此，开发人员现在需要知道如何：

* 编写语义化、可访问的 HTML，以便清楚地向浏览器和辅助技术传达结构和意图。
* 拥抱 [HTTP 谓词，如 GET 和 POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)，并依靠服务器呈现的响应来处理状态转换，而不是将所有内容都转移到客户端。
* 使用 CSS 功能，如用于动画的过渡、用于响应式布局的媒体查询和用于组件级响应式的容器查询，在原生解决方案足够时避免使用 JavaScript。
*围绕表单和可导航 URL 设计交互，从而实现更好的回退、可共享性并[降低前端复杂性](https://www.interaction-design.org/literature/article/design-patterns-for-fluid-navigation-how-to-use-inline-linking?srsltid=AfmBOor-uQNI44CcY-xlf4Cz_q9rOXccux7F0U-qDwGo08EGj2ui53HV)，而不是仅仅依赖封装的影子 DOM 或通过 API 进行路由。

这并非倒退。 而是重新发现从未停止工作的工具。 HTML 优先的理念迫使开发人员从一开始就考虑架构、交付和性能。 它鼓励意图性。

## 未来是分层的，而不是堆叠的

框架并没有消亡，它们正在发展。 前端的未来不会回归到纯 HTML，而是一种分层的方法，其中 HTML 是基石，而不是事后才考虑的。 你仍然可以使用 React、Svelte 或 Vue，但作为增强功能，而不是基础。

> 我们可能正在目睹 JavaScript 期待已久的成年期。

这就是 JavaScript 可以做的最成熟的事情：学习何时领先，何时跟随。 让 HTML 构建你的页面，让 CSS 绘制它，让 JavaScript 将它变为现实——小心、精确，并且仅在需要时。

我们可能正在目睹 JavaScript 期待已久的成年期。 它不浮华，不教条，也不再试图控制堆栈。 它只是想融入其中。

说实话？ 这可能是前端多年来发生的最令人兴奋的事情。