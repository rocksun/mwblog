借用 Gil Scott-Heron 那首[永恒的 1971 年抗议歌曲](https://www.youtube.com/watch?v=vwSRqaZGsPw)的话，如果有人认为 AI 革命不会被量化，那他们可能错了。一场文化变革正在中国进行，量化确实正在推动变革。

## 量化：AI 模型权重的压缩

[量化](https://thenewstack.io/edge-ai-and-model-quantization-for-real-time-analytics/)是将 AI 模型权重压缩至更低数值精度的过程，使其更小且运行成本更低。这是一项与开放权重模型访问并行运行的技术，开发者可以公开访问模型的训练参数，然后自定义模型并将其在本地或选定的云端运行。

根据 [RQR Intelligence](https://renovateqr.com/blog/chinese-ai-models-april-2026) 的观点，“中国 AI 生态系统的巨大优势在于其对开放权重的坚定承诺。”

软件工程师能够使用诸如 [Qwen](https://thenewstack.io/runpod-ai-infrastructure-reality/)、[Xiomei 的 MiMo](https://thenewstack.io/coding-agent-endurance-gap/) 或 [DeepSeek](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/) V4 Pro 等模型，下载权重（模型训练期间学习到的精确数值），通过量化过程进行处理，然后在他们自己的机器（或选择的云服务）上运行和托管，从而实现前沿水平的智能。

> “像 Z.AI、Qwen、GLM 和 DeepSeek 这样的中国前沿模型已成为当今软件开发的实用工具。它们非常适合测试生成、重构、代码库分析、文档编写和初步调试。需要注意的是，它们仍需人工验证。它们是有用的工程工具，但不是自主的高级工程师。” —— Gautam Korlam，Sonar。

AI 代码验证和治理公司 [Sonar](https://www.sonarsource.com/) 的首席工程师 [Gautam Korlam](https://www.linkedin.com/in/gautamkorlam/) 告诉 *The New Stack*，中国前沿模型最大的优势不仅仅是跑分提升，这是从不同视角进行的权力博弈。

“有了这些中国前沿模型，开发者可以检查它们、微调它们、本地运行它们，并将它们集成到仅靠 API 部署难以实现的各种工作流中。这让团队对成本和智能水平拥有了更多控制权，” Korlam 说道。

他进一步指出，中国前沿模型（如 Z.AI、Qwen、GLM 和 DeepSeek）已成为他眼中当今软件开发的“实用工具”。

“它们非常适合测试生成、重构、[代码库分析](https://thenewstack.io/phantom-secrets-the-hidden-threat-in-code-repositories/)、文档编写和初步调试。需要注意的是，它们仍需人工验证。它们是有用的工程工具，但不是自主的高级工程师，” Korlam 确认道。

针对专有闭源权重 AI 前沿模型公司（Anthropic 的 Claude、OpenAI 的 GPT-5.5、Google 的 Gemini 3 Pro、Meta 的 Llama、Mistral 等）的革命，部分或全部源于对 [美国 GPU 硬件出口管制](https://www.bbc.co.uk/news/articles/cedy6gl99eno) 的战略响应。

这些限制迫使中国 AI 实验室通过使用各种编码方法进行创新。根据 [Index.dev](https://www.index.dev/blog/chinese-ai-models) 的说法，诸如阿里巴巴云的 Qwen 等模型通过稀疏模型方法实现了效率提升，仅在推理期间激活参数的子集。

“与传统 AI 模型一次激活所有参数不同，Qwen3-Max 仅使用给定任务的相关部分。这使得它在推理时的效率提高了约 30%，这意味着它在不消耗大量计算能力的情况下即可提供高性能，” 该门户网站指出。

> “在中国模型处于前沿水平的情况下，情况变得很有趣，但这是一把双刃剑。对于公司和开发者来说，这是一个福音。同时，这也意味着这些工具可以被任何一方——国家或私人——用于防御或进攻。” —— Piotr Migdał，Quesma。

## 前沿 AI 不再是三巨头的竞争

[Quesma](https://quesma.com/)（一家代理 AI 评估和训练公司）的创始工程师 [Piotr Migdał](https://www.linkedin.com/in/piotrmigdal/) 告诉 *The New Stack*，随着中国前沿模型 Z.ai 发布的 GLM 5.2，事情变得“非常有趣”。

他认为，这一发展意味着 AI 竞赛“不再只是美国人的事”，不再仅涉及那三家常见的嫌疑人：OpenAI、Anthropic 和 Google。除了 Z.ai 的 GLM，Migdał 还指出了 Qwen 3.6 27B，他认为这是当今[本地开发的最佳切入点](https://quesma.com/blog/qwen-36-is-awesome/)。

“虽然竞赛现在和将来都会很激烈，但我们可以期待更多中国模型处于领先地位，” Migdał 说。“GLM 5.2 与专有模型不同，它可以被微调，根据需要进行调整以提高在特定任务上的表现，或者删除限制。这使它成为一把双刃剑。对于公司和开发者来说，这是一个福音，促进了商业和开源的发展，因为不再存在由寡头控制的 API 水龙头。同时，这也意味着这些工具可以被任何一方——国家或私人——用于防御或进攻。”

随着中国前沿 AI 模型在[开发者评论板](https://hn.algolia.com/?q=GLM-5.2)上被广泛基准测试、讨论，且极少因幻觉问题受到严厉批评或指责，下一个拐点可能会出现新的标准化、透明度，甚至我们敢说——商品化？

## **模型商品化的幽灵**

[OC&C Strategy Consultants](https://www.occstrategy.com/en/) 的合伙人 [James McGibney](https://www.linkedin.com/in/james-mcgibney-9059b916/) 告诉 *The New Stack*，这正是可能正在发生的事情。

“可以说，原始模型智能已经开始商品化，而更廉价的中国开源权重和量化模型的出现将加速这一转变，” McGibney 说。

他认为，这种转变的结果可能是企业会越来越多地根据具体情况或具体应用来选择模型。

“如果这种商品化全面开花，它将进一步推动前沿 AI 公司——无论是中国的还是美国的——向价值链上游移动，从而鼓励市场参与者将软件、工作流集成、治理和实施层货币化，这些层使得 AI 在实际业务环境中变得可靠且有价值。”

回到最初的话题，当 Gil Scott-Heron 告诉我们革命不会被直播时，他的意思是真正的改变是内在的，它不会被赞助或商业化，也不应该有人坐视不管，仅仅做一个旁观者。

如果他今天还活着（并且对中国前沿模型的发展产生了兴趣），他可能会对他当年针对的权力结构进行同样的审查，然后同意 AI 模型革命很可能将会被量化。也许唯一的区别是（考虑到软件开发者的存在），这场革命几乎肯定会伴随着可乐进行得更好。