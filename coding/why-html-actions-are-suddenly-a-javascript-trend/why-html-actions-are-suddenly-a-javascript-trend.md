
<!--
title: 为什么HTML Action突然成为JavaScript的趋势
cover: ./cover.jpg
-->

Astro 做到了。React 全力以赴。就像复古的妈妈牛仔裤，HTML action 又从 20 世纪 90 年代回来了。以下是它们风靡一时的原因。

> 译自 [Why HTML Actions Are Suddenly a JavaScript Trend](https://thenewstack.io/why-html-actions-are-suddenly-a-javascript-trend/)，作者 Loraine Lawson。

Action 并不新鲜。但它们正在复兴——如果你愿意的话，可以称之为——在 JavaScript 前端世界中。

在本月早些时候从拉斯维加斯现场直播的 React 大会上，[React 编译器和 React 19](https://thenewstack.io/meta-releases-open-source-react-compiler/) 成为焦点。但在演讲中隐藏着关于 React Action 的讨论。上周，Astro 宣布了对 action 的支持，[Astro 前端开发人员 Ben Holmes](https://www.linkedin.com/in/bholmesdev/) 在 Twitter 上表示，这与 [React Actions 类似](https://x.com/BHolmesDev/status/1793346886906036568)。

“这是我们在 [Astro](https://thenewstack.io/astros-journey-from-static-site-generator-to-next-js-rival/) 中定义 [RPC 端点](https://www.ankr.com/blog/what-are-rpc-nodes-and-endpoints-the-complete-guide-2023/) 的方式，”Holmes 说。它采用了服务器 action 的基础知识，并添加了错误处理和输入验证功能。”

[Andrew Clark](https://www.linkedin.com/in/andrew-clark-83b9857a/) 指出， Action 已经存在一段时间了，他是 [Vercel](https://thenewstack.io/vercel-creating-new-ai-framework-also-rust-and-adobe-updates/) 软件工程师和 React 核心贡献者，在 React 大会上。

“ action 是一种一流的模式，用于在响应用户输入时异步更新应用程序中的数据，”Clark 说。“作为一种通用模式， action 并不是 React 的发明。它们已经成为 Web 平台的一部分几十年了。事实上，在 HTML 表单 action 中， action 最早是在 1900 年代引入到 Web 中的。”

哎哟。是的，他说 1900 年代——就像牛仔在狂野的西部引入它们一样。对于你们这些历史学家来说，那是在 JavaScript 甚至还没有创建之前。

HTML 表单 action 是一种向网页添加交互性的方式。在经典的 HTML 表单中，开发人员通过将 URL 传递给 action 属性来指定服务器端点，Clark 解释说。当用户提交表单时，数据将发送到服务器，服务器将响应一个新的 HTML 页面。

“提交表单，加载页面，提交表单，加载页面，很简单，对吧？这个模型的优点是你可以用它来构建几乎任何东西，”他说。

然而，自 JavaScript 上线以来， action 就没有被广泛使用。

“如今，一个 Web [开发人员可以在其整个职业生涯中](https://thenewstack.io/the-future-of-developer-careers/) 都不会使用此 API，”他说。“发生的事情是，随着 JavaScript 的引入——我们都喜欢 JavaScript——最终有可能构建客户端密集型 Web 应用程序，这些应用程序提供了比行为仅限于服务器的应用程序更丰富、更具交互性的体验。”

用户期望也发生了变化。他说，他们希望与应用程序交互时获得即时反馈，因此他们不想每次都等待一个全新的 HTML 文档。用户希望应用程序记住他们的当前状态，以便在执行 action 时不会丢失滚动位置或文本输入。

“换句话说，用户期望的不仅仅是如果没有至少一些客户端交互就无法实现的目标，”他说。“客户端事件处理程序有一些好处。它们可用于对用户输入实施即时丰富的反馈，并且可以将客户端和服务器行为组合在一起。”

但仅使用 [JavaScript](https://thenewstack.io/top-5-cutting-edge-javascript-techniques/) 的方法也有一些缺点，例如：难以管理本地状态。他说，实现异步性也很困难，而且经常会导致错误。此外，由于事件处理程序依赖于 JavaScript，因此在代码加载并运行之前，UI 不会交互，与原始 HTML 相比，这很慢，并且会导致交互中断。这使得人们很容易恢复到纯 HTML  action ，因为应用程序在 HTML 呈现后立即交互。

“我们不应该忘记我们最初放弃 action 的原因，”他说。“它们几乎没有提供对用户输入的即时反馈。你基本上只能使用浏览器库存控件为你提供的任何东西。而且很难添加额外的客户端交互，因为它是一种完全不同的编程模型。”

Clark 说，React 的存在就是为了解决这种难题。

## 所以……等等，为什么 React 要添加 action ？

本月，React Actions 从金丝雀频道（自去年夏天以来一直存在）进入 React。

“你可能在服务器 action 功能的上下文中听说过它们，这些功能在 Next.js 等服务器组件框架中可用，但 action 并不仅限于 [服务器组件](https://thenewstack.io/react-server-components-in-a-nutshell/) 框架，”Clark 说。

React action 是两个现有 API 的发展，他说道。第一个是 react 过渡，用于更新状态而不阻塞用户输入。action 通过增加对异步函数的支持，构建在过渡之上。第二个是 HTML 表单 API。

“使用一个 React action 非常像使用 HTML 表单 action ，除了不将 URL 传递给 action 属性，你现在可以传递一个函数。”他说道。“在最基本的例子中，你所要做的就是将一个函数传递给 action 属性，当用户提交表单时，将触发 action 。通过使用 action 函数而不是 URL，你可以在组件内部直接定义 action 的行为。”

克拉克说，“由于 Remix 和 React 框架的功劳很大程度上”，所以 JavaScript 社区中“以 action 为灵感的 API 重新流行”。他补充说， action 作为服务器客户端通信模式已经被重新引入。

他说：“现在看来，似乎几乎每个 JavaScript Web 框架都会推出其自己版本的 action 模式”。“这有充分的理由。我们认为， action 是构建应用程序的好方法，它们完全符合 React 编程模型。”

他指出，这一点提出了一个问题：如果基于 action 的 API 在 React 框架中已经存在，为什么要将它们构建到 React 中？

React 团队认为，他们可以通过将 action 集成到 React 中，在不影响 Read 的可组合性的前提下实现更多 action ，这是通过以下功能实现的：

- 流式SSR
- 选择性服务端渲染
- 暂停和过渡

“Action 函数没有什么特别的。它们是常规函数：你可以把它们组合起来，你可以为它们编写抽象，就像你可以对任何其他函数那样，你可以在客户端上定义 action，或者如果你使用服务器组件框架，你可以通过使用服务器指令在服务器上定义 action 并直接访问你的数据层，”他说。“你可以在每个页面每个组件上执行任意次 action ，根据需要进行替换，你可以在运行时交换 action。” 

他补充说，这种最大程度的可组合性源自 React 团队集成了“从客户端运行时到流式渲染器，再到服务器组件数据格式， action 植入到 React 的每一层，相互协作以提供无缝体验”。 

“我们的目标是提供一个核心原语，像 Remix、Next 和 Redwood 这样的元框架可以基于其构建，就像它们现在基于流式处理和悬念等特性那样，”他说。

## React  action 为何如此出众

React 中的 action 看起来很像 HTML  action ，但它们看起来也类似于事件处理程序，例如 onsubmit 或 unclick，克拉克说道。

“尽管表面上看很相似，但 action 有一些重要的能力，让它们区别于常规的事件处理程序，”他继续说道。“其中一项这样的能力是对渐进增强的支持。在 React 中，窗体 action 在水化发生前就具有交互性。信不信由你，这不仅适用于所有 action ，也适用于并非在服务器上定义的 action 。

如果用户与客户端 action 交互，在它完成数据补全之前，React 会对该 action 进行提示，并立即在流化它时重播它，他说。如果用户与服务器 action 交互，该 action 会立即触发常规的浏览器导航，而无需[数据补全](https://thenewstack.io/javascript-hydration-is-a-workaround-not-a-solution/)或 JavaScript。

Action 还可以处理异步逻辑，他说。

“React action 对 UX 模式（例如乐观 UI 和错误处理）有内置支持，”他说。“ action 通过与 React 的暂停和过渡等功能深度集成，使得这些复杂的 UX 模式变得非常简单。它们可轻松组合。它们拥有统一的客户端和服务器 API。它们可在数据补全前进行交互，并且你只需几行代码即可实现高级的 UX。”