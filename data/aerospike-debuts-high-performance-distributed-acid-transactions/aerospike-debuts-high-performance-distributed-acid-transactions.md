
<!--
title: Aerospike发布高性能分布式ACID事务
cover: https://cdn.thenewstack.io/media/2025/02/8091e800-aerospike.png
-->

最新的数据库升级为高性能OLTP工作负载提供一致性，并为多记录事务提供严格的串行化。

> 译自 [Aerospike Debuts High-Performance Distributed ACID Transactions](https://thenewstack.io/aerospike-debuts-high-performance-distributed-acid-transactions/)，作者 Jelani Harper。

传统上，对于具有高写入速度的分布式数据库来说，可用性和一致性之间需要权衡。Aerospike 的[高性能多模数据库](https://thenewstack.io/from-db2-to-real-time-with-aerospike-founder-srini-srinivasan/)的8.0版本于周三发布，它通过提供大规模的实时分布式ACID事务支持来帮助消除这种观念。

[Aerospike](https://aerospike.com?utm_content=inline+mention)因其高性能联机事务处理 (OLTP) 而闻名[已久](https://thenewstack.io/how-to-manage-45-billion-client-records-with-aerospike/)，其引擎已更新了关键功能，非常适合在不牺牲速度的情况下确保一致性。除了提供分布式 ACID 事务外，8.0版本还保证了这些事务的严格串行化。

还有一些直观的交易 API，允许在单个事务中执行多个操作，同时简化开发人员的体验。

## 支持一致性

据 Aerospike 首席技术官 [Srini Srinivasan](https://www.linkedin.com/in/drvsrini)介绍，该版本的目的是“共同推动该领域向前发展，以获得更高性能的数据库，同时支持一致性。并且，我们试图在添加强一致性的同时最大限度地减少性能和可用性的折衷。”

Aerospike 的 ACID 属性确保事务不会相互干扰，同时产生易于理解的结果。这一点对于金融等受监管领域的组织至关重要，这些组织每秒处理的事务数量高达数亿次——每次事务可能包含多条记录。

Srinivasan 表示，此类组织“正在使用我们来实现高性能，但他们需要反规范化数据并将其放入单个记录中。”“而且，如果他们需要将多条记录链接在一起，同时出于监管原因而将它们分开，则需要实现适当的事务，这就是 Aerospike 8 所做的。”

最重要的是，更新后的引擎将维护一致性的责任从应用程序级别转移到数据库级别，从而解放了开发人员的这些重要顾虑。

## 一致性和性能

在发布 Aerospike 数据库 8 之前，Aerospike 为单记录操作提供事务一致性。新版本的分布式 ACID 特性为更复杂的事务提供了更强的一致性。“当您添加多记录 ACID 分布式事务支持时，您可以在同一事务中更改多条记录，”Srinivasan 解释道。此外，开发人员可以实现原子性、一致性、隔离性和持久性 ([ACID](https://thenewstack.io/can-nosql-databases-be-acid-compliant/)) 在跨越云、数据中心和地理位置的分布式系统中进行各自事务的好处。

原子性确保事务要么发生，要么不发生。隔离意味着其他事务不会访问事务当前正在访问的记录。持久性意味着系统不会丢失数据。最重要的是，这些好处是为高性能应用程序提供的。Aerospike 的“提供一致性的算法被设计成比许多其他算法提供更高的可用性，”Srinivasan 说。“这实际上是独一无二的。”

## 严格串行化

Aerospike 数据库 8 的分布式 ACID 事务的[严格串行化](https://stackoverflow.com/questions/60365103/differences-between-strict-serializable-and-external-consistency)也是开发人员的一项关键功能。Srinivasan 表示，此属性保证了事务在数据库中的执行顺序与其发生的顺序相同，这意味着解决这些问题不是应用程序构建过程的一部分。如果一个组织正在将资金从一个银行账户转移到另一个银行账户，并从后者提取资金，则在一系列操作中，使用严格的串行化，“如果一个事务在另一个事务开始之前完成，数据库将完全按照这种方式执行它，”Srinivasan 说。

严格的串行化意味着访问数据库的每个新事务都会使用先前事务对数据库所做的更改进行更新。此外，Aerospike 对多记录事务的严格串行化不会影响数据库以前拥有的单记录事务支持的性能。事实上，它实现了前者而“不会减慢单记录的速度，”Srinivasan 评论道。

## 免除应用程序和开发人员的责任

Aerospike数据库8的新特性将确保一致性的负担从依赖数据库的应用程序转移到了数据库本身。这一发展意义重大，原因如下：首先，它带来了更可靠的应用程序、可靠的运行时间和更好的性能。据Srinivasan介绍，许多为Aerospike提供一致性的算法可以在应用程序级别实现。“这意味着应用程序必须跟踪它们在数据库外部执行的每个事务的状态，”Srinivasan透露。“然后，如果应用程序服务器死机，就会丢失状态。因此，非常难以避免数据丢失。”

其次，很难识别分布式系统中的错误，这可能会导致事务执行顺序出现问题。除了提供上述一致性和事务正确顺序的保证外，Aerospike还提供其他工具来维护数据库级别的一致性。

据Srinivasan介绍，诸如[Jepsen的测试功能](https://jepsen.io/)之类的资源使“第三方应用程序开发人员能够检查，‘嘿，这个数据库，它能工作吗？它是算法的证明吗？’这使得应用程序程序员更容易。他们不必做所有繁重的工作。他们只需编写应用程序，就可以依赖这些保证，并且可以获得这些保证确实得到满足的验证。”


## 事务API熟练度

Aerospike数据库8还包含一个事务API，可用于为OLTP系统启用复杂事务。使用该API，一旦事务开始，就可以在达到事务结束阶段之前在其内执行许多操作。“在那时，你不能保证事务会提交，因为在那之前其他人可能已经干预了，”Srinivasan说。“但是，所有这些都在事务结束阶段完成。你基本上在一个信封里放入了你在数据库上执行的所有类型的操作。这就是API。”

Aerospike数据库8还支持[Spring](https://spring.io/)，以改善使用此框架与数据库的开发人员体验。据Srinivasan介绍，“应用程序开发人员只需使用Spring编程，然后，在幕后，我们提供一个库，将Spring API的应用程序调用转换为数据库级别的底层API调用。Spring开发人员不需要了解Aerospike数据库的API。”

## 推动领域发展

许多NoSQL数据库最初将可用性优先于一致性，然后逐渐添加后者的属性。Aerospike的与众不同之处在于它是一个分布式、高性能的多模式数据库（支持向量、键值、图形格式和文档格式），它为复杂的多记录事务提供一致性。

凭借其一致性保证，它允许开发人员专注于构建其应用程序的最佳逻辑，而无需因担心现在在数据库级别处理的问题而影响其生产力或进度。
