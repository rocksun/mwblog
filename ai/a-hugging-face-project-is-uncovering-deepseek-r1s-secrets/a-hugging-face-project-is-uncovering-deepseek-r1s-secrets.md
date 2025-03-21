<!--
title: Hugging Face项目正在揭示DeepSeek-R1的秘密
cover: https://cdn.thenewstack.io/media/2025/03/609ba3c6-solen-feyissa-ipskq4kllkg-unsplashb.jpg
summary: Hugging Face揭秘DeepSeek-R1，开源社区迎来新突破！通过Open-R1项目，复现DeepSeek的训练流程，探索数据收集、模型训练和Scaling Laws。已发布Open-R1-Math-220k数学推理数据集和代码编程数据集，并推出OlympicCoder 7B/32B模型，性能超越Claude Sonnet！关键技术包括MTP、MLA、GRPO和RLHF等。
-->

Hugging Face揭秘DeepSeek-R1，开源社区迎来新突破！通过Open-R1项目，复现DeepSeek的训练流程，探索数据收集、模型训练和Scaling Laws。已发布Open-R1-Math-220k数学推理数据集和代码编程数据集，并推出OlympicCoder 7B/32B模型，性能超越Claude Sonnet！关键技术包括MTP、MLA、GRPO和RLHF等。

> 译自：[A Hugging Face Project Is Uncovering DeepSeek-R1’s Secrets](https://thenewstack.io/a-hugging-face-project-is-uncovering-deepseek-r1s-secrets/)
> 
> 作者：Loraine Lawson

根据 [Jeff Boudier](https://www.linkedin.com/in/jeffboudier/) 的说法，[DeepSeek-R1](https://www.deepseek.com/) 的发布对 AI 领域来说是一个巨大的警钟，[Jeff Boudier](https://www.linkedin.com/in/jeffboudier/) 是 [Hugging Face](https://huggingface.co/) 的产品和增长负责人。

Boudier 说：“这个警钟是，为了获得尽可能最好的 AI，你不需要依赖 OpenAI、Anthropic、Google 等公司的封闭模型。”“你可以从 DeepSeek 这里访问一个具有类似功能的开放模型，它来自一个以前不太为人所知的研究实验室。”

[Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) 是一家为 [开源](https://thenewstack.io/making-good-on-the-promise-of-open-source-ai/) [大型语言模型 (LLM)](https://thenewstack.io/what-is-an-llm-token-beginner-friendly-guide-for-developers/) 提供存储库中心和社区的公司。它很快就看到了 DeepSeek-R1 的影响，DeepSeek-R1 [托管在该平台上](https://huggingface.co/deepseek-ai/DeepSeek-R1)。

Boudier 告诉 The New Stack：“有趣的是，这不仅仅是对普通大众的一个重大公告，它还在 AI 社区内引发了一系列活动，我们直接在 Hugging Face 上看到了这一点。”“[今天发布的 R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) —— 在 Hugging Face 上的下载量超过 1000 万次，这仅仅是过去 30 天的数据。”

## DeepSeek 如何改变 AI

[DeepSeek 创建了非常高效的模型，可以在功能较弱的硬件上运行](https://thenewstack.io/how-to-run-deepseek-models-locally-on-a-windows-copilot-pc/)。这在 AI 领域是不寻常的，以至于当其 R1 模型在 1 月份发布时，[它引发了 NVIDIA 的股票下跌](https://finance.yahoo.com/news/nvidia-stock-plummets-loses-record-589-billion-as-deepseek-prompts-questions-over-ai-spending-135105824.html)，[NVIDIA](https://thenewstack.io/after-deepseek-nvidia-puts-its-focus-on-inference-at-gtc/) 生产图形处理单元 (GPU)，其他 AI 系统依赖于这些 GPU。

DeepSeek 还使用了多个 [神经网络，而不是依赖于单个“通用”模型](https://thenewstack.io/who-needs-neural-networks-the-generative-prowess-of-state-transition-models/)。此外，与其他生成 AI 模型相比，它的训练成本很低，仅为 550 万美元，“这要归功于架构上的变化，例如 [Multi-Token Prediction (MTP)](https://arxiv.org/abs/2502.09419)、[Multi-Head Latent Attention (MLA)](https://arxiv.org/abs/2502.07864) 以及大量的（真的，大量的）硬件优化，”[Hugging Face 的研究人员在一篇博客文章中写道](https://huggingface.co/blog/open-r1)。

[Hugging Face 上的 DeepSeek 组织](https://huggingface.co/deepseek-ai) 也是该网站上关注者最多的组织，拥有超过 45,000 名关注者。这比 Google、Microsoft 或其他大型 AI 参与者还要多。他补充说，现在该中心有数千个 DeepSeek 模型衍生品。

它还改变了那些想要使用 AI 的组织的游戏规则。现在，组织可以下载在 [MIT 许可证](https://opensource.org/license/mit) 下发布的开源 DeepSeek，并将其托管在本地。

Boudier 说：“如果你是一家企业，你不再需要像 OpenAI 或其他公司那样将你的客户数据发送到 API。”“你实际上可以将所有内容都托管在内部。而且它也获得了 MIT 许可，因此你可以将其用于任何商业目的。这真的非常强大。”

## Open-R1 项目

DeepSeek 不仅仅发布了其开源 R1 和 R1-Zero 模型——这家中国公司还发布了一份 [技术报告](https://github.com/deepseek-ai/DeepSeek-R1/blob/main/DeepSeek_R1.pdf)，该报告“在他们分享的知识以及他们如何使用强化学习技术和一些技巧创建 R1 和 R1-Zero 模型方面非常慷慨”，Boudier 解释说。

他补充说，技术报告中描述的技术已在 Hugging Face 库中实现，因此世界各地的研究实验室都可以使用它们。这包括诸如 [Generative Reasoning and Planning Optimization (GRPO)](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/) 等技术，这些技术使 AI 能够思考完成更复杂的任务，然后随着时间的推移进行改进。

但 Boudier 说，DeepSeek 的研究中缺少一些内容。

他说：“该技术报告没有解释或描述用于训练和对齐 R1 模型的 [训练数据](https://thenewstack.io/dealing-with-distributed-data-when-training-ai-models/)。”“它没有描述提炼过程。”

具体来说，Hugging Face 的一个研究团队指出，该报告留下了关于以下问题：
- 数据收集，例如如何管理特定于推理的数据集。
- 模型训练。研究人员表示：“DeepSeek 没有发布任何训练代码，因此无法得知哪些超参数效果最佳，以及它们在不同模型系列和规模上的差异。”
- 缩放定律。Hugging Face 的研究人员问道：“在训练推理模型时，计算和数据之间如何权衡？”

这些问题促成了 [Open-R1 项目](https://huggingface.co/open-r1)的创建，该项目旨在系统地重建 DeepSeek-R1 的数据和训练流程，验证其声明，并“突破开放推理模型的界限”，研究人员写道。

他们表示：“通过构建 Open-R1，我们旨在提高强化学习如何增强推理的透明度，与开源社区分享可复现的见解，并为未来的模型利用这些技术奠定基础。”

Hugging Face 的研究人员概述了他们针对 Open-R1 的“攻击计划”：

- 通过从 DeepSeek-R1 中提取高质量的推理数据集来复制 R1-Distill 模型。
- 复制 DeepSeek 用于创建 R1-Zero 的纯 RL 流程。这将涉及管理新的、大规模的数学、推理和代码数据集。
- 证明他们可以通过多阶段训练从基础模型 → SFT → RL。

复制 DeepSeek-R1 流程使研究实验室能够经历与 DeepSeek 创建 DeepSeek-R1 和 DeepSeek-R1-Zero 时完全相同的过程，这些模型是从基础模型 DeepSeek-V3 中提取的推理模型。

## Open-R1 的目的

Open-R1 的目的不是创建新的模型本身，而是创建和免费发布工件。

DeepSeek 发布的研究所缺少的一个环节是，如何从一个拥有通用知识并在数万亿个 token 上训练的大型预训练模型，转变为一个非常擅长特定领域的模型。

关键是创建由这个“非常有能力的模型”在[特定领域](https://thenewstack.io/domain-specific-ai-aiseras-answer-to-enterprise-needs/)和问题上进行推理而产生的推理轨迹，Jeff Boudier 说。推理轨迹是指 AI 系统为得出结论或做出决策而采取的步骤的记录或日志。可以将其视为记录 AI 的“思考过程”。

> “实际上，您可以将所有内容都托管在内部。而且它也获得了 MIT 许可，因此您可以将其用于任何商业目的。这非常非常强大。”
>
> — Jeff Boudier, Hugging Face 产品和增长负责人

在 DeepSeek-R1 和 R1-Zero 的案例中，推理是针对特定领域的，而不是针对整个互联网。

Boudier 解释说：“你可以采用一个模型，然后通过提炼来教它非常非常擅长这种特定类型的任务”，通过推理轨迹。

这就是 [Hugging Face 团队在其第二次更新中发布的内容](https://huggingface.co/blog/open-r1/update-2)——一个名为 [Open-R1-Math-220k](https://huggingface.co/datasets/open-r1/OpenR1-Math-220k) 的数学推理轨迹数据集，其中包含超过 200,000 个复杂数学问题的推理轨迹。

该团队在谈到数学数据集时表示：“这些合成数据集将使每个人都可以通过简单地对其进行微调，将现有或新的 LLM 微调为推理模型。涉及 RL [强化学习] 的训练方法将作为任何人从头开始构建类似模型的起点，并将使研究人员能够[在此基础上构建更高级的方法](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/)。”

探索其他领域，包括代码以及医学等科学领域，都具有很大的潜力，“在这些领域，推理模型可能会产生重大影响”，他们表示。

## 最新版本

[Open-R1 项目刚刚发布了其第三次更新](https://huggingface.co/blog/open-r1/update-3)，Boudier 称其为“迄今为止最令人兴奋的更新”。

它包括一个代码编程数据集，其中包含从 DeepSeek R1 获得的超过 100,000 个事件编程推理轨迹。该数据集可用于训练新模型，以更好地理解代码的细微差别，从而使 AI 模型能够解释代码背后的推理。由此，该团队构建了 [OlympicCoder 70 亿](https://huggingface.co/open-r1/OlympicCoder-7B) 和 [320 亿参数模型](https://huggingface.co/open-r1/OlympicCoder-32B)。
Boudier 说：“真正令人兴奋的是，通过应用他们从 R1 论文和 R1 版本中重新创建的蒸馏管道，他们能够创建这些非常非常强大的模型。”“为了让您了解，这个 320 亿参数的模型胜过了 [Claude Sonnet](https://thenewstack.io/making-the-fediverse-more-accessible-with-claude-3-7-sonnet/)，后者是 [Anthropic](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/) 针对高级编程挑战的最先进模型。”

该团队还发布了一个新的 [IOI 基准](https://github.com/huggingface/ioi)——基于年度编程竞赛国际信息学奥林匹克竞赛——以提供一种衡量模型解决更具挑战性的编程问题能力的新方法。