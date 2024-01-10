<!--
title: 领域驱动设计（DDD）与企业集成模式（EIP）20周年
cover: https://cdn.thenewstack.io/media/2024/01/2b76075e-clark-van-der-beken-chcyjyrqv74-unsplash-1024x576.jpg
-->

20年后的今天，两本领域驱动设计(DDD)和企业集成模式(EIP)经典书籍中提出的设计模式、原则和实践，依然具有重要参考价值

> 译自 [Celebrating 20+ Years of Domain Driven Design (DDD) and EIP](https://thenewstack.io/celebrating-20-years-of-domain-driven-design-ddd-and-eip/)，作者 Eric Newcomer。

二十年在每个人的生命中都是漫长的一段时间，但对于一本信息技术书籍来说，这几乎是整整一代的时间。

当然，如果你说的是[Eric Evans](https://www.linkedin.com/in/ericevansddd/)所著的《[领域驱动设计](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215/ref=sr_1_1？crid=P4FCDNOAPY99&keywords=domain+driven+design&qid=1698087311&s=books&sprefix=domain+drivcen%2Cstripbooks%2C93&sr=1-1&ufe=app_do%3Aamzn1.fos.006c50ae-5d4c-4777-9bc0-4513d670b6bc)》(Domain Driven Design， DDD)以及[Gregor Hohpe](https://www.linkedin.com/in/ghohpe/？originalSubdomain=sg)和[Bobby Woolf](https://www.linkedin.com/in/bobbywoolf/)合著的《[企业集成模式](https://www.amazon.com/Enterprise-Integration-Patterns-Designing-Deploying/dp/0321200683/ref=sr_1_1？crid=37ST2VCRX3N1F&keywords=enterprise+integration+patterns&qid=1698087355&s=books&sprefix=enterprise+integration+patterns%2Cstripbooks%2C91&sr=1-1&ufe=app_do%3Aamzn1.fos.006c50ae-5d4c-4777-9bc0-4513d670b6bc)》(Enterprise Integration Patterns， EIP)这两本开创性著作，它们最近刚刚庆祝了出版20周年。

[据微软介绍](https://learn.microsoft.com/en-us/archive/msdn-magazine/2009/february/best-practice-an-introduction-to-domain-driven-design): 领域驱动设计(DDD)是一套设计优雅对象系统的原则和模式集合。如果正确应用，它可以引导开发人员构建被称为领域模型的软件抽象。这些模型封装了复杂的业务逻辑，缩小了业务实际情况和代码之间的差距。

同时，《企业集成模式》为描述跨多种技术的大规模集成解决方案提供了一致的词汇和视觉表示框架，亚马逊网站对该书的介绍如是写道。它提供了65种模式的目录，并给出了真实世界的解决方案，以帮助工程师为其企业设计有效的消息传递解决方案。

然而，尽管许多东西已经改变，但这些经典书籍中的设计模式、原则和实践20年后仍然非常相关——在某些方面比以往更甚。

2022年12月31日，亚马逊网站上对[DDD](https://thenewstack.io/domain-driven-design-aids-planning-microservices-architecture/)的评论写道: “该书对于创建API很有帮助。读过这本书之后，我感觉在如何创建API方面远远领先于我的同龄人。”

类似地，EIP最近的一条亚马逊评论说: “现在是2023年，这本书仍然很相关......因为这本书不是关于任何特定技术，而是解释你可以反复运用的模式。”

有趣的是，这两本书都理解组件设计和集成是手牵手进行的。例如，DDD的[聚合模式](https://blog.eventuous.dev/aggregate-pattern-in-domain-driven-design-7ad823475099)警告分布式事务的共享数据库锁定方案的危险。

同样，EIP不仅仅是设计菜谱的列表，而且已经成为DDD提出的[面向消息集成](https://www.geeksforgeeks.org/what-is-message-oriented-middleware-mom/)的[普适语言](https://martinfowler.com/bliki/UbiquitousLanguage.html)。

“DDD和EIP是配合良好的对应部分。EIP侧重于帮助多个应用程序像一个整体一样工作，而DDD展示了如何在一个应用程序内对领域功能建模。” Woolf告诉The New Stack。 “它就像线条和盒子——你的架构需要两者，” Hohpe补充说。

## 持续关联

DDD和EIP仍然如此相关的一个明显原因是，它们本质上不是关于技术的书籍。它们是奠基性的书籍，关注概念和权衡取舍，同时将技术作为示例而不是主要主题。

EIP中正式化的模式列表是几个成功的商业集成产品的基础，比如Mule、Camel和WSO2企业集成器。这些产品每个都为模式提供了特定领域的语言模板，将设计模式转化为可执行的领域语言。

在过去的二十年中，DDD和EIP已经被证明可以简化复杂系统的设计和开发过程，并且最近被证明非常适用于[微服务](https://thenewstack.io/microservices/)模式。

围绕[单体与微服务的辩论](https://thenewstack.io/monolith-vs-microservice-architecture-for-software-delivery/)已经浪费了大量笔墨。然而，似乎每个人都能认同的一点是，微服务的复杂性。这种复杂性分为两个维度: 业务领域的固有复杂性和构建与运营分布式系统的技术复杂性。

正如[Martin Fowler](https://www.thoughtworks.com/en-us/profiles/leaders/martin-fowler)在他对DDD的介绍中[所说](https://martinfowler.com/bliki/DomainDrivenDesign.html)，关于软件系统复杂性的常见抱怨，“......这种复杂性的核心在于问题领域本身的本质复杂性。”

换句话说，自动化业务功能之所以复杂，是因为业务功能本身就复杂。这一点使用什么技术来实现这些功能都不会改变。

设计和实现复杂系统的挑战在过去的20年里并没有消失。如果有什么变化的话，由于分布式计算和网络集成的普及，以及继续使用云中的Web和移动应用破坏传统业务模型，这些挑战可能变得更加突出。

## DDD和EIP的作者谈论什么发生了变化

“DDD的状态肯定比20年前好很多，”Eric Evans说。

“我认为最大的变化是这段时间系统架构的巨大变化所带来的。现在我们通常可以在微服务中做出更小、更专业的模型。”他补充道。

此外，Hohpe指出，“构建分布式系统的许多基本挑战，比如异步、幂等性、最终一致性，仍然存在。”

然而，改变的是，现在构建的几乎所有的系统，尤其是构建在云平台之上的系统，都是分布式的，Hohpe说。

“EIP的介绍开始于‘有趣的应用程序很少孤立存在。’现在你可能可以删掉‘有趣的’——如今几乎没有应用程序是孤立存在的，”他补充道。

这20年来明显发生的一件事是，DDD已被采用为减少微服务设计复杂性的默认方法，EIP被采用为减少实现这些设计的复杂性的方法(特别是对于事件或Hohpe坚持称之为“消息”的东西)。

“架构中消息的无处不在使得用事件建模变得更自然，”Evans观察到。“需要定义消息的意义增加了系统中语言的可见性。从这些和其他方面看，当前的技术平台比20年前占主导地位的平台更好地支持DDD。这仍然非常困难！我认为它总会这样。但似乎偶然的复杂性有所减少，”他补充道。

与此同时，Woolf解释说，20年来变得更加容易的就是应用程序与HTTP和REST无处不在地集成。

“我们最初是为了排队的消息传递系统写的这本书，但是与非排队传输的集成变得更加复杂，”他补充道。

## 使用DDD和EIP的一些示例

举个例子，假设你要将单体应用重新设计为处理季节性工作负载的云原生微服务，就像我们在2013年为[Citi](https://thenewstack.io/citi-shows-continuous-secure-ingestion-for-software-packages/)的支付处理系统所做的那样。

首先，你会使用DDD的语言识别你的业务领域，确定这些领域的微服务，并确定它们的粒度和在哪里画接口边界。

然后，你会使用EIP设计它们之间的连接，考虑耦合和运营方面的问题，如延迟或高负载下的行为，并决定何时使用请求/响应何时使用[异步消息传递](https://thenewstack.io/api-management-for-asynchronous-apis/)。

去年的[HPTS](http://www.hpts.ws/agenda.html)会议上，特斯拉的软件工程师[Colin Breck](https://www.linkedin.com/in/colinbreck/)描述了他们对事件驱动微服务模式的实现。(他没有发布幻灯片，但提供了一个[相关视频](https://youtu.be/ggdYts4muu0？si=Ck3ziYd2AS0Foogg)的链接。)

在特斯拉的应用程序中，一些事件是由汽车遥测触发的，并通过消息传递到微服务中，这些微服务存储和检索它们以进行分析，例如为低电量事件生成的汽车找到最近的开放充电站。

在事件驱动模式的另一个示例中，沃尔玛用一个系统替换了基于RPC的库存查询系统，该系统在特定商品的可用库存发生变化时，会通过事件传播到一个可查询的公共数据存储。 正如[Randy Shoup](https://www.linkedin.com/in/randyshoup/)在同一场会议上描述的那样。

## DDD和EIP的下一步是什么？

到目前为止，两本书都不需要更新，尽管作者在他们的网站上添加了参考材料和更新了实现示例(对于DDD，请参阅[Domain Language](https://www.domainlanguage.com/ddd/)，对于EIP，请参阅[Gregor's Ramblings](https://www.enterpriseintegrationpatterns.com/ramblings.html)和[The Architect Elevator](https://architectelevator.com/blog/))。

然而，“我们建模领域的方式有一些重要变化。最明显的是，领域事件作为领域模型的一等公民成员。[函数式编程](https://thenewstack.io/excel-the-functional-programming-tool-you-didnt-know-you-had/)成为主流也有帮助，它放松了人们对模型的思考方式，”Evans说。

的确，人们对模型应该看起来像什么或应该关注什么有先入为主的看法。而Evans的书旨在提供原则的示例或实例，而不是事物本身，他说。

这样的预设观念可能会短路思考。

Hohpe同意DDD(以及在某种程度上EIP)的兴趣有所提升，但他对人们简单复述术语却没有任何额外洞见感到失望。

他说: “你最终会看到许多关于‘在构建EDA/微服务时，定义一个普适语言’的博客文章。”

“这并不错误，但有点像说‘要赢得比赛，你应该开快点’。冒着成为‘老气横秋的人’的风险，我希望人们能在这些概念的基础上建立并使其发展。幸运的是，我们也有很好的例子，如[Vlad Khononov的DDD书籍](https://www.amazon.com/Learning-Domain-Driven-Design-Aligning-Architecture/dp/1098100131)，或EIP图标被集成到开源产品和工具中。” Hohpe补充道。

除了关于慎重使用概念和原则的经验教训之外，在DDD和EIP模式的语境中追踪现代系统的演变也很重要。

“我认为像[Netflix OSS](https://netflixtechblog.com/netflix-oss-and-spring-boot-coming-full-circle-4855947713a0)和[Istio](https://thenewstack.io/istios-complexity-demystified/)这样的[服务网格](https://thenewstack.io/service-mesh/)在很大程度上欠缺企业集成哲学，即请求者期望的和提供者执行的可以非常不同。尽管如此，只要中介足够，它们仍然可以成功协作。” Woolf说。

此外，API已经成为一等编程工件，而当Woolf合著EIP时，面向服务的架构仍然是新事物，它对服务接口的关注还没有形成，他说。

然而，“现在，开发人员更少关注诸如请求-响应、命令和文档等单个模式，而更多关注具有API的服务，认为请求者将使用请求-响应调用每个服务任务。”他补充道。

## 给DDD和EIP读者的建议

要真正使领域建模付出回报，你必须思想开明，Evans说。当在一个项目中时，Evans指出他考虑上下文边界在哪里，但不考虑它们应该有哪些实体或值对象。 “我想: 我们正在做的最棘手、最令人困惑的部分是什么？这就是我们应该试图建模的部分。”他说。

“关键是找到领域中那个重要且令人痛苦的部分。得到具体示例，说明为什么它很困难。试验语言，直到你能清晰简洁地谈论这些例子。” Evans说。“这是我们语言的起点，也是我们模型的第一草图。这些模型可以与我书中的示例(和模式)完全不同。对我来说，这些是有趣的模型。”

Hohpe说，他相信如果你问任何开发人员事件是否是消息(EIP明确说明是)，你会听到长篇大论，混合了异步、消息代理和耦合，但没有给出任何明确的答案。

“[语义扩散](https://martinfowler.com/bliki/SemanticDiffusion.html)已经成为行业规范。我希望我们在谈论分布式系统时能更精确地使用语言。”他说。

同时，图表表示法已经赶上并成为普遍使用的记录集成解决方案的方式。但是图表不是解决方案；软件架构图是一种表征。

“在直接从EIP样式图跳到解决方案时，开发人员可能会忘记图所代表的模式的丰富性。” Woolf说。

## 总结

时代变了。单体扩展设计假设网络不可靠，你只能依赖同一服务器上的东西。现在网络比以往任何时候都更可靠、更快。云原生计算实践的假设包括通过复制和重复实现的冗余，这假设网络是参与其中的，与某些传统的单体系统不同。

微服务是云原生计算的主导架构方式，这种方式假定网络将(几乎总是)存在。

与此同时，[RESTful](https://thenewstack.io/how-to-integrate-restful-apis-into-ci-cd-pipelines/)和其他API(包括异步API)已经成为主导的实现风格。我要说得远一点，网络已经渗透到企业——它不再仅仅是在企业及其客户之间建立桥梁，而且在企业内部也是如此。

但在所有这一切发生的同时，业务领域的复杂性没有改变。如果有什么改变的话，由于数字化的增加，IT范围内的业务领域比以往任何时候都更广泛。

在设计到实现的过程中应对这种复杂性，DDD和EIP这两本开创性书籍中的原则和概念同样(如果不是更加)有用。

Eric Newcomer是Intellyx LLC的CTO兼首席分析师。他是《[Principles of Transaction Processing](https://www.amazon.com/Principles-Transaction-Processing-Kaufmann-Management/dp/1558606238)》（译者很自豪，竟然读过）的合著者，其第二版于2009年出版。


