Anthropic 和 SpaceX 本周达成了一项新的合作伙伴关系，使 Anthropic 能够访问这家航天公司的 Colossus 1 数据中心的计算能力。

随着 Anthropic 与 Elon Musk 的航天公司握手言和，它将增加其计算能力，并且毫无疑问，希望摆脱最近来自用户的抱怨，这些用户表示他们达到使用限制的速度远快于预期。

Colossus 1 位于田纳西州孟菲斯，拥有超过 220,000 枚 Nvidia GPU（包括 H100、H200 和下一代 GB200 加速器），正如 SpaceX [称之为](https://x.ai/news/anthropic-compute-partnership)的那样，它是“世界上规模最大、部署最快的 AI 超级计算机之一”，为“AI 训练、微调推理和高性能计算工作负载提供规模化支持”。

这家 AI 公司将利用其新的计算据点做些什么？

正如其发布的[博客文章](https://www.anthropic.com/news/higher-limits-spacex)中所述，Anthropic 将通过 Colossus 1 获得超过 300 兆瓦的计算能力，并计划将其用于“直接提高 Claude Pro 和 Claude Max 订阅者的容量”。

具体而言，这意味着三件事。

首先，Anthropic 将 Pro、Max、Team 和按席位付费的 Enterprise 计划中 Claude Code 的五小时速率限制提高了一倍。它还取消了针对 Pro 和 Max 用户的峰值时段限制缩减。

此外，Claude Opus 模型的 API 速率也得到了提高。例如，对于 Tier 1 用户，每分钟最大输入 token 数从 30,000 跃升至 500,000，而每分钟最大输出 token 数从 8,000 增加到 80,000。

> “这种转变将工作流程从谨慎的提示词预算转向更深入的推理、更大的任务和更完整的工程输出。”

koderAI 的创始人 [Elmer Morales](https://www.linkedin.com/in/elmerm/) 告诉 *The New Stack*，限制的变化对开发人员的工作流程可能意味着什么：“这种转变将工作流程从谨慎的提示词预算转向更深入的推理、更大的任务和更完整的工程输出，”Morales 说道。

VAST Data 的现场首席技术官 [Andy Pernsteiner](https://www.linkedin.com/in/andypernsteiner/) 表达了类似的观点，他告诉 *The New Stack*，Anthropic 的交易可能会使开发人员“能够使用 Claude Code 构建更丰富的应用程序和更高级的智能体”，希望能让他们从“细致地维护上下文和减少 MPC 使用”的需求中解脱出来——他说，这些瓶颈已成为他日常工作流程中令人遗憾的一部分。

## Anthropic 知道必须做出改变

在 [Claude Code 用户表示其达到使用限制的速度快于预期](https://thenewstack.io/claude-code-usage-limits/)之后，Anthropic 与 SpaceX 签署了协议。例如，一位 Reddit 用户声称，单次提示就消耗了他们 10% 的限额，而预期仅为 0.5-1%。

在宣布合作伙伴关系的博客文章中，Anthropic 还指出，它“在各种 AI 硬件上训练和运行 Claude”，并列举了 AWS Trainium、Google TPU 和 Nvidia，并指出它“继续探索在线引入额外容量的机会”。

在过去的几个月里，Anthropic 一直在进行计算资源的大采购，与大型科技巨头圆桌会议的许多成员握手，以确保新的容量和投资。

4 月，Anthropic 和 Amazon 宣布了一项[协议](https://thenewstack.io/anthropic-amazon-aws-investment/)，根据该协议，Anthropic 获得了高达 5 吉瓦 (GW) 的 Amazon Trainium 和 Graviton 核心，以及来自这家电子商务公司高达 250 亿美元的投资。

同月早些时候，Anthropic 还与 Google 和 Broadcom 达成[交易](https://www.anthropic.com/news/google-broadcom-partnership-compute)，计划从 2027 年开始扩建其计算基础设施，拥有“数吉瓦的下一代容量”——在此之前，它已在 2025 年 10 月[扩大](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services)了对 Google Cloud 技术（包括多达 100 万个 TPU）的使用。

别忘了 2025 年 11 月 Anthropic 与 Microsoft 和 Nvidia 建立的[合作伙伴关系](https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships)，在这项合作中，这家 AI 公司同意购买价值 300 亿美元的 Azure 计算容量。

## 这一切对软件开发人员意味着什么？

Anthropic、Amazon、Microsoft 以及其他 AI 巨头之间看似永无止境的握手，让人很难对行业的未来下注。但 Morales 和 Andy Pernsteiner 都认为 Anthropic 最近的支出狂潮是一个信号，表明这家 AI 公司正在为持续增长和长期影响力做准备。

> “这是对确保其平台以及工具、应用程序和框架生态系统拥有足够动力进行规模化运行的重新承诺。”

即使在今年早些时候 Anthropic 与五角大楼发生[纠纷](https://thenewstack.io/pentagon-anthropic-model-orchestration/)之后，Andy Pernsteiner 表示，开发人员应该将这次新的 SpaceX 交易视为一个信号，表明这家 AI 公司是他们可以继续押注的公司：

“这是对确保其平台以及工具、应用程序和框架生态系统拥有足够动力进行规模化运行的重新承诺。”