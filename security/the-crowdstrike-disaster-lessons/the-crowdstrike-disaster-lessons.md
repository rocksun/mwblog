
<!--
title: CrowdStrike灾难中的7个教训
cover: https://cdn.thenewstack.io/media/2024/07/5ef24021-the-crowdstrike-disaster-lessons-2.jpg
-->

本周的软件更新让全世界陷入瘫痪，IT 机构能从中吸取什么教训？剧透：很多他们应该已经知道的知识。

> 译自 [7 Urgent Lessons from the CrowdStrike Disaster](https://thenewstack.io/the-crowdstrike-disaster-lessons/)，作者 Steven J Vaughan-Nichols。

坐在我的 [Linux](https://thenewstack.io/linux/) 桌面前，我的 Linux 服务器在后台嗡嗡作响，[CrowdStrike 崩溃](https://www.crowdstrike.com/blog/statement-on-falcon-content-update-for-windows-hosts/) 并没有直接影响到我。就像地球上几乎所有其他人一样，间接地，情况就不同了。

工作伙伴被困在机场。同事们在事件发生 48 小时后，仍在修复一台又一台故障的 Windows 系统，朋友们不得不使用现金购买杂货。

这一切本不必发生。

“[这提醒我们，我们生活在一个日益数字化的世界中，软件支撑着我们生活的几乎每一个方面——从交通和紧急服务到银行、零售甚至食品服务，”[Synopsys](https://www.synopsys.com/software-integrity.html?utm_content=inline+mention) 软件完整性部门总经理 [Jason Schmitt](https://www.linkedin.com/in/mjasonschmitt/) 在发布给新闻媒体的一份声明中指出。“软件问题会导致严重的业务问题——在某些情况下，还会导致影响消费者习以为常的许多必需品的问题。”

让我再说一遍：这一切本不必发生。让我来数一数这些教训。

## 1. 单一文化很危险。

无论是爱尔兰大饥荒期间的马铃薯，它让我的祖先来到美国，还是美国南方在棉铃虫出现之前的棉花，或者 Windows，只要每个人都依赖于单一系统，你就是在自找麻烦。

根据 [微软](https://news.microsoft.com/?utm_content=inline+mention) 的低估数据，只有 [850 万台 Windows 设备，不到所有 Windows 机器的一成，受到影响](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/)。但这些数字并不能说明全部情况。

根据 [6sense.com](http://6sense.com/) 的统计，这家商业数据分析公司，[CrowdStrike](https://www.crowdstrike.com/?utm_content=inline+mention) 是 [排名第一的企业端点安全公司](https://6sense.com/tech/endpoint-protection/crowdstrike-market-share)，拥有超过 3500 家客户。这听起来可能不多，但它包括四分之一使用端点安全的公司。这些往往是大型企业。因此，虽然在陷入无限重启的系统数量方面很少，但影响是巨大的。

“[这次停机事件的规模突出了过度依赖单一系统或供应商的风险，”云计算公司 [Civo](https://www.civo.com/) 的首席执行官 [Mark Boost](https://www.linkedin.com/in/markboost/) 在发布给新闻媒体的一份声明中说。“这是一个发人深省的提醒，规模和声誉并不能保证不受重大技术问题或安全漏洞的影响。即使是最大、最成熟的公司也必须保持警惕，不断更新和保护其系统。”

## 2. 糟糕的代码就是危险的代码。

根据 [Evis Drenova](https://www.linkedin.com/in/evisdrenova/) 在 X 上提出的一个流行理论，他是开发工具公司 [NeoSync](https://www.neosync.dev/) 的首席执行官，其 Falcon 传感器程序灾难性安全更新的根本原因是其 [C++ 代码](https://thenewstack.io/google-spends-1-million-to-make-rust-c-interoperable/) 中的 [空指针错误](https://x.com/evisdrenova/status/1814355536152015094)。[CrowdStrike 似乎否认了这一点。](https://x.com/patrickwardle/status/1814583925223678281/photo/3)

著名的 [Google](https://cloud.google.com/?utm_content=inline+mention) 漏洞研究员 [Tavis Ormandy](https://github.com/taviso) 也 [通过一条 X 推文](https://x.com/taviso/status/1814762302337654829) 表示不同意。Ormandy 和 [Patrick Wardle](https://www.linkedin.com/in/patrick-wardle-34580581/)，Mac 安全网站和工具套件 [Objective-See](https://objective-see.org/) 的创建者，也在 X 上发表了意见，他们怀疑[责任在于逻辑错误](https://x.com/patrickwardle/status/1814583573111812304)。

最终，我们会确切地知道出了什么问题，但毫无疑问，这段糟糕的代码永远不应该、永远不应该交付给客户。

## 3. 质量保证绝对必要。

这个问题始于 CrowdStrike。该公司质量保证 (QA) 团队如何让这次更新发布出去，这是一个问题，可能会导致许多人很快被解雇。

不过，他们并不是唯一应该为这一步走向灾难负责的人。

在今年四月于西雅图举行的北美开源峰会上，微软 Linux 平台组高级项目经理 [Jack Aboutboul](https://www.linkedin.com/in/jackaboutboul/) 在演讲中讨论了“懒惰的系统管理员”问题。这种刻板印象中的懒惰管理员会安装软件，开启自动更新，并处理最新的紧急问题。这很好……直到其中一次更新导致系统崩溃。

他们应该在每个新补丁发布时进行测试。Aboutboul 在演讲中谈论的是 Linux 发行版更新，但同样的想法也适用于所有关键任务软件。

正如软件开发和 QA 机构 [Redwerk](https://redwerk.com/) 和 [QAwerk](https://qawerk.com/) 的创始人 [Konstantin Klyagin](https://www.linkedin.com/in/thekonst/) 在发布给新闻媒体的一份声明中指出的那样，“自动化测试确保即使是微小的更改也不会引入新的错误。对于大型更新来说，这一点尤其重要，例如 CrowdStrike 的更新，仅靠人工测试是不够的。”

谁不做这个！？似乎至少有一些公司仍然没有这样做。

真的有那么多组织在这个基本步骤上失败了吗？有些人认为 CrowdStrike 应该受到指责，因为这个安全数据 [补丁“是一个绕过客户暂存控制的渠道更新”](https://www.resetera.com/threads/windows-blue-screen-of-death-bsod-happening-worldwide-right-now-up-caused-by-crowdstrike-falcon-sensor-see-threadmarks.931566/page-17?post=126020565#post-126020565)，并且无论用户是否愿意，都将其推广到所有人。

通过绕过客户的推广控制，更多公司受到了损害。由于如此多的企业受到这次故障的影响，这在我看来太有可能了。再次强调，问题仍然存在：“为什么有人会让如此重要的补丁在没有质疑的情况下部署？”

## 4. 阶段性推广避免灾难。

另一个相关的生产问题是，许多组织同时将其更新推广到所有系统。这是一个如此基本的错误；它永远不应该发生，但我们现在就遇到了。

是的，有反对阶段性推广的论点——当不同的团队使用不同的版本时，用户可能会感到困惑。但是，对于关键任务系统，如果出现故障是不可接受的，那么在进行任何升级时，您都需要格外小心。

此外，[有很多方法可以进行阶段性推广](https://thenewstack.io/5-deployment-strategies-the-pros-and-cons/)。它们包括滚动更新、[蓝绿部署、金丝雀发布](https://thenewstack.io/primer-blue-green-deployments-and-canary-releases/) 和 A/B 测试。选择一个。让它适合您的企业，只是不要把所有升级都放在一个大篮子里。

此外，强大的回滚程序对于在出现问题时快速恢复到稳定版本至关重要。您难道不希望只需按一下按钮就可以回滚到正常运行的系统吗？现在，数万名 IT 工作人员一定希望如此。

## 5. 灾难恢复和备份是必不可少的。

这应该是不言而喻的，但您必须有一个 [灾难恢复计划](https://thenewstack.io/supercharge-your-disaster-recovery-plan-in-5-simple-steps/) 和可靠的备份。

“我和几位 CISO 和 CSO 谈过，他们正在考虑触发从备份恢复协议，而不是手动将每台计算机引导到安全模式，找到有问题的 CrowdStrike 文件，将其删除，然后重新引导到正常 Windows，”公共演讲者和安全专家 [Eric O’Neill](https://www.linkedin.com/in/eric-m-oneill/) 在一份新闻声明中说。“没有投资快速备份解决方案的公司陷入了两难境地。”

确实如此。诚然，在 [云计算](https://thenewstack.io/k8s-backup-and-disaster-recovery-is-more-important-than-ever/) 的时代，灾难恢复和备份不像以前那么简单。但它们至关重要。而且，在这种情况下，传统的灾难恢复方法和备份将是一个很大的帮助。

## 6. 您需要增强的监控和事件响应。

这次停机事件的全球范围突出了对高级监控工具和强大的事件响应计划的需求。应到位实时监控和警报系统，以便在问题发生时捕获问题。IT 团队应制定详细的事件响应计划，其中包含明确的协议，以便快速识别、隔离和解决问题。这些计划应包括根本原因分析和 [事件后审查](https://thenewstack.io/top-12-best-practices-for-better-incident-management-postmortems/)，以不断改进响应策略。

说起来容易做起来难。

“在当今数字时代，企业需要制定积极主动且切实可行的策略来减轻停机风险并确保弹性，”[Cockroach Labs](https://www.cockroachlabs.com/)首席执行官兼联合创始人[Spencer Kimball](https://www.linkedin.com/in/spencerwkimball)在一份新闻媒体声明中表示。

他补充说：“停机问题不是我们能够完全解决的问题。云环境越来越复杂，相互关联性也越来越强。这种大规模的复杂性将继续增加风险，特别是对于仍处于云采用初期阶段的企业而言。持续监控和警报对于在问题升级之前检测和解决问题至关重要。”

Kimball 的观点得到了[Hydrolix](https://hydrolix.io/)副总裁 Anthony Falco 的呼应，该公司致力于实时查询性能，他在给 The New Stack 的一封电子邮件中表示。

“这次大规模停机事件突出了公司面临的新现实：如今推动业务发展的全球分布式软件平台是一个复杂的相互依赖网络，并非所有平台都受某一方控制，”Falco 说。“一个小小的错误可能会让全球业务陷入停顿。

“我们需要一种新的[可观察性](https://thenewstack.io/observability/)方法——一种实时方法，可以简化对来自无数来源的大量数据流的管理，以便在事件蔓延之前检测和缓解事件。”

## 7. 为下次做好准备。

CrowdStrike/Windows 事件是一个严峻的提醒，即使是例行维护，如果管理不当，也会导致重大中断。它突出了现代 IT 系统的互联性以及广泛使用的软件故障的深远影响。

通过从这次事件中吸取教训并实施稳健的风险管理策略，IT 团队可以更好地为类似事件做好准备并减轻其影响。

我们需要做得更好。我们必须做得更好。我年龄足够大，经历过第一次重大、广泛的安全问题，即 1988 年的[Morris Worm](https://www.zdnet.com/article/the-day-computer-security-turned-real-the-morris-worm-turns-30/)。当时，技术问题只困扰着那些从事技术工作的人。我们已经远远超出了那个时代。