<!--
title: GenAI揭示硅谷芯片古董
cover: https://cdn.thenewstack.io/media/2023/12/88ad96d3-year-wrapup-1-1024x576.png
-->

2023年，英特尔和AMD意识到，他们传统的CPU销售业务模式在新的以人工智能为主导的计算领域中变得不太相关。

> 译自 [Year in Review: GenAI Exposed Silicon Valley Chip Antiquity](https://thenewstack.io/year-in-review-genai-exposed-silicon-valley-chip-antiquity/)，作者 Agam Shah 覆盖了超过十年的企业IT。除了机器学习、硬件和芯片，他还对武术和俄罗斯感兴趣。

多年来，英特尔（Intel）和AMD一直是[芯片制造领域的贵族](https://thenewstack.io/farewell-moores-law/)，但ChatGPT的出现正唤醒了它们的沉寂。

“实际上，我们认为人工智能是过去50年来最具变革性的技术。也许唯一接近的是互联网的引入，” AMD首席执行官[Lisa Su](https://www.amd.com/en/corporate/leadership/lisa-su.html)在12月的一次活动中表示。

人工智能的概念已经存在几十年，但2023年将被视为GPU使得全面用户界面应用成为可能的一年。英伟达（Nvidia）[准备好了硬件和软件](https://thenewstack.io/nvidia-gpu-dominance-at-a-crossroads/)，顺利地加入了[生成式人工智能的狂潮](https://thenewstack.io/how-linkedin-overcame-challenges-of-building-generative-ai/)。

在年初，云服务提供商争相升级数据中心，配备大量的GPU和冷却系统，以处理史诗般的人工智能潮流。Nvidia的GPU成功地推动了微软加速进入生成式人工智能的步伐，搭配Bing搜索引擎。

自20世纪60年代以来一直以CPU为基础的英特尔和AMD在一夜之间意识到，他们传统的商业模式在新的计算格局下已经不再相关。人工智能需要加速器来处理大量低精度计算，而CPU在处理这方面并不高效。

生成式人工智能暴露了在数据中心运行推断和训练的高成本，微软和Meta启动了他们自己的人工智能芯片战略，以削减数据中心成本。

## Nvidia制霸

[Nvidia首席执行官黄仁勋](https://www.nvidia.com/en-us/events/aws-reinvent/?ncid=pa-srch-goog-453983&gad_source=1&gclid=Cj0KCQiAyeWrBhDDARIsAGP1mWTnNhaXbB8TQaWG_vNNeRbUTKpWquwjfl6VjSwurtcg7kvJS6bbYwgaArEvEALw_wcB)已经成为一位巨星，并被誉为使人工智能成为可能的关键人物。该公司的市值飙升，超过1万亿美元。

![](https://cdn.thenewstack.io/media/2023/12/98435d86-jensen_huang-nvidia-300x233.jpg)

*黄仁勋*

Nvidia的[H100 GPU备受瞩目](https://www.weforum.org/videos/what-is-h100-gpu-chip-ai-nvidia/)，等待名单很长。[该公司在软件方面也做好了充分准备](https://thenewstack.io/nvidia-hones-in-on-apple-like-approach-to-ai-with-cuda/)，使用了CUDA，该技术最早于2007年发布，作为一套编程工具，可利用GPU进行更快的计算。

随着人工智能的兴起，CUDA作为[软件堆栈的流行度](https://thenewstack.io/cuda-12-harnesses-a-nvidias-speedier-gpu-architecture/)迅速上升，Nvidia已经为医疗、汽车和工程等垂直领域创建了现成的人工智能软件包。而英特尔和AMD仍在努力整理他们的软件堆栈。

Nvidia还因试图绕过美国出口限制向中国出售其GPU而引起负面关注，而中国一直是该公司历史上非常重要的市场。

去年，美国对强大的GPU和人工智能芯片实施了出口限制，以遏制中国推进人工智能基础设施的努力，但Nvidia[调整了规格，为中国市场提供了符合规定的GPU](https://www.cnn.com/2023/12/06/tech/nvidia-china-chip-development-us-curbs/index.html)。今年初，美国再次实施出口限制以阻止Nvidia向中国出口，但该公司已经生产了符合新出口限制的芯片。

## 开源与闭源

对于AI中的专有技术，如GPT-4等闭源模型以及Nvidia的CUDA开发堆栈，也引起了一些[反感](https://thenewstack.io/open-models-not-stymied-yet/)。

英特尔和AMD似乎希望客户抵制闭源模型，转而采用开源模型，如[Llama 2](https://thenewstack.io/metas-llama-2-is-not-open-source-and-thats-ok/)，这消除了客户采用AMD和英特尔AI加速器的入门障碍。Llama 2已经与AMD最近推出的GPU MI300X和英特尔的Gaudi 2（该公司目前正在出货）兼容。

“在模型开发方面，有很多对开源框架的加强，比如[AMD的] [ROCm](https://www.amd.com/en/products/software/rocm.html) 和 [Intel的] [OneAPI](https://thenewstack.io/oneapi-computing-aims-to-ease-multi-architecture-computing/)。同时，苹果也在增加对ML框架的投资，例如面向Apple Silicon的MacOS的[MLX](https://github.com/ml-explore/mlx)，” [CCS Insight](https://www.ccsinsight.com/why-ccs-insight/)的首席分析师[James Sanders](https://www.linkedin.com/in/jamesaltonsanders/)表示。

Nvidia的竞争对手也在构建工具，以便开发人员可以轻松部署和运行模型，而不用担心后台运行的硬件。例如，Intel的SYCLomatic可以剥离CUDA代码，并指向最适合运行计算的硬件。

然而，Intel和AMD想要实现的目标仍然复杂，首先要从[Hugging Face](https://huggingface.co/)下载调优过的模型，然后将代码指向正确的硬件。

随着框架的成熟，基础模型的移植，硬件供应商将会更多地就在其平台上使用其系统的成本效益以及开源AI/ML模型的可用性和灵活性进行产品推广，Sanders说。

## 云服务提供商成为AI芯片制造商

Nvidia的芯片并不会消失，但云服务提供商并未把所有鸡蛋放在一个篮子里。年底时，前三大云服务提供商相继推出了他们的最新AI芯片。

[微软的Azure AI堆栈](https://thenewstack.io/sc500-microsoft-now-has-the-third-fastest-computer-in-the-world/)主要是基于Nvidia的GPU构建的，但今年推出了Maia 100 AI加速器，用于训练和推断。

微软的首席财务官[Amy Hood](https://news.microsoft.com/exec/amy-hood/)谈到了人工智能的每次交易成本，以及硬件和软件调优如何提高了GPU利用率，从而帮助产生更多收入。[微软表示](https://news.microsoft.com/source/features/ai/in-house-chips-silicon-to-service-to-meet-ai-demand)，其对自家芯片的投资旨在提高性能的同时降低使用Azure的成本。

“专门为其运行的芯片总是更好的选择，” [Tirias Research](https://www.tiriasresearch.com/)首席分析师[Jim McGregor](https://www.linkedin.com/in/tekstrategist/)表示。

谷歌最近在其云服务中推出了[TPU v5](https://cloud.google.com/blog/products/compute/announcing-cloud-tpu-v5e-and-a3-gpus-in-ga)芯片，供内部和外部使用。TPU v5p用于训练，最终将用于训练谷歌未来的转换模型，谷歌计算和机器学习基础设施副总裁兼总经理[Mark Lohmeyer](https://www.linkedin.com/in/marklohmeyer/)表示。

TPU v5芯片位于谷歌称之为“Hypercomputer”的AI超级计算机中。

“它设计用于出色的性能、高效率、非常划算，适用于我们在那里看到的最常见的部署场景，” Lohmeyer说。

[亚马逊云计算](https://aws.amazon.com/?utm_content=inline-mention)在其ReInvent大会上推出了[Trainium2](https://www.nextplatform.com/2023/12/04/how-aws-can-undercut-nvidia-with-homegrown-ai-compute-engines/)芯片。该芯片将通过其AWS服务提供给客户。

## 芯片和路线图的变革

芯片制造商还花费时间调优生成式人工智能的路线图。英伟达希望利用其早期优势，计划在2025年之前每年发布新的GPU，这是其典型的两年一次的变化。英伟达在其最新的GPU [H200](https://www.nvidia.com/en-us/data-center/h200/)中采用了HBM3e，该芯片将于明年上市，而[AMD的MI300X](https://www.nextplatform.com/2023/12/06/amd-is-the-undisputed-datacenter-gpu-performance-champ-for-now/)则堆叠内存芯片以增加容量。

![](https://cdn.thenewstack.io/media/2023/12/ca31aa16-nvidia-hgx-h200-300x169.jpg)

*英伟达HGX H200*

Intel取消了多款GPU，并将其下一代GPU“Falcon Shores”定于2025年发布。最初的Falcon Shores设计将CPU和GPU集成到一个芯片上，但由于客户对离散GPU用于生成式人工智能的兴趣更大，因此取消了该设计。

除了GPU之外，芯片制造商在芯片设计中将内存容量和带宽列为重中之重。查询通常存储在内存中，直到会话结束，而在单个会话中积累的问题越多，就需要更多的内存，并且需要快速的吞吐量以更快地响应。

围绕[Compute Express Link](https://www.computeexpresslink.org/download-the-specification)（CXL）规范的新系统架构将成为系统设计中的标准，以满足内存和带宽的要求。

## 2024年可以期待什么？

Intel和AMD成熟的AI芯片将为Nvidia的GPU提供有价值的第二来源。[微软](https://news.microsoft.com/?utm_content=inline-mention)和[甲骨文](https://developer.oracle.com/?utm_content=inline-mention)已经在云中采用了AMD的MI300X。

“你将会看到更多来自超大规模计算供应商的定制芯片，用于更特定的工作负载，” Tirias Research的首席分析师Jim McGregor表示。

生成式人工智能主要是服务器活动，但将会扩展到客户端设备以实现更低的延迟，McGregor说。

将生成式人工智能卸载到客户端设备将提高神经芯片或GPU在客户端设备上的相关性，这将作为本地加速器。笔记本电脑将被优化以承载实际应用的生成模型。已经有一些例子，比如微软集成GPT-4与Copilot，以及Adobe在Firefly中集成生成式人工智能。

“这些公司并非试图在云中运行这些生成式模型。焦点将放在‘如何获取通用模型以及如何为应用程序进行优化，如何进行知识蒸馏 — 例如用于法律和医疗应用等，” McGregor说。
