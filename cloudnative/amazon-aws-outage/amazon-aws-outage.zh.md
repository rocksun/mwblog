一次大规模故障正在影响亚马逊网络服务 (AWS)，甚至亚马逊自己的网页据报道也已下线，数十个其他在线服务和网站受到影响，其中包括英国的中断。

AWS 在太平洋夏令时上午 12:11（世界协调时 7:11）向其[健康仪表板](https://health.aws.amazon.com/health/status)报告了 US-EAST-1 区域（即亚马逊在北弗吉尼亚州的本土区域）多个服务的错误率和延迟增加的问题。

太平洋夏令时上午 1:26（世界协调时 8:26），这家云业务公司表示，对该区域 DynamoDB 端点发出的请求存在显著错误率，这正对其他 AWS 服务产生连锁反应。

[![](https://pubads.g.doubleclick.net/gampad/ad?co=1&iu=/6978/reg_offprem/paasiaas&sz=300x50%7C300x100%7C300x250%7C300x251%7C300x252%7C300x600%7C300x601&tile=2&c=2aPd3FM9Cp2NVUilXiMxH0gAAA9I&t=ct%3Dns%26unitnum%3D2%26raptor%3Dcondor%26pos%3Dtop%26test%3D0)](https://pubads.g.doubleclick.net/gampad/jump?co=1&iu=/6978/reg_offprem/paasiaas&sz=300x50%7C300x100%7C300x250%7C300x251%7C300x252%7C300x600%7C300x601&tile=2&c=2aPd3FM9Cp2NVUilXiMxH0gAAA9I&t=ct%3Dns%26unitnum%3D2%26raptor%3Dcondor%26pos%3Dtop%26test%3D0)

太平洋夏令时上午 2:01（世界协调时 9:01），亚马逊的技术人员确定了错误率的潜在根本原因，称其似乎与 DynamoDB API 端点的 DNS 解析有关，并且他们正在通过多条并行路径加速恢复。

该公司警告称，依赖 US-EAST-1 端点的全球服务或功能，例如 IAM（身份和访问管理）更新和 DynamoDB 全局表，可能也正在经历问题。

这似乎是一种保守说法，因为由于北弗吉尼亚州的问题，数十个网站和服务仍然不可用。名单包括 McDonald's、DisneyPlus、Snapchat、[Signal](https://x.com/mer__edith/status/1980182701610348654)、Roblox、Verizon、Fortnite、Venmo、Perplexity、Hulu、Duolingo、Perplexity、Reddit 和 Coinbase。甚至[Amazon.com 也一度下线](https://x.com/sqs/status/1980185380566753735)，一些用户还报告说他们的 Alexa 智能音箱和 Ring 门铃也停止工作了。

[![](https://pubads.g.doubleclick.net/gampad/ad?co=1&iu=/6978/reg_offprem/paasiaas&sz=300x50%7C300x100%7C300x250%7C300x251%7C300x252%7C300x600%7C300x601&tile=4&c=44aPd3FM9Cp2NVUilXiMxH0gAAA9I&t=ct%3Dns%26unitnum%3D426raptor%3Dfalcon%26pos%3Dmid%26test%3D0)](https://pubads.g.doubleclick.net/gampad/jump?co=1&iu=/6978/reg_offprem/paasiaas&sz=300x50%7C300x100%7C300x250%7C300x251%7C300x252%7C300x600%7C300x601&tile=4&c=44aPd3FM9Cp2NVUilXiMxH0gAAA9I&t=ct%3Dns%26unitnum%3D4%26raptor%3Dfalcon%26pos%3Dmid%26test%3D0)

银行，甚至一些政府网站也受到了影响，以及 Signal 和 WhatsApp 等通信应用程序。

在大西洋彼岸的英国，许多服务都已瘫痪，Lloyds Banking Group 的应用程序和网站无法访问，而一些英国政府服务也面临困境，其中包括 HMRC。

[![](https://pubads.g.doubleclick.net/gampad/ad?co=1&iu=/6978/reg_offprem/paasiaas&sz=300x50%7C300x100%7C300x250%7C300x251%7C300x252%7C300x600%7C300x601&tile=4&c=44aPd3FM9Cp2NVUilXiMxH0gAAA9I&t=ct%3Dns%26unitnum%3D426raptor%3Dfalcon%26pos%3Dmid%26test%3D0)](https://pubads.g.doubleclick.net/gampad/jump?co=1&iu=/6978/reg_offprem/paasiaas&sz=300x50%7C300x100%7C300x250%7C300x251%7C300x252%7C300x600%7C300x601&tile=4&c=44aPd3FM9Cp2NVUilXiMxH0gAAA9I&t=ct%3Dns%26unitnum%3D4%26raptor%3Dfalcon%26pos%3Dmid%26test%3D0)

我们请亚马逊置评，但它将我们转介到[健康仪表板](https://health.aws.amazon.com/health/status)，该仪表板表示公司将在有更多信息可分享时继续提供更新。®