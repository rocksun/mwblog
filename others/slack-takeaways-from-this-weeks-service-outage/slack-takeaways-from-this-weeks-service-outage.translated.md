# Slack：本周服务中断的经验教训

![Featued image for: Slack：本周服务中断的经验教训](https://cdn.thenewstack.io/media/2025/02/1cf9b338-slack-logo-outage-2-1024x576.png)

周三上午，我们在The New Stack的同事开始在会议上和通过恐慌的电子邮件互相询问：嘿，你[Slack](https://api.slack.com/?utm_content=inline+mention)有问题吗？

事实证明，我们并不孤单。据该事件的[服务状态网站上的记录](https://slack-status.com/2025-02/1b757d1d0f444c34)显示，这款即时通讯应用遭遇了大范围的服务中断，其工程师花了近九个小时才解决问题，中断始于美国东部时间上午10:47。

The New Stack是一个[完全远程的组织](https://thenewstack.io/build-a-highly-productive-work-from-anywhere-dev-team/)，员工和贡献者遍布全球；因此，我们非常依赖Slack来保持联系。超过150个国家的用户也是如此。[Slack](https://thenewstack.io/developer-guide-a-new-way-to-build-on-the-slack-platform/)由Salesforce拥有，据报道，财富100强中有77家使用该消息服务。Slack用户包括[Airbnb](https://thenewstack.io/how-airbnb-and-twitter-cut-back-on-microservice-complexities/)、[Target](https://thenewstack.io/target-embraces-cross-organizational-devops-culture/)、[Uber](https://thenewstack.io/devpod-ubers-monorepo-based-remote-development-platform/)和美国退伍军人事务部。

是什么导致了中断？其他工程团队可以从这次事件中吸取哪些教训？

除了在事件期间在其网站上发布的更新外，Slack尚未公开中断的原因。该公司也没有回应The New Stack关于中断的问题。

周三下午4:04（美国东部时间），Slack状态更新显示：“修复工作包括修复受影响的数据库分片，这些分片正在导致功能退化问题。”“这已成为一个细致的过程，以确保我们优先处理影响最大的数据库副本。”

美国东部时间下午7:42，该公司发布消息称，它已“恢复了所有受影响的Slack功能的全部功能，例如发送消息、工作流程、线程和其他与API相关的功能。”

但恢复正常服务的工作仍在继续。周四，它[发布了一则更新](https://slack-status.com/2025-02/d41e4bfd1ccae26a)，时间戳为美国东部时间上午10:17，提醒用户在停机期间创建的事件“已排队并当前暂停。我们预计这需要一些时间，并将每小时更新进度。对于新的提交和事件，应用程序和集成将继续正常运行。”

## MySQL的问题

在缺乏Slack更完整解释的情况下，我们知道本周可能出了什么问题吗？

我们知道的是：Slack应用程序于2013年首次推出，从一开始，[根据2020年12月发布的一篇文章](https://slack.engineering/scaling-datastores-at-slack-with-vitess/)在Slack工程博客上，它使用[MySQL](https://thenewstack.io/upgraded-mysql-crashes-on-restart-percona/)作为其数据的存储引擎。2017年，它开始将其数据存储迁移到Vitess，这是一个用于MySQL的开源数据库扩展系统。

文章写道，随着公司的发展，“我们的应用程序性能团队经常遇到扩展和性能问题，并且不得不为工作区分片架构的限制设计变通方案。”

迁移到Vitess的决定是由组织在扩展时面临的一个常见问题驱动的：放弃其遗留技术将是多么具有破坏性。它与MySQL紧密结合。

博客文章写道：“当时应用程序中有数千个不同的查询，其中一些使用了特定于MySQL的结构。”文章由Slack工程师撰写。

“与此同时，我们积累了多年的部署、数据持久性、备份、数据仓库ETL、合规性等等方面的运营实践，所有这些都是为MySQL编写的。”
“这意味着放弃关系型范式（甚至具体来说是 MySQL）将是一个更具破坏性的改变，这意味着我们几乎排除了像[DynamoDB](https://thenewstack.io/diving-into-aws-databases-amazon-rds-and-dynamodb-explained/)或[Cassandra](https://thenewstack.io/why-apache-cassandra-5-0-is-a-game-changer-for-developers/)这样的 NoSQL 数据存储，以及像 Spanner 或[CockroachDB](https://thenewstack.io/how-doordash-migrated-from-aurora-postgres-to-cockroachdb/)这样的 NewSQL 数据库。”

但可能坚持分片模型为周三发生的类似事件埋下了伏笔，[Cockroach Labs](https://www.cockroachlabs.com?utm_source=tns&utm_medium=sponsor&utm_campaign=brand-pipe-tns-sponsor-page-description&utm_content=lp-homepage-learn-more&utm_term=prosp&utm_content=inline-mention)的联合创始人兼首席执行官暗示道。

在周三事件期间 Slack 的状态更新中，“他们提到了数据库分片损坏的问题，”告诉 The New Stack。他表示，“分片”这个词表明，“基本上，你有很多客户，很多数据，多到无法放入单个的单体数据库中。所以你创建了大量的数据库，并将它们称为分片。

“然后你说，‘好的，客户 1 到 100 在分片 1 上，100 到 200 在分片 2 上’，以此类推，对吧？问题是，你实际上是在管理 100 个数据库。所以你不仅仅只有一个数据库，你拥有 100 个，而且它们都是独立的。它们是孤立的，这实际上是一个巨大的问题，因为你可能有一个客户太大，无法容纳在一个分片上。”

在这种情况下，说存在权衡。一方面，“当你丢失一个分片时，你只会丢失一部分客户。但问题是，你有 100 个东西需要管理，而且它们都有自己独特的怪异之处，因为不同的客户使用它们的方式不同。”


## 测试哪里出了问题
公司的旗舰产品 CockroachDB 是一个分布式 SQL 数据库管理系统。所以他对推广自己的产品以及与 Slack 不同的数据存储方式（在一个为水平扩展而设计的单个分布式数据库中，内置数据冗余）有着既得利益。

但他同时也提供了一些关于为什么 Slack 的遗留架构可能会遇到复杂性和弹性问题的一些见解。

“我不知道 Slack 有多少分片，但我认为现在已经相当多了，”他说。“由于他们构建的东西适应了分片的概念以及每个分片上的弹性，他们也已经成为一家数据库公司，以及一家企业消息公司。

“当你拥有这些东西时，你编写的每一行代码，你编写的每个新功能，都必须处理你拼凑起来的这个复杂架构的底层、暴露的现实，顺便说一句，这些架构并不协同工作。它不是一个集成、整体的整体。”

如果你是一家像 Slack 这样的公司，它大量投资于 MySQL 数据存储系统，拥有数百或数千个分片，你能做些什么来防止像周三那样发生的灾难性服务中断呢？

“无论刚刚发生在他们身上的事情，这都应该成为他们标准测试流程的一部分，”说。测试团队应该专注于改进其恢复时间目标 (RTO)，将其从周三中断后 Slack 恢复大部分服务所花费的 9 个小时左右缩短。

他表示，需要注意的是：“Slack 并非独一无二。今年各地都出现了这些中断。这太疯狂了。从[美国联邦航空管理局](https://www.reuters.com/business/aerospace-defense/us-faa-pilot-safety-messaging-system-resumes-operations-2025-02-02/)到[巴克莱银行](https://www.reuters.com/world/uk/britains-lloyds-bank-says-customers-hit-by-payments-service-outage-2025-02-03/)和[第一资本](https://fortune.com/article/capital-one-service-outage-january-2025-update/)，每个人都会遇到中断。

“但问题是，好的，无论刚刚发生了什么，让我们定期测试一下。当我们拥有运行手册并应用它们时，我们可以将我们的 RTO 优化到什么程度？”

如果组织甚至可以每季度或每年两次测试其数据库基础设施，并确保其团队能够修复服务中断并了解解决问题所需时间的可观测性，“那么你至少知道何时出现轻微的倒退，并且知道当这种情况不可避免地再次发生时，成本将会是多少。”

他说，将备份数据库部署在与主数据库不同的云中是另一个最佳实践。


## 弹性的成本
另一个问题是，他指出，[弹性](https://thenewstack.io/cdn-outages-exploring-ways-to-increase-resilience/)的标准一直在变化。十年前，Cockroach Labs成立时，标准是“让我们在数据中心消失的情况下也能生存下来。因为这很常见：就像[谷歌](https://cloud.google.com/?utm_content=inline+mention)刚开始的时候一样，嘿，让我们在节点或物理机器出现故障的情况下生存下来。

“然后是，‘让我们在数据中心消失的情况下也能生存下来。然后是，‘嘿，人们想要在[整个区域消失](https://thenewstack.io/google-cloud-services-hit-by-outage-in-paris/)的情况下生存下来。’就像，现在人们想要在整个云提供商消失的情况下生存下来。”

Kimball说，没有足够的组织每季度或每年两次测试其系统的弹性，这其中有一个很好的理由。“做这些事情很昂贵。”

他补充说，这不仅仅是金钱问题，还有人员时间。与创建新功能和服务相比，测试和重新架构遗留系统可能对公司来说并不那么重要。

“有些公司决定，让我们拭目以待。如果他们真的面临一些严重的限制，这可能不是一个糟糕的答案。就像，如果事情出错，我们会承担后果，我们会尽力而为。

“这取决于你的用例以及你认为停机时间的成本是多少。对于金融服务来说，这已经不再是选择了，尤其是在监管机构的审查下。对于Slack来说，你知道，他们可能会继续使用他们的东西，因为迁移太难了。最终，你必须对事物进行现代化改造，他们会找到合适的时间。”

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。