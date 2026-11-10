<!--
title: Anthropic发布Fable 5.2：降价促销并大幅提升编程跑分
cover: https://cdn.thenewstack.io/media/2026/11/75d15cd2-claude-fable-5.2-image.jpg
summary: Anthropic发布了最新旗舰模型Claude Fable 5.2与Mythos 5.2，带来更强的编程和推理能力、更快的速度以及价格下调。新版本在多项基准测试中表现亮眼，并支持复杂的智能体协作和硬件设计。
-->

Anthropic发布了最新旗舰模型Claude Fable 5.2与Mythos 5.2，带来更强的编程和推理能力、更快的速度以及价格下调。新版本在多项基准测试中表现亮眼，并支持复杂的智能体协作和硬件设计。

> 译自：[Anthropic launches Fable 5.2 with a price cut and stronger coding scores](https://thenewstack.io/anthropic-fable-coding-upgrade/)
> 
> 作者：Frederic Lardinois

周一，Anthropic[发布了Claude Fable 5.2和Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2)，这是其双旗舰模型的最新版本。

与之前一样，Fable 5.2今天将在所有平台上推出，包括亚马逊云科技（Amazon Web Services）、谷歌云（Google Cloud）和微软云（Microsoft Azure），而对Mythos的直接访问仍然限于Anthropic的[网络安全](https://www.anthropic.com/news/cyber-verification-program)和[生命科学](https://www.anthropic.com/news/life-sciences-verification-program)验证计划中的组织。

同样与之前类似，Fable和Mythos共享相同的底层模型，但Fable带有更严格的网络安全和生物学防护机制。

Anthropic没有将这些模型命名为“5.5”，这也许有点令人意外，因为它的Claude Opus、Sonnet和Haiku模型现在都处于该版本号。

该公司强调，它仍然建议用户在大多数编程和知识任务中使用Opus 5.5，而Fable 5.2旨在帮助用户“应对最艰巨的技术挑战”。

根据Anthropic的说法，虽然这两个模型在编程、推理和视觉方面都有所改进，但该公司强调的一个特点是速度。该公司表示，Fable 5.2和Mythos 5.2的输出生成速度分别比Fable 5.1和Mythos 5.1快高达30%。

![](https://cdn.thenewstack.io/media/2026/11/df96c5c9-screenshot-2026-11-09-at-11.06.08-am-800x1024.png)

图片来源：Anthropic。

## Fable快速模式（Fast mode）

对于想要更快响应的用户，现在这两个模型都推出了快速模式，Anthropic表示这可以将 Token 生成速度提高最多 2.5 倍。

它可在 Claude Code、Claude 平台上、通过谷歌云上的 Claude 模型以及通过 Anthropic 托管的微软 Foundry 使用。

## 定价

至于定价，Fable 的价格仍然比 Opus 贵，但 Anthropic 正在将每百万个输入/输出 Token 的价格从 10 美元/50 美元下调至 8 美元/40 美元。Mythos 5.2 享有相同的费率。

对于输入 Token 高达 272,000 的提示词，OpenAI 的旗舰产品[GPT-6 Astra 的标准费率仍为 10 美元/50 美元](https://developers.openai.com/api/docs/models/gpt-6-astra)，这使得 Anthropic 在这些 Token 费率上比其竞争对手低 20%（至少目前如此）。

对于这两个模型，快速模式的费用为每百万输入 Token 16 美元，每百万输出 Token 80 美元，是标准费率的两倍。

即使在降价之后，Fable 的标准输入和输出费率仍然是[Opus 5.5 当前价格](https://platform.claude.com/docs/en/about-claude/pricing)的两倍，不过 Anthropic 的新评估表明，这并不一定意味着每个任务的成本更高。

## Fable 5.2 瞄准复杂编程

在 FrontierCode 2.0 上，Anthropic 报告称 Fable 5.2 的得分为 49.1%，而 Fable 5.1 为 32.4%，Opus 5.5 为 45.5%，GPT-6 Astra 为 42.8%。在 FrontierSWE v2 上，它得分为 69.9%，领先于 Astra 的 65.5% 和 Opus 的 62.3%。

不过，与 Opus 的成本比较可能更有趣。Anthropic 表示，在早期的 FrontierCode 2.0 测试中，高工作量（High effort）模式下的 Fable 5.2 的表现与最大工作量（Max effort）模式下的 Opus 5.5 相当，而每个任务的成本大约只有后者的一半。

“中等”（Medium）现在是 Claude 应用和 Claude Code 中 Fable 5.2 的默认工作量级别。

不过值得注意的是，这些结果并非 Fable 5.2 的全面胜利。

Gemini 4 Carbon 在测试业务工作流的 AutomationBench 上领先于 Fable，得分为 53.9% 对 51.4%。同时，Opus 在知识工作评估 AA-Briefcase v1.1 的 Elo 衡量标准上仍然保持微弱领先。

Anthropic 表示，Fable 可以充当顾问，供较小的模型就更困难的问题进行咨询，或者充当编排器，将较简单的任务委派给它们。在一个内部实验中，一名工程师让 Fable 5.2 从一个空文件夹构建一个原型操作系统。

该公司表示，它在八天内协调了 1,000 多个子智能体，并生产了一个可以在笔记本电脑上启动的操作系统的完整版本，包括驱动程序、持久存储、图形界面和安装程序。

## Fable 承诺减少安全拦截

Anthropic 表示，Fable 5.2 的网络和生物学防护机制与 5.1 版本一样强健。在 Claude.ai、Claude Code 和 Cowork 的早期测试中，该公司观察到整体拦截率减少了约 55%，其中网络安全领域减少了约 60%，生物学领域减少了约 40%。

这可以减少对合法工作的干扰，尽管拦截减少并不一定意味着权限放宽。Fable 仍然会阻止高风险的网络活动（包括渗透测试和漏洞利用生成）以及大多数生物学研究任务。Anthropic 表示，当查询被阻止时，用户将改为收到来自 Opus 4.8（针对网络安全）或 Opus 5（针对生物学）的响应。

对 Mythos 的直接访问仍然受到门控限制，但企业安全工作还有另一条途径：Claude 企业版（Claude Enterprise）客户可以使用 Claude Security，该功能现在包含 Mythos 5.2，即使他们不是网络安全验证计划（Cyber Verification Program）的成员。

Anthropic 还表示，它在训练期间刻意限制了某些 AI 开发能力的改进，包括加速器内核优化和大语言模型架构的工作。该公司表示，在这些领域，模型的性能大约处于 Opus 5.5 的水平。它表示，这些限制不会影响智能体编程、硬件开发或传统的机器学习研究。

对于 API 开发者，Anthropic 正在向所有账户扩展保留思考（preserved thinking）功能。该功能限制了对 Claude 先前上下文的更改，这些更改可用于提取其推理过程以进行蒸馏。

## 企业级防护进入私有测试阶段

该公司在 9 月首次宣布的[企业前沿防护（Enterprise Frontier Safeguards）](https://www.anthropic.com/news/enterprise-frontier-safeguards)也正在进入私有测试阶段，Bridgewater、Salesforce 和 Stripe 是早期客户之一。Anthropic 表示，自动化安全监控在客户自己的基础设施中存储的提示词和响应上运行，使其与零数据保留（zero data retention）兼容。

符合条件的客户可以在实施该系统之前继续使用 Fable 5.2 和 Mythos 5.2 并实现零数据保留。对于其他客户，Anthropic 会保留数据 30 天用于安全监控。

## 适用于物理学的 Fable

Anthropic 认为，其模型的编程能力也适用于科学研究，因为大量的此类工作也是基于软件的，包括分析数据、建模分子、设计零件或控制仪器。

该公司表示，Fable 5.2 解决了两个涉及黑洞和全息对偶性的未决理论物理学问题。其中一个涉及完成 2003 年提出的计算，以确定在小宇宙量子描述中黑洞的形成是否仍然是一个突变。另一个则确立了在一处简化宇宙中用于排除量子引力候选理论的技术的极限。

Fermat 声明比早期的公告所暗示的更具体。Anthropic 表示，由 1,000 个 Fable 5.2 智能体组成的团队在人工干预极少的情况下，于 30 小时内在 Lean 中完全形式化了费马最后定理（Fermat’s Last Theorem）的证明。形式化用计算机可以一步步检查的语言表达了一个证明；这不同于发现新的证明。

据 Anthropic 称，智能体收到了用于衡量进度的中间定理陈述列表，但没有数学参考资料。Claude 的早期研究版本在有定制工具和人工指导的情况下花费了 11 天。该公司比较时每个模型使用单次运行，Opus 5.5 在 18 小时后达到 26%，并且在 30 小时后几乎没有取得进一步进展。

Anthropic 还测试了 Fable 5.2 在硬件设计方面的表现，与电路板公司 Diode 合作生产了语音助手集线器、USB 免提电话和手持虚拟宠物。该公司表示，Claude 选择了组件、设计了电路板和外壳，并编写了软件。Diode 制造了电路板，其工程师在 Claude 的指导下测试并组装了设备。

根据 Anthropic 的说法，这三个设备都在没有进行电气修改的情况下正常工作。