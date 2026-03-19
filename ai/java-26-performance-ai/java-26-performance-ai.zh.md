[Oracle](https://www.oracle.com/developer?utm_content=inline+mention) 于周二发布了 Java 26，这是其在加利福尼亚州红木海岸举行的 [JavaOne 2026](https://www.oracle.com/javaone/) 大会开幕当天发布的。此次发布延续了该平台六个月的发布周期，带来了一系列渐进但意义重大的改进，涵盖了性能、安全性和语言表达能力。

此版本带来了 10 个 JDK 增强提案 (JEP)，涉及从 HTTP/3 网络支持到垃圾收集效率、密码工具以及对 Applet API 的逾期清理等诸多方面。Java 26 不是一个长期支持 (LTS) 版本；JDK 25 拥有该称号。这意味着采取保守升级周期的企业团队将很大程度上不会采用此版本，但 Java 平台提供商 [Azul](https://thenewstack.io/azul-cto-java-at-30-still-rules-enterprise-dev/) 的副 CTO Simon Ritter 表示，追求前沿技术的开发人员仍有大量内容值得研究。

RedMonk 的首席分析师 Stephen O’Grady 告诉 *The New Stack*，此版本旨在让 Java 保持更新。

O’Grady 说：“有一些开发者体验和加密方面的改进，但对我来说，最大的亮点是面向性能的增强——一个改进了垃圾收集，另一个是惰性常量，这对于 AI 使用和工作负载特别相关。” “总的来说，这是另一个致力于全面推进、使 Java 保持最新和相关性的版本。”

Oracle 从企业角度阐述了此次发布。IDC 软件开发研究副总裁 Arnal Dayaratna 在一份声明中表示：“30 多年来，组织一直依赖 Java 平台和语言来为其关键任务系统提供动力，并支持应用程序和服务的快速开发。” “通过利用先进的 AI 和安全功能等新特性和服务扩展 Java 的功能，Java 26 为组织提供了更快的创新路径。”

> “对我来说，最大的亮点是面向性能的增强——一个改进了垃圾收集，另一个是惰性常量，这对于 AI 使用和工作负载特别相关……它旨在全面推进、使 Java 保持最新和相关性。”

与此同时，Oracle Java 平台高级副总裁兼 OpenJDK 管理委员会主席 Georges Saab 将此版本与 AI 时代联系起来。Saab 在一份声明中表示：“Java 26 中的新功能反映了 Oracle 致力于帮助客户利用 AI 和密码学构建加速业务增长的承诺。”

## 性能成为焦点

有两个 JEP 表明 Java 26 作为一个平台值得开发者关注，即使它不是一个 LTS 版本。

[JEP 522](https://openjdk.org/jeps/522) 针对 G1 垃圾收集器，减少了应用程序线程和 GC 线程之间的同步开销。实际结果是，在相同硬件下吞吐量更高，应用程序运行更快，服务更多用户，并降低基础设施成本，而无需架构更改。Ritter 表示，对于运行高并发工作负载的团队来说，这是下一次 JDK 升级时一次有意义的免费升级。

[JEP 516](https://openjdk.org/jeps/516) 是 [Project Leyden](https://openjdk.org/projects/leyden/) 的一项功能，它扩展了预先对象缓存，使其可与任何垃圾收集器（包括低延迟 ZGC）配合使用。该 JEP 在 JDK 25 中引入，但 GC 兼容性有限；Java 26 弥补了这一缺陷。它允许 HotSpot JVM 在启动时从与 GC 无关的格式加载缓存的预初始化 Java 对象，从而缩短了启动延迟和预热时间。

Ritter 在与 *The New Stack* 的发布前技术简报中指出：“他们发现他们有这个想法，但它不适用于所有垃圾收集器。所以，他们现在已经修复了这个问题，使其可以与 ZGC 配合使用。” 对于冷启动性能直接影响成本和用户体验的云原生应用程序来说，这很重要。

[JEP 526](https://openjdk.org/jeps/526)，惰性常量，在其第二个预览版中，完善了性能方面的表现。该功能——此前名为 Stable Values，后更名——为持有不可修改数据（仅在需要时初始化一次而非在类加载时初始化）的对象提供了新的 API。一旦设置，JVM 会将惰性常量视为真正的常量，从而实现与 final 字段相同的性能特性，同时赋予开发人员对初始化时机的控制权。

Ritter 解释说：“拥有惰性常量而非仅仅是 final 字段的原因是，使用惰性常量，你可以更好地控制值的设置时机。” “这是一件好事，它让开发者能够更好地控制如何使用它并提高效率。” 这种灵活性对于 AI 和数据驱动的应用程序特别有用，这些应用程序需要加载大型模型或配置数据而无需承担前期成本——O’Grady 在他的评估中也强调了这一点。

## 语言和库的内务管理

[JEP 530](https://openjdk.org/jeps/530)，模式、instanceof 和 switch 中的原始类型，迎来了它的第四个预览版。该 JEP 解决了原始类型与 Java 模式匹配特性交互时出现的摩擦——即行为与开发者预期不符的边缘情况。它收紧了 switch 构造中的主导性检查，允许编译器在编译时而非运行时捕获更广泛的错误。Oracle 表示，这项工作通过使 Java 更加统一和富有表现力，有助于简化集成 [AI 推理](https://thenewstack.io/scaling-ai-inference-at-the-edge-with-distributed-postgresql/)的应用程序的开发。Oracle Java 开发者关系副总裁 Chad Arimura 告诉 The New Stack，这项工作虽然不如头条功能那么令人兴奋，但对于认真使用模式匹配的开发者来说很重要。

[JEP 525](https://openjdk.org/jeps/525) 在 [Project Loom](https://www.baeldung.com/openjdk-project-loom) 下将其结构化并发带到了第六个预览版。该 API 将跨线程运行的相关任务组视为一个单一的工作单元，简化了取消和关闭处理，并降低了线程泄漏的风险。Ritter 将这种方法描述为借鉴了 try-with-resources 块的结构。

他告诉 *The New Stack*：“你可以有一个 try 语句，可以在其中包含一组任务，然后当你到达 try 块的底部时，你知道所有任务要么已正常完成，要么你有能力终止一些内部正在使用的线程——这比我们目前做事的方式效率高得多。” 它与 AI 和云原生工作负载（多线程协调普遍存在）的相关性并非偶然。

[JEP 517](https://openjdk.org/jeps/517) 为 HTTP Client API 增加了 HTTP/3 支持。HTTP/3 使用 QUIC 协议而非 TCP 的传统传输方式，这需要在其之上重新构建可靠性——但为 [微服务](https://thenewstack.io/introduction-to-microservices/) 和 API 驱动的应用程序提供了更低的延迟和更好的性能。

Ritter 在简报中提到了这种架构策略：“HTTP/3 使用 UDP 作为传输协议而非 TCP，而 UDP 是一个不可靠的传输协议，所以他们实际上必须在其之上构建一个层来有效地赋予它 TCP 的功能——但我猜它 somehow 工作得更快。” 他说，对于构建网络服务的 Java 开发者来说，以最少的代码更改与 HTTP/3 服务器交互的能力是一个实际的胜利。

## 安全与清理

[JEP 524](https://openjdk.org/jeps/524) 在其第二个预览版中为加密对象添加了 PEM 编码 API，简化了开发人员在企业和云部署中处理 [加密密钥](https://thenewstack.io/akeyless-wants-you-to-throw-away-the-encryption-key/)、证书和证书吊销列表的方式。该 API 简化了合规性工作，并提高了安全格式之间的可移植性，这对于任何处理加密数据监管要求的团队都非常有用。Oracle 表示，这一更改减少了错误风险，并增强了安全 Java 应用程序的互操作性。

除了 JEP 之外，Java 26 还引入了混合公钥加密支持、用于供应链安全的后量子时代 JAR 签名，以及对 Unicode 17.0 和 CLDR v48 的更新。其他更新包括更快的 JVM 启动、扩展的 C2 JIT 编译、更智能的堆管理以及 JavaDoc 的新深色模式。

[JEP 500](https://openjdk.org/jeps/500)，准备让 Final 真正最终化，开始针对一个长期存在的不一致性强制执行 Java 的默认完整性原则：final 字段可以通过深度反射进行修改，这迫使 JVM 在不变性方面采取保守态度并限制了优化。

Ritter 解释了其中的利害关系。

他说：“这在性能方面产生了一些影响，因为这意味着 JVM 必须接受 final 字段仍然可能通过深度反射进行更改。” “他们想要做的是阻止这种情况——从逻辑上讲，一个 final 字段确实是一个 final 字段——这将允许 JVM 更好地利用堆和内存中对象和值的布局，从而提高效率。” 该 JEP 现在会发出警告，为未来的强制执行步骤做准备，以实现这些堆布局的收益。

并且 [JEP 504](https://openjdk.org/jeps/504) 最终移除了 Applet API，该 API 自 JDK 17 以来已被弃用并计划移除。

Ritter 直言：“Applet 确实是过时的技术。” “已经没有浏览器为它们提供安全补丁并仍然支持 Applet 所需的功能了。所以，他们终于废除了这些。” 他补充说，移除 Applet 减少了平台的占用空间，并消除了一个既带来性能又带来安全隐患的区域。

## JEP 之外

除了此次发布之外，Oracle 还宣布了 [Java 验证产品组合](https://www.oracle.com/java/technologies/downloads/jvp/) (JVP)，这是一个由 Oracle 支持的生态系统组件精选包——包括对 [JavaFX](https://openjfx.io/) 和 [Helidon 微服务框架](https://helidon.io/) 的商业支持——以统一的许可和支持条款打包。Helidon AI 扩展了 Helidon，使 Java 开发者能够构建高性能 AI 应用程序。Helidon 还集成了 LangChain4j 和 Helidon MCP，并促进了将 AI 代理构建为微服务。JVP 还包括 Oracle 对 Oracle 用于 [Visual Studio Code](https://thenewstack.io/vs-code-ai-copilot/) 的 Java 平台扩展的支持。

> “公司里大多数人真正想做的是将现有模型集成到他们现有的应用程序中，或者构建代理……我们相信 Java 平台是 AI 开发的绝佳语言和平台。生态系统正在真正发展起来——所有这些东西都已用 Java 构建。”

Oracle 还在 JavaOne 大会上公布了 [Project Detroit](https://openjdk.org/projects/detroit/)，这是一个 OpenJDK 倡议，旨在使 Java 能够在 JVM 内部调用 [JavaScript](https://thenewstack.io/introduction-to-javascript/) 和 [Python](https://thenewstack.io/what-is-python/) 运行时——这是一个直接的尝试，旨在让企业 Java 开发者无需离开 JVM 或启动单独的进程，即可利用 Python 的 AI 库生态系统。

在简报中，Oracle 的团队坦诚地谈论了 Java 正在追逐的 AI 机遇。

Arimura 告诉 *The New Stack*：“公司里大多数人真正想做的是将现有模型集成到他们现有的应用程序中，或者构建代理。我们相信 Java 平台是 AI 开发的绝佳语言和平台。生态系统正在真正发展起来——所有这些东西都已用 Java 构建。他们不想重新学习其他领域。”

Oracle Cloud Infrastructure (OCI) 已成为首个支持 Oracle JDK 26 的云提供商，OCI 客户可免费获得此版本。