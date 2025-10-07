
<!--
title: OpenAI重磅推出：无代码智能体构建器！
cover: https://cdn.thenewstack.io/media/2025/10/23dcea28-img_2585-scaled.jpg
summary: OpenAI大会推出无代码智能体构建器AgentKit和ChatGPT应用功能。Codex全面可用，并发布多款新模型，包括GPT-5 Pro API。
-->

OpenAI大会推出无代码智能体构建器AgentKit和ChatGPT应用功能。Codex全面可用，并发布多款新模型，包括GPT-5 Pro API。

> 译自：[OpenAI Launches a No-Code Agent Builder](https://thenewstack.io/openai-launches-a-no-code-agent-builder/)
> 
> 作者：Frederic Lardinois

OpenAI本周在旧金山举办其年度开发者大会。在最近几天和几周内发布了一系列面向消费者和金融领域的公告，包括Sora视频创作应用的推出后，今天的消息明确聚焦于在OpenAI平台之上进行构建。

其中的两大亮点是OpenAI [无代码智能体构建器](https://openai.com/agent-platform/) AgentKit 的测试版发布，以及ChatGPT中的应用程序功能，这将允许开发者将更多类似应用的体验带入ChatGPT界面。

## OpenAI的智能体构建器

OpenAI联合创始人兼首席执行官 [Sam Altman](https://x.com/sama) 在主题演讲中表示：“过去几年，人工智能已经从你可以询问任何事情的系统，发展到你可以要求它为你做任何事情的系统——我们正通过智能体看到这一点，这些软件能够利用上下文工具和信任来承担任务。”“但尽管围绕智能体有诸多兴奋和潜力，真正投入生产的却寥寥无几。很难知道从何开始，使用什么框架，而且工作量很大。涉及到编排评估器、连接工具、构建良好的用户界面，每个这些层级都增加了许多复杂性，以至于在你真正了解什么会起作用之前，就已经增加了许多复杂性。”

AgentKit本质上是基于OpenAI平台的无代码智能体构建器，旨在让开发者和企业通过几次点击就能创建智能体——以及多智能体系统——并将其投入生产。

[![](https://cdn.thenewstack.io/media/2025/10/cf7a2582-visual_-agent-builder-template_assets.png)](https://cdn.thenewstack.io/media/2025/10/cf7a2582-visual_-agent-builder-template_assets.png)

*图片来源：OpenAI。*

在很大程度上，这与其他无代码/低代码智能体构建器并没有太大区别。但尽管OpenAI将其定位为企业工具——能够从Dropbox、Google Drive、Sharepoint和Microsoft Teams等外部服务以及第三方模型上下文协议（MCP）服务器（其中包含这些连接器的注册表）引入数据——一个完全企业级的系统（更类似于OutSystems或Mendix）还需要包括深度数据治理、审计和安全工具。

Agent Builder允许开发者为用户体验设置防护措施，例如，检测越狱行为并确保没有个人身份信息泄露到聊天中。它还集成了 [Evals](https://platform.openai.com/docs/guides/evals?api-mode=responses)，这是OpenAI用于测试提示和测量模型行为的工具。

[![](https://cdn.thenewstack.io/media/2025/10/d81940c0-img_2593-scaled.jpg)](https://cdn.thenewstack.io/media/2025/10/d81940c0-img_2593-scaled.jpg)

*图片来源：The New Stack/Frederic Lardinois。*

为了将这些智能体投入生产，OpenAI今天还推出了ChatKit，这是一个将这些智能体体验嵌入到应用程序中的工具包。这又进一步简化了将智能体投入生产的过程。OpenAI的一些客户，如HubSpot等，已经利用这项服务来支持内部和外部用例，例如客户支持智能体。

[![](https://cdn.thenewstack.io/media/2025/10/cf7a2582-visual_-agent-builder-template_assets.png)](https://cdn.thenewstack.io/media/2025/10/cf7a2582-visual_-agent-builder-template_assets.png)

*图片来源：OpenAI。*

## ChatGPT中的应用程序

当天的另一项重要公告是在ChatGPT中推出应用程序功能（适用于欧盟以外的所有用户）。其理念是在ChatGPT界面中调用第三方应用程序——开发者可以使用Apps SDK来构建它们，该SDK本身基于Anthropic的 [MCP](https://thenewstack.io/when-is-mcp-actually-worth-it/)。实际上，Apps SDK是开源的，它本质上是MCP的扩展，允许开发者构建其应用程序的逻辑和界面。

实际上，这看起来会像这样。假设用户想在Zillow上浏览房屋。他可以直接从ChatGPT中调用Zillow应用程序（“Zillow，显示我在俄勒冈州波特兰市50万美元以下的房屋”）。Zillow随后会弹出一个地图和交互式用户界面来查看这些房屋，用户可以在聊天栏中细化搜索或询问有关房屋的更多问题。

[![](https://cdn.thenewstack.io/media/2025/10/8cb81f03-img_2596-scaled.jpg)](https://cdn.thenewstack.io/media/2025/10/8cb81f03-img_2596-scaled.jpg)

*图片来源：The New Stack/Frederic Lardinois。*

该SDK包含允许用户登录应用程序的功能，这反过来又使开发者能够提供个性化和访问高级功能。

该公司在今天的公告中解释道：“ChatGPT中新一代应用程序的魔力在于它们如何将熟悉的交互元素——如地图、播放列表和演示文稿——与通过对话进行交互的新方式融合在一起。”

[![](https://cdn.thenewstack.io/media/2025/10/11db30ed-zillow-chatgpt.gif)](https://cdn.thenewstack.io/media/2025/10/11db30ed-zillow-chatgpt.gif)

*图片来源：OpenAI。*

首批可用的应用程序来自Booking.com、Canva、Coursera、Expedia、Figma、Spotify和Zillow。OpenAI计划很快推出一个符合 [其指南](https://developers.openai.com/apps-sdk/app-developer-guidelines) 的应用程序目录，并向开发者开放。

截至目前，SDK的某些部分仍在不断变化。OpenAI特别指出，它很快将提供更精细的控制，以管理数据如何与开发者共享。

这些市场始终存在的一个问题是发现。在Google Home和Amazon Alexa等语音助手的早期，这些公司非常重视构建开发者平台，但用户从未真正出现，因为没有人知道实际有哪些语音命令可用。今天的AI系统显然比那更智能，许多知名服务肯定在ChatGPT这样的大型平台上获得使用量方面不会有任何问题。但对于新开发者来说，发现可能仍然是一个挑战，如果OpenAI开始主动推荐服务——该公司表示会这样做——那么如何处理相互竞争的工具仍然存在疑问。

开发者可能也会对支持这项新功能有所犹豫，因为GPTs，OpenAI之前尝试将应用程序引入ChatGPT的尝试，自推出以来大多默默无闻。

## Codex全面可用及更多

除了这两项头条公告之外，OpenAI今天还将其AI编码智能体Codex推向了全面可用状态，并增加了Slack集成和 [一个SDK](https://developers.openai.com/codex/sdk)，该SDK允许开发者将其Codex CLI智能体所用的工具嵌入到他们的CI/CD管道和自己的工具中。

该SDK现已支持TypeScript，更多语言即将推出。

OpenAI今天还发布了一款新的实时语音模型——gpt-realtime-mini——它声称比其较大的同类模型便宜70%，同时不损失太多质量。还有一款新的小型图像模型——gpt-image-1-mini——承诺比OpenAI较大的图像模型使用成本降低80%。

对于希望在其应用程序中使用OpenAI最强大模型的开发者，GPT-5 Pro现已在API中可用。