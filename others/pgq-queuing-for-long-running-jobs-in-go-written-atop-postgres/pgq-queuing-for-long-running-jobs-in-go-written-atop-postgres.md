<!--
title: PGQ：Go语言中基于Postgres的长时间运行作业排队
cover: https://cdn.thenewstack.io/media/2024/02/1ef3e76d-pgq2-1024x632.png
-->

使用Postgres，开发人员可以利用他们可能已经熟悉的基础架构为其服务添加简单但可靠的消息队列。

> 译自 [PGQ: Queuing for Long-Running Jobs in Go Written Atop Postgres](https://thenewstack.io/pgq-queuing-for-long-running-jobs-in-go-written-atop-postgres/)，作者 Susan Hall 是 The New Stack 的赞助编辑。她的工作是帮助赞助商获得对其贡献内容的最广泛读者群。

当 Dataddo 将 RabbitMQ 的性能发挥到极限时，它发现已经有一个解决方案就在眼前：PostgreSQL。

长时间运行的任务在 RabbitMQ 上导致心跳超时和重新连接，但无法全面了解问题的原因。在托管的 AWS 上运行意味着这家数据集成公司无法按照自己期望的方式配置 [RabbitMQ](https://thenewstack.io/rabbitmq-is-boring-and-i-love-it/)，但又没有工程能力来自行管理这个开源消息代理。

通过与一些 Postgres 贡献者在其他项目上的合作，这家全球数据集成公司发现，[经得起考验的老牌数据库 Postgres](https://thenewstack.io/the-competitive-advantage-of-postgres/) 可以很好地处理这些长时间运行的任务，并提供更深入的洞察力，以发现任何潜在问题。因此，[队列机制 PGQ](https://github.com/dataddo/pgq?tab=readme-ov-file)，即 Postgres 队列，诞生并开源了。

使用 Go 编写，并构建在一个 Postgres 数据库之上，这意味着开发人员可以利用他们可能已经熟悉的基础架构，为他们的服务添加简单但可靠的消息队列。

Dataddo 的首席技术官 [Tomáš Sedláček](https://www.linkedin.com/in/tomasedlacek/?originalSubdomain=cz) 表示：“很多人对这个话题感兴趣……[他们]已经在公司或项目中使用 Postgres，并且面临着相同的困扰，或者他们将 Postgres 用于所有事情，并且对此感到满意。”他补充说，使用 RabbitMQ、[Kafka](https://thenewstack.io/decoding-kafka-why-its-worth-the-complexity/) 或其他工具只是增加了开发人员需要学习和维护的另一种技术。从招聘的角度来看，找到只懂得 Postgres 的工程师更容易，他说。

## 一个普通的 Postgres 表

PGQ 中的队列只是一个普通的 Postgres 表，因此任何具有标准 SQL 经验的人都可以使用它来查看表格、插入新行或者进行其他操作。PGQ 使用发布者-消费者模型，其中发布者将事件添加到队列，消费者异步处理这些事件。随着大量任务分布在多个工作进程之间，这也使得作业可以并行执行。PGQ 被设计为即使在临时故障时也具有弹性，具有处理错误和重试的机制。

根据 Sedláček 的说法，改进的可见性是一个很大的优点。

Dataddo 发现 RabbitMQ 的可观测性有限 —— 只能看到等待处理的内容，而无法查看正在处理或已经处理的内容。

在 Postgres 中，所有内容都写入硬盘而不是内存模式，以消除任何数据丢失的风险，这意味着无论处理是否完成，都有一条记录。您可以轻松跟踪指标，例如队列深度、处理和错误率，并根据需要进行自定义。

“使用 PGQ，您可以很好地观察队列中发生的事情；[错误]默认是被缓解的……就像昨天队列中发生了什么？……它已经存储在那里，直到您删除它，”他说道。

公司表示，对于已经使用 Postgres 的公司来说，PGQ 效果良好，不需要为速度进行优化，也不想处理另一种技术的学习曲线和维护工作。由于它将所有内容都写入硬盘，根据 Sedláček 的说法，PGQ 比 Kafka 稍慢一点，但差别不是很大。

但对于对消息路由有高度高级要求或处理极大容量且需要优化吞吐量的公司来说，PGQ 不太合适。

尽管目前只适用于 Go 应用程序，但 PHP 版本正在开发中。

## Dataddo 内部如何使用 PGQ

成立于2018年，[Dataddo](https://dataddo.com/) 提供了一个完全托管的、无代码的数据集成平台，提供了 ETL（提取、转换、加载）、ELT（提取、加载、转换）和反向 ETL 服务，以及超过250个连接器，安全地在基于云的应用程序和商业智能工具、数据仓库和数据湖之间传送数据。

其客户包括 X（前身为 Twitter）、Ogilvy、Uber Eats、国际金融服务提供商安联和微软。

Dataddo 每天内部使用 PGQ 处理超过20万个长时间运行的作业，以及发送电子邮件或保存日志等短作业，Go、PHP 和 Node.js 之间的异步应用程序通信，以及监视其平台性能。
