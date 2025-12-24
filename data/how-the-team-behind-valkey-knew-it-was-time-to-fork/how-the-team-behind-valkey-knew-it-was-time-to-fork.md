<!--
title: Valkey团队：为何他们选择分叉？
cover: https://cdn.thenewstack.io/media/2025/12/9e069f10-forks-2.jpg
summary: Valkey因Redis许可证变更及治理问题而分叉，旨在建立开放透明、社区驱动的项目。关键经验：起草章程、规范源码、团结社区、全面文档、支持下游。分叉是维护开源的最后手段。
-->

Valkey因Redis许可证变更及治理问题而分叉，旨在建立开放透明、社区驱动的项目。关键经验：起草章程、规范源码、团结社区、全面文档、支持下游。分叉是维护开源的最后手段。

> 译自：[How the Team Behind Valkey Knew It Was Time to Fork](https://thenewstack.io/how-the-team-behind-valkey-knew-it-was-time-to-fork/)
> 
> 作者：Steven J. Vaughan-Nichols

东京 — 分叉一个开源项目从来都不是首选。它会造成分裂、存在风险，并且在政治上是危险的。但有时，正如 [Valkey](https://valkey.io/) 负责人 Roberto Luna Rojas 和 Madelyn Olson 周一在[日本开源峰会](https://events.linuxfoundation.org/open-source-summit-japan/)上的演讲中所说，你别无选择。这是保护开源项目唯一可行的前进道路。

对于不了解这个故事的人，回顾一下：2024 年，广泛使用的内存键值 NoSQL 数据库的开发者 [Redis](https://redis.com/?utm_content=inline+mention)，[决定放弃其三条款伯克利软件发行版 (BSD) 许可](https://lwn.net/Articles/966133)，并将其替换为只读的 [Redis 源代码可用许可证 (RSALv2)](https://redis.com/legal/rsalv2-agreement/) 和 [服务器端公共许可证 (SSPLv1)](https://redis.com/legal/server-side-public-license-sspl/)。这让其核心开发团队成员感到非常不满。

因此，他们迅速决定[将代码分叉为我们现在所知的 Valkey 项目](https://thenewstack.io/valkey-will-not-just-be-a-redis-retread/)。Valkey 正在被证明是一个[非常成功的分叉](https://thenewstack.io/valkey-8-1s-performance-gains-disrupt-in-memory-databases/)。在 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)、[Google](https://cloud.google.com/?utm_content=inline+mention)、[Microsoft](https://news.microsoft.com/?utm_content=inline+mention)、[Oracle](https://www.oracle.com/developer?utm_content=inline+mention) 和其他科技巨头都支持 [Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/ "Valkey") 的情况下，这个开源分叉项目进展顺利。也许最能说明问题的是，Redis 在今年 5 月决定[根据 GNU Affero 通用公共许可证 (AGPL) 重新开放该项目的代码库](https://thenewstack.io/redis-is-open-source-again/)。

然而，早在 2024 年，Valkey 分叉团队的成员并不知道这一点。他们只知道必须采取行动。这就是他们的故事。

在日本开源峰会上，Olson 和 Luna Rojas 在座无虚席的会场中发表演讲，他们都是 Redis 的长期贡献者，详细介绍了 Valkey 从 Redis 分叉之前的警告信号、社区为准备所采取的步骤，以及他们认为每个开源维护者都应该理解的来之不易的经验教训。

## 发现危险信号

Olson，现任 AWS 首席工程师，表示最大的问题源于治理，它逐渐将控制权集中在 Redis 公司内部。

她回顾说，像她这样的 Redis 开源维护者看到了三个主要的警告信号，他们本应注意。

首先是封闭式治理：Redis 任命的维护者“在项目内部拥有特殊权限”，而像 Olson 这样的外部维护者“基本上只是普通成员”，将核心决策权留给了公司员工。

然后所有权力都掌握在公司手中，而不是社区。“Redis 还拥有明确的否决权……[以及]否决他们想要的任何东西的能力，”她补充说。这使得公司能够强行将功能引入项目——即使维护者不同意。

Olson 引用 [Redis Functions](https://redis.io/docs/latest/develop/programmability/functions-intro/) 作为 Redis“强制引入项目的一个功能示例……因为他们认为那是他们想要的”，尽管社区维护者对此表示反对。

社区还看到功能因非技术原因被拒绝，Olson 称之为“一个非常重要的警告信号”。AWS、Google 及其他公司广泛请求的一项功能，[集群槽统计](https://valkey.io/commands/cluster-slot-stats/)，仅仅因为 Redis 不想要它而被拒绝了。

Olson 表示，除了治理之外，Redis 的项目基础设施是不透明的。构建、性能测试甚至开源工件发布的宿主都是私有或专有的。“只有 Redis 的人才可以进行实际发布，”她指出，这在后来分叉时成为了一个严重的障碍。

Redis 拒绝就 Valkey 维护者的说法发表评论。

2024 年 3 月，Redis 更改了其许可证。Olson 说，开源维护者知道情况不对劲，变化可能迫在眉睫。这一转变促成了 Valkey 的创建，这是一个完全开放、由 Linux 基金会管理的 fork，旨在维护社区治理和用户的连续性。

## 分道扬镳

Valkey 团队立即设定了其优先事项：

*   保留核心流程和行为，以便用户体验到连续性。
*   建立强大、中立的治理结构。
*   维持社区的团结。
*   尽可能将一切公开

Valkey 团队采用了 [Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention)的[技术指导委员会模式](https://www.linuxfoundation.org/blog/blog/introducing-the-open-governance-network-model)，因为它“与我们之前拥有的非常相似”，并且从一开始就由工程驱动。但这一次，团队承诺，决策将是公开、透明和负责任的。

最早的改变之一是取消私人会议。“所有会议都是公开的，”Olson 说。“如果我们发现有人试图举行私人会议，我们将强制他们取消并公开。”

她强调了一个普遍原则：“默认一切都公开”，这一改变“对项目非常有效”。

由于 Redis 的内部基础设施一直是不可见的，Valkey 维护者很快发现他们缺乏基本信息。例如，他们不知道二进制文件是如何构建的，下游发行版从何处获取 Redis，以及谁维护关键软件包。

Olson 说，他们“非常幸运”地在一次活动中遇到了一位 Fedora 打包员，因为如果没有这个联系，“我们甚至不会知道……从何开始”重建下游支持。

为了避免重复 Redis 的不透明性，新团队还将文档和自动化作为优先事项。Olson 说，另一种选择“基本上是尝试明确地记录所有内容，或者围绕它建立公开可用的自动化。任何人都可以查看代码……并很快获得一个相对不错的答案”。

自动化允许任何人，而不仅仅是 AWS 工程师，来发布官方版本。“两次发布都是由社区成员完成的，而不是 AWS，”她自豪地说。现在“一切都是一键机制”，通过 GitHub Actions 和 CI 可以看到并修复问题。

关于 Redis 分叉前的主要抱怨之一是其不可预测的发布节奏。Olson 描述了 Redis 7.0.2，其代码截止日期是 5 月，但直到 8 月才发布。

Valkey 选择了一个六个月的发布周期作为开始；团队成员通过超出了预期而感到惊讶。Olson 说：“为你的社区提供可预测性真的非常重要。”她指出，规律的发布节奏有助于用户决定何时以及如何贡献修复和功能。

## 遇到的挫折

并非一切都顺利进行。开放也带来了成长的烦恼。

因为任何人都可以触发发布，所以错误也随之发生。一位工程师在忘记提交后“重新标记”了一个发布版本——这破坏了 [Homebrew](https://brew.sh/) 等下游系统。“不要让你的社区这样做，”Olson 笑着说。简单、正确的修复方法是创建一个新版本并正确标记它。

分支保护也至关重要。几位贡献者不小心将提交直接推送到了生产分支。“这并不是因为我们不信任人，”Olson 说。“每个人都会犯错”，保护措施是为了防止事故，而不是审查意图。

沟通工具也带来了自身的挑战。社区一直在使用 Slack，但许多人不喜欢它，包括 Olson：“我讨厌它。”

因此维护者尝试了 Matrix 和 Discord。所有这些迁移尝试都失败了。“没有人迁移，”Olson 承认。尽管 Slack 有局限性，包括消息过期和失效的邀请链接，她表示，“我们最终还是慢慢地都回到了 Slack”，因为贡献者们都在那里。

## 分叉前的检查清单

如果你在企业驱动的开源项目中看到这些警告信号（不透明的管理、高管忽视开发人员和客户请求），Olson 和 Luna Rojas 建议你应该开始考虑分叉，这样当你的公司试图关闭你的开源项目时，你就不会措手不及。

Luna Rojas 以一个比喻结束了会议：“当你看到分叉的怪物从你的代码库中跳出来时，你不想独自面对它。Linux 基金会会与你同在，帮助你构建一个社区拥有的项目。”

他强调了任何考虑分叉的项目都应遵循的明确检查清单：

*   “现在就开始起草章程。”
*   “源代码控制规范——在保护分支和标签的同时尽量确保安全。”
*   “让你的社区团结在一起……无论他们在哪里。”
*   “记录一切。”
*   并始终支持下游维护者——那些使软件在全球发行版中可用“无名英雄”。

分叉可能是最后的手段，但正如 Valkey 团队所展示的那样，当警示的暴风雨聚集，治理不再为社区服务时，分叉可能是最健康、最可持续的前进道路。