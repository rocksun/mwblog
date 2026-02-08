<!--
title: WebAssembly 对决 JavaScript：实测性能表现
cover: https://cdn.thenewstack.io/media/2026/01/5e959c93-paris-bilal-c1kpvqsgpcs-unsplashc.jpg
summary: 文章通过图像处理任务对比了WebAssembly与JavaScript的性能，结果显示Wasm在轻量任务中快两倍，重量任务中快六倍以上，证明了Wasm在处理复杂计算时的显著优势。
-->

文章通过图像处理任务对比了WebAssembly与JavaScript的性能，结果显示Wasm在轻量任务中快两倍，重量任务中快六倍以上，证明了Wasm在处理复杂计算时的显著优势。

> 译自：[WebAssembly vs. JavaScript: Testing Side-by-Side Performance](https://thenewstack.io/webassembly-vs-javascript-testing-side-by-side-performance/)
> 
> 作者：Jessica Wachtel

当我们谈论 [WebAssembly](https://thenewstack.io/webassembly/) (Wasm) 时，我们经常将其描述为“接近原生速度”和“比 JavaScript 更快”。但这在实践中究竟是怎样的呢？

在我们深入了解 Wasm 的优势之前，让我们先明确一点：在 UI 方面，JavaScript 仍然是开发者的最佳伙伴。它旨在操作 DOM（网络的文档对象模型）并处理 CSS 更新，而且它成功地完成了这项工作。但我们正在实时观察浏览器需求的变化。JavaScript 创建于 1995 年，旨在为文本页面添加简单的交互性。如今，我们要求浏览器处理 4K 视频并运行 Brendan Eich（[JavaScript 的创建者](https://thenewstack.io/brendan-eich-on-creating-javascript-in-10-days-and-what-hed-do-differently-today/)）从未设想过的复杂数学运算。

我之前已经写过一篇关于 [Wasm 如何提升您的 JavaScript 应用性能](https://thenewstack.io/when-should-javascript-devs-use-the-power_of_webassembly/) 的基本教程。在此基础上，现在我将对 Wasm 和 JavaScript 进行一些速度比较。

## Wasm 与 JS 教程简介

当你超越 UI 逻辑，进入繁重的数据处理时，JavaScript 需要一个伙伴。这就是 WebAssembly 的用武之地。但在实际场景中，Wasm 究竟比 JavaScript 快多少呢？让我们一探究竟。

对于这个项目，我们正在构建一个基于浏览器的图像处理器，旨在处理两种不同类型的操作：

*   **一个“轻量”任务：** 将彩色图像转换为灰度。
*   **一个“重量”任务：** 使用计算成本高昂的卷积矩阵应用锐化滤镜。

这两个操作都严重依赖数学转换来视觉改变图像。通过测试这两个极端，我们可以比较轻量任务和重量任务的性能。

在开始之前，请确保您已安装以下组件：

*   Node（与 `npx` 一起用于运行服务器）：[在此下载](https://nodejs.org/en/download)
*   Rust：[在此下载](https://rustup.rs/)
*   Wasm-pack（WebAssembly 构建工具）：在您的终端中运行 `cargo install wasm-pack`
*   带 Rust Analyzer 扩展的 IDE（例如，VS Code）

## 使用 Wasm 和 JavaScript 构建图像处理器

本项目使用 Rust，因为它在编译语言中拥有最成熟的 WebAssembly 生态系统。像 `wasm-pack` 和 `wasm-bindgen` 这样的工具生成 JavaScript 胶水代码并处理 Rust 和 JavaScript 之间的内存转换，让您可以专注于应用逻辑。

从您的主项目文件夹中，启动构建过程。

**创建项目：**

**打开工作文件夹：**

运行这些命令后，您将看到两个关键文件：

*   `Cargo.toml`：定义 Rust 项目的依赖项。
*   `src/lib.rs`：包含应用逻辑。WebAssembly 项目使用 `lib.rs`，因为它们编译成库而非独立可执行文件。

`Cargo.toml` 是 Rust 项目清单（类似于 `package.json`）。将其默认内容替换为以下内容：

`src/lib.rs` 包含核心图像处理逻辑。

`轻量任务` 遍历像素数据，平均红、绿、蓝值，并将其替换为单个灰度值。

`重量任务` 使用卷积算法，通过嵌套循环根据相邻像素计算新的像素值并应用锐化矩阵。

`use wasm_bindgen::prelude::*;` 这一行导入允许 Rust 代码与 JavaScript 交互的宏。

## 将 Rust 代码编译成 WebAssembly

运行以下命令将 Rust 代码编译成 WebAssembly 并生成 `/pkg` 目录：

## 设置 HTML 前端

`index.html` 作为性能比较的前端仪表板。

用户可以上传图像并在四个画布上查看结果。页面使用 WebAssembly 和原生 JavaScript 运行相同的操作，进行并排计时比较。

`performance.now()` API 提供毫秒级高精度计时。
*注意：将 `index.html` 放置在与 `Cargo.toml` 相同的目录下。*

## 如何运行性能测试

在项目目录中，运行 `npx serve` 并在浏览器中打开 `http://localhost:3000`。

更复杂的操作显示出 Wasm 和 JavaScript 之间更大的性能差距。

为获得有意义的结果，请使用 4K 图像（大约 3840 × 2160 像素）。

使用“选择文件”按钮上传图像并运行测试。

## 性能比较结果

![](https://cdn.thenewstack.io/media/2026/01/408623df-tutorial-results-1024x912.png)

在多次运行中，Wasm 持续优于 JavaScript——轻量任务速度快约两倍，重量任务速度快六倍以上。

此测试涵盖一台机器上的单个图像。在大规模应用或处理视频等更复杂的工作负载时，性能提升将更加显著。