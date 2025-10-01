<!--
title: 为什么您的应用程序最大的性能瓶颈可能是 SSL/TLS
cover: https://cdn.thenewstack.io/media/2025/09/a8812c0d-image3b.png
summary: SSL/TLS握手是CPU密集型操作，常被忽视，却是性能瓶颈。它会增加延迟和基础设施成本。OpenSSL 3.x曾出现性能问题。应深入理解和优化SSL/TLS，而非将其视为已解决问题。
-->

SSL/TLS握手是CPU密集型操作，常被忽视，却是性能瓶颈。它会增加延迟和基础设施成本。OpenSSL 3.x曾出现性能问题。应深入理解和优化SSL/TLS，而非将其视为已解决问题。

> 译自：[Why Your App’s Biggest Performance Bottleneck Might Be SSL/TLS](https://thenewstack.io/why-your-apps-biggest-performance-bottleneck-might-be-ssl-tls/)
> 
> 作者：Ron Northcutt

您的应用程序运行缓慢。您优化了数据库，修复了 N+1 查询，并调整了微服务。但是，如果您的服务上最大的性能开销就隐藏在显而易见的地方，隐藏在一个如此基础以至于我们常常将其视为已解决问题的层中呢？

我指的是 [SSL/TLS。](https://www.haproxy.com/glossary/what-is-transport-layer-security-tls) 几十年来，我们理所当然地将其视为一项不可协商的安全功能，是浏览器中的锁图标，是 HTTPS 中的“S”。我们启用它，从 Let's Encrypt 获取证书，然后就置之不理。

然而，这种“一劳永逸”的心态正成为一个危险的隐患。SSL/TLS 不仅仅是一个安全封装；它还是一个活跃的、CPU 密集型进程，运行在流经现代互联网的几乎每一个（新的）安全连接上。

考虑一个繁忙的电子商务 [API，每秒处理](https://thenewstack.io/api-management/) 1,000 个请求。如果其中 30% 需要新的 TLS（传输层安全）握手，那么每秒将有 300 次加密协商，与您的业务逻辑争夺 CPU 周期。忽略其性能特性，就像试图建造摩天大楼却不了解其下方的地质情况一样。迟早，裂缝会开始显现。

## 握手解析：安全连接的成本

[![初始完整握手](https://cdn.thenewstack.io/media/2025/09/a8e70a26-image1-1024x824.png)](https://cdn.thenewstack.io/media/2025/09/a8e70a26-image1-1024x824.png)

为了理解 TLS 的开销，我们必须跳出应用程序代码。正如工程师 Hussein Nasser 在他精彩的会议演讲“[请求解析：超越后端处理](https://www.haproxy.com/user-spotlight-series/anatomy-of-a-request-beyond-backend-processing)”中详细阐述的那样，单个客户端请求是一个复杂的舞蹈，早在您的后端框架看到它之前就开始了。

在您的应用程序能够处理请求之前，客户端和服务器必须完成一个多步骤的协商。这不仅仅是建立连接的三次 TCP（[传输控制协议](https://www.google.com/search?sca_esv=cda52438cd53ad97&rlz=1C5CHFA_enUS981US981&q=Transmission+Control+Protocol&sa=X&ved=2ahUKEwjUlsvtke-PAxWsLdAFHTcdCDIQxccNegQIRBAB&mstk=AUtExfAw4ANP203AdQXUNkmUu8nlYpUsaDZRdCzyho07a2KrYByZV41jDElYHuJ7tU4ckbBdKyLUQa9cl8MblXNQEhrD90B6UgPf540h0DNk9vi-72XDyBv0NBKZbktaMToLJOoHhM5iNKyMTi-SLz5l1UrqyeDfWo2yb9TtuGpJopaOfCQ&csui=3)）握手；它还是随后的 TLS 握手，以使其安全。此过程包括：

1.  **问候与协商：** 客户端和服务器打招呼 (ClientHello, ServerHello)，并就它们将使用的密码套件达成一致。
2.  **证书交换：** 服务器出示其数字证书以证明其身份。客户端必须根据其受信任的证书颁发机构列表验证此证书。
3.  **密钥生成：** 这是计算成本最高的部分。客户端和服务器使用非对称加密（速度慢，但适用于与陌生人安全地协商事物）来生成和交换共享的对称密钥。然后，这个新密钥用于应用程序数据的实际加密和解密（快速、高效）。

Hussein Nasser 的深入探讨强调了一个关键点：这种加密舞蹈是 CPU 密集型的。公钥密码学复杂的数学运算并非没有成本。每一次复制，每一次计算，都会消耗原本可以用于服务其他请求的 CPU 周期。

将 TLS 握手想象成进入建筑物前的强制性安全检查站。即使是最有效的检查站也有处理时间。现在想象一下您最喜欢的咖啡店入口处的那个检查站：您第一次不会介意，但如果每次访问都必须重复，您就会注意到。

## 普遍性开销：当毫秒变成危机时

[![](https://cdn.thenewstack.io/media/2025/09/bf8a7480-image2-1024x723.png)](https://cdn.thenewstack.io/media/2025/09/bf8a7480-image2-1024x723.png)

“好吧，”您可能会说，“一次握手只花费几十毫秒。谁会在乎？”

您应该在乎。

需要明确的是，您并非为每个请求都支付此成本——现代协议大大降低了这一点。持久连接（HTTP/1.1 [keep-alive](https://en.wikipedia.org/wiki/HTTP_persistent_connection)，HTTP/2 [多路复用](https://www.haproxy.com/glossary/what-is-http2#binary-framing) 和 HTTP/3 的 [QUIC](https://www.haproxy.com/glossary/what-is-quic)）意味着许多请求共享一个握手。TLS 1.3 会话恢复和 [0-RTT](https://www.haproxy.com/glossary/what-is-zero-round-trip-time-resumption-0-rtt)（零往返时间）可以使后续握手成本大大降低。

问题在于，每个新的安全连接仍然会产生此成本，在拥有大量短寿命连接、没有连接池的 API 或无法重用连接的客户端的繁忙系统中，这些握手会迅速累积——无论是延迟还是 CPU 负载方面。

让我们使用保守的、真实世界的数字：

*   一个典型的完整 TLS 1.3 握手可能会增加 1 或 2 次网络往返（约 30-50 毫秒，取决于网络条件），以及可测量的用于加密工作的 CPU 周期。
*   恢复或池化的连接会大幅削减这一成本，但在 20% 到 40% 的请求仍会触发新握手的工作负载中，这会给您的基础设施带来沉重的负担。

例如，每秒 1,000 个新连接，每个握手耗时 40 毫秒，您就会在每次连接启动时增加明显的延迟，并对服务器造成可测量的 CPU 负载。这些 CPU 工作会与业务逻辑争夺资源，这意味着您要么在负载下变慢，要么配置更多容量以跟上。

在大规模应用中，这会带来两个主要后果：

1.  **用户体验下降：** 对于像 [gRPC](https://thenewstack.io/grpc-a-deep-dive-into-the-communication-pattern/) 这样连接密集型协议或有许多短寿命 API 调用的应用程序，握手开销可能成为感知延迟的一个重要因素。
2.  **基础设施成本增加：** 更多 CPU 用于加密计算意味着需要更多服务器来处理相同的流量。这种“握手开销”直接增加了您的计算费用。

关键在于，这种开销无处不在——在 [HTTPS](https://thenewstack.io/http-3-is-now-a-standard-why-use-it-and-how-to-get-started/)、安全数据库连接、某些 DNS 查询（DoH/DoT）以及其他协议中。虽然并非每个请求都付出代价，但数量足够多，因此忽视它可能会代价高昂。

## 当基础出现裂缝时：OpenSSL 3 的变化

当我们大多数人每天使用的库中引入一个关键性能问题时，这种理论风险成为了整个行业的一个严峻现实。正如[最近的一项分析](https://www.haproxy.com/blog/state-of-ssl-stacks)所探讨的，OpenSSL 3.x 版本引入了严重的性能退化，完美地说明了这一危险。

OpenSSL 是无数网络服务器、操作系统和应用程序底层的加密引擎。3.0 版本旨在作为新的长期支持 (LTS) 版本，其架构设计选择导致其性能骤降——在某些多线程场景中，与前身相比，性能下降了高达 99%。更糟糕的是，随着 CPU 核心的增加，性能反而经常下降，这与预期完全相反。

这使组织当时处于一个不可能的境地：升级到新版本以获取关键安全补丁并遭受巨大的性能损失，或者坚持使用旧的、更快的版本并变得更脆弱。这是一个真实的例子，说明这个“已解决”层中的缺陷如何可能导致灾难性后果，迫使公司考虑需要[多达 42 倍的硬件](https://www.haproxy.com/blog/state-of-ssl-stacks#:~:text=1/42%20of%20its%20performance)才能维持服务水平。SSL/TLS 层不再仅仅是一种开销；它是一个障碍。

值得注意的是，在撰写本文时，OpenSSL 的当前版本是 3.5，它是更新的 LTS 版本。它已经解决了大部分报告的性能问题，并推荐用于典型使用。然而，动态设计在大规模应用中仍然不如以前的版本。

## 您能做些什么

关键在于，我们必须停止将 SSL/TLS 层视为一个万无一失的黑箱。我们需要像对待自己的代码一样，对其施加同样的严谨性。以下是一些可操作的步骤：

1.  **超越您的应用程序进行性能分析：** 不要仅仅假设延迟来自您的数据库。使用性能分析工具来查看 CPU 时间花在了哪里。您可能会惊讶地看到 `SSL_read` 或 `SSL_write` 等函数点亮您的火焰图。
2.  **了解您的技术栈：** 您实际使用的是哪个 SSL/TLS 库？OpenSSL？BoringSSL？LibreSSL？AWS-LC？每个库都有不同的性能特征和不同的开发理念。这个选择是一个关键的架构决策，而不是一个次要的实现细节。
3.  **调整您的系统：** 在操作系统层面，调整与 TCP 相关的内核设置（缓冲区大小、连接积压）可以帮助您的服务器更有效地处理更高数量的安全连接。
4.  **减少握手：** 实施连接池，启用 HTTP/2 或 HTTP/3，并确保您的客户端利用 TLS 会话恢复来最大程度地减少完整握手的次数。

SSL/TLS 是在线安全通信的基石。但就像任何基础一样，它也有负载能力。通过了解其成本、衡量其影响，并有意识地选择连接重用、协议设置和加密库，我们可以最大程度地减少安全通信对应用程序的影响。

要深入了解最有前景的 SSL 库，包括测试和比较，请查看 Willy Tarreau 和 William Lallemand 的“[SSL 栈的现状](https://www.haproxy.com/blog/state-of-ssl-stacks)”。