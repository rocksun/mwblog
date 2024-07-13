# Python 与 JavaScript 携手，Wasm 与 PythonMonkey 的魔法

![Python 与 JavaScript 携手，Wasm 与 PythonMonkey 的魔法](https://cdn.thenewstack.io/media/2024/07/eacad406-pythonmonkey2-1024x512.png)

[PythonMonkey](https://github.com/Distributive-Network/PythonMonkey) 是一款创新的 [JavaScript](https://thenewstack.io/javascript-on-demand-how-qwik-differs-from-react-hydration/) 运行时，它嵌入在 [Python](https://thenewstack.io/an-introduction-to-python-a-language-for-the-ages/) 中，弥合了世界上两种最 [流行的编程语言](https://thenewstack.io/rust-growing-fastest-but-javascript-reigns-supreme/) 之间的差距。

PythonMonkey 是一个运行在 Python 中的 JavaScript 运行时，它建立在 [Mozilla](https://thenewstack.io/mozilla-llamafile-builders-projects-shine-at-ai-engineers-worlds-fair/) 的 [SpiderMonkey](https://spidermonkey.dev/) 引擎之上。开发人员可以将其用作 Python 库，在 Python 中运行 JavaScript 代码。

[Distributive](https://distributive.network/) 是一家位于加拿大安大略省金斯顿的云计算初创公司，他们创建了 PythonMonkey，以便将他们的 JavaScript [NodeJS](https://thenewstack.io/node-js-22-release-improves-developer-experience/) SDK 直接移植到 Python，而无需维护两个项目，从而将代码维护成本降低了一半。

“我们希望 PythonMonkey 能帮助弥合数百万 npm 包和 Python 开发人员之间的差距，并有朝一日能够独立成为一个 JavaScript 运行时，与 [Node.js](https://thenewstack.io/node-js-22-release-improves-developer-experience/)、[Bun](https://thenewstack.io/meet-bun-a-javascript-runtime-for-the-whole-dev-lifecycle/) 和 [Deno](https://thenewstack.io/with-additional-funding-deno-sets-out-to-challenge-node-js/) 竞争，但它能够从 JS 中使用‘任何’ Python 包，”Distributive 的软件开发人员 [Will Pringle](https://www.linkedin.com/in/will-pringle/) 说。

事实上，PythonMonkey 使开发人员能够轻松地在 JavaScript 和 Python 之间使用代码，并且几乎没有性能损失，Pringle 在去年的一篇 [介绍该技术的博客文章](https://medium.com/@willkantorpringle/pythonmonkey-javascript-wasm-interop-in-python-using-spidermonkey-bindings-4a8efce2e598) 中写道——与此同时，Distributive 计划在下个月发布 PythonMonkey 1.0。

## WebAssembly API 和引擎

“例如，可以从 JavaScript 库中调用 Python 包，例如 [NumPy](https://numpy.org/)，或者直接从 Python 中使用 NPM 包，例如 [crypto-js](https://www.npmjs.com/package/crypto-js)，“Pringle 写道，“此外，使用 SpiderMonkey 中的 WebAssembly API 和引擎，在 Python 中执行 [WebAssembly](https://thenewstack.io/webassembly-adoption-is-slow-and-steady-winning-the-race/) (Wasm) 模块变得微不足道。”

是的，该库利用了 SpiderMonkey 的功能，包括其 WebAssembly 引擎，允许 Python 在沙箱中从各种语言（如 C、C++、[Rust](https://thenewstack.io/rust-on-the-rise-new-advocacy-expected-to-advance-adoption/) 等）运行不受信任的 Wasm 代码。

此外，开发人员可以使用 PythonMonkey 将用 Python 编写的缓慢的“热循环”重构为在 JavaScript 中执行，利用 SpiderMonkey 的即时编译器来实现接近本机的速度，Pringle 写道。

此外，PythonMonkey 还附带 PMJS，这是一个类似于 Node.js 的 JavaScript 运行时环境，它支持从 JavaScript 调用 Python 库。

## 简单代码示例

在他的文章中，Pringle 提供了一些编码指导，包括下面的“hello world”示例，它演示了从 JavaScript 生成的字符串被返回到 Python 上下文：

```python
>>> import pythonmonkey as pm
>>> hello = pm.eval(” ‘Hello World’.toUpperCase(); “)
>>> print(hello)
‘HELLO WORLD’
```

下面的更复杂的示例演示了将 Python print 函数作为参数传递给 JavaScript 函数，然后从 Python 调用该 JavaScript 函数：

```python
>>> import pythonmonkey as pm
>>> hello = pm.eval(“(func) => { func(‘Hello World!’)}”)
>>> hello(print)
Hello World!
```

此示例使用 pmjs 执行一个 JavaScript 文件，该文件使用 Python 的 print 函数（这可以通过 pmjs main.js 执行）：

*main.js*

```javascript
const pyPrint = python.eval(“print”);
pyPrint(“Hello, World!”); // 这将输出“Hello, World!”
```

## 项目目标

该项目的目标包括：

- 快速且内存高效。
- 使在 JS 或 Python 中编写代码成为开发人员的偏好。
- 从 Python 中使用 JavaScript 库。
- 从 JavaScript 中使用 Python 库。
- 相同的过程运行 JavaScript 和 Python 虚拟机——没有序列化、管道等。
- Python 列表和字典的行为与 JavaScript 数组和对象相同，反之亦然，完全适应给定的上下文。

## PythonMonkey 的起源
Distributive 的 CTO [Wes Garland](https://www.linkedin.com/in/wesley-garland-2203a23/) 创建了 PythonMonkey，旨在为公司开发人员简化工作。Garland 在 2007 年左右创建了 Node.js 的前身 [gpsee](https://github.com/wesgarland/gpsee)——基于 Mozilla 的 SpiderMonkey 引擎，与 PythonMonkey 类似。

“我们在 Distributive 拥有一个庞大而复杂的客户端 SDK，名为 dcp-client，用 JavaScript 编写，”Pringle 告诉 The New Stack。“其中包含大量逻辑，因此我们不想用 Python 重写它并维护两个项目——实际上是将 SDK 的开发成本增加一倍。PythonMonkey 使我们能够将 JavaScript 库中的所有底层逻辑移植到 Python，同时只维护一个代码库。”

**主要是一个 JavaScript 商店**

Distributive 主要使用 JavaScript 进行开发，因为公司需要在 Web 堆栈中运行。

“为了说明，我们正在构建 [DCP (Distributive Compute Protocol)](https://distributive.network/platform)，这是一个计算市场，人们可以在其中从其他人的家用电脑租用 CPU/GPU 周期，”Pringle 说。“这个想法是，如果你有一台闲置的电脑，你可以将其连接到我们的云计算网络并通过计算其他人的工作负载来赚钱。将你的电脑变成工作节点的程序是一个 JavaScript 引擎，它可以执行 JS 程序、WebAssembly 或任何可以编译到 (或具有编译到) WebAssembly 的编程语言。

“你也可以直接在浏览器中运行它。总之，我们实现中有很多 JavaScript 代码，但每个人都想用 Python 编写这种代码，因此 PythonMonkey 使 Python 开发人员能够使用我们的产品 (DCP)——而无需我们重新编写 SDK。”

Pringle 现在正在开发 Distributive 的 Python SDK，该公司预计将在未来几周内发布它。

## 项目演变
自去年 7 月推出 PythonMonkey 以来，Distributive 对该技术进行了大量改进，包括：

### Web 堆栈 API
- 从头开始实现 `XMLHttpRequest` API**——**使 socketio 等流行的 JavaScript 库能够使用标准 JavaScript 网络 API 在 PythonMonkey 中运行。
- 实现了一些计时器全局函数：[setInterval](https://developer.mozilla.org/en-US/docs/Web/API/setInterval)/[clearInterval](https://developer.mozilla.org/en-US/docs/Web/API/clearInterval)、setImmediate/clearImmediate 和 setTimeout/clearTimeout，返回 Node.js 风格的 `Timeout` 类，带有 `.ref()` 和 `.unref()` 方法。
- 实现 `console` API 中所有缺失的方法，现在 `console` 的行为与 Web 规范 [https://console.spec.whatwg.org/](https://console.spec.whatwg.org/) 相同。
- `atob`、`btoa` 函数。
### 跨语言强制转换
- 用户现在可以将任何任意 Python 对象包装/代理到 JavaScript 中。
- 更好的跨语言迭代器支持。
### 异常处理
- 实现完整的跨语言堆栈跟踪。
- 改进了跨语言嵌套异常处理和 Promise 拒绝处理。
- uncaughtExceptionHandler
### JavaScript 引擎更新
- 将 SpiderMonkey 更新到最新版本，因此用户可以享受与最新 Firefox 相同的新的 JS + WASM 语言功能，并且性能更好。
- 贡献了一个 [补丁](https://bugzilla.mozilla.org/show_bug.cgi?id=1904747) 到 SpiderMonkey，修复了一个 [错误](https://bugzilla.mozilla.org/show_bug.cgi?id=1904747)。
### 开发人员体验改进
- 更好的开发人员体验，带有嵌入式调试工具 `pmdb`（受 `gdb` 启发）和 WTFPythonMonkey（受 [wtfnode](https://www.npmjs.com/package/wtfnode) 启发）。
- 更好的 Python 类型提示和开发人员文档。
## 模块系统
PythonMonkey 的模块系统允许轻松地将 JavaScript 库移植到 Python，反之亦然。运行时使开发人员“能够轻松地将他们的 JavaScript 库移植到 Python，而无需承担用 Python 重写库并维护端口的昂贵负担，”Pringle 写道。

此外，“JavaScript 也非常适合高度异步的工作负载，而 Python 则不然，”Pringle 在他的帖子中解释道。“在 Distributive，我们打算使用这个库来执行我们复杂的 [dcp-client](https://docs.dcp.dev/api/dcp-client/index.html) 库，该库是用 JS 编写的，并支持 Web 堆栈上的分布式计算。”

同时，Pringle 指出，PythonMonkey 旨在通过尽可能共享不可变的备份存储来最大限度地减少内存消耗和复制开销。

## PythonMonkey 路线图
“PythonMonkey 的路线图包括许多功能和改进，以扩展其可用性，例如使用 esm 语法在 JavaScript 中导入 Python 模块，XMLHttpRequest，实现独立的事件循环而不依赖 Python 的事件循环，以及对 Node.js API 的支持，例如 fs、path、process，这将允许 Python 使用 NPM 包，例如 [express.js](https://expressjs.com/) 和 [socket.io](https://socket.io/)，”Pringle 在去年发布时写道。该公司已经实现了其中大部分。

路线图中另一个提出的目标是将 PMJS 扩展为一个完全集成的 Node.js 环境，它可以作为 Node.js 的直接替代品，并且还能够从 JavaScript 中使用 Python 包。

通过这些计划的增强功能，PythonMonkey 和 PMJS 旨在为开发人员提供一个完全集成的 Python-JS 环境。

## 比相关项目更优越？

同时，Pringle 将 PythonMonkey 与 [JS2PY](https://github.com/PiotrDabkowski/Js2Py)、[PyV8](https://github.com/okoye/PyV8) 和 [Metacall](https://github.com/metacall/core) 等相关项目进行了比较，强调了 PythonMonkey 在性能和功能方面的优势。

您可以在 [Google Colab](https://colab.research.google.com/drive/1INshyn0gNMgULQVtXlQWK1QuDGwdgSGZ?usp=sharing) 上试用 PythonMonkey。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。