# New Small AI Model Lets Developers Experiment on iOS
![Featued image for: New Small AI Model Lets Developers Experiment on iOS](https://cdn.thenewstack.io/media/2025/02/3a2744b4-ai2-ai-app-and-new-model-1024x683.jpg)
Developers have a new way to experiment with developing AI apps for [iOS devices](https://thenewstack.io/apples-open-source-roots-the-bsd-heritage-behind-macos-and-ios/) after the release this week of an small open source model from [The Allen Institute for AI](https://allenai.org/) (Ai2) and [Contextual AI](https://contextual.ai/).

The new [language model, called OLMoE,](https://github.com/allenai/OLMoE) works on iPhone 15 Pro or newer (due to hardware restrictions, it won’t work on earlier versions), as well as M-series iPads and Macs. Smaller models will be available on desktops and other versions of Apple phones in the coming weeks, the company added.

The AI can be used to test models locally and integrate the OLMoE model into other iOS applications. Or, you can just play with it.

There are two parts to this release. First, there’s an [open source app](https://github.com/allenai/OLMoE.swift) available under the Apache 2.0 license and available in the [Apple App store](https://apps.apple.com/us/app/ai2-olmoe/id6738533815); it was built by Ai2 and [GenUI](https://www.genui.com/). Second, there’s the [OLMoE language model](https://github.com/allenai/OLMoE) that allows developers to experiment with AI on an iOS device.

“To build this application, we combined our best fully open recipes,” Ai2 wrote in a [post announcing the OLMoE app](https://allenai.org/blog/olmoe-app). “The starting point is OLMoE, our most efficient, fully-open language model.”

## A Private AI
[OLMoE is a mixture-of-experts model (MoE)](https://huggingface.co/allenai/OLMoE-1B-7B-0125), which is a [machine learning technique](https://thenewstack.io/lifelong-machine-learning-machines-teaching-other-machines/) that combines multiple specialized sub-models, called “experts,” to solve a complex problem.
Interactions are private, because they never leave the device and each interaction is deleted once a new conversation begins, Ai2 added. The AI doesn’t track data or send it to the cloud unless the user allows data to be sent in for research purposes.

“Developers may choose to use fully local AI models that aren’t connected to the cloud for privacy, device context, and performance,” said Ai2 research scientist Luca Soldaini. “Privacy is a major factor when handling sensitive user data such as text messages, financial information, or other personal content — keeping everything on-device and never needing to be connected to the cloud ensures that this data is safe and secure.”

## Creating a Small Model
OLMoE can process text at a speed of over 40 tokens per second. [A](https://allenai.org/blog/olmoe-app)[i2 explained how it created the new version](https://allenai.org/blog/olmoe-app) of [allenai/OLMoE-1B-7B-0125-Instruct](https://huggingface.co/allenai/OLMoE-1B-7B-0125-Instruct) by using the [Dolmino mix](https://huggingface.co/datasets/allenai/dolmino-mix-1124) introduced in [OLMo 2](https://allenai.org/olmo) — OLMo is a family of fully-open language models — for mid-training, and the [Tülu 3](https://huggingface.co/collections/allenai/tulu-3-datasets-673b8df14442393f7213f372) post-training recipe.

It has 7 billion (B) parameters but uses only 1B per input token, according to a [research paper on the model](https://arxiv.org/abs/2409.02060). It was trained on 5 trillion tokens and further adapted to create OLMoE-1B-7B-Instruct.

“[OLMoE is a sparse MoE model](https://contextual.ai/olmoe-mixture-of-experts/) with 1 billion active and 7 billion total parameters, allowing it to run easily on common edge devices (e.g., the latest iPhone) while achieving similar or better MMLU performance when compared with much larger models,” wrote AI researcher [Niklas Muennighoff](https://www.linkedin.com/in/muennighoff/) for Contextual AI.

[MMLU stands for Massive Multitask Language Understanding](https://paperswithcode.com/dataset/mmlu?) and evaluates a model’s ability to perform multiple tasks across a variety of subjects.
![A graph that shows how the OLMoE language model compares on performance to cost ratio. It shows a favorable comparison.](https://cdn.thenewstack.io/media/2025/02/f5d3f5c4-olmoe.png)
Chart via [Ai2’s blog](https://allenai.org/blog/olmoe-an-open-small-and-state-of-the-art-mixture-of-experts-model-c258432d0514).

The result is a 4-bit quantized version optimized for mobile performance. Quantization is a technique in machine learning to reduce the precision of the numbers used to represent the model’s weights (parameters). It’s done to make the model smaller and faster to run. Four-bit quantization means each number is now represented using only 4 bits, which drastically reduces the model’s size and computational needs.

## Device as Context
Soldaini added that device context is another important consideration for the model.

“Some applications rely on data that is only available locally, such as a user’s photo album or personal files,” Soldaini said. “If a developer is building an app that uses [retrieval augmented generation (RAG)](https://thenewstack.io/how-to-add-rag-to-ai-agents-for-contextual-understanding/) on data stored on device, it wouldn’t be practical to send those GBs to the cloud for processing.”

Instead, developers can use the OLMoE app as a starting point to do it all where the data is already stored, they added.

Latency and availability play a crucial role in user experience.

“On-device models that aren’t connected to the cloud can operate without delays caused by network communication and remain functional even in environments with poor or no connectivity,” they said. “For many simpler AI tasks, avoiding the round trip to the cloud can significantly improve responsiveness and reliability.”

The model can work offline, allowing [developers to access AI](https://thenewstack.io/ai-is-evolving-rapidly-heres-how-developers-can-keep-pace/) at any time, the company explained. Users can choose to share data with back with Ai2 for research purposes, but do not have to.

“As on-device intelligence systems become more widely adopted, researchers and developers can integrate OLMoE into other iOS applications, or it can be used to experience which real-world tasks state-of-the-art on-device models are capable of,” [Ai2 stated](https://allenai.org/blog/olmoe-app). “It can also be used to improve efficient local AI models or test one’s own model locally using Ai2’s open source codebase.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)