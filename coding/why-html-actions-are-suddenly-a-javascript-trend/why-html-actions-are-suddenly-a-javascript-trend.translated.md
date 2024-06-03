# 为什么 HTML 操作突然成为 JavaScript 趋势

![HTML 操作突然成为 JavaScript 趋势的特色图片](https://cdn.thenewstack.io/media/2024/05/5a2fbc74-html-actions-1024x683.jpg)

操作并不新鲜。但它们正在复兴——如果你愿意的话，可以称之为——在 JavaScript 前端世界中。

在本月早些时候从拉斯维加斯现场直播的 React 大会上，[React 编译器和 React 19](https://thenewstack.io/meta-releases-open-source-react-compiler/) 成为焦点。但在演讲中隐藏着关于 React Action 的讨论。上周，Astro 宣布了对操作的支持，[Astro 前端开发人员 Ben Holmes](https://www.linkedin.com/in/bholmesdev/) 在 Twitter 上表示，这与 React Actions 类似](https://x.com/BHolmesDev/status/1793346886906036568)。

“这是我们在 [Astro](https://thenewstack.io/astros-journey-from-static-site-generator-to-next-js-rival/) 中定义 [RPC 端点](https://www.ankr.com/blog/what-are-rpc-nodes-and-endpoints-the-complete-guide-2023/) 的方式，”Holmes 说。它采用了服务器操作的基础知识，并添加了错误处理和输入验证功能。”

[Andrew Clark](https://www.linkedin.com/in/andrew-clark-83b9857a/) 指出，操作已经存在一段时间了，他是 [Vercel](https://thenewstack.io/vercel-creating-new-ai-framework-also-rust-and-adobe-updates/) 软件工程师和 React 核心贡献者，在 React 大会上。

“操作是一种一流的模式，用于在响应用户输入时异步更新应用程序中的数据，”Clark 说。“作为一种通用模式，操作并不是 React 的发明。它们已经成为 Web 平台的一部分几十年了。事实上，在 HTML 表单操作中，操作最早是在 1900 年代引入到 Web 中的。”

哎哟。是的，他说 1900 年代——就像牛仔在狂野的西部引入它们一样。对于你们这些历史学家来说，那是在 JavaScript 甚至还没有创建之前。

HTML 表单操作是一种向网页添加交互性的方式。在经典的 HTML 表单中，开发人员通过将 URL 传递给操作属性来指定服务器端点，Clark 解释说。当用户提交表单时，数据将发送到服务器，服务器将响应一个新的 HTML 页面。

“提交表单，加载页面，提交表单，加载页面，很简单，对吧？这个模型的优点是你可以用它来构建几乎任何东西，”他说。

然而，自 JavaScript 上线以来，操作就没有被广泛使用。

“如今，一个 Web [开发人员可以在其整个职业生涯中](https://thenewstack.io/the-future-of-developer-careers/) 都不会使用此 API，”他说。“发生的事情是，随着 JavaScript 的引入——我们都喜欢 JavaScript——最终有可能构建客户端密集型 Web 应用程序，这些应用程序提供了比行为仅限于服务器的应用程序更丰富、更具交互性的体验。”

用户期望也发生了变化。他说，他们希望与应用程序交互时获得即时反馈，因此他们不想每次都等待一个全新的 HTML 文档。用户希望应用程序记住他们的当前状态，以便在执行操作时不会丢失滚动位置或文本输入。

“换句话说，用户期望的不仅仅是如果没有至少一些客户端交互就无法实现的目标，”他说。“客户端事件处理程序有一些好处。它们可用于对用户输入实施即时丰富的反馈，并且可以将客户端和服务器行为组合在一起。”

但仅使用 [JavaScript](https://thenewstack.io/top-5-cutting-edge-javascript-techniques/) 的方法也有一些缺点，例如：难以管理本地状态。他说，实现异步性也很困难，而且经常会导致错误。此外，由于事件处理程序依赖于 JavaScript，因此在代码加载并运行之前，UI 不会交互，与原始 HTML 相比，这很慢，并且会导致交互中断。这使得人们很容易恢复到纯 HTML 操作，因为应用程序在 HTML 呈现后立即交互。

“我们不应该忘记我们最初放弃操作的原因，”他说。“它们几乎没有提供对用户输入的即时反馈。你基本上只能使用浏览器库存控件为你提供的任何东西。而且很难添加额外的客户端交互，因为它是一种完全不同的编程模型。”

Clark 说，React 的存在就是为了解决这种难题。

## 所以……等等。

*为什么* React 要添加操作？

本月，React Actions 从金丝雀频道（自去年夏天以来一直存在）进入 React。

“你可能在服务器操作功能的上下文中听说过它们，这些功能在 Next.js 等服务器组件框架中可用，但操作并不仅限于 [服务器组件](https://thenewstack.io/react-server-components-in-a-nutshell/) 框架，”Clark 说。
### React Actions: A Paradigm Shift in React Development

React Actions are an evolution of two existing APIs, he said. The first is React transitions, which are used to update state without blocking user input. Actions build on transitions by adding support for asynchronous functions. The second is the HTML form API.

“Using React Actions is a lot like using [HTML form actions](https://www.w3schools.com/tags/att_form_action.asp), except instead of passing a URL to the action attribute, you now pass a function,” he said. “In the most basic example, that’s all you have to do — pass a function to the action attribute, and when the user submits the form, the action will be triggered. By using an action function instead of a URL, you can define the behavior of the action directly within your component.”

Clark said that thanks in large part to the Remix and React frameworks, “there has been a resurgence of action-inspired APIs within the JavaScript community.” He added that actions have been reintroduced as a pattern for server-client communication.

“Today, it seems like almost every JavaScript web framework has its own take on the action pattern,” he said. “And for good reason. We believe that actions are a great way to build applications, and they fit perfectly into the React programming model.”

That begs the question, he noted: If action-based APIs already exist in React frameworks, why [build them into React](https://thenewstack.io/learn-react-build-a-working-file-tree-and-manage-state/)?

The React team believes that by integrating actions into React, they can do more without compromising React’s composability, by enabling features such as:

- Streaming SSR
- Selective hydration
- Suspense and transitions
“There’s nothing special about action functions. They’re regular functions: You can compose them, you can write abstractions for them, just like you would for any other function. You can define actions on the client, or if you’re using the Server Components framework, you can define actions on the server using server directives and have direct access to your data layer,” he said. “Every page, every component, every whatever can have multiple actions, and you can swap out actions at runtime.”

He added that this level of “maximum composability” is possible because the React team has “integrated actions into every layer of React, from the client runtime to the streaming SSR renderer to the Server Components data format, all of which work together to provide a seamless experience.”

“Our goal is to provide a core primitive that meta frameworks like [Remix](https://thenewstack.io/remix-react-router-merge-jetbrains-ide-for-test-automation/), [Next](https://thenewstack.io/remix-takes-on-next-js-in-battle-of-the-react-frameworks/), and [Redwood](https://thenewstack.io/redwood-framework-all-in-on-react-server-components/) can build on top of, just like they currently build on top of features like streaming and suspense,” he said.

## Benefits of React Actions

Actions in React look a lot like HTML actions, but they also resemble event handlers, such as *onsubmit* or *unclick*, Clark said.

“Despite the surface-level similarities, actions have some key capabilities that set them apart from regular event handlers,” he continued. “One such capability is support for progressive enhancement. Form actions in React are interactive before hydration occurs. Believe it or not, this is true for all actions, not just actions defined on the server.”

If a user interacts with a client action before hydration is complete, React will memoize the action and replay it immediately after streaming, he said. If a user interacts with a server action, the action can trigger a regular browser navigation immediately, without [hydration or JavaScript](https://thenewstack.io/javascript-hydration-is-a-workaround-not-a-solution/).

Actions can also handle asynchronous logic, he added.

“React Actions have built-in support for UX patterns like optimistic UI and error handling,” he said. “Actions make these complex UX patterns incredibly easy by deeply integrating with React features like Suspense and transitions. They’re easy to compose. They have a unified client and server API. They’re interactive before hydration, and you can implement advanced UX with just a few lines of code.”

[
YOUTUBE.COM/THENEWSTACK
Stay on top of the fast-changing world of technology. Subscribe to our YouTube channel to stream all of our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)