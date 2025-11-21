2025年11月18日，[Cloudflare](https://www.cloudflare.com/) 经历了一次长达数小时的[重大宕机](https://apnews.com/article/cloudflare-outage-x-openai-9335e8e0da2a0027d1fbac5eb97d11ae)，导致全球众多热门网站和在线服务无法访问。这仅仅是近期一系列互联网服务提供商宕机事件中的最新一起。其他受影响的服务还包括去年10月的[亚马逊网络服务](https://thenewstack.io/a-cascade-of-failures-a-breakdown-of-the-massive-aws-outage/) (AWS) 和 [Azure](https://www.zdnet.com/article/massive-azure-outage-is-over-but-problems-linger-heres-what-happened/)。我们对少数几家云服务和网络服务公司的过度依赖，正变得痛苦不堪。

然而，这并非单一原因。就[AWS](https://aws.amazon.com/?utm_content=inline+mention) 而言，最终是——是的，你懂这个故事——一次[域名系统](https://thenewstack.io/13-years-later-the-bad-bugs-of-dns-linger-on/) (DNS) 的错误配置；而 Azure 的故障则是由于一次错误的配置更改。至于[Cloudflare，其根本原因是一个数据库系统的权限配置错误](https://blog.cloudflare.com/18-november-2025-outage/)。这导致 Shopify、Amazon 和 Robox 等热门网站和服务出现故障，并且几乎所有的 AI 聊天机器人，如 ChatGPT、Perplexity 和 Anthropic Claude，都无法正常运行。

## 根本原因：数据库权限配置错误

具体而言，此次宕机并非由网络攻击引起，而是 Cloudflare 机器人管理系统中的一个软件错误。具体来说，最近对数据库查询权限的一次更改生成了一个过大的“特征文件”，该文件被机器人管理模块使用，其中包含大量重复条目。

该文件通常是固定大小的，并且每隔几分钟就会重新生成一次，但由于这个错误，文件大小超出了预期限制，导致[机器人管理模块](https://www.cloudflare.com/application-services/products/bot-management/)反复崩溃。由于该模块是 Cloudflare 核心代理管道不可或缺的一部分，任何依赖它的流量都受到了影响，导致大范围的 5xx 错误。

## 宕机时间线和解决方案

问题始于世界协调时 (UTC) 大约 11:20，症状包括延迟升高、访问认证失败以及 Cloudflare 核心网络中出现的错误代码。最初的困惑导致一些团队怀疑是一次大规模的 DDoS 攻击，但在确定根本原因是损坏的特征文件后，这一点被迅速排除。

与此同时，许多在网上工作和娱乐的人们都遇到了麻烦。正如[思科 ThousandEyes](https://www.thousandeyes.com/) 报告的那样，虽然到 Cloudflare 前端基础设施的网络路径似乎没有出现延迟升高或丢包的情况，但[思科 ThousandEyes 观察到大量超时和 HTTP 5XX 服务器错误](https://www.thousandeyes.com/resources/internet-outages-timeline)，这表明是后端服务出现问题。具有讽刺意味的是，就连监控网络宕机本身的网站，如 Downdetector，也因为 Cloudflare 的故障而宕机。

## 宕机时间线和解决方案

Cloudflare 解释说，在幕后，该特征文件由运行在[ClickHouse 数据库集群](https://clickhouse.com/docs/architecture/cluster-deployment/)上的查询每五分钟重新生成一次，而该集群正在逐步更新以改进权限管理。因此，“每五分钟，就有可能生成一组好的或坏的配置文件，并迅速传播到整个网络。”

Cloudflare 继续说：“最终，每个 ClickHouse 节点都生成了错误的配置文件，并且波动稳定在故障状态。” 修复方法是停止“错误特征文件的生成和传播，并将一个已知的好文件手动插入到特征文件分发队列中。然后强制重启我们的核心代理。”

幸运的是，Cloudflare 的工程师相对较快地阻止了错误文件的生成和传播。到 UTC 14:24，Cloudflare 已回滚到之前稳定的版本。核心流量在 UTC 14:30 左右基本恢复正常，并在 UTC 17:06 完成了系统的全面恢复。

## 对辅助系统的级联效应

正如这类事件总是会发生的那样，一个问题引发了另一个问题。其他受影响的辅助 Cloudflare 系统也受到了影响。这包括依赖于核心代理的[Workers KV 存储](https://developers.cloudflare.com/kv/)和[Cloudflare Access](https://www.cloudflare.com/zero-trust/products/access/)，它们出现了错误率上升和登录中断。由于内部调试系统为诊断未捕获的错误而超负荷工作，导致 CPU 使用率激增，[Cloudflare 仪表板登录](https://dash.cloudflare.com/)受到严重影响，同时也拖慢了内容分发网络 (CDN) 的速度。[Turnstile](https://www.cloudflare.com/application-services/products/turnstile/)，Cloudflare 的 CAPTCHA 服务，也未能正确加载。

总而言之，主要宕机持续了大约三个小时，之后是恢复期，最后在全面修复后实现稳定。一些客户由于服务恢复时的积压和重试风暴，经历了更长的中断时间。

## Cloudflare 阻止未来宕机的承诺

展望未来，Cloudflare 已承诺采取多项措施以防止类似事件再次发生。这些措施包括：

* 加强配置文件摄入，提供类似于用户输入的验证。
* 实施全局功能开关，以快速隔离问题。
* 消除错误报告或核心转储可能耗尽资源的场景。
* 对所有核心代理模块的故障模式进行全面审查。

这些措施都很好，但这次宕机事件，以及近期其他互联网宕机事件，都凸显了当今互联网的脆弱性。诚然，外部攻击，如可能导致数百万用户全球服务中断的[TB 级分布式拒绝服务 (DDoS) 攻击](https://www.zdnet.com/article/cloudflare-blocks-largest-ddos-attack-heres-how-to-protect-yourself/)，也是一个真实存在的问题。但是，即使没有这些攻击，这些系统故障事件也引发了关于关键云基础设施系统的安全性究竟有多大的重要问题。