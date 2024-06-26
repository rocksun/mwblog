# WebAssembly 用于服务器端：NGINX 的新方式

翻译自 [WebAssembly for the Server Side: A New Way to NGINX](https://thenewstack.io/webassembly-for-the-server-side-a-new-way-to-nginx/) 。

Wasm 通过更灵活和可管理的方式，彻底颠覆了标准插件模型。它们可以是语言和硬件中立的、模块化的和隔离的。

![](https://cdn.thenewstack.io/media/2023/04/d4d7c7f4-block-1024x772.jpg)

这是一个两部分系列的第一部分。

WebAssembly（Wasm）的迅猛崛起始于它是一种与语言无关的运行时环境，可在浏览器中安全快速地执行除 JavaScript 以外的其他语言。尽管 Wasm 最初的重点是在浏览器上，但开发人员已经开始探索将其用于后端的可能性，在那里它为服务器和网络管理打开了许多可能性。

类似于 NGINX，许多服务器端技术都采用标准插件模型，该模型依赖于静态或动态注入链接的对象文件到在同一地址空间运行的可执行文件中。

然而，插件有相当大的局限性。特别是，它们通过原生语言扩展来实现可扩展性，这限制了开发者在语言和语言特定功能方面的选择。其他插件必须符合复杂的链接方法，需要服务器和客户端语言都支持相同的功能接口。这可能会增加插件创建者的复杂度。

最后，一些插件通过动态语言和脚本层工作。这些更容易使用但牺牲了性能。动态脚本可以引入抽象层以及额外的安全风险。例如，远程过程调用（RPC）必须解决网络通信、序列化和反序列化、错误处理、异步行为、多平台兼容性以及延迟等问题时会带来挑战。虽然使用 RPC 的插件是灵活的，但代价是极大地增加了复杂性。

## 为什么 Wasm 很棒：快速、安全、灵活

那么，什么是 Wasm ？ Wasm 是一种二进制格式和运行时环境，用于执行代码。简而言之， Wasm 被创建为以接近本地速度的低级、高效和安全的方式来运行代码。  Wasm 代码旨在从诸如 C、C ++、Golang 和 Rust 等高级编程语言编译而成。实际上，Wasm 与语言无关且可移植。随着部署和维护应用程序的开发人员越来越倾向于尽可能使用单一语言（换句话说，减少YAML），这变得更加重要。

Wasm 通过允许更灵活和可管理的插件，彻底颠覆了标准插件模型。使用 Wasm ，使插件具有比现有的插件模型要容易得多的语言中立性、硬件中立性、模块化和隔离性。这使开发人员能够使用所选择的语言，在浏览器之外定制行为，以适应其环境和用例需求。

Wasm 通过以下方式实现了所有这些，同时保持接近原生代码水平的性能： 

* 一种比等效的人类可读代码更小的紧凑二进制格式，从而加快下载和解析时间。
* 更接近原生机器指令的指令集，允许更快地解释和编译为本机代码。
* 具有强类型的极快 JIT，通过应用各种优化技术提供更好的优化机会，以加快代码生成和执行速度。
* 一种连续的、可调整大小的线性内存模型，可简化内存管理，从而实现更高效的内存访问模式。
* 释放多核处理器性能的并发和并行执行（目前正在实现中）。

Wasm 最初设计用于在网络上运行不受信任的代码，它具有特别强大的安全模型，其中包括：

* 一种沙盒代码执行环境，限制其对系统资源的访问并确保它不会干扰其他进程或操作系统。
* 一种“内存安全”架构，有助于防止常见的安全漏洞，例如缓冲区溢出。
* 一个健壮的类型系统，执行严格的类型规则。
* 与其他运行时相比代码量小，减少了攻击面。
* 一种旨在易于分析和优化的字节码格式，可以更轻松地检测和修复潜在的安全漏洞。
* 由于其高度的可移植性，对不同平台重构代码的需求极少。

## 一种更灵活的构建插件的方式

服务器端的 Wasm 具有许多令人印象深刻的潜在优势，包括主要和次要的。首先，使用 Wasm 环境可以使标准应用程序开发人员更轻松地与后端系统交互。 Wasm 还允许任何人为函数设置细粒度防护措施，以限制其尝试与网络或服务器端应用程序的低级功能进行交互时所能做和不能做的事情。这很重要，因为后端系统可能正在与敏感数据进行交互或需要更高水平的信任。

同样地，服务器系统可以配置或设计为通过显式导出仅有限的功能或仅提供特定文件描述符来限制与 Wasm 插件环境的交互。例如，每个 Wasm 字节码二进制文件都有一个导入部分。在实例化之前必须满足每个导入要求。这使得主机系统能够注册（或按照 Wasm 术语导出）特定函数以作为系统进行交互。

当这些导入不满足时，运行时引擎将阻止 Wasm 模块的实例化，从而使主机系统能够保护、控制、验证和限制客户端与环境的交互。

使用更传统的插件模型和编译器技术来创建这种细粒度和实用级别是一项挑战。高难度程度会使开发人员望而却步，进一步限制了选择。也许最重要的是，基于角色的访问控制、基于属性的访问控制以及其他授权和访问控制技术可能会引入复杂的外部系统，这些系统必须与插件以及底层服务器端技术同步。相比之下，Wasm 访问控制功能通常直接内置在运行时引擎中，减少了复杂性并简化了开发过程。

## 展望伟大的 Wasm 未来

在未来，随着 Wasm 魔法的出现，开发者将能够更轻松地为他们的应用程序设计定制或半定制配置和业务逻辑。此外，他们还可以将其应用于服务器端，以消除后端、中间层和前端之间的大部分开发摩擦。

基于 Wasm 的插件未来可能意味着许多很酷的事情：更容易和更好地调整应用程序性能、基于应用程序级 metric 的特定扩展和策略触发器等等。

通过 warg.io，我们已经看到了Wasm如何推动创新的、可组合的方法来构建能力，这些能力应用现有的包管理和注册表方法来使用受信任的 Wasm 代码元素进行构建。换句话说，Wasm 可能会给我们提供可组合的插件，这与开发人员将几个 npm 模块组合在一起以实现特定功能配置文件并没有太大区别。

应用程序开发人员和 DevOps 团队通常使用生硬的工具来提高应用程序性能。当出现延迟问题或其他问题时，他们有几个选择：

1. 在这个问题上投入更多的计算。
2. 增加内存（以及间接地增加 I/O）。
3. 进入代码并尝试识别延迟的来源。

前两个可能很昂贵。最后一个非常费力。使用 Wasm，开发人员可以选择在 Wasm 结构中运行会降低性能的大部分应用程序或功能，并使用更快的语言或结构。他们可以做到这一点，而不必撕掉整个应用程序，并且可以专注于容易实现的成果（例如，用 C 代码或在 Wasm 内部编译的 Go 代码替换用于计算的慢速 JavaScript 代码）。

事实上，与 JavaScript 相比，Wasm 具有许多性能优势。在最初的 Wasm 团队中，Mozilla 的 Lin Clark 解释道：

* 获取 Wasm 的速度更快，因为它比 JavaScript 更紧凑，即使在压缩时也是如此。
* 解码 Wasm 比解析 JavaScript 更快。
* 由于 Wasm 比 JavaScript 更接近机器码，并且已经在服务器端进行了优化，编译和优化时间更短。
* 代码执行速度更快，因为开发人员为了编写始终如一的高性能代码而需要知道的编译器技巧和陷阱更少。另外，Wasm 的指令集更适合机器。

因此，让我们想象一下这个未来：微服务不是通过昂贵的 Kubernetes API 服务器调用或内部东西 RPC 进行编排，而是通过在较小的进程空间和表面积内绑定的模块化、安全且高性能的 Wasm 组件进行编排。

传统上，开发人员使用 YAML 等其他数据编码语言来调用自定义资源定义 (CRD) 和其他方式来向其在 Kubernetes 中作为微服务运行的应用程序添加功能。这增加了开销和复杂性，使性能调整更具挑战性。借助基于 Wasm 的插件，开发人员可以利用众所周知且值得信赖的语言原语（Go、Rust、C++），而不是用更多的 CRD 重新发明轮子。