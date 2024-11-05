# 液态 AI 如何挑战基于 Transformer 的 AI 模型

![Featued image for: How Liquid AI Is Challenging Transformer-Based AI Models](https://cdn.thenewstack.io/media/2024/11/957b21f0-susan-wilkinson-f14nh9w9woo-unsplashb-1024x576.jpg)

尽管具有相对令人印象深刻的能力，但大多数传统的深度学习 AI 模型都存在一些局限性——例如，无法在学习新任务后回忆起先前学习的知识（[灾难性遗忘](https://thenewstack.io/techniques-for-tackling-catastrophic-forgetting-in-ai-models/)）以及无法适应新信息（[可塑性丧失](https://thenewstack.io/how-to-increase-plasticity-in-llms-and-ai-applications/)）。

液态神经网络 (LNN) 是一种相对较新的发展，它可能解决其中一些局限性，这得益于其动态架构以及自适应和持续学习能力。

液态神经网络由麻省理工学院的研究人员团队于 [2020 年](https://news.mit.edu/2021/machine-learning-adapts-0128) 首次提出，是一种时间连续的 [循环神经网络](https://www.geeksforgeeks.org/introduction-to-recurrent-neural-network/) (RNN)，可以有效地处理顺序数据。与通常只在固定数据集上训练一次的传统 [神经网络](https://thenewstack.io/deep-learning-neural-networks-google-deep-dream/) 不同，LNN 还可以适应新的输入，同时保留先前学习任务的知识——从而有助于避免灾难性遗忘和可塑性丧失等问题。

Liquid AI 的新型基于 LLN 的模型提高了性能，同时最大限度地减少了内存使用，这与基于 Transformer 的 LLM 相比。

LNN 的“液态”本质源于其对液态时间常数 (LTC) 的实现，这使得网络能够通过动态改变网络连接的强度来适应新信息，同时保持对噪声的鲁棒性。值得注意的是，LNN 节点的权重是有限制的——这意味着 LNN 不容易受到 [梯度爆炸](https://machinelearningmastery.com/exploding-gradients-in-neural-networks/) 等问题的影响，这些问题会导致模型变得不稳定。

## 更少但更丰富的节点

[根据](https://news.mit.edu/2021/machine-learning-adapts-0128) 共同作者 [Ramin Hasani](https://www.linkedin.com/in/raminhasani/) 的说法，LNN 的灵感来自线虫 *C. elegans*，这是一种只有 302 个神经元的微观圆形蠕虫，但它可以“产生出乎意料的复杂动力学”——这与具有数千个神经元节点的大型深度学习神经网络形成对比。考虑到这一点，该团队的目标是开发一个规模缩小的网络，具有“更少但更丰富的节点”。

正是这些“更丰富”的连接使 LNN 能够以相对较小的网络规模运行，从而减少计算资源，同时仍然允许它们对复杂的行为进行建模。这种整体规模的减少也意味着 LNN 做出的决策更加透明和“[可解释](https://thenewstack.io/researchers-build-an-interpretable-ai-that-shows-how-it-thinks/)”，与其他功能更像难以理解的“黑盒子”的大型模型相比。

在现实世界中，这些特性使 LNN 在处理各种不同类型的数据方面具有优势——从处理图像、视频和自然语言到任何需要持续学习的时间序列数据。LNN 的较小规模和动态架构可能意味着对机器人、自动驾驶汽车、无人机和金融市场和医疗诊断的数据分析的推动——基本上，任何系统可能缺乏存储和运行大型语言模型能力的情况。

## 进入 Liquid AI 和液态基础模型

![](https://cdn.thenewstack.io/media/2024/10/3a6157d2-liquid-ai-lfm-launch.jpg)

截图

LNN 的巨大潜力促使它的创造者迈出了下一步，通过一家名为 [Liquid AI](https://www.liquid.ai/) 的新创业公司推出他们称之为 [液态基础模型](https://www.liquid.ai/liquid-foundation-models) (LFM) 的产品（Hasani 是联合创始人兼首席执行官）。Liquid AI 的这一系列最先进的生成式 AI 模型提高了性能，同时最大限度地减少了内存使用，这与基于 [Transformer](https://thenewstack.io/the-evolution-of-the-ai-stack-from-foundations-to-agents/) 的大型语言模型形成对比——这种现在熟悉的深度学习架构由 Google 于 2017 年推出，并 [在 2022 年由 ChatGPT 闻名](https://thenewstack.io/just-out-of-the-box-chatgpt-causing-waves-of-talk-concern/)。
据该公司称，Liquid 基础模型 (LFM) 与生成式预训练 Transformer (GPT) 模型的不同之处在于，它们使用基于“动力系统理论、信号处理和数值线性代数”的混合计算系统。这使得 LFM 能够作为通用模型，可以对任何类型的顺序数据进行训练，无论是视频、音频、文本、时间序列和信号，并且还能在使用更少神经元的情况下实现与传统深度学习模型相似的性能。

LFM（Liquid 基础模型）比基于 Transformer 的模型更节省内存，尤其是在处理长输入时。

最值得注意的是，LFM 比基于 Transformer 的模型更节省内存，尤其是在处理长输入时。对于基于 Transformer 的大型语言模型 (LLM)，[KV 缓存](https://thewhitebox.ai/kv-cache-chatgpts-memory/) 随着序列长度线性增长，而 LFM 可以使用相同的硬件处理更长的序列。令人印象深刻的是，LFM 被设计为支持 32K 个标记的上下文长度，使其非常适合复杂用途，例如更智能的聊天机器人或文档分析。

此外，该团队之前的研究表明，这些系统可以作为[通用逼近器](https://ojs.aaai.org/index.php/AAAI/article/view/16936/16743)、[用于顺序数据的表达性连续时间机器学习系统](https://ojs.aaai.org/index.php/AAAI/article/view/16936/16743)、[学习新技能时参数效率高](https://publik.tuwien.ac.at/files/publik_292280.pdf)、[因果性和可解释性](http://cap.csail.mit.edu/sites/default/files/research-pdfs/Robust%20flight%20navigation%20out%20of%20distribution%20with%20liquid%20neural%20networks.pdf)，并且在线性化后可以有效地[对顺序数据中的长期依赖关系进行建模](https://arxiv.org/abs/2209.12951)。

目前有三个版本的 LFM，它们在测试中都与或超过了同等规模的基于 Transformer 的模型：

**LFM-1B**: 拥有 13 亿个参数，这是 Liquid AI 的 LFM 中最小的一个。它被描述为一个密集模型，最适合资源受限的环境，初步测试表明，这是首次非 GPT 架构显著优于基于 Transformer 的模型。**LFM-3B**: 拥有 31 亿个参数的中端模型，更健壮，针对边缘部署（如无人机和移动设备）进行了优化。**LFM-40B**: 针对在云环境中运行复杂任务而设计，这是一个拥有 403 亿个参数的“[专家混合](https://www.datacamp.com/blog/mixture-of-experts-moe)”模型。

凭借其更高的效率、动态适应性和多模态能力，LFM 可以通过挑战当前 GPT 模型的统治地位，帮助将生成式 AI 技术推向新的高度。在最近的产品发布会上，该团队还推出了[Liquid DevKit](https://youtu.be/d19jhYtwgCA?si=4saIC_ZBlU_0T_fe&t=2148)，为开发人员提供了一种简化但全面的方法来构建、扩展和解释 LFM。要了解更多信息，您可以通过[网络直播](https://www.liquid.ai/oct-23rd-2024-live-stream)观看其最近的发布会。该公司还通过[Liquid Playground](https://playground.liquid.ai/login)、[Lambda Chat](https://lambda.chat/chatui/models/lfm-40b) 和[API](https://docs.lambdalabs.com/public-cloud/lambda-chat-api/#listing-models) 以及[Perplexity Labs](https://labs.perplexity.ai/) 提供 LFM 的演示访问。

[YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)