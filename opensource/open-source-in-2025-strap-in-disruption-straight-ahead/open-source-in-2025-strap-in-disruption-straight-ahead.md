
<!--
title: 2025年的开源：系好安全带，颠覆就在眼前
cover: https://cdn.thenewstack.io/media/2023/12/95c34a5e-year-forecast-1.png
-->

新年伊始，围绕许可、开源AI定义、安全合规以及如何支付志愿者维护人员等问题，预计将出现新的紧张局势。

> 译自 [Open Source in 2025: Strap In, Disruption Straight Ahead](https://thenewstack.io/open-source-in-2025-strap-in-disruption-straight-ahead/)，作者 Heather Joslyn。

开源软件世界有时感觉像一个泡沫，热爱解决问题的人们在这里钻研解决方案，自由分享想法，并建立全球贡献者社区。他们聚集在会议、聚会和网上，赞扬彼此的辛勤工作和创新，并互相提醒他们有多么优秀。

但外部力量有时会像摇动雪球一样撼动这个泡沫。三月份，[Redis](https://redis.com/?utm_content=inline+mention)调整了其开源内存数据存储的许可证，这[促使了Linux基金会支持的分支的创建](https://thenewstack.io/linux-foundation-forks-the-open-source-redis-as-valkey/)，[Valkey](https://thenewstack.io/valkey-whats-new-and-whats-next/)。

十二月份，围绕[Puppet](https://puppet.com/?utm_content=inline+mention)（一个基础设施即代码工具）的社区[宣布计划对其进行分叉](https://thenewstack.io/puppets-open-source-community-plans-to-fork-the-program/)，这是继[十一月份的新闻](https://www.puppet.com/blog/open-source-puppet-updates-2025)之后，其所有者[Perforce](https://www.perforce.com/)将“将其团队开发的任何新的二进制文件和软件包交付到一个私有的、强化和受控的位置。社区贡献者可以在最终用户许可协议 (EULA) 的条款下免费访问此私有存储库，用于开发用途。”

换句话说，Puppet现在将是源代码可用的，而不是开源的。

广泛使用的[开源软件转向更严格的许可证的趋势并非新鲜事](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/)。但当前的浪潮可以说是从[HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention) 2023年8月决定将Terraform（随后还有其他产品，如Nomad）从开源世界撤回，并将它们分配给[商业源许可证v1.1](https://www.hashicorp.com/bsl)开始的。一个围绕Terraform的分支OpenTofu的社区正在发展壮大。同样，[OpenBao，一个在2023年底创建的HashiCorp Vault密钥管理器分叉](https://thenewstack.io/meet-openbao-an-open-source-fork-of-hashicorp-vault/)也是如此。

用户确实经历了一些“动荡”——[Matt Butcher](https://thenewstack.io/author/mattbutcher/)（Fermyon Technologies的首席执行官兼联合创始人）创造的一个词，用来形容2023年和2024年的[开源许可](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/)风波——“湍流”和“磨难”的混合体。由于Fermyon使用HashiCorp的Nomad，他的公司受到了HashiCorp的决定造成的动荡的影响。Butcher告诉The New Stack (TNS)：“我们实际上最终向他们请求对某些部分的例外，因为我们运行的是Nomad的修补版本。”

但作为一家初创公司的创始人，他正在仔细观察许可证的决定。Fermyon专注于[WebAssembly](https://thenewstack.io/webassembly-in-2024-components-are-and-are-not-the-big-story/)，拥有开源项目和付费企业级产品。

他在十一月份的[KubeCon + CloudNativeCon北美大会](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)上告诉TNS：“我有点希望这种特殊的方法仍然非常可行，我认为它会。”“如果我们一开始就能这样规划，我们就不用撤回东西，而这往往会在社区中造成不信任，或者是不信任的假设。”

除了后期资本主义的需求和对基于开源工具的公司缺乏耐心的投资者之外，其他外部因素也正在给开源世界施加压力。例如，生成式人工智能的承诺/威胁。或者不断变化的地缘政治格局，带来了新的安全问题和治理法规。

还有一个长期存在的问题是如何补偿许多项目所依赖的全球成千上万的无偿志愿者维护人员。

2025年开源的未来是什么？以下是一些想法，这些想法是从去年秋季的技术会议的采访以及对120多位行业专家的[New Stack调查](https://thenewstack.io/programming-languages-coverage-matters-most-say-tns-readers/)（于十一月份进行）中收集的，该调查询问了开源的未来、开发人员对人工智能的使用以及IT基础设施。

## 更多整合，更多许可证变更
随着庞大的云原生生态系统整合，预计来年将出现更多“动荡”。IBM 4月份宣布的[以64亿美元收购HashiCorp](https://thenewstack.io/ibm-purchases-hashicorp-for-multicloud-it-automation/)，预计将于2025年第一季度完成，这可能预示着一种趋势。

Chainguard的CTO在回复TNS调查时表示，他希望IBM收购HashiCorp能够为开源社区带来成果。“我有点希望IBM收购Hashi后，[能够弥合Terraform和OpenTofu之间的隔阂](https://thenewstack.io/with-ibms-open-source-roots-terraform-could-be-free-again/)。Elastic的类似决定逆转已经为这方面树立了先例。”

Elastic通过为其添加[GNU Affero通用公共许可证](https://www.gnu.org/licenses/agpl-3.0.en.html)，[在8月份将Elasticsearch和Kibana转移到开源许可](https://thenewstack.io/whats-behind-elastics-unexpected-return-to-open-source/)。此举是在该公司决定将这两个项目从Apache 2.0许可证转移出去三年后做出的。Elastic的搜索和分析引擎Elastic一直在面临来自[OpenSearch](https://thenewstack.io/opensearch-how-the-project-went-from-fork-to-foundation/)的竞争，OpenSearch是由[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)赞助的分支。

预测许可证的未来之所以棘手，是因为开源软件赞助商面临的压力并非仅仅来自一个方向；[竞争](https://thenewstack.io/why-open-source-forking-is-a-hot-button-issue/)可能会促使公司对开源工具采用更严格的许可证，或者创建一个开源版本以加快采用速度。

Asperitas云实践负责人回复The New Stack行业专家调查时表示：“预测哪些开源项目正在转向更严格的模式是高度推测性的。”

尽管如此，Wheeler仍指出Elasticsearch和Kibana是未来可能面临新的许可压力的一些例子。并且，基于HashiCorp的例子，他认为以下项目未来也可能面临类似的压力：

[Hadoop](https://github.com/apache/hadoop)，[Kafka](https://github.com/apache/kafka)，[Lucene](https://github.com/apache/lucene)(由[Apache基金会](https://www.apache.org/)赞助)，[Kubernetes](https://github.com/kubernetes/kubernetes)和[Prometheus](https://github.com/prometheus/prometheus)(由[云原生计算基金会](https://cncf.io/?utm_content=inline+mention)赞助)，[Ansible](https://github.com/ansible/ansible)(由[Red Hat](https://www.openshift.com/try?utm_content=inline+mention)赞助)。

除了Ansible采用[GNU通用公共许可证v3](https://www.gnu.org/licenses/gpl-3.0.en.html)外，其余项目目前均采用[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)许可证。（除了Ansible之外，所有项目都位于非营利性基金会，大概免受商业利益的影响。）

相比之下，Argonaut Media总裁兼[Linux基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention)前编辑总监表示，“情况将相反”。

在回复TNS关于开源未来的调查问题时表示：“我认为Chrome甚至Android很可能会成为独立管理的开源项目，而不是被[Google](https://cloud.google.com/?utm_content=inline+mention)根据反垄断法规出售。”（8月，美国哥伦比亚特区地方法院认定该公司在在线搜索领域维持着非法垄断地位。）

GitLab首席产品官预计，2025年将有更多以前是开源的项目转向更严格的许可。但他对这一趋势持乐观态度。

他在11月的KubeCon上告诉The New Stack：“我认为这将开启对开源含义的全新理解。”他以HashiCorp的举动为例。

“他们一直在将Vault从非常宽松的开源许可证转移出去，但这导致了OpenBao的出现。在GitLab，我们正在构建我们自己的原生密钥管理器。这将产生下一轮未来的开源。”

## 开源AI辩论：才刚刚开始
十月，开放源代码倡议组织（OSI）[发布了其开源人工智能定义的1.0版本](https://thenewstack.io/the-open-source-ai-definition-is-out/)。OSI执行董事在发布前告诉The New Stack，[1.0版是一个“谦逊”的文件](https://thenewstack.io/osi-finalizes-a-humble-first-definition-of-open-source-ai/)，一个正在进行中的工作。

在定义发布之后，[批评者](https://thenewstack.io/the-open-source-ai-definition-what-the-critics-say/)对它进行了批判，抱怨说如果供应商不想透露他们的训练数据，这个定义会给他们一些掩护，[该定义从根本上改变了开源的含义](https://thenewstack.io/the-case-against-osis-open-source-ai-definition/)，并且鉴于人工智能与软件代码的不同之处，OSI也许根本不应该尝试定义开源人工智能。

“关于构成人工智能‘开源’的因素存在一场有趣的辩论，”[Cosine](https://cosine.sh/)的首席运营官在回复The New Stack的调查时说。

“[Meta](https://about.meta.com/?utm_content=inline+mention)和谷歌刚刚[被指责声称自己是开源的，而实际上并非如此](https://thenewstack.io/why-open-source-ai-has-no-meaning/)。真正的问题是：当我们生成更多[合成数据](https://thenewstack.io/the-future-of-ai-and-travel-relies-on-synthetic-data/)时，在哪里划清界限？你可以公开你的数据来源，但保留你的合成数据生成过程的专有性。在透露你的数据集和透露你如何创建它之间，界限模糊不清。”

显然，这场辩论才刚刚开始。大型企业的举动很可能成为2025年讨论的一部分。在一篇12月26日的公司博客文章中，[OpenAI声明其意图](https://openai.com/index/why-our-structure-must-evolve-to-advance-our-mission/)是从盈利和非盈利结构转变为公共利益公司——就像竞争对手Anthropic和xAI一样——支持一个非盈利组织。

最大的收获：人工智能及其主要参与者肯定会在2025年夺走开源泡沫中大量的氧气。

“[Solo.io](https://solo.io?utm_content=inline+mention)的全球现场首席技术官在回复关于开源未来的调查问题时回答说：“最大的威胁可能是现有开源项目的可持续性和可维护性。”

“随着人工智能继续主导技术进步，人们对人工智能相关倡议的关注发生了显著转变。这往往导致成熟的项目，例如CNCF毕业的项目，维护人员减少，危及其长期保持健康和可持续发展的能力。”

而且，在2025年，对于不是谷歌、Meta、[微软](https://news.microsoft.com/?utm_content=inline+mention)及其同类企业的实体来说，在开源人工智能领域竞争将变得更加困难。

“[Zilliz](https://zilliz.com?utm_content=inline+mention)的工程副总裁在回复TNS调查时说：“对于人工智能应用来说，计算和数据至关重要，但只有谷歌或Meta这样的巨头才能轻松获得数据。”

“较小的开发者群体甚至个体开发者都没有这种优势，因此将持续面临寻找开源模型的挑战。”

事实上，一些人担心深度学习模型最终可能会超越开源开发。[有人对此观点提出反对](https://thenewstack.io/genai-wont-replace-open-source-says-aws-exec/)。但威胁依然存在。

“[Lightrun](https://lightrun.com/?utm_content=inline+mention)的产品营销主管在其对TNS调查的回复中警告说：“GenAI工具通常是专有的，它们为开发人员提供了先进的自动化、代码生成和可观察性功能，这些功能在便利性和性能方面可能会超过开源替代方案。”

“与此同时，复杂的架构需要高度集成、可扩展的解决方案，而专有平台更能提供这些解决方案。这种转变有可能将开源项目边缘化，特别是那些无法跟上人工智能驱动创新或分布式系统需求的项目，导致开源生态系统的采用和投资减少。”


## 安全和合规性问题将会增加
你可能已经注意到，世界目前并非特别平静。而网络攻击者喜欢在危机中制造机会。
除了AI，另一个巨大的争论将是安全和合规性，“OSI的Maffulli告诉The New Stack。“它已经存在了。但到2025年，鉴于地缘政治格局变得越来越复杂和错综复杂，它将变得更加重要。这将是一件大事。”

Apiiro的联合创始人兼首席执行官Plotnik在回应TNS调查时指出，AI有可能增强威胁。

“到2025年，开源软件威胁将从传统的漏洞转向AI生成的隐蔽后门和嵌入在开源软件包中的恶意软件，”Plotnik说。“随着攻击者利用AI工具在开源代码中开发和伪装恶意软件，应对这些新的威胁将需要安全工具的重大进步，以领先于这些快速发展的挑战。

然而，一些好消息是：到2025年，AI自动化工具或许有助于查找和修复更多未维护的开源代码和技术债务，从而帮助堵住一些黑客的潜在入口。

“我相信，随着AI编码工具的普及，我们应该会看到未维护的开源组件有所减少，主要是因为即使经验有限的开发人员也能更容易、更快地编写一些高度细分领域的代码，”SingleStore的首席营销官Kumar在回应TNS调查时说。

## 付钱给维护者：需要更多资金和创意
几乎每个技术栈都使用开源代码，但是——仍然！——大多数开源维护者基本上只能获得GitHub上的星标和亲吻表情符号。

Tidelift 9月份发布的一项研究显示，60%的受访开源维护者表示他们没有为自己的工作获得报酬。（也许并非巧合的是，大约相同比例的受访者表示他们已经退出或考虑退出他们的项目。）

这种情况——持续依赖一支由未得到报酬、未被重视的业余爱好者组成的队伍来维护重要的代码库——将成为2025年开源面临的最大威胁，包括其工具和平台的安全性，行业专家表示。

Chainguard的Moore在回应TNS调查时说：“开源正在蓬勃发展，并且经常由人们在晚上和周末无偿维护。”“随着开源生态系统的复杂性和广度不断扩大，必要的更新速度呈指数级增长。”

“随着越来越多的组织集成开源解决方案，未修补的漏洞和过时的配置的可能性增加，使企业面临重大的安全和性能挑战。”

Snowflake的Snowpark生态系统和开发者平台产品总监Hollen在回复TNS调查时，评论了支付构建和维护开源项目人员的重要性。

Hollen写道：“开源依赖于赞助商和支持者。”“许多维护者和贡献者（包括我自己）除了日常工作职责外，还参与开源项目。对开源最大的威胁是，如果重要的企业赞助商停止鼓励、推广和支持这些努力，以帮助贡献者和维护者从中获得一些价值。”

除了Tidelift等赞助商的贡献以及大型公司将富有成效的维护者纳入其工资单外，预计2025年将出现一些有创意的尝试来补偿开源开发者。

未来一年值得关注的是Chai，这是一个由Homebrew创建者Howell共同创立的分散式技术协议。Howell已经启动了Chai，它通过包管理器数据来衡量开源的活力。

参与该项目“测试网”的参与者正在赚取代币；在2025年的某个时候，当该项目的“主网”阶段启动时，这些代币将在多个加密货币交易所推出，目的是使其具有货币价值。

Howell告诉The New Stack，大约有16,000个项目注册了Chai的测试网。这只是全球1050万个开源项目中的一小部分，但这清楚地表明，在补偿开源开发者方面，对创新思维的需求非常强烈。

Hecht为这篇文章做出了贡献。
