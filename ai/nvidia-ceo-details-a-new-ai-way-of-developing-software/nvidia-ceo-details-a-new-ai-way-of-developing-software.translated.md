# 英伟达首席执行官详细介绍了开发软件的新 AI 方式

![英伟达首席执行官详细介绍了开发软件的新 AI 方式的特色图片](https://cdn.thenewstack.io/media/2024/03/c206efb3-jensen_huang-nvidia-1024x589.png)

在过去几周，英伟达首席执行官黄仁勋 [直言不讳地表示](https://thenewstack.io/nvidia-wants-to-rewrite-the-software-development-stack/)，随着人工智能的不断进步，人们 [无需了解如何编程](https://thenewstack.io/making-sense-of-sam-altmans-7-trillion-ai-chips-gambit/)。

在本周举行的英伟达年度 GPU 技术大会 ( [GTC](https://www.nvidia.com/gtc/) ) 上，黄仁勋 [重申了他的话](https://blogs.nvidia.com/blog/2024-GTC-keynote/)，并在他的主题演讲中解释了该公司在主题演讲中如何重写软件开发。

许多人谈到了使用人工智能来生成代码，但英伟达正在将其付诸实践。黄仁勋谈到了更大的目标——用编写程序的新方法清除整个开发管道。

“我们如何在未来构建软件？你不太可能从头开始编写它，或者编写一大堆 Python 代码或类似的东西。你很可能会组建一个由人工智能组成的团队，”黄仁勋说。

## 计划是什么？

英伟达正在创建一个以聊天机器人和副驾驶为基础，用于创建应用程序的特定于人工智能的 [软件开发周期](https://thenewstack.io/security-testing-must-be-part-of-software-development-life-cycle/)。

“可能会有一个超级人工智能，它接受你的任务，并将其分解为执行计划，”黄仁勋说。

编程语言是英语。用户可以在 ChatGPT 风格的界面中输入他们想要的程序，输出将是应用程序，黄仁勋说。

随着能够推理的人工智能计算机站稳脚跟，软件创建模型正在向新的方向转变。

[当前的软件开发周期](https://thenewstack.io/devops/) 在很大程度上依赖于 CPU 的逻辑特性。

“新的计算机将‘帮助你为未来创建一种新型应用程序。不是你从头开始完全编写的应用程序，”黄仁勋说。

英伟达宣布了“人工智能代工厂”的概念，作为生成应用程序的所谓构建套件。用户只需拼出他们想要的应用程序类型，基于英伟达硬件和软件的人工智能代工厂就会吐出应用程序。

![](https://cdn.thenewstack.io/media/2024/03/8e4b0635-vivy0652-1-scaled.jpg-1024x683.webp)

由英伟达提供。

## 后端是什么？

英伟达的开发工作流依赖于使用会话和自动化界面来编写、打包和部署软件。目标是切断传统 CI/CD 管道中涉及的手动劳动。

“我们将为你发明一种接收和操作软件的新方法，”黄仁勋说。

英伟达希望通过副驾驶、人工智能界面、容器和微服务来自动化软件创建和代码生成。英伟达的界面 [自动配置依赖项](https://thenewstack.io/automated-dependency-management-with-depfu/) 并进行相关的微调。

最重要的组件是 NIM（英伟达推理微服务），它更像是一个人工智能 API，已在 GTC 上宣布。NIM 帮助用户通过访问正确的数据、大型语言模型、编程工具和依赖项来创建应用程序。

所有经过预训练的专有和开源 [大型语言模型](https://thenewstack.io/top-5-large-language-models-and-how-to-use-them-effectively/) 都存储在构建在 Kubernetes 之上的容器中。该容器（更像是一个黑匣子）还包括一个针对 GPU、英伟达的 [CUDA 并行编程语言](https://thenewstack.io/nvidias-cuda-12-is-here-to-bring-out-the-animal-in-gpus/)、CuDNN 神经网络和其他工具（如 TensorRT，它提高了推理性能）进行了优化的 [云原生堆栈](https://thenewstack.io/what-is-the-modern-cloud-native-stack/)。

各种 NIM 协同工作，在黑匣子中生成和执行代码，然后将最终结果传递给客户。

“该 NIM 可能可以理解 SAP——SAP 的语言是 ABAP，它可能理解 ServiceNow 并从其平台检索一些信息，”黄仁勋说。

用户无需编码，即可用简单的英语交谈。

“这是一款未来的软件，它有一个非常简单的 API。该 API 被称为人类，”黄仁勋说。

英伟达堆栈使用标准的行业 API 来处理语音、文本、图像和视频。英伟达宣布了名为 AI Enterprise 5.0 的新人工智能软件，其中包括可以检索信息的 NeMo Retriever 和提供信息的 Triton Inference Server。

英伟达软件堆栈从数据库中检索结构化和非结构化数据，并将其转换为会话数据。
## Nvidia 的 AI 数据库

“从本质上来说，获取结构化数据或非结构化数据，了解其含义，对其含义进行编码。因此，这现在变成了一个 AI 数据库，”黄说。“一旦创建它，你就可以与它对话。”

SAP、ServiceNow、Cohesity 和 [Snowflake](https://www.snowflake.com/?utm_content=inline-mention) 是使用 Nvidia 的 NIM 创建副驾驶、聊天机器人和虚拟助手的部分客户，以便客户可以使用简单的英语进行交互。

## Nvidia 的 AI 堆栈起源

Nvidia 的专有 AI 软件堆栈，[称为 CUDA](https://thenewstack.io/nvidia-hones-in-on-apple-like-approach-to-ai-with-cuda/)，最初于 2006 年作为高性能计算的编程模型。

2012 年，CUDA 与 AlexNet（一种用于图像识别的神经网络）进行了“首次接触”。这是在 Nvidia GPU 上训练的第一个神经网络。

“认识到这种计算模型的重要性，我们发明了一种全新的计算机类型，我们称之为 DGX-1 — 这台超级计算机有 170 万亿次浮点运算，八个 GPU 首次连接在一起。我亲手将第一台 DGX-1 送到了位于旧金山的初创公司 OpenAI，”黄说。

2022 年，Nvidia 的 GPU 被用于将 ChatGPT 变成现实。

![](https://cdn.thenewstack.io/media/2024/03/ac4fee75-mjc_2441-2-scaled.jpg-1024x683.webp)

由 Nvidia 提供。

## 这将是一个 AI 世界

可以肯定的是，黄的宏伟计划与 AI 系统的编程更相关，这些系统可以针对特定客户需求进行定制。这与传统的 CI/CD 模型不同。

但市场要求编码人员快速提升 AI 技能——根据 [马里兰大学](https://www.aimaps.ai/) 的研究，在 IT 工作岗位下降的市场中，与 AI 相关的技术工作岗位数量正在上升。

Nvidia 占据 AI 市场主导地位，并正在采取自下而上的方法——如果你想使用 Nvidia GPU，你 [需要了解其开发模型](https://thenewstack.io/ai-development-needs-to-focus-more-on-data-less-on-models/) 的工作原理。

“首先是拥有 AI 技术，其次是帮助你修改，第三是用于微调的基础设施，”黄说。

Nvidia 在贸易展上推出了一款名为 Blackwell 的新 GPU，公司高管表示，这款 GPU 在单个 GPU 上提供了 20 拍浮点的 AI 性能。一组 576 个 Blackwell GPU 可以训练数万亿参数模型。

## 挑战

Nvidia 希望客户使用其昂贵的硬件和软件，这需要使用 CUDA，并造成了进入壁垒。

云提供商（例如 [CoreWeave](https://www.coreweave.com/gpu-cloud-pricing) 和 [Lambda Labs](https://lambdalabs.com/service/gpu-cloud)）上的 Nvidia H100 GPU 实例每小时的价格是旧款 A100 型号的两倍。

谷歌提出了其基于 AI 的 Duet 服务创建自定义程序（例如财务工具）的想法，只需与 AI 交谈即可。Nvidia 的主要竞争对手 AMD、[英特尔](https://thenewstack.io/intels-gelsinger-openais-altman-augur-the-future-of-genai/) 和 Cerebras 正在采用开源软件方法。这些公司支持包括 Llama 2 和 Mixtral 在内的开放模型，但芯片制造商不提供客户可以通过与计算机交谈来编写应用程序的工具。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。