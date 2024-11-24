
<!--
title: 基于高性能 Java 平台的先进舰队规模优化
cover: https://cdn.thenewstack.io/media/2024/11/0d5195bc-sizes.jpg
-->

云环境下Java应用集群规模调整的挑战与策略

> 译自 [Advanced Fleet Right-Sizing With High-Performance Java Platforms](https://thenewstack.io/advanced-fleet-right-sizing-with-high-performance-java-platforms/)，作者 John Ceccarelli。


在当今以云为中心的IT环境中，[精细化调整计算资源](https://thenewstack.io/the-right-sizing-problem-in-cloud-computing-and-how-to-solve-it/)已成为全球开发人员、[DevOps](https://thenewstack.io/devops/)和站点可靠性工程师面临的一项重大挑战。精细化调整的主要驱动力通常是减少资源浪费和降低云支出。但这些考虑需要与其他业务需求（例如性能和运营复杂性）相平衡。目标是找到最佳点：精简到足以具有成本效益，同时又足够强大以确保可靠的服务交付。

虽然大多数云优化策略与编程语言无关，但[Java](https://thenewstack.io/oracle-unveils-java-23-simplicity-meets-enterprise-power/)应用程序为精细化调整带来了独特的挑战。此外，一类名为高性能Java平台的新型Java运行时环境已经出现，以解决Java的一些特定问题。这些下一代平台提供了改进的启动时间、减少的内存占用和更可预测的性能特性——从根本上改变了我们在云环境中处理Java应用程序大小的方式。

让我们探讨在云环境中精细化调整Java应用程序集群的具体挑战和策略。我们将检查关键的优化领域，深入探讨每个领域的Java特定考虑因素，并演示高性能Java平台如何简化这些工作。

## 目标

在理想情况下，我们只会在任何给定时间为满足流量所需的资源付费，并在不需要时关闭这些资源。最重要的是，这种弹性扩展不会影响响应时间、服务级别协议 (SLA) 或用户体验。

精细化调整集群的主要工作领域通常包括：

- 垂直精细化调整每个Pod以最大限度地减少空闲资源。
- 水平精细化调整集群以确保您拥有足够的服务器实例来处理负载。
- 设置扩展策略以根据负载调整服务器数量。

## 细节决定成败

对于所有云技术而言，节省成本和提供最大性能的目标之间存在冲突。虽然需求可以立即激增，但需要时间来配置服务器基础设施（K8s节点、EC2实例等）以满足该需求。这些冷启动延迟迫使组织做出艰难的权衡：要么以更高的成本维持过多的容量以处理潜在的峰值，要么在需求激增期间冒服务下降的风险。大多数公司倾向于过度配置，优先考虑性能和可靠性而不是成本效率。

牺牲成本以换取性能的示例包括：

- 不管负载如何，始终让服务器保持开启状态。
- 在每台服务器上使用较低的资源百分比。

对于Java而言，成本和性能之间的冲突更为突出。即使在基础设施配置之后，Java应用程序也需要额外的时间和CPU资源才能达到全速运行。虽然与JavaScript等解释型语言相比，Java提供了卓越的性能、安全性和可维护性，但在启动时，有时甚至在稳定状态下，您都需要付出代价。

## Java启动和预热

在弹性环境中启动Java应用程序的生命周期如下所示：

- **节点启动** – 配置虚拟机或容器，包括初始化容器的操作系统。
- **JVM启动** – 加载Java虚拟机 (JVM) 的所有内部库并准备运行应用程序。
- **应用程序启动** – 加载所有代码片段，包括SpringBoot初始化等内容，直到应用程序准备好接受第一个事务。
- **应用程序预热** – 根据当前服务器硬件和应用程序使用模式优化Java代码以全速运行。此过程称为即时 (JIT) 编译。

## 高性能Java平台

高性能Java平台包含两个关键组件：增强的JDK和支持性基础设施服务。增强的JDK保持与Java SE规范的完全兼容性，以获得长期支持 (LTS) 版本，同时在三个关键领域提供比标准OpenJDK发行版显著的改进：

- 更快的应用程序性能
- 减少启动和预热时间
- 更一致的运行时行为

超越JDK，高性能Java平台提供集中式服务，与客户端JVM协同工作，以实现独立JDK发行版无法达到的性能和运营效率水平。

本文主要介绍以下技术：

* [GraalVM](https://www.graalvm.org/)，特别是GraalVM Native Image——GraalVM是来自[Oracle](https://developer.oracle.com/?utm_content=inline+mention)的替代JDK，运行在Truffle和Graal技术之上。它拥有免费的开源社区版和专有的闭源企业版。GraalVM Native Image是GraalVM的一部分，它将Java应用程序提前编译(AOT)成自包含的原生可执行文件，消除了JVM启动开销并减少了内存使用，但代价是牺牲了一些运行时性能优化和动态Java特性。
* [Coordinated Restore at Checkpoint (CRaC)](https://openjdk.org/projects/crac/)——由Azul领导的CRaC OpenJDK项目旨在通过使JVM能够在检查点捕获和存储其完全预热的狀態来缩短启动和预热时间。然后，应用程序可以从此检查点恢复，绕过典型的初始化和预热阶段，从而实现近乎即时的性能。CRaC受多个JDK支持，例如Azul Platform Core、Azul Platform Prime和Bellsoft Liberica，以及[AWS](https://aws.amazon.com/?utm_content=inline+mention)Lambda函数和许多流行的应用程序框架，如Quarkus和SpringBoot。
* [Azul Platform Prime](https://www.azul.com/products/prime/)——Azul的高性能Java平台，一个优化的OpenJDK版本。它包括Optimizer Hub，这是一套可以帮助服务器协同工作以获得更好性能的服务。

## 垂直扩展

垂直扩展是调整服务器可用的CPU和RAM的过程，以确保有足够的容量来处理流量峰值，同时避免浪费未使用的容量。虽然传统的虚拟机和物理服务器需要以粗略的增量分配资源，但容器能够以精确的方式分配计算资源。

一种流行的方法是在Kubernetes中使用[Vertical Pod Autoscaler (VPA)](https://thenewstack.io/getting-the-most-from-kubernetes-autoscaling/)。VPA监控您的使用情况，然后调整pod可用的资源并重新启动它以使调整生效。

那么为什么不只在您的Java集群上使用VPA就完事了呢？好吧，当调整Java容器大小时，您通常还需要调整命令行Java堆参数以及pod大小，而VPA无法做到这一点。此外，由于JVM可以“保留”未使用的内存，因此VPA很难正确测量使用情况并进行调整。在大多数情况下，VPA不适用于Java应用程序，您需要手动设置Java容器的资源限制。

Java应用程序的问题在于运行开始时JVM预热应用程序期间的高JIT CPU活动周期。

![](https://cdn.thenewstack.io/media/2024/11/5416e065-image2-1024x565.png)

通常，您必须为该编译峰值保留CPU容量，即使该容量在稳定状态下将处于空闲状态。换句话说，您永远都要为应用程序运行开始时仅持续几分钟的峰值付费。

## 高性能Java平台如何提供帮助

用于减少由于JIT CPU峰值而导致的浪费容量的高性能Java平台：

* **GraalVM Native Image**
    * **优点**– 通过在应用程序运行之前执行所有优化，AOT减少了运行应用程序所需的CPU和[内存](https://thenewstack.io/how-to-test-how-much-memory-your-java-application-uses/)。
    * **缺点**– GraalVM Native Image不适用于很大一部分现有的Java代码，因为AOT无法应对许多Java模式。AOT代码的执行速度比JIT生成的代码慢。
* **CRaC**
    * **优点**– 通过在JIT消退后检查点应用程序，您可以在较小的机器上恢复CPU峰值后的状态。
    * **缺点**– 使用CRaC的现有应用程序需要进行代码更改才能正确恢复应用程序。由于CRaC尚未被广泛采用，因此很少有流行的库进行了这些更改。您还需要一个用于清理在快照之前用于预热机器的事务的状态。最后，您仍然需要为以后应用程序生命周期中可能发生的额外JIT活动（反优化）保留容量。
* **Azul Platform Prime – Optimizer Hub**
    * **优点**– 通过将JIT卸载到外部Cloud Native Compiler服务，Optimizer Hub适用于任何代码。由于Optimizer Hub可以处理反优化风暴以及初始预热，因此您可以自信地移除所有为JIT保留的CPU。
    * **缺点**– Azul Platform Prime是基于OpenJDK的商业解决方案，在配置和维护Optimizer Hub方面增加了复杂性。

## ‘Stuff Happens’

人们预留大量冗余容量的另一个原因，尤其是在对延迟敏感的应用程序中，是因为“意外情况时有发生”。从垃圾回收暂停到反优化风暴，再到JVM在执行长时间运行的任务时锁定某些资源，您必须处理JVM上各种尖峰行为。因此，人们通常将其容器的CPU利用率阈值设置为低至35%，以预留应对这些峰值的容量。

## 高性能Java平台如何提供帮助

- Azul Platform Prime – C4无暂停垃圾收集器通过允许应用程序在执行GC时继续接收请求来消除大多数GC暂停。Prime的ReadyNow技术可防止由反优化风暴（应用程序使用模式变化迫使JVM丢弃并重新编译优化代码的事件）引起的性能中断。通过在应用程序重启期间维护和智能地重用优化配置文件，ReadyNow即使在工作负载模式发生变化时也能确保一致的性能。
- GraalVM – GraalVM Native Image提前优化所有代码，这意味着当使用模式发生变化时不会出现反优化风暴。AOT编译的一个副作用是代码运行速度比使用JIT编译优化的代码慢。

## 水平集群规模调整

水平集群规模调整是指根据当前流量设置任何时间运行的服务器数量的过程。所需的服务器数量是每个服务器承载能力的函数——每个服务器在仍然符合SLA的情况下可以处理多少事务。

减少水平集群规模的最佳方法是从每台服务器获得更多工作量。一些高性能Java平台具有先进的JIT编译器，可以比OpenJDK以更低的CPU执行单个事务，因此可以完成更多事务而不会触发基于CPU的自动扩展策略。

## 高性能Java平台解决方案

- Azul Platform Prime – Falcon JIT编译器生成的代码运行速度比标准OpenJDK快40%。Azul Platform Prime还消除了大多数应用程序暂停和抖动，从而提高了具有基于延迟的SLA的服务器的承载能力。
- GraalVM – 虽然GraalVM CE和GraalVM Native Image生成的代码都比OpenJDK慢，但付费的GraalVM EE具有先进的JIT编译器，生成的代码速度比OpenJDK快。

## 根据需求扩展服务器数量

优化服务器以节省成本的最佳方法是完全关闭它。云的弹性特性意味着您可以根据计划或基于负载的自动扩展来扩展和缩减服务器规模，因此您只需支付使用的费用。

但是，虽然自动扩展听起来很简单，但实际上它很复杂，并且通常需要重新架构。即使是编写用于扩展和缩减的应用程序，也容易受到Java启动和预热问题的困扰，这使得在操作上难以确保新配置服务器的良好性能。大量的开发人员和DevOps时间都花在了如何让这些服务器能够足够快地准备好接受流量以应对突然的流量高峰上。

总而言之，以下是上面描述的高性能Java解决方案的优缺点：

**GraalVM Native Image**

- **优点**– 解决了启动和预热问题，通常在几毫秒内实现首次事务时间，并且运行时没有JIT。
- **缺点**– 不适用于很大一部分现有的Java代码，因为AOT无法应对许多Java模式。AOT代码的执行速度比JIT生成的代码慢。

**CRaC**

- **优点**– 解决了启动和预热问题，但即使在流量模式发生变化时也能实现全速代码。
- **缺点**– 使用CRaC的现有应用程序需要进行代码更改才能正确恢复应用程序。由于CRaC尚未被广泛采用，因此很少有流行的库进行了这些更改。您还需要一种方法来清理用于预热机器的交易状态，然后再进行快照。最后，您仍然需要预留容量以应对应用程序生命周期后期可能发生的额外JIT活动（反优化）。

**Azul Platform Prime和Optimizer Hub**

- **优点**– 通过将JIT卸载到外部云原生编译器服务，并从其他服务器学习最佳优化模式，Optimizer Hub使您的应用程序比OpenJDK更快地达到全速。由于Optimizer Hub可以处理反优化风暴以及初始预热，因此您可以放心地移除所有为JIT预留的CPU。
- **缺点**– Azul Platform Prime是基于OpenJDK的商业解决方案，在配置和维护Optimizer Hub方面增加了复杂性。

## 结论

当您的业务运行在 Java 上时，在尝试平衡成本、性能和运营灵活性时，您会有一些特殊考虑。使用高性能 Java 平台可以消除一些权衡，并在相同或更好的性能下降低云成本。

使用高性能 Java 平台，您可以：

- 消除每台服务器上的资源浪费（垂直调整）。
- 以最少的服务器数量满足需求（水平调整）。
- 根据当前负载动态调整服务器数量（自动伸缩）。
