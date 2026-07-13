<!--
title: OpenAI GPT-5.6 系列正式发布
cover: https://cdn.thenewstack.io/media/2026/07/fb2dd967-veii-rehanne-martinez-u319ecdfvak-unsplash-scaled.jpg
summary: OpenAI 发布了 GPT-5.6 系列模型，包含 Sol、Terra 和 Luna 三个版本。该系列不仅在编程与知识工作中性能卓越，更强调以更低的成本实现更高的效率，通过内置推理能力优化任务处理，并在安全合规方面进行了升级。
-->

OpenAI 发布了 GPT-5.6 系列模型，包含 Sol、Terra 和 Luna 三个版本。该系列不仅在编程与知识工作中性能卓越，更强调以更低的成本实现更高的效率，通过内置推理能力优化任务处理，并在安全合规方面进行了升级。

> 译自：[OpenAI's GPT-5.6 is now live](https://thenewstack.io/openai-gpt-56-live/)
> 
> 作者：Frederic Lardinois

正如[预期](https://thenewstack.io/gpt-5-6-developer-reactions/)的那样，OpenAI 于周四向全球的应用和 API 用户推出了 GPT-5.6 系列模型。

这是 OpenAI 首次同时发布其新模型的三种不同版本：

* **Sol** 是旨在与 Anthropic 的 Fable 5 竞争的旗舰模型
* **Terra** 是主流模型
* **Luna** 是速度更快、价格更亲民但能力稍弱的选择

## GPT 5.6 可用性与定价

在此次发布中，OpenAI 根据推理力度对模型能力进行了限制。正如 OpenAI 所述，Pro 和 Enterprise 用户可以使用 GPT-5.6 Sol Pro，“以在复杂任务上获得最高质量的结果”。

在 Codex 和全新的 ChatGPT Work（OpenAI 新推出的 Claude Cowork 竞品）中，Free 和 Go 用户可以使用 Terra 模型，而 Plus、Pro、Business 和 Enterprise 用户则可以在 Sol、Terra 和 Luna 之间进行选择，并为每个模型设置推理力度。

值得注意：在 Codex 中，Ultra 模式适用于 Plus 及更高级别的方案。

当然，所有新模型也将在 API 中提供。Sol 的价格为每百万输入 token 5 美元，每百万输出 token 30 美元。Terra 的价格为 2.50 美元/15 美元，Luna 的价格为 1 美元/6 美元。

## GPT 5.6 基准测试

Sol 作为新的旗舰模型，其表现通常与 Anthropic 业界领先的 Fable 5 模型相当或更胜一筹，但 OpenAI 此次为其模型提出的主要论点更多集中在成本上。

“我们训练 GPT-5.6 的目标是从每个 token 中获得更多有用的工作，”该公司在公告中指出。在基准测试中，这一点在 Artificial Analysis Intelligence Index 中体现得最为明显：GPT-5.6 Sol 的表现与 Fable 5 差距不到一个百分点，但成本却减半，耗时仅为其一半多一点。

### 专业能力

| 评估项目 | GPT-5.6 Sol | GPT-5.6 Terra | GPT-5.6 Luna | GPT-5.5 | Claude Fable 5 | Claude Opus 4.8 |
| --- | --- | --- | --- | --- | --- | --- |
| Agents’ Last Exam | 52.7% | 50.4% | 50.3% | 46.9% | 40.5% | 45.2% |
| GDPval-AA v2 | 1,747.8 Elo | 1,593 Elo | 1,591.8 Elo | 1,493.7 Elo | 1,759.6 Elo | 1,600.1 Elo |
| Management Consulting Tasks (Internal) | 43.2% | 37.2% | 35.4% | 31.3% | 35.5% | 31.6% |
| Big Finance Bench | 53% | 51% | 36% | 49% | — | 44% |
| Artificial Analysis Intelligence Index v4.1 | 58.9 Index score | 55 Index score | 51.2 Index score | 54.8 Index score | 59.9 Index score | 55.7 Index score |

### **编程能力**

| 评估项目 | GPT-5.6 Sol | GPT-5.6 Sol Ultra | GPT-5.6 Terra | GPT-5.6 Luna | GPT-5.5 | Claude Mythos 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Artificial Analysis Coding Agent Index v1.1 | 80 Index score | — | 77.4 Index score | 74.6 Index score | 76.4 Index score | — |
| SWE-Bench Pro | 64.6% | — | 63.4% | 62.7% | 59.4% | 80.3% |
| DeepSWE v1.1 | 72.7% | — | 69.6% | 67.2% | 67% | — |
| Terminal-Bench 2.1 | 88.8% | 91.9% | 87.4% | 84.7% | 85.6% | 88% |

## GPT 5.6 编程

对于代理工作流，基于测试长周期代理任务的 Agents’ Last Exam 基准测试，GPT-5.6 Sol 以 13.1 分的优势击败了 Fable 5。

![](https://cdn.thenewstack.io/media/2026/07/4e58842c-screenshot-2026-07-09-at-10.20.25-am-1024x901.png)

*图片来源：OpenAI*

在编程基准测试中，结果类似，GPT-5.6 Sol 经常击败 Anthropic 的 Fable 5，以显著更低的成本获得更高分数。这一点在 Terminal-Bench 2.1 和 DeepSWE 1.1 中同样成立。

OpenAI 认为，模型之所以表现如此出色，原因之一是它们内置了新的功能，允许其在内部执行某些任务。

“GPT-5.6 可以编写并运行轻量级程序来协调工具、处理中间结果、监控进度，并随着工作的展开选择下一步行动。这使得工具密集型任务能够以更少的 token、更少的模型往返次数和更少的指导来推进，”OpenAI 写道。

现在还新增了一种“ultra”模式——类似于 Anthropic 的“ultracode”，它并行调度一个由四个代理组成的团队，适用于您需要更好（且更快）结果，并且愿意在此过程中消耗更多 token 的场景。

![](https://cdn.thenewstack.io/media/2026/07/34e70b4b-screenshot-2026-07-09-at-10.29.57-am-1024x901.png)

*图片来源：OpenAI*

“GPT-5.6 Sol 为智能和效率树立了新标准，在编程、知识工作、网络安全和科学领域实现了最先进的结果，同时以更少的 token 和更低的预估成本超越了之前和竞争对手的前沿模型，”OpenAI 写道。“结果是单位成本的性能更强：以同样的支出完成更多成功的工作，或以更低的总成本获得相当的结果。”

## 知识工作

在知识工作方面，GPT-5.6 Sol 通常也处于领先地位，在 BrowseComp 代理浏览基准测试中得分 92.3%，在评估长周期计算机使用任务的 OSWorld 2.0 中得分 62.6%。

但对于用户来说，可能比原始基准测试数字更重要的是，该模型在制作演示文稿和文档方面有所改进。

“在遵循模板和参考幻灯片时，这种改进尤为明显，”OpenAI 写道。“GPT-5.6 可以推断幻灯片的视觉设计系统——布局、排版、间距、颜色和重复的内容模式（包括嵌入在幻灯片母版中的规则）——并将这些惯例一致地应用于新材料。”

此外，作为额外福利，正如公司在随发布会举行的直播中所说，GPT-5.6 不会过多地[谈论妖精](https://openai.com/index/where-the-goblins-came-from/)。

## 安全性

考虑到 Fable 5 发生的事件以及 OpenAI 本身推迟了新模型的发布以等待政府批准，该公司在发布材料中花费了不少篇幅介绍其安全栈。OpenAI 可能比 Anthropic 更接近特朗普政府——或者至少拥有更好的关系——但该公司当然也不希望看到其模型被下架。

> “在网络安全方面，我们的测试表明，GPT-5.6 在发现和修复漏洞方面的能力强于在针对受保护目标可靠地执行自主、端到端攻击方面的能力”——OpenAI

“GPT-5.6 模型在生物学和网络安全方面的能力都比我们之前的模型更强，但在任何类别中都没有越过临界阈值，”OpenAI 指出。“在网络安全方面，我们的测试表明，GPT-5.6 在发现和修复漏洞方面的能力强于在针对受保护目标可靠地执行自主、端到端攻击方面的能力——这为防御者提供了在弱点被利用之前加强系统的机会。在生物学方面，我们的测试表明，GPT-5.6 可以支持合法的研究，但不提供创建、设计或合成高度危险的新型威胁所需的端到端能力。”

OpenAI 没有像 Anthropic 那样过多谈论模型将如何处理拒绝请求。虽然 Anthropic 的 Fable 5 会将一些敏感请求降级到 Opus 模型，但 OpenAI 主要讨论的是拦截攻击。

“与之前的模型相比，我们的 GPT-5.6 Sol 网络安全保护措施拦截的潜在有害活动大约增加了十倍，”该公司解释道，并像 Anthropic 一样指出，“没有所谓的完美安全，我们保护日益强大的模型的工作仍在继续。新的弱点会被发现，绕过现有安全措施的新越狱手段也会被发现。”