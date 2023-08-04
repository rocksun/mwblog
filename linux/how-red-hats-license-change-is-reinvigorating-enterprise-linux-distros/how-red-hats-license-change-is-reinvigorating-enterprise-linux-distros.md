# 红帽许可证之变：如何为企业 Linux 发行版注入新活力

在软件自由保护协会的新会议上，一场充满活力的主题演讲小组展示了 Linux 发行版维护者如何应对 RHEL 最近的开源限制。

翻译自 [How Red Hat’s License Change Is Reinvigorating Enterprise Linux Distros](https://thenewstack.io/how-red-hats-license-change-is-reinvigorating-enterprise-linux-distros/) 。

![](https://cdn.thenewstack.io/media/2023/08/a853428c-3608f612-screenshot-from-keynote-panel-at-sfcs-first-fossy-conference-sfcs-bradley-kuhn-almalinuxs-benny-vasquez-ciqs-jeremy-alison-oracles-jim-wright-1024x559-1.jpg)

7 月中旬，在俄勒冈州波特兰市的俄勒冈会议中心，迎来了软件自由保护协会（[Software Freedom Conservancy](https://sfconservancy.org/)）举办的全新会议——[自由与开源软件年度大会](https://2023.fossy.us/)。

大会的[首个主题演讲](https://sfconservancy.org/blog/2023/jul/19/rhel-panel-fossy-2023/)小组竟然是关于红帽公司最近宣布计划改变其 Red Hat Enterprise Linux（RHEL）源代码许可的热烈讨论——实质上是将其藏在订阅者的付费墙后。

当天的问题是：下游 Linux 供应商应该如何应对？

小组成员阐明了各自的未来计划——以及对违反开源原则的立场。

但这次讨论也捕捉到了开源社区的一些原始热情——以及这一时刻的热度。

## 澄清形势

讨论的主持人是 [Bradley M. Kuhn](https://github.com/bkuhn)，他是软件自由保护协会的政策研究员/驻地黑客。小组成员包括受到红帽决定影响的各个组织的代表：

- [Benny Vasquez](https://www.linkedin.com/in/bennyvasquez/)，[AlmaLinux OS 基金会](https://almalinux.org/members/)主席。
- [Jeremy Alison](https://www.linkedin.com/in/jeremyallison/)，[Samba](https://thenewstack.io/create-a-samba-share-and-use-from-in-a-docker-container/) 创始人之一，CIQ（Creek and the Cave）的 [Rocky Linux](https://thenewstack.io/centos-creator-gregory-kurtzer-discusses-his-new-distro-rocky-linux/) 软件工程师。
- [James（Jim）Wright](https://www.linkedin.com/in/james-wright-446140/)，[甲骨文](https://developer.oracle.com/?utm_content=inline-mention)公司的首席架构师，负责开源政策/战略/合规/联盟事务。甲骨文拥有自己的 Linux 发行版，主要基于 RHEL。

Kuhn 首先承认，有一些公司没有派代表参加。“红帽自己没有回应我们对于他们加入此小组讨论的多次邀请，”Kuhn 告诉听众。（尽管上周红帽重申了其对开源的承诺，[告诉 Ars Technica](https://arstechnica.com/information-technology/2023/07/almalinux-says-red-hat-source-changes-wont-kill-its-rhel-compatible-distro/) “我们宁愿在 CentOS Stream 中一起合作，以实现可能的改进。”）

而 SUSE —— 最近在其[自己的 RHEL 分支上投资了超过 1000 万美元](https://www.suse.com/news/SUSE-Preserves-Choice-in-Enterprise-Linux/) —— “也受邀了，但他们告诉我们，他们无法在短时间内派人去波特兰参加这个小组讨论。”（不过 SUSE 的公告中包含 CIQ CEO / Rocky Linux 创始人 Gregory Kurtzer 的一份声明，称 CIQ “很高兴与 SUSE 合作，推进开放式企业 Linux 标准。”）

但 Kuhn 的第一个问题似乎旨在澄清基本情况。他问小组成员，如果你想重建 RHEL，仅仅支付红帽的订阅费用有什么问题。AlmaLinux 的 Vasquez 解释说事情没有那么简单。“他们要求我们与他们合作的方式明确不允许这样做——不要注册帐户并使用该代码重新打包并分发… ”

Samba/CIQ 的 Alison 也表示同意。“红帽的协议使这很难做到，因为实质上他们要求你放弃 GPL 赋予你的一些权利… 他们要求你放弃用户应该拥有的一些自由。不幸的是，我认为这是一个不合理的要求。”

SFC 的 Kuhn 后来开玩笑说，红帽的商业模式是“如果你行使 GPL 下的权利，你的钱在这里不值钱。”

但甲骨文的 Wright 表示有两种答案，并开玩笑地说他首先会“以甲骨文的方式来回答”。为什么不支付红帽来获得源代码？“因为我不想给你钱！”

“但更超越于此，我觉得这与社区规范本质上地和不可调和地冲突，我们都是利益相关者。自由软件基金会的‘自由软件’定义要求软件可以自由重新分发。开源促进会的‘开源’定义要求软件可以自由重新分发，并且源代码要公开。” 甚至在红帽自己的网站上还有一个名为“[什么是开源](https://www.redhat.com/en/topics/open-source/what-is-open-source)？”的网页。Wright 说，红帽甚至没有遵循自己的定义。

“第一段的第二句话说‘开源软件是设计成可以公开访问的代码——任何人都可以查看、修改和分发代码，如他们所愿’… 当你关闭这个源代码的可用性，这是否是设计成可以公开访问的？当你只在合同条款下提供它，明确规定你不能重新分发代码时，任何人都能如他们所愿地查看、修改和分发代码吗？不行。

“结论是无法避免的——他们正在做的与任何人对开源的想法并不一致，甚至是他们自己的。直到现在…”

Alison 赞扬红帽，“非常感谢他们创建了被认为是企业 Linux 标准的东西。人们想要 Alma、Rocky 和 Oracle，是因为红帽在这方面建立了如此强大的品牌，他们对此应该得到很多赞誉。” 但 Alison 将红帽的新立场描述为“来红帽获取一切”。

“这不是客户想要的。他们想要一系列的选项来购买企业 Linux。”

## 自由与标准

Alison 后来重申了这一观点。“客户想要自由… 这就是自由软件和开源的全部意义。他们想要掌控自己的命运，他们不想被迫只从一个地方获得产品。我的意思是，如果你想要这个，直接买 Windows 不就行了吗？”

后来，AlmaLinux 的 Vasquez 提出了更强烈的观点。“红帽在为我们所有人树立了一个很棒的目标，但他们并不拥有企业 Linux 的权利。我们可以做到这一点，而不用与红帽进行一场尴尬的交谈… 我们可以克服这个问题。我们将继续构建企业 Linux，而不违反甚至不必与红帽争斗。我对此的看法就是这样。这就是 Alma 正在做的。我们只是会构建它…”

Samba/CIQ 的 Alison 也相信代码会从红帽中脱颖而出。“红帽多么努力地阻止人们这么做都没有关系。人们将会这么做。即使他们必须深入研究 CentOS Stream 的发布，找出与 RHEL 位数完全匹配的内容，他们也会这么做。永远不要低估一个无聊程序员的坚韧…”

后来，AlmaLinux 的 Vasquez 再次强调：“我们不怕在源代码中挖掘。”

当听众中的某人问下游发行版现在是否会添加一些在 RHEL 中不可用的新功能时，Samba/CIQ 的 Alison 说“是的，当然”，而 AlmaLinux 的 Vasquez 也愿意添加新功能。“百分之百——是的。我们为此感到兴奋的其中之一是这为我们打开了机会… 我们有各种各样的选择。”

实际上，这个小组讨论恰好在 AlmaLinux OS 基金会宣布决定放弃与 RHEL 的 1:1 兼容性几天后举行的。（要求是“我们将继续致力于根据我们社区的需求制作与 RHEL 对齐且 ABI 兼容的企业级长期 Linux 发行版，以实现可能的程度，并且运行在 RHEL 上的软件也可以在 AlmaLinux 上运行。”）

该博文指出，现在 AlmaLinux 可以在 RHEL 的发布计划之外接受错误修复，这个问题后来浮出水面。博文还指出，“我们将在我们的补丁中包含评论，其中包含我们所应用的补丁的链接。”

但在 SFC 的小组讨论中，甲骨文的 Wright 提醒听众，对 RHEL 兼容性的需求直接来自客户，其中一些客户将 RHEL 视为标准。也许他们自己的客户正在运行 RHEL。

之后，SFC 的 Kuhn 分享了他自己的想法，作为一个“软件自由狂热分子… 对于那些真正想要兼容性以便做专有软件的人，我的同情心显然是有限的。”

但甲骨文的 Wright 指出，这种不便也影响了针对该平台的开源项目。

## 客户与竞争

或许最有趣的交流是听众中的某人问，创造一个新的开放式企业 Linux 标准，发行版可以遵循这个标准的机会有多大？

“机会非常大…” AlmaLinux 的 Vasquez 回答。“这是非常新的事情——我们进行了三个星期，对吧？所以我认为每个人都认为这是显而易见的答案。我认为这是显而易见的下一步。我就说这么多。”

甲骨文的 Wright 回到了他之前提到的观点，最终将是客户决定。但 Wright 也表示，“在市场发展的程度上——回答你的问题——在市场要求我们标准化的程度上？我们都是响应的。”

Samba/CIQ 的 Alison 同意企业 Linux“是客户说了算”。因此，如果客户说“接近红帽但不完全是红帽就足够好”，那么我们就会这样。如果客户说“不，它必须是重建的，与 RHEL 逐字逐句兼容”，那么我们将尝试做到这一点。我们将尽力满足市场需求，我们将努力满足用户的要求。”

因此，如果这次讨论捕捉到了我们当下的瞬间，那么最终最有意义的是每个小组成员在 Kuhn 分配给他们的最后 10 秒内选择说的话。

甲骨文的 Wright 重新回顾了他之前提到的一个观点。（“所以，我们正在大规模招聘，对吧？我们会招聘很多人，以便拥有自己的兼容发行版。”）他在结束时再次提醒听众，“如果你想在开源 Linux 上工作，我们正在招聘。”

AlmaLinux 的 Vasquez 说他们也在寻找贡献者。“过来看看。我们在做很棒的事情。我对我们所看到的支持和兴奋感到非常惊讶。这会是一个美好的时光。”

Samba/CIQ 的 Alison 更进一步，分享了一个用来描述红帽举动的笑话。RHEL 是“踩踏耙子的官方操作系统。” 所以他的结束思想是，红帽的失误对其所有竞争对手都有好处。

“他们通过这样做引起了人们对红帽替代品的浓厚兴趣和激动。所以，谢谢！感谢这一点。我很感激！”
