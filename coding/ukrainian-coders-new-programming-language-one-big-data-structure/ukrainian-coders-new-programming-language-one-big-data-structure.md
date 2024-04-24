
<!--
title: 乌克兰程序员的新编程语言：一个大型数据结构
cover: https://cdn.thenewstack.io/media/2024/04/8f4d7751-head-1597572_1280.jpg
-->

受 Forth、APL、Uiua 和 PostScript 等语言的启发，无名编程语言是对默示编程的一次实验。

> 译自 [Ukrainian Coder's New Programming Language: One Big Data Structure](https://thenewstack.io/ukrainian-coders-new-programming-language-one-big-data-structure/)，作者 David Cassel。

今年推出了一种由一个巨型数据结构组成的新编程语言——这样程序员就可以避免给事物命名。

软件工程师 [Oleksandr Kaleniuk](https://www.linkedin.com/in/okaleniuk/recent-activity/all/) 在电子邮件采访中表示：“这是一种对无处不在的命名问题的调侃反应。”“命名很难，所以我们干脆不命名任何东西，看看这样编程是否会变得更容易。”

剧透：他随后补充道，“并没有。”

“这种语言没有实际应用，但作为开发人员和用户，用它玩一玩很有趣。”

甚至这种语言本身都没有名字。

![无名编程语言 - 代码片段](https://cdn.thenewstack.io/media/2024/04/e0a6f63e-the-namingless-programming-language-code-snippet.png)

*无名编程语言文档中的代码片段。*

## 语言

[该语言的存储库](https://github.com/akalenuk/the_namingless_programming_language) 在 [GitHub](https://thenewstack.io/github-developer-productivity-at-30-billion-messages-per-day/) 上解释道：“只有一个数据结构。”“因为它只有一个，*所以不需要名称*。”然而，该数据结构中的分支和子分支可以表示较小的数组，甚至矩阵。成对的字符表示从字符串和数字到逻辑比较和数学运算的一切。（甚至还有用于从文件读取或写入数据，甚至删除该文件的符号。）

“还有一个操作。不是‘一个操作(an operation)’，而是‘操作(the operation)’，因为该语言中只有一个操作。

“因为它只有一个，*它也不需要名称*。”

解释器在其唯一的数据结构中运行，每当遇到*_* 符号时，它就会将值添加到堆栈中，或者对它们进行操作（如果 _ 符号出现在数学运算之前）。

> “由于只存在一种这样的语言，因此它不需要名称。”

而“帮助”的字符对是 *e_*（因此，运行名为 *the_namingless_programming_language* 的文件会在解析器命中 *e_* 字符后立即启动帮助菜单……）

生成的源代码块甚至用作文件名，“以避免为编写的程序命名的问题”。

最后，GitHub 上的官方存储库还强调，该语言本身也没有名称。因此，将其称为“无名编程语言”的行为实际上只是对这种尚未命名的语言试图实现的目标进行的*定义*。

“由于只存在一种这样的语言，因此它不需要名称。”

## 灵感

然而，这里有一些真正的编程概念在起作用。Kaleniuk 说，无名只是“面向堆栈和隐式的花哨名称”。

这意味着它受到 Forth、APL 和 [Uiua](https://www.uiua.org/)（Kalenuik 说它还包含数组编程和堆栈方向）等语言的启发。然而，在我们的电子邮件采访中，他说他的主要灵感是另一种面向堆栈的语言：[PostScript](https://en.wikipedia.org/wiki/PostScript)。

据 Kaleniuk 称，PostScript 是电子出版行业著名的“页面描述”语言，它不仅发送数据（关于应该绘制哪些线条和曲线），还发送代码——“一个可运行的程序，供实际执行打印的机器解释”。Kaleniuk 在一家全球 3D 打印公司的软件工程师工作时也遇到了同样的需求。

如果可以将要打印的形状编码为*公式*，而不是仅仅大量转储数据，那不是很有用吗？

Kaleniuk 选择了一种数组处理语言来保持一切简洁。“我们讨论的是千兆字节的代码/数据。”而且由于它是“99% 机器生成和 100% 机器消耗”，它也可以高度抽象（因为 Kaleniuk 认为，“反正没人愿意读它。”）这促使 Kaleniuk 使用高度抽象的[隐式编程](%E2%80%9Dhttps://en.wikipedia.org/wiki/Tacit_programming%E2%80%9D)来确定面向堆栈的语言。

Kaleniuk 称之为“仅仅是[设计实验](https://thenewstack.io/the-power-of-prototyping-in-user-experience-design/)，一个可以玩的东西，一个玩具……

## 在基辅编码

Kaleniuk 还编写了一个名为“单词和按钮在线”的网站，其中包含编程和数学教程（以及演示和测验）。（就在上个月，他添加了一篇帖子，介绍了所有应该在其长期编程语言 C++ 上具有竞争优势的技术。）去年，Kaleniuk 也撰写了《程序员几何学》。 (“掌握 CAD、游戏引擎、GIS 等背后的数学！”) 在 Manning Publications（其官方页面上提供整本书的免费在线访问）上说。

但自 2015 年以来，他一直担任 [3D 打印公司 Materialise](https://www.materialise.com/en/about/locations/ukraine) 基辅分公司的软件工程师，两年前转为项目经理。“我希望战争结束后，我们恢复正常生活，就能把这件事抛在脑后，”Kaleniuk 在我们的电子邮件采访中说道。


“说实话，我曾希望战争到目前为止已经结束了……”

Kaleniuk 2014 年在乌克兰东部工作，因此已经在俄罗斯占领下度过了几个月，并得出结论：“俄罗斯并不强大，只是野蛮。”他还记得俄罗斯全面入侵的第一天。“2022 年 2 月 24 日，我被一枚来袭导弹的声音惊醒，走到电脑前，打开银行应用程序，向军队捐款。我在 2014 年也做过同样的事情。这就像一条规则。每次听到爆炸声，你都会捐款。这会让你产生一种掌控感……

“你还会检查金融系统是否仍在运行。”

如今，他[表示他认识的大多数软件工程师](https://thenewstack.io/85-of-engineers-say-theyll-use-an-idp-in-2024/)，他们不在军队中，会缴纳税款，“并将剩余部分在军队和家人之间分配。尽管有些人直接为前线工作……我们希望战争结束，我们愿意为此付出代价……”

笼罩在这一切之上的是一种非常明确的感觉，那就是这是一场战争。“有些人已经用生命付出了代价。我的朋友在书出版前几天在行动中牺牲了。他也是一名软件工程师。”Kaleniuk试图将自己的捐款分配给他说“购买炮弹和火箭弹”的部委，以及非政府组织和个人志愿者（他们“帮助快速满足紧急请求，但他们不提供武器和弹药”）。

他从书的出版商那里收到的第一笔付款是在 2022 年 3 月初——就在俄罗斯入侵几周后——“我立即也捐赠了这笔钱。”战争仍在继续……12 月，Kaleniuk [在他的网站上写道](https://wordsandbuttons.online/why.html)，“大约一小时前，一枚俄罗斯导弹击中了我们附近的东西。又一次。”

“作为一个平民、工程师和数学家，我对此无能为力。但我可以赚一些钱，捐给那些有能力的人。从 2 月份开始，我就一直在做这件事，并且我计划一直做到胜利。”

## 反响

今年早些时候，Kaleniuk 发现他的编程语言在 [Hacker News](%E2%80%9Dhttps://news.ycombinator.com/item?id=39362200%E2%80%9D) 上被讨论。Kaleniuk 很高兴它收到了“大部分积极的评价”。

“这让我回想起超低级编程，例如操作数据栈等，” [澳大利亚网络开发者](https://benwinding.com/about/) [Ben Winding](https://news.ycombinator.com/item?id=39364589) [写道](https://news.ycombinator.com/item?id=39364589)，并补充说“它可能被证明是一个有用的学习工具”。

关于命名如何提高可读性，不可避免地进行了讨论，但几位评论者对Kaleniuk的努力表示赞赏，其中一位表示看到了[实验的真正价值](https://news.ycombinator.com/item?id=39426993)。“根据我自己的经验，从事像这样的‘愚蠢’项目，例如，具有严格的人为限制，可能非常有趣且具有挑战性，并且可以得出可以应用于以后的实际项目的经验教训。”

Kaleniuk说他已经转向其他项目——但感觉这段经历让他变得更加丰富。“我确实牢记我学到的教训，所以也许有一天你会看到一些令人惊叹的 3D 打印物品，并思考‘他们是如何设法打印出如此复杂的东西的？’然后你会想起那种没有实际应用的小众语言……”

## 尾声

在 README 文件的结尾，Kaleniuk承认这种语言的创建是为了“把它从我的系统中清除出去，这是一个巨大的成功。我的意思是，我确实成功地把它从我的系统中清除了，而且我不知何故不再想玩它了。”

“它漂亮吗？不，”Kaleniuk在 LinkedIn 上发帖说。“它实用吗？当然不。它有趣吗？比你想象的要有趣。”

在我们的电子邮件采访中，Kaleniuk还告诉我们这一切的最终结果。“我玩得很开心，现在我分享了代码，以便其他人也可以玩。”