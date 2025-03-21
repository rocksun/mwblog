
<!--
title: Oracle发布Java 24：副总裁表示“人工智能已是昨日黄花”
cover: https://cdn.thenewstack.io/media/2025/03/71dfe572-getty-images-jpx9yr5rggw-unsplash-1.jpg
summary: Oracle发布Java 24！力推24个JEP，专注AI集成、后量子密码(PQC)和性能优化。新特性包括Stream Gatherers API、Class-File API和Vector API改进，助力AI推理。更有密钥派生函数API应对量子计算威胁。副总裁更是语出惊人：“AI已是昨日黄花！”
-->

Oracle发布Java 24！力推24个JEP，专注AI集成、后量子密码(PQC)和性能优化。新特性包括Stream Gatherers API、Class-File API和Vector API改进，助力AI推理。更有密钥派生函数API应对量子计算威胁。副总裁更是语出惊人：“AI已是昨日黄花！”

> 译自：[Oracle Ships Java 24: 'AI Is So Yesterday' Says VP](https://thenewstack.io/oracle-ships-java-24-ai-is-so-yesterday-says-vp/)
> 
> 作者：Darryl K Taft

[Oracle](https://developer.oracle.com/?utm_content=inline+mention) 发布了 [Java](https://thenewstack.io/introduction-to-java-programming-language/) 24，其中包含 24 个 [JDK 增强提案 (JEP)](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/)，旨在帮助开发人员提高生产力并增强 [Java 语言](https://thenewstack.io/language-wars-2024-python-leads-java-maintains-rust-rises/)。 此版本的发布正值 Java 接近今年晚些时候的 30 周年纪念日。

在与 Oracle Java 团队成员的简报中，该小组谈到了 Java 24 的众多增强功能，包括对 AI 集成、后量子密码学和性能优化的更好支持。

[Java 24](https://openjdk.org/projects/jdk/24/) 的故事于 3 月 18 日在 [JavaOne conference](https://www.oracle.com/javaone/) 上发布，代表了该编程语言迈向 30 年历程中的重要篇章。 凭借 24 个 JEP 和 3,500 多个较小的改进，此最新版本带来了语言特性、库和性能增强方面的创新。

Oracle Java 平台高级副总裁兼 [OpenJDK](https://thenewstack.io/the-hidden-risks-of-unsupported-openjdk-in-financial-systems/) 管理委员会主席 [Georges Saab](https://www.linkedin.com/in/georgessaab/) 告诉 The New Stack：“这些数字非常强劲，人们对 Java 的热情比以往任何时候都高涨……没有人会预料到，当我们接近 30 周年纪念日时，我们会走上这条道路。”

## 最喜欢的 JEP

正如我们对当前 Java 主要版本六个月的发布节奏所期望的那样，Java 24 在稳步推进语言发展方面做得非常出色，巩固了过去几个发布周期中一直在后台“酝酿”的几项增强功能，The Futurum Group 副总裁兼实践主管 [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/) 说。

“虽然有很多有趣的 JEP 可供选择，但我认为最有趣的 JEP 之一是 JEP 483：提前类加载和链接，”他告诉 The New Stack。“我喜欢这一点，因为它不断使我们更接近 Java 启动时间的本机代码速度。 我们看到在整个技术领域，人们都在关注优化性能，以便以更低的成本实现更大的规模……这是有充分理由的。

“[Jensen Huang](https://www.linkedin.com/in/jenhsunhuang/)（英伟达 CEO）刚才在他的 [GTC](https://www.nvidia.com/gtc/) 主题演讲中说，未来每个数据中心都将受到能源的限制。 如果你想知道你作为一家公司能赚多少钱，你只需要看看你的数据中心有多少能源可用。”

**JEP 483**：提前类加载和链接：Oracle 在一份声明中表示，通过使应用程序的类在 HotSpot Java 虚拟机启动时立即以加载和链接状态可用，帮助开发人员提高生产力并缩短启动时间。 此功能不需要使用 jlink 或 jpackage 工具，也不需要更改从命令行启动应用程序的方式，也不需要更改应用程序、库或框架的代码。 因此，它有助于为持续改进启动和预热时间奠定基础。

## 新的语言和库特性

同时，新的语言特性包括模式中的原始类型、灵活的构造函数体、模块导入声明和面向初学者的简单源文件。

例如，[JEP 488](https://openjdk.org/jeps/488)：**模式、instanceof 和 switch 中的原始类型**，处于其第二个预览版本中。 此 JEP 通过使语言更加统一和富有表现力，帮助开发人员提高 Java 编程效率。 此功能通过消除开发人员在使用模式匹配、instanceof 和 switch 时遇到的与原始类型相关的限制，帮助开发人员增强模式匹配。 它还允许所有模式上下文中的原始类型模式，扩展 instanceof，并使 switch 适用于所有原始类型。 Oracle 在一份声明中表示，集成 AI 推理的应用程序的开发人员将特别受益于对原始类型的支持。

同时，新的 Java 库特性包括 Stream Gatherers API、Class-File API 和 Vector API 改进，这些改进有利于 AI 推理。

**JEP 485**: Stream Gatherers（Stream 收集器），通过增强 Stream API 以支持自定义中间操作，帮助开发人员更高效地读取、编写和维护 Java 代码。这些自定义中间操作允许流管道以现有内置中间操作难以实现的方式转换数据。

XDEV Software GmbH 的 CEO [Richard Fichtner](https://www.linkedin.com/in/richardfichtner/?locale=de_DE) 在一份声明中表示：“Java 24 引入了 Stream Gatherers，这是一个强大的增强功能，使开发人员能够精细地控制流中元素的组合和处理方式。这使得复杂的数据转换更具表现力和效率。我喜欢这个功能，因为它消除了自定义收集器或 flatMap 体操等变通方法，从而可以实现更具可读性和可维护性的流管道。”

## “人工智能已是昨日黄花”

虽然最近人工智能主导了科技讨论，但 Java 的架构师已经在展望未来。Oracle 产品管理副总裁 [Donald Smith](https://www.linkedin.com/in/donaldojdk/) 在一次采访中打趣道：“人工智能已是昨日黄花。让我们来谈谈[后量子密码 (PQC)](https://thenewstack.io/nist-secures-encryption-for-a-time-after-classical-computing/)。这才是新的热门话题。”

这种前瞻性的方法已成为 Java 的标志，工程师们已经在实施抗量子密码算法，为传统方法过时的未来做好准备。

Smith 说，首席信息官和安全官们越来越关注“当传统密码方案被弃用成为强制性要求时，我们是否可以依靠 Java 来提供解决方案”。Oracle 的回应借鉴了以往的经验：他们成功地完成了 TLS 1.3 的类似过渡，并将这些经验应用于后量子安全。

## PQC 和更多安全

实际上，**JEP 478**: Key Derivation Function API（密钥派生函数 API）是一个新的预览功能，通过为传输中的数据提供密码安全，帮助开发人员为新兴的量子计算环境做好准备。这提高了机密性和通信完整性。

Oracle Java 平台（语言、JVM、库、安全/漏洞、UI、嵌入式）软件开发副总裁 [Bernard Traversat](https://www.linkedin.com/in/btratra/) 告诉 The New Stack：“在 JEP 478 中，我们引入了一个新的 API 来处理密码算法中的派生函数。所以基本上，目标是让您了解基于 HMAC [Hash-based Message Authentication Code]（基于哈希的消息认证码）的校准函数。这种标准正在出现，PQC 领域的人们现在正在寻找协议实现的底层机制，这些协议是 IETF [Internet Engineering Task Force]（互联网工程任务组）目前正在制定的初始密码协议集。”

此外，从业务角度来看，Smith 指出，在过去三四年中，密码学的实现方式涉及私钥的生成。

他说：“这个 JEP 所做的是允许您生成抗量子密钥或量子抗性算法所需的密钥。因此，这通常意味着更大、更难猜测和关联的密钥……正如 Bernard 提到的，不同的标准机构和国际组织正在讨论这些内容。这是我们对它的实现。”

除了密钥派生函数 API 中的新抗量子密码功能外，其他安全增强功能还包括基于模块格的密钥封装机制和数字签名算法。

## 正值 30 岁

IDC 软件开发研究副总裁 [Arnal Dayaratna](https://www.idc.com/getdoc.jsp?containerId=PRF004946) 在一份声明中表示：“随着 Java 今年晚些时候即将迎来 30 周年，它将继续扩展其工具集，以满足开发人员不断变化的需求，包括支持开发人工智能驱动的应用程序的功能。新版本中的各种功能将有助于提高开发人员的生产力，使他们能够更快、更高效地向其组织和客户交付功能丰富的应用程序。Java 24 版本的发布强调了 Java 在大规模开发企业级、任务关键型应用程序方面是无与伦比的。”

Constellation Research 的分析师 [Holger Mueller](https://www.linkedin.com/in/holgermueller/) 表示，Java 正在迎来 30 岁，就像许多真正的 30 岁的人一样，它不再像 20 岁那样喧闹，但也不是“年长的”政治家。
“就像一位三十岁的人一样，它精通各种技术——包括新增的语言特性、新的库、工具、运行时更新和源代码动画，” 他告诉 The New Stack。“但它并不沉闷，因为它加入了人工智能向量，并且对后量子抗性 lattice 的添加负责。Java 将在它的三十多岁及以后通过这次更新保持活跃。”