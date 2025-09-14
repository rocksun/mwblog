
<!--
title: 分布式Postgres如何解决云的高可用性问题
cover: https://cdn.thenewstack.io/media/2025/09/5da24611-distributed-postgres-cloud-ha.jpg
summary: 企业因应用停机遭受巨大损失。开源软件和云基础设施的普及加剧了高可用性需求。pgEdge 通过分布式 Postgres 架构，支持多主多区域部署，解决数据同步和冲突问题，确保应用高可用性和低延迟。
-->

企业因应用停机遭受巨大损失。开源软件和云基础设施的普及加剧了高可用性需求。pgEdge 通过分布式 Postgres 架构，支持多主多区域部署，解决数据同步和冲突问题，确保应用高可用性和低延迟。

> 译自：[How Distributed Postgres Solves Cloud's High-Availability Problem](https://thenewstack.io/how-distributed-postgres-solves-clouds-high-availability-problem/)
> 
> 作者：Meredith Shubel

应用程序的可用性和停机时间是任何组织都不能忽视的问题。

虽然具体数字因用例而异，但大方向很明确：应用程序停机几乎总是意味着金钱损失。根据[牛津经济研究院](https://www.oxfordeconomics.com/resource/the-hidden-costs-of-downtime-the-400b-problem-facing-the-global-2000/)的研究，计划外停机每年给全球2000强企业造成4000亿美元的损失，平均每家公司每年损失2亿美元。

而这仅仅是个开始。根据pgEdge对任务关键型应用中[PostgreSQL](https://roadmap.sh/postgresql-dba)进行的一项新的[调查](https://www.pgedge.com/press-releases/new-survey-shows-strong-demand-for-high-availability-as-businesses-increasingly-use-postgresql-in-mission-critical-applications-and-to-alleviate-cloud-outage-concerns)显示，当企业超过最大停机时间目标时，56%的企业会经历业务运营延迟，49%的企业会遇到支持量增加或客户投诉，47%的企业需要紧急技术修复，33%的企业会损失收入或看到交易延迟。

[pgEdge](https://thenewstack.io/startup-pgedge-tackles-the-distributed-edge-with-postgres/)的联合创始人兼首席执行官Phillip Merrick在一次采访中解释说，对于医疗保健、政府或金融服务（如投资管理）等高风险组织来说，风险甚至[更大](https://thenewstack.io/distributed-postgres-high-availability-for-mission-critical-apps)。

Merrick说：“如果您用来管理股票头寸的交易平台宕机哪怕五分钟，都可能导致数百万美元的损失。”

当然，并非每次中断都一定需要恐慌。

Merrick指出：“有些应用程序，有些业务……或许可以容忍半小时或一小时的停机时间。但你必须问自己：‘鉴于我构建应用程序的方式，以及它们运行的位置，我发生停机的可能性有多大？’”

而这正是许多企业遇到麻烦的地方。

## 为什么开源需要高可用性策略

在过去的二十年中，Merrick注意到企业软件领域正在发生巨大的变化。

首先是从本地部署到云基础设施的稳定转变。与此同时，企业越来越依赖开源软件，Merrick认为，与选择传统供应商相比，选择开源可以带来更大的创新机会和更低的成本。

转向云基础设施和开源软件代表了行业内一次巨大的变革，但这是一个渐进的、几乎难以察觉的转变。

他回忆说：“早期的云使用实际上是开发人员用他们的信用卡购买云订阅。然后，在不知不觉中，您实际上拥有了一些在云中运行的关键应用程序。”

开源软件也出现了类似的趋势。随着公司开始使用更多的开源组件，他们最终意识到他们正在依赖开源软件来处理许多关键应用程序，但他们没有高可用性策略。

## 单一云区域的停机风险

Merrick指出：“如果你考虑那些依赖云提供商的公司，你的应用程序通常只会驻留在单个区域中。”

这听起来可能没什么问题，但是当你考虑到云提供商对重大、持续数小时的中断并不陌生时，这是一个令人恐惧的——或者至少是令人担忧的前景。

在对金融服务、软件、计算和制造业等拥有500多名员工的组织中的212名IT决策者进行调查后，pgEdge发现，21%的受访者在过去一年中经历过云区域故障。

它们当然登上了新闻头条。[2021年AWS东京中断](https://thenewstack.io/what-you-can-learn-from-the-aws-tokyo-outage/)、[2023年Google Cloud中断](https://thenewstack.io/google-cloud-services-hit-by-outage-in-paris/)和[2023年AWS US-East-1中断](https://www.sdxcentral.com/news/aws-us-east-1-region-outage-downed-many-websites-now-resolved/)只是其中几个例子。今年6月，[Google Cloud再次出现中断](https://techcrunch.com/2025/06/12/google-cloud-outage-brings-down-a-lot-of-the-internet/)，导致服务中断数小时，并对包括Cloudflare和OpenAI在内的下游供应商产生连锁反应。

因此，毫不奇怪，四分之一的IT领导者[告诉Splunk](https://www.splunk.com/en_us/form/digital-resilience-pays-off.html)，他们认为基础设施中断是其组织最可能的 disruption 来源。

不幸的是，组织可以预期进一步的中断，仅仅“因为云提供商构建云的方式。默认情况下是将你的应用程序放在一个区域中，”Merrick说。

危险就在于此。当组织将应用程序绑定到单个区域时，它们会引入单点故障，损害可用性，并为中断和代价高昂的停机时间带来风险。

Merrick说：“很多企业可能还没有完全想清楚这一点，或者真的没有量化这些风险对他们的业务的实际影响。对于任何关键应用程序停机会产生重大成本的企业来说，高可用性都是一个问题。每个企业都需要了解并量化停机时间对他们的意义，然后采取相应的行动。”

## 高可用性：日益增长的担忧

当然，停机时间和可用性的困境并不是什么新鲜事，“但这是每个人越来越关注的事情，”Merrick强调说。

这很大程度上是由于消费者用户造成的，他们现在甚至会谴责在滚动Instagram或其他通用应用程序时出现的轻微延迟。对速度的需求已经演变为对跨领域的延迟或停机的近乎零容忍：“我们希望我们使用的应用程序始终开启并且始终可用，”Merrick强调说。

虽然近年来最终用户的期望有所提高，但许多行业已经意识到了高可用性的重要性。

Merrick补充说：“在某些行业——医疗保健、金融服务、某些政府服务——它们根本不能停机。情况一直如此。”

尽管如此，这并不意味着这些行业有有效的策略来最大限度地减少停机时间并确保高可用性。

许多组织（例如银行）继续依赖计划内维护，在所谓的不方便的时间（例如美国东部时间凌晨2点到5点之间）将系统脱机几个小时。

但Merrick认为，“计划内维护应该成为过去。”

首先，日益全球化的社区意味着“非工作时间”不再真正存在。无论是提供任务关键型服务还是更商业化的服务，企业都应该全天候运行。

Merrick说：“你应该能够进行维护——升级软件，应用最新的安全补丁——而无需将应用程序关闭以支持维护。”

现实情况是，很多企业还没有做到这一点，尽管pgEdge最近的调查中，79%的受访者表示他们正在评估或考虑用于PostgreSQL环境的分布式或专用高可用性产品。

## 跨区域保持数据同步的挑战

无论是组织处理他们控制的物理数据中心，还是云提供商拥有的云区域，跨区域保持数据同步一直是一个挑战——尤其是对于Postgres而言，Postgres是事务性工作负载的广泛采用的关系数据库，最初并非为分布式部署而设计。

正如Merrick解释的那样，“除非两个地方的数据库都持续保持同步，否则你无法从一个区域即时故障转移到另一个区域。”

也就是说，除非你选择分布式[多主](https://www.pgedge.com/solutions/benefit/multi-master)架构，该架构允许多个节点（每个节点都能够进行读写）在区域之间持续保持同步。这样，如果一个节点甚至整个区域脱机，应用程序也可以继续运行，并且 disruption 最小。

如果情况确实如此，那么继续依赖传统的单区域方法的原因是什么？

一个犹豫的原因是对多主架构复杂性的认知。Merrick说：“人们的误解是它太难了。”

多区域策略也是如此，他承认“除非你拥有分布式数据库，否则为多区域架构进行设计实际上是困难的。”

尽管如此，尽管对复杂性有所保留，但这并不意味着公司没有关注它。例如，在最近的pgEdge调查中，几乎一半（47%）的跨多个云区域部署应用程序的组织表示，他们对多主复制感兴趣。

Merrick回忆说：“我知道有几位首席技术官将多区域故障转移作为产品路线图中的一项，但他们只是认为这太难了，因此它一直是一项非常重要但在路线图上排名较低的项目。”

Merrick认为情况不必如此——至少现在不必如此。

## pgEdge如何使多主Postgres成为可能

Postgres是一个强大的数据库，因其可靠性和灵活性而广受赞誉，但它没有开箱即用的高可用性分布式选项。

这正是pgEdge旨在通过其完全开源、完全基于Postgres的软件解决的问题。

pgEdge提供[分布式Postgres架构](https://www.pgedge.com/solutions/benefit/postgresql-high-availability)，支持多主、多区域部署，以确保高可用性和低延迟，并消除单区域云中断带来的代价高昂的风险。

Merrick说，这部分是由于pgEdge能够在节点之间进行复制，在一个位置所做的更改会自动实时同步到其他位置。

值得注意的是，这种复制不需要手动干预，Merrick将其列为工程团队经常关注的问题。

“我们合作的一些人过去曾尝试使用Postgres自己的逻辑复制，但它需要大量的人工干预。”

他说，pgEdge并非如此。

但是，如果两个不同位置的编写器尝试同时更新相同的数据怎么办？

这时，冲突解决就发挥作用了，pgEdge通过一组预定义的规则来解决冲突——简而言之，第二次写入获胜。对于不能应用此经验法则的情况，pgEdge使用“冲突避免”来防止最可能导致冲突的操作。

他解释说：“在冲突解决和冲突避免之间，不需要手动干预”，这对于那些对[分布式多主Postgres架构](https://www.pgedge.com/solutions/benefit/multi-master)感到好奇，但对其进行切换所需的工作表示怀疑的团队来说是一个胜利。

## 分布式多主架构的未来

凭借对多主、多区域部署的支持以及内置的冲突解决和避免，pgEdge旨在为组织提供一致的高可用性，从而提供更无缝的用户体验并减少破坏性停机时间。

一家[全球投资管理公司](https://www.google.com/url?q=https://a.storyblok.com/f/187930/x/d55b4b196d/financial_services_usecase.pdf&sa=D&source=docs&ust=1757014017919370&usg=AOvVaw3bX8TxPf6c1PBH3oAUI0HG)已经在看到好处。

该公司跨越多个地理区域、资产类别和时间框架，拥有1000多名员工和200亿美元的管理资产，需要高可用性来支持其高容量交易平台。借助pgEdge，它可以获得一个完全基于标准Postgres的开源解决方案，该解决方案提供高可用性功能和逻辑复制功能，可实现接近零停机的升级、提高性能并消除单点故障——随着云中断继续威胁服务连续性，这个问题日益棘手。

展望金融领域之外，Merrick认为各行业对分布式多主架构的需求不断增长。

在对AI应用程序进行了多年的实验之后，“公司正在实际推出它们，并使它们可供员工和客户使用，有时是在全球范围内，”他观察到。意识到这种转变将需要新的策略来确保始终开启、始终可用的数据访问、低延迟和最小的停机时间。

他补充说：“事实证明，pgEdge非常适合需要全球可用的AI应用程序。”

[详细了解](https://www.pgedge.com/PostgresHAsurvey)多主[分布式Postgres](https://www.pgedge.com/products/what-is-pgedge)如何解决高可用性和低延迟挑战，从而为全球应用程序提供支持。