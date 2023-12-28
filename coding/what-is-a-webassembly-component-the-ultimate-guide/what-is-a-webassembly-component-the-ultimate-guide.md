<!--
title: WebAssembly终极指南
cover: https://cdn.thenewstack.io/media/2023/12/93c12a7d-puzzle-1713170_1280-1024x539.jpg
-->

WebAssembly 组件在运行在 WebAssembly 模块内部的运行时部署中发挥着关键作用。然而，其标准化仍在进行中。

> 译自 [What Is a WebAssembly Component? The Ultimate Guide](https://thenewstack.io/what-is-a-webassembly-component-the-ultimate-guide/)，作者 B. Cameron Gain。

## 什么是 WebAssembly 组件？

WebAssembly 组件在运行时位于 WebAssembly 模块内部的运行时的部署中起着关键作用。但其标准化仍在制定中。

一旦最终确定下来，[组件模型将使 WebAssembly](https://thenewstack.io/can-webassembly-get-its-act-together-for-a-component-model/) 不仅能扩展其在 Web 浏览器和服务器之外的使用，而且能够允许用户通过称为 WebAssembly 系统接口(WASI)的组件接口，在数以千计的端点上同时以极高的速度部署运行在众多轻量级模块内的不同应用程序，而无需对代码做任何改变。

这至少在理论上是这样，但同时，社区正在努力实现这一目标。与此同时，关于[组件是什么以及它如何影响 WebAssembly 的采用](https://thenewstack.io/can-kubernetes-solve-webassemblys-component-challenges/)，存在很多困惑。

## WebAssembly 和组件如何协同工作？

在深入探讨什么是组件以及其功能之前，我们首先需要[描述一下什么是 WebAssembly](https://thenewstack.io/webassembly/what-is-webassembly-and-why-do-you-need-it/)，以及其演变如何导致了对组件模型的需求，特别是它与 WASI 的关系，WASI 是链接 web assembly 模块与组件的标准接口或 API。

WebAssembly 旨在[部署](https://thenewstack.io/webassembly/using-web-assembly-written-in-rust-on-the-server-side/)以开发者选择的语言编写的应用程序，以便同时在各种不同的环境中部署。这里的“不同”是指 [WebAssembly 在 CPU 上运行，只需要能够运行 CPU 指令集的设备](https://thenewstack.io/why-webassembly-is-perfect-for-tiny-iot-devices/)、服务器等。

这意味着单个 WebAssembly 模块中的应用部署在理论上应该能够在多种不同的设备上运行和更新，包括服务器、边缘设备、多云、无服务器环境等。

只要有能运行指令集的 CPU，WebAssembly 就旨在运行越来越多它可以托管在模块中的语言编写的应用程序。它现在可以容纳 Python、JavaScript、C++、Rust 等。

用不同编程语言编写的不同应用程序应该能够在单个模块内共存，尽管这种功能仍在大规模开发中。

本质上，一个装满微服务的模块应该能够在各种环境中部署多个服务，并提供应用程序更新，而无需重新配置端点。

理论上，这仅仅是配置模块中的应用程序的问题，这样模块部署的每个环境在模块内完成工作后都不需要单独重新配置。但是，这也取决于组件标准的最终确定。

## 我们如何从 Web 模块到具有组件的服务器？

现在，正如我们在 Kubernetes 和 Docker 中观察到的那样，同时在所有地方部署应用程序的愿望取决于标准化组件模型。

这个模型通常被比作乐高块。这些组件通过 WASI 充当 web assembly 模块提供运行时的接口。这些组件被堆叠在一起，将它们链接在一起以利用各种 WebAssembly 运行时的通用性和效用，形成由组件组成的统一软件包或单元。

这种方法的妙处在于它提供的安全性，就像 Kubernetes 确保组件不在内存、命名空间或命名空间分配中共享数据一样。它们通过 WebAssembly 机器人模块维护封闭或[沙盒接口](https://thenewstack.io/how-webassembly-offers-secure-development-through-sandboxing/)。

但是，实现标准化是挑战；使组件能在任何系统上运行是目标。这将允许 web assembly 模块与组件无缝交互，在 CPU 指令集上进行部署和运行。虽然它被配置为针对任何遵循标准的模块执行此操作，但这个标准仍在进行中，代表着 WebAssembly 旅程的最后一英里。

目前，组件开发在开源社区推进 WebAssembly 的努力中发挥着关键作用。标准组件接口正在以一种创新方式建立，预示着无限可能的世界。

许多开源项目和研究计划都在为这一最终确定过程做出贡献。对于开发人员来说，特别是类似 Kubernetes 的开发人员，组件开发的内部工作机制可能不会引起太大兴趣。他们主要寻求最终结果：[随着 WebAssembly 与 Kubernetes 的日益集成](https://thenewstack.io/webassembly/yes-webassembly-can-replace-kubernetes/)，按照意愿部署应用程序的能力。

这可能会让您想起 20 世纪 80 年代和 90 年代 DOS 的出现，当时大量书籍深入探讨了文件交互、配置和 DOS 命令。但是，对于大多数程序员和软件工程师来说，理解这些复杂性并不关键，特别是考虑到 Unix 和 Linux 在软件开发景观中的占主导地位。

## 组件由什么组成？

在 9 月举行的 WasmCon 的主题演讲中，Fastly 的杰出工程师 [Luke Wagner](https://twitter.com/luke_wagner?lang=en)，[Fastly](https://www.fastly.com/) 在其边缘交付平台的某些服务中极重视 WebAssembly，用一句话描述了 Wasm 组件是什么：一个正在出现的、标准的、便携式的、轻量级的、精细沙盒化的、跨语言的和组合模块。

他解释说，组件是一个包含导入、内部定义和导出的模块。导入包括导入的函数(例如日志函数)等元素，并且通常捕获组件提供的 I/O 及其实现依赖项，而不是依赖于一组固定的系统调用或固定的运行时全局命名空间。

内部定义表示运行的核心代码，主要由嵌入式Wasm模块组成，“这里存放了99%的字节数。内部定义也可以调用导入，”Wagner说。

“组件可以进一步嵌套其他组件，使它们本质上具有递归性，”Wagner说。“最后，导出通过为名称和类型赋值，使组件的内部定义和导入对客户端公开。”

在容器世界中，[开放容器接口](https://opencontainers.org/)(OCI)定义了可分发容器的标准。Docker构建从源创建容器，Docker运行和Kubernetes运行以及部署它，用于共享和组合，Docker推送和Docker组合发挥作用，Wagner说。

“所以一个自然的问题出现了：我们可以为此目的使用Wasm吗？”Wagner问道。“它无疑是一个标准的可分发格式，但挑战在于Wasm主要支持共享内存链接。当我们想将两个Wasm模块链接在一起时，它们通常需要共享内存才能通过该共享内存传递复合值，这类似于操作系统的DLL或共享对象。”

然而，当组合两个或多个WebAssembly模块时，它们应该保留自己的单独内存，这些内存不共享，Wagner说。需要一种在它们之间传递复杂值和转移所有权的方法，这些值不能在它们之间复制，类似于操作系统可执行文件，他说。

**是否有可能用便携式操作系统接口(POSIX)封装Wasm模块来创建Wasm可执行文件？**

分发单个 POSIX 可执行文件通常是不够的，因为我们通常需要分发必须协同工作的一组可执行文件，以及配置文件、静态资产和目录结构，Wagner说。Wagner说，一种解决方案可能是将 Wasm 模块捆绑到以 Wasm 为核心指令集的容器中。

“尽管这种方法可能有用，但它没有解锁我们设想的激动人心的新使用案例，”Wagner说。“为实现这一点，我们需要一些新的东西，一个 Wasm 的包装器，允许我们使用现有的编译器。我们正在提出并称为“组件”的这个新概念。”

## 接下来会发生什么？

必须牢记，由于 WebAssembly 的独特功能，业务模型正在其上建立，这在很大程度上取决于组件模型的最终确定。

Wagner说，[已经有开发人员选择 Wasm](https://thenewstack.io/webassembly/wasm-for-the-frontend-a-look-at-developer-uses/) “运行在其他情况下无法运行的代码”。

“这让我们构建一套可重用的工具，以支持第一波语言和 API。但因为这些工具不仅仅耦合到一个平台，它们通常使用组件模型，现在我们可以吸引一波新的平台构建者，他们正在利用这个元生态系统，获得很多自己不必构建的东西，”Wagner说。

"这可以吸引一大批新一代的开发者，他们目前选择使用 WebAssembly 是因为其易于重用和在所有这些可重用组件中提高生产力。然后，这可以引导我们构建一整套新的工具，使我们能够从组件中组合应用程序，并创造一种全新的开发者编程模型。”

需要牢记的是，由于其独特的能力，围绕 WebAssembly 正在形成各种业务模式，而其中很大一部分取决于最终确定的组件模型。

目前，开发者选择使用 WebAssembly 是为了“运行在其他情况下无法运行的代码”，正如 Wagner 所强调的那样。这促使了一套可重用工具的开发，旨在支持第一波的语言和 API。

由于这些工具不受限于单一平台，它们广泛采用组件模型。因此，一批新一代的平台构建者进入了这一领域，利用这个元生态系统，并获得了许多无需从头开始开发的资源。

因此，一批新一代的开发者被吸引到 WebAssembly，他们被其易于重用的特性和通过这些可重用组件提供的高生产力所吸引。这反过来又导致了一套新的工具的开发，用于从组件中组合应用程序，并创建一种全新的开发者编程模型。

## 这些发展的当前状态如何？

Wagner 表示，正在制定一个正式的规范，其中包括操作语义、一个参考解释器和一个参考测试套件。使用 BindGen 和 Wasm 工具已经在 Wasm 时间中实现了很大部分。预计在明年初将达到的一个重要里程碑是与完全参数化链接、值、资源和句柄类型同步的组件。

随后的主要里程碑是将未来和流程添加到组件模型中，引入异步支持。Wagner 表示：“这将是一个具有挑战性的步骤，但将简化许多本来需要重复完成的工作。最后，还有一些剩余的元素需要完成组件模型的 MVP，例如可选的导入和导出。”
