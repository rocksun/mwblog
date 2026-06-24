<!--
title: “供AI智能体遨游的细微差别数据湖”：AWS Context重塑推理能力
cover: https://cdn.thenewstack.io/media/2026/06/dc5e258c-greg-daines-scaled.jpg
summary: AWS发布了新服务AWS Context，旨在通过将企业分散的数据映射为知识图谱，为AI智能体提供治理后的业务规则与领域知识，从而提升AI的逻辑推理与决策能力，并确保数据访问的安全合规。
-->

AWS发布了新服务AWS Context，旨在通过将企业分散的数据映射为知识图谱，为AI智能体提供治理后的业务规则与领域知识，从而提升AI的逻辑推理与决策能力，并确保数据访问的安全合规。

> 译自：[“A data lake of nuance for AI agents to swim in”: AWS Context gets shipshape on reasoning](https://thenewstack.io/aws-context-knowledge-graph-agents/)
> 
> 作者：Adrian Bridgwater

**AI消耗了[大量数据](https://thenewstack.io/clario-data-enterprise-ai-rot/)，但在智能体情报的世界里，这种“自助餐式”的数据终将失去其原本的风味。** 仅仅增加数据库、数据仓库和数据量的纯粹规模，并不一定能丰富任何给定AI功能的推理能力。

而[上下文（Context）](https://thenewstack.io/why-agentic-ai-needs-a-context-based-approach/)却可以。

我们知道，智能体的智能程度取决于它们所能访问的上下文。为了将上下文的纳入过程编纂进AI的算法逻辑中，技术供应商们一直在大肆宣扬[使用知识图谱的优点](https://thenewstack.io/how-knowledge-graphs-make-data-more-useful-to-organizations/)，以使他们的数据对智能体目的更加有用。

AWS 对这个故事再熟悉不过了。该组织的庞大数据中心足迹代表其客户托管了海量的上下文，但这些上下文通常以原始和非结构化的形式存在于数据湖、数据仓库、数据湖仓、数据库和数据流中。它也渗透在智能体引擎很少能访问到的、几乎没有记录的制度性知识中。

这一切都解释了为什么这家云巨头在今天的[AWS纽约峰会](https://aws.amazon.com/events/summits/new-york/)上推出了[AWS Context](https://www.aboutamazon.com/news/aws/aws-summit-nyc-2026-ai-agents)。这是一项新服务，可自动将企业现有数据中存在的关系映射为知识图谱，并提供智能体搜索，以便组织中的AI智能体能在运行时访问这些经过治理的数据关系、业务规则和领域知识。

但将所有这些交织在一起是一项艰苦的工作。知识图谱的运作需要的不仅仅是简单的关键词匹配；它们需要结构和语义遍历。这意味着它们需要在各种信息孤岛和存储库之间进行多次跳转，以便它们能够聚合上下文，并（例如）能够解释为什么网络安全漏洞A是系统受损B的一个因素，而B与代码库C有核心依赖链接，C在应用程序D中执行并可能导致用户X、Y和Z离线。那么AWS是如何做到这一点的呢？

## 细微差别与信息的数据湖

AWS技术副总裁（数据与分析）Mai-Lan Tomsen Bukovec告诉*The New Stack*，AWS Context提供了一个“供AI智能体遨游的细微差别与信息的数据湖”，以便它们能正确推理并为业务做出正确的决策。

> “这与人类的工作方式没有什么不同。当我们采取行动时，我们依赖于我们自己关于领域、先前决定及其结果以及其他信息的上下文。” – Mai-Lan Tomsen Bukovec, AWS.

“这与人类的工作方式没有什么不同，”Tomsen Bukovec说。“当我们采取行动时，我们依赖于我们自己关于领域、先前决定及其结果以及其他信息的上下文。有了AWS Context，AI智能体就可以在知识图谱和开放数据格式中拥有其业务中每种数据形式的所有细微差别。AWS Context将成为AI智能体仅仅采取行动与做出正确决定之间的区别。”

鉴于可以选择采用这项新服务，软件工程师将需要制定行动计划并确定首先要做什么。对于AI开发人员和数据科学专业人士来说，这提出了一个问题：在使用AWS Context功能为上下文感知智能体准备现有企业数据时，应优先考虑什么，以及他们如何控制哪些数据被（以及不被）喂给这只“野兽”。

值得庆幸的是，似乎存在控制选项。

“如果开发人员想要从AWS Context中排除信息，他们将有能力阻止某些数据集（如测试数据或沙盒环境）被包含在AWS Context中，”Tomsen Bukovec解释道。“因为AWS Context会随着数据资源之间关系的变化而不断更新，AI智能体无需AI开发人员的任何干预即可获得最新的上下文，并有权设置护栏来排除智能体不应采取行动的内容。”

## 开发人员应该信任这项技术吗？

AWS Context扩展了运行[Amazon Quick](https://aws.amazon.com/quick/)的相同知识图谱技术，这是该组织的AI工作助手，可以“连接分散的工作”，跨越应用程序和资源，包括Slack、Microsoft Teams和Outlook、CRM、数据库和文档。

那么，软件开发人员应该在这里投入信任吗？毕竟，即使被捕获和连接后，并非所有的业务上下文都有用。一些情境化内容可能被破坏、薄弱、碎片化，对业务没有成效？AWS是否面临着在不考虑构成它的数据在业务有用性方面如何量化的情况下封装上下文的风险？

AWS已经考虑到了这个因素。

因为AWS Context使用了驱动Amazon Quick的相同知识图谱技术，它可以从使用模式中学习，使每次交互更智能。AWS Context表示，它正在将个人知识图谱扩展为组织知识图谱，即一个共享的、受治理的上下文层，组织中的智能体和应用程序可以从中汲取信息。

> “开发人员可以治理和塑造一个动态且智能的上下文层，AI智能体依赖它来做出正确的决定——AI智能体不仅会随着模型改进而变得更聪明——它们会因为触手可及的大量经过策划的上下文而变得更聪明。” – Tomsen Bukovec.

“AWS Context提供了一个[图和开放数据格式的上下文](https://thenewstack.io/aws-why-we-support-sustainable-open-source/)数据湖，”Tomsen Bukovec澄清道。“这意味着各地的AI开发人员可以在数据层使用功能来治理和塑造一个动态且智能的上下文层，AI智能体依赖它来做出正确的决定。通过这一变化，AI智能体不仅会随着模型改进而变得更聪明——它们会因为触手可及的大量经过策划的上下文而变得更聪明。”

## 超越用户个人图谱的策划知识

现有的Amazon Quick用户将看到，当启用AWS Context时，Quick的智能体可以访问更广泛的企业知识图谱，包括跨系统关系、业务规则和超越任何单个用户个人图谱所能提供的策划上下文。

Tomsen Bukovec还表示，AWS Context使用的智能体越多，它就越聪明。随着智能体查询图谱，它会观察哪些来源产生正确的结果，智能体依赖哪些连接路径，以及应用了哪些策划规则。它按实际使用情况对来源进行排名，并在组织内共享它所学到的东西，因此当一个智能体发现正确的连接路径或解决模式歧义时，其他智能体也会获取它，而无需人类重新策划图谱。

你投入生产的任何智能体都会引发治理问题：它可以触及哪些数据，以及你能否准确展示它访问了什么内容以及在谁的授权下？该组织解释说，AWS Context通过使每个查询都具有身份感知能力来回答这两个问题。

每个调用都设计为继承调用用户的身份访问管理 (IAM) 和[Lake Formation权限](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-reference.html)，因此智能体只能看到并遍历其身份被授权访问的关系。由于访问是通过身份运行的，因此每次交互都是可审计的。安全和合规团队可以使用相同的控制措施来验证智能体访问了什么内容以及在何种授权下。

## AWS Glue Data Catalog

与今天AWS Context到来相关的消息是，该公司还宣布了[AWS Glue Data Catalog](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/aws-glue-data-catalog.html#)的业务上下文和语义搜索功能预览，这是该公司用于跨各种数据源的所有数据资产的集中式元数据存储库。新功能旨在使人类和AI智能体更容易发现和理解数据。

同样在该产品流中，AWS现在提供了Glue Data Catalog中技能资产的预览，这是一项旨在允许“数据生产者”（AWS应用于任何创建数据的人的一个有些随意的术语，但最可能是数据库管理员或开发人员）创建技能资产的服务。

将技能资产关联到数据资产，为智能体提供了额外的上下文和指令，它们可以逐步检索这些内容以使用特定数据，而无需每次提示都重新教授每个智能体。

## 上下文工程的复兴

AWS的这一新举措是否会预示着上下文工程作为数据科学的一个子学科的诞生（或者可能是复兴，[行业已经讨论这种方法](https://thenewstack.io/context-engineering-the-foundation-for-reliable-ai-agents/)有一段时间了）？这很有可能……如果确实如此，随着我们在企业数据栈中交织越来越复杂的相互关系结构，它可能会将基于角色的多智能体编排也拖入这场混战中。

如果AWS或确实其他超大规模云厂商或主要的边际模型公司开始收购更多的多模型图结构公司和向量数据库专家，那可能是一个迹象，表明事情正围绕着大型上下文工程而巩固。

在此期间，建议在细微差别的上下文化数据湖中扬帆起航的开发人员穿上救生衣。