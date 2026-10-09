<!--
title: Anthropic发布降价大幅的Haiku 5.5模型
cover: https://cdn.thenewstack.io/media/2026/04/88e49de1-img_0987-2-scaled.jpg
summary: Anthropic发布了全新轻量模型Claude Haiku 5.5，不仅在各项基准测试中大幅超越前代及部分竞品，价格更是大幅下调高达75%，并首次引入了effort控制和计算机使用等新功能。
-->

Anthropic发布了全新轻量模型Claude Haiku 5.5，不仅在各项基准测试中大幅超越前代及部分竞品，价格更是大幅下调高达75%，并首次引入了effort控制和计算机使用等新功能。

> 译自：[Anthropic launches Haiku 5.5 at a much lower price](https://thenewstack.io/anthropic-claude-haiku-5-5/)
> 
> 作者：Frederic Lardinois

**Anthropic于周三发布了Claude Haiku 5.5**，这是其最小、最实惠的模型近一年来的首个新版本。

这也是Anthropic在一个月内推出的第三个5.5系列模型，不过目前还缺Fable 5.5。然而，该模型可能需要经历更严格的审查流程，因此它的发布推迟也在意料之中。

## Haiku 5.5 定价机制

与之前的迭代一样，该公司将 [Haiku 5.5](https://www.anthropic.com/claude/haiku) 描述为其“速度最快、效率最高的模型”，但这一次，它的价格也便宜得多。Haiku 4.5 的每百万输入/输出 Token 价格为 $1/$5，而 Anthropic 将针对 100,000 Token 以下的请求，把价格降至 $0.10/$0.50。

> Anthropic 将 Haiku 5.5 描述为其“速度最快、效率最高的模型”，但这一次，它的价格也便宜得多。

对于更大的请求，新价格为 $0.50/$2.50（无论请求中的 Token 数量多少，Haiku 4.5 的价格都相同），但 Anthropic 指出，Haiku 4.5 约有 90% 的请求属于较低价格类别（这可能是开发者过去发送给 Haiku 的工作类型所决定的）。

这分别使每 Token 价格降低了 90% 和 50%。Anthropic 预计平均节省成本约为 75%。这综合考虑了各类请求以及一个更新的 Tokenizer（分词器），该 Tokenizer 在每个任务中使用的 Token 略多。

这个新版本是首个带有 effort 控制（默认值为中等）的 Haiku 模型，让开发者能够控制模型在给定任务上消耗多少 Token。

|  | | Haiku 5.5 | Haiku 4.5 | GPT-6 Luna | Sonnet 5.5 |
| --- | --- | --- | --- | --- | --- |
| 知识工作 *GDPval-AA v2.1* | | 1620 | 735 | 1437 | 1840 |
| 知识工作 *AA-Briefcase v1.1* | | 1578 | 614 | 1336 | 1824 |
| 计算机使用 *OSWorld 2.1 (Offline subset)* | | 72.4% | 15.7% | 48.9% | 83.9% |
| 多学科推理 *Humanity’s Last Exam* | 无工具 | 45.9% | 10.2% | – | 56.9% |
| 有工具 | 57.4% | 18.7% | – | 64.5% |
| 智能体编程 *Terminal-Bench 4.0* | | 39.2% | 0.0% | 16.4% | 70.6% |
| 智能体编程 *FrontierCode 1.1 (Main)* | | 46.4% | – | 42.4% | 52.1% (Xhigh) |
| 视觉推理 *Chartography (no tools)* | | 46.4% | 6.4% | 29.1% | 61.6% |

## 小型模型，新的工作

这些小型模型的用例一直都是处理诸如摘要、分类和路由等高吞吐量任务。

当然，这也是 [像 Jev 这样的决策模型](https://thenewstack.io/typesafe-jev-system-one/) 目前大放异彩的领域——而且价格更低。

展望未来，这可能不再是像 Haiku 或 OpenAI 的 GPT-6 Luna 这样的小型模型最有用武之地的地方，因此 Anthropic 还指出该模型可以处理诸如压缩和数据库查询等任务，以及注重速度的智能体工作负载（包括实时客服和浏览器使用），这也就不令人意外了。

## Haiku 5.5 基准测试

Anthropic 自身的评估显示，它比 Haiku 4.5 有了显著改进。在测试计算机使用的 OSWorld 2.1 离线子集上，Haiku 5.5 得分为 72.4%，高于其前身的 15.7%，并领先于 GPT-6 Luna 的 48.9%。

在 GDPval-AA v2.1 知识工作基准测试中，Haiku 5.5 得分为 1,620，而 Haiku 4.5 为 735，GPT-6 Luna 为 1,437。毫无疑问，Sonnet 5.5 在这两个基准测试中依然领先。

在测试命令行环境中复杂多步骤任务的 Terminal-Bench 4.0 上，Haiku 5.5 得分为 39.2%，而 Haiku 4.5 为 0%，GPT-6 Luna 为 16.4%，Sonnet 5.5 为 70.6%。

## 中国竞争对手的对比

Anthropic 仅将 Haiku 5.5 直接与其自身模型以及 OpenAI 的 GPT-6 Luna 进行了对比。但谈到小型模型时，许多开发者也在关注来自 Z.ai、阿里巴巴等公司的竞争对手。

Artificial Analysis 目前给 Z.ai 的 GLM-5.3-Flash 在 [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) 上打出了 1,647 的高分，在 [AA-Briefcase v1.1](https://artificialanalysis.ai/evaluations/aa-briefcase) 上打出了 1,454 分。相比之下，Anthropic 报告称 Haiku 5.5 的得分分别为 1,620 和 1,578。

当然，还有更便宜的选择。在阿里巴巴的国际服务中，对于最高 32,000 Token 的输入，Qwen3.7 Flash 的价格为每百万输入 Token 0.03 美元，每百万输出 Token 0.13 美元。对于 32,000 到 256,000 Token 之间的输入，这些费率分别上升到 0.10 美元和 0.40 美元。

Haiku 5.5 已在 Claude Platform、Amazon Web Services、Google Cloud 和 Microsoft Azure 上线。使用 Anthropic 平台的开发者可以将其作为 claude-haiku-5-5 进行访问。该公司还在其 Python 和 TypeScript SDK 中添加对计算机使用和浏览器使用的 Beta 版支持。

## 同样是新品：Sonnet 5.5 缓存价格下调，Max 和 Team 订阅获得 API 额度

伴随此次发布，Anthropic 将 Sonnet 5.5 的缓存读取价格减半，从每百万 Token 0.20 美元降至 0.10 美元。该公司表示，这应该会使大多数智能体任务的成本降低约 20%。该降价措施于周三在各大平台上推出，不过部分现有的 Azure 和 Google Cloud 客户需要等待几天。

> Anthropic 正在将 Sonnet 5.5 的缓存读取价格减半

Anthropic 本周还为其 Max 和 Team 订阅用户增加了每月的 API 额度。Max 5x 订阅者每月将获得 100 美元，Max 20x 订阅者将获得 200 美元。Team 订阅者将获得高达 500 美元的额度，并在其用户之间共享。这些额度可用于 Claude Platform 上的任何模型。

Haiku 5.5 还附带了比 Haiku 4.5 更严格的网络安全防护，不过 Anthropic 表示，与 Sonnet 5.5 的防护相比，这些防护允许更广泛的防御性工作。它们仍然会阻止渗透测试。需要更广泛权限来进行网络安全或生物学研究的组织可以向 Anthropic 的验证计划申请。