韩国AI模型公司 [Upstage AI](https://www.upstage.ai/blog/en/solar-pro) 上周正式宣布推出其 [Solar Pro 4](https://www.upstage.ai/blog/en/solar-pro-4) 闭源商业大模型 (LLM)。该公司自2025年起在San Jose设立总部，旨在通过强大的 [代理行为可靠性](https://thenewstack.io/restack-gives-product-teams-the-reins-to-own-ai-agent-behavior/) 布局，切入AI软件工程市场。

## 我们如何定义代理的可靠性？

Upstage 不仅承诺其运营成本仅为美国前沿模型的一小部分，还将代理可靠性定义为一种能够稳定执行工作流的模型，该模型可以在多个步骤和阶段中一致地执行长上下文推理。

在这种语境下，可靠性还涵盖了文档理解和信息提取、模型遵循企业策略的能力，以及调用正确软件工具、子代理或 [数据集](https://thenewstack.io/5-useful-datasets-for-training-multimodal-ai-models/) 以完成特定任务，并以正确格式输出的能力。

Upstage AI 美国业务负责人 Kasey Roh 告诉 *The New Stack*，Upstage 构建的是模型界的“朴素商务西装”；这是一种能够完成核心业务职能的 AI 工蜂，不会产生与重试、输出格式错误和指令遵循失败相关的无效 token 浪费。

“将前沿模型留给前沿难题；我们构建的是一匹‘工作马’（workhorse），” Roh 说。“如果你正在生产环境中进行 AI 构建，你实际交付的大部分内容都是枯燥、重复的工作，比如文档提取、分流和一系列简单的决策。针对这些任务使用前沿模型不仅是大材小用，老实说也是一种负债：你支付着旗舰产品的价格和延迟，却只是为了运行同一项任务，且每天要运行数百万次。”

她指出，Solar Pro 4 旨在防止 token 浪费，其指令遵循能力“贯穿多轮对话”，工具调用结构保持完整，且代理能够按照指示、在公司政策范围内以及在任务的 [有效模式](https://thenewstack.io/json-schema-ai-reliability/) 边界内行事。

> “将前沿模型留给前沿难题；我们构建的是一匹‘工作马’。去问问任何真正在生产环境中运行代理的人，他们的要求从来不是‘让它更有创意’，而是‘让它足够可靠，以至于我不需要整天重新调整提示词并浪费 token’。”

“我们的‘工作马’穿着朴素的商务西装，正是为了让人类不必这么做。去问问任何真正在生产环境中运行代理的人，他们的要求从来不是‘让它更有创意’，而是‘让它足够可靠，以至于我不需要整天重新调整提示词并浪费 token’，” Roh 补充道。

## AI 开发者如何看待 Solar Pro 4？

在市场认知和采用率方面，Roh 表示，在 [上线 OpenRouter](https://openrouter.ai/upstage/solar-pro4#apps) 的一周内，Solar Pro 4 的 token 消耗量就超过了 3700 亿。

Solar Pro 4 还集成到了美国 [Nous Research](https://nousresearch.com/) 开发的 AI 代理 Hermes Agent 中，为多步骤、自我改进的 AI 代理提供动力。实际上，这意味着在某种程度上，Upstage 已与 [OpenAI](https://thenewstack.io/voice-ai-openai-anthropic/)、[Anthropic](https://thenewstack.io/anthropics-claude-security-beta/)、[Google](https://thenewstack.io/google-gemini-agent-platform/) 和 [Nvidia](https://thenewstack.io/palantir-nvidia-sovereign-ai/) 等齐名，成为模型提供商。该公司还与 AWS 和 AMD 建立了合作伙伴关系。

根据全球 [AI 评估机构 Artificial Analysis](https://artificialanalysis.ai/models/solar-pro4?models=solar-pro4)，Solar Pro 4 的综合性能得分为 42 分，与通用前沿模型相当。

根据 Roh 和其团队（至少以此为衡量标准）的说法，与 Solar Pro 3 相比，这已提升了三倍以上，并“超越了科技巨头模型”，如 Nvidia 的 Nemotron 3 Ultra（38 分）和 Google 的 Gemini 3.5 Flash-Light（37 分）。它还胜过了竞争对手的主权模型，如 [Mistral](https://thenewstack.io/mistral-vibe-cloud-agents/) Medium 3.5（30 分）和 [Cohere](https://thenewstack.io/cohere-sovereign-coding-model-north-mini-code/) Command A+（23 分）。

处理复杂长文档且不失败的能力意味着 Solar Pro 4 在长上下文理解基准（[AA-LCR](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning)）中获得了 71 分。该基准评估了从大量长文档中提取信息并根据该信息推断答案的能力，表现比上一版本优越 2.3 倍。

## 当长复杂推理失败时会发生什么？

Upstage 的核心业务是为金融服务、保险、制造和供应链等受监管的复杂行业提供服务，在这些行业中，模型必须在生产环境中表现出可预测性。但当长复杂推理失败时会发生什么？

“最经典的情况是长表格文档，” Roh 回忆道。“假设一张发票或技术规格说明书有数百页，包含数百个项目。”

她解释说，每一个代理工作流都是建立在从此类文档中准确提取信息的基础上的。在她举的例子中，模型处理第 1 到 200 行时表现良好，但在那之后开始“略读”：丢失行，或者通过模式匹配之前的行来悄悄填充单元格，而不是读取实际值。

“糟糕的是，输出看起来格式规范，所以直到最后阶段有人进行人工核对之前，没有人能发现。这种失败模式正是我们进行针对性训练的原因，” Roh 解释道。

> “（在长复杂推理失败中）糟糕的是，输出看起来格式规范，所以直到最后阶段有人进行人工核对之前，没有人能发现。这种失败模式正是我们进行针对性训练的原因。”

## 这里能节省多少成本？

Roh 明确表示，按标价计算，Solar Pro 4 的成本比“典型的文档工作流降低了约 90%”。

“例如，一个文档事实核查代理，输入多个文档，输出结构化报告，每个任务运行约 30 万输入/1.5 万输出 token：这在顶级前沿模型价格下大约是每个任务 1 美元，而在 Solar Pro 4 上只需 0.10 美元。每月 5 万个任务，5 万美元的账单变成了 5 千美元。而且在 9 月 10 日之前有 9 折发布优惠，所以现在你可以在前沿模型收费的几分之一成本下，运行整月的负载，” 她详细介绍道。

Solar Pro 4 的发布紧随 Upstage 发布其开发者开放生态系统 [Solar Open 2](https://www.linkedin.com/posts/upstageai_solaropen2-upstageai-solarllm-activity-7485853995350011904-c2lF/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAWx2KsBuQ0EY3EdQfRmgxKmjE9qbcllbdU) 之后。