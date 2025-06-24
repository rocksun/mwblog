Vision language models (VLMs) are a promising subset of [multimodal AI](https://thenewstack.io/top-7-tools-for-building-multimodal-ai-applications/), capable of processing the two different modalities of text and image in order to perform a wide range of vision-language tasks — like image captioning, image search and retrieval, text-to-image generation, [visual question answering](https://huggingface.co/tasks/visual-question-answering) (VQA), and [video understanding](https://blog.fastforwardlabs.com/2021/12/14/an-introduction-to-video-understanding-capabilities-and-applications.html).

In our [previous post](https://thenewstack.io/a-developers-guide-to-vision-language-models/) on vision language models, we covered some of the basics of their underlying architecture, some of the strategies for training them, and how they can be used. Now, we’ll look at the most widely used VLMs that are currently available, some common evaluation tools, and the datasets most often used to train them.

## Popular Vision Language Models

Vision language models are developing at an impressive pace, with new and more powerful models emerging all the time. In no particular order, below you can find a non-exhaustive list of some of the most popular VLMs and what they can do.

**[GPT-4o](https://openai.com/index/hello-gpt-4o/):** Developed by OpenAI, this is one of the top proprietary VLMs available, capable of excelling in visual understanding and in generating textual, visual and audio content.

**[Llama 4](https://www.llama.com/):** Meta’s powerful open source multimodal AI model is powered by a new [mixture-of-experts](https://www.ibm.com/think/topics/mixture-of-experts) (MoE) architecture and boasts an eye-watering context window of 10-million tokens. Coming in three different sizes, it’s based around the idea of native multimodality, without the external “patches” that preceding models required for handling vision-based tasks.

**[Gemini 2.5 Flash](https://deepmind.google/models/gemini/flash/):** This version of Google’s flagship AI model demonstrates stronger and faster performance in multimodal understanding and reasoning, with a 1-million token context window and support for multiple images, up to 3,000 images per prompt.

**[DeepSeek-VL2](https://github.com/deepseek-ai/DeepSeek-VL2):** With multiple variants, this impressive open source VLM from DeepSeek AI aims for advanced multimodal understanding in a variety of vision-language tasks. Thanks to its [mixture-of-experts](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/) (MoE) architecture, the model is able to activate fewer parameters to maximize efficiency, while achieving superior performance that rivals similar models.

**[Kimi-VL-Thinking](https://github.com/MoonshotAI/Kimi-VL):** This VLM from Moonshot AI is an “advanced long thinking variant” known for its solid performance in handling longer videos, images and documents.

**[Qwen2.5-VL](https://github.com/QwenLM/Qwen2.5-VL):** Created by Alibaba Cloud, this model shows impressive capabilities in understanding documents and long videos, as well as object localization and multilingual OCR.

**[Gemma 3](http://developers.googleblog.com/en/introducing-gemma3/):** Coming in various sizes, Gemma 3 is Google DeepMind’s answer for a versatile, efficient, lightweight, open-weight and highly capable multimodal AI that can be run on a single TPU or GPU.

**[Molmo](https://molmo.org/):** A family of open source VLMs from the Allen Institute for AI, Molmo is known for highly performant multimodal interaction, while utilizing much less training data than its competitors thanks to its innovative training pipeline that favors speech-based annotations over big datasets.

**[NVLM](https://research.nvidia.com/labs/adlr/NVLM-1/):** NVIDIA’s family of open, frontier-class multimodal AI models are known for their state-of-the-art results in vision-language tasks, notably outperforming many proprietary and open source models in OCR.

**[Pixtral](https://mistral.ai/news/pixtral-large):** Coming in two versions, the open-weight [Pixtral Large](https://mistral.ai/news/pixtral-large) and the open source [Pixtral 12B](https://mistral.ai/news/pixtral-12b), Mistral AI’s multimodal VLMs feature a powerful multimodal decoder and vision encoder to deliver enhanced reasoning and cross-modal comprehension, such as processing long documents with interleaved text and images.

## Evaluating Vision Language Models

The performance of vision language models can be evaluated with a diverse combination of task-specific metrics, benchmarks in specific domains, as well as human-led assessments.

* **Image captioning:** This task combines computer vision and natural language processing, with a textual caption being generated when the model is confronted with a visual image. Popular image-captioning metrics include [BLEU](https://aclanthology.org/P02-1040.pdf), [ROUGE](https://aclanthology.org/W04-1013.pdf), [CIDEr](https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Vedantam_CIDEr_Consensus-Based_Image_2015_CVPR_paper.pdf), [SPICE](https://github.com/peteanderson80/SPICE), [METEOR](https://aclanthology.org/W05-0909.pdf) and [CLIPScore](https://aclanthology.org/2021.emnlp-main.595v2.pdf). Useful benchmarks include [COCO Captions](https://github.com/tylin/coco-caption), [CapArena](https://caparena.github.io/) and [Flickr30K](https://www.kaggle.com/datasets/eeshawn/flickr30k).
* **Visual question answering (VQA):** Visual question answering tasks require the model to correctly answer questions that are derived from a question-image pair. For closed-ended, “yes” or “no” questions, accuracy is measured; while more complex, open-ended questions can be evaluated using human-based analysis, or readapting established metrics like CIDEr. Some helpful benchmarks for these types of tasks include [VQA v2.0](https://visualqa.org/), [GQA](https://cs.stanford.edu/people/dorarad/gqa/about.html) and [OK-VQA](https://okvqa.allenai.org/).

[![](https://cdn.thenewstack.io/media/2025/06/93d2915d-vqa.png)](https://cdn.thenewstack.io/media/2025/06/93d2915d-vqa.png)

* **Visual reasoning and understanding:** Models are evaluated based on their abilities for logical inference. Common benchmarks include [NLVR2](https://github.com/lil-lab/nlvr), the massive [MMMU](https://mmmu-benchmark.github.io/) that contains over 11.5K multimodal challenges, as well as [MathVista](https://mathvista.github.io/) for visual math reasoning, [MMBench](https://github.com/open-compass/mmbench/) for object localization and optical character recognition, and [DocVQA](https://www.docvqa.org/datasets) for visual document understanding.
* **Cross-modal retrieval**: Classed as either image-to-text or text-to-image retrieval tasks, relevant metrics include [Recall@k](https://milvus.io/ai-quick-reference/what-are-the-key-metrics-used-to-evaluate-visionlanguage-models) and [Mean Average Precision](https://www.geeksforgeeks.org/computer-vision/mean-average-precision-map-in-computer-vision/) (mAP).

[![](https://cdn.thenewstack.io/media/2025/06/442ef83e-vlm-tasks.png)](https://cdn.thenewstack.io/media/2025/06/442ef83e-vlm-tasks.png)

[Source](https://arxiv.org/pdf/2210.09263)

However, new evaluation strategies are emerging as VLMs evolve and gain a wider range of capabilities. Some of these include [VHELM](https://openreview.net/pdf?id=TuMnKFKPho) (Holistic Evaluation of Vision Language Models), which assesses VLMs on multiple levels including visual perception, reasoning, robustness, safety and toxicity, and bias and fairness. [Image2Struct](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0718553fd6b227a353c6432cf893285-Paper-Datasets_and_Benchmarks_Track.pdf) is yet another comprehensive approach that evaluates VLMs how well they extract structured information from images.

Nevertheless, human evaluation is also critical when it comes to assessing VLMs for nuance, fluency, relevance and creativity — besides catching any subtle errors that may be glossed over by automated metrics.

## Datasets For Training Vision Language Models

* **LAION-5B:**This open, large-scale [LAION-5B](https://laion.ai/blog/laion-5b/) dataset comprises over 5 billion [CLIP](https://openai.com/index/clip/)-filtered, diverse image-text pairs, with captions in a variety of languages; thus allowing for robust, multilingual model training.
* **PMD (Public Model Dataset)**: With over 70 billion image-text pairs that have been sourced from large-scale datasets like [COCO](https://cocodataset.org/#home), [Conceptual Captions](https://ai.google.com/research/ConceptualCaptions/) and [RedCaps](https://paperswithcode.com/dataset/tvrecap), the [Public Model Dataset](https://huggingface.co/datasets/facebook/pmd) provides a wealth of multimodal data.
* **VQA:** This set of data contains over 200,000 images that are each paired with five questions, which are in turn linked to ten ground-truth answers and three incorrect answers per question. The [VQA](https://visualqa.org/) dataset is commonly used to fine-tune pre-trained VLMs for visual question answering and visual reasoning tasks.
* **Visual Genome:**This [dataset](https://homes.cs.washington.edu/~ranjay/visualgenome/api.html) comprises over 100,000 images with 1.7 million question-answer pairs, with an average of 17 questions per image. In contrast to the VQA dataset, [Visual Genome](https://homes.cs.washington.edu/~ranjay/visualgenome/index.html) offers more balanced questions across six types of questions (who, what, where, when, why, and how), in addition to rich object annotations that capture a wide variety of attributes and relationships.
* **ImageNet:**With over 14 million annotated and organized images, the [ImageNet](https://www.image-net.org/) dataset is most often used for tasks like image classification and object recognition. For tasks that require enhanced explainability and model transparency, [ImageNet-X](https://facebookresearch.github.io/imagenetx/site/home) is yet another option.

## Conclusion

With so many VLMs available, it can be difficult to select the model that is best suited to your use case. Leaderboards and evaluation toolkits like [Vision Arena](https://huggingface.co/spaces/WildVision/vision-arena), [Open VLM Leaderboard](https://huggingface.co/spaces/opencompass/open_vlm_leaderboard), and the open source [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) can help developers make that choice.

Nevertheless, despite their powerful capabilities, some potential challenges will need to be addressed when working with VLMs — such as bias, cost, hallucinations, and difficulties with the model learning to generalize in order to make accurate predictions on new data it hasn’t seen before.

Ultimately, as the landscape for vision-language models continues to evolve, we can expect models to become more sophisticated and capable of tackling ever-more complex tasks.

For more information, check out our [previous post](https://thenewstack.io/a-developers-guide-to-vision-language-models/) on vision language models, outlining the architecture and some of the learning techniques for training VLMs.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/09/69f0904d-tgcfilao_400x400.jpg)

Kimberley Mok is a tech and design reporter who covers artificial intelligence, robotics, quantum computing, tech culture and science stories for The New Stack. Trained as an architect, she is also an illustrator and multidisciplinary designer who has been passionate...

Read more from Kimberley Mok](https://thenewstack.io/author/kimberleymok/)