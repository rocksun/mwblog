<!--
title: JS开发者：WebAssembly 的洪荒之力，你该何时驾驭？
cover: https://cdn.thenewstack.io/media/2025/12/1f934e7d-loren-king-of2zsonovzo-unsplashb.jpg
summary: WebAssembly (Wasm) 旨在弥补 JavaScript 性能不足，处理CPU密集型计算。它与JS协同工作，而非替代，实现高性能。AssemblyScript简化Wasm开发。
-->

WebAssembly (Wasm) 旨在弥补 JavaScript 性能不足，处理CPU密集型计算。它与JS协同工作，而非替代，实现高性能。AssemblyScript简化Wasm开发。

> 译自：[When Should JavaScript Devs Use the Power of WebAssembly?](https://thenewstack.io/when-should-javascript-devs-use-the-power-of-webassembly/)
> 
> 作者：Jessica Wachtel

JavaScript [三十年前](https://cybercultural.com/p/1995-the-birth-of-javascript/)问世，用于简单的网页交互。虽然它仍然是网络运行的基础，但如今的应用程序比那时复杂得多。这意味着浏览器中需要大量功能，JavaScript 可以处理，但通常会以牺牲性能为代价。作为一个每隔几秒钟就会刷新一次，等待缓慢应用程序加载的人（是的，我知道这没有帮助，但我还是会这么做），速度至关重要。

作为解决方案，[WebAssembly](https://thenewstack.io/webassembly/) (Wasm) 于 2017 年推出。

## 理解 Wasm 及其与 JavaScript 的协同工作

WebAssembly 除其他功能外，帮助开发者将计算密集型或复杂逻辑从 JavaScript 中移出，而无需放弃 JavaScript 生态系统。通过使用 WebAssembly，您可以用 Rust、C++ 或 AssemblyScript 等语言编写性能要求高的代码，这些代码仍然可以在浏览器或服务器上高效运行。由于 WebAssembly 编译后更接近机器代码，因此它使应用程序更快、更高效。

当然，Wasm 并非旨在取代 JavaScript。它不能操作 DOM、处理事件或与现有框架一起工作。相反，它被设计为与 JavaScript *协同工作*。将 Wasm 视为处理繁重工作的途径，而 JavaScript 则提供生态系统和便利。

在 WebAssembly 的早期，构建和集成 Wasm 组件很棘手——尤其是对于有 JavaScript 背景的开发者。它通常需要复杂的设置和不明确的调试工作流，使其远非对初学者友好。

> AssemblyScript 通过让 JavaScript 开发者使用熟悉的、类似于 TypeScript 的语法编写 Wasm 来降低入门门槛。

经过多年的更新，WebAssembly 现在对所有级别的开发者都更加易于访问，这导致了其采用率的增加。

如今，WebAssembly 工具链已趋于成熟。现代工作流使得在 Node.js 和浏览器中编译 Wasm 模块、组织项目和加载 WebAssembly 变得更加容易。AssemblyScript 通过让 JavaScript 开发者使用熟悉的、类似于 TypeScript 的语法编写 Wasm 来降低入门门槛；而 `asinit`、`asc` 和官方加载器等工具则处理了大部分样板代码。

## WebAssembly 在 JS 应用程序中的理想用例

以下是一些通过将 WebAssembly 与 JavaScript 结合而受益的应用程序示例。

### CPU 密集型计算

繁重的计算——例如数据处理、模拟、图像处理或复杂数学——在 JavaScript 中小规模运行时通常可以接受，但随着工作负载的增长，它们可能成为瓶颈。在这些情况下，WebAssembly 与 JavaScript 结合使用，通过以接近原生速度执行，可以显著优于等效的 JavaScript 实现。

### 使用现有的非 JavaScript 代码

借助 WebAssembly，您可以将用 C++、Rust 或 AssemblyScript 等语言编写的库引入浏览器。这使您无需用 JavaScript 重写即可集成经过实战考验的高性能代码，这在 JavaScript 生态系统之外已经存在解决方案时尤其有用。

### 性能关键型功能

此类别包括需要高速执行和低开销的工作负载，例如实时数据转换、图像处理或视频处理。

WebAssembly 不适合 DOM 操作、简单的应用程序逻辑或 I/O 密集型工作流等任务。将 WebAssembly 用于繁重的工作。

## 一个使用 AssemblyScript 的 WebAssembly 分步教程

以下教程展示了如何将用 AssemblyScript 编写的基于 Wasm 的数学功能引入浏览器。虽然这个例子很简单，但数学密集型计算是 WebAssembly 的一个绝佳用例。

让我们开始构建。

### 先决条件

* 对 JavaScript 有基本了解
* npm
* Homebrew（仅限 macOS）
* 一个 IDE（本教程中使用 VS Code）
* [Node.js](https://nodejs.org) 版本 22 或更高

第一步是安装 `wash`。它是一个命令行工具，虽然不需要全局安装，但这样做可以使事情变得更容易。以下是在 macOS 上全局安装它的示例。

```
brew install wasmcloud/wasmcloud/wash@0.42.0
```

在您的 IDE 中打开一个新项目，并确保所有先决条件都已安装。

```
node -v
npm -v
wash --help
```

现在，创建项目文件夹：

```
mkdir wasm-adder
cd wasm-adder
```

### 初始化 AssemblyScript

运行 `npm install --save-dev assemblyscript` 以在本地安装 AssemblyScript。然后运行 `npx asinit .` 初始化项目，包含推荐的结构，包括 `assembly/`、`build/`、`asconfig.json` 和示例文件。

```
npm install --save-dev assemblyscript
npx asinit .
```

这将创建推荐的 AssemblyScript 项目结构：

```
wasm-adder/
├─ assembly/       # AssemblyScript sources
├─ build/          # Compiled WASM artifacts
├─ package.json
├─ asconfig.json
├─ tsconfig.json
├─ index.js
└─ tests/
```

### 编写 AssemblyScript 函数

`add` 函数包含将在 WebAssembly 中运行的应用程序逻辑。编译后，此 AssemblyScript 代码将成为一个 `.wasm` 模块。

```
export function add(a: i32, b: i32): i32 {
  return a + b;
}
```

`i32` 是 AssemblyScript 提供的一种数字类型。

### 编译为 WebAssembly

代码被编译到 `build/` 文件夹，生成 `release.wasm` 和 `release.wat`。`.wasm` 文件是 Node.js 或浏览器执行的二进制文件，而 `.wat` 文件是一种人类可读的格式，可用于调试。

```
npx asc assembly/adder.ts -b build/release.wasm -t build/release.wat --optimize
```

## 总结

这就是一个可运行的 WebAssembly 示例。有了这个基础，您可以将复杂或性能关键的计算卸载到 WebAssembly，同时让 JavaScript 专注于协调和用户体验。