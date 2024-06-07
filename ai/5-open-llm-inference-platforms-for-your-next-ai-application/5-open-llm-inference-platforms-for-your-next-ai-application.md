
<!--
title: 可用于AI应用的5个开放式LLM推理平台
cover: ./cover.jpg
-->

五个生成式 AI 推理平台，可使用开放式 LLM，如 Llama 3、Mistral 和 Gemma。有些还支持针对视觉的模型。

> 译自 [5 Open LLM Inference Platforms for Your Next AI Application](https://thenewstack.io/5-open-llm-inference-platforms-for-your-next-ai-application/)，作者 Janakiram MSV。

[开放式大语言模型](https://thenewstack.io/large-language-models-open-source-llms-in-2023/) 变得越来越强大，并且是 [GPT-4](https://thenewstack.io/30-non-trivial-ways-for-developers-to-use-gpt-4/) 和 [Gemini](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/) 等商业 LLM 的可行替代方案。鉴于 AI 加速器硬件的成本，开发人员正在考虑使用 API 来使用最先进的语言模型。

虽然 [Azure OpenAI](https://azure.microsoft.com/en-in/products/ai-services/openai-service)、[Amazon Bedrock](https://aws.amazon.com/bedrock/) 和 [Google Cloud Vertex AI](https://cloud.google.com/vertex-ai) 等云平台是显而易见的选择，但有一些专门构建的平台比超大规模平台更快、更便宜。

以下是五个生成式 AI 推理平台，可使用开放式 LLM，如 Llama 3、Mistral 和 Gemma。其中一些还支持针对视觉的基础模型。

## 1. Groq

[Groq](https://groq.com/) 是一家 AI 基础设施公司，声称构建了世界上最快的 AI 推理技术。他们的旗舰产品是语言处理单元 (LPU) 推理引擎，这是一个硬件和软件平台，旨在为 AI 应用程序提供卓越的计算速度、质量和能效。开发人员喜爱 Groq 的速度和性能。

一个经过扩展的 LPU 网络为 [GroqCloud](https://console.groq.com/login) 服务提供支持，该服务使用户能够以（据称）比其他提供商快 18 倍的速度使用流行的开源 LLM，如 Meta AI 的 Llama 3 70B。您可以使用 [Groq 的 Python 客户端 SDK](https://github.com/groq/groq-python) 或 [OpenAI 客户端 SDK](https://github.com/openai/openai-python) 来使用 API。可以轻松地将 Groq 与 [LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/) 和 [LlamaIndex](https://thenewstack.io/llamaindex-and-the-new-world-of-llm-orchestration-frameworks/) 集成，以构建高级 LLM 应用程序和聊天机器人。

在定价方面，Groq 提供了一系列选项。对于他们的云服务，他们根据处理的令牌收费——价格从每百万个令牌 0.06 美元到 0.27 美元不等，具体取决于所使用的模型。免费层是开始使用 Groq 的绝佳方式。

## 2. Perplexity Labs

[Perplexity](https://www.perplexity.ai/) 正迅速成为 Google 和 Bing 的替代品。虽然其主要产品是 [AI 驱动的搜索引擎](https://thenewstack.io/more-than-an-openai-wrapper-perplexity-pivots-to-open-source/)，但他们还通过 [Perplexity Labs](https://labs.perplexity.ai/) 提供推理引擎。

2023 年 10 月，Perplexity Labs [推出了](https://www.perplexity.ai/hub/blog/introducing-pplx-api) pplx-api，这是一个 API，旨在促进快速高效地访问开源 LLM。pplx-api 目前处于公开测试阶段，允许拥有 Perplexity Pro 订阅的用户访问该 API，从而使广泛的用户群能够进行测试并提供反馈，这有助于 Perplexity Labs 持续增强该工具。

该 API 支持流行的 LLM，包括 Mistral 7B、Llama 13B、Code Llama 34B 和 Llama 70B。它旨在在部署和推理方面都具有成本效益，Perplexity Labs 报告了显著的成本节约。用户可以使用与 OpenAI 客户端兼容的界面将 API 与现有应用程序无缝集成，这对于熟悉 OpenAI 生态系统的开发人员来说非常方便。有关快速概述，请参阅我的 [Perplexity API 教程](https://thenewstack.io/accessing-perplexity-online-llms-programmatically-via-api/)。

该平台还包括 *llama-3-sonar-small-32k-online* 和 *llama-3-sonar-large-32k-online*，它们基于 [FreshLLM 论文](https://thenewstack.io/how-perplexitys-online-llm-was-inspired-by-freshllms-paper/)。这些基于 Llama3 的模型可以返回引文——这是一项目前处于封闭测试阶段的功能。

Perplexity Labs 为其 API 提供灵活的定价模式。按需付费计划根据处理的令牌数量向用户收费，无需预先承诺即可使用。Pro 计划每月收费 20 美元或每年 200 美元，其中包括每月 5 美元的 API 使用额度、无限文件上传和专门支持。

价格根据模型的大小在每百万个令牌 0.20 美元到 1.00 美元之间。除了令牌费用外，在线模型每千次请求还会产生 5 美元的固定费用。

## 3. Fireworks AI

[Fireworks AI](https://fireworks.ai/) 是一个生成式 AI 平台，使开发人员能够为其应用程序利用最先进的开源模型。它提供了广泛的语言模型，包括 [FireLLaVA-13B](https://huggingface.co/fireworks-ai/FireLLaVA-13b)（一种视觉语言模型）、[FireFunction V1](https://huggingface.co/fireworks-ai/firefunction-v1)（用于函数调用）、[Mixtral MoE](https://mistral.ai/news/mixtral-of-experts/) 8x7B 和 8x22B（指令遵循模型）、Meta 的 Llama 3 70B 模型。

除了语言模型外，Fireworks AI 还支持图像生成模型，如 [Stable Diffusion 3](https://fireworks.ai/models/stability/sd3) 和 [Stable Diffusion XL](https://fireworks.ai/models/fireworks/stable-diffusion-xl-1024-v1-0)，这些模型可以通过 Fireworks AI 的无服务器 API 访问，该公司表示该 API 提供了业界领先的性能和吞吐量。

该平台具有竞争力的定价模式。它提供基于处理令牌数量的按需付费定价结构。例如 [Gemma 7B](https://huggingface.co/google/gemma-7b) 模型每百万个令牌的成本为 0.20 美元，Mixtral 8x7B 模型每百万个令牌的成本为 0.50 美元。Fireworks AI 还提供按需部署，用户可以按小时租用 GPU 实例（A100 或 H100）。该 API 与 OpenAI 兼容，使其易于与 LangChain 和 LlamaIndex 集成。

Fireworks AI 面向具有不同定价层级的开发人员、企业和大型企业。开发人员层级提供 600 个请求/分钟的速率限制和最多 100 个已部署模型，而企业和大型企业层级提供自定义速率限制、团队协作功能和专门支持。

## 4. Cloudflare

[Cloudflare AI Workers](https://developers.cloudflare.com/workers-ai/) 是一个推理平台，使开发人员能够仅使用几行代码在 Cloudflare 的全球网络上运行机器学习模型。它为 GPU 加速的 AI 推理提供了一个无服务器且可扩展的解决方案，允许开发人员利用预训练模型执行各种任务——包括文本生成、图像识别和语音识别——而无需管理基础设施或 GPU。

Cloudflare AI Workers 提供了一组精选的流行开源模型，涵盖广泛的 AI 任务。支持的一些著名模型包括：

- llama-3-8b-instruct
- mistral-8x7b-32k-instruct
- gemma-7b-instruct
- vit-base-patch16-224
- segformer-b5-finetuned-ade-512-pt

Cloudflare AI Workers 提供了多功能的集成点，用于将 AI 功能纳入现有应用程序或创建新应用程序。开发人员可以利用 Cloudflare 的无服务器执行环境 [Workers](https://developers.cloudflare.com/workers/) 和 [Pages Functions](https://developers.cloudflare.com/pages/functions/) 在其应用程序中运行 AI 模型。对于那些希望与其当前堆栈集成的开发人员，可以使用 [REST API](https://developers.cloudflare.com/workers-ai/get-started/rest-api/)，从而能够从任何编程语言或框架发出推理请求。该 API 支持文本生成、图像分类和语音识别等任务，并且开发人员可以使用 Cloudflare 的 [Vectorize](https://developers.cloudflare.com/vectorize/)（一个向量数据库）和 [AI Gateway](https://developers.cloudflare.com/ai-gateway/)（用于管理 AI 模型和服务的控制平面）来增强其 AI 应用程序。

Cloudflare AI Workers 使用基于处理神经元数量的按需付费定价模式，为 AI 推理提供了一种经济实惠的解决方案。由于该平台提供了一组超越 LLM 的多样化模型，因此神经元充当类似令牌的单位。所有帐户都有一个免费层，每天允许 10,000 个神经元，其中一个神经元汇总了不同模型的使用情况。除此之外，Cloudflare 每 1,000 个额外神经元收取 0.011 美元。成本因模型大小而异；例如 Llama 3 70B 每百万个输入令牌的成本为 0.59 美元，每百万个输出令牌的成本为 0.79 美元，Gemma 7B 每百万个输入和输出令牌的成本为 0.07 美元。

## 5. Nvidia NIM

[NVIDIA NIM API](https://build.nvidia.com/explore/discover) 提供对各种经过预训的语言模型和其他 AI 模型的访问，这些模型经过 NVIDIA 的软件堆栈的优化和加速。通过 [NVIDIA API 目录](https://nvidia.github.io/GenerativeAIExamples/latest/api-catalog.html)，开发者可以浏览和尝试来自 NVIDIA、Meta、Microsoft、Hugging Face 和其他提供商的 40 多种不同的模型。其中包括来自 Meta 的 Llama 3 70B、Microsoft 的 Mixtral 8x22B 和 NVIDIA 自己的 Nemotron 3 8B 等功能强大的文本生成模型，以及诸如 Stable Diffusion 和 Kosmos 2 之类的视觉模型。

NIM API 允许开发者使用几行代码轻松地将这些最先进的 AI 模型集成到他们的应用程序中。这些模型托管在 Nvidia 的基础设施上，并通过标准化的 OpenAI 兼容 API 公开，从而实现无缝集成。开发者可以使用托管 API 免费对他们的应用程序进行原型设计和测试，并可以选择在准备投入生产时使用最近推出的 [Nvidia NIM 容器](https://nvidianews.nvidia.com/news/nvidia-nim-model-deployment-generative-ai-developers) 在本地或云中部署这些模型。

Nvidia 为 NIM API 提供免费和付费层级。免费层级包括 1,000 个积分以供开始使用，而付费定价基于处理的令牌数量和模型大小，从较小模型（如 Gemma 7B）的每百万个令牌 0.07 美元到大型模型（如 Llama 3 70B）的每百万个输出令牌 0.79 美元不等。

上述列表是提供语言模型作为服务的推理平台的一个子集。在即将发布的文章中，我将介绍可以在 Kubernetes 上运行的自托管模型服务器和推理引擎。敬请期待。
