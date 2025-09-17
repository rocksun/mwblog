
<!--
title: 人机协同：驯服失控的AI
cover: https://cdn.thenewstack.io/media/2025/09/805cfc41-herding.jpg
summary: AI代理风险日益增加，例如数据泄露和数据库删除。Eve Security通过代理在环技术应对，该技术检测可疑行为，减少误报。其EveGuard平台观察代理交互，了解意图，进行风险分析，并与SIEM等工具集成，提供全面的安全防护。
-->

AI代理风险日益增加，例如数据泄露和数据库删除。Eve Security通过代理在环技术应对，该技术检测可疑行为，减少误报。其EveGuard平台观察代理交互，了解意图，进行风险分析，并与SIEM等工具集成，提供全面的安全防护。

> 译自：[Using Agent in the Loop To Ride Herd on Wayward AI](https://thenewstack.io/using-agent-in-the-middle-to-ride-herd-on-wayward-ai/)
> 
> 作者：Susan Hall

开发团队面临着越来越大的压力，需要在采用 AI 代理的同时，应对代理失控的风险，例如[泄露敏感数据](https://www.pomerium.com/blog/when-ai-has-root-lessons-from-the-supabase-mcp-data-leak)，以及在某个案例中[删除生产数据库](https://x.com/amasad/status/1946986468586721478?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1946986468586721478%7Ctwgr%5E0b243406d50a289d0a25f3478ed7ff3f55bf7bd6%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.notion.so%2Fosohq%2F2389f1471f2b80c3b076e6bfcaac749b&utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)。

OpenAI 前首席科学家兼联合创始人 [Ilya Sutskever](https://www.linkedin.com/in/ilya-sutskever) 表示，AI 代理的自主行为将[随着时间的推移变得更加不可预测](https://www.reuters.com/technology/artificial-intelligence/ai-with-reasoning-power-will-be-less-predictable-ilya-sutskever-says-2024-12-14)，因此有人警告说[它们是“定时炸弹”](https://thenewstack.io/ai-agents-are-a-security-ticking-time-bomb/)，并呼吁建立[新型安全和治理措施](https://thenewstack.io/ai-agents-are-creating-a-new-security-nightmare-for-enterprises-and-startups/)。

位于德克萨斯州奥斯汀的初创公司 [Eve Security](https://www.eve.security/) 正在走出隐身模式，以代理在环技术应对这一挑战，该技术可以检测并处理可疑的代理行为，同时减少过多警报对人工干预的干扰。

Eve Security 的联合创始人兼首席执行官 [Nadav Cornberg](https://www.linkedin.com/in/nadav-cornberg/) 说：“我们从客户那里听到的是……许多部门现在都在推动代理活动、代理能力，因为他们觉得自己落后了。因此，有来自高层管理人员的授权，有来自部门领导的授权，甚至还有来自基层员工的推动。”

“CISO 部门有点被逼到了墙角。[他们说]‘你正在影响业务。我们需要一个解决方案。’另一方面……如果我们将 AI 代理连接到 Grubhub，[它] 不小心订购了 20 个赛百味，我没关系。但是，如果你开始将其连接到 Salesforce 或 GitHub 或 NetSuite，并且突然它弄乱了这些系统，猜猜 CEO 会来砍谁的头？对吧？我要承担责任。”

## 控制漫游代理

通过代理在环方法，人类仍然进行监督，但代理嵌入在工作流程中，以解析哪些操作真正值得怀疑。

当联合创始人 Cornberg、[Amit Eliav](https://www.linkedin.com/in/amiteliav/overlay/about-this-profile/) 和 [Sharon Eilon](https://www.linkedin.com/in/sharoneilon/overlay/about-this-profile/) 着手成立公司时，他们想了解 CISO 们的痛点。他们发现 CISO 们担心将 AI 代理连接到包含公司“皇冠上的宝石”数据的系统。他们将如何管理它？与此同时，他们担心会被太多的警报淹没，以至于他们必须安排专门的人员来筛选所有警报，以找到真正关键的警报。

凭借其 EveGuard 平台，其代理在环可以观察代理以及代理与业务系统之间的交互，以采取必要的措施或将问题上报给人。它旨在了解行动背后的意图，以解决基于英语的策略中存在的盲点（例如翻译和文化细微差别），并评估与之相关的风险。

根据 LiveOak Ventures 的合伙人 [Creighton Hicks](https://liveoak.vc/team/creighton-hicks/) 的说法，AI 代理正在创建当今的安全工具无法看到漏洞。LiveOak Ventures 与 Tau Ventures 一起为该公司提供了 300 万美元的种子轮融资。

“目前，大多数安全领导者都在盲目飞行。Eve Security 使安全团队能够获得对其企业中运行的已知和未知代理 AI 的可见性和控制权，”他说。

该技术会查看每个代理通常执行的操作以及它是否执行任何其他操作。

## 风险是什么？

“当你查看像 MCP 这样的协议时……它不再是传统的请求和响应。它可能只是一个参数，上面写着‘请生成一份关于 Q1 和 Q2 所有财务信息的报告。将该报告发送给 [这些人并抄送给其他人]。然后请获取所有这些信息，将其转换为 PDF，然后将其保存到此目录，’”他解释说。

如果代理执行它历史上所做的事情，那就没问题。但是如果存在异常，它可能具有正确的权限，但这从未见过。或者这是否是超出策略范围的事情并且被多次重复？

Eve 集群行为进行风险分析。

例如，如果代理正在收集有关奥斯汀天气的信息，则以前可能没有见过这种行为，但对业务而言风险不大，Cornberg 解释说。但是，如果它要求提供 CEO 或其他敏感公司信息的工资，那应该是一个危险信号。然后，该技术可以询问代理，以了解请求背后的原因。

“所以我可以查看推理历史来了解。我可以了解它为什么要求提供它，”Cornberg 解释说。“你知道，实际上，CEO 登录了这里。他要求提供它。所以我做出了挑战性回应。现在，作为对 CEO 审讯的一部分，CEO 说，‘是的，是我。我正在要求提供该信息。’好的，我只会允许一次，所以我不需要将其上报，而不是，你知道吗？不，这里没有真正的理由。我不允许这样做，但我会将其上报给我的经理，因为我无法批准。”

Eve 组件安装在客户侧，该组件与安全信息和事件管理 (SIEM) 以及公司在其中定义策略的其他工具集成，例如基于角色的访问控制、保护个人身份信息 (PII) 和其他数据。它支持 [模型上下文协议 (MCP)](https://thenewstack.io/mcp-a-practical-security-blueprint-for-developers/) 和 [代理到代理 (A2A)](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/) 协议，这些协议提供了[对 AI 代理交互的见解](https://thenewstack.io/why-are-agent-protocols-like-mcp-and-a2a-needed/)以及代理到代理的协调和委派链。

与网络工具、端点工具和构建代理所用的框架的集成对于提供对正在发生的事情的全面了解是必要的。

从那里，公司可以识别并仅允许经批准的代理运行，从而消除来自“影子”代理的风险；实时清理代理 AI 输出，以防止 [提示注入攻击](https://thenewstack.io/7-llm-risks-and-api-management-strategies/)；保护敏感信息并执行访问策略。

## 检测和响应

Cornberg 说，Eve Security 的重点比其最接近的竞争对手更窄——他指出了 [Lasso Security](https://www.lasso.security/) 和 [Aim Security](https://www.aim.security/post/aim-to-join-cato-network)（现在是 Cato Networks 的一部分）。它没有广泛地包括姿势方面，即设置权限和策略，而是深入研究检测和响应。代理允许做什么？它应该这样做吗？

Eve Security 顾问兼云原生计算基金会 CTO [Chris Aniszczyk](https://www.linkedin.com/in/caniszczyk/) 称这家新初创公司“有点像 AI 自动驾驶时代的**安全**带”。

联合创始人 Eilon 指出，并非所有风险都来自外部。

“这是任何监管，对吧？这是共享信息。这是利用这些信息做事情。也许它正在向外发送电子邮件。它应该使用我的姓名和地址向组织外部发送电子邮件吗？我不知道，”他说。

“我们查看该通信，我们看到，什么是意图，以及它被授权做什么。如果没有授权问题，它可以执行该活动。没有人告诉它不要这样做。但是它应该这样做吗？需要有人检查。……世界正在步入一个非常不确定的问题领域，我们来这里是为了解决这个问题。”