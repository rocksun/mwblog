
<!--
title: OpenStack Flamingo：轻装上阵，性能腾飞！
cover: https://cdn.thenewstack.io/media/2025/10/865539dd-openstack-flamingo-2.jpg
summary: OpenStack发布Flamingo版本，这是第32次重大更新。它减少了技术债务，增强了并发性、安全性和硬件支持。新版本引入了更灵活的发布节奏。
-->

OpenStack发布Flamingo版本，这是第32次重大更新。它减少了技术债务，增强了并发性、安全性和硬件支持。新版本引入了更灵活的发布节奏。

> 译自：[OpenStack Flamingo Reduces Technical Debt, Boosts Performance](https://thenewstack.io/openstack-flamingo-reduces-technical-debt-boosts-performance/)
> 
> 作者：Steven J. Vaughan-Nichols

最古老的开源基础设施即服务 (IaaS) 云刚刚发布了新版本，庆祝了它的最新生日。

[Flamingo](https://releases.openstack.org/flamingo/index.html) 是 [OpenStack](https://www.openstack.org/) 的最新版本，它显著减少了技术债务并扩展了企业功能。

作为第32次重大更新，此版本在并发性、安全性、硬件支持和更灵活的发布节奏方面取得了显著改进，巩固了其在大规模部署中的作用，无论您是追求最新功能还是更慢、更稳定的版本。

Flamingo 是由来自 BBC R&D、爱立信、英伟达、Rackspace、[红帽](https://www.openshift.com/try?utm_content=inline+mention)、三星 SDS、[SAP](https://www.sap.com/index.html?utm_content=inline+mention) 和沃尔玛等组织的480名贡献者共同努力的成果，整合了近8,000项代码更改。

Flamingo 发布时，OpenStack 正在全球生产环境中为超过5500万个计算核心提供支持。这与项目最初的起点相去甚远。

## OpenStack 的起源故事

2008年，人们仍然将云计算不屑一顾地认为是“别人的电脑”。像 [甲骨文](https://www.oracle.com/developer?utm_content=inline+mention) 首席执行官 [拉里·埃里森](https://x.com/larryellison) 这样的顶尖科技高管，[更是将云计算斥为最新的时尚](https://www.cnet.com/culture/oracles-ellison-nails-cloud-computing/)。

最终所有人都明白云计算是一种根本不同的范式，但有些人已经走在了前面。其中一个群体包括 [NASA 艾姆斯研究中心](https://www.nasa.gov/ames)、[Rackspace](https://www.rackspace.com/) 和 [Anso Labs](https://ansolabs.com/) 的开发人员，他们共同构建了开源 IaaS 云——[OpenStack](https://www.openstack.org/)。

它不是第一个云。争取这项荣誉的竞争者包括 [Amazon Elastic Compute Cloud](https://cc.zdnet.com/v1/otc/00hQi47eqnEWQ6T9d4QLBUc?element=BODY&element_label=Amazon+Elastic+Compute+Cloud&module=LINK&object_type=text-link&object_uuid=55639666-1d6c-4c2f-a8ab-e45d1ac00050&position=1&template=article&track_code=__COM_CLICK_ID__&url=https%3A%2F%2Faws.amazon.com%2Fec2%2F%3Ftag%3Dzd-buy-button-20%26ascsubtag%3D__COM_CLICK_ID__%257C257d03ef-f92f-4d4a-a542-de541967a0d2%257Cdtp&view_instance_uuid=d9ee8763-ebe0-4a07-a14c-02a9b2815eb5)，它是 [Amazon Web Services (AWS)](https://aws.amazon.com/?utm_content=inline+mention) 的前身，以及 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure。尽管它们是基于 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 和其他开源程序构建的，但它们是专有平台。

2010年，艾姆斯团队希望 NASA 能够托管和管理自己的计算和数据资源，于是创建了 Nebula，一个早期的 IaaS 云。但正如当时红帽产品战略高级总监 Brian Gracely [在2020年 NASA 博客文章中](https://www.nasa.gov/technology/tech-transfer-spinoffs/in-cloud-computing-open-source-becomes-big-business/) 所说，“NASA 没有足够的人员来全面构建并长期维护它。”

因此，艾姆斯团队选择了开源路线，并在此过程中为 OpenStack 奠定了基础。第一个主要构建模块 [Nova](https://docs.openstack.org/nova/latest/#:~:text=Nova%20is%20the%20OpenStack%20project,limited%20support%20for%20system%20containers.&text=Keystone%3A%20This%20provides%20identity%20and%20authentication%20for%20all%20OpenStack%20services.) 至今仍是 OpenStack 的一部分。然而，当时一位开发人员这样形容它：“它已上线，有bug，是测试版。去看看吧。”

与此同时，Rackspace 联合创始人 Jonathan Bryce 和他的团队正在开发他们自己的开源云项目。接着，Bryce 告诉我，“我们遇到了 NASA 的这些人，合作非常顺利。于是，我们飞到 [艾姆斯的主校区] 莫菲特联邦机场，和他们一起度过了整整一天。”

“整个过程中，每个人都在那里点头，因为我们当时正在用 Python 重建我们的东西。他们也在用 Python。我们选择了 Apache 2 许可证。他们也选择了 Apache 2 许可证。所以我们当时就想，‘是的，我们必须联合起来！’”

## 开源协作的新方法

他们确实这样做了。OpenStack 的第一个版本 Austin 于2010年发布。除了创建 OpenStack，这也是政府资助的软件首次以开源许可证发布。

“这与以往开源项目的处理方式略有不同，” Bryce 回忆道，他于六月 [被任命为](https://thenewstack.io/linux-foundation-appoints-jonathan-bryce-to-lead-cncf/) [云原生计算基金会 (CNCF)](https://cncf.io/?utm_content=inline+mention) 执行董事。

“在大多数情况下，开源项目要么是人们为了解决自身问题而进行的协作，要么是开源核心项目，其中一家公司构建了开源项目的核心，但所有附加功能都是专有的，并且他们拥有整个商业化过程。”

他说，对于 OpenStack，“我们希望开源软件不仅能成为我们业务的关键推动者，也能成为所有业务的关键推动者。因此从一开始，我们就非常希望有一个庞大的生态系统，让大家齐心协力共同构建它。”

## OpenStack 如何成为云计算的强大力量

从一开始，OpenStack 就吸引了众多公司投资并共享开源财富。早期的成员，包括 [戴尔](https://www.delltechnologies.com/en-us/index.htm?utm_content=inline+mention)、[思科](http://cisco.com/?utm_content=inline+mention)、[Mirantis](https://www.mirantis.com/resources/mirantis-ai-factory-reference-architecture/?utm_source=content-syndication&utm_medium=the-new-stack&utm_campaign=2026q2-whitepaper-building-ai-factories-with-mirantis-k0rdent-ai&utm_content=newsletter&utm_content=inline-mention) 和红帽，至今仍是其支持者。如今，OpenStack 拥有来自500多家公司的数千名贡献者。

几年之内，OpenStack 的受欢迎程度呈爆炸式增长。惠普、[IBM](http://www.ibm.com/products/webmethods-hybrid-integration?utm_content=inline+mention)、红帽、[VMware](https://tanzu.vmware.com?utm_content=inline+mention) 和许多其他科技巨头都纷纷支持 OpenStack。

“有几件事凑到了一起，” 当时 Rackspace 战略与企业发展高级副总裁 Jim Curry 说。“首先，云技术及其形态正达到一个拐点。几年后，Amazon Web Services 刚刚进入主流，人们不仅在寻找开源替代方案，而且在寻找任何 AWS 替代方案。”

Bryce 说，不仅如此：“我们已经打下了基础，建立了社区，并使软件达到了一个市场生态系统真正开始疯狂增长的程度。” 它几乎被用于所有可以使用云的场景。

为了更好地管理日益增长的项目，其企业支持者和开发人员于2012年9月成立了 [OpenStack 基金会](https://www.openstack.org/)。这是一个非营利性企业实体，旨在推广和管理 OpenStack 软件及其社区。

接着，Bryce 继续说：“一个最有趣也有些出乎意料的技术转折发生了。电信行业真正开始与 OpenStack 合作。当我们开始 OpenStack 时，我们还在考虑用于分布式存储的数据中心软件。”

然而，从2014年开始，[软件定义网络 (SDN)](https://thenewstack.io/defining-software-defined-networking-part-1/) 和 [网络功能虚拟化 (NFV)](https://thenewstack.io/de-ossify-the-network-with-function-virtualization/) 开始成为蜂窝网络的骨干。

OpenStack 已成为默认的电信云。Verizon、AT&T、中国移动和德国电信等公司已利用 OpenStack 构建了其5G 基础设施和 SDN，以取代老旧的4G 系统。

与此同时，OpenStack 也被用于其创建者最初设想的场景中。正如 Bryce 所说：“从航空公司、汽车制造商、金融服务、政府机构到私有云、混合云和公共云，所有这些都在使用 OpenStack。”

例如，在欧洲，OpenStack 被用作公共云的基础。其中包括 [德国电信/T-Systems](https://www.t-systems.com/us/en) 的超大规模云、[Cleura 公共云](https://cleura.com/) 和 [OVH 公共云](https://us.ovhcloud.com/public-cloud/)。此外，还有一些不寻常的公共云。一个例子是 [OneQuode](https://www.oneqode.com/)，它是一个总部位于太平洋地区的云提供商，专门为从韩国到旧金山以及其间岛屿的客户提供低延迟和高速的游戏服务。

## OpenStack 与 Linux 基金会强强联合

近年来，OpenStack 在私有云领域也悄然发展。例如，韩国汽车制造商现代汽车使用 OpenStack 来构建其私有云 [hCloud](https://www.hyundai.co.kr/story/CONT0000000000159670)。

现代汽车车云副总裁 Younghold Han 告诉我，“[我们使用 OpenStack 有几个原因](https://www.zdnet.com/article/why-openstack-and-kata-containers-are-both-seeing-a-resurgence-of-adoption/)。” “首先是数据安全。我们希望掌控自己的安全。”

“最后是成本。在现代汽车之前，我在三星的移动业务部门工作。我们为用户推出了多个运行在 AWS 上的服务，你无法想象成本是如何指数级增长的。所以我们构建了自己的私有云。”

除此之外，OpenStack 用户不断探索新的用例。例如，Bryce 说：“[TensorFlow](https://www.tensorflow.org/?utm_source=the%20new%20stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns%20platform) 出现了，现在 OpenStack 被用于人工智能和机器学习。它还被用于边缘视频转码，这样人们就可以在手机上观看4K视频。创新永无止境。”

此外，还有其他重要的项目从 OpenStack 中涌现。其中包括云供应系统 [Airship](https://wiki.openstack.org/wiki/Airship)；轻量级、类似容器的虚拟机 (VM) [Kata Containers](https://katacontainers.io/)；边缘云堆栈 [StarlingX](https://www.starlingx.io/)；以及 [CI/CD](https://thenewstack.io/introduction-to-ci-cd/) 程序 [Zuul](https://zuul-ci.org/docs/zuul/)。得益于这些项目，从2021年开始，[OpenInfra 基金会](https://openinfra.org/) 从 OpenStack 基金会演变而来，以反映超越 OpenStack 的更广泛使命。

然而，最近 OpenStack 社区又向前迈进了一步。三月份，[OpenInfra 基金会与 Linux 基金会](https://thenewstack.io/open-infrastructure-foundation-joins-forces-with-linux-foundation/) 进行了合并。Linux 基金会执行董事 [吉姆·泽姆林](https://www.linkedin.com/in/zemlin) 在当月其组织成员峰会的开幕主题演讲中总结了此举的逻辑：“OpenInfra 和我们的云项目就像花生酱和巧克力一样相得益彰。”

Bryce 在三月的那次活动主题演讲中表示：“我们正在扩大我们的整体影响力，并将能够把开源带到更多地方。”他目前仍领导 OpenInfra 基金会，并兼任 CNCF 的新职务。

OpenStack 及其新伙伴的未来一片光明。

## OpenStack Flamingo 版本有哪些新功能？

Flamingo 版本最主要的成就是大规模移除了 [Eventlet](https://pypi.org/project/eventlet/)，这个作为 OpenStack 基础近18年的 Python 并发库。此次向现代 Python 异步框架的迁移已在 Barbican、Heat、Ironic 和 Mistral 等 OpenStack 模块中完成。在从 Nova 和 Neutron 中移除 Eventlet 方面也取得了进展。

这些更改将减少持续存在的操作问题和技术债务。Eventlet 最终将从 OpenStack 中完全移除。结果将是此版本及后续版本的性能、可扩展性和可持续性得到提高。

OpenStack 技术委员会主席 Goutham Pacha Ravi 在一份声明中表示：“Eventlet 迁移方面的进展，从长远来看增强了 OpenStack。” 此次转型意味着更快、更可靠的裸机供应，更高的并发性以及降低因过时代码依赖而产生意外副作用的风险。

此外，Flamingo 继续推动 OpenStack 进军机密计算领域，并加强访问控制。[Flamingo 的主要升级](https://tfir.io/openstack-flamingo-release-accelerates-enterprise-cloud-capabilities/) 包括：

*   Nova 增加了对一次性直通设备和 AMD SEV-ES 安全飞地支持。
*   Magnum 实现了 Kubernetes 集群的凭证轮换——这是云原生部署的关键安全功能。
*   Manila 支持为文件服务器自带加密密钥。
*   Horizon 引入了用于双因素认证的二维码引导，简化了安全的云操作。

这些增强功能旨在支持人工智能、机器学习和高性能计算等现代工作负载，同时增强企业的隐私和数据保护。

## 推出 OpenStack 的新发布计划

随着 Flamingo 的发布，[OpenStack 正在引入一个“非跳级升级发布流程 (SLURP)”](https://docs.openstack.org/project-team-guide/release-cadence-adjustment.html)，即每六个月发布一次。一段时间以来，OpenStack 用户中一直存在争议：一些人喜欢快速的、每六个月发布一次的版本，而另一些人则希望版本之间间隔一年甚至更长。

在这项折衷方案中，每隔一个版本将被视为 SLURP 版本。除了目前相邻主要版本之间的升级外，SLURP 版本之间也将支持升级。

希望保持六个月发布周期的公司将像往常一样部署每个 SLURP 和“非 SLURP”版本。希望转向一年升级周期的企业将以 SLURP 版本为基准进行同步，然后跳过随后的“非 SLURP”版本，并仅在下一个 SLURP 版本发布时进行升级。

都明白了吗？下一个 SLURP 版本，OpenStack 2026.1 “Gazpacho”，计划于四月发布。

与此同时，我们很快就会看到用户对 Flamingo 的反应。我猜想，由于它对 Python 异步框架的现代化，它将成为迄今为止最受欢迎的 OpenStack 版本。