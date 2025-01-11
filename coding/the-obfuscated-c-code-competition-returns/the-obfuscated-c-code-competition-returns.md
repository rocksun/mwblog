
<!--
title: “混淆C代码”大赛回归
cover: https://cdn.thenewstack.io/media/2024/11/c7e3eb34-c-safety.jpg
-->

国际C代码混淆大赛回归，旨在让C++代码比以往更难阅读。

> 译自 [The 'Obfuscated C Code' Competition Returns](https://thenewstack.io/the-obfuscated-c-code-competition-returns/)，作者 David Cassel。

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

*IOCCC联合创始人Landon Curt Noll的GitHub个人资料截图*

## 巧克力与隐写术的邂逅

这种趣味性似乎无处不在——最终也变得具有感染力。“多年来，不止一位IOCCC评委曾以一些优质巧克力贿赂另一位IOCCC评委，以使其投票支持获奖作品，”[官方指南](http://www.ioccc.org/next/guidelines.html)指出。因此，一个[2012年的参赛作品](http://www.ioccc.org/2012/vik/index.html)展示了它的隐写术应用——将源代码隐藏在图像中——使用了美味巧克力的照片。

![](https://cdn.thenewstack.io/media/2025/01/65194eef-chocolate.png)

官方规则的[第26条规则](http://www.ioccc.org/next/rules.html#rule26)完全由包含所有26个字母且每个字母恰好出现一次的无意义句子组成。与此同时，大赛的官方FAQ对诸如[为什么他们会在Mastodon上](http://www.ioccc.org/faq.html#try_mastodon)之类的问题给出了俏皮的答案。“IOCCC不再使用Twitter，或者任何一个似乎缺乏冲动控制力的人（据称）现在称之为他们平台的东西。IOCCC更喜欢驻留在[联邦宇宙](https://fediverse.info/)。”

以及[比赛是如何开始的？](http://www.ioccc.org/faq.html#ioccc_start)“那是一个黑暗而暴风雨的夜晚……”

## 争夺最差的头衔

比赛始于1984年3月23日，当时23岁的Landon Curt Noll与Larry Bassel在国家半导体公司合作，将[UNIX](https://thenewstack.io/unix-creator-ken-thompson-to-keynote-scale-conference/)移植到该公司的微控制器上。Bassel正在与Bourne shell中的一个bug作斗争，而Noll正在处理早期BSD版本的finger命令。很快，他们[宣布了一场比赛](https://groups.google.com/g/net.lang.c/c/lx-TAuEyeRI/m/HdOOnNx6LC0J?hl=en)，“与周围最差的C语言黑客竞争”，参赛作品开始大量涌入。

Noll在FAQ中写道：“当我们开始收到来自美国以外的邮件时，我和Larry决定在名称中加入‘国际’二字。”

![](https://cdn.thenewstack.io/media/2025/01/ba8a9064-screenshot-of-home-page-for-obfuscated-c-competition-contributor-oscar-toledo-g.png)

即使在第一年，他们也看到了一些编码界大腕的参赛作品，包括贝尔实验室的程序员[David Korn](https://en.wikipedia.org/wiki/David_Korn_(computer_scientist))，Korn shell（1987年）的创建者，以及[Perl编程语言](https://thenewstack.io/week-programming-renaming-perl-save-terminal-unpopularity/)的创建者[Larry Wall](https://en.wikipedia.org/wiki/Larry_Wall)（1986年，1987年）。这设定了一个高标准，并在比赛的持续过程中延续了下来。

在过去的40年里，评委们已经评选出了197位不同的获奖者。其中一些人拥有自己的维基百科词条：

- Google DeepMind的研究员[Nicholas Carlini](https://en.wikipedia.org/wiki/Nicholas_Carlini)赢得了2020年的“[最佳展示：滥用libc]”奖](https://www.ioccc.org/2020/carlini/index.html)。
- 1989年，“最佳展示奖”授予了Ora Lassila，他因早期在语义网和RDF规范方面的工作而闻名。如今，Lassila是W3C咨询委员会的长期成员，也是AWS的首席图技术专家。1989年，他因编写了一个压缩的Lisp解释器而获奖。
- 其他获奖者包括C社区的杰出人物，如Walter Bright，他是D编程语言和Zortech C++编译器的创造者，以及Fabrice Bellard，他是Tiny C编译器的创造者。

还有几位知名的计算机科学学者，包括David Applegate、Lennart Augustsson、Daniel J. Bernstein、Vern Paxson、Diomidis Spinellis和John Tromp。

指南甚至包含了一条专门针对密歇根大学名誉教授Peter Honeyman的特殊规则：

> “过去，有些人曾试图通过加入像Peter Honeyman这样的著名互联网人物的评论来掩盖自己的身份。评委们已经识破了这一伎俩，因此认为任何声称来自Honeyman的混淆过的源文件或数据文件都不是来自Honeyman。”

信息似乎表明，令人惊叹的晦涩难懂的C代码也应该是匿名的晦涩难懂的C代码——至少在评判结束之前是这样。而这导致了1990年一个获奖作品出现了一个有趣且显著的巧合。评委们的评语抓住了ANSI C标准现在包含了三个字符的“三字符组”这一事实，这“使得编写难以阅读的程序变得更加容易”。因此，他们为程序员Larry Jones设立了一个特别奖项，表彰他编写了46行起伏不定的C代码，其中充斥着数十个这种三个字符的讨厌物（大多是问号）。

![](https://cdn.thenewstack.io/media/2025/01/e861b173-some-code-from-larry-jones-winning-entry-in-obfuscated-c-code-competition-1990.png)

在获得“ANSI委员会最糟糕的C语言滥用”奖项后，Jones 联系了评委，提出了一个简单的问题：“你们知道我是委员会成员吗？”

评委们向他保证这只是一种巧合，Jones 还表示他“非常感激”这个奖项。尽管他“原本真的希望得到一个更接近‘最像线路噪声’的奖项”。

但在所有的滑稽可笑之中，C语言混淆大赛仍然设法几乎成为每一代程序员的意外年鉴，将他们聚集在一起，展示我们自己的集体历史。还有玛丽·安·霍顿（Mary Ann Horton）也做出了贡献，她是一位BSD贡献者，被描述为“Usenet和互联网先锋”以及跨性别权利的早期活动家。霍顿在2022年的一部传记中说：“发明电子邮件附件是一回事，而一边从男性转变为女性，一边为工作场所的跨性别权利铺平道路，又是另一回事。”

在其中还有乔治·西切曼，他因在1978年创造了一种骰子的替代编号方案而闻名，这种方案仍然能产生与普通骰子相同的概率分布。

![](https://cdn.thenewstack.io/media/2025/01/3db2db25-screenshot-of-sicherman_dice-of-creative-commons-image-on-wikipedia-user-belbury-editing-original-dice-by-steaphan-greene.png)

## 穿越时光

这都是该活动漫长而传奇历史的一部分。“我们建议您避免尝试‘最小的自我复制’源代码，”指南警告说——因为已经有人凭借一个0字节大小的条目赢得了比赛。

但其他里程碑同样古怪且不可预测：

- 程序员 Thomas Covell 将竞赛首位获奖者的代码纹在了手臂上。
- 还有一次，在1993年的一场知识竞赛中，比尔·盖茨（Bill Gates）询问参赛者为“创造‘最晦涩难懂、富有创意、怪异但能运行的C程序’的事件”命名。其中一位参赛者回答说“Windows”。那一年的竞赛增设了纪念比尔·盖茨奖。
- 甚至连新网站的标志都链接到了一个2011年的国际C语言混乱代码大赛（IOCCC）参赛作品，那是一个光线追踪程序，其默认输出结果是……该网站的标志。（它获得了2011年的“最闪亮”奖项。）

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
