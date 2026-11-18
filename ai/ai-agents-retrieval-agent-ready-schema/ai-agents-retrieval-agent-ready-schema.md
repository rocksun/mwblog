<!--
title: 教你如何教会AI智能体像人类专家一样进行搜索
cover: https://cdn.thenewstack.io/media/2024/03/46b69bf3-untangle-vector-search-1024x576.jpg
summary: 本文介绍了如何通过优化数据结构和使用智能体就绪模式，教导AI智能体像人类专家一样进行复杂搜索，从而避免检索错误并提高工作自动化效率。
-->

本文介绍了如何通过优化数据结构和使用智能体就绪模式，教导AI智能体像人类专家一样进行复杂搜索，从而避免检索错误并提高工作自动化效率。

> 译自：[Here’s how to teach AI agents to search like human experts](https://thenewstack.io/ai-agents-retrieval-agent-ready-schema/)
> 
> 作者：Alex Wilhelm

**智能体检索成为热门话题是有原因的：** 每家公司都希望实现工作自动化，但他们往往还没准备好。启动一个智能体，将其指向海量数据，并在 Token 上花费巨资却只得到平庸的结果，这种做法既极其简单又极具诱惑力。

要释放能够完成实际工作的智能体，你需要一种不同的方法。如果不同时解决如何为其提供更好数据的问题，你就不可能通过向失败的智能体工作流投入更智能的 AI 模型来解决问题。这起不到太大作用。

那么，公司应该如何为快速、准确地使用智能体准备好他们的信息呢？这正是 *The New Stack* 将于 12 月 2 日星期三与 [Vespa.ai](https://vespa.ai/) 的 [Jenny Morris](https://www.linkedin.com/in/jennyjmorris) 一起深入探讨的直播内容。

立即注册本次网络研讨会

您已成功注册网络研讨会。

你可能会在智能体工作流中加入一个定制模型，以帮助在智能体请求和它正在查询的数据集之间进行转换。虽然这个想法有其优点，但它通过在搜索中增加整个步骤来增加延迟；谁愿意变慢或消耗*更多* Token 呢？

![](https://cdn.thenewstack.io/media/2026/11/65b83cfe-jenny-morris-vespa-ai.jpeg)

Jenny Morris，Vespa.ai 高级首席解决方案架构师

Vespa 认为，前进的方向是帮助智能体自己处理复杂且通常是多线程的同时搜索。如何做到？通过为智能体提供一张地图（markdown 文件），涵盖搜索工具的工作原理；如果没有明确标记的字段、排序配置文件和其他未明确向智能体解释的工具，它可能会决定发出一个通用查询，从而导致更慢的响应时间和更不相关的信。

惊讶于一个 markdown 文件竟然如此强大？不要惊讶。Vespa 正紧随 Anthropic 的脚步，向[Linux 基金会捐赠智能体技能](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)。文字具有不可思议的力量。

在本次网络研讨会中，我们的目标是更好地了解如何将企业界从对智能体好奇转变为具备智能体赋能。因此，我们正与 Morris 坐在一起，深入了解她的公司所称的“[智能体就绪模式（agent-ready schema）](https://thenewstack.io/agentic-ai-retrieval-problem/)”。最关键的是，我们将探讨修复至少部分上下文差距有多么困难。

Morris 将于 2026 年 12 月 2 日星期三太平洋时间上午 9:30 在“教导 AI 智能体像专家一样搜索”直播中深入探讨这一切，并在整个过程中留出时间回答你的问题。**[立即注册](https://thenewstack.io/webinar/teaching-ai-agents-to-search-like-experts/)加入我们。**

**你将学到什么：**

* 为什么模型能力无法修复检索错误，以及这些错误如何在多步骤任务中复合
* 为什么在更改模型之前，你应该检查智能体实际检索到了什么
* 为什么面向人类的搜索工具对智能体来说是不够的
* “智能体就绪模式”和“模式到技能”如何帮助智能体使用正确的字段、过滤器和排序策略构建查询