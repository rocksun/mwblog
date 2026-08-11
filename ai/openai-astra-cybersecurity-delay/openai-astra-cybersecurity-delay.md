<!--
title: OpenAI暂缓发布Astra模型：内部测试发现潜在关键网络安全风险
cover: https://cdn.thenewstack.io/media/2026/07/a2d3970a-and-machines-wjdr7cya8ts-unsplash-1-scaled.jpg
summary: OpenAI推迟发布Astra模型，因其在内部测试中表现出“关键”级别的网络安全风险，具备自主发现并利用零日漏洞的能力。公司已加强隔离测试与监管，未来可能限制该模型的使用权限。
-->

OpenAI推迟发布Astra模型，因其在内部测试中表现出“关键”级别的网络安全风险，具备自主发现并利用零日漏洞的能力。公司已加强隔离测试与监管，未来可能限制该模型的使用权限。

> 译自：[The AI model OpenAI won't release yet — and what it found in testing](https://thenewstack.io/openai-astra-cybersecurity-delay/)
> 
> 作者：Amanda Caswell

**OpenAI 正在减少对 [Astra](https://thenewstack.io/openai-astra-math-cost/) 的投入**，因为内部测试表明，该即将推出的模型可能触及了 OpenAI 此前任何模型都未曾触及的网络安全限制。尽管尚未确定官方发布日期，但这一突发障碍可能会推迟其随后的发布。

该公司表示，在 Astra 中“无法排除关键的网络安全能力”，[*Axios* 首次报道了这一点](https://www.axios.com/2026/08/07/openai-astra-model-delay-cybersecurity-risks)。目前，公司已暂停了不符合加强后安全要求的内部活动，同时扩大了测试范围并收紧了对该模型的控制。

## “关键”的真正含义

根据 OpenAI 的 [准备框架 (Preparedness Framework)](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf)，当模型能够在无需人工干预的情况下，识别并开发出针对许多加固的、真实世界关键系统的各种严重程度的零日活动时，该模型就达到了“关键 (Critical)”网络安全阈值。

如果模型在仅接收到一个高级目标后，就能开发并执行针对加固目标的创新型端到端攻击，也符合这一资格。初步结果非常明显，以至于公司无法自信地将其评估为该级别以下。

对于开发者而言，令人担忧的是，使 [编码代理 (coding agents)](https://thenewstack.io/microsoft-copilot-token-budgets/) 变得更有用的技能，同样可以被转向攻击它们本应为其服务的软件。

> 使编码代理变得更有用的技能，同样可以被转向攻击它们本应为其服务的软件。

## 在更严格的隔离环境中测试

此前的模型，包括 [GPT-5.6 Sol](https://thenewstack.io/sol-usage-limits-reset/)，被评估为“高 (High)”网络安全级别。OpenAI 现在对 Astra 的处理方式有所不同，即在隔离环境中对其进行测试，并对模型可以访问的网络和工具施加更严格的限制，因为“关键”级别的模型在开发过程中需要专门的防护措施。

OpenAI 也在加强围绕模型本身的保护，并增加了监督机制，以便在检测到不安全行为时能够停止模型运行。这些措施强调了一个紧迫的工程问题：随着代理在减少人工监督的情况下承担更多工作，它们周围的环境也就成为了安全边界的一部分。

## 代理突破真实组织防御

该公司表示，Astra 并未参与[最近的 Hugging Face 安全事件](https://openai.com/index/hugging-face-model-evaluation-security-incident/)，但该事件仍然证明了当代理的能力超过其测试环境的控制范围时可能会发生什么。

[Anthropic 披露](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals)称，其 Claude 模型在类似的网路安全评估中曾突破了三个独立的组织。随后，英国人工智能安全研究所报告称，Claude Mythos 5 和 GPT-5.6 Sol 在许可的网络安全评估中进行了 19 次未经授权的现实世界操作，包括试图创建虚假身份并将恶意代码插入开源项目。

## 访问可能需要审查

OpenAI 尚未说明 Astra 是否会通过 ChatGPT、Codex 或其 API 提供，但公司现有的方针表明，并非每个用户都能获得同等级别的访问权限。通过其 [网络可信访问 (Trusted Access for Cyber)](https://openai.com/index/trusted-access-for-cyber/) 计划，公司向获批的安全专业人员提供了并非人人可用的工具。Astra 可能也会走类似的道路，将其最强大的能力限制在愿意接受更严密监督的研究人员和组织范围内。

> 开发者在获得使用该模型最强大能力的权限之前，可能必须证明自己的身份并说明计划如何使用该模型。

开发者在获得使用该模型最强大能力的权限之前，可能必须证明自己的身份并说明计划如何使用该模型。即便如此，OpenAI 也可能对 Astra 被允许执行的操作设置更严格的边界。