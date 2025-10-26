
<!--
title: 揭秘麻省理工NANDA：AI智能体去中心化革新之路
cover: https://cdn.thenewstack.io/media/2025/10/9be57535-sophia-kunkel-cxlcuypqabs-unsplashb.jpg
summary: NANDA项目旨在构建去中心化的AI代理互联网，通过索引、AgentFacts、注册中心被子和跨协议互操作性，提供开放的代理网络蓝图，挑战商业平台垄断。
-->

NANDA项目旨在构建去中心化的AI代理互联网，通过索引、AgentFacts、注册中心被子和跨协议互操作性，提供开放的代理网络蓝图，挑战商业平台垄断。

> 译自：[How MIT’s Project NANDA Aims To Decentralize AI Agents](https://thenewstack.io/how-mits-project-nanda-aims-to-decentralize-ai-agents/)
> 
> 作者：Richard MacManus

2025 年已成为 [AI 代理之年](https://thenewstack.io/the-agentic-web-how-ai-agents-are-shaping-the-webs-future/)，迄今为止，大多数开发者的关注点都集中在构建这些代理的框架和工具上。我们最近在这个领域看到了大量发布：OpenAI 的 [AgentKit](https://openai.com/index/introducing-agentkit/) 和 [Agents SDK](https://thenewstack.io/introduction-to-the-openai-agents-sdk-and-responses-api/)、Anthropic 的 [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview)、Google 的 [Agent Development Kit](https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications/) (ADK) 以及 [Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder)。

那么代理的发布和分发呢？我们已经看到 OpenAI 新推出的 [Apps SDK](https://thenewstack.io/openai-launches-apps-sdk-for-chatgpt-a-new-app-platform/) 形成了一种类似应用商店的模型，它允许开发者在 ChatGPT 内部发布代理。但是，是否有一种不依赖于 OpenAI 等商业平台的方式来提供代理呢？MIT 的一个团队希望通过 Project NANDA 来实现这一点。

[Project NANDA](https://nanda.media.mit.edu/)——即 Network of AI Agents and Decentralized Architecture 的缩写——是 MIT 媒体实验室的一项倡议，旨在为“AI 代理互联网”构建去中心化基础设施。目标是建立一个代理生态系统，其中包括跨平台或跨供应商的发现、联邦式注册中心以及开放的身份和信任层。

## **NANDA 是什么？**

首先要注意的是，NANDA 基于 Anthropic 的模型上下文协议（MCP）和 Google 的代理到代理（A2A）协议。但除了这两个开源项目之外，还有更多内容。在 [今年早些时候的一次演示中](https://www.youtube.com/watch?v=yXxHb3LMygw)，NANDA 的负责人、MIT 副教授 Ramesh Raskar 将整个项目比作一块被子。

[![NANDA quilt](https://cdn.thenewstack.io/media/2025/10/46a6df5e-nanda-quilt-2025.png)](https://cdn.thenewstack.io/media/2025/10/46a6df5e-nanda-quilt-2025.png)

*NANDA 被子；图片来源：Ramesh Raskar*

NANDA 的架构由四个主要层组成：发现、身份、联邦和互操作性。它们共同旨在实现一个自主但可验证的代理世界。以下是每一层的详细说明：

### **NANDA 索引**

基础是**索引**，这是一个 [全球分布式参考索引](https://arxiv.org/pdf/2507.14263)，它将代理句柄映射到经过验证的元数据文件或端点。

在 [MIT 媒体实验室的概述中](https://www.media.mit.edu/projects/mit-nanda/overview/)，索引被描述为“代理的 DNS”，它能够“实现网络上的发现、身份验证和可验证交互”。

其理念是，当一个代理查询另一个代理时，索引会将请求路由到相关的注册中心，验证加密签名并返回请求的数据——所有这些都没有中央瓶颈。

目前，该索引托管在全球 15 所大学和合作机构。

### **AgentFacts**

每个代理都必须是可识别和可追溯的。这就是 **AgentFacts** 的作用所在：带有签名、经过模式验证的 JSON-LD 文档，描述了代理可以做什么、谁操作它以及如何安全连接。

这种机制为代理网络带来了“零信任”理念。是的，在 NANDA 的各种学术论文中，不幸地倾向于使用“Web3”这个术语，这有点令人不快。无论如何，关键是代理在参与之前会验证凭证。

### **注册中心被子**

也许 NANDA 文献中最具启发性的比喻是**注册中心被子**，这是一个由独立运行的代理注册中心组成的联邦式结构。

Project NANDA 的研究员 Mahesh Lambe [将注册中心被子描述为](https://medium.com/@maheshlambe/deep-dive-project-nanda-part-4-the-registry-quilt-federating-agent-registries-with-gossip-fb30a4179859)“一个联邦层，将许多自主代理注册中心（Web2 和 Web3）编织成一个全球可发现的结构——而无需创建单一控制点。”

这有点类似于 Mastodon 和 PeerTube 等产品如何 [在 ActivityPub 开放标准上运行](https://thenewstack.io/the-creator-of-activitypub-on-whats-next-for-the-fediverse/)，其理念是每个实体或组织都可以托管自己的注册中心，同时通过全球索引保持可发现。

### **跨协议互操作性**

如前所述，NANDA 已经支持 Anthropic 的 [MCP](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) 和 Google 的 [A2A](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/)。它还支持 [自然语言网络](https://thenewstack.io/cloudflares-balancing-act-protect-content-while-pushing-ai/)（NLWeb），这是 Microsoft 正在兴起的将 AI 聊天集成到网站中的标准。

Ramesh Raskar 在最近的 LinkedIn 帖子中 [将 A2A 描述为](https://www.linkedin.com/feed/update/urn:li:activity:7347037374851301377/)“道路”，将 NANDA 索引描述为 Project NANDA 正在构建的“代理之城”中的“房屋和商业目录”。此类项目中的比喻可能很快堆积如山并令人 overwhelmed，但关键在于 MCP 和 A2A 等协议是 NANDA 的技术基础——如果它要真正与 Anthropic、Google 和 OpenAI 等公司的代理框架互操作，就应该如此。

## **开发者活动**

尽管以研究为主导，Project NANDA 仍试图通过几个相关项目来启动开发者社区：

*   [Join39](https://join39.org/how-it-works) 邀请用户“创建您的个人 AI 代理，获取代理事实，并开始在 NANDA 网络中代表自己”。[目录](https://join39.org/agents) 目前列出了 1,000 多个代理。
*   [List39](https://list39.org/) 是一个“代理事实注册中心”，允许您将代理注册为 JSON 文档。
*   [aidecentralized GitHub 项目](https://github.com/aidecentralized/) 托管论文、代码和注册中心适配器。
*   [projnanda GitHub 网站](https://projnanda.github.io/projnanda/#/) 包含文档和演示。

## NANDA 有争议的 AI 商业报告

尽管这与本文讨论的 Project NANDA 的技术架构没有直接关系，但值得一提的是，NANDA 在 7 月份发布了一份报告，该报告被广泛宣传。[该报告](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf) 声称“95% 的组织从生成式 AI (GenAI) 中获得零回报”。

沃顿商学院教授 Kevin Werbach 在 [一篇 LinkedIn 帖子中](https://www.linkedin.com/posts/kevinwerbach_state-of-ai-in-business-2025-activity-7365026841759215616-SQWD/) 对这一发现提出异议，并表示该报告“问题重重”。牛津大学应用人工智能研究员兼教师 Ajit Jaokar 也表示同意，并 [称该报告](https://www.linkedin.com/pulse/mit-nanda-report-clever-marketing-gimmick-ajit-jaokar-uiufe/) 是“一个聪明的营销噱头”。与实际的 NANDA 项目更相关的是，Jaokar 指出：

“独特的是，该报告声称缺乏学习、记忆等正在阻碍企业部署。当然，NANDA 通过分布式架构实现了这一目标。这使得结论与产品功能绑定。”

## NANDA 会获得关注吗？

NANDA 的统计数据可能存在争议，但该项目的架构看起来足够稳固。这最终是否重要则是另一回事。

像 MIT 这样的学术机构，历史上曾发明过前瞻性平台，但这些平台要么从未发展成商业平台，要么其想法被硅谷初创公司采纳并成为专有技术。最著名的例子当然是 Xerox PARC 和图形用户界面（GUI），Steve Jobs 欣然采纳并推向市场。

很明显，某种用于代理开发和使用的去中心化架构将优于由一两家大公司拥有生态系统——正如智能手机应用程序所发生的那样。随着 [OpenAI 新兴的 ChatGPT 应用程序平台](https://webtechnology.news/openai-turns-chatgpt-into-a-web-app-platform/)，代理已经面临着遵循智能手机应用蓝图的风险。因此从这个角度来看，我希望 NANDA 确实能帮助引导代理走向开放的 Web 未来。

无论 NANDA 本身是否成为主流平台，其开放设计至少为**代理网络**如何演变提供了可靠的蓝图。这里面的想法很重要：联邦式发现、可验证身份、协议桥梁。这些想法呼应了早期网络的設計以及仍在发展的开放社交网络世界（又称联邦宇宙）。