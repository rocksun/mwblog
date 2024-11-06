*社区帖子最初由 Dotan Horovits 在 Medium 上发布*
## TL;DR 关键更新：
* 重大变更和 OpenTelemetry 兼容性
* **Prometheus UI 改头换面**
* 远程写入 2.0 和 OpenMetrics 存档
* **新的治理：让 Prometheus 更具包容性**
* 原生直方图和性能改进。
* Prometheus 生态系统更新：Thanos、Perses 等

PromCon Europe 2024 刚刚在柏林落下帷幕，今年的活动规模很大。不仅因为 Prometheus 社区齐聚一堂，还因为我们迎来了期待已久的 **Prometheus 3.0 发布！**维护人员在舞台上真正按下了 3.0-Beta 的“合并”按钮！

为此，我与 Prometheus 的创建者 Julius Volz 坐下来，一起回顾了主要公告以及它们对 Prometheus 生态系统未来的意义。我将在本博客中回顾重点内容，您可以在 [OpenObservability Talks 的最新一期](https://podcasters.spotify.com/pod/show/openobservability/episodes/Prometheus-3-0-Unveiled-PromCon-Highlights-with-Julius-Volz---OpenObservability-Talks-S5E04-e2o0455) 中找到完整的炉边谈话：

## 重大版本发布：重大变更和 OpenTelemetry 兼容性
Prometheus v2 已经存在了将近 7 年，发布了 54 个次要版本。是时候进行重大版本升级了。重大版本也是软件通常会进行重大变更的时候，Julius 说这确实是这次重大版本发布的原因之一。那么，当我们从 2.x 升级到 3.0 时，是否会遇到问题？

Julius 说，好消息是，对于大多数人来说，从 2.x 升级到 3.0 时，不会出现太多问题。他说这主要是为了摆脱“旧的巧妙的东西”，主要删除了已弃用的实验性功能标志，因此大多数用户应该不会遇到任何重大变更。不用担心，Prometheus 始终保持对用户的长期向后兼容性承诺。

这次重大版本发布不仅仅是增量变更，它代表着 Prometheus 未来使用方式的转变。Julius 解释说，v3.0 的主要主题之一是 OpenTelemetry (OTel) 兼容性。这并非易事，因为 [每个项目采用的设计原则不同](https://www.linkedin.com/feed/update/urn:li:share:7233510791277142016)，例如指标命名（点或下划线？带或不带单位？）、编码（Prometheus v3 现在支持 UTF-8）、拉取与推送模式、增量与累积时间性等等。但这样做有明显的优势。

![图片](https://miro.medium.com/v2/resize:fit:700/1*5VfS9QqWV9Vm2Um355Ujcg.png)
![图片](https://miro.medium.com/v2/resize:fit:700/1*5VfS9QqWV9Vm2Um355Ujcg.png)
Prometheus 一直以其强大的指标收集功能而闻名，但随着 [支持原生 OpenTelemetry 指标](https://medium.com/p/83f85878e46a) 的推出，Prometheus 维护人员希望将其定位为 OpenTelemetry 的首选后端。这是一个战略性步骤，旨在使 Prometheus 更加互操作，并随着 OpenTelemetry 在整个行业中不断普及而变得更加面向未来。

## Prometheus UI 改头换面
我们还讨论了 *Prometheus UI* 的改造。虽然 Prometheus 一直以其后端性能和灵活性而受到人们的喜爱，但前端有时却落后了。Julius 向我们介绍了 3.0 中的新 UI（他自己开发的），它将如何提高可用性，而不会牺牲 Prometheus 用户重视的核心简洁性。它基于 Mantine，这是一个现代 React 组件库，并实现了简洁美观的外观。

新的 Prometheus UI 还提供了新的功能，包括 PromLens 风格的树视图、更好的指标资源管理器和“解释”选项卡。改进的指标资源管理器可以轻松地可视化探索指标及其标签、基数等等。树视图的灵感来自 PromLens，[PromLens 是一个最近捐赠给 Prometheus 的 PromQL 查询构建器工具](https://horovits.medium.com/fbede9b5cc9#4951)。

针对我的问题，Julius 说 Alertmanager UI 目前没有进行任何修改，他也不确定何时会进行修改。他确实确认，目标是采用相同的 UI 框架（目前甚至不是基于 React 的）以及外观和感觉，与改造后的 Prometheus UI 一致。有关新 UI 的更多信息，请查看 [Julius 的博客文章](https://promlabs.com/blog/2024/09/11/a-look-at-the-new-prometheus-3-0-ui/)。

## 远程写入 2.0 和 OpenMetrics 存档
Prometheus 3.0 的一个突出特点是 **远程写入 2.0**。远程写入格式用于将大量指标从 Prometheus 传输到分析后端。Julius 分享了有关此新版本的远程写入如何增强 Prometheus 处理长期存储的方式的见解。Prometheus 的设计初衷是进行短期、高性能的指标收集。但生态系统已经发展到可以处理 Thanos、Cortex 和 Mimir 等长期存储解决方案，这些解决方案与 Prometheus 集成在一起。
## 远程写入 2.0 和性能改进

远程写入 2.0 的重点是可靠性和效率。它大幅降低了网络中断或停机期间数据丢失的可能性，并允许将数据更好地流式传输到远程存储。对于依赖 Prometheus 进行关键监控并需要防弹数据管道的团队来说，这是一个巨大的进步。

同样重要的是暴露格式，它定义了不同组件如何暴露指标以供 Prometheus 抓取。一段时间前，这种格式被剥离到一个名为 OpenMetrics 的独立项目中，希望将其发展成为一个独立的标准。但这并没有成功，反而使 Prometheus 生态系统变得混乱。现在 [OpenMetrics 已正式归档并合并回 Prometheus](https://horovits.medium.com/openmetrics-is-archived-merged-into-prometheus-d555598d2d04)，它应该在那里。

## 本地直方图和性能改进

Prometheus 3.0 即将推出的另一个令人兴奋的功能是 [引入本地直方图](https://horovits.medium.com/fbede9b5cc9#aa64)。此功能显着增强了 Prometheus 处理高基数数据的性能，使其更轻松地管理大型数据集，而不会牺牲性能。

借助 v3.0，本地直方图现在支持乱序摄取，这解决了 OpenTelemetry 以及更广泛的网络和类似断开连接以及指标数据中的临时间隙所带来的各种场景，现在可以填补这一空白。

通过原生支持直方图，Prometheus 3.0 降低了指标聚合的复杂性，并使查询更快、更高效。这是一种幕后改进，可能不会成为头条新闻，但它将对大规模用户产生重大影响。

## Prometheus 生态系统更新：Thanos、Perses 等

我们不能不谈论 Prometheus 生态系统。Prometheus 生态系统中一个重要的开源项目是 Thanos，它为 Prometheus 提供了长期可扩展的存储。与 Cortex 和 Mimir 类似，Thanos 正在引入原生多租户支持，允许从不同的租户发送数据，然后按租户跟踪和控制对数据的访问。

Thanos 另一个有趣的进展是分布式查询执行，它通过将部分处理推送到叶节点（以中心辐射式或 MapReduce 方式）来提高查询性能。

在可视化方面，今年 PromCon 推出的一个有趣的进展是 [Perses 项目，它最近加入了 CNCF](https://horovits.medium.com/unveiling-perses-the-gitops-friendly-metrics-visualization-tool-f05b5324d7da)。Julius 暗示，虽然 Grafana 一直是许多人的默认选择，但 Perses 提供了一种轻量级、原生于 Prometheus 的仪表板体验，具有 GitOps 功能和基础的开源理念。Perses 仍处于早期阶段，但随着它的发展，值得关注。

## 新的治理：让 Prometheus 更具包容性

随着 Prometheus 的不断发展，治理模式也发生了变化。我们提到了该项目向更 **正式的治理结构** 的转变，降低了人们参与的门槛，并使贡献者更容易在项目中获得关键职位，并共同努力塑造 Prometheus 的未来。此举与其他 CNCF 项目一致，这些项目在成熟时都采用了更结构化、分层、透明的治理模式。

Julius 指出，由于 Prometheus 现在被无数组织使用，因此确保对其方向的决策具有包容性非常重要。新的治理框架将提供更多层级，并赋予更广泛的社区更多责任、问责制和权限，最终影响路线图，同时保持使 Prometheus 成为可观察性领域基石的高标准。

## 展望未来：Prometheus 和生态系统的未来

PromCon 充满了更新，例如 Prometheus 配置的自动重新加载、正则表达式和查询功能、新的服务发现管理器以及代理模式达到稳定状态，我们无法在这里全部涵盖。

[3.0 Beta 版已发布](https://github.com/prometheus/prometheus/releases/tag/v3.0.0-beta.0)，欢迎您试用并查看发行说明。根据 Prometheus 维护者在 PromCon 之后举行的 DevSummit 的结果，Prometheus 3.0 GA 版本预计将在 2024 年 11 月的 KubeCon 北美大会上发布。

在我们结束讨论时，Julius 強调，虽然 Prometheus 3.0 是一个巨大的里程碑，但工作远未结束。该团队已经展望未来，包括改进可扩展性、与 OpenTelemetry 的更深层次集成以及持续增强整体用户体验。
PromCon Europe 2024 reminded us how far Prometheus has come. With the release of Prometheus 3.0, the project is poised to continue being a dominant force in the observability ecosystem for years to come.

Want to learn more? Check out the OpenObservability Talks program: *Prometheus 3.0 Unveiled: PromCon Highlights with Julius Volz*