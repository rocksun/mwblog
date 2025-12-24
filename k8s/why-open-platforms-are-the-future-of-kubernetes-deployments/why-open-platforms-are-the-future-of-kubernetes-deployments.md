<!--
title: 开放平台：Kubernetes 部署的未来图景
cover: https://cdn.thenewstack.io/media/2025/12/f53270f2-open-platforms-future-kubernetes-deployments.jpg
summary: Kubernetes部署有专有、DIY和公共云三种方式，各有限制如供应商锁定、高成本或复杂性。开放式平台提供灵活性、加速创新、避免锁定，且降低成本。
-->

Kubernetes部署有专有、DIY和公共云三种方式，各有限制如供应商锁定、高成本或复杂性。开放式平台提供灵活性、加速创新、避免锁定，且降低成本。

> 译自：[Why Open Platforms Are the Future of Kubernetes Deployments](https://thenewstack.io/why-open-platforms-are-the-future-of-kubernetes-deployments/)
> 
> 作者：Chris Brown, Aarthi Mahesh

Kubernetes是历史上[增长最快的开源项目](https://www.ibm.com/think/topics/kubernetes-history)之一。根据Grand View Research的数据，2024年它创造了[17.1亿美元](https://www.grandviewresearch.com/industry-analysis/container-orchestration-market-report)的收入，预计到2030年将超过85亿美元。最近[云原生计算基金会 (CNCF)](https://cncf.io/?utm_content=inline+mention)的一项调查发现，[93%的组织](https://www.cncf.io/wp-content/uploads/2025/04/cncf_annual_survey24_031225a.pdf)要么在生产环境中运行Kubernetes，要么正在测试环境中进行试点。

通常，组织部署[Kubernetes](https://thenewstack.io/kubernetes/)主要有三种方式：专有解决方案、自行搭建（DIY）和公共云。但每种方式都有局限性，可能阻碍创新、减缓发展势头并增加成本。开放、完整的Kubernetes平台提供了一种替代方案，可以帮助克服这些挑战。

## 专有Kubernetes平台的挑战

专有企业级Kubernetes解决方案试图将[您可能需要的一切](https://thenewstack.io/kubernetes-isnt-enough-for-a-production-ready-platform)打包在一个产品中。供应商通过修改或添加额外层，为开源Kubernetes加入了其“秘方”。尽管它们易于上手，但这些专有解决方案可能会极大地限制兼容性。这些平台不容易定制，因为您被锁定在由单一供应商控制的黑盒中。

专有供应商可能在集成开源Kubernetes的最新更新方面进展缓慢。供应商很难（如果不是不可能）跟上每年发布的在存储、服务网格、容器注册表、持续交付、智能运维、人工智能（AI）、机器学习（ML）、自动化、数据服务、成本管理、策略、网络、可观测性和安全等技术领域的大量云原生和开源项目更新。

您无法总是预测供应商优先集成（无论是直接集成还是通过合作）的创新是否是您最想要的。而且您几乎从不知道集成可能需要多长时间。您必须按照供应商的步伐前进，因此可能需要等待一段时间才能使用有用的新工具。

## 自行搭建（DIY）Kubernetes部署的陷阱

在自行搭建的DIY Kubernetes方法中，您的团队逐个组件地编译和编码一切，测试和验证所有内容，并亲自管理更新、安全、网络和新工具集成。一个完整、企业级的平台通常需要集成和管理25个以上的不同项目。这种持续的更新、修补漏洞和测试集成的循环需要付出巨大的努力。

已经具备Kubernetes内部专业知识的组织可能更喜欢这种方法，但它可能极其耗时，并且需要大量的[技术技能和资源](https://thenewstack.io/kubernetes-complexity-realigns-platform-engineering-strategy)。对于任何不具备所需技能、经验和资源的组织来说，DIY方法是不可能实现的。

## 理解公共云Kubernetes的成本

公共云Kubernetes服务通常非常好用且简单明了。但这种便利伴随着一个权衡：由于每月账单迅速攀升而产生的成本。

例如，为了降低不断上涨的云成本，一家运行200个集群的公司决定在夜间关闭某些集群。然而，云服务内置的自动扩缩容功能被激活并再次将它们全部打开。这些变化生成了大量的配置日志条目和更改，导致账单暴增。

在与超大规模云提供商合作时，供应商锁定也可能成为一个问题。例如，当[AWS](https://aws.amazon.com/?utm_content=inline+mention)推荐CloudWatch用于集群中的日志记录和指标监控时，遭到了偏爱[Fluent Bit](https://thenewstack.io/fluent-bit-core-concepts/)等开源工具的开发人员的抵制。最终，亚马逊让步，允许用户选择他们想要的开源工具。

## 开放式Kubernetes平台如何克服部署挑战

一个完整、开放的Kubernetes平台是一种部署模型，它能够在加速创新的同时提供灵活性和一致性。它组装并测试了一个模块化、可定制的架构，该架构在所有IT环境中（无论是在本地、云端还是边缘）都以相同的方式运行。

这种平台使组织能够更自由地创新：

*   它已为生产做好准备，并提供实际部署所需的一切。您无需拼凑安全、可观测性、网络和生命周期管理等关键功能。
*   它由最佳的开源软件组件构建，使用未经修改的上游版本Kubernetes和CNCF生态系统项目。所有组件均未被供应商修改，也未在Kubernetes系统之上包含专有层。
*   开放平台是模块化和可修改的，而不是运行在专有供应商的黑盒内。
*   通过公开开放API，而不是将其隐藏在专有API背后，开放平台使应用程序能够在任何Kubernetes环境中保持可移植性。它避免了供应商锁定，并允许您将应用程序和其他工作负载放置在它们运行最佳的位置。
*   由于开放的Kubernetes平台与上游开源项目保持一致，您可以比等待专有供应商追赶更快地从社区获取尖端技术。
*   开源的统一平台使团队能够利用他们之前的Kubernetes经验。这可以通过减少对专业技能的需求和简化流程来最大程度地降低管理成本。
*   无论您是在本地、云端、跨多个云还是在边缘部署，开放平台都可以在一个单一的统一平台上运行。这消除了在不同部署环境中使用不同Kubernetes解决方案时可能出现的技术和操作孤岛。
*   能够在不同环境中运行应用程序是最初使用容器的关键价值主张之一。然而，封闭平台可能使得在组织生态系统不同部分以相同方式运行应用程序变得不可能。开放的Kubernetes平台保留了应用程序在公共云和私有云、本地服务器和边缘环境之间的可移植性。

综合来看，这些优势转化为更快的开发和上市时间、简化的产品和服务生态系统增长、更低的成本，以及开发开源项目商业版本的更简便方式。

## 开放式Kubernetes平台的关键优势

Kubernetes的未来在于完整且开放的平台。它们提供生产级的解决方案，这些解决方案是完全组装好并可部署的，具有开放性、模块化和[灵活性](https://thenewstack.io/how-ai-is-pushing-kubernetes-storage-beyond-its-limits)，以推动创新并避免供应商锁定。

选择一个完整且开放的Kubernetes平台不仅仅是采用正确的技术。它是关于为运营效率、加速创新、供应商独立性和长期竞争优势奠定基础。

例如，[Nutanix Kubernetes Platform (NKP)](https://www.nutanix.com/products/kubernetes-management-platform) 解决方案基于纯粹、上游的开源组件。Nutanix 提供了一个企业级的Kubernetes平台，具有集中控制、内置弹性以及完整的第二天运维能力，可以管理跨云、数据中心和边缘的集群群，而无需复杂性或供应商锁定。它仅使用开源API，并且如果需要，几乎所有组件都可以替换为替代的开源或商业解决方案。

通过[试用](https://cloud.nutanixtestdrive.com/login)了解更多NKP信息。