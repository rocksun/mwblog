<!--
title: Kubernetes复杂性引发平台工程战略调整
cover: https://cdn.thenewstack.io/media/2025/07/5b198b8e-kubernetes-complexity-realigns-platform-engineering.jpg
summary: Kubernetes虽然被广泛采用，但也带来了复杂性挑战，如扩展难、成本高、缺乏可移植性等。平台工程通过创建内部开发者平台（IDP）来简化操作，提供黄金路径，并实现跨环境的一致性。人工智能的兴起加速了Kubernetes和云的采用，但同时也加剧了复杂性，平台工程战略旨在解决这些问题，提高效率，降低认知负担。
-->

Kubernetes虽然被广泛采用，但也带来了复杂性挑战，如扩展难、成本高、缺乏可移植性等。平台工程通过创建内部开发者平台（IDP）来简化操作，提供黄金路径，并实现跨环境的一致性。人工智能的兴起加速了Kubernetes和云的采用，但同时也加剧了复杂性，平台工程战略旨在解决这些问题，提高效率，降低认知负担。

> 译自：[Kubernetes Complexity Realigns Platform Engineering Strategy](https://thenewstack.io/kubernetes-complexity-realigns-platform-engineering-strategy/)
> 
> 作者：Jennifer Riggins

当 [Kubernetes](https://thenewstack.io/kubernetes/) 大约十年前出现在科技舞台上时，它迅速成为自下而上的开发者故事的光辉典范。

这个开源项目迅速成为开发者们的最爱，因为它承诺可以轻松地大规模编排容器，提供自动化、自愈和简化的部署流程。它促进了开发者们梦寐以求的约束分离，同时也让他们可以根据需要发挥创意和进行定制。

但是，Kubernetes 的这种灵活性在团队和组织中并不能轻松地平滑扩展。企业在扩展、安全、治理和平台一致性方面仍然面临困难。他们发现自己再次陷入困境——无法在云提供商之间迁移，并被 Day 2 运维的复杂性所淹没。

DevOps 和向云的转变给开发者和运维人员带来了巨大的[认知负担](https://thenewstack.io/platform-engineering-reduces-cognitive-load-and-raises-developer-productivity/)。组织长期存在工具蔓延和软件即服务 (SaaS) 订阅疲劳。与此同时，大多数团队都在尝试以更少的资源做更多的事情，包括管理[大规模人工智能的采用](https://thenewstack.io/ai/)。

在过去的几年里，[平台工程](https://thenewstack.io/platform-engineering/) 已经兴起，它通过创建黄金路径来抽象掉操作复杂性的各个层面——黄金路径是开发者完成“[非差异化但并非不重要的任务](https://thenewstack.io/how-to-foster-a-good-internal-developer-platform-experience/)”（如配置容器和部署到云）的最简单、自助式路线。它是通过[内部开发者平台（IDP](https://thenewstack.io/internal-developer-portal-what-it-is-and-why-you-need-one/)) 实现的，该平台为 Kubernetes 创建了一个单一的自动化操作模型，由集中的平台工程团队运营。如果实施得当，它还可以在技术、业务和合规性利益相关者之间实现通用语言。

我与 [Nutanix Kubernetes Platform](https://www.nutanix.com/en_gb/products/kubernetes-management-platform) (NKP) 背后的团队进行了座谈，以进一步深入了解这些主导企业 IT 战略的趋势。

## Kubernetes 复杂性挑战

根据 [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) 的数据，[80% 的组织已经采用了 Kubernetes](https://www.cncf.io/reports/cncf-annual-survey-2024/)。但这并不意味着 Kubernetes 管理很容易。

毕竟，无论您是在云端、本地还是在边缘环境中部署，Kubernetes 在设计上都很复杂。

这个容器编排器最初由 [Google](https://cloud.google.com/?utm_content=inline+mention) 构建并开源，旨在通过抽象底层基础设施来简化应用程序开发。然而，这意味着任何负责采用 Kubernetes 的团队不仅需要了解 Kubernetes（包括 pod、deployment、service 和 ingress），还需要了解其许多交互组件，包括 Kubernetes API 服务器、etcd 和 Redis 存储、kubelet、kube-proxy、策略管理、控制器管理器、控制器调度器等等。这些措施很难扩展。

虽然许多组织选择云是为了简单起见，但 Kubernetes 仍然存在因隐藏成本和缺乏可移植性而带来的挑战。

例如，Kubernetes 以其灵活性而闻名，允许大量的配置选项，这只会增加多样性和复杂性。这使得 Kubernetes 日志记录和监控变得特别具有挑战性，因为缺乏对集群的集中可见性。可见性不仅对于合规性和安全性至关重要，对于性能也至关重要。

来自云提供商的托管 Kubernetes 可以提供必要的监控，但这会大大增加成本，并剥夺了可移植性的选择，而可移植性是 Kubernetes 的主要优势之一。

还有一些最先进的开源解决方案可用，但使用它们意味着平台工程团队承担更大的责任，包括缓解常见的漏洞和风险、测试兼容性以及在整个集群中推出新版本。他们还必须对底层基础设施（包括代码库、网络和操作系统）有扎实的掌握，以避免常见的云迁移障碍。

由于大多数企业在多个位置（本地、云端和[边缘](https://thenewstack.io/kubernetes-fleets-beyond-the-iot-edge/)）运行 Kubernetes，因此平台工程团队必须准备好处理不同级别的抽象、自动化和责任，因为 Kubernetes 可以部署在裸机、虚拟机 (VM) 和/或云中。

不要忘记企业决策麻痹。最值得注意的是，[Cloud Native Computing Foundation landscape](https://landscape.cncf.io/) 似乎在不断扩展，这意味着这些开源工具选项和采用不断增加这种复杂性。

“[在云中部署 Kubernetes 存在很多](https://webthesis.biblio.polito.it/secure/21146/1/tesi.pdf)隐藏成本。虽然云提供商主要关注 Kubernetes 编排，但企业仍然需要将其他功能集成到 Kubernetes 企业级中，包括可观测性、网络、服务网格以及 Kubernetes 所需的其他工具，”[Nutanix](https://www.nutanix.com/en_gb) 的云原生产品负责人兼 OpenAPI Initiative 的联合创始人 [Dan Ciruli](https://www.linkedin.com/in/danciruli/) 说道。

即使他们采用了可用的最佳工具栈，各个 DevOps 和平台团队仍然需要花费时间进行更新——配置安全补丁和新功能——然后测试兼容性，最后在整个组织中推出补丁和升级。

而且，由于 Kubernetes 没有内置的工具来审计保护是否配置正确，因此这些团队需要与站点可靠性工程 (SRE) 和网络安全团队合作，以集成正确的安全策略和监控。难怪 DevOps 和平台团队因 Kubernetes 的广泛采用而面临倦怠。

然而，通过建立跨环境的一致性，[Nutanix Kubernetes Platform (NKP)](https://www.nutanix.com/en_gb/products/kubernetes-management-platform) 旨在降低这种操作复杂性。

## 回归有状态存储

虽然 Kubernetes 最初是为短暂的、无状态的工作负载而创建的，但随着越来越多的工作负载部署在 Kubernetes 中，对有状态工作负载的需求变得越来越大。

有状态工作负载在会话、请求甚至应用程序重启期间，在上下文中保留持久、可靠和一致的数据。有状态数据对于数据库、金融系统、实时通信、电子邮件服务器、消息队列、内容管理系统甚至电子商务购物车都是必需的。虽然云提供商通常为其托管解决方案提供存储，但行业和区域法规越来越要求本地数据存储以实现合规性。对于快速和详细的事件管理和灾难恢复，它也是必不可少的。

无论数据位于何处，更高容量的有状态数据正在 Kubernetes 环境中部署。尽管行业仍然缺乏“选择无状态和有状态架构的规范性指南，通常让架构师依赖于上下文判断和经验启发式”，但对支持有状态和无状态工作负载的需求[根据麻省理工学院研究人员](https://www.researchgate.net/publication/391017476_Stateless_vs_Stateful_Microservices_Design_Considerations) Mei Song 和 Margaret Joshua 的说法。

Kubernetes 提供了持久卷 (PV) 和持久卷声明 (PVC) 来满足对可靠存储、一致的网络标识和稳定调度的有状态需求。即便如此，管理存储访问模式、性能和容量会为 DevOps 团队管理 Kubernetes 中的有状态工作负载增加[显著的复杂性](https://www.researchgate.net/publication/392125011_Stateful_Application_Management_in_Kubernetes_Environments)。

此外，自建的 IDP 和大多数开箱即用的容器平台没有集成存储或数据服务，或者它们没有足够的存储来满足新客户或新的基于 AI 的工作负载的需求。

Ciruli 说道，企业通常不得不“附加”额外的存储容量——要么是限制可移植性的云存储，要么是购买本地存储，这又引入了另一家供应商。

他继续说道，这种“不如胶带”的额外存储方法通常会导致脆弱的集成，从而可能导致数据不一致，进而可能引发互相指责和追踪问题。

一旦你将这些数据放入云中或本地，再次传输这些数据以支持混合或多云战略就变得非常困难。

## 人工智能加速了 Kubernetes 和云的采用

现在，人工智能正在扩大对计算的需求和代码库的规模，一切都将变得更加复杂。

[Gartner 研究人员](https://www.gartner.com/en/newsroom/press-releases/2025-05-13-gartner-identifies-top-trends-shaping-the-future-of-cloud) 在 5 月份预测，到 2029 年，50% 的云计算资源将用于人工智能和机器学习 (ML) 工作负载。

“现在是组织评估其数据中心和云战略是否已准备好应对人工智能和机器学习需求激增的时候了，”Gartner 咨询总监 Joe Rogus 在最近的 Gartner IT 基础设施、运营和云战略会议上表示。“在许多情况下，他们可能需要将人工智能带到数据所在的位置，以支持这种增长。”

Ciruli 对此表示赞同，他告诉我：“我认为人工智能将会在本地。它将会在云端。它将会在任何地方。它将会在手机上——它已经在那里了。所有云应用程序最终都将成为人工智能应用程序，对吗？”

然而，他强调说，由于 Kubernetes 的复杂性，人工智能很难实施。

“对于人工智能应用程序，最好在容器上构建它们，因为这可以为您提供所需的可扩展性和可移植性，”Ciruli 说道。

“由于人工智能需要这些容器作为基础，因此许多公司现在开始考虑实际大规模管理这些容器”，这通常是第一次。

Ciruli 补充说，许多组织仍然没有掌握基础知识，包括微服务和云原生架构。更不用说如何大规模地进行 Kubernetes 和云。

## 平台工程的案例

如果不存在开源软件，企业将[需要比目前多花费 3.5 倍的软件费用](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4693148)。但开源绝不意味着免费。

开源的复杂性——尤其是驱动这种采用的云计算和 Kubernetes——引发了大规模的工具蔓延。大多数企业无法洞察已采用哪些工具以及跨数万个内部和外部 API 公开了哪些数据。他们没有准备好扩展和维护 Kubernetes。

大多数组织都采用自己动手、临时的方式，因为工程师们已经设计了自己的云端路径。这根本无法在企业环境中跨数百、数千或数万名工程师进行扩展。

也许最重要的是，Kubernetes 管理已经变成了繁琐的工作，分散了 [DevOps 团队的真正目标](https://thenewstack.io/platform-engineering-wont-kill-the-devops-star/)：

* 流向商业价值。
* 更快的反馈循环。
* 持续的实验、学习和改进。

让 DevOps 管理 Kubernetes 会迅速变得效率低下，并导致更大的技术债务，包括手动流程、缺乏自动化和配置漂移，即存储库中的内容与实际部署的内容之间存在差异。

正如 Govardhana Miriyala Kannaiah 在“[Kubernetes 反模式](https://www.oreilly.com/library/view/kubernetes-anti-patterns/9781835460689/)”中所写的那样，这种债务会让 DevOps 团队花费大量时间来管理现有系统，而不是进行创新：“当您选择捷径、绕过最佳实践并选择权宜之计时，就会产生利息。”

DevOps 团队和应用程序团队一样，可以从平台的铺平道路中受益。

平台工程已经兴起，成为解决这种大规模复杂性的一种方法，也是更好地抽象 Kubernetes 抽象的一种方式。平台团队已经成立，以减轻 DevOps 的大部分工作量。反过来，这也减轻了开发人员的云原生认知负担。

“存在很多歧义、知识差距，以及开发人员知道自己不知道的事情。开发人员不需要了解基础设施平台，”Ciruli 说道。“实际上，我们要求平台工程师构建该平台并将其提供给他们，这样他们就不必担心后端。他们只需要担心应用程序即可。”

然后，随着企业接近 Kubernetes 的采用，他继续说道，“他们希望向 DevOps 提供一个平台，以使他们的生活和体验更加丰富和轻松，并简化该流程。”

## 平台工程战略和 IDP 的交付成果

平台工程战略，无论是基于 [自建还是基于 SaaS 的平台产品](https://thenewstack.io/build-vs-buy-the-platform-engineers-guide/)，都是以更少的资源做更多事情的一种方式。它消除了 2010 年代的一些极端开发者自主性和工具蔓延，并将其换成了 [黄金路径或常见流程的倾向性工作流程](https://thenewstack.io/how-to-pave-golden-paths-that-actually-go-somewhere/)、标准化权限和整个组织中更高的可见性的便利性。

通常，平台工程战略以关注可发现性而开始。它允许平台工程、SRE 和安全团队获得跨组织的视图，了解：

* 已经采用了什么。
* 依赖项在哪里。
* 谁拥有哪些服务和 API。
* 在组织内部和外部公开了哪些数据。

[内部开发者平台](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/ "internal developer platform") 强调自助服务，以便开发人员可以更快地找出问题并完成工作。这通常会降低成本，因为它能够更好地重用这些服务和 API，而不是仅仅从头开始构建所有内容。IDP 通常使用搜索引擎或最近使用的对话式 AI 叠加层构建，从而启用搜索和文档，帮助开发人员找回平均 [每周浪费一天时间来寻找东西](https://thenewstack.io/why-do-developers-lose-1-day-a-week-to-inefficiencies/)。

虽然 IDP 有意专注于构建内部 DevOps 和工程客户实际想要使用的东西，但它确实包含其前身的一些功能，例如基于角色的访问控制。

内部开发者平台集中管理软件生命周期，从而实现单一部署的安全补丁和升级。这一点至关重要，因为根据 Infosec Institute 的数据，平均而言，[修复漏洞需要 60 到 150 天](https://allaboutgrc.com/vulnerability-remediation-timelines-how-fast-should-you-patch/)，这取决于漏洞，可能会威胁到您的正常运行时间、声誉等等。

除了 IT 领导层感到需要在削减成本的同时设置更多的护栏和流程之外，Ciruli 说道，“对我们来说，平台工程正在交付该平台，该平台是开放的、完整的、易于安装 [并且] 易于 DevOps [团队] 管理，从而通过易于使用的自助服务工具和功能更快地将其应用程序推向市场。”