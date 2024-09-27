# 开源分叉为何成为热门话题

![关于开源分叉为何成为热门话题的特色图片](https://cdn.thenewstack.io/media/2024/09/23c536f4-fork-1280701_1280-1024x627.jpg)

[Valkey](https://thenewstack.io/linux-foundation-forks-the-open-source-redis-as-valkey/), [OpenTofu](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/), 和 [OpenBao](https://thenewstack.io/meet-openbao-an-open-source-fork-of-hashicorp-vault/) 是由 Linux 基金会托管的开源软件项目分叉的名称。这些分叉是在去年由开源软件项目的商业赞助商（从开源许可证转向专有许可证）引发的；HashiCorp 被 OpenTofu、OpenBao 和 Redis Labs 分叉为 Valkey。后者在过去几周内一直占据着科技媒体的头条。

创建这些和其他分叉，例如 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 作为 Elastic 的 ElasticSearch 用户的 OpenSearch 分叉，将开源软件中“社区控制的终极武器”推到了前台，并引发了截然不同的讨论。它还看到了分叉的新基础和潜在影响，值得探索和理解。与开源软件的许多领域一样，分叉涉及许多细微差别，这些变化需要深入理解。

## 什么是分叉？

[分叉](https://thenewstack.io/open-source-projects-fork/) 允许开发人员“提升和转移”开源代码库，在特定时间创建新的独立项目版本。通过在代码库中创建新分支，此分叉可以作为具有自身愿景、治理和团队的独立项目的基石，可能朝着与原始项目完全不同的方向发展。将创建新的项目名称，因为开源软件许可证通常不会授予名称或商标的权利。商业赞助商通过商标政策将名称提供给社区的做法是可以接受的，但仅限于他们认可的代码库，而不是分叉。

新项目将希望建立其独特的身份，并与旧项目区分开来。

分叉不是专有软件的选项，因为即使代码库可访问，它也不符合开源软件标准。在专有系统中，修改、重新分发或创建代码新版本的必要权限通常受到限制。

## 什么是开源软件？

代码库必须满足 [开源定义 (OSD)](https://opensource.org/osd) 中概述的十项标准，才能被视为开源软件，该标准由 [开源计划](https://opensource.org/) 维护。其中，基本要求（第 5 和第 6 点）确保任何人都可以将代码用于任何目的，而不会对个人或领域有任何限制。这种不受限制的访问使无摩擦分发成为可能，这是开源的核心原则，它推动了广泛的采用。截至 2023 年，[根据 Synopsis 的说法](https://www.synopsys.com/software-integrity/resources/analyst-reports/open-source-security-risk-analysis.html)，96% 的所有软件都包含开源依赖项，这突出了开源在现代软件开发中的重要性。

开源的自由流动使设备制造商能够自信地上传和分发，因为他们通过满足许可证要求（包括代码作者的归属和使源 [代码可用](https://thenewstack.io/opentofu-1-6-general-availability-open-source-infrastructure-as-code/)），他们不需要额外的权限、进一步的许可证或以后支付版税。它增强了对代码的信心。

如果软件许可证不符合 OSD，这通常是由于对谁可以使用代码或如何使用代码的道德或商业限制。如果商业实体将项目从开源软件许可证转移到专有许可证，这通常是由于增加了商业限制，而提高商业赞助商的收入是许可证变更背后的驱动力。

这种代码实际上是第三种代码。从技术上讲，它是专有的，但由于其源代码是公开的，因此后一个事实可能会导致它与开源软件混淆，尤其是在其过去版本被许可为开源的情况下。被称为“公共源代码”或“分布式源代码”，最近也尝试在“公平源代码”品牌下建立它。关键是理解它不是开源，不要误导。如果分发者误导为开源，则将其描述为“开源洗白”，即暗示代码分发者通过其自由流动满足开源标准，而实际上并非如此。

## 改变未来，而不是过去

### 翻译者回应

### EDITOR'S RESPONSE
未来版本可能会在不同的专有许可下发布，但分叉前的代码库始终可以在应用于它们的原始开源许可下获得。它们的发布者可能不会收回该许可。

代码库可能被分叉的最后一点是开源许可版本中的最后一次提交。当[HashiCorp 向 Linux 基金会发送了一封信](https://thenewstack.io/opentofu-vs-hashicorp-takes-center-stage-at-open-source-summit/) 声称 LF 侵犯了 [OpenTofu] 的版权时，他们的[声明很快就被撤回](https://thenewstack.io/closure-is-open-source-licensing-suddenly-unsustainable/)，因为代码库的公共存储库证明了相关代码是在分叉之前。

## 社区控制的历史性武器

在开源软件社区中，分叉长期以来一直是与项目相关的社区控制的终极武器。分叉允许社区控制其领导层，正如过去 Sun 和 [Matrix](https://techcrunch.com/2023/11/06/decentralized-communication-protocol-matrix-shifts-to-less-permissive-agpl-open-source-license/) 都经历了社区分叉一样。

从历史上看，分叉赋予了开源项目的社区权力，如果其领导层与社区脱节或做出社区大部分成员不喜欢的决定，他们可以构建第二个版本。社区分叉使不满的社区能够继续前进，扭转了不受欢迎的项目领导层继续其所选方向的决定。这种能力仍然是社区的重要工具。

## 商业赞助商和分叉的新世界

在过去几年中，商业实体从 [开源许可](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/) 转变几乎已经成为常态。2018 年 Redis Labs、2019 年 [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention)、2020 年 ElasticSearch 和 2024 年开源典范 HashiCorp 的许可证变更引发的社区愤怒已经消退，Cockroach 在 2024 年的变更只引起了人们的抱怨：“又来了”。

这些公司通常被称为“单一供应商产品”，它们通常只有有限的社区来反对决定改变项目的许可证。它们可能在其开源代码库旁边运行“开源核心业务模型”。这利用开源基础产品吸引用户，然后签订合同以获得采用代码库的某种形式的企业版。作为用户，如果您想探索项目分叉的可能性，评估项目社区健康状况可能有助于作为指标。例如，员工以外的贡献者很少的公司似乎更有可能成为变更的候选者。

由于其自由流动，开源软件能够以与普遍性潜力相一致的速度被采用并成为事实上的标准。再加上通过标准许可证在广泛使用的公共存储库中进行分发，软件工程师可以将代码引入他们的公司，而无需法律、采购或财务审批。从历史上看，这些 [风险阻碍软件](https://thenewstack.io/navigating-open-source-software-risks-whose-job-is-it-anyway/) 采用的守门人。如今，由于开源的存在，合同无法管理风险。它应该由软件策略来处理，没有或没有良好软件策略的公司，以及没有工程师遵循的流程来支持该策略的公司，都没有适当地管理风险。

由于特定公司的行为，分叉在过去五年多时间里变得至关重要。这些公司包括 Sun、Neo4J、Redis Labs、MongoDB、Elastic、[Confluent](https://www.confluent.io/?utm_content=inline+mention)、HashiCorp 和 Cockroach。它们已经从最初设置为开源软件的特定项目的开源许可证转向专有许可证。

这种公司进行变更的趋势导致了一种模式，即最初的社区愤怒和反弹随着时间的推移而变得正常化。开源组织的创始人抱怨说，投资者现在会问“何时，而不是是否”他们会将 [代码转换为专有](https://thenewstack.io/synopsys-rapid-scan-can-now-security-check-proprietary-code/) 模型。

这产生了两种结果：商业赞助商有效地分叉了他们的代码库，以及用户而不是社区分叉了现有的开源代码库。
这种情况发生在 AWS 对 Elastic 的 ElasticSearch 许可证变更做出反应时，该变更导致 ElasticSearch 将专有代码和开源代码混合在一起。通过 [构建自己的 OpenSearch 分支](https://thenewstack.io/this-week-in-programming-aws-completes-elasticsearch-fork-with-opensearch/)，一个大型且可能更强大的商业用户获取了一个规模较小但成功的开源公司的代码库并对其进行了分支。具有讽刺意味的是，Elastic、MongoDB 等公司指责云公司，尤其是 AWS，窃取了他们的代码，而这种行为正是导致许可证变更的原因。Pivotal 的 James Watters 说：“今天你拥有一个企业，明天你就在云端拥有一个功能。”

OpenSearch 分支在几年后仍然存在并且相对成功。然而，Elastic 最近将其代码恢复到开源许可证（更严格的 AGPL，旨在将版权应用于没有分发的代码）下。它看到了与 AWS 关系的转变，这是其基础。这个特定的分支故事可能还没有结束。

在这种情况下，一个拥有磨损和所有权的用户必须获取供应商的代码库并使用内置的分支运行它。虽然围绕此行为的权利和错误存在伦理争议，但 AWS 在分支方面的行为肯定没有违反任何许可证。作为开源项目延续的一部分，Elastic 可以说对其产品进行了分支。相比之下，AWS 尽管 Elastic 拥有 ElasticSearch 的名称，但仍然维护着原始的开源项目，尽管名称发生了变化，这意味着原始项目更改了名称。ElastiSearch 的名称所有权及其使用可能违反商标，这也导致了显然已经解决的商标诉讼。

然而，重要的是，在使用分支方面，权力平衡发生了明显的变化。这不是分支变化故事的结束。

## 成功的分支
在分支之后，开源社区中的赢家不是软件的财务成功版本，而是代码丰富或采用最多的版本，即成功的项目是根据其代码库的质量和项目的利用率来衡量的。一个很好的例子是 MariaDB，它是从 MySQL 分支出来的。GitHub 星星往往与使用情况相关，MySQL 在 GitHub 上拥有超过 10,000 颗星星，而 MariaDB 只有 5,000 多颗。但 MariaDB 拥有近 400 位贡献者，而 MySQL 只有 100 多位，因此拥有社区的力量。

重点不在于产生的收入，尽管一些商业实体（可能是开源项目的先前商业赞助商）可能会继续关注他们在更改许可证后产生的收入，并且他们很快就会说他们已经继续——就像他们在项目分支发生之前一样——赚钱。他们可能会认为自己不受许可证变更和分支的影响，并认为自己是赢家。谁知道他们是否比他们没有更改许可证时更成功或更不成功？我们永远不会知道。

就像上周的 Redis 一样，他们经常争辩说，客户并不关心他们是否使用开源软件，并以他们持续的商业成功作为依据。MongoDB 的首席执行官甚至将使用开源软件描述为“营销工具”。这种方法被称为“诱饵和转换”。软件选项最初以开源形式提供（诱饵），但商业赞助商最终将许可证更改为专有（转换）。

构建和维护分支的成本和时间投入以及随之而来的挑战，造成了其历史成功率低下的根本原因。然而，[Linux 基金会的 Valkey 分支](https://thenewstack.io/linux-foundation-adopting-terraform-fork-provokes-ire-of-hashicorp-ceo/) 可能是分支发生另一转变和新事物曙光的证据。

## 分支的进一步转变？
[Percona](https://www.percona.com/?utm_content=inline+mention) 最近发布的一份报告表明，70% 的用户积极寻求替代方案，因为 Redis Labs 改变了许可证并放弃了开源模式。他们还发现，在接受调查的人中，有 75% 正在测试、考虑或已经采用了 [Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/) 分支。将此进行情境化可能会有所帮助。

正如 Redmonk 的 Stephen O’Grady 指出，Valkey 分支从技术和参与角度（包括 AWS 和 Google 等巨头参与分支）的创建速度（8 天）被认为是 [成功分支创建](https://redmonk.com/sogrady/2024/07/16/post-valkey-world/) 容易程度发生潜在转变的标志。它还增加了分支成功率（以用户衡量）的可能性。这种分支的使用方式是开源“诱饵和转换”方法的致命一击吗？

**结论**
像 Redis 这样的公司声称，云公司的“掠夺式开采”迫使他们放弃开源。从开源软件的角度来看，如果不是从道德和反垄断的角度来看，云公司将开源软件商业化的行为并没有违反开源许可，并且遵循了开源的核心原则——任何人都可以将代码用于任何目的。Redis、Elastic、Cockroach、MongoDB 等公司并没有被迫选择开源许可。他们主动选择开源，并利用开源带来的规模化采用和客户参与来建立自己的客户群。

从他们最初的开源许可转向其他许可可能随着时间的推移而变得正常化，但仍然是背叛了开源社区信任的行为，无论参与者是谁，并且仍然是背叛开源原则的行为。从像 Redis 这样的小型开源公司的角度来看，Valkey 分支可能不是由一群叛军创建的，而是由“[死亡之星](https://www.computing.co.uk/news/4358678/database-dust-redis-users-switching-valkey)”创建的。Redis 可能只是在为用户和社区厌倦了“诱饵和转换”方法而付出代价。

开源不是营销工具。它是终生的。

Valkey 分支可能证实了社区选择分叉是针对某些提供商对开源的“诱饵和转换”方法的完美反击。如今，社区背后有一些大公司。也许在未来，公司会意识到开源不是商业模式，并在开源之前三思而后行——如果他们不是为了长远利益。

*特别感谢 Stephen Walli、Liz Rice 和 Dawn Foster 的意见。*

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。