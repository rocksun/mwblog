# 使用扩散LLM，为更快的文本生成做好准备

![Featued image for: Get Ready for Faster Text Generation With Diffusion LLMs](https://cdn.thenewstack.io/media/2025/03/63f9c70b-pexels-cottonbro-9669101b-1024x576.jpg)

多年来，我们一直认为许多基于 Transformer 的大型语言模型 (LLM) 使用一种称为[自回归](https://www.ibm.com/think/topics/autoregressive-model)的技术是理所当然的。这种机器学习技术与许多语言的工作方式非常吻合，因为它从左到右依次处理和生成每个单词或[token](https://thenewstack.io/what-is-an-llm-token-beginner-friendly-guide-for-developers/)。但是，随着 AI 生成文本的复杂性不断增加，推理成本和延迟问题也随之增加。

然而，由于美国 [Inception Labs](https://www.inceptionlabs.ai/) 最近发布了 [Mercury](https://mercurycoder.org/)，这可能是更好的方法。Mercury 是第一个商业规模的扩散大型语言模型 (dLLM)，它承诺使用与 DALL-E、Stable Diffusion 和 Midjourney 等图像生成模型相同的基于扩散的方法，从而实现更快、更高效的文本生成。

## 自回归 vs. 扩散

传统的基于自回归的大型语言模型将连续[处理 token](https://www.lighton.ai/lighton-blogs/the-magic-of-tokens-in-generative-ai-a-deep-dive)，每个新单词的生成都依赖于序列中之前的 token。这种方法有明显的优势：它提供更高的连贯性、上下文深度和更真实的输出，可以捕捉单词和短语之间的依赖关系。但是，这些模型的缺点包括计算成本增加、推理速度变慢以及更多潜在错误。

相比之下，扩散模型的非顺序性质克服了许多这些问题。对于生成图像，扩散模型的工作方式是首先通过一个称为“加噪”的过程，逐步向图像添加随机噪声。然后，模型学习通过迭代“去噪”从添加的噪声中恢复，以重建原始图像。通过这些过程，模型学习识别模式，并最终学习如何在将来合成和不断改进类似的图像。

![](https://cdn.thenewstack.io/media/2025/03/fbc5796c-diffusion-models.jpg)

扩散模型如何用于图像生成——加噪和去噪。通过 [Tim Cvetko](https://timc102.medium.com/stable-diffusion-intuitively-explained-51157ef99d83)。

扩散模型的这种整体、并行化的方法在生成图像和视频方面非常有效，但直到现在，在文本方面一直难以实现。

“Transformer 主导着 LLM 文本生成，并按顺序创建 token。扩散模型提供了一种替代方案——它们同时生成所有文本，应用从粗到精的过程，”DeepLearning.ai 创始人 Andrew Ng 在 [X 上的一篇文章](https://x.com/AndrewYNg/status/1894979731726180765)中解释道。

## Mercury 加速语言生成

据该公司称，Mercury 比传统的大型语言模型快五倍，比其他速度优化的 LLM 快 10 倍——而且，总体而言，运行成本更低。Mercury 模型可以在 NVIDIA H100 上以每秒超过 1,000 个 token 的速度运行——这种极快的速度以前只能通过 Groq、Cerebras 和 SambaNova 等专业硬件公司的定制芯片才能实现。

目前，它以 [Mercury Coder](https://mercurycoder.org/) 的演示形式提供，Mercury Coder 是一种专门为生成代码而优化的扩散大型语言模型。您可以在下面的视频中看到它在实时代码生成方面与其他 LLM 的比较。

根据 Inception Labs 的说法，Mercury Coder 的“小型”版本与 OpenAI 的 GPT-4o Mini 和 Claude 3.5 Haiku 相当，同时在测试期间的运行速度快 10 倍。 “mini” Mercury 模型优于 Meta 的 Llama 3.1 8B 等小型开源模型，实现了每秒超过 1,000 个 token。与一些以每秒不到 50 个 token 运行的前沿 LLM 相比，Mercury 提供了 20 倍的加速。

![](https://cdn.thenewstack.io/media/2025/03/0d9a8006-mercury-coder-2.jpg)

速度比较：每秒输出 token，编码工作负载。通过 [Inception Labs](https://www.inceptionlabs.ai/news)。

在标准编码基准上进行评估时，Mercury Coder 能够在保持其输出高质量的同时，保持或超越其竞争对手。

![](https://cdn.thenewstack.io/media/2025/03/3cc02b7d-mercury-coder-4.jpg)

通过 [Inception Labs](https://www.inceptionlabs.ai/news)。

## 对 AI 的潜在影响
凭借 Mercury 更有效地利用通用 GPU，这意味着推理成本可能会降低，而对性能的影响不会太大，也无需专用硬件。随着 GPU 的不断发展，这可能意味着 Mercury 等扩散模型在未来会获得更强的性能。

目前，扩散模型也存在一些缺点。自回归模型每个 token 只需要一次传递，而扩散模型通常需要 token 在神经网络上进行多次正向传递才能生成输出。然而，扩散模型可以并行处理所有 token，这在很大程度上弥补了这一潜在的缺点。

## 基于扩散的文本生成的潜在用途

Inception Labs 认为，基于扩散的文本生成非常适合代码生成、企业自动化，以及对延迟敏感的用例，如会话式 AI、自主 AI 和资源受限的情况（如移动设备）。由于 dLLM 具有先进的推理能力，它们可以纠正幻觉，同时仍然可以在几秒钟内处理答案。从长远来看，像 Mercury 这样的模型可能预示着从自回归模型到基于扩散模型的快速高效文本生成的范式转变。

Mercury 现在可以通过 [编码演示](https://mercurycoder.org/)获得，企业客户也可以通过 API 和本地部署获得，并为两者提供微调支持。要了解更多信息，请访问 [Inception Labs](https://www.inceptionlabs.ai/)。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)