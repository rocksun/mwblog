<!--
title: Backstage五年：一切才刚刚开始
cover: https://cdn.thenewstack.io/media/2025/04/2e1cbd5f-chris-tyson-backstage-kubecon25-2.jpg
summary: Spotify开源的Backstage五周年啦！作为CNCF顶级项目，它定义了**平台工程**和**开发者门户**标准。拥有超3400家采用者和230+插件，集成**Argo CD**、**Grafana**等。新发布的AiKA插件，基于**RAG**，拥抱**AI**时代，助力企业提升**DevEx**和生产力！
-->

Spotify开源的Backstage五周年啦！作为CNCF顶级项目，它定义了**平台工程**和**开发者门户**标准。拥有超3400家采用者和230+插件，集成**Argo CD**、**Grafana**等。新发布的AiKA插件，基于**RAG**，拥抱**AI**时代，助力企业提升**DevEx**和生产力！

> 译自：[Five Years In, Backstage Is Just Getting Started](https://thenewstack.io/five-years-in-backstage-is-just-getting-started/)
> 
> 作者：Jennifer Riggins

伦敦 — 尽管 [Backstage](https://backstage.io/) 仅仅成立五年，但它确实是[平台工程](https://thenewstack.io/platform-engineering/)领域的佼佼者，已经[为内部开发者门户设定了标准](https://thenewstack.io/spotifys-backstage-a-strategic-guide/)。不仅在受欢迎程度方面，而且在开源社区的影响力方面也是如此。

Backstage 最初是音频流媒体公司 [Spotify](https://thenewstack.io/how-spotify-achieved-a-voluntary-99-internal-platform-adoption-rate/) 内部的一个开放生态系统，开发人员通过内部采购了一百多个插件来扩展其功能。在过去的五年里，它成为了一个大型开源项目，拥有超过 3,400 家采用者，包括 [Airbnb](https://thenewstack.io/platform-as-a-product-101/)、Booking.com、H&M、HCA Healthcare、[LEGO](https://thenewstack.io/how-data-helps-lego-click-developer-experience-into-place/)、OVO Energy、Philips、[Toyota North America](https://thenewstack.io/how-toyota-drove-agile-load-testing-to-the-cloud/) 和 [SeatGeek](https://thenewstack.io/case-study-how-seatgeek-adopted-hashicorps-nomad/)。现在，在创始公司之外，有超过 200 万的开发人员使用 Backstage。

去年，[用于构建开发者门户的 Backstage 开放框架](https://github.com/backstage/backstage) 是[云原生计算基金会](https://cncf.io/?utm_content=inline+mention) (CNCF) 在速度方面排名前五的项目之一。2023 年，它的提交次数比任何其他 [CNCF 项目](https://landscape.cncf.io/) 都要多。该开源项目已经在进行安全审计，以便加入 CNCF 的毕业项目。

Backstage 开源生态系统现在拥有大约 1,600 名贡献者，有 13,000 名开发人员获得了 [Backstage 认证](https://www.cncf.io/training/certification/cba/)。有超过 [230 个 Backstage 插件](https://backstage.io/plugins/)，包括那些与 [Argo CD](https://thenewstack.io/make-a-scalable-ci-cd-pipeline-for-kubernetes-with-github-and-argo-cd/)、[Datadog](https://www.datadoghq.com/?utm_content=inline+mention)、[GitHub Actions](https://thenewstack.io/boost-your-ci-cd-pipeline-automate-docker-with-github-actions/)、[Grafana](https://thenewstack.io/grafana-seeks-to-correct-observabilitys-historic-terrible-job/)、[Snyk](https://snyk.io/?utm_content=inline+mention) 和 [Terraform](https://thenewstack.io/new-terraform-features-manage-migrations-modules/) 集成的插件。[Spotify Portal](https://thenewstack.io/new-spotify-portal-for-backstage-eases-platform-engineering/) 是去年发布的预构建的内部开发者门户软件即服务 (SaaS) 产品。

在 [KubeCon + CloudNativeCon Europe](https://thenewstack.io/kubecon-cloudnativecon-eu-2025/) 上，The New Stack 与 Spotify 的平台和技术负责人 [Tyson Singer](https://www.linkedin.com/in/tysonsinger/) 和 CNCF 的 CTO [Chris Aniszczyk](https://www.linkedin.com/in/caniszczyk/) 坐下来，独家回顾了 Backstage 如何从内部开发门户发展成为拥有 [89% 市场份额](https://newsletter.getdx.com/p/backstage-and-the-developer-portal-market) 的开源框架。当然，他们还谈到了一些关于 Backstage 插件和 [人工智能时代平台工程的未来](https://thenewstack.io/whats-the-future-of-platform-engineering/) 的激动人心的消息。

## 开源铺平道路

Spotify 工程部门的目标是率先开源其创新成果（如其内部开发者门户框架），否则，其开发人员最终将被迫转向其他工具。

该公司在 [Kubernetes](https://thenewstack.io/kubernetes/) 方面吸取了惨痛的教训，当时 Spotify 最初为其容器编排选择了不同的供应商。后来，当 Spotify 不得不重新平台化到 K8s 时，因为该编排器在市场上胜出，Singer 说，此举使这家流媒体公司损失了 1000 万美元。他说，开源只是明智的经济选择。

一旦完成向 Kubernetes 的转变，Spotify 就会成为其自身开发者体验和开发者生产力的早期投资者。

“Spotify 早在很久以前就了解到的一件事是——在‘平台工程’这个[术语] 实际出现之前——你最终会面临一系列压力，这些压力会真正让你专注于改善开发者体验，”Singer 说。
我们当时在与世界上最大的公司竞争。我们发展非常迅速，我们需要真正专注于快速的功能开发，”他继续说道。“当我们减少在[那些]底层基础设施层上花费的时间时，我们将堆栈向上移动，以使这些功能开发人员能够更快地行动。”

随着科技行业迎来又一次经济衰退，他预测人们会更加重视开发者体验。公司必须以更少的资源做更多的事情。

“我们的许多科技公司[客户]都在考虑：如何提高员工的工作效率？” Singer说。“Backstage——以及一般的IDP——是一种非常非常有效的方法，可以使事情更简单[和]更相似。”

他的平台和工程组织的一个重点是弄清楚如何培养更多T型开发者：那些深入研究某个专业领域，但对其他领域也有很好理解的人。

在Spotify，这转化为后端开发人员能够进行快速的数据工程。但要实现这一点，整个数据生态系统、管道和端点都必须看起来相同。这是通过一个软件目录来实现的，该目录鼓励跨组织的发现和重用。

“我认为，随着我们提供越来越多的功能，我们看到越来越多的人说，‘这也是我们的问题，’”Singer说。然后，一旦你解决了主要的开发者体验问题，比如后端开发人员的问题，你就可以将这些解决方案复制到研发组织的其他部分，比如数据生态系统。

目前正处于现有Portal客户的alpha测试阶段，这个[Backstage的数据体验插件](https://backstage.spotify.com/docs/portal/guides/data-experience#overview)将很快发布到高级Portal产品中。该产品将：

- 使组织能够在Portal中发现、理解和管理业务数据。
- 从不同的数据源提取元数据，然后在Backstage软件目录中对其进行建模，从而在与所有其他软件实体相同的平面上提供对数据生态系统的可见性。
- 与数据仓库工具BigQuery、Redshift、Snowflake和dbt集成。
- 与Portal的核心功能集成，使团队能够以与软件完全相同的方式搜索、编目和管理数据集。

“现在我也可以在那里解决来自混乱数据生态系统的所有问题，使用相同的范例，”Singer说，“使用像Soundcheck这样的相同工具，它可以让你将质量驱动到你的生态系统中，整理生态系统，并达到每家公司[为]更快的开发和功能所需要的程度。”

Soundcheck是最受欢迎的Backstage插件之一，它专注于团队健康和围绕[DevOps最佳实践](https://thenewstack.io/devops/)的协调。

## 维护者、贡献者和用户

除了音频流媒体的核心使命外，Backstage还使Spotify成为一家开源企业。

“作为产品的维护者、贡献者和用户，面临的挑战之一是，你最初使用的东西可能与你发布的东西略有不同，”Singer说。

他称之为“钻石问题”的问题，出现在内部和开源项目出现分歧时。随着开源项目开始占据主导地位，内部团队努力将它们重新整合在一起。为了更具成本效益，Spotify团队一直在迁移和重构其自己的Backstage版本，使其更像开源版本。Singer说，这两个版本非常接近融合。

这场Jenga的[商业/开源游戏](https://thenewstack.io/entrepreneurship-for-engineers-from-open-source-to-monetization-profit/)也归结为工具和语言的选择。他将Spotify描述为“主要是一家[Google](https://cloud.google.com/?utm_content=inline+mention)商店”，这意味着他的平台团队通常会为[BigQuery](https://thenewstack.io/bigquery-pricing-a-users-guide/)和[Dataflow](https://cloud.google.com/products/dataflow)等数据产品构建。然而，由于[Snowflake](https://www.snowflake.com/?utm_content=inline+mention)也非常受欢迎，即使Spotify不使用它，数据体验插件也必须与之兼容。

“我们开发了这个插件，以便你可以与足够多的数据源集成，这样我们只需进行一些调整就不会太难，”Singer说。

“这是一个相当常见的模式，当我们采用我们在内部拥有的插件时，我们认为这些插件很有价值，并完成了每个人需要做的70%的工作。然后还有30%的工作，我们必须根据我们不使用的案例进行定制。”

最后，他补充说，这些看似无私的选择实际上是“质量的积极力量”，因为这些选择有助于Spotify抽象问题，同时加强领域边界。
在另一个福利方面，[PagerDuty](https://www.pagerduty.com/?utm_content=inline+mention) 目前是 Portal 的设计合作伙伴。Singer 说，由于 PagerDuty“在确保其插件成为最有价值的插件之一方面投入了大量工作”，因此该插件“对 Backstage 生态系统进行了工具化，并为 Spotify 开发人员提供了高质量的信号反馈”。

## 指标始终重要

由于[内部开发者平台](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/)或门户的特点是可选使用，因此采用率是衡量成功的关键指标之一。在关注外部使用情况之前，关注 Spotify 内部的情况非常重要。

所有开源社区的增长都是在 Spotify 开发者团队参与 Backstage 的同时实现的。Spotify 内部 Backstage 的采用率在所有研发人员（不仅仅是开发者）中仍然高达 96%，令人印象深刻。

Singer 说：“我们跟踪了大量关于我们开发生态系统的指标”，包括整个开发生态系统的工具化、集成开发环境和 Backstage 中的人力资源系统。

在 #RTO（重返办公室）成为趋势之际，Spotify 公开加倍强调其远程办公政策。这个决定并非一时兴起。正如 Singer 所说，“我们关注的是：我们的远程开发人员的效率是否高于在办公室工作的人？我们真的没有看到任何差异。”

作为 [DX](https://getdx.com/?utm_content=inline+mention) [开发者洞察平台](https://thenewstack.io/4-north-star-metrics-for-platform-engineering-teams/) 的长期客户，Spotify 和 DX 合作并在上周发布了一个 [DX Backstage 插件](https://backstage.spotify.com/partners/dx/plugin/dx/)，以便其他组织可以深入了解可衡量的开发者体验。

Singer 说：“他们真的很棒——可能不如我们在 Spotify 内部拥有的那么好，但他们真的很棒。我认为这将为人们在尝试弄清楚如何从 Backstage 中获得价值并获得[投资回报]并了解他们应该关注的地方时，增加一个非常大的价值。”

“DX 拥有一件其他人没有的东西，那就是他们拥有大量关于行业的信息。所以我查看他们的行业数据，以便您可以比较和对比您的表现。”

平台工程团队的任务之一是[证明开发人员的商业价值](https://thenewstack.io/the-real-business-value-of-platform-engineering/)，并进一步证明为什么将资金投入到开发者生产力中很重要。Singer 说，Portal 企业团队一直在与大型企业（包括银行）进行对话，在这些企业中，财务和采购团队绝对是决策者。

“在 Spotify，我们收到的信号表明，开发者门户可以将您的改进提高 2 倍。但是，当您是一家拥有 30,000 名开发人员的银行时，比如 5%、2% 的改进，这些都是巨大的数字，这让他们非常兴奋，因为他们拥有如此多的开发人员，”他说。“我们看到大量信号表明，比 Spotify 大几个数量级的大型开发组织看到了推进这一目标的价值主张。”

## 驾驭平台工程的浪潮

Singer 和 Aniszczyk 认为，平台工程和内部开发者门户是下一波浪潮，它将像云、Kubernetes 和现在的 AI 一样，对科技行业产生关键性的改变。

的确，虽然 Backstage 占据了主导市场份额，但只有大约 3,400 个组织采用它，这听起来并不多。

Aniszczyk 说：“最终发生的情况是，如果他们做一个自制版本，那就像一个半吊子的 IDP——也许他们编写了自己的服务目录”，但这些公司采用 Backstage 只是时间问题。

他说：“在 Kubernetes 的早期，人们在上面编写了自己的小型调度程序。人们会自己做一些事情一段时间，直到出现更好的解决方案，而现在已经有了。”

虽然 Backstage 最初被认为是为解决云中复杂性的中型和大型公司设计的，但 Singer 说他看到很多初创公司也在采用它，这些初创公司只有 50 名工程师。

他说：“您已经看到了小型公司的这种压力和问题。我认为这反映了现代软件的构建方式——如此组件化、如此分解、移动如此之快——以至于小型公司也意识到了价值主张。所以我认为这预示着这股浪潮将继续发展。”

此外，在人工智能时代，创建的代码比以往任何时候都多，速度也更快。
“使用 [Cursor AI](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/)，所有这些了不起的事情，你可以非常快速地创建软件，”Singer 说。“而这一直是 Spotify 面临的挑战之一：我们非常擅长创建软件。我们有 9000 万行代码，或者类似的数量，这会迅速增加复杂性。

“你看到这些公司。他们发展迅速。他们正在创建软件。然后重用就成了一个问题。而这最终会成为拖累你的船锚。”

## 在人工智能面前

[AI agents](https://thenewstack.io/ai-agents/) 的出现并没有让 Singer 感到不安。“你用这些智能 IDE 创建的代码越多，”他说，“它就越有可能，一是快速创建，二是质量低下。”

这使得平台工程、IDP 护栏和可见性更加重要。Backstage 致力于通过 Soundcheck 和模板功能等特性来控制 AI 的快速发展，这些特性应该有助于标准化和保持质量。借助仪表板、[可观测性和监控](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/) 插件，用户可以在不符合所选数据生态系统策略时查找并标记安全违规行为。

也许 Spotify 在 KubeCon Europe 上最大的发布是 Portal 的 AiKA 插件。这个“AI 知识助手”是一个 AI 聊天机器人，它首先被集成到 Spotify 的内部 Backstage 实例、其 IDE、[Slack](https://thenewstack.io/developer-guide-a-new-way-to-build-on-the-slack-platform/) 等中。AiKA 是一个 [基于检索增强生成 (RAG)](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/) 的聊天机器人，它了解组织和数据生态系统，包括引用其源材料。

Spotify 一直是一家热衷于“吃自己的狗粮”的公司，他们发现同事们即使在技术岗位之外也渴望使用 AiKA，每天有超过 1,000 名员工使用该聊天机器人。

AiKA 应该会在 4 月底之前发布给现有 Portal 客户的 alpha 版本。请返回 The New Stack 查看，以了解更多关于 AiKA 的信息。