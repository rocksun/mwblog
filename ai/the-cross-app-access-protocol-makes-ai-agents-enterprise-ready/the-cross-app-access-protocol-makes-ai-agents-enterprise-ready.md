<!--
title: 跨应用访问协议：解锁AI智能体，赋能企业级应用
cover: https://cdn.thenewstack.io/media/2025/09/9458c9c1-okta-logo-2025-scaled.jpg
summary: “跨应用访问”（XAA）协议获Okta、AWS等支持，旨在将AI代理整合到现有身份管理中，确保代理安全访问数据。它将安全管理负担从用户转移至管理员，提高企业AI治理和可见性。
-->

“跨应用访问”（XAA）协议获Okta、AWS等支持，旨在将AI代理整合到现有身份管理中，确保代理安全访问数据。它将安全管理负担从用户转移至管理员，提高企业AI治理和可见性。

> 译自：[The Cross App Access Protocol Makes AI Agents Enterprise-Ready](https://thenewstack.io/the-cross-app-access-protocol-makes-ai-agents-enterprise-ready/)
> 
> 作者：Frederic Lardinois

*Okta 为本文作者提供了差旅资助，以参加其 Oktane 大会。*

拉斯维加斯——大多数企业现在都以某种形式使用 [AI 代理](https://thenewstack.io/ai-agents-and-their-life-cycle-what-you-should-know/)，但很少有企业建立任何治理系统来控制它们。一项名为“跨应用访问”（Cross App Access，简称 XAA）的新开放协议，获得了 Okta、[AWS](https://aws.amazon.com/?utm_content=inline+mention)、Box、Glean、Grammarly、Miro 和 Writer 等公司的支持，旨在将代理引入现有的[身份管理](https://thenewstack.io/banking-on-identity-management-to-boost-revenue/)解决方案中，以管理它们可以访问的数据类型。

XAA 将代理视为现有安全和身份管理服务（如 [Okta](https://www.okta.com/)）中的一等实体。这反过来也意味着，随着开发人员在几乎没有监督的情况下试用和部署代理，安全团队可以收回他们目前正在失去的一些控制权和可见性。

该协议旨在与 Anthropic 的模型上下文协议 (MCP) 和 Google 的 Agent2Agent (A2A) 等现有协议互补。XAA 关注的不是代理如何与其工具对话，而是确保这些代理可以安全地访问应用程序，并且只获得其应有权限访问的应用程序和数据。

身份管理服务 Okta 的总裁兼首席运营官 Eric Kelleher 本周早些时候在该公司年度 Oktane 用户大会上表示：“当代理在没有适当治理的情况下从原型进入生产时，公司目前面临巨大风险，因为需要确保代理身份得到妥善管理、存在于目录中、经过身份验证、获得授权并且有适当的治理措施。”

目前，如果代理需要访问主要用户之外的任何内容，基本上有两种方法。大多数开发人员会简单地使用 API 密钥。“这对 CISO 来说是可怕的，因为你实际上必须将‘王国’的钥匙交给这个代理——这个非确定性实体，”Okta 产品副总裁 Jack Hirsch 告诉我。

![跨应用访问控制图](https://cdn.thenewstack.io/media/2025/09/d33613ae-caa-okta.png)

*图片来源：IETF。*

另一种选择是用户控制的 OAuth 授权，但这很快就会让安全团队不堪重负，并且难以追踪。Hirsch 补充说：“它将安全负担从安全组织转移到最终用户——在企业中，这是一种糟糕的用户体验。”因为例如，一名新员工可能需要经历几十甚至数百个 OAuth 流程才能开始真正的工作。

XAA 旨在通过让安全操作员控制这些代理的访问权限，使这一切变得容易得多。而且，由于它是 [OAuth 标准的扩展](https://oauth.net/cross-app-access/)，从开发人员的角度来看，XAA 也不会造成太大干扰。

Hirsch 解释说：“它将企业中最终用户的授权负担转移到了管理员身上。从构建者的角度来看，它所做的就是在进行 OAuth 握手之前，与[身份提供商](https://oauth.net/cross-app-access/)核对。”

事实证明，Okta 早在 AI 代理甚至大型语言模型 (LLM) 成为行业流行词之前，就开始着手开发 XAA 协议了。当然，它也不限于 AI 代理，但 AI 代理的激增现在已将 XAA 试图解决的问题推到了前沿。

Okta 和其他公司现在正努力推动行业采用 XAA。在内部，Okta 和 Auth0（Okta 的开发平台，使开发人员更容易将身份验证和授权构建到他们的应用程序中）将使用 XAA 来实现细粒度权限。Auth0 将很快在其 API 和 SDK 中支持 XAA，而 Okta 将使其成为其平台核心架构的一部分。

XAA 支持者 Automation Anywhere 的首席产品官 Adi Kuruganti 表示：“随着自主 AI 代理在从财务合规到客户服务等关键任务操作中承担日益复杂的任务，企业需要对代理、模型和工具之间的每一次交互进行全面可见性和治理。跨应用访问提供了一个关键的新标准，用于建立在整个企业中安全扩展这些强大功能所需的信任。”

XAA 正在解决的核心问题非常真实，并且不是 MCP 或 A2A 目前正在解决的问题。然而，与所有新标准一样，尤其是在这个快速发展的 AI 生态系统中，行业最终会达成何种共识仍有待观察。

XAA 拥有足够强大的支持者，很有可能成为该标准，但正如我们所看到的 MCP 等协议，一个全新的协议可能会突然出现并被社区迅速采用，而无需任何行业组织的参与。