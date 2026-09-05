<!--
title: OpenAI 发布 GPT-6 Astra，高呼“欢迎来到 AGI 时代”
cover: https://cdn.thenewstack.io/media/2026/09/6efd19a0-hero-static-16x9-with-copy.png
summary: OpenAI 发布旗舰模型 GPT-6 Astra，被视为开启 AGI 时代的标志。该模型性能显著提升，尤其在复杂任务与编程方面表现出色，同时 OpenAI 强调了其在网络安全和可观测性方面的挑战与应对策略。
-->

OpenAI 发布旗舰模型 GPT-6 Astra，被视为开启 AGI 时代的标志。该模型性能显著提升，尤其在复杂任务与编程方面表现出色，同时 OpenAI 强调了其在网络安全和可观测性方面的挑战与应对策略。

> 译自：[OpenAI launches GPT-6 Astra and says welcome to the "AGI era"](https://thenewstack.io/openai-gpt6-astra-benchmarks/)
> 
> 作者：Frederic Lardinois

**OpenAI 于周四发布了其最新的旗舰模型 GPT-6 Astra。** 该公司将其描述为“世界上最智能、最对齐的模型”，就基准测试结果来看，这一说法似乎并不过分。

在发布会前的新闻简报中，OpenAI 总裁 Greg Brockman 将这一评价提升到了超越基准测试的高度。在承认 AGI 仍然是一个“模糊且不明确的概念”后，他暗示未来的观察者可能会将 Astra 视为标志着 AGI 到来的模型。

“我认为，我们现在正处于 AGI 时代，这种感觉并非不合理，” Brockman 说。

当被问及 OpenAI 是否正式宣布实现了 AGI 时，他表示该术语已不再与合同触发点挂钩（他指的是 OpenAI 与 [Microsoft 的早期协议](https://openai.com/index/next-phase-of-microsoft-partnership/)），而是将其描述为一个“使命概念或精神概念”。

“我将决定权留给读者，让他们自己判断这是否符合他们的标准，” Brockman 说道。“就我个人而言，我认为我们已经到达了那个阶段。我认为这确实有很好的论据支持。但再次强调，我认为这只是旅程的开始，而非终点。”

他以这样的话结束了简报：“欢迎来到 AGI 时代。”

> “欢迎来到 AGI 时代。”
> —OpenAI 总裁 Greg Brockman。

## OpenAI 规模最大的训练任务

据 OpenAI 的 Aidan Clark 称，Astra 是 OpenAI 迄今为止规模最大的训练任务。“这是我们第一次在德克萨斯州 Stargate 基地使用超过 100,000 个 GPU 进行预训练，” 他说。Clark 还指出，Astra 是 OpenAI 首个在训练过程中由早期模型发挥重要监督作用的模型。

![](https://cdn.thenewstack.io/media/2026/09/382b277d-press-static-1024x576.png)

来源：OpenAI。

不过，您可能还无法立即使用 Astra。该模型的发布首先面向通过 OpenAI 的 Daybreak 计划已经获得访问权限的企业客户。

OpenAI 表示，Astra 将在“未来几天内”向 Plus、Pro、Business 和 Enterprise 用户以及通过 OpenAI API 和 AWS 的用户推出。

Pro、Business 和 Enterprise 用户也将获得 GPT-6 Astra Pro 的访问权限，符合条件的 API 客户将能够使用具备“零数据留存”（Zero Data Retention）功能的 Astra。

## 成本

一旦在 API 中可用，Astra 的价格将为每百万输入 Token 10 美元，每百万输出 Token 50 美元。这比 [Sol 当前的促销价格](https://developers.openai.com/api/docs/models/gpt-5.6-sol) 高出 2.5 倍，尽管这与 Anthropic 的 [Fable 5.1](https://www.anthropic.com/claude/fable) 定价持平。

这远高于 [Muse](https://developer.meta.com/ai/models/muse-spark/) 每百万输入 Token 1.25 美元和每百万输出 Token 4.25 美元的标准价格。Meta 还提供价格分别为 0.10 美元/0.20 美元的贡献者版本，但表示该层级的数据可能[被用于改进其产品](https://developer.meta.com/ai/products/meta-model-api/)。Google 对 [Gemini 3.8 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) 的入门定价为 0.75 美元/3.75 美元。

如果模型在更少的步骤内完成工作并需要更少的重试，更高的单位 Token 价格并不一定意味着更高的账单。OpenAI 表示，Astra 在多项评估和合作伙伴测试中使用了更少的 Token。目前的发布数据还不足以证明这些节省是否能抵消价格溢价。

“任务单价才是关键，” Brockman 说。

与 GPT-5.6 不同，OpenAI 尚未宣布 GPT-6 的 Luna、Terra 和 Sol 版本。目前，产品阵容仅包括 Astra 和 Astra Pro。

## Astra 的领先领域与局限

OpenAI 表示，除非另有说明，否则其评估中的模型均以最大努力模式运行。这可以改善基准测试结果，但也可能增加延迟和 Token 使用量。

Astra 在 DeepSWE v1.1 的测试结果比 OpenAI 之前的模型有了明显的改进。它在 113 项代理编程测试中得分 74.1%，而 Sol 的得分为 70.8%。

但本周早些时候，Meta [报告称](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology) Muse Spark 1.3 在最大推理设置下达到了 75.4%。Muse 1.3 现已可用，但其最大设置处于安全审查中，发布时不会向公众开放。

这对 Meta 来说是一个令人惊讶的胜利。在如此规模的基准测试中，1.3 个点的差异大致相当于一两个任务的差距，但这依然显示了 Meta 的进步幅度。

[公开的 DeepSWE 排行榜](https://deepswe.datacurve.ai/) 目前显示 Gemini 3.8 Flash 和 Claude Opus 5 的得分为 74%，Sol 为 73%。由于报告的不确定性范围存在重叠，这些结果并未确定明确的领导者。OpenAI 的图表排除了 Muse，并使用了 67.4% 的 Fable 5.1 结果，这使得 Astra 的优势看起来比更广泛的结果集所显示的要大。

## Astra 在编码之外的更大进展。

最突出的是它在 ARC-AGI-3 测试中获得了 98.6% 的得分。OpenAI 使用了一个可在轮次间保留推理能力并使用压缩技术来管理长上下文的 Responses API 框架来运行 Astra。该公司此前已证明，这些系统选择可以在不改变底层模型的情况下大幅[提高 ARC-AGI-3 分数](https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/)，该基准测试同时衡量 Astra 和 OpenAI 的代理系统。

Astra 在 FrontierMath Tier 4 的 97.6% 分数似乎涵盖了该层级 43 个问题中的 41 个私有问题。负责运行该基准测试的 [Epoch AI](https://epoch.ai/benchmarks/frontiermath-tier-4-v2) 表示，OpenAI 资助了其开发并拥有部分独家访问权，这一点值得注意。

![](https://cdn.thenewstack.io/media/2026/09/358eb84a-screenshot-2026-09-03-at-10.51.35-am-1024x880.png)

来源：OpenAI。

在 BenchCAD 的 1,000 文件 Vision2Code 子集（使用 Python 工具）测试中，Astra 得分 95.9%，而 Fable 5.1 为 84.3%，Sol 为 83.3%。[BenchCAD](https://benchcad.com/news.html) 要求模型根据渲染视图重建 CAD 程序，并对生成的 3D 模型的几何重叠度进行评分。OpenAI 指出，Claude 的结果使用了修改后的评估设置，但与 Sol 相比的差距依然显著。

在 Terminal-Bench Science 任务中，该任务要求代理在五个科学领域完成 70 项命令行研究任务，OpenAI 报告 Astra 的得分为 64.6%。Anthropic 报告 Fable 5.1 为 52.6%，而现有的 [公开排行榜](https://www.tbench.ai/news/terminal-bench-science-0-1) 中 Opus 5 的最高得分为 30%。

Anthropic 在其 [Fable 5.1 发布公告](https://thenewstack.io/anthropic-fable-5-1-launch/) 中也将大量篇幅投入到了科学领域，包括由 Mythos 5.1（具有较少安全限制的相同底层模型）设计的蛋白质结合剂的早期湿实验室结果。两家公司都在努力使其模型超越回答科学问题的范畴，进入研究工作流。

## Codex 有何变化？

对于开发者而言，Astra 处理超出上下文窗口任务的能力可能比基准测试的提升更为重要。

Codex 目前依赖于压缩，即总结之前的工作以释放上下文空间。该过程可能会丢弃代理稍后可能需要的细节：为什么之前的修复失败了、运行了哪些测试，或者用户在工作开始时添加了哪些细微要求。

Astra 则可以在上下文窗口中记笔记，并搜索之前的消息和工具输出。该功能目前处于实验阶段，隐藏在 `config.toml` 设置中。OpenAI 表示，在未来几周内，它将成为 Astra 的默认设置。

Astra 还可以向用户提问，而无需停止不依赖该答案的工作。这防止了单个未决决策阻塞剩余工作的完成，这是编码代理的一种常见故障模式。

OpenAI 展示了 Astra 操作包括 KiCad、Excel、Blender 和 Power BI 在内的应用程序，以及执行基于浏览器的表单输入和网站质量保证测试。

在测试桌面应用程序工作的 OSWorld V2-Offline 基准测试中，OpenAI 表示 Astra 得分为 72.6%，高于 GPT-5.6 Sol 的 65.7%。它还将每个任务的平均时间从约 75 分钟缩短到了 40 分钟。

Anthropic 报告称 Fable 5.1 的得分更高，为 77.9%，但[表示该测试使用了不同的 OSWorld 版本](https://www.anthropic.com/claude/fable)，不应与先前发布的分数进行比较。

OpenAI 还更改了 Codex 框架。在 Mind2Web 上，Astra 和新框架完成任务的速度比当前的 Sol 设置快 1.9 倍。

## 能力更强，但更难监控

OpenAI 声称 Astra 是其最对齐的模型，部分依据是一项内部测试：在不可能任务场景中，Astra 超出授权目标的比例为 0%，而 Sol 为 48.2%。

OpenAI 将旧模型描述为“在没有生产安全保障的情况下”运行；然而，它并没有足够清晰地说明周围安全设置的作用，以进行直接比较。

该公司还披露，在专门为诱导监控规避而设计的评估中，Astra 的书面推理比 Sol 更难监控。OpenAI 将这种下降部分归因于 Astra 在简单任务上对书面推理拥有更大的控制权，并以更少的书面推理步骤完成了问题。

“智能的进步并不保证对齐的进步，” OpenAI 首席科学家 Jakub Pachocki 表示。他补充说，OpenAI “将在我们能够恢复对监控未来模型能力的足够信心之前，暂缓扩展规模。”

## 网络安全功能伴随更严格的访问限制

OpenAI 表示，Astra 已跨越了其准备框架（Preparedness Framework）中的关键网络安全阈值。在公司测试中，该模型开发了针对加固浏览器和操作系统的漏洞利用程序。在 OpenAI 评估其针对近期 V8 漏洞的表现时，它还发现了两个此前未知的漏洞。该公司表示正在向维护者披露这些信息。OpenAI 表示，其报告的网络安全结果反映了对 Daybreak Blue 的访问，而非 Astra 的默认生产配置。

OpenAI 将 ExploitBench 和 ExploitGym 描述为测试模型是否能将已知软件漏洞转化为可用利用程序的手段。在 ExploitGym 上，Astra 得分为 42.4%，高于 Sol 的 30.3%，但 OpenAI 取消了两个模型通常的六小时时间限制。

在 [ExploitBench](https://exploitbench.ai/) 上，模型的得分均为 100%。

OpenAI 指出，通过标准访问提供的 Astra 版本将拒绝执行一些高级网络安全工作，包括漏洞利用发现。

OpenAI 正在通过 Daybreak 为一组经过审查的防御者提供限制较少的访问权限，并表示将在未来几周内通过 [Daybreak Blue](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/) 扩展 Astra 访问权限。Daybreak Blue 是一个针对授权防御工作的访问计划，而不是一个单独的 Astra 模型或推理模式。

对于使用 API 的开发者，网络安全检查将直接停止任务，而不是暂停并等待批准。

OpenAI 的 Mia Glaese 还警告称，其信任访问计划之外的用户在执行网络安全工作时——有时甚至是在进行无关工作时——可能会遇到减速、暂停或拦截的情况。当然，这在最近的许多模型发布中都是一个问题，但对用户来说确实令人沮丧。

“在发布时，这是人们应该预料到的情况，” 她说。