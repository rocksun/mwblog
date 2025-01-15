# Mirantis Rockoon：Kubernetes上的OpenStack管理

![Featued image for: Mirantis Rockoon: OpenStack Management on Kubernetes](https://cdn.thenewstack.io/media/2025/01/18b25618-ardian-pranomo-x2vxvweo7w-unsplash-1024x765.jpg)

[Mirantis](https://www.mirantis.com/) 发布了 [Rockoon](https://github.com/Mirantis/rockoon)，这是一个创新的开源项目，它提供了一个 [Kubernetes](https://thenewstack.io/Kubernetes/) 控制器，用于 [OpenStack](https://www.openstack.org/) 云的生命周期管理。虽然以开源形式出现尚属新事物，但Mirantis多年来一直在为其客户[使用](https://thenewstack.io/mirantis-unveils-next-generation-kubernetes-platform-with-mke-4-release/)和部署该程序。

信不信由你，Rockoon 确实是“火箭+气球”的真实单词。然而，Mirantis Rockoon并非将火箭发射到太空，而是提供一个Kubernetes控制器，用于简化OpenStack管理。它通过使用[OpenStack Helm](https://wiki.openstack.org/wiki/Openstack-helm)图表提供高级抽象层。此外，它还提供了对OpenStack Helm应用程序编程接口（API）的稳定、版本化的抽象。

该程序还提供了一个[统一的API](https://thenewstack.io/its-time-to-start-preparing-apis-for-the-ai-agent-era/)，用于管理OpenStack集群配置和生命周期操作，同时支持自愈过程并促进更智能的升级。使用Rocktoon，您可以简化复杂的运营例程，允许管理员将OpenStack作为一个统一的整体来管理，而不是一系列不同的服务。

它们共同提供了一个统一的API，用于管理OpenStack集群配置和生命周期操作，抽象复杂的网络任务，支持自愈过程，并促进更智能的升级和编排。

Rockoon拥有大量的受众。[OpenInfra Foundation](https://openinfra.dev/)总经理[Thierry Carrez](https://www.linkedin.com/in/thierry-carrez-652662a/?originalSubdomain=fr)在电子邮件采访中解释说：“超过三分之二的OpenStack部署利用了OpenStack和Kubernetes的集成。全球数千万个核心正在实施该开放基础设施蓝图。Mirantis将Rockoon开放给社区，这与该公司长期以来对这两个项目的承诺相符。在开源许可下发布Rockoon是合理的。”

## OpenStack中缺失的要素

你为什么要这么做？Mirantis开源战略和技术副总裁[Randy Bias](https://www.linkedin.com/in/randybias/)解释说：“我们很高兴提供OpenStack生态系统中一个关键的缺失组件：由Rockoon支持的，在Kubernetes上运行的OpenStack的高级生命周期管理。Rockoon已经在一些最大的Mirantis客户那里经过实战检验，这些客户在生产环境中大规模运行它已有五年或更长时间。Mirantis通过发布这个解决OpenStack最大挑战之一的关键代码片段，巩固了其作为OpenStack生态系统创新者的角色。它是永久免费的，并且今天即可使用。”

在另一封电子邮件采访中，Mirantis员工产品经理[Artem Andreev](https://www.linkedin.com/in/arandreev/?originalSubdomain=de)补充说，Rockoon是我们对开源社区承诺的重要一步。继我们去年在巴黎KubeCon上承诺加倍关注开源之后，Rockoon将[Mirantis OpenStack for Kubernetes (MOSK)](https://www.mirantis.com/software/mirantis-openstack-for-kubernetes/)的优势带给了所有人。”

Andreev补充说：“鉴于[最近的市场变化](https://thenewstack.io/vmware-users-adjust-to-broadcom-subscription-licensing/)，人们对VMware的开源替代方案，特别是OpenStack，产生了新的兴趣。Mirantis认识到对易于访问和高效的OpenStack环境管理工具的需求日益增长，我们相信MOSK和Rockoon能够满足这一需求。”

也就是说，虽然Rockoon针对Mirantis的[K0s](https://k0sproject.io/)发行版进行了优化，但它与其他Kubernetes环境兼容。Mirantis通过对存储库的每次提交进行自动化测试来确保稳定性。

听起来很有趣？Mirantis让开发人员和企业可以轻松开始使用Rockoon。只需访问[Rockoon GitHub存储库](https://github.com/Mirantis/rockoon)。然后，使用提供的部署脚本在轻量级的笔记本电脑或虚拟机（VM）上进行自动化设置，以便您可以查看它是否适合您。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)