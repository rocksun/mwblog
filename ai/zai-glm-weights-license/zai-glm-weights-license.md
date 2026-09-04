<!--
title: Z.ai推出GLM-5.3开放权重模型，新许可协议剑指超大规模云服务商
cover: https://cdn.thenewstack.io/media/2026/08/af32fe00-hendi-perkasa-10d-dglurve-unsplash-scaled.jpg
summary: Z.ai发布的GLM-5.3模型已公开权重，但其新许可协议要求年营收超百亿美元的超大规模企业必须通过安全审查。此举被视为Z.ai在平衡模型安全性与商业变现，同时也反映了中美科技公司在模型生态控制权上的潜在博弈。
-->

Z.ai发布的GLM-5.3模型已公开权重，但其新许可协议要求年营收超百亿美元的超大规模企业必须通过安全审查。此举被视为Z.ai在平衡模型安全性与商业变现，同时也反映了中美科技公司在模型生态控制权上的潜在博弈。

> 译自：[Z.ai's GLM-5.3 goes open weight, but its new license aims at hyperscalers](https://thenewstack.io/zai-glm-weights-license/)
> 
> 作者：Frederic Lardinois

今年8月初，Z.ai（曾推出引发病毒式传播的 [ox-alpha 模型](https://thenewstack.io/ox-alpha-privacy-terms/)，后被证实为 [GLM-5.3-Flash](https://thenewstack.io/glm-5-3-chinese-chips/) 的中国 AI 实验室）正式发布了其旗舰模型 GLM-5.3。周五，该公司将该模型的权重发布在了 [Hugging Face](https://huggingface.co/zai-org/GLM-5.3) 上（Nvidia 可能很快会收购该公司）。目前已有几家第三方推理服务商托管了该模型，并将其提供在 OpenRouter 等平台上（Stripe 即将收购该平台）。

正如 *The New Stack* 的 Amanda Caswell 在该模型最初发布时[所报道的那样](https://thenewstack.io/glm-5-3-post-training-coding/)，Z.ai 在训练 GLM-5.3 时将重心放在了训练后阶段。其成果不仅在基准测试性能上较前代 GLM-5.2 有了显著飞跃，而且在性能上经常领先于其他中国开放权重模型，并能与美国前沿实验室目前的模型保持同步。

## 一个超大规模云服务商不会喜欢的全新许可

Z.ai 确实做出了一项重大改变，即模型的许可协议。虽然 GLM-5.2 是在宽松的 [MIT 许可](http://huggingface.co/zai-org/GLM-5.2/raw/main/LICENSE) 下发布的，但新模型采用的是公司所谓的 GLM-5.3 许可，且有一个主要限制：任何希望托管该模型（不仅仅是像 OpenRouter 那样进行路由，或将其嵌入到产品中），且在连续 12 个月内总营收超过 100 亿美元的公司，“在将该软件及其衍生作品用于任何商业目的之前，必须通过 Z.AI 的安全审查。”

对于个人用户而言，几乎没有任何变化——该许可更针对模型，并包含了运行、部署和微调的权利。但对于超大规模云服务商（以及一旦达到这些营收数字的新兴云服务商）来说，现在有了需要跨越的门槛。

![](https://cdn.thenewstack.io/media/2026/08/459fa358-screenshot-2026-08-28-at-10.01.37-am-1024x584.png)

该公司表示，为了进行安全评估和加固，GLM-5.3 的权重延迟了两周发布。GLM-5.3 在漏洞发现基准测试 CyberGym 上达到 84.5% 的准确率，Z.ai 称这是目前已发布的最优结果。当然，这个数字是由该公司自行报告的，目前尚未有公司外部人员进行复现。

Z.ai 表示，它已利用该模型在 269 个开源项目（包括 Linux 内核）中发现了 2,436 个漏洞，尽管目前只有几十个发现结果可供公开查阅。

尽管有安全方面的考量，但值得注意的是，该许可本身并不包含可接受使用条款，也未提及网络安全或攻击性安全方面的内容。

当然，Z.ai 修改许可协议是出于安全原因，还是为了更好地将其模型商业化，这是一个值得深思的问题。随着 GLM-5.3-Flash 的推出，该公司强调推理是在中国芯片上运行的，因此 Z.ai 显然有兴趣掌握这些模型的推理层。现在，这些开放权重的模型在性能上已经非常接近美国前沿实验室的产品，这也意味着有更多的盈利空间。

回溯到 2023 年和 2024 年，Z.ai 也曾为 ChatGLM3-6B 等模型使用自定义许可。根据该许可，商业用途需要注册。然而从那时起，所有新的 Z.ai 模型都采用了 MIT 许可。

Z.ai 的许可协议也比其他中国实验室使用的许可更具限制性。例如，[Moonshot](https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE) 规定，如果模型即服务（MaaS）提供商提供对 Kimi K3 的访问权限，且拥有超过 1 亿活跃用户或月收入超过 2000 万美元，则“必须在此类产品或服务的用户界面上显著展示‘Kimi K3’字样。”

DeepSeek 的旗舰模型仍然使用基础的 [MIT 许可](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)。

## 运行 GLM-5.3

在底层架构上，GLM-5.3 与 GLM-5.2 使用相同的 7530 亿参数专家混合（MoE）架构，拥有 100 万 token 的上下文窗口，最大输出为 12.8 万 token。

模型权重以 BF16 和 FP8 格式提供，支持在 vLLM、SGLang、KTransformers 和 Hugging Face 自身的 Transformers 库上运行。

![](https://cdn.thenewstack.io/media/2026/08/3ac592e1-screenshot-2026-08-28-at-9.23.36-am-1024x833.png)

来源：Z.ai。

API 发布与开放权重发布之间两周的时间间隔对 Z.ai 来说是新的尝试。GLM-5.2 的权重在发布当天就已可用。

尽管该模型现在是开放权重的，但除非你拥有非常强大的机器，否则你不太可能在本地运行它。即使是 Unsloth [声称](https://unsloth.ai/docs/models/glm-5.3) 仍能达到约 86% Top-1 准确率的 2-bit 量化版本，也需要 245GB 的内存。这勉强能装进一台拥有 256GB 统一内存的 Mac 中。而 8-bit 量化版本则需要 810GB 内存。

以每百万输入/输出 token 1.40 美元/4.40 美元的价格来看，它比几乎所有最直接的竞争对手都要便宜得多——尽管售价为 0.15 美元/0.47 美元的 GLM-5.3-Flash 模型目前拥有相当无敌的性价比。

## 未来展望

乍一看，许可协议在绝对意义上只是一个小改动，但它发生的同一周，Nvidia 传出以 129 亿美元收购 Hugging Face，而 Stripe 同意收购 OpenRouter。如果两笔交易均完成，开发者下载开放权重模型的仓库以及租赁模型的市场都将被美国公司控制，而 [模型本身](https://openrouter.ai/rankings#top-models) 却越来越多地出自中国实验室之手。

Z.ai 为 Flash 模型保留了 MIT 许可，因此该公司并没有完全放弃宽松的许可方式，但它已停止将其应用于其最顶尖的模型。如果 GLM-5.4 也是以同样的方式发布，那么该公司的“MIT 时期”看起来就像是客户获取阶段，而开放权重开始看起来不再像是对生态系统的馈赠，而更像是一个带有附加条款的发行渠道。