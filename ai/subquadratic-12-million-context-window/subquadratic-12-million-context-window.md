<!--
title: 上下文窗口已被粉碎：Subquadratic 首次推出 1200 万 token 窗口模型
cover: https://cdn.thenewstack.io/media/2026/05/d2090430-screenshot-2026-05-05-at-10.02.53.png
summary: 迈阿密初创公司 Subquadratic 发布了拥有 1200 万 token 上下文窗口的新模型，采用其创新的 SSA 架构实现了线性成本缩放。该模型在处理速度和检索准确率上均超越了 GPT-5.5 等模型。
-->

迈阿密初创公司 Subquadratic 发布了拥有 1200 万 token 上下文窗口的新模型，采用其创新的 SSA 架构实现了线性成本缩放。该模型在处理速度和检索准确率上均超越了 GPT-5.5 等模型。

> 译自：[The context window has been shattered: Subquadratic debuts a 12-million-token window](https://thenewstack.io/subquadratic-12-million-context-window/)
> 
> 作者：Frederic Lardinois

2026 年的每一个前沿模型都宣传拥有至少一百万 token 的上下文窗口，但几乎没有一个模型能真正很好地利用所有这些信息。在多引用检索基准实验室报告 [MRCR v2](https://arxiv.org/html/2409.12640v2) 上，表现最好的模型是 [GPT-5.5，得分为 74.0%](https://openai.com/index/introducing-gpt-5-5/)。而像 Claude Opus 4.7 仅为 32.2%，远远落后。

目前，一百万 token 似乎是主要前沿实验室提供的上下文窗口上限。一百万 token 上限的一个主要原因，与自 [2017 年](https://arxiv.org/abs/1706.03762)以来塑造每个基于 Transformer 的模型的原因相同：注意力机制的成本随上下文长度呈二次方增长，因此输入增加一倍，工作量就会增加四倍。本质上，RAG（检索增强生成）、智能体分解、混合模型架构以及业界构建的每一种其他变通方法，都是为了绕过这一问题而进行的折衷。

总部位于迈阿密的初创公司 [Subquadratic](https://subq.ai/) 在周二发布了其第一个模型，并声称可以解决所有这些问题，现在提供了一个可以处理 1200 万 token 窗口的模型。此外，该公司表示计划很快提供一个具有 5000 万上下文窗口的模型。

![](https://cdn.thenewstack.io/media/2026/05/48f5e0d1-screenshot-2026-05-05-at-09.54.30-1024x602.png)

这家拥有 11 名博士研究员的公司辩称，其名为亚二次选择性注意力（SSA）的架构在计算和内存方面相对于上下文长度呈线性缩放。该公司表示，在一百万 token 时，它的运行速度比稠密注意力快 52 倍；在 1200 万 token 时，其大海捞针检索率达到 92.1% —— 这是目前任何前沿模型都无法企及的上下文长度；并且在 MRCR v2 上得分为 83，领先 OpenAI 9 个百分点。

> 该公司表示，其亚二次选择性注意力架构在一百万 token 时的运行速度比稠密注意力快 52 倍，在 1200 万 token 时的大海捞针检索率达到 92.1%，并在 MRCR v2 上获得 83 分，超过 OpenAI 9 分。

这些都是宏大的声明，而 Subquadratic 并不是第一个尝试解决这个问题的公司。该公司发布的基准测试结果令人印象深刻，包括在 SWE-bench 上获得 82.4% 的分数，超越了 Anthropic 的最新模型 [Opus 4.6](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/)（得分为 81.42%）和 [Google 的 Gemini 3.1 Pro](https://thenewstack.io/googles-gemini-3-1-pro-is-mostly-great/)（得分为 80.6%）。而且它在实现这一切的同时，成本显著降低。

Subquadratic 正通过 API 提供该模型 —— 该 API 将具备 1200 万 token 的上下文窗口 —— 以及一个编码智能体（SubQ Code）和一个深度研究工具（SubQ Search）。

## 前人的探索

注意力机制的二次方成本显然不是一个新问题，SSA 也不是解决它的第一次尝试。研究路线几乎可以追溯到最初的 Transformer 论文，整体模式保持一致。每种方法都牺牲了一个必要的属性来换取另一个属性，但没有一种方法能够在前沿规模上取代稠密注意力。

> 每种方法都牺牲了一个必要的属性来换取另一个属性，但没有一种方法能够在前沿规模上取代稠密注意力。

在不同的方法中，例如有固定模式的稀疏注意力。在像 [Longformer](https://arxiv.org/abs/2004.05150) 这样的模型中，它通过让每个 token 仅关注滑动窗口来实现线性缩放。当相关信息位于附近时它有效，而当信息不在此处时就会失效。

像 [Mamba](https://arxiv.org/abs/2312.00752)、Mamba-2、[RWKV](https://arxiv.org/abs/2305.13048)、[RetNet](https://arxiv.org/abs/2307.08621) 这样的状态空间模型（SSM）用一个压缩了目前为止所见所有内容的循环状态取代了全对比较。然而，这种压缩是有损的。Nvidia 在 8B 规模下的研究发现，纯 Mamba-2 [在 MMLU 和电话簿查找方面落后于 Transformer](https://ea-crux-project.vercel.app/knowledge-base/intelligence-paradigms/ssm-mamba/)，只有在重新加入注意力机制后，差距才会缩小。

混合架构，如 [Jamba](https://arxiv.org/abs/2403.19887)、[Kimi Linear](https://arxiv.org/abs/2510.26692)、[Qwen3-Next](https://qwenlm.github.io/blog/qwen3_next/) 和 Nvidia 的 Nemotron v3 所见，是对此的务实回答。它们保持大多数层的高效，并保留几个稠密注意力层用于检索。但经济效益并不像看起来那么理想。一个在 32K token 时便宜三倍的混合模型，在 10M token 时仍然只便宜三倍，因为它保留的稠密层仍然在做 O(n²) 的工作。

最近的参与者转向了不同的方向。他们不再试图修复模式或压缩状态，而是学习该关注哪些位置。

例如，DeepSeek 的 [原生稀疏注意力（Native Sparse Attention）](https://arxiv.org/abs/2502.11089) 获得了 ACL 2025 最佳论文奖。其继任者 DeepSeek 稀疏注意力（DSA）正应用于 [DeepSeek V3.2-Exp.](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp) 中。DSA 的闪电索引器将注意力引导到一小部分选定的键上，对这些键的注意力确实是稀疏的。然而，挑选它们的索引器必须对每个查询与每个键进行评分，这意味着选择步骤本身就是二次方的。

SubQuadratic CTO [Alex Whedon](https://www.linkedin.com/in/alexander-whedon/) 告诉 *The New Stack*：“稀疏注意力基本上意味着，不再像 Transformer 那样（如果你有 1,000 个词，你就查看这 1,000 个词之间所有可能的联系，即 1,000 的平方种组合），而是意识到其中只有一部分真正重要，你只处理重要的那部分。”

## SSA 声称的不同之处

SSA 的卖点在于，它实现了 DSA 试图实现的目标，但没有陷入索引器陷阱。选择是内容相关的。对于任何给定的查询，模型会根据查询和键实际包含的内容来挑选哪些位置重要 —— 最重要的是，选择机制本身不会变成二次方。

“对于提示词 A，词 1 和词 6 相互之间可能很重要，” Alex Whedon 说，“对于提示词 B，也许是词 2 和词 3。每个输入都是不同的。”

根据 Alex Whedon 的说法，混合模型提供的是“标量收益”，但纯亚二次机制提供的是缩放定律优势。根据基准测试，SubQ 在 128K 时速度提升了 7.2 倍，在 1M 时提升了 52.2 倍。

## 基准测试

在 128K 的 [RULER](https://arxiv.org/abs/2404.06654) 测试中，SubQ 的得分为 97.1，而 Opus 4.6 为 94.8。在 MRCR v2 上，它与前沿模型其余部分的差距，比其余部分与它自身的差距还要大。

在 [SWE-Bench Verified](https://www.swebench.com/) 上，SubQ 报告的分数为 82.4%，略高于 Opus 4.6 的 81.4% 和 Gemini 3.1 Pro 的 80.6%。在没有前沿模型运行的 1200 万 token 规模下，SubQ 在大海捞针基准测试中保持了 92.1% 的准确率。

但也存在一些注意事项。根据技术论文，由于推理成本较高，每个模型仅运行了一次。正如论文所承认的，SWE-Bench 的领先优势“既取决于测试环境，也取决于模型”。而且按 Alex Whedon 自己的描述，SubQ 模型“比大实验室的模型小得多”。

## Subquadratic 目前发布的产品

该公司正在推出两个测试版产品：一个暴露完整 12M token 窗口的 API，以及一个基于同一模型构建的命令行界面（CLI）智能体 SubQ Code。两者都运行在云服务商而非主要超大规模运营商之上 —— “他们非常昂贵，”首席执行官 Justin Dangel 表示。

该公司目前没有开源权重，但计划为企业提供训练工具，以便进行后续训练。5000 万 token 上下文窗口的目标设定在第四季度。

不过，这里有一个前车之鉴。Magic.dev 在 2024 年 8 月宣布了一个 1 亿 token 上下文窗口的模型，并[声称具有 1000 倍的效率优势](https://magic.dev/blog/100m-token-context-windows)。它凭借这一实力筹集了超过 [5 亿美元](https://magic.dev/blog/100m-token-context-windows)。截至 2026 年初，[尚无公开证据](https://codingscape.com/blog/llms-with-largest-context-windows)表明 LTM-2-mini 在 Magic 之外被使用。

## 融资情况

Subquadratic 至今已以 5 亿美元的估值筹集了 2900 万美元，投资者包括前软银愿景基金合伙人 Javier Villamizar 和 Tinder 联合创始人 Justin Mateen。该公司之前名为 [Aldea](https://aldea.ai/)，在转型前从事语音模型研究。技术案例是真实的，而该类别的历史记录则是故事的另一部分。