<!--
title: GitLab 的 AI 豪赌：用 19 世纪经济理论重塑软件开发未来
cover: https://cdn.thenewstack.io/media/2026/05/28896533-mohammad-bazar-jbx8zfd57l0-unsplash-scaled.jpg
summary: GitLab 正在转向由 AI 智能体主导的开发模式。首席执行官 Bill Staples 援引“杰文斯悖论”，认为生产成本降低将刺激软件需求激增。公司正重构平台以支持“机器规模”的自动化编排，并利用深层的企业上下文数据构建竞争壁垒。
-->

GitLab 正在转向由 AI 智能体主导的开发模式。首席执行官 Bill Staples 援引“杰文斯悖论”，认为生产成本降低将刺激软件需求激增。公司正重构平台以支持“机器规模”的自动化编排，并利用深层的企业上下文数据构建竞争壁垒。

> 译自：[GitLab is betting a 19th-century economic theory will shape its AI era](https://thenewstack.io/gitlab-ai-agents-jevons-paradox/)
> 
> 作者：Paul Sawers

作为现代开发者工具行业的佼佼者，GitLab 无需过多介绍。该公司帮助普及了单一平台管理软件开发生命周期的理念，在同一个系统中涵盖了源码控制、CI/CD、安全扫描、协作和部署。

但现在，GitLab 正在针对一种全新的范式进行重组：AI 智能体（AI agents）将增加软件的构建量，而开发者的时间将花在监督、审查和协调机器生成的代码上，而不是亲自编写每一行代码。

[Bill Staples](https://www.linkedin.com/in/williamstaples/) 自联合创始人 [Sid Sijbrandij](https://www.linkedin.com/in/sijbrandij/) 于 [2024年](https://www.linkedin.com/posts/sijbrandij_on-todays-earnings-call-i-am-announcing-activity-7270548131891556352-eBU5/) 卸任以来一直担任 GitLab 的首席执行官。他本周宣布了公司的一系列变革，包括裁员、高管变动、产品整合以及对 AI 驱动软件开发的重新聚焦。

这次大修发生在 GitLab 的艰难时期。在过去的 15 个月里，随着投资者质疑 AI 将如何重塑软件开发及更广泛的开发者工具领域，该公司的市值缩水了约 66%，降至约 37 亿美元。

就 Staples 而言，他认为自己找到了遏制这种下滑的答案。在[周一发表的一封公开信](https://about.gitlab.com/blog/gitlab-act-2/)中，Staples 主张 AI 不会缩小软件行业，反而会扩大它。这种想法认为，降低软件的生产成本只会创造对软件的更多需求。经济学家称之为[杰文斯悖论（Jevons’ paradox）](https://en.wikipedia.org/wiki/Jevons_paradox)——这是一个 19 世纪的经济理论，得名于当年[观察到的现象](https://cssh.northeastern.edu/what-is-jevons-paradox-and-why-it-may-or-may-not-predict-ais-future/)：更高效的蒸汽机反而导致了煤炭消费量的上升而非下降。GitLab 正将其未来押注于此。

> “随着生产软件的成本崩溃，对软件的需求将会扩大。”

“在过去的二十年里，软件几乎是每一次业务转型背后的力量倍增器，”Staples 写道。“约束因素一直是生产和管理软件的成本和时间。现在这种约束正在崩溃。随着生产软件的成本崩溃，对软件的需求将会扩大。”

## 针对智能体时代的“机器规模”重建

深入探讨公开信的细节，Staples 指出了几个围绕着 GitLab 所谓的软件开发“智能体时代”而构建的大型架构和组织赌注。

“软件将由机器构建，由人指导，”Staples 写道。“智能体将进行规划、编码、审查、部署和修复。”

至关重要的是，Staples 认为这不会降低工程师的重要性，尽管它确实改变了他们的价值所在。开发者将专注于更高层面的系统设计、架构、治理、故障推理以及协调在整个软件生命周期中运行的 AI 系统群。

这一构思也解释了为什么 GitLab 如此强调编排（orchestration）。在 Staples 的描述中，新的挑战是协调跨代码库、流水线、审批、部署和企业策略系统同时运行的大量智能体。

> “企业需要的不是智能体的活动。他们需要的是能够推动业务发展的运行中的软件。编排就是带你到达那里的那一层。”

“企业需要的不是智能体活动，”Staples 指出。“他们需要能够推动业务发展的运行中的软件。编排就是带你到达那里的那一层。”

为了支持这一转变，GitLab 正在针对其描述的“机器规模”需求重构其底层平台的很大一部分。Staples 认为，现有的开发者基础设施很大程度上是围绕人类节奏的工作流设计的——个人开发者以相对可预测的频率开启合并请求、触发流水线并提交代码。AI 智能体完全改变了这种动态。

“智能体并行开启合并请求，全天候触发流水线，并以任何人类团队都无法企及的速度推送提交，”Staples 写道。

GitLab 已经为这一新方向奠定了基础，包括其在 [1 月份发布](https://ir.gitlab.com/news/news-details/2026/GitLab-Announces-the-General-Availability-of-GitLab-Duo-Agent-Platform/default.aspx)的 [Duo Agent Platform](https://ir.gitlab.com/news/news-details/2026/GitLab-Announces-the-General-Availability-of-GitLab-Duo-Agent-Platform/default.aspx)。在 2 月份接受 *The New Stack* 采访时，[Staples 主张](https://thenewstack.io/gitlab-ceo-on-why-ai-isnt-helping-enterprise-ship-code-faster/)编码从未真正成为瓶颈——开发者每天只有 10% 到 20% 的时间在写代码，其余时间都被审查、流水线运行、安全扫描和合规性检查所占据。“生成的代码速度再快，也只会卡在编码之后的队列中，”他说。Duo Agent Platform 是 GitLab 试图在整个生命周期（而不不仅仅是编码部分）实现自动化的尝试。

## 依靠其遗产

该公司更大的赌注包括将 GitLab 重建为更具 API 优先、可组合的服务，开发智能体专用的 API，并重新设计能够协调贯穿完整开发生命周期的自主软件智能体的编排系统。

但 GitLab 还认为，其在 AI 时代的最大优势可能来自于一些更古老、更庞大的东西：流经其平台的巨大企业上下文数据量。

> “每个开发工具供应商都在趋向于相似的代码生成能力。不会被商品化的是模型所能处理的独特上下文。”

“每个开发工具供应商都在趋向于相似的代码生成能力，”Staples 写道。“不会被商品化的是模型所能处理的独特上下文：一种连接每个项目和代码库的规划、代码、审查、安全、部署和运营的数据模型，这些数据是团队多年工作积累下来的。”

他的论点是，虽然代码生成模型在全行业范围内正趋于雷同，但组织上下文更难以复制。该公司实际上是在赌，在 GitLab 现有生态系统中运行的智能体将做出更好的决策，因为它们可以借鉴多年积累的客户工作流数据，涵盖代码库、CI/CD 流水线、部署、审批和运营历史。

这也解释了为什么治理（governance）仍然是该公司面向企业客户定位的重要组成部分。Staples 将治理描述为允许公司在生产系统中安全部署大量自主智能体的机制。

“就像赛车一样，如果你无法保持控制，你能跑多快并不重要，”他写道。

不过，对于 GitLab 来说，时机可能有些尴尬。该公司最初是作为 GitHub 最有力的竞争对手之一出现的，随后围绕更广泛的软件生命周期和企业 DevOps 工具进行了重新定位。然而，尽管在[最近几个月里](https://medium.com/@NMitchem/github-is-dying-and-developers-dont-even-know-it-yet-cca14b732ae5)，开发者社区的部分群体对 [GitHub 的不满情绪激增](https://leaddev.com/software-quality/whats-gone-wrong-at-github)——从[对可靠性的投诉](https://www.reddit.com/r/ExperiencedDevs/comments/1r0cytn/has_github_just_become_a_dumpster_fire/)到对该平台在微软领导下发展方向的批评——但 GitLab 并没有成为主要的受益者。

一个可能的原因是切换成本：深陷于 GitHub 的 CI/CD 工作流、集成和工具中的团队并不容易迁移，即使他们感到沮丧。讽刺的是，这种同样的动态——平台粘性作为竞争护城河——正是 GitLab 现在在 AI 时代押注其企业客户的地方。正如 X 上的一位社区成员[所言](https://x.com/tekbog/status/2053986174822457666)：“*在 GitHub 这一混乱时期，GitLab 居然没有变得更强大，这简直太疯狂了*。”

> “在 GitHub 这一混乱时期，GitLab 居然没有变得更强大，这简直太疯狂了。”

## 杰文斯悖论，一个反复出现的主题

传统的开发者工具市场在历史上很大程度上依赖于按开发者席位（seat）收费。AI 智能体使这一等式变得复杂：它们可以完成许多开发者的工作，但它们不需要席位。

如果软件可以以更大的规模和速度生产，这就会引出一个问题：传统的开发者工具业务在这个世界上如何捕捉价值。GitLab 的答案是，AI 增加软件总需求的初速将超过它减少工程师需求的速度——因此，能够以机器速度协调智能体的平台价值将更高，而不是更低。

这在 [AI 圈子里是一个熟悉的论点](https://www.npr.org/sections/planet-money/2025/02/04/g-s1-46018/ai-deepseek-economics-jevons-paradox)，并得到了诸如 Box 首席执行官 [Aaron Levie 等高管的公开支持](https://www.linkedin.com/pulse/jevons-paradox-knowledge-work-aaron-levie-qalmc/)，他也提出了类似的观点，即随着生产成本下降，软件需求将会扩大。

博主兼开源开发者 [Simon Willison](https://www.linkedin.com/in/simonwillison/) 写道，对 AI 的这种“受杰文斯悖论启发的希望”在很大程度上与他自己的想法一致，但他提醒说，GitLab 的立场也受到其商业动机的影响——特别是在投资者对 AI 智能体将如何影响开发者工具公司的长期经济效益感到不确定的时刻。

“如果你的整个业务都依赖于软件工程作为一个领域的增长并产生更大量、更丰厚的席位收益，你就有强烈的动机去相信智能体会产生这种效果，”[Simon Willison](https://simonwillison.net/tags/jevons-paradox/) 写道。

对于 GitLab 来说，赌注在于杰文斯理论在智能 AI 时代是否成立——除此之外的另一种可能由于过于惨淡而不堪设想。