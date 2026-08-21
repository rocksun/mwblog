GitHub 现在每月处理 29 亿次提交、1.3 亿次合并的拉取请求以及 2400 万个新存储库。早在今年 4 月，GitHub 在处理“仅” 14 亿次提交时就已经感到非常吃力。

在很大程度上，这归功于氛围编程（Vibe coding）的日益流行以及软件开发迭代速度的飞速提升。但同样显而易见的是，尽管 GitHub [正在努力向更现代化的架构迁移](https://thenewstack.io/github-will-prioritize-migrating-to-azure-over-feature-development/)，但它显然无法实现足够快的扩展以满足这种需求。

> “我们已经取得了进展，但这些事故清楚地表明，我们必须加快这项工作。” —— GitHub 首席技术官 Vlad Fedorov。

## 为什么 GitHub 在 8 月 17 日宕机

这些新数据来自于 [8 月 17 日宕机事故的事后分析报告](https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/)，那次宕机持续了近八个小时。这仅仅是 8 月份 GitHub 发生的第二次重大宕机事故。

正如 GitHub 首席技术官 Vlad Fedorov 在事后分析中所指出的：“我们已经取得了进展，但这些事故清楚地表明，我们必须加快这项工作。”

![](https://cdn.thenewstack.io/media/2026/08/8cf84602-blog-post-aug-17-outage-1.png-1024x576.webp)

图片来源：GitHub。

他强调，这次宕机是由于扩展性问题，而非代码变更导致的。GitHub 的基础设施容量耗尽，这些问题引发了连锁反应，最终导致了宕机。

“我们的调查发现，宕机始于流量达到新的峰值，而我们美国中部数据中心的一个关键基础设施组件未能随之进行扩展，”他解释道。“由此产生的容量压力扩散到我们的整个系统中，导致了身份验证失败并中断了多个 GitHub 服务。”

![](https://cdn.thenewstack.io/media/2026/08/c43f4ad8-blog-post-aug-17-outage-gitfetch.png-1024x576.webp)

图片来源：GitHub。

## 新增 300 万个 CPU 核心，GitHub 依然难以为继

值得注意的是，这并不是因为 GitHub 没有对其基础设施进行扩展。Fedorov 在文章中披露，GitHub 目前 58% 的平台负载由 Azure 处理。这一数字在 5 月份仅为 12%。目前，所有 Git 操作中有一半也是由 Azure 处理的。

Fedorov 写道，该团队今年增加了 300 万个 CPU 核心，以及 120 PB 的高速存储。

至于 GitHub 自己的数据中心，现在已经达到了极限。“我们在现有数据中心安装了尽可能多的硬件，同时也在加速向 Azure 的迁移，”Fedorov 说道。

他还承认 GitHub 也面临着其他挑战。

“随着变革的节奏和复杂性不断增加，我们现有的运营实践已经跟不上步伐。我们已经重新调配了团队和资源，重点转向系统的可用性，并投资于更严格的测试、更安全的部署、更好的可观测性以及更有效的预警机制。我们已经取得了进展，但这方面的工作尚未完成，”他写道。“此外，我们还在隔离关键系统，并消除它们之间的共享依赖。这项工作旨在降低宕机的可能性，并在宕机发生时限制其影响。”

目前，为了避免引发近期宕机的问题，GitHub 正在采取一些具体的变更措施：正如 Fedorov 所写的，它正在应用一致的重试限制和预算，并调整服务间交互的超时设置，“以防止重试风暴和连锁负载”。

## 摇摇欲坠的 GitHub 为他人提供了机会

GitHub 是开发者生态系统——尤其是开源生态系统——的核心。然而，它近期出现的问题为其他公司推出竞争产品创造了契机。

这其中包括 [Entire](https://thenewstack.io/entire-git-for-agents/)，这家由 GitHub 前首席执行官 Thomas Dohmke 创立的初创公司，正押注于分布式系统，以更好地处理由 AI 驱动的开发工作负载。随着 [Origin](https://thenewstack.io/cursor-origin-github-alternative/) 的推出，Cursor 也加入了这场竞争。