<!--
title: 发挥创意：ThePrimeagen与Lex Fridman的五小时访谈
cover: https://cdn.thenewstack.io/media/2025/05/bbf41c2c-michael-paulson-screenshot-from-lex-fridman-interview-remembering-breaking-production-clearer-1.png
summary: ThePrimeagen五小时访谈爆火！Rust、Neovim、SQL引热议。他曾是Netflix工程师，自曝“搞崩生产环境”糗事。直播编程源于Extra Life慈善，旨在打破技术精英主义，鼓励创新和包容。AI时代，保持编程乐趣至关重要！
-->

ThePrimeagen五小时访谈爆火！Rust、Neovim、SQL引热议。他曾是Netflix工程师，自曝“搞崩生产环境”糗事。直播编程源于Extra Life慈善，旨在打破技术精英主义，鼓励创新和包容。AI时代，保持编程乐趣至关重要！

> 译自：[Be Creative: ThePrimeagen's Five-Hour Interview With Lex Fridman](https://thenewstack.io/be-creative-theprimeagens-five-hour-interview-with-lex-fridman/)
> 
> 作者：David Cassel

这几乎是历史性的：与编程界的直播开发奇才“ThePrimeagen”进行了一次史诗般的[五小时访谈](https://www.youtube.com/watch?v=tNZnLkRBYA8)。

ThePrimeagen以其在[Twitch](https://www.twitch.tv/theprimeagen)和[YouTube](https://www.youtube.com/@ThePrimeTimeagen/)上的热门频道（以及他快速、活泼的个性）而闻名，ThePrimeagen（又名Michael Paulson）与广受欢迎的程序员转型播客主持人[Lex Fridman](https://lexfridman.com/)进行了一次自由的峰会。

这次热闹的访谈迅速吸引了140万次观看（以及3,021条评论）。ThePrimeagen是一个色彩鲜明的人物，他对从Rust到元编程以及“仅仅因为有小胡子而产生的这种奇怪的能量”等各种话题发表了看法。

![Screenshot from Lex Fridman interview of ThePrimeagen — discussing Stack Overflow's popular languages list](https://cdn.thenewstack.io/media/2025/04/6650644b-screenshot-from-lex-fridman-interview-of-theprimeagen-popular-programming-languages-from-stack-overflow.png)

*ThePrimeagen评论Stack Overflow上最流行的编程语言列表。“为什么Assembly比Ruby更受欢迎？”*

两人争论了SQL是否是一种编程语言以及Bash的优点。（“我喜欢它，直到我需要一个数组。”）他们讨论了为什么*assert*语句“超级有趣”，而ThePrimeagen补充说，“每个人都一直告诉我新的C++很棒。它拥有你想要的所有功能和你*不*想要的所有功能……”

![](https://cdn.thenewstack.io/media/2025/04/224cba15-screenshot-from-theprimeagen-youtube-channel.png)

但在此过程中，他们还深入探讨了他编程故事的个人层面，以及他为达到目标所经历的艰难道路，包括促使他从事编码生活的热情，以及是什么让他不断地为他庞大但隐形的观众宣传它。

不知何故，随着对话的进行，Fridman的观众看到了真实的Michael Paulson，揭示了他漫长的编程之旅中发现的所有至关重要的真相——关于学习的乐趣、个人的救赎以及保持编程世界尽可能具有包容性的重要性。

包容性甚至足以容纳像他这样热爱乐趣的格格不入的人……

## “地狱般的生活”

早些时候，Fridman开玩笑说，“对于那些不知道ThePrimeagen是谁的人来说，他几乎每隔一句话都会提到他非常成功，并且曾在Netflix工作过。”

“没错，”ThePrimeagen说。“几乎和我提到[Neovim](https://thenewstack.io/neovims-future-could-have-ai-and-brain-computer-interfaces/)一样多。”

但随后他的采访者更认真地说，Paulson“过着地狱般的生活。我认为这对很多人来说都是鼓舞人心的……”

Paulson的父亲在他七岁时去世。他逐渐养成了一些不健康的习惯（包括8岁时吸食大麻和15岁时饮酒），并且在高中即将结束时，他试图自杀。他在播客中说，从医院出来后，他完全不在乎了。有更多的毒品——LSD、蘑菇、甲基苯丙胺——然后是大学。“那整个时期都被糟糕的决定所标记。然后在某个时候，大约19岁的时候……我只是在一个晚上感受到了非常戏剧性和真实的上帝的存在……”

Paulson说，他当时觉得他必须做出选择，并决定，“我不喜欢我所过的生活。”在接下来的日子里，当他伤害别人或转向毒品时，他感到羞愧。“突然之间，我有了良心。”在蒙大拿州的天空下，他试图成为一名好学生。他在数学学习中心花了“无数个小时”。“然后在某个时候，经过多年的努力……有些东西点击了。

“突然之间，我成了数学最好的人……”

## 学习和探索

回顾过去，Paulson看到了学习变成探索的时刻。他将它比作音乐家突然意识到他们知道如何演奏乐器：“感觉太棒了。”做某事的愿望已经转变为更多的东西，Paulson生活的重要部分开始发生变化。

Paulson克服了他的瘾。他遇到了他未来的妻子。但他也发现，“我喜欢编程。我开始每天编程12个小时。”他使用PHP推出了他的第一家创业公司。“我非常有动力……有时我会连续编程24或36个小时……这就是我想做的……

“这就是我如何成为我的。”
他并非从未犯错。在[Netflix](https://thenewstack.io/from-netflix-to-walmart-open-source-kafka-in-action/)工作时，他发现 Netflix 使用 Groovy 编程语言，并且有自己定制的响应式编程库，其中包括“observables”，它们会在事件发生时广播事件。Paulson 曾经试图暂时暂停其中一个，给它 sleep 命令，结果发现了两件事：

- 当一个线程休眠时，没有线程可以唤醒它。
- 他的堆栈不是多线程的。

“我只是关闭了所有的 staging 环境，”他说。更糟糕的是？由于他的命令没有响应，“我运行了 10 次……

“下午剩下的时间里，没有开发人员可以工作——因为我锁定了所有的实例！”

ThePrimeagen 也有多个“[搞崩生产环境](https://thenewstack.io/qa-erica-brescia-bitnami/)”的故事——但最重要的问题始终是你学到了什么。他回去阅读了 Groovy 的官方语言参考，很快他就成了“那个了解这些事情的人”。

因此，虽然 Netflix 以对新员工要求严格而闻名——“他们的文化宣言是‘快速招聘，快速解雇！’”——但 Paulson 很快就开始找到了自己的定位：“成为那个愿意做别人不愿意做的事情的人。”

## 起源故事

他的流媒体职业生涯也是在 Netflix 开始的，这要归功于 [Extra Life](https://www.extra-life.org/index.cfm?fuseaction=cms.page&id=1306)，这是一个为医学研究筹集资金的在线慈善机构。“你进行直播，”Paulson 解释说，“你筹集到的任何资金都将用于儿童癌症研究。”

就这么简单——然后一件事接着一件事。在设置好他的 Fortnite 直播系统后，“我最终真的很喜欢它……！我一直在做，然后有一天我决定做一些编程。因为我真的很喜欢 Vim，而且我认为我使用 [Vim](https://thenewstack.io/a-look-at-vim-a-text-editor-for-the-ages/) 的速度很快。也许人们认为编程很酷。”

Paulson 是最早直播编码的人之一，但他带着一种深刻的使命感来到这里。

![Turok-son-of-stone-comic 封面（通过 Wikipedia）](https://cdn.thenewstack.io/media/2025/04/8b62b774-cover-of-turok-son-of-stone-comic-via-wikipedia-198x300.jpg)

Paulson 从他童年最喜欢的 Nintendo 游戏 [Turok: Dinosaur Hunter](https://en.wikipedia.org/wiki/Turok:_Dinosaur_Hunter)（基于 [1950 年代的漫画系列](https://en.wikipedia.org/wiki/Turok)）的最后一关借用了他的名字 *ThePrimeagen*。

多年后，他发现自己想要反抗科技行业变成“这个超级自命不凡的地方…… 就像，‘我们正在构建最复杂的东西，这是为*聪明*人准备的，其他人都是*笨*人。别担心，我们会为你设计的，笨蛋……！我们会告诉你如何构建完美的架构。’”

“我记得我更改了我的 Twitter 账号，因为我太生气了——然后就改回了我的游戏名称。”他拾起了这个称号，成为了 ThePrimeagen，“因为我想：我希望事情变得*有趣*。”

Paulson 告诉 Fridman，“我的目标是摧毁任何那种技术心态，因为它不包括任何人。每个人都认为自己是聪明人，他们为笨蛋设计…… 我希望技术成为一个人们可以感到有创造力、兴奋并真正构建东西的地方。如果你是新手，问一些愚蠢的问题也没关系……”

在某个地方，他的人生经历给了他深刻的同情心。“没有人期望你聪明。选择你想要的任何东西——比如，真正*做*一些事情，玩得开心，并构建你疯狂的想法。

“哦，你要重新发明轮子？重新发明轮子，了解你在做什么，学得非常好，并互动和交流！”

一年前，他终于决定离开他在 Netflix 的长期职位，成为一名全职主播，“我想我没有回头。”在那一年里，他的 YouTube 频道增加了 13 万多名订阅者——增长了 38%——另外还有 26 万粉丝在 Twitch 上观看他。但最重要的是，ThePrimeagen 说，“这真的很有趣！”并且“人们真的很喜欢观看和参与……”

他现在有 473,000 名 [YouTube 频道](https://www.youtube.com/c/theprimeagen)订阅者——但这都是他独自完成的。“这不像在 Netflix 那样，我可以听到人们正在构建的东西……” Paulson 说，作为团队的一员工作是“我真的很怀念的事情…… 那种被迫的、一起解决难题的感觉。”

## 展望未来

总而言之，他似乎在告诉年轻的程序员们要记住快乐。即使在人工智能变得越来越强大的世界里，“我仍然希望我的孩子们学习如何编程…… 如果这是一个足够好的答案。”

在面试中，他看起来玩得很开心。他把 SQL 念成 “Squeal”。而且不可避免地，微软的 Windows Subsystem for Linux，WSL，变成了 “Weasel”。在结束之前，他们回顾了他一直以来最喜欢的项目：将一个 ASCII 艺术版的 Doom 移植到网页上，然后[让人们使用在 Twitch 上输入的命令来控制它](https://www.youtube.com/watch?v=3f9tbqSIm-E)。

ThePrimeagen 分享了他从多动症 (ADHD) 经历中学到的东西，比如能够专注于编程的快乐和支持型家庭的好处。（“也许我找到了一个秘籍：一个爱我的妻子。”）他解释了为什么沉迷于坏消息会让你焦虑，以及对抗干扰的重要性。但最重要的是，他坦诚地分享了*不*该做什么，以及一些从经验中获得的宝贵智慧。

他对年轻的程序员有什么建议吗？ThePrimeagen 回顾了自己的经历，看到了一个坏榜样。在编程方面，“我变得着迷和沉迷。”

这导致他“花了太多的时间编程——忘记花时间陪伴我的妻子、我的朋友，所有这些……”这让 ThePrimagen 承认了一个残酷的现实：“我认为——虽然它成就了现在的我——但这可能是一种不健康的行为，可能不是一个明智的行为。”

那么他会对年轻的程序员说什么呢？首先，“你必须培养对它的热爱、技能和渴望……无论那种味道是什么，它都会让你每天都回来。如果你愿意，可以把它看作是编程的‘在健身房里进行重复训练’。”

但他的建议还有第二部分。“也要知道如何重视有价值的东西——不要‘迷失在酱汁中’，你只是太执着于创造下一个最伟大的创业公司，以至于牺牲了你的健康，牺牲了你的人际关系。

“或者更糟糕的是，你牺牲了自己的道德，为了能够实现这些目标，采取了一些本不应该采取的捷径。”

当他们长达五个小时的讨论接近尾声时，Fridman 用巴西小说家 Paulo Coelho 的一句完美引言结束了节目。

“当我们努力变得比现在的自己更好时——我们周围的一切也会变得更好。”