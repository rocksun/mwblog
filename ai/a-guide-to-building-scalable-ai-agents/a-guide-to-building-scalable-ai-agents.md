<!--
title: 构建可扩展AI智能体：实战指南
cover: https://cdn.thenewstack.io/media/2025/12/c27c9a74-building-scalable-ai-agents.jpg
summary: 本指南介绍如何使用Salesforce Agentforce和Heroku AppLink构建实时决策系统。Agentforce利用AI驱动工作流，结合Heroku扩展定制操作，确保数据安全，提供如机场导航等个性化实时信息，提升用户体验。
-->

本指南介绍如何使用Salesforce Agentforce和Heroku AppLink构建实时决策系统。Agentforce利用AI驱动工作流，结合Heroku扩展定制操作，确保数据安全，提供如机场导航等个性化实时信息，提升用户体验。

> 译自：[A Guide To Building Scalable AI Agents](https://thenewstack.io/a-guide-to-building-scalable-ai-agents/)
> 
> 作者：Doug Sillars

当正确的信息未能及时传达给正确的人时，事情会迅速失控。当系统未被构建为实时响应时，这些时刻就会变得混乱。自动化这种体验不仅仅需要警报或通知；它还需要连接的数据、智能流程以及安全、时间敏感的决策。

本指南将引导您使用 Salesforce Agentforce 和 Heroku AppLink 构建实时决策系统。它将展示 Agentforce 的 AI 驱动工作流程如何响应实时事件，以及 Heroku 的 [AI 平台即服务](https://thenewstack.io/what-is-an-ai-paas-a-guide-to-the-future-of-ai-development/) (PaaS) 如何通过自定义操作和 API 扩展这些流程。其结果是一种个性化的体验，帮助人们自信地访问他们需要的数据，从而即时做出决策。

## 什么是 Salesforce Agentforce？

[Agentforce](https://thenewstack.io/avoiding-the-ai-agent-reliability-tax-a-developers-guide/) 是一个始终在线的应用程序框架，它利用 AI 和组织的 Salesforce 数据来大规模主动执行任务。通过智能地利用您 [Salesforce](https://www.salesforce.com/data/?utm_content=inline+mention) 生态系统中已有的数据，Agentforce 可以构建更适合您用例的强大自动化。由于驱动 Agentforce 的 AI 位于您的 Salesforce 环境中，您无需担心数据安全或客户私人数据泄露。

使用 AI 代理的一种流行方法是构建流程——AI 代理在自动处理和执行任务时遵循的工作流程。以下是一个工作流程示例：


![](https://fastly.jsdelivr.net/gh/bucketio/img0@main/2025/12/09/1765288801331-a83df0f4-5f79-4a2a-8689-3d574369a1f6.png)


*Agentforce 流程示例。*

在这个工作流程中，代理的任务是安排会议，如果有可用时间，代理将为所有参与者安排会议。

## 使用 Agentforce 和 Heroku 定制工作流程

市场上有许多自动化工具，但跨公司边界共享客户数据会增加数据被泄露的风险。将代理式 AI 保留在 Salesforce 内部有助于保护公司数据的安全。

许多常用功能已在 Agentforce 中预构建、预训练并包含在内。使用这些工作流程任务不需要任何编码；它们可以添加到流程中，以加速代理式流程的迭代和构建。但公司通常需要针对特定用例或垂直领域定制流程。

这正是将 Agentforce 与 Heroku 集成变得有价值的地方。Heroku 强大的 AI PaaS 可以通过自定义操作和 API 扩展 Agentforce 工作流程，从而实现 [快速简便的应用程序](https://www.heroku.com/customers) 云部署。Heroku 是 Salesforce 家族的一部分，Salesforce 和 Heroku 的紧密集成使得构建 Agentforce 应用程序更加容易。

[Heroku AppLink](https://devcenter.heroku.com/articles/heroku-integration) 将基于 Heroku [AI PaaS](https://www.heroku.com/blog/heroku-fir-generally-available-new-platform-capabilities/) 构建的服务作为 API 暴露出来，以便在 Salesforce Agentforce 流程中使用。AppLink 执行 Salesforce 的权限和规则，确保 Heroku 应用程序中处理的数据在 Salesforce 生态系统中保持安全。

## 构建 AI 工作流程

为了了解其工作原理，让我们使用 Agentforce 构建一个航空旅行流程。当乘客抵达目的地时，他们需要知道接下来要去哪里。以下是一个可以在 Agentforce 中构建的流程：

* 获取航班的乘客名单。
* 对于每位乘客，查询后续步骤。为简化起见，假设有两种选择：
  + 如果乘客有转机航班：查询航班工具以获取下一航班的起飞时间/登机口信息详情。
  + 如果这是乘客的最终目的地：获取行李领取转盘号。
* 对于任一流程，估算从登机口到目的地的步行时间。
* 识别方向：乘客离开廊桥后是左转还是右转？
  + 如果时间充足，可沿途推销咖啡。
  + 如果时间不足，则提示不应耽搁。
* 在 Salesforce 中查找乘客的电话号码。
* 向每位乘客发送定制的短信，告知他们在机场的后续导航步骤。

乘客无需再听到空乘人员宣布十几个转机信息（反正也没人能听清：“飞往芝加哥的 614 航班将从 <因静电干扰而听不清> 登机口起飞”），也无需匆忙跑向屏幕寻找下一航班，飞机降落时，所需信息将通过短信平静地传达给乘客。

## 构建应用程序

现在我们有了工作流程，我们可以用它在 Agentforce 中构建一个定制应用程序，使用定制的 Heroku 应用程序为代理式 AI 提供支持，并使用 Heroku AppLink 将您的 Heroku 应用程序作为 API 服务在 Salesforce 中公开。

### 1. 定义数据源

让我们对数据源做一些假设：

* 所有客户数据都存储在 Salesforce 中：姓名、地址、手机和电子邮件。
* 客户航班预订也存储在 Salesforce 表中，并与客户数据进行交叉索引。
  + 如果此数据位于另一个数据存储库中，则需要更多的处理，但整体流程将相似。
* 存在一个包含每个机场内所有登机口、行李领取处和重要位置的现有数据集，以及位置之间的近似距离。
  + 机场信息数据集之前已在 Heroku 中创建并部署为 API。

### 2. 创建数据流

为了启动数据流，我们将使用 [Heroku eventing](https://www.heroku.com/blog/heroku-eventing-router-for-your-events/) 服务。Heroku eventing 是一个试点计划，可用于调用 Heroku 应用程序——在本例中是一个代理流程。启用了 eventing 的 Heroku 应用程序的行为类似于 webhook：监听生态系统中特定事件的服务。在飞行过程中运行的另一个自动化流程可以在航班飞行时触发一个“降落”事件。应用程序接收到此事件并开始运行流程。

流程开始时，代理会检索每位乘客的航班清单。它处理航班清单以获取抵达登机口和每位乘客的后续步骤。它可以在 Heroku 应用程序内部运行，也可以在预构建的代理流程应用程序中运行，该应用程序在 Salesforce 中进行并处理 SQL 调用。

收集并解析乘客数据后，我们需要确定机场内部的步行时间。为了获取此信息，我们将在 Heroku 中构建一个与流程交互的定制应用程序。

### 3. 构建 Heroku 应用程序

我们的 Heroku 应用程序将通过 [AppLink 暴露给 Agentforce](https://devcenter.heroku.com/articles/getting-started-heroku-applink-agentforce)。AppLink 将您的 Heroku 应用程序转变为一个仅在 Salesforce 生态系统内部运行的自定义 API。使用 AppLink 的应用程序经过配置后，将安全地连接到您的 Salesforce 组织，以确保数据完整性。此应用程序可以连接到多个 Salesforce 组织，但必须在每个组织中单独进行配置。

由于此应用程序构建在 Heroku 的 AI PaaS 上，开发团队无需管理任何基础设施或 DevOps。它都已包含在内。这使得开发人员更容易采用强大、复杂的 [云原生技术](https://thenewstack.io/cloud-native/ "云原生技术")，例如 Kubernetes。

Heroku 集成的应用程序必须遵循 [OpenAPI 规范](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/) 才能正确集成。我们假设有四条数据发送到此 API：`airport code`、`arrival gate`、`destination` 和 `time of next flight`。

只有前三个参数是必需的（前往行李提取处的乘客不会有 `time of next flight`）。我们的应用程序将包含一个 OpenAPI 规范（通常称为 Swagger JSON），该规范将由流程使用。

对于航班上的每位乘客，都会调用 Heroku 应用程序来处理他们在机场的行程。它可能会使用 [Google](https://cloud.google.com/?utm_content=inline+mention) 地图来计算步行时间，或者使用带有实时数据的机场地图服务。数据如何处理和评估在这里并不重要。重要的是 Heroku 应用程序安全地处理航空公司的客户数据，因此它永远不会离开 Salesforce 组织。

Heroku 应用程序的输出是数据：转机需要步行多长时间，以及关于乘客需要多快完成转机的个性化提示。这将作为 JSON 对象返回给 Agentforce 流程。

### 4. 完成流程

在最后一步，代理会为乘客撰写一条简短的短信。通过提示，我们可以指导代理创建一条适当的消息，欢迎每位乘客，并向他们提供最新的旅行后续步骤信息。

如果 AI 判断转机时间紧张，可能会鼓励乘客不要耽搁。

“欢迎来到纽约肯尼迪机场。您飞往波士顿的转机航班将于 3:20 从 B10 登机口起飞，登机口于 3:00 关闭。步行时间约为 10 分钟。请立即前往登机口。”

如果时间充足，AI 也许可以交叉销售沿途咖啡店的服务。

“欢迎来到芝加哥奥黑尔机场！您飞往克利夫兰的转机航班将于晚上 6:20 从 B12 登机口起飞。步行时间约为 15 分钟，所以您有充足的时间。”

## 飞行变得轻松

在 Salesforce 内部使用代理流程可以帮助航空公司轻松处理机场转机。利用 Salesforce 中的客户数据和定制的 Heroku AppLink 集成，代理流程可在飞机降落时向每位乘客发送定制短信。客户私人数据永远不会离开 Salesforce 生态系统，而定制的 Heroku 应用程序则提供个性化体验。通过 Agentforce 中的代理流程，客户可以实时获知变化以及处理这些变化的紧迫程度。

当 AI 代理能够处理通知客户行程变更时，航空公司可以专注于客户体验的其他部分，有助于让所有人的旅行体验更加轻松。