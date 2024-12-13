# 5 Multimodal AI Models That Are Actually Open Source
![Featued image for: 5 Multimodal AI Models That Are Actually Open Source](https://cdn.thenewstack.io/media/2024/12/7ffb0188-oleg-ivanov-pnx4vnp_fgm-unsplashb-1024x576.jpg)
Multimodal AI is attracting a lot of attention, thanks to the tantalizing promise of AI systems that are designed to be jacks of all trades — capable of processing a combination of text, image, audio, and video.

But while there is already a constellation of [powerful, proprietary multimodal AI systems](https://thenewstack.io/top-7-tools-for-building-multimodal-ai-applications/) on the market, [smaller multimodal AI models](https://thenewstack.io/5-small-scale-multimodal-ai-models-and-what-they-can-do/) and open source alternatives are also rapidly gaining ground, as users continue to seek out options that are more accessible and adaptable, and prioritize transparency and collaboration. To get you up to speed on the latest open source multimodal AI systems, we’ll outline some of the more popular options — including their features and uses.

## 1. Aria
The recently introduced [Aria](https://github.com/rhymes-ai/Aria) AI model from [Rhymes AI](https://rhymes.ai/) is [touted](https://www.rhymes.ai/blog-details/aria-first-open-multimodal-native-moe-model) as the world’s first open source, multimodal native [mixture-of-experts](https://huggingface.co/blog/moe) (MoE) model that can process text, code, images, and video — all within one architecture.

This versatile model is relatively powerful compared to even larger models, yet is more efficient, as it [selectively leverages](https://arxiv.org/pdf/2410.05993) relevant subsets (or “mini-experts”) of its framework, depending on the task. Its architecture is designed for ease of scalability, as new “experts” could be added to address new tasks without straining the system. Aria excels at long multimodal input understanding, meaning that it is adept at quickly and accurately parsing long documents and videos.

![](https://cdn.thenewstack.io/media/2024/12/348e4131-aria.png)
Aria’s architecture.

## 2. Leopard
Developed by an interdisciplinary team of researchers from University of Notre Dame, Tencent AI Seattle Lab, and the University of Illinois Urbana-Champaign (UIUC), [Leopard](https://github.com/tencent-ailab/Leopard) is an open source multimodal model that is specifically designed for text-rich image tasks.

Leopard is [intended](https://arxiv.org/pdf/2410.01744) to tackle two of the biggest challenges in the multimodal AI space, namely the scarcity of high-quality multi-image datasets, and balancing image resolution with sequence length. To achieve this, the model is trained with a curated [dataset](https://huggingface.co/datasets/wyu1/Leopard-Instruct/tree/main) featuring over 1 million high-quality, human-made and synthetic data pieces that have been collected from real-world examples. It is also openly [available](https://huggingface.co/datasets/wyu1/Leopard-Instruct/tree/main) for use in other models.

“Leopard stands out with its novel adaptive high-resolution encoding module, which dynamically optimizes the allocation of visual sequence lengths based on the original aspect ratios and resolutions of the input images,” [Wenhao Yu](https://www.linkedin.com/in/wenhao-yu-242355153/), a senior researcher at Tencent America and one of the creators of Leopard, explained to The New Stack. “Additionally, it uses pixel shuffling to losslessly compress long visual feature sequences into shorter ones. This design enables the model to handle multiple high-resolution images without sacrificing detail or clarity.”

These features make Leopard an excellent tool for multi-page document understanding (think slide decks, scientific and financial reports), data visualization, webpage comprehension, and in deploying multimodal AI agents capable fo handling tasks in visually complex environments.

![](https://cdn.thenewstack.io/media/2024/12/fd2720de-leopard.png)
Leopard’s overall model pipeline.

## 3. CogVLM
Utilizing deep fusion techniques to attain high performance, CogVLM stands for [Cognitive Visual Language Model](https://arxiv.org/pdf/2311.03079), an open source, state-of-the-art visual language foundational model that can be used for [visual question answering](https://blog.roboflow.com/what-is-vqa/) (VQA) and image captioning.

CogVLM uses an [attention-based fusion mechanism](https://openreview.net/pdf?id=c72vop46KY) that fuses text and image embeddings, and freezes network layers to keep performance high. It also employs a [EVA2-CLIP-E](https://arxiv.org/pdf/2303.15389) visual encoder and a multi-layer perceptron (MLP) adapter for co-mapping visual and text features onto the same space.

## 4. LLaVA
[Large Language and Vision Assistant](https://llava-vl.github.io/) (LLaVA) is another open source, state-of-the-art option. It leverages [Vicuna](https://huggingface.co/lmsys/vicuna-7b-v1.5) to decode language, and CLIP for fine-tuning on instruction-following textual data. The model has been trained using instruction-following text-based data generated by ChatGPT and GPT-4. LLaVA uses a trainable projection matrix to map visual representations onto the language embedding space.
As a versatile visual assistant, LLaVA can be used to create more advanced chatbots that can handle text- and image-based queries.

## 5. xGen-MM
Also known as BLIP-3, this state-of-the-art, open source suite of multimodal models from [Salesforce](https://www.salesforce.com/) features a line of variants, including a [base pretrained model](https://huggingface.co/Salesforce/xgen-mm-phi3-mini-base-r-v1.5), an [instruction-tuned model](https://huggingface.co/Salesforce/xgen-mm-phi3-mini-instruct-interleave-r-v1.5), and a [safety-tuned model](https://github.com/salesforce/LAVIS/tree/xgen-mm?tab=readme-ov-file) that is intended to reduce harmful outputs.

One crucial development is that the systems were trained using a massive, open source trillion-token [dataset of “interleaved” image and text data](https://blog.salesforceairesearch.com/mint-1t/), which the researchers characterize as the “the most natural form of multimodal data”. That means the models are skilled at handling inputs with text and multiple images, which could be useful in a wide range of settings — such as autonomous vehicles, or image analysis and diagnosing diseases in healthcare, or creating interactive educational tools, or promotional marketing materials.

## Conclusion
There is still an ongoing, [vigorous debate](https://thenewstack.io/why-open-source-ai-has-no-meaning/) surrounding the [actual definition of open source AI](https://thenewstack.io/the-open-source-ai-definition-is-out/), peppered with accusations of large tech companies “[open washing](https://thenewstack.io/calls-to-ban-open-source-are-misguided-and-dangerous/)” their AI models in order to gain wider credibility and cachet.

Regardless of how the open source AI debate unfolds, it’s clear that there’s still a further need for truly open source systems — and datasets — that emphasize transparency, collaboration and accessibility and that actually live up to the open source ethos.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)