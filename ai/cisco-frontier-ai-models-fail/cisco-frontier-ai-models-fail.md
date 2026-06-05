<!--
title: 思科研究：OpenAI、谷歌及亚马逊等大模型均未能抵御此类攻击
cover: https://cdn.thenewstack.io/media/2026/06/2c3289f6-pawel-czerwinski-tk43-x-yjta-unsplash.jpg
summary: 思科研究表明，现有的单轮安全评估无法预测多轮对话攻击的防御能力。包括GPT、Gemini在内的15款主流闭源模型在多轮攻击测试中均宣告失败。
-->

思科研究表明，现有的单轮安全评估无法预测多轮对话攻击的防御能力。包括GPT、Gemini在内的15款主流闭源模型在多轮攻击测试中均宣告失败。

> 译自：[OpenAI, Anthropic, Google, Amazon, and xAI all fail on type of attack, study finds](https://thenewstack.io/cisco-frontier-ai-models-fail/)
> 
> 作者：Darryl K. Taft

企业买家用来评估 AI 模型的安全基准测试可能测错了方向。

这是 [Cisco](https://thenewstack.io/cisco-is-using-ebpf-to-rethink-firewalls-vulnerability-mitigation/) 最近一项研究所得出的结论。该研究对来自 [OpenAI](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/)、[Anthropic](https://thenewstack.io/anthropic-agent-sdk-confusion/)、[Google](https://thenewstack.io/is-ai-the-ultimate-version-of-google-as-larry-page-wanted/)、[Amazon](https://thenewstack.io/amazon-ai-assisted-errors/) 和 [xAI](https://x.ai/) 的 15 个闭源前沿模型进行了单轮和多轮评估的对比。

每个模型都在相当大比例的多轮攻击中败下阵来，在这一测试群体中，这些攻击的成功率在 7.89% 到 88.30% 之间，其跨度比单轮攻击的 2.19% 到 64.91% 还要宽。

单轮是“一问一答”式的单次交互。多轮则是连续的来回对话。

报告指出：“多轮评估之所以重要，首要原因在于：这是攻击者施展手段的地方。现实中的对手会不断迭代、重新定义被拒绝的请求、跨轮次分解任务、扮演特定角色并逐步升级攻击。”

## 单轮得分无法说明全部问题

最具影响力的发现并不是那些原始数据，而是单轮表现很难预测多轮的抗御能力。跨模式的差异在两个方向上的波动高达 55 个百分点。

[Gemini 3 Pro](https://thenewstack.io/google-launches-gemini-3-pro/) 在单轮攻击成功率（ASR）仅为 18.10% 的情况下，在迭代攻击下飙升至 73.35%，翻了近四倍。[OpenAI 的 GPT-5.4](https://thenewstack.io/openai-gpt-5-4-ai-jobs-report-anthropic-dow-supply-chain-risk/) 在单轮攻击中表现出色，ASR 仅为 2.74%，但在多轮压力下达到了 24.68%，激增了九倍。在非推理配置下的 [Grok 4.1 Fast](https://x.ai/news/grok-4-1-fast)，尽管其单轮基准测试的 ASR 仅为 34.15%，但其多轮 ASR 却达到了 88.30%。

报告显示，[Anthropic Claude](https://thenewstack.io/anthropic-launches-claude-opus-4-and-sonnet-4/) 系列在多轮测试中整体表现最佳，在迭代攻击下的 ASR 范围在 11.16% 到 16.20% 之间，虽然较其单轮基准（2.19% 到 3.64%）有所上升，但仍远低于测试群体中的大多数模型。

[Amazon 的 Nova](https://thenewstack.io/aws-updates-its-nova-models-to-compete-with-google-anthropic-and-openai/) 变体表现出了最反直觉的结果。这三个变体均呈现出与大多数模型相反的趋势：单轮故障率高，但多轮 ASR 较低。Nova 2 Lite 的单轮 ASR 为 34%，但在同类模型中却实现了最低的多轮 ASR，仅为 7.89%——这是单轮脆弱性并未转化为迭代暴露风险的最典型案例。

## 一个配置标记，45 个百分点的差异

或许在操作层面上，最重大的发现与 Grok 4.1 Fast 相关。在完全相同的测试条件下，仅由于启用推理模式这一单一配置更改，就使多轮 ASR 从 88.30% 降至 43.47%——降幅达 44.83 个百分点。

Cisco 表示，据其所知，目前尚无任何公开基准测试或模型说明（model card）能够捕捉到这种由配置驱动的安全变化，并主张 AI 供应商在发布能力基准测试的同时，应披露部署时设置对安全的具体影响。

## 故障集中在何处

报告指出，并非所有攻击策略都同样有效，也不是所有模型都以相同的方式失败。Cisco 将多轮评估结果分解为五个攻击策略族。在每个策略族中，最容易受到攻击的模型与最不容易受攻击的模型之间的差距在 79 到 89 个百分点之间，这意味着综合得分可能会掩盖针对特定策略的漏洞。

在单轮测试方面，失败主要集中在少数几个过程中。冒充 AI 攻击以 37.50% 的加权 ASR 位居首位，比排在第十位的过程高出 14 个百分点以上。温和释义（Soft Paraphrase）和系统提示（System Prompts）紧随其后。在内容方面，仇恨言论（Hate Speech）、亵渎性语言（Profanity）和专业建议（Specialized Advice）占主导地位。

## 企业应该怎么做

Cisco 将其发现转化为以下三条实用建议：

* 首先，AI 供应商在每次发布模型时，应公布按策略族细分的攻击成功率。
* 其次，企业部署网关应包含针对高风险过程和内容类型的回归测试，并将触发审查的阈值设定为 3 个百分点。
* 第三，任何在单轮与多轮 ASR 之间差距超过 15 个百分点的模型，在部署前都必须进行人工审查——这一规则将筛出本次测试的 15 个模型中的 8 个。

一个重要警告：Cisco 测试的是*不含*系统提示、内容过滤器或自定义编排的基础模型，而实际的企业部署通常包含这些控制措施，这可能会在不同方向上改变最终结果。

报告总结道，更广泛的启示在于，“即使对于领先供应商的前沿模型而言，安全性仍是一项持续的、视模式而定的属性，而非非黑即白的认证。”