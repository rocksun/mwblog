# 利用开源 CNOE 框架构建 IDP

![Featued image for: Building an IDP With Help From the Open Source CNOE Framework](https://cdn.thenewstack.io/media/2024/08/2a48fc20-building-an-idp-with-help-from-the-open-source-cnoe-framework-1024x576.jpg)

纽约 - 如何为一个组织构建一个[内部开发者平台](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/)，该组织经常会遇到大量的在线流量激增，并且其开发者已经习惯了高度的自主权？

以及如何从不断增长的工具选项中进行筛选，以标准化组织的工具？

这些是《纽约时报》平台团队面临的问题，这家拥有 170 多年历史的全球新闻机构。近年来，这个曾经以传统为重的组织[大力投入数字世界](https://thenewstack.io/a-candid-assessment-from-the-new-york-times-cto-with-serverless-and-the-1990s-in-mind/)，不仅提供全球新闻和思想领导力，还提供大量受欢迎的功能：利基兴趣新闻通讯、烹饪应用程序、Wirecutter 消费者指南，当然还有[Wordle](https://thenewstack.io/programmers-explore-the-secrets-of-wordle/)。

随着《纽约时报》创建了新的环境，其大约 1000 名开发者和工程师也随之发展。而这正在成为一个问题。

在 5 月份的[纽约 Kubernetes 日](https://www.kcdnewyork.com/) 上的演讲中，《纽约时报》的软件工程师[Luke Philips](https://www.linkedin.com/in/lukephilips/) 描述了该公司在构建自己的内部开发者平台 (IDP) 之前的情况。

Philips 说，与其他组织一样，《纽约时报》拥有[大量的 Kubernetes 集群](https://thenewstack.io/neglect-kubernetes-resource-management-at-your-peril/)，在基础设施配置、代码交付和部署方面采用了混乱的各种方法：[混合使用云原生工具](https://thenewstack.io/how-to-tackle-tool-sprawl-before-it-becomes-tool-hell/)，包括单集群和多集群环境，开发者负责其基础设施的整个升级生命周期，嵌入式[DevOps/站点可靠性工程师](https://thenewstack.io/platform-engineering/sre-vs-devops-vs-platform-engineering/) 的功能团队管理自己的集群。等等。

Philips 说，很多开发者都有自己的集群，这增加了复杂性。

大约三年前，《纽约时报》启动了[平台工程计划](https://thenewstack.io/platform-engineering/)，构建了它称之为交付共享工程平台 (DSP) 的平台。

该项目由《纽约时报》的使命和作为组织的独特需求塑造，但也受到一组称为[云原生运营卓越 (CNOE)](https://cnoe.io/)（发音为“KUH-noo”，像一艘小船）的开源指南的影响。这就是《纽约时报》如何在约 60 名平台团队成员（该组织称之为“交付工程”团队）的帮助下构建其 DSP 的故事。

Philips 和他的同事[Tiara Sykes](https://www.linkedin.com/in/tiara-sykes/) 说，这是一个正在进行的工作，但早期迹象令人鼓舞，Sykes 也是纽约 Kubernetes 日的演讲者。

Philips 告诉 The New Stack：“我认为，我们公司大约 25% 的工作负载都在这个托管的 IDP 体验中。我们的目标是让每个人都迁移到那里。”

## 平台工程入门

Philips 在 Kubernetes 日的演讲中说，《纽约时报》的使命是“为每个寻求了解和参与世界的英语母语的求知者构建必不可少的订阅包”。

为了构建其内部平台，推动该项目的团队需要对客户最需要什么表现出好奇心。

Sykes 在演讲中说：“您的平台支持是让产品工程师、产品经理和其他领导层使用它的起点。一些指导和评估支持模型的问题可能是，平台开发者或产品开发者想要从平台获得什么，以及他们在开发新产品时会感受到什么样的支持？”

她说，理想的开发工作流程将让开发者专注于功能交付，专注于编写高质量代码，“用测试覆盖它，并使用他们的总线模式来实现它，以保持代码库的可维护性。”

然而，她指出，“这与现实相去甚远。” 需要构建基础设施，并且开发者必须存储和部署其代码的工件。
她说，一旦代码部署完成，“仍然存在路由、DNS [监控和可观测性](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/)——这些任务本身就非常庞大，需要大量的时间、精力和知识，还要了解安全威胁和最佳实践。”

《泰晤士报》需要为开发人员提供一条[“黄金路径”](https://thenewstack.io/heres-one-golden-path-to-build-an-mvp-enterprise-idp/)，一套标准化的自助服务工具，并方便地访问[文档](https://thenewstack.io/poor-documentation-is-costly-heres-how-to-fix-it/)，Sykes 说。此外，她说，它还需要提供“集中化的代码管理和部署管道、帮助在云中运行系统的基础设施，以及帮助团队了解和操作其系统的可观测性工具。”

## 什么是 CNOE？
与《泰晤士报》的平台项目同时进行的是，一项创建构建 IDP 指南的开源工作正在蓬勃发展。去年 10 月，五家公司——Adobe、[亚马逊网络服务](https://aws.amazon.com/?utm_content=inline+mention)、Autodesk、Salesforce 和[Twilio](https://www.twilio.com/?utm_content=inline+mention)——[共同发起 CNOE](https://aws.amazon.com/blogs/opensource/cloud-native-operational-excellence-cnoe-a-joint-effort-to-share-internal-developer-platform-tools-and-best-practices/)；Intuit 和耐克随后也加入了支持 CNOE 的行列。

CNOE 是一种框架，旨在汇集处于相同平台旅程的企业的最佳实践。

根据该项目网站，该框架旨在帮助规模相似的组织“共同应对其运营技术决策，降低其工具选择的风险，协调贡献，并为大型企业提供有关使用哪些[sponsor_inline_mention slug="cncf" ]云原生计算基金会[/sponsor_inline_mention]技术以实现最佳云效率的指导。”

《泰晤士报》交付工程团队的成员开始参加 CNOE 社区会议。“我们只是开始倾听和学习，”Philips 说。当他们开始构建自己的项目时，团队成员能够“利用这些其他工程师的智慧。我们不必雇用所有为我们工作的工程师——我们可以从彼此的经验中分享协作学习。”

CNOE 项目包括一些平台工程中最常见任务的模板，包括一个[IDP 构建器](https://github.com/cnoe-io/idpbuilder)——已预发布，目前仍在积极开发中。该工具可以帮助用户使用[Kubernetes](https://thenewstack.io/streamline-platform-engineering-with-kubernetes/)、[Argo](https://thenewstack.io/gitops-on-kubernetes-deciding-between-argo-cd-and-flux/) 和[Backstage](https://thenewstack.io/spotifys-backstage-a-strategic-guide/)（Spotify 工程师创建的内部开发人员门户模板）启动 IDP，只需要[Docker](https://www.docker.com/?utm_content=inline+mention) 作为依赖项。

Philips 在 Kubernetes Day 观众面前表示，另一个仓库[“cnoe-cli”](https://github.com/cnoe-io/cnoe-cli) 将帮助创建 Backstage 的脚手架[自定义资源定义 (CRD)](https://thenewstack.io/kubernetes-crds-what-they-are-and-why-they-are-useful/) 用于用户自己的 CRD。GitHub 项目还包括用于 CNOE 堆栈使用的[Argo 工作流的 Backstage 插件](https://github.com/cnoe-io/plugin-argo-workflows)、用于[堆栈使用的 Backstage 镜像](https://github.com/cnoe-io/backstage-app) 以及用于[CNOE 及其工具在 AWS 云上的参考实现](https://github.com/cnoe-io/reference-implementation-aws) 的仓库。

CNOE 网站还包括[“技术雷达”](https://cnoe.io/radars)，这些雷达是社区成员关于他们用于不同任务（例如服务网格或 CI/CD 管道）的各种工具的数据可视化，以及每个工具目前在评估-试用-采用连续体中的位置。

## 开始构建内部平台
《泰晤士报》DSP 的核心是集中运营和管理的一组 Kubernetes 集群，用于开发、登台和生产。

“团队和开发人员不再需要维护自己的基础设施，”Philips 在 Kubernetes Day 演示中说。

他补充说，“我们在集群中提供不同的多租户空间。每个团队的操作都与其他团队的操作分开，并使用我们的后端安全控制。”

以下是 DSP 的 Kubernetes 集群的简化视图：

DSP 需要提供某些功能，才能作为《泰晤士报》开发人员的自助服务平台无缝运行。以下是所需的功能：

“我们开始逐步构建我们的平台，利用最优秀的 CNCF 和开源项目，Kubernetes 作为我们的基础计算平台，以及一个相关的专门团队，”Philips 在他的演示中说。
“除了 Kubernetes，您还需要添加一个声明式配置管理工具，遵循 GitOps 最佳实践并添加 Argo CD，以及另一个专门负责应用程序交付的团队。最后，我们想添加一个开发者门户——Backstage 看起来是正确的选择——以及另一个专门的团队。”

以下是 CNOE 的可视化图表，菲利普斯和赛克斯在他们的演示中使用了该图表，该图表展示了该项目的建议工具选项。

在她的演示中，赛克斯将此可视化图表称为“一套技术，之所以选择它们是因为它们之间如何无缝地协同工作。希望这个子集能够消除错误选择的痛点。”

## 平台团队的经验教训
菲利普斯和赛克斯分享了他们在该项目中吸取的经验教训。

首先：做一个好的倾听者很重要。随着平台的扩展，工具选择有时需要重新考虑；即使在一个组织内部，某些工具也不适合所有用例。

菲利普斯告诉 The New Stack，在为开发人员提供服务时，目标“不是仅仅告诉他们这是必须遵循的方式，而是要了解他们在做什么。如果这不是他们习惯使用的工具，我们如何才能接触到他们？”

《纽约时报》的内部平台项目仍在进行中。组织的各个部门需要在一年中的特定时间快速扩展——例如，烹饪应用程序在感恩节前后流量最大。新闻部门在即将到来的美国总统大选前将迎来读者数量的激增。

“所以我们已经完成了新闻的转换，我们已经为 11 月的目标做好了准备，我们等待着这一切的发生，”菲利普斯告诉 The New Stack。接下来，“我们将处理其他事情，其他具有不同影响的迁移可以接踵而至。”

他建议那些希望效仿《纽约时报》努力的组织，要逐步前进，并在投入生产之前处理好所有细节：“中间有很多粘合剂，比如所有安全加固、多租户等等。”

菲利普斯承认，“我们一直在埋头苦干，做着艰苦的安全工作。我们的开发者体验有点粗糙。”

但随着 25% 的工作负载已经迁移到 DSP，他对更多采用该平台的前景仍然持乐观态度。

在演示过程中，一位观众询问如何说服习惯于管理自己的 Kubernetes 集群的开发人员迁移到共享集群。

“你只要把呼叫器给他们，”菲利普斯说。“凌晨 2 点，你想运行这个吗？这是正确的激励平衡。你能运行这个——而不是某个人，或者一群人，他们可能会优化它？

他提出了开发者生产力核心问题：“你如何才能最好地利用接下来的一个小时？”

## CNOE 的下一步计划？
在 Kubernetes Day 演示中，赛克斯建议那些希望构建自己的共享自助开发平台的组织查看 CNOE 及其 [在线功能路线图](https://cnoe.io/docs/category/technology-capabilities)。

“你可以详细了解这些功能，注意他们推荐的最佳实践以及一些演示、模板化的示例，”她说。

赛克斯还建议查看该项目的双周社区会议和专门针对该项目的 CNCF Slack 频道：“你也可以通过在 GitHub 上提交与你如何操作 IDP 相关的 issue 来做出贡献。”

总的来说，CNOE 是构建内部平台的蓝图，但不是万能的解决方案，赛克斯在 Kubernetes Day 观众面前说。

“你的平台将取决于你的产品工程师的需求以及你的业务需求，”她说。她补充说，CNOE 是一个团队最初关于构建其 IDP 的对话的“良好起点”。

“这样，你就不会走上遇到问题的弯路。尝试从那里找到一个提供整体概述的解决方案。在开始旅程之前，先让你的 GPS 导航正常运行。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等等。
](https://youtube.com/thenewstack?sub_confirmation=1)