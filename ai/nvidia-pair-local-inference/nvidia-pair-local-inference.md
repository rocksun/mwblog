<!--
title: Nvidia PAIR：让你的闲置Mac和PC为AI代理效力
cover: https://cdn.thenewstack.io/media/2026/09/ba098e5c-local_ai_consumer_blog_ifa_sept_3_kv.jpg
summary: Nvidia推出了开源软件PAIR，利用家庭网络中的闲置Mac和PC运行小型AI模型，通过将任务分发给多个子代理，有效提升了AI代理的工作流程效率，目前支持Windows、macOS及Linux系统。
-->

Nvidia推出了开源软件PAIR，利用家庭网络中的闲置Mac和PC运行小型AI模型，通过将任务分发给多个子代理，有效提升了AI代理的工作流程效率，目前支持Windows、macOS及Linux系统。

> 译自：[Nvidia PAIR lets you put your idle Macs and PCs to work for AI agents](https://thenewstack.io/nvidia-pair-local-inference/)
> 
> 作者：Frederic Lardinois

Nvidia 在开放模型和本地 AI 领域的布局已经成型一段时间了。其[收购 Hugging Face](https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/) 的举措只会加速这一进程，但在产品层面，该公司也在努力吸引更多潜在用户在自己的机器上运行 AI 模型。

周四，Nvidia [发布了](https://blogs.nvidia.com/local-ai%E2%80%93ifa-next-gen-agents-nv-pair-rtx-spark) [Nvidia Personal AI Router (PAIR)，这是一款面向家庭网络的开源](https://www.nvidia.com/en-us/ai-on-rtx/personal-ai-router/)软件路由器，旨在让你利用家中闲置的 Mac 和 PC 按需运行小型模型，并通过子代理（subagents）加速代理工作流。

PAIR 的核心目的是通过允许 NemoClaw、OpenClaw 或 Hermes 等代理并行使用更多子代理来提升其工作效率。其设计理念是让主代理将任务分解给子代理，随后这些子代理的模型请求便可在闲置机器上运行。

![](https://cdn.thenewstack.io/media/2026/09/7d121da0-pair-demo.gif)

图片来源：Nvidia。

Nvidia 将其称为“虚拟推理路由器”，并明确指出这并非一种新的推理引擎。相反，它利用机器上已经安装的 Ollama 或 LM Studio 来运行模型。一旦在每台机器上完成安装，PAIR 即可通过本地网络发现不同的系统（使用 mDNS），并检查它们是否具备处理请求的能力。

需要注意的是，这并不会将单个推理请求拆分到不同机器上。Nvidia 强调，它不会合并 GPU 或将显存池化到一个统一的加速器中，也无法跨机器分割单个推理请求。

“代理可以通过其预期的熟悉本地接口发送请求，”Nvidia 解释道。“PAIR 通过其代理接收请求，识别其引擎和模型需求，并选择一个符合条件的节点。该节点从头至尾执行请求，并通过 PAIR 将响应发回。代理看到的仍然是一个连接，而 PAIR 则在后台处理任务分配。”

![](https://cdn.thenewstack.io/media/2026/09/aebeca77-screenshot-2026-09-03-at-7.56.11-am-1024x587.png)

图片来源：Nvidia。

PAIR 支持配备兼容 GPU 的 Windows、macOS 和 Linux 机器。具体而言，基准要求为 Nvidia GeForce RTX 20 系列及更新的 GPU、配备 M4 芯片或更新架构的 Mac，或 Nvidia DGX Spark（以及预计于今年晚些时候推出的 RTX Spark PC 和笔记本电脑）。

值得称赞的是 Nvidia 对 Mac 的支持，尽管 Mac 不使用 Nvidia GPU，但它们显然已成为运行本地模型和 OpenClaw 等代理的热门选择。

每个系统可以托管不同的模型，但 PAIR 只会将请求路由到已启用所需引擎且拥有确切可用模型的机器上。在多台机器上安装相同的模型，可以为路由器在分发并发请求时提供更多选择。

![](https://cdn.thenewstack.io/media/2026/09/f960beda-screenshot-2026-09-03-at-8.17.23-am-1024x578.png)

图片来源：Nvidia。

PAIR 会实时监控哪些计算机处于可用状态。一旦用户回到某台机器上开始工作（或游戏）并收回 GPU 使用权，本地推理引擎就会停止运行。

在 Nvidia 的案例中，使用 PAIR 连接两台运行高端 RTX 5090 GPU（配有 32 GB 内存，目前售价 5,000 美元，尽管初始建议零售价为 2,000 美元）的 PC，并运行 Qwen3.6 35B A3B 模型，将五个子代理的工作效率提升了约 1.6 倍。

很少有人在家中拥有多张 RTX 5090 显卡（或许还有几台 DGX Spark 台式机），因此，在一个包含 Mac Studio、几台 Mac mini 以及一台游戏 PC 的环境下表现如何还有待观察，但即便如此，这也应该能加速本地代理的工作流。

## 可用性

Nvidia PAIR 目前已发布测试版。若要开始使用，你只需在想要纳入网络的每台机器上安装它，完成系统发现和配对，并确保已安装 Ollama 或 LM Studio（以及已下载模型）。

PAIR 还可以通过在配对机器上安装 Ollama 或 LM Studio 并发起模型下载来辅助设置。