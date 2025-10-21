今晚在弗吉尼亚州北部某个地方，一群 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 管理员可能在经历了漫长的一天故障排除之后，正在享受一杯饮品。

周一，亚马逊网络服务（Amazon Web Services）在其 US-EAST-1 区域 [遭遇了一连串故障](https://www.aboutamazon.com/news/aws/aws-service-disruptions-outage-update)，导致包括 [AWS Lambda](https://thenewstack.io/three-reasons-why-teams-move-away-from-aws-lambda/)、Amazon API Gateway、Amazon Appflow、Amazon Aurora DSQL Service 等在内的众多云服务出现中断。

正如屡见不鲜的情况一样，罪魁祸首是 [DNS 配置错误](https://thenewstack.io/why-you-need-distributed-dns-implementation/)。真是让人费解。

在全球 15 个 AWS 区域中，US-EAST-1 可能是最大的，其 [数据中心](https://thenewstack.io/how-much-energy-is-really-being-consumed-by-data-centers/) 集群分布在 Loudoun、Prince William 和 Fairfax 县。从今天的故障来看，许多当今最大的企业在该区域至少都有业务部署。

据该公司称，AWS 目前已几乎完全恢复，客户服务积压的工作将在未来几小时内完成。依赖 AWS 的 Snapchat、Reddit、Venmo 及其他云服务也显示出恢复迹象。

## US-EAST-1 宕机始末

问题最初在东部时间凌晨 3 点左右显现，当时多项服务报告 DynamoDB API 端点的 DNS 解析错误率升高。该问题在三小时内得到报告，到早上 6 点，工作人员确信，经过一段恢复期后，服务将很快恢复全速运行。

他们在早上 6:03 [乐观地在日志中写道](https://health.aws.amazon.com/health/status)：“我们确认依赖 US-EAST-1 的全球服务和功能也已恢复。我们将继续努力全面解决问题，并在获得更多信息后提供更新。”

也就是说，几乎所有服务都恢复了。然而，在 US-EAST-1 区域启动新的 EC2 实例（或启动 EC2 实例的服务，如 ECS）的请求仍然遇到错误。最初，怀疑的罪魁祸首是陈旧的缓存，需要将其清除。

尽管两小时后启动 EC2 实例时仍然出现错误，但管理团队仍然相信他们可以轻易解决 EC2 问题。他们建议不要在将此区域指定为可用区的情况下启动实例。

更糟的是，Lambda 服务从一开始就表现不稳定，现在也开始出现严重的恢复问题。随着早晨的流逝，一连串的 AWS 服务中断困扰着管理团队。

## EC2 的更多问题

他们在上午 10:14 写道：“我们确认 US-EAST-1 区域内的多个服务出现显著的 API 错误和连接问题。”他们将问题追溯到 EC2 内部网络，该网络影响了 DynamoDB、SQS、Amazon Connect 和其他服务。

问题最终被发现是负载均衡器的监控系统给 Lambda 服务带来了压力。

东部时间下午 6:48 发布的消息指出，EC2 实例启动已恢复，但对于需要 EC2 实例启动的服务（如 Redshift）以及分析和报告数据，仍有两小时的积压工作。

## 对主要在线业务的广泛影响

尽管只有一个区域受到影响，但事实证明它对互联网上许多最大的云服务产生了深远影响。报告云服务可用性的 Downdetector 网站全天涌入了大量 AWS 服务中断报告，其中绝大多数来自 US-EAST-1 区域。

[![显示故障投诉的图表](https://cdn.thenewstack.io/media/2025/10/a03c0424-downdetector-1-aws-oct20.png)](https://cdn.thenewstack.io/media/2025/10/a03c0424-downdetector-1-aws-oct20.png)

来源：Downdetector

这反过来又给 [许多依赖](https://www.cnbc.com/2025/10/20/amazon-web-services-outage-takes-down-major-websites.html) AWS 的公司带来了问题。Downdetector 今天报告了与 AWS 相关的问题，涉及 [Snapchat](https://downdetector.com/status/snapchat/)、[Apple Music](https://downdetector.com/status/apple-music/)、[Reddit](https://downdetector.com/status/reddit/)、[Venmo](https://downdetector.com/status/venmo/)、[Doordash](https://downdetector.com/status/doordash/)、[Hulu](https://downdetector.com/status/hulu/) 以及 [Amazon](https://downdetector.com/status/amazon/) 本身。它们受影响的程度大概取决于它们对该特定区域的依赖程度。