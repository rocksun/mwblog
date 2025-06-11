<!--
title: 部署安全的企业级Agentic AI：MCP+Agent2Agent
cover: https://cdn.thenewstack.io/media/2025/06/ad46897a-teodor-skrebnev-x9qktlqucco-unsplash-1-scaled.jpg
summary: 企业级 Agentic AI 安全部署：利用 MCP 扩展 LLM 应用面临 Prompt Injection 等风险。Agent2Agent (A2A) 通过代理模式，实现身份验证和授权分离，有效防御跨服务器泄露。结合输入/输出检测，构建安全可扩展的云原生 AI 架构，保障企业数据安全。
-->

企业级 Agentic AI 安全部署：利用 MCP 扩展 LLM 应用面临 Prompt Injection 等风险。Agent2Agent (A2A) 通过代理模式，实现身份验证和授权分离，有效防御跨服务器泄露。结合输入/输出检测，构建安全可扩展的云原生 AI 架构，保障企业数据安全。

> 译自：[Deploying A Secure Enterprise Agentic AI: MCP + Agent2Agent](https://thenewstack.io/deploying-a-secure-enterprise-agentic-ai-mcp-agent2agent/)
> 
> 作者：Rikki Singh

LLM、AI 代理及其不断发展的工具生态系统（如 [Model Context Protocol (MCP)](https://www.anthropic.com/news/model-context-protocol)）的引入，为各种新的用例打开了大门。尽管如此，它们也给生产中的安全带来了独特的挑战，让我们对如何为用户创建安全可靠的应用程序留下了许多未解之谜。

当我们的团队开始探索 MCP 及其应用时，我遇到了一些这样的问题。我们问自己这样的问题：“MCP 规范没有明确说明我们应该如何进行身份验证……那么我们应该如何考虑它？”我们想知道提供 API 密钥的最佳方式是什么，未来的远程服务器会是什么样子，以及不同的客户端及其 LLM 将如何解释和利用我们通过服务器提供的工具。

本文探讨了使用 LLM 固有的主要风险，我们如何看待随着 MCP 等新标准的引入而发生的变化，以及我们如何考虑使用更新的标准（如 [Agent2Agent (A2A)](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)）构建安全且可扩展的 agentic 架构。

## 我们是如何走到这一步的？

在安全评估中，我们经常考虑两个概念：**攻击面**，即系统中容易受到攻击者利用的地方的数量；以及 **爆炸半径**，即一次成功的攻击可能对系统产生的影响。LLM 最近因其灵活性和自动化世界的承诺而迅速普及，但当添加到我们的应用程序中时，它们也会带来易受攻击的攻击面。基本的聊天机器人通过接受和推理用户提供的不可信自然语言来扩大我们的攻击面。由于 LLM 的非确定性性质，输出缺乏可预测性，并且重现问题以进行诊断的能力有限。因此，我们也无法完全确定其答案可能造成的潜在危害，从而增加了我们的爆炸半径。作为构建我们自己的 agentic 平台的早期采用者，该团队面临着各种新的安全挑战，其中最著名的是 [Prompt Injections](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) 和 [Jailbreaks](https://www.bugcrowd.com/blog/ai-deep-dive-llm-jailbreaking/)，这两者都是由提供给 LLM 的不可信内容促成的，旨在导致意外的操作或响应。

然后是代理。Agentic AI 通过引入与 API 和数据的更多特权交互来提高复杂性和风险因素。现在，我们可以引入更智能的系统，这些系统使用工具和知识来源。代理与 API 交互，连接到数据源（有些来自公共互联网），甚至可以与其他[代理通信或由另一个 AI](https://thenewstack.io/agentic-ai-for-enterprises-4-key-benefits-driving-innovation/) 代理主管管理。但是，如果您扩展我们的攻击面和爆炸半径的逻辑，您可以看到随着我们在组件之间传递更多不可信内容，问题是如何复合的。[间接提示注入](https://cetas.turing.ac.uk/publications/indirect-prompt-injection-generative-ais-greatest-security-flaw)可以通过为 LLM 知识抓取的网站传递，等待激活的合适用户查询。工具域的 DNS 记录可能会[欺骗主机](https://github.blog/security/application-security/localhost-dangers-cors-and-dns-rebinding/)访问其自身本地网络上的服务。不幸的目标可能会遇到数据泄露或远程代码执行。

并不是说我们以前没有见过类似漏洞，但架构格局的变化起初可能会让人感到困惑，需要新的安全思维方式。为了使更安全的 agentic 流的愿景成为可能，我们有 MCP 和 Agent2Agent 框架。虽然 MCP 侧重于创建对工具的访问，但 A2A 侧重于代理之间的互操作性。

![](https://cdn.thenewstack.io/media/2025/06/19c98aad-image2-1024x546.png)

## 我们能做些什么？

下面，我们重点介绍了我们认为通过我们与 MCP 的合作很重要的三个关键漏洞，以及如何解决这些漏洞（详细信息如下）：

1. **跨服务器泄露和敏感数据暴露：** MCP 的优势之一在于，您的应用程序/代理/客户端可以收集完成请求所需的一切，可能来自多个 MCP 服务器，并将它们传递给 LLM（单个或多个供应商）进行处理。这隐含地存在将一个服务器中的资源暴露给另一个服务器的风险。我们建议希望将其工具暴露给这些客户端的企业，利用代理来执行此操作，而不是直接使用 MCP 服务器，以便他们可以保持控制并保护自己免受数据暴露。
2. **身份验证和授权：** MCP 缺乏对用户进行通用身份验证的机制，例如 OIDC 或 SSO，并且可能绕过跨资源的授权要求（又名：[The Confused Deputy](https://en.wikipedia.org/wiki/Confused_deputy_problem)）。因此，我们建议分离身份验证和授权层，以便您可以使用现有的控制平面基础设施来识别用户和代理，确保他们始终拥有对其所操作数据的适当凭据。A2A 在这方面提供了便利，因为实现该协议的客户端代理可以通过代理卡发现其他代理的身份验证方案。这使企业能够在探索维护和[管理代理身份](https://thenewstack.io/ai-agents-are-redefining-the-future-of-identity-and-access-management/)的替代方法时取得进展。
3. **Prompt 注入和越狱：** MCP 客户端及其 LLM 容易受到来自其他连接的 MCP 服务器的 prompt 注入和越狱攻击。对于客户端和服务器，了解您的工具和资源是值得信赖的至关重要。在 A2A 服务器层采用检测策略以降低这些攻击成功的可能性会非常有效。A2A 不是这里唯一的架构选择，任何免受直接输入和输出影响的代理模式都将为实施检测策略提供空间。

正如您阅读了以上内容，您可能已经清楚地意识到，本质上，与必须专门利用 MCP 服务器或 A2A 相比，代理架构的网格可以解决许多这些挑战。

我们将在下面进一步阐述这些风险以及我们为那些希望通过示例了解它们的人提出的建议。我们在本次探索中的指导原则是确保我们能够为我们的客户构建[安全系统](https://thenewstack.io/customer-facing-incidents-on-the-rise-it-leaders-say/)，而不会使架构过于复杂而无法扩展。随着企业希望采用这些框架来加速他们自己的 AI 创新，我们希望我们能够共同做到这一点，而不会危及我们用户的安全。

### 1. 跨服务器泄露和敏感数据暴露

第一次使用 MCP 时，它会让人觉得很神奇。看着你的代理弄清楚如何与 API 交互并使用它来完成任务非常酷，它确实给人一种未来的感觉。我们应该扩展我们的代理并让它访问更多的服务器吗？嗯，不幸的是，一个服务器存在与另一个服务器[交互](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)的风险。这里的问题是代理可以将来自每个服务器的组件混合在一起，[允许它们潜在地查看和访问](https://thenewstack.io/10-things-to-consider-when-allowing-access-to-production/)它们不应该访问的内容。这种跨服务器访问也[扩大了我们的攻击面和我们的爆炸半径](https://thenewstack.io/how-supply-chain-attackers-maximize-their-blast-radius/)。

![](https://cdn.thenewstack.io/media/2025/06/db60787c-image3-1024x484.png)

*多个 MCP 服务器会产生潜在的危险数据特权访问混合。*

A2A 通过在您的应用程序和连接的 MCP 服务器之间引入一个抽象层来帮助解决此问题。它引入了一个代理接口，该接口公开任务，通过隐藏其自身对 MCP 服务器的访问权限来充当受信任的委托，从而保护您免受将特权数据暴露给应用程序中其他连接的服务器的风险。这并不能完全消除风险，因为从理论上讲，您总是可能遇到隐藏在代理后面的恶意活动，但它有助于防止来自其他 MCP 服务器的窃听和意外的资源使用。

![](https://cdn.thenewstack.io/media/2025/06/4d66c8b8-image1-1024x852.png)

*A2A 代理委托对 MCP 资源的访问，从而限制了对其他代理和服务器的直接暴露。*

### 2. 身份验证和授权

[MCP 服务器目前主要在本地运行](https://thenewstack.io/how-to-access-local-mcp-servers-through-a-secure-tunnel/)，但随着时间的推移，它们将变为远程运行，以便您的代理可以通过标准 HTTPS 连接到它。MCP 目前建议使用 OAuth 进行授权，但缺乏企业常用的身份验证方式，例如 OpenID Connect、Single Sign-On 或 SAML。A2A 允许进行这种缺失的身份验证，并支持灵活的授权架构，以确保我们的用户和代理以可信的方式行事。

A2A 服务器通过标准交换提供身份验证和授权选项，并期望客户端和服务器自行协商。代理卡提供了访问所需的身份验证类型字段，授权字段计划添加到规范中。借助 A2A，我们无需对当前的处理方式进行太多更改，即可扩展 MCP 提供的选项。也许您的公司使用 OpenID 进行员工登录，并且您希望确保他们在允许任何代理代表他们执行授权操作之前，使用此系统进行身份验证。MCP 本身目前无法在这方面为您提供太多帮助。

关于身份，我们应该进行的一项具体补充是将代理身份与用户身份分开。用户应该使用您的系统进行身份验证，但代表该用户的代理也应该被唯一标识以进行授权。用户及其授权代理之间的授权权限可能存在差异。A2A 服务器应验证每个工具和资源授权请求的任务要求，确保通过权限滥用无法进行未经授权的访问，并且代理及其代表的用户都具有正确的权限范围。

[抽象](https://developers.cloudflare.com/agents/model-context-protocol/authorization/#3-bring-your-own-oauth-provider) 已经在构建并作为服务提供，以规避 MCP 的某些限制，但它们仍处于实验阶段。更直接的路径可能是您已经使用的标准流程。

### 3. Prompt 注入和越狱

在讨论 LLM 的安全性时，我们不可避免地会遇到 [prompt 注入](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) 和越狱。它们是代理应用程序中最常被提及的两个漏洞，并且经常参与促进其他攻击。LLM 容易受到影响并且相对容易被欺骗。除非受到可以检查不受信任的输入和输出的系统的保护，否则应用程序存在通过 LLM 解释的更改指令来执行意外操作的风险。

由于 prompt 注入非常普遍，因此隔离和检查 LLM 的任何不受信任的输入至关重要。与具有可预测的工具和资源的定制代理相比，使用 MCP，我们的攻击面和爆炸半径会大大增加。我们无法真正信任多个连接的 MCP 服务器不会更新一个看起来安全的工具以稍后包含注入（您不知情的情况下），或者它们不会提供包含尝试跨服务器访问的 prompt 注入指令的资源。

可以通过扫描工具、运行时验证以及在将任何不受信任的输入发送到 LLM 之前实施注入检测来缓解此问题。

但是，借助 A2A，我们的代理服务器可以充当抵御注入的第一道也是最后一道防线。在这种架构中，我们与外界的接口限制了来自其他服务器的注入所带来的攻击面。我们可以在代理服务器的入口点或请求流程中任何有意义的地方采用标准的输入和输出防护措施。我们还可以保护我们的用户免受其他服务器的侵害，因为 A2A 服务器控制代理将用于完成其任务的工具和资源。