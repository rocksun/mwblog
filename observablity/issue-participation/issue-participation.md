<!--
title: GitHub Issue：提升信号，减少噪音，优先排序
cover: https://opentelemetry.io/img/social/logo-wordmark-001.png
summary: 文章介绍了OpenTelemetry项目如何通过推广GitHub issue reactions（👍）来帮助维护者更好地确定issue的优先级。最终用户可以通过点赞issue来表达需求，维护者可以通过reactions数量对issue进行排序，从而更有效地管理和响应社区的需求。
-->

文章介绍了OpenTelemetry项目如何通过推广GitHub issue reactions（👍）来帮助维护者更好地确定issue的优先级。最终用户可以通过点赞issue来表达需求，维护者可以通过reactions数量对issue进行排序，从而更有效地管理和响应社区的需求。

> 译自：[More Signal, Less Noise: How GitHub Issue Reactions Help Prioritize](https://opentelemetry.io/blog/2025/issue-participation/)
> 
> 作者：Dan Gomez Blanco

您是否知道，自 OpenTelemetry 项目启动以来，已经有超过 23,000 名贡献者——即在 GitHub 上分享 issue、commit、pull request 或评论的个人？我们始终鼓励每个人都参与进来，无论是加入我们的（众多！）[CNCF Slack](https://slack.cncf.io/) 频道，还是参与任何[公开会议](https://github.com/open-telemetry/community/?tab=readme-ov-file#calendar)来倾听和分享不同的观点。这种开放性是我们最大的优势之一，但这也意味着我们会通过许多不同的渠道收到大量的反馈：GitHub、Slack、StackOverflow、会议，甚至社交媒体上的帖子。

作为活跃于该项目并每天与最终用户合作的人，我看到了贡献硬币的两面。用户提交 GitHub issue，希望修复 bug 或构建功能，而维护者则筛选大量的通知，试图找出最好地利用他们有限的时间的地方。为了让您了解规模，仅在 2024 年，整个项目中关闭的 GitHub issue 数量就超过了 7,000 个！

对于这样一个活跃的项目来说，最大的挑战之一始终是理解 OpenTelemetry 用户和贡献者认为最重要的事情是什么。而且，当我们考虑 GitHub issue 时，一连串的“+1”或“我也是！”评论并不能使这个问题变得更容易。虽然这种情绪很有价值，但这种方法会产生大量的噪音，并使维护者更难以衡量有多少人 *真正* 受到了 issue 的影响。

我们希望让每个人都更容易。这就是为什么，作为最终用户 SIG 的一部分，我们一直在努力对我们使用 GitHub 的方式进行一项小而重要的更改：**推广使用 👍 [issue reactions](https://github.blog/news-insights/product-news/add-reactions-to-pull-requests-issues-and-comments/) 作为表达兴趣的主要方式。**

### 更好的信号来帮助确定优先级

这里的目标很简单：为社区提供一种清晰、低成本、数据驱动的方式来发出什么是最重要的信号。对于维护者来说，这个系统可以减少通知噪音。他们可以[按 reaction 数量对 issue 进行排序](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#sorting-issues-and-pull-requests)，以便快速、一目了然地了解社区的需求。这有助于 SIG 和维护者在确定其 backlogs 的优先级时做出更明智的决策。

对于您，最终用户来说，这意味着您的反馈更可见。您的“+1”评论不会迷失在冗长的讨论串中，而是您的 👍 成为一个可量化的数据，有助于增加 issue 的权重。

为了使这一变化坚持下去，我们推出了一些东西。我们发布了关于 OpenTelemetry 维护者如何管理和解释这些 reaction 的[建议](https://github.com/open-telemetry/community/blob/main/guides/maintainer/popular-issues.md)，并且我们的网站现在有一个部分解释[这对最终用户意味着什么](/community/end-user/issue-participation/)。您还将在所有 OTel 存储库的[issue templates](https://github.com/open-telemetry/community/blob/main/guides/maintainer/popular-issues.md#recommended-footnote-on-issue-templates)的新脚注中看到友好的提醒。如果您要打开一个新的 issue，请保留该页脚，以便其他人可以第一手获得此建议。

### 您的快速影响指南

那么这在实践中对您意味着什么呢？这很简单。

下次您浏览 issue 时，不要只是阅读然后离开。当您发现一个 issue 描述了您也面临的问题或您希望看到实现的功能时，**只需给 issue 描述一个 👍 reaction**。就这样。点赞并订阅。这就是信号。

当然，如果您有新的、独特的用例、尚未提及的技术细节或其他有助于维护者解决问题的信息，请发表评论。这种上下文非常有价值！请记住，高 reaction 数量是一个强烈的信号，但它不会自动保证 issue 成为最高优先级。

开源是一项团队运动，这是一个完美的例子，说明小行动如何共同产生巨大的影响。

感谢您帮助我们一起使 OpenTelemetry 变得更好。