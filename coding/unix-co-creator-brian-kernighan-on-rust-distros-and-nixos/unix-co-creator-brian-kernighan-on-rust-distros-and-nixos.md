
<!--
title: Unix共同创造者Brian Kernighan谈Rust、发行版和NixOS
cover: https://cdn.thenewstack.io/media/2025/08/088e8bf4-83-year-old-brian-kernighan-laughs-at-vintage-computer-festival-east-2025-1.png
summary: Brian Kernighan在InfoAge科技与历史博物馆的演讲中分享了他对Rust、Linux发行版、以及当今软件的看法。他对Rust的性能和复杂性表示不满，认为许多软件质量很差，并建议程序员们做自己觉得有趣的事情。
-->

Brian Kernighan在InfoAge科技与历史博物馆的演讲中分享了他对Rust、Linux发行版、以及当今软件的看法。他对Rust的性能和复杂性表示不满，认为许多软件质量很差，并建议程序员们做自己觉得有趣的事情。

> 译自：[Unix Co-Creator Brian Kernighan on Rust, Distros and NixOS](https://thenewstack.io/unix-co-creator-brian-kernighan-on-rust-distros-and-nixos/)
> 
> 作者：David Cassel

“我还在普林斯顿教书，”83 岁的 [Brian Kernighan](https://www.cs.princeton.edu/~bwk/) 最近在新泽西州沃尔镇的 [InfoAge 科技与历史博物馆](https://www.infoage.org/) 向观众说道。“我还没有退休！”

作为贝尔实验室 Unix 贡献的极客传奇人物，以及 1978 年 [C 编程语言](/thenewstack.io/introduction-to-c-programming-language/) [权威指南](https://www.pearson.com/en-us/subject-catalog/p/c-programming-language/P200000000368/9780137460847) 的合著者，Kernighan 受邀在“[Vintage Computer East” 节](https://vcfed.org/vcf-east-2025/) 上发言。上个月，视频被上传到 YouTube，显示他的演讲以一个独特的问答环节结束，几乎成为历史……

除了对操作系统创新辉煌岁月充满乐趣和怀旧的回顾之外，Kernighan 还分享了他对*当今*世界的看法——C 语言逐渐被内存更安全的编程语言取代，Linux 有数百个发行版——Unix 的后代几乎为每部手机提供动力。

“我会尽可能地让它更随意，”Kernighan 向观众承诺，回答了他们近半个小时的问题。

除了内容丰富且富有洞察力之外，很明显 Kernighan 和他的听众都玩得很开心……

## Rust 取代 C？

这是一个具有划时代意义的时刻。“你认为 Rust 取代 C 有任何价值吗？”一位观众问道，[这是 TNS 上经常讨论的话题](https://thenewstack.io/code-wars-rust-vs-c-in-the-battle-for-billion-device-safety/)。

“或者这只是一个巨大的炒作泡沫，等着破灭？”

在一个多年来一直在认真过渡到更安全的内存语言的世界中，一位长期以来对 C 语言（超过半个世纪）的拥护者的回答注定将是非凡的。

“哦，Rust，”Kernigham 说，引起观众的笑声。

“我只写过一个 Rust 程序，所以你应该对此持保留态度，”他说。“我发现它很——*痛苦……*我只是无法理解在内存甚至不是问题的程序中，实现内存安全所需的机制！”

然而，他对 Rust 最大的抱怨似乎是其性能——对于一个早期职业生涯始于 16 位 PDP 11/20 的人来说，这是一个特别具有破坏性的抱怨。

[![Digital_PDP11-20 front panel - IMG_1498_cropped - Creative Commons via Wikipedia - author Rama and Musee Bolo](https://cdn.thenewstack.io/media/2025/08/366730fb-digital_pdp11-20-front-panel-img_1498_cropped-creative-commons-via-wikipedia-author-rama-and-musee-bolo-1024x480.jpg)](https://cdn.thenewstack.io/media/2025/08/366730fb-digital_pdp11-20-front-panel-img_1498_cropped-creative-commons-via-wikipedia-author-rama-and-musee-bolo-1024x480.jpg)

在谈到 Rust 时，Kernighan 说：“与其配套的支持机制——这种 crates 和 barrels 之类的概念——简直大得令人难以理解，而且速度很慢。”

“而且编译器很慢，生成的代码也很慢……”

总而言之，Kernighan 有过一次糟糕的经历。“当我试图弄清楚发生了什么时，自上次有人发布描述以来，该语言已经发生了变化！所以花了几天时间编写一个用其他语言可能需要五分钟的程序……”

这是他唯一一次使用该语言的经历，因此 Kernighan 承认，当谈到 Rust 时，“我可能过于愤世嫉俗了。

“但我——我不认为它会立即取代 C。”

[![83-year-old Brian Kernighan laughs at Vintage Computer Festival East (2025) — hands up](https://cdn.thenewstack.io/media/2025/08/1351be12-83-year-old-brian-kernighan-laughs-at-vintage-computer-festival-east-2025-hands-up.png)](https://cdn.thenewstack.io/media/2025/08/1351be12-83-year-old-brian-kernighan-laughs-at-vintage-computer-festival-east-2025-hands-up.png)

## 什么是发行版？

Kernighan 还被问到一个真正让他为难的问题。“你最喜欢的发行版是什么？”

在观众的笑声中，Kernighan 心知肚明地笑了笑，然后假装不了解这个新世界，这个世界拥有[不止一个](https://thenewstack.io/choosing-a-linux-distribution/)类 Unix 操作系统的发行版。（“*那*是什么词？！”）

但随后他诚实地说，虽然他使用 Mac，但只是为了打开一堆终端窗口“连接到计算机科学系在任何给定时刻运行的任何 Linux 系统。我什至不知道它是什么。所以，呃——抱歉！我帮不上什么忙。”

但另一个问题似乎深深地扎根于被遗忘的编程语言的传说中。“鉴于您在 C 语言方面的开创性作用，您是否熟悉派生的 [Holy C](https://holyc-lang.com/)？”

这是由[已故的 Terry A. Davis](https://thenewstack.io/the-troubled-legacy-of-terry-davis-gods-lonely-programmer/) 为他自己开发的以圣经为主题的操作系统 TempleOS 编写的 C 语言的一种奇特变体。HolyC（将源代码与 x86_64 汇编代码混合）仍然可以编译成 x86_64 汇编代码。

![TempleOS 截图](https://cdn.thenewstack.io/media/2018/09/a7a4ac27-templeos_4.05_session-released-into-public-domain-by-terry-davis.png)

在观众的笑声中，Kernighan 微笑着说“简短的回答是否定的。”但“稍微扩展的答案是：这是否出现在像 [*99 Bottles of Beer on the Wall*](https://www.99-bottles-of-beer.net/) 这样的网站上？”（这个长期运行的网站展示了这首歌的歌词如何在 1500 种不同的编程语言中打印出来——但遗憾的是，HolyC 并不在其中。）

当另一位提问者询问 Kernighan 对 [包管理器 Nix](https://thenewstack.io/nixos-a-combination-linux-os-and-package-manager/) 和 [NixOS](https://nixos.org/) 发行版的看法时，一种模式变得清晰起来。Kernighan 笑着说：“天啊，这是*另一个*我从未听说过的。”

他后来澄清说，“我想我听说过，但我对它一无所知，所以我无法给你一个答案。”）

## 昨日与今日

在他的演讲中，Kernighan 深情地回忆了贝尔实验室的整体环境，称其具有合作性、合议性和趣味性……“和这些人一起出去玩非常有趣。”

[![Multics slide - 83-year-old Brian Kernighan laughs at Vintage Computer Festival East (2025) - hands up](https://cdn.thenewstack.io/media/2025/08/48e69d34-multics-slide-83-year-old-brian-kernighan-laughs-at-vintage-computer-festival-east-2025-hands-up.png)](https://cdn.thenewstack.io/media/2025/08/48e69d34-multics-slide-83-year-old-brian-kernighan-laughs-at-vintage-computer-festival-east-2025-hands-up.png)

但他也记得，在 [Microsoft Windows](https://thenewstack.io/bill-gates-paul-allen-and-the-code-that-started-microsoft/) 出现后，整个技术世界发生了变化，“许多努力、重点和有才华的人开始在 PC 世界工作……”Kernighan 回忆说，“好的想法和有才华的人在某种程度上——甚至很大程度上——从 Unix 那里流失了。”并且“更加关注互动”，因为微软正在制造消费产品（并非针对“技术人群”）。

尽管他还提醒观众，当时世界看到了 Linux 的发展，这“使 Unix 的遗产得以延续”。

那么，他对当今 Unix 的消费化有何看法？这是另一个被问到的问题，Mac/iPhone/iPhone 用户在不知情的情况下使用其后代——并且“偏离了最初的自由、开源理念”。

“我认为你说到了点子上，”Kernighan 回答说，“当你说大多数人不知道它时……”

他指出，iPhone 正在运行“相当长路径演变的 Unix 版本”，而 Android 手机“正在运行另一种 Linux 的底层版本……我认为从我这方面来看，作为一个——你知道，一个松散地参与早期的人——并且拥有一部手机——我发现这很有趣。

“我也觉得有点恼火，因为底层有一个我可以用来做事的系统——但我无法访问它！”

他的观众再次欢笑和鼓掌……

一位提问者甚至指出，Kernighan“实际上参与了软件作为一种商业事物的一生。”但这也意味着他亲眼目睹了它变得商业化和“产品化”。

那么“你对当今软件的现状有什么看法……？”

Kernighan 狡猾地笑了笑——他的观众再次笑了——提问者补充说，“如果可以的话，10 个字或更少！”

“很多都很糟糕……！”他说，引起观众的掌声。“不幸的是，这太真实了。”

然后他补充说，对他的提问者说，“我可以详细说明。但也许可以私下……”

## Kernighan vs. 氛围编程

在他的演讲中，Kernighan 曾说过 Unix 的一个遗产是“编写程序的程序”。

“编译器创建汇编语言……？这是一个编写程序的程序……一旦你做对了，编写程序的程序就会做得很好。它们通常比人做得更好。”

但是，在听到他的话后，他很快补充了一个警告。“我将跳过大型语言模型正在发生的事情……”在观众的笑声中，他继续说道，“因为我在这方面的一些尝试已经使我刚才所说的话失效了！”

[![83-year-old Brian Kernighan shows Jurrasic Park's Unix line at Vintage Computer Festival East (2025) ](https://cdn.thenewstack.io/media/2025/08/837dab46-83-year-old-brian-kernighan-shows-jurrasic-parks-unix-line-at-vintage-computer-festival-east-2025-hands-up.png)](https://cdn.thenewstack.io/media/2025/08/837dab46-83-year-old-brian-kernighan-shows-jurrasic-parks-unix-line-at-vintage-computer-festival-east-2025-hands-up.png)

当演讲接近尾声时，有人问他对未来几代程序员的建议。这是一个他以前回答过的问题，他的第一个反应是承认“这个答案——真正的答案——是‘我不知道’。”

但当然，他还有更多的话要说。这位 Unix 先驱的深思熟虑的回答中包含了一些肯定。“我认为可能以有用的形式存在的计算机，你可以用它们来做事情，将在很长很长的时间内与我们同在。”

“可能大多数人不会真正意识到他们在多大程度上受到硬件上运行的软件（使用通信系统）的控制。但是*你*，如果你做这些事情，*会*知道这一点。我认为这将为你提供一些可以做的事情，这些事情会很有趣——并且可能在未来一段时间内实际上是可以*雇用*的。”

他还有一件事要说。尽管这已经成为一种陈词滥调，但 Kernighan 告诉他的听众，“如果这些东西让你兴奋，那就去做吧。好吗……？我认为你可以做这类事情，你可以玩得很开心，你可能会谋生并享受你正在做的事情……

“我认为做你觉得有趣的事情才是正确的道路。”