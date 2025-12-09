偶尔，在大型会议上会发布一些特别有趣的项目或版本，它们往往没有市场营销支持，也不是由大型企业团队推出。在 [KubeCon + CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 上，卡内基梅隆大学的博士研究生 Elizabeth Gilbert 介绍了一个名为 [Whamm](https://ejrgilbert.github.io/whamm/) 的项目，它只需一行代码即可开箱即用。它不替代、不改善、不优化现有工具和流程，但却能实现以前从未真正存在过的功能。

Gilbert 对她创建的这个项目进行了出色的描述，在她之前提到的演讲 [“Whamm：一个用于高性能、沙盒化插桩的框架”](https://colocatedeventsna2025.sched.com/event/28D4w/whamm-a-framework-for-performant-sandboxed-instrumentation-elizabeth-gilbert-carnegie-mellon-university) 之后，该项目获得了大量的下载和分支。该演讲是在 [CNCF](https://cncf.io/?utm_content=inline+mention) 主办的 KubeCon + CloudNativeCon 协同活动 [WasmCon](https://colocatedeventsna2025.sched.com/overview/type/ArgoCon) 上进行的。

Whamm 旨在允许用户使用编程语言或代码对其 [WebAssembly](https://thenewstack.io/webassembly/)（简称 Wasm）应用程序进行插桩，或者直接在模块中编写 WebAssembly 应用程序。借此，他们可以在 WebAssembly 模块内调试、监控等其应用程序。

Whamm 最初在一篇题为 [“WebAssembly 的灵活非侵入式动态插桩”](https://dl.acm.org/doi/10.1145/3620666.3651338) 的论文中被介绍，它被描述为一个用于“Wasm 应用程序监控和操作”的框架。在 Gilbert 的 [GitHub 页面](https://ejrgilbert.github.io/whamm/)上，她这样描述 Whamm 的插桩、监控和字节码重写功能：

*   **插桩 (Instrumentation)：** 当我们说“对程序进行插桩”时，在宏观层面，我们的意思是“将一些代码注入到程序的执行中以执行某些操作”。这个定义是故意泛化的，因为插桩确实可以做我们能想象到的任何事情！你可以使用插桩来构建调试器、动态分析工具、遥测生成器等等。
*   **动态分析 (Dynamic analysis)：** 动态分析是在程序执行时对其进行分析（与分析未运行程序的静态分析相对）。这种类型的分析可以深入了解程序，因为它能够访问静态分析无法获得的信息（例如热点代码位置、随时间变化的内存访问、测试套件的代码覆盖率等）。
*   **字节码重写 (Bytecode rewriting)：** 这是一种将插桩逻辑注入到应用程序中的示例策略。它通过字面上将新指令插入到应用程序字节码中来实现插桩。

“插桩实际上是一种观察应用程序行为的方式，这是一个足够灵活的定义，可以涵盖所有不同的事情。它可以是可观测性，但也可以用于测试用例，例如故障注入测试，”Gilbert 在她的演讲结束后在 KubeCon + CloudNativeCon 上告诉我。“你可以向应用程序注入故障，看看它是否能够正确处理。插桩也可以用来操纵应用程序的执行方式。”

正如 Gilbert 所解释的，专注于 WebAssembly 的主要动机是语言互操作性。“由于多种不同的语言都可以编译成 WebAssembly，这就是工具如此酷炫的原因。如果你有与语言无关的工具，那么如果出现某种新的编程语言，只要它能编译成 WebAssembly，你就可以免费获得所有工具，”Gilbert 说。“这种多语言的可能性对很多人来说都非常、非常棒。随着 Wasm 被更广泛地采用，如果我们在插桩方面有所发展，那么所有的开发工具都可以免费获得，并且该平台可以与各种不同的事物连接。”

Gilbert 表示，该项目目前的状况是“可以做很多事情，但需要开发更多的用例以使其更健壮”。“该项目目前一直在独立进行。如果有更多的人，尤其是工程师的贡献，那将是‘非常棒的’，因为这样工作可以更快地进展。”

确实，我预计会有许多工程师寻求为 Whamm 做出贡献并从中受益。