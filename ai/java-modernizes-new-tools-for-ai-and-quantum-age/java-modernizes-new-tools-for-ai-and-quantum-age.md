
<!--
title: Java的现代化：AI和量子时代的新工具
cover: https://cdn.thenewstack.io/media/2025/03/4e2bc7b7-mike-kenneally-zlwdjoktua8-unsplash-1.jpg
summary: Java 24重磅发布！🚀解锁AI和后量子密码新纪元！🔥 JEP 489加速AI推理，Vector API性能飙升！🛡️ JEP 496/497硬核抗量子，安全升级！💪 Stream Gatherers、Scoped Values、Structured Concurrency等新特性加持，云原生应用更上一层楼！
-->

Java 24重磅发布！🚀解锁AI和后量子密码新纪元！🔥 JEP 489加速AI推理，Vector API性能飙升！🛡️ JEP 496/497硬核抗量子，安全升级！💪 Stream Gatherers、Scoped Values、Structured Concurrency等新特性加持，云原生应用更上一层楼！

> 译自：[Java Modernizes: New Tools for AI and Quantum Age](https://thenewstack.io/java-modernizes-new-tools-for-ai-and-quantum-age/)
> 
> 作者：Chris J Preimesberger

自从 Sun Microsystems 在 2006 年[开源](https://thenewstack.io/open-source/) [Java](https://thenewstack.io/introduction-to-java-programming-language/) 以来，创新源源不断地从其忠诚且富有创造力的开发社区涌现。目前的 Java 公司管理者 [Oracle](https://developer.oracle.com/?utm_content=inline+mention) 通过发布 [Java 24](https://thenewstack.io/oracle-ships-java-24-ai-is-so-yesterday-says-vp/) (Oracle JDK 24)，延续了其在 2010 年收购 Sun 时继承的传统，该版本于本月早些时候在 [JavaOne 2025](https://www.oracle.com/javaone/) 上发布。

这个被广泛使用的编程语言和开发平台的最新迭代版本包含了旨在提高开发者生产力和改进企业级应用程序功能的重大进步。JDK 24 包括一个涵盖语言特性、库、安全性、工具和性能的升级——几乎涵盖了平台中所有重要的内容。

根据 [IDC 分析师 Arnal Dayaratna](https://www.linkedin.com/in/cloudcomputingtoday/) 的说法，Java 通过满足开发者的需求，特别是在 AI 驱动的应用程序领域，不断发展并保持其价值。[Georges Saab](https://www.linkedin.com/in/georgessaab/) 是 Oracle 的高级副总裁，他提到了 Java 24 的包容性，其中包括 20 多个新功能，包括 AI 和后量子密码支持。此版本加强了 Oracle 对可预测的六个月发布节奏的承诺。

下面列出了几个与量子相关的项目。最重要的与 AI 相关的升级是 JEP 489 (Vector API)，它加速了向量计算——这对于 AI 推理和计算密集型任务至关重要。毫无疑问，AI 开发者将大量使用它。

以下是根据 Oracle 规范，JDK24 改进的详细信息：

## 加强安全性

Java 24 优先考虑安全性，特别是在面对新兴的量子计算威胁时。

- **JEP 478**(Key Derivation Function API) 提高了传输中数据的密码安全性。
- **JEP 496**(Quantum-Resistant Module-Lattice-Based Key Encapsulation Mechanism) 和**JEP 497**(Quantum-Resistant Module-Lattice-Based Digital Signature Algorithm) 提供了抗量子机制的实现，这是朝着后量子密码支持迈出的重要一步。这些功能解决了后量子世界中安全通信和数据身份验证的需求。

## 语言更新

旨在简化开发和提高代码可靠性的关键语言特性是。

- **JEP 488**(Primitive Types in Patterns, instanceof, and switch) 通过将模式匹配扩展到原始类型，提供了更大的统一性和表达性，从而使 AI 推理应用程序受益。
- **JEP 492**(Flexible Constructor Bodies) 通过在构造函数主体中引入不同的序言和后记阶段，简化了逻辑放置，从而增强了代码可靠性。
- **JEP 494**(Module Import Declarations) 简化了模块化库的重用，特别是对于初学者和集成 AI 逻辑的开发人员而言。
- **JEP 495**(Simple Source Files and Instance Main Methods) 为新程序员提供了平滑的学习曲线，并允许经验丰富的开发人员编写简洁的小程序。

## 库添加

几个重要的库改进。

- **JEP 485**(Stream Gatherers) 增强了 Stream API，允许自定义中间操作和更有效的数据转换。
- **JEP 484**(Class-File API) 提供了一个用于解析、生成和转换 Java 类文件的标准 API。
- **JEP 487**(Scoped Values) 改进了跨线程的不可变数据共享，从而提高了性能和鲁棒性。
- **JEP 489**(Vector API) 加速了向量计算，这对于 AI 推理和计算密集型任务至关重要。
- **JEP 499**(Structured Concurrency) 简化了多线程编程，从而提高了可维护性和可靠性。

## 工具、性能优化

- **JEP 493 (Linking Run-Time Images without JMODs)** 实现了在没有 JMOD 文件的情况下创建自定义运行时镜像，从而减小了 JDK 的大小。
- **JEP 450 (Compact Object Headers)** 减小了 HotSpot JVM 中的对象头大小，从而提高了堆大小和性能。
- **JEP 475 (Late Barrier Extension for G1)** 优化了 G1 垃圾收集器，从而提高了效率和代码质量。
- **JEP 483 (Ahead-of-Time Class Loading and Linking)** 提高了应用程序的启动时间。
- **JEP 490 (ZGC: Remove the Non-Generational Mode)** 简化了 ZGC 的维护。
- **JEP 491 (Synchronize Virtual Threads without Pinning)** 增强了虚拟线程的可伸缩性。
- **JEP 404 (Generational Shenandoah)** 引入了实验性的分代收集功能。
- **JEP 479 (Remove the Windows 32-bit x86 Port)** 和 **JEP 501 (Deprecate the 32-bit x86 Port for Removal)** 精简了 JDK 的构建和测试基础设施。

## 移除某些特性以保证安全性

OpenJDK 社区还强调移除其认为不安全的功能，包括 JEP 472、JEP 486 和 JEP 498，以维护 Java 的完整性并符合最佳实践。JEP 472、486 和 498 是增强默认 [Java 平台完整性](https://inside.java/2025/01/03/evolving-default-integrity/) 的更广泛工作的一部分，重点是限制潜在的不安全特性和实践。

以下是这些 JEP 被认为不安全的原因：

**JEP 472: Prepare to Restrict the Use of JNI**：JNI (Java Native Interface) 允许 [Java 代码](https://thenewstack.io/trash-pandas-love-enterprise-java-code/) 与本地 (C/C++) 代码交互，这可能会引入安全风险和可移植性问题。安全管理器是一种限制远程加载代码（如小程序）权限的机制，但随着小程序的衰落，它变得越来越不相关。

**JEP 486: Permanently Disable the Security Manager**：JEP 486 永久禁用了安全管理器，从而移除了一个导致摩擦和复杂性的功能。此举简化了平台，并降低了与遗留安全机制相关的潜在安全漏洞。

**JEP 498: Warn upon Use of Memory-Access Methods in sun.misc.Unsafe**：JEP 498 在使用不安全方法时发出警告，这些方法已被弃用，并将在未来的版本中移除。这使开发人员为最终移除这些不安全的 API 做好准备，并鼓励他们使用更安全的替代方案。

## 云集成和社区支持

正如人们所期望的那样，Oracle 声称 Java 24 在 Oracle 云基础设施 (OCI) 上运行时提供了更高的性能和成本节省，因为它们是共同设计的。该公司表示，Oracle Java Universal SE Subscription 提供了新的支持，包括 Java SE Subscription Enterprise Performance Pack 和对 [GraalVM](https://thenewstack.io/how-to-build-with-graalvm-inside-github-actions/) 的访问。

在 JavaOne 大会上，行业专家对 JDK 24 进行了评价。[Frank Greco of Crossroads Technologies](https://www.linkedin.com/in/frankdgreco/) 强调了 Vector API 对 AI 应用程序的增强，而 [Richard Fichtner of XDEV Software](https://www.linkedin.com/in/richardfichtner/) 赞赏 Stream Gatherers 用于高效的数据转换。[Dr. Venkat Subramaniam of Agile Developer, Inc.](https://www.linkedin.com/in/vsubramaniam/) 称赞了 Stream Gatherers、Scoped Values 和 Structured Concurrency。[CodeRanch moderator Jeanne Boyarsky](https://www.linkedin.com/in/jeanne-boyarsky/) 指出了灵活构造函数的好处以及 Stream Gatherers 的潜力。[JetBrains’ Marit van Dijk](https://www.linkedin.com/in/maritvandijk/) 强调了她的公司致力于在 IntelliJ IDEA 中为 Java 24 提供首日支持。