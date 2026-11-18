<!--
title: AI 智能体席卷 KubeCon，但生产落地仍是另一回事
cover: https://cdn.thenewstack.io/media/2026/11/81c5d979-thumbnail-24-1024x576.png
summary: CNCF执行董事表示，AI智能体在KubeCon备受热议但生产落地仍处早期。云原生社区正通过OpenShell等项目强化安全与可观测性，助力基础设施应对智能体负载。
-->

CNCF执行董事表示，AI智能体在KubeCon备受热议但生产落地仍处早期。云原生社区正通过OpenShell等项目强化安全与可观测性，助力基础设施应对智能体负载。

> 译自：[AI agents were all over KubeCon. Production is another story](https://thenewstack.io/cncf-bryce-ai-agents/)
> 
> 作者：Frederic Lardinois

AI 智能体正在考验原本为人类设计的系统，而 Jonathan Bryce 认为，云原生社区还有大量工作要做，才能帮助这些系统跟上这个新时代的步伐。

在盐湖城举办的 KubeCon + CloudNativeCon North America 大会期间，The New Stack 对云原生计算基金会（CNCF）执行董事 Bryce 进行了专访，探讨加入该基金会的最新项目以及 AI 如何改变基金会的各项工作。

视频

Bryce 告诉 *The New Stack*：“我们世界中现有的许多系统都是按照人类的响应速度构建的，而智能体的运行速度是一种完全不同的使用模式和场景，因此这些系统的可扩展性和韧性远远不足以应对智能体所产生的这类工作负载。”

在 Kubernetes 上运行训练和推理工作负载对云原生社区而言早已驾轻就熟，但 Bryce 指出，智能体交互的金融服务、医疗保健和交通运输系统同样需要云原生技术所提供的弹性和可观测性。

### OpenShell 与 Agent Substrate

在本届 KubeCon 上，Nvidia 宣布[将 OpenShell 捐赠给 CNCF](https://thenewstack.io/nvidia-donates-openshell-cncf/)。此前，Google 也已于大会开幕前[宣布捐赠 Agent Substrate](https://cloud.google.com/blog/products/containers-kubernetes/open-infrastructure-for-autonomous-agents-comes-to-cncf/)。这两个项目均以沙箱（Sandbox）项目的身份加入 CNCF，即该基金会的入门级项目层级。

从核心功能来看，OpenShell 负责执行策略控制，包括限制智能体可以访问哪些文件、网络、凭据和模型端点。Agent Substrate 则解决了一个相关但侧重点不同的问题，它为 Kubernetes 上的智能体提供隔离环境，并具备挂起空闲会话并在需要时恢复等功能。

“我们可以从基础设施层面将安全性和可控性直接融入 AI 系统的架构之中，”Bryce 表示。

鉴于 AI 在安全性和资源消耗方面引发的诸多问题，他认为这是整个社区肩负的责任。他表示，将 OpenShell 这样的项目纳入中立治理体系，也能让更多企业参与其中并做出贡献。

### 利用现有硬件实现更高效率

此外，智能体工作负载的分布也不像传统企业级应用那样均匀。

“即使你的智能体始终处于待命状态、随时听候差遣，它也未必会全天候 24 小时不间断地工作，”Bryce 说，“你该如何实现快速缩容和拉起，让用户感觉它随时待命？这将是人们所追求的用户体验。你又如何在不让它空占资源、白白浪费 CPU 周期的情况下做到这一点？”

[Agent Substrate](https://thenewstack.io/kubernetes-ai-agent-runtime/) 能够保存智能体的状态并释放其占用的计算资源，随后再将会话恢复到可用的工作节点上。

Bryce 还重点提到了分布式推理框架 [llm-d](https://thenewstack.io/llm-d-cncf-kubernetes-inference/)，将其作为通过软件充分释放现有硬件潜力的范例。尽管硬件购置成本高、运行开销大，且（至少在目前）供应有限，但软件层面却是开发者当下就可以着手优化的领域。

### 漏洞报告如潮水般涌来

本届 KubeCon 上，零日漏洞与安全问题被提及的频率也高于往年。

Bryce 表示，随着越来越多人使用 AI 工具来挖掘和提交漏洞，开源项目维护者正被大量重复且未经验证的报告淹没，但他们却依然不得不认真对待每一份报告。

他认为目前的增长速度可能不再像今年年初那样急剧加快，但随着模型能力持续提升，他也不确定 2027 年将会面临怎样的局面。

“千年虫（Y2K）最终并没有酿成多大的危机，”他说，“但这一次不同，如果我们不齐心协力、尽快采取行动，这真的可能会演变成一场大危机。”

### 智能体的普及仍处于早期阶段

尽管大会上随处可见关于智能体的讨论，但 Bryce 对其实际落地情况的评估却相当审慎。

“除了软件开发领域之外，智能体的采用率仍然相当低，”他表示。

他观察到，目前智能体在客户服务以及其他拥有明确历史知识库积累的领域已经有了生产级应用。

“距离实现数十亿智能体持续不断地代表我们执行各种操作，我们仍处于非常、非常、非常早期的阶段，”Bryce 说道。

对于向智能体授予访问权限后一旦出现差错会引发何种后果，企业依然持谨慎态度——如果你最近花时间与大型企业及其客户交流过，对此便不会感到意外。

就目前而言，Bryce 认为这是一件好事，因为这或许刚好能让社区有足够的时间来打磨和加固 OpenShell、Agent Substrate 等项目，赶在企业更大规模地将智能体投入实际工作之前做好准备。