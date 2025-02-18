# 深入探究DeepSeek-R1：其工作原理和功能

![DeepSeek-R1：其工作原理和功能的特色图片](https://cdn.thenewstack.io/media/2025/02/b0f86eb2-pexels-uma-media-2149408028-30608379-1024x576.jpg)

最近发布的[DeepSeek R-1](https://github.com/deepseek-ai/DeepSeek-R1/blob/main/DeepSeek_R1.pdf)是一款中国大型语言模型，据称其推理能力与[OpenAI的o1 LLM](https://openai.com/o1/)不相上下，但训练成本约为600万美元——仅为训练[OpenA1的o1](https://thenewstack.io/openais-realtime-api-takes-a-bow/)大约1亿美元成本的一小部分。其发布后仍在持续引发关注。

值得注意的是，R1模型的权重和推理代码已分别在[Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-R1)和[GitHub](https://github.com/deepseek-ai/DeepSeek-R1)上公开发布，但训练代码和训练数据本身尚未公开。尽管DeepSeek似乎正在成为一个[开源成功案例](https://thenewstack.io/icymi-deepseek-is-an-open-source-success-story/)，但[由此引发的股市和更广泛的AI行业震荡](https://finance.yahoo.com/news/what-big-tech-execs-have-said-about-deepseek-as-us-contemplates-ban-140030220.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAG0ESvLn2vdGKx8BtC4WYJzfD7B1Sg9zRXuJKGUj5J99jeQyh2YeolPH5F5WkAifXQIaLBBoSEiSrZBnZv6lSOcSWI_7OKLcUOyUULFc5lUS8PRFzd9DBnXBoT9mP6bWqtsZWr2h1zCJefAOWuFNaX5uxrgQJw4mKhRn5BK3KnPl)暗示了大型语言模型领域潜在的范式转变。

那么，DeepSeek-R1是如何工作的？它有什么能力？它有哪些潜在的缺陷？让我们深入了解其模型架构、功能和缺点。

## DeepSeek-R1的模型架构

以下是我们了解到的架构：
**专家混合模型:** DeepSeek-R1 使用专家混合模型 (MoE) 架构，该架构将模型划分为多个“专家”子网络，每个子网络擅长处理输入数据的子集。这意味着只有在执行任务时才会激活模型的相关部分，从而降低计算资源的消耗。**门控和无损负载均衡:** DeepSeek 的 6710 亿参数的这种选择性激活是通过门控机制实现的，该机制动态地将输入导向合适的专家，从而提高计算效率，而不会影响性能或可扩展性。对于每个 token，在单次前向传递中仅激活 370 亿个参数，并使用诸如[无损负载均衡](https://medium.com/yugen-ai-technology-blog/deepseek-v3-advances-in-moe-load-balancing-and-multi-token-prediction-training-f6d68c59749c)之类的技术，这有助于确保所有专家子网络的使用均匀分布，以防止瓶颈。**上下文长度:** DeepSeek-R1 基于[DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) 的基础模型架构构建。两者都具有 128K 的上下文长度，这通过一种称为[YaRN](https://arxiv.org/abs/2309.00071)（另一种 RoPE 扩展）的技术扩展，该技术扩展了大型语言模型的上下文窗口。YaRN 是[旋转位置嵌入](https://medium.com/ai-insights-cobet/rotary-positional-embeddings-a-detailed-look-and-comprehensive-understanding-4ff66a874d83)(RoPE)的改进版本，这是一种使用旋转矩阵编码绝对位置信息的位置嵌入，YaRN 有效地内插了矩阵中这些旋转频率的缩放方式。这是一种提高模型上下文长度并增强更长上下文泛化能力的实用方法，无需代价高昂的重新训练。**层:** DeepSeek-R1 包含一个嵌入层以及 61 个 Transformer 层。Transformer 层上并没有使用典型的多头注意力 (MHA) 机制，前三层由创新的[多头潜在注意力 (MLA)](https://planetbanatt.net/articles/mla.html)层和标准的前馈网络 (FFN) 层组成。**多头注意力:** 团队表示，MLA 配备了低秩键值联合压缩，在推理过程中只需要更少的键值 (KV) 缓存，从而将内存开销降低到传统方法的 5% 到 13% 之间，并提供比 MHA 更好的性能。为了方便扩展、高效学习和降低计算成本，混合专家层取代了第 4 层到第 61 层的前馈网络 (FFN) 层。**多 token 预测:** 这是一种高级的语言建模方法，它并行预测序列中的多个未来 token，而不是一次预测一个后续词。最初由[Meta](https://about.meta.com/?utm_content=inline+mention) 引入的[多 token 预测](https://medium.com/@himankvjain/accelerating-language-models-with-multi-token-prediction-9f0167232f5b)(MTP) 使模型能够利用多个预测路径（也称为“头”），从而更好地预测 token 表示，并提高模型在基准测试中的效率和性能。

## DeepSeek-R1 的能力
DeepSeek-R1 在各种推理基准测试中展现了最先进的性能，尤其是在与数学和相关学科相关的题目中。在一些与数学相关的指标上，它被证明优于 OpenAI 的 o1。它擅长复杂的推理、问答和指令任务。特别是，以下功能的组合使 R1 与竞争对手区别开来。

![](https://cdn.thenewstack.io/media/2025/02/fe514e93-deepseek-r1-rl.png)

来自 adasci.org
**基于群体相对策略优化的强化学习:** DeepSeek-R1 基于之前的模型 [DeepSeek-V3-Base](https://huggingface.co/deepseek-ai/DeepSeek-V3-Base) 构建，采用多阶段训练，包括监督微调和基于 [群体相对策略优化](https://medium.com/@sahin.samia/the-math-behind-deepseek-a-deep-dive-into-group-relative-policy-optimization-grpo-8a75007491ba) 的强化学习。GRPO 专为增强推理能力和降低计算开销而设计，它无需外部“评论家”模型；而是相对评估各组响应。此功能意味着模型可以随着时间的推移逐步提高其推理能力，以获得奖励更高的输出，而无需大量标记数据。**奖励建模:**这种试错学习方法激励模型给出既正确又合理的答案。它通过在任务完成后分配“奖励信号”的形式反馈来实现这一点，从而帮助改进强化学习过程。**冷启动数据:**DeepSeek-R1 使用“冷启动”数据进行训练，这指的是一个最小标记、高质量的监督数据集，它可以“启动”模型的训练，使其快速获得对任务的一般理解。**思维链:**DeepSeek-R1 使用 [思维链](https://www.ibm.com/think/topics/chain-of-thoughts) (CoT) 提示来处理推理任务并进行自我评估。这通过指导模型以结构化的方式分解复杂问题来模拟类人的推理，从而使其能够逻辑地推导出连贯的答案，并最终提高其答案的可读性。**拒绝采样:**该模型还使用拒绝采样来剔除低质量数据，这意味着在生成不同的输出后，模型只选择满足特定标准的输出，用于进一步的微调和训练。**蒸馏:**使用精选的数据集，DeepSeek-R1已被蒸馏成更小、更开放的版本，这些版本性能相对较高，但运行成本更低，最值得注意的是使用了 Qwen 和 [Llama](https://thenewstack.io/get-started-with-metas-llama-stack-using-conda-and-ollama/) 架构。
![](https://cdn.thenewstack.io/media/2025/02/00f776e5-deepseek-r1-distilled-models.png)

来自“DeepSeek-R1：通过强化学习激励大型语言模型的推理能力”，[研究论文](https://github.com/deepseek-ai/DeepSeek-R1/blob/main/DeepSeek_R1.pdf)。

## 潜在缺陷
对于任何模型来说，都存在需要与整体性能和成本相权衡的缺陷。根据 [AppSOC](https://www.appsoc.com/blog/testing-the-deepseek-r1-model-a-pandoras-box-of-security-risks) 和 [Cisco](https://blogs.cisco.com/security/evaluating-security-risk-in-deepseek-and-other-frontier-reasoning-models) 的人工智能安全研究人员的说法，以下是 DeepSeek-R1 的一些潜在缺点，这表明在部署此模型时，强大的 [第三方安全和安全“护栏”](https://thenewstack.io/llm-integration-pitfalls-protecting-sensitive-data-in-the-ai-age/) 可能是一个明智的补充。

**安全性:**DeepSeek-R1 可能容易受到 [提示注入攻击](https://thenewstack.io/when-prompt-injections-attack-bing-and-ai-vulnerabilities/)，导致错误输出和潜在的系统受损。在测试中，DeepSeek-R1 表明它可能能够生成恶意软件，例如恶意脚本和代码片段。**安全性:**当使用 [越狱](https://www.kelacyber.com/blog/deepseek-r1-security-flaws/) 技术进行测试时，DeepSeek-R1 始终能够绕过安全机制并生成有害或受限制的内容，以及包含有害措辞的响应，这表明该模型容易受到算法越狱和潜在误用的影响。**幻觉:**DeepSeek-R1 可能容易 [生成虚假或捏造的答案](https://thenewstack.io/ai-agentic-evaluation-tools-help-devs-fight-hallucinations/)。

## 结论
尽管存在这些缺点，DeepSeek-R1 仍然展示了应用于大型语言模型的 [强化学习](https://www.ibm.com/think/topics/reinforcement-learning) 背后的奖励系统的潜在能力。

在 DeepSeek-R1 的训练过程中，很明显，通过奖励准确和连贯的答案，新生的模型行为，如自我反思、自我验证、长链推理和自主解决问题，都指向了随着时间推移而学习到的涌现推理的可能性，而不是公开教授的——因此可能为人工智能研究的进一步突破铺平了道路。

[YOUTUBE.COM/THENEWSTACK](https://www.youtube.com/c/thenewstack)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。
[https://youtube.com/thenewstack?sub_confirmation=1]