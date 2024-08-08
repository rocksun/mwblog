
<!--
title: 使用JavaScript构建可扩展的实时应用程序
cover: https://cdn.thenewstack.io/media/2024/08/d903aca6-age-barros-yx1zkifihto-unsplash.jpg
-->

使用 WebSocket、服务器发送事件 (SSE) 和 Socket.IO 等库，构建可扩展的实时 JavaScript 应用程序的技巧。

> 译自 [How To Build Scalable Real-Time Applications With JavaScript](https://thenewstack.io/how-to-build-scalable-real-time-applications-with-javascript/)，作者 Alexander T Williams。

实时应用程序提供实时报告和分析，帮助企业做出更快、更明智的决策，同时提供更好的用户体验和增强的安全性。

本文将探讨 [构建可扩展的实时应用程序](https://thenewstack.io/how-to-build-a-real-time-app-with-gpt-4o-function-calling/) 的挑战和解决方案，重点介绍 WebSocket 实现、服务器发送事件 (SSE) 以及 Socket.IO 等库，以有效地管理实时通信。同样，我们还将考虑处理数据同步、确保低延迟和随着用户需求增长而保持可扩展性的最佳实践。

## 对实时应用程序的需求

越来越多的行业开始依赖实时应用程序 (RTA)，因为企业努力提高通信和决策的速度。从消费者的角度来看，[RTA 提供更好的用户体验 (UX)](https://ably.com/blog/the-realtime-web-evolution-of-the-user-experience)，使组织能够更快地响应查询并评估实时数据以提高运营绩效和效率。

但是，构建实时应用程序确实存在挑战，尤其是在处理延迟和性能方面。用户 [期望在不到 4 秒内获得响应](https://blog.hubspot.com/marketing/page-load-time-conversion-rates#good-page-load-time)，并且对任何延迟的容忍度极低。为了避免这些问题，许多开发人员转向 JavaScript 来提供高性能、低延迟的 RTA。

## 实时应用程序：关键挑战

由于实时应用程序预计将提供几乎即时响应的体验，因此在部署之前需要完全解决任何与性能和延迟相关的问题。以下是可能损害 RTA 的性能和可用性的几个挑战，以及如何克服这些挑战。

- **延迟**，数据传输开始之前的延迟，[通常是由网络拥塞引起的](https://www.geeksforgeeks.org/what-is-network-congestion-common-causes-and-how-to-fix-them/)，服务器处理时间缓慢或数据传输协议配置错误。为了减轻这种情况，开发人员需要消除所有可能减慢用户设备和应用程序服务器之间数据传输速度的障碍。
- **同步**问题可能在多个用户尝试同时执行操作时出现 - 例如，[在在线多人游戏中](https://news.ycombinator.com/item?id=31512257)。这要求开发人员确保所有连接设备上的所有应用程序内交互都按顺序正确且准确地进行。
- **可扩展性**在 RTA 的用户群增长时可能是一个挑战。当应用程序的数据库无法处理更大数量的数据和用户请求时，它会影响 JavaScript 开发人员。这可能是 [资源利用率低下造成的](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_management)，某些应用程序组件的负载高于其他组件。
- **安全性**和可扩展性在实时应用程序中经常并存。因此，随着 RTA 用户群的增长，其攻击面也会随之增长。为了应对这种情况，开发人员需要 [提高监控和可观察性](https://thenewstack.io/monitoring-and-observability-whats-the-difference-and-why-does-it-matter/)、[保护 API](https://thenewstack.io/how-to-secure-apis-the-new-shadow-it/) 并实施 [强大的云安全](https://cast.ai/cloud-security/) 实践，以确保随着应用程序的扩展，数据和服务免受潜在威胁。

## 使用 JavaScript 在 2024 年构建可扩展的实时应用程序

Node.js 通常是 JavaScript 开发人员的首选运行时环境，因为它开源且拥有强大的社区支持。即使是 Uber 等全球巨头 [也在 Node.js 的帮助下开发他们的应用程序](https://www.uber.com/en-GB/blog/uber-tech-stack-part-two/)，因为它单线程处理能力有效地处理每秒超过 200 万个远程过程调用 (RPC)。

当然，大多数 RTA 永远不会达到这种规模；但无论如何，任何应用程序都需要考虑到未来的扩展。在本节中，我们将讨论开发人员在使用 JavaScript 开发可扩展的实时应用程序之前需要了解的创新解决方案。

### 使用 WebSocket 创建实时应用程序

当您选择在 [如 Node.js 这样的运行时环境](http://node.js) 中构建您的 RTA 或使用 Next.js 等框架时，建议您 [实现 WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)。WebSocket 是一种通信协议，它允许在单个 TCP 连接上建立全双工通信通道。与 HTTP 相比，WebSocket 是双向的，允许客户端和服务器都发起数据传输——从而实现实时交互。同样，该协议以其以下特点而闻名：

- **低延迟**：数据可以立即传输，从而创造出更佳的用户体验。
- **高效性能**：WebSocket 不会为每次交互建立新的连接，从而进一步减少实时应用程序中的延迟。
- **双向**：客户端和服务器可以同时发送数据，而无需等待请求。

尽管 WebSocket 的性能优势很多，但该协议在安全性方面并非没有漏洞。这就是为什么开发人员在使用 JavaScript 开发 RTA 时必须始终遵守安全最佳实践，实施诸如数据验证、输入清理、访问控制和身份验证等措施。

通过建立强大的安全策略，可以防止 [常见的威胁，如跨站点脚本 (XSS) 攻击](https://thenewstack.io/xss-vulnerability-discovered-in-backstage-software-catalog/)、跨站点请求伪造 (CSRF) 攻击和会话劫持。

WebSocket 是开发实时、交互式、动态和协作式 RTA 的强大解决方案，它可以轻松地发布实时更新并促进即时交互。这种性能水平确保了在 [WebSocket 中构建的应用程序可以轻松扩展](https://thenewstack.io/the-challenge-of-scaling-websockets/)，而不会影响数据传输速度和用户体验。

### 使用服务器发送事件 (SSE) 进行实时更新
服务器发送事件 (SSE) 是一种基于 HTTP 的技术，它为开发人员提供了一个名为 EventSource 的 API，允许应用程序轻松连接到服务器并接收来自服务器的更新。如果实时应用程序需要更复杂的更新，而不是简单的文本警报或新的价格更新，那么这是一个高级解决方案。对于标准更新，WebSocket 就足够了。

SSE 也是单向的，与 WebSocket 不同，事件不可用二进制格式——只能使用 UTF-8。但是，[SSE 相对于 WebSocket 的两个主要优势](https://softwaremill.com/sse-vs-websockets-comparing-real-time-communication-protocols/#:~:text=Probably%20the%20biggest%20difference%20between,any%20events%20from%20both%20sides.) 是对自动重新连接和事件 ID 跟踪的内置支持。这意味着，如果断开连接，将自动尝试重新连接，而事件 ID 跟踪确保在断开连接期间不会丢失任何消息。

SSE 比 WebSocket 灵活度低，但在 [构建实时应用程序](https://auth0.com/blog/developing-real-time-web-applications-with-server-sent-events/) 时可能是一个更好的解决方案，这些应用程序具有简单的用例，主要侧重于发送实时更新 *并且* 不需要频繁的客户端到服务器请求。

### Socket.io（事件驱动库）
[Socket.io](http://socket.io) 是一个事件驱动的库，它促进客户端和服务器之间的实时、双向通信。除了是一个库之外，Socket.io 也是一个协议，可以使用 Node.js 实现，[使用 WebSocket 提供其核心功能](https://www.linode.com/docs/guides/using-socket-io/)。

但是，Socket.io 通过心跳和超时等附加功能改进了标准 WebSocket 提供的功能。心跳是一种 [持续检查客户端和服务器之间是否建立连接的机制](https://socket.io/docs/v4/how-it-works/)。同时，超时——类似于 Node.js EventEmitter——在连接到服务器时设置超时，以避免无限期等待，这会影响用户体验。

在大多数情况下，Socket.io 通过提供附加功能（如自动重新连接和能够将事件（如警报）同时广播到所有连接的用户）来改进 WebSocket。这使得 Socket.io 成为实时聊天和即时消息应用程序的热门选择，尽管该库有广泛的用例。

## 结论
[JavaScript 的多功能性使其成为开发人员构建可扩展实时应用程序的热门选择](https://www.sencha.com/blog/how-javascript-has-become-the-most-utilitarian-programming-language/#:~:text=JavaScript%20is%20undoubtedly%20the%20most,side%20and%20client%2Dside%20applications.)，并得到 WebSocket 等通信协议的支持，这些协议可以通过 Socket.io 等事件驱动库变得更加强大。

这些解决方案确保 RTA 具有低延迟和高性能，同时促进双向通信以避免同步问题等挑战。

在构建可扩展的 RTA 时，安全性也必须是一个关键的考虑因素，遵循最佳实践以确保每个数据传输都经过验证和编码，并且所有用户都经过身份验证。