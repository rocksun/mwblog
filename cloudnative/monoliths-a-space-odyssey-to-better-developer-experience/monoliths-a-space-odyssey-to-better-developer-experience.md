<!--
title: 单体应用：通往更优开发者体验的太空奥德赛
cover: https://cdn.thenewstack.io/media/2024/01/e580229f-spaceart-1024x576.jpg
-->

通常情况下，默认的单体应用会被逐步淘汰，让位于解耦和容器化的微服务架构，但如果你有意识地构建一个单体应用呢？

> 译自 [Monoliths: A Space Odyssey to Better Developer Experience](https://thenewstack.io/monoliths-a-space-odyssey-to-better-developer-experience/)，作者 Sarah Morgan。

这篇文章是系列文章的第一篇。

除了描绘了一个迷人但具有杀人倾向的 AI 的电影《2001: A Space Odyssey》外，该影片最为人记忆深刻的或许是其巨大的石碑。这些貌似突然出现的完美光滑、深邃如夜空的石板，引导着史前的猿猴，以及后来的一支先进的宇航员队伍，向前触摸并试图理解它们，窥视它们可能包含的秘密。

电影刻意对这些石碑的意义保持模糊。它并没有提供具体的真相，而是反映了人类的雄心壮志和成长，呈现给任何可能观察它们的人。

开发者对于单体应用（monoliths）有一个不同的概念。虽然同样神秘且引人注目，但通常缺乏完美的比例和无与伦比的表面处理，软件单体讲述了一个团队通过代码重构、关键人员的雇佣和离职，以及业务需求的重大变化来设计和发展应用的故事。

与电影中石碑的模糊不同，软件中的单体故事只有两种走向：

1. 你的应用有机地发展到一个程度，你开始担心服务之间的紧密耦合以及前端客户端与后端业务逻辑之间的灰色地带。可能会有一次操作性的惊吓，比如最近引入的一个 bug 阻止用户保存他们的数据，这成为最后一根稻草：所有新的服务都必须在单独的存储库中开发，并通过 API 层连接起来。
2. 其次，你被迫将复杂的传统单体应用分裂成几十，甚至几百个离散的 API，作为你的首席技术官在一次创业公司的会议上从一个承诺将所有主流开源技术打包成“一体化软件交付平台”的战略的一部分。

起初，人们对你的单体应用的离世并不经常感到伤感。微服务简化了你在整个应用中范围重大或破坏性变更影响的方式，你的同行喜欢他们可以用除 JavaScript 之外的任何语言开发新的 API。再次，每个人都开始感觉自己是贡献者，编写新功能并解决复杂的优化难题，而不是坐在为旧单体的每个主要版本发布而进行数小时会议的情况。

你的单体的消亡使得围绕组织开发人员和工程师方面的一些小问题变得平稳，但它也引入了一些最初你没有完全考虑到的新的技术要求。你开始思考：我们花在重构和配置基础设施，然后处理微服务的挑战的所有时间，鉴于我们面临的工程问题的复杂性，这一切都是必要的吗？

选择微服务是因为你认为它能解决你的技术问题，但实际上它更适合解决组织和协作问题，而你的公司几乎肯定没有这些问题。通过让你的单体应用消亡，你在系统中引入了许多不必要的复杂性，比如：

- 你曾经只需用一个命令就能启动的本地开发环境，现在需要进行更复杂的操作，比如设置本地 Kubernetes 集群或支付平台作为服务，以便在每次运行 CI/CD 流水线时启动新的实例。
- 配置和编排工作，也就是运维，从你的核心竞争力中夺走了时间：构建新功能，并将质量、安全性和良好策略层叠到你的应用中。
- 你对系统有深刻的了解，但对其周围的环境知之甚少，导致你或其他人在没有全面了解应用如何运作的情况下应对事故。你被迫在没有人指导的情况下调试未知领域。
- 在每次 CI 运行时启动整个应用的临时部署，时间、成本和复杂性都达到了极限，导致成本和复杂性不断增加。
- 共享库无意中创建了版本碎片化，而不是简化常见的转换和功能，因为每次更改都需要在依赖它的每个服务上进行广泛测试，除非你使用上次为你工作的版本。

如 Kelsey Hightower 警告的那样，你从“[编写糟糕的代码到构建糟糕的基础设施](https://changelog.com/posts/monoliths-are-the-future)”，寻找你希望从一开始就拥有的工程纪律。或者，正如[Basecamp](https://basecamp.com/)的CTO和[Ruby on Rails](https://rubyonrails.org/)的创作者David Heinemeier Hansson[所说](https://world.hey.com/dhh/even-amazon-can-t-make-sense-of-serverless-or-microservices-59625580)，你增加了不必要的复杂性：“在几乎所有情况下，用网络调用和服务分区替换方法调用和模块分离，而这一切都在一个一致的团队和应用程序中进行，简直是疯狂的。”

现在，在这个“疯狂”中，你开始后悔自己没有保留单体应用。也许，如果你是幸运的少数人之一，就像 [Twilio 内的 Segment 团队](https://segment.com/blog/goodbye-microservices/)一样，你可以尝试用一种有意图的新型单体应用：一个你有意识构建的单体。

## 另一种故事：有意识单体的成熟

这个故事的开始也有两种方式：

1. 你从第一天就致力于这种架构，不是因为单体应用是开始开发应用的默认方式，而是因为你知道如果不需要微服务的复杂性，前方将会有挑战。
2. 你尝试过微服务，但由于公司规模和需求，未能实现协作天堂、可扩展性和运维简单性的承诺。你痛苦地意识到微服务给方程式注入了太多的复杂性，正在谨慎地设计一个新的综合服务。

随着你继续沿着单体的道路前进，这种架构成功扩展，因为你意识到了常见的担忧和误解。

“**开发者不喜欢在单体应用中工作。**”虽然没有官方的调查表明开发者更喜欢哪种方式，但只要单体应用[保持性能良好](https://www.craigkerstiens.com/2019/03/13/give-me-back-my-monolith/)，开发者在单一代码仓库中的工作体验往往更简单。通过按文件夹和调用分隔服务，而不是基础设施即代码、不同语言和不同代码仓库，你甚至可以将重大变更同步到单一的拉取请求中，以提高速度和质量。

当 Segment 团队转向有意识的单体应用时，他们在共享库中进行的改进从一年的 32 次增加到了接下来的短短六个月的 46 次。

“**单体应用就是一个没人能理解的黑盒。**” 很多人也对微服务有同样的看法。

“**单体应用很慢。**” 单体应用并不是垂直扩展的理想选择，但它们可以独特地快速。数据传输保持在进程内存中，比起机器间通信更便宜和更快，并且不必经过分布式服务的编排逻辑。当需要进行水平扩展时，你可以依赖具有更可预测性能和成本的服务，比如 AWS EC2，而不是依赖无服务器选项。此外，有许多应用性能监控工具，比如 [Scout APM](https://scoutapm.com/?utm_source=tns&utm_medium=affiliate&utm_campaign=q1_2024&utm_content=monolith1_blog)，专门设计帮助你识别优化机会，甚至到特定代码行。

“**单体应用需要进行更多的测试。**” 这似乎是个好问题。正如 Hightower 所建议的那样，编写基础设施并不是解决[编写糟糕代码](https://thenewstack.io/its-no-longer-about-how-you-write-code-but-how-you-operate-it/)问题的方法，这通常归结为编写不好的测试，或者不够多的测试。

“**你不能使用新的（云原生）技术！**”是的，单体应用可能无法在最新的无服务器或容器编排潮流上运行，但你仍然有选择。例如，你可以部署一个服务网格，比如 [Linkerd](https://linkerd.io/) 或 [Istio](https://istio.io/)，通过 [mTLS](https://scoutapm.com/blog/securing-ruby-applications-with-mtls) 将你的单体应用连接到外部服务。你可以通过负载均衡器和多云部署来提高可伸缩性，或者将你的应用连接到 OpenTelemetry Collector，将日志、指标和跟踪发送到当今众多的可观测性解决方案之一。

了解这些误解及其现实，你还可以实施应对构建单体应用的真正挑战的策略：

- 确保所有服务使用给定依赖的单一版本，以防止版本碎片化。
- 像 Segment 在其 [Centrifuge 项目](https://segment.com/blog/introducing-centrifuge/)中所做的那样，在基础设施和外部世界之间构建一层，用于排队请求/消息/事件，并优雅地处理故障，而不是期望你的单体应用不会崩溃。
- 构建具有模拟或[记录的](https://github.com/vcr/vcr) HTTP 交互的强大测试套件，以进行快速、确定性的测试，最小化任何小错误导致应用的部分或全部崩溃的风险。
- 消除抽象和不必要的概念模型，倾向于简单性，认识到微服务架构解决了企业规模下的人类协调问题，这可能不是你当前工作的问题。
- 用 Hansson 的话说，你要“将[系统集成到](https://m.signalvnoise.com/the-majestic-monolith/)一个人无法全部理解的程度”。如果 Basecamp 还没有达到这一点，你可能也不会。

关键在于，你不是因为单体应用是默认选择而构建单体应用。即使是最出于良好意图的单体应用也可能走向失败。你是有意图地构建单体应用，因为它解决了你组织当前存在的一级工程问题。因为你仍然可以将你的应用全部理解在脑海中。因为你不想一旦微服务不再流行，就意识到你对所构建的东西了解甚少，然后不得不从头开始。

有意图地构建一个单体应用并亲自体验吧：几乎每次单体应用都是正确的选择。

单体应用的最大优势之一在于，谁能从微服务架构导致的成本飙升中获益最多。请继续关注我们系列的第二篇文章，但在那之前，给你一个提示：这个人不是你。
