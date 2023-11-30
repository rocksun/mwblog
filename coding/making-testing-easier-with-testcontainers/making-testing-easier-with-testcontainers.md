<!--
title:Testcontainers助您轻松测试
cover: https://cdn.thenewstack.io/media/2023/11/88425269-dall·e-2023-11-28-12.05.36-a-jar-that-looks-atomic-floating-in-space.-it-has-a-background-of-cosmic-stars.-the-jar-is-transparent-it-looks-like-space-inside-pixel-art.-the-bac.png
-->

AtomicJar公司代表了测试新潮流，该公司为开源库Testcontainers及其创始人兼首席执行官Sergei Egorov开发的开源测试工具提供支持。

> 译自 [Making Testing Easier with Testcontainers](https://thenewstack.io/making-testing-easier-with-testcontainers/)，作者 Alex Williams 是 The New Stack 的创始人和出版人。他是一位资深的技术记者，曾在 TechCrunch、SiliconAngle 和现在被称为 ReadWrite 的公司工作过。Alex 自 20 世纪 80 年代末以来一直是一名记者，开始在......
来自 Alex Williams 的更多内容

测试变得更加容易。如今，测试的重点在于频繁快速地进行。不断迭代以达到所期望的状态。并以DevOps应做的方式来实施——帮助开发者让工作流程持续运行。

[AtomicJar](https://www.atomicjar.com/) 公司反映了测试新时代的特征，为 [Testcontainers](https://testcontainers.com/) 提供工具和支持，后者是首席执行官兼联合创始人 [Sergei Egorov](https://www.linkedin.com/in/bsideup) 在 8 年前启动的开源库。

该开源框架抽象了 [Docker](https://www.docker.com/?utm_content=inline-mention) [API](https://thenewstack.io/docker-rolls-out-3-tools-to-speed-and-ease-development/)，提供了近似本地体验，使开发者能够在本地环境中测试依赖项。如 AtomicJar 的开发者倡导者 Oleg Selajev 最近在一篇报告中所说，开发者可以插入代码来创建“[几乎任何能放入容器中的](https://www.atomicjar.com/2023/09/state-of-local-development-and-testing-2023/)”实例。

通过这种方法，为开发者、运维团队和整个[平台工程](https://thenewstack.io/platform-engineering/)团队打开了几个机会。最基本而言，Testcontainers 抽象了使用[容器](https://thenewstack.io/containers/)的复杂性。配置被抽象化了。运维团队不必设置模拟环境；平台团队从使用和指标、治理以及与开发者对内循环开发的关注点的协同作用中获益。

“尽管我们在过去十年左右的时间里一直在 DevOps 的旅程中，但是当你与那些组织的平台团队交谈时，你经常会听到这样一种观点，即人们既需要控制，又需要所谓的 ‘自助’。”AtomicJar 的联合创始人 [Eli Aleyner](https://www.linkedin.com/in/elialeyner) 说。

"当我把这些联系起来时，我想 ‘为什么 Testcontainers 获得了如此多的采用？’ 我实际上觉得这正是那些趋势的原因，因为开发者能够在代码库中引入这个库，而无需任何人的许可，无需任何人批准或做任何事情，他们能够立即获得生产力和即时反馈，并能够在内部开发中更快地迭代。"

Testcontainers 模块预配置了，允许开发者在代码中而不是 YAML 中进行配置。尽管最初用于测试 [Java](https://thenewstack.io/java-adapts-to-cloud-native-computing/)，但现在开发者使用 Testcontainers 用于 C++、[Go](https://thenewstack.io/go-the-programming-language-of-the-cloud/)、[Python](https://thenewstack.io/an-introduction-to-python-a-language-for-the-ages/)、[Rust](https://thenewstack.io/rust-vs-go-why-theyre-better-together/) 和多种其他编程语言。

预配置的 Testcontainer 模块还支持[关系数据库](https://thenewstack.io/the-case-for-boring-tech-relational-databases-in-the-cloud/)、[NoSQL 数据库](https://thenewstack.io/why-choose-a-nosql-database-there-are-many-great-reasons/)、消息代理、云服务、Web 和其他环境。

对于开发者而言，好处在于反馈循环，它允许他们在本地环境中针对依赖项进行测试，允许并行的工作环境，并让开发者进入流程。它解决了开发者多年来一直在努力解决的一个问题：等待与共享的开发者环境集成，开发者做出的更改常常发生冲突。

“测试团队不再存在，测试从开发者那里开始，只是扩展了他们可以做什么。” Egorov 说。

## 代码高于 YAML

Testcontainers 库针对的是 Docker API。Testcontainers 使用域特定语言(DSL)，而不是 YAML。在 Testcontainers 的上下文中，该库为开发者提供了用于配置和管理容器的自定义语言或 API。DSL 内嵌在编程语言中。

对于开发者而言，使用 DSL 可以使一切保持程序化。这种方法抽象了大量复杂性。例如，开发者编写新的 MySQLContainer()，而不必指定实现，如 Docker 镜像、端口、卷等。

测试和应用程序代码可以让开发者全神贯注。Docker 的复杂性不需要考虑。定义和运行容器在代码中变得自然。它不再感觉像是一个编排问题。

例如，当平台迁移到云服务时，运维团队通常需要预配共享环境。Testcontainers 允许开发者在本地仿真环境，而无需访问该服务。开发者可以立即开始工作，无需等待运维团队设置共享环境。

DevOps 的梦想是什么?它是内外循环的协同和和谐。长期以来，运维团队做了所有设置和模拟，而开发团队则等待。AtomicJar 的测试，无意双关，将是它作为工具提供商执行的好坏。它面临着 [IBM](https://www.ibm.com/?utm_content=inline-mention)、Parasoft 和 SmartBear 等同行的激烈竞争。
