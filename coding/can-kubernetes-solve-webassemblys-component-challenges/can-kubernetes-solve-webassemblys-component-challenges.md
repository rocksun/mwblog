<!--
# Kubernetes可以解决WebAssembly的组件挑战？
https://cdn.thenewstack.io/media/2023/11/25b9af59-kubernetes-webassembly-1-1024x576.jpg
-->

尽管有关[WebAssembly(Wasm)](https://thenewstack.io/webassembly/)有朝一日可能取代容器甚至Kubernetes的讨论，但是WebAssembly和Kubernetes的组合正在出现。

译自 [Can Kubernetes Solve WebAssembly’s Component Challenges?](https://thenewstack.io/can-kubernetes-solve-webassemblys-component-challenges/) 。

[WebAssembly (Wasm)](https://thenewstack.io/webassembly/)的承诺尚未实现。Wasm应该能够使用你选择的语言一次性部署应用程序代码，跨越多个环境和设备类型，使用能够运行CPU指令集的宿主。

虽然已经证明Wasm在浏览器和某些针对性的服务器部署中可以非常好地工作，但是[标准化的组件模型](https://thenewstack.io/can-webassembly-get-its-act-together-for-a-component-model/)还没有实现，这个模型允许开发人员“一次部署，处处可用” - 尽管这个里程碑可能在明年就能实现。

当开发人员能够将代码加载到Wasm模块中，并同时在各种环境和设备类型上部署时，这将实现。这些环境和设备类型能够运行CPU指令集。

更具体地说，开源社区也[正在努力开发Wasi](https://thenewstack.io/mozilla-extends-webassembly-beyond-the-browser-with-wasi/)，在很多方面它是连接Wasm模块和组件的标准接口或API。但同样，我们还[没有做到这一点](https://thenewstack.io/whats-holding-up-webassemblys-adoption/)。

然后就是[Kubernetes](https://thenewstack.io/kubernetes/)。

[容器](https://thenewstack.io/containers/)和Kubernetes环境在很大程度上已准备好用于Wasm模块部署，而Wasm模块也在很大程度上已准备好在Kubernetes上部署。尽管最初有怀疑论，甚至讨论[Wasm有朝一日可能取代容器或者甚至是Kubernetes](https://thenewstack.io/webassembly/yes-webassembly-can-replace-kubernetes/)，但是一个非常好的Wasm和Kubernetes搭配正在出现。

## 使用Wasm和Kubernetes的优势

将Wasm与Kubernetes一起使用具有一些内置优势。例如: [安全性](https://thenewstack.io/security/)。因为Wasm二进制文件冷启动时间以毫秒为单位，而某些虚拟机可能需要几分钟，所以[Wasm的安全模型](https://thenewstack.io/how-webassembly-offers-secure-development-through-sandboxing/)实际上比容器和Kubernetes的安全模型更强。这是因为没有立即访问Linux内核。

所有的代码都是通过Wasm主机运行时中介的，这意味着你可以拦截所有的系统调用 - 至少在理论上是这样。换句话说，Wasm可以在容器和Kubernetes集群内提供额外的安全层。

你还不能轻松点击按钮在Kubernetes上部署Wasm模块。但是一些供应商，比如[Fermyon](https://www.fermyon.com/?utm_content=inline-mention)，已经提供了一个[无服务器](https://thenewstack.io/serverless/)服务，可以在容器和Kubernetes上部署Wasm。

这主要是由于[containerd](https://containerd.io/)对Wasm的支持以及Docker在[2022年引入的Wasm测试支持](https://thenewstack.io/webassembly/docker-needs-to-get-up-to-speed-for-webassembly/)。自那时以来，它一直是促进Kubernetes支持高度分布式部署的主要促成因素，并允许用户随意提升和降低由Wasm模块组成的应用程序。

使用containerd也发挥着重要作用；[容器shim](https://github.com/deislabs/containerd-wasm-shims)是帮助将容器与运行时代码集成的进程。

Fermyon联合创始人兼CEO [Matt Butcher](https://www.linkedin.com/in/mattbutcher/)在一次在线对话中告诉The New Stack: "[微软](https://news.microsoft.com/?utm_content=inline-mention)和许多其他人对containerd项目添加Wasm shim(如[Spin shim](https://github.com/fermyon/spin))的工作，这解锁了Docker Desktop和许多Kubernetes发行版上的Wasm。"

Butcher说，Docker Desktop和Microsoft Azure AKS都率先体现了这是如何完成的。最近，他指出，Civo在其Kubernetes产品中引入了支持，"这说明大型和小型云提供商都在促进朝着WebAssembly的转变。"

## Wasm 和 OpenShift

其他软件制造商和服务提供商也跃跃欲试地跳上Kubernetes列车以支持Wasm。他们包括[Red Hat](https://www.openshift.com/try?utm_content=inline-mention)，它已经适应OpenShift以容纳Wasm模块并支持Fermyon的Spin。Red Hat将Wasm视为跨平台开发的有趣方法，并为相关的上游社区做出贡献。

目前，Kubernetes提供了运行基于Wasm工作负载所需的编排和基础架构，这为现有的Kubernetes投资提供了额外的灵活性，Red Hat首席软件工程师[Ivan Font](https://www.linkedin.com/in/ivanmfont/)告诉The New Stack。

目前，Red Hat的平台中没有将Wasm产品化。但该公司表示，它将继续与其他供应商和社区合作，根据用户组织的需求开发其潜力。

Red Hat正在开发Spin以便在OpenShift上运行，同时也在为Wasi(Wasm和组件接口)以及[WasmEdge](https://wasmedge.org/docs/category/what-is-wasmedge)的开发做出贡献，后者是一个为云原生(当然是Kubernetes)、边缘和去中心化应用程序创建的可扩展Wasm运行时。根据WasmEdge文档，WasmEdge也支持无服务器应用程序、嵌入式函数、微服务、智能合约和物联网设备。

目前，Red Hat的OpenShift默认偏向WasmEdge，因为[Fedora](https://fedoraproject.org/) Linux发行版上已经支持它的Red Hat软件包管理器(RPM)，而且Red Hat对Wasm提供了额外的支持。

“但是，你可以使用任一种，因为两个WebAssembly运行时都朝着相似的方向发展，”Font说。“它们都侧重于[边缘](https://thenewstack.io/edge-computing/)计算，并且都具有AI功能等。”

为了在OpenShift上以基于Wasm的工作负载执行特定的工作负载，你目前需要指定一个注解来指明你要做什么。这个执行是在一个容器内完成的，但它具有独特的特征。

当Wasm应用程序被打包时，它只是一个镜像中的模块。这意味着[Open Container Initiative (OCI) ](https://opencontainers.org/)容器镜像不包含任何外部依赖项或完整的操作系统文件系统。因此，镜像大小非常小，因为它们只包含你的Wasm模块。这适用于一般的容器，而OCI在这方面是一个标准，Font说。

Butcher说，Fermyon一直与KWasm的创建者Liquid Reply以及Red Hat合作，以在OpenShift的Wasm能力与基于containerd的Kubernetes发行版之间达到某种程度的平衡。他说，这种合作“从企业级的AKS扩展到微小的K3s”。

## 更多Wasm和Kubernetes工具即将推出

Civo首席技术官兼[云原生计算基金会](https://cncf.io/?utm_content=inline-mention)大使[Saiyam Pathak](https://www.linkedin.com/in/saiyampathak/)告诉The New Stack，开发人员将有更多工具可用于在Kubernetes集群上构建和部署应用程序。

“如果你有一个Kubernetes集群，你可以简单地添加一个载荷使其成为WebAssembly就绪，”Pathak说。

Pathak说，这个过程很简单: 它涉及确保所有内容都配置正确，包括重启containerd、编辑containerd .normal文件，并在该特定节点上使用Wasm运行时。然后它就可以运行你的Wasm工作负载了。

“这非常棒，因为你现在可以使用过去10年来一直在使用的相同工具和部署流程来利用最新的WebAssembly技术为你的下一套应用程序服务，”Pathak说。“无论你是构建API还是扩展应用程序，你都可以在相同的基础设施和Kubernetes集群中使用WebAssembly，与Docker一起工作。”

提供Kubernetes数据管理平台和灾难恢复支持的[Kasten](https://www.kasten.io/?utm_content=inline-mention)，也在关注Wasm对其[Kasten K10](https://www.kasten.io/product/)平台技术能力的效用，以及对其客户的支持。Wasm不是数据移动支持的全面解决方案，但Kasten正在研究Kubernetes上的Wasm，因为Kasten正在探索如何在K10内使用Wasm。

Veeam旗下Kasten的全球首席技术官Michael Cade告诉The New Stack: "作为一个面向Kubernetes的应用程序，我们正在探索如何利用WebAssembly来简化、加快速度、提高效率和安全性: 这些都是你从Wasm本身获得的所有好处。但是WebAssembly是万能的吗？当然不是。"

相比之下，虚拟机也不是万能的，Cade说。“如果我在我最重要的应用服务器上的一台物理机器上有一个物理硬件卡，我可能会或可能不会将其虚拟化。如果不虚拟化，我就永远无法将其容器化。”

WebAssembly在哪里繁荣，尤其是对于Kubernetes，是围绕三个S: 速度、安全性和大多数Web前端服务器或Web模块已经支持它。”

## RunWasi: 进步的催化剂

开源[RunWasi项目](https://github.com/containerd/runwasi)取得的进展可能是Wasm在Kubernetes上的部署的催化剂。RunWasi通过containerd创建支持Wasm运行时的Wasm模块。

使用containerd shim完成运行时的部署过程，RunWasi提供必要的代码。这些shim通过containerd编排Wasm模块到部署代码的低级运行时。

以下列表显示了受Microsoft Deis Labs欢迎的[Wasm containerd shim](https://github.com/deislabs/containerd-wasm-shims):

- **Lunatic**，一个灵感来自Erlang的用于快速、可靠和可扩展的服务器端Wasm应用程序的运行时。
- **Spin**，一个用于构建和运行无服务器Wasm应用程序的开发者工具。
- **Slight**，一个基于Wasmtime的运行时，用于运行使用SpiderLightning (WASI-Cloud-Core)功能的Wasm应用程序。  
- **Wasm Workers Server**，一个在Wasm之上开发和运行无服务器应用程序的工具。

在10月初的[Docker年度用户大会](https://www.dockercon.com/2023/v/s-1736607?i=mdKfWEobFlr5iwT0yz33heANX6UBatF2)上，作家兼软件培训师[Nigel Poulton](https://www.linkedin.com/in/nigelpoulton/)展示并描述了他如何使用Spin作为Wasm框架在Wasm模块内为应用程序创建Wasm工件，然后将其打包成Docker容器。他还描述了他如何搭建一个具有控制平面节点和两个工作节点的多节点Kubernetes集群。

关键的是，Poulton描述了他“运行这些Wasm工作负载所需的软件，这些都是直接的containerd东西”。

