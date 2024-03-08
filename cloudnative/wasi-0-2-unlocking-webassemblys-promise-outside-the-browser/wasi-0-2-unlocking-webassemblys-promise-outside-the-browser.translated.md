## WASI 0.2：释放 WebAssembly 在浏览器之外的潜力

![WASI 0.2 的特色图片：释放 WebAssembly 在浏览器之外的潜力](https://cdn.thenewstack.io/media/2024/02/89838150-legos-1024x682.jpg)

WebAssembly 系统接口 (WASI) 小组最近通过投票发布了 [WASI 0.2（也称为 WASI 预览版 2）](https://thenewstack.io/wasi-preview-2-what-webassembly-can-and-cant-do-yet/)，从而达到一个重要的里程碑。这个激动人心的新 WASI 标准基于 Wasm [组件模型](https://github.com/WebAssembly/component-model/)，允许应用程序开发人员像乐高积木一样构建软件，其中 [不同的组件可以轻松连接](https://thenewstack.io/webassembly-in-the-browser-matures-and-cool-things-happen/)，以创建更大、更复杂的应用程序。这种方法简化了编写、重用和维护代码，同时确保最终产品在不同的设备和系统中安全、快速且兼容。

### 回顾：WebAssembly 和 WASI 的演变

[WebAssembly](https://thenewstack.io/webassembly/) 最初是针对浏览器开发的，以便人们可以在浏览器中运行性能关键型代码或图像编辑程序和视频游戏等繁重的工作负载。与此同时，关于其在浏览器*之外*的潜力的讨论也相当多。Node.js 成功地用 JavaScript 做到了这一点，而开发人员社区对 WebAssembly 也有类似的愿望。

但这种愿望充满了复杂性。

[WebAssembly 在很大程度上依赖于在网络浏览器中运行](https://thenewstack.io/cheerpj-3-0-run-apps-in-the-browser-with-webassembly/)，并且无法直接访问浏览器环境之外的系统资源和 API。围绕沙盒和安全也存在担忧，这些担忧在浏览器执行的背景下至关重要，沙盒确保在浏览器中执行的代码无法访问敏感的系统资源或干扰其他浏览器进程。

然而，尽管存在这些最初的限制，但将 WebAssembly 扩展到浏览器环境之外的愿景仍然盛行。随着开发人员和利益相关者开始认识到其在安全、跨平台应用程序开发方面的潜力，他们开始努力扩大其范围。这促成了 WASI 的开发，WASI
[旨在为在非浏览器环境（如服务器、命令行工具和嵌入式系统）中执行 WebAssembly](https://thenewstack.io/webassembly-aims-to-eliminate-the-file-system/) 代码提供一个标准化接口。

2019 年引入的 WASI 预览版 1 包含旨在帮助 WebAssembly 与外部世界（如文件系统和命令行界面）交互的功能。WASI 预览版 1 类似于 POSIX（可移植操作系统接口）的一个超级可移植子集，它留下了这样一个问题：是否沿着 POSIX 继续走下去，沿着我们知道会通向容器的道路前进，或者 WASI 是否应该开辟一条通向本质上更轻量级、启动更快速、更安全、更能抵抗的道路
[供应链攻击](https://thenewstack.io/supply-chain-attacks-and-cloud-native-what-you-need-to-know/)。

在预览版 1 中朝着 POSIX 方向工作了一段时间并制定了
[对未来的共同愿景](https://hacks.mozilla.org/2019/11/announcing-the-bytecode-alliance/) 之后，我们决定走第二条路，开辟一条新路，但也产生了许多新问题。

### 组件模型进入故事

一旦我们决定离开 POSIX 这条人迹罕至的道路，我们就需要找到新的东西来取代 POSIX 风格的可执行文件和共享对象，它们是传统 POSIX 系统中应用程序构建之上的主要代码单元。在提炼了一组激励性的
[目标](https://github.com/WebAssembly/component-model/blob/main/design/high-level/Goals.md) 和 [用例](https://github.com/WebAssembly/component-model/blob/main/design/high-level/UseCases.md) 之后，我们决定采用一个 [高级设计](https://github.com/WebAssembly/component-model/blob/main/design/high-level/Choices.md) 为一个称为“组件”的新代码单元，该单元将建立在 WebAssembly 模块之上并包含 WebAssembly 模块。

那么模块和组件有什么区别？模块已经完全标准化并在浏览器中得到支持，它们包含非常底层的代码，这些代码试图尽可能接近 CPU（同时确保安全性和可移植性）。
**组件：模块化和安全性的关键**

组件通过充当模块的包装器并了解如何与其他组件交互（无论它们使用哪种语言编写）来发挥魔力。组件还通过为模块提供一种结构化的方式来进行通信和交互，而无需共享低级内存（类似于传统的 POSIX 进程），从而帮助解决许多安全问题。这有助于降低未经授权的访问或恶意行为的风险，并有助于减轻漏洞在系统中传播的风险。

**WASI 0.2：朝着正确方向迈出的重要一步**

随着 WASI 0.2 的发布，开发者社区正在庆祝，因为它标志着组件模型和一系列 WASI API 的官方稳定点，并为 WebAssembly 在浏览器之外建立了一个强大且通用的基础。此次发布仅仅是个开始，还有很多工作要做，但它为完全模块化的应用程序和可组合性和兼容性的新可能性提供了清晰的思路。

WASI 0.2 还引入了两个不同的“世界”，它们描述了 WebAssembly 可以运行的不同类型的宿主。第一个世界是“命令”世界，类似于传统的 POSIX 命令行应用程序，可以访问文件系统、套接字和终端。

第二个世界是“HTTP 代理”，它描述了像 Fastly 这样的平台，这些平台可以发送和接收流式 HTTP 请求和响应，充当正向或反向代理。这些世界代表了一个更广泛生态系统的开始，为开发者提供了多条探索和创新的途径，未来还将向 WASI 添加更多世界。

**展望未来：WASI 的未来**

随着 [WASI 的不断发展](https://thenewstack.io/webassembly-4-predictions-for-2024/)，未来前景令人兴奋。未来版本的路线图包括增量更新、功能增强和对可组合并发性的支持的计划。目标是创建一个强大的生态系统，可以适应各种用例和编程语言，包括 Rust、C#、JavaScript、Python、C++、Kotlin 和 Go。

可组合性和兼容性的原则将指导从 WASI 0.2 到未来版本的过渡。凭借组件模型的灵活性，WASI 旨在促进不同版本之间的无缝升级和互操作性。这种迭代方法确保 WASI 能够适应新兴技术和不断变化的开发者需求。

**庆祝 WebAssembly 征程中的一个里程碑**

WASI 0.2 象征着多年协作努力和创新的成果，为跨平台开发和部署的新时代铺平了道路。

展望未来，WASI 的征程仍在继续，由充满活力的多元化开发者社区的共同愿景所驱动。随着每一次发布，WASI 都让我们更接近一个代码可移植性、安全性和互操作性不仅是理想，而且是软件开发基本原则的世界。

*要了解有关 Kubernetes 和云原生生态系统的更多信息，请于 3 月 19 日至 22 日在巴黎加入我们在 KubeCon + CloudNativeCon Europe 的活动。*

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。