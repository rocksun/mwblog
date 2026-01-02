2025年被证明是JavaScript生态系统转型的一年，其特点是转向性能优化和“[后React](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)”探索。我们回顾了2025年主导JavaScript社区的故事和趋势。

## 挑战React

尽管React仍然是开发的中心支柱——甚至大型语言模型（LLM）在自主运行时也主要[输出React代码](https://thenewstack.io/why-ai-is-generating-lowest-common-denominator-react-code/)——但在2025年，更多开发者呼吁采用“Web标准优先”的理念，强调简洁性，因为开发者开始质疑重型客户端抽象的必要性。

部分原因在于，现代浏览器已经足够成熟，可以处理以前需要React完成的任务，包括支持[View Transitions API](https://thenewstack.io/interop-unites-browser-makers-to-smooth-web-inconsistencies/)和[Web组件](https://thenewstack.io/how-microsoft-edge-is-replacing-react-with-web-components/)。我们还在[Remix 3](https://thenewstack.io/remix-3-and-the-end-of-react-centric-architectures)中看到了这一点，它通过将加载器/操作等Web基础功能置于React特定的状态管理之上，挑战了以React为中心的架构。这表明React应该是视图层，而非基础层。

但对React来说并非全是坏消息：它现在有了自己的基金会。在[React治理的重大变革](https://thenewstack.io/react-foundation-leader-on-whats-next-for-the-framework/)中，Meta将其框架的治理权移交给了Linux基金会旗下的一个独立基金会，旨在促进企业中立性和更广泛的生态系统贡献。

## 框架趋势：MPA、Signals和编译器

2025年，框架的发展并未放缓。事实上，这一年引入了新的框架——包括用于边缘计算的[微框架Hono](https://thenewstack.io/hono-shows-the-way-for-microframeworks-in-a-post-react-world/)。

此外还有[基于React的One](https://thenewstack.io/one-lets-frontend-devs-build-once-deploy-web-and-native-apps/)，它支持创建Web和原生平台应用。这一年还发布了[极简主义的Mastro](https://thenewstack.io/minimalist-mastro-framework-offers-modern-take-on-mpas/)，用于多页应用。它倡导“默认零JS”，并支持浏览器原生路由，而不是笨重的客户端SPA。最后是[Wasp](https://thenewstack.io/javascripts-missing-link-wasp-offers-full-stack-solution/)，它提供了一个全栈解决方案，为React/Node生态系统带来了类似Ruby on Rails的体验。

对于非React框架，Signals成为了响应性的基石。Signals只对UI中需要更新的精确部分使用响应性。[Angular](https://thenewstack.io/angular-v21-adds-signal-forms-new-mcp-server/)、Vue、Solid和Svelte现在都使用Signals进行状态管理。甚至有人推动将[Signals添加到JavaScript规范中](https://github.com/tc39/proposal-signals)。

但展望2026年，SolidJS的创建者Ryan Carniato预测，[细粒度响应性可能成为非React框架的下一个前沿](https://thenewstack.io/solidjs-creator-on-fine-grained-reactivity-as-next-frontier/)。

“当几乎所有非React框架都在这一点上率先采用了Signals时，其影响是难以忽视的，”他说，并补充道，“我们正处在一个更大变革的开端，我并非唯一持有这种想法的人。”

我们还在2024年末发布的[Svelte 5中的Runes](https://thenewstack.io/youll-write-less-code-with-svelte-5-0-promises-rich-harris/)中看到了对细粒度响应性的关注。

编译器也承担了更多繁重的工作。2024年底稳定发布的[Svelte 5的Runes](https://svelte.dev/blog/svelte-5-is-alive)依赖于Svelte的编译器。该编译器将看起来像函数的[Runes](https://svelte.dev/blog/runes)转换为Signals运行时。[React编译器](https://thenewstack.io/meta-releases-open-source-react-compiler/)也在今年被标记为稳定版。React使用编译器自动化记忆化（memoization），这是一个术语，指的是改变UI重新渲染的多少，而不是改变数据更新的方式（这正是Svelte编译器所做的）。

然而，在这两种情况下，编译器都在进行一些繁重的工作，将“人类可读”的代码转换为优化的机器代码，以避免不必要的重新渲染。

## 工具链：统一栈之战

2024年底，Vite的创建者Evan You[宣布成立VoidZero](https://thenewstack.io/vite-creator-launches-company-to-build-javascript-toolchain/)，一家致力于为Web开发社区创建统一的基于Rust的工具链的公司。这个工具生态系统将最终解决JavaScript开发的“碎片化税”——开发者“拼凑”数十个工具的情况。

TNS高级编辑Richard MacManus在10月[与You进行了交谈](https://thenewstack.io/how-vite-became-the-backbone-of-modern-frontend-frameworks/)，讨论了由此产生的统一工具链Vite+。You说：“Vite+是一个[统一层](https://thenewstack.io/vites-creator-on-a-unified-javascript-toolchain-and-vite/)，它将所有这些东西整合在一个连贯的解决方案中，对吗？所以它是Vite本身的一个直接可用的超集。”

它捆绑了You的公司正在开发的几个不同的[开源项目](https://thenewstack.io/does-your-open-source-project-need-foundation-oversight/)，包括：

* Rolldown，一个Vite新的基于Rust的[打包器](https://thenewstack.io/vites-new-rust-based-javascript-bundler-available-in-beta/)；
* Oxlint，一个由Rust驱动的JavaScript和TypeScript代码检查器；
* Vitest，一个Vite原生的测试框架；以及
* Oxc，一个用Rust编写的JavaScript工具集合。

## AI与框架

2025年，AI从后端走向前端。我们看到了一系列MCP服务器的推出，旨在帮助框架将最佳实践和标准与AI连接起来，其中包括来自Angular和React的MCP服务器，以及TanStack Start等框架计划推出的更多服务器。

Minko Gechev等框架维护者甚至尝试了一个“[LLM优先”框架](https://blog.mgechev.com/2025/04/19/llm-first-web-framework/)，该框架专门设计用于AI代理轻松编写和调试。TanStack最近发布了[TanStack AI](https://thenewstack.io/tanstack-adds-framework-agnostic-ai-toolkit/)，这是一个面向开发人员的新的与框架无关的AI工具包的alpha版本。

我们也看到了AI在浏览器内的使用转变，[像AsterMind-ELM和TensorFlow.js这样的库](https://thenewstack.io/javascript-library-runs-machine-learning-models-in-browser/)允许开发者直接在浏览器中训练和运行机器学习模型，延迟微秒级，从而绕过了对昂贵服务器端GPU的需求。还有[Hashbrown](https://thenewstack.io/run-ai-agents-in-the-browser-with-the-hashbrown-framework/)，一个允许AI代理在浏览器中运行的开源框架。

## 展望2026

2025年以令人惊讶的方式推动了JavaScript的进步，但它提出的问题或许比解决的更多。框架[最终会走向融合吗](https://thenewstack.io/google-angular-lead-sees-convergence-in-javascript-frameworks/)？2026年是否会推出更多框架来解决新的担忧和需求？AI对JavaScript及其支持生态系统意味着什么？

希望在未来一年里，我们能找到这些问题的答案。