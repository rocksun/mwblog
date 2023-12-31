<!--
title:  2023年开源大语言模型一览
cover: https://cdn.thenewstack.io/media/2023/12/aec929b1-year-wrapup-1-1024x576.png
-->

人工智能领域出现了各种开源方案，竞争日渐激烈。本文整理了一些影响力最大的开源大语言模型。

> 译自 [Large Language Models: Open Source LLMs in 2023](https://thenewstack.io/large-language-models-open-source-llms-in-2023/)，作者 Kimberley Mok。

随着 OpenAI [去年](https://thenewstack.io/just-out-of-the-box-chatgpt-causing-waves-of-talk-concern/)底发布 ChatGPT 聊天机器人，[大型语言模型](https://thenewstack.io/what-is-a-large-language-model/)(LLM)已引起公众广泛关注。

尽管这种基于生成式 AI 的工具具有充足的利润潜力，但更广泛的 AI 社区中的许多小企业和独立研究人员仍对采用封闭源 LLM 持谨慎态度，这不仅是因为其操作成本和巨大的计算要求，还有其他问题，如[数据所有权](https://thenewstack.io/the-power-and-ethical-dilemma-of-ai-image-generation-models/)、隐私以及它们[有时“幻觉”错误信息的令人不安的倾向](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/)。

因此，开源替代品在过去一年中也获得了牵引力并不令人惊讶。正如一些调查[所指出的](https://arxiv.org/pdf/2311.16989.pdf)，尽管开源 LLM 通常还不如其[封闭源表亲强大](https://thenewstack.io/top-5-large-language-models-and-how-to-use-them-effectively/)，但开源选项可以针对[特定任务进行微调](https://thenewstack.io/6-reasons-private-llms-are-key-for-enterprises/)，以超过专有模型。

随着 AI 领域因各种开源替代方案的出现而变得更加多样化，以下是 2023 年产生最大影响的几个有力竞争者。

## 1. LLaMA 和 LLaMA 2

今年 2 月，Meta 发布了 LLaMA，这是其拥有 130 亿参数的大型语言模型，[经测试](https://arxiv.org/abs/2302.13971)在大多数基准测试中优于 175 亿参数的 [GPT-3](https://thenewstack.io/openais-gpt-3-makes-big-leap-forward-for-natural-language-processing/) 模型。这个第一版以开源包的形式发布，开发者可以在非商业许可下请求访问它;然而，该模型及其权重很快在[网上泄露](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/)，使其实际上对任何人开放使用。

7 月，Meta 推出了 [LLaMA 2](https://ai.meta.com/llama/) 的后续版本，该公司称它比原始版本训练了 40% 更多的数据，还有其他像 LLaMA 2-Chat 等微调版本，该版本已针对类人的对话进行了优化，以及 LLaMA Code，该版本专门用于生成代码。

尽管 LLaMA 2 [是否真正开源存在一些争议](https://thenewstack.io/metas-llama-2-is-not-open-source-and-thats-ok/)，但 Meta 已在一定程度上放宽了这些模型的使用限制，以包括商业使用，这导致了基于开源 LLaMA 的衍生产品的发展，如 Alpaca、Alpaca-LoRA、Koala、QLoRA、llama.cpp、Vicuna、Giraffe 和 StableBeluga。

## 2. Pythia

非营利实验室 EleutherAI 于今年 4 月发布了 [Pythia](https://www.eleuther.ai/papers-blog/pythia-a-suite-for-analyzing-large-language-modelsacross-training-and-scaling)，这是一套使用公开数据训练的不同大小的 LLM 套件。[Pythia 旨在](https://github.com/EleutherAI/pythia)作为一个可解释性工具，供研究人员更好地理解 LLM 背后的训练过程及其产生的结果。

## 3. MPT

MosaicML 从 5 月开始推出 [MPT](https://www.mosaicml.com/mpt) 系列大型语言模型，首先是一个初始的 [70 亿参数模型](https://www.mosaicml.com/blog/mpt-7b)，随后在 6 月是一个 300 亿参数的版本，该公司声称它在某些需要较长文本提示的用例中[优于 LLaMA 和 Falcon](https://thenewstack.io/mosaicml-launches-30b-model-takes-on-llama-falcon-and-gpt/)。

MPT 结合了 LLM 这个不断发展领域的一些最新技术，以提高效率、上下文长度外推和改进稳定性，以减少损失尖峰。

## 4. Falcon

这个最先进的语言模型系列于 6 月初由阿布扎比技[术创新研究所](https://www.tii.ae/)在 Apache 2.0 许可下发布。由于这个具有 [400 亿参数的第一个模型](https://huggingface.co/blog/falcon)随权重一起发布，它立即受到该领域的开发者和研究人员的欢迎。

9 月，一个拥有 1800 亿参数的更大 [Falcon](https://falconllm.tii.ae/) 模型宣布面世，这使其成为可用的最大开源 LLM 之一。Falcon 背后的团队认为，虽然 180 亿参数版本略落后于 OpenAI 的 [GPT-4](https://thenewstack.io/openais-gpt-4-can-analyze-visual-images-pass-bar-exam/) 等封闭源模型，但它仍然超过了 Meta 的 LLaMA 2，并与谷歌的 PaLM 2 Large 齐平。

## 5. BLOOM

另一个产生巨大影响的模型是 [BLOOM](https://huggingface.co/bigscience/bloom)(即 BigScience Large Open-science Open-access Multilingual Language Model 的缩写)。尽管它实际上是在 2022 年 7 月发布的，但它入选我们的列表，因为它是一个由 60 个国家、250 个机构的 1000 多名 AI 研究人员在 [Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) 和法国 GENCI(大型国家强烈计算设备)与 IDRIS(强烈科学计算资源开发研究所)的协调下开发的模型。

BLOOM 旨在促进对大型语言模型的公共研究，其最大的模型拥有 1780 亿参数，并在 46 种人类语言和 13 种编程语言派生的多语言数据上进行训练，这使其成为到目前为止最大的开源大规模多语言模型。

## 6. Mistral

Mistral由此前与Meta和谷歌相关的研究人员创立，于9月首次发布了一个70亿参数的LLM。根据这家巴黎初创公司的说法，[Mistral](https://mistral.ai/) 7B在许多指标上优于其他开源LLM，如LLaMA 2。就在本月，该团队通过[Torrent链接](https://venturebeat.com/ai/mistral-ai-bucks-release-trend-by-dropping-torrent-link-to-new-open-source-llm/)发布了一个新模型Mixtral 8x7B，在更大的科技公司发布前炒作过度的产品时，它产生的讨论声量更大。

随着开源LLM领域的不断扩大，许多开发者正通过转向更具成本效益、透明度和可调节性的[开源替代方案](https://thenewstack.io/pivot-ai-devs-move-to-switch-llms-reduce-openai-dependency/)，来减少对OpenAI API的依赖。

专有模型目前可能仍略占优势，但开源模型正在迅速赶上，一些开源LLM的表现已经超过了其更大参数的对应模型，这表明训练数据的质量可能比规模更重要。过去一年中，开源LLM获得了非常令人振奋的进展，明确表明它们将继续在大型语言模型的景观演变中发挥重要作用。
