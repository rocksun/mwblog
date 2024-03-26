
<!--
title: 这个世界为什么不升级数据库？
cover: https://cdn.thenewstack.io/media/2024/03/6fef3377-database-upgrade-2.jpg
-->

如果您的开源数据库现在运行良好，为什么还要动它？因为生命周期结束的软件更难维护，而且您可能会错过有价值的新功能。

> 译自 [Why Isn’t the World Upgrading Its Databases?](https://thenewstack.io/why-isnt-the-world-upgrading-its-databases/)，作者 Richard Gall。

[数据库](https://thenewstack.io/data/) 是应用程序和软件的基础。它们也有些隐形；正如软件的通用语言所说，它们是后端，这意味着它们位于其他所有内容的*后面*或*下面*。

这意味着在升级时，很容易陷入两个陷阱之一：要么忘记它们的存在，要么强烈担心自己正在摆弄不应该碰的东西。

这是 [David Stokes](https://www.linkedin.com/in/davidmstokes/) 提出的观点，他是 [Percona](https://www.percona.com/?utm_content=inline-mention) 的技术布道者，Percona 是一家为 [开源数据库](https://thenewstack.io/open-source-databases-in-the-age-of-the-dbaas/) 提供支持和服务的组织。

他告诉 The New Stack：“部分原因是，如果它在运行，并且 [团队] 不确定数据库的实际作用或工作原理，他们就不想碰它。”

他补充说：“同样，谁会将某个东西从生产中取出以对其进行升级？如果它没有按时恢复，会产生什么后果？”

他建议，这种态度通常是：“它现在正在运行……为什么要碰它？等到它坏了再说。”

在某些版本的开源数据库达到其生命周期结束 (EOL) 的情况下，升级数据库的问题尤其重要。

例如，在 2023 年，[MySQL 5.7](https://thenewstack.io/oracle-support-for-mysql-5-7-ends-soon-key-upgrades-in-8-0/) 走到了尽头，这是一个非常流行的版本，已经存在了将近十年（它 [早在 2015 年就发布了](https://thenewstack.io/mysql-5-7-gets-savvy-with-a-cool-replication-hack/))，PostgreSQL 11、Apache Cassandra 3 和 MongoDB 6.3 也是如此。当然，当一款软件“退休”（因为找不到更好的术语）时，通常会有新版本，供应商或社区已决定投入精力——[MongoDB 7.0](https://thenewstack.io/how-to-plan-your-mongodb-upgrade/) 于 2023 年 8 月发布，[PostgreSQL 16](https://thenewstack.io/postgresql-16-expands-analytics-capabilities/) 于 2023 年 9 月发布，[Apache Cassandra 5](https://thenewstack.io/cassandra-5-0-what-do-the-developers-who-built-it-think/) 于 2023 年 11 月发布。

## 生命周期结束的悬崖边缘

对于许多团队来说，EOL 代表着悬崖边缘。这意味着该软件将不再被修补和更新，从而导致 [安全性](https://thenewstack.io/security/) 问题以及潜在的性能问题风险更大。

当然，[文档](https://thenewstack.io/an-engineers-best-tips-for-writing-documentation-devs-love/) 不会得到维护，并且任何支持（如果一开始有任何支持）都将完全消失。在某些情况下，这可能是一个合规性问题——例如，在支付领域，获得 PCI-DSS 认证的组织——那些需要遵守支付卡行业数据安全标准的组织——必须在发布后最多一个月内部署任何关键补丁。

Percona 的高级产品经理 [Jan Wieremjewicz](https://www.linkedin.com/in/janwier/) 回忆了 [Log4J 安全漏洞](https://thenewstack.io/log4j-the-pain-just-keeps-going-and-going/)。“想象一下运行在生命周期结束的软件上，该软件没有得到修补以排除潜在的零日漏洞，”他告诉 The New Stack。“每当我想到这一点，我都会起鸡皮疙瘩！”

不升级数据库的风险很大。从本质上讲，原本应该是更广泛系统的稳固基础的东西变成了一个累赘，一个随时可能破坏看似功能稳定的一切的定时炸弹。

但同样值得注意的是，新版本（尤其是主要版本）的发布可以为工程团队带来机遇。考虑任何软件在发布时通常具有的新功能和改进的体验。虽然其中一些可以被视为营销炒作，但重要的是要认识到，不升级可能意味着你错失了更好的做事方式。

## 为什么不升级？

鉴于这些重大风险，值得深入研究某些组织所特有的回避感（如果不是恐惧的话）。Wieremjewicz 强调的一个原因是软件工程团队的构成发生了变化。

他说，数据库架构师“是一个濒临灭绝的物种”——他们正被网站可靠性工程师挤出。“[DBA 越来越少，SRE 越来越多](https://thenewstack.io/why-a-dataops-team-needs-a-database-reliability-engineer/)，他们通常不像 DBA 那样精通数据库问题。”

他认为，这在一定程度上是因为基于云的[数据库即服务 (DBaaS)](https://thenewstack.io/developer-caveats-for-database-as-a-service/)。一方面，数据库即服务 (DBaaS) 简化了数据库配置和管理的许多方面。另一方面，它也让复杂性蔓延到其他地方，而技能和组织结构却以无法应对这种复杂性的方式演变。

“我们从几年前可能只有少数几个数据库变成了数千个，甚至更多。”斯托克斯说。“你仍然需要有人来检查查询并进行基本的卫生工作，确保帐户正确、密码正确、软件是最新的、复制正常、数据正在备份。”

这与数据库升级问题无关：它突出了问题的核心。在数据库被视为轻量级构建块而不是笨重、看似不可移动的锚点的时代，就在我们被提醒数据库是需要持续关注和维护的复杂事物时，我们想要假装它们根本不能被触及，或者它们是明天的难题。

## 缺乏吸引力？

有人可能会认为，升级数据库根本没有其他项目所具有的吸引力（或者更具体地说，没有明显的商业价值）。用斯托克斯的话来说，这在很大程度上是“卫生工作”。

他用另一种方式解释道：“一位高级副总裁进来，说，‘嘿，我有一个关于我们即将要做的新事物的绝妙想法。这是我的心血项目。我想让你负责。’你说‘好的，但管理库存流程的旧系统需要一些升级。’‘是的，但这是我的心血项目，我真的很需要它。’”

斯托克斯认为，这只会有一种结果——而且不利于升级。

“数据库升级总是很棘手，”他说，“因为即使在最好的情况下，它们也只是一些细微的改变。这需要大量阅读发行说明，并希望进行一两次测试，以确保一切正常。”

## 开源数据库的独特挑战

在升级方面，开源数据库特别具有挑战性。你几乎只能靠自己，可能依赖于[贡献社区](https://thenewstack.io/how-community-helps-developers-grow/) 来获取相关文档甚至支持。

在这些情况下，开源数据库可以为工程团队提供的灵活性变成了负担。团队受到一些他们无法轻松管理的事情的阻碍——即使是最活跃的开源项目在为团队提供特定实现方面的支持时也只能做这么多。

这就是 Percona 发挥作用的地方。它始于一段时间前，Wieremjewicz 讲述了创始人[Peter Zaitsev](https://thenewstack.io/author/peter-zaitsev/) 在 MySQL 担任开发人员后离开 MySQL 的故事，他的目标是为用户提供更大的支持。

尽管 MySQL 是该公司起源故事的基本组成部分，但其范围更广泛地涵盖了开源数据库。该团队很可能为使用 PostgreSQL 或 MongoDB 的公司提供支持，就像为 MySQL 提供支持一样。

这种平台或工具不可知论是有利的，原因有很多。

Wieremjewicz 说：“我们能够就解决方案提供建议——甚至可以非常真实和诚实地从一个数据库迁移到另一个数据库，因为我们不会通过推广我们创建的一些软件来赚钱。”“这完全是为了用户的利益。”

在升级数据库的特定情况下，供应商不可知论可能允许组织在解决数据库问题时更加开放甚至有创造力。当然，从 MongoDB 升级到 MongoDB 可能有意义，但如果探索一个新数据库与你的特定技术环境更相关呢？

即使拥有最博学多才和最开放的团队，也很难自己做出这些决定——外部的、不可知的建议在提供必要的支持和变革动力方面可能非常有价值。

## 升级的关键：预测和准备

不可否认，升级数据库可能具有挑战性。至关重要的是规划并保持领先一步。

Wieremjewicz 说：“你必须提前计划，不能等到生命结束才采取行动，你应该更早地预测。”

未能这样做可能会产生重大的技术问题——甚至商业问题——这些问题在以后更难纠正。

Stokes 不认为有一种正确的方法来升级数据库。它的方法最终取决于实际执行它的组织的成熟度和信心。

他说：“这是我们正在学习骑自行车的事情之一。”“有些人跳上去自己做——其他人需要有人在学习如何上下踩踏板和如何转向时安抚并稳定座椅。”他确信，只要有人需要了解数据库，Percona 就会对这些客户保持价值：“我们已经存在足够长的时间，知道如何绕过坑洼，避免上坡。”
