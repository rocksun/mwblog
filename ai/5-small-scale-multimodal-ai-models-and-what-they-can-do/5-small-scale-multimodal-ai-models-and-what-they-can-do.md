
<!--
title: 5个小型多模态AI模型及其功能
cover: https://cdn.thenewstack.io/media/2024/12/73fd52e7-getty-images-o5asjrfw4lo-unsplashb.jpg
-->

随着对多模态AI系统兴趣的增长，这些多功能工具的小型版本也随之增多。

> 译自 [5 Small-Scale Multimodal AI Models and What They Can Do](https://thenewstack.io/5-small-scale-multimodal-ai-models-and-what-they-can-do/)，作者 Kimberley Mok。

过去几年，我们见证了大型语言模型（LLM）的迅速发展，其参数数量已激增至数十亿，使其成为分析、[摘要](https://thenewstack.io/how-to-summarize-large-documents-with-langchain-and-openai/)和生成文本和[图像](https://thenewstack.io/the-power-and-ethical-dilemma-of-ai-image-generation-models/)或创建[拟人化聊天机器人](https://thenewstack.io/building-smarter-chatbots-with-advanced-language-models/)等任务的强大工具。

当然，如此强大的功能也带来了一些显著的局限性，尤其是在用户资金不足或硬件无法满足这些LLM所需的大量计算资源的情况下。因此，我们见证小型语言模型（SLM）的[兴起](https://thenewstack.io/the-rise-of-small-language-models/)也就不足为奇了，它专门针对资源受限的用户。

现在，随着人们对能够同时处理不同类型数据（图像、文本、音频和视频）的[多模态AI系统](https://thenewstack.io/top-7-tools-for-building-multimodal-ai-applications/)的兴趣日益增长，这些多功能工具的小型版本也随之增多。在本文的其余部分，我们将介绍五种最近备受关注的小型多模态AI工具。

## 1. TinyGPT-V

这款功能强大且资源高效的28亿参数多模态模型可以处理文本和图像输入，并在使用比大型同类产品少得多的资源的同时保持令人印象深刻的性能水平。

[TinyGPT-V](https://github.com/DLYuanGod/TinyGPT-V) 的缩小规模架构具有优化的Transformer层，在规模、性能和效率之间取得了平衡，此外还使用了一种专门的机制来处理图像输入并将它们与文本输入集成。它使用相对较小的LLM [Phi-2](https://dev-kit.io/blog/ai/microsoft-phi-2?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)构建，并结合了来自[BLIP-2](https://thenewstack.io/a-guide-to-model-composition/)或[CLIP](https://openai.com/index/clip/)的预训练视觉模块。

它可以使用较小的数据集进行微调，使其成为中小型公司或希望在教育或研究环境（资金和资源可能更有限）中本地部署它的用户的理想选择。

## 2. TinyLlaVA

这个新颖的框架集成了CLIP-Large和SigLIP等视觉编码器，以及小型LLM解码器、中间连接器和定制的训练管道——所有这些都是为了获得高水平的性能，同时将计算使用量保持在最低限度。

[TinyLlaVA](https://huggingface.co/collections/bczhou/tinyllava-65e584a5e8b017ee1347a0a7) 使用两个不同的数据集进行训练：LLaVA-1.5和ShareGPT4V。监督微调过程允许调整LLM和视觉编码器的部分可学习参数。

根据[测试](https://arxiv.org/pdf/2402.14289)，TinyLlaVA性能最佳的变体TinyLLaVA-share-Sig-Phi 3.1B变体优于LLaVA-1.5和Qwen-VL等7B模型。此外，该框架还对模型选择、训练方法和数据对小型LLM性能的贡献进行了全面的分析。这是一个很好的例子，说明了如何利用小型LLM可以在不牺牲性能的情况下显著提高可访问性和效率。

## 3. GPT-4o mini

GPT-4o mini作为OpenAI [GPT-4o](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/)多模态模型的较小且更便宜的版本发布，其运行成本比OpenAI模型系列中以前最实惠的模型GPT-3.5 Turbo低约60%。

GPT-4o mini 通过[蒸馏过程](https://www.datacamp.com/blog/distillation-llm)从更大的GPT-4o衍生而来，在性能和成本效益之间取得了极佳的平衡。它具有128K的大上下文窗口，能够处理文本和图像的多模态功能，并计划未来支持视频和音频。它还具有增强的安全功能，可以防止越狱、系统提示提取和提示注入。

GPT-4o mini 的用例可能包括为新的聊天机器人进行快速原型设计、用于语言学习或个人助理的设备应用程序、互动游戏以及教育环境中的应用程序。

## 4. Phi-3 Vision
微软强大的Phi-3视觉语言变体是一个基于Transformer的模型，包含图像编码器、连接器、投影器和Phi-3 Mini语言模型。该模型拥有42亿个参数，[Phi-3 Vision](https://huggingface.co/microsoft/Phi-3-vision-128k-instruct)能够支持高达128K个token的上下文长度，并具有“[广泛的多模态推理能力](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/phi-3-vision-%E2%80%93-catalyzing-multimodal-innovation/4170251)” ，使其能够理解和生成基于图表、图形和表格的内容。

其性能可与OpenAI的GPT-4V等大型模型相媲美，Phi-3 Vision非常适合资源受限的环境和延迟敏感的场景，在离线运行、成本和用户隐私方面具有优势。

潜在用例包括文档和图像分析以改进客户支持、社交媒体内容审核以及公司或教育机构的视频分析。

## 5. Mississippi 2B 和 Mississippi 0.8B

最近由[H2O.ai](https://h2o.ai/)发布，这两个多模态基础模型专为OCR和文档AI用例而设计。这些视觉语言模型旨在紧凑高效，为企业提供了一种可扩展且经济高效的方式来实时执行文档分析和图像识别。

这些模型采用多阶段训练，对层进行微调，并具有最小的延迟——这使得它们非常适合医疗保健、银行、保险和金融领域，这些领域需要处理大量的文档。

[H2OVL Mississippi 2B](https://huggingface.co/h2oai/h2ovl-mississippi-2b)和[H2OVL Mississippi 0.8B](https://huggingface.co/h2oai/h2ovl-mississippi-800m)目前都在Hugging Face上免费提供，为开发人员、研究人员和企业提供了易于访问的选项来进行微调和修改。

## 结论

多模态模型以及大型语言模型的可访问性和成本效益仍然是主要问题。但随着越来越多的相对轻量级但功能强大的多模态AI选项可用，这意味着更多机构和小型企业将能够在其工作流程中采用AI。
