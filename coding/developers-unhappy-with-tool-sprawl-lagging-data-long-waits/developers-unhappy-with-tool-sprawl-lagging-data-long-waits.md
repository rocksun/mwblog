
<!--
title: 开发者对工具蔓延、数据滞后、长时间等待感到不满
cover: https://cdn.thenewstack.io/media/2025/02/5c86d3ac-dev-portal-2.jpg
-->

根据 Port 发布的最新调查，内部开发者门户尚未解决工程团队面临的一些最具挑战性的瓶颈。

> 译自 [Developers Unhappy With Tool Sprawl, Lagging Data, Long Waits](https://thenewstack.io/developers-unhappy-with-tool-sprawl-lagging-data-long-waits/)，作者 Jennifer Riggins。

在过去的几年里，科技行业加速了整合工具和提高自动化的努力，旨在减轻降低开发者速度的认知负担。

[内部开发者门户](https://thenewstack.io/internal-developer-portals-can-do-more-than-you-think/)已经成为一种有效的方式，通过标准化和更好的服务发现来消除这种复杂性。

然而，根据[Port](https://www.getport.io/?utm_content=inline+mention)的最新“[内部开发者门户状态](https://www.getport.io/state-of-internal-developer-portals)”调查，只有大约一半的组织采用了这种行业最佳实践。这份2025年的报告反映了美国和西欧300名开发者和工程领导的经验。报告发现，无论他们是否有内部开发者门户，三分之二的工程团队仍然需要等待一天或更长时间才能得到运维团队的响应。因为那些[site reliability engineering](https://thenewstack.io/observability/) (SRE) 和 [DevOps](https://thenewstack.io/devops/) 团队都在与他们自己的积压工作作斗争。

无论他们是否使用内部开发者门户，开发者仍然等待太久，他们仍然不信任数据质量，并且他们绝大多数对他们的工具不满意。内部开发者门户的状态无疑揭示了开发者在2025年的经历。

## 对开发工具的总体不满

开发人员的生活中运维工作太多了。

这些不仅仅是功能请求。开发人员的日常工作流程仍然依赖于与其他团队联系来完成标准任务。事实上，该报告发现，27%的开发人员必须为每个[Infrastructure as Code](https://thenewstack.io/introduction-to-infrastructure-as-code/)实例打开一个pull request。另有20%的工程师仍然处理自己的运维工作。

但即使是那些拥有某种自助服务工作流程的人也不喜欢它。高达94%的受访者表示他们对自己的自助服务工具不满意，其中最大的挫折是：

- 创建云资源，48%的受访者提到。
- 确定合规性，44%。
- 搭建新服务或API，44%。

部分原因是工具的数量太多——绝大多数受访者需要在六个或更多工具之间跳转。这些工具通常涉及不帮助开发者交付价值的运维任务。此外，虽然人们正在努力构建更好的开发者体验，但组织仍然很少将内部开发者视为客户，并将[他们的平台视为产品](https://thenewstack.io/how-to-build-an-internal-developer-platform-like-a-product/)。

由于工具蔓延——软件开发者面临的大量工具选择，这导致75%的开发者每周浪费6到15个小时。导航和集成所有选项会对[developer experience](https://thenewstack.io/can-devex-metrics-drive-developer-productivity/)产生负面影响，破坏流程，加重认知负担并增加反馈时间。

另一方面，并非所有手动审批都在拖慢开发者的速度。几乎一半的开发者可以创建云资源、确定合规性和/或搭建新服务。略高于三分之一的人可以创建一个新的[Kubernetes](https://thenewstack.io/kubernetes/)集群。但是，这真的是软件开发者应该关注的重点吗？

在据称工具整合的时代，仍然存在惊人的蔓延，自动化步骤的数量很少。

## 没有单一的事实来源

更糟糕的是，一半的受访者表示他们不信任其中心数据存储库的质量。

虽然对数据质量的一些怀疑是明智的，但只有3%的受访者认为他们组织的元数据是完全值得信赖的。正如报告指出的那样，如果开发者觉得他们不能依赖元数据，他们就会开始依赖DevOps、SRE或其他团队来获取他们的机构知识。这是不可扩展的。

报告还发现，更糟糕的是，不信任数据质量的开发者明显多于他们的工程领导，这表明与开发者体验的现实脱节。
“内部开发者门户通过集中信息、标准化格式和确保实时准确性来提高元数据质量和信任度，”Port 的产品营销负责人 [Jim Armstrong](https://www.linkedin.com/in/jdarmstro/) 告诉 The New Stack。 他说，当数据量扩大时，这一点尤其重要，因为手动更新是不可持续的。

令人惊讶的是，在回复的工程组织中，仍有 17% 的组织使用电子表格来跟踪其微服务数据。 另有 25% 的受访者表示他们使用配置管理数据库 (CMDB) 或企业资产管理 (EAM) 系统。 Armstrong 说，这两种方法都不能很好地扩展，因为这些解决方案难以处理更大的数据量，需要手动更新，而这些更新只能反映时间上的快照，而不是实时状态。

“如果没有可靠的事实来源，开发人员就会对数据产生怀疑，导致效率低下和不必要的来回沟通，”Armstrong 说，而且软件资产和所有权的记录往往不完整或不准确。

这也意味着开发人员平均需要频繁地手动更新软件资产的元数据。

另一方面，超过一半的受访组织选择了内部开发者门户或 [Backstage](https://github.com/backstage/backstage) 开源框架来创建自己的开发者门户。 内部开发者门户利用 API 和插件来确保元数据自动保持准确和可信。

“门户通过自动聚合和更新信息来解决这个问题，让开发人员和其他用户可以获得服务、所有权和依赖关系的最新视图，”Armstrong 说。“通过消除过时或冲突的元数据，门户确保团队可以信任他们每天依赖的信息。”

## 标准？什么标准？

今年报告中最令人担忧的发现也许是开发人员对其组织标准的完全不清楚。 超过一半的受访者表示他们不知道这些标准，而另有三分之一的受访者则以神秘的“中立”回应。

由于标准对每个组织来说都是独一无二的，因此内部开发者门户通常被用作简化或强制合规的方式，以及提高对标准的认识。 但是，Port 调查的所有开发人员和工程领导者都发现了他们认为其组织的工程流程不符合的标准差距——但是，他们又不确定。

“虽然许多组织使用类似的工具组合，但他们的开发人员应该如何使用这些工具——以及编码标准、生产质量的定义、合规性要求和法律法规——差异很大，”Armstrong 说。

“门户必须与这些特定标准保持一致，确保每个用户只看到与其角色、职责和组织更广泛的治理框架相关的内容。”

这意味着不要用所有的规则淹没你的开发人员——尽管要用所有的规则来执行它们。 他继续说，团队应该实时了解他们负责和授权处理的任何事情，包括未完成的任务、功能请求、错误和漏洞——以及谁在处理什么。

“门户还应该显示与我的工作相关的组织标准，清楚地表明我是否符合期望或未达到期望，以及我需要采取哪些步骤才能保持合规，”Armstrong 说。“这种程度的个性化确保开发人员可以专注于他们的工作，而无需不断搜索信息或猜测哪些信息适用于他们。”

## 门户不是万能药

只有 22% 的受访者报告说，他们的问题平均在一天内得到解决。 如果团队采用了内部开发者门户，这个数字会增加到 30%——但这并不是一个巨大的改进。

采用内部开发者门户不会自动缩短解决时间。 Armstrong 指出了通过内部开发者门户改进所有这些数字的一些方法：

- **工作流程自动化。** 门户必须支持自助服务操作，开发人员可以在其中发起和完成请求——无需人工干预。
- **开发者工作流程。** 许多组织仍处于门户采用的初期阶段，这意味着门户创建者应优先考虑和衡量开发者工作流程的优化。
- **建立信任。** 这些开发团队已经习惯了手动审批和不可靠的数据。 关键在于规划和沟通自动化前后的步骤，并逐步消除瓶颈——而不是像打开电灯开关一样中断开发人员的工作流程。

如有疑问，请在采用内部开发者门户之前、期间和之后与您的工程师交谈。 从简单入手，解决他们最关心的问题，并在此基础上发展您的计划。 只有这样，您才能提高内部开发者门户的采用率——并重建对开发者工具的信任。
