谷歌周二发布了三款新的 Gemini 模型：Gemini 3.6 Flash、更便宜更快的 3.5 Flash-Lite，以及专为网络安全用例优化且性能通常优于 [Anthropic’s 4.6 Opus](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/) 模型的 3.5 Flash Cyber。

该阵容中明显缺失的是谷歌最新的旗舰模型 3.5 Pro，该模型已超过承诺发布日期数周。谷歌最初在 5 月的 I/O 大会上宣布了 3.5 Pro，并承诺在 6 月发布。谷歌表示，Pro 模型“目前正与合作伙伴进行测试”，并计划“一旦准备就绪”就广泛提供。

谷歌也从未停止前瞻，表示已开始 Gemini 4 的预训练工作。

## 3.6 Flash

我们大多数人都没有预料到在 Gemini 3.5 Pro 模型之前会看到 Gemini Flash 模型的更新，但事实确实如此。

好消息是，3.6 Flash 是对其前身的一次有意义的更新，而且价格稍微便宜了一些。每百万个输入 token 的价格保持在 1.50 美元，但谷歌将每百万个输出 token 的价格从 9 美元降至 7.50 美元。

> 我们大多数人都没有预料到在 Gemini 3.5 Pro 模型之前会看到 Gemini Flash 模型的更新，但事实确实如此。

谷歌还特别指出，3.6 Flash 在代理工作流中实现目标所需的推理步骤和工具调用更少，这也应使其运行更具成本效益。据 Artificial Analysis 称，它使用的 token 减少了 17%。

## 3.6 Flash 基准测试

在大多数基准测试中，3.6 Flash 轻松超越了其前身，尤其是在编码方面。例如，在新的 [DeepSWE 软件工程基准测试](https://deepswe.datacurve.ai)中，3.6 Flash 得分为 49%，而 [3.5 Flash](https://thenewstack.io/googles-gemini-3-5-flash-beats-the-frontier-models/) 为 37%。不过，这并不是最好的结果。[Anthropic 的 Claude Sonnet 5](https://thenewstack.io/claude-sonnet-5-launch/) 在此项测试中达到了 54%，而顶尖的前沿模型得分超过 70%。

该团队还在 MLE Bench 机器学习研究基准（63.9% 对 49.7%）和 [OSWorld-Verified](https://benchlm.ai/benchmarks/osWorldVerified) 计算机使用测试（83% 对 78.4%）中看到了巨大的收益。大多数现代模型在此范围内的得分相似，对于像 3.6 Flash 这样的中端模型来说，这实际上令人印象深刻。相比之下，Claude Fable 的得分仅稍好一些，为 85%。

![](https://cdn.thenewstack.io/media/2026/07/830ad80f-screenshot-2026-07-21-at-8.32.12-am-1024x548.png)

来源：Google。

在知识工作方面，3.6 Flash 在 [GDPval-AA v2](https://artificialanalysis.ai/evaluations/gdpval-aa) 上达到 1421 分，远好于 3.5 Flash 的 1349 分，但就目前而言，这仍远低于其他前沿实验室的中端模型，如 Anthropic 的 Claude Sonnet 5（1600 分）和 Open 的 GPT-5.6 Terra（1581 分）。

当然，需要记住的一点是，谷歌也在价格上展开竞争，但即使在那里，情况也很复杂。例如，3.6 Flash 的性能并不总是优于 [GPT 5.6 Luna](https://thenewstack.io/openai-gpt-56-live/)，后者的价格为每百万输入/输出 token 1 美元/6 美元（但仅在上下文窗口小于 272,000 个 token 时有效）。Anthropic 的 Sonnet 5 在 8 月底前也提供 2 美元/10 美元的入门价格。

## 3.6 Flash 和 3.5 Flash-Lite 的可用性

3.6 Flash 和 3.5 Flash-Lite 现在可通过 Google AI Studio 和 Android Studio 在 Gemini API 中使用，而 3.6 Flash 也可在 [Google 的 Antigravity 氛围编程工具](https://thenewstack.io/hands-on-with-antigravity-googles-newest-ai-coding-experiment/)中使用，并供 Gemini Enterprise Agent Platform（以前称为 Vertex AI）中的企业用户使用。

对于消费者，3.5 Flash-Lite 即将进入 Google 搜索。

## 3.5 Flash-Lite

3.5 Flash-Lite 是谷歌最新的低端模型。鉴于最近的“轻量级”版本 3.1 Flash Lite 已经发布[近半年之久](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/)，3.5 Flash 全面改进也就不足为奇了。但它的价格也略贵了一些，每百万输入/输出 token 为 0.3 美元/2.5 美元（之前为 0.25 美元/1.5 美元）。

在基准测试方面，它不会打破任何记录，但这也不是该模型的目的。它旨在用于高吞吐量任务，如代理搜索和文档处理，而不是推理和规划代理工作负载的关键任务。

话虽如此，它确实比 3.1 Flash Lite 好得多。在 GDPval-AA v2 上，它的得分为 1140，而之前的轻量级模型为 642。SWE-Bench Pro 的数字从 49.6% 上升到 54.2%，在 OSWorld-Verified 上，它现在达到 74%。

对于许多公司来说，它将成为延迟敏感型工作负载的理想选择，正如 Ramp 的应用 AI 主管 Veeral Patel 指出的那样。“Gemini 3.5 Flash-Lite 在我们的收据提取基准测试中落在了帕累托前沿，提供了我们在准确性、延迟和成本之间测试过的最佳权衡之一，”他在今天的公告中写道。“这种组合对于 Ramp 至关重要，我们需要快速、可靠地大规模处理收据。”

## 3.5 Flash Cyber：价格相同，访问受限

借助 Gemini 3.5 Flash Cyber，谷歌正在更深入地利用 AI 处理网络安全用例，而无需冒任何 [Fable 5 类似后果](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/)的风险。

正如谷歌指出的那样，今天的“AI 模型已经能够比当前系统修复速度更快地发现安全漏洞。”该公司在常规 3.5 Flash 模型的基础上构建了 3.5 Flash Cyber，并且收费相同，这使得谷歌有能力声称它“为大型、昂贵的网络安全模型提供了一种具有成本效益且功能强大的替代方案。”

但你目前还无法使用 Cyber 模型。它仅在针对政府和受信任合作伙伴的有限访问试点中提供，且仅在谷歌自己的 CodeMender 工具中提供。计划是随着时间的推移扩大访问范围。

在发现和利用软件漏洞方面，3.5 Flash Cyber 似乎不太可能达到 [Anthropic Mythos](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/) 的水平，但这显示了前沿实验室现在对推出这些模型是多么紧张。“这将使一线防御者在关键漏洞被利用之前就有先机去发现和修复它们，同时减轻更广泛的滥用，”谷歌指出。

与此同时，许多像 [Kimi K3](https://thenewstack.io/kimi-k3-open-weight-coding/) 这样的中国开源模型可能与 3.5 Flash Cyber 处于同一水平。

谷歌表示其性能达到了 Opus 4.6 的水平，并指出“由于护栏限制，最近的竞争对手模型表现不如 Claude Opus 4.6。”