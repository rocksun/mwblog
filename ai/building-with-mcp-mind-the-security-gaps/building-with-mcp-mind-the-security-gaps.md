
<!--
title: 使用MCP构建？注意安全漏洞
cover: https://cdn.thenewstack.io/media/2025/04/74f43954-mind-the-gap-mcp-security-2.jpg
summary: 爆！Anthropic力推的AI神器MCP爆出安全漏洞！😱 缺乏身份验证，易受工具中毒攻击，WhatsApp聊天记录恐泄露！速自查`MCP server`，启用身份验证，小心`OWASP Top 10 API Security Risks`，用`mcp-scan`排雷！
-->

爆！Anthropic力推的AI神器MCP爆出安全漏洞！😱 缺乏身份验证，易受工具中毒攻击，WhatsApp聊天记录恐泄露！速自查`MCP server`，启用身份验证，小心`OWASP Top 10 API Security Risks`，用`mcp-scan`排雷！

> 译自：[Building With MCP? Mind the Security Gaps](https://thenewstack.io/building-with-mcp-mind-the-security-gaps/)
> 
> 作者：Bill Doerrfeld

固有的安全缺陷正在引发人们对基于 [模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/) 构建的 AI 系统的安全性的质疑。

[MCP](https://modelcontextprotocol.io/introduction) 由 [Anthropic](https://www.anthropic.com/company) 开发，是一个开源规范，用于将基于大型语言模型的 AI 代理与外部数据源（称为 MCP 服务器）连接起来。

作为 [代理到 API 通信](https://thenewstack.io/its-time-to-start-preparing-apis-for-the-ai-agent-era/) 的第一个提议的行业标准，近几个月来，人们对 MCP 的兴趣激增，导致 MCP 服务器数量激增。

最近几周，开发人员发出警报，称 MCP 缺乏默认身份验证，并且开箱即用并不安全——有些人说它是一个 [安全噩梦](https://equixly.com/blog/2025/03/29/mcp-server-new-security-nightmare/)。

[Invariant Labs 的最新研究](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) 表明，MCP 服务器容易受到工具中毒攻击，在这种攻击中，不受信任的服务器会将隐藏的指令嵌入到工具描述中。

根据 Invariant Labs 的说法，Anthropic、OpenAI、Cursor、Zapier 和其他 MCP 客户端容易受到此类攻击，Invariant Labs 演示了如何 [泄露 WhatsApp 聊天记录](https://invariantlabs.ai/blog/whatsapp-mcp-exploited)。

Invariant Labs 的联合创始人兼首席技术官 [Luca Beurer-Kellner](https://www.linkedin.com/in/luca-beurer-kellner-0b345616a) 告诉 The New Stack，“MCP 本身通常不存在安全问题，因为根本的漏洞实际上是模型的问题。”

他补充说：“与此同时，MCP 的采用正在推动越来越多的用户将 LLM 系统连接到敏感数据源和工具，这使得 AI 和尤其是代理 AI 的安全挑战变得更加重要。”

## MCP 安全问题“非常真实”

MCP 被描述为“[AI 的 USB-C 端口](https://docs.anthropic.com/en/docs/agents-and-tools/mcp)”。根据 [MCP.so](https://mcp.so/servers) 的数据，已有超过 8,000 台 MCP 服务器在运行。

OpenAI 的 [Sam Altman](https://thenewstack.io/what-openai-ceo-sam-altman-really-expects-in-ais-future/) 最近 [承诺采用 MCP](https://techcrunch.com/2025/03/26/openai-adopts-rival-anthropics-standard-for-connecting-ai-models-to-data/) 用于他们的平台。像 [Digidop](https://www.digidop.com/blog/mcp-ai-revolution) 这样的早期采用者报告说，开发时间和复杂性降低了 55%。

然而，快速的进展可能会忽略安全风险。API 安全公司 Equixly 的 [最新研究](https://equixly.com/blog/2025/03/29/mcp-server-new-security-nightmare/) 发现，43% 的 MCP 服务器包含命令注入漏洞。

Layered System 的 API 战略师 [Kevin Swiber](https://www.linkedin.com/in/kevinswiber/) [在 LinkedIn 上分享](https://www.linkedin.com/posts/kevinswiber_api-mcp-plugin-activity-7309598242646700032-zQHh?utm_source=share&utm_medium=member_desktop&rcm=ACoAAA-8zTABlsmtYe-zC-Uf5z3oD5nm6qXDVVo) 说：“安全问题非常真实”。

研究人员已经确定了与 MCP 系统相关的几个关键风险：

- 工具中毒。
- Rug pulls（其中受信任的服务器在获得客户端批准后更改工具，变为恶意）。
- 工具阴影（一个服务器改变另一个服务器的行为）。
- 远程命令执行（当攻击者运行系统命令时）。

缓解策略包括：

- 扫描 MCP 服务器是否存在漏洞。
- 实施身份验证。
- 使用受信任的身份提供商。
- 将最小权限范围应用于工具访问。

## 深入研究 MCP 漏洞

工具中毒攻击是一种间接提示注入，可用于劫持基于 MCP 的系统中的行为。这可能会暴露敏感机密，例如 SSH 密钥，或通过其他连接的工具触发未经授权的操作。

这种风险源于一个核心架构问题：不受信任的 MCP 服务器可以将隐藏的指令嵌入到工具描述中，AI 模型将处理这些指令，但用户通常看不到。

Invariant Labs 的报告称：“根本问题在于，代理系统暴露于所有连接的服务器及其工具描述，这使得被 rug-pulled 或恶意服务器可以注入代理关于其他服务器的行为。”

Swiber 告诉 The New Stack，“恶意行为者可以伪装成调度代理，而实际上它所做的只是窃取私人通信以发起复杂的网络钓鱼攻击。风险范围从基本的隐私问题到高级数据泄露。”
Invariant Labs 发现，恶意软件包可以在安装后被修改，从而包含不可信的代码，这是一种已知的供应链风险。

Anthropic 的一位发言人告诉 The New Stack：“MCP 服务器与任何第三方软件包一样，都存在相同的供应链风险。” “我们建议企业在使用第三方软件包时，继续遵循安全最佳实践。”

一位 DevOps 研究人员[也强调了](https://elenacross7.medium.com/%EF%B8%8F-the-s-in-mcp-stands-for-security-91407b33ed6b) MCP 系统中跨服务器工具影子和命令注入漏洞。

## 小心本地 MCP 服务器

MCP 服务器通常分为两类：远程和本地。最紧迫的问题围绕本地 MCP 服务器展开。

Equixly 的联合创始人兼 CTO [Alessio Dalla Piazza](https://www.linkedin.com/in/alessiodallapiazza) 告诉 The New Stack：“MCP 服务器在设计上存在一些安全挑战，开发人员必须主动解决这些挑战，以确保稳健和安全的通信。”

Swiber 指出，远程 MCP 服务器在授权和传输协议方面仍在不断发展。因此，开发人员越来越多地转向本地 MCP 服务器，这些服务器在当前规范中定义得更清楚。

缺点是本地 MCP 服务器构成更高的安全风险，因为它们通常从 npm 或 PyPI 等公共注册表中提取未经审查的第三方软件包，从而大大增加了引入恶意代码的可能性。

Swiber 补充说：“本地 MCP 服务器在用户的操作系统上运行，通常具有与用户相同的权限。” “这为恶意行为者打开了窗口。”

因此，请小心本地 MCP 服务器。[Erik Wilde](https://www.linkedin.com/in/erikwilde) 是 INNOQ 的首席顾问，他[在 LinkedIn 上分享道](https://www.linkedin.com/posts/erikwilde_api-mcp-plugin-activity-7309515359361945601-fmey?utm_source=share&utm_medium=member_desktop&rcm=ACoAAA-8zTABlsmtYe-zC-Uf5z3oD5nm6qXDVVo)：“您可能不应该盲目下载和使用 MCP 服务器，因为它们的行为可能会危及您的数据源。”

Piazza 补充说，开发人员还应确保不会无意中访问不安全的功能。这包括读取或写入未受保护的文件、执行系统命令或获取远程资源的能力。

如果 MCP 服务器未正确验证或显示工具描述，则可能会受到威胁。Invariant 的 Beurer-Kellner 建议使用 [mcp-scan](https://github.com/invariantlabs-ai/mcp-scan) 等工具来验证正在使用的服务器是否安全。

Anthropic 的一位发言人说：“我们目前正在与社区合作，为 MCP 服务器建立标准化注册表。” “这些注册表将提供有关服务器实现的基本元数据，使用户能够就支持和集成哪些服务器做出明智的决定。”

## 保护 MCP：身份验证、授权、抽象

当涉及到 LLM 工具安全性时，工具中毒只是冰山一角。

Beurer-Kellner 说：“许多流行的代理系统缺乏适当的防护措施和行为保证，这使得将它们连接到敏感工具和数据非常危险。” “即使是现在最好的 LLM 仍然会受到注入的影响，并且很容易被劫持。”

实施适当的身份验证非常重要。展望未来，Piazza 希望 MCP 能够包含内置的安全措施，例如默认情况下的标准化身份验证和沙盒。

他说：“在此之前，开发人员需要注意，不仅要注意 LLM 的预期用途，还要注意潜在的恶意交互，确保他们的 MCP 实现是安全的、经过身份验证的和经过验证的。”

对于远程暴露的 MCP 服务器，它们的安全性实际上取决于开发人员已经实施的底层 API 最佳实践。

Swiber 敦促团队构建与后端 API 接口的 MCP 服务器，以评估 [OWASP Top 10 API Security Risks](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)。他们补充说，适当的授权、设置小范围、速率限制和安全令牌存储是关键活动。

Piazza 说，API 的安全措施应该提供一些保护：“如果底层 API 已经采取了安全措施，那么通过 MCP 添加另一个抽象层的暴露不应带来额外的风险。”

然而，[Matt DeBergalis](https://www.linkedin.com/in/debergalis/) 是 [Apollo GraphQL](https://www.apollographql.com/) 的 CTO 兼联合创始人，他认为这种抽象层必须是经过深思熟虑的。DeBergalist 告诉 The New Stack：“AI 代理不能直接连接到生产 API——这是一个安全和治理的噩梦。”

他补充说：“需要有一个抽象层来执行策略、处理身份验证、管理速率限制以及将 AI 系统的快速迭代与现有服务分离。”
最后，还有身份和访问管理的问题。按照 MCP 的设计，它给用户带来了很大的实施负担。

与其要求每个 MCP 自己处理身份验证和授权，不如像 Okta 的身份标准主管 Aaron Parecki [在一篇博文中](https://aaronparecki.com/2025/04/03/15/oauth-for-model-context-protocol) 建议的那样，将 MCP 服务器[视为 OAuth 资源服务器](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/205)，并将诸如令牌颁发之类的难题委派给身份提供商。

Anthropic 的一位发言人表示：“MCP 身份验证规范仍在不断完善中。我们正在积极改进它，以更好地符合企业安全要求和现有身份验证系统。”

## 一点异议

在急于拥抱 MCP 的同时，公司不应放弃其为提供可靠 API 而采取的常用程序。

API Evangelist [Kin Lane](https://www.linkedin.com/in/kinlane/) 告诉 The New Stack：“在过去的十年中，企业出于许多商业原因，一直在认真地使用 HTTP API 来定义和公开其数据库、文件和其他系统中存在的数字资源和功能，以供多个内部、合作伙伴和公共应用程序使用。”

“您会在当前围绕 MCP 的辩论中找不到这些商业原因，因为这些原因正在被规避，以便获取您的数据来训练他们的模型，同时说服您他们会将所有点连接起来。”

虽然 MCP 似乎已经开始起步，但对于任何以闪电般的速度炒作的技术来说，一点异议可能是有益的。

## 参与塑造 MCP 的邀请

[Agentic AI](https://thenewstack.io/ai-agents/)，以及 MCP，都处于早期阶段。随着它的更多使用，新的威胁向量可能会出现。
Beurer-Kellner 说：“Agentic 安全防护实际上是一个非常难解决的问题”，并补充说“代理系统的复杂性即将爆发，并将不断引发新的安全威胁。”

Anthropic 希望该协议随着时间的推移而改进，并列举了即将进行的改进，例如 MCP 服务器的标准化注册表、更简单的版本控制和身份验证附加组件。该公司还邀请社区参与。

正如 Anthropic 的一位发言人告诉 The New Stack 的那样：“我们继续邀请社区积极参与塑造 MCP。我们鼓励人们关注 GitHub 上的讨论——您可以贡献想法、报告问题并提出对规范的更改。”

Swiber 一方面感到好奇，另一方面又很谨慎：“这是一个令人兴奋的领域，我期待看到这些标准随着企业级安全性的成熟。”

然而，他们承认，“这项技术仍处于早期阶段。”