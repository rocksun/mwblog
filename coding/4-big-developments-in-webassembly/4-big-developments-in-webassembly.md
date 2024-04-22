
<!--
title: WebAssembly的4个发展动态
cover: https://cdn.thenewstack.io/media/2024/04/83b6f355-cars.jpg
-->

Wasm 正在成熟，拥有主流语言支持、Kubernetes 部署选项、组件模型的革命性可能性等等。

> 译自 [4 Big Developments in WebAssembly](https://thenewstack.io/4-big-developments-in-webassembly/)，作者 Matt Butcher。

在巴塞罗那举行的 [Wasm I/O](https://wasmio.tech/) 和在巴黎举行的 [KubeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 上，宣布了有关 WebAssembly (Wasm) 的多项更新。其中，出现了四种重大模式。

## 编程语言支持正在蓬勃发展

自 Wasm 诞生以来，其成功面临的最大风险就是缺乏编程语言的支持。即使是最好的跨平台字节码格式，如果没有语言编译成该格式，也无法成功。

我一直在追踪 [WebAssembly 中的语言支持](https://developer.fermyon.com/wasm-languages/webassembly-language-support)。具体来说，我追踪的是 [根据 RedMonk](https://redmonk.com/rstephens/2024/03/08/top20-jan2024/) 的说法，排名前 20 的语言中有多少正在采用 WebAssembly。Python、JavaScript/TypeScript、Ruby、Rust、C/C++ 和 Zig 都已采用 Wasm，其他语言也在采用中。

在 Wasm I/O 上，JetBrains 的 Zalim Bashorov 报告了 Kotlin 的快速进展。除了本身是一种流行的语言之外，[Kotlin 代表](https://thenewstack.io/kotlin-multiplatform-mobile-from-jetbrains-takes-on-flutter/) 了 Java 世界中最具前瞻性的元素。随着 Kotlin 接近 WebAssembly 核心支持和 WASI 0.2 支持，我预计随着它找到新的目标开发者受众，该语言的普及将再次提升。不仅如此，它还将吸引更广泛的 Java 社区转向 WebAssembly。

Dart 现在附带一个 WebAssembly 编译目标。在 Wasm I/O 上，谷歌的 Kevin Moore 分享了 Dart 和 Flutter 世界中的激动人心的发展。Moore 没有给人留下 Dart 将超越其浏览器和移动应用根源的印象，但 Wasm 带给该世界的性能提升非常棒。Moore 展示的基准表明，Wasm 执行速度可以比基于 JavaScript 的执行时间快 50% 以上。

最后，由 Rajiv Singh 和 Achille Roussel 代表的 Go 团队介绍了 Go 的 WebAssembly 的新[进展](https://thenewstack.io/webassembly-developers-lust-for-rust-and-assemblyscript-but-not-go/)支持。Go 已将其部分 WebAssembly 支持让给了 TinyGo（该项目的负责人 Ron Evans 也在 Wasm I/O 上进行了展示）。但核心 Go 团队现在重新燃起了在浏览器内外支持 Wasm 的兴趣。

然而，编程语言支持的另一个主要功能是可调试性。微软的 Natalia Venditto 和 Ralph Squillace 展示了 Visual Studio Code 中的 Wasm 调试。语言中立的 Wasm 调试对于现代软件开发来说是绝对必须的，而微软正在努力使之成为现实。

## Kubernetes 是 WebAssembly 部署的目标

Wasm I/O 和 KubeCon 都热议了 [在](https://thenewstack.io/dev-news-angulars-new-loading-an-ai-compiler-and-js-runs-wasm/) Kubernetes 中运行 Wasm。Fermyon、微软、SUSE、Liquid Reply 等公司共同发布了[开源 SpinKube 项目](https://www.spinkube.dev/)，用于运行 Spin 风格的 Wasm Kubernetes 应用程序。在 KubeCon 上，国际光学公司蔡司集团在[主题演讲阶段](https://youtu.be/tu8a-GefJL8?si=Nr_takAmgqp61JjB)展示了实际用例。

SUSE 宣布 Rancher Desktop [支持 WebAssembly](https://www.suse.com/c/rancher_blog/rancher-desktop-1-13-with-support-for-webassembly-and-more/)，使用其 K3s Kubernetes 运行时。Fermyon 宣布了一个商业支持的超高密度 [Kubernetes Fermyon 平台](https://www.fermyon.com/blog/introducing-spinkube-fermyon-platform-for-k8s)，每 Kubernetes 节点可以运行 5,000 个 Wasm 应用程序。[Cloud Native Computing Foundation 的 wasmCloud 项目](https://wasmcloud.com/blog/wasmcloud-1-brings-components-to-enterprise) 达到 1.0，并支持 Kubernetes 集成。NGINX Unit 宣布支持[在其应用程序平台中运行 Spin 应用程序](https://unit.nginx.org/news/2024/fermyon-spin-rust-sdk/)。

在 WebAssembly 的 KubeCon 主题演讲之后，EMA 分析师 Torsten Volk 指出，Wasm 已[成为](https://thenewstack.io/kubecon-europe-webassembly-ebpf-are-huge-for-cloud-native/)会议上讨论最多的主题。

Wasm 有什么特点[与 Kubernetes 如此契合](https://thenewstack.io/webassembly/yes-webassembly-can-replace-kubernetes/)？Wasm 的冷启动时间使其成为类似 lambda 的无服务器函数的绝佳平台。Kubernetes 用户长期以来一直有兴趣在集群内运行此类工作负载，但第一波 Kubernetes 无服务器解决方案无法与 Wasm 的密度、性能和启动速度相匹配。

## 组件模型变得真实

在 [WebAssembly](https://thenewstack.io/webassembly/webassembly-component-model-is-here-and-its-a-game-changer/) 的组件模型方面有八场会议。[WebAssembly 组件模型](https://component-model.bytecodealliance.org/) 在今年的 Wasm I/O 上亮相。虽然去年的 Wasm I/O 主要从理论角度介绍了组件模型，但今年我们看到了组件开发一年来的成果。

我特别喜欢 Fermyon 的 Thorsten Hans 讲解使用组件进行多语言编程的三场系列讲座，Ryan Levick 解释了组件的[来龙去脉](https://youtu.be/zqfF7Ssa2QI?si=MEzzCF0csQEdMP59)，Luke Wagner 以[组件间异步调用](https://youtu.be/y3x4-nQeXxc?si=gTL0tIZxFrp0aphd)（WASI 中尚未完成的部分）为主题结束了三部曲。

还有其他一些讲座重点介绍了如何使用组件来完成特定任务，主讲人包括 InfinyOn 的[Sejyo Chang](https://www.linkedin.com/in/sehyo/)、Design Systems 的[Pierre Dureau](https://github.com/pdureau)、Dilla.io 的[Jean Valverde](https://www.linkedin.com/in/jean-valverde/?locale=en_US)、Cosmonic 的[Taylor Thomas](https://twitter.com/i/flow/login?redirect_after_login=%2F_oftaylor) 等。总的来说，现在很明显，组件模型已准备就绪。

然而，最重要的组件相关开发成果来自[F5 的 Oscar Spencer 和 JAF Labs 的 Danny Macovei](https://youtu.be/2_-10mRN30s?si=8FIz-ys-KVkU5KAQ)。定义组件注册表的这项工作已经持续了三年，但在 Wasm I/O 第一天结束时，Macovei 和 Spencer 推出了 WA.dev，这是第一个 Wasm 组件注册表。将 WA.dev 与 npm 甚至 Docker Hub 进行比较是公平的。开发人员可以将他们的组件上传到一个中央注册表，这使得我们所有人都可以轻松地发现和管理组件。

## Wasm 仍然是一种先锋语言

也许最后一个发展趋势是一种反潮流。语言支持正在趋于一致。Kubernetes 和 Wasm 正在取得进展。Wasm 组件模型规范正在融入实用工具中。这些都是成熟和稳定的迹象。然而，Wasm 并没有停滞不前；它仍然处于持续探索阶段。

没有比[Wanix 项目](https://wanix.sh/)更好的例子来说明这一点，独立开发人员 Jeff Lindsay 和 Julian Del Signore 在 Wasm I/O 的第二天介绍了该项目。Lindsay 是一位有远见的梦想家，他的项目经常迫使软件开发人员重新思考他们对事物如何完成的假设。从发明 Webhook 到他在容器领域的早期贡献，Lindsay 一直在突破界限。Wanix 也毫不例外。

Del Signore 和 Lindsay 展示了一个受 Plan9 启发的浏览器内操作系统，它为一个类似 CMS 的系统提供支持，该系统能够将状态同步到 GitHub。这是一个很好的例子，说明了 Wasm 的多功能性、性能和跨平台特性如何结合起来构建一类目前还没有名称的工具。

同样，前 VMware Wasm Labs 负责人 Daniel Lopez 在展示各种演示时，带领观众进行了一次充满乐趣的旅程。从[在浏览器中运行 Windows 95](https://copy.sh/v86/)到演示 AI 推理，Lopez 指出了这项高度多功能技术的各种有趣应用。在最幽默的时刻，Lopez 展示了如何在 Wasm 中运行 Docker，从而增加了多层虚拟化。然而，他演讲的主旨是，Wasm 不应该被归类。

在 Wasm I/O 的最后一天，TinyGo（以及其他一些东西）的创建者 Ron Evans 介绍了一个用于物联网 (IoT) 嵌入式开发的开源框架。[Mechanoid](https://github.com/hybridgroup/mechanoid) 由 Wasm 提供支持，支持使用多种编程语言进行嵌入式开发，包括 Rust、Go 和 Zig。物联网是 WebAssembly 的一个新兴领域。虽然它已经在[娱乐设备](https://medium.com/bbc-product-technology/building-a-webassembly-runtime-for-bbc-iplayer-and-enhanced-audience-experiences-7087455808ef)中站稳了脚跟，但 Evans 探索了在微控制器中使用它，将 Wasm 推广到微型设备类别。

## 结论

在很多方面，Wasm 已经显示出它的成熟性。现在几乎所有主流语言都支持 WebAssembly。Kubernetes 被证明是托管 Wasm 应用程序的流行环境，而 WebAssembly 组件模型正在释放 WebAssembly 的革命性可能性，包括真正的多语言编程。

但就像 Java 找到了超出其最初意图的用例一样，我们也看到 Wasm 在物联网等迷人领域以及 Wanix 等新兴领域中开辟了机会。这很好地提醒我们，成熟并不意味着停滞。
