<!--
title: 软件定义存储赋能开发者
cover: https://cdn.thenewstack.io/media/2025/07/a09fc610-storage.jpg
summary: 各组织正将数据库基础设施的控制权交给开发人员。传统测试方法无法发现潜在的存储问题。软件定义存储 (SDS) 通过为开发人员提供对其资源的更大控制权来赋能他们。SDS 有助于自动化和优化基础设施管理。
-->

各组织正将数据库基础设施的控制权交给开发人员。传统测试方法无法发现潜在的存储问题。软件定义存储 (SDS) 通过为开发人员提供对其资源的更大控制权来赋能他们。SDS 有助于自动化和优化基础设施管理。

> 译自：[How Software-Defined Storage Empowers Developers](https://thenewstack.io/how-software-defined-storage-empowers-developers/)
> 
> 作者：Carol Platz

为了满足对更精简的开发工作流程和加速创新的需求，各组织正将数据库基础设施的控制权和所有权推给开发人员。

[数据库](https://thenewstack.io/databases/)越来越多地成为开发人员工作流程的一部分，作为各种 Web、企业和移动应用程序的[后端](https://thenewstack.io/introduction-to-backend-development/)数据存储。

数据平台的性能和可靠性，特别是存储层，对于高效的开发周期至关重要。然而，对于缺乏数据平台架构专业知识的开发人员来说，确保数据库的可靠性和性能可能是一个巨大的挑战。

存储会影响您的 [Oracle](https://www.oracle.com/developer?utm_content=inline+mention) 工作负载的运行状况、它们的可靠性以及与您的业务相关的成本。不幸的是，规划不周的存储基础设施会带来高昂的代价：更长的开发周期、破坏性的回滚、较差的应用程序性能或故障、停机以及企业的财务损失。所有这些都让开发人员想要放弃他们的数据库，但这并不是一个可行的选择。

值得庆幸的是，有一种方法可以选择合适的存储架构，从而简化开发人员的配置、扩展和管理。这可以通过构建一个以软件定义存储为基础的数据平台来实现，使他们能够自己处理更多与数据库相关的任务，并重新获得对其数据库的控制权。

## 传统测试的不足

开发人员努力实现持续的应用程序性能和可靠性，旨在实现能够在生产中以最佳方式运行、有效扩展并允许安全代码部署的设计。

传统的测试方法旨在确保应用程序代码与存储系统正确交互，数据得到适当处理，以及整个系统可靠且高效地运行。尽管做出了这些努力，挑战仍然存在，并且问题通常在测试期间未被发现。

这是因为大多数测试优先考虑数据操作的准确性，而不是性能，因此常常无法发现潜在的存储问题。因此，即使数据处理正确，该解决方案的执行速度也可能太慢，无法满足生产需求，从而导致失败和客户满意度下降。

旨在解决性能问题的负载测试引入了自身的一系列问题，因为这些测试复杂、昂贵且通常在开发过程的后期才进行。当负载测试揭示性能瓶颈时，为时已晚，并且对业务的成本很高，需要耗费大量时间和金钱进行返工。

## 通过简化的基础设施赋能开发

[软件定义存储](https://www.lightbitslabs.com/product/?utm_source=TNS&utm_medium=article&utm_campaign=aug) (SDS) 通过为开发人员提供对其资源的更大控制权来赋能他们。该软件可以安装在商用硬件上，并在本地私有云中运行，以创建灵活且可扩展的存储系统。或者，它可以运行在公共云上。SDS 的灵活性简化了存储资源的配置、管理和扩展。

配置变得更容易，因为开发人员可以通过软件界面分配存储资源，而无需处理复杂的硬件配置。管理通过对存储资源的集中控制和监控来简化，通常具有自动化任务和基于策略的管理。扩展变得更加简单和高效，使开发人员能够根据需要轻松添加或删除存储容量，通常无需进行重大的硬件更改或停机。

当开发人员能够控制开发、部署和故障排除时，他们才能蓬勃发展。SDS 为开发人员提供了掌握所有权和加速开发周期的能力。[开发人员可以专注于创新](https://thenewstack.io/serverless-helps-developers-focus-on-differentiating-features/)，而不是被基础设施的考虑所累。

## Oracle on AWS 的优势

云存储提供了本地存储无法比拟的灵活性和可访问性。像 Oracle 这样 IO 密集型的数据库工作负载非常适合迁移到公共云，因为那里有大量的存储容量和计算能力可用。

但是，虽然 Oracle 对计算和内存的要求很容易在 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 上得到满足，但使用 Oracle 的 Tier 1 和 2 应用程序的性能要求是一个挑战。

这些挑战并非 Oracle 数据库所独有的，但由于多种因素，它们对于 Oracle 工作负载来说可能尤其成问题。虽然云[提供了大规模和灵活性](https://thenewstack.io/event-driven-microservices-offer-flexibility-and-real-time-responsiveness/)，但 Oracle 数据库的特定性能要求，尤其是对于任务关键型和高事务性应用程序，经过专门设计，旨在利用非常低延迟、高吞吐量和可预测的 I/O 环境。

云基础设施的虚拟化和共享特性，虽然对许多应用程序有利，但会引入性能变化和延迟，从而直接影响 Oracle 苛刻的 I/O 特征。Oracle 使用各种功能，如自动存储管理 (ASM)、实际应用集群 (RAC) 和大块大小，所有这些功能都旨在优化高性能本地存储上的 I/O。

在本地，这是通过高度优化的存储区域网络 (SAN) 和具有高性能 NVMe 驱动器的 DAS 架构实现的。在高度虚拟化、多租户的云环境中复制这种完全相同的性能水平和确定性 I/O 行为可能很困难。

值得庆幸的是，[AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-vv3tjsnmao7ak?sr=0-1&ref_=beagle&applicationId=AWSMPContessa) 中提供了 SDS 选项，可以提供解决方案。

[![标题：原生云存储与 AWS 上的 Lightbits 的性能比较。](https://cdn.thenewstack.io/media/2025/07/d9adac6c-image.png)](https://cdn.thenewstack.io/media/2025/07/d9adac6c-image.png)

使用运行 SLOB（Silly Little Oracle Benchmark）的 3 个 i4i.metal 实例比较原生云存储与 AWS 上的 Lightbits 的性能。更高的 IOPS 更好。（来源：Lightbits Labs）

## 一种新的数据库基础设施方法

传统的存储解决方案通常会给开发人员带来复杂性、性能和可靠性方面的限制，这会对业务产生重大影响。SDS 提供了一种新的范例，可以增强从测试到生产的整个软件开发生命周期。

SDS 有助于自动化和优化基础设施管理，使开发人员能够专注于应用程序开发和数据库设计，而不是存储基础设施。这可以提高效率、缩短上市时间并实现更可靠的数据库部署。

无论您是在本地私有云还是在公共云上部署 SDS，开发人员都可以确保其数据库工作负载的最佳性能和可靠性，并推动业务增长。

如果您有兴趣了解有关用于 Oracle 的软件定义存储的更多信息，以简化开发人员应用程序的生命周期，请下载我们的白皮书：“[使用软件定义存储运行 Oracle](https://www.lightbitslabs.com/tech-paper-run-oracle-with-lightbits-on-aws/?utm_source=TNS&utm_medium=article&utm_campaign=aug)”。