根据 [Linux 基金会](https://www.linuxfoundation.org/press/press-release/openssf-announces-15-new-members-to-further-strengthen-open-source-software-supply-chain-security) 的数据，98% 的组织经常使用开源软件（OSS）。开源软件非常普及，它已嵌入到我们日常使用的大多数应用程序中。但是，要跟上开源软件版本弃用和生命周期结束（EOL）的步伐变得越来越难。

[HeroDevs](https://www.herodevs.com/) 的联合创始人兼 CEO [Aaron Frost](https://www.linkedin.com/in/aaronfrost/) 告诉 The New Stack，“开源版本生命周期肯定在缩短”。HeroDevs 为已弃用的开源软件提供长期支持。“仅在 2025 年，顶级开源项目就有超过 100 个计划的 EOL。”

这些 EOL 分为两个主要类别：次要版本和主要版本的 EOL，以及整个项目的 EOL。第一个例子是 [.NET 6 的退役](https://thenewstack.io/herodevs-throws-net-6-users-a-post-deprecation-lifeline/)，它发生在 2024 年底，但许多人仍然依赖它。后者的一个例子是 [Google](https://cloud.google.com/?utm_content=inline+mention) 在 2021 年 [完全停止对 AngularJS 的支持](https://www.herodevs.com/blog-posts/sunsetting-a-framework-lessons-from-angularjs)。

开源领域出现了一系列许可证变更、缩短的版本弃用以及流行的 OSS 软件包的彻底停用。即使对于 [高度使用的开源项目](https://thenewstack.io/open-source-is-at-a-crossroads/) 来说，被遗弃而没有明确的未来也并不罕见。

非营利组织 [Drupal 协会](https://www.drupal.org/association) 的 CTO [Timothy Lehnen](https://www.linkedin.com/in/hestenet/) 告诉 The New Stack，“在依赖关系树中的某个地方，几乎所有团队都至少会有一个资金不足、计划进行重大版本更新，甚至正在考虑关门的软件包。”

突然的转变让开发人员挠头，匆忙寻找解决方法，维护自定义分支或重新评估预算以支持商业替代方案或长期支持计划。那么，当开发人员 [高度依赖的开源软件崩溃时，他们应该怎么做](https://thenewstack.io/how-developers-can-head-off-open-source-licensing-problems/) 呢？

当你依赖的 OSS 达到 EOL（或更糟，完全无人维护）时，你需要一个行动计划。下面，我们将考虑公司如何为 OSS EOL 做好准备，维护者和供应商正在做些什么来支持已弃用的项目，并为依赖于未来不确定的软件包的开发团队提供指导。

## 开源 EOL 趋势持续

[Bloomberg](https://www.bloomberg.com/company) 首席技术官办公室的开源项目办公室负责人 [Alyssa Wright](https://www.linkedin.com/in/alyssapwright/) 告诉 The New Stack，“我们看到开源项目达到生命周期结束的趋势正在显著加速”。她将此归功于人工智能的采用，导致整个堆栈中使用的 OSS 软件包数量激增，以及 [普遍存在的维护者倦怠](https://thenewstack.io/beat-developer-burnout-how-the-right-platform-makes-a-difference/)。

维护者权益问题继续加剧被遗弃项目的问题。[根据 2024 年 Tidelift 的一份报告](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/)，60% 的开源维护者已经或考虑过放弃维护项目，其中五分之一的人表示他们已经放弃了。

Wright 补充说，“快速的 OSS 发布周期和较慢的企业更新之间的步调不一致进一步加剧了这些 EOL 挑战。”

她说，消失的不仅仅是“闪亮的新项目”，还有主力中间件、库或流行框架的旧版本。当这些关键依赖项丢失时，很难迁移。

也就是说，并非所有人都看到了危险信号。Lehnen 认为，最近的 EOL 更多与版本有关，而不一定是整个项目：“实际上没有很多项目正在关闭——开源生态系统实际上非常健康。”

要跟上整个软件供应链中快速增量项目版本的更新步伐具有挑战性。尽管如此，Lehnen 认为开源方面已经有了更多的改进，无论是在 [资金援助](https://thenewstack.io/open-source-needs-maintainers-but-how-can-they-get-paid/) 方面，还是特别是在 Drupal 的案例中，在版本控制系统周围改进了治理，并支持向后兼容性。

开源领域的突然转变并不新鲜，其中大部分代表了自然的技术周期。[Rocky Linux](https://rockylinux.org/) 的创始人兼基础设施总监 [Neil Hanlon](https://www.linkedin.com/in/hanlonneil/) 说，Rocky Linux 是一个社区支持的 CentOS 替代品。

Hanlon 告诉 The New Stack，“在不了解具体情况的情况下指责很容易，但是一旦你了解了内部动态，许多这些变化就更有意义了。”

但是，他承认，最近发生重大变更的项目数量正在增加。“出现了一些更令人震惊的例子——[Ceph](https://thenewstack.io/ceph-20-years-of-cutting-edge-storage-at-the-edge/) 和 [oVirt](https://www.ovirt.org/) 就是其中的例子——管理或投资的变化引起了真正的担忧。”

## OSS 转变让开发人员陷入困境

当一个 OSS 项目突然被放弃时，可能会导致许多下游后果。这些后果与任何关键软件依赖项变得不受支持的情况相似：由于未修补的缺陷而导致的安全风险、由于维护旧代码而增加的技术债务以及兼容性问题。

持续代码质量工具提供商 [Sonar](https://www.sonarsource.com/) 的副总裁 [Donald Fischer](https://www.linkedin.com/in/donaldfischer/) 告诉 The New Stack，“最紧迫的问题之一是未来的安全漏洞可能无法得到解决。” 这可能包括软件包本身中的漏洞，以及与 [传递依赖项](https://thenewstack.io/a-guide-to-software-dependencies/) 的集成中断，传递依赖项是项目依赖的其他开源软件包。

Bloomberg 的 Wright 指出，当项目消失时，缺乏错误修复、性能改进和社区帮助是其他重大挑战。“由于系统稳定性和正常运行时间可能受到威胁，公司面临着更高的运营和合规风险，”她说。所有这些都可能削弱消费者的信任并减缓创新。

Hanlon 说，有计划的 EOL 是常规风险和生命周期管理的一部分，而突然的放弃则更加困难。他补充说，这种影响会波及用户和项目维护者：“人们经常抨击维护者，但在许多情况下，这是倦怠或健康问题——尤其是对于单独的维护者而言。”

## 当项目达到 EOL 时该怎么办

组织不应坐等突然的 EOL 情况发生，而应做好充分准备。这包括清点你的关键开源依赖项，并密切关注公开的停止支持公告。但是，当你完全措手不及时，可以采取以下几个步骤。

### 收集信息

当项目消失时，第一步是收集信息。是整个项目都已达到生命周期结束？还是只是一个版本？如果是后者，则可能有一条简单的迁移路径可以迁移到次要版本或主要版本。

但是，如果 EOL 更加严重，Hanlon 鼓励进行透明的沟通：询问维护者项目达到 EOL 的原因。“通常，通过直接参与，你将了解真正发生了什么，有时甚至可以通过提供帮助找到前进的道路，”他说。

### 评估损失

接下来是损失评估。为了制定缓解计划，Wright 鼓励从技术、安全和业务角度评估丢失的依赖项的影响。这将告知你的爆炸区域和你对替代项目的研究。

Lehnen 说，“现代软件建立在相互连接的依赖关系网络之上。” 他说，有帮助的是创建一个“风险管理树”，该树公开了跨许多项目使用的底层组件，这些项目将需要更多支持。

### 寻找替代方案

如果维护者退出，下一个合乎逻辑的步骤是寻找积极维护的替代开源项目。Fischer 说，“在许多情况下，最好的解决方案是将你的软件迁移到使用替代开源软件包，或积极维护的开源软件包的主要版本。” 尽管如此，即使在 AI 助手的帮助下，这也需要更改代码，他补充说。

### 掌握控制权

如果没有合适的替代方案，你可以提议集体管理或独自承担项目的重任。Wright 说，“对于真正关键的开源组件，组织可以考虑在内部承担维护工作或为项目做出重大贡献。”

Lehnen 说，这种灵活性是开源的基本优势，与专有软件相反：“开源软件不是由单个参与者维护的，并且始终可以引入新的维护者来支持它。”

### Fork 它

另一种选择是 Fork 该项目，但这是一个不应掉以轻心的途径。可能需要整个社区来支持旧分支，例如 [Debian 长期支持（LTS）](https://www.debian.org/lts/) 或 Rocky Linux 的情况。

Hanlon 说，“Fork 是开源的一项基本权利，但有效的 Fork 需要深入的领域知识，通常跨多个系统。” “这不是一个随机团队可以随便接手并运行的。”

### 寻求专家帮助

如果你觉得自己完全力不从心，另一种选择是聘请维护私有软件、构建补丁或提供扩展安全支持的顾问或第三方供应商。Lehnen 说，这可以为用户升级到最新版本提供额外的空间。

但是，花钱摆脱问题会带来一些关于长期可持续性的缺点。正如 Fischer 指出的那样，“当你转移到开源软件包的私有 Fork 时，你会失去从开源中获得的许多实际好处。” 你将依赖于外部业务及其定价结构。

Hanlon 说，在这种情况下，“诀窍在于找到并激励合适的专家。”

另一种途径是 [与开源基金会合作](https://thenewstack.io/does-your-open-source-project-need-foundation-oversight/) 以安排扩展支持。

## 社区在维持 OSS 中的作用

除了事后响应之外，[维持重要的 OSS](https://www.infoworld.com/article/3557846/how-do-we-fund-open-source.html) 实际上应该从更上游开始。要完全避免项目被放弃，就需要投资于你积极使用的项目。

Hanlon 说，“这不仅仅意味着金钱——它意味着出现、贡献工程时间、提出周到的问题并了解他们的路线图。” “如果你的业务依赖于 OSS，那么你是该生态系统的一部分，也是责任的一部分。”

其他人也有同样的感受，并且了解投资于社区的重要性。Wright 说，“在 Bloomberg，我们将此视为战略性地投资于开源健康的机会，以便将这些风险转化为我们对作为开源的公共利益的承诺的证明。”

像 Bloomberg 这样的组织正在成立开源项目办公室，并投资于内部战略，以回馈并保持连续性。Wright 补充说，“行业如何管理生命周期结束实践对于整个数字生态系统的健康至关重要。”

值得庆幸的是，该行业也在采取行动，通过某些资金计划来帮助保留关键的 EOL 开源项目。例如，HeroDevs 在 6 月份启动了一项 [2000 万美元的开源基金](https://www.herodevs.com/blog-posts/herodevs-launches-20-million-sustainability-fund-for-open-source-creators-to-secure-end-of-life-software)，以帮助支持生命周期结束的 OSS，为高影响力项目的维护者提供支持。

其他公司主导的基金、承诺、非营利计划和新的赞助模式已经出现，以维持项目。例如，[Bloomberg 的 FOSS 贡献者基金](https://www.bloomberg.com/company/stories/bloomberg-ospo-launches-foss-contributor-fund/) 自 2023 年成立以来，已向 25 多个不同的开源项目提供了赠款。[The Open Source Pledge](https://opensourcepledge.com/) 是另一项公司主导的倡议，迄今为止已向维护者提供了超过 200 万美元的资金。

Fischer 与他人共同创立了 Tidelift，该公司于 12 月被 Sonar 收购。Sonar 继续执行 Tidelift 的向开源维护者提供赠款的计划。他说，“在经济上支持 OSS 项目可以为维护者提供很大的帮助，并防止项目达到 EOL。”

尽管如此，对于 Hanlon 来说，仍然存在差距：富裕的公司仍然更多地为自己优化，而不是为了更大的利益。“我希望看到更多的维护者通过供应商支持的合同和合作社获得授权，这些合同和合作社优先考虑经济和技术可持续性，”他说。“太多的努力仍然依赖于善意或旨在提取而不是维持的片面合同。”

而且，Lehnen 指出，除了技术领域之外，支持仍然处于萌芽状态。“不幸的是，更广泛的行业在做必须做的事情以确保关键开源软件的长期可持续性方面严重落后，”他说。社会需要时间来重新思考对数字公共产品的公共支持，就像我们公开支持物理基础设施一样。

## “这不应该是一个惊喜”

软件达到生命周期结束是开发生命周期的一个典型部分。Lehnen 说，“你的软件堆栈的任何部分达到生命周期结束都不应该是一个惊喜，”他指出时间表和升级路径通常会提前发布。

但是，挑战在于组织通常依赖于数千个不同的项目，这使得跟踪每个 EOL 时间表都具有挑战性。Fischer 说，自动化工具可以生成软件物料清单（SBOM）来帮助更好地进行清点，但这仍然需要积极的响应。

他说，“有了这些信息，组织就可以寻找关键软件包即将达到生命周期结束的明显迹象，例如贡献减少或发布节奏放缓，或者明确的生命周期结束公告。”

尽管如此，对于目前依赖于未来不明的 OSS 软件包的团队，Wright 建议主动为高风险依赖项制定迁移策略，并在内部沟通 OSS 健康的重要性。

参与其中也没有什么坏处。即使是小小的贡献，例如错误报告或小修复，也能产生很大的影响。因此，Hanlon 建议，最好的建议可能是在为时已晚之前采取行动。

他说，“不要等到博客文章告诉你它已被放弃。” “联系、贡献、赞助维护者，表达你的关心。”

“参与其中的最佳时机是昨天。”