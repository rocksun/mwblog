在 Computex 上预发布了拥有 5500 亿参数的开源权重混合专家模型 Nemotron 3 Ultra 之后，英伟达（Nvidia）于周四在 [Hugging Face](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4)、[ModelScope](https://modelscope.ai/collections/nv-community/Nemotron-3x)、[OpenRouter](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b)（提供免费端点）以及 [build.nvidia.com](https://build.nvidia.com/) 等平台上正式发布了该模型。

这款新模型采用了与 Nemotron 3 系列其他模型相同的潜在混合专家（latent mixture-of-experts）技术和 [Mamba 2](https://goombalab.github.io/blog/2024/mamba2-part1-model/) 架构，将激活参数量减少到了 550 亿。它可支持高达 100 万 token 的上下文窗口。

正如英伟达所指出的，新模型经过了微调，旨在为需要规划、调用工具并对复杂任务进行迭代的长期运行 Agent 提供动力。为此，模型不仅需要足够智能，还需要足够快。事实上，英伟达在这次发布中强调了速度，指出它比上一代模型要快得多。

鉴于当前人们对 token 成本的担忧，更重要的一点可能是，英伟达还声称，与性能相当的其他模型相比，该模型可为用户节省高达 30% 的成本。

![](https://cdn.thenewstack.io/media/2026/06/82f066ae-nemotron-3-ultra-aa-quadrant-chart-scaled-1-1024x468.png)

图片来源：Nvidia

虽然它是 Kimi-K2.6、Qwen-3.5 和 GML-5.1 等直接竞争对手中速度最快的模型——也是迄今为止美国最好的开源权重模型——但在大多数基准测试上，它仍然落后于这些优秀的中国模型，尽管差距只有几分。

虽然英伟达称其为前沿模型，但基准测试的结果却并不完全支持这一说法。在测试模型执行现实世界中具有经济价值的任务的能力的 GDPVal 测试中，Nemotron 3 Ultra 的 NVFP4 变体（使用了英伟达全新的量化感知预训练技术）得分仅为 47.9%。相比之下，OpenAI 的 GPT-5.5 得分为 84.9%。

![](https://cdn.thenewstack.io/media/2026/06/4fbb7e19-screenshot-2026-06-04-at-16.16.35-1024x577.png)

图片来源：Nvidia

不过，基准测试并不总能体现模型的全部优势，英伟达指出，该模型能够处理“自主工作流中的编排以及最难的推理调用：在长时间运行的编程任务中做出架构决策、整合数百个研究来源，以及验证数千个相互依赖的约束条件”。

![](https://cdn.thenewstack.io/media/2026/06/c53886af-accuracy_plot-2-1024x587.png)

图片来源：Nvidia

该模型是在精心筛选的 14.8 万亿 token 的数据集上进行训练的，这使其能够支持 12 种语言（英语、法语、西班牙语、意大利语、德语、日语、韩语、印地语、巴西葡萄牙语和中文）以及 43 种编程语言。

英伟达正在提供权重、数据集和训练秘籍。该模型根据 OpenMDW-1.1 许可证提供。