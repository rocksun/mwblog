随着前沿模型竞争的加速，AI 爱好者们在用户和开发者层面都对各大主流提供商产生了忠诚度的分歧。推理能力的差异已被普遍接受——但大多数人认为，在最高水平上，前沿大语言模型（LLM）应该会在基础的现实世界事实上达成一致。

然而，事实并非如此。

本月在声明验证平台 [Lenz](https://lenz.io/research/llm-disagreement) 上发布的一项分析发现，在 1,000 个近期真实用户的事实核查声明（即被断言为真实的关于世界的陈述）中，五个前沿大语言模型组成的评估小组在 67% 的声明上产生了分歧，这意味着至少有一个模型对多数裁决提出了异议，或者根本没有形成明确的多数意见。

## 从四分类评估标准中做出裁决

这五个模型（[GPT](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/)-5.4、[Claude Opus 4.7](https://thenewstack.io/claude-opus-47-launch/)、[Gemini 3 Pro](https://thenewstack.io/google-launches-gemini-3-pro/)、[Gemini 3 Pro](https://thenewstack.io/googles-gemini-3-1-pro-is-mostly-great/) + Search、[Sonar Pro](https://thenewstack.io/how-developers-can-take-advantage-of-perplexitys-sonar-llms/)）被赋予了相同的现实世界声明，并被要求从四分类[评估标准](https://en.wikipedia.org/wiki/Rubric_(academic))（真实 / 大致真实 / 误导性 / 虚假）中做出裁决。由于每个声明只能有一个分类是正确的，因此评估小组中的任何分歧都意味着至少有一个模型的标签是不一致的。

根据 Lenz 的说法，这五个模型的“分歧是刻意设计的”，因为它涵盖了生产级 AI 系统中常见的各种推理模式。

## 推理有多少种类型？

推理的范围[从](https://www.gocodeo.com/post/from-data-to-understanding-how-ai-inference-works---engines-optimization-tricks-and-production-frameworks?utm_source=copilot.com)延迟敏感型推理到吞吐量感知型、资源受限型和可扩展型推理，通常分为低延迟高吞吐量推理（例如用于互动式聊天机器人）和离线或批量推理（在这种情况下，系统会在针对成本进行优化后，在后续分析之前积累数据）。

> “与标准的基准测试问题不同，这些模型在训练期间没有见过这些声明——也就是说，这是一个跨越科学、医疗保健、政治、法律和其他领域的全新现实世界语料库。”

支撑 5 月 21 日这篇论文的研究是由 [Kosta Jordanov](https://www.linkedin.com/in/kjordanov/) 领导的，他是 Lenz 的创始人，也是 [Wiser](https://wisertech.com/)（一家总部位于保加利亚索非亚的 IT 咨询和软件工程集团）的联合创始人。

[Kosta Jordanov](https://www.linkedin.com/in/kjordanov/) 告诉 *The New Stack*，他的团队在研究中使用的声明是自 2026 年 2 月 15 日以来，用户在 Lenz 上进行事实核查的真实声明。

## 全新的现实世界数据集

“我们排除了私有声明、近乎重复的声明以及任何包含个人身份信息（PII）的声明，”[Kosta Jordanov](https://www.linkedin.com/in/kjordanov/) 表示。“这个语料库的有趣之处在于，与标准的基准测试问题不同，这些模型在训练期间没有见过这些声明——也就是说，它是一个跨越科学、医疗保健、政治、法律和其他领域的全新现实世界语料库，涵盖了人们关心并进行事实核查的话题。”

> 除了 67% 的异议指标外，34% 的声明存在实质性分歧

除了 67% 的异议指标外，34% 的声明存在实质性分歧（相差 2 个及以上的分类），而 21% 的声明则处于对立两极（至少有一个模型判定为“虚假”，至少有一个模型判定为“真实”）。在这种水平上，我们可以开始看到，从提出异议到产生分歧的过程，正在对在线生产环境中的 AI 系统和工具产生实际影响。

> “如果软件工程团队运营的系统涉及法律、财务或声誉风险，并且它向用户提供了不真实或虚构（幻觉）的内容，那么你应该考虑在 AI 生成的内容到达用户之前，如何对其进行验证。”——Kosta Jordanov。

## AI 开发者应该如何看待这种脱节？

实际的启示是，对于现实世界的声明，单个前沿大语言模型给出的意见来自明显不稳定的分布。而第二个模型往往会给出另一个完全不同的意见。

“对于许多应用来说，这没什么大不了的，”[Kosta Jordanov](https://www.linkedin.com/in/kjordanov/) 澄清道。“但如果一个软件工程团队运营的系统涉及法律、财务或声誉风险，并且它向用户输出了不真实或虚构（幻觉）的内容，那么你就应该思考在 AI 生成的内容触达用户之前，该如何对其进行验证。”

那么问题来了：为什么前沿模型能在“真实/虚假”的两极自信地达成一致，却在中间地带的裁决上严重破裂？不幸的是，基于这项研究，这是一个很难回答的问题。[Kosta Jordanov](https://www.linkedin.com/in/kjordanov/) 提出的一个假设是，“大致真实”和“误导性”这两个类别比“真实”和“虚假”类别更加模糊。

他表示：“不过，我们测量到，某些模型使用中间分类的频率远低于其他模型——Gemini 非常‘自信’，仅将 6% 的声明归入中间的两个分类，而 Opus 4.7 的这一比例为 45%。”

## Anthropic 的表现是否特别失常？

看看这里可能出现的低级错误，如果 [Claude Opus 4.7](https://thenewstack.io/claude-opus-47-launch/)（之前曾[受到过早期批评](https://thenewstack.io/claude-opus-47-flaky-performance/)）与同行多数意见达成一致的比例最低（为 70%），这是否应该引起 Anthropic 的担忧？

“不一定，”[Kosta Jordanov](https://www.linkedin.com/in/kjordanov/) 澄清道。“我们有限的初步研究表明，多数人往往也是错的，有时我们甚至会看到错误的全体一致裁决；也就是说，与多数人意见不同并不一定意味着是错的。”

这项研究没有使用任何“地面实况”（ground truths，即经过广泛验证和证实的无可争议的现实世界事实），而仅仅测量了模型裁决之间的差异。它无法回答哪一个模型在针对哪一个声明时是正确的。

> “我们[对大语言模型准确性]的分析表明，基准测试准确率表面上的趋同可能掩盖了深层认知上的分歧。” —— 康奈尔大学的 Eddie Yang 和 Dashun Wang。

## 该领域的其他研究

学术界和有商业支持的模型研究目前似乎正在转向这一领域。康奈尔大学的 Eddie Yang 和 Dashun Wang 于 2 月发表的一项[研究](https://arxiv.org/abs/2602.11898)指出，基准测试是衡量和信任大语言模型（LLM）进展的基础。

“然而，我们的分析表明，基准测试准确率表面上的趋同可能会掩盖深层的[认知分歧](https://www.linkedin.com/pulse/epistemic-divergence-predictive-artificial-when-machines-diamond-ggjse/)。通过使用两个主要的推理基准测试——MMLU-Pro 和 GPQA——我们展示了即使是取得相似准确率的大语言模型，在 16-66% 的项目上仍然存在分歧，而在表现最好的前沿模型中，这一分歧比例也有 16-38%，”Eddie Yang 和 Dashun Wang 在 2 月写道。

## 下一步引入人类反馈

[Kosta Jordanov](https://www.linkedin.com/in/kjordanov/) 证实，该分析只是第一步。

“我们确实计划进行后续研究，评估这些模型与人类提供的标签之间的差距，并评估基于数据源的多步多模型 Lenz 管道与这些标签以及前沿模型之间的对比，”[Kosta Jordanov](https://www.linkedin.com/in/kjordanov/) 表示。“耗时的部分是由各领域人类专家进行方法论上正确的标签标注，但我们目标是在未来几个月内发布相关成果。”

报告最后发表了一份声明，解释说这项工作的目的并不是为了创建一个排行榜。

其目的在于绘制分歧的结构图，即前沿评估小组在何处系统性地偏离人类共识、Lenz 在何处偏离两者、每个单独的模型和 Lenz 如何与相同的人类参考保持一致，以及哪些声明类别导致了每种分歧（评估标准模糊性、时间框架、领域专业化、校准漂移）。