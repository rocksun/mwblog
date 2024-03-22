
<!--
title: FediForum展示新的联邦宇宙应用和开发者网络
cover: https://cdn.thenewstack.io/media/2024/03/823e38fd-agnieszka-ziomek-ucyx_xn8y1i-unsplash.jpg
-->

在 FediForum，新的联邦宇宙应用程序向活跃的开源倡导者社区进行了演示。还讨论了联邦宇宙开发者网络。

> 译自 [FediForum Showcases New Fediverse Apps and Developer Network](https://thenewstack.io/fediforum-showcases-new-fediverse-apps-and-developer-network/)，作者 Richard MacManus。

本周我参加了 [FediForum](https://fediforum.org/)，这是一个为期两天的关于 fediverse 技术的虚拟活动。[fediverse](https://thenewstack.io/the-fediverse-points-to-our-social-media-future-post-musk/) 是一个分散的应用程序网络，通过 W3C [ActivityPub 协议](https://thenewstack.io/devs-are-excited-by-activitypub-open-protocol-for-mastodon/) 相互连接。它最大、最知名的应用程序是 Mastodon，这是一个微博平台，Meta 的 Threads 目前正在与之 [互联](https://thenewstack.io/threads-adopting-activitypub-makes-sense-but-wont-be-easy/)（通过 ActivityPub）。

然而，FediForum 今年展示的是，fediverse 不仅包含 Mastodon（以及即将推出的 Threads），还包含更多应用程序。我将在本文中讨论一些更有前途的应用程序/服务。

我们还将了解 Fediverse Developer Network，这是一个由 Andy Piper 和其他几位活跃的 fediverse 开发者组织的热情的“fedidevs”的新网络。

## 有前途的 Fediverse 应用程序

除了 Mastodon，你可能已经听说过 Lemmy（一个 Reddit 类型的应用程序）、Pixelfed（照片共享）和 PeerTube（一个 YouTube 克隆）。但在 FediForum 的两天活动中每天开场的 5 分钟快速演示环节中，我发现了一堆其他非常有前途的应用程序。

第一天演示的亮点是被 Meta 员工 [Peter Cottle 的演示](https://www.youtube.com/watch?v=XGEVy-CjBBg&t=1s) 所掩盖，该演示展示了 Threads 如何连接到 Mastodon。他指出，Threads 用户可以在其设置中选择启用“fediverse 共享”，其中包括一个弹出窗口，解释 fediverse 是什么。

![](https://cdn.thenewstack.io/media/2024/03/7129b092-threads_settings_fedi2-990x1024.png)

但我发现查看正在构建的新应用程序更有趣。第一天的一个例子是 [Newsmast](https://newsmast.org/)，这是一个基于 Mastodon 软件分支的基于主题的新闻聚合器。它背后的团队是一个非营利组织，其目标是“利用社交媒体的力量造福社会”。

除了 Newsmast，该团队还在构建 Patchwork，演示者 Michael Foster 将其描述为“一个易于使用的可定制的 fediverse 入门工具，供组织使用”。使用这项技术（它同样基于 Mastodon 软件），组织可以为自己的主题创建一个“社区服务器”。

Newsmast 如何很好地整理各种主题，你的体验可能会有所不同，但很高兴看到有人尝试为 fediverse 创建主题提要。

![](https://cdn.thenewstack.io/media/2024/03/c6427cc6-newsmast-1024x772.jpg)

虽然 Newsmast 基本上是 Mastodon 的一个扩展，但我曾在 FediForum 上看到的一些新的 fediverse 应用程序正在构建前所未有的全新事物。一个例子是 [Emissary](https://emissary.social/)，由来自科罗拉多的 Ben Pate 在第二天演示。Emissary 尚未公开发布，但它被描述为“一个独立的 Fediverse 服务器，专为最终用户、应用程序创建者和托管管理员设计——它为每个人提供了加入社交网络的强大新方式”。

在演示中，Pate 展示了如何关注来自各种开放网络协议的提要——ActivityPub、RSS 和 IndieWeb 格式，如微格式和 webmentions。让我感兴趣的是，它似乎可以轻松地互连所有这些不同的但开放的标准协议。它就像一个提要阅读器，允许你关注来自 Mastodon、Threads、Bluesky、博客等平台的人。

Emissary 也具有 [开发者](https://emissary.dev/developers) 吸引力。根据 [文档](https://github.com/EmissarySocial/emissary?tab=readme-ov-file)，开发者可以使用基于“HTML 模板和 JSON 配置文件”的低代码环境“创建易于部署和维护的功能齐全的社交应用程序”。开源技术栈非常有趣：Go、MongoDB、HTMX/Hyperscript。

![](https://cdn.thenewstack.io/media/2024/03/f6778a86-emissary-1024x737.jpg)

另一个在 FediForum 上引起我注意的项目是 IFTAS FediCheck，这是一个由 [Emelia Smith](https://hachyderm.io/@thisismissem) 演示的“Moderation-as-a-Service”工具。该服务仍在开发中，将允许 Mastodon 服务器管理员订阅“CARIAD”（共识聚合可撤销 IFTAS 允许拒绝列表），并让 IFTAS FediCheck 自动维护它们。这有望成为 [Mastodon 管理员](https://thenewstack.io/what-its-like-to-run-a-mastodon-server-in-the-musk-twitter-era/) 急需的审核服务，其中许多管理员都是兼职（且基本上无偿）运行实例的。

NodeBB（开源论坛软件）的联合创始人 [Julian Lam](https://mastodon.social/@julian@community.nodebb.org/112129270034316415) 评论说：“由于正在开发中，IFTAS FediCheck 仅限于 Mastodon，但对更广泛的 fediverse 应用程序网络（包括 NodeBB）有巨大的好处。”

## Fediverse 开发者网络

英国开发者 Andy Piper 在第二天主持了一场关于新兴的联邦宇宙开发者网络的会议。他首先将其与 Mozilla 开发者网络 (MDN) 进行了比较。

“它有点像网络标准、网络 API 等内容的一站式商店，”Piper 在谈到 MDN 时说。“如果开发者拥有一项资源，用于构建新服务以与联邦宇宙集成，那不是很好吗？”他指出，联邦宇宙不仅仅是 ActivityPub，还提到了 ActivityStreams、HTTP 签名和 Webfinger 等其他相关技术。

![](https://cdn.thenewstack.io/media/2024/03/07600fd1-fedidevs_diagram-1024x631.png)

联邦宇宙开发者网络旨在提供资源库并为开发者提供指导。除了技术方面之外，该小组的另一个“核心概念”只是让其他人提出想法。

![](https://cdn.thenewstack.io/media/2024/03/d3240a9e-fedidevs_coreconcepts-1024x747.png)

该小组有一个[网站](https://fedidevs.org/)、[GitHub 项目](https://github.com/fediverse-devnet)、[Mastodon 实例](https://mastodon.social/@fedidevs) 和 [Matrix 论坛](https://matrix.to/#/#fediverse-developer-network:matrix.org)（类似于 Discord 小组）。

## FediForum 上大多是积极的氛围

总体而言，为期两天的 FediForum 展示了不断壮大的联邦宇宙社区的热情。我确实感觉到社区对 Meta 即将进入联邦宇宙感到有点不安，但除此之外，对于正在开发的新应用程序和服务，大家都很兴奋。

FediForum 由联邦宇宙企业家 Johannes Ernst、非会议专家 Kaliya Young 和活动制作人 Jennifer Holmes 组织。这是该团队的第三次活动，紧随去年 3 月和 9 月的类似非会议之后。

创新的步伐如此之快，在下一届 FediForum 活动之前，看看会构建哪些应用程序，这将是一件很有意思的事情。正如 [Ernst 在 Mastodon 上评论的那样](https://mastodon.social/@J12t@social.coop/112124112942357119)，"显然，FediForum 现在是联邦宇宙中的时间衡量标准。"
