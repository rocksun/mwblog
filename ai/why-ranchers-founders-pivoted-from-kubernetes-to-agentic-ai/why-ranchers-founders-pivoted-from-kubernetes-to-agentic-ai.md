
<!--
title: Rancher创始人：为何告别Kubernetes，all in智能体AI？
cover: https://cdn.thenewstack.io/media/2025/09/85455045-obot.png
summary: 生成式AI向代理式AI转变，Obot.ai团队利用基础设施经验，通过MCP网关和Nanobot提供治理与安全，解决“影子AI”挑战。
-->

生成式AI向代理式AI转变，Obot.ai团队利用基础设施经验，通过MCP网关和Nanobot提供治理与安全，解决“影子AI”挑战。

> 译自：[Why Rancher's Founders Pivoted From Kubernetes to Agentic AI](https://thenewstack.io/why-ranchers-founders-pivoted-from-kubernetes-to-agentic-ai/)
> 
> 作者：Janakiram MSV

生成式人工智能（GenAI）从对话工具向自主的、[面向行动的代理](https://thenewstack.io/5-factors-for-predictable-autonomy-with-agentic-ai/)的转变，标志着企业技术的一个[重要的转折点](https://thenewstack.io/why-agentic-ai-orchestration-is-key-to-managing-ai-complexity/)。随着组织超越初步试验，他们面临着一套新的围绕治理、安全性和可扩展性的[运营挑战](https://thenewstack.io/how-to-build-agentic-ai-that-ships/)。

一个熟悉的模式正在浮现，它呼应了前几波技术浪潮中虚拟机（VM）和容器的蔓延。这项新挑战是AI代理的无限制扩散及其通过模型上下文协议（MCP）服务器与关键业务系统的连接，从而创建了一个“影子AI”的格局，引入了重大风险。

解决这个问题需要一层新的基础设施，一个专用于代理式AI的控制平面。[MCP](https://thenewstack.io/is-model-context-protocol-the-new-api/)已迅速成为赋能新一代AI的标准，为代理与外部工具和数据源交互提供了一种通用语言。

[Obot.ai](https://obot.ai/)进入了这个领域，该公司由一个在创建基础企业基础设施方面拥有深厚历史的团队建立，旨在为这个新生态系统提供必要的治理层。

## 团队在基础设施创新方面的传承

Obot.ai的旅程始于[Acorn Labs](https://thenewstack.io/acorn-a-lightweight-portable-paas-for-kubernetes/)，一家最初专注于简化Kubernetes上应用程序部署的公司。该公司的团队，由首席执行官Sheng Liang领导，在云原生世界中拥有重要的传承，曾创立Cloud.com（后被Citrix收购）和Rancher Labs（后被SUSE收购）。

在退出Cloud.com后，Liang与联合创始人Shannon Williams、Darren Shepherd和Will Chan重聚，于2014年创立了[Rancher Labs](https://thenewstack.io/rancher-labs-rio-an-application-deployment-engine-for-kubernetes/)。该公司成为了Kubernetes管理的代名词，Shepherd创建了[k3s](https://k3s.io/)，这是最受欢迎的[轻量级Kubernetes发行版](https://thenewstack.io/ranchers-k3s-joins-cncf-sandbox-as-first-kubernetes-distribution/)，它改变了边缘计算的部署方式。Rancher在2020年12月被SUSE以8亿美元收购之前，下载量超过1亿次，拥有3.7万个活跃团队。

这种背景不仅仅是历史注脚，更是他们当前战略的核心要素。他们决定从以Kubernetes为中心的产品转向以AI为重点的平台，这证实了代理式AI不仅仅是另一个需要容器化的工作负载。相反，它是一个根本性的新计算范式，需要自己专门构建的基础设施和管理平面。团队观察到，基于大型语言模型（LLM）构建的应用程序是使用自然语言提示设计的，AI开发者更喜欢使用源代码而不是二进制容器，这使得他们以前的运行时不那么适合。

这项[战略调整](https://obot.ai/acorn-labs-is-now-obot-ai/)和品牌重塑为Obot.ai，通过一轮[3500万美元的种子轮融资](https://obot.ai/obot-ai-secures-35m-seed-to-build-enterprise-mcp-gateway/)得到了验证。这项投资由Mayfield Fund和Nexus Venture Partners共同领投，这两家风险投资公司在支持基础企业技术方面有着良好的记录。对一个协议的开源网关而非一个新的基础模型进行巨额种子投资，这标志着AI市场的成熟。

精密投资的焦点正在从模型本身扩展到使这些模型在复杂企业环境中安全高效地使用的关键“管道”和基础设施。这些资金明确旨在加速公司两个核心开源项目——Obot MCP网关和Nanobot MCP代理框架——的开发。

## Obot MCP网关：AI代理的控制平面

Obot平台是一个由三个主要组件组成的集成系统：MCP网关、面向用户的聊天界面和用于管理的全面管理仪表盘。Obot的核心是一个企业级控制平面，旨在管理MCP服务器的生命周期和安全性。

Obot MCP网关的架构模式与微服务兴起时不可或缺的API网关的模式非常相似。正如那些网关为庞大的后端API格局提供了集中控制点一样，Obot也为新兴的MCP服务器生态系统提供了类似的控制平面，MCP服务器是AI与企业系统之间的连接组织。

[![](https://cdn.thenewstack.io/media/2025/09/f298af1b-obot-arch-1024x339.png)](https://cdn.thenewstack.io/media/2025/09/f298af1b-obot-arch-1024x339.png)

网关的功能通过几个关键能力实现。它提供了一个集中式注册中心，作为经过精心策划的、内部批准的MCP服务器目录。这通过为IT组织提供可发现和有文档记录的AI工具的单一事实来源，直接解决了工具蔓延的问题。该平台还充当安全代理，通过中央扼流点路由AI代理和MCP服务器之间的所有通信。这使得安全策略的执行、完整的审计日志记录和路由控制成为可能，这对于防止未经授权的数据访问和确保合规性至关重要。

通过强大的基于角色的访问控制（RBAC），安全性得到了进一步增强。Obot使用OAuth 2.1等标准与现有企业身份平台集成，允许管理员定义细粒度权限，以规定哪些用户或组可以访问特定的MCP服务器。这为人类用户和代表他们行事的AI代理强制执行了最小权限原则。

最后，该平台提供了全面的可观测性。通过检查所有代理流量，网关生成详细的审计追踪和性能指标，提供对工具使用的完全可见性，这对于调试、监控和满足法规要求至关重要。

[![](https://cdn.thenewstack.io/media/2025/09/6637eed9-obot-mcp-1024x556.jpg)](https://cdn.thenewstack.io/media/2025/09/6637eed9-obot-mcp-1024x556.jpg)

对于其目标受众Kubernetes用户来说，Obot被设计为无缝集成。该平台作为[容器化应用程序](https://github.com/obot-platform/obot/pkgs/container/obot)提供，可以使用官方[Helm Chart](https://github.com/obot-platform/obot/tree/main/chart)部署到任何Kubernetes集群上。这种方法与已建立的云原生工作流对齐，简化了整个平台的安装、配置和生命周期管理。该架构依赖于经过验证、可扩展的技术，利用PostgreSQL存储结构化元数据（例如用户权限和服务器配置），并使用Amazon S3进行工作区存储。这种自托管、开源模式是一种刻意赢得企业信任的策略，允许组织通过在其自身基础设施中部署控制平面，对其数据和安全态势保持完全控制。

## Nanobot：开源代理开发框架

[![](https://cdn.thenewstack.io/media/2025/09/eaa13e6f-nanobot-300x225.png)](https://cdn.thenewstack.io/media/2025/09/eaa13e6f-nanobot-300x225.png)

*Obot提供管理和治理框架，而公司的第二个主要项目[Nanobot](https://www.nanobot.ai/)则专注于开发AI代理。*

Nanobot是一个紧凑的开源MCP主机，提供运行时环境、状态管理和身份功能，这些是打包MCP服务器与推理模型，使其成为功能齐全、有状态代理所必需的。

这种方法促进了可组合架构，其中代理的“大脑”（LLM）与其“身体”（通过MCP服务器公开的工具）解耦。开发者可以通过简单地定义一个配置来构建新代理，该配置将现有、预批准的MCP服务器与新的系统提示结合起来，从而显著加速开发并鼓励安全组件的复用。

[![](https://cdn.thenewstack.io/media/2025/09/935cbb66-nanobot-1024x530.png)](https://cdn.thenewstack.io/media/2025/09/935cbb66-nanobot-1024x530.png)

Nanobot采用声明式模型。开发者通过YAML配置文件定义代理应该做什么，指定其工具和指令，而不是编写复杂的命令式代码来处理对话逻辑。Nanobot的一个关键特性是支持[MCP-UI](https://mcpui.dev/)，这是MCP标准的一个扩展，允许代理直接在聊天对话中渲染丰富、交互式的用户界面。

此功能将代理式AI扩展到纯文本交互之外，通过图形组件（如表单、按钮或可视化数据表示）实现更直观、更强大的用户体验。这种对更丰富用户体验的关注代表了对AI从技术用户的工具演变为更广泛受众主流界面的战略性预判。

## 企业AI版图中的战略立足点

Obot.ai已战略性地定位自己，以满足企业AI版图中一个关键的新兴需求。通过利用团队在构建云计算基础架构方面的丰富经验，该公司正在将经过验证的治理、安全和开源协作原则应用于代理式AI的新领域。

Obot MCP网关为IT组织提供了核心控制平面，使其能够自信地管理AI工具的采用，而Nanobot框架则赋能开发者构建下一代强大、交互式代理。这两个项目共同形成了一个共生生态系统。

Obot创建了安全且受治理的企业工具“应用商店”，而Nanobot提供了“SDK和运行时”来构建消耗这些工具的代理。随着MCP巩固其作为AI互操作性标准的角色，像Obot.ai这样提供必要安全和管理层的平台，必将成为企业AI堆栈的基础组成部分。