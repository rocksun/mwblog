
<!--
title: 千里之行，始于足下：打造开放社交Web应用
cover: https://cdn.thenewstack.io/media/2025/10/7be9a070-getty-images-jqokwlzwrbk-unsplashb.jpg
summary: 开放社交网络（如联邦宇宙、Bluesky）正在发展但开发者关注度不足。FediForum强调“从小处着手”。新产品AltStore、Bridgy Fed、Frequency和CrowdBucks亮相，预示去中心化、注重隐私的社区构建机遇。
-->

开放社交网络（如联邦宇宙、Bluesky）正在发展但开发者关注度不足。FediForum强调“从小处着手”。新产品AltStore、Bridgy Fed、Frequency和CrowdBucks亮相，预示去中心化、注重隐私的社区构建机遇。

> 译自：[Everything Big Starts Small: Building Open Social Web Apps](https://thenewstack.io/everything-big-starts-small-building-open-social-web-apps/)
> 
> 作者：Richard MacManus

埃隆·马斯克（Elon Musk）[收购 Twitter](https://thenewstack.io/twitter-turmoil-we-need-an-open-protocol-for-public-discourse/) 至今已近三年。自那时起，联邦宇宙（fediverse）——一个由 [W3C 标准 ActivityPub](https://thenewstack.io/devs-are-excited-by-activitypub-open-protocol-for-mastodon/) 驱动的去中心化网络产品集合——持续发展。[Bluesky 的 AT 协议](https://thenewstack.io/blueskys-at-protocol-pros-and-cons-for-developers/)也推出了一些引人入胜的新应用。但总体而言，这些协议上的应用开发仍处于初始阶段。坦率地说：开放社交网络尚未获得应有的开发者关注。

本周，我参加了最新一届的 [FediForum](https://fediforum.org/)，这是一个为期两天的线上活动，旨在了解开放社交网络开发的最新动态。

## 开放社交网络的“从小处着手”理念

FediForum 的主题演讲由 ProPublica 的技术高级总监 Ben Werdmuller 发表。他的核心主题之一是“所有伟大的事物都始于微小。”他提到 Twitter 最初是一个短信群发服务，其灵感来源于 2004 年美国民主党和共和党大会期间出现的一个名为 TextMob 的行动主义工具。其理念是让抗议活动的组织者和参与者能够快速安全地通过短信发送群组文本消息。

Werdmuller 说：“我们所有的微博工具都承袭了这一脉络。为特定人群设计、因特定原因而长度受限的短消息，就是*那个*用例的产物。一个特定的用例催生了一个可行的原型，进而推广到更广泛的应用。这种模式一再重复。”

> “……开放社交网络若要蓬勃发展，我们需要回归拥有真实世界用例的真实社区，并比任何其他方案更好地解决他们的问题。”
> 
> **——Ben Werdmuller，ProPublica 技术高级总监**

Werdmuller 暗示，这种理念可以更广泛地应用于其他类型的联邦宇宙应用。

“因此，开放社交网络若要蓬勃发展，我们需要回归拥有真实世界用例的真实社区，并比任何其他方案更好地解决他们的问题——不一定是解决社区内个人的需求，而是解决相互关联的社区本身的需求。”

## 新兴联邦宇宙产品和公告

如今大多数人已经[了解 Mastodon](https://thenewstack.io/what-its-like-to-run-a-mastodon-server-in-the-musk-twitter-era/)，并且可能也知道 [Meta 的 Threads](https://thenewstack.io/threads-adopting-activitypub-makes-sense-but-wont-be-easy/) 对 ActivityPub 的“半熟”采纳。如果你是一名技术爱好者，可能也听说过用于视频的 PeerTube、用于照片的 Pixelfed 以及用于社交新闻和链接聚合的 Lemmy。但开放社交网络上还有哪些新事物呢？

在本周的 FediForum 上，有一些有前景的公告。

### AltStore：一个替代应用商店加入联邦宇宙

其中之一是 [AltStore](https://altstore.io/) 进军联邦宇宙。顾名思义，AltStore 是一个适用于 iOS 的替代应用商店——换句话说，它实现了 iOS 应用的“侧载”。目前它仅在欧洲可用，但该公司[计划](https://rileytestut.ut.com/blog/2025/10/07/evolving-altstore-pal/)“在年底前”在日本、巴西和澳大利亚推出，“英国将于 2026 年跟进”。

AltStore 的创始 CEO Riley Testut 在 FediForum 上展示了新的联邦宇宙整合。基本上，每个 AltStore 源都会通过 [AltStore 的 Mastodon 服务器](https://explore.alt.store/)获得自己的 ActivityPub 账户，随后可以被任何其他开放社交网络账户关注——包括通过 Bridgy Fed 桥接技术在 Bluesky 上关注。

Testut 解释说：“这是 AltStore 中所有内容的一个公开信息流，因此你不再需要打开应用就能看到发生了什么。”

[![AltStore](https://cdn.thenewstack.io/media/2025/10/9536d507-altstore-mastodon-oct25.jpg)](https://cdn.thenewstack.io/media/2025/10/9536d507-altstore-mastodon-oct25.jpg)

*联邦宇宙上的 AltStore。*

AltStore 上目前最受关注的应用是 Fortnite；它由 Epic Games 拥有，该公司一直在法庭上与苹果就 iOS App Store 应用内购买 30% 的佣金进行斗争。

Fortnite 信息流包含 AltStore 上其应用的更新、新闻项目以及 Epic Games 希望与联邦宇宙分享的任何其他内容。

在 Testut 做了 5 分钟的演示后，FediForum 联合主持人 Johannes Ernst 指出，这是一个很好的例子，说明了*不类似 Twitter* 的应用也可以加入联邦宇宙。“我们可以做更多具有社交性质的事情，例如社交商务，”Ernst 说。

### Bridgy Fed：连接 Mastodon 和 Bluesky

我前面提到了 Bridgy Fed——其背后的人们也在 FediForum 上分享了消息。[Bridgy Fed](https://fed.brid.gy/) 基本上允许你将你的 Mastodon 账户同步到 Bluesky，反之亦然。早在八月，Bridgy Fed 背后的非营利组织 *A New Social* 推出了一款名为 [Bounce](https://blog.anew.social/bounce-beta-now-live/) 的产品，帮助 Bluesky 用户使用 Bridgy Fed 迁移到 Mastodon。在 FediForum 上，它宣布了进行反向迁移的能力：[从 Mastodon 到 Bluesky](https://blog.anew.social/bounce-mastodon-to-bluesky/)（技术上来说，是任何 AT Protocol 账户——因此也包括 BlackSky，一个受黑人社区欢迎的 BlueSky 服务器）。

正如联合创始人 Anuj Ahooja 在 FediForum 上所说：“我们通过将你的 Mastodon 账户迁移到 Bridgy Fed，让你保留所有关注者和所有桥接关注来实现这一点。”

鉴于 Bluesky 最近[关于审核的争议](https://techcrunch.com/2025/10/05/waffles-eat-bluesky/)——这似乎导致 Mastodon 注册量激增（或者至少是现有 Mastodon 用户发布“别再把新用户吓跑了”的帖子激增），这条消息发布的时间可能不合时宜。

### Frequency：一款注重隐私的照片共享应用

在 FediForum 上引起我注意的另一个新应用是 [Frequency](https://frequency.app/about)，这是一款注重隐私且没有算法的参与诱饵的照片共享应用。它由 Jesse Karmani 开发，她在 FediForum 上进行了展示。她将 Frequency 描述为“一款联邦制的照片和视频共享应用，让你与朋友和家人分享个人生活。”

[![Frequency app](https://cdn.thenewstack.io/media/2025/10/80e494a2-frequency-app-screenshots.jpg)](https://cdn.thenewstack.io/media/2025/10/80e494a2-frequency-app-screenshots.jpg)

*Frequency 应用*

在我的测试中，我能够注册一个账户（有少量月费或年费），从 Mastodon 关注该账户（需要 Frequency 账户批准），发布一张照片，然后在 Mastodon 中将该照片视为仅关注者可见的帖子。对隐私的关注使 Frequency 有别于典型微博应用默认公开的设置——甚至目前的领先联邦宇宙照片共享应用 Pixelfed。

### CrowdBucks：一个面向创作者的变现平台

说到支付少量费用，[CrowdBucks](https://crowdbucks.fund/) 是一个新项目，希望能将此带给联邦宇宙的创作者。它被描述为“一个联邦宇宙原生的众筹、打赏、支付和会员平台”。

创始人 Charles Iliya Krempeaux（又名 reiver）在 FediForum 上谈到了这个产品。他解释说，其动机是帮助“让联邦宇宙持久存在”。

“其中一部分原因是，我认为人们需要在联邦宇宙中能够自给自足。这包括运营服务器的系统管理员、开发软件的开发者、创作者以及其他人员。”

[![CrowdBucks](https://cdn.thenewstack.io/media/2025/10/bfd1b64e-70de82f4bdec5f0f.png)](https://cdn.thenewstack.io/media/2025/10/bfd1b64e-70de82f4bdec5f0f.png)

*CrowdBucks 用户界面。*

## 联邦宇宙中的开发者机遇

与我[在六月的上一届 FediForum](https://thenewstack.io/bringing-joy-back-to-the-web-fediverse-vs-centralized-apps/) 上撰写的联邦宇宙产品类似，上面提到的产品——AltStore、Bounce、Frequency、CrowdBucks——仍处于早期阶段，并且（在某些情况下）对“普通人”来说难以采纳。但这不应分散我们对此处机遇的注意力：以注重隐私的方式、秉持与网络精神一致的开放心态，构建连接社区的新方式。请记住，蒂姆·伯纳斯-李爵士（Tim Berners-Lee）设计网络是为了使其成为一个开放的网络，而不是由公司控制的网络。

目前在开放社交网络上构建的应用可能规模尚小，但它们正在将去中心化和真正的自由带回互联网。用 Werdmuller 的话来说，所有伟大的事物都始于微小。