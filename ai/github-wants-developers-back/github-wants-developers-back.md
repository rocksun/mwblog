<!--
title: 面对频繁宕机，GitHub 计划如何挽回开发者的心？
cover: https://cdn.thenewstack.io/media/2026/05/cc2144dc-img_3679-scaled.jpg
summary: 因AI智能体带来超高流量导致频繁宕机，GitHub正全员重构底层系统、迁移至Azure并加强隔离，在微软支持下全力提升系统高可用性，以期挽回开发者信任。
-->

因AI智能体带来超高流量导致频繁宕机，GitHub正全员重构底层系统、迁移至Azure并加强隔离，在微软支持下全力提升系统高可用性，以期挽回开发者信任。

> 译自：[How GitHub plans to win developers back](https://thenewstack.io/github-wants-developers-back/)
> 
> 作者：Frederic Lardinois

在过去一年的大部分时间里，GitHub 已经不再是开发者早已习惯的那个稳定工具了。[频繁宕机](https://www.githubstatus.com/history)频发，从搜索到 GitHub Actions 以及依赖于它的 CI/CD 流水线，无一幸免。在过去的 12 个月里，该公司记录了数百起事件，并不得不公开致歉。

*The New Stack* 采访了 GitHub 首席运营官 [Kyle Daigle](https://www.linkedin.com/in/kyledaigle/)（他现在也是微软开发者首席营销官），探讨了这一切发生的原因以及 GitHub 正在采取哪些措施来解决这一问题。

## 为什么规划 100% 的增长还不够

![](https://cdn.thenewstack.io/media/2026/06/30168453-1712319381689.jpg)

Kyle Daigle

该公司相当坦诚的一点是，在这个智能体编程（agentic coding）时代，它正面临着前所未有的增长——这种增长远远超出了即使是处于超高速增长期的云公司通常所经历的。

正如 Kyle Daigle 所说，为了应对这种超高速增长，GitHub 现在正处于“全员动员”（all hands on deck）的状态。

“在云时代，这不仅仅是通常的扩展解决方案，比如换一台更大的机器，或者增加更多机器，”Kyle Daigle 告诉 *The New Stack*。“现在我们要确保在未来一年内能够实现 30 到 40 倍的扩展，而不是像过去那样实现令人瞩目的 100% 同比增长。”

Kyle Daigle 表示，GitHub 原本以为从 50% 的增长跨越到 200% 的增长会是一个惊喜。“事实证明，这只是个简单的数字，我们需要走得更远，”Kyle Daigle 说道。GitHub 的工程团队目前正在努力将系统提升到能够处理如今 30 倍的提交（commits）、拉取请求（pull requests）和问题（issues）的水平。

> “在云时代，这不仅仅是通常的扩展解决方案，比如换一台更大的机器，或者增加更多机器。”  
> ——GitHub 首席运营官 Kyle Daigle

考虑到 GitHub 本身在 2021 年推出 Copilot 并在很大程度上开启了这一时代，这其中可能带有一丝讽刺意味。在许多方面，这向开发者普及了 AI 代码生成，并训练他们开始依赖它。现在，GitHub 正在重载之下不堪重负。在 2025 年全年，该服务处理了 10 亿次提交。而现在，它每个月处理 14 亿次。Kyle Daigle 表示，仅智能体（agents）现在每月就会创建超过 1700 万个拉取请求。

## “全员动员”究竟意味着什么

GitHub 一直在从自己的数据中心迁移到 [微软的 Azure 云](https://thenewstack.io/github-will-prioritize-migrating-to-azure-over-feature-development/)，以满足这一需求，但 Kyle Daigle 指出，这不仅仅是增加容量的问题。

“我们真正关注的不仅是以常规方式扩展，即继续获取更多 CPU 并进行那种正常的水平和垂直扩展，更重要的是，真正深入挖掘底层系统，更新或重构它们，或者改进那些执行核心工作的隐藏系统，”Kyle Daigle 说道。

正如 GitHub 首席技术官 Vlad Fedorov 在今年早些时候的一篇博客文章中所指出的，早期的许多工作都集中在缓解数据库压力上。GitHub 解决了 MySQL 竞争问题，将 webhook 完全移出 MySQL，并重新设计了其会话缓存（session cache）和身份验证流程，以减轻数据库负载。

针对 GitHub Actions，Kyle Daigle 表示，向运行器（runners）派遣作业（jobs）的方式必须重写。更广泛的架构目标是将 Actions 和 Git 等关键服务与其它所有服务隔离开来，这样一个出现问题的子系统就不会把其它子系统也拖垮。GitHub 还在将对性能敏感的代码从 Ruby 单体架构中移出，转而使用 Go 语言。

“大部分容易实现的目标（low-hanging fruit）我们已经攻克了，”Kyle Daigle 说道，尽管他承认这些成果很难直观地展现出来。“这就是提高可用性的两难境地（catch-22），”他说。“当服务正常运行时，你没有一个简单的方法可以说，看，我们做了这个改进。”

GitHub 也在依靠微软的帮助。“在 GitHub，这确实是全员动员，”Kyle Daigle 说。“我们得到了前所未有的支持，有经验丰富的工程师来帮助我们快速扩展。”其中许多支援力量来自微软，包括曾经扩展过这种规模系统的工程师。

“我们的首要任务是拥有一个正常运行、值得信赖、且对全球开发者——现在也包括全球智能体——来说可靠的平台，”Kyle Daigle 说道。

## 为什么 GitHub 仍在不断推出新功能

一个值得思考的问题是：如果可用性是首要任务，为什么 GitHub 仍然在 Build 大会上推出新的 Copilot 应用和其它功能？

Kyle Daigle 认为，并非每个层面的风险都是相同的。CLI 和新的 Copilot 应用在托管版 GitHub 的“爆炸半径”之外进行迭代，因此它们可以快速推进，而无需触及正在修复的系统。后端工作则“专注于稳定性和弹性”，有时重建底层架构会顺便解锁一些新功能。

“如果我发布一个 CLI 功能，它不像 [github.com](https://github.com) 那样具有相同的稳定性和弹性特征，”Kyle Daigle 说道。

当然，当下层基础设施宕机时，这些也就不那么重要了，但 Kyle Daigle 似乎对 GitHub 历史的这一阶段将很快结束抱有希望。

“希望每个月都比上个月好一点，”Kyle Daigle 说道，“伴随着我们所能付诸的所有紧迫感。”