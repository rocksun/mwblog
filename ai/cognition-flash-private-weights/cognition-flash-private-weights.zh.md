Cognition将其最新的编程模型建立在任何人都可以下载的基础之上，然而该公司却将自己完成的版本锁了起来。

周三发布的 [SWE-2 Flash](https://cognition.com/blog/swe-2-flash) 的成本仅为 Cognition 更大的 SWE-2 模型的五分之一，据该公司称，其生成 Token 的速度大约快三倍。该新模型建立在 Thinking Machines Lab 的开源权重 Inkling-Small 之上，但有一个附加条件：Cognition 援引网络安全方面的担忧，将权重设为私有。

Inkling-Small 是一个拥有 2760 亿参数的混合专家模型，其中包含 120 亿个活跃参数。由联合创始人兼 CEO [Mira Murati](https://www.linkedin.com/in/mira-murati-4b39a066/) 领导的初创公司 Thinking Machines Lab 于 7 月 30 日在 Apache 2.0 许可证下发布了该模型，这意味着任何人都可以从 Hugging Face 获取权重并在其基础上进行构建。

> “将薄弱的开源基础转化为可用智能体模型的实用方法，”

Cognition 表示，其性能的大部分提升来自于在强化学习之前增加了一个中期训练阶段，并且其公布的数据令人瞩目——在 Terminal-Bench 4.0 上，Flash 的得分为 20%，而 Inkling-Small 为 0.9%；其 FrontierCode 2.0 的得分从基础模型的 3.2% 攀升至 24%，险胜 SWE-2 的 23.8%。

CultOfAI 是 X 平台上的一个 AI 评论[账号](https://x.com/TheCultOfAI/status/2118664755514876078)，它将中期训练称为“将薄弱的开源基础转化为可用智能体模型的实用方法”，尽管该账号同时也警告称，这些数据是 Cognition 自己的数据，尚未经过独立验证。

## 更便宜、更快，但依然落后

Flash 并非在每项测试中都能跟上较大模型的步伐，在 SWE-Bench Pro v2 Hard 上以 89.9% 对 90.6% 的微弱差距紧随 SWE-2 之后，但在 DeepSWE 1.1 和 Terminal-Bench 4.0 上有所落后，同时包括 Claude Haiku 5.5 和 DeepSeek V4.1 Flash 在内的竞争对手在多项基准测试中的得分都超过了它。

## 开源基础，私有权重

在根据 Apache 2.0（最具包容性的[开源许可证](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/ "open source licenses")之一）发布的模型进行构建时，并不强制 Cognition 公开自己的工作，因为该许可证允许开发人员修改和商业化衍生作品，而无需分享他们的更改——因此，将 SWE-2 Flash 的权重保持私有完全在公司的权利范围内，尽管这违背了它所借用的基础的精神。

这一决定引起了 GenerAIte Solutions CEO [David Hendrickson](https://www.linkedin.com/in/david-hendrickson-667971102/) 的注意，他赞扬 Cognition 将 Inkling-Small 变成了一只“编程野兽”，但[在 X 上指出](https://x.com/TeksEdge/status/2118100981309190355)“改进后的权重并未公开”。

他的观察正值开源权重模型缩小与专有替代方案的性能差距，并成为[编程平台的有力竞争者](https://thenewstack.io/kimi-k3-open-weight-coding/)之际。Cognition 决定对其改进后的模型保密，这与这一趋势形成了鲜明对比。

Cognition 表示，它正在建立一个计划，与精选的行业合作伙伴和研究实验室共享权重，这些合作伙伴和实验室可以在自己的基础设施上检查、微调和运行该模型，这种安排可能会吸引担心敏感代码离开其系统的企业和政府。

该公司表示，更多细节将在未来几周内公布，目前尚不清楚谁将有资格、他们将面临什么限制，或者是否允许他们分享基于 SWE-2 Flash 构建的模型。

## 网络安全驱动的封锁

网络安全是 Cognition 限制权重决策的核心。该公司将网络安全任务纳入了 Flash 的训练中，将其 ExploitBench 得分从 Inkling-Small 的 11.3% 提升至 34.8%。这是一个显著的改进，尽管该基准并没有确定该模型在现实世界的攻击中会表现如何，或者发布其权重是否会增加被滥用的风险。

> Cognition 将 AI 驱动的网络攻击的增加作为限制访问的理由。

令人担忧的是，用于发现和调查漏洞的功能同样可以轻易地帮助攻击者。Cognition 将 AI 驱动的网络攻击的增加作为限制访问的理由。类似的挑战正在整个行业流行；AI 工具现在可以[以比维护人员调查和修复更快的速度，识别开源项目中成千上万个潜在的漏洞](https://thenewstack.io/anthropic-oss-scanner-vulnerabilities/)。

## 美国模型，有限访问

Cognition 将 SWE-2 Flash 描述为一个完全美式的编程模型，并声称它在领先的评估中击败了所有美式开源权重模型，包括比它大三倍的模型，这一说法很有分量，因为该公司自己的基准表显示，在美国境外构建的模型（其中包括 DeepSeek V4.1 Flash）在多项测试中的得分都超过了 Flash。

开发人员可以通过 Devin Desktop 和 CLI 试用 SWE-2 Flash，该模型在 11 月 30 日之前免费。

> Cognition 将 SWE-2 Flash 描述为一个完全美式的编程模型，并声称它在领先的评估中击败了所有美式的开源权重模型

[网络安全专家
2026年成为网络安全专家的分步指南

基础 IT 技能
CTF（夺旗赛）
操作系统
网络知识
认证
安全技能与知识
云技能与知识
编程技能](https://roadmap.sh/cyber-security?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=cognition-flash-private-weights)