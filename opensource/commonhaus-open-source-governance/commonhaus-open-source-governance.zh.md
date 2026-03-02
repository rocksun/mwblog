**2024年，一个后门被发现隐藏在** [**XZ Utils**](https://www.youtube.com/watch?v=9NUOiL48hbo&t=2072s) 中，这是一个嵌入在许多流行Linux发行版中的压缩工具。这个后门本可以赋予黑客对全球数百万系统完整的管理控制权。它是由项目负责人和恶意行为者 [Jia Tan](https://www.wired.com/story/jia-tan-xz-backdoor/) 植入该工具的。

这个后门或多或少是偶然被发现的。一位名叫Andres Freund的微软工程师，在Debian上的远程连接协议SSH中发现了一个奇怪的延迟，对此感到不解。

Tan于2021年11月首次以GitHub用户名JiaT75出现，为其他开源项目做贡献。到2023年1月，他们的代码被集成到XZ Utils中。在接下来的一年里，他们 [逐渐接管了这个项目](https://www.akamai.com/blog/security-research/critical-linux-backdoor-xz-utils-discovered-what-to-know#:~:text=to%20action%20items-,Backstory,-XZ%20Utils%2C%20and)，从Lasse Collin手中接过，Collin是一位精力耗尽、感到无人支持和孤立的独立维护者。

尽管安全研究人员和记者进行了大量调查，但Tan的真实身份从未被明确揭露。许多分析师怀疑是国家支持的行为者，矛头经常指向俄罗斯或中国。Collin曾收到几封用户抱怨更新缓慢的电子邮件。这似乎很可能是同一次攻击的一部分，目的是向Collin施压，让他交出控制权。

对于 [Erin Schnabel](https://www.linkedin.com/in/erinschnabel/)，[Commonhaus Foundation](https://www.commonhaus.org) 的联合创始人来说，那一刻至今仍让她难以释怀。与其他开源组织一样，Commonhaus关注治理文书工作和法律框架。但它也希望确保下一位精疲力尽的维护者能在为时已晚之前找到人求助。

Commonhaus是一个两年前由Schnabel与Ken Finnigan和Cesar Saavedra共同创立的非营利组织。他们正试图解决开源软件中根深蒂固的问题。

“当我在思考基金会想做什么时，很大程度上是，我能做些什么来造福所有人？” Schnabel告诉 *The New Stack*。“但我想做的一部分是为那些原本没有归属的独立维护者提供一个更好的家。我心里想着这些独立维护者，因为我觉得他们最需要支持。”

2024年，Commonhaus在成立时，Schnabel [强调](https://thenewstack.io/commonhaus-foundation-launches-at-critical-time-for-oss/) 该组织倡导一种非传统方法，优先考虑继任规划、最小化治理以及为成员项目提供经济援助，包括无需寻求个人非营利组织地位即可接受捐赠的能力。

这一策略已证明颇受欢迎，基金会在2025年期间，其 [旗下项目数量](https://www.commonhaus.org/#our-projects) 几乎翻了一番，从14个增加到25个。项目包括Debezium、Hibernate、JReleaser、Quarkus、SDKMAN!、SlateDB和WildFly。Quarkus的竞争对手 [Micronaut是最新加入的](https://micronaut.io/2026/01/12/micronaut-announces-plans-to-join-the-commonhaus-foundation/)，目前正在进行入职流程。

## 打破常规

Commonhaus的投票程序旨在让项目负责人能够轻松影响政策的运作方式。在基金会成立的第一年，Schnabel研究了各种议会投票程序，并最终确定了 [Martha’s Rules](https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1825&context=sociologyfacpub#:~:text=In%20their%20study%20of%20consensus,issues%20in%20large%20group%20meetings.) 的改编版本。Martha’s Rules与英国的患者安全倡议“Martha’s Rule”不同，它是在20世纪70年代由威斯康星州麦迪逊的一个住房合作社开发的。这是一种五步、基于共识的替代Robert’s Rules of Order的方法，旨在实现更高效、协作的会议，通过允许“意向”投票来确定是否需要耗时的完全共识，从而加快决策速度。

> “我希望每个项目的运营者都能‘开自己的车’，但我确实要求透明度。开发者讨厌文书工作，所以我与他们核对，确保他们将决策流程记录下来……”

Commonhaus使用 [GitHub Discussions](https://docs.github.com/en/discussions) 的点赞/点踩机制进行意向投票，并且只在存在异议时才开启讨论。“这使得参与变得容易，”Schnabel说。“你不需要回复邮件列表，也没有人需要统计回复，因为它会自动发生。参与度很好，因为它摩擦小。”

维持这种精神并非偶然，正如 [SDKMAN!](https://sdkman.io) 的负责人 [Marco Vermeulen](https://www.linkedin.com/in/marco-vermeulen-1645421/) 告诉 *The New Stack* 的那样。“Erin [Schnabel] 极具前瞻性。她在这个领域工作了很长时间，并且她也曾站在另一边，所以她了解它是如何运作的，”他说。

随着基金会的发展，其非传统的精神依然存在：“在其他基金会中，投票和决策都有一些惯例，我试图打破这些惯例，”Schnabel在接受 *The New Stack* 采访时表示。

## 谁来照顾那些关心开源的人？

Commonhaus在设计上采用了一套与Apache或Cloud Native Computing Foundation相比更为轻量级的流程，这更适合成熟的项目和维护者。“我希望每个项目的运营者都能‘开自己的车’，”Schnabel告诉我，“但我确实要求透明度。开发者讨厌文书工作，所以我与他们核对，确保他们将决策流程记录下来，即使那只是一个赤裸裸的信息，表明‘我是终身仁慈的独裁者；所有决定都由我通过。’”

基金会提供了一份功能性的行为准则，并在发生争议时介入。“如果你是一个仁慈的独裁者，而有人不同意你，那么这种申诉可以提交给基金会，我们可以帮助解决，”她解释说。

需要调解的最常见问题是性格差异和沟通问题。“在这个神经多样性行为的世界里，文本沟通带来了最大的挑战，”她说。特别是对于独立维护者，基金会提供了宝贵的支持。

Schnabel希望在项目负责人之间建立辅导和指导机制，以帮助经验不足的维护者感到更有联系——这是从XZ Utils事件中吸取的教训，当时上述维护者正在挣扎，显然需要额外支持。

Commonhaus的方法并非唯一选择。“例如，GitHub有一个很棒的维护者社区，”Schnabel说。“我认为我们看到越来越多这样的情况，因为人们越来越意识到维护者感到孤立是导致倦怠的一个巨大因素。”

在导致倦怠的其他因素方面进展较少，尽管这仍然是Schnabel的首要任务，她目前关注的是降低 [巴士系数](https://activecollab.com/learn/glossary/bus-factor)。“我们鼓励独立维护者培养替代者，将凭据存储在1Password中，拥有良好的文档等。我们较大的项目已经这样做了。”

继任计划是 [JReleaser](https://jreleaser.org) 项目负责人 [Andres Almiray](https://andresalmiray.com) 选择与Commonhaus合作的一个主要原因。JReleaser是一个发布自动化工具，旨在简化跨多个包管理器（包括Homebrew、Scoop、Chocolatey和Snapcraft）创建发布和发布工件。它支持任何项目，无论源语言（Java、Go、Node、Rust、Perl、Python、C/C++、C#、Elixir、Haskell等），尽管它为基于Java的项目提供了额外的好处。它也是Commonhaus的创始项目之一。

“这是我从事这个项目的第六年，我仍然充满活力，但将来我可能想做其他事情，其他人将不得不接手，”Almiray告诉 *The New Stack*。“Commonhaus帮助我培养下一代开发者，他们最终将接管。”

> “Commonhaus帮助我培养下一代开发者，他们最终将接管。”

Schnabel还在寻求解决项目旧版生命周期结束分支的CVE支持和维护问题。“我想建立一个项目，让独立维护者能够专注于前瞻性开发，并减轻专注于CVE的压力，”她说。她鼓励项目对CVE以及是否处理受禁代码制定明确政策。

“严格来说，独立维护者不需要处理禁运问题，”她说。“如果你对此透明，一家有紧迫感的公司会意识到，如果他们想快速解决问题，就必须做出贡献。”

## 更多自由，更多责任

自推出以来，Commonhaus一直非常关注Java。“我想吸引更多非Java项目，”Schnabel告诉我，“但我们目前几乎所有项目都是Java，而且我的网络也非常以Java为导向。”

[SlateDB](https://slatedb.io) 是一个基于对象存储的嵌入式键值数据库，是一个例外；它用Rust编写。基金会倡导的轻量级方法使其成为经验丰富的开源维护者（如其负责人 [Chris Riccomini](https://www.linkedin.com/in/riccomini/)）的天然家园。他使用开源项目超过30年，并为其中约20个项目做出了贡献。他第一次与开源基金会互动是与Apache，当时他于2008年开始使用Apache Hadoop。从那时起，他为许多Apache项目做出了贡献，创建了Apache Samza，并担任Apache Airflow的导师和项目倡导者。

“我建立SlateDB的时间与Commonhaus开始与几个不同的初创公司合作的时间差不多，”Riccomini说。“很快就清楚，我们需要为项目提供一些结构，无论是在治理方面还是在安全模型方面，以及其他支持，例如贡献者许可协议（CLA）。”

Apache将是显而易见的选择，但Apache的一个悖论是，它在教育开发者方面做得如此出色，以至于他们最终会超越它。

“我对待Apache就像写书一样。每当我完成与它的互动时，我都觉得‘我再也不会这样做了’，但不可避免地，我最终还是会这样做，”Riccomini说。“我在寻找一个可以用来运行SlateDB许多流程的基金会时，不希望它是Apache，因为我发现它们在流程方面过于繁重，而且它们的 инфраструкture 相当老旧且脆弱。”

Riccomini向CNCF提交了申请，他告诉我，他的经历“并不十分积极”。他后来 [撤回了](https://github.com/cncf/sandbox/issues/114) SlateDB的CNCF申请，并将该项目捐赠给了Commonhaus。

“CNCF比Apache有更多的流程，而且它们非常以云原生为中心。我不知道如何应对。我的结论是CNCF就像Apache，但基础设施更好。这并没有错，但这并不是我想要的。”

就其而言，Cloud Native Computing Foundation首席技术官Chris Aniszczyk通过电子邮件告诉 *The New Stack*，“CNCF不强制单一的开发路径，而更像是一个‘[自带治理](https://www.cncf.io/blog/2019/08/30/cncf-technical-principles-and-open-governance-success/)’的基金会，因为我们相信维护者最清楚他们自己的社区需要什么。我们提供的是一个 [结构化的成熟度框架](https://contribute.cncf.io/community/governance/) ——从沙盒到毕业——它充当路线图，而没有僵硬、一刀切的治理带来的摩擦。”

> “感觉有点像螺母和螺栓都散落在地上，我们还在组装这个东西。这不困扰我，但我可以看到这对于一些人来说可能是一个挑战。”

是Gunnar Morling将Riccomini介绍给Commonhaus的，他的Debezium项目于2024年加入了Commonhaus基金会。“这正是我所寻找的——更低的接触、更灵活、以及更多的自主权，我对此非常感激，”他说。

自主权要求维护者具备自我激励的能力，这样入职流程就不会拖延。“没有人催促你，也没有季度董事会会议。如果你不积极主动，你可能会发现一年过去了，没有任何进展。所以你需要负责遵循Erin [Schnabel]的清单。”

作为一个年轻的基金会，Commonhaus也经历了自己的成长烦恼。“有时流程会改变，或者缺少文档，或者GitHub链接无效，因为东西被移动了。感觉有点像螺母和螺栓都散落在地上，我们还在组装这个东西。这不困扰我，但我可以看到这对于一些人来说可能是一个挑战。”

这种精简的方法也吸引了Vermeulen加入Commonhaus。“我不想让繁重的治理和繁文缛节阻碍我前进，因为这是一个快速发展的活跃项目。Commonhaus有着完全不同的思维模式；它关乎支持社区，而不是阻碍我们。”

## 没人给维护者买杯咖啡

出于对项目提供财务帮助的兴趣，Schnabel特别热衷于鼓励为项目维护者提供小额捐款。

在我们的谈话中，我回想起，当我担任InfoQ主编时，我们采用 [AsciiDoc](https://asciidoc.org) 作为图书出版格式之一。我们第一次使用它时，生产过程困难重重，我们不得不与项目维护者合作，才摆脱困境。他非常友善，慷慨地付出了时间。当书出版后，我向执行团队的其他成员建议我们捐款。我记得回应相当冷淡，最终我选择个人捐款。

这种不愿意为免费获得的东西（无论是代码、设计工作还是文档）付费的态度，是Schnabel深感担忧的，这也解释了为什么Commonhaus的成员是个人而非公司。

“我在另一个社区，对支持内容创作者很感兴趣。如果你创作了一些其他人喜欢的东西，他们会给你买杯咖啡或者捐七八块钱。当你正在做某事时，有这种支持感觉很好。然而，在企业Java领域，那种随意捐几块钱的意愿是不存在的。我真的想改变这一点。”

“我们大多数从事开源工作的人都希望以此谋生，”Almiray说。“我们中的一些人很幸运被一家非常乐于从事开源工作的公司雇用，但另一些人则没有。Commonhaus提供透明的财务责任，这意味着赞助商可以将资金发送给基金会，并看到它不会消失；这个基金会没有黑洞。”

Commonhaus要求使用其项目的个人提供小额捐款；依赖这些项目的公司也可以赞助并担任顾问。有了更多资金，Schnabel希望能够支付设计师和技术作家。“我知道有些项目希望重新设计他们的标志。还有一些项目希望在网站上获得帮助以改进文档，或者在如何组织信息以使其更易于访问方面获得指导。”

Riccomini对基金会的财务独立性表示了一些保留。“他们非常依赖IBM，但能够独立生存会非常好。” 这并不罕见。CNCF在其成立之初严重依赖Google，因为Google不仅为基础的 [Kubernetes](https://thenewstack.io/kubernetes/) 项目做出了贡献，而且在其治理和早期财务支持方面也发挥了重要作用。

IBM/RedHat是Commonhaus最大的捐助者，但基金会也有几个较小的贡献者：[Gradle](https://gradle.org)（Gradle Build Tool背后的公司）正在提供一个专门的Develocity实例，这是该公司的可观测性和加速平台；[1Password](https://1password.com) 提供密码库和用于存储凭据的基础设施；而 [scarf.sh](https://about.scarf.sh) 则提供中央指标和分析的访问层。尽管如此，更多的财务独立性仍将受到欢迎。

Riccomini发现Commonhaus是一次非常积极的经历。“我认为Commonhaus是那些创作者经验更丰富、知道如何运营开源项目，但仍希望获得商标管理、法律等方面支持和框架的项目的一个绝佳归宿。它为这类群体提供了一个很好的平衡，”他说。

Commonhaus能否最终改变开源可持续性文化仍有待观察，但该基金会两年来的记录表明它已经找到了一个真正的利基市场。它不会取代Apache或CNCF对于需要集中治理（例如围绕多供应商合作的规则）的项目，而且它可能不适合需要更多指导的早期项目。

但对于那些希望获得法律框架而又不被官僚主义窒息、希望拥有一个没有为每个决策都设立委员会的社区，以及一个将他们视为专业人士而非恳求者的基金会的经验丰富的维护者来说，Commonhaus可能正是生态系统一直所缺失的。

更困难的问题是，这种模式能否足够快地发展壮大，并超越其Java根基，对因倦怠和放弃而悄然掏空无数人赖以生存却鲜有人愿意付费的开源社区，产生有意义的影响。