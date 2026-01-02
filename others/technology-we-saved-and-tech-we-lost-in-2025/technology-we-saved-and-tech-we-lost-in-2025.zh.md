旧岁飞逝，令人欣慰的是，我们看到了人们对前人工作的传承和保护。计算机历史博物馆、Stack Overflow 以及无数非营利组织和基金会，将过去的操作系统、技术讨论及其他创意作品带入了崭新的一年。

随着技术不断演进——有些变得过时，有些却又意外复活——我们看到了科技界是一个珍视其历史和遗产的社群的迹象。

而在2025年，他们的一些保护工作尤其引人注目。

## 1974年Unix磁带的发现

那是一个值得铭记的日子。犹他大学研究教授 [Rob Ricci](https://ricci.io/)（他的工作通常涉及构建云基础设施）在清理储藏室时有了一个惊人的发现。在一个被遗忘的盒子里，“我们的员工发现了这盘包含贝尔实验室约1973年的UNIX v4的磁带，” Ricci [在Mastodon上发帖](https://discuss.systems/@ricci/115504720054699983)称。

由于这可能是Unix v4唯一幸存的副本，这卷磁带被小心翼翼地运往硅谷。Ricci提到，发现它的工作人员亲自将这珍贵的磁带送到了博物馆，而不是通过邮寄。

在那里，这盘磁带被硅谷计算机历史博物馆的软件策展人 [Al Kossow](https://computerhistory.org/profile/al-kossow/) 细心地恢复并首次重新读取——这一刻[在](https://exquisite.tube/w/qoHtHzpNXncHwrfqpx31tF)我们现代社交媒体上[分享](https://exquisite.tube/w/qoHtHzpNXncHwrfqpx31tF)。“到目前为止，我们的一些人认为他们找到了《追捕怪兽》(Hunt The Wumpus)，” Ricci [打趣地发帖](https://discuss.systems/@ricci/115748587328701031)说，“以及一个Snobol解释器的C语言代码。”

[![Robert Ricci关于Unix v4社交媒体帖子的截图](https://cdn.thenewstack.io/media/2025/12/1c1a9089-screenshot-from-robert-ricci-social-media-post-about-unix-v4.png)](https://cdn.thenewstack.io/media/2025/12/1c1a9089-screenshot-from-robert-ricci-social-media-post-about-unix-v4.png)

而在地球的另一端，一位柏林的复古计算爱好者创建了一个[网站](http://squoze.net/UNIX/v4/README)，提供了磁带内容，可供引导启动，包括所有必要的说明，供爱好者在其自己的系统上使其运行。

那么他们发现了哪些技术文物呢？Ricci [后来发帖](https://discuss.systems/@ricci/115749601614636888)称，其中似乎包含一个名为 *sh.c* 的文件，他怀疑这可能是已知最古老的 [C 语言](https://thenewstack.io/introduction-to-c-programming-language/) shell 程序版本。一位社交媒体用户注意到，该操作系统的时区转换代码[包含一个名为 *nixonflg* 的标记变量](https://social.atypique.net/@zorun/115751343053946103)，显然是为了纪念1974年一个值得铭记的时刻。

当年一月——在辞职前七个月——尼克松总统颁布了[全年实行夏令时](https://www.congress.gov/bill/93rd-congress/senate-bill/2702)的法令。这项举措在杰拉尔德·福特总统任期八周后被[废止](https://www.fordlibrarymuseum.gov/sites/default/files/pdf_documents/library/document/0055/1668702.pdf)，但Unix磁带中仍然保留了 *nixonflg* 变量，该变量“如果设置为1，将全年启用夏令时，与‘白昼’无关。”

Tom’s Hardware [将这盘磁带称作](https://www.tomshardware.com/software/linux/unix-v4-recovered-from-randomly-found-tape-at-university-of-utah-only-known-copy-of-first-os-version-with-kernel-and-core-utilities-written-in-c)“一份应该温暖许多冰冷系统管理员心灵的圣诞礼物”，并回忆道，在磁带创建之时，Unix“仍然是一个逃脱实验室的实验品”。

12月26日，Ricci又发布了[另一条引人入胜的公告](https://discuss.systems/@ricci/115787578199513770)。“顺便说一句，还有更多的磁带。我们除了UNIX V4磁带外，还向计算机历史博物馆寄送了一盒其他磁带。”其中包括一个34年前的惠普（Hewlett-Packard）自家专有Unix版本，以及mt Xinu（该公司曾制作商业授权版BSD Unix）的一些1988年软件。尽管这些发现“不一定是‘丢失’的，并且可能由于许可问题而无法重新分发”，Ricci在社交媒体上显得很兴奋。

他发帖说：“如果他们从中发现任何有趣的东西，我会告诉你们。”

## Stack Overflow 关闭其数据中心

远离犹他州——在新泽西州——Stack Overflow 在2025年达到了自己的一个里程碑，最终将其所有业务完全迁移到云端，放弃了其站点可靠性工程（SRE）团队“在我们几乎整个16年历史中”一直管理的物理服务器。

2025年，Stack Overflow 精心淘汰了其硬件，同时仍保留了所有*数字*内容。

在“大撤柜”那天，博客/播客编辑 [Ryan Donovan](https://www.linkedin.com/in/ryan-donovan-1477b64/) 深情地回忆道，这些服务器“在我们历史和心中占有特殊地位”。

当他于2019年加入公司时，他曾看到“原始服务器像一只受宠的宠物一样，挂在墙上，并配有赞美牌匾”。但在[7月2日的一篇博客文章](https://stackoverflow.blog/2025/12/24/the-great-unracking-saying-goodbye-to-the-servers-at-our-physical-datacenter/)中，他记录了他们拔掉400多根电缆的那一天——“我们的拔线过程就是把所有东西扔到房间角落”——并堆放了七大堆退役服务器/网络设备。“再见，感谢所有的数据！”

[![废弃电缆堆 - Stack Overflow 博客图片截图（原发布于7月2日）](https://cdn.thenewstack.io/media/2025/12/678398c3-junk-pile-of-cords-screenshot-of-image-from-stack-overflow-blog-originally-published-july-2.png)](https://cdn.thenewstack.io/media/2025/12/678398c3-junk-pile-of-cords-screenshot-of-image-from-stack-overflow-blog-originally-published-july-2.png)

接着：50台服务器被销毁或拆解，“出于安全原因（并保护我们所有用户和客户的个人身份信息）”。正如该网站的可靠性工程总监告诉他的那样，“不再需要温柔对待了。”在过去的16年里，其SRE团队负责所有布线、上架（以及更换故障磁盘）工作，正如博客文章回忆的，“这需要有人亲自到数据中心并操作机器。”

但现在呢？“我们的服务器现在是‘牛’，而不是‘宠物’。没有人需要开车去我们的新泽西数据中心更换或重启硬件了。”

[![Stack Overflow 博客图片截图（原发布于7月2日）](https://cdn.thenewstack.io/media/2025/12/f4a3b4ce-screenshot-of-image-from-stack-overflow-blog-originally-published-july-2.png)](https://cdn.thenewstack.io/media/2025/12/f4a3b4ce-screenshot-of-image-from-stack-overflow-blog-originally-published-july-2.png)

## 2025年其他技术告别与传承

除了Unix v4，2025年还见证了世界技术史被保存和纪念的其他时刻。

但2025年也见证了一些技术的告别。AOL 终止了其[拨号上网服务](https://help.aol.com/articles/dial-up-internet-to-be-discontinued)。Roomba [申请破产](https://www.reuters.com/technology/irobot-enters-chapter-11-lender-acquire-roomba-maker-2025-12-15/)。PC Magazine 甚至创建了自己的纪念文章，题为[“连接丢失：2025年逝去的技术”](https://www.pcmag.com/news/tech-that-died-in-2025-aol-dial-up-skype-dyson-zone-pocket)，其中包括 [Humane AI Pin](https://thenewstack.io/ambient-ai-humanes-ai-pin-embarks-on-a-dreams-long-road/) 和 [Skype](https://support.microsoft.com/en-us/skype/skype-is-retiring-in-may-2025-what-you-need-to-know-2a7d2501-427f-485e-8be0-2068a9f90472/)。

Enron.com 在其商标被一家T恤公司收购后重新上线，这家公司开玩笑说他们现在正在研究[蛋形核反应堆](https://enron.com/pages/the-egg)。

[![重新启动的 Enron.com 网站截图 (2025)](https://cdn.thenewstack.io/media/2025/12/3b445266-screenshot-from-relaunched-enron-dot-com-2025.png)](https://cdn.thenewstack.io/media/2025/12/3b445266-screenshot-from-relaunched-enron-dot-com-2025.png)

## 展望2026年

所以，也许今天正是庆祝我们在2025年*没有*失去的东西的绝佳时机。尽管Vim的创建者 [Bram Moolenaar](https://thenewstack.io/bram-moolenaar-author-of-the-open-source-vim-code-editor-has-died/) 已于2023年去世，Vim [仍在继续发展](https://thenewstack.io/vim-after-bram-a-core-maintainer-on-how-theyve-kept-it-going/)。甚至[国际混淆C语言代码大赛](https://www.ioccc.org/)也在2025年——中断四年后——重新回归，[庆祝并纪念其40周年](https://thenewstack.io/the-obfuscated-c-code-contest-confronts-the-age-of-ai/)。在今年最感人的时刻之一，75岁的EFF联合创始人 [Mitch Kapor](https://en.wikipedia.org/wiki/Mitch_Kapor) 甚至完成了[他1979年为创立Lotus而辍学](https://www.bostonglobe.com/2025/06/24/business/mitch-kapor-mit-degree-bill-aulet/)的研究生项目。

Kapor撰写了一篇[及时而真诚的论文](https://www.d-eship.com/wp-content/uploads/2025/06/kapor-mdkapor-msms-ssm-2025-sig.pdf)，主题是“弥补差距的投资”。

展望未来，我们已经可以看到更多技术里程碑正向2026年的我们走来。[史蒂夫·乔布斯](https://en.wikipedia.org/wiki/Steve_Jobs)将[出现在一美元硬币上](https://www.usmint.gov/news/press-releases/united-states-mint-releases-2026-american-innovation-one-dollar-coin-program-designs)。

[![史蒂夫·乔布斯硬币 - 2026-American-Innovation-Unc-Reverse-California.jpg](https://cdn.thenewstack.io/media/2025/12/6aa184fc-steve-jobs-coin-2026-american-innovation-unc-reverse-california.jpg)](https://cdn.thenewstack.io/media/2025/12/6aa184fc-steve-jobs-coin-2026-american-innovation-unc-reverse-california.jpg)

Java 将[停止支持 Java Applet](https://inside.java/2025/12/03/applet-removal/)。我们将看到 [Digg.com 的重新上线](https://reboot.digg.com/)，而劳拉·克劳馥（Lara Croft）将[继续她的古墓探险](https://youtu.be/n6JxVxSHjqE)。

当1月1日太阳升起时，数百份1925年的录音将[最终进入公共领域](https://web.law.duke.edu/cspd/publicdomainday/2026/)——同时还有数百份1930年出版的作品。

或许这一切都证明了科技界依然是一个充满活力的地方——它在展望截然不同的未来时，仍不忘回望过去。一如既往，在2026年，问题将不再是我们拥有什么技术，而是我们最终将如何使用它们。但至少那些铭记过去的人，不会注定重蹈覆辙。

令人欣慰的是，2025年也包含了一些闪光的例子，展现了科技界是一个珍视其历史的社群。