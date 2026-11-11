<!--
title: 保持智能体状态的挑战
cover: https://cdn.thenewstack.io/media/2026/11/eb49a6c7-allison-saeng-p41rhm6ivjo-unsplash-1024x576.jpg
summary: 本文探讨了Perplexity推出新功能Teammates面临的核心挑战，即如何在多智能体并发工作时保持状态同步、管理共享项目状态以及处理权限问题。
-->

本文探讨了Perplexity推出新功能Teammates面临的核心挑战，即如何在多智能体并发工作时保持状态同步、管理共享项目状态以及处理权限问题。

> 译自：[The challenge of keeping agents stateful](https://thenewstack.io/perplexity-teammates-agent-orchestration/)
> 
> 作者：Amanda Caswell

Perplexity 的全新功能 Teammates 可以协调多个智能体，记住上一次会话结束时的状态，并在无需再次提示的情况下继续工作。然而，挑战在于如何保持所有内容的同步，特别是当智能体同时工作、共享项目状态并以不同权限运行时。

[周三发布](https://www.perplexity.ai/en-GB/hub/blog/teammates-are-agents-for-complex-ongoing-work)的 Teammates 建立在 Perplexity 花费了大半年时间开发的底层基础设施之上。这次发布将先前的成果应用到了工作流中，使得智能体能够委派任务并在各个会话之间持续运行。

## 保持智能体状态的挑战

当 Perplexity 基础设施副总裁 [Nate Kupp](https://www.linkedin.com/in/natekupp/) 带领 *The New Stack* [深入了解公司的智能体沙盒](https://thenewstack.io/perplexity-space-agent-sandboxes/)时，他描述了在这一规模下维护可靠系统的难度。

Kupp 指出，鉴于运营数百万个沙盒对持久性和正常运行时间的要求，“有状态的系统构建起来极其困难。”

> “有状态的系统构建起来极其困难”

Teammates 依赖于 Perplexity Computer 现有的基础设施，该设施将持久的项目状态与单独的执行环境隔离开来。这使得智能体能够继续在同一个项目上工作，而不依赖于单一的不间断会话。

## 共享状态存在于 Git 中

在对其[共享工作空间的的技术解析](https://www.perplexity.ai/en-GB/hub/blog/building-shared-workspaces-for-people-and-agents)中，该公司描述了其如何利用基于 Git 的仓库来保持项目状态跨会话的完整性。每个 Computer 项目都有自己的仓库，而智能体则在各自独立的沙盒中工作，并将更改提交回共享项目。

当智能体同时在同一代码上工作时，情况就会变得更加复杂，因为如果一个智能体先提交了更改，另一个智能体可能必须针对最新版本重新应用其工作。

Perplexity 表示，由于基于过时的仓库状态，被拒绝的提交比例不到 2%。提交延迟的中位数低于 1.7 秒，而 p99 则保持在 8 秒以下。

> 提交延迟的中位数低于 1.7 秒，而 p99 则保持在 8 秒以下。

内存通过 Perplexity 的 Brain 系统进行独立处理，该系统将智能体学到的内容保存在专用的仓库中。这使后台智能体能够更新共享知识，而不会干扰对项目文件的更改。

## 暂停和派生智能体

Perplexity 围绕 Firecracker 微虚拟机（microVMs）和 Btrfs 快照构建了 SPACE，这使得暂停、恢复或派生智能体会话成为可能，而不会丢失其保存的状态。

借助 Teammates，开发人员可以连接 Slack 和 GitHub 等工具，并设置触发器来告知智能体何时采取行动。Perplexity 并没有过多说明当工作卡住时会发生什么，特别是当一个智能体在等待另一个智能体，或者根据已经过时的信息进行操作时。

## 公开的权限问题

每个 teammate 都在其自己的独立环境和浏览器会话中运行，访问权限通过 Computer 现有的权限进行管理，凭据则通过加密进行安全处理。用户还可以监控进度并在需要时接管。

目前尚不清楚当任务交接时，它如何防止智能体访问超出其权限的资源。对于企业而言，这种不确定性可能会影响他们愿意赋予智能体多少自主权，而无需人工批准。

Teammates 最初在网页端面向 Perplexity Max 订阅者推出，并计划支持 iOS。

> Teammates 最初在网页端面向 Perplexity Max 订阅者推出，并计划支持 iOS。

这篇文章最初发布在 [The New Stack](https://www.thenewstack.io)，标题为 [Perplexity 的 AI 智能体在你关闭标签页后仍在继续工作](https://thenewstack.io/perplexity-teammates-agent-orchestration/)。