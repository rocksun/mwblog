**Anthropic于周五发布了Opus 5**，这是该公司曾经的旗舰模型系列的最新版本（在Fable 5发布之前）。

Anthropic表示，Opus 5在许多领域的表现都接近Fable 5，而且价格仅为Fable 5的一半。其token成本维持在每百万输入/输出token 5美元/25美元，与Opus 4.8相比没有变化。与Fable 5不同的是，用户无需同意30天数据保留政策即可使用Opus 5。目前，它是Claude Max订阅用户的默认模型（也是Claude Pro订阅用户可访问的最佳模型）。

## 近乎Fable 5

不出所料，Opus 5是Anthropic迄今为止能力最强的Opus模型，该公司强调，它不仅能比以往更长时间地自主完成工作，还能自行检查工作成果并从错误中恢复。

不过，Anthropic表示，对于“最雄心勃勃的任务”以及需要长达数天自主性的项目，Fable 5仍然是首选模型。与此同时，Anthropic将Opus 5描述为“专为日常使用而设计”。

![](https://cdn.thenewstack.io/media/2026/07/1bb4ab5e-screenshot-2026-07-24-at-10.20.02-am-1024x699.png)

或许正是这种在项目上长时间工作的能力使Fable 5脱颖而出，因为在Anthropic迄今为止分享的几乎每一项基准测试中，Opus 5的表现实际上都超过了Fable 5。

这使得几周前才发布的Sonnet 5处于一个略显尴尬的位置：它夹在更便宜、更快但能力远逊的Haiku 4.5，以及能力更强但昂贵的Opus和Fable系列之间。毕竟，Sonnet 5之前被定位为“日常任务最高效的模型”。

## Opus 5 基准测试

这款新的Opus模型在处理知识工作方面表现尤为突出，并改进了Opus 4.8的编码能力。它在GDPval-AA v2知识工作基准测试中得分为1861，领先于Fable 5 (1747)、GPT-5.6 Sol (1736) 和 Opus 4.8 (1593)。

它也是Zapier [AutomationBench](https://zapier.com/benchmarks) 上的顶级模型，该测试衡量AI智能体在端到端业务工作流中的表现（Google的新款 [Gemini 3.6 Flash](https://thenewstack.io/google-ships-3-new-gemini-models-just-not-the-one-everyones-waiting-for/) 本周早些时候曾在该榜单榜首停留了很短时间）。Anthropic表示，Opus 5在相同任务成本下的通过率是次优模型的两倍，即使在最低的工作强度设置下，该模型通过的任务也比其他任何模型都多。

| 基准测试 | Opus 5 | Fable 5 | Opus 4.8 | GPT-5.6 Sol |
| --- | --- | --- | --- | --- |
| **智能体终端编码** Frontier-Bench v0.1 | **43.3%** | 33.7% | 18.7% | 37.5% |
| **知识工作** GDPval-AA v2 | **1861** | 1747 | 1593 | 1736 |
| **智能体搜索** BrowseComp | **90.8%** | 87.4% | 84.3% | 90.4% |
| **多学科推理** Humanity’s Last Exam | 56.3% 无工具 **64.7%** 有工具 | **56.5%** 无工具 63.9% 有工具 | 49.8% 无工具 57.9% 有工具 | — — |
| **计算机使用** OSWorld 2.0 | **70.6%** | 66.1% | 55.7% | 62.6% |
| **智能体编码** DeepSWE v1.1 | 68.8% | 69.7% | 59.0% | **72.7%** |
| **智能体编码** FrontierCode v1.1, Main | **53.4%** | 53.5% | 46.5% | 47.5% |
| **业务工作流** AutomationBench | **26.0%** | 17.4% | 17.0% | 18.1% |
| **法律** Legal Agent Benchmark, Held-out | 11.7% | **13.3%** | 10.4% | 2.5% |
| **健康** HealthBench Professional | 59.8% | Mythos 5 **66.0%** | 57.4% | 60.5% |
| **生物学** BioMysteryBench | **49.4%** 困难 **90.1%** 人类解决 | 46.5% 困难 Mythos 5 89.0% 人类解决 | 42.4% 困难 88.5% 人类解决 | — — |

图片来源: Anthropic

**Anthropic还表示，Opus 5是其迄今为止在DeepSearchQA和Humanity’s Last Exam（使用工具）上表现最好且性价比最高的模型**，甚至在这些测试中以微弱优势超过了Fable 5（64.7% 对 63.9%）。在不给模型使用工具权限的情况下，Fable 5依然保持领先。

不过，Fable 5确实在少数几个领域保持了领先地位，其中包括Anthropic的保留法律智能体基准测试和DeepSWE，而Mythos 5仍然是该公司在健康基准测试中最强的模型。

在编码方面，Anthropic表示在CursorBench 3.2上，Opus 5在高性能、超高性能和最大设置下的性价比表现超过了所有其他模型；该公司表示，在最大强度下，该模型的得分与Fable 5的峰值得分相差不到0.5%，而每个任务的成本仅为后者的一半。

在Anthropic发布的准备好的评论中，Cursor联合创始人Sualeh Asif表示：“Claude Opus 5以Opus的速度和成本提供了接近Fable 5的智能水平。在CursorBench上，它略低于Fable 5，并且具有许多相同的行为。我们很期待看到开发者如何在Cursor中使用它。”

和以前一样，Anthropic产品的用户可以在低、中、高、超高和最大设置之间进行选择，以获得相应的智能提升（以及token使用量）。

## Opus 5 的安全性

基于自动行为审计，Anthropic还称Opus 5是其迄今为止最对齐的模型，并且与Fable 5一起，它是最不容易被诱导进行误用的模型。

该公司表示，它刻意没有在网络安全任务上训练该模型。尽管如此，Opus 5在发现开源代码中的漏洞方面仍接近Mythos 5，但在实际利用漏洞方面则远落后——这正是Anthropic [想要达到的状态](https://thenewstack.io/anthropic-fable-ban-lifted/)。

![](https://cdn.thenewstack.io/media/2026/07/52c9c9d8-screenshot-2026-07-24-at-7.56.58-am-1024x470.png)

为了确保其安全，避免任何 [类似于Fable 5的问题](https://thenewstack.io/anthropic-fable-mess-explained/)，Opus 5配备了一套安全分类器，可以筛选针对一小部分网络任务的请求，包括漏洞利用生成和渗透测试。由于它们的范围比Fable 5的安全分类器更窄，Anthropic预计它们的干预频率将降低约85%。

Anthropic表示，其理念是为寻找源代码漏洞等防御性工作留出空间，同时阻止所谓的 [“基于二进制的漏洞扫描”](https://www.binarly.io/blog/introducing-vulhunt-a-high-level-look-at-binary-vulnerability-detection)——Anthropic称这是一种更有可能与恶意行为者相关的技术。

当分类器在Claude.ai、Claude Code或Cowork中标记请求时，它默认回退到Opus 4.8，API用户也可以启用相同的行为。Anthropic网络验证计划中的企业和研究人员可以访问一个限制较少的Opus 5版本。

与其他前沿实验室一样，Anthropic正利用此次发布来强调其模型的高性价比。在目前这个阶段，每一家企业都在关注token成本，每一家实验室现在也都对市场如何看待其模型价格感到敏感。

> 在目前这个阶段，每一家企业都在关注token成本，每一家实验室现在也都对市场如何看待其模型价格感到敏感。

法律AI公司Harvey的研究主管Niko Grupen表示，Harvey在Opus 5上获得的收益主要集中在公司治理和仲裁等实践领域。“我们印象深刻的是，”Grupen说，“Opus 5在较低推理水平下保持质量的能力，在获得类似性能的同时，与最大推理下的Opus 4.8相比，平均token生成量减少了26%。”

## Opus 5 快速模式

与Opus 4.8一样，Opus 5也将提供“快速模式”，无论是在开发者的Claude Platform上，还是通过扣除额外使用额度在Claude Code中。它生成的输出token速度将快2.5倍，成本增加2倍。

今天还有两个较小的平台更新以测试版形式发布。通过自动回退功能，Anthropic安全分类器在Opus 5或Fable 5上拒绝的API请求可以自动路由到同一请求内的另一个模型，而不是返回错误。开发者现在还可以在对话中途更改Claude可以使用的工具，而无需使提示词缓存失效，因此智能体工作的每个阶段只会看到它需要的工具。

Opus 5现已在Anthropic的所有付费方案以及Claude Platform上以 `claude-opus-5` 的名称提供。

## 背景

虽然 [Opus 4](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/) 于2025年5月发布，但2025年11月的 [Opus 4.5](https://thenewstack.io/anthropics-new-claude-opus-4-5-reclaims-the-coding-crown-from-gemini-3/) 和2026年2月的 [Opus 4.6](https://thenewstack.io/claude-sonnet-46-launch/) 巩固了该模型系列作为编码最佳（有时是*最强*）模型之一的声誉。

对于许多用户来说，2026年4月发布的 [Opus 4.7](https://thenewstack.io/claude-opus-47-launch/) 有些令人失望，这或许可以解释为什么Anthropic仅在一个半月后就发布了广受好评的 [Opus 4.8](https://thenewstack.io/claude-opus-48-release/)。

随着Mythos和Fable的推出，Anthropic最近创建了一个新的旗舰模型层级，但该公司表示，它预计Opus 5将成为“我们期望人们每天都会使用的模型，特别是在企业中”。

OpenAI最近发布了其 [GPT-5.6 Sol、Terra和Luna系列](https://thenewstack.io/openai-gpt-56-live/)，Sol旗舰模型的价格比Opus 5略贵，为每百万输入/输出token 5美元/30美元。在Anthropic此次发布分享的基准测试表中，Sol仅在一项基准测试中击败了Opus 5，即智能体编码测试DeepSWE v1.1（72.7% 对 68.8%）。在其他所有领域，Anthropic都处于领先地位，包括知识工作、计算机使用和业务工作流。

与此同时，Google的Gemini模型根本没有出现在Anthropic的对比表中。显然，Anthropic认为它们不值得额外占用一列。