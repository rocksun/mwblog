<!--
title: 分叉五年后，OpenSearch 正逐渐走出 AWS 的阴影
cover: https://cdn.thenewstack.io/media/2026/10/e88d1014-aws-hero.jpg
summary: 分叉五年并转交 Linux 基金会治理后，OpenSearch 正在减少对 AWS 的依赖，代码贡献和自管部署均有所增长，并通过拥抱企业 AI 基础设施加速拓展市场。
-->

分叉五年并转交 Linux 基金会治理后，OpenSearch 正在减少对 AWS 的依赖，代码贡献和自管部署均有所增长，并通过拥抱企业 AI 基础设施加速拓展市场。

> 译自：[Five years after the fork, OpenSearch is slowly stepping out of AWS’s shadow](https://thenewstack.io/opensearch-foundation-aws-elasticsearch/)
> 
> 作者：Paul Sawers

**OpenSearch 已经走过了漫长的道路**。早在 2021 年 1 月，亚马逊云科技（AWS）首次[宣布了该项目](https://aws.amazon.com/blogs/opensource/stepping-up-for-a-truly-open-source-elasticsearch/)，以回应[Elastic 决定将 Elasticsearch](https://www.elastic.co/blog/licensing-change) 及其配套的可视化工具 [Kibana](https://www.elastic.co/lp/kibana) 从 Apache 2.0 许可证转为专有和源码可用（source-available）相结合的许可证。Elastic 当时表示，此举是为了防止像 AWS 这样的云巨头在不作任何回馈的情况下将 Elasticsearch 作为“服务”提供，同时还指责 AWS [侵犯了 Elasticsearch 商标](https://www.elastic.co/blog/elastic-and-amazon-reach-agreement-on-trademark-infringement-lawsuit)。

尽管 Elastic 随后通过将 AGPL 添加为许可证选项，[将 Elasticsearch 和 Kibana 重新带回开源](https://thenewstack.io/whats-behind-elastics-unexpected-return-to-open-source/)，并[在此过程中与 AWS 重归于好](https://venturebeat.com/business/once-frenemies-elastic-and-aws-are-now-besties)，但 OpenSearch 一直作为独立的开源项目开辟自己的道路——尽管它仍然与创造它的这家科技巨头紧密相连。

## 减少对 AWS 的依赖

2024 年 9 月迎来了重大里程碑，当时 [AWS 将 OpenSearch 移交给 Linux 基金会](https://thenewstack.io/aws-transfers-opensearch-to-the-linux-foundation/)，成立了 OpenSearch 软件基金会，将该项目置于“厂商中立”的治理之下。此举旨在让其他公司更有信心为 OpenSearch 做贡献，而不必担心 AWS 对其未来保留最终控制权。

两年过去了，[OpenSearch](https://opensearch.org/) 显示出超越其最初支持者的发展势头。OpenSearch 软件基金会向 *The New Stack* 提供的数据显示，AWS 在该项目各个代码库中的贡献活动占比已从第一年的 91% 下降到 2025-26 年的 72%。与此同时，在 [2022 年 4 月](https://github.com/opensearch-project/OpenSearch/blob/a6b4967dcf39b7ff3d47aff0a75314becbce72f4/MAINTAINERS.md)，亚马逊affiliated 工程师占核心 OpenSearch 代码库维护者的 95%，而如今这一比例为 71%。

这种转变在组织部署软件的方式中也清晰可见。在 Linux 基金会和 OpenSearch 软件基金会上个月发布的《*[2026 年开放数据基础设施报告](https://www.linuxfoundation.org/research/opensearch-data-infrastructure-2026)*》中，数据显示自 2024 年以来，自管部署（self-managed deployments）的增长速度快于亚马逊托管的 OpenSearch 服务。约 60% 的受访 OpenSearch 用户现在在云中运行自管部署，高于 2024 年的 37%，而亚马逊托管服务的使用量增长较为温和，从 44% 上升到 48%。

然而，AWS 历史上与 OpenSearch 的关联对一些潜在用户来说仍然是一个障碍。根据该报告，在 71 名受访的非采纳者中，近四分之一（24%）的人将对该项目的厂商中立性以及与 AWS 的历史联系的担忧作为保持观望的原因。

这些数字指出单靠治理变更无法解决的挑战：说服潜在用户和贡献者，OpenSearch 的未来不再主要由 AWS 决定。

## OpenSearch 的“分水岭时刻”

*The New Stack* 本月在布拉格举行的 [欧洲开源峰会](https://events.linuxfoundation.org/open-source-summit-europe/) 上采访了 OpenSearch 软件基金会执行董事 [Bianca Lewis](https://www.linkedin.com/in/biancalewis/)，讨论了该项目超越其 Elasticsearch 起源的演变，包括任何挥之不去的 AWS 影响力的看法。

Lewis 认为，两多年前实现的法律独立性，为建立这种信任提供了重要的基础。

> “当他们把它捐给 Linux 基金会时，那是一个分水岭时刻。”

Lewis 告诉 *The New Stack*：“当他们把它捐给 Linux 基金会时，那是一个分水岭时刻。”“因为他们无法关闭 OpenSearch，也无法更改许可证。他们不再拥有这个应用程序了。”

Lewis 还暗示，这一决定对 AWS 来说具有商业意义，其云业务通过运行应用程序所使用的计算资源产生收入，而不一定是通过拥有应用程序本身产生收入。

她说：“AWS 不靠应用程序赚钱。AWS 靠算力赚钱。因此，长期运营和发展 OpenSearch 从来都不是 AWS 计划的一部分。”

> “AWS 不靠应用程序赚钱。AWS 靠算力赚钱。因此，长期运营和发展 OpenSearch 从来都不是 AWS 计划的一部分。”

但关于 AWS 继续发挥多大影响力的疑问依然存在。该公司仍然占 OpenSearch 代码库记录贡献活动的近四分之三。尽管 AWS 在该项目的技术指导委员会（TSC）的 15 个投票席位中只占 4 个，但一名 AWS 员工 [Andrew Ross](https://www.linkedin.com/in/andrew-ross-781ab1a/) 刚刚在 10 月再次当选委员会主席。

## OpenSearch 的 AI 机遇

虽然 AWS 的影响力在 OpenSearch 的治理中仍然显而易见，但自分叉以来，软件本身已经发生了很大变化。Lewis 毫不讳言该软件在早期与 Elasticsearch 的相似程度。

她说：“不可否认，OpenSearch 的早期版本就是换了名字的 Elasticsearch。它们有相同的插件。甚至 OpenSearch 的很多文档都是 Elasticsearch 文档。[但]当它几年前被捐赠给 Linux 基金会时，它已经真正地与其最初的母项目分道扬镳了。”

今天，OpenSearch 将自己定位为需要搜索、分析和检索数据的应用程序的基础设施，包括那些围绕大语言模型（LLMs）构建的应用程序。例如，它对向量和混合搜索的支持使其与检索增强生成（RAG）相关，在 RAG 中，AI 应用程序从外部源检索信息以补充模型的响应。

该项目的最新版本 OpenSearch 3.9 [于 9 月首次亮相](https://opensearch.org/blog/get-to-know-opensearch-3-9/)，在这些功能的基础上进行了改进，旨在帮助开发者搜索和检索 AI 应用程序的信息，同时更新了性能、监控和警报功能。

Lewis 相信这为 OpenSearch 成为企业 AI 基础设施的核心组件创造了机遇。

她说：“如果你决定将 AI 基础设施建立在开放平台上，我认为今天的 [OpenSearch] 就是默认选择。”

## 赢得企业市场

雄心是一回事。将这些雄心转化为长期的企业采用则是完全另外一回事。基金会的报告表明，很大一部分 OpenSearch 部署仍处于实验阶段，组织仍在评估该技术或将其用于可以被替换的应用程序。

当被问及此事时，Lewis 指出了公司摆脱既定商业平台所需的时间，特别是当它们受到多年期许可证协议束缚时。

她说：“他们可能与 Splunk 签了三年合同，与 Elastic 签了五年许可证。所以他们不会直接把它扔掉。”

换句话说，企业可能在测试 OpenSearch 的同时继续使用他们已经付费的产品。当然，并不能保证这些评估会带来永久性的部署。

Lewis 认为，组织最终可能转用该平台的一个原因是拥有更改技术提供商的自由，而无需重新构建其应用程序。

> “如果我被锁定怎么办？如果我被锁定又想离开，那会是什么样子？我必须重新架构我所有的应用程序吗？”

她说：“如果我被锁定怎么办？如果我被锁定又想离开，那会是什么样子？我必须重新架构我所有的应用程序吗？”

这种担忧超越了许可证成本。企业还必须考虑更换供应商、移动数据以及随时间维护应用程序所涉及的工程工作。

这一切又将讨论带回了关于 OpenSearch 独立性的问题。如果组织选择该平台的部分原因是为了避免对单个供应商的依赖，那么该项目吸引和留住 AWS 以外贡献者的能力就显得尤为重要。

当被问及她希望五年后的 OpenSearch 会是什么样子时，Lewis 回到了供应商影响力的问题——以及她对一个没有任何单一公司主导的项目的雄心。

她说：“拥有一个真正可持续、快速创新的平台，且不受世界上任何单一供应商的主导或严重影响。那么，你就拥有了一个稳定的平台。”