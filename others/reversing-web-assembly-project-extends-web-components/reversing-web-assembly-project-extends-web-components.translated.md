# 新的 Wasm 项目将 Web 组件引入后端语言

![用于：新的 Wasm 项目将 Web 组件引入后端语言的特色图片](https://cdn.thenewstack.io/media/2024/04/f193e4c1-hal-gatewood-werqau9ta-a-unsplash-1-1024x683.jpg)

WebAssembly 基本上允许非前端语言（如 Rust 或 Python）在 Web 浏览器中运行。但 Web 开发人员和 [Enhance](https://enhance.dev/) 维护者 [Ryan Bethel](https://github.com/ryanbethel) 思考：你能否逆转这种范例，并使用 Wasm 在 Python 或 Rust 环境中运行 Web 组件？

事实证明，答案是肯定的。经过一些微调，这是可能的。Bethel 和 Enhance 团队解决了这个问题，并于 4 月 8 日发布了 [Enhance Wasm](https://enhance.dev/wasm)。

[Begin](https://begin.com/) 的首席执行官 [Brian LeRoux](https://www.linkedin.com/in/brianleroux/) 解释说：“为了让 [Wasm 生态系统](https://thenewstack.io/wasmcon-2023-a-conversation-about-the-future-of-webassembly/) 发挥作用，Rust、Python、Java 和所有这些其他运行时也可以执行 Wasm。”他创建了 Enhance，本身也是一名 Web 开发人员。“因此，我们现在可以反其道而行之。我们可以获取浏览器代码，并在 [Java](https://thenewstack.io/why-wasm-wins-where-java-applets-failed/) 或 [Python](https://thenewstack.io/python-and-webassembly-elevating-performance-for-web-apps/) 或 [PHP](https://thenewstack.io/php-has-survived-for-26-years-because-it-keeps-evolving/) 或 [Rust](https://thenewstack.io/rust-gets-security-wasi-0-2-support-productivity-boost/) 或其他语言中运行它。我们正在使用 Enhance 解释器，它根据 Web 组件定义生成 HTML，并且我们正在将其编译成 Wasm。”

LeRoux 解释说，其影响范围从解决 Web 问题（如在不同语言的数字属性中重复使用标题），到可能创建一种全球通用设计，其中按钮、下拉菜单和其他常见设计元素可以作为组件在语言之间重复使用。

## Web 开发回到浏览器

要了解其工作原理，了解 [Enhance](https://enhance.dev/why-enhance)（一个开源全栈 HTML 框架）会有所帮助。要了解 Enhance 的重要性，考虑 [JavaScript](https://thenewstack.io/top-5-underutilized-javascript-features/) 的广泛采用会有所帮助。

LeRoux 指出，十年前，大约有 2000 万程序员——现在 [GitHub](https://thenewstack.io/github-developer-productivity-at-30-billion-messages-per-day/) 将这一数字定为 1 亿开发人员。他认为，他们中的大多数人不是通过学习 Rust 等较低级别的编程语言成为编码人员的，而是通过学习 HTML、CSS 和 JavaScript（尤其是 JavaScript）——根据 [Stack Overflow 的开发者调查](https://survey.stackoverflow.co/2022/#technology)，JavaScript 已连续 11 年成为最常用的编程语言。

LeRoux 说：“我们的假设是 [软件开发人员中] 最大的一部分是前端开发人员，坦率地说，他们学到的很多东西也已经过时十年了。”“如今，关于我们如何为前端构建的许多假设都被浏览器否定了。”

但 LeRoux 指出，浏览器只会不断改进。他说，尽管如此，当今围绕前端的许多假设都是关于转换 JavaScript，以便它可以更现代化，并且具有“组件和模块等事物的更漂亮的语法”。

LeRoux 继续说道：“好消息是：浏览器现在都内置了组件和模块。”“因此，需要一个框架来实现这一点——实际上，用一个云术语来说——是无差别的、繁重的任务。”

## React 是否创建了太多代码？

JavaScript，特别是 [React](https://thenewstack.io/react-panel-frontend-should-embrace-react-server-components/)，为聚会带来了很多代码，以复制浏览器已经可以创建的组件。他说，这会降低用户的体验速度。

他说：“Enhance 的理念是回到为平台编写代码，为浏览器编写较低级别的代码。”“现在，这并不是说浏览器完美无缺。它到处都是纸张剪切，而且大规模使用 Web 组件等内容存在困难，而且你到处都能听到这些内容。这不仅仅是 FUD。很多人抱怨用户体验的状态，开发人员使用较低级别的浏览器基元进行工作的体验，并且为此付出了很多努力；因此，Enhance 的总体目标是让使用 Web 组件进行构建变得有趣。”

他说，当开发人员编写 Web 组件时，他们倾向于编写扩展 HTML 元素的 JavaScript。但是，页面上的大多数元素实际上都不是交互式的。
“他说：“给定网页上的元素，可能 90% 不会监听 JavaScript，不会提交表单，不会解释滚动事件或拦截、表单提交或点击或其他任何内容。”“因此，我们希望服务器渲染 Web 组件，并且我们不一定希望运行客户端 JavaScript。”

Enhance 为开发人员提供了一个包含自定义元素的页面，他说。虽然开发人员可以使用 JavaScript，但他们可能不需要它，LeRoux 补充道。

“事实上，你可能不想要它，因为做所有这些额外工作会让你的性能大打折扣，”他补充道。

一个普通的网站有 1 到 2 MB 的 JavaScript。LeRoux 指出了 Enhance 的主页，尽管有丰富的动画，但只有 4 到 5 KB 的 JavaScript，并且依赖于

[HTML](https://thenewstack.io/html-markup-tips-for-developing-accessible-websites/) 和 [CSS](https://thenewstack.io/css-frameworks-in-vogue-but-dont-forget-style-fundamentals/)。

“我们的假设是 [即] 软件开发人员中最大的新群体是前端，坦率地说，他们学到的很多东西也已经过时了十年。”——Brian LeRoux，Begin 的 Web 开发人员兼首席执行官

对于那些被告知构建网站需要 React JavaScript 的人来说，这是一个激进的消息。人们使用 Enhance 面临的挑战之一是，例如，React 允许你将复杂对象传递给属性。HTML 不允许这样做；属性仅用于传递样式，而不是复杂对象。他说，这种事情经常让 React 开发人员感到惊讶。

“React 掩盖了浏览器的工作原理，它创造了一个令人毛骨悚然的山谷，这对很多人来说实际上是一种非常糟糕的学习，”他说。“如果你是一名 Web 开发人员，并且已经使用 React 构建网站长达十年，那么意识到自己不知道浏览器的运作方式会让你感到有点扫兴，这可能会令人失望和沮丧。因此，他们经历了各种情绪，从一开始的愤怒，然后是绝望，然后是接受并继续前进。”

![Enhance 的代码](https://cdn.thenewstack.io/media/2024/04/bef3721f-enhance-code.png)

Begin 的首席执行官兼开发人员 Brian LeRoux 展示了 Enhance 网站使用的代码。

随着浏览器的进步，使用 JavaScript 的很多原因已经消失，他补充道。

LeRoux 说：“我们可以非常高效地使用 Web 的基础知识。”“我们现在拥有自动更新、超级向后兼容的 Web 浏览器，它可以像加载今天的网站一样加载 90 年代的网站，我们甚至不必再告诉它更新，而且我们不再像以前那样充分利用它。”

他说，Enhance 适用于那些超级注重性能并希望构建持久网站的人。

“我觉得使用现代

[JavaScript 框架](https://thenewstack.io/jamstack-panel-multiple-javascript-frameworks-are-a-good-thing/)，它们会经常崩溃，而且非常脆弱，每年都会有一场新的大型会议，他们会在会上宣布所有重大更改，每个人都欢呼雀跃；而我就像，好吧，你是在为未计划的工作欢呼雀跃 […] 以提供一个网页，”他说。“因此，业界肯定需要就此主题进行一些灵魂拷问。”

## 创建 Enhance Wasm

Bethel 阅读了 Shopify 使用

[Qwik.js](https://thenewstack.io/javascript-on-demand-how-qwik-differs-from-react-hydration/) 的实验，这是一个旨在小巧的新型 JavaScript 运行时。Shopify 假设他们可以采用解释器，使用 Wasm 编译它，将其与一些 JavaScript 捆绑在一起，并在支持 Wasm 的任何运行时中运行该 JavaScript。Bethel 和 Enhance 团队希望看看他们是否可以反其道而行之，在其他语言中运行 Web 组件。

他解释说，该团队采用了 Enhance 解释器，该解释器根据

[Web 组件](https://thenewstack.io/introduction-to-web-components-and-how-to-start-using-them/) 定义生成 HTML，并将其编译成 Wasm。他说，大约需要十个原型才能获得一个效果良好的解决方案——秘诀来自一家名为 [Extism](https://extism.org/) 的初创公司，这是一个用于使用 WebAssembly 构建的跨语言框架。

“Extism 使我们能够真正快速地采用此代码并在所有这些不同平台上运行它，”他说。“Wasmtime [WebAssembly 的运行时]，我们无法在 Java 中使用，还有另一个我们无法在 PHP 上使用，除非我们进行本机外壳，但现在我们可以在任何地方使用它。这个想法是编写一组 Web 组件，然后可以在任何后端运行它们。”

该团队在

[4 月 8 日的博客文章](https://begin.com/blog/posts/2024-04-08-introducing-enhance-wasm) 中介绍了 Enhance，称其为“前端开发的飞跃时刻”。
“团队写道，“[服务器端渲染](https://thenewstack.io/spas-and-react-you-dont-always-need-server-side-rendering/) 是个性化 Web 应用程序的关键要求。”“优先考虑 Web 标准的稳定性、性能和可访问性的组织在各种后端运行时中运行工作负载。现在，我们可以构建跨越运行时鸿沟的浏览器原生 Web 界面。”

Enhance Wasm 是开源的，它在启动时支持：

- [Node](https://thenewstack.io/why-viable-uses-next-js-and-node-js-for-ai-applications/)
- [Deno](https://thenewstack.io/with-additional-funding-deno-sets-out-to-challenge-node-js/)
- Python
- Ruby
- PHP
- Java
- C#
- Rust
- [Go](https://thenewstack.io/go-language-riding-high-with-devs-but-has-a-few-challenges/)

## Enhance Wasm 的用例

在发布后，Enhance 立即被开发人员用于重新调整 Web 属性中的标题样式。LeRoux 说，它在通过收购而发展壮大并可能拥有四个或五个完全独立的不同技术部门的大公司中特别有用。例如，他的妻子在大型科技公司 [LaunchDarkly](https://launchdarkly.com/?utm_content=inline+mention) 工作，该公司拥有来自收购的初创公司的多个系统。他说，在这些系统中维护一个设计系统是一件很头疼的事情，因为它们有一个 PHP 博客和一个 Go 应用程序，并且在不同的数字属性中实施了不同的技术。

他说：“如果你必须为每个运行时重新实现的东西维护一个设计系统。”“使用 Enhance Wasm，我们可以使用 Web 组件完成所有这些定义，并从一组定义中在所有这些属性中运行它们，这就是它引人注目的原因。”

该团队还与著名设计师 [Brad Frost](https://bradfrost.com/) 进行了交谈，他提出了一个类似于 Google 的 Material 或 Salesforce 的 Lightning 的全球设计系统，但目的是让每个人都能使用。

Enhance 团队还加入了 W3C [Web 组件工作组](https://www.w3.org/community/webcomponents/) 和 [Open UI 组](https://open-ui.org/)。

Le Roux 说：“最终目标是 [将] 很多东西放入浏览器本身。”“我们现在不必为按钮共享这些设计系统——这些应该已经内置到平台中……选项卡、轮播或手风琴或其他任何东西，每个网站都有这些东西。能够拥有一组在任何地方都能工作的此类组件，理想情况下无需客户端 JavaScript，这会很好。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。