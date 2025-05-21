<!--
title: Google拥抱MCP
cover: https://cdn.thenewstack.io/media/2025/05/2c1306b6-google-io-scaled.jpg
summary: 重磅！Google拥抱Anthropic的Model Context Protocol (MCP)，集成至Gemini API和SDK！Agent2Agent (A2A)协议互补，增强AI代理互联。Gemini生态迎来更新，Vertex AI服务加持，Deep Think模式、生成视频模型齐发力！
-->

重磅！Google拥抱Anthropic的Model Context Protocol (MCP)，集成至Gemini API和SDK！Agent2Agent (A2A)协议互补，增强AI代理互联。Gemini生态迎来更新，Vertex AI服务加持，Deep Think模式、生成视频模型齐发力！

> 译自：[Google Embraces MCP](https://thenewstack.io/google-embraces-mcp/)
> 
> 作者：Frederic Lardinois

Anthropic 的 [Model Context Protocol](https://thenewstack.io/tutorial-set-up-an-mcp-server-with-net-and-github-copilot/) (MCP) 已经迅速成为将 AI 代理连接到工具和数据源的标准。谷歌在其 I/O 开发者大会上宣布，它也将支持 MCP，将其作为 Gemini API 和 [SDK](https://ai.google.dev/gemini-api/docs/migrate) 的内置部分。

该公司还表示，它正在考虑让开发者更容易地部署 MCP 服务器和其他用于 AI 代理的托管工具，但它没有提供关于这方面的任何细节。

谷歌自己最近也宣布了 [Agent2Agent protocol](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/) (A2A)，虽然关于 MCP 和 A2A 之间的关系存在一些混淆，但谷歌一直强调两者是互补的。顾名思义，A2A 旨在增强代理之间的交互方式，而 MCP 则是关于将代理连接到数据。

![Image](https://cdn.thenewstack.io/media/2025/05/8f5c907a-img_0917-scaled.jpg)

*图片来源：The New Stack。*

谷歌 CEO Sundar Pichai 在今天发布会前的新闻发布会上表示：“像 Agent2Agent 和 Model Context Protocol 这样的协议是构建更强大代理的重要步骤。[...] 这些技术将协同工作，使代理更有用。”

到目前为止，开发者必须使用第三方库才能从他们的应用程序中调用 MCP 服务器。

该协议已经变得非常流行，现在似乎每个 SaaS 服务都公开了一个 MCP 服务器，甚至 Microsoft Windows 也在获得 [local MCP servers now](https://thenewstack.io/microsoft-brings-mcp-local-ai-models-and-post-quantum-security-to-windows/)，以便基于桌面的 AI 应用程序可以访问它们。

值得注意的是，Google Deepmind CEO Demis Hassabis 已经 [hinted](https://techcrunch.com/2025/04/09/google-says-itll-embrace-anthropics-standard-for-connecting-ai-models-to-data/) MCP 支持将在 4 月份进入 Gemini，但当时他没有提供时间表。

![Image](https://cdn.thenewstack.io/media/2025/05/3c0dfa0b-d017a051-b7eb-4eb7-aa5c-3e8f01589ffa-scaled.jpg)

*图片来源：The New Stack。*

MCP 支持只是谷歌 Gemini 生态系统的众多更新之一，其中包括向 Gemini API 及其 Vertex AI 服务添加计算机使用工具，例如，该工具将能够自动化基于浏览器的任务，以及更新的模型，为流行的 Gemini 2.5 Pro 模型提供更深入的“Deep Think”深度思考模式，更新的生成视频模型等等（以及一个新的 249 美元/月的订阅服务，需要该服务才能访问许多这些高端功能）。