## Java 22：让 Java 更适合 AI 应用/工作负载

![Java 22 的特色图片：让 Java 更适合 AI 应用/工作负载](https://cdn.thenewstack.io/media/2024/03/d5240aff-java-horz-clr-1-1024x672-copy.png)

[Oracle](https://developer.oracle.com/?utm_content=inline-mention) 已发布 [Java 22](https://www.oracle.com/java/)，这是流行的通用编程语言和开发平台的最新版本。

Java 22（Oracle JDK 22）提供了数千项性能、稳定性和安全性改进，包括 12 项新的 JDK 增强提案 (JEP)，这些提案增强了 Java 语言、API、性能和 [Java 开发工具包 (JDK)](https://thenewstack.io/oracle-sets-foundation-for-the-languages-future-in-java-19/) 中包含的开发工具。

### Java 和 AI

此外，新版本中还包含了语言特性，这些特性让开发者能够更好地使用 Java 来构建 AI 应用程序。

[Azul](https://www.azul.com/) 的副首席技术官 [Simon Ritter](https://www.linkedin.com/in/siritter/?originalSubdomain=uk) 告诉 The New Stack：“JDK 22 将让企业更容易部署 AI。一项已经开发完成并已最终确定的功能是 [Foreign Function and Memory API](https://docs.oracle.com/en/java/javase/20/core/foreign-function-and-memory-api.html#GUID-FBE990DA-C356-46E8-9109-C75567849BA8)。”“这是更大的 [OpenJDK](https://thenewstack.io/your-guide-to-navigating-openjdk-in-2023/) [项目 Panama](https://openjdk.org/projects/panama/) 的一部分。由于这允许 Java 代码更轻松地与非 Java 库进行交互，因此非常适合开发和部署 AI/ML 应用程序，这些应用程序通常会使用非 Java 库。”

Oracle Java 平台高级副总裁兼 OpenJDK 管理委员会主席 [Georges Saab](https://www.linkedin.com/in/georgessaab/) 告诉 The New Stack，Java 作为一种编程语言持续发展，因为它不断演变以适应人们当今在软件中解决的最感兴趣的特定用例。

他说：“我们希望确保他们想到 Java 时自然而然。”但是，“如果我向你提到 AI，你可能会说，[Python](https://thenewstack.io/what-is-python/)。好的，很棒。你为什么说 Python？那么，我们可以从中吸取什么教训？嗯，你知道 Python 做得很好的一点是，它实际上为执行 AI 工作负载的大部分繁重任务的本机库提供了胶合代码。好的，很棒。那么，你为什么不会自动想到那里的 Java 呢？嗯，可能是因为 Python 早期做了很多工作，让本机代码和 Python 的接口变得更容易。因此，几年前，我们意识到了这一点，并开始着手 Panama，它在 JDK 22 中通过 Foreign Function and Memory API 确定下来。我们希望让本机和 Java 之间的接口更容易用于 AI 等用例。”

为此，Oracle 必须想办法让 Java Native Interface (JNI) 的新版本更易于使用。Saab 说：“Python 被视为非常适合 AI，因为有所有这些执行繁重任务的本机库。”“为什么是那些本机库？为什么不在 Java 中？嗯，它们不在 Java 中…？”

### Oracle 正在努力解决这个问题

Oracle 一直在不同的项目中处理这个问题，时间长短不一。其中许多项目已经交付或已经交付，或者准备交付到 Java 的六个月版本中。

Saab 告诉 The New Stack：“虽然它们没有专门关注 AI，但它们关注的是用例类型、编程范例类型和即将到来的硬件功能，以便这些努力中的每一个，虽然专注于特定领域，但整体上使 Java 更适合现代编程和人们想要做的事情。”

此外，由于 Project Amber 的目标之一是本机代码和内存互操作性，因此 Oracle 的 [Project Babylon](https://inside.java/tag/babylon) 专注于外来编程模型互操作性，并让开发者更容易使用 GPU。

[项目描述](https://openjdk.org/projects/babylon/) 中说：“Babylon 的主要目标是将 Java 的范围扩展到外来编程模型，例如 SQL、可微编程、机器学习模型和 GPU。Babylon 将通过对 Java 中的反射编程（称为代码反射）的增强来实现这一目标。”

[图形处理单元 (GPU)](https://thenewstack.io/free-gpus-and-ai-chips-are-available-to-run-ai/) 已成为人工智能处理的基础。从本质上讲，它们将 AI 的语言传达给硬件。例如，[Nvidia](https://thenewstack.io/nvidia-gpu-dominance-at-a-crossroads/) 本周正在举办其 [年度 GTC 大会](https://thenewstack.io/nvidia-gtc-hyperscaler-happiness-and-enterprise-indigestion/)，它正在大肆销售 GPU 以加速 AI 创新。
**Java 22：持续创新，赋能开发人员**

**跨越用例的复杂性**

“经过近三十年的发展，Java 能够支持跨越广泛用例的复杂开发任务，这使得该平台与以往一样具有相关性，”IDC 软件开发研究副总裁 [Arnal Dayaratna](https://www.linkedin.com/in/cloudcomputingtoday/) 在一份声明中表示。“Java 的多功能性和全面的工具集使其能够支持大规模开发生产级、任务关键型应用程序，这使其成为生成式 AI 等创新用例的关键使能技术。”

**更广阔的视角**

Omdia 分析师 Brad Shimmin 表示，从更广阔的角度来看会更好。

“如果你稍微后退一步，整体来看这些更新，很明显可以看出该公司热衷于确保 Java 的长期价值，Java 即将在如此多的不同公司中迎来其第 30 个生产年，”他说。“这种关注体现在增强功能中，例如引入外函数和内存 API（在 Project Loom 中），这使 Java 能够以更高效和更安全的方式访问外部应用程序和数据。在此，通过不要求开发人员在不调用平台的本机接口来运行该代码的情况下调用外部代码和数据——这一过程可能导致性能瓶颈和稳定性问题。”

**支持所有阶段的开发人员**

与此同时，Oracle 已添加功能来帮助接纳新开发人员。尽管 Java 已有 29 年的历史，但随着该语言在企业和其他地方的持续流行，新开发人员一直在采用它。

“接纳 Java 的下一代开发人员是 Oracle 的一项关键投资领域，”Oracle Java 平台产品管理高级总监 [Sharat Chandar](https://www.linkedin.com/in/sharatchander/) 告诉 The New Stack。“Java 22 版本通过我们所谓的‘Paving to Onramp’解决了这个问题。在 Java 22 中，两个关键功能可以帮助新开发人员加速采用 Java，即‘启动多文件源代码程序’（JEP 458）和‘隐式声明的类和实例主方法’（JEP 463，第二次预览）。

JEP 458 有助于让新开发人员更容易运行作为多个 Java 源代码文件提供的程序，从而避免了配置复杂构建工具环境的需要。JEP 463 旨在减少最初了解为大型程序设计的语言特性的需要，从而帮助开发人员更容易构建流线型程序，这些程序最终可以无缝扩展以在他们的技能增长时采用更高级的功能。

Saab 在一份声明中表示：“通过提供简化应用程序开发的增强功能，并扩展 Java 的覆盖范围使其可供所有技能水平的开发人员使用，Java 22 将帮助推动为组织和开发人员创建广泛的新应用程序和服务。”

“Java 作为一种编程语言、平台和开发者社区的受欢迎程度在摩洛哥和非洲地区持续增长，”[xHub](https://life.x-hub.io/) 的创始人兼首席信息官 [Badr El Hourari](https://www.linkedin.com/in/badrelhouari/?originalSubdomain=ma) 在一份声明中表示。借助 Java 22，Oracle 的 Java 团队对创新的关注将帮助新开发人员更快地采用 Java，例如使用 JEP 463。通过简化语言，Java 的入门变得更容易，适用于新一代程序员。

**更多更新和改进**

最新的 JDK 提供了更新和改进，包括来自 OpenJDK [Project Amber](https://openjdk.org/projects/amber/) 的语言改进（super[…] 之前的语句、未命名变量和模式、字符串模板以及隐式声明的类和实例主方法）；来自 Project Panama 的增强功能（外函数和内存 API 以及矢量 API）；与 [Project Loom](https://cr.openjdk.org/~rpressler/loom/Loom-Proposal.html) 相关的功能（结构化并发和作用域值）；核心库和工具功能（类文件 API、启动多文件源代码程序和流收集器）；以及性能更新（G1 的区域固定）。

与此同时，Java 22 中提供的重大更新包括：

**Project Amber 功能**
* [JEP 447](https://openjdk.org/jeps/447)：super(…): 之前的语句
* [JEP 456](https://openjdk.org/jeps/456)：未命名变量和模式
* [JEP 459](https://openjdk.org/jeps/459)：字符串模板（第二次预览）
* [JEP 463](https://openjdk.org/jeps/463)：隐式声明的类和实例主方法（第二次预览）

**Project Loom 功能**
* [JEP 425](https://openjdk.org/jeps/425)：结构化并发（预览）
* [JEP 426](https://openjdk.org/jeps/426)：作用域值（预览）

**Project Panama 功能**
* [JEP 419](https://openjdk.org/jeps/419)：外函数和内存 API（预览）
* [JEP 433](https://openjdk.org/jeps/433)：矢量 API（预览）

**核心库和工具功能**
* [JEP 457](https://openjdk.org/jeps/457)：类文件 API（预览）
* [JEP 458](https://openjdk.org/jeps/458)：启动多文件源代码程序
* [JEP 461](https://openjdk.org/jeps/461)：流收集器（预览）

**性能更新**
* [JEP 423](https://openjdk.org/jeps/423)：G1 的区域固定
**Java 22**

“虽然 JDK 22 不是长期支持更新，但没有理由不在生产中使用它，”Azul 的 Ritter 说。“字符串模板和 Stream 收集器等更新对开发人员很有吸引力，并且可以让他们更轻松地完成工作。Java 的 6 个月发布节奏比我们在 JDK 9 之前看到的更快地提供了更多新功能。”

“Java 22 感觉有点像 JDK 平台的早期更新，因为 Oracle 在该公司的大多数核心增强项目中引入了绝对数量惊人的增强功能——比如 Loom、Amber 和 Panama，”Omdia 的分析师 Brad Shimmin 告诉 The New Stack。

## Java 订阅

除了新的增强功能和特性外，Java 22 还受以下支持：

- [Java 管理服务](https://docs.oracle.com/en-us/iaas/jms/index.html) (JMS)——[Oracle 云基础设施](https://www.oracle.com/cloud) (OCI) 原生服务——它提供了一个统一的控制台和仪表板，以帮助组织管理 Java 运行时和应用程序（无论是在本地还是在任何云中）。
- Oracle 表示，在 OCI 上的云中部署 Java 时，它可以提高性能、效率、创新和成本节约，OCI 是首批支持 Java 22 的超大规模云之一。
- Oracle Java Universal SE 订阅是一种按需付费的产品。它包括对整个 Java 产品组合的三级支持、对 [GraalVM](https://www.graalvm.org/) 的授权、Java SE 订阅企业性能包、访问 Java 管理服务的高级功能以及以其业务速度升级的灵活性。

“看到 Java 22 为所有人（从学生到高级开发人员，从充满冒险精神的 Java 爱好者到寻求稳定性能的组织）捆绑功能，我感到惊讶，”[Mala Gupta](https://www.linkedin.com/in/malagupta/?originalSubdomain=in) 说，她是 Java 开发人员倡导者，[JetBrains](https://thenewstack.io/jetbrains-developer-survey-tracks-rapid-adoption-of-ai-chatgpt/)。“Java 正在通过继续减少编写代码初始步骤（通过实例 main 方法和隐式类）的仪式来采用极简主义方法，从而使人们更容易开始学习 Java。通过构造函数改造（super[...] 之前的语句），Java 再次证明它支持负责任的创新，并放宽了自 Java 1.0 版本以来存在的语言限制，而不会破坏任何现有代码……[IntelliJ IDEA](https://www.jetbrains.com/idea/) 2024.1 已准备好支持 Java 22 功能，以便 Java 开发人员可以轻松使用它们。”

## JavaOne 回归

在其他备受期待的消息中，Oracle 宣布 [JavaOne 大会将于 2025 年回归](https://thenewstack.io/java-21-is-nigh-whither-javaone/)。作为全球 Java 社区的旗舰活动，JavaOne 将于 2025 年重返旧金山湾区。JavaOne 2025 将于 2025 年 3 月 17 日至 20 日在加利福尼亚州红木城举行，与会者可以了解最新的 Java 开发，并与 Oracle 的 Java 专家和行业专家互动。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。