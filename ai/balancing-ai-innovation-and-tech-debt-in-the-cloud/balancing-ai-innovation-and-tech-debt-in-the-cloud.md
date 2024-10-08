
<!--
title: 在云端平衡AI创新与技术债
cover: https://cdn.thenewstack.io/media/2024/08/d3257f97-governance.jpg
-->

通过细致的治理，组织可以利用人工智能的力量，同时保持安全、合规且经济高效的云环境。

> 译自 [Balancing AI Innovation and Tech Debt in the Cloud](https://thenewstack.io/balancing-ai-innovation-and-tech-debt-in-the-cloud/)，作者 Ido Neeman。

近年来，特别是自 2022 年 11 月 ChatGPT 发布以来，人工智能以空前的速度推动着创新，改变着各个行业和企业的运营方式。如今，每一家公司及其高管团队都[认识到人工智能](https://thenewstack.io/ai/)必须成为其未来战略的一部分，否则将被淘汰。这就是我们目睹一场竞赛，旨在基于人工智能驱动的所有事物提供最大可能的创新。这在很大程度上是人工智能民主化的副产品，它使人工智能能够被大众使用，从用户到创新者。

如今，技术高管们正在告诉他们的工程团队：“我们现在需要一个人工智能故事”，而很少考虑如何在他们的系统中最终实现这一点。这场竞赛是真实的，它有自己的一套独特的影响，特别是对于那些管理云基础设施的人来说。这场人工智能热潮正在以前所未有的规模创造人工智能技术债务，了解这些影响对于确保我们的云环境保持高效、安全和经济高效至关重要。

## 人工智能的双重影响

作为一家云资产管理公司，我们通过我们的遥测数据见证了人工智能的颠覆，越来越多的公司正在使用人工智能驱动的云服务和资产。从 GPU 到托管的[检索增强生成 (RAG) 数据库](https://thenewstack.io/freshen-up-llms-with-retrieval-augmented-generation/)、[大型语言模型 (LLM)](https://thenewstack.io/llm/) 以及其他所有内容，所有这些人工智能创新都是建立在当今最昂贵的云资源之上。我们敦促您检查托管图数据库的成本。

人工智能的影响是双重的，既影响消费者，也影响支持它的基础设施。对于消费者来说，越来越需要确保人工智能生成的代码能够识别并兼容他们的环境。这包括确保人工智能驱动的应用程序符合现有的策略、安全协议和合规性要求。

在基础设施方面，人工智能需要大量的资源和可扩展性。最近的[Datadog“云成本现状”2024 年报告](https://www.datadoghq.com/state-of-cloud-costs/) 强调，随着组织尝试使用人工智能，GPU 实例的支出增长了 40%，其中仅 GPU 实例的支出就占计算成本的 14%。Arm 支出在过去一年中翻了一番，这是人工智能驱动的开发的新支柱，是 AWS 的 Graviton 等处理器（为这场人工智能革命提供动力）的架构选择。

这种对资源需求和云支出的激增会导致许多 CTO 开始抱怨的人工智能技术债务。我们正处于人工智能开发速度往往超过组织有效管理和优化它的能力的阶段。这可以从启动昂贵的机器而没有适当的拆卸或清理（导致云成本失控）中看到。这与数据没有得到妥善管理和输入到模型和机器中，这些模型和机器后来以意想不到的方式不当暴露数据，只是其中一些例子。

## 平衡创新与治理

虽然人工智能为创新提供了令人难以置信的机会，但也突出了重新评估现有治理意识和框架以纳入人工智能驱动的开发的必要性。历史上，[DORA 指标](https://thenewstack.io/despite-the-hype-engineers-not-impressed-with-dora-metrics/) 被引入以根据速度和安全这两个关键类别来量化精英工程组织。如果完全忽略安全方面，速度本身并不能表明精英工程。在考虑人工智能驱动的应用程序的安全时，不能忽视人工智能开发。

现在比以往任何时候都更加重要，在技术债务失控和数据隐私被不再受人类控制的机器侵犯之前，根据数据隐私、治理、FinOps 和策略标准运行人工智能应用程序至关重要。当然，数据不是唯一面临风险的东西。成本和故障也应该考虑在内。

如果上个月的[CrowdStrike 停机](https://www.firefly.ai/blog/the-misconfig-heard-around-the-world-why-ops-is-always-business-critical/) 教会了我们什么，那就是即使是看似简单的代码更改，如果没有得到适当的发布和治理，也会在全球范围内导致整个关键任务系统崩溃。这包括执行严格的数据策略、注重成本的策略、合规性检查和对人工智能相关资源的全面标记。
JFrog 近期收购 [Qwak.ai](https://investors.jfrog.com/news/news-details/2024/JFrog-to-Acquire-Qwak-AI-to-Streamline-AI-Models-from-Development-to-Production/default.aspx) 是另一个迹象表明，拥有足够资金的公司将抢购新兴的 AI 玩家，以更快地将竞争对手的 AI 解决方案推向市场。如今，超过 50% 的程序员定期利用 AI 来编写或增强代码，任何承诺在该领域提供更高敏捷性的工具和平台都将受到更密切的审查和收购兴趣。敬请关注这方面的更多进展。

最近 AI 驱动的研究和开发中出现的一个有趣数据点是代码质量（与 DORA 指标相关）。GitClear 的这份 [最新报告](https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality) 表明，AI 正在对代码质量产生负面影响。报告指出，代码 churn 明显增加，代码重用率大幅下降。可以在 [此处](https://devops.com/does-using-ai-assistants-lead-to-lower-code-quality/) 阅读有关这些发现的有趣文章。

最近对 AI 的一些批评表明，基于文本的 AI 助手很棒，因为有大量基于文本的数据可供分析。这就是为什么 AI 助手能够增强典型文本并在生成创意或功能性文本方面取得高于平均水平的结果。然而，代码并非如此。

绝大多数可用于 AI 建模的代码实际上低于平均水平。这些包括有抱负的工程师和学生的早期项目，以及未用于商业用途的开放代码。生产高性能、经济高效且高质量的代码需要多年的领域专业知识。然而，这些类型的存储库通常被解析和收集用于基于代码的 AI 大型语言模型 (LLM)，这使得 AI 辅助代码质量在目前低于高级工程师的代码质量。高质量的代码存储库通常是封闭源代码，属于商业应用程序，[LLM 无法用于数据建模](https://thenewstack.io/chatting-with-data-llms-are-transforming-aiops/)。

这强调了将 AI 驱动的创新与强大的治理结构相结合的重要性。云资产管理人员必须配备必要的工具和知识，才能在其上下文中有效地监控和管理 AI 工作负载，了解他们管理的复杂系统的细微差别。这包括确保对 AI 操作的可见性，并严格遵守治理策略。

## 为 AI 的未来做好准备

展望未来，我们必须问：在运行 AI 方面，后天意味着什么？对于没有开发自己的 LLM 或模型的组织来说，重点将转移到管理昂贵的云基础设施。这需要与任何其他云操作一样，牢记治理和成本效益。

组织必须制定策略，在 AI 带来的创新与对更大、甚至更细致的治理的需求之间取得平衡。这包括利用 AI 感知工具和平台，这些工具和平台提供对 AI 资源的可见性和控制。通过这样做，公司一方面可以将 AI 的力量引导到更高层次的目标，同时保持安全、合规且经济高效的云环境。

随着 AI 继续推动创新，其对云基础设施和治理的影响不容忽视。将 AI 的优势与有效的管理和治理实践相结合是确保由新兴云技术驱动的可持续 AI 创新的关键。
