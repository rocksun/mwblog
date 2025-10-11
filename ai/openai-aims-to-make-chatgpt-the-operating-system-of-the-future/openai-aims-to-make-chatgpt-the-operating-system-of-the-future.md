
<!--
title: OpenAI 欲将 ChatGPT 打造为未来操作系统
cover: https://cdn.thenewstack.io/media/2025/10/80987166-aron-yigin-4g4h2lua41u-unsplash-c.jpg
summary: OpenAI Apps SDK 将 ChatGPT 变为 AI 超级应用/操作系统，颠覆软件范式。它吸引开发者，重塑用户互动，并引发与科技巨头的激烈竞争。
-->

OpenAI Apps SDK 将 ChatGPT 变为 AI 超级应用/操作系统，颠覆软件范式。它吸引开发者，重塑用户互动，并引发与科技巨头的激烈竞争。

> 译自：[OpenAI Aims To Make ChatGPT the Operating System of the Future](https://thenewstack.io/openai-aims-to-make-chatgpt-the-operating-system-of-the-future/)
> 
> 作者：Janakiram MSV

OpenAI 于 2025 年 10 月 6 日在旧金山举行的 DevDay 大会上[宣布推出其 Apps SDK](https://thenewstack.io/openai-l​​aunches-apps-sdk-for-chatgpt-a-new-app-platform/)，这从根本上将 ChatGPT 从一个对话式人工智能转变为一个全面的应用平台。随着这一声明，ChatGPT 不再仅仅是一个聊天机器人。它正在转型为一个完整的平台，并可能成为负责管理用户交互的各种其他应用的“超级应用”。

OpenAI 没有将人工智能视为现有应用中添加的功能，而是将整个应用带入 ChatGPT 以人工智能为中心的语境中，颠覆了传统方法。其结果是一个聊天驱动的环境，用户可以根据名称或上下文按需调用应用，并在不需切换独立网站或程序的情况下完成任务。

本文将分析 [OpenAI Apps SDK](https://developers.openai.com/apps-sdk) 如何将 ChatGPT 转变为超级应用乃至人工智能操作系统。我将讨论这一演变对开发者、用户和更广泛的技术社区意味着什么。

## 从聊天机器人到人工智能超级应用

OpenAI 的 Apps SDK 计划有效地使 ChatGPT 成为一个超级应用，类似于一个融入人工智能助手的应用商店。Apps SDK 代表了一种与竞争对手截然不同的人工智能集成方法。Google 通过 [Gemini 功能](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/)增强 Chrome，Perplexity 将自己定位为[人工智能驱动的问答引擎](https://thenewstack.io/how-perplexitys-online-llm-was-inspired-by-freshllms-paper/)，而 OpenAI 则将整个应用带入人工智能对话本身。用户通过自然语言命令调用应用，例如“Spotify，为我的派对制作一个播放列表”或“Zillow，在东京寻找 3000 美元以下的公寓”，而无需离开 ChatGPT 界面。

首批合作伙伴——包括 Spotify、Canva、Zillow、Figma、Coursera、Expedia 和 Booking.com——展示了这一平台愿景的广度。这些应用直接在聊天中呈现互动组件，包括地图、播放列表、设计工具和视频内容。基于开放的 [Model Context Protocol](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (MCP) 构建的 SDK，为开发者提供了即时访问 OpenAI 庞大用户群的途径，同时避免了传统应用商店的发行挑战。Sam Altman 在 DevDay 上表示，这“催生了新一代互动、适应性和个性化的应用，你可以与它们进行对话。”

OpenAI 和 Stripe 共同开发的 [Agent Commerce Protocol](https://developers.openai.com/commerce/) (ACP) 已经定义，公司有办法将支付和结账集成到 ChatGPT 中。这填补了其他人工智能应用所缺乏的关键空白。

> 鉴于 ChatGPT 已有 8 亿周活跃用户，该公司掌控着用户花费时间的界面层。

OpenAI 的战略优势在于用户注意力经济学。鉴于 ChatGPT 已有 8 亿周活跃用户，该公司掌控着用户花费时间的界面层。

OpenAI 的战略与 Google 在 Chrome 等现有平台（拥有 30 亿用户，但仍保持传统浏览范式）上添加 AI 功能的方法根本不同。[Google 正在 Chrome 中推出 Gemini](https://thenewstack.io/chrome-switches-on-ai-the-future-of-browsing-begins-now/)，其功能包括多标签页分析以及用于预约和订购杂货的代理功能。然而，这种增强模型将浏览器保留为与 AI 交互的主要界面，将其视为增强而非编排层。

Perplexity 凭借其专注于研究准确性和有引证依据的回复的问答引擎，走上了第三条道路。该公司于 2025 年 7 月推出了其 Comet 浏览器，每月 200 美元，目标是专业研究用例。虽然 Perplexity 在信息发现方面表现出色，并提供透明的来源，但它缺乏 ChatGPT 的规模和广度。目前的竞争格局呈现出三种截然不同的理念，关于 AI 如何与用户工作流集成以及智能在软件堆栈中的位置。

当谈到微软时，其战略方向有所不同。OpenAI 正在围绕 ChatGPT 作为应用环境构建一个 AI 原生平台，而微软则在其现有的生产力堆栈中嵌入 AI。Copilot 体验与 Office、Windows 和 Azure 紧密集成，确保开发者和企业用户在熟悉的语境中接触 AI。该公司的方法将 AI 视为一种贯穿应用和基础设施的底层架构，而非一个单独的目的地。与 Google 类似，微软的优势在于分发。Windows 和 Office 仍然主导着工作场所，使该公司能够嵌入访问数十亿个终端。其面临的挑战是，用户参与度仍然分散在各个应用中，而 OpenAI 则将用户参与度整合到一个对话层中。

| 维度 | OpenAI (ChatGPT) | Google (Gemini) | Microsoft (Copilot) | Perplexity (Comet) |
| --- | --- | --- | --- | --- |
| **理念** | AI中的应用 – AI作为核心操作系统。 | 应用中的AI – 增强层。 | 应用中的AI – 企业底层架构。 | AI即研究 – 准确性和透明度。 |
| **分发** | ChatGPT 应用 (8亿+用户)。 | 搜索、Chrome、Android、Workspace。 | Microsoft 365、Windows、Azure。 | Comet 浏览器和 Perplexity 网页/应用。 |
| **开发者重心** | 通过 Apps SDK 和应用目录的 ISV。 | Firebase、Vertex AI、云开发者。 | 通过 Copilot Studio 的企业和 ISV。 | 研究人员和 API 合作伙伴。 |
| **变现** | 应用商店收益分成、ACP 费用、API 调用。 | 云和 Workspace 订阅、广告。 | Copilot 许可、Azure 用量。 | 高级 ($200/月) 计划、API 访问。 |
| **界面模型** | 对话式 + 内联图形用户界面。 | 以浏览器为中心，带有人工智能附加功能。 | 现有应用中的嵌入式助手。 | 独立、引证驱动的研究界面。 |
| **生态系统目标** | AI 原生应用平台。 | 保持网页/应用主导地位。 | 加强企业人工智能集成。 | 引领可信人工智能研究。 |
| **用户价值** | 适用于所有任务的单一对话中心。 | 熟悉工具的 AI 增强。 | 统一的企业生产力。 | 经过验证、有来源支持的答案。 |
| **战略目标** | 使 ChatGPT 成为 AI 操作系统。 | 将 AI 保留在现有界面内。 | 掌控企业 AI 技术栈。 | 主导高信任度知识搜索。 |

## 解构“ChatGPT 作为操作系统”战略

Apps SDK 与 ChatGPT 集成的技术架构承载着一个更大的战略抱负。OpenAI 高管明确表示，ChatGPT 的演变是创建一个新的计算平台，类似于操作系统，旨在成为用户访问广泛数字服务的中央门户。

“ChatGPT 作为操作系统”这一概念不仅仅是一个比喻。它深刻地反映了 OpenAI 采用的结构化平台战略。在这个类比中，核心 GPT 模型充当内核，管理推理和语言等基本计算资源。Responses API 等核心 API 作为系统调用，提供对内核功能的低级访问。ChatGPT 界面本身充当 Shell（用户界面外壳），是用户发出命令和接收操作系统输出的主要交互层。最后，新发布的 Apps SDK 和 AgentKit 提供了构建在此新操作系统上运行的第三方应用的高级开发者工具包。

| 传统操作系统组件 | OpenAI 生态系统对应项 | 在生态系统中的功能 |
| --- | --- | --- |
| 内核 | GPT 基础模型 (例如，GPT-5 Pro) | 管理核心计算资源（推理、语言生成、多模态理解）。 |
| 系统调用 | 核心 API (例如，Responses API、Realtime API) | 为开发者提供对内核能力的低级、编程访问。 |
| Shell | ChatGPT 用户界面 (网页、移动) | 用户发布命令和接收操作系统输出的主要交互层。 |
| 应用层 | 第三方应用 (例如，Spotify、Canva) | 为用户提供特定功能和服务，由外部开发者构建。 |
| 开发者工具包 (SDK) | Apps SDK、AgentKit | 简化应用层构建过程的高级库和工具。 |
| 文件系统 / 数据层 | 用户对话历史、连接的数据源 | 管理并提供对用户和应用的持久数据和上下文的访问。 |

操作系统战略不可或缺的一部分是创建一个新的市场，一个直接内置于 ChatGPT 中的应用目录，用户可以在其中发现并启用第三方集成。OpenAI 将通过审查和批准流程来管理这个市场，其中包含符合高功能和设计标准的应用。

该公司还表示有意引入变现工具，允许开发者从他们的创作中获得收入，可能通过类似于 Apple 和 Google 所使用的收益分成模式。这种双边市场的创建旨在触发强大的飞轮效应。不断增长的用户群吸引更多的开发者，他们的应用使平台更有价值和实用，这反过来又吸引更多的用户。通过控制这个市场，OpenAI 成为守门人，管理发现、标准和变现，使其对在其平台上构建的生态系统拥有巨大的影响力。

## 微软悖论：从不可或缺的伙伴到强大的对手

最复杂的关系是 OpenAI 与微软之间的关系。尽管微软是重要的投资者和基础设施合作伙伴，但两家公司现在正走向竞争性冲突。

微软正在积极围绕 Microsoft 365 Copilot 和 Copilot Studio 建立自己的开发者生态系统，后者是一个低代码平台，供企业构建与其内部数据源（如 Microsoft Graph）集成的自定义代理。这一产品直接与 OpenAI 吸引相同企业开发者加入其平台的努力构成竞争。

> ChatGPT 应用平台的推出是独立宣言的必要之举，是直接掌控最终用户和开发者关系的战略举措。

如果 OpenAI 仍然只是一个模型提供商，它就有可能作为微软平台的一个组件被商品化。因此，ChatGPT 应用平台的推出是独立宣言的必要之举，是直接掌控最终用户和开发者关系的战略举措。这迫使一个“竞合”新时代的到来，合作伙伴必须在 AI 技术栈中争夺主导平台角色。

## 结论

ChatGPT 应用平台的推出并非增量更新，而是向 AI 原生计算新模型的基础性转变。它预示着未来软件开发可能从构建离散、孤立的应用转向创建由中央 AI 代理协调的专业服务。

对于开发者和独立软件供应商 (ISV) 而言，这一时刻需要仔细的战略考量。分发机会是毋庸置疑的，但它也伴随着平台依赖固有的风险。一种谨慎的方法是识别现有产品中可以受益于新的混合对话式图形界面的特定用例。对于具有交易组件的企业而言，通过评估 ACP 规范来制定代理式商务战略现在是竞争的必然要求。

最后，在探索 OpenAI 平台上的机会时，开发者应寻求通过维护多平台战略并专注于构建带来独有、专有数据和功能的应用程序来降低长期风险，从而使其不易被平台所有者复制。