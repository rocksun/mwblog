# 甲骨文和 SUSE 因开源业务与红帽发生争执

竞争对手对红帽提议的新许可条款感到愤怒，根据这些条款，RHEL 的源代码只对付费客户开放。

![](https://cdn.thenewstack.io/media/2023/07/6a128ac3-logosa3b3d963-glen-carrie-n0zoovlpeja-unsplash-1024x589-1.png)
*图片来自 Unsplash 的 Glen Carrie 。*

科技巨头之间的争端总是引人注目的，尤其当它涉及开源软件开发这样贴近开发者心的事情。

这可能是为什么围绕[红帽](https://www.openshift.com/try?utm_content=inline-mention)公司决定限制其旗舰产品红帽企业版 Linux（RHEL）发行版源代码可用性的争议一直持续不断。简而言之：在此之前，该源代码对任何人都是可用的，这导致了与 RHEL 兼容的替代 Linux 发行版的大量出现，比如 [Rocky Linux](https://thenewstack.io/centos-creator-gregory-kurtzer-discusses-his-new-distro-rocky-linux/) [和AlmaLinux](https://thenewstack.io/jack-aboutboul-how-almalinux-came-to-be-and-why-it-was-needed/) 。根据红帽公司提出的新许可条款，RHEL 的源代码将只对付费客户开放。这一决定是在 [IBM 斥资 340 亿美元收购](https://thenewstack.io/turning-blue-ibm-to-acquire-red-hat/)红帽公司近乎四年后宣布的。

关于详细的时间线，[Tom Krazit 在 Runtime 通讯中提供了一份详细的回顾](https://www.runtime.news/suse-takes-the-fork-in-the-road/?ref=runtime-newsletter)。总之，红帽公司的决定遭到了开源社区许多人的敌对态度。具体来说，批评者认为将原本广泛可用的代码放在付费墙后与红帽公司 1993 年成立的开源原则背道而驰。毕竟，开源的核心原则是共享与分享。

红帽公司为此进行了辩护，称这些变化是为了保护其业务并支付员工报酬：“我们必须支付这些从事工作的人——那些对开源价值观坚定信念的热情贡献者，他们通宵达旦地辛勤工作，”[红帽公司核心系统副总裁 Mike McGrath 在六月的一篇博客文章中写道](https://www.redhat.com/en/blog/red-hats-commitment-open-source-response-gitcentosorg-changes)。重要的是， McGrath 还重申，红帽公司将继续使用 [CentOS Stream](https://thenewstack.io/centos-9-stream-is-now-available-but-should-you-use-it/) 项目作为分享 RHEL 即将发布版本的预览的地方，尽管不会提供当前稳定版本的代码。

## 甲骨文和 SUSE 对红帽进行抨击

然而，这篇文章并不代表事件的终结，本周甲骨文和 SUSE 纷纷发声，对正在苦苦挣扎的竞争对手红帽公司进行抨击。

在一篇由高管 [Edward Screven](https://www.oracle.com/corporate/executives/edward-screven/) 和 [Wim Coekaerts](https://www.oracle.com/corporate/executives/wim-coekaerts.html) 签署的博客文章中，甲骨文一方面抨击了红帽的策略，同时推出了自己的 Oracle Linux ，这是一个与 RHEL 兼容的发行版，据称对于被红帽公司抛弃的客户来说，将是一个不错的选择。甲骨文甚至暗示，这种改变是 IBM 的影响导致的，对此他们对此表示怀疑，认为这并不是必要的商业举措。

“有趣的是，IBM 不希望继续公开发布 RHEL 源代码，因为它必须支付自己的工程师？这似乎很奇怪，因为红帽作为一家成功的独立开源公司，早在 2019 年 IBM 以 340 亿美元收购红帽之前，就选择公开发布 RHEL 源代码并向其工程师支付报酬。”甲骨文高管们写道。

更令人吃惊的是，总部位于德国的开源巨头 SUSE 表示，[将投资 1000 万美元构建自己的 RHEL 分支](https://www.suse.com/news/SUSE-Preserves-Choice-in-Enterprise-Linux/)，并计划将其代码捐赠给尚未确定的基金会。值得注意的是，SUSE 将与 CIQ 合作，这是一家也赞助 RHEL 替代版本 Rocky Linux 开发的 Linux 支持公司，以开发这个新的操作系统。

SUSE 首席执行官 Dirk-Peter van Leeuwen 在[一篇正式的博客](https://www.suse.com/news/SUSE-Preserves-Choice-in-Enterprise-Linux/)文章中表示：“这项投资将确保未来多年内创新源源不断，并确保客户和社区不受供应商限制，今天和明天都能有真正的选择。”显然，这是对红帽公司的暗讽。

## 许多问题没有简单的答案

因此，摆在桌面上的重要问题是，所有这些对未来的开源开发意味着什么。

整个争端让人想起了 2019年 的开源讨论，当时像 Elastic 和 MongoDB 这样的初创公司采用了新的许可证，[使得亚马逊或腾讯等巨头很难基于它们的代码发布商业产品](https://www.businessinsider.com/amazon-web-services-elastic-elasticsearch-2019-3)。虽然细节有所不同——这次争斗是关于代码本身的发布，而且红帽公司远比上次涉及的初创公司要大得多——但所涉及的根本问题在很多方面上是相似的，即围绕开源理念和冷酷的商业现实之间的平衡。

在[本周发表的 TechCrunch 采访中](https://techcrunch.com/2023/07/11/why-suse-is-forking-red-hat-enterprise-linux/)，红帽公司的副总裁兼红帽企业版 Linux 的总经理 [Gunnar Hellekson](https://www.linkedin.com/in/gunnarhellekson/) 将该公司以前免费发布 RHEL 代码的做法视为利用红帽公司的资源来支持竞争对手。虽然他没有点名，但他暗示像甲骨文这样的公司拿走红帽公司的代码，然后“对其进行任何有趣或创新的工作，并在其版本上放上自己的标志，然后积极招募我的用户去使用他们的版本，而不是我的，”用他的话说。

“在开源社区，这是不良行为。它是合法的，但不受欢迎。这是适得其反的，不利于生态系统的发展，”他对 TechCrunch 表示。

所有这些在开源社区中引发了大量激烈的讨论。像 Chef 的联合创始人兼 System Initiative 的 CEO Adam Jacob 等人通过 Twitter [表达了对甲骨文立场的怀疑](https://twitter.com/adamhjk/status/1678883971462201346)，认为甲骨文的立场并非完全出于善意，并提醒人们，尽管这次受到了不少负面新闻报道，但红[帽公司几乎是现代开源商业模式的创始者](https://twitter.com/adamhjk/status/1678884645696581633?s=20)。另一方面，[像 Duckbill Group 的首席云经济学家和 IT 通才 Corey Quinn 则说](https://twitter.com/QuinnyPig/status/1678550737603923968?s=20)：“你有没有意识到，你需要付出多大的努力来对待开源，才会让甲骨文显得更好？”

短期内，红帽公司面临公关危机。然而，从长远来看，公司提出了围绕开源盈利的一系列棘手问题，这些问题并不容易解决。尽管开源代码已经对世界运作变得至关重要，但[实际编写这些代码的人在寻找获取合理报酬的方式方面仍面临困境](https://www.businessinsider.com/open-source-developers-burnout-low-pay-internet-2022-3)。虽然目前不会有人为红帽公司举办慈善活动，但这一开源时刻的结果将对未来开源公司及其员工如何赚钱产生重要影响。
