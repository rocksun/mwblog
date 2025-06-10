<!--
title: Azul首席技术官：Java在30岁时仍然主导企业开发
cover: https://cdn.thenewstack.io/media/2025/05/71dcac54-jac-alexandru-nx6fp9n4xgw-unsplash-1.jpg
summary: Java 30 周年仍主导企业开发！Azul CTO 揭秘其持久力：生态完善、易维护。力压 LAMP、Ruby on Rails 等“杀手”，拥抱云原生，发力 AI。Optimizer Hub 提升 JVM 性能，Falcon JIT compiler 加速 30%-40%。未来属于云原生 Java！
-->

Java 30 周年仍主导企业开发！Azul CTO 揭秘其持久力：生态完善、易维护。力压 LAMP、Ruby on Rails 等“杀手”，拥抱云原生，发力 AI。Optimizer Hub 提升 JVM 性能，Falcon JIT compiler 加速 30%-40%。未来属于云原生 Java！

> 译自：[Azul CTO: Java at 30 Still Rules Enterprise Dev](https://thenewstack.io/azul-cto-java-at-30-still-rules-enterprise-dev/)
> 
> 作者：Darryl K Taft

Java 编程语言今天满 30 岁了。

在其首次亮相 30 年后，[Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) 仍然是[企业软件开发](https://thenewstack.io/why-pure-ai-coding-wont-work-for-enterprise-software/)的冠军，它无视数十年来关于其消亡的预测，并继续为世界上最关键的业务应用程序提供支持。

“[Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/)到目前为止，对这个问题的回答是最好的，”[Gil Tene](https://www.linkedin.com/in/giltene/)，[Azul Systems](https://www.azul.com/)的联合创始人兼 CTO 在被问及长期应用程序可维护性时告诉 The New Stack。“你今天可以雇用人员。你今天可以雇用数百万具有技能的人员来维护 10 年和 15 年前用 Java 编写的应用程序。没有其他语言可以真正做到这一点。”

## 在炒作周期中生存

Java 经受住了许多本应取代它的技术挑战。Tene 举例说：“我记得 20 年前回答过这个问题，而且我一直以同样的方式回答这个问题，因为你可能还记得在 2000 年代初期，[LAMP](https://thenewstack.io/should-the-lamp-stack-add-an-open-llm-like-metas-llama/) [[Linux](https://thenewstack.io/introduction-to-linux-operating-system/), [Apache](https://thenewstack.io/configure-multiple-websites-on-a-single-rhel-based-apache-host/), [MySQL](https://thenewstack.io/a-cheat-sheet-to-database-access-control-mysql/), [PHP](https://thenewstack.io/why-php-usage-has-declined-by-40-in-just-over-2-years/)/[Perl](https://thenewstack.io/this-week-in-programming-pondering-the-evolution-of-perl-7/)/[Python](https://thenewstack.io/what-is-python/)] 堆栈将接管世界并杀死 Java，但现在已经没有太多的 LAMP 堆栈程序员了。”

Java“杀手”的名单读起来就像一个曾经热门的技术墓地。“然后我们有了 [Ruby on Rails](https://thenewstack.io/dhh-wants-to-make-web-dev-easy-again-with-ruby-on-rails/)，它将接管世界并杀死 Java，而且现在真的很难找到 [Ruby 程序员](https://thenewstack.io/ruby-creator-yukihiro-matsumoto-on-the-challenges-of-updating-a-programming-language/)来维护那些东西了，”Tene 补充道。

令人瞩目的不仅仅是 Java 的生存，还有它的持续增长。“Java 根本没有萎缩。Java 一直在增长和增长，它也有邻居也在增长和增长，”Tene 解释说。

## 从硬件先驱到软件创新者

Azul Systems 本身就体现了 Java 的演变。该公司成立于 2002 年，最初采用了一种新颖的方法，通过构建定制硬件来解决 Java 性能问题。“我们围绕运行 Java 应用程序并在其中整合它们，将它们集中在我们称之为计算机设备和计算设备集群中的数据中心构建了一些有趣的硬件解决方案，”Tene 回忆道。“今天，我们会称之为虚拟 Java 云。”

但随着计算环境的变化，Azul 也发生了变化。“在 2000 年代后期，随着商品硬件变得足够好，以及随着虚拟机管理程序、虚拟化程序并最终云接管，我们从硬件转向了，”他解释说。大约 15 年前，该公司转型为他所谓的“纯软件公司”。

今天，Azul 在 Java 生态系统中占据着独特的地位。“我们拥有 Java 中最大的工程团队，”Tene 说。“我们可能拥有 Java 领域中除 [Oracle](https://developer.oracle.com/?utm_content=inline+mention) 之外最大的商业产品，”他说。该公司现在为每个行业垂直领域的客户提供服务，专注于使 Java 运行得更快、更高效。

## 打破性能壁垒

Azul 的 [Optimizer Hub](https://www.azul.com/products/components/azul-optimizer-hub/) 代表了 [Java 虚拟机](https://thenewstack.io/introduction-to-java-programming-language/) (JVM) 运行方式的根本转变。该技术允许整个 JVM 集群共享优化数据，而不是每个 JVM 独立优化代码。

“它允许 JVM 集群进行协调、共享经验并共同进行交叉优化，而不是每个 JVM 独立运行并完全处理它必须单独处理的问题，”Tene 说。

他说，一些“非常大的地方”已经采用了这项技术，将其投入到拥有数万个 JVM 的生产环境中并“协调集群”。
Azul 最新推出的创新产品是上个月发布的 [JVM Inventory](https://www.azul.com/products/components/jvm-inventory/)。作为 Azul Intelligence Cloud 的一项功能，JVM Inventory 是一种 Java 发现工具和“云服务，可连续编目正在运行的 JVM，从而将 Oracle Java 迁移时间缩短数月，并帮助确保持续的 Oracle 许可证合规性，以进行审计防御”，该公司声称。

此外，该公司的 [Falcon JIT compiler](https://www.azul.com/products/components/falcon-jit-compiler/) 基于 LLVM 框架构建，展示了 Azul 致力于突破 Java 性能界限的决心。“Falcon JIT 编译器产生的 Java 速度比世界上任何 JVM 都要快很多。它比 [OpenJDK](https://thenewstack.io/microsoft-releases-its-own-distro-of-java-21/) 中的 [C2 compiler](https://www.baeldung.com/jvm-tiered-compilation) 快 30% 到 40%，”Tene 声称。

## 从 Applets 到 AI

Java 的发展历程讲述了现代计算本身的故事。Tene 说，从 30 年前“Web 浏览器中这个有趣、古怪的小东西”开始，它已经成为企业计算的支柱。

在 90 年代后期，Java“有点闯入了企业计算领域，然后在最初推出的三四年内就主导了企业应用程序”，他补充道。

“如果你看看 Java 的开端，以及它如何迅速取代了之前用于构建业务应用程序的所有其他东西，我们可以说我们还没有看到将取代 Java 的东西，”Tene 指出。“从它发生的那一刻起，直到每个人都只是用[新语言]而不是 Java 构建应用程序，可能只需要两到四年，而且我们根本没有看到这种趋势发生的迹象。”

然而，即使在新兴的 AI 领域，Java 也在找到自己的位置。“根据我几个月前听到的统计数据，Java 目前是 AI 领域的第三大语言，Python 遥遥领先，”Tene 在谈到 AI 应用程序开发时说。“我们看到越来越多的应用程序希望将 AI 融入到应用程序中，这对于 Java 应用程序来说是很自然的事情。”

## 企业优势

Java 的持久力归结为一个简单的商业现实：企业需要持久的软件。“当你试图弄清楚你想用什么来构建你的应用程序时，你应该考虑的一件事是，你将如何在 5 年后、10 年后维护它？你是否能够雇佣到你需要的人来维持它的生命并继续运行？”

这种理念延伸到了 Java 的开源生态系统。“整个 Java 社区倾向于产生长期存在的框架、项目和库，人们使用它们并在许多年里依赖它们，”Tene 解释说。“大多数 Java 社区项目，如果你看看它们，没有发生很多丑闻，没有很多独裁者或令人讨厌的人在运行它们。”

Azul 在其客户群中亲眼目睹了这种稳定性。“由于 Java 如此普遍，如此流行，我们在几乎所有你能想到的垂直领域都有各种规模的客户，”Tene 说。“当他们想要良好或更好地运行 Java 时，当他们想要 Java 应用程序的良好指标（这是我们主要平台的优势所在），或者他们只是想要非常好、负责任地构建、支持的开源时，这就是我们核心平台所提供的。我们为这些客户提供服务。”

此外，JavaScript 用于 Web GUI，Python 是开发人员“编写非常轻量级的东西和服务”的方式。但是，每当你看到事物成熟时——从原型设计和一些初始功能到“我需要在规模上运行它，而且我不能让它的成本是它需要的 50 倍”，它们往往会过渡到像 Java 这样的东西，”Tene 说。他引用了 [Twitter](https://www.infoq.com/articles/twitter-java-use/)（现在的 X）和 [LinkedIn](https://www.linkedin.com/blog/engineering/infrastructure/linkedin-s-journey-to-java-11) 作为例子。

“我们看到很多人用 Java 或基于 Java 的语言（如 [Kotlin](https://thenewstack.io/get-started-using-kotlin-multiplatform-with-a-network-listener-project/) 或 [Scala](https://thenewstack.io/scala-creator-proposes-lean-scala-for-simpler-code/)）重写大型后端，或者今年 JVM 的任何新语言，但从这个意义上说，它们都是基于 Java 的，我们只是看到更多，而不是更少，”Tene 说。

## 现代 Java 的复兴

与此同时，可能还记得 Java 冗长而繁琐的用户可能会对其现代版本感到惊讶。“[Java 25](https://openjdk.org/projects/jdk/25/) 将于今年晚些时候发布，它比 Java 8 更平易近人、更好、更容易启动，”Tene 说。
该语言也采用了[云原生开发](https://thenewstack.io/cloud-native/)，并推出了诸如虚拟线程之类的创新技术，这些技术有望简化并发编程。“至少在 Java 中，并且我认为在 Java 25 及更高版本中，我们将有机会回到一个操作在其中运行的线程的简单旧概念，以及同时运行数百万个线程的能力。”

Azul 也在通过诸如 [Coordinated Restore at Checkpoint](https://openjdk.org/projects/crac/) (CRaC) 之类的项目为 Java 的即时启动能力做出贡献。“我们领导的那个 OpenJDK 项目专注于为 Java 应用程序和云环境提供非常快速的启动。因此，可以考虑自动扩展的微服务或需要非常快速启动的云函数。”

## 没有什么是永恒的

尽管 Java 目前占据主导地位，Tene 承认在技术领域中没有什么是永恒的。最终会有某种东西取代 Java。“当这种情况发生时，我确信，无论它被称为 Java 还是其他什么，我们肯定会大量使用它，谈论它，并对它感到兴奋。”

但就目前而言，在其诞生三十年后，Java 继续证明，有时最好的技术不是最新的技术，而是有效、可扩展且持久的技术。正如 Tene 所说，关于下一个大型编程语言可能是什么：“我们只是还没有看到它，而且我从 2000 年代初到中期就一直在这么说，所以，你知道，我一直在寻找，只是还没有看到它。”

与此同时，在一个痴迷于下一个重大事件的行业中，Java 在其 30 周年之际继续蓬勃发展，表明可靠性、可维护性和强大的生态系统通常比尖端功能更重要。