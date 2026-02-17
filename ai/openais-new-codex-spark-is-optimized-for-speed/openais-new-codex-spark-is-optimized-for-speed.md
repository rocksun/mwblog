<!--
title: OpenAI新模型Codex Spark：为速度而生
cover: https://cdn.thenewstack.io/media/2026/02/9cb2857f-glenn-hansen-vw4xilrr-do-unsplash-scaled.jpg
summary: OpenAI发布Codex Spark模型，专为降低延迟和追求速度设计，由Cerebras硬件驱动，可实现快速原型和代码编辑。它牺牲部分性能以换取极速响应，补充现有模型。
-->

OpenAI发布Codex Spark模型，专为降低延迟和追求速度设计，由Cerebras硬件驱动，可实现快速原型和代码编辑。它牺牲部分性能以换取极速响应，补充现有模型。

> 译自：[OpenAI's new Codex Spark model is built for speed](https://thenewstack.io/openais-new-codex-spark-is-optimized-for-speed/)
> 
> 作者：Frederic Lardinois

OpenAI新推出的[GPT-5.3-Codex-Spark](https://openai.com/index/introducing-gpt-5-3-codex-spark/)模型与其Codex软件开发模型家族略有不同：它将重点完全放在降低延迟上。

Codex Spark模型由Cerebras 125 petaflop的[晶圆级引擎3](https://www.cerebras.ai/chip)提供支持，旨在用于延迟与智能同样重要（甚至更重要）的用例。它的速度确实很快：Codex Spark可以[每秒处理超过1,000个token](https://www.cerebras.ai/blog/openai-codexspark)。

几天前，当OpenAI发布GPT-5.3-Codex时，它强调了团队如何将延迟降低25%。然而，虽然该模型擅长长时间运行的编码和代理任务（其中延迟不那么重要），但Codex Spark专为快速原型设计和快速获取答案而设计。

这里的核心思想是拥有两个互补的模型：一个用于实时协作的快速模型，一个用于需要更深层推理的长时间运行任务的较慢模型。

OpenAI指出，其新模型最适合对代码进行小而有针对性的编辑。不过，速度带来的额外好处是，该模型可以轻松中断和重定向，帮助开发人员快速迭代。

然而，由于它是针对这种用例进行优化的，因此在发布时也只提供128,000个token的上下文窗口。它也仅支持文本。随着时间的推移，团队计划为这个更快的模型家族添加更多功能，包括更大的模型、更长的上下文长度和多模态输入。

## 基准测试

该公司承认，新模型将不如GPT-5.3-Codex，“但可以在极短的时间内完成任务。”

在标准SWE-Bench Pro基准测试中，Codex Spark的得分确实远低于GPT-5.3-Codex，但它确实能更快地获得可用结果，这可能足以满足许多用例。

![](https://cdn.thenewstack.io/media/2026/02/905a1e10-swe-bench-pro.png)

图片来源：OpenAI。

在Terminal-Bench 2.0上，该基准测试评估模型在终端中代理工作流的性能，它的得分也显著低于更大的GPT-5.3-Codex（58.4%对77.3%）。

## 可用性

GPT-5.3-Codex-Spark层级现在作为研究预览版，通过CLI、VS Code和[Codex应用](https://thenewstack.io/openais-codex-desktop-app-is-all-about-managing-agents/)（下载量已超过100万次）向ChatGPT Pro用户开放。部分OpenAI合作伙伴也将通过API抢先体验Codex Spark。

OpenAI指出，新的Codex Spark模型的容量可能会受到限制，访问速度较慢并可能出现临时排队。该模型将有自己的速率限制，使用它不计入公司常规的速率限制。

由于它尚未在API中提供，OpenAI尚未发布任何定价信息。

## 为何OpenAI选择Cerebras的晶圆级AI加速器

当然，使用不同模型层级并非一个新想法。Anthropic及其三个模型层级（Haiku、Sonnet和Opus）以及其他公司长期以来都采用类似的方法，提供主要通过智能、速度和定价来区分的模型。OpenAI本身也长期提供其模型的[nano](https://developers.openai.com/api/docs/models/gpt-5-nano)版本。

这里的主要区别在于OpenAI也为这个新模型使用了截然不同的硬件平台。

OpenAI选择在Cerebras的硬件上运行此模型并非巧合。2026年初，两家公司宣布了一项为期多年的合作协议，据报道[价值高达100亿美元](https://www.cnbc.com/2026/01/14/cerebras-scores-openai-deal-worth-over-10-billion.html)。根据该协议，Cerebras将建造并托管数据中心，为OpenAI提供750兆瓦的容量来运行其晶圆级芯片。

与大多数标准GPU和AI加速器相比，Cerebras的芯片是巨大的。NVIDIA的旗舰Blackwell B200加速器拥有2080亿个晶体管。Cerebras的芯片拥有四万亿个晶体管，分布在近90万个核心之间。

但这不仅仅是纯粹的计算能力。目前，推理的真正瓶颈不是计算，而是[内存带宽](https://thenewstack.io/why-d-matrix-bets-on-in-memory-compute-to-break-the-ai-inference-bottleneck/)。Cerebras承诺通过使用片上内存和高达每秒27拍字节的内部带宽来消除这一瓶颈。

OpenAI在其声明中强调，GPU仍然是其训练和推理管道的基础。但该公司也指出，“Cerebras通过擅长要求极低延迟的工作流来补充这一基础，从而收紧端到端循环，使Codex在您迭代时感觉响应更快。”

正如Cerebras首席技术官兼联合创始人Sean Lie所说：“GPT-5.3-Codex Spark最让我们兴奋的是与OpenAI和开发者社区合作，发现快速推理能实现什么——新的交互模式、新的用例以及根本不同的模型体验。此次预览只是一个开始。”