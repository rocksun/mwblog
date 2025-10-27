
<!--
title: 肯·汤普森：Unix的狂野不羁与黑客起源
cover: https://cdn.thenewstack.io/media/2025/11/91ab99cb-ken-thompson-2024-screenshot-from-computer-history-museum-acm-oral-history.png
summary: Ken Thompson回顾Unix早期，强调贝尔实验室的开放协作文化。Unix从失败中意外诞生，社区推动其发展。贝尔实验室影响他一生，后来参与Go语言开发。
-->

Ken Thompson回顾Unix早期，强调贝尔实验室的开放协作文化。Unix从失败中意外诞生，社区推动其发展。贝尔实验室影响他一生，后来参与Go语言开发。

> 译自：[Ken Thompson Recalls Unix's Rowdy, Lock-Picking Origins](https://thenewstack.io/ken-thompson-recalls-unixs-rowdy-lock-picking-origins/)
> 
> 作者：David Cassel

82岁的Ken Thompson对[Unix操作系统](https://thenewstack.io/unix-co-creator-brian-kernighan-on-rust-distros-and-nixos/)的早期岁月——以及一群喧闹的极客共同构建它的场景——有着一些令人惊叹的回忆。

本月，硅谷的计算机历史博物馆与计算机协会合作，发布了[一段长达四个半小时的特别口述历史](https://computerhistory.org/blog/a-computing-legend-speaks/)，由技术历史学家[David C. Brock](https://computerhistory.org/profile/david-brock/)于18个月前录制。Thompson尽职尽责地回顾了他职业生涯中的[许多](https://thenewstack.io/what-made-golang-so-popular-the-languages-creators-look-back/)亮点——从他在C编程语言和Unix上的工作，到“贝尔实验室的Plan 9”操作系统，再到[Go编程语言](https://thenewstack.io/what-made-golang-so-popular-the-languages-creators-look-back/)。

但从中流露出的，是他对曾与他共事的人们的感激，以及他们在一个开放的环境中共同实验、探索新兴技术极限的机会。这是一个关于好奇心、一种随性而发的巧合感以及社区持久价值的故事。

在此过程中，Thompson还讲述了一个故事：他饲养了一只小鳄鱼，那是朋友寄到他[贝尔实验室](https://thenewstack.io/how-two-bell-labs-researchers-set-the-rules-for-the-modern-compiler/)办公室的。（“它就是通过邮件送来的……它们可不是最可爱的宠物。”）

## Unix的意外诞生

回到1966年，当时23岁的Thompson在贝尔实验室的第一个项目是命运多舛的[Multics](https://multicians.org/history.html)，这是与麻省理工学院和通用电气合作的项目，Thompson回忆说它“糟糕透顶……庞大、缓慢、丑陋且昂贵”，需要一台巨大的专门建造的计算机才能运行，并且“注定在开始之前就已死亡”。

但当Multics项目中止时，“那台计算机完全空闲了——这台独一无二的庞然大物计算机……于是我利用了它。”

Thompson当时想使用[CRAM](https://retrocomputingforum.com/t/from-1960-cram-card-based-external-memory-by-ncr/3111)，一种带有高速磁鼓存储器的数据存储设备，但就像当时的磁盘存储一样，从内存中读取数据很慢。

[![Drum memory](https://cdn.thenewstack.io/media/2025/10/38fcd561-pamiec_bebnowa_1-drum-memory-photo-via-wikipedia.jpg)](https://cdn.thenewstack.io/media/2025/10/38fcd561-pamiec_bebnowa_1-drum-memory-photo-via-wikipedia.jpg)

一个磁性“磁鼓存储器”数据存储设备

Thompson认为他可以通过同时（和重叠）的内存读取来改善这种情况，但这当然需要用于测试的程序，以及加载和运行它们的方法。

视频

YOUTUBE.COM/THENEWSTACK

技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，观看我们所有的播客、访谈、演示等内容。

[订阅](https://youtube.com/thenewstack?sub_confirmation=1)

“突然之间，在不知不觉中——我是说，这正悄悄地向我袭来……突然它就成了一个操作系统！”Thompson最初的内存读取工作成了Unix文件系统的“磁盘部分”。他仍然需要一个文本编辑器和一个用户切换多路复用层（以及一个编译器和汇编器来编写程序），但它已经拥有了文件系统、磁盘驱动程序和I/O外设。

Thompson想知道，是否因为他被明确告知*不要*从事操作系统工作，所以花了这么长时间才认识到它的潜力。他被告知，Multics对贝尔实验室来说“是一次糟糕的经历”。“我们投入了大量的钱，却一无所获！”

“我实际上受到了训斥，说‘不要做操作系统。贝尔实验室不再搞操作系统了！’”

## 一位数的用户ID

但现在Unix有了它的第一个用户社区——未来的传奇人物，如Dennis Ritchie、Doug McIlroy、Robert Morris以及偶尔出现的[Brian Kernighan](https://thenewstack.io/brian-kernighan-remembers-the-origins-of-grep/)。（“所有的用户ID都是一位数。这无疑设定了一个限制。”）Thompson回忆起与Rudd Canaday在办公室的黑板上设计Unix文件系统的情景——他们使用贝尔实验室的一个特殊电话号码，可以口述内容，第二天就会收到打印好的记录。而Joe Ossanna凭借其在贝尔实验室官僚体系中游刃有余的特殊才能，“把事情办成了”，最终为Unix团队争取到了一台至关重要的PDP-11。

“我们被告知不行，‘因为我们不从事操作系统业务。’”但Ossanna知道专利部门正在评估一个用于准备文档的第三方系统——Ossanna提出了一个内部替代方案。“所以我们得到了第一台PDP-11来做*文字处理*。”

[![Ken Thompson (sitting) and Dennis Ritchie at PDP-11](https://cdn.thenewstack.io/media/2018/07/1b0075b6-ken_thompson_sitting_and_dennis_ritchie_at_pdp-11_2876612463-photo-by-peter-hamer-via-wikipedia-1024x820.jpg)](https://cdn.thenewstack.io/media/2018/07/1b0075b6-ken_thompson_sitting_and_dennis_ritchie_at_pdp-11_2876612463-photo-by-peter-hamer-via-wikipedia-1024x820.jpg)

Ken Thompson（坐者）和Dennis Ritchie在PDP-11旁

历史表明，这部分原因在于支付这笔钱的部门“有多余的资金，如果他们不花掉，第二年就会失去……”

因此，年轻的Unix社区新增了五到八名用户，Thompson回忆道，“专利部的秘书们，在我们的系统上撰写专利！”

## Unix室的友谊

Thompson回忆说，那台PDP-11最终被安置在“六楼的一个地方，我们清理了一台自动售货机和几个装着1920年储存下来的废品的笼子”。他们最终安装了第二台PDP-11，这使房间变成了“一个充满各种事情的温床”，讨论着网络——以及即将用于文档的排版机。Thompson称之为Unix室，他们中的大多数人最终都将电话分机接入了那个房间。（它甚至有自己的呼叫交换PBX……）

那里有友情和笑声。他后来补充道，几乎是顺便提及，“在Unix室里，我们过去经常撬锁偷东西。”（当一位秘书发现安保人员给她的车——停错了区域——锁上了“停车靴”时，“我们走下去，撬开了锁，偷走了停车靴。在那之后，我们慢慢地把所有四只停车靴都偷走了，把它们藏在Unix室的架空地板下……”）

结局是？“安保主管过来恳求我们。‘如果你们把停车靴还给我们，我们就不会为难你们的秘书了。’”

交易达成。

[![Ken_Thompson_and_Dennis_Ritchie--1973 (public domain via Wikipedia)](https://cdn.thenewstack.io/media/2025/10/f72126e7-ken_thompson_and_dennis_ritchie-1973-public-domain-via-wikipedia.jpg)](https://cdn.thenewstack.io/media/2025/10/f72126e7-ken_thompson_and_dennis_ritchie-1973-public-domain-via-wikipedia.jpg)

Dennis Ritchie（左）后来表示，他们的动机是构建一个“可以形成一个社群”的系统，但Thompson说这更多是对已发生事情的描述，而非实际的设计目标。

Thompson回忆起在贝尔实验室餐厅定期举行的“Unix午餐会”，这“促进了思想和事物的共生。这很棒。”尽管这总是发生在餐厅停止供餐后的几分钟内。“如果我迟到了，我就会买麦当劳，然后带着我的麦当劳坐在餐厅里。他们为此常常生我的气……”

## 从社区中成长

回首过去，Thompson将C语言和Unix的成功归功于贝尔实验室及其无压力/无用户的环境。“这本质上是一种‘你想做什么就做什么’的氛围，而且‘为了任何你想为之做的人’……贝尔实验室是这类编程的迄今为止最大的贡献者。”

视频

YOUTUBE.COM/THENEWSTACK

技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，观看我们所有的播客、访谈、演示等内容。

[订阅](https://youtube.com/thenewstack?sub_confirmation=1)

贝尔实验室是一个兼收并蓄的组合，但这个社区带来了意想不到的红利。虽然Lee McMahon最初被聘为语言学研究员，但他最终为Unix团队获得了机器可读的词典，以及机器可读版的《联邦党人文集》。（当整个文本无法放入他们的文本编辑器*ed*时，Thompson[著名地创建了逐行模式扫描工具*grep*](https://thenewstack.io/brian-kernighan-remembers-the-origins-of-grep/)。）

最后，Thompson说Unix之所以能发展壮大，原因很简单：人们喜欢它。它在贝尔实验室内部传播开来，最初用于“行政事务，输入故障单……”但由于这是一家电话公司，“后来它开始实际处理一些交换事务，诸如此类。它越来越深入贝尔系统的核心，变得非常受欢迎。”

## 开放早于开源

Thompson认为Richard Stallman在开放源代码哲学方面做出了更大的贡献。“但Unix也有点这种精神。”也许它源于Dennis Ritchie所回忆的，围绕Unix形成的那个社群。“出于某种原因，我想仅仅因为我和Dennis，一切都是开放的……”

那就是他们的运作方式。“我们对文件有保护——如果你不想让别人读取它，你可以设置一些位，然后就没人能读取它们了，对吧？但没有人*在任何东西上设置*那些权限……所有的源代码都是可写的，任何人都可以写！它就是开放的……”

“如果你对一个编辑器有想法，你就会把它拿出来，在上面修改，然后放回去……当时有个口头禅是，‘你碰了它，你就是它的主人。’”

Thompson举了一个例子：贝尔实验室的同事P. J. Plauger，他后来与他合著了1974年的书《编程风格要素》。Thompson回忆说，Plauger也是一位[职业科幻作家](https://www.isfdb.org/cgi-bin/ea.cgi?3011)，“他正在写的东西在他的目录里，对吧？所以，我们都会进去，在他写作时阅读它……我们都会回复，‘你应该杀了这个人，把他移到这边，然后把他变成绿色！’之类的。”

“他并不介意，因为那只是当时Unix的理论……

“我想那产生了社群。仅仅是因为它就像在黑板上写东西一样——每个人都能看到。”

贝尔实验室的更多实验成果走向世界，后来在Plan 9操作系统上的一些工作融入了UTF-8标准，而该标准支撑着当今大多数的Web连接。

## 离开贝尔实验室之后

Thompson于2000年离开贝尔实验室，那是贝尔系统分拆之后。（“它变了；真的不一样了……你必须为自己所做的事情辩护，这超出了我的职责范围。”）但他在那里的三十年似乎影响了他余生。

Thompson首先转到一家名为Entrisphere的网络设备公司，在那里工作了六年——之后加入Google是自然而然的下一步。Entrisphere的负责人已经去了Google，并极力敦促Thompson也去——事实证明，Google首席执行官Eric Schmidt是一位老朋友，他实际上在1975年曾在贝尔实验室工作过。（Thompson说Google给了他“一个极好的报价”……）

在Google，Thompson“稍微”从事了Android安全方面的工作。（“我发现了一些具体问题，但总的来说，做得非常好。”）但最终Thompson加入了创建Go编程语言的三人团队。

他与Rob Pike一起工作，Rob Pike正是他近30年前在贝尔实验室的老战友之一！

视频

YOUTUBE.COM/THENEWSTACK

技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，观看我们所有的播客、访谈、演示等内容。

[订阅](https://youtube.com/thenewstack?sub_confirmation=1)
视频

YOUTUBE.COM/THENEWSTACK

技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，观看我们所有的播客、访谈、演示等内容。

[订阅](https://youtube.com/thenewstack?sub_confirmation=1)

由Sketch创建的群组。

![](https://cdn.thenewstack.io/media/2023/11/82081813-7zddypfe_400x400.jpg)

David Cassel是旧金山湾区的一位自豪的居民，他在那里报道科技新闻已有二十多年。多年来，他的文章出现在CNN、MSNBC和《华尔街日报互动版》等各种媒体上……

[阅读更多David Cassel的文章](https://thenewstack.io/author/destiny/)