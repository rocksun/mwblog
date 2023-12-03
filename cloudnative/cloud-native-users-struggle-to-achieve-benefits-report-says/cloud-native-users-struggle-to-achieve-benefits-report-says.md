<!--
title: 云原生用户难以实现效益
cover: https://cdn.thenewstack.io/media/2023/11/d5734667-cloud-native-lightning-1-1024x576.jpg
-->

已“上云”组织95%称难见实益，UST Foundry新调查显示，那些已经“采用云原生”的组织中，大多数人表示当前面临的挑战让其难以看到云原生全部的效益。

> 译自 [Cloud Native Users Struggle to Achieve Benefits， Report Says](https://thenewstack.io/cloud-native-users-struggle-to-achieve-benefits-report-says/)，作者 Charles Humble 是一位前软件工程师、架构师和 CTO，曾担任技术和内容组的高级领导和执行官。他于 2014-2020 年担任 InfoQ 的总编辑，并于 2020-2023 年担任 Container Solutions 的首席编辑......

[根据一项新调查](https://www.ust.com/en/insights/cloud-native-app-dev)，对于已经采用[云原生](https://thenewstack.io/cloud-native/)方法的 82% 的组织来说，这一转变并没有完全实现其承诺。

在已经"采用云原生"的组织中，95%的组织报告说，挑战正在阻碍他们看到云原生开发的全部优势。

主要挑战包括：适应云端的传统流程(46% 的[云原生用户](https://thenewstack.io/5-things-to-know-before-adopting-cloud-native/)引用)、培训他们的开发团队(也有 46% 的报告)以及像测试、部署和监控等流程的自动化(44%)。

调查显示，这些挑战产生了连锁反应。用户在安全性、工具扩张和文化困难(包括开发者、安全和运维之间的差强人意的协作)方面遇到问题。

这项在 9 月由 [Foundry](https://foundryco.com/)([IDG](https://www.idginc.com/) 的全资子公司)为 [UST](https://www.ust.com/?utm_content=inline-mention)(一家数字化转型服务公司)进行的在线调查，共抽样了 100 名 IT 专业人士和高管。

受访者在 IT 或执行管理角色的大型企业受雇，这些企业正在测试、试点或采用云原生开发方法和工具。近一半来自 C 套房，高级工程师和 IT 经理占其余部分。

## 定义云原生

虽然样本量小，但这项调查表明，向云原生开发过渡中涉及的一些有趣的趋势和一些挑战。

需要在这种背景下考虑这项研究的发现：与像[云原生计算基金会](https://cncf.io/?utm_content=inline-mention)这样的机构接受的"云原生"的[定义](https://github.com/cncf/toc/blob/main/DEFINITION.md)相比，研究人员使用的定义明显更广泛。

云原生也许正遭受着一个日益模糊的定义——软件开发者和作者[马丁·福勒](https://martinfowler.com/)极妙地称之为"[语义扩散](https://martinfowler.com/bliki/SemanticDiffusion.html)"。正如 [Red Hat](https://www.openshift.com/try?utm_content=inline-mention) 的高级首席软件工程师 [Holly Cummins](https://www.linkedin.com/in/holly-k-cummins?originalSubdomain=uk) 向 The New Stack 表示，"我经常认为我们只是将云原生作为‘现代化和不错’或者‘在 2020 年代建立的’的同义词。"

也就是说，这项调查中表明的有趣之处——特别是[低码/无码工具](https://thenewstack.io/low-code-vs-no-code/)的广泛使用，在某些行业中使用率为 57%，以及对[生成式 AI](https://thenewstack.io/how-generative-ai-can-support-devops-and-sre-workflows/) 的浓厚兴趣。

后者或许并不令人惊讶，考虑到我们在 [AI 炒作周期](https://thenewstack.io/steve-wozniak-on-tesla-artificial-intelligence-apple/)中的所处位置，但看到低码工具获得这种水平的采用却令人惊讶。或许这显示了与其前身相比，当前一代低码工具有了多大的改进，正如我们在[查看 WS02 的 Choreo 时指出的](https://thenewstack.io/choreo-a-serverless-platform-for-building-cloud-native-apps/)那样。

## 是什么激励了云迁移？

大多数调查受访者将成本效率和业务敏捷性列为向云迁移的主要驱动因素。可扩展性的得分也很高。

这与我自己的经验相吻合。正如Anne Currie和我在我们的书 [The Cloud Native Attitude](https://info.container-solutions.com/the-cloud-native-attitude-2nd-edition) 中指出的，速度、规模和利润率的某种组合是公司从自己的数据中心迁移到云的最常见原因。有趣的是，这项调查还强调了改善运维、开发人员和 SRE 之间协作的更文化方面的作用，37%的公司引用了这一点。

调查参与者引用了与分布式、云架构相关的各种技术的采用水平：

- 60% 的受访者在其应用环境的一个或多个区域采用了[微服务](https://thenewstack.io/microservices/)
- 55% 的人说他们正在使用[无服务器](https://thenewstack.io/serverless/)。
- 不到一半(49%)的人也在其应用环境的一个或多个区域采用了 [Kubernetes](https://thenewstack.io/kubernetes/)，另有 41% 正在评估或计划评估这个容器编排巨头。

## 云转型的技术挑战

正确实施的微服务和无服务器与提高业务敏捷性的目标紧密契合。然而，为此，您需要独立部署的单元，这反过来又意味着正确定义服务边界，这是许多人困难的领域。如果最终您的 [CI/CD](https://thenewstack.io/ci-cd/) 流水线不得不一起部署许多甚至全部微服务，那么您可能没有获得任何好处。

如果您确实正确定义了服务边界，您将能够更快地构建新功能并获得强大的水平可扩展性，但运营复杂性的代价很高。这种复杂性让[网飞](https://www.infoq.com/presentations/netflix-monitoring-system/)和 [Facebook](https://research.facebook.com/publications/scuba-diving-into-data-at-facebook/) 等公司构建自己的[可观测性](https://thenewstack.io/observability/)工具，后来通过开源和先驱供应商(如 [Honeycomb.io](https://blog.container-solutions.com/charity-majors-on-code-rewrites-observability-and-team-performance))更广泛地可用。

在调查中，我们可以看到 31% 的公司注意到错误检测时间更长，29% 的公司提到应用环境中可见性/可观测性降低，这反映了这一挑战，这更可能是大型企业(这里定义为年收入 100 亿美元或更多)引用的问题。

在 45% 的企业中，开发人员的安全责任范围有所增加，可能是采用[“左移”方法](https://thenewstack.io/shift-left-where-cloud-native-computing-security-is-going/)的后果，更大型的企业受到的影响更大。

2022 年 Shadowserver Foundation 的报告作为一个相关情况指出，[全球范围内超过 38 万个 Kubernetes API](https://www.shadowserver.org/news/over-380-000-open-kubernetes-api-servers/?utm_source=thenewstack&utm_medium=website&utm_content=inline-mention&utm_campaign=platform) 暴露在公共互联网上。这反映了开发人员面临的日益复杂的情况。分布式环境增加了攻击面，缺乏可见性会加剧这个问题。

在 UST 调查中开发团队引用的其他痛点包括:

- 复杂性/工具过载(43%)
- [与 IT 运维和/或安全运维团队之间的沟通不畅](https://thenewstack.io/part-2-how-checklists-on-github-and-gitlab-can-help-team-collaboration/)(41%)
- 在不引入风险的情况下提高生产力的压力(40%)。

## 太多选择？

假设如果我们给予开发人员更多的自主权来选择他们想要的工具和语言，他们将更快乐、更有生产力，这是一个错误。根据我的经验，如果这些选择已经为开发人员做出，只要他们能够在特定需求需要时做出不同的决定，开发人员通常更喜欢。

Red Hat 的 Cummins 说："除了左移，我们还应该考虑向下移动。不要只扩大一名工程师的角色；通过增加的自动化和改进的策展，将一些有点无聊、乏味和重复的东西下移并纳入我们的平台。通过这种方式，我们可以从更高价值的平台中受益，而不是让这些技术成为额外的负担。"

UST 云咨询高级总监 [Carl Coryell-Martin](https://www.linkedin.com/in/carlcoryell?originalSubdomain=ca) 回应了同样的感受，他认为调查中的许多组织没有实施平台工程，或者没有正确实施平台工程。

他说："我认为 Kubernetes 在开发团队层面上非常危险，您可以从生产力和风险之间的权衡以及安全工作负载的增加中看到问题信号。公司没有理解或投资于平台工程学科。"

## 投资于平台

这种对平台工程投资不足通常是由于更大型组织中的资金运作方式。

在我今年早些时候与 [Syntasso](https://www.syntasso.io/) COO Paula Kennedy 一起制作的 “[Hacking the Org](https://sites.libsyn.com/406853/syntasso-coo-paula-kennedy-on-platform-team-responsibilities-patterns-and-anti-patterns)” 播客中，我们接触了一些反模式，例如当资金与产品团队一起存在时，平台团队最终会资源匮乏。肯尼迪认为这是因为“平台团队只被视为另一个基础设施成本”。

Coryell-Martin 回应了这个想法，他告诉 The New Stack，“平台工程很难支付，因为它是一个新的、开发起来很昂贵的功能。一个典型的业务客户会更倾向于在构建他们的应用程序上增加 10% 的投入，而不是为平台的开发支付费用。”

此外，他补充说，“尽管有效的平台工程的好处可以扩展到所有业务结果，但它只有在您能改变团队的工作方式时才有效。”

他提供的一个建议是在个别团队层面上建立概念验证。这使您可以向一个团队展示他们能够以更快的速度和更高的质量交付软件的能力。然后，Coryell-Martin 说，“您需要与 CFO、CIO 或 CTO 进行对话，在对话中讨论如果交付更高质量，您可以获得的业务收益。” 

我要补充的是，[作为开发人员和软件团队](https://thenewstack.io/managing-software-development-team-dynamics-from-within/)负责人，我们也需要更好地用业务术语表达我们的论点。如果没有明确定义的商业利益，就没必要试图说服业务赞助商投资平台、更多自动化或支付技术债务。

## 云原生文化

Coryell-Martin 强调的另一个问题是：“成功的许多障碍是交织在一起的，要实现云原生开发的转型结果，您需要解决所有这些问题。这不是‘我解决一个，生活变好 10%，然后我解决第二个，生活又变好 10%’的情况。相反，每个都使生活变好约 2%，但当您解决整套 10 件事时，您的生活会变好 100%。”

这一系列事情包括文化方面的内容以及技术内容。Cummins 甚至说过，“[云原生关系文化，而不是容器。](https://blog.container-solutions.com/cloud-native-is-about-culture-not-containers)”

Cummins 说，这次新的调查结果强调了这一点。她说：“云原生很难，您必须考虑人这一因素。”她说。“虽然一些挑战是技术性的，但如此多的挑战涉及人们没有技能，或者存在的业务流程没有他们希望的那么多的修复。所以，如果迁移到云原生的动机是敏捷性，仅仅这些技术并没有改善协作，这仍然是一个难点。”

即使在成本是主要驱动因素的情况下，这也可能是真的，因为通常驱动成本上涨的就是缺乏有效的协作。

Cummins 重申，仔细考虑您正在尝试解决的问题真的很重要：“如果您匆忙行事，希望提高敏捷性，那是无济于事的。”

成功的协作需要您具有强大的[心理安全感](https://thenewstack.io/5-ways-to-build-psychological-safety-at-fast-moving-startups/)。Cummins 说：“云原生转型成功的先决条件是人们必须信任组织，这样员工就不会花费所有的精力来保护他们拥有的东西。”

同样，如果人们认为工作有被裁员的风险，他们会不愿意告诉您事情。Coryell-Martin 说：“如果我认为我的朋友会被裁员，因为在您解决了该问题后，您需要的员工更少了，那么我不会告诉您有关低效的地方。”

在任何大型转型中，您也有 IT 员工会变得更加熟练和有价值的风险——然后他们会离开，寻找更有吸引力的机会。

Coryell-Martin 说：“我遇到过这么多次的情况，一家公司正在转型，然后他们最好的人才会离开公司。” 一定程度的流失是不可避免的，但您需要确保您的薪酬是与市场价值相称的。

这一切听起来相当消极。但 Coryell-Martin 说，面对云原生转型的挑战对许多组织来说是值得的。

他说：“通过云原生，可以创建一套工作关系、团队结构、平台工程工具和功能，使结果提高 10 倍。”团队更满意，因为他们交付了更好的软件，所以他们的业务客户也更高兴，而他们的控制人员也更放松，因为它更安全。

Coryell-Martin 说：“如果您在平台上管理风险，并将大部分风险从团队层面中消除，那么生产力和风险之间就不会有权衡。一个更美好的世界确实是可能的。”
