# 5 Small-Scale Multimodal AI Models and What They Can Do
![Featued image for: 5 Small-Scale Multimodal AI Models and What They Can Do](https://cdn.thenewstack.io/media/2024/12/73fd52e7-getty-images-o5asjrfw4lo-unsplashb-1024x576.jpg)
Over the past few years, we’ve seen the meteoric growth of [large language models](https://thenewstack.io/what-is-a-large-language-model/) (LLMs) that have now mushroomed into billions of parameters, making them powerful tools when it comes to tasks like analyzing, [summarizing](https://thenewstack.io/how-to-summarize-large-documents-with-langchain-and-openai/) and generating text and [images](https://thenewstack.io/the-power-and-ethical-dilemma-of-ai-image-generation-models/), or creating [human-sounding chatbots](https://thenewstack.io/building-smarter-chatbots-with-advanced-language-models/).

Of course, all that power comes with some significant limitations, especially if users don’t have deep pockets or the hardware to accommodate the considerable computational resources these LLMs require. So it’s no wonder that we’re witnessing the [emergence of small language models](https://thenewstack.io/the-rise-of-small-language-models/) (SLMs), which cater specifically to users who are more resource-constrained.

Now, with the growing interest in [multimodal AI systems](https://thenewstack.io/top-7-tools-for-building-multimodal-ai-applications/) that can simultaneously process different types of data (images, text, audio and video), there’s also been a coinciding increase in smaller versions of these polyvalent tools as well. In the rest of this article, we’ll cover five small multimodal AI tools that have been getting a lot of attention lately.

## 1. TinyGPT-V
This powerful yet resource-efficient 2.8-billion parameter multimodal model processes both text and image inputs, and maintains an impressive level of performance while using significantly fewer resources compared to its larger cousins.

[TinyGPT-V](https://github.com/DLYuanGod/TinyGPT-V)‘s scaled-down architecture features optimized transformer layers that strike a balance between size, performance and efficiency, in addition to using a specialized mechanism that processes image inputs and integrates them with text inputs. It is built using the relatively small LLM [Phi-2](https://dev-kit.io/blog/ai/microsoft-phi-2?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform), combining it with pre-trained vision modules from [BLIP-2](https://thenewstack.io/a-guide-to-model-composition/) or [CLIP](https://openai.com/index/clip/).
It can be fine-tuned with smaller datasets, making it a good option for small- and medium-sized companies, or for those looking to locally deploy it in educational or research contexts (where funding and resources might be more limited).

## 2. TinyLlaVA
This novel framework integrates vision encoders like CLIP-Large and SigLIP, as well as a small-scale LLM decoder, an intermediary connector, and customized training pipelines — all in order to attain high-level performance that still keeps computational use to a minimum.

[TinyLlaVA](https://huggingface.co/collections/bczhou/tinyllava-65e584a5e8b017ee1347a0a7) is trained with two different datasets: LLaVA-1.5 and ShareGPT4V. The supervised fine-tuning process permits the adjustment of partially learnable parameters of the LLM and the vision encoder.
According to [tests](https://arxiv.org/pdf/2402.14289), TinyLlaVA’s best-performing variant, the TinyLLaVA-share-Sig-Phi 3.1B variant, outperforms 7B models like LLaVA-1.5 and Qwen-VL. Additionally, the framework offers a holistic analysis of model selections, training recipes, and data contributions to the performance of small-scale LMMs. It’s a great example of how leveraging small-scale LLMs can provide significant advantages in accessibility and efficiency, without sacrificing performance.

## 3. GPT-4o mini
Released as a smaller and cheaper version of OpenAI’s [GPT-4o](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/) multimodal model, GPT-4o mini costs approximately 60 percent less to run than GPT-3.5 Turbo, previously the most affordable model in OpenAI’s line of models.

GPT-4o mini is derived from the larger GPT-4o via a [distillation process](https://www.datacamp.com/blog/distillation-llm), resulting in an excellent balance between performance and cost-efficiency. It features a large 128K context window, multimodal capabilities to process both text and images, with planned future support for video and audio. It also features enhanced safety features against jailbreaks, system prompt extractions, and prompt injections.

Use cases for GPT-4o mini might include rapid prototyping for new chatbots, on-device apps for language learning or personal assistants, interactive games, as well applications in educational settings.

## 4. Phi-3 Vision
This powerful vision-language variant of Microsoft’s Phi-3 is a transformer-based model that contains an image encoder, connector, projector, and the Phi-3 Mini language model. At 4.2-billion parameters, [Phi-3 Vision](https://huggingface.co/microsoft/Phi-3-vision-128k-instruct) is capable of supporting up to 128K context length in tokens, and “[extensive multimodal reasoning](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/phi-3-vision-%E2%80%93-catalyzing-multimodal-innovation/4170251)” that permits it to understand and generate content based off charts, graphs and tables.

With performance that rivals that of larger models like OpenAI’s GPT-4V, Phi-3 Vision could be well-suited to resource-constrained environments and latency-bound scenarios, offering advantages for offline operation, cost, and user privacy.

Potential use cases include document and image analysis to improve customer support, social media content moderation, and video analysis for companies or educational institutions.

## 5. Mississippi 2B and Mississippi 0.8B
Recently released by [H2O.ai](https://h2o.ai/), these are two multimodal foundation models designed specifically for OCR and Document AI use cases. Intended to be compact yet efficient, these vision-language models offer businesses a scalable and cost-effective way to perform document analysis and image recognition in real-time.

The models feature multi-stage training with fine-tuning of layers and minimal latency — making them a good fit for healthcare, banking, insurance and finance, where a large volume of documents need to be processed.

Both [H2OVL Mississippi 2B](https://huggingface.co/h2oai/h2ovl-mississippi-2b) and [H2OVL Mississippi 0.8B](https://huggingface.co/h2oai/h2ovl-mississippi-800m) are freely available on Hugging Face at the moment, making it an accessible option for developers, researchers, and enterprises to fine-tune and modify.

## Conclusion
Accessibility and cost-efficiency remain major issues with multimodal models, and with large language models in general. But with an increasing number of relatively lightweight yet powerful multimodal AI options becoming available, this means that many more institutions and smaller businesses will be able to adopt AI into their workflow.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)