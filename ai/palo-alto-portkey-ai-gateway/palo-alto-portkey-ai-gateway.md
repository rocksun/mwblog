<!--
title: Palo Alto Networks 斥资 7 亿美元收购 Portkey，重注 AI 网关安全领域
cover: https://cdn.thenewstack.io/media/2026/05/2346e9a0-getty-images-cemfwj6t27u-unsplash-scaled.jpg
summary: Palo Alto Networks 宣布收购 AI 网关 Portkey 并整合至 Prisma AIRS。此举标志着 AI 网关从开发者的 API 路由工具演变为企业的核心安全检查站，旨在通过深度监控实现 AI 代理的合规治理。
-->

Palo Alto Networks 宣布收购 AI 网关 Portkey 并整合至 Prisma AIRS。此举标志着 AI 网关从开发者的 API 路由工具演变为企业的核心安全检查站，旨在通过深度监控实现 AI 代理的合规治理。

> 译自：[Palo Alto Networks bets $700M-class AI bet on Portkey gateway](https://thenewstack.io/palo-alto-portkey-ai-gateway/)
> 
> 作者：Janakiram MSV

在 LLM 时代的最初三年里，AI 网关一直是开发者头疼的问题。你面对着 10 个模型供应商，每个都有 10 个不同的 SDK 和 10 种身份验证方案。网关将它们统一了起来。

Portkey、LiteLLM、Kong AI Gateway 和 Cloudflare AI Gateway 分别以略有不同的方式解决了这一碎片化挑战。开发者选择其中一个，获得一个兼容 OpenAI 的单一端点，然后继续后续工作。而安全团队当时并不在场。

现在，Palo Alto Networks 搬来了一把椅子坐下了。

上周，Palo Alto Networks 宣布有意[收购](https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-acquire-portkey-secure-rise-ai-agents) [Portkey](https://portkey.ai)，并将其整合到 [Prisma AIRS](https://www.paloaltonetworks.com/prisma/prisma-ai-runtime-security) 中，作为一个统一的控制平面，用于保障企业内部每一笔 AI 交易的安全。虽然交易尚未完成，但战略信号非常明确：位于你的代理（Agent）与它调用的每个模型之间的那一层，不再仅仅是底层管道。它是一个检查站。

> 虽然交易尚未完成，但战略信号非常明确：位于你的代理与它调用的每个模型之间的那一层，不再仅仅是底层管道。它是一个检查站。

想想 AI 网关实际能看到什么。你的代理发送的每一个提示（Prompt）。它收到的每一个模型响应。每一次工具调用，每一次内存读取，每一次 MCP 服务器交互。在你的企业 AI 技术栈中，没有什么比网关层更能完整地描绘出你的代理在做什么。安全行业比大多数开发者更早意识到了这一点。

在 Palo Alto 行动之前，Portkey 已经在为财富 500 强客户每月处理数万亿个 Token。只需三行代码即可实现。支持 3000 种 LLM、MCP 服务器和代理。对于开发者来说，这个故事非常简单。

> Palo Alto 在 Portkey 原有服务基础上增加的是身份识别、身份验证、伪影扫描、自动化红队测试以及运行时安全。

Palo Alto 增加的是身份识别、身份验证、伪影扫描、自动化红队测试以及运行时安全。所有这些都在每一个代理调用经过的节点强制执行。网关变成了你发现代理实际在做什么，而不是你希望它们在做什么的地方。

## 安全行业曾多次改写规则

这并不是安全大厂第一次改写由开发者主导的基础设施类别的规则。Web 应用防火墙（WAF）最初是网络团队的问题。然后，开发者开始将每个 HTTP 请求路由通过它。Cloudflare 将其变成了一个平台。模式是相同的：开发者便利性，然后是可见性，接着是控制权，最后是收购。

让这一时刻变得特殊的是代理。一个单一的代理工作流在执行任务时可能会进行数十次 LLM 调用。每一次调用都会经过网关。在这种体量下，网关不再只是一个代理。它是你的自主系统决定做什么以及为什么这么做的记录日志。对于受监管行业（金融服务、医疗保健、政府）来说，该日志不是可选的，而是审计追踪。

Kong 已经在推动代理网关功能和 A2A 流量治理。Cloudflare 在 2026 年为其 AI 网关扩展了统一计费和边缘缓存功能。[LiteLLM](https://github.com/BerriAI/litellm) 仍然是尚未达到生产规模的团队的开源切入点。

但它们都没有进行安全领域的收购。Palo Alto 刚刚确立了这样一个事实：该领域真正的企业级博弈点在于网关与安全的交汇处，而不是网关与 API 管理的交汇处。

## 我们关于这个故事最可能判断错误的地方是时机

我们关于这个故事最可能判断错误的地方是时机。如果代理进入受监管的企业工作负载所需的时间比预期更长，那么安全层仍将是边缘情况的检查站。但发展轨迹已经确定。

AI 网关曾经是你路由 Token 的地方。而在这次收购之后，它将成为你治理代理的地方。