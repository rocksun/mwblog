# Amazon CEO predicts 6 to 8 AI models will be ‘good enough’ for almost everything

亚马逊CEO Andy Jassy 预计，前沿 AI 模型竞赛将催生出多个极具竞争力的模型，而不是单一的赢家。他在周四的亚马逊 2026 年第三季度财报电话会议上对分析师表示，未来的挑战将是在众多模型中进行选择，而不是死守某一个模型。

> “6-8 个模型在性能上不相上下，或者至少足以应对 95% 以上的工作负载。”

在[这次电话会议](https://stockanalysis.com/stocks/amzn/transcripts/720308-q3-2026/)中，[Jassy](https://www.linkedin.com/in/andy-jassy-8b1615/) 回答了高盛分析师 [Eric Sheridan](https://www.linkedin.com/in/eric-sheridan-b2866736/) 关于[亚马逊 Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) 市场机遇的问题，他预测在两到三年内将出现“6-8 个模型，它们的水平不相上下，或者至少足以满足 95% 以上的工作负载。”

## 没有唯一的 AI 赢家

在过去的 20 年里，Jassy 见证了许多技术领袖失去其早期的领先优势。他以数据库和分析技术为例，还有 TensorFlow，它曾一度有望成为标准框架，但在 PyTorch 占据主导地位之前失势。

他预计 AI 模型领域也会发生类似的事情。正如 Jassy 所说，“没有一个工具能统治世界。”某些模型在推理或编程方面表现更好，而另一些模型在视觉任务、速度或 [Token 成本](https://thenewstack.io/minimax-flash-agent-costs/)方面具有优势。这使得企业有充足的理由使用多个模型。Jassy 相信，“大多数客户都将使用多个模型，并且许多客户会在同一个生成式 AI 应用中使用多个模型。”对于开发者而言，这意味着可以根据当前的任务选择合适的模型，而不必将所有东西都绑定在单一供应商身上。

> “大多数客户都将使用多个模型，并且许多客户会在同一个生成式 AI 应用中使用多个模型。”

## 一个 API，众多模型

这一论点实际上描述了 Bedrock 的构建方式，因为该服务通过一个 API 连接了来自 Anthropic、OpenAI、Meta、Mistral、DeepSeek、Moonshot AI 和 xAI 等提供商的 100 多个基础模型，使团队能够调用 Claude、GPT、Llama 或更小的专有模型，而无需为每个模型单独搭建管道。

亚马逊[最近将 OpenAI 的模型](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-cross-region-openai-v2/)引入该服务，与它已经托管的闭源模型并驾齐驱。Jassy 表示，此后它还添加了诸如 Moonshot 的 Kimi 和智谱 GLM 等开源模型的托管版本，这是 Bedrock 将继续满足对西方开源模型渴望的一部分。

## 切换模型并非没有代价

Bedrock 的[Converse API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) 为开发者提供了一种通用方法来处理来自不同提供商的模型，而无需每次都重写集成。但切换并非总是那么简单。模型的上下文限制、工具能力和支持的功能各不相同，因此开发者仍然需要测试其应用程序的行为。

当团队围绕特定供应商的[智能体工具链](https://thenewstack.io/microsoft-copilot-harness-foundry/)构建其工作流时，事情可能会变得更加复杂。Jassy 表示，当应用程序的不同限制要求他们进行切换时，客户希望能够“在它们相互超越时来回切换”。

安全性也是这一决策的考量因素。根据 [AWS](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html) 的说法，Bedrock 不会向模型提供商授予访问客户提示词或响应的权限，这些信息也不会用于训练底层模型。Jassy 将这些保护措施视为企业选择该服务的又一个原因。

## 为什么亚马逊最终会赢

这一预测背后的策略是，只要亚马逊拥有开发者挑选模型的聚集地，它就不需要发布最好的模型。谷歌的 Vertex AI 和微软的 Azure AI Foundry 也在争夺这一地位，它们提供着大致相同的多供应商目录和统一访问权限。

一个由六到八个模型不断轮流领先、团队[在它们之间频繁切换](https://thenewstack.io/anthropic-s1-models-revenue/)的市场，正是中立访问层能够实现商业化变现的市场。Jassy 毫不掩饰 Bedrock 是预期的受益者这一事实，他称这个机遇“巨大”，并暗示它可能会发展成为一个“规模堪比 EC2”的服务，而 EC2 至今仍是 AWS 最大的业务之一。

早期的数字为这一观点提供了一些分量：财富 500 强企业现在对 Bedrock 的年支出同比增加了近 7 倍，Token 量增长了近 17 倍。据 Jassy 介绍，该服务正成为 AWS 历史上增长最快的数十亿美元产品。

这一切都伴随着 AWS 的重新加速而到来，该业务部门在本季度增长了 39.3%，达到 46 亿美元，年化运行率达到 184 亿美元。Jassy 指出，绝大多数 Bedrock 流量已经在亚马逊自己的 Trainium 芯片上运行，这使得公司能够在保持利润率的同时压低价格。

> Jassy 指出，绝大多数 Bedrock 流量已经在亚马逊自己的 Trainium 芯片上运行，这使得公司能够在保持利润率的同时压低价格。

[AI 工程师
2026 年成为 AI 工程师的分步指南

引言
使用大语言模型
上下文工程
AI 模型
嵌入与向量数据库
嵌入模型
RAG
AI 智能体
AI 安全与伦理
评估与可观测性](https://roadmap.sh/ai-engineer?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=jassy-bedrock-multimodel-prediction)