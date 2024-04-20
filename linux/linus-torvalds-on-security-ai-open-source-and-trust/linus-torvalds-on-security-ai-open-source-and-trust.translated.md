# Linus Torvalds 谈论安全、人工智能、开源和信任

![Linus Torvalds 谈论安全、人工智能、开源和信任的特色图片](https://cdn.thenewstack.io/media/2024/04/855ce6ac-torvalds-hohndel-02-1024x768.jpg)

西雅图——Linux 创始人 [Linus Torvalds](https://thenewstack.io/linus-torvalds-on-community-rust-and-linuxs-longevity/) 星期三在西雅图举行的 [Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) 的 [北美开源峰会](https://thenewstack.io/opentofu-vs-hashicorp-takes-center-stage-at-open-source-summit/) 上进行了一场“主题采访”。Torvalds 接受了 [Dirk Hohndel](https://www.linkedin.com/in/dirkhohndel/) 的采访，Dirk Hohndel 是早期 [Linux 贡献者](https://thenewstack.io/linus-torvalds-on-why-open-source-solves-the-biggest-problems/)（目前是 Verizon 的开源计划办公室负责人）——这场采访被宣传为“炉边谈话”。

但 Torvalds 毕生对开源开发的热爱显而易见——以及它如何在充满上游安全问题、过分炒作的人工智能和其他人的硬件错误的现实世界中发挥作用。

尽管他们的谈话以一段幽默的交流开始……

**Hohndel：**我们都知道内核开发包含很多戏剧性和很多高风险的讨论……例如，一个再次抬头的重要话题是 [制表符与空格](https://thenewstack.io/spaces-vs-tabs-a-20-year-debate-and-now-this-what-the-hell-is-wrong-with-go/)。

**Torvalds：**哦，天哪……

## 超出你控制范围的问题

![](https://cdn.thenewstack.io/media/2024/04/6579aabe-torvalds-03-225x300.jpg)

Linus Torvalds

Hohndel 说 [技术](https://www.phoronix.com/news/Linux-Kconfig-Tabs) [新闻](https://www.theregister.com/2024/04/16/torvalds_complicates_his_indents/) [网站](https://arstechnica.com/gadgets/2024/04/linus-torvalds-reiterates-his-tabs-versus-spaces-stance-with-a-kernel-trap/) 报道 Torvalds [插入制表符](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?utm_source=anzwix&id=d5cf50dafc9dd5faa1e61e7021e3496ddf7fd61e)（用于捕获无法正确将它们转换为空格的解析工具）是对开源项目的一种胜利——“Linux 成熟和健康的标志，一条小评论就能产生新闻文章。”

但随后 Hohndel 转到“超出你控制范围的问题，但你最终还是要处理”的话题——具体来说，“[又一轮硬件错误](https://www.bleepingcomputer.com/news/security/new-spectre-v2-attack-impacts-linux-systems-on-intel-cpus/)。”Torvalds 同意新发现的 Spectre v2 漏洞令人沮丧——但并非出于显而易见的原因。

“我开始做内核是因为我对硬件感兴趣，”Torvalds 指出。但他也喜欢 [开源开发](https://thenewstack.io/whats-next-for-companies-built-on-open-source/)，而且“非常、非常令人沮丧的是，你遇到了这些技术上有趣的问题，但随后它们因所有秘密而变得糟糕透顶……”

“我担心 RISC-V 会犯与之前所有人相同的错误。”——Linus Torvalds

![](https://cdn.thenewstack.io/media/2024/04/f12b24e5-torvalds-04-225x300.jpg)

Linus Torvalds

Torvalds 说，对于反应迅速的软件开发人员来说，面对缓慢的硬件开发速度会令人沮丧。（“哦，我们有五代硬件，事后无法修复，还需要几年时间才能推出可以帮助你解决问题的实际新硬件。”）“这最终会非常令人沮丧——加上所有与任何安全问题相关的公关。”

Hohndel 问，开源硬件是否会让事情变得更好——尤其是在 RISC-V 开发五年之后。但 Torvalds 并不同意。“我担心 RISC-V 会犯与之前所有人相同的错误……当 RISC-V 变得更像一个大型、广泛部署的平台时，他们将遇到我们在 ARM 方面遇到的所有相同问题，而 x86 在他们之前也遇到过。他们需要几代人才能说，‘哦，我们没想到’——因为他们有新人参与。”

但如果硬件在公开环境中开发，这是否会让软件开发人员更容易警告他们不要重复过去的错误？

“Verilog [标准硬件描述语言] 甚至内核之间都有相当大的差距，”Torvalds 回答说，“更不用说堆栈更高的地方，你在那里远离硬件，以至于你真的不知道硬件是如何工作的。因此，很难跨越如此广泛的事物鸿沟。”
## 依赖信任

![](https://cdn.thenewstack.io/media/2024/04/1a7b36eb-torvalds-hohndel-03-300x225.jpg)

托瓦兹和霍恩德尔

但最近，开源社区面临着一个严峻的提醒，即安全问题也可能来自另一个方向——来自维护者社区。当被问及最近的 [xz Util 漏洞](https://thenewstack.io/linux-xz-backdoor-damage-could-be-greater-than-feared/) 时，托瓦兹分享了自己的观点——首先强调，即使是专有软件也依赖于信任。“[用户]依赖于对公司的信任。但同样，在公司内部，你依赖于信任——对你的员工的信任。而这种信任可能会被破坏。”

“以及如何找出它何时被破坏是一个悬而未决的问题。”

托瓦兹根据数十年的经验发表了讲话。托瓦兹说，即使像 Linux 这样的长期开源项目也“以前见过这种情况”，他回忆起 [2021 年事件](https://thenewstack.io/university-of-minnesota-researchers-tried-to-poison-the-linux-kernel-for-a-research-project/)，明尼苏达大学的研究人员测试了将错误的内核补丁上游发送到上游有多容易。（“那实际上是一项有趣的研究。他们只是做得不是很好。他们没有告诉第三方这件事，他们只是给我们发送了错误的补丁。”）但现在，开源生态系统已经看到了实际的恶意尝试将错误的代码上游发送到上游——在托瓦兹所说的世界中，“没有人真正明确地设置了网关来尝试捕获这一点。”

然而，托瓦兹也看到了一个充满希望的迹象。无论是 xz 还是学生们试图在 2021 年为内核上传的那些错误补丁，“在这两种情况下，它们实际上都被相当快地捕获到了。”这一事实“确实暗示了相当强的稳定性——并且这些东西确实会被捕获。”

![](https://cdn.thenewstack.io/media/2024/04/86056b62-torvalds-05-225x300.jpg)

Linus Torvalds

即便如此，托瓦兹也承认，“显然这是一个警钟——毫无疑问……我认为我们会看到很多工作投入到某种信任模型中，人们会看到，‘哦，这是一个新人’，或者‘这是一个与以前行为不同的人’。”

霍恩德尔指出，在 Linux 开发者社区的深处，签名要求包括面对面会议——以及政府颁发的身份证件。托瓦兹同意霍恩德尔的观点，即最好的防御是一个健康的社区。

霍恩德尔继续指出，“Linux 内核拥有这个令人难以置信的庞大，但同时又令人难以置信的紧密联系和联系的社区，其中多年、数十年的关系是这一切的核心。”

但这促使托瓦兹提醒——Linux 的内核是一个非典型的开源项目。“很多开源项目，即使是非常核心的项目，基本上都是由一两个人或三个人运行的……”

## 开源的 AI？

![](https://cdn.thenewstack.io/media/2024/04/9c30582a-torvalds-02-225x300.jpg)

Linus Torvalds

在一点上，霍恩德尔引入了人工智能的话题，并指出可怕的预测是它有一天会取代程序员、作者、电影创作者和工作。“所以你将被一个 AI 模型取代。”

“终于！”托瓦兹开玩笑说。

托瓦兹更严肃地回应说：“不……我讨厌炒作……我个人的意见是，让我们等待 10 年，看看在做出所有这些疯狂的‘你的工作将在五年内消失’的声明之前它实际上会走向何方。”

但编码工具中的 AI 呢？托瓦兹承认他对 AI “持乐观态度”，并且“期待着实际找到错误的工具”。由于内核开发人员（和其他项目）已经虔诚地使用他们拥有的工具，“让工具变得更智能并不是一件坏事”。

他称更智能的工具为“只是下一个不可避免的步骤……但我认为它不一定像有些人所说的那样悲观和厄运，我绝对不认为它是那些向外伸手要钱的人所说的应许世界。”

当托瓦兹警告他的听众时，发生了一次有趣的交流，“你需要对科技行业中的整个炒作周期保持一点愤世嫉俗……在人工智能之前是加密，在加密之前，无论是什么。”

“云原生，”霍恩德尔建议。（后来补充说，他从“前面的一个响亮的声音”那里听说过“那不是炒作！”）
**但 Torvalds 重申了他呼吁谨慎判断新闻的号召。**

“我的意思是，炒作？炒作背后总有一丝现实。但你需要小心围绕这一丝现实的所有废话。”

## 开源的意义

![](https://cdn.thenewstack.io/media/2024/04/00b72265-hohndel-01-225x300.jpg)

迪尔克·霍恩德尔

在整个半小时的采访中，我们瞥见了在超过 30 年的 Linux 内核开发后，Torvalds 的个人动机。当霍恩德尔说 [开放数据](https://thenewstack.io/linux-foundation-overture-maps-the-globe-with-open-data/) 几乎是更有趣的问题时，Torvalds 反射性地回答“不，不是”，然后补充说“对我来说不是”。但 Linux 基金会拥有开放数据项目，并且“对其他人来说更有趣。我认为，对我来说，开源的意义在于不同的人对不同的事物感兴趣……我一直对 CPU 实际工作原理的底层细节感兴趣。这就是我仍在研究内核的原因。”

临近结束时，Torvalds 说他无意启动任何新项目。“对我来说，Linux 解决了我所有的问题，早在 92 年，也许是 93 年。如果不是因为其他人出现并说‘嘿，我需要这个’，我不会继续下去。”

让项目继续进行的事情是“‘嘿，这实际上对其他人有用’这一事实。因为如果它只是我的东西，从长远来看它并不真正有趣。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、采访、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)