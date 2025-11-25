
<!--
title: 为何Notebooks是AI智能体的“完美界面”
cover: https://cdn.thenewstack.io/media/2025/11/1164d37b-thumbnail-27.png
summary: Deepnote 旨在弥合计算工具鸿沟，通过打造协作式笔记本，支持数据探索与生产化。Deepnote 现已开源，新增多种构建块，致力于成为 AI 时代理想的计算媒介和用户界面。
-->

Deepnote 旨在弥合计算工具鸿沟，通过打造协作式笔记本，支持数据探索与生产化。Deepnote 现已开源，新增多种构建块，致力于成为 AI 时代理想的计算媒介和用户界面。

> 译自：[Deepnote CEO: Why Notebooks Are the 'Perfect User Interface' for AI Agents](https://thenewstack.io/deepnote-ceo-why-notebooks-are-the-perfect-user-interface-for-ai-agents/)
> 
> 作者：Michelle Gienow

当 [Jakob Jurových](https://www.linkedin.com/in/jakubjurovic/) 和他的团队在 2019 年开始构建 Deepnote 时，他们看到了两个计算世界之间存在的鸿沟，而现有工具都无法弥合。

“世界 A 是那些易于使用、易于上手但功能也有限的工具，” Deepnote 的创始人兼首席执行官 Jurových 说，他以电子表格为例。

“在世界 B 中，工具更加先进，你可以构建任何你能想象到的东西——但首先你需要花费大量时间学习这些工具。”

Jurových 把构建这个缺失的计算中间地带作为自己的使命。

在 The New Stack Makers 的本期“在路上”节目中，Jurových 在圣迭戈的 [JupyterCon](https://thenewstack.io/from-physics-to-the-future-brian-granger-on-project-jupyter-in-the-age-of-ai/) 上与 TNS 主编 [Heather Joslyn](https://thenewstack.io/author/hjoslyn/) 坐下来，讨论了 [Deepnote 为什么要开源](https://thenewstack.io/deepnote-a-successor-to-jupyter-notebook-goes-open-source/)，并分享了他对笔记本作为 AI 时代终极媒介的愿景。

## 缺失的计算媒介

Jurových 喜欢笔记本（Notebooks）的概念，它自 80 年代以来就已存在，但现有格式并非为数据探索所需的紧密反馈循环而设计。与拥有整洁 Jira 任务和明确最终状态的软件工程师不同，数据科学家拿到一个 CSV 文件，然后被告知“去发现一些有趣的东西”。

“数据探索是一种完全不同的工作方式，”他说。“没有明确的终点，你总能对数据进行更广或更深的探索。”

Deepnote 被设计成一个用于持续协作的笔记本，而不是异步拉取请求。“我们展示了在一个笔记本中，不仅可以有两三个人结对编程，还可以有数百人同时进行。现在，我们经常有数千人同时在一个笔记本中进行会话。”

## 从草稿到生产

决定开源并非易事。团队从第一天起就想这样做，但必须首先解决更紧迫的问题：稳定性、可复现性和协作。

“我们意识到，首先解决问题很重要，然后开源就只是锦上添花了，”Jurových 指出。团队成员还需要对他们的架构有信心，才能承诺向下兼容。

现在，六年之后，[Deepnote 准备开源](https://github.com/deepnote/deepnote)，它采用了为云、协作和 AI 时代设计的新格式。Jupyter 只有两种单元格类型（代码和 Markdown），而 Deepnote 则有 23 种构建块——并且还在增加。

“我们认为笔记本是一种美妙的格式，你可以在同一个地方一直保留并完成工作流程的生产化，”Jurových 说。“笔记本本身可以成为整个数据应用程序。它可以成为你安排每 12 小时运行一次的东西。它可以附加一个 API 端点。”

他总结道，这种灵活的多任务处理能力正是“笔记本是与 AI 代理协作的完美用户界面”的原因。

查看完整节目，了解更多关于 Deepnote 从在课堂负载下崩溃到成为生产就绪工具的历程，以及为什么未来十年的计算工作可能与我们自 2011 年以来所依赖的格式完全不同。