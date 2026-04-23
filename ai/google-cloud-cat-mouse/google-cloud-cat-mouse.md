<!--
title: 谷歌：让AI防御跑赢AI攻击
cover: https://cdn.thenewstack.io/media/2026/04/2a5d3621-adriandra-karuniawan-kqfr6agv0s-unsplash-scaled.jpg
summary: 谷歌通过推出新型AI安全智能体并整合Wiz的能力，应对AI驱动的快速攻击。这些工具旨在自动化多云环境下的威胁狩猎与修复，确保防御速度能与AI漏洞利用相匹配。
-->

谷歌通过推出新型AI安全智能体并整合Wiz的能力，应对AI驱动的快速攻击。这些工具旨在自动化多云环境下的威胁狩猎与修复，确保防御速度能与AI漏洞利用相匹配。

> 译自：[Google wants AI defense to be as fast as AI offense](https://thenewstack.io/google-cloud-cat-mouse/)
> 
> 作者：Frederic Lardinois

目前AI安全的核心问题在于，攻击者正利用AI模型在数小时内发现并利用零日漏洞，而防御者往往仍处于手动分类警报的阶段。

谷歌云在周三的 Next ’26 大会上给出的对策是，针对这一问题投放新型AI驱动的安全智能体——并且从长远来看，还包括其斥资320亿美元收购的 Wiz。该公司的赌注很明确，也是我们最近经常听到的观点：防御必须像进攻一样具备智能体化特征——而且必须跨越每一个云平台。

> 防御必须像进攻一样具备智能体化特征——而且必须跨越每一个云平台。

“漏洞存在”到“野外利用”之间的时间窗口正在缩小。
Anthropic 的 Claude Mythos 预览版于4月初发布，并通过 Project Glasswing 向大约40个组织开放，它可以[自主发现并利用零日漏洞](https://thenewstack.io/claude-mythos-preview-simulation/)。Anthropic 认为该模型对公众发布过于危险，但从长远来看，AI厂商不会一直雪藏此类模型。

值得注意的是，谷歌是 Glasswing 的合作伙伴之一。该模型可在周三前被称为 Vertex AI（现更名为 Google Gemini Agent Platform）的平台上用于防御用途，安全团队可以将其指向自己的基础设施，并在攻击者之前发现可利用的缺陷。不过，谷歌目前尚未在自己的任何产品发布中使用它。

## 谷歌云新增了哪些内容

谷歌正在其云原生安全信息和事件管理（SIEM）及安全编排、自动化和响应（SOAR）平台——Google Security Operations 中，新增三个AI智能体（目前均为预览版）。

**威胁狩猎（Threat Hunting）智能体**主动扫描绕过传统基于规则防御的新型攻击模式和对手行为。**检测工程（Detection Engineering）智能体**识别组织检测覆盖范围中的缺口，并自动为威胁场景创建新的检测——将历史上一直由分析师驱动的手工技艺转化为更接近自动化流水线的流程。**第三方上下文（Third-Party Context）智能体**则利用来自外部资源的上下文数据丰富安全工作流。

> “漏洞存在”与“野外利用”之间的时间窗口正趋于零。

这些新增功能构建在现有的**分类与调查（Triage and Investigation）智能体**之上，谷歌称该智能体在过去一年中处理了超过500万个警报。公司表示，该智能体已将通常需要30分钟的手动分析缩短至约60秒。

这四个智能体共同覆盖了大部分安全运营工作流：分类智能体处理初始警报量并过滤掉误报，威胁狩猎智能体寻找规则遗漏的威胁，检测工程智能体填补狩猎发现的缺口，而第三方上下文智能体则引入外部情报将一切有机结合。

## Wiz 带来了什么

谷歌花费320亿美元收购 Wiz，在 Google Cloud Next 上自然也会有一些关于 Wiz 的发布。

在很大程度上，Wiz 并非发布新产品，而是为现有产品提供新功能以及新的集成。与谷歌本身一样，其中许多功能也针对 AI 原生开发生命周期，因为现在有越来越多的代码在未经广泛审查的情况下被推送到生产环境。

有趣的是，Wiz 不仅关注谷歌云，还关注第三方云和生态系统。该公司今年早些时候推出了 AI 应用保护平台（AI-APP），这是其端到端保护 AI 应用的服务。现在，该公司将其支持范围扩展到了 Databricks、AWS Agentcore、Gemini Enterprise Agent Platform、Microsoft Azure Copilot Studio 和 Salesforce Agentforce。

Wiz [自己在2025年的研究](https://www.wiz.io/blog/common-security-risks-in-vibe-coded-apps)发现，20%的“氛围编程（vibe-coded）”应用包含安全风险。从5月开始，一项新的集成将在“氛围编程”服务 Lovable 内部直接运行 Wiz 扫描，在代码交付前发现漏洞和配置错误。

对于专业开发者，Wiz 正在 IDE 和智能体工作流中添加内联 AI 安全钩子（hooks），理想情况下，这些钩子也将在代码提交前捕捉到问题。

对于 Wiz 发现漏洞的情况，现在提供了一种基于智能体的修复功能，允许智能体以拉取请求（pull request）的形式生成针对性的修复方案。

最后一部分解决了影子 AI（shadow AI）问题。Wiz 的动态 AI-BOM（AI 软件物料清单）旨在终结对 Claude Code 等工具的未经授权使用，并能自动盘点环境中每一个 AI 框架、模型和 IDE 扩展。考虑到 AI 编程工具扩散的速度之快，自动盘点几乎是执行任何连贯安全策略的前提条件。