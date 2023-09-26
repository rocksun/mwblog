<!--
# 平台工程帮助规模化公司控制 DevOps 复杂度
https://cdn.thenewstack.io/media/2023/09/2cd7a602-scale-up-complexity-1-1024x576.jpg
Image by Liam Pozz on Unsplash.
 -->

随着 Capillary Technologies 客户基数翻倍并进入新市场，该公司经历了成长期的阵痛。与 Facets.cloud 的合作伙伴关系帮助提高了其在线时间和开发人员生产力。

译自 [Platform Engineering Helps a Scale-up Tame DevOps Complexity](https://thenewstack.io/platform-engineering-helps-a-scale-up-tame-devops-complexity/) 。

从创业公司向规模化公司的转变对任何科技公司来说都是个伟大的时刻。这意味着你已经具有了很好的客户黏性和价值证明，可以将你的触达面扩展到新的市场和垂直领域。

但这也意味着是时候扩大你的技术规模了，通常是在云中。这并不容易。

Capillary Technologies 开发客户忠诚度和参与度领域的 SaaS 产品，随着其客户数量从 100 增长到 250，开始经历典型的规模化公司的成长痛苦，该公司 CTO [Piyush Kumar](https://www.linkedin.com/in/piyush-kumar-71425315/) 向 The New Stack 透露。

随着 Capillary 的团队规模显着增长，其与 DevOps 复杂性相关的挑战也在增长。继续阅读以了解这些挑战是否对你也同样真实，以及 Capillary Technologies 如何利用 [Facets.cloud](https://www.facets.cloud/?utm_content=inline-mention) 的自助基础设施管理和采用[平台工程](https://thenewstack.io/platform-engineering/)来加速开发人员的生产力，并更快地为最终客户提供价值。

## DevOps 本身不会扩展

当 Kumar 在 2016 年以首席架构师的身份加入 Capillary 时，该公司的业务正在印度、东南亚和中东扩张，同时开始在中国获得客户的信任。 但当它希望进一步发展时，这家建立在[亚马逊网络服务(AWS)](https://aws.amazon.com/?utm_content=inline-mention)上的公司开始遇到云计算中的一些常见障碍。

“开发人员与我们 DevOps 基础设施团队人数之间的比例开始变得不平衡。”Kumar 说。“这意味着从工程师到 DevOps 团队的请求数量在增长，所以操作工单的数量基本上在增长，我们的响应时间开始放慢。”

接近 2019 年底，Capillary 开始扩张到美国和欧洲的新市场和新的云区域。这些机会也带来了挑战。

“新的区域本质上意味着在不同的区域完全重新启动软件、基础设施、监控等所有内容。”他说。

在新区域启动业务需要机构遵守数据主权和数据本地化法律。

随着这些启动的发生，Capillary 的基础设施处于半自动化模式。 “当你处于这种模式时，有些事情是自动化的，然后还有很多事情不是。 所以你对整个环境堆栈没有足够的可视性。”Kumar 说。

新的区域带来了很多惊喜 -- DevOps 团队不得不发展壮大以管理新的环境，并满足日益增长的客户群、产品组合和所需基础架构组件数量的新需求。

与此同时，Capillary 的工程师人数从约 100 人增长到 250 人。

“我们不希望稳定性开始受到影响，因为我们现在需要在多个环境中发布。” Kumar 说。 简而言之，他指出：“需要比线性扩展更多的东西来管理所有这些。”

## 云原生复杂性问题

很多[平台工程](https://thenewstack.io/new-ebook-free-platform-engineering-guide/)计划都是由于开发和运维工具的差异而启动的。这并不是 Capillary 的案例，该公司一直在中心管理基础设施。

正因如此，为了在扩展时与这种复杂性作斗争，团队成员逻辑上试图增加其基础设施的自动化覆盖范围。但是他们发现自己陷入了一个不断追赶的困境。

“所以我们继续自动化越来越多，作为一个团队，你会做更多，然后你会意识到还有更多要做的，所以它感觉像是一个不断的斗争，因为那个图景继续增长。” Kumar 说。

“在六个月内，我们继续前进并自动化的任何事情，我们基本上承担了更新的[债务](https://thenewstack.io/how-to-persuade-your-organization-to-pay-down-technical-debt/)，所以还有更多要自动化的。”

例如，他们采用了开源数据库 [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline-mention)，将新的基础设施、存储和数据库功能引入 Capillary 生态系统。DevOps 团队很快意识到他们无法轻松自动化一切——从启动新区域到监控、备份、升级、修补程序和恢复。

到 Capillary 团队自动化他们能自动化的一切时候，他们也已经采用了 [Apache Kafka](https://thenewstack.io/apache-kafka-primer/) 进行[实时数据流](https://thenewstack.io/how-to-get-started-with-data-streaming/)，并使用 AWS EMR 来运行和扩展工作负载——他们然后也试图自动化这些。

Capillary 的团队走开源路线是为了避免供应商锁定。但是无论他们选择开源还是专有，他们意识到[云原生图景](https://landscape.cncf.io/)的复杂性意味着很多自动化工具链的拼接。

为了解决这个问题，他们需要:

- 使整体基础设施和部署架构更加统一、更加可见，并实现从构建到部署的 100% 自动化。
- 将开发人员从依赖 DevOps 团队转变为可以自助方式配置基础设施。这包括文档的统一性以创建单一版本的事实。
- 一个工具来管理环境、基础设施和部署。

Kumar 说，Capillary 寻求的解决方案将允许用户“继续创建一个文档。你会说这是我的唯一真理来源。现在我用这种方式继续做所有这些。我始终以统一的方式做。”

简而言之，他想知道：“这是否是软件可以转换的东西，以管理您的环境、基础设施、部署等？”

## 构建基础设施蓝图

很多公司通过发现之旅来启动他们对[平台工程的采用](https://thenewstack.io/at-platformcon-for-realtor-com-success-is-driven-by-stories/)。 他们会问自己：我们拥有什么技术，谁拥有什么？

2020 年底，Capillary 开始与 Facets 合作共同构建一个解决方案，以帮助回答这个问题。 Capillary 选择 Facets 部分原因是它可以自动编录应用程序、数据库、缓存、队列和跨基础设施的存储，以及它们之间的依赖关系。 这种编录帮助创建了环境中架构应如何出现的部署蓝图。

![Facets.cloud蓝图设计器界面的示例](https://cdn.thenewstack.io/media/2023/09/4e0e35fe-facets.cloud-2-1-1024x786.png)
Facets的蓝图设计器提供了整个体系结构的高层次视图和已部署资源的详细信息。

“一旦你有了一个单一的蓝图，那么在启动基础设施方面所做的任何后续操作，在运行应用程序方面，在监控和管理方面所做的任何操作，所有这些都会成为从那里衍生出来的后续活动。” Kumar 说。

“这本质上是将你的整个环境和应用程序的蓝图结构带入标准化和良好可视性的部分。”

Capillary 选择 Facets 的另一个原因是它在全球运行了 10 个环境——3 个用于测试，其余用于生产。这意味着整个迁移到 Facets 的过程花了四到五个月才完成，以确保所有现有数据都已迁移。

团队特别花了大约三个月的时间将测试环境迁移过来，以确保一切正常工作。 Kumar 说，生产环境的迁移要快得多。

## 看到成果

到 2021 年中期，Kumar 的团队已经看到了一些明显的成果：

### 运维工单减少 95%。 

“我们通过 Facets 所能做的是，我们创建了一个自助服务环境，作为开发人员，如果你需要创建一个新的应用程序，你需要将其添加到目录中。” Kumar 说。 “你团队中的某个人，比如你的负责人或架构师，会批准它。 然后它自己启动。不需要 DevOps 团队参与。”

DevOps 团队不再参与日常软件启动。 现在，他们能够使用 6 个成员的 DevOps 团队在两个产品堆栈中运行约 15 个环境。

事实上，Capillary 将其 DevOps 团队重命名为“SRE 和开发者体验”，转向网站可靠性工程，并创建解决方案以支持其开发人员。

### 整体在线时间从 99.8% 提高到 99.99%。

“我们的环境稳定性基本上已经取得了质的飞跃，”Kumar 说。“我们的环境得到持续监控。你看到的任何故障基本上都会触发警报。你的备份，你的回退，都是非常标准化的。”

### 开发者生产力提高 20%。

“发生的最大的事情是，DevOps 团队的队列时间或等待时间不复存在，”Kumar 说。

现在工程运维也具有统一性，包括日志和监控，这进一步提高了[开发人员的生产力](https://thenewstack.io/can-devex-metrics-drive-developer-productivity/)。

“而且因为我们的发布是完全自动化的，发布的监控也是完全自动化的，”Kumar 说。

这意味着在过去两年中，Capillary 团队已经从每两周发布一次转变为现在每天发布一次。此外，他们转向了具有验证的自动化无人值守发布模式。现在，Kumar 说，“如果某些东西被破坏了，你会立即收到警报去处理它。”

随着新的产品的出现，首席技术官表示，Capillary 工程团队不断壮大，并变得更有效率。 2016 年，启动一个环境需要 64 个开发人周。现在，包括所有验证和稳定化在内，只需要 8 个开发人周。

他说，使用与 Facets 共同创建的蓝图，用户必须定义一个新的环境“将如何处理这种工作负载，因此需要这种容量。一旦你设置好了，环境启动就是全部自动化的。所以你可以节省很多时间。”

今年早些时候，Capillary 收购了另一家科技公司，这需要启动一个新的开发人员环境。工程团队能够在 Facets 内定义蓝图，并在两个半星期内启动了一个新的环境。

### 基础设施成本的更大可见性。

最后，三到四年前，Kumar 只能通过事后分析来监控基础设施成本，这导致响应延迟和成本泄漏。现在，他说，Facets 在审计方面提供了帮助，并使其更多地了解其基础设施的使用情况以及过度配置的位置。

Kumar 说，这些新功能引发了更多主动监控和 [CloudOps](https://thenewstack.io/what-makes-a-good-cloudops-organization/) 与 [FinOps](https://thenewstack.io/finops-the-why-what-and-how/)，“我可以更早地得到成本飙升的信号。”