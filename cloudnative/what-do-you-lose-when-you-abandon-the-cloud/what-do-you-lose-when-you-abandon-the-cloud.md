
<!--
title: 放弃云计算，你会失去什么？
cover: https://cdn.thenewstack.io/media/2024/12/ec61c850-what-do-you-lose-when-you-abandon-the-cloud.jpg
-->

云回迁似乎是解决高基础设施成本的方案，但在组织规模扩大时，这可能被证明是短视的。

> 译自 [What Do You Lose When You Abandon the Cloud?](https://thenewstack.io/what-do-you-lose-when-you-abandon-the-cloud/)，作者 Charles Humble。

[37signals](https://www.linkedin.com/posts/david-heinemeier-hansson-374b18221_our-cloud-exit-savings-will-now-top-ten-million-activity-7252755548859727874-k5V2/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)（[Basecamp](https://basecamp.com/)和[HEY](https://www.hey.com/)的母公司）和[GEICO](https://www.thestack.technology/warren-buffetts-geico-repatriates-work-from-the-cloud-continues-ambitious-infrastructure-overhaul/)的引人注目的举动引发了人们对云计算回迁——将工作负载从公共云迁移出去——的[renewed interest in](https://thenewstack.io/why-companies-are-ditching-the-cloud-the-rise-of-cloud-repatriation/)。当然，它们并非首例。[Dropbox](https://www.dropbox.com/enterprise)早在2016年就[undertook a similar journey](https://techcrunch.com/2017/09/15/why-dropbox-decided-to-drop-aws-and-build-its-own-infrastructure-and-network/)，因为他们发现这样做更具成本效益。但是[is cloud repatriation a growing trend](https://thenewstack.io/cloud-migration-regrets-should-you-repatriate/)？

[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)当然希望英国主要的竞争监管机构竞争与市场管理局（CMA）这么认为。在7月的一次听证会上，AWS在向CMA调查大型云提供商（如AWS、微软和谷歌）是否从事限制客户选择的反竞争行为时，[cited repatriation as a threat to its business](https://assets.publishing.service.gov.uk/media/66e7fa6910f8726dc23aa16a/240702-aws-hearing-summary.pdf)。

这很容易让人感到愤世嫉俗，但市场研究公司[IDC](https://www.idc.com/)的咨询和研究集团副总裁[Daniel Saroff](https://www.linkedin.com/in/daniel-saroff-9301991/)在一篇公司博客文章中写道，他[believes there are several factors driving the repatriation process](https://blogs.idc.com/2024/10/28/storm-clouds-ahead-missed-expectations-in-cloud-computing/)：成本超支；性能和延迟问题，技术和人工智能相关的工作负载在公共云环境中遇到瓶颈；以及安全和合规性问题，尤其是在数据隐私至关重要的行业（如金融和医疗保健）中。

虽然很容易将回迁想象成非此即彼，就像37signals和Dropbox那样，但事实要微妙得多。在硅谷风险投资公司[Andreessen Horowitz](https://a16z.com/) 2021年发布的一份关于云计算成本的报告中，[the authors stated that](https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/)，“在我们与之交谈的许多公司中，即使是最积极收回其工作负载的公司，仍然保留了10%到30%甚至更多的云资源。”

换句话说，我们现在看到的情况可能仅仅是日益成熟的标志，组织正在就特定工作负载的最佳部署位置做出明智的决策。但由于架构中的所有内容都是一组权衡，我们在采取此类行动之前应该权衡哪些因素呢？

## 云计算是否能节省您的资金？

迁移到云计算的一个有时被忽视的优势是，它允许您在需要时付费使用资源，例如，当新的客户上线时。支出从预先的资本支出（购买新机器以预期成功）转变为运营支出（按需支付额外的服务器）。

回到数据中心意味着相反的情况——根据增长预测提前购买机器。

这种区别有时与迁移到云计算可以节省资金的想法混淆，但这并不总是正确的。“我看到的许多回迁案例都是那些已经迁移并发现成本更高，现在完全感到幻灭的公司，”“绿色软件构建”的[co-author](https://thenewstack.io/want-to-create-software-sustainably-anne-curries-got-ideas/) [Anne Currie](https://thenewstack.io/author/annecurrie/)告诉The New Stack。

事实证明，在云计算中花钱很容易。即使是小规模的，我们许多人都收到过公共云提供商的账单，其中包含我们忘记仍在运行的内容；想象一下规模扩大后的情况。虽然许多初创公司依赖于通过信用卡轻松获取更多计算资源，但最终，自然会想要[stop giving a large chunk of your profits to a public cloud provider](https://thenewstack.io/finops/)。
然而，您需要权衡的是，能否在保持工作负载不变的情况下降低成本，或者运行自己的基础设施是否更便宜。通常情况下，如果您规模较大，后者更有可能——像eBay、[Google](https://cloud.google.com/?utm_content=inline+mention)和亚马逊这样的公司之所以这样做是有原因的。

对于我们其他人来说，关注更好的成本管理更有意义。处于云端的副作用是，技术和财务决策的拥有权从采购部门转移到了工程、架构和产品团队。这是实现更快创新的部分原因，但作为工程师，这也意味着运行我们系统的成本也转移到了我们这里，成为了我们职责的一部分。

为了有效地管理它，工程师需要准确的、理想情况下是实时的信息，以便了解资金的去向并能够做出明智的选择。这是另一个紧密反馈循环的例子，它使您能够更快地调整工作。

一个公认的管理方法是采用集中的[FinOps](https://thenewstack.io/finops-what-is-it-and-why-should-developers-sign-on/)实践，这可以为云的可变支出模式带来财务责任。这可以帮助各个产品团队利用云供应商提供的优惠，例如预留的深度折扣、固定费率定价以及批量和合同折扣。像37signals这样的工作负载，其资源需求是可以预测的，可以利用[承诺使用折扣](https://cloud.google.com/docs/cuds)来降低成本。

大多数云提供商还提供用于限制API使用、配额和预算的机制：

- 在对业务影响最小或没有影响的情况下，限制API使用是有意义的。
- 配额可用于设置限制资源部署的硬性限制。
- 可以为需要绝对使用限制的项目设置预算和警报。

采取这种方法最终可能比昂贵的回迁计划更具成本效益。

## 案例研究：Zynga的创新与成本

另一个需要权衡的是创新速度——来自云提供商和消费者的创新速度。

“云让您有机会快速搜索可能性空间——换句话说，就是创新，”云原生咨询公司[Container Solutions](https://thenewstack.io/container-solutions-cloud-migration-with-the-best-tools-and-the-right-culture/)的合伙人告诉The New Stack。“当您到达创新周期结束时，您会考虑优化，然后您会考虑重新平衡成本、效率和减少人员招聘。这就是我们看到37signals这样做的原因。”

了解一个值得注意的回迁逆转案例也很关键，那就是移动游戏公司[Zynga](https://www.zynga.com)，该公司早在2011年就构建了自己的zCloud基础设施。

该公司经历了爆炸式增长。“我于2009年7月加入Zynga，”顾问兼前CTO和CIO告诉The New Stack。“FarmVille在一个月前在AWS上推出。三个月内，我们的日活跃用户达到3300万。

“如果我们在自己的服务器上推出它，我们根本无法增长。我们没有足够的物理硬件或数据中心空间，而且我们也无法足够快地获得它们。”

然而，18个月后，Zynga开始遇到问题。有些问题是由适当强制的安全更新引起的。“我们有数千个实例，但员工非常有限，”Carroll说。“重新启动所有内容是一项艰巨的任务，而且我们的软件开发卫生状况不是很好，所以我们不知道如果我们重新启动实例，游戏是否会恢复。”

该公司还开始遇到容量不足的情况。“当然，我们不是AWS的唯一客户，所以我们不可能拥有他们推出的每个实例，但这给我们带来了问题，”Carroll说。

Zynga的首席执行官兼创始人决定公司需要构建自己的环境。这是一项巨大的工作。Zynga聘请了100名数据中心专家，制定了可以在其上运行自己云的特定硬件配置，并在不同位置构建了几个新的定制数据中心，以提供弹性和冗余。

通过这样做，该公司将成本降低了三分之二，这似乎是一个巨大的成功。然而，“大约三四年后，我们所有的设备从资本支出角度来看都已完全折旧，毫无价值，”Carroll说。“我们有超过40,000个实例，我们正在考虑如何更新所有设备。”

除此之外，公司业务也表现不佳，由于公司规模缩减，所有顶级数据中心专家都离职了。“我们既缺乏专业知识，也缺乏预算，而且游戏的设计初衷是为了应对爆炸式增长，却没有制定任何缩减规模的实际计划，”Carroll说。

Zynga决定转向AWS，在迁移回云的过程中关闭了一些游戏，并在租赁到期时关闭数据中心。这很艰难。“大约75%的游戏软件工程师都专注于关闭系统并迁移数据，”Carroll说。“这并不理想，但最终为我们节省了2.5亿到3.5亿美元的资本投资。”

这很可能挽救了公司，但即便如此，Carroll也表示，“成本节约实际上是最不重要的部分。它真正帮助我们做的是加速创新。”

Zynga的游戏使用了经典的三层架构：前端的Web服务器，[Memcached](https://thenewstack.io/how-pinterest-tuned-memcached-for-big-performance-gains/)作为缓存层，然后是后端的[NoSQL](https://thenewstack.io/sql-nosql-and-vectors-oh-my/)或[MySQL](https://thenewstack.io/oracle-support-for-mysql-5-7-ends-soon-key-upgrades-in-8-0/)用于持久化。“这是一个简单的例子，”Carroll承认，“但我们有数千台缓存服务器，并且我们想要实现一个需要新版Memcached的功能。这需要一个新版本的[libevent](https://libevent.org/)，而这又需要一个新版本的[Linux](https://thenewstack.io/linux/)。”

Zynga的工程师们不确定他们的技术栈是否能够承受这种变化，但是，“在AWS上，我们可以很快地启动一些Memcached实例，将它们轮换到服务器池中，并在几天内查看一切是否正常工作，”Carroll告诉TNS。

一旦确认更改成功，Zynga的工程师就可以启动新实例并将其替换。每一步都带来了巨大的效率提升，并且这种提升不断累积。

“我们从100台服务器减少到12台，但如果我们在自己的数据中心这样做，我们就必须购买所有这些新硬件才能进行A/B测试和蓝绿部署，”Carroll告诉我们。“这种实验能力是关键，这是我们在自己的设施中永远无法做到的。

“随着我们转向新的游戏和功能，我们可以快速行动，启动并测试它们。如果用户或玩家喜欢它们，就保留它们；如果不喜欢，就恢复到之前的版本。”


## 对招聘和容量规划的影响

Zynga的例子突出了其他一些权衡。需要考虑的一点是，如果您自己运行数据中心，就需要能够招聘合适的人才并留住他们。“这种人力专业知识几乎不可能复制，”Carroll说。

自己运行数据中心需要持续的容量规划。如果您从未做过这件事，或者已经很久没有做过这件事，那么它可能会出乎意料地充满挑战。您能否现实地预测您提前需要多少服务器？

那些记得过去情况的人会熟悉我们不得不应对的漫长的采购周期。购买一台新服务器，将其安装好，在其上安装所有必要的软件，并将其添加到集群中，可能需要数周甚至数月的时间；这肯定不是您可以一键完成的事情。

结果是，我们倾向于为了风险管理策略而大幅度地过度配置，最终导致大量机器闲置。这仍然会花费您的资金——您必须购买它们并支付运行和冷却它们的电费，即使它们没有运行工作负载。

这种情况也具有可持续性影响，因为服务器的静态功耗仍然很高；即使它处于空闲状态，它也会消耗电力，并且假设电力是由化石燃料产生的，它还会释放碳。


## 云后可持续性挑战

这并不意味着构建绿色软件的唯一方法是使用公共云（我已经[在会议演讲中论证了事实并非如此](https://www.conissaunce.com/presentations.html#writing-greener-software)），但是基础流程在公共云上无疑比在您自己的基础设施上更容易管理。

这些技术包括自动缩放和多租户技术，以将CPU利用率保持在50%到80%左右；将工作负载部署在电力主要来自可再生能源和/或核能的地方；以及使用[需求转移和整形技术](https://www.conissaunce.com/demand-shifting-and-shaping.html)在电力最清洁的时候运行计算密集型工作负载。

但这并非免费。“这是一种共享责任模型，”Currie 说。“如果你只是[迁移和转换](https://thenewstack.io/app-modernization-why-lift-and-shift-isnt-good-enough/)，它可能会更环保一些，但并不十分环保。如果你进行现代化改造并完全采用云原生技术，你可以获得一个比你可能在本地实现的更高效的系统。”

AWS、[Microsoft Azure](https://news.microsoft.com/?utm_content=inline+mention)和 Google Cloud 都拥有强大的可持续发展目标，并提供工具来评估你在其平台上的碳足迹（[客户碳足迹工具](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)、[Azure 排放影响仪表板](https://www.google.com/search?client=safari&rls=en&q=Azure+Emissions+Impact+Dashboard&ie=UTF-8&oe=UTF-8)和[碳足迹](https://cloud.google.com/carbon-footprint)）。[云碳足迹](https://www.cloudcarbonfootprint.org)是一个由[Thoughtworks](https://www.thoughtworks.com/)赞助的开源替代方案，可以测量、监控和减少你在公共云上的碳排放。

公共云为你提供了更广泛的工作负载可能部署位置，这意味着你可以使用诸如[Electricity Maps](https://app.electricitymaps.com/map/24h)之类的工具来识别具有更环保能源组合的位置，并将你的工作负载部署在那里；这比建设新的数据中心容易得多。你还可以考虑使用更先进的技术，例如[需求转移](https://www.conissaunce.com/demand-shifting-and-shaping.html)，在能源最环保的时间或地点执行更多计算密集型工作负载。

通过利用各种云提供的某些服务——特别是突发型实例、抢占式实例（在 Google Cloud 上称为“抢占式实例”）和无服务器服务，例如 Google Cloud Run、AWS Lambda 和 Azure Functions——你通常可以以更环保的方式设计应用程序，这在自己的数据中心中很难实现。

更广泛地说，你通常可以通过利用公共云提供的服务来充分利用公共云，但这意味着锁定，这对我们许多人来说是令人厌恶的。

“你想要做的是采用一个平台，它将带你走向全天候无碳电力，而你无需做任何事情，只需按照预期使用该平台即可，”Currie 说。“而你将无法自己做到这一点。”


## 云后安全挑战

围绕[安全](https://thenewstack.io/security/)还有一系列权衡。保持服务器更新并防止入侵是一项耗时的工作，大型云提供商在这方面经验丰富。仅仅[招聘和留住合格的人员来做这件事就很难](https://thenewstack.io/how-to-get-started-filling-3-4-million-cybersecurity-jobs/)。

云服务提供商很少报告安全漏洞，并理所当然地以其在数据安全方面的高标准而自豪。一个相关的问题是，作为一个私营公司，你将如何处理大量的数据主权规则？

在金融和医疗保健等行业，监管机构可能更倾向于使用私有数据中心。“当我还在一级银行工作时，担心的并不是客观上云比本地更不安全，”Miell 说。“更多的是监管机构对本地感到满意。这与客观风险无关，而是与监管机构对风险的认知有关。”

许多公司都遭受了云基础设施配置错误的影响。[2019 年 Capital One 丢失 1 亿用户记录](https://thenewstack.io/capital-ones-cloud-misconfiguration-woes-have-been-an-industry-wide-fear/)就是一个例子。“问题是你可以在云中按下这些红色的按钮，例如‘向全世界开放我的 S3 存储桶’，”Miell 说。“云提供商已经做了缓解工作，但仍然存在这种事件发生并让你非常尴尬的挥之不去的恐惧。”

还有一些云实际上并不适合的特定工作负载。例如，如果你需要完全控制你的网络，那么云并不理想。


## 到底什么是云原生？

你可能已经意识到，这是一项相当微妙的工作；许多这些权衡是重叠和交叉的。另一件需要考虑的事情是，有可能获得公共云的所有优势，“云原生”，并且仍然在自己的数据中心运行。

“如果你使用开源工具并构建合适的平台，你可以在本地拥有云原生软件，”Miell 告诉 TNS。“你无需在云上才能成为云原生。”

在某种程度上，这就是像[SoftIron](https://softiron.com)和[Oxide](https://oxide.computer)这样的初创公司试图利用的。
然而，Carroll对此表示怀疑。“除非你是云服务提供商，否则你没有理由投资于你需要的个人硬件、网络和存储。你在错误的地方投资。”

对于Zynga，他补充道，放弃云计算的决定最终是错误的。“因为成本、对创新的影响以及造成的损害。当时这看起来像是正确的决定，因为没有人看得足够远。”
