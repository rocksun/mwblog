
<!--
title: 在山景城举行的Kubernetes十周年庆典：回顾历史
cover: https://cdn.thenewstack.io/media/2024/06/da23f913-eric-brewer-closes-talk-at-kubernetes-10-celebration-in-mountain-view-screenshot.png
-->

昨晚，一场非常特别的活动提供了超过三个小时的见解和历史，讲述了世界第二大开源

> 译自 [At Kubernetes 10th Anniversary in Mountain View: History Remembered](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/)，作者 David Cassel。

昨晚，一场非常特别的活动提供了三个多小时的见解和历史，讲述了世界第二大开源项目（仅次于 Linux）。随着 [Kubernetes](https://thenewstack.io/Kubernetes/) 庆祝其十周年，谷歌山景城园区迎来了来自社区的关键人物，他们共同促成了这一盛事。

随着晚会的进行，演讲者来自该项目的各个层面：

- [Dawn Chen](https://www.linkedin.com/in/chendawnhomepage) 在谷歌工作 17 年后发表了讲话——作为其命运多舛的 Borg 项目的负责人之一。
- [Sarah Novotny](https://www.linkedin.com/in/sarahnovotny/) 从她作为 Kubernetes 社区项目经理（2015 年至 2018 年）和谷歌云平台开源战略负责人（2017-2019 年）的角度，介绍了 Kubernetes 的旋风历史。
- 当晚的活动以资深员工软件工程师 [Janet Kuo](https://www.linkedin.com/in/janetkuo/) 感谢观众和 Kubernetes 社区“凭借你们的精彩创意，让 Kubernetes 社区保持如此创新”而结束。

但似乎每个人都分享了他们自己的坚持不懈的证明，他们对个人和社区工作的回忆，以及他们在那些充满希望的时刻共同合作完成一个他们真正相信可以改变世界的项目中的最佳故事。

这一切都来自在场的人——他们仍然深情地怀念着它……

## 59 年的愿景

最感人的时刻之一是，一位情绪激动的 [Eric Brewer](https://en.wikipedia.org/wiki/Eric_Brewer_(scientist))（谷歌基础设施副总裁）解释说：“对我来说，这不是 10 年。而是 30 年。”1997 年，他曾与他人合著了一篇关于“基于集群的可扩展网络服务”的[论文](https://people.eecs.berkeley.edu/~brewer/cs262b/TACC.pdf)，并提出了一种始终在线的计算机实用程序，正如他告诉观众的那样，“可以实现所有事情”。

但令人惊讶的是，那篇论文还引用了 1965 年的一段具有类似愿景的文字——来自 [介绍开创性 multics 系统的论文](https://dl.acm.org/doi/10.1145/1463891.1463912)。“在我看来，这三者——multics、我在 90 年代的工作以及 Kubernetes——都是对同一愿景的尝试。”

![](https://cdn.thenewstack.io/media/2024/06/cbdd5cac-eric-brewer-at-kubernetes-10-celebration-in-mountain-view-screenshot.png)

那么，为什么最终是 Kubernetes 取得了成功，而且仅在第三次尝试中才成功？Brewer 指出，multics 时代没有互联网。（“他们真的认为世界上会有五台计算机，我们都会通过分时连接到这五台计算机中的一台……”）在 20 世纪 90 年代，人类更接近于实现可以实现一切的实用程序的愿景。“我们有类似云的服务——我们确实有……它们以进程为中心，它们是无状态的，它们有 API 和服务以及所有这些支持。但它们直接在硬件上运行，而真正的机器很难——它们没有弹性。构建这种类型的系统非常困难。”

然后 Brewer 来到了 Kubernetes，深情地说：“它正在实现这一愿景，是真的……”但这不仅仅是因为弹性基础设施可用——Brewer 说这是“因为社区”。回顾过去 59 年，Brewer 的脸上流露出明显的情绪。“回想起来，这是显而易见的。但如果你想服务于所有事物，社区必须编写所有事物。没有其他办法……

“我认为这可能是我最感谢这个社区的原因——就是你们编写了所有内容。”

## 早期团队发言

[Kelsey Hightower](https://thenewstack.io/kelsey-hightower-on-his-very-personal-kubernetes-journey/) 介绍了 Kubernetes 联合创始人 [Craig McLuckie](https://www.linkedin.com/in/craigmcluckie)，他回忆起他们的原始团队“非常杂乱”。后来，谷歌 Kubernetes 产品经理 [Kit Merker](https://www.linkedin.com/in/kitmerker/) 将该团队描述为“叛逆”。

团队早期成员 [Ville Aikas](https://www.linkedin.com/in/villeaikas/) 也指出，即使该项目著名的 [首次提交](https://github.com/kubernetes/kubernetes/commit/2c4b3a562ce34cddc3f8218a2c4d11c7310e6d56) 实际上是在 code.google.com 上更早的工作之后。（“不幸的是，它不再存在了……”Aikas 补充道。“当它消失时，我们失去了很多历史。”）他的观点是，“了解我们真正卑微的开端非常重要”。

后来，Kubernetes 员工软件工程师 [Tim Hockin](https://www.linkedin.com/in/tim-hockin-6501072/) 说，“每个人都在做所有事情……我们都做了任何需要做的事情来完成任务。”（尽管 Hockins 被分配到网络，但他的背景实际上是操作系统。“我在谷歌的第一份工作之一是用汇编语言编写 BIOS。”）

随着故事的进展，Hockin 强调了这件事对项目的影响。“现在请记住，我仍然不是一个网络人员。但大多数应用程序开发人员也不是，我深信他们不应该成为网络人员……我牢记这一点，这是我的目标，并将继续成为我的目标。”

## Docker 想法

McLuckie 告诉观众，他当时担心的是亚马逊“有效地创造了这种令人难以置信的颠覆性方式来商业化开源”。但 Kubernetes 响应的一个关键部分是 Docker “如何出色地解锁 Google 构建的大量核心技术——并使开发人员能够使用它们。Solomon Hykes 在创造一种可立即访问的开发人员体验方面真正做到了点石成金。”

这是一个不断出现的话题。在 Google 早期的 [Borg 系统](https://thenewstack.io/google-learned-borg-container-management/)上工作时，Hockin 已经有了给每个作业分配自己的 IP 地址的想法。但这个想法被搁置了——直到几年后，Docker 使用命名空间才将其带了回来。“我认为……‘这是我想要的用户体验’……它确实描述了一种感觉像魔术的用户体验。”Hockin 称之为“我们都了解并……可能喜欢的每个 Pod 一个 IP 模型的诞生”。

然后，Hightower 将 Docker 的原始创建者 [Solomon Hykes](https://thenewstack.io/solomon-hykes-leader-open-source-world-needs/) 请上台，进行了一对一的特别采访。“我认为如果没有 Docker，Kubernetes 就不会存在，”Hightower 开始说……

![](https://cdn.thenewstack.io/media/2024/06/8e8b7322-kelsey-hightower-interviews-solomon-hykes-at-kubernetes-10-celebration-in-mountain-view-screenshot.png)

Hightower 说，Docker 的用户界面给 Kubernetes 团队留下了深刻的印象——这种竞争推动了这两个项目的发展。但 Hykes 记得他们的团队是真正的局外人，默默无闻。“我们来自法国——你知道，我们收拾好行李，搬到一个新国家，只为获得这个没人关心的初创公司的一线机会。我们已经做了五年的容器工作——而且真的没人关心……”但随后在设计和倾听用户意见的互动过程中，突然出现了“大规模歇斯底里……”

“在某个时候，它变得超级有竞争力，而且风险非常高……”Hykes 在得出更具和解性的想法之前说道。“但最终，你知道，这很有趣，因为 Kubernetes 和 Docker 实际上是非常互补的项目。最终，它们整合得非常好……”

Kelsey Hightower 感谢了他。“我想让你知道，我绝对确定，你创造了这个基础，它足够强大，可以将这样一个大项目提升到持续 10 年……”观众鼓掌。Hykes 随后缓慢而深思熟虑地说，他很欣赏“这次活动和社区的这个阶段”，他说他感到受欢迎，并且是“容器家族”的一部分。我享受这个阶段，因为我以前没有这种感觉……”

“对我来说，至少对 Docker 团队的其他成员来说，这是一个非常突然的转变——从‘走开，没人关心’到‘谢谢，我们已经从这里得到了。另外，走开。’”他笑了。“我的意思是，这是真的，我们有点——你知道，我们有点不方便……我们就像，占用了太多空间。我认为我们真的想被包括进来……”

“这是我的语言。这是我的民族。很高兴——很高兴随着时间的推移，伟大的工程、最佳实践和开源原则最终会胜出。”

## 感谢和纪念

该活动一再感谢社区。一张早期的幻灯片显示了排名前 25 位贡献者的姓名，赢得了阵阵掌声——另一张幻灯片感谢了所有版本负责人。

![Chris Aniszczyk 在山景城的 Kubernetes 10 庆祝活动中感谢版本负责人。](https://cdn.thenewstack.io/media/2024/06/05e42b87-chris-aniszczyk-thanks-release-leads-at-kubernetes-10-celebration-in-mountain-view-screenshot.png)

*Chris Aniszczyk 在山景城的 Kubernetes 10 庆祝活动中感谢版本负责人。*

但这只是让这一切协同工作的一部分。在小组讨论中，[Paris Pittman](https://www.linkedin.com/in/parispittman/)，Kubernetes 开发人员关系项目经理回忆起谷歌软件工程师 [Brian Grant](https://www.linkedin.com/in/bgrant0607/) 也敦促她创建更多角色。“人们需要所有权。人们需要有动力……我觉得这是真正的秘诀。”

随着晚会的开始，CNCF 的首席技术官 [Chris Aniszczyk](https://www.linkedin.com/in/caniszczyk) 也花了一点时间来纪念 [Dan Kohn](https://thenewstack.io/an-open-source-leader-is-gone-a-remembrance-of-dan-kohn/)。“他真正关心将人们带入这个社区，帮助获得奖学金，努力包容。虽然 Kohn 恩最近去世了，“但我认为他在塑造这个组织方面确实发挥了重要作用。所以我只想感谢他，并记住我们作为一个社区共同建立的一切。”

另一个回顾来自 [Ian Coldwater](https://en.wikipedia.org/wiki/Ian_Coldwater) — 现任职于 Docker，但最初是 Heroku 的平台安全工程师，在此之前是一名独立渗透测试员。Coldwater 回忆起那些形成期的日子，当时他还是“中西部的一个妈妈，我在一家非常早地采用这种非常奇怪的新技术的公司找到了一份工作，这种技术本不应该在生产中运行，但我们还是这么做了”。有人要求 Coldwater 尝试 [破坏 Kubernetes](https://thenewstack.io/the-top-5-kubernetes-security-mistakes-youre-probably-making/)，“事实证明，我可以破坏它……当时的 Kubernetes 非常容易破坏”。

“你可以使用未经身份验证的 [curl 调用](https://thenewstack.io/you-too-could-have-made-curl-daniel-stenberg-at-fosdem/) 在集群上以 root 身份执行命令。我们已经取得了长足的进步——作为一个项目，作为一个团队，作为一个社区。我们共同做到了这一点。我们共同构建了这个东西，我为我们所有人感到无比自豪。”

但随后 Coldwater 向那些帮助其安全性“与过去截然不同”的人们表示感谢。“实际上，我认为在很多情况下，它都非常好。”而这份名单从 Kris Nova 开始，她“做了很多匿名且未被认可的工作”。Nova 于去年 8 月去世，[享年 36 岁](https://thenewstack.io/good-bye-kris-nova/)，Coldwater 回忆说“她对获得认可不感兴趣。所以在她去世后——当她不在身边为这件事感到尴尬时——我想给她应有的认可。她负责很多事情，而你们永远不知道她负责这些事情。

“她很了不起，我们想念她。”

还有更多对安全人员的感谢，比如 [Rory McCune](https://www.linkedin.com/in/rorym/) 和 [Brad Geesaman](https://www.linkedin.com/in/bradgeesaman/)，“以及所有那些一开始就弄清楚如何破解这个东西的人——没有文档——然后弄清楚如何记录它！”

Coldwater 现在有一个已经长大的儿子——但他说也许“我们已经长大了——作为一个项目，作为人——在一起。我非常高兴能够升级，让你们所有人升级——并一起做到这一点。

“我非常高兴能与你们一起成长。”

![Ian Coldwater 在 Kubernetes 十周年庆典上。](https://cdn.thenewstack.io/media/2024/06/6d63504d-ian_coldwater_at_kubernetes_10_celebration_in_mountain_view__screenshot__-_closeup.png)

*Ian Coldwater 在 Kubernetes 十周年庆典上。*