# 2023 年云原生预测

本文翻译自 CNCF 的 [2023 cloud native predictions](https://www.cncf.io/blog/2023/01/26/2023-cloud-native-predictions/)，查看原文可以访问原文的连接。

作者：Chris Aniszczyk（也在 [LinkedIn](https://www.linkedin.com/pulse/cloud-native-predictions-2023-chris-aniszczyk/) 上）

我希望每个人都和所爱的人一起度过了愉快的假期！ CNCF 最近发布了关于我们去年完成的所有工作的[年度报告](https://www.cncf.io/reports/cncf-annual-report-2022/)。我建议大家抓住机会仔细阅读这份报告，因为我们花了很多时间对社区所做的所有出色工作进行分类。此外，自从我发布年度预测以来已经有几年了，所以对于延迟，我深表歉意，希望你喜欢今年的列表！

## 云 [原生] IDE 变得规范化

最近，GitHub Codespaces 结束了 [beta 版](https://github.blog/2022-11-10-whats-new-with-codespaces-from-github-universe-2022/)，虽然我们没有很多来自 GitHub 的公共使用数据，但 Twitter 上似乎有很多[积极情绪](https://twitter.com/search?q=codespaces&src=typed_query)。此外，[GitPod](https://www.gitpod.io/blog/next-chapter-for-gitpod) 与该领域的其他公司一起完成了他们的 A 轮融资，这些公司已经筹集了令人印象深刻的[几轮融资](https://blog.replit.com/b)。

我 100% 相信，转瞬即逝的开发工作区以及开发人员在设置工作区时节省的时间将推动这项技术成为行业规范。你看到 [Uber](https://www.youtube.com/watch?v=YdmzVzxz9DI)、[Shopify](https://shopify.engineering/shopifys-cloud-development-journey)、[Slack](https://getdx.com/podcast/remote-development-at-slack)、[Stripe](https://www.infoq.com/presentations/stripe-dev-env-infrastructure/) 等公司使用这种形式是有原因的，随着 Codespace 和 Gitpod 等产品的标准化，这些最佳实践将传播到整个行业。

最后，Gitpod 汇集了一套优秀的“[云开发环境](https://www.gitpod.io/cde)”(CDE) 原则，我建议您看一看。此外，Redmonk 的好人在他们精彩的文章“[年度云开发环境](https://redmonk.com/jgovernor/2022/12/01/the-year-of-the-cloud-development-environment/)”中分享了我的情绪，我建议从分析师的角度阅读。

## FinOps 成为主流并左移

几年前，Linux 基金会帮助建立了“[FinOps 基金会](https://www.finops.org/blog/linux-foundation)”，以培养该领域的创新。 FinOps 基金会有了一个良好的开端，从举办第一届 [FinOpsX](https://x.finops.org/) 会议到启动 [FinOps 现状调查](https://data.finops.org/)，甚至整理了一些[很棒的介绍材料](https://www.edx.org/course/introduction-to-finops)。

为什么今年对 FinOps 来说是重要的一年？在过去几年中，云支出显着增加，并且正在成为组织内部的一大成本，有时甚至与薪水相抗衡：

![](https://yylives.cc/images/2023-cloud-native-predictions/twi1.png)


此外，您可以通过 Google 趋势查看 FinOps 工作趋势，以了解事情已经达到增长拐点的指标。

![](https://yylives.cc/images/2023-cloud-native-predictions/twi2.png)

所有这些市场压力的另一个好处将是更多的标准化和开源选项，如 [OpenCost](https://www.opencost.io/)。传统上，破译云账单是一个难题，如果您使用多个云（没有涵盖所有主要云的云定价和成本管理的开放标准），则更加复杂。

这些市场压力加上全球经济衰退将增加大多数组织的 FinOps 实践，而不仅仅是高科技湾区公司。与过去相比，FinOps 将更多地成为一个工程问题，过去工程团队可以相当自由地控制云消费。您将看到 FinOps 信息更接近开发人员，并最终将基础设施拉取请求到这个层面。

最后，成本管理和 FinOps 将默认成为可观测性解决方案的一部分（例如，Datadog 宣布推出[成本管理产品](https://www.datadoghq.com/about/latest-news/press-releases/datadog-introduces-cloud-cost-management/)）。我预计这个领域也会有很多整合，大型传统公司会通过收购进入他们的领域。

## 无处不在的开源 SBOM

美国政府在过去几年制定了有关提高软件安全性的政策和法律，从 2021 年的行政命令(Executive Order)到最近的“[美国保护开源软件法案](https://www.govinfo.gov/content/pkg/BILLS-117s4913is/pdf/BILLS-117s4913is.pdf)”，其中涵盖了无数的安全改进措施。开源安全基金会 (OpenSSF) 对该法案及其如何解决开源安全问题的[动员计划](https://openssf.org/oss-security-mobilization-plan/)进行了很好的总结。此外，就在最近，美国政府通过了一项法律，要求医疗设备制造商必须生产 SBOM：

![](https://yylives.cc/images/2023-cloud-native-predictions/twi3.png)

这种趋势不可避免地会继续下去并影响开源软件，像 Kubernetes 这样的领先关键项目已经在[生产 SBOM](https://www.youtube.com/watch?v=N0ZNdnnHL40) 供[消费](https://kubernetes-sigs.github.io/bom/tutorials/creating_bill_of_materials/)。在所有行业强制执行 [SBOM 的道路上可能会遇到一些障碍](https://www.cyberscoop.com/dhs-sbom-adoption/)，但我个人认为这是不可避免的，因为监管或行业正在成熟。

这个领域还将有许多新的开源创新、初创公司和项目，它们致力于聚合大量此类安全信息（请参阅 [https://deps.dev](https://deps.dev/) 作为一个简单示例）。我个人正在关注 [GUAC](https://github.com/guacsec/guac)、[Scorecards](https://github.com/ossf/scorecard)、[Sigstore](https://www.sigstore.dev/)、[Witness](https://github.com/testifysec/witness) 等项目。

## GreenOps 融入 FinOps

可持续性是一个热门话题，参与 ESG 领域的人们都知道计算基于云的工作负载的碳足迹有多么复杂。普华永道最近的[研究](https://www.pwc.com/us/en/tech-effect/cloud/esg.html)来自“财富 1000 强公司，60% 的企业领导者正在使用或计划使用云来增强 ESG 报告，59% 使用或计划使用云来改进他们的 ESG 战略。”

我相信，随着我们提高云的效率，这里会出现[杰文悖论](https://en.wikipedia.org/wiki/Jevons_paradox)……除了有趣的[研究](https://www.washingtonpost.com/technology/2023/01/13/self-driving-cars-greenhouse-gas-emissions/)表明，“未来仅在支持全球自动驾驶汽车的计算机所需的能源就可能产生与当前全球所有数据中心一样多的温室气体排放量”。

在我看来，GreenOps 是 FinOps 的一种形式，专注于云工作负载的碳足迹。我希望这些社区能够合并为一个，并就该领域的开放规范和标准进行协作，可能会[扩展 OpenCost](https://github.com/opencost/opencost/issues/1011) 以包括跨云的碳足迹信息。这里有很多跨公司和行业的开源协作机会。

## GitOps 成熟并进入生产力稳定期

自 Alexis Richardson 在 [2017 年首次创造 GitOps 这个词](https://github.com/readme/featured/defining-gitops)以来，随着 GitOps 工具的成熟，这个领域发生了巨大的变化。在 CNCF 中，Argo 和 Flux 项目[最近毕业](https://www.cncf.io/blog/2022/12/27/argo-and-flux-grown-up-gitops-for-cloud-native-generation/)，展示了项目的稳定性和成熟的治理以及快速的采用水平。因此，它们也是 CNCF 生态系统中[开源速度最高的项目](https://www.cncf.io/blog/2023/01/11/a-look-at-the-2022-velocity-of-cncf-linux-foundation-and-top-30-open-source-projects/)之一。

如果您对这个空间感兴趣，我建议您参与上面的开源项目并参与 CNCF Open GitOps 工作组：[https://opengitops.dev](https://opengitops.dev/)。

## OpenTelemetry 走向成熟

如果你查看来自 CNCF 的最新开源项目速度数据，[OpenTelemetry 位居第二](https://www.cncf.io/blog/2023/01/11/a-look-at-the-2022-velocity-of-cncf-linux-foundation-and-top-30-open-source-projects/)，仅次于 Kubernetes，对于这样一个年轻的项目来说令人印象深刻。

在过去的几年里，几乎所有主要的现代可观测性供应商都致力于集成 OTel。 OTel 收集器框架使供应商无需实现此功能，并使最终用户的生活更加美好。 2023 年，您不仅会看到[许多](https://www.nginx.com/blog/integrating-opentelemetry-modern-apps-reference-architecture-progress-report/)[技术前沿公司](https://github.blog/2021-05-26-why-and-how-github-is-adopting-opentelemetry/)采用 OTel，还会看到传统企业最终用户利用这项技术。

## Backstage 开发者门户成熟度

开发人员体验一直是达到一定规模的组织关注的问题，以此作为提高工程吞吐量的一种方式。如今，随着越来越多的组织踏上云原生之旅，这对大多数行业来说变得很重要。在我的上一次[预测](https://www.aniszczyk.org/2021/01/19/cloud-native-predictions-for-2021-and-beyond/)中，我提到“服务目录”成为必需品，但不止于此。

在 CNCF 社区中，Backstage 是我见过的少数几个在 Kubernetes 落地之前首先部署在传统企业中的项目之一。它在这方面有点独特，但它确实被银行或[航空公司](https://backstage.spotify.com/blog/adopter-spotlight/american-airlines-runway/)等传统企业以及 Spotify 等尖端科技公司使用。您可以从他们的 [ADOPTERS.md](https://github.com/backstage/backstage/blob/master/ADOPTERS.md) 文件和 BackstageCon 视频中看到项目中的一些疯狂采用。

为了更上一层楼，Backstage 需要巩固其 API 并继续培养其插件生态系统，以便它实质上成为该领域的“Jenkins”。

关于 Backstage 和现代开发人员门户的另一件有趣的事情是，[Gartner 甚至注意到并开始在这个领域进行研究](https://twitter.com/themarkoneill/status/1488552595757182982?s=11)，这始终是不久后成熟的标志。

## WebAssembly 创新 + 启蒙坡度

我坚信 Web Assembly (Wasm) 将在不久的将来成为一种主要的计算形式，因为它探索了浏览器之外的用例，从边缘到服务器工作负载。我发现 Sapphire Ventures 的这篇[文章](https://sapphireventures.com/blog/whats-up-with-webassembly-computes-next-paradigm-shift/)，承诺 Wasm 将成为该主题中最好的选择之一。从个人经验来看，我不断看到 Wasm 在未来的云原生生态系统中出现在更多领域，从 Envoy 的插件系统的重组，到 WasmCloud 和 WasmEdge 等项目。该死，甚至 Docker 在最近的技术预览中也支持 Wasm：[https://www.docker.com/blog/docker-wasm-technical-preview/](https://www.docker.com/blog/docker-wasm-technical-preview/)

然而，随着 Wasm 用例的发现、运行时的成熟以及技术的普遍发展，将会出现一些成长的烦恼。用炒作周期的说法，Wasm 将介于幻灭的低谷和启蒙的斜坡之间。虽然有很多关于 Wasm 潜力的积极压力，确实也正在实现一些事情，同时也有许多进行中的配件，如 [WASI](https://wasi.dev/) 和 tail call 还不能完全支持：

![](https://yylives.cc/images/2023-cloud-native-predictions/twi4.png)

![](https://yylives.cc/images/2023-cloud-native-predictions/twi5.png)

此外，我认为你会看到像 Cloudflare 这样的精品云提供商和小型初创公司为这项技术的成熟铺平了道路，超大规模公司将在今年开始提供他们的第一批 Wasm 相关产品。

最后，我想明确一点，我看到一个容器、Wasm 甚至 VM 将并存的世界……甚至我们在 Docker 的朋友也这么说：[https://www.docker.com/blog/why-containers-and-webassembly-work-well-together/](https://www.docker.com/blog/why-containers-and-webassembly-work-well-together/)

## 削减成本有利于精品云（或任何超级云）

为了延续今年的成本管理主题，我相信随着组织退后一步并评估其云使用情况，精品云提供商（或任何超级云）将从这一趋势中受益。有关 2023 年这一趋势的示例，请参阅 Cloudflare 最近发布的公告……“[Palantir 宣布与 Cloudflare 建立战略合作伙伴关系，专注于云成本优化](https://www.prnewswire.com/news-releases/palantir-announces-strategic-partnership-with-cloudflare-focused-on-cloud-cost-optimization-301717292.html)”以及他们如何将 [R2](https://www.cloudflare.com/press-releases/2022/cloudflare-makes-r2-storage-available-to-all/) 产品与 S3 进行比较。

这些精品云提供商将自己定位为关注这一特定领域的成本优化和客户服务。他们将宣布在这个领的域新收购和产品，以便与更大的云竞争。

## Kubernetes 有其 Linux 风格的成熟时刻

不提 Kubernetes 就不能做云原生预测，对吧！？就在最近，我发布了一篇关于 2022 年云原生生态系统内外的[开源项目速度](https://www.cncf.io/blog/2023/01/11/a-look-at-the-2022-velocity-of-cncf-linux-foundation-and-top-30-open-source-projects/)的博文。作为开源项目历史发展速度的一部分，Kubernetes 一直与 Linux 并驾齐驱。 Kubernetes 将继续存在并在企业和整个行业中巩固自己的地位。采用 Kubernetes 的不仅是湾区公司和高科技前沿组织，还有像[沃尔玛](https://siliconangle.com/2023/01/17/walmarts-supercloud-cloud-native-kubernetes-based-platform-supercloud2/)这样的世界传统企业。该死的，[Kubernetes 甚至在每家 Chick-Fil-A 餐厅都在运行](https://medium.com/chick-fil-atech/enterprise-restaurant-compute-f5e2fd63d20f)，有一些基于边缘的计算适合你！甚至有人在[轨道](https://www.suse.com/success/hypergiant/)上运行 Kubernetes……在[太空中](https://www.youtube.com/watch?v=Yk6wRsckroA)！

当我说 Kubenetes 正处于 Linux 风格的成熟时刻时，我的意思是曾经有一段时间 Linux 最初是为特定的爱好者用例构建的，然后最终更广泛的生态系统扩展到在手机、汽车、实时系统等等上运行。 Kubernetes 项目正在进行类似的演变，组织正在扩展 Kubernetes 以在该项目最初设计的新型环境中运行，例如嵌入式设备。这些新用例将创新带回到 Kubernetes 项目和更广泛的生态系统中，就像 Linux 中发生的那样。开源创新泵已经准备就绪并将继续下去。

## 其他预测

- **有生产力的 AI 将被立法并在开源社区中引起摩擦。** 关于归属、版权和遵守开源基金会和公司政策的有趣问题将会很有趣地展开（例如，一些公司已经禁止使用从 CoPilot 生成的代码）。我们还看到在这个领域[针对 CoPilot 甚至艺术版权和 Stable Diffusion 的诉讼](https://www.theverge.com/2023/1/17/23558516/ai-art-copyright-stable-diffusion-getty-images-lawsuit)，这只会加速，并且可能会导致一些版权法发生变化。Heather Meeker 发表了一篇很棒的[关于版权消费 AI 的博文](https://heathermeeker.com/2023/01/19/is-copyright-eating-ai/)，我强烈推荐阅读。
- **VSCode 将继续发展并主导 IDE 领域。** 这是一个非常活跃的项目，微软迄今为止在管理社区方面做得很好。如果你查看来自 [Stackoverflow 的调查](https://survey.stackoverflow.co/2022)或来自 Top IDE 索引的数据，那么 VSCode 将成为几乎所有主要编程语言的主导 IDE（甚至不包括它在 Codespaces 和 Gitpod 中的嵌入式使用）。
- **RISC-V 将作为一个开源社区走向成熟，并看到嵌入式和移动设备的使用率飙升。** 就在最近，Google 宣布 [Android 计划支持 RISC-V 作为“第 1 层”架构](https://arstechnica.com/gadgets/2023/01/google-announces-official-android-support-for-risc-v/?utm_content=233552732&utm_medium=social&utm_source=linkedin&hss_channel=lcp-7953130)，这意味着您将在不久的将来看到 RISC-V 所在的位置。世界各地也存在[地缘政治逆风](https://www.scmp.com/tech/big-tech/article/3204265/tencent-joins-open-source-chip-design-community-risc-v-china-seeks-mitigate-impact-us-sanctions)，有利于某些地区采用 RISC-V。
- **游戏引擎行业的开源创新飞速发展。** 游戏行业与云原生世界有点不同……其中大部分 AAA 风格的开发仍然发生在 Windows 机器、巨大的 monorepos 和专有游戏引擎（如 Unity 和 Unreal）上。正如 [a16z 在 2016 年所说的那样](https://a16z.com/2016/06/01/open-source-gaming-vr/)……我们需要更多的游戏开源，而这最终将通过 [Bevy](https://bevyengine.org/news/scaling-bevy-development/)、[Godot](https://godotengine.org/)、[O3DE](https://o3de.org/) 等开源游戏引擎实现。
- **由于监管和安全问题的增加，[OSPO](https://github.com/todogroup/ospodefinition.org) 得到跨行业和政府的发展。** 我是 [TODO 集团](https://todogroup.org/)的联合创始人之一，该集团是开源计划办公室 (OSPO) 网络的所在地，并且[见证了 OSPO ](https://www.linuxfoundation.org/research/the-evolution-of-the-open-source-program-office-ospo)在高科技行业中的演进。随着我们依赖的越来越多的软件基于开源，组织将需要一种战略方法来管理采用该软件的创新和安全风险。此外，各国政府开始规范[欧盟内 OSPO 的形成](https://openforumeurope.org/wp-content/uploads/2022/06/The-OSPO-A-New-Tool-for-Digital-Government-2.pdf)，这将被其他国家效仿。

## 最后，2023 年快乐，今年好运！

我总是有更多的预测和趋势要分享，尤其是围绕最终用户驱动的开源、eBPF、服务网格蚕食和保护软件供应链，但我会把它留到今年晚些时候更详细的帖子中，一些预测足以开启新的一年！无论如何，感谢阅读，我希望在一周后在 [CloudNativeSecurityCon](https://events.linuxfoundation.org/cloudnativesecuritycon-north-america/) 上见到大家，当然还有我们将于 2023 年 4 月在阿姆斯特丹 [KubeCon + CloudNativeCon EU](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 举行的大型会议，注册已经开始！