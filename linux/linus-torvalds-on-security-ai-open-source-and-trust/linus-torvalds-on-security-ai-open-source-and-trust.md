
<!--
title: 李纳斯谈论安全、人工智能、开源和信任
cover: https://cdn.thenewstack.io/media/2024/04/855ce6ac-torvalds-hohndel-02.jpg
-->

即使在一个充斥着上游安全问题、过分炒作的 AI 和其他人的硬件漏洞的世界里，Torvalds 仍然保持着他毕生的对开源开发的热爱。

> 译自 [Linus Torvalds on Security, AI, Open Source and Trust](https://thenewstack.io/linus-torvalds-on-security-ai-open-source-and-trust/)，作者 David Cassel。

西雅图——周三，Linux 创始人 [Linus Torvalds](https://thenewstack.io/linus-torvalds-on-community-rust-and-linuxs-longevity/) 在 [Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention)在西雅图举办的[北美开源峰会](https://thenewstack.io/opentofu-vs-hashicorp-takes-center-stage-at-open-source-summit/)上进行了一场主题采访。Torvalds 由早期 Linux 贡献者（目前是 Verizon 开源项目办公室的负责人）[Dirk Hohndel](https://www.linkedin.com/in/dirkhohndel/) 采访——号称这是一场“壁炉谈话”。

但明确表现出来的是，Torvalds 毕生都热爱开源开发——以及如何在充斥着上游安全问题、过度炒作的 AI 和其他人的硬件 Bug 真实世界中进行开源开发。

虽然他们的谈话从一段颇具幽默感的交流开始……

**Hohndel:** 众所周知，内核开发包括很多戏剧化因素，并有很多高风险的讨论……例如，一个再次重现丑恶头颅的重要主题就是 tab 与空格。

**Torvalds:** 哦，基督…

## 超出你控制的问题

![](https://cdn.thenewstack.io/media/2024/04/6579aabe-torvalds-03-225x300.jpg)

*Linus Torvalds*

Hohndel 称，报道 Torvalds 加入制表符（用于捕捉无法正确转换为空格符的解析工具）的技术新闻网站是对开源项目的一种胜利——“标志着 Linux 的成熟度和健康状况，一条小小的评论就能产生新闻文章。” 

但随后 Hohndel 转向“不受你的控制，但你最终需要处理的问题”的话题——特别是，“又一轮的硬件缺陷”。Torvalds 认同诸如最新发现的 Spectre v2 漏洞之类的故障令人沮丧——但并非出于明显的原因。

“我涉足内核是因为我对硬件感兴趣，”Torvalds 强调说。但是他也热爱开源开发，并且“真的非常令人沮丧的是，你遇到了这些在技术上饶有兴趣的问题，但随后这些问题因为这些保密而变成了可怕的体验……”

> “我担心 RISC-V 将会犯下过去所有人犯过的同样错误。” ——  Linus Torvalds

Torvalds 说，对于快速反应的软件开发者来说，面对更慢的硬件开发速度会令人沮丧。（“哦，我们有五代硬件在事后无法修复，并且在能够帮助解决问题的实际新硬件问世之前还需要几年时间。”）“最终，这会令人非常沮丧 — 连同因任何安全问题而产生的所有公关活动。” 

Hohndel 问道，事情是否会由于开源硬件变好——尤其是在 RISC-V 发展了五年之后。但 Torvalds 并未被说服。“我担心的是 RISC-V 会犯与之前所有人相同的错误……当 RISC-V 演变成一个更加庞大、部署广泛的平台时，他们将会遇到与我们在 ARM 方面相同的各种问题，而 x86 之前也遇到过。他们需要花费几代时间才能够意识到‘哦，我们没想到’——因为他们有新的人员参与。”

但是，如果硬件开发放在公开场合，那么这会不会让软件开发人员更容易警告他们不要重蹈过往的错误呢？

“Verilog [标准硬件描述语言] 甚至内核之间存在相当大的差距，”Torvalds 回答，“不要去想堆栈上更高的部分，你在那里距离硬件工作非常遥远，你简直对硬件工作方式毫无概念。因此，跨越这一巨大的鸿沟非常困难。”

然后，Hohndel 做出了一个有趣的观察。十年前，仅仅是将 x86 移植到一个新平台都是一件困难的事情，但“今天，大多数人甚至都不知道他们是在 [AWS] Graviton…还是 AMD 或英特尔芯片上运行的。在云中，所有内容看起来都完全一样，具有相同的软件规范。只是价格不同。

而 Torvalds 说“那是开源承诺之一。人们十年前就说这是真的”。

“十年前那并不是真的。但现在肯定达到那种程度了”。


## 依赖信任

![](https://cdn.thenewstack.io/media/2024/04/1a7b36eb-torvalds-hohndel-03-300x225.jpg)

*Torvalds 和 Hohndel*

但最近，开源社区面临着一个严峻的提醒，即安全问题也可能来自另一个方向——维护者社区。当被问及最近的 [xz Util 漏洞](https://thenewstack.io/linux-xz-backdoor-damage-could-be-greater-than-feared/) 时，Torvalds 分享了自己的观点——首先强调，即使是专有软件也依赖信任。“[用户]依赖对公司的信任。但公司内部也依赖信任——对员工的信任。而这种信任可能会被破坏。”

“如何找出它何时被破坏是一个悬而未决的问题。”

Torvalds 从数十年的经验中谈到。Torvalds 说，即使像 Linux 这样的长期开源项目也“以前见过这种情况”，他回忆起 [2021 年事件](https://thenewstack.io/university-of-minnesota-researchers-tried-to-poison-the-linux-kernel-for-a-research-project/)，明尼苏达大学的研究人员测试了将不良内核补丁上游发送到多容易。（“那实际上是一个有趣的研究。他们只是做得不是很好。他们没有告诉第三方这件事，他们只是给我们发送了不良补丁。”）但现在，开源生态系统已经看到了实际的恶意尝试将不良代码上游发送——在Torvalds 所说的“实际上没有人明确设置任何闸门来尝试捕获这种情况”的世界中。

然而，Torvalds 也看到了一个充满希望的迹象。无论是 xz 还是学生们试图在 2021 年为内核上传的那些不良补丁，“在这两种情况下，它们实际上都被相当快地捕获到了。”这一事实“确实暗示了相当强的稳定性——这些东西确实会被捕获。”

即便如此，Torvalds 承认，“显然这是一个警钟——毫无疑问……我认为我们会看到很多工作投入到某种信任模型中，人们会看到，‘哦，这是一个新人’，或者‘这是一个与以前行为不同的新人’。”

Hohndel 指出，在 Linux 开发者社区的深处，签名要求包括面对面会面——以及政府颁发的身份证件。Torvalds 同意 Hohndel 的观点，即最好的防御是一个健康的社区。

Hohndel 继续指出，“Linux 内核拥有这个令人难以置信的庞大社区，但它也是一个令人难以置信的深度交织和联系紧密的社区，其中存在着多年的、数十年的关系。”

但这促使 Torvalds 提醒——Linux 的内核是一个非典型的开源项目。“很多开源项目，即使是非常核心的项目，基本上都是由一两个人或三个人运行的……”

## 开源的 AI？

![](https://cdn.thenewstack.io/media/2024/04/9c30582a-torvalds-02-225x300.jpg)

*Linus Torvalds*

在某一点上，Hohndel 引入了 AI 这个话题，并指出可怕的预测是它有一天会取代程序员、作者、电影创作者和工作。“所以你将被一个 AI 模型取代。”

“终于！” Torvalds 开玩笑说。

Torvalds 更严肃地回应说：“不……我讨厌炒作……我个人的意见是，让我们等待 10 年，看看在做出所有这些疯狂的‘你的工作将在五年内消失’的声明之前它实际上会走向何方。”

但编码工具中的 AI 呢？Torvalds 承认他对 AI “持乐观态度”，并且“期待着实际找到错误的工具”。由于内核开发人员（和其他项目）已经虔诚地使用他们拥有的工具，“让工具变得更智能并不是一件坏事”。

他称更智能的工具为“只是下一个不可避免的步骤……但我认为它不一定像有些人所说的那样悲观和可怕，我绝对不认为它是由那些向你伸手要钱的人所说的应许世界。”

当 Torvalds 警告他的听众时，发生了一次有趣的交流，“你需要对科技行业中的整个炒作周期保持一点愤世嫉俗……在 AI 之前是加密，在加密之前，无论是什么。”

“云原生，”Hohndel 建议。（补充一下，当时“前面一个响亮的声音”说“那不是炒作！”）

但 Torvalds 重申了他呼吁谨慎判断新闻的观点。“我的意思是，炒作？炒作背后总有一丝真实性。但你需要小心炒作背后的所有废话。”

## 开源的意义

![](https://cdn.thenewstack.io/media/2024/04/00b72265-hohndel-01-225x300.jpg)

**Dirk Hohndel**

在整个半小时的采访中，我们瞥见了在 30 多年的 Linux 内核开发后，Torvalds 的个人动机。当 Hohndel 说[开放数据](https://thenewstack.io/linux-foundation-overture-maps-the-globe-with-open-data/)几乎是更有趣的问题时，Torvalds 反射性地回答“不，不是”，然后补充说“对我来说不是”。但 Linux 基金会确实有开放数据项目，而且“对其他人来说更有趣。我认为，对我来说，开源的意义在于不同的人对不同的事物感兴趣……我一直对 CPU 实际工作原理的底层细节感兴趣。这就是我仍在致力于内核的原因。”

临近结束时，Torvalds 说他无意启动任何新项目。“对我来说，Linux 解决了我所有的问题，早在 92 年，也许是 93 年。如果不是因为其他人过来并说‘嘿，我需要这个’，我不会继续下去。”

让项目继续进行的事情是“‘嘿，这实际上对其他人有用’的事实。因为如果它只是我的东西，从长远来看它并不真正有趣。”
