<!--
title: 谷歌云重磅推出托管式远程MCP服务器
cover: https://cdn.thenewstack.io/media/2025/04/c90e05a8-img_3909-edit.jpg
summary: 谷歌为其多项服务提供完全托管的MCP服务器，简化了开发者构建AI代理与谷歌服务（如BigQuery、地图）交互。Anthropic已将MCP协议捐赠给Linux基金会。
-->

谷歌为其多项服务提供完全托管的MCP服务器，简化了开发者构建AI代理与谷歌服务（如BigQuery、地图）交互。Anthropic已将MCP协议捐赠给Linux基金会。

> 译自：[Google Launches Managed Remote MCP Servers for Its Cloud Services](https://thenewstack.io/google-launches-managed-remote-mcp-servers-for-its-cloud-services/)
> 
> 作者：Frederic Lardinois

模型上下文协议（MCP）已成为大型语言模型（LLM）与第三方服务交互的事实标准，为实现这一点，这些第三方服务必须提供LLM可以连接的MCP服务器。目前，尽管MCP面世不到一年，几乎所有在线服务都已配备MCP服务器。今天，[谷歌](https://cloud.google.com/?utm_content=inline+mention)通过为其众多谷歌和谷歌云服务提供[完全托管的MCP服务器](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services)来[扩展其MCP支持](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services)——未来还将有更多服务加入。

到目前为止，开发者不得不使用谷歌社区构建的本地服务器或部署开源解决方案，谷歌指出，这些方案通常难以安装和管理。通过提供这些新的托管MCP服务器，谷歌消除了所有这些额外的工作，使开发者能够更容易地构建一个由谷歌新的Gemini 3模型支持的代理，例如，该代理可以连接到BigQuery数据服务和谷歌地图，以地理空间信息丰富这些数据。

谷歌云副总裁兼总经理Michael Bachman和谷歌云工程研究员Anna Berenberg在今天的声明中写道：“通过这些新的和扩展的MCP功能，我们确保开发者和代理可以轻松地与数据交互并执行操作。谷歌致力于引领人工智能革命，不仅通过构建最佳模型，还通过为这些模型和代理的蓬勃发展构建最佳生态系统。”

BigQuery和地图是首批获得新托管MCP服务器的服务之一，同时还有谷歌计算引擎（GCE），它将允许代理管理基础设施工作流，例如配置和调整实例大小，以及谷歌 Kubernetes 引擎（GKE），它将提供一个允许代理与Kubernetes和GKE API协同工作的服务器。

以下是未来几个月也将获得MCP支持的其他服务：

*   **项目、计算和存储：** Cloud Run, Cloud Storage, Cloud Resource Manager
*   **数据库和分析：** AlloyDB, Cloud SQL, Spanner, Looker, Pub/Sub, Dataplex Universal Catalog
*   **安全：** Google Security Operations (SecOps)
*   **云操作：** Cloud Logging, Cloud Monitoring
*   **谷歌服务：** Developer Knowledge API, Android Management API

为了发现、治理、使用和监控这些服务，谷歌正在使用仍处于预览阶段的Cloud API Registry。该Registry将提供关于代理可以使用哪些API和工具（以及它们可以访问这些API的哪些功能）的所有详细信息。

今天的声明发布前一天，Anthropic [向Linux基金会捐赠了MCP协议规范](https://thenewstack.io/anthropic-donates-the-mcp-protocol-to-the-agentic-ai-foundation/)，作为新的厂商中立Agentic AI基金会（AAIF）的一部分。

MCP的共同创建者、Anthropic技术人员David Soria Parra表示：“谷歌在如此广泛的产品中对MCP的支持，结合他们对规范的密切合作，将帮助更多开发者构建代理式AI应用程序。随着领先平台采用率的增长，我们离在人们已经使用的工具和服务中无缝工作的代理式AI更近了一步。”

谷歌的Apigee API管理服务也获得了扩展的MCP支持，允许企业使用他们已经用于管理API的同一工具来管理其自定义MCP服务器以及代理如何访问它们。