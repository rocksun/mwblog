Ripple，一个基于[TypeScript](https://thenewstack.io/typescript-5-9-brings-less-friction-more-features/)的新UI框架，如果不是由[Dominic Gannaway](https://github.com/trueadm)创建，可能会被视为又一个普通的框架。

Gannaway 创建了 [InfernoJS](https://www.infernojs.org/)，一个类似于 React 的快速 UI 库。他在 Meta 工作的六年中有三年在 [React](https://thenewstack.io/why-reacts-boring-maturity-is-actually-its-main-strength/) 核心团队工作。他曾是 [Vercel](https://thenewstack.io/next-js-in-chatgpt-vercel-brings-the-dynamic-web-to-ai-chat/) 和 Bloomberg 的软件工程师，现在是 [Attio](https://attio.com/)（一个AI原生客户关系管理（CRM）平台）的首席产品工程师。对了，他还为 [Svelte](https://thenewstack.io/svelte-adds-asynchronous-sync-inside-components/) 5 做出了贡献。

Ripple 尚处于早期开发阶段，尚未准备好投入生产，但它已在 JavaScript 圈中引起轰动。The New Stack 与 Gannaway 探讨了该框架以及他为何选择在[AI 已经冲击前端开发](https://thenewstack.io/how-ai-agents-are-悄悄 transforming-frontend-development/)时创建它。

## 原因：调试 AI 的开发者体验

事实证明，AI 和 [大型语言模型 (LLMs)](https://thenewstack.io/introduction-to-llms/) 是 Ripple 创建的部分原因。

“几年前我甚至不会尝试这个，但现在有了 AI 工具，这实际上是一个相当有趣的提议，”他说。“如果我们进入一个让 LLM 编写大量逻辑的世界，那么我们将进行更多的阅读，而阅读的将不会是我们自己的代码。它将是维护和查看 AI 生成的内容。”

他补充说，大多数工程师阅读和审查的代码量已经超过他们编写的代码量，并指出随着 LLM 生成更多代码，这种情况不太可能改变。

这也是他为该框架专注于开发者体验而非速度的原因。他说，尽管它很快，但他首先专注于创造“令人兴奋的调试体验”，目标是让用户更容易找出问题发生的原因。

“Ripple 总是非常快速，所以我们主要关注的是开发者体验：代码更简洁、更易读、更符合人体工程学，拥有一个你不会与之抗争的响应式系统，拥有一组非常小的 [API](https://thenewstack.io/its-time-to-build-apis-for-ai-not-just-for-developers/)，API 越少意味着你可以更快地记住它们，然后更好地组合它们，”他解释道。

## Ripple 是一种语言

在框架方面，Ripple 在许多关键方面有所不同。首先，Gannaway 说，Ripple 不仅仅是一个框架，它是一种语言。

“为了成为自己的语言，但又要让来自 JavaScript 和 TypeScript 的人足够熟悉，Ripple 需要是其中一种的超集，”他解释道。

他选择将其设为 TypeScript 的超集，因为 TypeScript 包含了类型。

“这是一个大项目，因为它不仅仅是一个框架；这听起来很奇怪，但你必须构建一个语言服务器，才能让你的 TypeScript 相关功能工作，”他说。“你必须让你的语法高亮工作。你必须让 Prettier 和 ESLint 以及所有这些生态系统工具都工作。”

> “为了成为自己的语言，但又要让来自 JavaScript 和 TypeScript 的人足够熟悉，Ripple 需要是其中一种的超集。”  
> **—— Ripple 的创建者 Dominic Gannaway**

[Prettier](https://prettier.io/) 是一种在 JavaScript 和 TypeScript 中使用的固执己见的[代码格式化工具](https://prettier.io/)。[ESLint](https://thenewstack.io/poor-password-hygiene-enabled-eslint-supply-chain-attack-on-npm/) 是一种广泛使用的开源静态代码分析工具。

Ripple 也有自己的文件扩展名：.ripple。

## Ripple 的细粒度渲染方法

Ripple 支持细粒度渲染，这有点像 React……但又不一样，他提醒道。他说，这是 React 顶层渲染世界和细粒度级别渲染的结合。

“值需要与组件树相关联，这有点像 React，即新状态必须在组件内部使用，这使得连接与组件相关，而不是与副作用相关，”他说。“我们所做的则是，我们让依赖项能够知晓信号的版本。”

他补充说，每次信号改变时，其版本也会改变。当 Ripple 调用更新时，它会遍历树，并且不是重新渲染，而是仅仅检查是否需要更新。

## 不支持 SSR、Signals 或 React Server Components

Ripple 目前不支持的一项功能是[服务器端渲染](https://thenewstack.io/is-server-side-rendering-reacts-holy-grail/) (SSR)。

“我想专注于打造真正的 [SPA（单页应用）](https://thenewstack.io/spas-and-react-you-dont-always-need-server-side-rendering/)体验并完善其功能，”他说。“这样做的原因是，它能让我们很好地了解稳定性、我们的 API 以及我们的设计选择是否奏效。同时，它也让我们有时间重新思考如何实现水合作用以及与服务器端渲染相关的各种事情。”

Ripple 与其他框架的另一个不同之处在于，许多其他框架同时依赖于[虚拟 DOM](https://thenewstack.io/javascript-framework-reality-check-whats-actually-working/)（UI 树的内存表示）和响应式图或[信号](https://thenewstack.io/did-signals-just-land-in-react/)。这种双重架构在连接、断开连接和清理方面需要更多的内存和 CPU 时间。

“我在开发 Svelte 时发现，我们其实并不需要那样做，”他说。“有不同的方法来做这件事。”

他解释说，通过不使用信号，Ripple 不需要那么多的内存，也没有那么多开销来清理或创建初始树。

此外，Ripple 将不支持 [React Server Components](https://thenewstack.io/react-server-components-in-a-nutshell/)。他表示，这是因为 Ripple 不支持服务器端渲染。

## Ripple 可以在 React 内部使用，反之亦然

可以在现有的 React 应用程序中使用 Ripple，反之亦然：开发人员可以在 Ripple 应用程序中使用 React。

“Ripple 具有兼容性，这意味着你可以在现有应用程序中逐步采用 Ripple，”Gannaway 说。

Ripple 即将发布一个用于 React 的兼容适配器。未来，他计划添加 [Solid](https://thenewstack.io/solidjs-creator-on-fine-grained-reactivity-as-next-frontier/)、Svelte、[Vue](https://thenewstack.io/a-peek-at-whats-next-for-vue/) 和其他框架，以便 Ripple 与所有这些框架都兼容。