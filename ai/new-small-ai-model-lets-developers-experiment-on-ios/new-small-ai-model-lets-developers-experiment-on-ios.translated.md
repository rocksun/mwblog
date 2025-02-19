# 新的小型AI模型让开发者在iOS上进行实验

![用于：新的小型AI模型让开发者在iOS上进行实验的特色图片](https://cdn.thenewstack.io/media/2025/02/3a2744b4-ai2-ai-app-and-new-model-1024x683.jpg)

在本周发布了来自艾伦人工智能研究所 (Ai2) 和Contextual AI的一个小型开源模型后，开发者有了一种新的方法来实验为[iOS设备](https://thenewstack.io/apples-open-source-roots-the-bsd-heritage-behind-macos-and-ios/)开发AI应用程序。

新的[名为OLMoE的语言模型](https://github.com/allenai/OLMoE)可在iPhone 15 Pro或更新机型上运行（由于硬件限制，它无法在早期版本上运行），以及M系列iPad和Mac。该公司补充说，未来几周内，将提供可在台式机和其他版本的苹果手机上运行的较小型号。

该AI可用于在本地测试模型并将OLMoE模型集成到其他iOS应用程序中。或者，你也可以只玩玩它。

此版本有两个部分。首先，有一个[开源应用程序](https://github.com/allenai/OLMoE.swift)在Apache 2.0许可下可用，并在[Apple App Store](https://apps.apple.com/us/app/ai2-olmoe/id6738533815)中提供；它由Ai2和GenUI([https://www.genui.com/](https://www.genui.com/))构建。其次，是[OLMoE语言模型](https://github.com/allenai/OLMoE)，它允许开发者在iOS设备上试验AI。

Ai2在其[发布OLMoE应用程序的博文中](https://allenai.org/blog/olmoe-app)写道：“为了构建这个应用程序，我们结合了我们最好的完全开放的方案。”“起点是OLMoE，我们最高效的、完全开放的语言模型。”

## 私人AI

[OLMoE是一个专家混合模型 (MoE)](https://huggingface.co/allenai/OLMoE-1B-7B-0125)，这是一种[机器学习技术](https://thenewstack.io/lifelong-machine-learning-machines-teaching-other-machines/)，它结合了多个专门的子模型（称为“专家”）来解决复杂问题。
Ai2补充说，交互是私密的，因为它们从未离开设备，并且每次交互在新的对话开始时都会被删除。除非用户允许将数据发送用于研究目的，否则AI不会跟踪数据或将其发送到云端。

Ai2的研究科学家Luca Soldaini说：“开发者可以选择使用完全本地化的AI模型，这些模型不连接到云端，以确保隐私、设备上下文和性能。”“在处理敏感用户数据（例如文本消息、财务信息或其他个人内容）时，隐私是一个主要因素——将所有内容保存在设备上，无需连接到云端，确保这些数据安全可靠。”

## 创建小型模型

OLMoE可以每秒处理超过40个token的文本。[Ai2解释了它是如何创建allenai/OLMoE-1B-7B-0125-Instruct的新版本](https://allenai.org/blog/olmoe-app)的，方法是使用在[OLMo 2](https://allenai.org/olmo)中引入的[Dolmino混合](https://huggingface.co/datasets/allenai/dolmino-mix-1124)——OLMo是一个完全开放的语言模型系列——进行中期训练，以及[Tülu 3](https://huggingface.co/collections/allenai/tulu-3-datasets-673b8df14442393f7213f372)后期训练方案。

根据一篇[关于该模型的研究论文](https://arxiv.org/abs/2409.02060)，它有70亿(B)个参数，但每个输入token仅使用10亿个参数。它在5万亿个token上进行了训练，并进一步调整以创建OLMoE-1B-7B-Instruct。

Contextual AI的AI研究员Niklas Muennighoff写道：[OLMoE是一个稀疏的MoE模型](https://contextual.ai/olmoe-mixture-of-experts/)，具有10亿个活动参数和70亿个总参数，使其能够轻松地在常见的边缘设备（例如最新的iPhone）上运行，同时与更大的模型相比，实现了相似或更好的MMLU性能。

[MMLU代表大规模多任务语言理解](https://paperswithcode.com/dataset/mmlu?)，它评估模型在各种主题上执行多项任务的能力。

![显示OLMoE语言模型在性能与成本比率上的比较的图表。它显示了一个有利的比较。](https://cdn.thenewstack.io/media/2025/02/f5d3f5c4-olmoe.png)

图表来自[Ai2的博客](https://allenai.org/blog/olmoe-an-open-small-and-state-of-the-art-mixture-of-experts-model-c258432d0514)。

结果是一个针对移动性能优化的4位量化版本。量化是机器学习中一种技术，用于降低用于表示模型权重（参数）的数字的精度。这样做是为了使模型更小，运行速度更快。4位量化意味着每个数字现在只使用4位来表示，这大大减少了模型的大小和计算需求。

## 设备作为上下文
Soldaini补充说，设备上下文是模型的另一个重要考虑因素。

“一些应用程序依赖于仅在本地可用的数据，例如用户的相册或个人文件，”Soldaini说。“如果开发人员正在构建一个使用[检索增强生成 (RAG)](https://thenewstack.io/how-to-add-rag-to-ai-agents-for-contextual-understanding/)处理存储在设备上的数据的应用程序，那么将这些GB的数据发送到云端进行处理是不切实际的。”

他们补充说，开发人员可以使用OLMoE应用程序作为起点，在数据已存储的位置完成所有操作。

延迟和可用性在用户体验中起着至关重要的作用。

“与云端未连接的设备端模型可以在没有网络通信造成的延迟的情况下运行，即使在连接不良或无连接的环境中也能保持功能，”他们说。“对于许多更简单的AI任务，避免往返云端可以显著提高响应速度和可靠性。”

该公司解释说，该模型可以在离线状态下工作，允许[开发人员随时访问AI](https://thenewstack.io/ai-is-evolving-rapidly-heres-how-developers-can-keep-pace/)。用户可以选择与Ai2共享数据以用于研究目的，但并非必须这样做。

“[随着设备端智能系统越来越广泛地被采用，研究人员和开发人员可以将OLMoE集成到其他iOS应用程序中，或者可以使用它来体验最先进的设备端模型能够完成哪些现实世界的任务，”[Ai2声明](https://allenai.org/blog/olmoe-app)，“它还可以用于改进高效的本地AI模型，或使用Ai2的开源代码库在本地测试自己的模型。”

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。