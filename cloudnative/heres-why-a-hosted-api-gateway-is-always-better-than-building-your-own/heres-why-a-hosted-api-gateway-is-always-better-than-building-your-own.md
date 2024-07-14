
<!--
title: 托管API网关为何总是优于自建
cover: https://cdn.thenewstack.io/media/2024/07/963124f9-chip-6517875_1280.jpg
-->

不要浪费开发人员的时间在基础设施和安全方面追赶。

> 译自 [Here’s Why a Hosted API Gateway Is Always Better Than Building Your Own](https://thenewstack.io/heres-why-a-hosted-api-gateway-is-always-better-than-building-your-own/)，作者 Josh Twist。

当您准备启动 API 时，自己构建 [API 网关](https://thenewstack.io/the-api-gateway-and-the-future-of-cloud-native-applications/) 似乎是个好主意——更多控制权、定制化，甚至更多成本节约。有什么不喜欢的呢？

很多。一旦您深入 [内部 API 管理](https://zuplo.com/build-vs-buy-api-management-tools) 的深渊，您会发现很多不值得喜欢的东西。

构建很有趣，但维护很糟糕。您构建的 [API](https://thenewstack.io/api-management/) 越多，维护工作就会越让您的团队感到厌烦，从而阻止构建工作。您需要考虑限速、授权、测试和基础设施等问题，所有这些都会让您的团队无法构建用户想要的东西。

托管 API 网关消除了所有这些负担，并将从各个方面改善您的 API、团队和用户。以下是具体方法。

## 更低的成本

成本是 API 团队不愿转向云托管解决方案的首要原因之一。他们会看到一个明确的价格，知道它会出现在他们的信用卡账单上，然后会想，“我们可以通过自己动手来节省 X 元。这有多难？”

这是典型的“最后的遗言”。这显然是虚假经济，表面上的 [节省掩盖了隐藏的成本](https://thenewstack.io/enterprise-application-cost-savings-using-serverless-computing/)，但：

1. **开发人员很贵**。工程是一项宝贵的技能，尤其是在开发、维护和管理 API 网关所需的水平上。您需要个人贡献者或专门负责此任务的团队。您还需要考虑随着时间的推移，招聘、入职和留住这些人才的成本。这些成本会迅速累积，超过任何通过内部构建获得的感知节省。
2. **无论如何，您都需要为基础设施付费**。API 管理工具提供了一些用于管理 API 的基础设施。[如果您不使用平台来执行此操作](https://thenewstack.io/developing-a-platform-mindset-for-apis/)，则需要构建该平台。这将需要什么？也许是一些令人愉快的无服务器实例。它有点像边缘网络。这里那里有一个负载均衡器。一些反向代理、一些监控、一些缓存。所有这些都有成本（除非您要环游世界设置您的边缘网络？我想您必须考虑机票成本），并且都需要管理。
3. **您无法做其他事情**。用专业术语来说，每当您选择独自完成而不是寻求帮助时，都会产生*机会*成本。如果您有开发人员维护您的 API，他们就不会构建它。如果您想让他们制作您的 API，您必须雇用专门负责管理 API 的人，这（回到第一点）将比支付网关费用更贵。

[托管 API 网关可以节省资金](https://zuplo.com/build-vs-buy-api-management-tools%23cost)，这意味着您的开发人员可以继续开发，您的基础设施可以继续成为一个简单的后端，因此您不需要一个全新的运维团队。

## 更高的安全性

API 会受到攻击——很多。世界上充斥着 [API](https://www.itsecurityguru.org/2024/03/11/what-we-learned-from-these-3-api-security-breaches/) [被](https://thehackernews.com/2022/11/dropbox-breach-hackers-unauthorizedly.html) 泄露 [数据](https://www.darkreading.com/cyberattacks-data-breaches/fbi-helping-australian-authorities-investigate-massive-optus-data-breach-reports) 的故事。API 是攻击者攻击的重要目标。[Salt Security 的 API 安全状况报告](https://content.salt.security/state-api-report.html) 发现 **94%** 的受访者在其 *生产* API 中遇到了安全问题。

如果您认为自己可以在内部抵御这些攻击，那您就是在自欺欺人。您也在欺骗您的客户，让他们认为您的 API 是安全的。就像支付、合规性或准备 Fugu 一样，[API 安全](https://zuplo.com/docs/articles/securing-your-backend%235-secure-tunneling) 应该外包给专业人士。当我们说安全时，我们的意思是：

- **身份验证**。你是谁。*验证您的用户是[API 安全的最低要求](https://thenewstack.io/what-it-requires-to-secure-apis-for-microservices/)。但是，需要进行大量的集成才能识别提供商，了解 OAuth 2.0 和 JWT 等标准，以及[在整个 API 使用过程中管理用户及其数据](https://thenewstack.io/data-management-on-a-decentralized-data-mesh/)。API 网关将提供与 OAuth 2.0 和 JWT 等身份验证机制的开箱即用集成，确保您的[API 安全](https://thenewstack.io/to-support-business-continuity-address-your-api-security/)。
- **授权**。你能做什么。*这是用户更多地使用您的 API 时的下一步。他们到底被允许做什么？他们可以获取什么？他们可以发布什么？他们可以删除什么？您需要通过访问控制机制（例如基于角色的访问控制 (RBAC)、基于属性的访问控制 (ABAC) 或基于资源的访问控制 (ReBAC)）来控制所有这些。您认为自己可以做到吗？以下是[Google 关于其系统（供您实施）的十四页研究论文](https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/)。API 网关应提供全面的授权功能，例如 RBAC，使您能够轻松地在整个 API 生态系统中定义和执行访问策略。
- **API 密钥管理**。API 密钥是您最常用来管理对 API 访问的方式。这意味着实施密钥生成、分发、存储、轮换和撤销。然后，这里的每个组件都成为攻击的独立媒介。API 网关提供内置的 API 密钥管理功能，处理 API 密钥的安全创建、存储和生命周期管理，减轻开发团队的负担，并降低密钥泄露的风险。
- **速率限制**。速率限制似乎是为了阻止您的后端过载。但是，其核心功能是作为[防止滥用并保护您的 API 的关键安全措施](https://thenewstack.io/beyond-api-security-testing-runtime-protection/)，防止过多的恶意流量淹没您的 API。通过设置用户或系统在给定时间段内可以发出的请求数量限制，您可以降低 DDoS 攻击的风险，并确保 API 的稳定性和性能。API 网关提供可配置的速率限制选项，允许您根据各种标准（例如 API 密钥、IP 地址或用户帐户）定义和执行使用限制，而无需实施和维护此功能。
  
## 更适合定制

这似乎违反直觉。实际上，内部构建为您提供了无限的定制——毕竟，内部构建是定制的缩影！

在某种程度上。内部构建将为您提供一个完全定制的解决方案，但方向错误。您最终将获得针对例如 OAuth 2.0 集成的定制解决方案（仅供说明：*这很糟糕*），但无法访问可能对您的 API 有用的定制。

例如：**降级**。降级是一种技术，用于在完全弃用功能之前优雅地降低 API 性能。与其让 API 崩溃或变得无响应，不如暂时禁用特定功能，以便为用户做好即将下降的准备。实施降级需要仔细规划、监控和根据实时条件调整 API 行为。

另一个例子：**A/B 测试**。您应该测试不同的 API 功能或性能版本，以确定哪个版本提供最佳的用户体验或实现特定的业务目标。A/B 测试涉及将一部分 API 流量路由到 API 的变体版本，而其余流量则发送到原始版本。

这些只是 API 网关提供的定制选项的两个示例。主要优势是这些定制建立在平台强大的、安全的和可扩展的基础之上。这意味着您可以专注于根据自己的需求和用户要求定制 API，而不是为基本功能重新发明轮子。

[API 网关通常提供各种预构建的策略](https://thenewstack.io/effective-traffic-management-with-kubernetes-gateway-api-policies/)、模板和集成，这些策略、模板和集成可以轻松定制和扩展以适应您的独特用例。这使您能够利用最佳实践，同时仍然具有灵活性，可以根据您的业务目标调整 API。

## 专注于创新，而不是维护

[云托管 API 网关](https://zuplo.com/) 是管理 API 的最佳选择。通过将基础设施、安全性和定制的繁重工作外包给专家，您可以腾出团队的时间专注于重要的事情：构建和创新 API。

总而言之，[云托管 API 管理解决方案](https://zuplo.com/features/multi-cloud/) 的优势显而易见：

- **安心**：拥有专家团队处理可靠性、可扩展性和安全性等细节问题，您知道您的 API 处于安全可靠的状态。
- **效率**：外包基础设施管理可以让您的开发人员专注于他们最擅长的工作：构建优秀的软件。
- **战略优势**：凭借按需扩展的灵活性以及定制和功能的访问权限，您可以保持领先地位，并随着 API 的增长快速适应。

因此，不要让您的开发人员浪费时间追赶基础设施和安全问题。让他们发挥自己的优势：构建出色的 API，以取悦您的用户并推动您的业务发展。
