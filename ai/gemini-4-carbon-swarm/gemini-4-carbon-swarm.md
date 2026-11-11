<!--
title: 多智能体编程时代到来
cover: https://cdn.thenewstack.io/media/2026/11/94b532e0-getty-images-ngci-nquuq-unsplash-1024x677.jpg
summary: 谷歌发布面向复杂软件工程和网络安全的 Gemini 4 Carbon 模型，推出支持多智能体协同编程的 /swarm 功能，并在形式化验证和漏洞挖掘方面展现出强大能力。
-->

谷歌发布面向复杂软件工程和网络安全的 Gemini 4 Carbon 模型，推出支持多智能体协同编程的 /swarm 功能，并在形式化验证和漏洞挖掘方面展现出强大能力。

> 译自：[Multi-agent coding arrives](https://thenewstack.io/gemini-4-carbon-swarm/)
> 
> 作者：Amanda Caswell

**周二，谷歌向付费开发者发布了 Gemini 4 Carbon**，将其最新的前沿模型定位在 Gemini 4 Argon 之上，用于复杂的软件工程、网络安全和科学推理。

Argon 仍然是谷歌推荐用于日常工程和知识工作的模型，而 Carbon 则专为更高要求的任务而设计，包括多包迁移、跨子系统调试以及长期视野的智能体工作流。

Google DeepMind 高级副总裁兼谷歌首席 AI 架构师 [Koray Kavukcuoglu](https://www.linkedin.com/in/koray-kavukcuoglu-0439a720/) 在[发布公告](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)中将 Carbon 描述为该公司处理复杂、多步骤工作最强的模型。

该版本还引入了 `/swarm`，这是 Google Antigravity 中的一项预览功能，可通过单个提示词协调多个编程智能体。

## 多智能体编程时代到来

Carbon 可以构建、测试和调试全栈应用程序，同时检查代码和渲染的 UI。谷歌表示，它在多包迁移和跨子系统调试方面表现尤为出色。

谷歌尚未解释的是，`/swarm` 如何在智能体之间共享上下文、处理冲突的更改，或者决定哪些任务需要 Carbon 而不是更轻量级的模型。

谷歌声称，Carbon 在 CursorBench 4.0、Perplexity 的 WANDR 和 Zapier 的 AutomationBench 上排名第一，完成任务的成本不到次优模型的一半。

> 谷歌尚未解释的是，/swarm 如何在智能体之间共享上下文、处理冲突的更改，或者决定哪些任务需要 Carbon 而不是更轻量级的模型。

## 定价将于 11 月 30 日翻倍

该公司并未提供足够的细节来独立验证这些成本比较。Carbon 的推出价格为每百万输入 Token 2 美元，每百万输出 Token 10 美元，与 Argon 相当，但在 11 月 30 日之后价格将翻倍至 4 美元和 20 美元。

Carbon 的性能是否能够抵消这些更高的成本（包括多智能体编排和验证的开销），还有待在生产环境中验证。

## 验证 Signal 的代码

谷歌公告中最具技术雄心的例子之一涉及 AlphaProof Code，这是一个用于形式化验证的新型智能体框架。

谷歌研究人员将 Carbon 与其他模型结合使用，以数学方式证明了 Signal 加密协议底层代码的关键安全属性。

研究人员将安全需求转化为数学定理，并使用 AlphaProof Code 智能体生成了数百万行的 [Lean](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)（一种用于表达和检查数学证明的语言）。

谷歌表示，这项工作花费了数周时间，而以往专家团队进行类似验证工作历史上需要数年时间。

该公告没有具体说明验证属性的完整范围、它需要多少人工干预，或者谷歌是否会公开证明工件。

> 谷歌表示，这项工作花费了数周时间，而以往专家团队进行类似验证工作历史上需要数年时间。

## 双刃剑的安全特性

谷歌最初在 10 月下旬通过其[Fairwind 计划](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)向选定的防御者开放了 Carbon 的网络安全功能。

该公司表示，Carbon 在 SEC-bench Pro、ExploitGym 和 CWE-bench v1 上处于领先地位，这些基准测试涵盖漏洞发现、利用和修补。

在 Project Fortify（谷歌的自主扫描、分诊和修复系统）中，Carbon 在内部基准测试中实现了 100% 的扫描召回率和 95% 的分诊准确率。谷歌还报告称，在测试开源代码库时，其召回率比 Argon 相对提升了 25% 以上。

谷歌的云漏洞研究团队使用 Carbon 确认了某流行开源项目中的两个漏洞是可以被利用的，促使维护人员将其归类为关键漏洞并发布了补丁。谷歌表示，这些漏洞的严重程度与最近的 [PHP2Shell 漏洞利用](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/)相当，但在披露过程仍在进行中时，未透露受影响的项目。

另外，Wiz 通过其 Scan for Good 计划使用 Carbon 在不到两个小时的时间内发现了两个主要 SaaS 提供商的零日漏洞。受影响的组织与研究人员合作进行了修复。

## 网络安全的双面性

更强的利用能力也引发了对滥用的担忧。谷歌表示，Carbon 的安全防护在模拟环境中阻止了自适应红队智能体尝试的 99% 的攻击轨迹，将每次尝试的漏洞利用率降低至 0.8%，而 Argon 则为 3.1%。

该公司还报告称，在 Gray Swan 的间接提示词注入基准测试中，攻击成功率为 0%，同时也承认更复杂的攻击仍然是一个需要改进的领域。

这些结果来自特定的评估环境，并不能证明 Carbon 能够抵抗所有现实世界的攻击。

> 这些结果来自特定的评估环境，并不能证明 Carbon 能够抵抗所有现实世界的攻击。

## 获取 Carbon 的访问权限

Gemini 4 Carbon 可通过 Google AI Studio 和 Android Studio 中的付费 Gemini API 层以及谷歌的企业产品获得。

Google AI Ultra 订阅者可以通过 Antigravity、Gemini 应用和搜索中的 AI 模式访问 Carbon。/swarm 编排功能仍处于预览阶段。

访问 Carbon 的高级网络安全工具仍需要通过 Fairwind 获得批准。谷歌还通过 Antigravity 向精选科学家提供六个月的 Carbon 免费访问权限，申请通道现已开放，每周都有新研究人员加入。

谷歌发布了更新的 [Gemini 4 开发者指南](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)，涵盖迁移和实现。

原文 [Google says Gemini 4 Carbon proved Signal’s encryption in weeks](https://thenewstack.io/gemini-4-carbon-swarm/) 发表于 [The New Stack](https://thenewstack.io)。