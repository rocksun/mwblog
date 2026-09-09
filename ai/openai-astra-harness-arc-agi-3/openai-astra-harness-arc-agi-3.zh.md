投资人 Matt Turck 的[精彩播客](https://www.mattturck.com/podcast)曾邀请过 [ARC-AGI](https://arxiv.org/pdf/2603.24621) 的开发者们，他用三个词总结了 Astra 的重磅跑分：“[太疯狂了](https://x.com/mattturck/status/2095653093148885274?s=20)。”随后，他在括号里又补了四个词：“带着它的原生 harness。”

[ARC Prize 用自己的标准 harness 对 GPT-6 Astra 进行了测试](https://arcprize.org/blog/astra)，该模型的得分为 62.7%。当使用 OpenAI 的 Provider Adapter 进行运行时，同样的模型在相同的推理设置下得分达到了 98.6%。模型本身没有变，但其周边的软件变了，这为得分贡献了 36 分。而且，性能更好的系统成本更低：使用 OpenAI 的适配器为 17,332 美元，而使用 ARC Prize 的则为 26,098 美元。

这就是为什么 harness 工程正变得与模型选择同等重要。围绕模型的软件既能改变其最终成果，也能改变其成本。

## 基准测试衡量的是系统，而非模型

ARC-AGI 的构建初衷就是为了抵御那种消耗了许多其他基准测试的暴力扩展。ARC-AGI-3 今年通过将模型放入交互环境（没有说明、没有既定目标、也没有既定规则）再次提高了门槛，并根据其学习操作的效率进行评分。当 [ARC Prize 今年发布该测试时](https://arcprize.org/blog/arc-agi-3-launch)，人类得分为 100%。前沿 AI 的得分为 0.51%。

周四，[Amanda Caswell 报道了 OpenAI 在 ARC-AGI-3 基准测试中不断提高的分数](https://thenewstack.io/astra-arc-agi-benchmark/)。正如她所指出的，Astra 在与竞争模型不同的设置下运行。ARC Prize 对这些设置的具体作用有明确定义。其标准 harness 允许模型保留它选择保存的笔记。而 OpenAI 的适配器则在请求之间保留了不透明的推理状态，并压缩了较长的对话，因此模型可以恢复自己的思考，而不是重新构建。

ARC Prize 公布了每个推理层级的数据。

同样的模型，两种 harness

GPT-6 Astra 在 ARC-AGI-3 上的表现，按推理努力程度划分。在每一项设置中，在 OpenAI Provider Adapter 内部运行的跑分都高于 ARC Prize 标准 harness 内部的同一模型，且成本更低。

| 推理努力程度 | ARC Prize 标准 harness | OpenAI Provider Adapter |
| --- | --- | --- |
| 最大 | 62.7% / $26,098 | 98.6% / $17,332 |
| 超高 | 59.3% / $37,317 | 98.4% / $18,147 |
| 高 | 54.8% / $40,705 | 99.9% / $18,817 |
| 中 | 38.6% / $48,090 | 98.4% / $19,285 |
| 低 | 17.5% / $38,166 | 98.0% / $21,298 |
| 无 | 35.2% / $49,791 | 96.7% / $23,457 |

Astra 在 OpenAI 的 harness 内部，在没有任何推理努力的情况下，以 23,457 美元的成本取得了 96.7% 的分数。同样的模型在 ARC Prize 的标准 harness 内部以最大推理努力运行，得分为 62.7%，成本为 26,098 美元。harness 的表现直接压倒了推理调节器。几个月来我一直主张 [harness 至关重要](https://thenewstack.io/cursor-sdk-harness/)。但我没想到结果会如此悬殊。

分数并非唯一的差距。在两个 harness 都解决了的 167 个游戏推理对中，ARC Prize 记录显示，Provider Adapter 运行时的 Token 消耗减少了 49%，速度快了约 3.66 倍。

OpenAI 并没有隐瞒细节：适配器运行在任何人都可以调用的文档化 Responses API 功能之上。你无法购买的是那套拿下 98.6 分的整合系统。

这也是为什么 OpenAI 总裁 Greg Brockman 本周在新闻发布会上所说的——“我认为感觉我们现在处于 AGI 时代并不不合理”——比预期产生的影响力更大。Brockman 描述的是由特定系统产生的基准测试结果，而不是确定底层模型就是 AGI。[Frederic Lardinois 为 *The New Stack* 撰写的发布报道](https://thenewstack.io/openai-gpt6-astra-benchmarks/)准确地指出了这一点：这种表述远超出了现有证据所能确立的范围。也许我们确实处在 AGI 时代，但这个基准测试并不能证明这一点。

## Harness 正在成为产品

在编码方面，前沿模型现在在几分之内扎堆。*Artificial Analysis* [通过在 harness 内运行每个模型而不是单独运行来衡量其编码代理指数](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra)：Astra 在 Codex 中得分为 67，Opus 5 和 Fable 5 在 Claude Code 中得分大致相同，Muse Spark 1.3 在 Muse Code 中也与之并列，而 Fable 5.1 在 Claude Code 中以 70 分领先。被测量的单位已经是两者组成的组合。

实验室已经弄明白了这一点。早在四月，[Janakiram MSV 就记录了这种四方分歧](https://thenewstack.io/ai-agent-harness-pricing-split/)：Anthropic、OpenAI、Google 和 Microsoft 都将 harness 视为一种销售产品，唯一的区别在于如何定价。Anthropic 除了 Token 费用外，还按每会话小时 0.08 美元计量托管代理。OpenAI 免费提供了其代理 SDK，没有任何运行费用。Google 和 Microsoft 则将会话、内存、代码执行和可观测性作为单独的项目进行计费。

没人再把 harness 当作模型的免费配件了。

其他公司也在朝这个方向发展。据 [Paul Sawers 为 TNS 的报道](https://thenewstack.io/stripe-acquires-openrouter-tokens/)，Stripe 在八月以 80 亿美元收购了 OpenRouter，这是一个每天为 1000 万开发人员在 400 多个模型之间路由 10 万亿 Token 的网关。Patrick Collison 的框架是，Token 是使用 AI 构建的公司所使用的核心货币。Stripe 买下的是位于模型前端的路由层。Nvidia 也构建了自己的 harness。

我们在两周前就报道过这一证据。[Adrian Bridgwater 报道称](https://thenewstack.io/nvidia-avo-arcagi3-benchmark/)，Claude Opus 5 在 ARC-AGI-3 公共数据集上单独运行得分为 30.2%。在 Nvidia 的 AVO 中，它获得了持久内存和程序化监督，能够在进度停滞时介入，最终完成了全部 25 个环境中的 183 个关卡。那次测试并非 ARC Prize 在 Astra 上运行的那种干净的 A/B 测试。Nvidia 同时改变了内存、监督和上下文管理。变动的变量不止一个。

Nvidia 在[此处](https://developer.nvidia.com/blog/nvidia-avo-reaches-100-on-arc-agi-3-demonstrating-a-frontier-level-general-purpose-architecture-for-long-horizon-autonomous-agents/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)对此做了精彩描述：“模型能力固然重要，但周边系统决定了这种能力能多有效地转化为持续的自主进步。”

## Harness 工程就是工作本身

[Janakiram MSV 发现](https://thenewstack.io/agent-harness-token-costs/)，Aider、Claude Code 和 OpenClaw 在运行相同模型时，Token 使用量差异高达 70 倍。缓存命中率根据服务路径的不同，从约 70% 波动到 1.5%。没有哪种模型选择能解释这种差异。

工作本身相当普通。决定代理记住什么、忘记什么；决定它被允许接触什么，以及何时需要停下来征求人工意见。[Jeremy Daly 在我们网站上的文章](https://thenewstack.io/building-ai-agent-harness/)是包含工程细节的版本，如果你是构建者，一定要读读这篇文章。

我曾在六月主张[模型分流是值得招聘的技能](https://thenewstack.io/claude-fable-cost-model-triage/)。但我现在要修正这个观点。选择模型只是简单的一半，而且随着前沿技术的收敛，这个过程每季度都会变得更容易。一年后，我认为运行代理的人，每周花在选择模型上的时间会减少，而花在构建模型周边系统上的时间会更多。