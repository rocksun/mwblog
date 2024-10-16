# Spin + StarlingMonkey 等于 WebAssembly 的 JavaScript

![Spin + StarlingMonkey 等于 WebAssembly 的 JavaScript 的特色图片](https://cdn.thenewstack.io/media/2024/09/8d5aab92-christophe-hautier-902vnyeows4-unsplash-1024x683.jpg)

维也纳 - 虽然花了一些时间，但 JavaScript 与 [WebAssembly](https://thenewstack.io/webassembly/) (Wasm) 的部署已经取得了不错的进展，[Fermyon](https://thenewstack.io/fermyon-says-webassembly-on-kubernetes-is-now-doable/) 的 [Spin](https://www.fermyon.com/spin) 为在 [Wasm](https://thenewstack.io/what-makes-wasm-different/) 模块中部署 [JavaScript](https://thenewstack.io/google-angular-lead-sees-convergence-in-javascript-frameworks/) 提供了更直接的途径，这一点在这里得到了体现。借助 Spin JavaScript SDK，这种方法解决了以前存在的限制，被认为更加优雅。

此外，[字节码联盟](https://thenewstack.io/webassembly-to-let-developers-combine-languages/) 为一个名为 [StarlingMonkey](https://github.com/bytecodealliance/StarlingMonkey) 的新 JavaScript 运行时做出了贡献，该运行时增强了 Fetch API 支持并与 Node.js API 兼容。一个基于 Starling Monkey 构建的新 JavaScript SDK 应运而生，旨在扩展 JavaScript 在后端服务中的功能，与字节码联盟的目标相一致。

一个关键特性是 Spin 开发如何有助于提供一种更直接的方式来使用 WebAssembly 部署 JavaScript 代码。这种部署方法比以前更优雅，并解决了 JavaScript 之前存在的许多问题和限制。这种使用 Spin JavaScript SDK 的方法为在 Wasm 模块中实现的 JavaScript 提供了一条直接的部署途径。

“主要的是我们做了两件事：首先，我们为一个名为 StarlingMonkey 的新 JavaScript 运行时做出了贡献，它现在是字节码联盟的一部分。其次，我们为 Spin 实现了一个新的 SDK，”Fermyon 的产品和开发者关系主管 [Mikkel Mørk Hegnhøj](https://www.linkedin.com/in/mikkelhegn/?originalSubdomain=dk) 在维也纳的欧洲开源峰会上告诉我。“这个基于 Starling Monkey 构建的新 JavaScript SDK 实际上帮助我们为 Fetch API 提供了适当的 Fetch 支持，但它也提供了更广泛的 Node.js API 兼容性。以前使用 Node.js 解决的许多后端服务问题现在可以通过这个新环境中的 JavaScript 来处理。”

Spin JavaScript SDK 属于 Fermyon 的 Spin 框架。Spin 是一个开发者工具，你可以用它来构建无服务器 WebAssembly 工作负载或应用程序。除了 JavaScript，Spin 还支持多种编程语言，例如 [Rust](https://thenewstack.io/rust-growing-fastest-but-javascript-reigns-supreme/)、C++ 等。借助 Spin JavaScript SDK，将 JavaScript 代码编译成 WebAssembly 所需的特定于语言的命令将被处理。根据 Spin 文档，Spin 还旨在通过访问用于创建应用程序、将它们编译成 WebAssembly 以及在部署到不同环境之前使用 Spin CLI 中捆绑的运行时在本地测试它们的模板来简化开发过程。

## 让我们运行它

为了将你的 JavaScript 代码添加到 Spin JavaScript SDK，你需要先安装 [Spin](https://github.com/fermyon/spin)。

模板使用以下命令安装：

```bash
spin init --template=javascript
```

创建一个新的应用程序并构建：

```bash
spin build
```

从上一步安装的模板创建一个新的应用程序：

```bash
spin run
```

更改到应用程序目录：

```bash
cd my-app
```

安装依赖项并构建应用程序：

```bash
npm install && npm run build
```

使用例如 curl 在另一个终端中测试你的应用程序：

```bash
curl http://localhost:8080
```

你应该看到类似以下内容：

```
Hello, world!
```

能够在后端运行 JavaScript 应用程序是几十年来 JavaScript 以及最近的 WebAssembly 工作的结果。作为背景，在广为人知的万维网的早期，就有了 JavaScript。JavaScript 诞生于 1995 年，当时 [Brendan Eich](https://thenewstack.io/brendan-eich-on-how-javascript-survived-the-browser-wars/) 创建了这种语言来支持 Netscape，Netscape 是一款现在已经消失但美观且革命性的网页浏览器。从那时起，[ECMAScript](https://thenewstack.io/inside-ecmascript-javascript-standard-gets-an-extra-stage/) 标准一直是 Web 开发的基础，代表了在 Web 浏览器中运行的大多数应用程序。

最近，WebAssembly 出现了，它实际上已经存在了一段时间。在万维网联盟 (W3C) 于 2019 年将其命名为 Web 标准之后，它已成为继 HTML、CSS 和 JavaScript 之后的第四个 Web 标准。但是，虽然 Web 浏览器应用程序代表了 Wasm 的核心和历史用例，但重点是它被设计为可以在任何配置正确的 CPU 上运行 - 这就是 Wasm 和 JavaScript 同时分叉并在某些用例中变得更加集成的部分。
Wasm 和 JavaScript 紧密相连，但 Wasm 远不止 JavaScript。简而言之，Wasm 最初的目的是帮助 JavaScript 在 Web 浏览器中更高效地运行，这仍然是它们集成的关键部分。现在，这种集成已扩展到 Web 浏览器之外，进入边缘和服务器应用程序，而 JavaScript 本身并不适合这些应用程序。

这是因为 Wasm 在 CPU 级别以二进制格式运行。而且，别忘了，与 JavaScript 不同，Wasm 不是一种编程语言。Wasm 的主要优点之一是，它的功能使其能够除了 JavaScript 之外，还能容纳多种语言，包括 [Python](https://thenewstack.io/python-3-13-blazing-new-trails-in-performance-and-scale/)、[Rust](https://thenewstack.io/rust-and-c-work-better-for-webassembly/) 以及 Go、.NET、C++、Java 和 PHP。

因此，WebAssembly 可以根据需要集成 JavaScript，但它并不局限于集成 JavaScript。这种集成和与 JavaScript 的使用一直是 WebAssembly 和 JavaScript 共生关系的基石，尤其是在 Web 应用程序领域。

JavaScript SDK 是基于一个名为 [Javy](https://github.com/bytecodealliance/javy) 的项目构建的，该项目是 Bytecode Alliance 的一部分，Bytecode Alliance 是一个专注于 WebAssembly 系统接口的人员和组织团体。Javy 项目最初使用 QuickJS，这是一个根据规范对 JavaScript 运行时的最小但完整的实现。这个最初的 JavaScript SDK 基于 QuickJS，但为创建新组件提供了有限的灵活性。

快进到几个月前，Bytecode Alliance 项目 [ComponentizeJS](https://github.com/bytecodealliance/ComponentizeJS) 的开发。根据 Hegnhøj 和 Fermyon 的文档，该项目允许生成任意绑定，并使用 StarlingMonkey 作为引擎，该引擎基于 Mozilla 的 SpiderMonkey 引擎。这种转变使 SDK 更符合服务工作者规范，为开发人员提供了更大的 API 表面来创建更多样化的应用程序，并提高了与许多以前不适用于旧 SDK 的 Node.js 包的兼容性。

新 SDK 中最大的改进之一是 Fetch 实现。以前，Fetch 是一个基本实现，只支持简单的出站请求。现在，Fetch 符合服务工作者规范，允许依赖于完全实现的 Fetch 的包（例如用于 SQS 和 S3 的 [AWS](https://aws.amazon.com/?utm_content=inline+mention) SDK）工作。此增强功能使开发更多样化的应用程序成为可能，例如从 S3 存储和检索数据的应用程序。

Hegnhøj 表示，新 Spin JavaScript SDK 的目标是使其对经验丰富的 JavaScript 开发人员来说更具惯用性。新 API 在一定程度上模仿了 [Express.js](https://thenewstack.io/a-showdown-between-express-js-and-fastify-web-app-frameworks/)，这是一个用于构建 Web 应用程序的流行框架。SDK 的签名已更改为更像 Express，并且 SDK 现在允许流式响应，Hegnhøj 说。

新 SDK 在内部引入了组件 ID，而 StarlingMonkey 针对服务工作者规范，这意味着它无法访问所有 Node.js API。一些依赖于 Node.js API（如文件系统或进程）的包将无法原生运行，但 wasi-exd 库提供了一个 polyfill，允许使用 process.env 等功能，但需要进行一些修改。

StarlingMonkey 与所有 WebAssembly 运行时兼容，这意味着不依赖于 Spin 特定功能（如键值存储、SQLite 或 [Postgres](https://thenewstack.io/postgres-is-now-a-vector-database-too/)）的应用程序应该可以在任何支持 OAC3 的 WebAssembly 运行时上运行。即使没有 Spin 特定功能的应用程序也应该在任何支持的运行时中无问题地运行，Hegnhøj 说。

## 未来工作
新 Spin JavaScript SDK 需要改进。在 [一篇博文中](https://www.fermyon.com/blog/introducing-the-new-js-sdk)，Fermyon 的首席工程师兼 Bytecode Alliance 联合创始人 [Till Schneidereit](https://de.linkedin.com/in/tillschneidereit) 指出：

- 边缘云平台提供商 Fastly 是 WebAssembly 项目和 Bytecode Alliance 的重要贡献者，它继续为 WebAssembly 中的 JavaScript 执行做出贡献。这项工作的第一个迭代已集成到 StarlingMonkey 中，导致执行速度提高了几倍，具体取决于工作负载。这种集成最近完成，但尚未集成到 JavaScript SDK 中，但将在不久的将来添加，Schneidereit 写道。
StarlingMonkey 的一项关键改进即将完成，它允许将运行时和它提供的 Web API 的部分用 Rust 而不是 C++ 实现，Schneidereit 写道。此更改将使更容易跟上 Web 生态系统中的最新发展，并提供更完整、更兼容的 Web API 实现，这些 API 对现有 JavaScript 应用程序至关重要。由于并非所有 JavaScript 代码都依赖于基于 Web 标准的 API，有些使用 Node.js API，因此正在开发一个兼容性层来支持这些 API 在 Spin 应用程序中的使用，Schneidereit 写道。

支持更多触发器类型：新的 JavaScript SDK 目前仅支持 HTTP 触发器。Schneidereit 写道，正在努力添加对其他触发器类型的支持，例如 Cron 和 Redis 触发器。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等。