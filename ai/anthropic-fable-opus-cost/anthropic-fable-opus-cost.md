<!--
title: 当价格更高的模型反而更省钱
cover: https://cdn.thenewstack.io/media/2026/11/9c59d8b3-imhaf-maulana-4r2mctrudkm-unsplash-1024x745.jpg
summary: Anthropic发布了性能超越Opus 5.5的新编码模型Fable 5.2。尽管单Token价格更高，但其执行复杂任务的整体成本更低，并能充当多智能体架构的协调者。开发人员或可调整策略，更早切换到该模型以实现降本增效。
-->

Anthropic发布了性能超越Opus 5.5的新编码模型Fable 5.2。尽管单Token价格更高，但其执行复杂任务的整体成本更低，并能充当多智能体架构的协调者。开发人员或可调整策略，更早切换到该模型以实现降本增效。

> 译自：[When pricier runs cheaper](https://thenewstack.io/anthropic-fable-opus-cost/)
> 
> 作者：Amanda Caswell

Anthropic 刚刚[发布了一款编码模型](https://thenewstack.io/anthropic-fable-coding-upgrade/)，在两个主要基准测试中击败了 Opus 5.5，并且能够以一半的成本完成某些困难的任务。

然而，在周一的 [Fable 5.2 公告](https://www.anthropic.com/claude-fable-and-mythos-5-2)中，该公司建议大多数开发人员坚持使用 Opus，称其为编码和知识工作的“最强日常主力”。

Anthropic 告诉 *The New Stack*：“基于功能和定价，Claude Opus 5.5 仍然是我们推荐用于大多数日常工作的模型，从编码到知识工作。”

> “基于功能和定价，Claude Opus 5.5 仍然是我们推荐用于大多数日常工作的模型，从编码到知识工作。”

Anthropic 表示，Fable 旨在用于大型软件迁移、多智能体构建和长时间运行的研究，但其性能数据使得这一推荐变得复杂。更昂贵的模型在完成某些任务时可能会花费更少，该公司提出的多模型架构增加了关于任务委派、上下文管理和执行成本的考量。

## 当价格更高的模型反而更省钱

根据 Anthropic 的数据，在 FrontierCode 2.0 上，处于高努力程度下的 Fable 5.2 得分为 45.3%，几乎与 Opus 5.5 的最高结果 45.5% 持平，同时完成基准测试任务的成本大约只有一半。

Fable 的每个 Token 价格是 Opus 的两倍（每百万输入 Token 8 美元，每百万输出 Token 40 美元，而 Opus 分别为 4 美元和 20 美元），但其报告的任务成本却更低，这表明仅凭 Token 定价并不能决定哪个模型更经济。

Anthropic 还引用了一项内部实验：1,000 个 Fable 5.2 智能体在 30 小时内完成了费马大定理的形式化。根据该公司公布的结果，在相同的智能体配置下，Opus 5.5 在 18 小时后仅完成了 26%，并且在 30 小时大关时几乎没有取得进一步的进展。

该实验展示了 Anthropic 针对 Fable 的工作规模，尽管它并未证实这种优势有多少能延续到较小的部署或常规编码工作负载中。

## 模型管理器模式

该公司还将 Fable 定位为低成本模型的协调器，因此开发人员可以为其他模型无法可靠完成的工作保留推理能力。

> “Fable 5.2 可以充当一个协调器，将更简单的任务委派给 Opus 5.5 或 Sonnet 5.5，或者作为这些模型在遇到更难问题时咨询的顾问。”

Anthropic 告诉 *The New Stack*：“开发人员也不再只需要选择一个模型，Fable 5.2 可以充当一个协调器，将更简单的任务委派给 Opus 5.5 或 Sonnet 5.5，或者作为这些模型在遇到更难问题时咨询的顾问。”

对于大型软件迁移，Fable 可以分析依赖关系，规划跨服务的更改，并将各个实现任务委派给 Opus 或 Sonnet。然后，可以将更困难的决策升级回 Fable，而不需要更昂贵的模型来执行每一步。

Coinbase 已经[构建了多模型基础设施](https://thenewstack.io/multi-model-ai-infrastructure/)，根据需求和成本路由任务，该公司表示，即使 Token 使用量增加，其内部 AI 支出也减少了近一半。

Anthropic 希望 Fable 能够自行处理部分路由决策，尽管任何节省都取决于更便宜的模型在不需要帮助的情况下完成分配工作的频率，因为在长时间运行的智能体任务过程中，额外的模型调用、上下文传输和失败的尝试会[推高成本](https://thenewstack.io/agentic-ai-token-costs/)。

## 上下文切换税

当开发人员在对话过程中在不同模型之间切换时，还有一个复杂的情况。[Fable 5.2 可以读取 Opus 5.5 生成的思考块](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2/)，但 Opus 无法读取 Fable 生成的思考块。

这意味着在构建在模型之间转移工作的系统时，必须找到另一种传递相关上下文的方法，这可能需要额外的更昂贵的 Token，更不用说会蚕食使用更便宜模型所节省的费用了。

## 更早切换，节省更多

Anthropic 建议从 Opus 开始，当更高努力程度的 Opus 评估无法满足项目的要求时再转向 Fable，这提供了一种基于功能的切换规则，但该规则不一定考虑了最低的总执行成本。

其 FrontierCode 结果显示 Fable 以大约一半的任务成本实现了可比的性能，因此开发人员很可能从比 Anthropic 建议的更早切换中受益。

> 其 FrontierCode 结果显示 Fable 以大约一半的任务成本实现了可比的性能，因此开发人员很可能从比 Anthropic 建议的更早切换中受益。