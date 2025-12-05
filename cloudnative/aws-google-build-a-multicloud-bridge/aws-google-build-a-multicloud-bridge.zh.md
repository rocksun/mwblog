针对长期以来被认为是阻碍系统跨越[多个云服务](https://thenewstack.io/consider-making-shift-toward-multi-cloud/)的障碍，[亚马逊云科技](https://aws.amazon.com/?utm_content=inline+mention)和[谷歌云](https://cloud.google.com/?utm_content=inline+mention)共同开发了一项标准，客户可以轻松地通过[第 3 层](https://thenewstack.io/how-to-decide-between-a-layer-2-or-layer-3-network/)连接来桥接他们的云部署。

根据两家公司说法，其理念是让在两个云中都有云操作的客户能够通过私有网络将它们连接起来，从而减轻维护多云连接的负担，甚至可能消除对云锁定（cloud lock-in）的担忧。

[两家公司在新闻稿中表示](https://cloud.google.com/blog/products/networking/aws-and-google-cloud-collaborate-on-multicloud-networking)，这种便捷的连接甚至可能促使客户创建更多的多云应用程序。

开放源代码的 [Connection Coordinator API](https://github.com/aws/Interconnect) 规范基于 [OpenAPI 3.0](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/) 构建，并经过定制，旨在轻松配置两个云提供商之间的专用带宽。这两家云巨头也希望其他云提供商使用该 API。

AWS 在其目前处于预览阶段的 [AWS Interconnect – multicloud](https://aws.amazon.com/interconnect/) 服务中实现了该规范。谷歌云也在其 [Google Cloud 的跨云互连（Cross-Cloud Interconnect）](https://cloud.google.com/hybrid-connectivity#multicloud-networking-connectivity)中做了同样的事情。根据 AWS 网站，两家公司都承诺“持续监控以主动检测和解决问题”。

谷歌和 AWS 之间的专线将基于 [MACsec 加密](https://www.juniper.net/documentation/us/en/software/junos/security-services/topics/topic-map/understanding-macsec.html)构建。

## 多云面临的问题

迄今为止，构建跨多个云或希望在多个云上运行系统的客户有多种选择，每种选择都有其自身的痛点。

他们可以通过公共互联网在云之间进行连接，但这种方式在满足任何形式的实际[服务水平协议 (SLA)](https://thenewstack.io/ignoring-slas-doesnt-pay/) 方面，性能是极不可预测的。

或者他们可以配置连接各云的专线，但这并不便宜，而且通常需要漫长的等待时间来配置线路本身。

或者他们可以自己构建专线，这将需要大量的网络工程人才。

## 连接服务承诺的便捷性

AWS 将其服务定义为完全托管，并通过 AWS 管理控制台、命令行界面或 API 提供接口。

要配置私有网络，用户必须（用 AWS 的话来说）：

* *指定目标云服务提供商*
* *选择另一侧的目标区域*
* *选择所需的带宽*

[![](https://cdn.thenewstack.io/media/2025/12/f7c36173-2-simplifying_cross-cloud_connectivity.gif)](https://cdn.thenewstack.io/media/2025/12/f7c36173-2-simplifying_cross-cloud_connectivity.gif)

来源：Google

## 多云能实现什么

谷歌表示，这项服务的简洁性是革命性的，因为它的易用性将鼓励更多用户考虑如何跨多个云进行操作。

在一篇博客文章中，两位谷歌工程师[提供了](https://cloud.google.com/blog/products/networking/extending-cross-cloud-interconnect-to-aws-and-partners)组织可以利用多云连接的多种方式。

一个显而易见的用途是灾难恢复。应用程序可以在两种服务上运行，代理式 AI 应用程序或数据库副本能够快速同步状态。因此，如果一个[云服务宕机](https://thenewstack.io/a-cascade-of-failures-a-breakdown-of-the-massive-aws-outage/)，另一个可以迅速接管。

或者，用户可以在 AWS 上构建一个服务，该服务调用在谷歌云上运行的服务，例如托管在 BigQuery 中的关键数据仓库。

这也可以反向操作。谷歌云分析应用程序可以从 AWS S3 或 RDS 实例中拉取大型数据集。

工程师们写道，在每种情况下，多云应用程序都将受益于性能的提升。并且不通过公共互联网路由这些流量也将带来安全优势。

## 其他连接方式

微软 Azure 未参与本周的公告，但它已提供 [Azure ExpressRoute](https://azure.microsoft.com/en-us/products/expressroute) 和 [Azure Virtual WAN](https://azure.microsoft.com/en-us/products/virtual-wan) 作为将 Azure 与其他云提供商或本地设施连接的方式。

其他可以通过自己的数据中心完成这项工作的第三方云交换服务包括 [Equinix Cloud Exchange](https://www.equinix.com/products/digital-infrastructure-services/equinix-fabric)、[CoreSite Open Cloud Exchange](https://www.coresite.com/cloud-networking/open-cloud-exchange) 和 [Digital Realty 的 Interconnection Fabric](https://www.digitalrealty.com/platform-digital/connectivity)。

AWS 在其年度 [AWS Re:Invent 大会](https://thenewstack.io/amazon-cto-werner-vogels-predictions-for-2026/)的开幕式上宣布了这部分消息，该会议本周在拉斯维加斯举行。