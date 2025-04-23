<!--
title: GraalVM（最终）获得了用于 WebAssembly 的 Java
cover: https://cdn.thenewstack.io/media/2025/04/74984e01-daniel-dan-fj11x2c4ui8-unsplash.jpg
summary: 重磅！GraalVM 终于支持 Java 编译为 WebAssembly (Wasm) 模块啦！🚀 这对 Java 和 Wasm 都是巨大利好，加速企业级应用Serverless化和边缘计算。利用 GraalWasm 和 WasmGC，实现 Java 与 JavaScript 对象互操作，性能 up up！拥抱云原生，Java “一次编写，随处运行”的时代来了！
-->

重磅！GraalVM 终于支持 Java 编译为 WebAssembly (Wasm) 模块啦！🚀 这对 Java 和 Wasm 都是巨大利好，加速企业级应用Serverless化和边缘计算。利用 GraalWasm 和 WasmGC，实现 Java 与 JavaScript 对象互操作，性能 up up！拥抱云原生，Java “一次编写，随处运行”的时代来了！

> 译自：[GraalVM (Finally) Gets Java for WebAssembly](https://thenewstack.io/graalvm-finally-gets-java-for-webassembly/)
> 
> 作者：B Cameron Gain

巴塞罗那 — [GraalVM](https://thenewstack.io/how-to-build-with-graalvm-inside-github-actions/) 现在受益于 WebAssembly ([Wasm](https://thenewstack.io/webassembly/)) 后端，因此 [Java](https://thenewstack.io/introduction-to-java-programming-language/) 代码和应用程序可以直接编译成 Wasm 模块。 这被视为一项重大发展和里程碑，该发展不仅对 Java 用户来说是一个潜在的福音，而且对 [WebAssembly](https://thenewstack.io/why-webassembly-will-disrupt-the-operating-system/) 的整体发展也是如此。

“这对 Java 和 Wasm 来说都是好消息。 它扩大了 WebAssembly 的主流采用，尤其是在 Java 盛行的企业环境中，” Endor 的首席执行官 [Daniel Lopez](https://x.com/vomkriege?ref_src=twsrc%5Etfw) 说道。Endor 是一家初创公司，可以让你在浏览器中运行服务器端软件，他也是 Bitnami 的联合创始人兼前任首席执行官。他在上个月的 [Wasm I/O 2025](https://2025.wasm.io/) 上告诉 The New Stack。“它还有助于 Java 在许多新场景中的采用，例如浏览器。”

到目前为止，Java 一直是一个被忽视的孩子。 WebAssembly 模块在许多原因上更有利——我们不会在这里讨论——[C 和 C++](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/)、[Rust](https://thenewstack.io/rust-programming-language-guide/) 和 [Go](https://thenewstack.io/introduction-to-go-programming-language/)，甚至现在的 [Python](https://thenewstack.io/python/) 也被嵌入为解释器。

Java 是一种受欢迎的开发者语言，但社区长期以来一直试图解决它的缺点，例如不太理想的延迟规范，以及与其他编程语言相比相对的笨重性，尤其是在浏览器、serverless、边缘计算和其他用例中运行应用程序时。

当然，WebAssembly 提供了可以被描述为几乎零延迟的东西，有时仅以几分之一毫秒来衡量。 它不仅在浏览器中获得了关注，在浏览器中它已经存在了十多年，而且随着它向边缘计算的扩展，它也获得了关注。

开源 [Chicory](https://thenewstack.io/chicory-write-to-webassembly-overcome-jvm-shortcomings/) 的创建是为了将 Wasm 的一些好处带给原生 [JVM](https://thenewstack.io/how-do-javas-virtual-threads-help-your-business/)，并带来了 WebAssembly 模块提供的安全性、隧道和隔离方面（或沙盒功能，用行业术语来说）。 作为一种 VM 原生的 WebAssembly 运行时，Chicory 旨在使 WebAssembly 程序能够在没有原生依赖项或 Java Native Interface (JNI) 的情况下运行。 换句话说，虽然 Chicory 以前是一个出色的纯 Java Wasm 解释器，具有轻量级功能和零依赖性，使其具有超强的可移植性，但 [GraalWasm](https://www.graalvm.org/webassembly/docs/) 提供了你可能不一定想使用 Chicory 的用例。

> 🧩 一次编写，随处运行的未来：从 Java 到 WebAssembly，作者：
>
> [@_patrickziegler]&[@fniephaus]@ Wasm I/O 2025▶️ 视频：
>
> [https://t.co/Qs8xBdq4RB](https://t.co/Qs8xBdq4RB) 🔗 幻灯片：
>
> [https://t.co/LTvqSrB9v2](https://t.co/LTvqSrB9v2) [#wasmio25] [@graalvm]
> — Wasm I/O (@wasm_io),April 22, 2025

以前，通过 GraalVM（Oracle 和其他供应商维护）执行 Java 的 WebAssembly 缺少垃圾收集功能，这些功能对于 Java 的内存管理、即时编译、动态调度功能和其他功能至关重要。 但是，正如在 GraalVM 上工作的 Oracle 工程师 [Patrick Ziegler](https://2025.wasm.io/speakers/patrick-ziegler/) 和 [Fabio Niephaus](https://www.linkedin.com/in/fniephaus/details/education/) 在他们的演讲 [一次编写，随处运行的未来：从 Java 到 WebAssembly](https://www.youtube.com/watch?v=Z2SWSIThHXY&ab_channel=WASMI%2FO) 中所展示的那样，GraalVM 和 GraalWasm 已被证明可以克服这些挫折。

“WebAssembly 消除了在任何地方（从数据中心到浏览器再到 IoT 设备）部署代码的摩擦，并将其变成了一种无缝体验，” TechTarget 的企业战略集团分析师 [Torsten Volk](https://www.linkedin.com/in/torstenvolk) 告诉我。“支持 WebAssembly 是 Java 及其社区摆脱其传统形象的关键一步，因为它不仅使 Java 能够在边缘运行，而且还简化了 Java 应用程序与任何支持 Wasm 的语言的应用程序的组合。”

## 演示

![](https://cdn.thenewstack.io/media/2025/04/d7220d5d-capture-decran-2025-04-22-194707.png)

在启用 GraalVM 以进一步适应 Java 的后端工作中，涉及了 [WasmGC](https://github.com/WebAssembly/gc) 提案和异常处理，Ziegler 在他的演讲中提到。“这使得将 Java 映射到 Wasm 变得容易得多，”Ziegler 说。“每个 Java 类型都表示为一个 WebAssembly 结构，异常处理也是如此，对吧？基本上，它几乎一对一地映射到 WebAssembly。这在很大程度上降低了复杂性，也有助于减小代码大小。”

正如 Ziegler 解释和展示的那样，用 Java 编写的 HelloWorld 脚本可能大约为 1 MB。“这看起来很大——当然，它确实很大——但对于 Java 程序来说，它并不算大，”Ziegler 说。“此外，这是在您应用压缩或运行 WasmOpt 之前。如果您执行所有这些操作，您可以轻松地将大小缩小到大约 300 KB。”

由于 WasmGC，具有 Java 的 JavaScript 对象现在可以与 GraalVM JavaScript 互操作性 API 共享。虽然所有交互都由 Java 代码支持，“每个按钮都有一个调用 Java 代码的事件侦听器，该代码执行实际的编译，”Ziegler 说。

“该 API 可以处理所有不同类型的转换。它可以管理方法调用等等，”Ziegler 说。“如果您以 JS 嵌入为目标，那么您可以做很多事情。”

另一个好处是 Java 标准库或 JDK 的可用性。“当然，并非所有功能目前都能正常工作，”Ziegler 说。“如果调用线程、网络和图形等功能，目前会引发异常。但这一切都是循序渐进的。”

![](https://cdn.thenewstack.io/media/2025/04/a8bd6f4d-capture-decran-2025-04-22-182619-1024x417.png)

一个名为 [GraalJS](https://www.graalvm.org/latest/reference-manual/js/) 的 JavaScript 运行时也可用，它实现了 WebAssembly ES 模块集成。这意味着您可以使用 JavaScript 绑定来促进 Java 和 WebAssembly 之间的高级通信，Niephaus 在本次演讲中说。“无论 wasm-bindgen 吐出什么，您都可以使用它从 Java 到 JavaScript，然后从 JavaScript 到 Wasm 进行接口，”Niephaus 说。

## 完整的循环

如上所述，Java 明显地缺席了 WebAssembly 对语言的处理或其多语言功能。除了 Rust、C 和 C++ 等低级语言以及 JavaScript 等更抽象的语言外，WebAssembly 目前还支持一系列语言。通过 GraalVM，用户可以在 WebAssembly 中运行 Java，这不仅对 WebAssembly 的使用可能是一个福音，而且对非常庞大的 Java 开发人员和用户社区也是如此。

Fermyon 联合创始人兼首席执行官 Matt Butcher 在最近的 [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 期间告诉我：“我认为这个消息让我们这些语言爱好者如此兴奋的原因是，我们看到一直在引导 Java 的组织采用了最酷的虚拟机技术之一——GraalVM——并拥抱了 WebAssembly 标准。”“这真的很令人兴奋。”

Volk 说，Sun Microsystems 最初将 Java 营销为一种“一次编写，随处运行”的语言。“虽然这个承诺在服务器和桌面领域表现良好，但它在边缘领域却失败了。Java 虚拟机对 CPU 和内存的需求对于受限环境来说实在太大了，”他说。“输入 WebAssembly：它是最终兑现原始 Java 承诺的颠覆者，但没有包袱，具有更小的二进制文件、闪电般的启动时间、精简的内存需求以及选择编程语言的自由。WebAssembly 消除了在任何地方（从数据中心到浏览器再到 IoT 设备）部署代码的摩擦，并将其变成了一种无缝体验。”

Volk 说，GraalVM 对 WebAssembly 的扩展支持是“Java 及其社区摆脱其传统形象”的关键举措。“这不仅使 Java 能够在边缘运行，而且简化了 Java 应用程序与任何支持 Wasm 的语言的应用程序的组合，”他说。

自引入 WebAssembly 以来，Oracle 一直被认为意识到激发 Java 在 WebAssembly 中使用的潜力，但它并没有努力拥抱它以服务 Java 社区。（Oracle 公关代表没有回复 The New Stack 通过电子邮件发送的查询。）

Butcher 说：“多年来，Oracle 一直在引导 Java 项目。当 WebAssembly 首次出现时，Oracle 的担忧——或者甚至可能不是 Oracle 的担忧，而是 Java 社区的最初反应——是，‘等等，这只是另一种字节码，就像 Java 字节码一样。我们为什么要试图重新发明我们花了二十多年时间完善的技术？’”“我认为很明显，它们足够不同，并且有足够不同的用例——其中之一是支持组件模型，但另一个是在每种情况下获得的不同的性能配置文件。”
社区逐渐开始将 WebAssembly 视为“威胁性较小”的技术，Butcher 说。“Java 在虚拟机方面做了一些了不起的事情，而 GraalVM 已经成为以性能为中心的 Java 虚拟机的佼佼者，”Butcher 说。“因此，很高兴看到 Oracle 以 GraalVM 为基础贡献 WebAssembly 支持。”

“我知道用‘技术落后者’这样的词听起来很刺耳，但由于他们最初不愿接受 WebAssembly，他们在采用它方面甚至落后于 .NET、Python、Ruby、Rust 和 Go，”Butcher 说。“但既然他们已经发布了这个公告，我认为最大的收获是，整个 WebAssembly 生态系统现在已经得到了每一个主要语言社区的验证——从 Swift、Rust 和 Go 这些更新、更闪亮的语言，到 C、Java 和 .NET 这些经典的的企业阵容。”