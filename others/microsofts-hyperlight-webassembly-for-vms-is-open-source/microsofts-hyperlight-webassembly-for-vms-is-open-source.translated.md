# 微软的 Hyperlight WebAssembly 虚拟机开源了

![Featued image for: Microsoft’s Hyperlight WebAssembly for VMs Is Open Source](https://cdn.thenewstack.io/media/2025/01/338a7e4a-brucemoss1-1024x576.jpg)

微软 Azure Core Upstream 团队表示，其[Hyperlight](https://opensource.microsoft.com/blog/2024/11/07/introducing-hyperlight-virtual-machine-based-security-for-functions-at-scale/) 为[无服务器](https://thenewstack.io/serverless/) 应用提供了 100% 以上的冷启动延迟降低，同时受益于[WebAssembly](https://thenewstack.io/webassembly/) (Wasm) 的沙箱安全。Hyperlight 项目现已开源，并计划捐赠给[CNCF](https://cncf.io/?utm_content=inline+mention)，该项目依赖于小型嵌入式函数，并为大规模的每个函数调用使用基于虚拟机的保护。每个函数请求也有其自己的[虚拟机](https://thenewstack.io/4-reasons-devops-engineers-still-rely-on-hypervisors/) 用于保护。

[虚拟机](https://thenewstack.io/deploy-a-virtual-machine-with-oracles-open-source-virtualbox/) 长期以来一直是云原生基础设施的基石，被广泛信任为安全地隔离主机和客户机环境，微软 Azure 的首席工程师在 11 月的 KubeCon+CloudNativeCon 大会主题演讲中表示。“然而，对于无服务器计算等事件驱动的场景，传统的虚拟机启动速度太慢，”  说。“那么，我们如何在保持应用程序安全的同时降低这种延迟呢？”

## 什么是 Hyperlight？

Hyperlight 是一个[Rust](https://thenewstack.io/rust-programming-language-guide/) 库，它允许开发人员利用基于内核的虚拟机或 Hyper-V（微软原生的虚拟机管理程序）在[微型虚拟机](https://www.techtarget.com/searchsecurity/definition/micro-VM-micro-virtual-machine) 中运行不受信任的代码，而无需加载完整的操作系统。她说，这些微型虚拟机可以在微秒内创建。

在一个演示中，展示了应用程序如何从虚拟机到主机进行顺序调用，然后将值从主机返回到客户机。Hyperlight 为每次调用创建一个新的微型虚拟机，平均每次请求仅需 900 微秒。“那是微秒——不到一毫秒，” 说。

## 重大构想

这个想法已经存在一段时间了：使用 Wasm 模块作为轻量级和沙箱安全。根据云供应商的不同，微型虚拟机将允许内部部署或云端资源通过云端分发来自内部部署系统的大量数据流量。[谷歌](https://cloud.google.com/?utm_content=inline+mention) 云应该在 2025 年标准制定完成后提供类似的产品。

微软 Azure 的 CTO 和技术研究员在微软 Ignite 用户大会上说：“我们现在可以使用这些轻量级沙箱来处理进入系统的网络流量。”“这为实时、高效的网络处理带来了令人难以置信的可能性。”

Adobe 和 Google 是开发 WebAssembly 标准的科技领导者之一。此外，使用它来流式传输视频的公司包括 Netflix、亚马逊 Prime、迪士尼等。

微软通常对其之前在 WebAssembly 方面的大部分工作都语焉不详（当被询问时，微软无法就之前的文章发表评论），但已证实该公司已经开始使用 WebAssembly 来支持其运营，同时继续积极为社区贡献 Wasm 的开发。就微软而言，其 WebAssembly 工作可以追溯到几年前。例如，多年来，微软模拟飞行已经使用 WebAssembly 进行模组保护，因为它被证明可以提高作为 WebAssembly 模组分发的附加组件的安全性和可移植性。Excel Online 使用 WebAssembly 计算 Lambda 函数。
微软目前的大部分工作都集中在投资即将推出的组件模型和WASI上。例如，微软正在扩展Azure Kubernetes Service WASI NodePool预览版，并通过Hyperlight项目在其服务的每个请求上添加额外的虚拟机监控程序保护，以增强Wasm沙箱的安全性。在边缘浏览器之外，微软主要投资于基于服务器的Wasm和围绕Bytecode Alliance的Wasm组件生态系统，以及支持高效使用和WASI的基础设施和语言工具。微软还在开发Containerd项目Runwasi，它是SpinKube项目的一部分。

“Hyperlight是我们真正隔离细粒度、轻量级代码片段所需要的缺失部分。你可能会想，‘容器不就是为此而设计的吗？’但容器实际上占用了相当大的空间，”微软高级开发者布道师和微软Azure核心上游首席产品经理在博客文章中写道。“对于诸如存储服务中的用户定义函数或边缘网络流量处理（当它进入您的系统时）之类的场景，您需要更轻量级的东西。它还需要具有敌对性和多租户安全性，这意味着客户可以并排部署在这些环境中而不会影响安全性。这促使我们创建了我们所谓的微型沙箱或微型虚拟机。”

当Azure的一位同事“有一天找到我说，‘嘿，我可以使用Hyper-V API创建一个除了我加载到其中的很小一部分代码之外没有任何代码的虚拟机。它可以在几微秒内启动，并同样快速地关闭’时，一个‘啊哈’时刻出现了，”Squillace写道。“就这样，我们有了Hyperlight，一个基于虚拟机监控程序隔离的微型虚拟机。”

微软推出了基于Hyperlight虚拟机的安全功能，并如上所述将其开源。它现在不仅适用于Hyper-V，也适用于KVM。此外，微软正在将Hyperlight贡献给CNCF，“旨在共同进步，为所有人提供微型虚拟机技术，”Wuyts和Squillace写道。“Hyperlight是我们通过安全沙箱交付此功能的方式。”

[YOUTUBE.COM/THENEWSTACK](YOUTUBE.COM/THENEWSTACK)
技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。