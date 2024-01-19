<!--
title: 思科收购Cilium对开发者的意义
cover: https://cdn.thenewstack.io/media/2024/01/8b6dfa18-max-harlynking-64grc3amrh8-unsplash-1024x683.jpg
-->

思科收购Isovalent，获得开源项目Cilium。Cilium利用eBPF(扩展伯克利包过滤器)技术，实现内核级网络和安全。

> 译自 [Cisco Gets Cilium: What It Means for Developers](https://thenewstack.io/cisco-gets-cilium-what-it-means-for-developers/)，作者 Torsten Volk。

2023年底，[思科](http://cisco.com/？utm_content=inline-mention)宣布其意图[收购](https://thenewstack.io/isovalent-open-sources-tetragon-ebpf-based-observability-platform/)Isovalent，这是[Cilium](https://cilium.io/)开源项目背后的公司。Cilium利用[eBPF(扩展伯克利包过滤器)](https://thenewstack.io/what-is-ebpf/)进行内核级网络和安全，是2023年云原生空间中值得注意的重要进展之一。

[Cilium利用eBPF](https://thenewstack.io/cilium-cncf-graduation-could-mean-better-observability-security-with-ebpf/)提供高级网络和安全控制。eBPF是一项Linux内核技术，允许动态插入强大的安全、可见性和网络控制逻辑。这项技术在Cilium中被用来提供高性能网络、多集群和多云能力以及高级负载均衡。Isovalent由一批享誉盛名的投资者支持，如谷歌、安德森·霍洛威茨(Andreessen Horowitz)、[微软](https://news.microsoft.com/？utm_content=inline-mention)、Grafana以及思科本身。但是思科为什么真的要进行此次收购，它对应用开发者和DevOps专业人员意味着什么呢？

## 让我们从头开始

[Dan Wendlandt](https://www.linkedin.com/in/danwendlandt)，CEO，和[Thomas Graf](https://www.linkedin.com/in/thomas-graf-73104547/？originalSubdomain=ch)(CTO)都参与了Open vSwitch和Nicira的网络虚拟化平台(NVP)的诞生，后者后来成为VMware最重要的产品之一: [软件定义网络(SDN)](https://thenewstack.io/networking/software-defined-approach-networking-security/)的NSX平台。SDN的全部意义在于将网络交换机转化为软件。这使得应用开发者能够快速迭代和部署网络配置，例如微分段，与应用开发周期同步。[DevOps](https://thenewstack.io/devops/)人员可以自动化和简化网络供应和管理流程，使其与[CI/CD](https://thenewstack.io/ci-cd/)流水线保持一致。安全专业人员可以以编程方式强制细粒度的安全策略和隔离网络流量，增强整体安全态势。这一切听起来都很棒，那么我们为什么需要Cilium和eBPF呢？

## SDN和带有eBPF的Cilium

![](https://cdn.thenewstack.io/media/2024/01/11ee8609-image.png)

*网络中SDN和eBPF的详细集成*

SDN通过可编程接口在第1、2和3层提供对网络配置和管理的控制。另一方面，利用eBPF的Cilium将这种可编程控制扩展到传输层(第4层)和应用层(第7层)。这允许通过TCP、UDP、ATP和MTCP等协议强制网络策略，这些协议为应用程序提供端到端的通信服务。

eBPF，一个起源于Linux内核的革命性技术，允许沙箱化的程序在操作系统内运行，为云原生环境中的网络和安全提供更细粒度和更灵活的控制。与传统的用户空间网络相比，这种内核级网络消耗更少的资源并且运行更快，主要是由于Linux内核和用户空间之间的通信减少，以及直接访问系统资源。作为[Kubernetes](https://thenewstack.io/kubernetes/)集群上每个节点的守护程序集部署的Cilium，强制执行用户定义的网络策略，并将这些定义转换为eBPF程序。这种方法使Cilium能够提供一个简单的平面Layer 3网络，并能够在第3、4和7层(应用程序级别)为HTTP、gRPC或[Kafka](https://thenewstack.io/decoding-kafka-why-its-worth-the-complexity/)等协议强制执行网络策略。

总之，虽然SDN在较低层提供对网络配置和管理的可编程控制，但带有eBPF的Cilium将这种控制扩展到传输层和应用层。这为网络和安全提供了更细粒度和更灵活的控制，特别适合云原生环境。

## 对应用开发者的优势

SDN与eBPF的集成，特别是通过像Cilium这样的工具，为应用开发者带来许多优势，尤其是在云原生环境中。以下是这些优势的详细分析:

**增强的可编程性和适应性**: eBPF的可编程性质使开发者能够快速适应云原生格局的变化。这种灵活性在一个以不断演进和需要快速迭代为特征的领域至关重要。

**简化的开发过程**: Cilium抽象了eBPF的复杂性，使开发者能够利用其功能而不需要深入探究编写eBPF代码的复杂性。这种抽象降低了学习曲线和开发时间，使其更易于为广泛的开发者所接受。

**改进的应用效率**: 通过在内核级实现更智能的网络和安全控制，应用程序可以更有效地利用资源。这种效率在云环境中特别重要，因为资源通常是动态分配和优化成本与性能的。

**增强的安全性**: eBPF和Cilium有助于在内核级直接实施高级安全措施。这种方法允许更细粒度和更有效的安全控制，这对安全性至关重要的云原生应用程序来说是必不可少的。

**更好的可观察性和故障排除**: Cilium和eBPF的组合增强了对Kubernetes工作负载的可见性。这种增加的可观察性有助于性能监控、故障排除，并确保开发人员更清楚地了解其应用程序在云环境中的行为方式。

**基于可观察性的策略执行**: 根据实时可观察性数据执行策略的能力使网络和安全态势更具动态性和响应性。这一方面对于确保合规性和维持强大的应用程序性能特别有益。

**解决云特有的挑战**: 传统的内核模块或增强功能通常难以处理云环境中管理网络接口相关的碎片化和开销。SDN、Cilium和eBPF的组合有效地解决了这些问题，提供了减少延迟和增强可扩展性。

**内核级操作的可扩展性**: 通过SDN和eBPF为操作系统内核带来可编程性和可扩展性，可以实现更创新和高效的内核级网络和安全任务方法。

简而言之，Cilium和eBPF与SDN的协同效应为应用开发者，特别是在云原生环境中，提供了一个令人信服的解决方案。它在简化内核级网络和安全任务中传统相关的复杂性的同时，提供了增强的安全性、效率和可编程性的平衡。这种组合在动态和资源优化的云环境中特别有益。

## 为什么内核级网络对云原生应用开发至关重要

如果一个装有eBPF策略的Linux机器尝试与另一个没有相同策略的Linux机器通信，该通信不会被自动拒绝。相反，这些策略将根据其自己配置的规则来决定启动机器如何处理出站和入站网络流量，而不考虑另一台机器上的策略。这可能包括根据网络流量中的可疑模式进行过滤、重定向或观察。可以将[Ansible](https://thenewstack.io/red-hat-ansible-gets-event-triggered-automation-ai-assist-on-playbooks/)、Puppet或[Terraform](https://thenewstack.io/terraform-vs-ansible-which-is-best-for-you/)等工具配置为在预配过程的一部分自动部署和配置eBPF工具和策略到新机器上。这种方法确保每个新机器在设置时都采用一致的预定义策略和配置，在整个基础架构中维护统一性和合规性。

## 一致的开发者API

Cilium开源项目为应用开发者提供了一组consistent API，以便细粒度地控制网络路由、负载均衡、加密、安全性和可观察性。由于eBPF代码在系统级运行，所有这些功能都可以在不对应用代码或容器配置进行任何更改的情况下添加。由于eBPF在操作系统级运行，它可以访问在特定节点上运行的任何pod，使开发者可以使用一个consistent的API来连接该节点上运行的所有Kubernetes Pod的网络。基于统一的策略集，开发者可以确保Kubernetes节点所需的一致配置，以确保特定应用程序(Pod)可以安全、可靠地以期望的性能运行。

## 用Cilium增强思科的产品组合

将Cilium/eBPF与思科的套件(包括Splunk、AppDynamics、思科ACI、Intersight和Tetration)集成，无疑不仅增强了这些平台，而且为开发者带来显著优势:

**Splunk和AppDynamics集成**: 与Cilium/eBPF的集成极大地丰富了Splunk的网络洞察力和安全分析功能。对于开发者来说，这意味着可以访问更详细和准确的内核级数据，使他们能够做出更明智的决策并开发更健壮的应用程序。对于[AppDynamics](https://thenewstack.io/appdynamics-why-todays-developers-are-in-a-good-place/)，增强的应用程序性能监控功能意味着开发者可以深入了解应用程序行为、网络效率和安全性，从而改进应用程序性能和可靠性。

**思科ACI集成**: 通过利用Cilium/eBPF，思科ACI可以提供高性能网络和先进的安全功能。对开发者来说，这意味着其应用程序的网络效率和安全性得到改善。内核级数据采集和分析功能为开发者提供了对其应用程序网络交互的增强可见性，允许进行更有效的故障排除和优化。

**Intersight集成**: Cilium/eBPF与Intersight的集成拓宽了它在Kubernetes和传统基础架构上的管理能力。这对于在混合云环境中工作的开发者特别有利，因为它简化了监控和管理任务。eBPF的可编程性使开发者能够创建更高效和通用的应用程序，以快速适应不断发展的云原生格局。  

**Tetration集成**: 有了Cilium/eBPF，[Tetration](https://www.cisco.com/c/en_my/products/security/tetration/index.html)可以针对安全提供细粒度的可观测性和策略执行。开发者可以从其应用程序改进的安全性中受益，因为他们可以更轻松地实现高级网络和安全控制。这种集成为开发者节省了时间并降低了复杂性，他们可以专注于应用程序逻辑而不是安全复杂性。

总之，在这些思科平台上整合Cilium/eBPF增强了每个工具的功能，同时为开发者提供了实质性收益。这些收益包括改进的网络洞察力、增强的应用程序性能监控、简化的混合云环境管理以及加强的应用程序安全性。这种集成很好地满足了现代IT格局中开发者的需求，在该格局中，效率、安全性和适应性至关重要。

## 最后的话

2023年成为eBPF真正起飞的一年并非巧合，因为这也是Kubernetes大规模采用之年的开始。这项技术在网络、安全性和可观察性方面具有巨大的潜力，而不仅仅是网络和安全性。企业采用分布式云原生应用架构的越多，自动确保策略驱动和因此一致的网络、安全性以及细粒度的实时监控就会变得越重要，而几乎不会带来性能开销。综上所述，虽然我不知道价格标签，但这次收购是正确的，因为Isovalent基于eBPF的功能可能会成为思科未来在云原生应用领域区分自己的重要因素。
