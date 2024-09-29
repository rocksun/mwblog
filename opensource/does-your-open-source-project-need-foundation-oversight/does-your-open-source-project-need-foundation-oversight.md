
<!--
title: 您的开源项目需要基金会监管吗？
cover: https://cdn.thenewstack.io/media/2024/09/38d69a92-does-your-open-source-project-need-foundation-oversight-2.jpg
-->

云原生计算基金会已收容了 190 多个项目。CNCF 项目有哪些好处，以及如何维持 CNCF 项目？

> 译自 [Does Your Open Source Project Need Foundation Oversight?](https://thenewstack.io/does-your-open-source-project-need-foundation-oversight/)，作者 Joe Fay。

如果您正在开发一个开源的云原生项目，将它移至[云原生计算基金会 (CNCF)](https://cncf.io/?utm_content=inline+mention) 的监管之下似乎是理所当然的。毕竟，看看像[Prometheus](https://thenewstack.io/prometheus-at-10-whats-been-its-impact-on-observability/) 或[Falco](https://thenewstack.io/falco-is-a-cncf-graduate-now-what/) — 当然还有[Kubernetes](https://thenewstack.io/kubernetes/) — 如何主导着这个领域。

当然，这些项目已经加入 CNCF 多年了。过去的成功并不保证未来的成功。而且还有其他基金会或模型来管理[开源项目](https://thenewstack.io/20-years-in-open-source-resilience-failure-success/)。

但现在，“这是行之有效的游戏”，[Edd Wilder-James](https://www.linkedin.com/in/wilder-james/) 说道，他在[Google](https://cloud.google.com/?utm_content=inline+mention) 和[Sysdig](https://sysdig.com/?utm_content=inline+mention) 工作期间管理过多个开源项目。这就是为什么 CNCF 自九年前成立以来，已经收纳了 192 个项目，由 252,000 名贡献者提供支持。

然而，在申请加入 CNCF 之前，任何项目团队都需要考虑两个重要问题。他们应该将自己的项目移至 CNCF 吗？如果他们这样做，谁应该在整个过程中引导项目？

## 基金会监管的优势

对于第一个问题，答案取决于您想要实现的目标。

CNCF 将自己视为不仅仅是一个代码存放地。CNCF 首席技术官[Chris Aniszcsyk](https://www.linkedin.com/in/caniszczyk/) 指出，它拥有专业的员工——与其他基金会不同，其他基金会主要由志愿者运营。这意味着它可以为成员提供一系列服务，包括硬技术支持，例如提供安全审计。

此外，他告诉 The New Stack，“我们有专门负责网站、技术文档的人员。我们还有开发人员倡导者，他们帮助推广项目。”

当然，CNCF 还举办各种活动，从专门的项目活动，例如[PromCon](https://promcon.io/2024-berlin/)（专门针对[Prometheus](https://prometheus.io/)），到像[KubeCon + CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america) 这样的盛会。Aniszcyk 说，CNCF 非常关注“商业化活动”。

Aniszcyk 指出，CNCF 项目治理和技术治理与预算治理是分开的。理事会成员决定将预算整体分配到项目和他们关心的方面。然后，技术监督委员会提出预算申请。

他说，目标是“将资金集中起来，用于安全审计、技术文档、活动等的共同利益”。

但这只是等式的一面。Wilder-James 说，同样重要的是，大型组织——大多数 CNCF 项目的最终用户——会发现 CNCF 负责项目的治理令人放心。

“我认为企业市场已经接受了这样的观念，即如果某个项目在基金会中，它显然保证了自己作为更安全的选择被采纳。一个单一供应商的开源项目可能会在一夜之间消失。”

在过去的一年里，这个问题变得更加突出。一些以前开放的项目——[Terraform](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/) 和[Redis](https://thenewstack.io/linux-foundation-forks-the-open-source-redis-as-valkey/)，最引人注目——已经切换到更不开放的许可证，甚至完全是专有许可证，这让其他贡献者感到沮丧，并给商业用户带来了不确定性。失去关键的商业支持者可能会让项目陷入困境。

同时，Wilder-James 说，将项目移至 CNCF 或任何基金会，可以为有可能变得无处不在并主导市场的技术提供“反垄断保护伞”。正如他所描述的，这是“人们在没有无数律师在场的情况下进行交流的唯一方式”。

正如另一位资深人士告诉我们，将您的项目移至 CNCF 的监管之下并不能保证它会成为标准，但它确实增加了这种可能性。他们补充说，当一家公司将项目移至 CNCF 时，其维护人员和支持者会在组织内获得影响力。

[Kapil Thangavelu](https://www.linkedin.com/in/kapilvt/)，Cloud Custodian 的共同创建者，以及 Stacklet 的首席技术官，告诉 The New Stack，他将项目移至 CNCF 的最终目标是尽可能减少其贡献者和维护者社区的摩擦。
“CNCF 在流程方面很轻量级，并且对每个项目都开放，每个项目都有自己的治理模型概念……这对该项目来说是有意义的，”Thangavelu 说。

## 基金会监管的挑战
[加入 CNCF](https://thenewstack.io/istio-applies-to-join-cncf-why-now/) 毫无疑问有很多好处，但这并不是一个轻率的决定。WilderJames 说，公司或团队需要了解将项目移至基金会保护伞下所带来的挑战。

Wilder-James 说，这包括清楚地了解他们究竟放弃了什么作为回报。“你需要从一开始就明白，你将成为一个有效的跨供应商项目。有很多项目没有做到这一点，没有继续下去。”

为此，他说，“你必须选择时机。因为从这一点开始，它就成了一个锚。从根本上说，基金会中的成熟项目是商品化的平台技术。”

因此，如果你对尖端创新感兴趣，跨供应商基金会环境可能不是最佳选择——至少现在不是。

毕竟，“你实际上是在放弃你的知识产权，因为项目将成为 CNCF 的版权，”Sysdig 的创始人兼 CTO [Loris Degioanni](https://www.linkedin.com/in/degio/) 告诉 The New Stack。“商标将归 CNCF 所有。”

这对任何项目团队或公司来说都可能很困难，对于安全公司来说更是如此。

对于 Sysdig 来说，将 Falco 移入 CNCF 的影响是“可怕的”，Degioanni 说。“我记得我们进行过几次激烈的内部讨论，甚至与我们的董事会进行了讨论。”

但艰苦的工作并没有就此结束。通过 CNCF 的沙盒和孵化过程，进入令人垂涎的毕业阶段意味着获得社区支持。Degioanni 说，实际上，“CNCF 要求你出去招募其他公司来拥抱这个项目，使用它。因此，你实际上是在出去尝试创造竞争对手。”

在整个过程中，个人和团队必须公开运作。“如果你习惯于在内部跟踪你的路线图和开发，也许使用 Jira 或 Asana，那么将所有这些内容移至公开可能非常具有挑战性，”Aniszczyk 承认。“举办公开会议，邀请所有人参加，这是一种文化变革。这对很多人来说都很难。”

事实上，Wilder-James 建议，“无论你是小公司还是大公司，拥有大型开源项目都没有免费午餐。”

对于一个团队投入到项目中的所有工程努力，它仍然面临着[创建业务的挑战](https://thenewstack.io/whats-next-for-companies-built-on-open-source/)。“换句话说，如果你想做这件事并将其货币化，你必须付出双倍的代价，对吧？”

然后，还有与他人合作或为委员会做出贡献的挑战。这可以被视为对发展的阻碍。仅仅与他人相处融洽就是一项艰苦的工作。因此，Wilder James 说。“你必须拥有[具有人类技能的工程师](https://thenewstack.io/why-empathy-in-open-source-matters-more-than-you-think/)。”

从 Thangavelu 的角度来看，除了技术技能，“毅力、适应能力，将是首要的[品质]。”

Degioanni 说，推动项目向前发展意味着以真正动手的方式与社区互动，包括发布版本，“在 Slack 上提供支持，在 GitHub 上与贡献者交谈。”

换句话说，保持你的双手沾满泥土。

“至少在 Falco，”Degioanni 说，“真正推动这一过程的人是[核心开发人员社区](https://thenewstack.io/open-source-needs-maintainers-but-how-can-they-get-paid/)。”

这对任何团队来说都是一组艰巨的要求。

## 做出决定
那么，这一切都值得吗？从 Degioanni 的角度来看，这确实取决于项目。有些项目最好保持独立实体——比如他之前的项目[Wireshark](https://thenewstack.io/wireshark-celebrates-25th-anniversary-with-a-new-foundation/)，直到它存在了 25 年才移至非营利性监管（[Wireshark 基金会](https://wiresharkfoundation.org/)）。

但对于应该成为更广泛生态系统的一部分的项目——云原生、AI——他的感受不同：“在这种情况下，是的，我绝对会选择基金会，因为有好处，我们正在看到这些好处。”

对于 Thangavelu 来说，“如果我再次进行基金会计算，我肯定会得出相同的结论。”

也就是说，他对“年轻的自己”的建议是找到其他人来“坚持这个过程”。

但那是因为他并不完全适应任务的公开部分。他说，他可以做“社交蝴蝶”，但“我在我的编码位置很开心。”这对于许多工程师来说肯定如此。
最终，虽然协作很难，但 Wilder-James 说：“我个人认为协作中蕴藏着美。我认为它能带来极大的满足感，对我个人而言，协作既困难又罕见，这使得它对我来说极具满足感。”
