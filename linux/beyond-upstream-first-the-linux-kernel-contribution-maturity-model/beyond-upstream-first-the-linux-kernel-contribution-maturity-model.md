
<!--
title: 超越上游优先：Linux内核贡献成熟度模型
cover: https://cdn.thenewstack.io/media/2024/07/ecabf01c-cornelius-ventures-ak81vc-kcf4-unsplash-linux.jpg
-->

一种开发Linux内核的新方法可能带来超越Linux领域的深远益处。

> 译自 [Beyond Upstream First: The Linux Kernel Contribution Maturity Model](https://thenewstack.io/beyond-upstream-first-the-linux-kernel-contribution-maturity-model/)，作者 Steven J Vaughan-Nichols。

加州纳帕——[Theodore “Ted” Ts’o](https://en.wikipedia.org/wiki/Theodore_Ts%27o) 对[Linux内核](https://thenewstack.io/linux-kernel-6-12-is-official-real-time-app-support-better-scheduling/) 了如指掌。毕竟，他是第一位北美Linux内核开发者。在他的个人电脑上，Ts’o 还运行着第一个托管Linux内核的FTP服务器，我正是在那里于1992年下载了我的第一个[Linux](https://thenewstack.io/learning-linux-start-here/) 版本。因此，当他在[2024年Linux基金会成员峰会](https://docs.google.com/document/u/0/d/1CSVtpazPgbNxROho8ea5WNyktBJqKeSUsZ01CgE--Ms/edit)上发表关于[Linux内核贡献成熟度模型(CMM)](https://docs.kernel.org/process/contribution-maturity-model.html) 的发人深省的演讲时，你应该认真倾听。

Ts’o首先解释说，从第一天起，Linux内核开发就一直围绕着“[上游优先](https://thenewstack.io/how-to-keep-up-with-linux-bugs-jump-upstream/)”展开。这意味着当你开发一个新的软件功能时，你将其添加到Linux上游。“与直觉相反的是，”T’so说，“这比针对你的产品内核进行工程工作效率更高，而你的产品内核可能落后于Linux上游数年。这种方法避免了重新调整树外补丁以及在功能最终进入上游时更改用户空间接口。”

虽然一些公司，例如[使用Android的Google](https://arstechnica.com/gadgets/2021/09/android-to-take-an-upstream-first-development-model-for-the-linux-kernel/)，已经采用了上游优先的方法，但许多其他公司还没有。为了鼓励他们加入上游优先的行列并帮助Linux开发，T’so指出，“向上游贡献很重要，因为它允许公司影响内核开发的方向。”他解释说，这种影响不仅仅是推动公司的议程，而是将内核塑造成更好地服务于整个行业的各种需求。

T’so补充道：“如果你现在是一名工程经理，你可能已经看到，在一个可靠且可预测的时间框架内将一些关键功能向上游提交是非常非常困难的。尤其是在今天，有很多公司都在努力推出新的AI产品，所以你们都想尽快将自己的功能提交到上游。”

这不仅仅是Linux的问题，Tso解释道。“这是一个普遍的主题。我和[OpenTelemetry](https://opentelemetry.io/) 的负责人谈过。他说，‘是的，我也看到了这种情况。’所以这不仅仅是Linux内核。”

## 不仅仅是Linux的问题

这就是为什么T’so建议我们超越Linux的“上游优先”。但他目前称之为“全组织上游”。他知道，它需要一个“更朗朗上口的标题”。公司必须超越“仅仅将你的树外补丁提交到上游，并对所有新功能进行上游优先开发，然后雇佣几个象征性的上游开发者或上游维护者，然后就完事了”。

他继续说道：“相反，你应该鼓励，或者甚至强制要求，你的所有工程师都花一定的时间做上游工作。”而且，这种方法应该被认为是你们公司所有关键业务的开源项目。

为什么？从公司的工程经理的角度来看，向上游发展符合他们自身的最佳利益。通常情况下，内核维护者在补丁完善且相关的技术债务得到解决之前，会犹豫是否接受新功能。不幸的是，一旦新的功能发布，贡献者往往会消失。工程团队负责支持整个内核，包括公司没有积极投资的内核部分。通过鼓励内核工程师通过上游工作来发展他们的专业知识，他们更有可能继续从事内核工作。

这有两个优点。首先，公司更有可能更快地将“他们的”功能纳入内核。其次，Linux内核获得了更多开发者、审核者和维护者来帮助支持它。

最后一点并非小事。CMM的根源可以追溯到2021年Linux内核维护者峰会。在这次Linux顶级内核开发者的聚会上，招募内核维护者和确保维护者继承的问题是一个热门话题。CMM框架旨在帮助解决这个问题。

正如Ts’o所描述的那样，CMM概述了公司参与上游内核开发的几个成熟阶段：

1. **临时贡献:** 工程师利用业余时间贡献代码，通常没有公司支持。
2. **鼓励贡献:** 公司允许并在工作时间内鼓励贡献。
3. **战略贡献:** 组织将贡献与业务目标相结合。
4. **社区领导:** 工程师担任维护者角色，并显著影响内核方向。

Ts’o强调了通过这些阶段发展的的重要性：“提升成熟度模型不仅仅关乎贡献的数量，更关乎参与的质量和战略性。”

根据Ts’o的说法，达到更高贡献成熟度的公司可以期待以下几个好处：

- **降低成本:** “通过上游贡献，公司可以降低维护树外补丁的成本，”Ts’o解释道。
- **提高产品质量:** 上游贡献从长远来看，可以带来更好的集成和更少的错误。
- **增强声誉:** 积极参与提升了公司在开源社区中的地位。
- **吸引和留住人才:** “工程师重视有机会参与上游项目并提升技能，”Ts’o指出。

Ts’o承认公司在实施成熟的贡献实践方面面临的挑战。他引用了一个常见的误解：“‘我们承担不起让工程师花时间在上游工作。’这种短期思维往往会导致长期成本更高。”

为了克服这些挑战，Ts’o建议：

- 教育管理层了解上游贡献的长期利益。
- 实施支持和奖励开源参与的政策。
- 制定指导计划，帮助工程师成长为社区领导角色。

“至关重要的是要创造一种重视和支持上游贡献的文化，”Ts’o强调。“Linux内核生态系统的健康取决于公司提升其贡献实践的成熟度。通过投资上游开发并培养重视开源参与的文化，公司可以在塑造Linux的未来方面发挥至关重要的作用，同时也能为自身业务和员工带来显著的好处。”

Linux也迫切需要扩大其审阅者和维护者队伍。“大部分维护工作是由极少数工程师完成的。”Thomas Gleixner，一位在本次演讲中也出席的领先Linux内核开发者，报告说只有1909名维护者和审阅者。其中，653人两年内没有任何活动。总而言之，这些至关重要的Linux活动中有80%是由仅11%的人完成的。难怪[Linux维护者倦怠是一个严重的问题](https://www.zdnet.com/article/what-linux-kernel-maintainers-do-and-why-they-need-your-help/)。

T’so指出，虽然这么说听起来工作量很大，但其实没那么糟糕。“如果我们能让所有贡献者多做一次代码审查或多做一次测试等等，就会产生巨大的影响。如果每天的维护者活动从两次增加到三次，你就会有很大的提升。我们实际上并不需要很多维护者。我们需要很多人稍微帮忙一点。人多力量大。”其结果将是“公司能够更好地实现其业务计划”，而Linux也将变得更强大，“这将是一个双赢的局面。”

我认为他是对的。Ts’o的演讲是促使公司重新评估其上游内核开发和开源开发方法的令人信服的行动号召。通过转向组织范围内的上游，我建议我们称之为“普遍上游”，开源软件链中的每个人，从开发者到最终用户，都将互惠互利。
