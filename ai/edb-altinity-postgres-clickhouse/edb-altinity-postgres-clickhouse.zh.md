**如果你构建过同时需要记录系统和快速分析的应用**，你一定懂这种痛。Postgres® 存储着订单、账户以及你的应用绝对不能出错的状态。ClickHouse 软件则负责回答各种查询。

一个针对事务进行调优的行存储，永远无法快速回答这些问题：过去一小时内跨越十亿个事件发生了什么、哪个用户群体正在流失、智能体接下来应该做什么。这两个引擎在各自的领域都极其出色。痛苦完全存在于它们之间的鸿沟中。

> “这两个引擎在各自的领域都极其出色。痛苦完全存在于它们之间的鸿沟中。”

EnterpriseDB (EDB) 已经 [收购了](https://www.enterprisedb.com/announces/altinity?utm_source=paid_media&utm_medium=press_release&utm_campaign=altinity_announcement) Altinity，这家独立公司是 Altinity Stable Builds、Altinity Kubernetes Operator 以及 Altinity.Cloud 背后的功臣。

头条新闻充满着商业气息。而开发者应该关心的原因则更为具体：[Postgres 的头号贡献者](https://www.enterprisedb.com/company/postgres-vitality-index)与[在生产环境中运行 ClickHouse 软件近十年的团队](https://altinity.com/clickhouse-contributions/)现在正致力于同一个路线图，而该路线图旨在解决你每周都要面对的三大痛点。

## **痛点 1：CDC 作业是无人问津的产品**

数一数已提交的 Postgres 事务与同一行数据在 ClickHouse 软件中可被查询之间有多少个活动部件。一个复制槽。一个拥有自身故障模式的连接器。一个需要你调整大小、确保安全并打补丁的消息中间件。一个必须在不静默丢弃列的情况下经历模式变更的接收端。一个去重策略，因为至少一次投递（at-least-once delivery）意味着会有重复。

对每一个跃点进行监控，因为其中任何一个跃点的延迟都会让“实时”仪表盘变成谎言。这些代码没有一行是你的产品。所有这些都在你的值班轮换表中，这就是凌晨 3 点收到报警的原因。

## **痛点 2：你的智能体正在基于昨晚的数据进行推理**

智能体工作负载改变了陈旧数据的经济学。落后 20 分钟的仪表盘令人烦恼。一个基于落后 20 分钟的聚合数据来批准退款、重新给库存定价或标记交易的智能体则是错误的，并且它会以机器的速度在任何人注意到之前错误数千次。

> “一个基于落后 20 分钟的聚合数据来批准退款、重新给库存定价或标记交易的智能体是错误的，并且会以机器的速度出错……”

因此，构建智能体的开发者在编写同样尴尬的代码：查询 Postgres 获取当前状态，查询 ClickHouse 软件获取趋势，在应用中将两者拼接起来，并祈祷时钟是一致的。你已经成为了集成层，而集成层正是 bug 滋生的地方。

## **痛5（译者注：原文如此）：你运行了两次技术栈**

每一个行级规则、“被屏蔽的列”以及“分析师只能看到聚合数据而不是客户ID”的策略，在 Postgres 中存在一次，在 ClickHouse 软件中又存在一次，而当有人更新其中一个却忘记更新另一个时，两者就会产生分歧。在 Kubernetes 上运行 ClickHouse 软件本身就是一份工作：Keeper、存储类、副本放置、备份、升级，以及一两个悄悄变成“ClickHouse 专家”的工程师。

如果你走了托管分析服务的捷径，你的数据就会存放在厂商指定的地方，你的账单也会随着他们的定价模型而不是你的基础设施规模增长。两个引擎、两个权限模型、两个操作器、两个支持合同，以及一个你并未选择的供应商锁定。

对照这三大痛点，这笔交易开始变得合理：每一项都对应 EDB 和 Altinity 现在计划共同构建的一个支柱。

## **支柱 1：一个共享层，而非管道**

今天，Postgres、[WarehousePG](https://www.enterprisedb.com/products/warehouse-analytics?_gl=1*bjtjqb*_up*MQ..*_ga*OTMzMTUwODQyLjE3OTM0MDI2NjE.*_ga_ND3EP1ME7G*czE3OTM0MDI2NjEkbzEkZzAkdDE3OTM0MDI2NjEkajYwJGwwJGgxMzI5MjI2NTI0)（EDB 的 MPP 数据仓库）以及 ClickHouse 软件可以读取相同的 Apache Iceberg 表并互相查询。Postgres 写入记录，而 ClickHouse 软件通过相同的开放表格式读取它，它们之间的数据移动和集成工作更少。计划中的是所有三个引擎之间的统一共享目录和统一治理模型，以及针对 Postgres 和 ClickHouse 软件的统一自主控制平面。

目前的组织架构是以 Iceberg 作为共享层，随后将 EDB 的控制平面作为共享操作。将共享目录视为正在构建的东西，而不是今天就能下载的东西。但设计目标正是你会为自己设定的目标：更少的跃点、一个目录、无需定制的协调代码。CDC 作业注定不再是你需要拥有的东西。

## **支柱 2：为智能体提供实时数据，在数据所在地进行治理**

EDB Postgres AI 将自主的[多模型数据层](https://www.enterprisedb.com/press-releases/edb-named-leader-multimodel-data-platforms-evaluation)与智能体运行时相结合，并在 Postgres 的数据层强制实施治理——在行动点进行并带有审计追踪。对于智能体而言，目标是让它请求业务上下文并从一个系统中获取记录和分析，而不是让你的代码去编排两个数据库和一个队列。

对于权限而言，所有三个引擎采用一个统一的治理模型是计划的一部分。今天，Postgres 为智能体强制执行按需访问，而 ClickHouse 软件则强制执行自己的基于角色的访问。计划是在数据所在的地方定义一次策略，让每个引擎去执行它，而不是在应用代码或第二个权限模型中重新实现它。这使得你的智能体能够在不需要安全审查阻塞发布的情况下，对当前真实的数据进行推理。

## **支柱 3：操作器、专家以及运行位置的选择**

Altinity 在生产环境中运行 ClickHouse 软件的解决方案一直是 [Kubernetes Operator](https://altinity.com/kubernetes-operator/)，拥有超过 1 亿次的拉取量，并且 Altinity Stable Builds 提供了三年的安全和错误修复向后移植维护。现在，这些知识融入到了 Postgres 的头号贡献者之中，后者还创建了 CloudNativePG 并将其捐赠给开源社区，如今它已成为一个 CNCF 项目以及许多团队已经在运行的 Postgres 操作器。一个供应商同时精通这两个操作器。

该计划是一个能够运行 Postgres 和 ClickHouse 软件的统一自主控制平面，并在它们发生冲突的夜晚为其提供一个支持组织的支持。运行在哪里由你决定：自备云（bring-your-own-cloud）、在自己的 Kubernetes 或 OpenShift 上自托管、气隙隔离（air-gapped）或完全托管。Altinity.Cloud 已经部署在客户自己的云账户中，而 EDB Postgres AI 则运行在你的自有账户或本地（on-premises）。因此，如果你的监管机构、CFO 或延迟预算要求数据留在原地，那么技术栈会跟随你，而不是反过来。

## **唯一的答案**

三大痛点，三大支柱，一个结论：应用层不应该再是协调两个数据库的地方。Postgres 保存记录。ClickHouse 软件在同一份实时数据上回答难题。你从中间删除的一切，都是你不再需要调试、监控或向审计员解释的代码。

> “最好的管道是你永远不必编写的管道。”

最好的管道是你永远不必编写的管道。对于那些花了好几年时间手动保持两个数据库一致，并向审计员、产品经理以及他们自己解释数据漂移的开发者来说，这个承诺值得关注。而且这是当每个计划中的部分落地时首先要测试的东西。

---

**本公告中描述的软件和服务由 EDB 和 Altinity 提供，而非 ClickHouse, Inc.。本公告并不意味着获得 ClickHouse, Inc. 的赞助或背书。Altinity 是一家独立公司，与 ClickHouse, Inc. 无关。ClickHouse 是 ClickHouse, Inc. 的注册商标。** [*clickhouse.com*](https://clickhouse.com/)*。*