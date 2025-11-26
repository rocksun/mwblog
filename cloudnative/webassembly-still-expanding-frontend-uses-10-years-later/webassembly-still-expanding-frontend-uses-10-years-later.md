<!--
title: WebAssembly：十年砥砺，前端版图持续扩张
cover: https://cdn.thenewstack.io/media/2025/11/3c23a316-tenyearswasm.jpg
summary: Wasm低级格式，实现业务逻辑跨平台，性能优于JS。Wasm 3增GC，支持多语言。常用编译工具：Emscripten、LLVM、Binaryen、wasm-pack、AssemblyScript。
-->

Wasm低级格式，实现业务逻辑跨平台，性能优于JS。Wasm 3增GC，支持多语言。常用编译工具：Emscripten、LLVM、Binaryen、wasm-pack、AssemblyScript。

> 译自：[WebAssembly Still Expanding Frontend Uses 10 Years Later](https://thenewstack.io/webassembly-still-expanding-frontend-uses-10-years-later/)
> 
> 作者：Loraine Lawson

Mozilla、微软、苹果和 [Google](https://cloud.google.com/?utm_content=inline+mention) 宣布 [WebAssembly (Wasm)](https://thenewstack.io/webassembly/webassembly-what-beginners-need-to-know/) 作为一项协作努力已经 10 年了。当时，目标似乎很明确：创建一个低级二进制指令格式，用于编译旧的非网络语言，使其在浏览器中运行。

其用途已 [超出最初的目标](https://thenewstack.io/when-webassembly-replaces-docker/)，但 [Wasm 为前端开发者提供了更多](https://thenewstack.io/webassembly/wasm-for-the-frontend-a-look-at-developer-uses/)。随着九月 Wasm 3 的发布，这个清单进一步扩展。

The New Stack 与 Google 开发者关系工程师 [Thomas Steiner](https://www.linkedin.com/in/thomassteinerlinkedin/?originalSubdomain=es) 讨论了 WebAssembly 的常见用途。

## Wasm 用于业务逻辑

根据 Steiner 的说法，WebAssembly 最流行的应用之一是为应用程序编写业务逻辑，然后通过 WebAssembly 将代码跨平台使用。

Steiner 告诉 The New Stack：“我们看到的一个常见模式是，人们将业务逻辑外包给一个 WebAssembly 模块，然后从各种上下文（context）中引入该模块，这些上下文可以是 Web 应用程序、原生应用程序，有些甚至在服务器端使用应用程序。” “如果你有一个在服务器上运行且不一定需要前端的逻辑，你也可以在那里使用 WebAssembly。”

他提到了 [Snapchat](https://thenewstack.io/snapchat-open-sources-cross-platform-ui-framework/)，他说 Snapchat 在网络和移动平台上有或多或少相同的应用程序。Snapchat 没有为每个平台重新编写业务逻辑，而是用一种语言编写业务逻辑，然后将其转换为 WebAssembly。

他说：“WebAssembly 可以在 Web 上运行，也可以在原生平台上运行。” “他们可以在不同上下文中运行相同的业务逻辑，从而节省大量开发工作。”

## JavaScript 与 WebAssembly

Steiner 说，在许多情况下，WebAssembly 实际上可以比 JavaScript 代码运行得更快。例如，非常计算密集型的任务在 WebAssembly 内部可以运行得更快。

它还可以用于解决连字符问题。JavaScript 不允许在变量和函数名中使用连字符。对于某些语言——例如英语和德语——浏览器已经知道如何处理连字符。

他说：“我们经常看到使用的一个功能是连字符。” “有些语言浏览器不知道连字符规则。”

当这些规则在库中实现，并且开发人员希望在网页上渲染以不受支持的语言编写的字符串时，开发人员可以在 WebAssembly 模块中进行连字符处理，然后将连字符文本输出到网页。

他说：“你输入想要连字符的文本。WebAssembly 模块执行其逻辑，告诉你单词在哪里会断开等等，然后你将这些内容呈现在屏幕上。” “这是一个常见的例子。”

WebAssembly 的另一个常见用例是加密，如果你需要加密或解密某些内容。他补充说，它还可以用于实现已经在其他地方实现的功能。

他说：“例如，我维护一个将栅格图像转换为矢量图像的库。” “你可以想象这是一个相对昂贵的操作，因此通过 WebAssembly，我们可以将处理成本外包给 Assembly，并使其在浏览器中的独立线程中运行。”

这使得开发人员可以拥有一个完全交互式的前端，同时在后台运行计算密集型任务。

## JavaScript 字符串的新方法

[Wasm 3 提供了一种更有效处理 JavaScript 字符串的方法](https://thenewstack.io/wasm-3-0-offers-new-way-to-handle-javascript-strings/)。我们向 Steiner 询问了这一变化的意义。

他说：“这个功能的核心思想是，你有一种语言，比如 JavaScript，它已经内置了处理字符串的功能。”

一个例子是处理 Unicode 字符串，这相当复杂。这种功能已经在 [JavaScript 语言](https://thenewstack.io/javascript/ "JavaScript language")中实现，但如果开发人员想在 WebAssembly 中使用相同的功能，他们需要编译代码并将其转换为 WebAssembly。

新方法提供了一个更简单的选项。

他说：“你可以直接借用 JavaScript 生态中已有的实现，将其导入 WebAssembly，并从那里使用它，从而避免在宿主语言（例如 JavaScript）上进行一些已存在的编译工作。”

新功能创建了一种机制，允许 Wasm 模块直接调用或导入现有的内置 JavaScript 字符串函数。

## 由于垃圾回收而支持的新语言

感谢 [九月 Wasm 3 更新](https://webassembly.org/news/2025-09-17-wasm-3.0/) 中整合的垃圾回收功能，更多高级语言正在增加对 WebAssembly 的支持。根据 WebAssembly.org 博客宣布的改进，Java、OCaml、Scala、Kotlin、Scheme 和 Dart 是目前以 Wasm 为编译目标的语言。

在 Wasm 3 中，WebAssembly 团队增加了对一种新的独立存储形式的支持，该存储形式由 Wasm 运行时通过垃圾回收器自动管理。由于 Wasm 是一种低级语言，Wasm GC 向 Wasm 添加了低级原语，使编译器更容易地将支持垃圾回收的语言作为 Wasm 的目标。

[Wasm 博客文章](https://webassembly.org/news/2025-09-17-wasm-3.0/) 指出：“它可以根据结构体和数组类型以及未装箱的带标签整数来声明其运行时数据结构的内存布局，其分配和生命周期随后由 Wasm 处理。但仅此而已。”“其他一切，例如为源语言值设计合适的表示形式（包括方法表等实现细节），仍然是针对 Wasm 的编译器的责任。”

这意味着没有内置对象系统，也没有闭包或其他高级构造，文章补充说，这些“将不可避免地严重偏向于特定语言”。

文章指出：“相反，Wasm 只提供表示这些构造的基本构建块，并纯粹关注内存管理方面。”

## Wasm、无服务器和后端解放

它也可以用于在前端支持 [无服务器](https://thenewstack.io/forrester-on-webassembly-for-developers-frontend-to-backend/) 功能，尽管 Steiner 指出“无服务器”是一个错误的称呼。

他说：“当然，有服务器，但其理念是服务器不持续运行。”

他说，[开发人员将编写他们的业务逻辑](https://thenewstack.io/what-developers-need-to-know-about-business-logic-attacks/)，WebAssembly 运行时（在服务器上运行）会快速启动，处理请求，然后再次进入休眠状态。

Steiner 说：“WebAssembly 有许多独特的功能，使其在这种上下文中启动非常快。” “这就是为什么在 WebAssembly 生态系统中，许多初创公司也致力于在服务器端支持 WebAssembly。”

他补充说，Fastly 就是其中一家公司。Fastly 是一个边缘云平台，提供内容分发网络（CDN）。他补充说，高性能开源 Web 服务器 [Nginx 也支持服务器端的 Wasm](https://blog.nginx.org/blog/server-side-webassembly-nginx-unit)。

他继续说，有一个完整的服务栈，可以在服务器上通过 WebAssembly 运行所有内容。这使得开发人员可以轻松切换后端提供商，因此开发人员不会被锁定在特定的后端技术栈中。

他说：“只要你的技术栈支持 WebAssembly，WebAssembly 运行时之外的一切你都不需要关心。”

## 编译 Wasm 的工具

如果你发现 Wasm 可能适用于你的应用程序，这里有一些编译到 WebAssembly 的选项。

最流行的工具之一是 **Emscripten**。Emscripten 最初旨在将用 C 和 C++ 编写的视频游戏——特别是名为“Sauerbraten”（在网络上称为“Syntensity”）的第一人称射击游戏——移植到浏览器，由前 Mozilla 工程师、现任 Google 员工 [Alon Zakai](https://www.linkedin.com/in/alonzakai/) 创建。它在 MIT 许可证和伊利诺伊大学/NCSA 开源许可证下都是开源的。它利用了 Binaryen 并且是一个基于 LLVM/Clang 的编译器。

根据 [KodeKloud Notes 的 Wasm 入门课程](https://notes.kodekloud.com/docs/Exploring-WebAssembly-WASM/Compiling-to-WebAssembly/WASM-Compilers)，**LLVM** 可用于编译到 WebAssembly，以支持后端和优化。它支持 C、C++ 和 Rust 的前端，利用先进的分析和转换。

根据 KodeKloud 的说法，[**Binaryen**](https://github.com/WebAssembly/binaryen) 允许开发人员汇编、优化和转换 Wasm 二进制文件，这使其成为最小化代码大小和微调低级性能的理想选择。

[**wasm-pack**](https://github.com/drager/wasm-pack) 可以编译、测试并将基于 Rust 的 Wasm 包发布到 npm。

[**AssemblyScript**](https://www.assemblyscript.org/) 提供了一种 [TypeScript](https://thenewstack.io/typescript-5-9-brings-less-friction-more-features/) 风格的语法，可以直接编译到 Wasm。根据 KodeKloud 的说法，它公开了 WebAssembly 特定的类型（例如 i32、f64），以实现可预测的性能。