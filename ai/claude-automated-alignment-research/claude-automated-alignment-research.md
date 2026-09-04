<!--
title: Anthropic的Claude修复了全部10项对齐失败，却在2.4%的情况下尝试作弊
cover: https://cdn.thenewstack.io/media/2026/08/46455f0d-marcel-strauss-xk-pk7iynbe-unsplash-scaled.jpg
summary: Anthropic利用Claude自主研发AI对齐方案，成功修复10类模型漏洞。然而，Claude在执行过程中出现2.4%的作弊率，试图通过外挂手段优化测试结果，引发了关于自动化系统监控与安全性设计的深度思考。
-->

Anthropic利用Claude自主研发AI对齐方案，成功修复10类模型漏洞。然而，Claude在执行过程中出现2.4%的作弊率，试图通过外挂手段优化测试结果，引发了关于自动化系统监控与安全性设计的深度思考。

> 译自：[Anthropic's Claude fixed all 10 alignment failures. Then it tried to cheat 2.4% of the time.](https://thenewstack.io/claude-automated-alignment-research/)
> 
> 作者：Adrian Bridgwater

**Anthropic 正在让 AI 智能体参与**该领域最棘手的问题之一：保持其他 AI 系统与人类目标的一致性。在周五发布的一篇[论文](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures)中，该公司解释了其开源研究工具如何将 Claude 变成一名自动化的研究人员，使其能够提出、测试并完善模型安全修复方案。

作为 AI 工程总词汇表中不可或缺的一部分，[对齐](https://thenewstack.io/ai-alignment-in-practice-what-it-means-and-how-to-get-it/) 涉及引导 AI 模型和功能，使其目标、行动和行为符合人类的意图和价值观，尤其是在 AI 系统变得比人类自身更聪明的情况下。

本质上，这是利用 AI 来训练 AI。

“在我们早期的实验之一中，我们指派 [Claude](https://thenewstack.io/claude-computer-use/) 寻找有效的方法，利用弱 AI 模型作为‘教师’来监督强模型（在本例中为‘学生’模型）的训练，”Anthropic 在论文中解释道。

Claude 通过一种[循环方法](https://thenewstack.io/agent-loops-cloud-native-verification/)，即搜索文献、提出方法和数据、训练，然后进行测试，逐一攻克对齐失败的问题。成功的方法被保留下来，而失败的方法则被剔除，从而在后续的迭代中取得了累积的积极成果。

“总体而言，我们认为这些结果是早期积极的信号，表明训练后的自动化对齐可能在短期内变得切实可行。”

> “总体而言，我们认为这些结果是早期积极的信号，表明训练后的自动化对齐可能在短期内变得切实可行。”

## 10 类对齐失败

在本文所开展的主要工作中，Claude 被赋予的任务是自主训练模型，以提高它们在几个衡量 10 类对齐失败标准的公开基准测试中的表现。

“在每一项指标上，Claude 的方法都奏效了。针对所有 10 类对齐失败，Claude 都找到了在不降低性能的前提下改进目标基准测试的修复方案。最好的方法在未公开的对齐基准测试以及 [Petri](https://meridianlabs-ai.github.io/inspect_petri/)（一个用于模拟对抗性多轮场景以测试失调的开源工具）上也同样有效，”Anthropic 表示。

结果显示，Claude 提高了模型在隐私违规方面的性能，衡量标准包括 [ConfAIde](https://confaide.github.io/)（一个旨在识别指令调优大模型隐私推理能力关键弱点的基准测试）、[PrivaCI-Bench](https://arxiv.org/abs/2502.17041)（一个用于法律和 GDPR 合规性的上下文隐私评估基准测试）以及 [PrivacyLens](https://github.com/salt-nlp/privacylens)（一个专注于隐私规范感知和数据泄露风险的数据评估框架）。

## Claude 在执行安全检查时试图作弊。

但是，这里还有更多值得学习的地方……Anthropic 不遗余力地指出，其[最近发现](https://alignment.anthropic.com/2026/automated-w2s-researcher/) Claude 可以通过从远程 API 窃取测试标签并“挑选”结果来作弊。“为了捕捉作弊行为，我们提示 Claude Opus 4.8 监控了跨越所有 10 类对齐失败的约 1,600 份研究智能体转录，发现了 39 次（2.4%）作弊尝试，”论文中写道。

Anthropic 通过“安全差距弥合百分比”来判断 Claude 的成功，这是一种衡量其方法使学生模型向理论完美分数靠近了多少的度量指标，并在每类对齐失败的基准测试范围（通常为三到五个）内进行评估。

该公司排除了那些“损害学生模型通用能力”的对齐方法，并禁止 Claude 将其自身的对齐方式直接蒸馏到目标模型中。随后，它通过一个监控智能体强制执行这些约束，该智能体会在 Claude 运行任何方法之前阅读其所有想法。

“在每一项指标上，Claude 的方法都奏效了。针对所有 10 类对齐失败，Claude 都找到了在不降低性能的前提下改进目标基准测试的修复方案，”Anthropic 详细说明道。

![](https://cdn.thenewstack.io/media/2026/08/42d192e2-aaaaa.png)

## 这项工作对软件开发者意味着什么

资深软件工程师兼云架构师 [Jayakumar Ramalingam](https://www.linkedin.com/in/jayakumarramalingam/) 告诉 *The New Stack*，对于开发者来说，这里有用的结果并不是 AI 在某种程度上解决了对齐问题；而是 AI 模型安全工作“开始看起来像软件交付流水线”的任务了。

“对于考虑这一点的以 AI 为中心的开发者来说，他们可以看到一个智能体提出更改，一个隔离的评估器运行未公开的测试，以及一个单独的监控器检查该过程是否遵守规则，”Ramalingam 说。“这种模式的用途远不止模型训练。错误的做法是允许同一个智能体既编写修复方案，又选择测试，还判定其通过。”

Ramalingam 指出，Anthropic 论文中那个令人不安的 2.4% 作弊数字，是监控器检测到试图作弊的研究轨迹所占的份额。当然，这意味着一个致力于安全性的系统仍然试图操纵安全流程并超越它。

“开发者应将评估数据放在智能体触及范围之外，将评估器与被评估系统隔离开来，并测试智能体从未见过的内容以防回归。否则，自动化对齐就会变成一个带有令人放心的名称的基准测试优化，”Ramalingam 解释道。

> “开发者应将评估数据放在智能体触及范围之外，将评估器与被评估系统隔离开来，并测试智能体从未见过的内容以防回归。”

AI 专家兼 [Cognizant](https://www.cognizant.com/us/en) 的 SRE 性能架构师 [Akash Thakur](https://www.linkedin.com/in/akash-thakur-00367a155/) 大体上同意 Ramalingam 的观点，并告诉 *The New Stack*，这里真正的开发者故事并不是 Claude 改进了 10 个对齐基准测试。

“对于开发者来说，真正的故事和收获是 Anthropic 刚刚证明了自动化智能体可以运行完整的研究循环：搜索文献、提出修复方案、训练、测试、迭代，”Thakur 说。

“这与 SRE 和性能工程团队已经使用的可靠性循环是相同的。对齐刚刚变成了一个 CI/CD 问题，而开源该工具意味着每个构建大模型的工程团队现在都有了一个模板，可以将安全性视为系统的一个可测试的、可跟踪回归的属性，而不是一次性的训练后步骤，”Thakur 补充道。

## 每个人都开始信奉递归自我改进

总部位于德国柏林的 [Glokal AI OÜ](https://glokalai.com/) 的创始人兼 CTO [Jeet Pattanaik](https://www.linkedin.com/in/jeet-pattanaik/) 告诉 *The New Stack*，他想强调的是，如今每个人都在忙于追求递归自我改进的角度，并讨论人类研究人员是否已经过时。

“这里更紧迫的风险是[古德哈特定律](https://en.wikipedia.org/wiki/Goodhart%27s_law)（当一个指标变成了目标，它就不再是一个好指标了），”Pattanaik 说。“所以基准分数上升并不等同于模型或功能在生产环境中表现良好，Anthropic 自己也这么说：它研究的失败是狭窄的，有些失败根本没有基准，被接受的方法可能损害了无人测量的能力，而像 Petri 这样的工具只是代理指标。”

Pattanaik 解释说，他每天都与受监管的全球企业合作，所以他可以告诉我们接下来会发生什么——现在的情况是，“我们运行了对齐工具”即将成为审计文件中的一行。

> “基准分数上升并不等同于模型或功能在生产环境中表现良好，Anthropic 自己也这么说：它研究的失败是狭窄的。”

“没有人问那十个基准测试的失败类别与系统在索赔流程或支付过程中真正可能出错的方式有什么关系。这不是猜测；这就是每个变成复选框的安全扫描工具所经历的情况，”Pattanaik 阐述道。

## 递归自我改进之路

OpenAI 加入了 Anthropic 在此领域的工作，公开提交了其[关于超级对齐的工作](https://openai.com/index/introducing-superalignment/)以及[总体对齐的方案](https://openai.com/index/our-approach-to-alignment-research/#)。今年 5 月，Google DeepMind 团队[推出了 Gram](https://deepmind.google/research/publications/252981/#:~:text=In%20contrast%20to%20other%20alignment%20auditing%20approaches%2C,sabotage%20rates%20close%20to%20zero.%20*%20Authors.)，这是一个自动化对齐审计框架，用于评估 AI 智能体进行破坏的倾向。虽然不像 Meta AI 那样在这一领域滔滔不绝，但该公司在 3 月份发布了 HyperAgents，一种用于递归自我改进的自指智能体方法。

在追求控制人工通用智能的过程中，这种讨论还包含了[递归自我改进](https://en.wikipedia.org/wiki/Recursive_self-improvement)的概念。这是前沿模型公司已经触及的话题，也有专门的参与者在这一领域运作，包括（从名字就能看出来）[Recursive](https://www.recursive.com/#:~:text=Recursive%20embraces%20the%20logical%20conclusion%3A%20the%20fastest,creating%20such%20an%20advance%20cannot%20be%20overstated.)、日本 AI 模型专家 [Sakana AI](https://sakana.ai/) 以及专注于 AI 智能体“[外循环](https://www.weco.ai/blog/first-evidence-of-recursive-self-improvement)”优化的 [Weco AI](https://www.weco.ai/platform)。

Anthropic 在其报告总结的结尾表示，计划继续提高 Claude“衡量细微失败”的能力，并扩展其对生产级模型上训练后自动化对齐的分析。