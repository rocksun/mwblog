<!--
title: 英伟达推出支持提示词的语音转写模型
cover: https://cdn.thenewstack.io/media/2026/10/3f644518-img_5875-edit-scaled.jpg
summary: 英伟达发布了开源的多语言提示词转写模型 Nemotron 3.5 Transcribe。该模型在 Hugging Face 榜单上名列前茅，支持通过提示词设置上下文、指定术语、区分说话人以及音频问答等功能，具备极高的准确率与多语言处理能力。
-->

英伟达发布了开源的多语言提示词转写模型 Nemotron 3.5 Transcribe。该模型在 Hugging Face 榜单上名列前茅，支持通过提示词设置上下文、指定术语、区分说话人以及音频问答等功能，具备极高的准确率与多语言处理能力。

> 译自：[Nvidia launches a promptable transcription model](https://thenewstack.io/nvidia-nemotron-promptable-transcription/)
> 
> 作者：Frederic Lardinois

Nvidia 周三发布了 Nemotron 3.5 Transcribe，这是其最新的多语言转写模型。该公司表示，这款新的开源权重模型在 Hugging Face 的 Open ASR 开源模型英文排行榜上名列前茅，平均词错误率（WER）为 5.33%，并且在两个说话人归属基准测试中也名列榜首。

但可能更有趣的是，这是一个**支持提示词（promptable）**的转写模型。这里的支持提示词意味着用户可以在模型听取音频之前为其提供具体指令。通常，这意味着通过告诉模型给定的音频文件是一个关于英语的医学讨论，并为其提供一个医学术语列表来为转写设置上下文。

用户还可以指示模型标记每个说话人或询问有关音频的问题。例如，他们可以请求逐字转录或精简版本，并告诉模型如何格式化数字。

![来自 VoiceArena 的 Diarization-Bench v1 的条形图，按拼接最小排列字错误率 (cpWER) 排列了 14 个在有重叠语音的英语完整会话上的双向分离加 ASR 系统，其中越低越好。NVIDIA Nemotron 3.5 Transcribe 以 32.4% 排名第一，其次是 NVIDIA Multitalker Parakeet + N3D，为 34.2%；其余系统的范围从 34.7% 到 71.9%。](https://cdn.thenewstack.io/media/2026/10/c0e04146-transcribe-35-nvidia-1024x522.png)

图片来源：Nvidia。

Nvidia 将这些功能与翻译功能打包到一个单一的检查点中，这可以简化围绕它们构建应用程序的工作。

理想情况下，设置此上下文会降低错误率。代价是这些模型的体积比传统的转写模型大得多，传统模型的参数量通常不到 10 亿个。Nemotron 3.5 Transcribe 是一个拥有 300 亿参数、40 亿激活参数的混合专家（MoE）模型。

不过，这并不是一个完全崭新的概念。我们最近看到了一些其他的语音转文本模型，比如 Mistral 的 Voxtral 模型和 AssemblyAI 的 [Universal 3 Pro](https://www.assemblyai.com/universal-3-pro)。

不过，Nvidia 能够以少得多的激活参数与 Voxtral 的错误率相媲美。在 Artificial Analysis 的基准测试中，Nemotron 的词错误率为 2.81%，而 Voxtral Small 为 2.77%，同时它使用大约 40 亿个激活参数，而 Voxtral 则为 240 亿个。不过，该比较衡量的是准确性与激活参数数量的关系，而不是运行时间或内存需求。

该模型可以转录 40 种语言，并将其中 31 种语言翻译成英文或从英文翻译。说话人归属功能适用于其中 13 种语言，并且它可以区分最多八个说话人的声音。音频问答功能则是使用英语进行训练的。

该模型处理最长一小时的录音。不过，它是为录制音频而构建的，不支持实时流式传输。

![](https://cdn.thenewstack.io/media/2026/10/2f5127e7-screenshot-2026-10-27-094551-1024x621.png)

图片来源：Nvidia。

开发者可以使用 [vLLM](https://github.com/NVIDIA-NeMo/Speech/blob/main/docs/source/speechlm2/vllm_serving.rst) 提供模型服务，或者使用 [NeMo-Speech.cpp](https://github.com/NVIDIA/NeMo-Speech.cpp) 在本地运行它。Nvidia 表示它可以在单个 GPU 上运行，支持的硬件范围从 Jetson AGX Thor 和 DGX Spark 到 Blackwell 数据中心 GPU。

由于这是一个开源权重模型（在 OpenMDW-1.1 许可证下），用户可以使用 NeMo Speech 的微调工具等工具根据自己的需求对其进行微调，以降低错误率。

在医疗转录案例研究中，Nvidia 表示，通过微调，使用其最佳提示词时，未参与训练的说话人的词错误率从 22.44% 降至 12.17%，相对减少了 45.8%。完整的适配工作流在单个 GB300 上花费了约 14 个 GPU 小时。

Nvidia 还发布了 Granary v2，这是一个使用 NeMo Curator 构建的可重用数据策展管道，以及涵盖 48 种语言和 16 个源语料库大约 463,062 小时的公共清单。开发者可以在自己的录音上运行该管道，为自定义准备数据。这些数字描述的是数据集发布情况，而不是 Transcribe 的完整训练混合物或其采样权重。