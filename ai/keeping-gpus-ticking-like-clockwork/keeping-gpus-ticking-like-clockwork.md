<!--
title: 让GPU滴答作响
cover: https://cdn.thenewstack.io/media/2025/11/759d90c0-thumbnail-21.png
summary: Clockwork公司开发了一款软件层，专注于优化AI工作负载中GPU间的通信，提供深度可见性和容错能力（如FleetIQ），以提高AI训练效率和正常运行时间。该公司最初源于时钟同步研究，后扩展到网络遥测和动态流量控制。
-->

Clockwork公司开发了一款软件层，专注于优化AI工作负载中GPU间的通信，提供深度可见性和容错能力（如FleetIQ），以提高AI训练效率和正常运行时间。该公司最初源于时钟同步研究，后扩展到网络遥测和动态流量控制。

> 译自：[Keeping GPUs Ticking Like Clockwork](https://thenewstack.io/keeping-gpus-ticking-like-clockwork/)
> 
> 作者：Frederic Lardinois

“今天，Clockwork 构建了一个软件层，专注于优化大型集群中 GPU 之间的通信，这些集群用于 AI 工作负载，”Vasudevan 告诉我。“正如您所熟知的，AI 工作负载是有史以来分布最广、要求最高的分散式应用程序。工作负载的性能在很大程度上取决于 GPU 之间通信的有效性。Clockwork 专注于一系列软件构建模块，让您能够获得最终提高 AI 效率的三个关键功能。”

这些功能包括对 GPU 群组中发生的情况进行深度可见性，从网络层到应用程序层。但其客户最可能看中的是 FleetIQ，它能够通过自动将流量重路由到损坏的网络交换机来提供容错能力。

这对于大型 LLM 训练工作负载尤其重要，因为一旦出现问题，它们就很难重新启动。典型的 GPU 集群正常运行时间在 80% 到 90% 之间。

“与通常以三到四九（three to four nines）来衡量的云可用性相比，这是一个完全不同的世界。更糟糕的是，当链接消失时，您必须停止工作负载，回退到可能已经过去数小时的检查点，然后重新开始训练。因此，数百到数千个 GPU 都在浪费他们已经完成的所有计算，”Vasudevan 解释道。

## 从时钟到 GPU

这与 Clockwork 的创始人在创办公司时最初的想法完全不同。

该公司于 2018 年在斯坦福大学孵化（当时名为 TickTock，后来因显而易见的原因更名），由 [Balaji Prabhakar](https://www.linkedin.com/in/balaji-prabhakar-45426bb7/)、[Deepak Merugu](https://www.linkedin.com/in/deepak-merugu-334b3775/) 和 [Yilong Geng](https://www.linkedin.com/in/yilong-geng-7b15a16a/) 创立，基于 Prabhakar 和 Geng 在时钟同步方面进行的研究。Vasudevan 于今年早些时候加入该公司，担任首席执行官，此前他曾担任 Sysdig、Nimble Storage 和 Omneon 的首席执行官。

“公司最初的四年，是一个小团队，几乎是斯坦福大学的延伸，大约有五六个人，”Vasudevan 解释道。“我们追求的核心技术和用例都与时钟同步有关。例如，我们的一些财富 100 强金融公司使用我们来同步时钟，以便对金融记录和市场数据进行时间戳。”

从那时起，团队领悟到，他们可以利用其测量数据包从 A 到 B 所需时间的能力，作为网络遥测系统的基础。

“在此过程中，我们能够用另一项我们称之为动态流量控制的构建模块技术来补充我们的全局时钟同步。因为我们现在确切地知道 GPU 之间网络中发生的情况，所以我们也可以通过在软件层面进行拦截来重定向流量，”他解释道。“我们接入 Nvidia 称为 [NCCL](https://developer.nvidia.com/nccl) 的通信库，接入 TCP 通信库，接入 [RDMA 通信库](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_infiniband_and_rdma_networks/understanding-infiniband-and-rdma_configuring-infiniband-and-rdma-networks)。当我们看到拥塞或流量争用时，我们能够进行重定向。其演变是：有了时钟，我可以测量事物。一旦我测量了事物，我就可以控制它们。然后，我如何将控制权不仅限于网络层，而是延伸到 PyTorch 训练工作负载，并为容错和性能管理整个应用程序？”

有关 Clockwork 如何做到这一点的更多详情，以及 Vasudevan 对我们是否处于 AI 泡沫的看法——以及这是否重要——请查看 YouTube 上的完整视频或订阅我们的播客。