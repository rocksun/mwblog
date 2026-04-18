周三，Anthropic 发布了 Claude Opus 4.7，这是对 Opus 4.6 的直接升级。它在处理复杂、长期运行的任务方面可能优于前代模型，但在广义能力上略逊于上周发布的近乎神话般的 [Claude Mythos 预览版](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/)。

现在，Opus 4.7 已在所有 Claude 产品和 Anthropic 的 API（以及 Amazon Bedrock、Google Cloud 的 Vertex AI 和 Microsoft Foundry）中上线，定价与 [Opus 4.6](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/) 相同。Anthropic 的公告称，Opus 4.7 在指令遵循、视觉、创造力、记忆和财务分析方面均有更出色的表现。

## Anthropic 称 Opus 4.7 在哪些方面做得更好

Anthropic 报告称，Opus 4.7 的早期测试者（包括 Intuit、GitHub 和 Notion）给出了强烈的正面反馈。

首先，之前的 Claude 模型在遵循用户指令时可能会推测“弦外之音”（或者完全忽略指令），而最新的迭代版本据报道更擅长听从指挥。

> 据报道，Claude Opus 的最新迭代版本更擅长按要求办事。

有趣的是，Anthropic 的公告指出，这种更新后的能力意味着“为早期模型编写的提示词有时现在会产生意想不到的结果”。因此，Claude 用户可能需要调整他们的提示词编写风格，以适应 Opus 4.7 更加字面化的指令遵循方式。

> “为早期模型编写的提示词有时现在会产生意想不到的结果。”

此外，模型还承诺为高分辨率图像提供更好的视觉能力，随之而来的是更多的多模态用途。Opus 4.7 用户可以预期模型能够接受比以前多三倍以上像素的图像，从而为更多依赖精细视觉细节的用途铺平道路，例如阅读密集的屏幕截图。

比较模糊的一点是，Anthropic 称 Opus 4.7 在“完成专业任务时更有品味且更有创意”，并引用了一些早期测试者的反馈来证明该模型具有据称“更高质量”的界面、幻灯片和文档设计：

> “设计品味真的令人惊讶——它做出的选择是我在实际工作中会采用的，”Triple Whale 的联合创始人兼 CEO Aj Orbach 在 Anthropic 的博客文章中表示。

Opus 4.7 的下一个亮点是增强的记忆力。Anthropic 的公告称，新模型“更擅长使用基于文件系统的记忆”，使其能够记忆并引用不同任务之间的笔记，从而使用户无需反复提供前期背景信息。

最后，在发布博客文章中，Anthropic 强调 Opus 4.7 在 [GDPval-AA](https://artificialanalysis.ai/evaluations/gdpval-aa) 测评中处于领先地位。这是一项第三方评估，旨在测试大语言模型（LLM）在金融和法律等领域处理具有经济价值的真实世界任务的能力。

与此同时，这家 AI 公司表示，其内部测试显示 Opus 4.7 是“比 Opus 4.6 更有效的财务分析师”，这归功于其严谨的分析、更专业的演示文稿以及跨任务的紧密集成。

## 安全性表现如何？

虽然 Opus 4.7 宣传改进了指令遵循、视觉和记忆，但在安全性方面进展甚微。

根据 Anthropic 的测试，与今年 2 月发布的 Opus 4.6 相比，新模型在欺骗、谄媚和配合滥用方面的比例同样较低，据报道在诚实度和抵御提示词注入攻击方面有所改进。

但 Opus 4.7 确实有一项安全性降级：根据 Anthropic 的说法，在“针对受控物质提供过度详细的减少危害建议的倾向”方面，Opus 4.7 稍显逊色。

总体而言，根据 Anthropic 的对齐评估，该模型被描述为“大部分对齐良好且值得信赖，尽管其行为并非完全理想”。

## 绕不开的 Mythos 模型

自然，紧随上周发布的 Claude Mythos 预览版（以及[后续 ASI 评估的结果](https://thenewstack.io/claude-mythos-preview-simulation/)）之后，人们难免会将其与 Anthropic 发言人告诉 [*Fortune*](https://fortune.com/2026/03/26/anthropic-leaked-unreleased-model-exclusive-event-security-issues-cybersecurity-unsecured-data-store/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) 的“我们迄今为止构建的能力最强的[模型]”进行比较。

三周过去了，这家 AI 公司的论调没有改变。在 Opus 4.7 的发布博客文章中，Anthropic 再次确认了 Claude Mythos 预览版作为“我们训练过的对齐最好的模型”的地位。

此外，它表示正在履行其承诺，即使用能力较弱的模型作为新网络安全防护措施的试验场——Opus 4.7 就是第一个此类模型。

Anthropic 表示，该模型的发布包含了能够“自动检测并阻止指示禁止或高风险网络安全用途请求”的防护措施。展望未来，它希望利用 Opus 4.7 现实部署中的经验教训，最终实现“Mythos 级模型”的更广泛发布。

当被问及公司希望从 Opus 4.7 的部署中了解哪些关于网络安全防护的信息时，Anthropic 未予置评。

## 但要注意 Token 使用量

在最近的[一连串坏运气](https://thenewstack.io/anthropic-claude-code-leak/)中，Anthropic 一直在处理用户关于[达到使用限制的速度比平时快](https://thenewstack.io/claude-code-usage-limits/)的投诉。

现在，当用户计划从 Opus 4.6 迁移到 Opus 4.7 时，这家 AI 公司强调了两个将影响 Token 使用量的变化：Opus 4.7 使用了更新的分词器（tokenizer），并且“在更高努力水平下思考得更多”。

虽然这些变化应该会提高可靠性和文本处理能力，但 Anthropic 提醒 Claude 用户可能会看到 Token 使用量增加。为了缓解这种情况，它建议用户使用 effort 参数、调整任务预算，或者直接告诉模型要更简洁。