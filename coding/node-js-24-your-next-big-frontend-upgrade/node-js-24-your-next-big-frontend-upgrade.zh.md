开源软件开发者 [Matteo Collina](https://github.com/mcollina) 是 Node.js 技术指导委员会的成员，他想问你一个问题：你为什么不更新 Node.js？

而且，看在上帝的份上，当 Node 20 已经进入维护模式时，为什么对不受支持的 Node 12 的下载量还在增长？

“Node 12 在那里，你看到红色的那个在上升，我不知道为什么，”Collina 说，他指着一张图表，图表显示 Node 12 的下载量确实在增加。这引起了一阵紧张的笑声。“无论如何，你们没有更新 Node，是吗？你们为什么不更新？……[Node 24](https://nodejs.org/en/blog/release/v24.0.0) 将成为新的 Active LTS；拜托各位，更新吧。”

Active LTS，即长期支持，意味着该版本会得到积极维护，并且比常规版本获得更长时间的定期更新。

Collina 创建了 [Fastify 框架](https://thenewstack.io/introducing-fastify-speedy-node-js-web-framework/)，同时也是 [Platformatic.dev](https://platformatic.dev/) 的联合创始人兼首席技术官，这是一个旨在简化 Node.js 开发的云原生平台。他提供了一份 Node.js 状态报告，以向开发者更新关于 Node.js 的信息，Node.js 是一个流行的跨平台运行时，允许开发者在浏览器之外执行 JavaScript 代码。他在本月的 [JSNation](https://jsnation.com/) 大会上发表了他的评论，这是一场在阿姆斯特丹举行的混合活动。

他首先提到，[Node 包管理器 (NPM)](https://www.npmjs.com/) 和 [Node.js](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/) 是同一枚硬币的两面。[NPM](https://thenewstack.io/npm-security-woes-continue-amidst-a-series-of-cdn-attacks/) 是目前最流行的开源注册表，用于下载各种东西，他说。

“模块化使用量每年增长大约 50%，每两年翻一番，”他说。“你们正在下载大量模块，伙计们，我不知道。它并没有下降。”

仅 Node.js 的下载量在 2024 年 12 月就达到了 2.71 亿次，而在 5 月，这个数字是每月 3.75 亿次下载，他说。

“首先，我不知道你们为什么不更新 Node.js，”他说。

Node 18 在 4 月份停止支持，但仍然有很多人在使用它——事实上，5 月份它被下载了 5000 万次，他指出。

数据还显示，开发者在更新时倾向于跳过一个版本。

“这是 Node 16，好的，正在下降——仍然被下载，我不知道，每月 3000 万次，”他说。“对不起，各位，我惊呆了。……你们可以看到，没有很多人直接从 Node 16 跳到 Node 20。”

[![Matteo Collina 在本月的 JSNation 上讨论 Node.js 旧版本的下载情况。](https://cdn.thenewstack.io/media/2025/06/bc38eba7-flabberghasted_node.jpg)](https://cdn.thenewstack.io/media/2025/06/bc38eba7-flabberghasted_node.jpg)

Matteo Collina 在本月的 [JSNation](https://jsnation.com/) 上讨论 Node.js 旧版本的下载情况。截图来自 JSNation 的演示。

这引出了他关于你为什么应该更新 Node.js 的理由：一言以蔽之，[安全性](https://thenewstack.io/nodejs-interactive-security/)。

“Node 项目非常努力地保证你们所有人的安全，并每季度为你们提供一个不错的安全版本。你们喜欢我们的安全版本吗？也许，可能不喜欢，”他说。“好吧，我们也不喜欢它们，但我们生活在这个世界里。”

[Alpha Omega](https://alpha-omega.dev/) 是一个 Linux 基金会项目，为 Node.js 提供部分资金以维持其安全态势，他说。此前，这些资金约为 30 万美元，但在 2025 年，资金减半至 15 万美元，他补充说。

## Node.js 更新

Node 现在有 `require()` ESM——它可以直接使用，因此你可以在 CommonJS 上下文中加载 ES 模块，从而提高 Node.js 应用程序中 CommonJS 和 ESM 之间的互操作性。

与此相关的是，如果你使用的是最新版本的 Node.js，则不再需要 .mjs。.mjs 过去用于明确指示 JavaScript 文件应被视为 ECMAScript 模块。现在，开发者可以直接运行它，而无需使用 .mjs。

“没有人喜欢那个 [...] 脚本，”他说。“所以你可以直接运行它，它就能工作。”

另一个重大变化：TypeScript 现在可以直接运行，Collina 将此归功于 [Marco Ippolito](https://github.com/marco-ippolito) 的工作，他是 HeroDevs 的高级安全工程师，也是 Node.js 技术指导委员会的成员。

他们希望将其作为 Node 22 上的一个标志，并在 Node 24 中实现稳定，他补充说。

V8 中也发生了一些变化，允许 Node 团队将开放遥测跟踪的性能提高大约 7%，他说。[V8](https://v8.dev/) 是谷歌的开源、高性能 JavaScript 和 WebAssembly 引擎，用 [C++](https://thenewstack.io/bjarne-stroustrup-on-how-he-sees-c-evolving/) 编写。它是驱动 Node.js 的引擎。

“它还使许多基于异步本地存储的东西运行得更快，”Collina 说。“由于它，[有] 很多新东西即将到来。”

最后，他谈到了使用 [显式资源管理](https://github.com/tc39/proposal-explicit-resource-management)，这是 TC39 的一项新功能，它提供了一种 [结构化的方式来管理资源生命周期](https://dev.to/zacharylee/explicit-resource-management-in-js-the-using-keyword-d9f#)，例如文件句柄或网络连接。资源被自动释放，这意味着只要退出使用它们的代码块，资源就会被自动清理，即使发生错误也是如此。

“你可以做，本质上是一个终结器或一个在退出作用域时的释放器，”他说。“它已经适用于 Node 24 上的计时器和其他 API，但我们计划将此添加到所有 API 中。这有什么用？因为，本质上，你将能够使用一个文件或使用一个流，并且这些文件或流将被自动释放和正确清理，特别是如果底层有一个原生资源。它也适用于同步和异步。所以它非常棒。”

这解决了 JavaScript 中一个长期存在的挑战，这个问题很棘手，尤其是在异步操作中。在开发者显式关闭资源之前发生错误的可能性可能导致资源保持打开状态，从而导致泄漏。JavaScript 的自动垃圾回收不会清理这些非内存“原生资源”，如文件描述符。

通过允许资源在其作用域退出时自动释放——无论代码正常完成还是出现错误——显式资源管理功能为同步和异步操作提供了一种可靠的清理机制。

## Watt：一个 Node.js 应用程序服务器

Collina 还谈到了他去年在 Platformatic.dev 平台上发布的 [Node.js 应用程序服务器](https://blog.platformatic.dev/introducing-the-node-application-platform)。他说，这个名为 Watt 的服务器使应用程序开箱即用地达到企业级水平。

“它以精简的多线程方式运行你的应用程序，在同一线程、同一进程中运行多个 Node.js 应用程序，使用线程并标准化探针、日志、指标、开放遥测等等，”他说。

他补充说，这使得 Node.js 能够做一些好事——比如运行 PHP。

以前可以在 Node.js 上运行 [PHP](https://medium.com/@MartinMouritzen/how-to-run-php-in-node-js-and-why-you-probably-shouldnt-do-that-fb12abe955b0)，但现在 Node.js 内部的 PHP 作为原生插件在单独的线程上运行，他说。

“你基本上可以创建一个单一进程，其中包含你的 Next.js 应用程序和你的 PHP 应用程序，”他说。“它是如何工作的？它在单独的线程上运行 PHP，这样它就可以阻塞并做所有这些事情。”

他告诉观众，支持 PHP 的主要原因是人们想要运行 PHP，并且仍然拥有 [无头模式](https://thenewstack.io/maximizing-headless-architecture-a-guide-for-developer-teams/)。

“我想我在 2017 年与一家非常受欢迎的报纸合作开发过这样一个应用程序，他们使用 WordPress 进行编辑，然后 [他们] 想要使用 React 作为他们的 [前端](https://roadmap.sh/frontend)，”他说。“如今，有很多软件是用 PHP 构建的，而且可能不会很快消失。”