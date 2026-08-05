**DeepSeek 推出了 DeepSeek-V4-Flash-0731**，在不改变模型核心架构的情况下，实现了智能体（agent）性能的显著提升。

继上周发布公告后，该公司已通过 DeepSeek API 将此更新作为公测版提供，并于当天晚些时候在 Hugging Face 上以 MIT 许可证发布了[开放权重](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)。

尽管模型本身没有改变，但 DeepSeek 表示，额外的后训练（post-training）是性能提升的关键，这表明有意义的改进并不总是需要更大的模型。

DeepSeek 决定在宽松的许可证下发布生产就绪的权重，这使得组织在部署和自定义模型时拥有了更大的自主权。

> 尽管模型本身没有改变，但 DeepSeek 表示，额外的后训练是性能提升的关键，这表明有意义的改进并不总是需要更大的模型。

## 架构不变，效果更好

DeepSeek 表示，V4-Flash-0731 使用与预览版相同的架构，总参数量为 2840 亿，每个 token 激活参数为 130 亿。

这比总参数 1.6 万亿、激活参数 490 亿的 V4-Pro 小得多。对于大规模运行智能体的公司来说，激活参数的差距直接转化为推理成本——[尽管仅看模型价格并不能反映全貌](https://thenewstack.io/agentic-ai-token-costs/)。

> 尽管它仍然是较小的模型，但 DeepSeek 表示，更新后的 Flash 版本现在在多个侧重智能体的基准测试中击败了早期的 V4-Pro 预览版。

尽管它仍然是较小的模型，但 DeepSeek 表示，更新后的 Flash 版本现在在多个侧重智能体的基准测试中击败了早期的 V4-Pro 预览版。

该公司报告其在 Terminal-Bench 2.1 上的得分为 82.7，在 DeepSWE 上为 54.4，在 Toolathlon-Verified 上为 70.3。

## 基准测试结果受审视

[Artificial Analysis](https://artificialanalysis.ai/articles/deepseek-v4-flash-0731-scores-50-on-the-artificial-analysis-intelligence-index-10-points-above-previous-deepseek-v4-flash) 的早期独立测试得出的 Terminal-Bench 2.1 分数较低，为 79%，这表明 DeepSeek 报告的数据并不总是与独立测试结果一致。

DeepSeek 还分享了一些内部测试结果，尽管这些结果尚未经过独立验证。如果这些结果成立，它们将进一步证明企业可以通过后训练从现有模型中获得更多性能，而不必仅仅通过增加模型规模来实现。

## 开放权重，完全掌控

MIT 许可证意味着组织不必仅通过 DeepSeek 的托管 API 使用模型。此次发布增加了开放权重模型缩小与[专有模型替代方案](https://thenewstack.io/open-weight-models-frontier-costs/)之间差距的趋势。这种灵活性与许多开发者已经使用的工具支持相结合。V4-Flash 现在支持用于构建 AI 智能体和多步工作流的 Responses API，并且 DeepSeek 已经发布了将模型集成到 [基于 Codex 的开发工作流](https://api-docs.deepseek.com/updates/)中的说明。

## 熟悉的 API，更低的切换成本

对于已经使用 OpenAI 风格 API 的团队来说，这降低了尝试其他模型的门槛，因为他们无需对现有设置进行重大更改即可对其进行评估。

[V4 技术报告](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)还涵盖了推理方面的改进，例如使用 DeepSeek 的 [DSpark 框架](https://www.techtimes.com/articles/319236/20260628/deepseek-releases-dspark-speculative-decoding-makes-v4-85-percent-faster.htm)进行推测解码（speculative decoding），旨在使服务更高效。当与自托管部署相结合时，这些功能为基础设施团队提供了更多根据自身生产需求调整性能的方法。

此次发布反映出，企业现在正在寻找提高模型效能的新方法，而无需扩大模型规模，并且它们正在模型交付方式上展开竞争。虽然许多 AI 供应商专注于托管 API，但 DeepSeek 继续发布可下载的权重，组织可以在自己的基础设施上运行。对熟悉 API 格式的支持也使团队更容易测试开放权重模型，而无需彻底改变当前的工作流。

> 企业正在寻找提高模型效能的新方法，而无需扩大模型规模，并且它们在模型交付方式上的竞争也日益激烈。