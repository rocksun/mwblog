Ox-alpha，这个在过去几天迅速成为 OpenRouter 上最受欢迎的隐身模型，实际上是 Z.ai 的 GLM-5.3-Flash。这是一个拥有 3200 亿参数的混合模型（包含 180 亿活跃参数），是团队专门为超低成本推理而训练的。

周三，Z.ai [揭开了该隐身模型的面纱](https://z.ai/blog/glm-5.3-flash)，并在 [Hugging Face](https://huggingface.co/zai-org/GLM-5.3-Flash) 上以 MIT 许可证开源了其权重。

它也已经在多个推理平台上架，包括 OpenRouter。目前其价格为每百万输入 token 0.075 美元，每百万输出 token 0.25 美元（尽管这些价格反映了 50% 的折扣）。

## 基准测试：表现不错，但未达 Fable 水平

虽然早期的一些炒作将该模型与 Anthropic 的 Claude Fable 5 相提并论，但基准测试并不支持这一说法。不过，在开启最大努力推理模式时，该模型在大多数情况下可以跟上 Claude Opus 4.8 和 OpenAI 的 GPT-5.6 Terra 的步伐。

在 [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/models/glm-5-3-flash) 上，GLM-5.3-Flash 获得了 57 分，与 GPT-5.6 Terra、Google 的 Gemini 3.7 Flash、Meta 的 Muse Spark 1.2 以及 Qwen 3.8 2.4T A95B 处于同一水平。

在[驱动 AI 智能体](https://artificialanalysis.ai/models/glm-5-3-flash?intelligence=agentic-index)的性能表现方面，这可能是衡量其在现实场景中表现的更好指标，它甚至优于其竞争对手。

该模型能够理解多模态输入，包括图像、视频和文件。Z.ai 还强调，他们对该模型进行了针对性训练，使其在制作演示文稿和网站等视觉任务，以及处理文档、电子表格和仪表板等标准知识工作任务方面表现更好，所有这些都受益于该模型改进的视觉能力。

![](https://cdn.thenewstack.io/media/2026/08/640a3339-rjg_rlhpzl-1024x638.webp)

图片来源：Z.ai。

一个需要注意的地方是：该模型非常“健谈”，会消耗大量的 token，对于需要更多推理步骤才能达到这种性能的小型模型来说，这并不罕见。不过，由于推理成本极低，这并不是什么大问题。

## 国产芯片上的低成本推理

没有任何竞争模型能在价格上与 Z.ai 匹敌，这或许是此次发布最重要的一点。这些中国开源权重模型——包括来自 Alibaba、Deepseek 和 Moonshot (Kimi) 的模型——正越来越接近美国前沿实验室所能达到的性能，并且它们以极低的成本（对于拥有运行硬件的人来说甚至是免费的）提供这些模型。

![](https://cdn.thenewstack.io/media/2026/08/8db4c472-h1hakxndmx.png-1024x729.webp)

图片来源：Z.ai。

一个让许多早期 ox-alpha 用户感到惊讶的事实是，该模型背后的实验室每天能够提供 100 万亿个免费 token（根据 OpenCode 的数据）。很少有基础设施提供商能处理这种规模的任务。但事实证明，Z.ai 是在国产 AI 芯片上完成这一切的，该公司在 [公告](https://z.ai/blog/glm-5.3-flash) 中重点强调了这一点。

“与我们在同一硬件上的初始基准相比，我们实现了端到端服务性能 3 倍的提升，达到了与主流 NVIDIA GPU 相当的硬件效率和单 token 成本，” Z.ai 写道。“这证明了国产芯片可以高效、经济地支持大规模前沿模型推理。”

![](https://cdn.thenewstack.io/media/2026/08/8100a788-sy_ehd3wzx-1024x682.webp)

图片来源：Z.ai。

## 线性与稀疏注意力

该公司没有详细说明，但指出单个芯片在计算和内存容量方面有限。但是，Z.ai 为此服务栈构建了基于 SGLang 的推理引擎——在其旗舰 GLM-5.3 模型驱动的基础设施智能体的帮助下，公司称这创造了一个“反馈循环，模型帮助优化了服务模型本身的系统”。

Z.ai 没有说明该模型是在什么芯片上训练的，但该公司确实提到它是在 3 万亿多模态预训练语料库上训练的，并且团队使用了结合了线性注意力和稀疏注意力的混合架构。

![](https://cdn.thenewstack.io/media/2026/08/2732b7df-hyqvzw2wze.png-1024x544.webp)

图片来源：Z.ai。

“线性注意力通过状态建模捕获局部依赖关系，而稀疏注意力通过轻量级索引器检索相关的全局上下文，” 团队解释说。他们还指出，与完整的 GLM 5.3 模型相比，GLM 5.3-Flash 的架构将计算量减少了 3 倍，KV 缓存大小减少了 4.4 倍。

该模型拥有 100 万 token 的上下文窗口，因此这些减少的 KV 缓存大小产生了巨大的影响。

对于开发者来说，这里的考量非常简单。一个在智能体关键基准测试中匹配 Opus 4.8，价格却只有十分之一的模型，很难被忽视。对于美国实验室来说，更难的问题是，当中国实验室能够以这种规模进行服务时，未来会发生什么。