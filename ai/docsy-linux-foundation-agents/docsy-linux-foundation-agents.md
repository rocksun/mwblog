<!--
title: Docsy 动态：随着 AI 智能体成为读者，谷歌文档项目加入 Linux 基金会
cover: https://cdn.thenewstack.io/media/2026/10/da8d1af3-robot-heart-sticker-on-keyboard2.jpg
summary: 谷歌创建的开源技术文档项目 Docsy 已正式加入 Linux 基金会。随着 AI 智能体成为技术文档的新读者，Docsy 正在积极推出多项新功能，帮助项目更好地适应机器阅读。
-->

谷歌创建的开源技术文档项目 Docsy 已正式加入 Linux 基金会。随着 AI 智能体成为技术文档的新读者，Docsy 正在积极推出多项新功能，帮助项目更好地适应机器阅读。

> 译自：[What's up, Docsy? Google’s docs project joins the Linux Foundation as AI agents become readers](https://thenewstack.io/docsy-linux-foundation-agents/)
> 
> 作者：Paul Sawers

技术文档正越来越多地被 AI 智能体阅读，这给信息的发布和结构化方式带来了一套新的需求。[Docsy](https://www.cncf.io/blog/2025/01/07/docsy-2024-review-adoptions-and-enhancements/) 是一个由谷歌创建、被各大云原生项目广泛使用的文档项目，现在它正移交给 Linux 基金会，同时该项目正在添加专门针对这种机器受众的功能。

谷歌高级开发者关系工程师兼 Docsy 指导委员会成员 [Erin McKean](https://www.linkedin.com/in/emckean/) 在布拉格 Linux 基金会[欧洲开源峰会](https://events.linuxfoundation.org/open-source-summit-europe/)周三的主题演讲中宣布了这一举措。

Docsy 最初由[谷歌于 2019 年宣布](https://opensource.googleblog.com/2019/07/announcing-docsy-website-theme-for.html)，是专为技术文档设计的 [Hugo 静态网站生成器](https://thenewstack.io/tutorial-use-hugo-to-generate-a-static-website/)的开源主题。它通常可用于各种文档（包括专有项目），尽管它在开源领域已经变得尤为流行。截至 [2024 年底](https://www.cncf.io/blog/2025/01/07/docsy-2024-review-adoptions-and-enhancements/)，大约有 2,200 个项目正在使用 Docsy，其采用者遍布云原生计算基金会（CNCF），包括 Kubernetes、OpenTelemetry、gRPC 和 Jaeger。

在 Linux 基金会社区内部已有的足迹是此次迁移背后的部分原因。McKean 在主题演讲结束后接受 *The New Stack* 采访时表示，将 Docsy 引入基金会使其更贴近许多已经在使用它的项目。

“开源项目在贴近用户时运作得最好，”她说。

> “开源项目在贴近用户时运作得最好。”

## AI 也需要好的文档

在她的主题演讲中，McKean 重点关注了 AI 作为技术文档新消费者的到来。她承认，一些技术作家对 AI 花了这么长时间才为文档带来更多资源感到“有点不爽”。但她认为，重要的一部分在于信息最终是否能送达并帮助开发者，无论它走的是什么路线。

> “当我们制作技术文档时，信息如何对人类变得有用其实并不重要，只要它能做到这一点就行。”

McKean 说：“当我们制作技术文档时，信息如何对人类变得有用其实并不重要，只要它能做到这一点就行。”“如果有人告诉我，有证据表明歌剧是接触项目用户的最佳方式，那我就会去写歌剧。”

Docsy 已经开始调整其输出以适应 AI 工具。自 5 月份的[版本 0.15.0](https://www.docsy.dev/blog/2026/0.15.0/)以来，除了常规的 HTML 之外，它还可以为每个页面生成一个 Markdown 副本，以及一个为 AI 工具提供网站内容索引的 llms.txt 文件。这两项功能都是可选的，目前仍处于实验阶段。

更广泛的理念是为 AI 系统提供一条更直接的途径，以获取项目希望它们使用的信息。

> “你可以将你的大语言模型和智能体重定向到告诉它们如何使用该项目的文本上。”

McKean 说：“你可以将你的大语言模型和智能体重定向到告诉它们如何使用该项目的文本上。”

围绕这一基本概念，Docsy 继续添加各项功能。7 月发布的[版本 0.16.0](https://www.docsy.dev/blog/2026/0.16.0/)包含了一份升级指南，其编写方式使得 AI 助手也可以按照指南操作，并且说明中内置了条件、步骤和检查。而在 8 月发布的[版本 0.17.0](https://www.docsy.dev/blog/2026/0.17.0/)中，Docsy 在帮助智能体消费文档本身方面迈出了更远的一步。启用了 llms.txt 的网站现在会在每个页面的顶部自动包含一个隐藏指令，引导访问的智能体指向该网站的 llms.txt 索引。该功能同样处于实验阶段。

## 为智能体评估文档

路线图上的下一个目标是“AF”（即面向智能体友好，agent-friendly）的“文档评分”，旨在为维护者提供一种评估 AI 工具查找、导航和消费其文档难易程度的方法。McKean 表示，这应该为项目提供一个努力的基准。

“你将不必去猜测，”她说。“你可以衡量你的文档对智能体有多友好。”

更好的文档还有一个更常规的好处：发给维护者的常规问题减少了。McKean 表示，好的文档可以在人工介入之前就回答这些问题。

她说：“当你拥有好的文档时，它会减少那些可以通过文档轻松解答的问题数量，从而减轻维护者的负担。”