
<!--
title: PostgreSQL与云原生GenAI：4个需要考虑的因素
cover: https://cdn.thenewstack.io/media/2024/12/87e010cd-postgres-vs-cloud-genai.jpg
-->

与云相关的法规、安全和财务问题促使许多人权衡在本地和混合数据库上构建生成式AI的优势。

> 译自 [PostgreSQL vs. the Cloud for GenAI? 4 Things To Consider](https://thenewstack.io/postgresql-vs-the-cloud-for-genai-4-things-to-consider/)，作者 Valeria Bogatyreva。

生成式AI（GenAI）已展现出重塑各行各业的潜力，有望提高生产力、接管运营任务并推动营收增长。根据[德勤2024年企业生成式AI现状报告](https://www2.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions.html/#introduction) ，80%拥有先进AI专业知识的企业计划增加AI能力方面的支出。

然而，尽管GenAI的光环闪耀，企业也意识到AI项目并非易事。随着公司继续争相利用GenAI的能力，安全和数据管理方面新的挑战和机遇正在出现。


## 主流AI开发模式的挑战

在开始[GenAI之旅](https://thenewstack.io/ai/)之前，需要巨额投资来现代化遗留系统并解决数据相关问题。然而，大多数公司，包括财富500强企业，都在[使用数十年前构建的技术](https://www.techradar.com/pro/fix-it-even-if-it-aint-broke-the-price-of-legacy-technology)，这些技术通常不适合处理AI工作负载。

从遗留软件过渡成本高昂，并可能导致严重的停机和中断。与此同时，公司迫切希望看到投资回报率 (ROI)：近一半的美国生成式AI决策者预计AI投资将在[三年内获得回报](https://www2.deloitte.com/content/dam/Deloitte/us/Documents/consulting/us-state-of-gen-ai-report.pdf)——考虑到所涉及的复杂性，这是一个激进的时间表，并且忽略了挑战的现实。

云计算的可扩展性和快速配置使其成为部署AI模型的首选。然而，云计算的成本效益承诺往往与现实相冲突。支出往往分散且难以控制，许多企业已经采用财务运营([FinOps](https://thenewstack.io/finops-what-is-it-and-why-should-developers-sign-on/))框架来管理成本。

许多企业都担心使用第三方云服务可能带来的威胁，包括数据主权法、法规遵从性和AI模型训练期间敏感信息泄露的担忧。这些因素可能使本地和混合解决方案更具吸引力。德勤预测，到2025年，全球约有一半的企业将[增加本地AI开发模型](https://www2.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions.html#introduction)。因此，虽然云服务仍然至关重要，但企业正越来越多地投资于本地硬件，以保护知识产权、遵守法规并降低数据泄露的风险。


## 如何为GenAI选择合适的数据库

虽然AI创新的道路充满挑战，但这绝非不可能。成功的秘诀之一是为您的用例选择最佳平台，对于许多用例而言，这意味着采用可靠、通用的数据库解决方案，例如[PostgreSQL](https://roadmap.sh/postgresql-dba)。

以下是PostgreSQL在GenAI开发中脱颖而出的四个原因：

1. **可扩展性和向量搜索支持**: PostgreSQL支持丰富的原生数据类型，包括向量。向量搜索是AI应用程序的核心需求；它允许企业在不彻底改变其数据库基础设施的情况下对模型进行原型设计和迭代。这不仅降低了成本，而且还加快了开发时间。
2. **无缝集成**: 与迁移到全新的数据库不同，[利用PostgreSQL](https://thenewstack.io/postgresql-17-gets-incremental-backup-sql-queries-for-json)可以实现逐步现代化。企业可以在尝试新的AI功能的同时继续使用熟悉的SQL工具，从而最大限度地减少中断。
3. **开源优势**: Postgres的社区驱动特性有助于确保持续改进和免费访问。而且，由于开源消除了许可证费用，因此它对ROI产生了积极影响。组织还可以选择增强的产品，例如[Percona for PostgreSQL](https://www.percona.com/postgresql)，它提供PostgreSQL的开箱即用版本以及针对企业需求的定制支持。
4. **部署自由**: 使用PostgreSQL和[Percona Everest](https://www.percona.com/software/percona-everest)等工具，企业可以在最合适的地方部署AI项目——本地、私有云或混合方法——以降低数据泄露的风险。

## AI成功因素

我们从客户那里了解到，成功的生成式AI方法包含三个因素：快速开发、低成本失败和有效扩展。[了解更多](https://learn.percona.com/comprenhensive-postgis-support) Percona 如何帮助您实现所有这些。
