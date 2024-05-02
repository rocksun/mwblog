# API 趋势：平台工程、解耦和 AI 的作用

![API 趋势的特色图片：平台工程、解耦和 AI 的作用](https://cdn.thenewstack.io/media/2024/04/3ffd9b33-unrolling-1024x576.jpg)

在营销炒作的喧嚣中找到对开发人员真正重要的事情可能具有挑战性。最近，在 Ambassador，我们 [策划了一个行业专家小组](https://www.youtube.com/watch?v=vHTknfpE6Jg&t=3s)，涵盖了 [API 开发](https://thenewstack.io/what-is-api-management/) 领域，以探讨塑造 API 格局的关键趋势最近几个月。现在，让我们考虑一下真正值得关注的内容以及哪些只是背景噪音。

## 大解耦尚未达成普遍共识

尽管过去六个月来，Gartner、Kong 和其他行业专家在业内引起了轰动，但 [API 管理的大解耦](https://apievangelist.com/2023/10/14/the-great-api-unbundling/) 理论仍然是一个有争议的话题。“[大解耦](https://thenewstack.io/the-great-unbundling-jamstack-and-the-future-of-the-web/)” 的理念侧重于从单一全套工具转向最佳的利基解决方案。我们的一些专家认为，这是一种更加消极的姿态，他们解释说，他们合作的大多数企业不想投入时间、资源和预算来将不同的 [API 管理工具](https://www.getambassador.io/api-management-hub) 集成到其交付管道中。

“[Launch Any](https://launchany.com/about/) 的行业专家组成员兼 API 顾问 James Higginbotham 分享道：“我的许多客户都感到非常沮丧，因为没有一种简单的方法可以将所有这些工具整合在一起，所以这并不像有些人想象的那么容易。”

然而，另一位小组成员 Keith Casey 认为，解耦是对多年来幕后发生的事情的一种认可——它现在只是公开的。他指出，虽然许多公司声称已经标准化了一套工具，但实际上，例如微网关正在整个组织中部署。所有人都同意，无论开发人员选择哪条路线，更好的工具集成和打包都会让事情变得更容易。简而言之：应用于您的 API 开发流程的策略比您添加到技术堆栈中的工具数量或数量少更重要。

“开发人员在生活中有两个目标：构建有用的东西并回家。现在，有太多事情阻碍我们构建有用的东西，以至于我们无法回家，这令人沮丧。”

– [Pangea] 的高级产品经理 Keith Casey

## AI 是 API 安全中的双刃剑

随着 AI 系统 [更多地集成](https://thenewstack.io/ai-has-become-integral-to-the-software-delivery-lifecycle/) 到日常应用程序和流程中，通过 API 交换的数据变得越来越敏感、可能暴露和有价值。确保 [这些 API 的安全性](https://thenewstack.io/why-api-security-is-different-and-how-the-openapi-spec-can-help/) 对于防止潜在的违规、数据泄露和未经授权的访问至关重要。随着 AI 时代安全漏洞的潜在后果变得更加严重，小组讨论的一个明确结论是，我们必须优先实施 [严格的安全协议](https://thenewstack.io/security/) 来保护 API 基础设施及其处理的敏感数据。

Casey 分享道：“每次我们想到‘哦，没有人会用我们的 API 做那件事’时，我们需要回顾并重新考虑我们的假设。我们需要假设有人会用我们的 API 做这件事，但意识到那个人可能不是人类。”

[APIsec University](https://www.apisecuniversity.com/) 的创始人、小组成员 Dan Barahona 强调了 API 与 AI 之间不断交织的关系，以及这种关系对 API 安全的影响。人们非常担心 AI 可能被用作攻击媒介。执行极其复杂的攻击变得越来越容易。另一方面，AI 也极有可能用于防御和安全。

Barahona 说：“我们需要询问如何利用 AI 进行防御，以及如何主动防御 AI 安全攻击。我们需要评估安全硬币的双方。所有 API 从业者都应该问自己，‘我们如何将 AI 纳入我们的安全工具中？’”

技术领导者应该假设他们的开发人员已经在大量使用 AI 作为探索和测试工具，并且随着技术的进步，这种使用只会增加。立即制定您的 AI 政策和最佳实践，并聘请对如何最大化 AI 工具功能有深刻理解的开发人员，同时认识到没有一种工具可以完全替代强大的开发人员。
**左移安全**

此外，我们的专家组成员指出，在安全领域似乎有一种强烈的推动，即“左移”[安全](https://www.apisec.ai/blog/shift-left-security)”，而不是有争议的“右移盾牌”。“右移盾牌”专注于采取被动安全措施，以保护已部署系统免受潜在威胁。另一方面，“左移”优先考虑在开发过程的早期阶段主动集成安全，以防止漏洞，例如尽早集成 API 网关之类的工具（https://www.getambassador.io/products/edge-stack/api-gateway/security-authentication）。这种早期集成允许将安全功能构建到开发过程中，这与“左移”理念相一致，即尽早解决安全问题。

**从卓越中心到赋能中心**

虽然[平台工程](https://www.getambassador.io/kubernetes-expert-interviews/self-service) 席卷全球，但我们首先需要踩刹车，并正确掌握基础知识。有时，平台团队或卓越中心 (COE) 的神话是，他们是从象牙塔中发表声明，而不是成为解决 DevOps 挑战的解决方案中不可或缺的一部分。专家组成员一致认为，重点需要从“*我如何管理此平台？”演变为“我如何帮助人们提高工作效率？”

“稍微后退一步，从平台工程的热潮中跳出来，平台工程目前非常注重内部，而且规模很大，在我们甚至谈论平台之前，我们需要为我们的开发人员做很多自动化使能工作，”Higginbotham 分享道。“让我们将对话转移到专注于 API 使能，并着眼于使能中心或卓越中心。”

Casey 附和了 Higginbotham 的观点，他表示向使能中心 (C4E) 的转变是成功实施现实世界平台工程的关键。他对比了服务和帮助人们提高工作效率的心态与传统的做法，即发布高级声明，并期望开发人员盲目地遵循。

“COE 专注于使能 API 设计人员、提供团队和消费者，而不是如此专注于实现和交付 API 的代码，”Higginbotham 分享道。

例如，如果你有一个团队正在构建 API，那么在组织内可能有 150 个不同的团队在使用它，这意味着如果没有一个精简的平台团队，你可能每次都与这 150 个利益相关者进行完全相同的对话。

投资采用 COE 方法的稳固平台团队意味着你正在投资适当的文档、支持、代码示例和其他资源，这些资源可以减少或完全消除这些对话。此外，这些资源还可以更好地使消费者能够开始使用你的 API。

因此，结论是：是的，平台工程在 API 开发中越来越重要，只要我们首先关注交付使能和开发人员使能。你的平台策略和 COE 应该协同工作，以实现真正的 API 成功。

**最后**

这些并不是新概念，但 API 开发领导者对这些趋势所采取的方法和尽职调查将对他们的开发人员是否能够做出积极响应产生天壤之别。有关更多信息，请查看我们[YouTube 频道](https://www.youtube.com/watch?v=vHTknfpE6Jg&t=3s) 上的 API 管理小组的完整技术讨论。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。