Anthropic [周四推出了 Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6)，这是其旗舰 Opus 模型的更新，在几乎所有基准测试中都比其前身以及许多竞争对手有了重大改进。

Opus 4.6 还增加了一些有用的新功能，包括一个一百万个 token 的上下文窗口，能够输出多达 128,000 个 token，以及 Claude 代码中的代理团队，可以并行处理任务。

定价与之前相同：每百万输入/输出 token 分别为 5 美元/25 美元。

## 企业用户的一大飞跃

该公司认为，Opus 4.6 在企业工作流程中使用大型语言模型（LLMs）方面是一大飞跃，因为它能够处理更复杂的任务并更快地交付结果。

正如 Anthropic 发言人告诉 *The New Stack* 的那样，“它在首次尝试时就比我们见过的任何模型都更接近生产就绪的质量——文档、电子表格和演示文稿将需要更少的反复迭代。”

Anthropic 指出，例如，Excel 中的 Claude 现在可以一次性处理运行时间更长、更复杂的任务和多步骤更改。

![](https://cdn.thenewstack.io/media/2026/02/fe13a206-claude-opus-4.6-in-powerpoint.png)

PowerPoint 中的 Claude Opus 4.6（图片来源：Anthropic）。

## 基准测试

按照 Anthropic 模型的传统，Opus 4.6 再次在编码基准测试中有所改进，但 SWE-bench 验证测试和用于测试工具使用的 [MCP Atlas 基准](https://scale.com/leaderboard/mcp_atlas) 除外，两者都显示出小幅退步。这有点异常，特别是考虑到该模型在检查终端中的代理编码（[Terminal Bench 2.0](https://www.tbench.ai/)）和代理工具使用（[t2-bench](https://github.com/sierra-research/tau2-bench)）的类似基准测试中表现出色。

在 Terminal Bench 上，Opus 4.6 的得分从 Opus 4.5 的 59.8% 上升到 65.4%，在 OSWorld 代理计算机使用基准测试中，其得分从 66.3% 上升到 72.7%。这使其现在领先于 OpenAI 的 GPT-5.2 和 Google 的 Gemini 3 Pro，并且根据 Anthropic 的说法，新模型在诊断更复杂的错误方面表现尤其出色。

![](https://cdn.thenewstack.io/media/2026/02/c9a89c1f-claude-opus-4.6-terminal-bench-benchmark-scaled.jpg)

Claude Opus 4.6 Terminal Bench 基准测试（图片来源：Anthropic）。

Anthropic 报告称，在各项基准测试中均取得了类似进展。然而，最突出的是其在 [ARC AGI 2](https://arcprize.org/arc-agi/2/) 基准测试中获得了 68.8% 的分数，该基准测试关注的不是在专业任务中达到博士级表现，而是解决对人类来说容易但对 AI 系统来说非常困难的问题。Opus 4.5 仅获得 37.6%，而 Gemini 3 Pro 获得 45.1%，GPT-5.2 获得 54.2%。

当然，基准测试只说明了部分情况，并不总是反映这些模型在实践中的工作方式。Anthropic 认为，在其内部使用中，Opus 4.6 即使没有明确指示，也处理了更具挑战性的任务，并且处理得更快，结果更好。

在安全评估中，Anthropic 发现 Opus 4.6 在欺骗、奉承和鼓励用户妄想等错位方面与 Opus 4.5 表现一致。

![](https://cdn.thenewstack.io/media/2026/02/842f80a7-claude-opus-4.6-all-benchmarks--897x1024.png)

## 更多功能

尽管版本号变化很小，但除了推理性能的改进之外，还有其他更新。例如，Opus 4.6 是 Opus 系列中第一个具有一百万个 token 上下文窗口的模型。

它也是第一个采用自适应思维的 Anthropic 模型，这使其能够考虑上下文线索来确定在提示中投入多少精力。开发人员仍然可以通过 `/effort` 参数对此进行更多控制，以在质量、推理速度和成本之间进行明确的权衡。然而，以前的选项只是启用或禁用扩展思维，所以现在这给了他们更多的控制。

对于 API 用户，Claude 现在可以使用压缩来总结上下文，使其能够处理运行时间更长的任务而不会达到其上下文限制。

此次更新也涉及数字主权。如果您的工作负载只能在美国运行，现在这是一个选项，但您将为此多支付 10%。更常见的是，我们看到公司为 *不能* 在美国运行的工作负载提供此选项。

## 代理团队

然而，对于开发人员来说，最有趣的新功能可能是代理团队。虽然开发人员已经找到了规避方法，但默认情况下，Claude Code 到目前为止一次只运行一个代理。现在，Anthropic 正在引入代理团队，允许开发人员将工作分配给多个代理。这些代理可以并行工作并自主协调他们的努力。

Anthropic 指出，这对于读取密集型工作特别有用，例如代码库审查。