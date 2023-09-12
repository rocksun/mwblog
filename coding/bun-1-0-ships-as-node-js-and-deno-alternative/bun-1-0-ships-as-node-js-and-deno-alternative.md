# Bun 1.0 作为 Node.js 和 Deno 的替代品发布

Bun 1.0 已经发布;它被设计成 Node.js 的替代品。Bun 速度很，但速度是唯一重要的因素吗？

最近在用 next.js 做一个东西，感觉对 node.js 和 React 相关的工具很感兴趣。译自 [Bun 1.0 Ships as Node.js and Deno Alternative](https://thenewstack.io/bun-1-0-ships-as-node-js-and-deno-alternative/) 。

![](https://cdn.thenewstack.io/media/2023/09/acec7ac0-bun.png)
*图片来自 Bun*

[发布 Bun 1.0](https://bun.sh/blog/bun-v1.0) 最困难的事情之一，作者 [Jarred Sumner](https://github.com/Jarred-Sumner) 通过 推特分享，是移除测试版中的前端服务器。

“我希望我们有更多的时间来使 Bun 对前端开发友好，”周四发布后，Sumner 在推特问答时说。“对它来说不算糟糕——你可以使用[...]你已经使用的工具。但我仍然认为这里对于直接集成前端构建工具的运行时有很大的机会。”

也就是说，Bun 发布后，没有人对此表示关注。他指出，用户反馈明确表示可以移除前端服务器，他注意到对这个新闻的[社交媒体的反响](https://twitter.com/jarredsumner/status/1699756697806660083)基本上是积极的。到了周五，关于 Bun 的讨论全部集中在它的速度和易用性上。

## 构建用于速度

Bun 与 Node.js 以及基于 Rust 的 Deno 竞争，两者都是由 Ryan Dahl 创建的。事实上，根据周四播出的发布直播，它被[设计](https://thenewstack.io/meet-bun-a-javascript-runtime-for-the-whole-dev-lifecycle/)成 Node.js 的替代品。团队在直播中说，Bun 的写入速度是 Node.js 的三倍，读取文件速度最高可达三倍。 Oven 公司的产品经理 Ashcon Partovi 谈到了 Bun 运行时。

“Bun 工具包中有很多工具，”Partovi 说。“但皇冠上的宝石是 Bun 运行时。Bun 是一个向下兼容的 Node.js 替代品，可以运行 Typescript 和 TSX 文件，不需要依赖。”

他还补充说，Bun 可以用 Bun run 替换任何 npm run 命令，而 npm 在 MacBook Pro 上运行脚本需要约 150 毫秒。与此相比，Bun 只需要 30 毫秒，他说。

“Npm 感觉明显有延迟。而 Bun 感觉是瞬间的，”Partovi 说。

Bun 从 WebKit 的 [JavaScriptCore](https://developer.apple.com/documentation/javascriptcore) 获得提速，这是以异常快速而闻名，根据通过推特分享[她对速度看法](https://twitter.com/maybeshalinii/status/1701198811119403022)的全栈开发人员 [Shalini Tewari](https://twitter.com/maybeshalinii) 的说法。

“Node.js、Bun 和 Deno 都是服务器端 js 运行时，但它们有完全不同的目标。

在 Bun 和 Node.js 之间的选择取决于你项目的需求，”Tewari 建议说。“如果您需要速度和直截了当、轻量级的体验，请选择 Bun。如果您希望更广泛的生态系统和社区支持以及许多工具，Node.js 是一个不错的选择。您甚至可以同时使用两者，使 JavaScript 应用程序强大高效。”

## 基准测试运行时

Snky 开发者安全平台的软件工程师 [James Konik](https://snyk.io/contributors/james-konik/) 最近[比较了这三个运行时](https://snyk.io/blog/javascript-runtime-compare-node-deno-bun/)，发现 Bun 的表现优于 Node.js 和 Deno。

“Bun 由 [Zig](https://ziglang.org/) 提供动力，其目标是成为一个一体化的运行时和工具包，侧重于速度、捆绑、测试和与 Node.js 包的兼容性，”他写道。“它最大的吸引力之一是其性能，明显比 Node.js 和 Deno 都要快。如果它能够兑现所有诺言，这将是一个非常有吸引力的主张。”

他指出，Bun 维护者提供了一个基准测试的例子，运行一个 HTTP 处理程序，使用 React 在服务器端渲染页面。Bun 处理了大约 68，000 个请求每秒，而 Deno 和 Node.js 分别处理大约 29，000 和 14，000 个请求。

在自己对早期版本 Bun 的测试中，Konik 发现 Node.js 处理了 21.29 个平均查询每秒，而 Deno 的评分为 43.50。Bun 处理了 81.37 个平均查询每秒。

“在 Node.js、Deno 和 Bun 的[另一个比较](https://medium.com/deno-the-complete-reference/node-js-vs-deno-vs-bun-vs-go-a-re-look-at-the-performance-with-json-request-response-aacbb29aa0a0)中，Bun 处理并发连接最快。它的每秒请求数也相当高，”Konik 写道。“例如，在 10 个并发连接的情况下，Bun 实现110，000个请求每秒，而 Node.js 实现 60，000 个请求每秒，Deno 实现 67，000 个请求每秒。”

值得注意的是，[不同的比较发现 Deno 和 Bun 的表现非常相似](https://medium.com/deno-the-complete-reference/node-js-vs-deno-vs-bun-vs-go-a-re-look-at-the-hello-world-performance-d90b76ad61a5)。

当然，速度不是考虑运行时的唯一因素。在 [Deno 讨论](https://github.com/denoland/deno/discussions/20429#discussioncomment-6955031)中，开发人员 [markthree](https://github.com/markthree) 指出每个运行时都有其优势。

“Bun 目前在性能方面更关注，所以它在性能方面比其他两个运行时好得多，”他写道。“在我看来，Deno 与安全同义，我可以安全地使用社区中的包，不必担心它们在我不知情的情况下对我的系统做一些事情。Node 现在也开始在性能和安全方面做出巨大的推动。

“竞争是好事，js 运行时正在开始发展，”他补充道。

## Bun还有更多要展示

也就是说，Bun 仍在进展中。例如，Sumner 在周四发布后的一个 推特问答中透露，Bun 安装对 Linux 和 Mac OS 准备就绪，但团队在使 Windows 版本工作方面遇到了困难。Bun 为 Windows 提供有限的实验性本机构建。目前，根据文档，仅支持 Bun 运行时。

“我的猜测是，Bun 安装可能要再晚两周，”Sumner 说。“在第一版中，Windows 的性能会非常不优化。实际上快速运行还需要一段时间。”

除了运行时之外，Sumner 说，Bun 内置了一些功能，将使开发者的生活更轻松，例如:

- 同时支持常见的 JS 和 [ES 模块](https://hacks.mozilla.org/2018/03/es-modules-a-cartoon-deep-dive/)
- 支持通过 --hot server.ts 进行即时重载
- 一个插件 API，让开发者定义自定义加载器

“你可以扩展 Bun 运行时以支持像 .Yaml 导入这样的东西，”他说。“它使用一个受 ES 构建启发的 API，这意味着许多 ES 构建插件可以直接在 Bun 中使用。”
