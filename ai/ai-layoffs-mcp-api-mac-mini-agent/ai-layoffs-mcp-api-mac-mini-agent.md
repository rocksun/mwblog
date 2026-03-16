<!--
title: AI裁员潮来袭，MCP与API之争，以及Mac Mini驱动AI代理的崛起
cover: https://cdn.thenewstack.io/media/2026/03/e3792f2e-img_2202.jpg
summary: 本周AI行业动态：科技巨头因AI裁员加剧；AI代理连接方案MCP与API之争，API受青睐；Mac Mini成AI代理新主机；氛围编程获巨额融资，但存安全隐患；Claude用户激增，价值观成竞争优势。
-->

本周AI行业动态：科技巨头因AI裁员加剧；AI代理连接方案MCP与API之争，API受青睐；Mac Mini成AI代理新主机；氛围编程获巨额融资，但存安全隐患；Claude用户激增，价值观成竞争优势。

> 译自：[AI layoffs are here, the MCP vs API debate, and the rise of the Mac Mini-powered Agent](https://thenewstack.io/ai-layoffs-mcp-api-mac-mini-agent/)
> 
> 作者：Matthew Burns

我是 Matt Burns，Insight Media Group 的内容主管。每周，我都会汇总最重要的 AI 发展，并解释它们对于那些真正将这项技术付诸实践的人意味着什么。论点很简单：学会使用 AI 的员工将定义他们行业的下一个时代。这份时事通讯旨在帮助你成为其中之一。

---

**本周：** 工作岗位正在被人工智能取代，公司不再找借口。MCP 工具链已面临反弹，一些人呼吁用 API 取代它。Mac Mini 正在成为托管 AI 代理的默认选择。Replit 和其他氛围编程者获得了大笔融资。而且 Claude 每天新增一百万用户。

## 人工智能正在导致裁员（显而易见）

公司不再躲在空洞的借口背后。[Atlassian 本周裁员 1,600 人](https://www.cnbc.com/2026/03/11/atlassian-slashes-10percent-of-workforce-to-self-fund-investments-in-ai.html)——占其员工总数的 10%——并将原因归咎于 AI，称裁员将“自筹资金进一步投资 AI 和企业销售”。这本质上是一种置换：裁员，AI 入驻。Atlassian 的首席技术官将于 3 月底卸任。

Atlassian 发布这一消息的几周前，[Block 首席执行官 Jack Dorsey 解雇了 4,000 名员工](https://x.com/jack/status/2027129697092731343)，这几乎是当时其 10,000 名员工的一半。Dorsey 表示，裁员是由 AI 自动化驱动的。

*路透社* [今晨报道](https://www.reuters.com/business/world-at-work/meta-planning-sweeping-layoffs-ai-costs-mount-2026-03-14/?utm_campaign=svc-beehiiv&utm_medium=referral&utm_source=newsletter.strictlyvc.com) 称 Meta 计划裁员 20%，因为它预计 AI 将创建更小的团队。

他们并非个例。[*彭博社*报道称 Oracle](https://www.bloomberg.com/news/articles/2026/03/05/oracle-layoffs-to-impact-thousands-in-ai-cash-crunch) 计划裁减数千个工作岗位，以应对 AI 数据中心大规模扩张带来的资金紧张，[一些估算](https://qz.com/ai-layoffs-oracle-data-centers-costs) 甚至将实际数字推高至 30,000 人。Amazon [1 月份宣布的 16,000 人裁员](https://www.cnbc.com/2026/01/28/amazon-layoffs-anti-bureaucracy-ai.html) 仅仅是“第一阶段”，[内部文件指出](https://americanbazaaronline.com/2026/03/12/after-16000-layoffs-amazon-may-cut-14000-more-jobs-in-second-phase-476695/) 第二季度还将有 14,000 人被裁。 [仅 3 月份全球科技行业就裁员 45,000 人](https://technode.global/2026/03/09/2026-tech-layoffs-reach-45000-in-march-more-than-9200-due-to-ai-and-automation-rationalfx/)，其中超过 9,200 人明确归因于 AI 和自动化。科技员工信心[创历史新低](http://v)，不到一半的 IT 员工对未来六个月持积极看法。

上周，Anthropic [指出](https://thenewstack.io/openai-gpt-5-4-ai-jobs-report-anthropic-dow-supply-chain-risk/) 科技是风险敞口最大的行业。这似乎是正确的。

裁员在科技行业并非新鲜事。改变的是裁员理由。公司不再引用宏观经济逆风。他们直接将 AI 指为裁员的原因和节余资金的去向。

## MCP 与 API 之争

你刚刚学习的 AI 技术栈可能已经过时了。模型上下文协议 (Model Context Protocol, MCP) 在 2025 年曾被认为是连接 AI 代理到外部世界的标准，而本周，怀疑者们正在质疑其实用性。

Perplexity 的联合创始人兼首席技术官 Denis Yarats 在内部表示，[他们正在放弃 MCP](https://x.com/morganlinton/status/2031795683897077965) 并回归 API 和 CLI。这一时机恰逢 [Perplexity 推出一个全栈、模型无关的 API 平台](https://thenewstack.io/perplexity-agent-api/)，该平台将你的模型提供商、搜索层和嵌入整合在一个包中。该公司的立场很明确：API 是基础设施，而不是 MCP 服务器。

Y Combinator 总裁 Garry Tan 甚至更直接地表示，“[MCP 说实话很糟糕](https://x.com/garrytan/status/2031910564344262988)”，他列举了上下文窗口膨胀、笨拙的认证以及需要频繁开关服务器等问题。他对 Claude 基于 MCP 的浏览器集成感到非常沮丧，以至于他氛围编程了一个 CLI 包装器，结果发现 Vercel 已经构建了一个。

*The New Stack* 深入报道了这种架构上的紧张关系。他们对[技能 vs. MCP](https://thenewstack.io/skills-vs-mcp-agent-architecture/) 的分析提出了一个双层模型的案例：如果知识是永恒的，它首先进入 markdown 技能文件；如果它需要实时连接，它通过 MCP。例如，一个 GitHub MCP 服务器消耗了大约 50,000 个上下文 token 来教代理如何与 GitHub 交互，而一个 [SKILL.md](http://skill.md) 文件在大约 200 个 token 中实现了相同的效果。这是一个 250 倍的差异。Microsoft 的 .NET Skills Executor 刚刚发布几周，就已经能协调在不同层调用 MCP 工具的技能文件。

这一切并不意味着 MCP 已死。但“MCP 包罗万象”的时代似乎在开始之前就已经结束了。业界正试图变得更智能：为任务使用最轻的工具，并在需要时才使用重量级协议。越来越清楚的是，AI 开发者必须保持敏捷并及时了解工具和最佳实践。

## Mac Mini AI 代理

AI 代理现在开始拥有自己的机器，而 Mac Mini 正在迅速成为始终在线 AI 的默认主机。

Perplexity 本周预告了[“个人电脑”](https://x.com/perplexity_ai/status/2031790180521427166)——一个始终在线的本地 AI 代理，运行在 Mac Mini 上，24/7 跨你的文件、应用程序和会话工作。这可能是普通消费者能获得的最佳 OpenClaw 类产品。与此同时，[Moonshot 推出了一款产品](https://x.com/ojaskandy/status/2031801456718987765)，它通过修改 macOS 为 AI 代理创建一个单独的用户账户——两个用户，一台 Mac，并排工作。

这正发生在硅谷 AI 泡沫之外。在中国，*MIT Technology Review* 报道了 OpenClaw 的淘金热。一位在北京的软件工程师在 1 月份开始尝试 OpenClaw，现在经营着一家拥有 100 多名员工和 7,000 份安装订单的企业。相关活动吸引了 1,000 多名参与者。腾讯举办了公共活动，提供免费的 OpenClaw 安装支持。中国网络安全监管机构[于 3 月 10 日发布警告](https://www.technologyreview.com/2026/03/11/1134179/china-openclaw-gold-rush/)，指出了安全风险，这说明设备上的代理程序在那里已经变得多么主流了。

这种模式是显而易见的：AI 代理正在从你的浏览器转移到它们自己的桌面上。它们正在运行后台任务、监控文件并执行跨会话持久存在的工作流。问题不在于 AI 代理是否会成为你的同事——而在于当它们成为你的同事时，你是否知道如何管理它们。

## 氛围编程市值突破 90 亿美元

“学习编程”是过去十年的职业建议。新版本是：学会描述你想要构建什么。[Replit 在 D 轮融资中筹集了 4 亿美元](https://techcrunch.com/2026/03/11/replit-snags-9b-valuation-6-months-after-hitting-3b/)，估值达到 90 亿美元，在六个月内估值翻了三倍。Replit 在融资的同时推出了 Agent 4，公司预计到年底将实现 10 亿美元的年化收入。目前有 5,000 万用户在该平台上进行构建。

工具层也在快速成熟。[Cursor 推出了自动化功能](https://thenewstack.io/cursor-agents-developer-workflows/)，这些始终在线的代理可以由代码库更改、Slack 消息或计时器触发——将 IDE 变成了更接近于自主工程队友的东西。Replit 和 Cursor 共同定义了相同转变的两种不同风味：Replit 作为任何人都可以通过描述其需求来构建软件的平台，而 Cursor 则是经验丰富的工程师让代理处理繁琐任务的工具。不同的入口点，相同的目的地。

与此同时，[Crafting 获得 550 万美元种子轮融资后推出](https://thenewstack.io/crafting-ai-agents-platform/)，旨在为企业编码代理提供类似生产环境的测试环境，而 [TanStack Start 将自身定位](https://thenewstack.io/tanstack-start-vibe-coding/) 为专门为氛围编程者构建的全栈框架。

但氛围编程的警示故事也正在浮出水面。在多次停机被追溯到 AI 辅助的代码更改后，Amazon 举行了一次[紧急工程会议](https://thenewstack.io/amazon-ai-assisted-errors/)。该公司现在已经实施了为期 90 天的“代码安全重置”，要求高级工程师批准 AI 生成的部署。讽刺的是：Amazon 裁掉了数千名工程师，然后发现取代他们工作的 AI 代码需要工程师来审查。

在 *Towards Data Science* 上，[Reya Vir 探讨了同样的紧张关系](https://towardsdatascience.com/the-reality-of-vibe-coding-ai-agents-and-the-security-debt-crisis/)，并警告了日益增长的安全债务危机。氛围编程不能替代工程判断。如果说有什么不同的话，氛围编程放大了工程判断的必要性。如果你理解什么是好的代码，代理会让你大大加快速度。如果你不理解，代理会让你变得更加危险。

## Claude 日增百万用户时刻

Claude [每天新增百万用户](https://x.com/mikeyk/status/2029662454079512598?s=20)，这一趋势似乎始于 3 月初。这比 2026 年初增长了四倍。Claude 在 20 多个国家取代 ChatGPT 成为 Apple App Store 中排名第一的免费应用程序——这是自 ChatGPT 推出以来任何 AI 应用程序首次做到这一点。目前，Anthropic 正在构建的不再仅仅是一个聊天机器人，而是一个涵盖浏览器、桌面和终端的全方位生产力平台，包括面向开发者的 Claude Code、面向非技术桌面自动化的 Cowork 模式，以及其三个 AI 模型的稳定更新周期。

Anthropic 也得到了五角大楼的一些帮助。该公司[起诉 DoW](https://www.axios.com/2026/03/09/anthropic-sues-pentagon-supply-chain-risk-label)，原因是该公司拒绝允许将其 AI 用于（除其他用途外）大规模监控后，DoW 对其施加了“供应链风险”的认定。[Microsoft 提交了一份法庭之友简报表示支持](https://americanbazaaronline.com/2026/03/11/microsoft-files-brief-in-support-of-anthropic-against-us-defense-476656/)。

在 AI 领域，价值观正在成为一种竞争优势，也显然是人们选择一个平台而非另一个平台的原因。

## AI 公司新闻

*   [AMI Labs](https://x.com/amilabs/status/2031234832454324639) — Yann LeCun 的初创公司表示，它正在构建从现实而非仅仅语言中学习的 AI。它在欧洲有史以来最大的种子轮融资中筹集了 10.3 亿美元，估值达到 35 亿美元。获得 Nvidia、Bezos Expeditions、Samsung 和 Eric Schmidt 的支持。
*   [Replit](https://replit.com/news/funding-announcement) — D 轮融资 4 亿美元，估值 90 亿美元，由 Georgian 领投。与融资同时推出了 Agent 4。拥有 5,000 万用户，目标是到年底实现 10 亿美元的年化收入。
*   [Legora](https://legora.com/newsroom/legora-raises-550-million-series-d-to-fuel-us-growth) — 这家瑞典法律 AI 平台完成了 5.5 亿美元的 D 轮融资，估值翻了三倍，达到 55 亿美元。用于案例法研究、文档审查和合同起草的生成式 AI。
*   [Jump](https://www.businesswire.com/news/home/20260219487440/en/Jump-Raises-80-Million-Series-B-Led-by-Insight-Partners-to-Expand-AI-Operating-System-for-Financial-Advisors) — 由 Insight Partners 领投的 8,000 万美元 B 轮融资，用于构建面向财务顾问的 AI 操作系统。在不到两年内已扩展到 27,000 名顾问。
*   [Pasito](https://www.insightpartners.com/ideas/pasito-raises-21-million-series-a-led-by-insight-partners-to-build-ai-workspace-for-the-benefits-industry) — 由 Insight Partners 领投的 2,100 万美元 A 轮融资，用于构建面向团体健康和退休福利的 AI 原生工作区。
*   [Crafting](https://www.globenewswire.com/news-release/2026/03/09/3252022/0/en/Crafting-Announces-General-Availability-of-Crafting-for-Agents-and-5-5M-Seed-Round-to-Build-Infrastructure-for-AI-Driven-Engineering.html) — 由 Mischief 领投的 550 万美元种子轮融资，用于为 AI 编码代理构建类似生产环境。客户包括 Faire、Brex 和 Webflow。