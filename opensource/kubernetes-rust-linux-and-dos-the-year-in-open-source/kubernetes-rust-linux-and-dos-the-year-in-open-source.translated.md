# Kubernetes、Rust、Linux和DOS？开源年度回顾

![开源年度回顾特色图片：Kubernetes、Rust、Linux和DOS？](https://cdn.thenewstack.io/media/2023/12/aec929b1-year-wrapup-1-1024x576.png)

开源运动浩瀚无垠，涵盖了半个世纪前启动的项目，以及几个月前启动（或重新启动）的项目。随着旧年匆匆逝去，让我们回顾一下2024年一些最热门的开源项目——检查它们的健康状况和发展情况，并祝愿它们在新的一年里好运。

有一些显而易见的大事件。[“Elasticsearch再次开源！”](https://thenewstack.io/whats-behind-elastics-unexpected-return-to-open-source/)[Elastic](https://www.elastic.co/) [在八月宣布](https://www.elastic.co/blog/elasticsearch-is-open-source-again)，为其产品添加了[开放源代码倡议](https://opensource.org/)-批准的许可证，以回应对其[2021年许可限制](https://thenewstack.io/this-week-in-programming-the-elasticsearch-saga-continues/)使其产品成为“[伪开源](https://opensource.org/blog/the-sspl-is-not-an-open-source-license)”的批评。

当[Redis](https://redis.com/?utm_content=inline+mention) [更改其NoSQL数据库的许可证](https://github.com/redis/redis/blob/0b34396924eca4edc524469886dc5be6c77ec4ed/LICENSE.txt)时，它突然面临着一个名为Valkey的分支[得到资金雄厚的重量级人物的支持](https://thenewstack.io/valkey-is-a-different-kind-of-fork/)，例如[亚马逊网络服务](https://aws.amazon.com/?utm_content=inline+mention)、[谷歌](https://cloud.google.com/?utm_content=inline+mention)、[Linux基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention)和[甲骨文](https://developer.oracle.com/?utm_content=inline+mention)。

但是，开源运动的影响范围与[自由软件基金会](https://www.fsf.org/)本身一样广泛，也像一个[Kubernetes](https://roadmap.sh/kubernetes)集群一样庞大。那么，2024年开源运动的其他亮点——无论是大型项目还是小型项目——以及被忽视的里程碑是什么呢？

## Kubernetes、Linux和Rust

随着时间的推移，2024年Kubernetes迎来了十周年纪念日，并在谷歌加利福尼亚州山景城的园区举行了特别的[为期三小时的庆祝活动](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/)。回顾过去，Kubernetes的共同创建者回忆起一个令人担忧的时代，亚马逊的云服务“有效地创造了一种极具破坏性的开源商业化方式”。

但他补充说，Kubernetes团队从开源容器管理平台[Docker](https://www.docker.com/?utm_content=inline+mention)的成功中获得了灵感。“我认为如果没有Docker，Kubernetes就不存在，”在Docker创建者为Docker创作的特别介绍中说道。

因此，有很多值得庆祝的事情，[Kubernetes社区在世界各地都参与其中](https://thenewstack.io/how-the-kubernetes-community-celebrated-its-10th-anniversary/)。

![Snyk容器产品总监在伦敦OpenUK KuberTENes生日派对上吹灭蜡烛（照片由Jennifer Riggins拍摄）](https://cdn.thenewstack.io/media/2024/06/2008cb45-snyk-container-product-director-hannah-foxwell-blows-out-candles-at-openuk-kubertenes-birthday-bash-in-london-photo-by-jennifer-riggins-1024x576.jpg)

Snyk容器产品总监吹灭了OpenUK的KuberTENes生日派对上的蜡烛。

yall.

[#kubernetes]改变了我的一生。我非常感谢社区的早期创始人及成员，他们对价值观和组织设计如此用心。如此精致，如此美好。如果你问我，这就是秘诀。[#kuberTENes]永远[pic.twitter.com/awlVpuYdc0]— @paris@hachyderm.io (@ParisInBmore) [2024年6月7日]

但正如Kubernetes开发者喜欢说的那样，Kubernetes只是Linux提供了一个接口和包装器，用于熟悉的Linux功能。
十月，Jalal在KubeFM播客的一个精彩剧集中（由Cloud Native Computing Foundation大使Bart Farrell主持）阐述了他的观点。幸运的是，2024年，Linux也依然强劲，庆祝其33周年，并创下了安装率在桌面电脑中占比的新纪录。（根据StatCounter 8月份的数据，为4.55%，这引发了关于期待已久的“Linux桌面元年”到来的笑话。）

然而，12月初，Linux内核维护者Greg Kroah-Hartman看到了未来真正进展的迹象，预测在一些关键的驱动程序绑定器被添加到即将发布的Linux内核6.13之后，“一个转折点”将为内核带来“更多Rust驱动程序”。

Rust本身也是开源家族的一员，并被视为未来几年中将内存安全带入代码库的关键工具。因此，谷歌在2月份宣布向Rust基金会提供一百万美元的资助，以支持“提高Rust代码与现有遗留C++代码库互操作性的能力”的工作。11月，AWS和Rust基金会宣布了新的现金奖励，用于完成一项在线倡议中的挑战，以验证Rust标准库的安全性。

## 开发者资金？
寻找新的资金来源继续困扰着开源社区。开源倡议的最初联合创始人Bruce Perens甚至正在开发一种替代许可证，该许可证允许个人和小型组织免费使用软件，而“财力雄厚的实体”必须为支持开源开发者的基金做出贡献。

![Bruce Perens, 2009年活动照片 (来源：维基共享资源)](https://cdn.thenewstack.io/media/2024/11/c1fa6192-bruce-perens-2009-2.jpg)
2009年Bruce Perens在活动中的存档照片，来自维基共享资源。

但一些资金仍在不断涌现。

- 十月，据Phoronix报道，德国的主权科技基金宣布，在过去两年中，已向60个开放技术项目投资超过2490万美元。
- GitHub安全开源基金于11月启动，承诺投资“用于支持大型项目的快速增长的依赖项的安全”，初始捐款为125万美元，捐赠者包括American Express、Microsoft、Shopify和Stripe。
12月，Linux基金会发布了一份关于开源资金的报告，该报告与GitHub和哈佛大学创新科学实验室合著。他们发现，他们调查的501个组织每年投资17亿美元用于开源，“这可以推断出，整个开源生态系统每年大约投资77亿美元。”

然而，86%的投资来自其员工的劳动贡献，只有14%（或10.78亿美元）是直接的财政贡献。

为了刺激更多贡献，旧金山甚至开始出现广告牌，羞辱那些不资助开源维护者的科技公司。

看到旧金山的这些令人震惊的广告牌，并问道WTF？我们也是——资金在哪里？加入我们，承诺为每个开发者提供2000美元，以支持您的业务所依赖的开源项目：

[https://t.co/uBZF3M19h0](https://t.co/uBZF3M19h0) [pic.twitter.com/Z5GoCXnjUP](https://pic.twitter.com/Z5GoCXnjUP) — Chris Jennings (@ckj) [2024年10月11日](2024年10月11日)
“我们的目标是在科技行业建立一种新的社会规范，即公司付费给开源维护者，这样倦怠和相关的安全问题（例如XZ和Apache Log4j中的问题）将成为过去，”[开源承诺](https://opensourcepledge.com/about/)网站上写道。或者，正如项目联合创始人[Chad Whitacre](https://www.linkedin.com/in/chadwhitacre/) [告诉The Register](https://www.theregister.com/2024/10/25/open_source_funding_ads/)的那样，“这些广告牌显然是一种俏皮的方式来吸引人们的注意，而且它们很有效。”

开源计划组织发布了一份[支持声明](https://opensource.org/blog/the-open-source-initiative-supports-the-open-source-pledge)来支持该组织。

## 2024年姗姗来迟的开源发布

开源软件继续其漫长的征程，随着岁月的流逝，不断创造里程碑。2025年，自由软件基金会将庆祝其40周年，今年则带来了一些[庆祝其39周年的活动](https://www.fsf.org/blogs/community/fsf-turns-39)。但在另一种完全不同的里程碑中，微软在四月终于[开源了1988年MS-DOS 4.0的代码](https://opensource.microsoft.com/blog/2024/04/25/open-sourcing-ms-dos-4-0/)，这些代码是在开源时代开始之前很久就编写好的，当时微软是一家完全封闭源代码的公司。

也许更有意义的是，六月，开发者[Jim Hall](https://freedos.org/jhall/)庆祝了[FreeDOS](https://www.freedos.org/) 30周年，这是他于1994年推出的开源MS-DOS替代品。现在协调着一个更大的开发社区，Hall利用这个周年纪念日分享了[他过去30年学到的经验](https://opensource.net/lessons-learned-open-source-30-years-freedos/)，并在OpenSource.net博客上发表了一篇文章，首先强调项目“必须扎根于社区”，并且必须进行尊重的沟通。

Hall写道：“对于任何开源项目来说，三十年是很长的一段时间，特别是对于像FreeDOS这样的复古计算操作系统来说。”“但这都是因为我们社区中优秀的开发者和用户。在庆祝FreeDOS的同时，我们也在庆祝所有为其创建程序、修复bug、添加功能、翻译消息、编写文档、分享文章或以其他方式做出贡献的人。”

也许这一切都证明了开源运动的美妙之处在于它包含了如此广泛的项目，无论大小。轻量级的Dillo网络浏览器通过[一个新的GitHub仓库](https://github.com/dillo-browser/dillo/)庆祝其25周年纪念日，重新启动了该项目。首席开发者[Rodrigo Arias Mallo](https://github.com/rodarima)受到Atari论坛宣布这款25岁的浏览器已[成功移植到Atari模拟器](https://github.com/dillo-browser/dillo/issues/34)的启发，很快科技新闻网站就[欢呼](https://hackaday.com/2024/05/11/the-minimalistic-dillo-web-browser-is-back/)为期[九年停滞](https://9to5linux.com/dillo-3-1-open-source-web-browser-released-after-9-year-hiatus)的[结束](https://www.theregister.com/2024/05/07/dillo_browser_v3_1/)。

甚至还有一个1995年视频游戏《运输大亨豪华版》的开源重制版，仍在积极开发中，并在三月份[庆祝其20周年纪念日](https://www.openttd.org/news/2024/03/06/happy-birthday)。Steam还[重新发布](https://store.steampowered.com/app/2330720/ChipWits/)了1984年的教育游戏[ChipWits](https://en.wikipedia.org/wiki/ChipWits)，并[开源了其1984年的原始代码](https://github.com/chipwits/chipwits-forth)。

三月份还发布了类Unix开源操作系统NetBSD的10.0版本。NetBSD 10.0于1993年首次发布，“自2019年以来一直在开发中，”[Phoronix报道](https://www.phoronix.com/news/NetBSD-10.0-Released)，带来了自动交换加密、WireGuard支持和“对许多更新的Arm平台的支持，包括Apple Silicon和更新的Raspberry Pi主板。”

九月甚至带来了[Haiku的新测试版候选版本](https://www.haiku-os.org/news/2024-09-13_haiku_r1_beta5/)，这是一个受1985年操作系统[BeOS](https://en.wikipedia.org/wiki/BeOS)启发的MIT许可操作系统。

## 开源开发者使用的开源工具

开源运动的一大乐趣是不断创建开源工具，用于进行更多开源编码。

Photoshop替代品[Gimp](https://www.gimp.org/)自1998年以来就存在了。但今年出现了[Gimp 3.0的新测试版候选版本](https://www.gimp.org/news/2024/11/06/gimp-3-0-RC1-released/)，这是自2018年以来首次重大更新，[据LWN.net报道](https://lwn.net/Articles/998793/)。（Gimp还宣布重组其开发流程，“以减少版本发布之间的时间”。）
GIMP的logo。

虽然GitHub已于[2022年](https://github.blog/news-insights/product-news/sunsetting-atom/)停止了其[Atom](https://github.com/atom-community/atom)文本编辑器的开发，但这只是导致了更多开源替代方案的出现。2024年见证了[Pulsar](https://github.com/pulsar-edit/pulsar)的持续开发，它自称为“一个真正的社区主导项目，旨在使原Atom项目现代化、更新和改进，成为一个现代化、可修改且完全开放的编辑器”。

与此同时，三位前Atom开发者也组建了一家初创公司，致力于构建Atom的“更完善和成熟的版本”，并在2024年1月[开源了其Zed编辑器的代码](https://zed.dev/blog/zed-is-now-open-source)。（他们的博客文章宣称：“我们将需要所有可能的帮助”，并补充道：“我们也认为开源会更有趣。”）

2024年又出现了一个开源开发环境。[Eclipse基金会](https://www.eclipse.org/)宣布其[开源Theia IDE](https://eclipsesource.com/blogs/2024/06/27/introducing-the-theia-ide/)正式上市，适用于云端和桌面——“兼容VS Code扩展”。

所以，如果2024年有什么信息，也许那就是开源运动无处不在，它以一个非常好的想法的不可磨灭的力量跨越时空。它的影响回荡在过去的岁月里——并延续到未来的岁月里——同时留下了一个不断壮大的快乐和满意的用户社区。

我们祝他们新年快乐。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1) 科技发展日新月异，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。