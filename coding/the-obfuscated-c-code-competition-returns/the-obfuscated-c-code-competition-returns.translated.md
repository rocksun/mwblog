# “混淆C代码”大赛回归

![“混淆C代码”大赛回归的特色图片](https://cdn.thenewstack.io/media/2024/11/c7e3eb34-c-safety-1024x683.jpg)

经过四年的休整，“国际混淆C代码大赛”将于2025年荣耀回归。

IOCCC的目标：

- 在规则范围内编写最晦涩/最混淆的C程序。
- 以一种讽刺的方式展现编程风格的重要性。
- 用不同寻常的代码来考验C编译器。
- 阐述C语言的一些细微之处。
- 享受C语言的乐趣！

随着乐趣再次升级，评委们将从1月31日开始接受精彩的[新的“混淆C”程序](https://thenewstack.io/a-tradition-continues-the-international-obfuscated-c-code-contest/)（截止日期为4月1日——愚人节）。但他们也在过去四年里对[大赛网站](http://www.ioccc.org/)进行了大规模更新——因此，即使是过去40年存档的获奖作品，现在也“能够被现代Unix/Linux系统编译和运行”。

[更新后的FAQ](http://www.ioccc.org/faq.html)承认，该网站“已经转向更具教育意义的主题”，而不是保持代码的混淆性。

也许组织者们最终意识到了自己作为文化偶像的地位——他们持续扮演着以令人难以置信的复杂性和创造力的例子激励年轻程序员的角色，同时见证着自己编程历史的点点滴滴。

尽管如此，本着比赛的真正精神，他们有时似乎是在边走边想。

![Landon Curt Noll的GitHub个人资料截图](https://cdn.thenewstack.io/media/2025/01/a5947686-screenshot-from-landon-curt-nolls-github-profile.png)
IOCCC联合创始人Landon Curt Noll的GitHub个人资料截图

## 巧克力与隐写术的邂逅

这种趣味性似乎无处不在——最终也变得具有感染力。“多年来，不止一位IOCCC评委曾以一些优质巧克力贿赂另一位IOCCC评委，以使其投票支持获奖作品，”[官方指南](http://www.ioccc.org/next/guidelines.html)指出。因此，一个[2012年的参赛作品](http://www.ioccc.org/2012/vik/index.html)展示了它的隐写术应用——将源代码隐藏在图像中——使用了美味巧克力的照片。

官方规则的[第26条规则](http://www.ioccc.org/next/rules.html#rule26)完全由包含所有26个字母且每个字母恰好出现一次的无意义句子组成。与此同时，大赛的官方FAQ对诸如[为什么他们会在Mastodon上](http://www.ioccc.org/faq.html#try_mastodon)之类的问题给出了俏皮的答案。“IOCCC不再使用Twitter，或者任何一个似乎缺乏冲动控制力的人（据称）现在称之为他们平台的东西。IOCCC更喜欢驻留在[联邦宇宙](https://fediverse.info/)。”

以及[比赛是如何开始的？](http://www.ioccc.org/faq.html#ioccc_start)“那是一个黑暗而暴风雨的夜晚……”

## 争夺最差的头衔

比赛始于1984年3月23日，当时23岁的Landon Curt Noll与Larry Bassel在国家半导体公司合作，将[UNIX](https://thenewstack.io/unix-creator-ken-thompson-to-keynote-scale-conference/)移植到该公司的微控制器上。Bassel正在与Bourne shell中的一个bug作斗争，而Noll正在处理早期BSD版本的finger命令。很快，他们[宣布了一场比赛](https://groups.google.com/g/net.lang.c/c/lx-TAuEyeRI/m/HdOOnNx6LC0J?hl=en)，“与周围最差的C语言黑客竞争”，参赛作品开始大量涌入。

Noll在FAQ中写道：“当我们开始收到来自美国以外的邮件时，我和Larry决定在名称中加入‘国际’二字。”

即使在第一年，他们也看到了一些编码界大腕的参赛作品，包括贝尔实验室的程序员[David Korn](https://en.wikipedia.org/wiki/David_Korn_(computer_scientist))，Korn shell（1987年）的创建者，以及[Perl编程语言](https://thenewstack.io/week-programming-renaming-perl-save-terminal-unpopularity/)的创建者[Larry Wall](https://en.wikipedia.org/wiki/Larry_Wall)（1986年，1987年）。这设定了一个高标准，并在比赛的持续过程中延续了下来。

在过去的40年里，评委们已经评选出了197位不同的获奖者。其中一些人拥有自己的维基百科词条：

- Google DeepMind的研究员[Nicholas Carlini](https://en.wikipedia.org/wiki/Nicholas_Carlini)赢得了2020年的“[最佳展示：滥用libc]”奖](https://www.ioccc.org/2020/carlini/index.html)。
- 1989年，“最佳展示”奖颁给了
Ora Lassila is known for his early work on the semantic web and the RDF specification.  Now a long-time member of the W3C advisory board and Chief Graph Technology Architect at AWS, Lassila won an award in 1989 for writing a compact Lisp interpreter.  Other winners included notable figures in the C language community, such as Walter Bright, creator of the D programming language and the Zortech C++ compiler, and Fabrice Bellard, creator of the Tiny C compiler.

Several notable computer science academics were also involved, including David Applegate, Lennart Augustsson, Daniel J. Bernstein, Vern Paxson, Diomidis Spinellis, and John Tromp.

The guidelines even included a special rule specifically for Peter Honeyman, Professor Emeritus at the University of Michigan:

*“In the past, some have attempted to obfuscate their identities by including comments from well-known Internet figures such as Peter Honeyman.  The judges have caught on to this trick, and therefore consider any obfuscated source code or data files claiming to be from Honeyman to not be from Honeyman.”*

The implication seems to be that beautiful obfuscated C code should also be *anonymous* obfuscated C code—at least until judging is complete. This led to a funny and remarkable coincidence with a 1990 winning entry. The judges' comments caught the fact that the ANSI C standard now included three-character “trigraphs,” “making it easier to write programs that are hard to read.”  Therefore, they established a special award for programmer Larry Jones, for producing 46 lines of undulating C code (mostly question marks).

After receiving the award for “the most egregious abuse of the C language by the ANSI committee,” Jones contacted the judges and posed a simple question: “Did you know I *am* a member of the committee?”

The judges assured him it was a coincidence, and Jones added that he was “very grateful” for the award, though he “really hoped for something like ‘closest to line noise.’”

But mixed in with all the hilarity, the International Obfuscated C Code Contest remains almost an accidental yearbook for each generation of programmers, bringing them together to showcase our own collective history.  Mary Ann Horton also contributed; a BSD contributor known as a “Usenet and internet pioneer,” and an early transgender rights activist.  “Inventing email attachments is one thing,” Horton said in a 2022 biography. “Doing it while transitioning from male to female and paving the way for transgender rights in the workplace is another.”

Somewhere in there is George Sicherman, who rose to fame for creating, in 1978, an alternative numbering scheme for dice that still produces the same probability distribution as ordinary dice.

## Throughout History

All of this is part of the event's long and storied history.  “We suggest you avoid trying for ‘smallest self-replicating’ source code,” the guidelines warn—because someone already won with a 0-byte entry.

But other milestones are equally quirky and unpredictable:

- Programmer Thomas Covell tattooed the code of a first-place winner onto his arm.
- Then there’s Bill Gates, who in a 1993 trivia contest asked contestants the name of the event that called for creating “the hardest-to-read, most creative, most bizarre, yet functional C program.” One contestant answered “Windows.” That year, the contest added a commemorative Bill Gates Award.
- Even the new website’s logo links to a 2011 IOCCC entry, a ray tracer whose default output is…the website’s logo. (It won the 2011 “Most Glittery” award.)
有一种感觉，任何事情都可能发生，也许是因为评委们确实是在边走边编。官方指南[http://www.ioccc.org/next/guidelines.html](http://www.ioccc.org/next/guidelines.html)解释说：“当提交作品数量减少到大约25份时，我们开始形成奖项类别。”因此，每年最终奖项的名称“将根据我们收到的提交作品类型而有所不同”。

有一些C语言相关的奖项类别，例如“最糟糕的C预处理器滥用”和“最不可能成功编译”。一个[2020年的参赛作品](http://www.ioccc.org/2020/tsoj/index.html)获得了“最[误导性缩进](https://github.com/ioccc-src/winner/blob/master/2020/tsoj/prog.c)”奖，因为它巧妙地将代码对齐到*右边*距。

但随着程序越来越疯狂，类别名称也越来越疯狂：

- 2001年的一份参赛作品获得了“最佳用户滥用”奖。（它的[代码库页面警告](http://www.ioccc.org/2001/rosten/index.html)说该程序“会干扰你的鼠标”，也可能“使程序难以退出”。）
- 2006年[一个参赛作品](http://www.ioccc.org/2006/sloane/index.html)获得了新设立的“荷马最爱”奖——因为打印出一个动画甜甜圈。
- 一个[2012年的参赛作品](http://www.ioccc.org/2012/dlowe/index.html)获得了“最佳丧命方式”的荣誉，因为它创建了一个基于康威“生命游戏”的街机风格视频游戏。
- 2015年程序员Christopher Mills获得了“飞鸟！”奖，因为[重现了手机游戏Flappy Bird](http://www.ioccc.org/2015/mills1/index.html)，并具有更改鸟类宇宙中物理属性的自定义选项。

## 展望未来

是什么让这一切持续下去？评委们从哪里找到热情，连续四个十年仔细研究一堆混淆的C代码？这一切疯狂的目的是什么？

在网上搜索足够长的时间，你就会在Landon Curt Noll的个人网站上找到线索。它包含一些[非常旧的照片](http://www.isthe.com/chongo/pictures.html)，这些照片是他担任SGI密码学家/数论学家时的照片——以及Noll担任加利福尼亚州桑尼维尔市议员时的官方照片。

但它也展现了他对算法艺术的独特欣赏。“我认为数学既是一门艺术，也是一门科学，”Noll写道。

“有些人，当他们在打电话时涂鸦时，会画‘兔子’。我喜欢涂鸦方程式和图表，通常是通过Mathematica工具。”

但是比赛的回归几乎就像久别重逢的亲戚——一种持续到未来的极客另类历史。

2025年的新一批获奖者将以一种独特的极客方式公布——由评委通过git push一个新的获奖者目录，并在新的[@IOCCC Fostodon](https://fosstodon.org/@ioccc) 提要上发布公告。

[YOUTUBE.COM/THENEWSTACK 科技发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)