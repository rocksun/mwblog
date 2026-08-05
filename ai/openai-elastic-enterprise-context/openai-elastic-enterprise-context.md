<!--
title: OpenAI联手Elastic，破解企业AI无法忽视的难题
cover: https://cdn.thenewstack.io/media/2026/07/16611805-5010-xezwmxxlarw-unsplash-scaled.jpg
summary: OpenAI与Elastic深化合作，通过将Elasticsearch的检索与权限管理能力与OpenAI推理模型结合，有效解决了企业AI在数据上下文、可观测性及安全方面的落地瓶颈，大幅提升了检索精度并降低了推理成本。
-->

OpenAI与Elastic深化合作，通过将Elasticsearch的检索与权限管理能力与OpenAI推理模型结合，有效解决了企业AI在数据上下文、可观测性及安全方面的落地瓶颈，大幅提升了检索精度并降低了推理成本。

> 译自：[OpenAI and Elastic are tackling the AI problem enterprises can’t ignore](https://thenewstack.io/openai-elastic-enterprise-context/)
> 
> 作者：Amanda Caswell

**企业AI存在上下文问题，这是不可否认的事实**。尽管前沿模型能力惊人，但如果它们无法安全地访问企业实际所需的信息，其价值就大打折扣。这正是[所谓“上下文债务”引发的问题](https://thenewstack.io/vibe-coding-context-debt/)，也是OpenAI和Elastic在周四宣布扩大合作所要解决的挑战。

## 当检索遇上推理

通过将OpenAI的推理模型与Elasticsearch的搜索、检索和权限功能相结合，这两家公司正在正面应对生产级AI中最大的瓶颈之一。通常，信息散落在文档、支持工单、日志文件、安全警报以及企业内部多年的知识积累中。但其中大部分信息受到基于角色的访问控制（RBAC）保护，AI代理只有在拥有查看权限的情况下才能检索这些信息。

这就是Elastic发挥作用的地方。[OpenAI正在依赖Elasticsearch](https://www.elastic.co/blog/elastic-openai-partnership)来呈现企业数据，同时遵守现有的访问控制，确保模型仅针对请求用户明确授权查看的数据进行推理。

> AI系统在开始推理之前，能越精准地找到所需信息，其成本就越低，准确性往往也越高。

自2023年以来，两家公司都提供了基础连接器，但这次更深度的集成涵盖了上下文感知AI代理、代理可观测性和代理安全性这三个核心运营前沿。

AI系统在开始推理之前，能越精准地找到所需信息，其成本就越低，准确性往往也越高。这一观点[不仅延伸到推理定价，还涉及到关于代理如何管理上下文的架构级决策](https://thenewstack.io/agentic-ai-token-costs/)。

为了展示其在实践中的效果，Elastic分享了其内部基准测试的结果。该公司表示，Elasticsearch在检索测试中达到了0.89的召回率，同时保持了多租户数据隔离。在另一项使用BrowseComp-Plus基准测试的实验中，Elastic报告称，与标准的RAG（检索增强生成）流水线相比，其预计算的知识指标（Knowledge Indicators）使输入token使用量减少了多达75%，同时将回答准确率从60%提高到了92%。

## 自主代理的可观测性

此次合作还直接扩展到了系统可观测性。随着工程师将自主代理投入生产，对模型行为、token消耗和运行时故障模式的可见性成为了流程中的关键部分。

Elastic整合了OpenAI API使用指标和审计记录，使SRE团队能够在统一的控制平面内监控token使用情况、模型活动和基础设施遥测。因此，当事件发生时，Elastic的代理调查工作流会将这些信号关联起来，以确定根本原因并建议后续步骤，这减少了开发人员在日志和指标之间频繁切换的时间。

## 安全警报转化为攻击链

在安全方面，此次集成为企业安全运营中心（SOC）提供了直接的实际效用。安全分析师经常面临数千条孤立的警报。利用OpenAI的模型，Elastic Security驱动了一个“攻击发现”（Attack Discovery）引擎，能够自动将分散的警报合成为映射到MITRE ATT&CK框架的连贯攻击链。这使分析师有机会审查有据可查的叙述，而不是筛选原始日志条目。

> 分析师可以审查有据可查的叙述，而不是筛选原始日志条目。

早期采用者报告了可衡量的运营改进：

* **Visa：** 作为SIEM现代化计划的一部分，Visa实施了一个带有人机协同验证的代理工作流，将高风险大型机检测的分类时间从15分钟缩短至几秒钟，同时保留了完整的审计记录，这正是[每个AI代理工作流所要求的有据可查的决策路径](https://thenewstack.io/agent-evidence-packet-analytics/)。
* **Airtel：** 该公司的托管安全团队报告称，结合使用Attack Discovery和Elastic Agent Builder，警报分类速度提高了40%，整体事件调查时间缩短了30%。

展望未来，双方的合作将接入OpenAI的Daybreak Cyber计划，并计划将专业的安全模型集成到Elastic Security工作流中，以实现事件响应建议的自动化并动态生成检测规则。

> Elasticsearch花了十多年时间为人类查询建立企业数据索引。现在，它正在为自主代理履行同样的职责。

## 作为上下文引擎的搜索引擎

Elasticsearch花了十多年时间为人类查询建立企业数据索引。现在，它正在为自主代理履行同样的职责。通过支持[模型上下文协议 (MCP)](https://thenewstack.io/api-vs-mcp-incident-management/)、Elastic Agent Builder以及与[OpenAI Codex](https://thenewstack.io/gpt-5-6-codex-user-surge/)的深度集成，开发人员可以直接将代理连接到企业数据源，而无需从零开始构建复杂的授权和检索粘合代码。