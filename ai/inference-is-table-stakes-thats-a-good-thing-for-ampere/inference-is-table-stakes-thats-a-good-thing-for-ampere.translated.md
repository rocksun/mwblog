## 推理是基本赌注。这对 Ampere 来说是件好事

![Ampere 的特色图片：推理是基本赌注](https://cdn.thenewstack.io/media/2024/05/c259c0c0-table-stakes-2-1024x576.jpg)

**巴黎 —**

基于 ARM 架构制造 CPU 的制造商 [Ampere](https://amperecomputing.com/) 正在利用 [推理](https://thenewstack.io/when-cloud-meets-intelligence-inference-ai-as-a-service/) 作为一大亮点，让人们了解其存在。[AI 训练](https://thenewstack.io/hpc-kubernetes-ai-training-on-3500-gpus/) 是一个批处理工作流，但推理在以 AI 为重点的应用程序开发中至关重要。所有应用程序最终都需要推理才能保持微调和更新。

Ampere 的亮点是什么？云原生是其中之一，此外还有其性能以及它对虚拟机可能带来的嘈杂邻居问题的看法。

Ampere 是一家半导体公司，

[由英特尔高管创立](https://www.reuters.com/technology/oracle-use-amperes-newest-chips-its-cloud-offering-2023-09-20/)，由 [首席执行官 Renée James](https://www.linkedin.com/in/renee-j-james-64182424/) 领导。它为云服务和构建其基础设施的公司制造芯片。其客户包括所有主要云提供商，但 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) 除外，后者拥有类似的技术 [Gravitron](https://thenewstack.io/amazon-q-a-genai-to-understand-aws-and-your-business-docs/)。

Ampere 的故事围绕

[开源](https://thenewstack.io/open-source/) 展开，以及在不使用 [NVIDIA](https://thenewstack.io/nvidia-wants-to-rewrite-the-software-development-stack/) 和集成其 CUDA 库（将 GPU 与软件集成的必需软件）的情况下在其架构上运行任何工作负载的能力。

“因此，重点在于启用整个开源生态系统，”

[Victor Jakubiuk](https://www.linkedin.com/in/jakubiuk/)，Ampere 的 AI 副总裁，在巴黎举行的 KubeCon + CloudNativeCon Europe 上告诉 The New Stack。

## 推理在规模上很重要

Jakubiuk 说，PyTorch 和 TensorFlow 等开源

[框架](https://thenewstack.io/the-ultimate-guide-to-machine-learning-frameworks/) 在纯 CPU 上高效运行推理。它们专门针对推理进行优化，以确保在运行时为这些 AI 模型生成的代码对其 CPU 来说是最佳的，并且可以同时跨多个服务器进行扩展。

Jakubiuk 说，推理效率在规模上很重要。

他说：“如果对于 AI 训练，你训练了一个模型，它可能很昂贵。” “但是一旦你有了这个模型，一旦你投入部署，你实际上会将它乘以 10 倍、100 倍、1000 倍，因为你在大规模部署它。当你将它乘以 1000 倍时，你可能遇到的任何低效率都会乘以 1000 倍。同时，任何效率提升都会显著增加。”

通过结合软件和硬件优化，客户可以为其数据中心提供的每瓦特能源获得更好的性能，因此，云中的最终用户可以获得更好的总体拥有成本 (TCO)。

Jakubiuk 说，有三个核心用例：

**计算机视觉工作负载：**处理视频和图像的任何内容。**推荐引擎：**例如，电子商务推荐引擎。**大型语言模型 (LLM)：**处理文本以生成文本，或尝试理解文本。Ampere 对 Mistral 和 Llama 等开源模型表现出了特别的兴趣。

首先，CPU 的原始性能及其大量的内核使其适合与 LLM 一起使用。下一步是每瓦性能方面的 TCO。Jakubiuk 说，这是一个优势，它让 Ampere 的 CPU 优于 GPU。如果你运行组织的数据中心，这会产生差异；电力几乎在所有地方都是一个问题。随着数据中心需要大量电力，最大化性能变得至关重要。

Jakubiuk 说，Ampere CPU 运行超过 128 个内核。它们可以在没有任何嘈杂邻居问题的情况下运行任何工作负载，避免了 x86 CPU 在运行虚拟机时出现的性能限制问题。一台虚拟机可能会变得计算密集型，而另一台虚拟机可能正在运行数据库或繁重的工作负载，由于热量和电源问题，这会降低 x86 CPU 的性能。Ampere 重新设计了 CPU 以避免嘈杂邻居的问题。

Jakubiuk 说，Ampere 提供开箱即用的推理。由 GPU 训练的模型在 Ampere 上运行，建议使用 TensorFlow 或 PyTorch。三个核心 AI 框架在 Ampere 的 CPU 上运行：TensorFlow、PyTorch 和 Onyx。它们专注于为开源社区提供支持，以及来自 Hugging Face 和使用 Jupyter Notebook 上的 VM 构建的模型等来源。
**Corrected Markdown Text:**

“值得一提的两个模型是 LLaMA 和 MiSTRAL，因为它们迄今为止是最流行的模型，”Jakubiuk 说。“它们的运行性能非常好，尤其是在每瓦性能方面。正如我所说，对于 LLaMA，每花费一美元，你最多可以获得 80% 的性能提升，而不是在 GPU 上运行它们。”

[Janakiram MSV](https://thenewstack.io/author/janakiram/)，长期分析师，也是 The New Stack 的常客，表示推理将成为应用程序开发的关键，类似于 API 的重要性。代理将从推理中出现，这将通过检索增强生成 (RAG) 开发。

这将导致云原生社区代理的新兴，他表示这将在今年和 2025 年成为焦点。

“每个可观察性公司都将拥有自己的代理，该代理可以发现异常、执行根本原因分析并使用此数据来实施 RAG，”

[Janakiram](https://thenewstack.io/large-language-model-observability-the-breakdown/) 说。

代理——讨论的都是代理。它们将出现在消费者技术中，例如

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、采访、演示等。