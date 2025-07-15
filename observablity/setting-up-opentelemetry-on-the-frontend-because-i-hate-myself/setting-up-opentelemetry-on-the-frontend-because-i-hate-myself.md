
<!--
title: 前端OpenTelemetry配置：我与痛苦共舞
cover: https://cdn.thenewstack.io/media/2025/07/dfda0181-frown.jpg
summary: 本文探讨了在前端使用 OpenTelemetry 的挑战，指出其最初设计是为了后端服务，与前端的事件驱动和长时间运行的特点不兼容。文章强调了数据关联方式（立即关联 vs. 稍后关联）的差异，并提出了务实的改进建议，包括关注前端需求、逐步改进 JavaScript 库，并与社区合作改进 OpenTelemetry。
-->

本文探讨了在前端使用 OpenTelemetry 的挑战，指出其最初设计是为了后端服务，与前端的事件驱动和长时间运行的特点不兼容。文章强调了数据关联方式（立即关联 vs. 稍后关联）的差异，并提出了务实的改进建议，包括关注前端需求、逐步改进 JavaScript 库，并与社区合作改进 OpenTelemetry。

> 译自：[Setting Up OpenTelemetry on the Frontend Because I Hate Myself](https://thenewstack.io/setting-up-opentelemetry-on-the-frontend-because-i-hate-myself/)
> 
> 作者：Hazel Weakly

想象一下：你度过了一个美好的下午，做了美味的晚餐，在附近散步，感觉非常愉快。嗯，这可不行。愉快？在这种经济形势下？我有一个完美的解决方案！在你最喜欢的 [ReactJS](https://thenewstack.io/instrumenting-a-react-app-using-opentelemetry/) 前端 side project 中设置 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/)。当你感觉快乐，需要在周一早上恢复严肃表情时，这是一个理想的解决方案。

只需 82 个令人困惑的说明，这些说明可能无法与你最喜欢的工具链一起使用，你也可以迷失在微妙的细节迷宫中。事实上，我们将免费提供 [应用程序异步代码的性能损失](https://github.com/angular/angular/blob/main/packages/zone.js/MODULE.md)！

但是等等，还有更多！仅仅安装依赖项是不够的，你还必须使用它们。幸运的是，使用 OpenTelemetry 来检测前端肯定会让你皱眉。从面临将 [服务器端渲染](https://github.com/open-telemetry/opentelemetry-demo/blob/96b292d5f3281d1bbde0309a8d9325475f356a4b/src/frontend/pages/_document.tsx#L22) 与 [客户端 hydration](https://github.com/open-telemetry/opentelemetry-demo/blob/96b292d5f3281d1bbde0309a8d9325475f356a4b/src/frontend/pages/_app.tsx#L27-L28) 相关联的上下文问题，到观察 [用户会话在页面导航时中断](https://github.com/open-telemetry/opentelemetry-demo/blob/96b292d5f3281d1bbde0309a8d9325475f356a4b/src/frontend/gateways/Session.gateway.ts)，除非你 [小心地将其穿梭于本地存储](https://github.com/open-telemetry/opentelemetry-demo/blob/96b292d5f3281d1bbde0309a8d9325475f356a4b/src/frontend/utils/telemetry/SessionIdProcessor.ts)，再到 [处理用户关闭或切换选项卡时遥测数据消失的问题](https://github.com/highlight/highlight/blob/881eb80b8065b13c7b388d9b3907bfb2a98a7bb9/sdk/highlight-run/src/client/otel/exporter.ts#L13-L20)，你一定会找到一种体验恼怒的方法。

如果这还不够，你总是可以通过问自己如何向“main” span 添加属性来触发存在危机。是否有 API 方法可以做到这一点？当然没有。幸运的是，所有酷孩子都知道引用 Jeremy 的博客文章，了解 [一个巧妙的解决方法](https://jeremymorrell.dev/blog/a-practitioners-guide-to-wide-events/#write-a-middleware-to-help-you)（当然，使其在浏览器上工作留给读者作为练习）。

好吧，这里有点夸张，而且事情正在随着时间的推移而改善，但摩擦是普遍存在的，尤其是与后端的 [Java](https://thenewstack.io/introduction-to-java-programming-language/) 或 [Go](https://roadmap.sh/golang) 相比。也就是说，嗯……等等，前端开发人员不是行业的大多数吗？他们不是几十年都需要高基数可观测性吗？我们是怎么走到这一步的？也许我们需要退一步，问问我们是否以错误的方式处理前端可观测性。

## 你太上下文了，宝贝，你甚至不知道

让我们退一步，谈谈前端的 OpenTelemetry 是如何发展到今天的。首先，OpenTelemetry 的 [JavaScript 实现](https://thenewstack.io/javascript/ "JavaScript implementation") 正在尽其所能。考虑到所有因素，该实现（及其维护团队）做得非常出色！虽然抱怨前端的事情有多烦人可以让人得到精神宣泄，但了解我们是如何走到这一步的，对于确定我们可以切实改进事情的方法至关重要。

稍微退一步，我们真正看到的是在 JavaScript 中实现 OpenTelemetry 的 SDK 和 API 规范的难度，以及实现的设计怪癖的结合。

回顾历史，OpenTelemetry 最初的设计是供无状态且为多个租户提供服务的后端使用，这些请求的生命周期很短。这些请求通常持续不到 200 毫秒左右，并且涉及手动检测的子服务调用链，其深度非常浅。诸如用户会话之类的持久性概念自然会在每个请求中携带，因此处理长期状态对于服务器来说从来都不是真正的问题。

鉴于后端托管在数据中心中，网络快速且可靠，因此最大限度地减少遥测本身的有效负载很少成为一个大问题。此外，由于原始实现的关注点在于服务，因此将追踪可视化并将其设计为调用堆栈非常有意义；这种调用堆栈设计在 API、SDK 和数据规范中根深蒂固。

所有这些选择在上下文中都没有什么不好，而且它们对于今天的大多数后端系统仍然有意义。不幸的是，前端与许多这些假设并不兼容，这使得使用 OpenTelemetry 有时特别具有挑战性。

一个简单的例子是将其用于在事件循环架构中工作的异步代码：在 ReactJS 应用程序中经常遇到这种情况。另一个例子更难看到，但事实证明，处理事件驱动架构和 [OpenTelemetry 中的长时间运行的 span](https://thenewstack.io/opentelemetry-challenges-handling-long-running-spans/) 需要类似的方法。这并非巧合。这两种架构有几个相似之处，其中最突出的是需要在遥测管道内部表示不完整的信息（类似于预写日志的概念）。

## 数据流的形状

当我们构建系统时，开发人员习惯于紧密相关的数据流和代码结构。但是，遥测并非如此。使用遥测，开发人员需要考虑 [用户如何与系统交互](https://thenewstack.io/the-case-for-user-focused-observability/)。换句话说，我们使用 OpenTelemetry 来讲述系统行为的故事，以便更好地理解它。

对于后端，通常用户和开发人员是同一批人，因此叙述可以与代码结构紧密匹配，特别是如果你实践 DevOps 文化，团队运营他们构建的系统。相反，对于前端，用户和开发人员之间的差距扩大了，因为用户交互与代码结构没有任何相似之处。

这很好。嗯，除非你的工具假设代码结构和用户交互之间存在很强的相关性。糟糕！这种天真的假设最终使前端的生活变得非常麻烦。理想情况下，理解前端涉及查看用户与系统交互时的事件的时间流。每个用户交互都会讲述一个故事，开发人员需要能够将这些故事拼凑起来，才能了解发生了什么。但是，这会带来摩擦，因为它与最初构建工具的方式背道而驰。

将这种紧张关系想象成给人播放音乐专辑与让他们以任何顺序播放歌曲之间的区别。使用专辑，你知道歌曲的顺序，因此你可以使专辑非常连贯。然后出现了音乐流媒体：现在人们选择歌曲的顺序并在专辑之间混合，这意味着无法推断出你的歌曲在他们的聆听体验的上下文中是如何出现的。随着时间的推移，这会鼓励你改变创作音乐和发布音乐的方式。事实上，我们已经从将专辑设计成一个连贯的艺术品，转变为声明歌曲需要每七秒钟有一个 hook。

将相似之处拉回到技术领域：用户是不可预测的，他们会从多个选项卡中使用同一个应用程序，并且他们可能会从一个设备开始并在另一个设备上继续。现实世界是混乱的，永远无法很好地映射到你的代码结构。没有什么比前端和后端的检测连接在一起形成混乱的上下文泥潭时更明显的了。

那么，这对于设计适用于两者的有效检测意味着什么？嗯，这意味着你可能会度过一段糟糕的时光。这也意味着你可能会选择不同的数据结构、代码模式和检测技术（这本身可能就是一个系列）。除非我们真的没有 OpenTelemetry 的选择。要理解为什么，我们需要进一步挖掘。

## 立即关联与稍后关联

首先，我们需要谈谈可观测性供应商。他们如何存储和摄取数据对于检测库的后续发展具有非常深刻的含义。简而言之，对于可观测性供应商来说，理想的情况是客户发送完整的数据，以便供应商可以按原样将数据附加到其数据存储中。这在很大程度上是今天 OpenTelemetry 的情况（使用开箱即用的功能），但采用这种方法会导致通过网络传输的大量数据重复，因为数据被最大程度地非规范化。例如，OpenTelemetry 的语义约定建议使用 `service.address` 设置，但它会在发送的每个 span 上重复——尽管它是一个永远不会改变的值。

如果想象一下添加有用的调试数据，例如构建 ID、服务版本、用户 ID 或用户代理信息，这将迅速增加。带宽的增加在浏览器中更加令人痛苦，因为浏览器 OpenTelemetry 导出器 [尚不支持压缩](https://github.com/open-telemetry/opentelemetry-js/issues/5686)。

在一个网络既快速又可靠的世界中，权衡取舍是完全有意义的。毫不奇怪，OpenTelemetry 开发了一种带宽密集但计算量轻的规范。将数据处理的复杂性推向客户更有意义，因为许多原始供应商的实现都受到了内部工具的启发，在历史上，同一家公司构建了检测、库 *和* 遥测后端。

一旦进入前端服务的世界，所有这些约束都开始改变。前端 [计算和网络带宽受到严重限制](https://embrace.io/blog/best-practices-for-monitoring-network-conditions-in-mobile/)，当考虑到移动浏览占网络上所有流量的一半以上时，情况会更加恶化。因此，通过重复数据删除并让供应商关联数据，将数据管理的复杂性卸载到可观测性供应商是理想的。出于错误检测和带宽原因，[发送不完整的追踪作为快照](https://www.cncf.io/blog/2024/06/14/why-embrace-created-span-snapshots-for-mobile-observability-with-opentelemetry/) —— 而不是将整个追踪保存在内存中 —— 也是有意义的。当然，这与大多数现有工具、库和供应商支持的相反，尽管这种情况正在慢慢改变。

你可以将这种紧张关系视为“立即关联”与“稍后关联”。在“立即关联”系统中，你需要发送一个完整的 span，其中包含你想要一次性查询的所有数据，而无需稍后更新。“稍后关联”系统意味着你可以在拥有任何数据时发送它，但你必须稍后进行工作以关联它（通过索引），这可能会变得非常昂贵。听起来很熟悉？这是我们几十年一直在进行的旧数据库辩论。索引还是没有索引？一张表还是多张表？我们应该使用模式吗？我们应该规范化数据吗？

最终，这取决于情况，但我们将遇到的问题是，虽然这确实取决于情况，但前端和后端最有可能最终会得出不同的理想；当两者相遇时，情况会变得混乱。

## JavaScript 到底是怎么回事？

唷！内容很多，但这是有用的背景知识。也就是说，我们开始谈论 JavaScript，感觉我们有点跑题了……所有关于上下文、流媒体和关联的讨论与前端 Web 上的 JavaScript 有什么关系？

答案首先是观察到 JavaScript 处于独特的位置，它是 Web 浏览器支持的唯一可以直接与浏览器的文档对象模型 (DOM) 交互的编程语言；它也恰好在后端非常流行。因此，它以一种特别令人沮丧的方式遇到这些问题：JavaScript 中最初的 OpenTelemetry 检测库是为 NodeJS 构建的，并在后端环境中运行，这意味着它们在前端引入了很大的摩擦。哎呀！

我们能做些什么吗？如果我们能做到这一点，那就太好了。也许我们“只是”调整 JavaScript 库，制作一些 [浏览器友好的版本](https://github.com/embrace-io/embrace-web-sdk)，然后砰的一声，完美？太棒了！每个人都很高兴，一切都井井有条。我已经听到独角兽在草地上嬉戏了。等等，那是什么？独角兽不嬉戏？我要假装我没听到。

回到现实，如果你想知道为什么浏览器友好的 OpenTelemetry 库是不够的，请问自己一个问题：“我们如何以一种在实际网络条件下对前端用户友好的方式将数据发送到符合 OpenTelemetry 规范的后端？”

答案会有点可怕：事实证明，你有点不能（至少，使用 OpenTelemetry 开箱即用：但是，[Embrace](https://embrace.io/?utm_content=inline+mention) [解决了这个问题](https://www.cncf.io/blog/2024/06/14/why-embrace-created-span-snapshots-for-mobile-observability-with-opentelemetry/)）。那么，我们是否被困住了？是否永远注定要在平庸的工具、古怪的库和令人沮丧的语言支持的土地上游荡，因为 OpenTelemetry 目前暗示的数据模型与前端应用程序使用的数据模型不匹配？如果我们的目标是完美，那么有人可能会这样说，但如果我们不让完美成为优秀的敌人，我们现在就可以解决前端的几个直接挑战，即使不改变 OpenTelemetry 的工作方式。

## 务实的未来之路

前端开发人员应该为 OpenTelemetry 得到更好的东西，特别是考虑到他们可以从采用高基数和高上下文检测中获益匪浅。了解用户体验，尤其是在交互如此不受约束的情况下，会改变游戏规则。

我认为我们可以实现这一目标。这是我的建议：

1. 让我们弄清楚前端 Web 现在最需要什么。
2. 我们尽快实现这一目标，逐步进行，而不会破坏所有其他 JavaScript 用户。
3. 然后，使用来自社区的反馈来改进 OpenTelemetry 本身。
4. 协作构建更强大的可观测性体验，为每个人服务。

你心动了吗？我知道我很心动，而且我不是唯一一个。恰好 OpenTelemetry 社区启动了一个前端浏览器特别兴趣小组 (SIG)，致力于改进浏览器中的 OpenTelemetry。[前端浏览器 SIG](https://github.com/open-telemetry/community/blob/main/projects/browser-phase-1.md) 的一些我最喜欢的举措是：

* 改进浏览器中加载和卸载的处理
* 更好的会话支持，而不会破坏现有的 OpenTelemetry 数据模型
* 更好的客户端事件日志记录模型、依赖项大小和跨异步边界跟踪上下文

这些都是巨大的，这仅仅是个开始。我喜欢这一点的原因是，无论改进前端的 OpenTelemetry 看起来多么困难，都有一个国际社区的人们热衷于一步一步地让事情变得更好。今天的开发痛苦将慢慢地但肯定地成为遥远的过去。它不会在一夜之间发生，但它会发生。我们将能够一路合作，使了解我们的用户并改善他们的体验成为参与其中的每个人更快乐、更高效的体验。

如果你想了解更多关于 OpenTelemetry 对浏览器的支持的信息，[请查看 7 月 31 日太平洋时间上午 10 点由 [Embrace](https://embrace.io/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-on-the-frontend) 主办的 [这个实时小组讨论](https://get.embrace.io/web-otel-panel/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-on-the-frontend)。