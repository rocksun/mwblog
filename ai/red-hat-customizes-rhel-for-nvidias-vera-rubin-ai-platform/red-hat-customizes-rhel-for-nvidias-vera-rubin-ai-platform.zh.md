在与芯片公司持续合作的基础上，[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 承诺将在英伟达新发布的 [Vera Rubin 平台](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer) 于今年晚些时候推出时，提供“Day 0”支持。

这家企业开源软件公司旨在缩小英伟达硬件平台发布与其自身支持软件堆栈（为其旗舰操作系统 Red Hat Enterprise Linux (RHEL) 针对 Rubin 设计的定制版本）全面上市之间的发布差距。

英伟达的 Vera Rubin 平台旨在降低 AI 推理的成本。它基于新型 CPU、GPU 和数字处理单元 (DPU) 构建，所有这些都与其他组件紧密相连。

## 硬件和软件同步发布

根据 Red Hat 发言人的说法，该平台和 Red Hat 的软件都预计在 2026 年下半年推出。

当 Rubin 平台推出时，Red Hat 存储库将提供经过验证的 Nvidia GPU OpenRM 驱动程序和 CUDA 工具包。

Red Hat 的软件还将能够在英伟达最新发布的 [机密计算](https://www.nvidia.com/en-us/data-center/solutions/confidential-computing/) 安全架构的范围内运行 AI 生命周期，该架构提供工作负载保护的加密证明。

除了 RHEL，Red Hat 还将发布适用于 Rubin 的 Kubernetes [Red Hat OpenShift](https://thenewstack.io/red-hat-openshift-4-20-boosts-ai-security-hybrid-cloud/) 平台，并且 [Red Hat AI 平台](https://thenewstack.io/choosing-the-right-red-hat-ai-solution-rhel-ai-vs-openshift-ai/) 将扩展对 Red Hat AI 推理服务器、Red Hat Enterprise Linux AI 和 Red Hat OpenShift AI 上使用英伟达开源模型进行分布式推理的支持。

## 介绍 Vera Rubin

英伟达首席执行官 [黄仁勋](https://www.linkedin.com/in/jenhsunhuang/) 在 2026 年国际消费电子展 ([CES](https://thenewstack.io/ces-2025-worst-in-show-betas-for-a-dystopian-future/)) 的主题演讲中介绍了 [Vera Rubin](https://www.nvidia.com/en-us/data-center/technologies/rubin/)。它以美国天文学家 [Vera Florence Cooper Rubin](https://airandspace.si.edu/stories/editorial/meet-vera-rubin) 的名字命名，她发现了暗物质，暗物质占据了我们宇宙的大部分。

该平台承担着另一个艰巨的任务：降低运行大规模 [AI 推理工作负载](https://thenewstack.io/5-reasons-to-use-kubernetes-for-ai-inference/) 呈爆炸式增长的计算（和电力使用）成本。

该公司声称，通过精心设计组件使其更紧密地协同工作，Vera Rubin 可以将训练模型的推理令牌成本降低 10 倍，同时使用的 GPU 数量减少 4 倍，相比之下，传统上用于此类任务的是英伟达 [Blackwell 平台](https://thenewstack.io/developers-can-now-uber-gpus-with-nvidias-lepton-platform/)。

该平台的以太网光子交换系统也有望将能效提高五倍。

Vera 是该平台的 [88 核 CPU](https://www.nvidia.com/en-us/data-center/vera-cpu/) 的名称，而 Rubin 则是 GPU 的名称，它 [提供 50 PFLOPs](https://youtu.be/0NBILspM4c4?list=TLGGTaKMRZHNIn4wNjAxMjAyNg&t=9875) 的数学运算能力（是 Blackwell 提供的 5 倍）。通过 [Nvidia BlueField-4 DPU](https://www.nvidia.com/en-us/networking/products/data-processing-unit/) 进一步锁定计算加速。这些处理单元都与 [NVLink 6 Switch](https://www.nvidia.com/en-us/data-center/nvlink/)、[Nvidia ConnectX-9 SuperNIC](https://www.nvidia.com/en-us/networking/products/ethernet/supernic/) 和 [Nvidia Spectrum-6 以太网交换机](https://www.nvidia.com/en-us/networking/ethernet-switching/) 紧密交织，所有这些都采用英伟达芯片制造。

## 推理的成本

随着公司加大 AI 投入，他们发现通过 GPU 最有效完成的推理工作变得越来越昂贵。

本周，[亚马逊网络服务](https://aws.amazon.com/?utm_content=inline+mention) (AWS) [将其 GPU 的成本提高了 15%](https://x.com/MuthaNagavamsi/status/2008339575346000252)。

推理成本确实一直萦绕在英伟达高管的心头。该公司还与 Groq 签署了 [一份价值 200 亿美元的许可协议](https://www.fierce-network.com/cloud/heres-why-nvidia-dropping-20b-groqs-ai-tech)，以获取其推理和编译器技术。

在他的主题演讲中，英伟达的黄仁勋谈到了最近 AI 系统中推理活动的急剧增加。不仅模型本身变得越来越大，推理量本身也急剧飙升。推理不再用于生成单个“一 shot”答案，而是一个通常涉及多个模型和额外后训练的“思考过程”。

因此，需要更多的推理。

黄仁勋表示：“现在有了强化学习，这本质上是计算机尝试不同的迭代来学习如何执行一项任务。因此，预训练、后训练和测试时间扩展所需的计算量已经爆炸式增长。”

Anthropic 联合创始人兼首席执行官 Dario Amodei 在一份声明中指出：“英伟达 Rubin 平台的效率提升代表着基础设施的进步，能够实现更长的记忆、更好的推理和更可靠的输出。”

除了 Red Hat（IBM 旗下公司）之外，其他已承诺支持 Rubin 平台的公司包括：

AWS、Anthropic、[思科](http://cisco.com/?utm_content=inline+mention)、CoreWeave、戴尔、[谷歌](https://cloud.google.com/?utm_content=inline+mention)、[HPE](https://www.hpe.com/us/en/ezmeral.html?utm_content=inline+mention)、Lambda、联想、Meta、微软、Mistral AI、OpenAI、[Oracle 云基础设施](https://www.oracle.com/developer?utm_content=inline+mention) (OCI) 等众多公司。

视频

[YOUTUBE.COM/THENEWSTACK

技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、采访、演示等等。

订阅](https://youtube.com/thenewstack?sub_confirmation=1)