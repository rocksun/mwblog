# KubeCon24: VictoriaMetrics’ Simpler Alternative to Prometheus
![Featued image for: KubeCon24: VictoriaMetrics’ Simpler Alternative to Prometheus](https://cdn.thenewstack.io/media/2024/03/8c760a6d-victoria.metrics-1024x683.png)
![](https://cdn.thenewstack.io/media/2024/03/9bf8a2a0-kubecon24-eu-300x206.jpg)
KubeCon/CloudNativeCon
KubeCon attendees: Unhappy with the price and/or complexity of your cloud native observability tools? Stop by booth H21 to learn more about
[VictoriaMetrics.](https://victoriametrics.com/about-us/) [VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics) is an open source monitoring package and associated time-series database, open source under an Apache2 license. The software offers both metrics and logging capabilities, with work being done to [complete the final piece](https://thenewstack.io/chronospheres-calyptia-buy-completes-observability-trinity/) of observability trinity: traces.
The company also offers a commercial version of the software,
[VictoriaMetrics Enterprise](https://victoriametrics.com/products/enterprise/trial/).
And this week, the company launched a new feature,
[VictoriaMetrics Anomaly Detection](https://positivemarketing-dot-yamm-track.appspot.com/2j-0aTiw8TdLK_4frorYuNBuMtTTBq9HsaYlshpo6GQTT4O1VjgFK5t41H84IEORdcQbMVXMrELDpzaSDnVZhnnDW24ySC06zZN_siDBe5R5gMvgcoHdcSpBYkBhesfHyPmxwsV5gV0F8BPNnrn2IeizkAzzi1W-8ji-UaSVL7r4HYSb5-vfJh6Zo1b_LWLIU6x1-KbnYohxSBa3AHhzU2CN1oU4PwzML6g), which uses machine learning to lower the rate of false positives in alerting.
Despite not being as well-known as Prometheus, the technology has quietly built up its dedicated users, counting
[Adidas](https://docs.victoriametrics.com/casestudies/?_gl=1*rvy1qr*_ga*MTU1OTY4MjY1My4xNzEwOTQ2NDIz*_ga_N9SVT8S3HK*MTcxMDk1ODIyNS40LjEuMTcxMDk2MjI2MS41NS4wLjA.#adidas), [Grammarly](https://www.grammarly.com/blog/engineering/monitoring-with-victoriametrics/), [Wix](https://docs.victoriametrics.com/casestudies/#wixcom) and [CERN](https://docs.victoriametrics.com/casestudies/#cern) as users.
“Our mission is to provide a cost-efficient, reliable and scalable product for monitoring,” said
[Roman Khavronenko](https://github.com/hagen1778), co-founder of VictoriaMetrics, in an interview with The New Stack.
## Can VictoriaMetrics Replace Prometheus?
[Cloud native observability](https://thenewstack.io/observability/) is a competitive field with the open source [Prometheus](https://thenewstack.io/know-the-hidden-costs-of-diy-prometheus/)/ [Grafana](https://thenewstack.io/grafana-seeks-to-correct-observabilitys-historic-terrible-job/) monitoring stack commanding a lot of attention in this emerging market.
VictoriaMetrics offers, in the words of Khavronenko,
[a simpler alternative](https://thenewstack.io/victoriametrics-offers-prometheus-replacement-for-timeseries-monitoring/) to Prometheus.
“The key differentials are simplicity and cost efficiency,” Khavronenko said. “When people migrate from Prometheus, they get a three, four times reduction in resource usage.”
Using the same protocols, VictoriaMetrics can be a drop-in replacement for Prometheus. But Prometheus can only run on a single server. VictoriaMetrics, in contrast, while also a
[single binary,](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest) can also be [run across a cluster](https://docs.victoriametrics.com/Cluster-VictoriaMetrics.html).
VictoriaMetrics can be used for
[long-term storage](https://github.com/VictoriaMetrics/VictoriaMetrics#prometheus-setup) for Prometheus. It can be used as a [drop-in replacement](https://github.com/VictoriaMetrics/VictoriaMetrics#prometheus-querying-api-usage) for Prometheus in Grafana, as well as a [drop-in replacement](https://github.com/VictoriaMetrics/VictoriaMetrics#graphite-api-usage) for [Graphite](https://grafana.com/oss/graphite/), Prometheus’ default time-series database.
## What Advantages Does VictoriaMetrics Offer?
The software was created in 2018 for an Internet ad broker, by
[Aliaksandr Valialkin](https://github.com/valyala), who is now VictoriaMetrics’ CTO. Originally, the ad tech company used Prometheus but quickly ran into scalability issues. Initially, Valialkin filed bug reports with the [Prometheus project](https://prometheus.io/), but the response was slow for his liking. So he ended up quitting the company and working on new monitoring software, posting a proof-of-concept on GitHub within a few months. The first paying customer came along shortly after, and so the company was formed.
The performance improvements that company execs boast about largely come from superior engineering, Khavronenko boasted. Both Prometheus and VictoriaMetrics are
[written in Golang](https://thenewstack.io/what-made-golang-so-popular-the-languages-creators-look-back/). Valaialkin is a frequent contributor to [Go](https://thenewstack.io/learn-the-go-programming-language-start-here/), and so is familiar with the internals of [that programming language](https://thenewstack.io/golang-co-creator-rob-pike-what-go-got-right-and-wrong/).
The company has also been a big proponent of simplicity.
“People like to overcomplicate things. They do it all the time, with software, with protocols, even with basic solutions. It’s one of the bad things in this industry,” Khavronenko said. “So our take is to try to keep it simple. When it is simple, it is reliable. And it is far easier to understand what’s happening and easier to scale.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)