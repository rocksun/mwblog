
<!--
title: 为什么中心化AI在企业中会失败：联邦架构的案例
cover: https://cdn.thenewstack.io/media/2025/03/58b3b4df-alex-kotliarskyi-qbpzgqemskg-unsplash-scaled.jpg
summary: 企业AI落地难？集中式AI违背数据治理和安全！联邦架构成解法：数据保留在源系统，利用AI Agent进行域内处理，身份权限传递，合规性无忧。拥抱“Data Mesh”，释放企业级AI潜力，实现“AI-native”！
-->

企业AI落地难？集中式AI违背数据治理和安全！联邦架构成解法：数据保留在源系统，利用AI Agent进行域内处理，身份权限传递，合规性无忧。拥抱“Data Mesh”，释放企业级AI潜力，实现“AI-native”！

> 译自：[Why Centralized AI Fails in Enterprise: The Case for a Federated Architecture](https://thenewstack.io/why-centralized-ai-fails-in-enterprise-the-case-for-a-federated-architecture/)
> 
> 作者：Anant Bhardwaj

随着公司希望从其AI投资中获得价值和投资回报率，一个关键的挑战威胁着这些举措的进行。问题是什么？传统的AI实施[策略需要集中来自不同来源的数据](https://thenewstack.io/choosing-the-right-database-strategy-on-premises-or-cloud/)，这种方法与企业治理策略、安全框架和监管义务相冲突。

根据分析师的调查，[90%的企业已经制定了多云策略](https://thenewstack.io/multicloud-why-its-the-best-choice-for-data/)，数据分布在各种系统中。 这种现实使得传统的“将所有数据复制到一个地方”的方法效率低下，并且对于企业规模的实施通常是完全不可行的。

## 中心化AI系统中的致命缺陷

集中数据会产生多个治理问题，这些问题在规模上变得越来越难以管理。当组织在中央AI存储库中创建来自源系统的新数据副本时，它们会引入重大挑战：

* **数据准确性** ：当AI系统依赖于过时的重复副本时，使用“新鲜”的、及时的的数据具有挑战性。
* **治理复杂性** ：每个[数据副本都会创建另一个必须根据组织策略进行管理的实例](https://thenewstack.io/aws-brings-trusted-extension-support-to-managed-postgres/)。
* **合规性风险** ：当用户数据存在于多个位置时，GDPR的“被遗忘权”和类似法规的执行变得异常困难。
* **访问控制降级** ：源系统中精心设计的权限通常会演变为中央存储库中最低级别的通用控制。
* **安全漏洞** ：集中式数据存储呈现出具有潜在灾难性破坏影响的诱人目标。

最大的挑战在于，对于许多企业而言，即使是将所有数据集中在一个来源中的想法也是不可行的——治理和隐私问题使得这在法律和技术上都是不可能的。

## 联邦架构：以数据为中心的方法

解决方案在于数据工程中一种成功的架构模式：联邦架构，也称为[数据网格设计](https://thenewstack.io/designing-a-data-mesh-to-reign-in-data-sprawl/)模式。 这种方法从根本上重新构想了AI系统与企业数据交互的方式。

在联邦架构中：

1. 数据保留在其所属的源系统中
2. 治理、访问控制和合规性仍然本地化到每个数据域
3. 处理发生在数据所在的，尊重现有安全边界
4. 只有结果会暂时集中起来进行分析和展示

这种模式并非理论上的——像Capital One这样的组织已经成功地大规模实施了[数据网格架构](https://www.capitalone.com/tech/cloud/data-mesh-for-data-governance/)。 这些组织通过将[数据](https://thenewstack.io/python-mqtt-tutorial-store-iot-metrics-with-influxdb/)保留在其自然域中并将计算资源引入数据（而不是相反）来保持治理，同时释放分析能力。

## 联邦系统中的AI代理

联邦方法自然地扩展到AI实施。 联邦AI系统不是由一个中央AI访问所有数据，而是在不同的数据域中部署专门的代理。

在这种模式下：

* 协调层将任务委派给特定于域的AI代理。
* 每个代理都专注于其具有针对性功能的的数据域。
* 代理在本地处理数据，并且仅返回结果。
* 不会在源系统之外创建数据的持久副本。

这反映了有效的组织结构。 如果您是一家公司的CEO，并且您给您的领导团队分配了一项任务，那么不是一个人去任何地方并完成所有工作。 它被委派给具有在其领域中运营的必要专业知识、访问权限和知识的人员。 然后，将信息重新整合在一起并作为结果呈现给CEO。 我们可以对AI代理使用相同的方法。

这种方法使组织能够利用针对特定系统优化的专用AI模型。 例如，Salesforce Einstein可以处理Salesforce数据，而不同的代理可以处理Atlassian数据——每个代理都在其专业领域中运行。

## 联邦AI中的身份和访问控制

这种架构中的一个关键挑战是维护适当的访问控制。 解决方案是“身份传递”——当用户与AI交互时，他们的身份和权限将传递到所有底层系统。

大多数 IT 系统都建立在基于角色的访问控制 (RBAC) 之上，这意味着 AI 系统需要考虑用户的[角色，然后才能确定某人是否可以查看某些数据](https://thenewstack.io/how-time-plays-a-crucial-role-in-aggregating-mobile-data/)类别，例如社会安全号码。当训练数据组合在一起时，这种集中式数据会产生“最小公分母”问题，即所有数据都向最低 RBAC 访问级别开放，从而导致隐私和安全问题。

为了使 AI 系统能够遵守这些控制，需要在访问数据时实时检查这些 RBAC 控制。

在联合系统中，AI 与特定领域的代理协调，每个代理本质上都充当请求用户，从而确保 AI 代理仅访问特定用户有权查看的信息。这意味着：

- 不同用户提出的相同查询会根据用户的角色和权限返回个性化的结果
- 源系统中访问控制的更改会立即反映在 AI 交互中
- 治理仍然存在于旨在执行它的系统中

这种方法无需复制复杂的权限结构或维护多个同步的访问[控制系统——这项任务不可避免地会导致安全](https://thenewstack.io/role-based-access-control-five-common-authorization-patterns/)漏洞。

## 解决合规性和区域数据要求

联合架构为 GDPR 和 CCPA 合规性等监管挑战提供了优雅的解决方案。AI 系统继承了这些功能，因为数据保留在已经实施合规性控制的源系统中。

例如，在处理“被遗忘权”请求时：

1. 该请求像往常一样在源系统中实施
2. AI 系统没有要管理的持久副本
3. 未来的查询会立即反映更新后的数据状态

这种方法对于在不同监管制度下运营的跨国企业尤其有价值。欧洲系统中的数据可以继续遵守 GDPR，而美国系统则遵守当地要求，无需在中央存储库中协调这些差异。

与在[用户数据上微调模型](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/)（创建可能违反删除请求的持久性工件）的系统不同，我们的联合 AI 系统将数据用作运行时上下文。当源数据更改或删除时，后续的 AI 交互会反映这些更改，而无需重新训练模型。

## 超越概念验证

对于许多企业来说，联合架构不是一种选择，而是 AI 停留在有限的概念验证阶段与成为生产能力之间的实际、受治理的差异。如果没有这种方法，组织通常会使用有限的[数据集进行小型试点，永远无法充分发挥 AI 在公司范围内使用不同数据源的潜力](https://thenewstack.io/can-companies-really-self-host-at-scale/)。

通过采用联合 AI 方法，公司可以从所有[数据源的可观测性中获得巨大的价值，并使用 AI 自动化业务流程](https://thenewstack.io/how-event-processing-builds-business-speed-and-agility/)。这不仅让信息安全团队放心，而且使实施成为可能。

通过采用联合 AI 架构，企业可以将其 AI 战略与现有的治理框架、安全要求和合规义务相协调。这释放了 AI 的变革潜力，同时保持了保护其业务和客户的控制。