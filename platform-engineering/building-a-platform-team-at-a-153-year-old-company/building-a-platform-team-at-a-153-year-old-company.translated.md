# Building a Platform Team at a 153-Year-Old Company

![Featued image for: Building a Platform Team at a 153-Year-Old Company](https://cdn.thenewstack.io/media/2024/06/7bf6b0ed-building-a-platform-team-at-a-153-year-old-company-2-1024x576.jpg)

Every company is different, so every platform must be unique.

We hear this phrase often in the tech world. Embracing a bespoke [platform engineering](https://thenewstack.io/platform-engineering/) approach leads companies to invest significant time and money customizing open-source software and building their own [internal developer platforms](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/) from scratch.

As [Syntasso](https://thenewstack.io/platform-engineering-demands-a-product-mindset/)'s chief engineer [Abby Bangser](https://www.linkedin.com/in/abbybangser/) says, [platform engineering teams should focus](https://thenewstack.io/how-to-foster-a-good-internal-developer-platform-experience/) on important shared services, such as infrastructure, scaling, and security, but these services shouldn't impact the uniqueness of your business.

Platform teams are dedicated to reducing cognitive load and tool complexity, helping application developers deliver value to end users faster. So, unless you're a platform tool company, spending time building your own custom platform means you're not focusing on your organization's unique value proposition or improving your internal developer experience.

As [Mathias Gebbe](https://www.linkedin.com/in/mathias-gebbe/) and [Aljoscha Pörtner](https://www.linkedin.com/in/aljoschap/) described at [PlatformCon 2024](https://platformcon.com/talks/logbook-of-a-journey-building-a-platform-team-in-a-150-year-old-logistics-company/), the digital transformation of [Hellmann Worldwide Logistics](https://www.hellmann.com/en), a 153-year-old company, is both a unique experience and one shared by many other companies across different industries and sizes. Their lessons learned reveal a platform engineering model that other organizations can learn from.

## Beware of Partial Transformations

Hellmann Worldwide Logistics, a privately held company founded in 1871, has grown into a global enterprise with 40,000 employees operating in 54 countries. While Hellmann's tech stack isn't that old, it did need an upgrade.

"You saw a lot of AS/400 green screens, [Oracle](https://developer.oracle.com/?utm_content=inline+mention), [VMware](https://tanzu.vmware.com?utm_content=inline+mention), and an on-premises data center. Code was written in Java Enterprise [Edition], C#, and even Visual Basic," said Gebbe, head of developer experience and platform team.

The on-premises data center had dedicated teams, including a network team, a server team, and a database team. "Development teams were siloed because one team was building on [IBM](https://www.ibm.com?utm_content=inline+mention) WebSphere Portal servers, and another team was building flat lines for employee and customer portals."

Each team brought a lot of business context, but Gebbe said they lacked [cloud-native](https://thenewstack.io/cloud-native/) experience entirely.

Still, Hellmann's engineering culture embraced digital transformation, and the logistics company started putting containers on ships, and then on the cloud with [Moby](https://thenewstack.io/the-moby-project-post-kubernetes-3-new-releases-in-2023/). Product development teams quickly started embracing the [DevOps](https://thenewstack.io/devops/) philosophy — "you build it, you run it" — sharing resources, blueprints, and operational pathways.

## "I Don't Feel Like a Software Developer"

While most of Hellman's engineers were still on-premises and had some cloud experience, they were using cloud-native technologies like [Docker](https://www.docker.com/?utm_content=inline+mention)[ Swarm](https://thenewstack.io/docker-swarm-a-user-friendly-alternative-to-kubernetes/) for orchestration.

"But then things diverged," Gebbe said. "We had some teams that were lucky enough to have the resources, the knowledge, the time, and all of that to move towards a platform that leverages cloud infrastructure services."

Those who stayed on-premises couldn't achieve as much.

"We had other teams that were very product-focused, and they stuck with the old platform stack," Gebbe said. These teams "were still ticket-driven, had very little automation, and were limited by things like not being able to use distributed file systems."

Then the gap between teams grew wider. Some teams chose [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) cloud, while others chose [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure cloud. Different teams used different source code management tools.
“我的一位同事曾经说过，‘我在这里感觉不像一名软件开发人员。我是一名测试工程师、DevOps 工程师、一级支持安全专家。我不是一名全栈开发人员。我是一个完整的 IT 部门，’”Gebbe 回忆道。

然后，他向 PlatformCon 观众展示了一张 [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention)[ 景观](https://landscape.cncf.io/) 的拥挤图片，从中“每个产品团队都必须为其团队找到合适的解决方案。”

这种 [开发人员倦怠](https://thenewstack.io/how-to-recognize-recover-from-and-prevent-burnout/) 和认知负荷过重是采用平台工程的常见动力。

与许多进行平台工程项目的公司一样，钟摆需要从最初的云原生开发人员自主权转向集中化。这意味着平台团队必须做出一些并非所有人都满意的决定，因为他们被迫迁移到平台上。

“在这种情况下，唯一感到高兴的是支持不同产品团队升级基础设施和数据库的咨询公司，”Gebbe 评论道。“我们真的浪费了时间，没有为我们的客户开发功能。”

## 不要从头开始构建
是时候尝试一些不同的东西了，灵感来自其他组织的平台故事。

Hellmann 团队决定“从为什么开始”，Pörtner 接过 PlatformCon 的麦克风说道，引用领导力大师 [Simon Sinek](https://x.com/simonsinek)。“我们定义了使命宣言：我们努力释放所有开发人员的潜力，以塑造数字未来和人类的成长。”

由此，平台团队确定了七个支柱：

- 透明度
- 信任
- 自动化
- 创新
- 自主权
- 以开发人员为中心
- 安全
平台工程是关于定义 [最佳路径](https://thenewstack.io/how-to-pave-golden-paths-that-actually-go-somewhere/)，以最小的阻力发布软件。牢记这七个价值观，清晰的路径是通过云，以 [Kubernetes 配置管理](https://thenewstack.io/the-new-basics-of-configuration-management-in-kubernetes/)、源代码管理和 [CI/CD](https://thenewstack.io/ci-cd/) 为基础。

Pörtner 是一位平台工程师，他引用了软件开发人员常见的 [非我所创综合症](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9310.1982.tb00478.x)，表示团队最初认为他们应该自己从头开始构建。

“我们在自己的集群中部署了数据库。这不是一个好主意，”他说。“最好是基于现有的东西构建平台——我们正好有一个云提供商。”

事实上，托管云服务和自动化 [始终优于](https://thenewstack.io/want-to-save-the-world-start-by-cutting-your-cloud-costs/) 任何自管理方式。通过使用托管服务来部署数据库，Hellmann 平台团队能够将更多工作负载迁移到云中，并加快多个团队使用的功能的集成，而无需承担构建、部署和管理的成本。

## 构建最小的可行平台
在铺设这条黄金之路时，平台工程的共同目标是实现自助服务，以避免充满摩擦的工单编写和人为干预重复性工作。但尝试过早地过度自动化可能会带来更多麻烦。

“我们认为自助服务当然很重要，”Pörtner 说，但“最好不要过度设计所有东西，构建越来越多的功能，因为这样你的团队就会开始遇到问题，因为它变得更加复杂。”

如果平台工程不是逐步进行，就会有成为过时的、自上而下的庞大平台的风险。

[团队拓扑](https://thenewstack.io/how-team-topologies-supports-platform-engineering/) 是现代软件组织中流行的模型，建议从一个名为 [最小的可行平台](https://thenewstack.io/documentation-is-more-than-your-thinnest-viable-platform/) (TVP) 的概念开始——你可以构建的最基本的东西，它可以使你的开发人员客户的生活更轻松。这通常是一个轻量级的维基或某种文档。
这可以在最小可行产品格式中发布，以便快速反馈，而无需长期投资，但 [TVP 不同于最小可行产品 (MVP](https://thenewstack.io/mvp-or-tvp-why-your-internal-developer-platform-needs-both/))，因为任何内部开发人员平台都是你必须构建和维护的东西。

“这是我们从错误中吸取的教训，”Pörtner 说。“我们了解到我们应该寻求更多反馈，并向他们展示我们所做的事情。”

在平台工程中，你的开发人员同事是你的客户，这应该使快速反馈变得容易，但情况并非总是如此。
“当我们问他们的时候，他们的反馈是‘让它工作’，因为有时他们参与了产品开发，他们没有时间回答你的问题或提供反馈，或者有时他们不知道真正的反馈是什么，”他说。

或者，有时如果平台不是他们真正需要的，工程师会开始构建临时解决方案。

Hellmann 平台团队必须负责平台的演变

## 主导客户关怀
内部开发者平台以其可选性而著称。这意味着你必须说服你的同事使用它。

像所有好的产品追求一样，[平台即产品思维](https://thenewstack.io/platform-engineering-demands-a-product-mindset/) 依赖于快速反馈和开放式沟通。在 Hellmann，这包括：

- 冲刺评审
- 架构决策记录
- 事后分析
- 产品路线图和即将推出的功能

该组织还添加了一个帮助中心，开发者可以在那里提问和提交问题。

除了发布这些信息之外，平台团队还会向其客户征求需求。同样，这可能是一场斗争，因为应用程序团队忙于产品开发，这就是为什么平台团队聘请了一位产品负责人，以优先考虑利益相关者的需求。

产品负责人 Pörtner 说，“这个人可以与团队交谈，优先考虑事情，并找到一种方法来穿越构建平台时所有可能性的丛林，并识别痛点。”

平台团队需要意识到，他们不仅仅是在构建闪闪发光的或他们认为最好的东西。

“最终，像依赖项自动化工具——[Renovate](https://github.com/renovatebot/renovate)，[Dependabot](https://github.com/dependabot)——[可观察性](https://github.com/dependabot) 解决方案和秘密管理为开发人员节省了难以置信的时间，这对我们和团队来说确实是一个改变游戏规则的东西，”Pörtner 说。“然后他们开始欣赏我们的平台。我们感觉我们现在正朝着正确的方向前进。”

但是，平台团队仍然习惯于构建太多功能。繁忙的产品团队没有时间进行如此多的更新，因此平台团队养成了代表他们实施更改的习惯。这在规模上行不通。

“你必须以一种他们可以轻松集成的方式构建你的平台，”Pörtner 说。“因此你需要文档和培训。让我们向他们展示如何使用它，并给他们自己动手操作的可能性。”

## 不要一次性让所有团队加入
是的，内部开发者平台专注于共享工具和流程，但并非每个人都会有相同的切入点。

如此庞大的组织总是会存在不同的知识和技术经验。Hellmann 的一部分已经采用云原生，而其他部分则在本地工作。

“我不会对你撒谎。有时这很难，你必须有耐心，你必须教他们，”Pörtner 说，并进一步警告说，“有时它会有点迷失。平台开发的很大一部分是记录东西，并培训你的开发人员使用你的平台做正确的事情。”

除此之外，平台工程团队通常只有几个人支持各种各样的团队。

“花时间让每个团队都加入你的平台。”Gebbe 补充道。“找到你的道路。你可能不是 [Netflix](https://thenewstack.io/developer-productivity-engineering-at-netflix/) 或者 [Spotify](https://thenewstack.io/spotifys-backstage-roadmap-aims-to-speed-up-adoption/)，但你需要找到你的方式，让你的开发人员提供一个好的平台。”

平台工程策略既是你的组织独有的，也是需要随着时间推移而培养的。

正如 Gebbe 所说，“你必须建立一个真正好的土壤，一个好的基础，花朵和蝴蝶就会来，他们会对你的平台感到满意。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等等。
](https://youtube.com/thenewstack?sub_confirmation=1)