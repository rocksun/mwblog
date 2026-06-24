<!--
title: DNS能否成为AI智能体身份识别的基础？
cover: https://cdn.thenewstack.io/media/2026/06/2f838e2e-a-c-7iptbg5y99m-unsplash-scaled.jpg
summary: Linux基金会推出代理名称服务（ANS），旨在利用现有的DNS和证书体系为AI智能体提供可验证的身份。该方案旨在通过域名所有权验证解决智能体身份识别与发现问题，虽获业界支持，但仍面临互联网信任机制脆弱及各大科技巨头标准不一的挑战。
-->

Linux基金会推出代理名称服务（ANS），旨在利用现有的DNS和证书体系为AI智能体提供可验证的身份。该方案旨在通过域名所有权验证解决智能体身份识别与发现问题，虽获业界支持，但仍面临互联网信任机制脆弱及各大科技巨头标准不一的挑战。

> 译自：[Can DNS become the basis for AI agent identity?](https://thenewstack.io/can-dns-become-the-basis-for-ai-agent-identity/)
> 
> 作者：Frederic Lardinois

Linux基金会周二宣布有意推出代理名称服务 (ANS)，这是一项开放标准，通过将 AI 智能体与互联网的域名系统 (DNS) 挂钩，为其提供[可验证的身份](https://thenewstack.io/ai-agent-identity-crisis/)。

ANS 背后的理念其实已经存在一段时间了。它始于 [OWASP GenAI Security Project](https://genai.owasp.org/) 于 2025 年 5 月发表的一篇研究论文，由一群应用安全研究人员撰写。其作者包括安全咨询公司 DistributedApps.ai 的首席执行官、被广泛引用的《OWASP Top 10 for LLM Applications》（记录了与 LLM 相关的主要安全风险）合著者 Ken Huang，以及 Cisco 的 AI 安全工程师 Akram Sheriff。

ANS 是对最初构想的改进版本，自发布以来已经历了几次迭代。[2025 年的原始版本](https://arxiv.org/abs/2505.10609)将 ANS 描述为“通用目录”——本质上是一个借用 DNS 命名机制的中央注册表。4 月份在互联网工程任务组 (IETF) 发布的一份[个人草案](https://datatracker.ietf.org/doc/draft-narajala-courtney-ansv2/)是该项目的第二个版本，它更进一步，将每个智能体直接与其运营商已经控制的真实域名绑定。

## 工作原理

该设计本质上复制了网站目前证明其身份的方式。运营商通过 Let’s Encrypt 背后的自动化协议 ACME 来证明其对域名（如 example.com）的控制权，注册机构则向该智能体颁发一对证书。智能体状态的每一次变更，从注册、续期到撤销，都会被写入一个仅限追加的日志中。检查智能体的客户端可以选择其所需的保障级别，从基本的证书检查到咨询日志的进阶验证。

值得注意的是，ANS 系统将身份识别与发现功能分离，并将寻找智能体的工作交给在此基础上构建的其他服务。

## DNS 行业与 AI 智能体

发现功能实际上由 [DNS-AID](https://datatracker.ietf.org/doc/draft-mozleywilliams-dnsop-dnsaid/) 处理，这是基金会于 5 月 27 日接纳的另一项发现标准。它允许智能体将其端点发布为 DNS 记录，以便其他智能体能够找到它们。DNS-AID 最初由 Infoblox 构建，同样参与 ANS 的 GoDaddy 也是其支持者之一。

不过，基于 DNS 的智能体身份和发现项目并不局限于这两个 Linux 基金会项目。包括这两个在内，目前至少有四个类似的提案。例如，来自注册商 Identity Digital 的持久身份方案 DNSid，以及源自开发者社区的极简发现草案 AID。

现就职于 OWASP 的 ANS 合著者 Vineeth Sai Narajala 在公告中表示：“我们不需要重新发明轮子，我们需要将互联网的基础信任扩展到新一代自主技术。”

不重新发明轮子也意味着基于现有的注册商和证书颁发机构，以及他们建立的信任层级——尽管安全研究人员长期以来一直认为该层级[十分脆弱](https://meetcyber.net/dns-is-still-one-of-the-internets-most-fragile-control-planes-a2b89a6530ab)。

许多智能体身份和发现解决方案来自域名行业也就不足为奇了。毕竟，GoDaddy 负责注册域名，Identity Digital 运营顶级域名，而支持 ANS 的 Infoblox 则销售 DNS 基础设施。对他们所有人来说，链接 DNS 的智能体身份和发现方案扩展了他们现有的（有利可图的）业务。

## A2A 等其他方案如何？

正如经常发生的那样，Linux 基金会同时也托管了[多个替代](https://thenewstack.io/agentic-ai-foundation-launch/)系统。例如，Google 的 [A2A 协议](https://thenewstack.io/google-donates-the-agent2agent-protocol-to-the-linux-foundation/)为智能体提供了一张签名“智能体卡片”，它们可以将其发布在已知的网址上，其路线图中还包括一个智能体注册表。Cisco 的 [AGNTCY](https://thenewstack.io/cisco-donates-the-agntcy-project-to-the-linux-foundation/) 提供了一个智能体目录及其自己的加密身份服务。在基金会之外，Microsoft 的 Entra Agent ID 和 [Okta for AI Agents](https://thenewstack.io/okta-wants-to-secure-your-ai-agents-too/) 自春天以来均已普遍可用，它们将智能体视为企业目录中管理的身份，通过短期令牌将每个操作追溯到授权人员。

尽管 Cisco 同时支持 ANS 和 AGNTCY，但名单中缺失了一些重要名字，包括 Google、Anthropic、Microsoft 和 Amazon 等主要参与者。鉴于它们在智能体生态系统中的巨大作用，看看它们是会加入这项努力，还是决定制定自己的标准（此处插入必不可少的 xkcd 漫画 [链接](https://xkcd.com/927/)），将是一件很有趣的事情。