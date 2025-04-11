<!--
title: Google的Agent2Agent协议帮助AI Agent互相交流
cover: https://cdn.thenewstack.io/media/2025/04/c90e05a8-img_3909-edit.jpg
summary: Google Cloud Next重磅发布Agent2Agent (A2A)协议！50+技术伙伴力挺，赋能AI Agent互联互通。A2A互补Anthropic的Model Context Protocol (MCP)，基于HTTP、SSE、JSON-RPC等标准，支持文本、音频、视频，打造更强大的Agent系统，开启Agent互操作新纪元！
-->

Google Cloud Next重磅发布Agent2Agent (A2A)协议！50+技术伙伴力挺，赋能AI Agent互联互通。A2A互补Anthropic的Model Context Protocol (MCP)，基于HTTP、SSE、JSON-RPC等标准，支持文本、音频、视频，打造更强大的Agent系统，开启Agent互操作新纪元！

> 译自：[Google’s Agent2Agent Protocol Helps AI Agents Talk to Each Other](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/)
> 
> 作者：Frederic Lardinois

在拉斯维加斯举行的Cloud Next大会上，[Google](https://cloud.google.com/?utm_content=inline+mention) 今天宣布了一项新的开放协议，该协议可以帮助AI Agent相互通信，无论该Agent是为何种框架而构建的。

被称为[Agent2Agent](https://github.com/google/A2A)的协议，在发布时获得了Google 50多家技术合作伙伴的支持，其中包括Atlassian、Box、Cohere、Intuit、Langchain、[MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention)、Salesforce、[SAP](https://www.sap.com/index.html?utm_content=inline+mention)、[ServiceNow](https://www.servicenow.com/products/observability.html?utm_content=inline+mention)、UKG和Workday。

Antrophic的[Model Context Protocol](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (MCP) 已经迅速成为将Agent连接到外部应用程序和数据源的事实标准。Google强调，Agent2Agent (A2A) 并非旨在以任何方式取代MCP。相反，它的目的是通过帮助开发人员构建Agent可以更轻松地相互通信的系统来补充MCP，而不管他们使用什么工具和框架来构建这些Agent。

“MCP和A2A我们的Agent间协议是互补的，因为MCP允许你以开放、标准的方式访问数据，而A2A允许不同Agent之间的互操作性，”Google Cloud的ML、系统和Cloud AI副总裁Amin Vahdat在本周早些时候的新闻发布会上解释说。

“可以将MCP视为模型到数据，而A2A允许Agent之间的互操作性，Agent到Agent。这两者——对于数据和Agent交互——结合在一起，可以非常容易和高效地构建非常强大的Agent。”

这项新协议支持文本、音频和视频，它基于现有标准（HTTP、SSE、JSON-RPC），并包括身份验证和授权功能，Google表示这些功能“在发布时与OpenAPI的身份验证方案相当”。该公司还强调，新协议为长时间运行的任务提供支持，A2A能够提供实时反馈、通知和状态更新。

使用A2A，Agent可以是“客户端”或“远程”Agent。客户端制定和传达任务，而远程Agent则执行这些任务。远程Agent可以在JSON格式的“Agent卡片”的帮助下宣传其功能。

“A2A有潜力开启Agent互操作性的新时代，促进创新并创建更强大和通用的Agent系统。我们相信，该协议将为Agent可以无缝协作以解决复杂问题并改善我们生活的未来铺平道路，”Google在今天的公告中指出。“我们致力于与我们的合作伙伴和社区合作，以开放的方式构建该协议。我们将以开源方式发布该协议，并为贡献设置清晰的途径。”