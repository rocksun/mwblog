
<!--
title: 未来的开源公司要怎么办？
cover: https://cdn.thenewstack.io/media/2024/04/78e9352d-what-now-open-source-2.jpg
-->

你可以期待看到更多开源项目创建者收紧他们的许可。但首席执行官和创始人表示，这些决定很复杂。

> 译自 [What’s Next for Companies Built on Open Source?](https://thenewstack.io/whats-next-for-companies-built-on-open-source/)，作者 Heather Joslyn。

巴黎 —— 2023 年末，三岁初创公司 [DataCebo](https://datacebo.com/) 推出了其产品的企业版，该产品帮助组织从关系型和表格数据库创建合成数据。

该公司旨在解决组织的常见问题：收集数据以测试应用程序，这是一个繁琐且耗时的过程，并且难以扩展。例如，一家银行可能拥有 1,000 多个应用程序，每个应用程序都需要测试数据。

DataCebo 联合创始人 [Kalyan Veeramachaneni](https://www.linkedin.com/in/kalyan-veeramachaneni-9861b821/) 表示，显而易见的缺点是安全风险和缺乏灵活性，因为无法快速收集数据。

相比之下，合成数据“在格式结构和统计质量方面都与真实[数据](https://thenewstack.io/data/)非常相似，”Veeramachaneni 在 3 月份的 [KubeCon + CloudNativeCon Europe](https://thenewstack.io/kubecon-europe-webassembly-ebpf-are-huge-for-cloud-native/) 上告诉 The New Stack。“但这并不是真实的东西。它与真实数据没有关联。”

Veeramachaneni 和 DataCebo 联合创始人 [Neha Patki](https://www.linkedin.com/in/nehapatki/) 在 2016 年作为 [麻省理工学院](https://web.mit.edu/) 人工智能实验室的同事开始开发此类技术，该技术可能曾经是开源状态的明显候选者，而 KubeCon 设计的项目就是为了庆祝此类技术。但在 2023 年，DataCebo 撤回了该项目的[开源许可证](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/)；现在是源代码可用，这一区别限制了使用。

[让开源获得报酬一直很困难](https://thenewstack.io/closure-is-open-source-licensing-suddenly-unsustainable/)。但在过去几个月里，一些知名公司已将关键项目从[开源许可证迁移到更具限制性的许可证](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/)请参阅：[HashiCorp 和 Terraform](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/)，[Buoyant](https://buoyant.io/) 在 2 月份决定[提供 Linkerd 服务网格的独家商业新版本](https://thenewstack.io/buoyant-revises-release-model-for-the-linkerd-service-mesh/)，以及 Redis 在 KubeCon 上宣布其[未来版本及其许可计划](https://thenewstack.io/linux-foundation-forks-the-open-source-redis-as-valkey/)）。

然而，保持代码开源并鼓励开发人员进行修改和调整以及上游贡献——[围绕产品构建社区](https://thenewstack.io/entrepreneurship-for-engineers-how-to-build-a-community/)——历来是加速其采用的最佳方式。

在 KubeCon，The New Stack 听到了很多关于开源商业模式是否真的能带来投资回报的争论，[是否会有更多公司可能效仿](https://thenewstack.io/the-open-source-markets-in-flux-how-can-it-managers-cope/) [HashiCorp](https://thenewstack.io/opentofu-vs-hashicorp-takes-center-stage-at-open-source-summit/) 和 Redis（剧透提示：是的），以及为什么开源精神对创新仍然很重要。

## 太多“一次性”产品？

DataCebo 更改了其许可证，因为“我们看到很多人使用它来与初创公司竞争”，使用该技术推出直接竞争的产品，Veeramachaneni 说，他还负责麻省理工学院的[数据到人工智能](https://dai.lids.mit.edu/)实验室。

“许可证更改也是因为我认为[人工智能是一个非常嘈杂的领域](https://thenewstack.io/ai/)，”他说。“从我的人工智能背景来看，我们开始注意到的不仅仅是公司竞争。人们也在构建一次性产品。”

他认为，“一次性”产品的激增可能会损害人工智能的长期商业利益。它们不会“以产生投资回报率的方式采用人工智能”。

[Lightbend](https://www.lightbend.com/) 是一家云原生[微服务](https://thenewstack.io/microservices/)平台提供商，[在 2022 年 9 月宣布将 Akka 框架](https://www.lightbend.com/company/news/lightbend-changes-its-software-licensing-model-for-akka-technology)（其旗舰产品）迁移到 [BSL v1.1（商业源代码许可证）](https://www.lightbend.com/akka/license)。

“我认为每家公司都有不同的动机来解释他们为何需要这样做，” [Tyler Jewell](https://www.linkedin.com/in/Tylerjewell/)，Lightbend 的新任首席执行官，告诉 The New Stack：“我们的动机之一是可持续性……我们拥有的是一种极其宽松的许可证，几乎允许任何类型的行为。”

![](https://cdn.thenewstack.io/media/2024/04/5f19e22b-lightbend-jewell-boner-1024x625.jpg)

Lightbend 首席执行官 Tyler Jewell（左）和该公司的创始人兼首席技术官 Jonas Bonér。

他还补充说，还有一个永恒的问题，即如何让开源发挥作用。“老实说，我们正在制定经济模式，”Jewell 说，他曾任职于 [WSO2](https://wso2.com/)、[戴尔](https://www.delltechnologies.com/en-us/index.htm?utm_content=inline+mention) 和 [Oracle](https://developer.oracle.com/?utm_content=inline+mention)。

“我们的客户基本上离开了我们，愿意免费使用它，而不给予任何回报。因此，我们采用了 BSL 模型，该模型表示，如果您作为一家公司的收入低于 2500 万美元，则开发是免费的，生产也是免费的。”

他说，这一改变让小公司得以喘息，同时让有能力负担的更大客户购买订阅。“这让我们重新与社区取得了平衡，”Jewell 说。他说，Akka 研发团队的规模已经扩大到原来的三倍，使公司能够投资于改进产品。

“随着公司寻求平衡，即如何在资助开源的同时以可行的方式维护开源，我们将看到更多这样的事情。”

## 没有“围墙花园”

[英特尔](https://www.intel.com/content/www/us/en/now/data-centric/overview.html?utm_content=inline+mention)的 19,000 多名软件开发人员中，有数千人定期为 300 多个开源项目做出贡献，据该公司开放生态系统副总裁兼总经理 [Arun Gupta](https://www.linkedin.com/in/arunpgupta/) 说。

其开发人员做出贡献的项目包括 [PyTorch](https://thenewstack.io/pytorch-takes-ai-ml-back-to-its-research-open-source-roots/)、[TensorFlow](https://thenewstack.io/googles-new-tensorflow-tools-and-approach-to-fine-tuning-ml/)、[OpenJDK](https://thenewstack.io/your-guide-to-navigating-openjdk-in-2023/)，当然还有 [Kubernetes](https://thenewstack.io/kubernetes/)。

3 月份，英特尔发布了 [Continuous Profiler](https://github.com/Granulate/gprofiler)，这是一款由英特尔 Granulate 开发的优化代理，它将多个分析器组合到一个火焰图中，增强了可观测性。

英特尔对开源的承诺很坚定，古普塔对开源社区的承诺也是如此：他目前担任 OpenSSF 管理委员会主席。

该公司继续在开源项目之上构建产品。2024 年初，英特尔获得了[云原生计算基金会 (CNCF)](https://cncf.io/?utm_content=inline+mention)认证，用于其英特尔 Kubernetes 托管服务，该服务是其英特尔开发者云的一部分。“它主要针对在云原生生态系统中运行人工智能工作负载，”古普塔在 KubeCon 上告诉 The New Stack。

他理解为什么越来越多的公司开始重新考虑其项目许可证。“企业必须做对他们有意义的事情，对吧？”Gupta 说。“没有一种模式……对于某些企业来说，这种模式非常有效。但对于某些企业来说，它不起作用。特别是对于由风险资本家支持的公司来说，他们面临着很大的赚钱压力。”

但他警告说，将项目转移到更具限制性的许可证也可能加剧不平等并阻碍创新。“英特尔的信念是，开放生态系统为每个人创造了一个公平的竞争环境。它不应该被锁在围墙花园中，”他说。“你可以说‘我们正在创造一种新的产品，它是一种仅限于企业的许可证’，但中途更改许可证是对信任的破坏。”

他补充说，开源社区释放出的协作和创造力，“是我们推动世界前进的方式，因为这些都是全球性挑战。因此，它确实需要全球合作。而你只能通过开源许可证获得全球合作。”

## 策略：OpenTofu、Terraform、Cilium

[Harness.io](https://www.harness.io/) 是最早支持 [OpenTofu](https://thenewstack.io/opentf-disgruntled-hashicorp-rivals-threaten-to-fork-terraform/) 的公司之一，OpenTofu 是 HashiCorp 的 Terraform 的开源分支，Terraform 是无处不在的 [基础设施即代码 (IaC)](https://thenewstack.io/infrastructure-as-code-the-ultimate-guide/) 工具，该公司在 8 月份将其转移到了商业源代码许可证。

Harness.io 在其自己的产品中同时使用 Terraform 和 OpenTofu，该公司现场首席技术官 [Martin Reynolds](https://www.linkedin.com/in/martinreynolds/) 在 KubeCon 上告诉 The New Stack，并支持这两个项目的成功。“只是为了持续公开讨论开放基础设施即代码。”

他预计会看到更多公司效仿 HashiCorp，将他们的产品迁移到 BSL，但他也指出了 CNCF 在保持基本项目开源方面所扮演的角色。

以 Spotify 开发并捐赠给 CNCF 的平台 [Backstage](https://thenewstack.io/spotifys-backstage-a-strategic-guide/) 为例。Backstage 是一个使组织能够构建定制内部开发者门户的平台，[一直是平台工程趋势的关键推动因素](https://thenewstack.io/spotifys-backstage-roadmap-aims-to-speed-up-adoption/)。

Reynolds 说：“如果 Spotify 采用了它并将其制作为相同的商业源代码许可证，那么我认为这会影响许多运行自己的 Backstage 的组织。”

[Thomas Graf](https://www.linkedin.com/in/thomas-graf-73104547)，[Isovalent](https://isovalent.com/) 的联合创始人，对开源项目和商业压力略知一二：他是 Cilium 的联合创建者，Cilium 提供高级网络和安全控制，利用[扩展 Berkeley 数据包过滤器 (eBPF)](https://thenewstack.io/what-is-ebpf/)。2023 年末[思科](http://cisco.com/?utm_content=inline+mention)[宣布收购 Isovalent](https://thenewstack.io/cisco-gets-cilium-what-it-means-for-developers/)。

在 KubeCon，Graf 正在讨论 [Cilium](https://cilium.io/) 的最新开源版本及其当时即将发布的企业级项目版本。他还回顾了该项目的早期以及围绕该项目建立的公司。

Graf 告诉 The New Stack：“我们从一开始的策略始终非常明确，即什么是开源，什么是企业部分。”

他建议，将开源版本和企业版本视为具有独特需求，有助于他的组织发展：“这不仅仅是点击并安装，然后你就有了一个企业级解决方案。”

他说，从一开始就没有考虑好商业产品，建立在开源基础上的公司面临着艰难的选择：“我认为一些项目有点像，‘我完全开源。然后我稍后会想出货币化策略。’然后需要进行这种转换。”

他说，被思科收购不会改变该项目与开源的关系。

他说：“我们找到了一个强大的合作伙伴，它真正致力于延续我们的开源策略，就像我们以前所做的那样，同时明确哪些是可货币化的路径，这在企业传统网站上更多一些。”

“该策略不会尝试将现在开放的内容变为封闭或更改许可证。”

## 寻求更多透明度

[NGINX](https://www.nginx.com?utm_content=inline+mention) 建立在开源应用程序交付产品之上，并在 F5 的支持下运营了五年，它对社区和商业之间的紧张关系并不陌生。

F5 的产品管理高级总监 [Liam Crilly](https://www.linkedin.com/in/liamcrilly/) 在 KubeCon 告诉 The New Stack：“我们正在调整产品策略。在过去几年中，我们尝试通过拥有这款人们普遍了解和喜爱的核心 NGINX 产品来发展业务。然后我们尝试围绕它构建越来越多的包装，以满足我们企业客户的需求。那是一条坎坷的道路。”

Crilly 说，新策略是将 NGINX 构建的许多管理、可观测性和编排工具转移到 F5 的分布式云控制台。

Crilly 说，[NGINX One](https://thenewstack.io/nginx-melds-open-source-tools-into-an-enterprise-platform/)，新的按需付费软件即服务产品，处于早期访问状态，将在夏季末向公众开放。

他说，就开源而言，NGINX 打算变得更加开放。

他说：“其中一件主要的事情是我们对源项目和 NGINX 的治理更加透明。”他补充说，目标“是让 NGINX 被视为一个现代的多项目组织”。

拥抱他所说的“现代开放治理”包括教育开发者社区 [NGINX 支持哪些项目](https://github.com/nginxinc/)：不仅是核心 NGINX 项目，还包括 Kubernetes ingress controller、gateway fabric等。

为此，NGINX 聘请了一名社区经理和团队，他们目前正在通过社区 Slack 频道联系开源开发者；它还在寻找其他方式来接触新一代开发者。

Crilly 说，开源仍然为寻求产品采用的企业提供了优势。“我认为我们会继续看到企业利用开源，没有比这更好的方式来接触开发者。因此，如果那是你的市场，你必须这样做。”

但他还预见到科技公司在如何处理开源商业模式方面会发生变化。“我认为我们会看到人们在表达自己的意图和章程时会更加明确。因此，这会更加透明。”

Crilly 补充说，“组织或公司可以通过多种方式将开源货币化。但没有一刀切的办法。理想的货币化策略并不总是可行的。我认为，考虑到市场状况和时机，现在确实很难。”
