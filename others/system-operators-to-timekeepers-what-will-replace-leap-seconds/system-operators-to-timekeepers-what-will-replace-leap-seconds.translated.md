# 系统运营商致计时员：闰秒的替代方案是什么？

![Featued image for: System Operators to Timekeepers: What Will Replace Leap Seconds?](https://cdn.thenewstack.io/media/205/02/81a06816-george_washington_french_empire_mantel_clock-creative-common-image-via-wikipedia-by-george_washington_french_empire_mantel_clock-creative-commons-image-by-maulleigh-via-wikipedia-1024x772.jpg)

本月早些时候，许多科技工作者从《旧金山纪事报》上看到了令人不安的消息，即[气候变化正在从字面上影响时间本身](https://www.msn.com/en-us/science/earth-science/climate-change-is-literally-impacting-time-itself/ar-AA1xqgGj)。

报纸上写道：

*数千年来，地球的自转速度大多在减慢，最大的驱动因素是月球引力作用带来的潮汐变化。地球外核的洋流（科学家仍在努力研究）也减缓了自转速度。但地核也能加快自转速度，这可能是最近发生的情况。在过去的二十年中，闰秒的增加变得越来越少。*

根据《纪事报》引用的[《自然》杂志文章](https://www.nature.com/articles/s41586-024-07170-0) ，这种影响微乎其微——地球自转速度每年变化不到一秒。但这确实增加了地球自转速度可能比预期略微*更快*的可能性，这最终将为计算机网络计时带来“前所未有的问题”。

《自然》杂志的文章是斯克里普斯海洋研究所加州大学圣地亚哥分校的地球物理学家Duncan Agnew的作品。《圣地亚哥联合论坛报》[称他为](https://www.sandiegouniontribune.com/2025/01/01/someone-san-diego-should-know-duncan-agnew/)“所谓的地球潮汐领域的领先科学家”，他也是[英国皇家天文学会](https://ras.ac.uk/journals/Editorial-Boards-and-Team/prof-duncan-agnew-deputy-editor-chief-2015-present)的副主编。

Agnew告诉《纪事报》：“一秒钟听起来不算什么”，但“在当今互联互通的世界中，时间错误可能导致巨大的问题。”想象一下，带有时间戳的数据库和同步的网络操作突然需要处理一个自上而下的命令，要求在年底*加快*一秒——这是史无前例的。

如果这种情况发生，《纪事报》写道，这可能是一个“让人想起[千年虫](https://thenewstack.io/how-the-y2k-bug-returned-on-jan-1-2020/)”的场景，当时人们担心日历翻到2000年时会出现广泛的错误。

但幸运的是，世界各地的计时员已经开始着手进行一些改变，可以在问题开始之前就避免这个问题。

![旧金山纪事报头条——气候变化影响时间本身 (Agnew关于负闰秒)](https://cdn.thenewstack.io/media/2025/01/1836500e-20250127_131829-scaled.jpg)

《纪事报》写道，来自融化的极地冰盖的水可能会微妙地影响地球的自转，并引用了去年发表在《自然》杂志上的一篇文章。

## 闰秒的终结？

自1972年以来，地球自转速度的微小变化一直通过在某些年份年底增加“[闰秒](https://www.timeanddate.com/time/leapseconds.html)”来解释。这使我们观测到的自转速度与来自[原子钟](https://thenewstack.io/farewell-to-the-internets-master-timekeeper-david-mills/)的更精确的时间持续时间测量结果同步。（Agnew的文章引用了一本[1960年的教科书](https://archive.org/details/rotationofearthg0000munk)，指出“地球是一个地球物理实验室，而不是计时器”。）

但是这些闰秒一直受到批评。《纪事报》记得2012年的闰秒是如何导致Reddit和澳洲航空公司出现问题的，而《计算机世界》2010年的一篇文章补充说，2008年的闰秒也“[在某些情况下导致Oracle集群软件意外重启](https://www.computerworld.com/article/1521003/time-waits-for-no-one-leap-seconds-may-be-cut.html)”。最终，这些担忧传到了计时领域最高层： [国际计量大会](https://www.bipm.org/en/cgpm-2022)（以其法语缩写*CGPM*而闻名），该大会每四年举行一次会议，并选择国际计量局的正式成员。

在他们2022年的最后一次会议上，大会投票决定在未来正式减少闰秒的频率，方法是在“2035年或之前”进行规则更改。
国际计量大会（CGPM）的理由很明确。他们的[2022年决议](https://www.bipm.org/en/cgpm-2022/resolution-4)承认，使用闰秒“会造成中断，从而可能导致包括全球导航卫星系统、电信和能源传输系统在内的关键数字基础设施发生严重故障。”（此外，这些卫星系统和数字网络的运营商“已经开发并应用了不同的方法来引入闰秒，这些方法并没有遵循任何商定的标准。这些不同的、不协调的方法的实施威胁着支撑关键国家基础设施的同步能力的弹性。”）

他们的决议还指出，“对计量、科学和技术机构进行的广泛调查”发现，需要解决闰秒相关的“中断”……


## 未定义的细节
那么，我们现在处于什么位置？科罗拉多大学博尔德分校的兼职物理学教授Judah Levine说：“闰秒规则现在没有变化。”Levine也是美国[国家标准与技术研究院](https://www.nist.gov/)的研究员——并且研究过时钟同步——他说，虽然CGPM可能会做出改变，但这些改变也进展缓慢。“如果系统发生变化，将在2035年或之前发生，可能会额外延迟到2040年。”

尽管如此，讨论已经在进行中。Levine强调，虽然变化的细节“现在还没有确定”，但计划是CGPM“在2026年的下次会议上讨论并决定这一变化。我认为届时会有一个决定，但也许不会。”

在过去的52年里，为了调整两种标准时间测量——协调世界时（UTC）和世界时（UT1）之间的差异，在某些年份的年底增加了闰秒。根据NIST的[说明](https://www.nist.gov/pml/time-and-frequency-division/leap-seconds-faqs) ，目标是将差异保持在小于0.9秒，“通常当UTC领先UT1 0.4秒或更多时，就会增加闰秒。”

Levine告诉我，当CGPM再次开会时，“决定将包括增加UT1和UTC之间的最大容差，但最大容差的值以及达到最大容差时会发生什么现在还没有定义。”尽管如此，Levine一直在仔细关注讨论，一些提案意味着我们多年内都不会再看到闰秒。“容差可能会增加到至少60秒，但也有一些替代方案：100秒或一小时。”

“也有可能将容差增加到更大的值，或者完全取消，但我认为这些可能性不大。”

那么，正在提出什么样的想法呢？Levine说：“这个群体主要分为两大类：”

- “有一组人主张最大容差大约为100秒或几分钟，”
- “还有一组人主张最大容差至少为一小时。”

Levine已经考虑过这一切将如何发展。“如果最大容差设置为一小时或更长，则需要几个世纪才能达到容差，并且调整过程将在很久以后，更接近事件发生时才能决定。

“如果容差大约为几分钟，那么或多或少在一个世纪左右就会达到最大容差，这时该做什么的问题就变得很重要。

“有很多不同的提案。我建议进行周期性的算法调整，但还有其他可能性，而且还没有决定。”


## 没有负闰秒？
Agnew的文章提出了网络运营商通过在年底加快时间戳来调整[地球自转速度加快](https://thenewstack.io/webreduce-programmers-on-earth-humans-in-space/)的可能性，即使用“负闰秒”——可能最早在2029年。纪事报提醒读者，CGPM投票决定在2035年前取消闰秒，但“这是否会在可能需要负闰秒之前完成尚不清楚。”

那么，如果在正式批准更大的差异之前发生另一个闰秒事件——甚至可能发生“负闰秒事件”——会发生什么呢？Levine承认，“如果在2035年之前出现负闰秒迫在眉睫的情况，那么整个业务几乎肯定会发生变化。最可能的解决方案是或多或少立即增加最大容差，以避免负闰秒。”
但他同时也补充了一个重要的警告：“负闰秒的概率很难准确确定。这个问题上有很多不同的论文，但十年级的推断有不确定性，我不会在这方面押注。”

Agnew的文章发表在[另一篇文章](https://www.nature.com/articles/d41586-024-00850-x)旁边，该文章同意Agnew的计算可能令人担忧。更重要的是，这第二篇文章的合著者是国际计量局时间部门主任[Patrizia Tavella](https://www.bipm.org/en/bipm-staff/tai)博士——该组织负责维护UTC。如果Agnew的计算正确，并且调整不得不渗透到我们当前的计时系统中，“它可能造成的麻烦是前所未有的，”Tavella写道。

但这只是一个很大的假设。《旧金山纪事报》也刊登了Levine的警告：“地球自转速度的短期变化意味着任何推断都存在很大的不确定性……在2035年之前，我不会对闰秒事件做出任何预测。”

这是世界时间标准制定者日常生活中面临的现实。当我问Tavella关于Levine所说的他对2035年地球自转预测的“重大不确定性”时，Tavella表示他也看到了同样的不确定性。

关于预测地球自转的具体时间间隔的困难，“我完全同意我的同事Judah Levine的观点。”

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1) | 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。