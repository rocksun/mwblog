
<!--
title: KubeCon24：Prometheus的轻量级替代方案VictoriaMetrics
cover: https://cdn.thenewstack.io/media/2024/03/8c760a6d-victoria.metrics.png
-->

此可观测性软件包背后的开源团队以其简单性和易扩展性为荣。

> 译自 [KubeCon24: VictoriaMetrics' Simpler Alternative to Prometheus](https://thenewstack.io/kubecon24-victoriametrics-simpler-alternative-to-prometheus/)，作者 Joab Jackson。

KubeCon 与会者：对云原生可观测性工具的价格和/或复杂性不满意？请到 H21 展位详细了解 [VictoriaMetrics](https://victoriametrics.com/about-us/)。

[VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics) 是一款开源监控程序包和相关时间序列数据库，在 Apache2 许可证下开源。该软件同时提供指标和日志记录功能，目前正在努力完成可观测性三要素的[最后一块](https://thenewstack.io/chronospheres-calyptia-buy-completes-observability-trinity/)：跟踪。

该公司还提供该软件的商业版本，[VictoriaMetrics Enterprise](https://victoriametrics.com/products/enterprise/trial/)。

本周，该公司推出了一项新功能，[VictoriaMetrics 异常检测](https://positivemarketing-dot-yamm-track.appspot.com/2j-0aTiw8TdLK_4frorYuNBuMtTTBq9HsaYlshpo6GQTT4O1VjgFK5t41H84IEORdcQbMVXMrELDpzaSDnVZhnnDW24ySC06zZN_siDBe5R5gMvgcoHdcSpBYkBhesfHyPmxwsV5gV0F8BPNnrn2IeizkAzzi1W-8ji-UaSVL7r4HYSb5-vfJh6Zo1b_LWLIU6x1-KbnYohxSBa3AHhzU2CN1oU4PwzML6g)，它使用机器学习来降低警报中的误报率。

尽管知名度不如 Prometheus，但该技术已悄然积累了其忠实用户，包括 [Adidas](https://docs.victoriametrics.com/casestudies/?_gl=1*rvy1qr*_ga*MTU1OTY4MjY1My4xNzEwOTQ2NDIz*_ga_N9SVT8S3HK*MTcxMDk1ODIyNS40LjEuMTcxMDk2MjI2MS41NS4wLjA.#adidas)、[Grammarly](https://www.grammarly.com/blog/engineering/monitoring-with-victoriametrics/)、[Wix](https://docs.victoriametrics.com/casestudies/#wixcom) 和 [CERN](https://docs.victoriametrics.com/casestudies/#cern)。

“我们的使命是提供一款经济高效、可靠且可扩展的监控产品，”VictoriaMetrics 联合创始人 [Roman Khavronenko](https://github.com/hagen1778) 在接受 The New Stack 采访时表示。

## VictoriaMetrics 能否取代 Prometheus？

[云原生可观测性](https://thenewstack.io/observability/) 是一个竞争激烈的领域，开源 [Prometheus](https://thenewstack.io/know-the-hidden-costs-of-diy-prometheus/)/ [Grafana](https://thenewstack.io/grafana-seeks-to-correct-observabilitys-historic-terrible-job/) 监控堆栈在这个新兴市场备受关注。

VictoriaMetrics 提供了，用 Khavronenko 的话说，[更简单的替代品](https://thenewstack.io/victoriametrics-offers-prometheus-replacement-for-timeseries-monitoring/) 来替代 Prometheus。

“关键差异在于简单性和成本效益，”Khavronenko 说。“当人们从 Prometheus 迁移时，资源使用量会减少三到四倍。”

使用相同的协议，VictoriaMetrics 可以作为 Prometheus 的直接替代品。但 Prometheus 只能在单个服务器上运行。相比之下，VictoriaMetrics 虽然也是[单个二进制文件](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest)，但也可以 [在集群中运行](https://docs.victoriametrics.com/Cluster-VictoriaMetrics.html)。

VictoriaMetrics 可用于[长期存储](https://github.com/VictoriaMetrics/VictoriaMetrics#prometheus-setup) Prometheus。它可以用作 Grafana 中 Prometheus 的 [直接替代品](https://github.com/VictoriaMetrics/VictoriaMetrics#prometheus-querying-api-usage)，以及 [Graphite](https://grafana.com/oss/graphite/) 的 [直接替代品](https://github.com/VictoriaMetrics/VictoriaMetrics#graphite-api-usage)，后者是 Prometheus 的默认时间序列数据库。

## VictoriaMetrics 提供了哪些优势？

该软件于 2018 年为一家互联网广告经纪公司创建，由 [Aliaksandr Valialkin](https://github.com/valyala) 编写，他现在是 VictoriaMetrics 的首席技术官。最初，这家广告技术公司使用 Prometheus，但很快遇到了可扩展性问题。最初，Valialkin 向 [Prometheus 项目](https://prometheus.io/)提交了错误报告，但响应速度不符合他的要求。因此，他最终辞去了公司职务，并致力于开发新的监控软件，并在几个月内在 GitHub 上发布了概念验证。不久之后，第一个付费客户出现了，于是公司成立了。

Khavronenko 自豪地表示，公司高管吹嘘的性能改进主要来自卓越的工程。Prometheus 和 VictoriaMetrics 都是[用 Go 语言编写](https://thenewstack.io/what-made-golang-so-popular-the-languages-creators-look-back/)。Valaialkin 是 [Go](https://thenewstack.io/learn-the-go-programming-language-start-here/) 的常客，因此熟悉[该编程语言](https://thenewstack.io/golang-co-creator-rob-pike-what-go-got-right-and-wrong/)的内部结构。

该公司一直是简单性的坚定支持者。

“人们喜欢把事情复杂化。他们总是这样做，用软件、用协议，甚至用基本解决方案。这是这个行业的一大弊端，”Khavronenko 说。“所以我们的做法是尽量保持简单。当它简单时，它就是可靠的。而且更容易理解发生了什么，也更容易扩展。”
