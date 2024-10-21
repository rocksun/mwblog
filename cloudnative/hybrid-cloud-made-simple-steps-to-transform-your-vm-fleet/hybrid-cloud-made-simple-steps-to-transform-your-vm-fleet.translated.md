# 简化混合云：VM 集群转型步骤

![Featued image for: Hybrid Cloud Made Simple: Steps To Transform Your VM Fleet](https://cdn.thenewstack.io/media/2024/10/d95b5c8c-luis-andres-villalon-vega-f5xe0otfd7o-unsplash-1024x683.jpg)

[Luis Andrés Villalón Vega](https://unsplash.com/@avillalonv?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/a-man-climbing-up-the-side-of-a-mountain-f5xE0oTfD7o?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).

大多数人即使有兴趣，也缺乏攀登裸露岩壁的才能或技能。

同样，将传统企业计算基础设施和应用程序现代化以管理复杂性、释放开发人员速度和加速业务创新，似乎也是一项艰巨的任务。预算和资源总是有限的，成功需要学习新技能。

如果您是 VMware 客户，鉴于 Broadcom 最近收购 VMware 带来的动态，这种转型将呈现出更陡峭的坡度。随着 Broadcom 实施产品组合重组、产品创新投资更新和价格变化，IT 高管和架构师应该立即开始向现代 [混合云平台](https://thenewstack.io/vmware-cloud-a-single-platform-for-hybrid-cloud-environments/) 迈进，并规划一条去风险化的路径，为现代化应用程序奠定基础。

## 为什么现在要转型 VM 集群？

任何经营超过十年的企业都会拥有各种传统服务器、VM、网络硬件和容器工作负载，这些工作负载运行着他们无法允许出现故障的关键应用程序。

与此同时，公司必须满足我们应用程序基础设施的现代期望，例如敏捷性、可移植性、高性能和数据主权，否则将面临落后的风险。IT 高管必须通过云原生和混合云架构交付新的 [应用程序功能](https://thenewstack.io/kubernetes-applications-for-multicloud-hybrid-cloud-environs/)，并以满足当今竞争激烈的市场中客户需求的速度和可扩展性，而不会超出有限的预算。

为了迈向混合云的未来，企业将需要：

- 数据互操作性和工作负载可移植性。由于没有哪个企业是孤岛，现代应用程序必须支持来自各种来源的数据：边缘的传感器、分布式云服务、流式 Kafka 主题和云数据仓库。这些数据结合起来可以实现高级的、计算密集型工作负载，例如机器学习、AI 推理和分析。
- 运营效率。IT 预算正在收紧，而企业对更快应用程序交付和弹性的业务期望比以往任何时候都高，这促使企业转向弹性云基础设施。与此同时，许多公司正在将 [公共云工作负载回迁到私有](https://thenewstack.io/private-vs-public-cloud-how-kubernetes-shifts-the-balance/)云和内部数据中心，以保证服务级别和数据主权，同时避免意外的云使用成本。
- 底层平台的现代化。当然，现有的 VM 必须运行在某些东西上，它们通常位于传统的三层架构之上，其中计算、存储和网络都是不同的硬件层。或者，它们可能运行在较新的 VPC 或容器上，这些容器具有一些软件定义的元素，但仍然需要进一步的平台现代化才能为混合云做好准备，无论新的资源将运行在裸机上还是在 Kubernetes 集群中。
- 风险分散。每个主要的企业软件供应商都必须在其发展过程中不断对其产品套件进行合理化。在某个时候，开发和支持人员必须放弃一个平台，以便公司能够在下一代技术中保持相关性。最终用户还应与合作伙伴合作，将 [部署从内部系统分散到多个云提供商](https://thenewstack.io/cdn-providers-rival-hyperscale-clouds-for-web-developers-deploying-jamstack/)，同时防范软件许可变更和支持结束期限，这些期限可能会影响他们的未来。

## 我可以采取哪些步骤？

优先考虑变更。对您现有的应用程序 IT 基础设施进行盘点，并评估您希望对每个应用程序执行的“6 个 R”——保留、退休、重新托管、替换、重构或重新架构——同时关注虚拟化许可和当前续订风险。

您虚拟化技术堆栈中的一些软件，包括 vSphere、vSAN 和 NSX，可能在一年内到期，而其他软件则可以推迟几年。此外，一些现有的 VMware 元素将来可能只能作为更完整的 Broadcom 解决方案包的一部分提供，而不是按需许可。
能够大幅减少其传统许可证库存的公司甚至可以负担得起维护特定难以切换的传统系统的成本，也许可以通过将其中一些系统“整体迁移”到云基础设施，尽管这听起来很荒谬。

依靠合作伙伴的专业知识。MSP 和系统集成商需要积极主动地帮助客户对其客户的 VM 集群进行现代化改造，因为存在重大弊端。

技术买家应该询问其当前或潜在的合作伙伴是否已为其他公司实施类似的 VM 迁移或 [云原生启用项目](https://thenewstack.io/cloud-native/how-do-we-cultivate-community-within-cloud-native-projects/)。如果是这样，他们更有可能在替补席上拥有具有相关云专业知识的资深人才。

此外，博通可能会更改其经销商和合作伙伴计划，以仅支持规模更大的 SI 和企业。相比之下，据一些报道，中小型咨询合作伙伴可能会支付其当前价格的 5 倍，或者完全被排除在外。这应该促使他们帮助推动更快地解决问题！

迁移到混合云平台。任何公司都不应该需要接受单点故障。公司将出于治理、风险规避或数据主权的原因，在多个超大规模云提供商的数据中心或私有云中维护特定应用程序或数据。

使用 [Nutanix 云平台](https://www.nutanix.com/products/cloud-platform)，公司可以在 AWS、Azure 或本地重新平衡 VM 和容器部署，而无需进行重构。这种多元化方法提供了许多其他优势，包括更低的延迟、更少的潜在停机时间以及更好的价格/性能比。

更改虚拟机管理程序或保留它们。Nutanix 提供了一个过渡计划，用于在所有包含虚拟机管理程序 (AHV) 的混合多云环境中对所有工作负载进行统一操作，从而实现许可证可移植性和跨混合云架构的一致操作。因此，无需进行大规模更换操作。

## Intellyx 观点
大多数 IT 组织已经积累了太多势头，无法在一夜之间改变方向。无需惊慌和冻结。自博通首次宣布收购 VMware 以来，新的许可和打包变更已经开始实施，我们可以随时预期新的定价。

幸运的是，仍然有一些时间来优先考虑必要的变更。

无论您选择哪条路线，都将有一些工作要做。现代云平台可以简化过渡，并为将您的企业 IT 资产提升到混合云未来提供安全的立足点。

保持您的选择开放以保留现有的 VM 并重构到一个新的 [云平台，同时对您的应用程序进行现代化改造](https://thenewstack.io/journey-to-the-cloud-modernizing-applications-fast-and-at-scale-at-fidelity/)，该平台可以在本地或任何知名的云超大规模云提供商上运行，被证明是最安全、最快的迁移路线。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)