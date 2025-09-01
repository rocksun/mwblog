
<!--
title: 网络弹性法案：恐惧、困惑与安心
cover: https://cdn.thenewstack.io/media/2025/08/dcba9560-michelle-tresemer-mjkuuayqq6u-unsplash.jpg
summary: 欧盟《网络韧性法案》(CRA) 将于 2027 年生效，影响通过开源软件产生收入的组织。该法案要求产品投放市场时“没有已知的漏洞”。OpenSSF 和 Linux 基金会提供免费课程以帮助适应。目前合规性要求尚不明确，但重点在于修复和报告已知的、可利用的漏洞。该法案主要针对货币化的开源软件，上游开源被广泛排除在外。
-->

欧盟《网络韧性法案》(CRA) 将于 2027 年生效，影响通过开源软件产生收入的组织。该法案要求产品投放市场时“没有已知的漏洞”。OpenSSF 和 Linux 基金会提供免费课程以帮助适应。目前合规性要求尚不明确，但重点在于修复和报告已知的、可利用的漏洞。该法案主要针对货币化的开源软件，上游开源被广泛排除在外。

> 译自：[The Cyber Resilience Act: Fear, Confusion — And Reassurance](https://thenewstack.io/the-cyber-resilience-act-fear-confusion-and-reassurance/)
> 
> 作者：B. Cameron Gain

阿姆斯特丹 - 如果您的组织通过开源软件直接或间接产生收入，那么您至少应该了解即将到来的[《网络韧性法案》](https://thenewstack.io/what-the-eus-cyber-resilience-act-cra-means-for-open-source/) (CRA) 的影响。

虽然[CRA](https://thenewstack.io/open-source-development-threatened-in-europe/)将于 2027 年生效，但许多组织并未意识到准备时间是以月来计算的。这既适用于仍在讨论中的立法（这增加了混乱），也适用于了解如何为生效做好准备。

在介绍 CRA 的最新进展之前，您现在可以做的是通过现有的不同计划进行准备。如果有人说他们可以向您收费以确保合规性，而您为此付费，那么他们说的不是实话，因为没有人确切知道您必须做什么才能符合 CRA 的要求，因为它尚未最终确定。

## 没有已知的漏洞

CRA 规定，在“具有数字元素的商品”投放市场时，必须“没有已知的漏洞”。[OpenSSF](https://thenewstack.io/openssf-boosts-software-supply-chain-security-with-slsa-1-0/) 首席安全架构师 Christopher Robinson 在阿姆斯特丹举行的 [Open Source Summit Europe](https://events.linuxfoundation.org/open-source-summit-europe/) 期间告诉我，这意味着产品首次在欧盟境内销售时，必须经过检查和扫描，确认没有当前漏洞。

当产品发货时，供应商和创建者必须披露正在被积极利用的漏洞，或者是否存在中断服务或可能泄露可利用漏洞的网络安全事件。供应商——或欧盟委员会所说的“制造商”（也指软件供应商）——必须制定一个流程，以便“及时”提供传统漏洞的安全更新，但对于这些“常规”漏洞，没有规定确切的时间范围，Robinson 说。

虽然对该指令的一般描述听起来可能很简单，但事实远非如此，尤其是考虑到该指令尚未最终确定。虽然 OpenSSF 是通过提供技术和其他指导来帮助塑造该指令的参与方之一，但它究竟将涵盖什么以及如何涵盖仍有待完成。Robinson 将其目前的 90 页文本描述为“90 页的细微差别”。

当然，修复和报告开源代码中的每一个漏洞的想法是荒谬的。但是，对于攻击者理论上可以利用的已发现漏洞，根据 [CRA 指令](https://thenewstack.io/how-linux-kernel-deals-with-tracking-cve-security-issues/)，理论上仍然可能需要合规。必须发布报告，并且需要修复它。

同样，虽然该指令尚未最终确定，但合规性可能不像许多人担心的那样繁重。目前，只需要修复已知的漏洞，并根据它们被利用的难易程度和严重程度来确定优先级。诺基亚网络软件和互联网标准化负责人 Timo Perala 在 OSS Europe 期间告诉我：“这些要求是合理的。行业和开源不会被要求修复所有问题，这是可以理解的。目前，它不是很精细，但重点是最严重和最具破坏性的问题，然后从那里开始处理列表。”

在描述了他在 OSS 演讲“批准后六个月我们在哪里”中提到的利害关系后，Perala 告诉我，与 Robinson 的描述一致，该指令的影响仍然存在歧义。“它仍然不是定量的，因为你如何确定限制在哪里？高于此阈值，一切都是立即的；低于此阈值，则不那么紧急，”Perala 说。“低于此阈值，也许有时。在这个层面上，这种理解是存在的，但工程师们当然想要定量的措施。”

关键术语是“货币化”。广义上讲，除非涉及利润，否则该指令不包括开源维护者。一个非常具体的短语适用：销售支持合同。同时，[上游开源](https://thenewstack.io/open-source-development-threatened-in-europe/)被广泛排除在外。

一个假设的例子说明了其影响：一个组织、制造商或实体在欧洲市场上销售具有数字元素的商品，Robinson 描述道。在这种情况下，可以是一家汽车公司。它也可以是玩具、Wi-Fi 路由器或交换机。该产品，包括内部的所有组件——硬件、固件和软件——被认为是供应商的责任。Robinson 说，为项目设计和使用开源并为路由器添加特定代码的人也将被追究责任。

## 免费课程

为了帮助开源社区适应，[Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention)和 OpenSSF 创建了一个关于 CRA 的免费课程。该课程涵盖上游维护者、开源管理者和制造商。该课程持续 90 分钟，并概述了该法律的内容。[GitHub](https://thenewstack.io/github-loses-its-ceo-and-independence/) 存储库和其他来源提供了其他资源。

OpenSSF 是 Linux 基金会的安全主题专家。OpenSSF 拥有 30 个基金会，发挥着核心作用。OpenSSF 还维护一个关于 CRA 的专门网站，并计划扩展到涵盖 NIST 2、《数字运营弹性法案》(DORA) 以及欧盟和国际范围内的其他合规制度。

一旦标准可用，将向成员和其他基金会提供指导。商业服务可能会出现，但任何关于保证合规性的声明都为时过早，因为目前没有人知道明确的要求，Robinson 说。欧洲议会和委员会的最终批准将在 2027 年 10 月进行，距离执行还有两个月。

“总体影响预计会减缓欧洲的进展，但对于那些在国际上销售的组织来说，这些法规既是挑战，也是一个重要的市场机会，”Robinson 说。“合规对于进入市场是强制性的。”
