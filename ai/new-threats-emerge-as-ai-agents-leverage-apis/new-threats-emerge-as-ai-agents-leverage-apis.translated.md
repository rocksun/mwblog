# 随着 AI Agent 利用 API，新的威胁涌现

![Featued image for: New Threats Emerge as AI Agents Leverage APIs](https://cdn.thenewstack.io/media/2025/06/372cda12-kaffeebart-krpulsduetk-unsplash-1024x678.jpg)

[Kaffeebart](https://unsplash.com/@kaffeebart?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在 Unsplash 上发布。

一个简单的 AI 应用程序中的单个 API 漏洞可能会在几秒钟内泄露数千条用户记录。随着 AI Agent 成为主流，风险也随之而来。

AI Agent 代表了 AI 能力的巨大飞跃，超越了传统的 AI 自动化场景。虽然对于[确切的特征存在一些争论](https://www.wsj.com/articles/everyones-talking-about-ai-agents-barely-anyone-knows-what-they-are-8941e234?mod=cio-journal_lead_pos2)，但我们将 AI Agent 定义为一种多层 AI 应用程序，它根据其推理和上下文知识做出决策并自主行动。

即使您的公司尚未实施这些复杂的 AI 应用程序，您可能也已经意识到[采用率正在增长](https://www.gartner.com/en/articles/ai-agents)。AI Agent 将越来越多地影响 API 和应用程序，增加复杂性和自主性，并[产生独特的安全](https://thenewstack.io/security-needs-create-more-work-for-open-source-maintainers/)挑战。

## 为什么 AI Agent 依赖于 API

AI Agent 已经集成到各个行业的应用程序中，包括金融、电子商务、旅游、销售和游戏等。

它们可以为应用程序和系统做很多事情：自动化流程、实现即时决策和增强用户个性化。但是，如果没有 API 的帮助，这一切都不可能实现。API 将 AI Agent 连接到系统、应用程序、数据源和其他 Agent。它们还使 AI Agent 能够协调跨这些多层的操作。

**API 支持访问数据。** AI 应用程序需要访问准确、高质量的数据才能正常运行，通常包括实时数据和历史数据。
API 提供对[多个数据源](https://thenewstack.io/best-practices-collect-and-query-data-from-multiple-sources/)的访问，包括数据库、第三方 Web 服务、实时数据馈送和企业软件。

**API 扩展了 AI Agent 的能力。** API 使您能够向 AI 应用程序添加新的或专门的功能，例如实时翻译、图像识别或情感分析。为了构建这些 API，许多第三方服务可以提供专门的 API，或者您可以构建自定义 API 来增强 AI Agent 的能力。
**更多的 AI Agent 意味着更多的 API 访问数据和服务。** 随着 AI 应用程序数量的增加，与数据交互的 API 数量也会增加。这意味着攻击者有更多的 API 和数据可以攻击。
假设您的 Agent 仅访问存储在您的内部企业软件中的数据。它仍然需要一个 API 来检索和使用该数据。该 API 仍然容易受到我们今天所知的所有传统威胁的影响，例如 SQL 注入、跨站脚本 (XSS) 和身份验证漏洞。

如果您的 AI Agent 需要第三方数据或服务，您还必须为这些 API 中潜在的安全缺陷和漏洞做好准备。

## API 和 AI Agent 的未来

随着 AI Agent 发展成为复杂的、自主的工具，以无数种方式帮助人类和机器，[API 的作用变得越来越重要](https://thenewstack.io/the-future-of-apis-lessons-in-security-composability-ai/)。

**API 将提高 AI Agent 的自主性。** AI Agent 变得越来越自主，API 在这种独立性中发挥着重要作用。我们很快就会看到 AI 应用程序根据实时数据、上下文线索和不断变化的条件动态响应并协助用户。
例如，AI 旅行 Agent 可以帮助用户规划行程——自主决定调用哪些 API 以及以什么顺序调用，访问有关实时航班、酒店、交通和天气的数据。它还可以自动提出建议并预订旅行的一切。

**API 将增强**[AI Agent 协作。API 将促进 AI Agent 和人类用户之间的自动](https://thenewstack.io/how-ai-agents-are-starting-to-automate-the-enterprise/)协作，使他们能够更有效地完成任务。
一家连锁杂货店可以使用 AI Agent 监控实时天气数据，预测对特定产品的需求增加，例如，在重大热浪期间冰淇淋购买量的突然激增。AI Agent 可以跟踪热浪进展时的库存水平，自动下达补货订单并将高需求冰淇淋产品运送到受影响地区的仓库。移动购物应用程序中的 AI Agent 可以与库存 AI Agent 协同工作，根据客户的偏好和可用性推荐产品。
复杂的 AI 代理生态系统可能导致混乱的 API 连接。AI 代理通常利用多个 API 来获取完成一系列任务所需的数据和服务。我们正在构建一个由数千个多层 AI 应用程序组成的生态系统，这些应用程序协同工作以解决复杂的问题并处理大量长期用户交互。

这些相互连接的 AI 应用程序和 API 的复杂性将使[保护它们比以往任何时候都更具挑战性](https://thenewstack.io/the-challenges-of-securing-the-open-source-supply-chain/)。尤其是因为攻击者不断调整他们的技术，以更好地在雷达下飞行。

公司必须重新评估其 API 和应用程序开发流程，以应对即将到来的 AI 发展，尤其是在安全性方面，因为这些应用程序将放大常见的漏洞并引入新的漏洞。

## AI 代理带来独特的安全挑战

在 2024 年 CISA 已知被利用漏洞 (KEV) 目录中列出的[漏洞](https://www.wallarm.com/reports/2025-api-security-report)中，超过 50% 与 API 相关，高于前一年的 20%。

API 漏洞是所有类型 AI 产品的一个重要问题。直接威胁包括过度的数据暴露以及薄弱或损坏的 API 身份验证或访问控制。间接漏洞包括第三方集成或 API 充当中间媒介的系统中的缺陷。

管理新的 API 安全挑战与 AI 代理的增长息息相关。尽管如此，最重要的原则仍然是熟悉的，因为它与所有软件开发相同：[零信任](https://www.getambassador.io/blog/the-importance-of-zero-trust)。保护 AI 和 API 意味着默认情况下永远不要信任任何用户（人或机器）、设备或系统。进入内部后，按会话对它们进行身份验证（而不是在边界处进行一次身份验证）。

要在即将到来的 AI 代理时代保持领先地位，意味着要管理传统的 API 漏洞和新兴的 AI 特定威胁。API 或 AI 功能中只需一个漏洞就可能危及您的 AI 应用程序，并最终危及您的系统和数据。

## 保护 AI 代理的未来

公司必须为即将到来的由 AI 代理和 API 驱动的应用程序海啸做好准备，[转型时代已经来临。](https://www.forbes.com/councils/forbestechcouncil/2025/03/18/ai-will-transform-software-development-but-not-the-way-you-expect/)

使 AI [代理能够更难手动管理安全性](https://thenewstack.io/what-hal-9000-teaches-us-about-ai-driven-authorization/)或快速响应的复杂 API 交互，因此请选择自动化方法和主动默认限制。被动措施根本无法跟上变化的步伐。

立即开始准备安全策略，以保护未来的 API 和 AI 代理。

*TNS 的所有者 Insight Partners 也投资了 Ambassador。因此，Ambassador 作为贡献者获得了优先权。*

[
[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
]