
<!--
title: 现代可观测性圆桌会议：人工智能、不断上涨的成本和 OpenTelemetry
cover: https://cdn.thenewstack.io/media/2025/06/818b9c8e-om-kamath-5kr1hbdpc5y-unsplash-scaled.jpg
summary: 可观测性成本飙升？专家热议AI驱动下，如何平衡复杂性与成本。OpenTelemetry作为CNCF关键项目，在日志和网络领域仍需发力。未来SRE工具包中，AI解决方案将成标配，但社会技术系统的重要性不容忽视。
-->

可观测性成本飙升？专家热议AI驱动下，如何平衡复杂性与成本。OpenTelemetry作为CNCF关键项目，在日志和网络领域仍需发力。未来SRE工具包中，AI解决方案将成标配，但社会技术系统的重要性不容忽视。

> 译自：[The Modern Observability Roundtable: AI, Rising Costs and OpenTelemetry](https://thenewstack.io/the-modern-observability-roundtable-ai-rising-costs-and-opentelemetry/)
> 
> 作者：Adam LaGreca

“可观测性”这个术语是否仍然有效？ 当它在 2017 年左右首次进入常用语时，它在区分自身与传统基础设施和应用程序监控方面具有指导意义。 早在应用程序更加静态的时候，SRE 就会在其关键应用程序上设置“监视器”，并在超过某些阈值时收到警报，例如，不希望出现的 CPU 峰值、面向客户的延迟问题，甚至整个服务都已离线。

但是，现代可观测性解决方案试图解锁的是实时询问我们的系统的能力，而无需预先定义可能出现的问题。 因为在微服务的分布式世界中，根本不可能在所有重要事物上设置监视器；我们需要有能力处理意外情况并做出相应的反应。

鉴于各种可观测性解决方案的成功（Datadog 于 2019 年首次公开募股，Lightstep 于 2021 年被 ServiceNow 收购），许多初创公司和大型企业都采用了可观测性这个术语，使其成为任何可以提供对您的数字业务某种洞察力的解决方案的统称。

所以我与可观测性领域一些最受尊敬的思想领袖坐下来，询问了一些棘手的问题。

*   [Paige Cruz](https://www.linkedin.com/in/paigerduty/)，[Chronosphere](https://chronosphere.io/)的首席开发者倡导者。
*   [Severin Neumann](https://www.linkedin.com/in/severinneumann/)，[Causely](https://www.causely.ai/)的社区和开发者关系主管。
*   [Shahar Azulay](https://www.linkedin.com/in/shahar-azulay-54156bb4)，[groundcover](https://www.groundcover.com/)的首席执行官兼联合创始人。
*   [Avi Freedman](https://www.linkedin.com/in/avifreedman/)，[Kentik](https://www.kentik.com/)的首席执行官兼联合创始人。
*   [Charity Majors](https://www.linkedin.com/in/charity-majors/)，[Honeycomb](https://www.honeycomb.io/)的首席技术官兼联合创始人。

## 可观测性仍然是一个合适的术语吗？

正如团队不一定想要更多工具一样，他们也不一定想要新术语。 许多公司仍然缺乏基本的监控，这为大多数企业[改进其可观测性](https://thenewstack.io/the-new-face-of-data-quality-anomalo-and-automated-monitoring/)实践留下了相当大的空间。 因此，虽然考虑进一步区分（例如*可理解性*和*可控性*）很有趣，但随着实践和平台不断发展，这里的小组似乎达成共识，即可观测性仍然是一个术语和实践。

## 客户的成本是否过高？

人们一致认为，可观测性的成本是一个合理的担忧。 在人工智能的推动下，现代应用程序正以前所未有的速度变得更加复杂，因此，随着复杂性的增加，[运营成本的扩大](https://thenewstack.io/can-companies-really-self-host-at-scale/)对于许多企业来说可能变得难以承受。 也就是说，细微之处在于价值是否与成本成正比。 通常，成本在增加，但用户体验却在恶化。 圆桌会议讨论了解决此问题的不同方案，从改进采样到新的自带云 (BYOC) 实践，该实践使客户能够存储其数据，同时保持 SaaS 体验。

## OpenTelemetry 对现代可观测性至关重要吗？

OpenTelemetry 是云原生计算基金会 (CNCF) 中仅次于 Kubernetes 的第二大最活跃的开源项目。 有趣的是，许多 Kubernetes 用户仍然更喜欢 Prometheus，至少对于指标而言是这样。 因此，虽然该小组一致支持开放的[可观测性标准](https://thenewstack.io/chronosphere-nudges-observability-standards-toward-maturity-prometheus/)遥测的想法，但 OTel 在执行方面仍有很大的增长空间，尤其是在日志记录和网络等领域。

## 人工智能将如何影响可观测性的未来？

整个小组当然希望避免 2017 年 AIOps 的过度承诺。 也就是说，人工智能驱动的开发正在以比以往更快的速度发展，并且小组中的一些人甚至说，在 IT 管理方面将人类*排除在循环之外*是一种合理的可能性。 小组中的其他人更坚持[围绕社会技术系统重要性的传统信息传递](https://thenewstack.io/werner-vogels-6-lessons-for-keeping-systems-simple/)，即使机器承担更多责任，也要让人类参与其中。 我认为可以公平地说，就目前而言，在性能和可靠性工程方面，人类不会很快消失……但利用人工智能解决方案肯定会成为任何现代 SRE 工具包的一部分。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。 订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
[The New Stack on YouTube](https://youtube.com/thenewstack?sub_confirmation=1)