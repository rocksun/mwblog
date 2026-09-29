<!--
title: 从内核分析到AI：Adrian Cockcroft的性能工程之道
cover: https://cdn.thenewstack.io/media/2026/09/d8c78ab2-getty-images-vgi8oknylk4-unsplash.jpg
summary: 本文介绍了资深系统架构师Adrian Cockcroft对性能工程的见解，探讨了他从早期钻研内核源码到如今利用AI进行氛围编程、分析响应时间分布峰值的经历与思考。
-->

本文介绍了资深系统架构师Adrian Cockcroft对性能工程的见解，探讨了他从早期钻研内核源码到如今利用AI进行氛围编程、分析响应时间分布峰值的经历与思考。

> 译自：[Performance engineering from kernel analysis to AI: Adrian Cockcroft’s take](https://thenewstack.io/cockcroft-performance-engineering-ai/)
> 
> 作者：Tim Koopmans, Cynthia Dunlop

在 P99 CONF 五年的历史中，曾有多位演讲者对这个同名指标提出过犀利的批评。在去年的会议上，Adrian Cockcroft 并没有明确说 [P99 是胡扯](https://thenewstack.io/if-p99-latency-is-bs-whats-the-alternative/)……但他确实暗示了这一点。

如果你不了解 [Cockcroft](https://www.linkedin.com/in/adriancockcroft/)，他曾在 Sun Microsystems、Netflix、eBay 和 Amazon 等科技巨头花费数十年时间，负责架构、扩展和优化具有弹性的高性能系统。我们完全可以把 P99 CONF 的整整一天时间，用来讨论从他参与的*部分*项目中汲取的经验教训（Solaris 内核性能、多处理器优化、Netflix 从本地迁移到云端、Chaos Monkey……）

幸运的是，RedMonk 分析师 [Rachel Stephens](https://redmonk.com/team/rachel-stephens/) 成为了这场聚焦于让事物运行得更快的大会的完美主持人。她与 Adrian 进行了深入交流，带我们领略了 AI 如何影响性能工程的精彩全貌。以下是访谈的一些亮点（完整视频见文末）。

*注：P99 CONF 2026 是一场专注于性能的全方位免费虚拟会议，将于 10 月 21 日至 22 日在线举办。快来领取*[免费通行证](https://www.p99conf.io/?latest_sfdc_campaign=701Rb00000qrLWi&campaign_status=Submitted&utm_campaign=smo%20new%20stack%202026-10-21%20p99%20conf&utm_medium=social%20media%20-%20organic&utm_source=the%20new%20stack&lead_source_type=the%20new%20stack)*加入我们吧！*

作为 Sun 全盛时期的性能专家，探究性能问题的根源需要大量的挖掘和推测。Cockcroft 回忆道：“在 Sun 的老日子里，人们会查看 [vmstat](https://www.redhat.com/en/blog/linux-commands-vmstat) 或其他工具中的系统指标输出，然后去猜测这些数字代表什么。对于这些东西的含义，大家的理解非常模糊。手册页也不是很清楚。”

Cockcroft 最终选择直奔源头。我去阅读了所有的内核源码，确切弄清楚了这些数字来自哪里、到底代表什么、哪些是在近似模拟什么，并把这些全部记录了下来。”这催生了两本性能著作：《Sun Performance and Tuning》和《Resource Management》。

> “我的加速是无限的，因为如果没有这些工具，这段代码根本就不会存在。我没有时间去构建它们。”

四十年后，如今有了丰富的端到端追踪实用工具，但 Cockcroft 的好奇心依然在于工具没有显现出来的地方。他继续说道：“在工具中，一切*看起来*都还算正常——但系统的行为表现却很糟糕。我通常会介入并尝试寻找观察数据的新方法。一种新型的分析方式，或者更深入、更精细一点，又或者停止观察平均值并开始关注分布，从而发现所有人以前都不知道正在发生各种有趣的事情。”

目前，他正在进行[氛围编程](https://thenewstack.io/beginners-guide-to-vibe-coding/)来构建工具，以便更好地分析他发现的异常情况。由于免去了复习 Python 或在 Stack Overflow 上搜寻图形库代码片段的烦恼，Cockcroft 现在可以在几分钟内搭建出自定义工具。“我的加速是无限的，因为如果没有这些工具，这段代码根本就不会存在。我没有时间去构建它们。”

## 峰值而非百分位数

一个具体的氛围编程项目：Cockcroft 构建（并开源）了相关工具，以便更好地理解响应时间分布。

十多年来，响应时间分布一直占据着 Cockcroft 的脑海。虽然大多数人痴迷于百分位数——是的，包括 P99 CONF 在内——但 Cockcroft 最感兴趣的是直方图中响应时间峰值的分布。他认为，在试图理解现代网络服务的延迟和性能时，百分位数并不起作用。像 P99 这样的单一数字无法告诉你底层分布究竟是一个峰值还是多个峰值。而当存在多个峰值时（现实世界中往往如此），平均值、标准差甚至 P99 本身都会失去大部分意义。

> “在试图理解现代网络服务的延迟和性能时，百分位数并不起作用。”

![展示人们认为的响应时间分布与实际分布的对比图](https://cdn.thenewstack.io/media/2026/09/a42212ef-image1-1024x559.png)

*(来源：[两个直方图的故事](https://github.com/adrianco/slides/blob/master/Monitorama%20Histograms.pdf))*

例如，假设你有一个包含两个响应时间峰值的直方图：一个来自缓存命中的快速峰值，另一个来自需要实际工作的缓存未命中的缓慢峰值。随着缓存命中率的变化，每个峰值的位置保持不变（即快速响应模式和慢速响应模式的延迟值没有改变），但峰值的高度会此消彼长。“你的平均值和 P99 在四处变动，但实际上发生的一切只是你的缓存命中率在改变，”Cockcroft 说道。

那么，如何超越对 P99 和平均值的测量呢？Cockcroft 做出了他几十年来一直在做的事情：深入研究并[构建一个自定义](https://thenewstack.io/with-nova-forge-aws-makes-building-custom-ai-models-easy/)工具。但如今，多亏有了 LLM，这一切变得简单多了。

> “你的平均值和 P99 在四处变动，但实际上发生的一切只是你的缓存命中率在改变。”

他此前已经制定了用于分析分布的统计方法。ChatGPT 问世后，他迅速用它构建了一个自动化该过程的工具。它没有把所有东西折叠成一个平均值，而是识别出分布中任意数量的峰值，并追踪它们随时间的波动情况。它是用 R 语言实现的——这门语言 Cockcroft 已经有一段时间没用了，但 ChatGPT 却非常精通——并且它已经[开源](https://github.com/adrianco/responsetime-distribution-analysis/blob/main/README.md)。如果你对此感到好奇，可以在他的[《百分位数不起作用》](https://adrianco.medium.com/percentiles-dont-work-analyzing-the-distribution-of-response-times-for-web-services-ace36a6a2a19)文章以及[《两个直方图的故事》](https://www.youtube.com/watch?v=kKx1E8C2tv0)[演讲](https://github.com/adrianco/slides/blob/master/Monitorama%20Histograms.pdf)中了解更多（*“这是响应时间最好的时代，也是响应时间最坏的时代……”*）

## 我们将去向何方？

最后，Stephens 询问 Cockcroft，他会对当前从事高性能系统工作的团队分享什么建议。他的头号建议是：从宏观视角开始以发现有趣的问题，然后不断深入挖掘，直到能够端到端地检查单个慢速请求。

“还记得你小时候得到的显微镜吗，”Cockcroft 说。“首先，你必须用最低分辨率（10倍）来对焦，然后你可以点击切换到 100倍并进行调整，此时观察的只是一个小斑点。一旦你将它对焦，你就可以点击切换到 1,000倍。”

Cockcroft 的整个职业生涯都在构建工具，让那些晦涩难懂的性能问题清晰呈现。我们期待看到今年在 P99 CONF 上，其他人利用智能代理工具（agentic tooling）碰撞出怎样的火花，以帮助识别和[解决性能问题](https://thenewstack.io/the-complexity-of-solving-performance-problems/)。

*在 P99 CONF 上了解最新的性能优化技术、工具和案例研究——这是一场免费的虚拟会议，于 10 月 21 日至 22 日举行。快来领取*[免费通行证](https://www.p99conf.io/?latest_sfdc_campaign=701Rb00000qrLWi&campaign_status=Submitted&utm_campaign=smo%20new%20stack%202026-10-21%20p99%20conf&utm_medium=social%20media%20-%20organic&utm_source=the%20new%20stack&lead_source_type=the%20new%20stack)*加入我们吧！*