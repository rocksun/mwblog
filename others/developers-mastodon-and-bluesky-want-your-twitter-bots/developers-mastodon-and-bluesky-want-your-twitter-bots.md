
<!--
title: 开发者：Mastodon 和 Bluesky 想要你的 Twitter 机器人
cover: https://cdn.thenewstack.io/media/2024/11/cdc1b941-bots-nov24.jpg
-->

Mastodon和Bluesky已成为Twitter之后可行的第三方开发社交平台，但开发者仍面临风险。

> 译自 [Developers: Mastodon and Bluesky Want Your Twitter Bots](https://thenewstack.io/developers-mastodon-and-bluesky-want-your-twitter-bots/)，作者 Richard MacManus。

2022 年 10 月初，我发表了一篇时机最糟糕的文章之一：[开发者：Twitter 欢迎你的机器人](https://thenewstack.io/developers-twitter-wants-your-bots-and-other-read-write-apps/)。这是一篇对当时 Twitter 开发者平台负责人的采访，内容是关于第三方开发者如何被欢迎回到 Twitter 平台。

大约三周后，埃隆·马斯克收购了 Twitter。此后不久，[Shevat 被解雇](https://thenewstack.io/twitter-turmoil-we-need-an-open-protocol-for-public-discourse/)，他的整个团队也都被解雇了。不用说，X（以前称为 Twitter 的公司）不再需要你的机器人了。但好消息是，从第三方开发者的角度来看，Mastodon 和 Bluesky 作为 X 的主要替代品，会欢迎你的机器人——以及任何其他应用程序。

机器人指的是使用平台的 API 发布内容的自动化帐户，通常按照开发者定义的计划发布。它们是了解社交媒体平台的 API 和应用程序开发能力的好方法。

## 在 Mastodon 和 Bluesky 上运行机器人

要在 Mastodon 上托管机器人，你可以使用专门用于机器人的服务器——尽管我目前发现唯一一个开放注册的服务器是 [mastodon.bots](https://mastodon.bot/about)——或者你可以只使用其中一个通用实例。我关注的一个机器人，[never obsolete](https://mastodon.social/@256)，运行在主要的 Mastodon 服务器 mastodon.social 上。（稍后详细介绍专门的机器人服务器！）

![](https://cdn.thenewstack.io/media/2024/11/f46700e0-never-obsolete.jpg)

*永不过时的Mastodon机器人。*

许多 Mastodon 开发者使用 Glitch，[一个免费的在线 Web 应用程序构建器](https://thenewstack.io/developers-can-now-discover-and-curate-open-web-apps-on-glitch/)，来运行他们的机器人。例如，机器人开发者 [Stefan Bohacek](https://stefanbohacek.com/)，他同时运营资源网站 [Botwiki](http://botwiki)，拥有一个包含 54 个活跃 Mastodon 机器人的集合 [运行在 Glitch 上](https://stefans-creative-bots.glitch.me/)。但是，还有其他创建机器人的方法，例如通过 [一个 Python 应用程序](https://shkspr.mobi/blog/2018/08/easy-guide-to-building-mastodon-bots/) 或使用 [GitHub Actions](https://til.simonwillison.net/mastodon/mastodon-bots-github-actions)。

至于处理 [Mastodon API](https://docs.joinmastodon.org/client/intro/)，Bohacek 说这很容易。

“特别是对于 Mastodon 来说，创建机器人帐户非常容易，”[他在](https://stefanbohacek.online/@stefan/113373504557329086)回复我的 Mastodon 查询时写道。“就像设置常规帐户一样，你不需要验证你的电话号码，而这是 Twitter 的一项要求。Mastodon API 也非常易于使用，并且文档编制得很好，至少对于我自己的需求是这样。我喜欢你可以在其个人资料页面上将你的帐户标记为“自动化”。

如果你有兴趣创建 Mastodon 机器人，你可以在 [Botwiki 上找到更多资源](https://botwiki.org/resources/fediverse-bots/)。

那么 Bluesky 呢？你可以使用 [AT Protocol SDK](https://atproto.blue/en/latest/) 在那里创建机器人。Bluesky 甚至贴心地为你提供了创建机器人的 [代码模板](https://docs.bsky.app/docs/starter-templates/bots)（它是用 TypeScript 编写的），并推荐使用 Heroku 或 Fly.io 来部署它。

在撰写本文时，Bluesky 的 [社区展示](https://docs.bsky.app/showcase/?tags=bot) 中列出了 21 个机器人。但我喜欢的一个未列出的机器人是 [Retro Computers](https://bsky.app/profile/retrocomps.bsky.social)，它实际上是受 Mastodon 上的 *never obsolete* 启发的。Retro Computers 使用 [Python](https://thenewstack.io/what-is-python/) 脚本生成其“半自动化”帖子。

![](https://cdn.thenewstack.io/media/2024/11/cd27293b-retro-computers-bluesky.jpg)

*Bluesky上的复古计算机机器人。*

## Mastodon：稳定的机器人平台，但也存在风险

由于 Mastodon 比 Bluesky 存在的时间更长，因此它已经围绕机器人建立了一个可靠的生态系统。一些机器人开发者自 2017 年以来一直在 Mastodon 上活跃。其中一位是 [Darius Kazemi](https://tinysubversions.com/)，[我在 2022 年 5 月采访过他](https://thenewstack.io/why-developers-should-experiment-with-the-fediverse/)。Kazemi 之前曾在 Twitter 上大量创建机器人，但在 Twitter 打压机器人后于 2017 年转向了 fediverse。“然后他们还更改了所有 API，”Kazemi 解释道，“这些 API 是机器人与 Twitter 通信的编程接口。所以他们在没有任何警告的情况下更改了这些 API，所有东西都坏了。”

因此，甚至在埃隆·马斯克到来之前，Twitter 就已经在机器人开发方面搞砸了。与 Bohacek 一样，Kazemi 现在也在 Glitch 上托管他的 Mastodon 机器人。

尽管Mastodon上的机器人开发已经持续多年，但所选服务器仍存在风险。直到最近，专门从事机器人服务的领先Mastodon服务器是botsin.space。但它刚刚宣布将于12月关闭。

![](https://cdn.thenewstack.io/media/2024/11/738ab0c6-botsinspace.jpg)

*Botsin.space，一个专门用于Mastodon的实例，刚刚宣布关闭。*

botsin.space背后的开发者Colin Mitchell在其[博客文章](https://muffinlabs.com/posts/2024/10/29/10-29-rip-botsin-space/)中概述了关闭它的原因。在解释他是一名技术专业人员（“服务器管理是我的工作职责的一部分”）之后，他指出他的服务器支出一直在逐渐增加。在最近的Mastodon升级——[Mastodon 4.3](https://blog.joinmastodon.org/2024/10/mastodon-4.3/)于10月发布——之后，它达到了某种危机点，他表示这“导致了他的服务性能显著下降”。与其“投入大量资金购买硬件”，他选择优雅地关闭botsin.space。

这并非对Mastodon软件的谴责，但这是一个残酷的现实，许多[运行Mastodon实例的人](https://thenewstack.io/what-its-like-to-run-a-mastodon-server-in-the-musk-twitter-era/)都在亏损——因此这些服务器比Threads（Meta所有）或Bluesky这样的风投公司资助的平台更容易关闭。

## Bluesky的开发者风险

但Bluesky的风险同样严峻，甚至更甚。正如我在之前的文章中提到的那样，[Bluesky目前并没有非常去中心化](https://thenewstack.io/blueskys-at-protocol-pros-and-cons-for-developers/)——大约99%的基础设施直接受Bluesky公司控制。如果Bluesky被出售（就像Twitter一样）会怎样？或者如果它决定更改开发人员的规则（就像Twitter一样）会怎样？

自从我发表那篇文章以来，对Bluesky的更深入的批判出现了。自由软件开发者Gavin Anderegg [解释说](https://anderegg.ca/2024/11/15/maybe-bluesky-has-won)，Bluesky基础设施的关键部分——一个[中继](https://docs.bsky.app/docs/advanced-guides/federation-architecture#relay)，它抓取数据并将其输出到“一个大的数据流”中——对于第三方开发者来说运行起来非常昂贵。换句话说，开发者短期到中期可能不得不使用Bluesky的中继。他还指出，DID:PLC（一种用于管理身份的加密公共账本）和私信也“直接受Bluesky控制”。Anderegg的精辟语录如下：

“Bluesky比Facebook稍微去中心化一些——但并没有多多少。是的，你可以托管自己的数据。是的，你可以抓取网络上的所有内容。但是，除非你连接到Bluesky服务，否则你无法对其进行任何操作。我相信这种情况会随着时间的推移而改变，但这将是极其昂贵的，而且我们还没有达到那个阶段。”

## 结论

我认为Mastodon和Bluesky都值得作为第三方开发平台进行尝试，尽管显然要记住上述风险。但由于机器人作为一种应用程序类型风险相对较低（不像构建TweetDeck这样的大型应用程序），因此它是试用新社交平台的好方法。
