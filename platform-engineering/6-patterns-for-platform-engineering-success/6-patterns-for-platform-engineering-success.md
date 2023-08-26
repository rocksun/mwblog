# 平台工程成功的六种模式

从 PlatformCon 2023 大会的演讲者那里学习平台工程的最佳实践，包括由谁构建什么，遵循哪些框架和蓝图。

翻译自 [6 Patterns for Platform Engineering Success](https://thenewstack.io/6-patterns-for-platform-engineering-success/) 。

![](https://cdn.thenewstack.io/media/2023/08/e764b5c7-platform-patterns-1-1024x576.jpg)
*图片来自 Unsplash 的 [Claudio Schwarz](https://unsplash.com/@purzlbaum?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)*

毫无疑问，IT 工具选择是令人不知所措的——只需浏览一下[云原生计算基金会](https://cncf.io/?utm_content=inline-mention)的[图景](https://landscape.cncf.io/)，它跨越数个屏幕，充满了各种微小的图标。

《The New Stack》的出版商 [Alex Williams](https://thenewstack.io/author/alex/) 在 [2023 年的 PlatformCon](https://platformcon.com/) 大会上发表了观点，特别强调在[平台工程](https://thenewstack.io/platform-engineering/)社区中，“人们对于如何构建强大的内部开发者平台，如何设计架构以及使用哪些工具的指导需求很高”。

在如此众多的选择中，问题远多于清晰的答案：

- 自建还是购买 — 还是购买并定制？
- 选择开源平台还是私有平台？
- 如何整合现有的工具和工作流程？
- 部署在单一云、多云还是混合云，一些工作负载是否在本地部署？
- 如何在现有设置的基础上构建现代的内部开发平台[IDP]？
- 谁负责这个平台 — DevOps、运维、系统管理员还是一个平台团队？
- 如何与开发人员建立紧密的反馈循环？

最重要的是，[你的内部开发人员实际上需要什么](https://thenewstack.io/which-features-does-your-platform-engineering-portal-need/)？

今天，我们将揭示出几种新兴的模式，并强调一些反模式，因为年幼的[平台工程](https://thenewstack.io/platform-engineering/)社会技术学科正处于发展初期。以下是来自 PlatformCon 大会关于[现代平台工程蓝图](https://www.youtube.com/watch?v=lIDb6J78aDo&ab_channel=PlatformEngineering)的讨论的亮点，希望您和您的团队能够找到适合自己的独特方式，从而使用开发人员真正想要使用的平台。

## 1. 认识到你的平台将是独特的。

现代组织的内部开发平台（IDP）是什么？这是一个没有明确答案的关键问题。

在讨论中，荷兰电子商务公司 Bol.com 的平台工程师 [Anastasija Efremovska](https://www.linkedin.com/in/anastasijaefremovska/) 表示：“这与你所谈论的公司非常具体相关。较小公司的用户界面模板或蓝图效果非常好，但一旦涉足企业，你确实需要更多样化的方法。”

随着规模的扩大，您需要为不同的技能和工程师类型提供支持，很可能还必须满足更多的合规性和安全性需求。所有这些都可以转化为从蓝图到CLI的IDP，可能是任何事物。

“我们对于 ID 的第一印象是有一个用户界面，我们正在为新的服务或资源提供支架，”[Humanitec](https://humanitec.com/?utm_content=inline-mention) 的 CEO [Kaspar von Grünberg](https://www.linkedin.com/in/kvgruenberg/) 说道。但他补充说：“那只是整体中的一小部分，而且聚焦有点狭窄。”

Von Grünberg 认为，IDP 蓝图必须考虑应用程序的整个生命周期。

他说：“我真的认为你不能将这归结为工具，因为企业的现实是多 CI、多注册表、多一切。因此，并没有适用于平台工程的工具集，而是看你如何将它们结合起来。”

对于 Von Grünberg 来说，现代参考架构包括五个层面：

- **开发者控制平面**：版本控制系统与基础设施即代码，可能还包括工作负载规范或开发者门户，比如 [Backstage](https://thenewstack.io/spotifys-backstage-a-strategic-guide/) ，不同的个人组与整个平台互动。
- **集成和交付平面**：接受开发者的请求，并将它们与平台的基线配置同步。其中包括 [CI/CD 流水线](https://thenewstack.io/ci-cd/)、镜像注册表和平台编排器。
- **资源平面**：云或云、数据库、集群。
- **监控**、日志记录和可观察性平面。
- **安全平面**：例如策略层和[机密管理](https://thenewstack.io/the-challenges-of-secrets-management-from-code-to-cloud/)。

对于 Von Grünberg 来说，这些的组合就是内部开发者门户背后的东西。然后，您选择哪些工具来交付这个平台堆栈将取决于团队和组织的复杂性。

## 2. 弄清楚谁是老板。

[什么是平台工程师？](https://thenewstack.io/platform-engineering/platform-engineer-vs-software-engineer/)这是一个经常被搜索的短语，因为坦率地说，很多组织都在匆忙地以名义上采用平台工程。有时，人力资源部门只是将职位标题从系统管理员、DevOps 工程师或站点可靠性工程师（SRE）更新为“平台工程师”。

问题的一部分在于，当您的组织中没有人专门指定平台架构团队时，不同的角色可能会被指派这项工作。这些同事可能来自以下任一团队：

- 系统管理。
- [DevOps](https://thenewstack.io/devops/) 和 CI/CD。
- 运维。
- 安全性或站点可靠性工程（SRE）。
- 开发者体验或 DevEx 团队。
- 应用程序开发团队。

所有这些团队都应该以某种方式参与到创建您组织的平台中。它应该划分出一条更安全、无摩擦的生产路径。最终，它应该在您的 DevOps 或 CI/CD 流水线中融合。始终要记住，平台的目的是减轻应用程序团队的负担，这意味着他们应该能够提供充分的反馈意见，但他们很可能不应该构建整个平台。

“许多公司正在意识到需要策划使用这个平台的体验，因为存在着许多不同的系统，”开发者体验咨询公司 Frontside Software 的首席执行官 [Taras Mankovski](https://www.linkedin.com/in/tarasm/) 说道，他也是 [Backstage](https://github.com/backstage/backstage) 组织的成员之一。

他们会问类似于，开发者应该使用 Terraform 吗？Mankovski 说：“开发体验团队所从事的是一个过程：开发者有哪些困难，我们如何消除这种摩擦？”

这使得构建现代开发者平台有两个关键问题：

- 我们开发人员的苦差事是什么？
- 我们如何消除它？

这一切都归结于识别出 [Abigail Bangser](https://www.linkedin.com/in/abbybangser/) 称之为团队在组织中共享的“非差异性但并不不重要的工作”。你知道的，跨组织的优先事项，如安全性和部署速度，通常以相同的方式在整个组织中处理。这些事情是优先事项，但单个应用团队不会通过纠缠于这些事情来为最终用户带来差异化的价值。

不同的公司在平台发展的过程中可能有不同的阶段或目标。实际上，大多数公司根本没有从平台思维开始。可能已经有一个 DevOps 团队负责一些平台，比如 CI/CD 流水线。或许有一个负责[混沌工程](https://thenewstack.io/chaos-engineering-business-value/)、[监控和可观测性](https://thenewstack.io/observability/)的 SRE 团队。然后，当然，单个应用团队正在构建自己的东西或使用第三方工具——通常是为了绕过其他团队的障碍。

在我们与几家公司的交流中，平台的概念，或者根据 [Puppet](https://puppet.com/?utm_content=inline-mention) 的“[平台工程状况报告](https://www.puppet.com/resources/state-of-platform-engineering)”实际上是三到六个平台，有机地浮现出来。一个云工程师或 DevOps 工程师甚至可能意识不到他们已经成为了平台工程师——或者甚至不知道这意味着什么。

随着分散的平台逐渐演变为更具体、跨组织的平台战略，您需要明确谁负责——一个联系点和积压源。

哦，还有一件事。平台团队可能负责，但不要忘记老话，即“客户永远是对的”。如果你不听取内部开发人员客户的意见，并构建大多数人想要的内容，那么他们可能会再次绕过你强加给他们的任何东西。

## 3. 首先建立一种文化。

平台绝非新颖的概念。只是在当今，它是通过合作构建的，而以前更多是命令和控制。

“在平台工程出现之前，我们只是构建东西，然后期望我们的工程师和最终用户使用它，” Bol.com 的软件工程师 [Quiran Storey](https://www.linkedin.com/in/qstorey/) 说道。现在的关键是要思考您的内部用户实际上想要什么。

尽管工具选择很重要，但平台工程是一种固有的社会技术努力。这意味着培养开发者为先的文化是任何成功的重要部分。

“当我们开始讨论是否构建或购买平台时，我们需要首先问问自己和公司关于我们的心态、文化以及平台如何适应这个公司，” Mercado Libre 拉丁美洲电子商务平台的云和平台高级技术经理 [Juliano Marcos Martins](https://www.linkedin.com/in/julianommartins/) 说道。

毕竟，跨组织的沟通既是平台战略的一个好处，也是其成功的秘诀。公司文化支持平台，但平台工程也应该对文化产生积极影响。平台应该充当翻译器或透明度启用器，使 IT 能够更好地与业务价值保持连接，业务能够更好地了解 IT 作为大型成本中心的情况。

Martins 观察到，当平台团队从 DevOps 那里夺走职责时，可能会产生摩擦，这就是为什么他说 IDP 不应仅考虑开发者的角度，还应考虑公司的角度，从而改善治理、安全、效率、成本和上市时间等方面。

## 4. 维护一个 API 访问点。

“突然之间，我们的客户成了平台工程师，” Efremovska 说道。“你需要让他们满意，同时保持稳定性、安全性和可审计性。”

在她担任 Bol.com 平台工程师五年的时间里，她认为不应过于抽象事物，因为当工程师尝试弄清楚如何做事情或底层发生了什么时，这会增加他们的认知负荷。

应用团队从他们的平台中想要的东西之一是统一的访问方式。通过 API 来实现。

Efremovska 建议，平台 API 应类似于 Kubernetes 资源模型，您可以使用 Kubernetes API 作为访问许多不同云提供商和第三方提供的单一、一致的方式。

因此，一旦您发布了第一个平台原型或[最薄的可行平台](https://thenewstack.io/how-team-topologies-supports-platform-engineering/)，她建议您通过一个单一的内部 API 创建一个单一的访问点。然后您可以在其上创建模板。

## 5. 关注自助服务的目标。

平台团队不希望成为应用团队的另一个障碍。API 优先的设计对实现平台及其自动化的需求至关重要。您的应用团队希望能够选择、选择并使用平台的各个部分。

“良好的架构设计允许系统分散地增长，” von Grünberg 说。“用户可以说，这个金色的路径适合我，但如果对我不起作用，我知道如何扩展它并增加系统。”

任何扩展都可能后来被平台团队采用，以创建一个新的金色路径。

自助服务平台的另一个必备条件是可搜索的文档，这样您的开发人员就可以自己找到答案、操作指南、代码示例和错误代码定义。

## 6. 让开发人员驱动决策。

Storey 在启动您的平台之旅时的建议是：问问你的开发人员 80% 的时间需要做什么。

对于您发布的每个平台部分，您需要提供和维持[服务级别协议](https://thenewstack.io/sre-fundamentals-differences-between-sli-vs-slo-vs-sla/)、黄金路径、[文档](https://thenewstack.io/an-engineers-best-tips-for-writing-documentation-devs-love/)、合规性和支持。Mankovski 提醒我们，与其不得不推销类似于单块式的内部更新，不如努力发布和采用较小的成果。这也可以保持一个更紧密的开发者反馈循环。

“在提供的内容上要明智，因为这样会成为平台团队的运营负担，”这个团队负责维护和处理您创建的复杂性或技术债务。Storey 呼应了减少复杂性的最薄可行平台的方式：“如果您提供一件事并且做得很好，宁愿这样做，也不要提供一堆质量都一般的东西。”

想要了解更多关于平台工程的知识吗？预注册以接收即将发布的电子书“平台工程：您现在需要了解的内容”，该电子书由 [VMware Tanzu](https://tanzu.vmware.com/?utm_content=inline-mention) 赞助。

[![](https://cdn.thenewstack.io/media/2023/08/7dfbd08f-free-platform-engineering-book.png)](https://thenewstack.io/ebooks/platform-engineering/platform-engineering-what-you-need-to-know-now/)
