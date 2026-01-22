<!--
title: Nvidia DGX Spark：The New Stack开发者指南
cover: https://cdn.thenewstack.io/media/2026/01/a7fb5204-dgx-spark.b8400a71.jpg
summary: Nvidia DGX Spark是台式AI超算，提供本地化AI开发能力，统一内存架构支持大模型微调和推理，通过DGX OS整合Nvidia AI生态，优化开发者工作流。
-->

Nvidia DGX Spark是台式AI超算，提供本地化AI开发能力，统一内存架构支持大模型微调和推理，通过DGX OS整合Nvidia AI生态，优化开发者工作流。

> 译自：[Nvidia DGX Spark: The New Stack Developer's Guide](https://thenewstack.io/nvidia-dgx-spark-the-new-stack-developers-guide/)
> 
> 作者：Janakiram MSV

[在本地运行大型AI模型](https://thenewstack.io/red-hat-customizes-rhel-for-nvidias-vera-rubin-ai-platform/)的能力定义了开发者生产力的下一个前沿。如果没有桌面级AI计算，数据科学家和AI开发者仍然受限于云基础设施，受到延迟、成本不可预测性和数据主权问题的制约。

[Nvidia DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)是一款紧凑型桌面外形的“个人AI超级计算机”。有了DGX Spark，开发者可以获得一个自包含的AI开发平台，将数据中心的功能带到他们的桌面，从而无需离开CUDA生态系统，即可对多达2000亿参数的模型进行快速迭代。

对于构建生产就绪模型的Nvidia科学家和AI开发者来说，理解DGX Spark的架构至关重要。其模式与熟悉的GPU计算概念相呼应——统一内存架构类似于现代SoC（片上系统）中的共享地址空间，软件栈扩展了您已在使用的Nvidia NGC容器生态系统，而集群功能则呼应了桌面规模的分布式训练范式。

本指南全面概述了DGX Spark的硬件规格、软件环境、主要用例以及定价和可用性的实际考量。

## Nvidia DGX Spark是什么？

[Nvidia DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)是一款紧凑型AI工作站，以仅重2.6磅的桌面外形提供高达1 petaFLOP的FP4 AI性能。它围绕GB10 Grace Blackwell超级芯片构建，将基于ARM的CPU与Blackwell一代GPU集成在一个封装中，通过NVLink-C2C连接以实现高带宽的芯片间通信。

该系统预装了Nvidia完整的AI软件栈，使开发者无需配置复杂的依赖项即可对大型语言模型进行原型开发、微调和运行推理。

将DGX Spark视为一个针对开发者工作流优化的便携式数据中心节点。就像您可能使用高内存工作站进行数据预处理，然后再部署到生产集群一样，DGX Spark充当您的本地AI开发环境，在Spark上验证的模型可以在更大的DGX基础设施上无缝运行。

统一内存架构消除了CPU和GPU内存之间PCIe（外围组件互连快速）传输的传统瓶颈，允许两个处理器无缝访问相同的128 GB内存池。

该系统代表了Nvidia将其生态系统从云和数据中心部署扩展到个人开发者工作站的战略。该设备最初在CES 2025上作为DIGITS项目发布，随后在GTC 2025上更名为DGX Spark，并于去年10月实现商业可用。它面向AI研究员、数据科学家和学生，他们需要持续访问强大的本地计算来进行模型开发，而无需争夺共享集群资源或管理云成本。

## 硬件架构：GB10 Grace Blackwell超级芯片

DGX Spark的核心是Nvidia GB10 Grace Blackwell超级芯片，这是一个与MediaTek共同设计的片上系统，将计算、内存和高速网络集成到一个封装中。GB10结合了20核ARM CPU（具有10个高性能Cortex-X925核心和10个效率导向的Cortex-A725核心）以及配备第五代Tensor Cores的Blackwell一代GPU。这种架构平衡了原始计算能力与能源效率，使整个系统能够在140瓦的热设计功耗包络内运行。

这里的类比很简单：GB10的功能类似于您在现代移动设备中遇到的集成式SoC，但针对AI工作负载进行了扩展。正如Apple的M系列芯片统一了CPU和GPU内存以实现无缝数据访问一样，GB10提供了相干的统一内存寻址，其中两个处理器共享相同的物理DRAM而无需显式数据传输。

CPU和GPU通过NVLink-C2C互连而不是PCIe进行通信，与独立GPU配置相比，提供了更快、更节能的芯片间通信。

考虑一个场景，您正在加载一个700亿参数的模型进行微调。在传统的独立GPU设置中，模型权重必须通过PCIe总线从系统RAM传输到VRAM，带宽限制在大约64GB/s。而DGX Spark的统一内存，整个128GB内存池可由CPU和GPU直接访问，消除了这种传输开销。GPU可以立即开始张量操作，而CPU在相同的地址空间中处理预处理。

### 内存配置

DGX Spark配备128 GB的LPDDR5X统一内存，由围绕GB10封装的八个16GB芯片组成。此内存由CPU和GPU相干共享，提供大约273 GB/s的总带宽。虽然此带宽低于RTX 5090等独立GPU的1700 GB/s，但统一架构通过完全消除CPU-GPU数据传输的PCIe瓶颈来弥补。

### 存储子系统

该系统支持1TB到4TB的NVMe（非易失性内存高速）存储配置，具体取决于SKU，Nvidia创始人版附带4TB存储。存储可以配置自加密，以满足具有数据安全要求的组织的需求。NVMe接口提供了足够的吞吐量，可在开发迭代期间加载大型模型检查点和数据集。

### 网络功能

DGX Spark包括一个Nvidia ConnectX-7 SmartNIC，提供双QSFP（四通道小型可插拔）端口，能够提供200 Gbps的总带宽。这种企业级网络硬件，作为独立组件通常价值超过1500美元，使两个DGX Spark单元能够集群在一起，对多达4050亿参数的模型进行分布式推理。其他连接包括一个10 GbE RJ-45以太网端口、四个支持240瓦供电的USB-C端口、HDMI输出和Wi-Fi 7，以适应灵活的部署场景。

### 散热和电源设计

紧凑型机箱采用前后气流冷却，前后表面均配有金属泡沫面板。该系统需要随附的240W USB-C电源适配器才能获得最佳性能，对于工作站级硬件而言，这是一种不寻常的设计选择，它简化了在没有专用电源基础设施的办公环境中的部署。

## 软件环境：DGX OS和AI栈

DGX Spark运行[DGX OS](https://docs.nvidia.com/dgx/dgx-spark/software.html)，这是一个定制化的[基于Ubuntu 24.04的Linux发行版](https://thenewstack.io/how-to-safely-upgrade-ubuntu-22-04-to-ubuntu-24-04/)，针对Nvidia硬件上的AI工作负载进行了优化。操作系统预配置了完整的CUDA工具包、cuDNN库、用于优化推理的TensorRT以及Nvidia容器运行时（用于Docker）。这种开箱即用的软件配置消除了在设置GPU环境时通常会消耗开发者数小时的复杂驱动程序和依赖项管理。

将DGX OS视为一个经过验证的AI开发参考平台。正如企业级Linux发行版为生产服务器提供经过测试、支持的配置一样，DGX OS提供了一个专门针对GB10硬件验证的已知良好软件环境。

相同的DGX OS基础在数据中心中更大的DGX系统上运行，确保在Spark上开发的代码迁移到生产基础设施时不会出现兼容性问题。

该软件栈包括对[Nvidia NGC](https://docs.nvidia.com/dgx/dgx-spark/ngc.html)的访问，这是一个GPU优化容器、预训练模型和AI框架的注册表。开发者可以拉取针对Grace Blackwell架构进行性能调优的PyTorch、TensorFlow和JAX容器。

NGC还提供对Nvidia NIM微服务（用于模型服务）和Nvidia Blueprints（用于标准化AI应用程序模式）的访问。这些资源通过提供经过验证的起点来加速开发，而无需从头开始进行环境配置。

### 容器运行时集成

Nvidia容器运行时预装并配置好，使Docker容器能够透明地访问GPU资源。开发者可以立即从NGC拉取并运行GPU加速容器，无需额外设置。ARM64原生的NGC CLI提供了对针对Grace CPU架构优化的容器注册表和模型下载的命令行访问。

### 开发工具

DGX Spark包括一个可通过网页浏览器访问的集成DGX仪表板，用于监控系统利用率、管理JupyterLab会话和配置系统设置。该仪表板提供了对GPU和内存利用率的可见性，无需SSH访问，使其对偏好图形界面的开发者也易于使用。JupyterLab集成支持在Spark硬件上直接进行交互式基于笔记本的开发。

### 框架兼容性

包括[PyTorch](https://thenewstack.io/why-pytorch-won/)和[TensorFlow](https://thenewstack.io/googles-new-tensorflow-tools-and-approach-to-fine-tuning-ml/)在内的主要深度学习框架在DGX Spark上原生运行，并提供完整的CUDA加速。RAPIDS和Dask等数据科学工具也受支持，可以实现GPU加速的数据处理工作流和模型训练。该系统支持包括Ollama、SGLang和vLLM在内的流行推理框架，用于本地服务大型语言模型。

## 主要用例：DGX Spark的优势所在

DGX Spark专为AI工作流的迭代开发阶段而设计，在该阶段，快速实验比生产规模的吞吐量更为重要。128GB的统一内存容量和完整的CUDA支持使其成为那些原本依赖云GPU实例或共享集群分配的团队的本地开发环境。

### 模型原型开发和实验

DGX Spark使开发者能够完全离线地进行AI工作流原型开发，在投入云资源之前测试模型架构、数据管道和服务配置。一致的硬件环境消除了共享基础设施的变数，在整个开发会话中提供可重现的结果。团队可以在提示工程、检索增强生成管道和代理式AI工作流上进行迭代，而无需按小时支付计算成本。

### 微调中型模型

凭借128GB的统一内存，DGX Spark支持微调多达约700亿参数的模型，具体取决于精度和技术。开发者可以为特定领域应用定制基础模型，训练LoRA（低秩适应）适配器，或对开源模型执行指令微调。本地执行将专有训练数据保留在本地，解决了具有数据主权限制的组织的合规性要求。

### 大型语言模型推理

DGX Spark可以对多达2000亿参数的模型进行推理，包括Llama、DeepSeek、Mistral和Qwen等流行的开源模型。该系统擅长提示处理，即LLM推理的计算密集型阶段，其中Blackwell GPU的张量核心提供了强大的性能。令牌生成速度受内存带宽限制，因此Spark最适合开发验证而非高吞吐量生产服务。

### 本地AI应用开发

[CUDA支持](https://thenewstack.io/nvidia-finally-adds-native-python-support-to-cuda/)、容器运行时和网络功能的结合使DGX Spark适用于开发最终将部署到边缘或本地环境的AI驱动应用程序。构建机器人应用、计算机视觉系统或私有AI助手的开发者可以在部署前在本地进行开发和测试。一致的软件栈确保容器化应用程序在Spark和生产DGX基础设施上运行相同。

### 教育和研究

大学和研究机构可以为学生和研究员提供专用的AI计算资源，而无需管理共享集群调度或云预算。DGX Spark的自包含特性简化了IT管理，同时为学术项目提供了访问企业级AI软件和硬件的途径。

## 理解权衡

DGX Spark代表了计算频谱中的一个特定点，了解其局限性有助于开发者选择合适的工作负载。273 GB/s的内存带宽虽然足以满足开发工作流，但与具有专用高带宽内存的独立GPU相比，限制了令牌生成速度。对于需要最大吞吐量的生产推理，仍然需要更大的系统或GPU集群。

ARM64 CPU架构为假定x86处理器的软件引入了兼容性考量。虽然CUDA生态系统和主要框架支持ARM64，但一些专业工具和库可能需要额外配置或替代方案。DGX OS提供了经过最彻底测试的软件环境，社区正在努力扩展分发兼容性。

| 要求 | DGX Spark适用性 | 理由 |
| --- | --- | --- |
| 原型开发LLM应用 | 优秀 | 完整CUDA栈、128 GB内存、本地执行 |
| 微调多达700亿参数的模型 | 优秀 | 统一内存支持大型模型微调 |
| 对多达2000亿参数的模型进行推理验证 | 良好 | 内存容量支持加载，带宽限制速度 |
| 高吞吐量生产推理 | 有限 | 内存带宽限制令牌生成速率 |
| 多GPU分布式训练 | 有限 | 仅支持双节点集群，不适用于大规模训练 |
| 以Windows为主的工作流 | 不推荐 | DGX OS基于Ubuntu，不支持Windows |
| 通用桌面计算 | 不推荐 | 针对AI工作负载优化，不适用于消费级应用 |

生产部署通常将DGX Spark用于开发，并结合更大的DGX系统或云基础设施进行训练和服务。DGX家族一致的软件栈确保在Spark上验证的代码可以部署到生产环境而无需大量返工。

## 定价和可用性

Nvidia DGX Spark于2025年10月15日商业上市，创始人版定价3999美元，包含4TB NVMe存储。此定价使DGX Spark成为专业AI开发的一项重要但可承受的投资，大约相当于数百小时的云GPU租用，同时提供无限的本地计算访问。

基于GB10架构的合作伙伴OEM系统提供更多选择，起价更低。配备1TB存储的华硕 Ascent GX10定价约为2999美元，而Dell、HP、Lenovo及其他合作伙伴的系统提供不同的存储配置和外形。国际定价因增值税和地区因素而异，英国零售价约为3700英镑，欧盟市场约为3689欧元。

### 直接购买选项

Nvidia通过其市场[marketplace.nvidia.com](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/)直接销售创始人版，包括一个价值90美元的免费深度学习学院课程。自发布以来供应一直受限，许多零售商显示按需订购或缺货状态，而非立即供货。

### OEM合作伙伴系统

几家Nvidia合作伙伴提供基于GB10的系统，在存储、散热设计和定价方面有所不同。Dell的Pro Max（配备GB10）与Dell AI Factory生态系统集成，适用于标准化Dell基础设施的组织。HP的ZGX Nano AI工作站面向具有HP支持和保修结构的企业环境。华硕、宏碁、技嘉、联想和微星也已宣布或发布了具有不同配置的基于GB10的系统。这些合作伙伴系统运行相同的DGX OS和软件栈，确保无论硬件供应商如何，都与Nvidia的AI平台兼容。

### 成本考量

对于持续的开发工作负载，一次性硬件成本与云GPU租用相比具有优势。以每小时2到10美元的典型云定价，DGX Spark的购买价格相当于数百小时的计算时间，并具有数据隐私、零出口费用和消除竞价实例波动等额外好处。对数据本地性有合规性要求的组织可能会在本地AI开发基础设施中发现特殊价值。

## 后续内容

Nvidia DGX Spark代表了AI开发基础设施的重大转变，将完整的DGX软件栈带给以前依赖云资源或共享集群的个人开发者和小型团队。统一内存架构消除了传统的CPU-GPU数据传输瓶颈，而Nvidia完整的AI栈确保了与生产DGX部署的兼容性。

对于数据科学家和AI开发者来说，这些模式都很熟悉。GB10的统一内存行为类似于您在Apple Silicon或移动处理器中遇到的现代SoC架构。NGC容器生态系统扩展了您在云GPU上使用的相同工具。DGX OS环境反映了在企业DGX基础设施上运行的内容。

对于AI团队而言，实际意义是在开发到部署工作流中多了一个新选择。DGX Spark为迭代开发阶段提供了持续、可预测的本地计算，在该阶段，实验速度比原始吞吐量更为重要。团队可以在投入生产基础设施之前，在本地验证模型、测试服务配置和开发代理式AI工作流。在本地DGX Spark开发和云资源之间做出选择取决于工作负载特性、数据敏感性要求以及每个组织特定的成本结构。

在下一篇文章中，我们将仔细研究DGX OS和软件栈。敬请期待！