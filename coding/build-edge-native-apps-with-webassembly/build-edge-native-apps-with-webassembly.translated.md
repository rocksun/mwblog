# 使用 WebAssembly 构建边缘原生应用

![Featued image for: Build Edge Native Apps With WebAssembly](https://cdn.thenewstack.io/media/2025/05/50a5769a-ilias-haddad-oekcfimctcg-unsplash-1024x683.jpg)

[Ilias Haddad](https://unsplash.com/@iliashaddad3?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash.](https://unsplash.com/photos/a-man-sitting-on-a-couch-with-a-laptop-OeKCFIMcTcg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

客户端-服务器模型在传统软件开发中根深蒂固，以至于我们很少挑战这种教条。然而，边缘计算曾经只包括 CDN 加速和 DDoS 防护，现在已经发展成为第三层计算。

我们正在见证边缘计算的转型，因为像 WebAssembly 这样更强大的运行时使开发人员能够在分布式边缘构建整个应用程序，而不是在云服务中。

如果您的应用程序可以同时在 50 个城市运行，而无需传统服务器，会怎么样？这就是由 WebAssembly 驱动的边缘原生开发的承诺。

**什么是边缘计算以及它对 WebAssembly 的重要性**

客户端-服务器模型是构建互联网的经典架构。我们常见的在线任务（电子邮件、Web、消息传递等）最初都是在这种两部分模型中构思的，其中用户有一个呈现数据的客户端，但数据本身由服务器管理（并存储在服务器上）。

在 20 世纪 90 年代后期，第三层悄然插入到客户端和服务器之间。当时，我们称之为内容分发网络 (CDN)。它的最初工作是将静态资源（如图像和样式表）存储在更靠近用户的位置。一个典型的 CDN 可能有几十个、几百个甚至几千个位于全球各地的[存在点 (POP)](https://networkencyclopedia.com/point-of-presence-pop/)。这些小型计算和存储能力库介入网页加载以更快地交付资产。CDN 旨在提高交付速度，但仅适用于不经常更改的资产。

CDN 网络也被证明是运行其他类型操作的好地方。随着时间的推移，CDN 扩展到安全领域并成为边缘提供商。例如，它们的分布式特性意味着它们可以在攻击者攻陷上游服务器之前阻止分布式拒绝服务 (DDoS) 攻击。

随着[云提供商取代本地数据](https://thenewstack.io/the-architects-guide-to-the-modern-data-stack/)中心，边缘提供商开始尝试托管计算。通过在 CDN 位置嵌入简单的 JavaScript 引擎，边缘公司允许客户对入站 HTTP 请求进行轻量级转换。边缘计算用于执行以下操作：

- 在内容重新定位时发出重定向
- 管理 HTTP 请求中的 CORS 标头
- 根据位置信息智能地路由流量

开发人员喜欢这种模式，但系统的限制意味着只能在边缘完成一定量的处理。这开启了一个新的机会。

**边缘计算如何演进以支持 WebAssembly**

早期的边缘计算（运行小型 JavaScript 代码片段来更改 HTTP 请求）本质上是一种辅助功能。在边缘执行的代码并非旨在执行任何繁重的工作或将完整的结果返回给用户。它旨在做出小的决策，以简化上游服务器处理请求的方式，或者通过提前做出决策来减轻上游服务器的一些工作。例如，在边缘执行身份验证是一项小任务，但（对于失败的身份验证尝试）可以减轻更繁忙和昂贵的上游服务器的工作。

然而，有两件事阻碍了边缘计算。首先是[边缘工作者可用的计算能力](https://thenewstack.io/vmware-discloses-its-edge-computing-future/)较低。第二个是在边缘运行的数据服务匮乏。当没有地方存储数据时，很难进行任何重要的计算。

**WebAssembly：解决边缘运行时挑战**

如果计算能力低是第一个问题，那么有两种潜在的解决方案：提高可用边缘硬件的功率或提高运行时的效率。无论如何，扩展硬件是必要的，但它往往进展缓慢，因为它非常昂贵。虽然从长远来看，边缘位置可能会获得更好的硬件，但在短期内，这种解决方案是站不住脚的。
但更快运行时的出现改变了游戏规则。Fastly 是第一个使用 WebAssembly 作为边缘运行时的公司，推出了 [Compute@Edge](https://docs.fastly.com/products/compute) 平台。Akamai 和 Fermyon 已经联手[提供了一个由 WebAssembly 驱动的运行时](https://thenewstack.io/should-you-care-about-fermyon-wasm-functions-on-akamai/)，其性能与亚马逊的 Lambda 无服务器环境一样强大，但运行在 Akamai 的核心边缘区域。Fastly 和 Akamai 现在都支持小段 JavaScript 代码和越来越多的其他编程语言，所有这些都作为 WebAssembly 二进制文件运行。即使是坚定的 JavaScript 倡导者 Cloudflare 也已经[在 WebAssembly 的支持下](https://developers.cloudflare.com/workers/runtime-apis/webassembly/)进军多语言支持领域。

WebAssembly 在边缘计算方面有四个优点：

*   默认情况下是安全的，并且是多租户安全的。
*   WebAssembly 二进制文件很小，特别是与[容器和虚拟机](https://thenewstack.io/containers-vs-virtual-machines-another-perspective/)(第一代无服务器背后的技术)相比。
*   编译为 WebAssembly 的程序几乎可以在任何硬件和操作系统上运行，而无需修改。
*   冷启动 WebAssembly 非常快，使其既具有高性能又具有高度可扩展性。

WebAssembly 是一种安全且平台中立的运行时，它开启了复杂的边缘计算的可能性，在某些情况下，它可能会完全取代服务器组件。除了适应所有早期的边缘计算用例外，它还足够强大，可以运行分布式内容管理系统、数字体验平台和 AI 推理，而无需云提供商的上游支持。

WebAssembly 分布在边缘，而不是在一个云区域中运行的集中式计算库，这意味着同一应用程序的数万个实例可以分布在全球各地运行，以惊人的速度响应请求。如果云原生计算定义了向云的迁移，那么这种新兴趋势恰如其分地被称为边缘原生计算。

**为什么分布式存储对于边缘的 WebAssembly 至关重要**

边缘原生[计算的第二个要求是需要可以从边缘函数轻松访问的分布式存储](https://thenewstack.io/what-are-time-series-databases-and-why-do-you-need-them/)。

Cloudflare 引领了潮流，几年前推出了分布式键/值存储、对象存储和数据库存储。Akamai 收购了 Linode，后者提供了强大的云计算能力（Akamai 继续将其推向边缘）和云级存储。包括 [Harper](https://www.harperdb.io/)、[Neon](https://neon.tech/) 和 [Turso](https://turso.tech/) 在内的许多第三方已经推出了边缘原生 SQL 数据库，这些数据库解决了与分布式计算相关的数据访问问题。今年 3 月，新的 [Graft 数据库](https://sqlsync.dev/posts/stop-syncing-everything/) 宣布了一种同步机制，非常适合边缘的无服务器工作负载。

**由 WebAssembly 驱动的边缘原生应用程序的兴起**

通过将边缘的数据访问与边缘计算运行时的巨大改进相结合，[开发人员现在可以构建应用程序](https://thenewstack.io/google-wants-developers-to-build-on-device-ai-applications/)，这些应用程序分布在边缘运行，并且几乎或完全不依赖于数据中心内的上游服务器。较旧的客户端/服务器模型让位于客户端/边缘/服务器模型，现在已经开启了分布式客户端/边缘模型的潜力。

这种新的边缘原生方法不仅使分布式计算变得容易，而且还将成为新兴的基于推理的 AI 应用程序（包括代理工作流）的基地。通过使工作更接近最终用户，边缘应用程序不仅满足了速度要求，而且还实现了信息的本地化并遵守了数据主权要求。所有这些都将由 WebAssembly 提供支持。

*TNS 的所有者 Insight Partners 也在 Fermyon 投资。因此，Fermyon 作为贡献者获得了优先权。*

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)