<!--
title: Claude Opus 5在ARC-AGI-3得分仅30%，搭载Nvidia AVO系统后达到100%
cover: https://cdn.thenewstack.io/media/2026/08/c0ba356b-vector-1786236125324-922d0224c117-1024x576.avif
summary: Nvidia开发的AVO代理系统通过引入持久化内存和监督机制，成功将Claude Opus 5在ARC-AGI-3测试中的得分从30%提升至100%。该成果证明，系统架构对提升AI长期自主推理与复杂任务执行能力至关重要，而非仅依赖模型本身。
-->

Nvidia开发的AVO代理系统通过引入持久化内存和监督机制，成功将Claude Opus 5在ARC-AGI-3测试中的得分从30%提升至100%。该成果证明，系统架构对提升AI长期自主推理与复杂任务执行能力至关重要，而非仅依赖模型本身。

> 译自：[Claude Opus 5 scored 30% on ARC-AGI-3. Wrapped in Nvidia's AVO, it hit 100%.](https://thenewstack.io/nvidia-avo-arcagi3-benchmark/)
> 
> 作者：Adrian Bridgwater

[Nvidia](https://thenewstack.io/nvidia-local-frontier-models/) 于 2026 年 3 月下旬首次推出了其 [Agentic Variation Operators (AVO)](https://arxiv.org/pdf/2603.24517) 通用编码代理系统。该公司现已揭开了使 AVO 能够维持长期自主工作的架构和系统级机制的面纱，并将其应用于开放平台高级 AI 推理基准 [ARC-AGI-3](https://arcprize.org/arc-agi/3)。

在周五发布的一篇[团队博客](https://developer.nvidia.com/blog/nvidia-avo-reaches-100-on-arc-agi-3-demonstrating-a-frontier-level-general-purpose-architecture-for-long-horizon-autonomous-agents/)中，由 Nvidia 软件工程师、机器学习专家和 AI 研究实习生组成的五人小组描述了 AVO 如何将 [Claude Opus 5](https://thenewstack.io/anthropics-opus-5-almost-fable-5/) 在 ARC-AGI-3 上的基础模型得分从报告的 30.2% 提升至作为完整 AVO 代理系统一部分运行时的 100%。

“（这一结果）表明，系统设计——而不仅仅是模型能力——可以解锁前沿水平的长期任务表现，”团队写道。

## Nvidia 的 AVO 处理哪些任务？

AVO 从构成 [代理工具包 (agent harness)](https://thenewstack.io/agent-harness-distributed-feedback-problem/) 的核心基因演变而来，处理与检查和编辑代码、运行命令、查阅文档以及通过执行验证工作相关的代理架构任务。据称，AVO 的独特重点在于在长视野（long horizons）的多步任务中实现“持续的上下文内自主操作”。

非营利性 AI 研究与基准测试机构 [ARC Prize](https://arcprize.org/) 在 [今年 7 月的一篇分析文章](https://arcprize.org/results/anthropic-claude-opus-5) 中报告了 Claude Opus 5 在 ARC-AGI-3 系统公共环境和任务集上以高推理力度运行时的 30.2% 得分。据 ARC Prize 称，这“展示了强大的逻辑推理能力”，并且当 Claude Opus 5 以最大推理力度运行时，其在 ARC-AGI-1 上得分为 97.5%，在 ARC-AGI-2 半私有集上得分为 90.4%。

ARC-AGI-3 基准测试使用 [相对人类行动效率 (RHAE)](https://docs.arcprize.org/methodology)，这是一种将任务完成情况与相对于首次人类基准的每级行动效率相结合的指标，其表现是在不同级别和环境中聚合得出的。

“AVO 在 ARC-AGI-3 公共集的全部 25 个环境中取得了 100.00 的 RHAE 分数，完成了所有 183 个级别。该结果说明了一个更广泛的观点：评估模型并不等同于评估代理。模型能力固然重要，但周围的系统决定了该能力能够多有效地转化为持续的自主进展，”Nvidia 博客团队（由首席工程师 [Terry Chen](https://www.linkedin.com/in/terry-chen-11a85310a/) 领导）表示。

> “模型能力固然重要，但周围的系统决定了该能力能够多有效地转化为持续的自主进展。”

## 代理如何决定其下一个候选方案

AVO 最初是在困难的软件工程和 GPU 内核优化任务上进行演示的。在这项工作中，AVO 用一个自主代理取代了 Chen 和团队所描述的“传统进化搜索系统的预定义变异步骤”，该代理决定如何生成下一个候选方案，即检查什么、改变什么、测试什么以及提交什么。

该团队将这项工作作为基础研究基石，随后推进到 ARC-AGI-3 基准测试。

“GPU 内核优化和 ARC-AGI-3 基准测试表面上看起来非常不同，”Nvidia 团队指出。“一个涉及源代码、编译器、分析器和吞吐量。另一个涉及不熟悉的交互式环境，代理必须在其中推断可用操作的效果、发现目标并采取足够有效的行动以取得进展。但底层的计算模式是相似的。”

在这两种设置中，代理都必须：

* 从不完整证据中构建假设
* 通过外部接口采取行动
* 观察结果
* 保留有用的状态
* 修订其问题模型
* 从错误的假设中恢复
* 在长视野内持续取得进展

保留状态和进展，在处理超过单个模型上下文窗口且对系统前方内容了解不完整的情况下重做错误假设并进行长期任务，需要在 AVO 中存在两个特定机制：[持久化内存 (persistent memory)](https://thenewstack.io/how-to-add-persistence-and-long-term-memory-to-ai-agents/) 和监督。

> “保留状态和进展（以及）在处理超过单个模型上下文窗口且对系统前方内容了解不完整的情况下进行长期任务，需要在 AVO 中存在两个特定机制：持久化内存和监督。”

持久化内存在这里用于向前携带先前的实现、评估结果、[编译器](https://thenewstack.io/meta-releases-open-source-react-compiler/) 和分析器输出，以及积累的推理。它允许代理从当前状态恢复，而不必重复重建搜索——这正是 Chen 和团队将其视为圣杯的“持续自主进展”。

监督也是关键；一个监督者（AVO 系统内的程序化软件模块，本例中非人类）监控更广泛的搜索轨迹，并在进展停滞时进行干预。

## Nvidia AVO 搭配 GPT-5.6 Sol

AVO 也被设计为可在前沿模型间运行。虽然该团队的公共集完整结果使用了 Claude Opus 5，但它还额外将 AVO 与 [GPT-5.6 Sol](https://thenewstack.io/gpt-sol-chatgpt-split/) 搭配，用于其分类为“挑战性游戏子集”的进一步实验。在这些测试中，Sol 在几种情况下以更快的挂钟时间（wall-clock time）达到了匹配级别，而 Opus 在匹配级别比较中使用了更少的环境操作。

挂钟时间（显然）是指人类所经历的现实世界时间。它不同于 CPU/GPU 时间，后者可能由多个核心（假设为 8 核）划分，因此 80 秒的计算时间可能变为 10 秒的挂钟时间。

“这些初步结果表明模型之间具有互补的运行配置文件，我们将更广泛的系统比较留给未来的工作，”Chen 和团队指出。“这些结果涵盖了使用官方记分卡和 RHAE 指标的 25 环境 ARC-AGI-3 公共集。它们不是半私有或完全私有竞赛集上的结果。”

## 团队从 ARC-AGI-3 的 AVO 基准测试中学到了什么

组建的工程师们表示，最重要的结果不仅仅是 100.00 的分数，而是相同的代理架构从高度专业化的 GPU 内核优化转移到了一个截然不同的交互式推理任务这一事实。

团队提醒我们，在 GPU 优化中，反馈来自编译器、测试、分析器和性能基准。在 ARC-AGI-3 中，反馈来自环境转换和行动结果。这意味着，本质上，接口不同，但循环是相同的，即循环致力于形成假设、行动、观察证据、更新状态并继续。

“这表明，通用性不仅可以来自领域知识，还可以来自允许推理和反馈随时间积累的机制。更广泛地说，长视野能力是整个系统的属性。内存决定了什么能留存，工具决定了什么行动是可能的，反馈奠定了进展的基础，而恢复能力允许工作在单个模型调用之外继续进行，”Nvidia AI 团队总结道。

Nvidia 博客团队成员包括上述的 Terry Chen、Nvidia 竞争性机器学习总监兼杰出工程师 [Jean-Francois Puget](https://www.linkedin.com/in/jfpuget/)、高性能 AI 副总裁 [Humphrey Shi](https://www.linkedin.com/in/humphreyshi/)，以及 AI 研究实习生 [Yeyin (Eva) Zhu](https://www.linkedin.com/in/yeyin-zhu-571b072a4/) 和 [Zhifan Ye](https://www.linkedin.com/in/zhifan-ye/)。

团队的最后总结重申了此次调查的核心：模型很重要，但模型并不是代理的全部。