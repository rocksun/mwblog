<!--
title: 力压群雄：Pebblebed AI工具洞察Linux二十载漏洞
cover: https://cdn.thenewstack.io/media/2026/01/a31f7bd3-getty-images-4wzh2sftphu-unsplash.jpg
summary: 安全研究员Jenny Guanni Qu开发了一款AI工具，通过分析Linux内核20年bug数据预测新漏洞。研究显示，多数bug修复加快，但安全漏洞仍难发现。该工具表现出色，但资深内核开发者Greg Kroah-Hartman指出，Linux社区已拥有成熟的bug检测和分析流程，包括AI工具，并认为现有公共数据已足够。Qu仍在继续验证其工具。
-->

安全研究员Jenny Guanni Qu开发了一款AI工具，通过分析Linux内核20年bug数据预测新漏洞。研究显示，多数bug修复加快，但安全漏洞仍难发现。该工具表现出色，但资深内核开发者Greg Kroah-Hartman指出，Linux社区已拥有成熟的bug检测和分析流程，包括AI工具，并认为现有公共数据已足够。Qu仍在继续验证其工具。

> 译自：[Pebblebed Ventures' AI tool analyzes 20 years of Linux bugs](https://thenewstack.io/hacker-jenny-qus-ai-tool-analyzes-20-years-of-linux-bugs/)
> 
> 作者：David Cassel

我们能否通过分析Linux内核过去20年的提交记录并利用AI，开发出更好的bug查找工具？

在[最近的一篇博客文章](https://pebblebed.com/blog/kernel-bugs)中，安全研究员 Jenny Guanni Qu 分析了Linux内核中125,183个bug修复——追溯到2005年4月，[Git](https://thenewstack.io/beyond-code-control-git-for-everything/)首次向世界发布的那一个月。

随后，Qu利用这项研究，原型化了一个AI辅助工具，用于预测哪些新的提交可能引入bug……

Qu告诉The New Stack，“我们计划在验证实验完成后，可能会在未来几周内发布训练好的模型和推理代码。”

The New Stack联系到Linux内核开发者 Greg Kroah-Hartman 征求意见，他提醒了Linux为搜索和消除bug、以及微调补丁流程[已在做的工作](https://thenewstack.io/how-ai-helps-maintain-the-linux-kernel/)。

这都证明开发者社区认真对待消除bug——并投入大量时间构建最佳工具，以便在提交之前识别它们。但有没有新的方法来处理这个问题呢？

随着一个认真（且不断壮大）的社区审查Linux内核代码，一位研究员决定启动自己的研发工作，看看他们能否提出更好的方案。

## Linux内核bug研究的主要发现

Qu花了六个小时在Git上挖掘了内核20年的提交历史。（Qu在MIT许可下[在GitHub](https://github.com/quguanni/kernel-vuln-data)和[HuggingFace](https://huggingface.co/datasets/quguanni/kernel-vuln-dataset)上发布了数据集）Qu的第一个发现是什么？今天的bug很难躲过Linux内核开发者。

“我们正在同时更快地捕获新bug，*并且*正在缓慢地解决大约5,400个隐藏了五年多的老旧bug。”

事实上，Qu的研究显示，到2022年，69%的bug在一年内被发现。（这比2010年的0%有所上升。）根据她的博客文章，Qu认为这表明“工具改进带来了真正的进步”。到2025年，bug的平均生命周期（在被发现、修复和关闭之前）仅为0.7年。只有13.5%的bug超过5年。

Qu认为，这部分是因为到2026年，我们现在有更多贡献者审查Linux内核代码。但她也将其归因于高质量测试工具的使用日益增多，其中包括：

*   Syzkaller模糊测试工具（2015年发布）
*   动态内存错误检测器，如KASAN、KMSAN和KCSAN消毒剂
*   更好的静态分析

此外，在分析的125,183个bug中，只有158个有CVE——仅占0.12%。

Qu补充了一个注意事项。Git实际上显示Linux内核有448,000个提交，提到了某种“修复”，但其中只有28%使用了Git上的*Fixes:*标签，Qu用这个标签来识别用于她分析的提交。所以，“我的数据集捕获了有充分文档记录的bug，也就是维护者追踪了根本原因的那些。”

但Qu看到了一个明确的信息。“我发现安全bug平均隐藏2.1年才被发现，”她告诉The New Stack。有些持续超过20年。这不是工具问题，而是模式识别问题……”

这些见解能否用于开发一种新型bug查找工具？

## AI bug检测工具背后的黑客

Qu的研究是在风投公司Pebblebed Ventures进行的（其[投资包括生成式AI图像初创公司](https://pebblebed.com/portfolio)[Krea](https://pebblebed.com/blog/krea)）。其主页承诺“我们支持进步的基础层面”。

Qu将其描述为“技术投资者支持技术创始人”，提供一个“相当非结构化”的驻地项目，旨在进行“可能成为公司基础”的研究。在我的案例中，是自主漏洞发现。”（Pebblebed的网页称“我们让研究人员自由探索那些过于奇特而无法纳入路线图的想法。”）

Qu是探索AI驱动bug发现工具的完美人选。Pebblebed的主页称Qu“在加州理工学院训练AI解决数学问题”，并且“是世界上最优秀的竞技黑客之一”。

Qu的团队SuperDiceCode在2025年DEF CON CTF中获得第三名——“我多年来一直在竞技性地参与CTF，”Qu告诉The New Stack——这种实际经验启发了她的调查。“同样的漏洞类型在内核中十年又十年地出现。Use-after-frees（释放后使用）、竞争条件、边界检查缺失。我想了解为什么这些bug持续存在，以及我们是否能更早地发现它们。”

Qu在加州理工学院的学习甚至包括数学AGI的强化学习，以及在加州大学戴维斯分校学习数学、物理和计算机科学（根据[一个模拟Linux命令行的主页](https://quguanni.com/)）。正如Qu所说……

“Pebblebed给我钱来构建首先发现零日漏洞的AI，我全身心投入。”

Qu的研究表明，最难发现的bug是竞争条件，它平均持续5.1年（竞争条件bug的中位数为2.6年）。“它们是非确定性的，只在特定时序条件下触发，可能每百万次执行才发生一次。即使像KCSAN这样的消毒剂也只能标记它们观察到的竞争。”

![来自 Jenny Guanni Qu 在 PebbleBed Ventures 博客文章的截图——Linux bug 20年统计](https://cdn.thenewstack.io/media/2026/01/0a435cd2-screenshot-from-jenny-guanni-qu-blog-post-at-pebblebed-ventures-stats-on-20-years-of-linux-bugs.png)

Qu认为其他bug更难发现，是因为它们不常被今天的模糊测试工具检测到。

她的自身经验在这里发挥了作用。“一位优秀黑客和一位优秀程序员的区别主要在于接触。黑客见过成千上万有漏洞的程序，所以我们培养出对可疑代码的直觉。这正是对大数据集的模式匹配，而机器学习擅长此道。”

因此Qu着手将这一洞察转化为一个工具。

## 开发AI辅助的bug预测工具

Qu的研究首先识别了长期存在的bug中的模式，包括引用计数错误、解引用后缺少NULL检查或大小计算中的整数溢出。随后，Qu创建了一个工具，它通过神经网络模式识别和一些“手工制作”的检查，查看修复前后的代码。

这些手工检查使用正则表达式和类似AST的分析来发现51种潜在有问题代码结构——从错误处理语句到内存分配语句——寻找关键模式，例如“不平衡”的数字或缺少空值检查的引用或指针（暗示内存泄漏）。Qu写道，神经网络随后学习哪些条件关系实际上暗示了一个bug，“无论是神经网络还是手工规则，单独使用都无法达到最佳效果。组合起来才能。”

Qu对其结果印象深刻。

*   “在所有安全提交中，我们错误标记了1.2%。”
*   “在我们标记为有风险的提交中，98.7%确实有风险。”
*   “在所有实际引入bug的提交中，我们捕获了92.2%。”

Qu的博客文章承认了其数据集可能存在的缺点。（例如，该系统只对带有*Fixes:*标签的28%的bug进行了训练——这意味着它们是文档齐全的bug，往往更严重。）该模型的局限性之一是它只对*已发现*的bug进行了训练——因此，并未针对遵循新颖独特模式的bug进行训练。

Qu的博客文章总结道，这使得她的工具VulnBERT“成为一个分类工具，而非保证。它能捕获92%具有可识别模式的bug。剩余的8%和新颖的bug类别仍需要人工审查和模糊测试。”Qu认为数据显示该工具已可投入生产。

## Linux内核开发者对AI bug工具的看法

在博客文章中，Qu表示她也希望看到一个通过强化学习训练的代理，在探索代码路径时能够*识别*bug。（如果像Syzkaller这样的模糊测试工具在标记的代码路径中发现崩溃，也许这可以作为积极信号纳入。）

“目标不是取代人工审阅者，而是将他们指向最可能存在问题的10%的提交，以便他们将注意力集中在关键之处。”

自她的博客文章发布以来，“一些内核开发者已经联系了我，”Qu告诉The New Stack，“这令人鼓舞。”她还报告“在安全研究界获得了积极的参与”。

但Linux内核开发者 Greg Kroah-Hartman 已经见过类似的研究。“多年来，也有其他研究人员深入挖掘我们的提交历史，发表了许多研究论文，”他在一封电子邮件采访中告诉The New Stack，“因为我们拥有大量的公共数据，这是‘传统’闭源操作系统根本不提供的。”

因此，虽然他将Qu的博客文章视为“一份很酷的报告”，但 Greg Kroah-Hartman 也觉得“我们进行这类报告已经十多年了。”（他引用了Linux安全工程师 Kees Cook 在Linux安全会议上[的年度演讲](https://www.youtube.com/watch?v=c_NxzSRG50g)，以及 Jon Corbet 在[lwn.net](https://lwn.net/%20)上[许多追踪相同事物的报告](https://lwn.net/Articles/914632/)。）

因此，尽管Qu的博客文章描述了原型化一个新的工具，但 Greg Kroah-Hartman 指出，他们已经一直在警惕地关注可能引入新bug的提交。“我们有工具在内核补丁提交*之前*运行，以试图发现这些类型的问题。

“在我们的代码树中已经存在的提交上运行这些工具也会很好，*但是*我们已经有大量人员在代码本身上做着同样的事情。这正是静态分析检查器一直以来的作用，对吗？”

这仅仅是个开始。“我们也已经将LLM工具应用于我们的提交十多年了，关于所使用的工具和流程有许多论文和演示。这不是什么新鲜事，这是我们如何将补丁正确地回溯到旧内核树的工作方式。”

尽管 Greg Kroah-Hartman 在他的电子邮件中重申，他们始终欢迎新的bug报告……

![Greg Kroah-Hartman (Linux内核维护者) 回应内核bug博客文章——2026年1月20日电子邮件截图](https://cdn.thenewstack.io/media/2026/01/5bcf7a53-greg-kroah-hartman-linux-kernel-maintainer-responds-to-kernel-bugs-blog-post-screenshot-from-email-january-20-2026.png)

他的结论是？“这份报告很酷，但我们已经有了更好的数据，在我们用于CVE报告的公共工具（及其生成的数据库）中。不需要用任何‘AI工具’来获取信息，普通的SQL就能很好地工作……”

但Qu的工具开发工作仍在继续。“我将在2026年4月的BugBash上发表演讲，希望在那里与更多的内核安全社区成员建立联系。

“真正的考验将是前瞻性验证：我们能否在新提交中的漏洞被发现之前就捕获它们？”