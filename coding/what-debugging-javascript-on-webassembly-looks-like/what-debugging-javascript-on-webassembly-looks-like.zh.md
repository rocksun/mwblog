[WebAssembly](https://thenewstack.io/webassembly/) (Wasm) [调试](https://thenewstack.io/master-the-art-of-python-debugging-with-these-tips/) 仍然是一项挑战，这是可以理解的，因为这项相对较新且令人兴奋的技术仍在发展中。最初设计用于浏览器，它在该环境中运行良好，特别是对于从另一个浏览器中调试 Web 应用程序。[Emscripten](https://thenewstack.io/how-to-compile-c-code-into-webassembly-with-emscripten/) 作为工具链编译器以及 Firefox 和 Chrome 中内置的扩展，为在浏览器中运行的 Wasm 提供了相当可靠的调试。

然而，超越浏览器——特别是到后端用例以及跨不同环境和语言的部署——调试变得更加复杂。尽管存在这些挑战，但已经取得了进展。

去年，在 Wasm I/O 2024 期间，当时提出的调试讨论与 [Wasm I/O 2025](https://2025.wasm.io/) 中的讨论形成了鲜明对比，当时 Microsoft 的 [Ralph Squillace](https://github.com/squillace) 将前端和后端的 JavaScript 调试状态描述为“令人尴尬”。

## 挑战

在 Wasm I/O 2024 的演讲 “Nobody Knows the Trouble I’ve Seen: Debugging Wasm for web and server” 中，Microsoft 的 [Natalia Venditto](https://www.linkedin.com/in/anfibiacreativa/) 和 Squillace 描述了由于缺乏浏览器之外的 Wasm 代码的标准 API，特别是在后端，调试方面持续存在的挑战。正如 Venditto 在她的演讲中所说，出现了两个挑战：

首先，确定 WebAssembly 模块内部应该包含什么，以及 JavaScript 标准中应该保留什么。[JavaScript](https://thenewstack.io/introduction-to-javascript/) 其次，管理调试过程。可能存在多个层，并且访问这些层可能并不简单。“可能需要新的知识，” Venditto 说。

正如 Venditto 指出的那样，当被问及首选代码编辑器时，几乎 100% 的 JavaScript 开发人员都选择 [VS Code](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/)。她说，在整个工作流程中，首选环境保持一致：在构建、部署和云调试期间。

“浏览器仍然是 JavaScript 开发人员的核心环境。此环境提供了熟悉度、众所周知的工具和高效的工作流程，” Venditto 说。

Venditto 描述了一个 JavaScript 开发人员希望在应用程序中使用 WebAssembly 并管理整个工作流程的场景。挑战包括：首先，确定 WebAssembly 模块内部应该包含什么，以及 JavaScript 标准中应该保留什么；其次，管理调试过程。“可能存在多个层，并且访问这些层可能并不简单。可能需要新的知识，” Venditto 说。尽管存在这些挑战，“在熟悉的环境中构建仍然很重要，” Venditto 说。

## SpiderMonkey 和 VS Code

快进到 2025 年 Wasm I/O，在由 Squillace 和 Fermyon 的 [Till Schneidereit](https://www.linkedin.com/in/tillschneidereit/?originalSubdomain=de) 做的演讲 “No More Printf: Interactive Debugging Wasm for Web and Server” 中。讨论的重点是使用 [SpiderMonkey](https://thenewstack.io/python-meets-javascript-wasm-with-the-magic-of-pythonmonkey/) 引擎和 Visual Studio Code 调试 WebAssembly 中的 JavaScript。关键点包括使用 components.as.js 生成调试绑定、套接字连接对于远程调试的重要性以及无需重新部署即可进行调试的能力。演讲者强调了跨不同语言（包括 [.NET](https://thenewstack.io/net-modernization-github-copilot-upgrade-eases-migrations/) 和 [Python](https://thenewstack.io/what-is-python/)）统一调试体验的需求，以及在多语言环境中跨组件启用调试的目标。会议还涵盖了在 VS Code 中使用启动配置进行调试以及在实时环境中进行部署后调试的潜力。

Squillace 对调试工具的进步表示热情，特别强调了 [C++](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/) 和 [静态分析工具](https://thenewstack.io/how-static-analysis-can-save-your-software/) 的集成。他提到了过去一年中遇到的先前挑战，并注意到摆脱了对本机代码的依赖。

Schneidereit 强调了 Fermyon 调试 WebAssembly 的方法。他澄清说，重点不是为 WebAssembly 字节码构建新的调试器，而是利用现有的工具，如 SpiderMonkey。这种方法避免了直接检查字节码的需要，从而降低了 DWARF 和 LLDB 等工具的有效性。相反，采用了 SpiderMonkey 中内置的内容调试器，通过套接字接口连接到 Visual Studio Code 等外部调试器。这种方法对于生产版本证明是有益的，消除了对嵌入式调试符号或禁用优化的需求。此外，它不特定于任何特定的运行时，不像其他需要全面的基于 DWARF 的调试实现的解决方案，Schneidereit 说。

该演示展示了运行在 Jacob 处理的组件上的 Node.js，Jacob 将主要的 JavaScript 配置文件转换为一组 WebAssembly 模块，并附带 JavaScript 胶水代码。此设置使在 Node.js 中执行成为可能，Node.js 缺少本机模块支持。默认情况下，Jacob 使用端口 8000，从而可以在 Node.js 中的 WebAssembly 组件内的 SpiderMonkey 中运行 JavaScript 的相同管道。这种配置允许跨不同环境保持一致的调试体验，包括单步执行代码和命中断点，Schneidereit 说。

这种方法的一个显着优势是只需要一个传出的套接字连接，而不需要运行套接字服务器，Schneidereit 说。传统的调试通常涉及在被调试的设备上运行调试服务器，例如在 iOS 或 Android 应用程序中。相比之下，此方法反转了该过程，仅需要传出的连接，从而简化了远程调试。此功能允许通过发送带有身份验证密钥的特殊请求在实时环境中进行部署后调试，连接回环境而无需重新部署，Schneidereit 说。

接下来的步骤包括与其他编程语言（包括 .NET 和 Python）协调，旨在统一跨不同平台的调试体验，Schneidereit 说。目标是启用相同的扩展，理想情况下是在 Visual Studio Code 中，以调试各种语言。由于使用的协议不需要 Visual Studio Code 识别被调试的特定语言，因此它只需要接收有关堆栈布局和其他调试信息的适当消息，Schneidereit 说。

“这项工作背后的一个重要动机是为标准化解决方案铺平道路，其中运行时在促进统一的调试工作流程中发挥作用。目前，该方法完全包含在内容中，这限制了在组件之间无缝切换的能力，” Schneidereit 说。

鉴于组件模型强调从各种语言的不同构建块中组合应用程序，“最终目标” 是提供一种跨越这些组件的调试体验，Schneidereit 说。“这将允许开发人员从其他组件单步执行导入的函数，在不同的语言之间平滑过渡，例如从 JavaScript 移动到 C#，” Schneidereit 说。“希望在不久的将来实现这种集成的调试功能。”