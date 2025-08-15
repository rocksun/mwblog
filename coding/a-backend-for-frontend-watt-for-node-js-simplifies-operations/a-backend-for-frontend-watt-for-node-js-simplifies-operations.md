
<!--
title: Backend for Frontend：Watt for Node.js 简化操作
cover: https://cdn.thenewstack.io/media/2025/08/c1f7b514-1922_duesenberg_indianapolis_500_winner_.jpg
summary: 杜森博格是美国豪华汽车制造商，Watt 类似于 Node.js 的应用平台，提供结构和自动化，简化 Node.js 应用开发。Platformatic 由 Luca Maraschi 和 Matteo Collina 创建，旨在连接开发者和运维人员，解决如事件循环阻塞等问题，并支持 JavaScript 框架，加速前后端融合。
-->

杜森博格是美国豪华汽车制造商，Watt 类似于 Node.js 的应用平台，提供结构和自动化，简化 Node.js 应用开发。Platformatic 由 Luca Maraschi 和 Matteo Collina 创建，旨在连接开发者和运维人员，解决如事件循环阻塞等问题，并支持 JavaScript 框架，加速前后端融合。

> 译自：[A Backend for Frontend: Watt for Node.js Simplifies Operations](https://thenewstack.io/a-backend-for-frontend-watt-for-node-js-simplifies-operations/)
> 
> 作者：Loraine Lawson

杜森博格（Duesenberg）是一家美国赛车和豪华汽车制造商，成立于 1920 年。它与众不同之处在于，它会运送发动机、底盘、车架、轮胎和车轮，但买家必须另外付费给豪华马车制造商来制造车身。有趣的事实：Jay Leno 拥有一辆 1932 年的杜森博格 SJ Murphy 敞篷车，其价值难以估算，因为它太罕见了，但一辆 1931 年的 Model J 隐藏式顶篷车型在 2023 年的拍卖会上以超过 400 万美元的价格售出。

[Watt](https://docs.platformatic.dev/docs/getting-started/quick-start-watt) 对于 [Node.js](https://thenewstack.io/node-js-24-your-next-big-frontend-upgrade/) 来说，也是如此。

Node.js 提供了引擎和原始机械部件，用于构建实时应用程序、API 和[微服务](https://thenewstack.io/introduction-to-microservices/)等。它用于构建具有 RESTful API 的 Web 应用程序。[Express.js](https://thenewstack.io/a-showdown-between-express-js-and-fastify-web-app-frameworks/)、[NestJS](https://thenewstack.io/configure-microservices-in-nestjs-a-beginners-guide/)、[Hono](https://thenewstack.io/hono-shows-the-way-for-microframeworks-in-a-post-react-world/) 和 [Fastify](https://thenewstack.io/introducing-fastify-speedy-node-js-web-framework/) 都使用 Node.js，它可以运行 [JavaScript](https://thenewstack.io/introduction-to-javascript/)。它甚至被 JavaScript 框架（如 [Next.js](https://thenewstack.io/next-js-react-router-tanstack-when-to-use-each/)）所利用，Next.js 使用 Node.js 进行服务器端渲染 (SSR)。

Watt 使 Node.js 使用起来更加“舒适”，为使用 Node.js 构建应用程序提供结构和自动化。它是一个专门的工具包，可以自动组装 Node.js 部件。Watt 由 [Platformatic](https://docs.platformatic.dev/) 创建，是一个 [Node.js 应用程序平台](https://blog.platformatic.dev/introducing-the-node-application-platform)。它提供了一个预配置和管理的应用程序服务器实例，但它还可以做更多的事情。例如，它可以帮助构建、管理服务器以及创建 [API](https://thenewstack.io/generative-ai-creates-apis-faster-than-teams-can-secure-them/) 和微服务。

## 连接世界的桥梁

Platformatic 是一个开源开发平台，可帮助开发人员构建和管理 Node.js 应用程序。联合创始人 [Luca Maraschi](https://www.linkedin.com/in/lucamaraschi/?originalSubdomain=ca)（首席执行官）和 [Matteo Collina](https://www.linkedin.com/in/matteocollina/?originalSubdomain=it)（首席技术官）在意识到企业需要 Node 方面的帮助后创建了 Watt。Maraschi 说，例如，许多银行使用 Java 作为其骨干。

他说：“缺少的是连接这两个世界的桥梁，即开发人员的世界和运营商的世界。”“我们知道那里缺少一些东西，Node 的应用程序服务器真正缺少的是可以真正协调开发人员和运营商之间对话的东西。”

[![Watt 及其如何与 Node.js 和 Next.js 等框架交互的图表](https://cdn.thenewstack.io/media/2025/08/1a45e74a-watt.jpg)](https://cdn.thenewstack.io/media/2025/08/1a45e74a-watt.jpg)

图片来自 [Platformatic 的博客](https://blog.platformatic.dev/introducing-the-node-application-platform)。

他们开始开发 Watt，之所以这样命名，是因为他们认为这是“Node 世界的第二次伟大革命”，Maraschi 说。

他说：“正如蒸汽机更好地改变了工业世界一样，我们认为需要一个引擎来改变整个 Node 企业生态系统中的游戏规则。”

他补充说，这几乎就像一种语言，可以在企业世界的两个领域之间创建一个共同的桥梁。

Maraschi 说：“在 Java 中，您有像 [JBoss](https://thenewstack.io/red-hat-jboss-data-grid-not-just-storing-java-objects-anymore/)、[WebSphere](https://www.ibm.com/products/websphere-application-server) 和 [WebLogic](https://www.oracle.com/java/weblogic/) 这样的应用程序服务器，仅举三个最受欢迎的例子。”“Node 需要一些可以创造同样舒适感的东西。我们知道有一些功能是必需的——比如日志记录、指标、遥测、多线程，Watt 开箱即用为我们提供的所有功能——它们也应该为 JavaScript 和 Node 世界提供。”

## Watt 解决的问题示例

Collina 指出了 [事件循环阻塞](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop) 的问题。

他说：“本质上，开发人员很容易通过滥用 Node.js 并从根本上导致事件循环阻塞来‘拒绝服务’他们的系统；并且由于这个问题，如果事件循环被阻塞，什么也无法执行。”“因此，做任何工作，任何事情进入那里，本质上都是不好的。”

Collina 补充说，这是一个只能缓解和预防的问题，但开发人员很难解决。

Collina 说：“本质上，回收该应用程序。”“您告诉它优雅地关闭该应用程序，停止向该系统发送请求，然后在原地启动一个新的应用程序，从而保持事件循环的健康和系统的健康。”

Collina 和 Maraschi 在他们与 Platformatic 的咨询工作中发现这是一个大问题，他补充说。Platformatic 没有强迫开发人员更改他们的代码，而是开发了一个自我监控系统，可以检测 Node.js 应用程序的事件循环何时被阻塞。

Collina 说：“他们要么不愿意实现它，要么不知道如何实现它，或者更糟糕的是，他们的框架不支持它，那是可能出现的最糟糕的情况，因为如果他们的框架不支持安全地执行此操作的方法，那么他们基本上只能靠自己。”“为了手动实现这种解决方案，您需要一些‘底层’知识。”

Watt 的一个关键特性是它会获取您的应用程序并在一个线程中运行。

他说：“通过这种二元性，我们可以做很多普通的 Node 应用程序无法做的事情，因为我们本质上为该系统嵌入了一个监视器。”

Watt 还支持套接字选项，这是一个可配置的参数，允许应用程序修改网络套接字的行为，称为来自 Linux 内核的 `SO_REUSEPORT`。它允许系统运行多个独立的进程来绑定并侦听同一端口。当流量很高时，它可以帮助提高性能，使其更具弹性和性能。`SO_REUSEPORT` 最近已添加到 Node.js 中。

## 前端的后端

Watt 开箱即用地支持 JavaScript，并且其所有功能都与 JavaScript 完全兼容。它支持的框架包括 Remix、Astro 和 Next.js，以及带有 TypeScript 的 Node.js 应用程序。

Collina 说：“如果您想在 [Kubernetes](https://thenewstack.io/kubernetes/) 上运行 Next.js，这可能是您应该使用的工具。”“它具有所有开箱即用的功能。……对于许多公司来说，这是一个很大的难题，尤其是对于 Next.js，但也包括所有其他前端框架。”

还有一个用于 [Apache Kafka](https://thenewstack.io/the-new-look-and-feel-of-apache-kafka-4-0/) 的适配器，这是一个用于构建实时应用程序的分布式事件流平台。

此外，Watt 使用名为 [AI Warp，一个 AI 网关](https://blog.platformatic.dev/ai-warp-1-0-0) 的 Platformatic 工具支持无服务器函数。

虽然 Watt 是一种后端工具，但它通过显著加快工作流程并减少开发瓶颈，从而显著帮助 [前端开发人员](https://roadmap.sh/frontend)。例如，Watt 可以从数据库模式生成一个功能齐全的 API。这意味着前端开发人员不必等待后端团队构建 API，就可以开始构建和测试他们针对真实 API 的用户界面。

前端开发人员还可以使用它来创建一个用于概念验证的全栈应用程序，而无需专门的后端人员。

有了 Watt，创建者的目标是使后端非常接近前端，以创造最佳性能。

Maraschi 说：“我们实际上相信，对于这些现代应用程序，后端和前端会融合到这个全栈中。”“这是向企业承诺的，这个全栈应用程序。”