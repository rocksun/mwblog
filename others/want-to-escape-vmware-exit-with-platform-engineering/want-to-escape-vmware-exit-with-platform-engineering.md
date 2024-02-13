<!--
title: 平台工程助您摆脱供应商锁定
cover: https://cdn.thenewstack.io/media/2024/02/000ab88a-exit-1024x576.jpg
-->

VMware变革不可避免，及时开启转换至关重要。

> 译自 [How Platform Engineering Can Help Solve Vendor Lock-In](https://thenewstack.io/want-to-escape-vmware-exit-with-platform-engineering/)，作者 Luca Galante 是Humanitec的产品经理。他每个月都会与数十个工程团队进行交流。他将从查看数百个DevOps设置中汲取的经验教训总结为全行业可读的简洁且有见地的文章，...

去年，[Forrester](https://www.forrester.com/blogs/predictions-2024-technology-infrastructure/)预测有20%的VMware客户会放弃该生态系统。随着Broadcom以610亿美元收购VMware，看来这种情况正在迅速发生—大量VMware客户突然受到一波变化的影响。数以千计的VMware客户突然遭遇了[大量产品被取消](https://www.thestack.technology/vmware-is-killing-off-56-products-including-vsphere-hypervisor-and-nsx/)、[永久许可证被放弃](https://redresscompliance.com/broadcom-vmware-licensing-and-subscription-changes-explained/)以及[预期成本大幅增加的情况](https://www.forbes.com/sites/stevemcdowell/2023/12/21/why-your-costs-may-go-up-with-vmwares-cheaper-new-bundles/)。

这并不令人惊讶，因为随着新老板的到来，业务重心也会发生变化。[根据《华尔街日报》的报道](https://www.wsj.com/articles/broadcoms-vmware-overhaul-draws-attention-of-cios-c76998b6)，Broadcom已经明确表示，其目标是“完全关注其顶级600家客户的需求和优先事项”。这就让剩下的30多万客户，其中许多客户对VMware产品有着高度依赖，正面临着一个非常不确定的未来。

为此，三家平台工程公司——Humanitec、Thoughtworks和Bechtle Competence Center AVS——联手帮助VMware客户通过平台工程和模块化[内部开发者平台](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/)来建立一个简单可靠的退出通道。

## 这些变化可能带来的影响

这些变化对您的影响程度取决于您正在使用的VMware技术以及您的集成策略。总共有三种不同的使用案例:

- 案例1: 您正在使用[Tanzu](https://tanzu.vmware.com/tanzu?utm_content=inline-mention)作为K8s基础。Tanzu Kubernetes Grid(TKG)可能在VMware或任何云提供商上运行。
- 案例2: 您正在使用Tanzu Application Service(TAS)，即旧的Pivotal Cloud Foundry(PCF)。您在VMware或任何云提供商上运行。
- 案例3: 您正在使用[Tanzu Application Platform(TAP)](https://thenewstack.io/vmware-expands-tanzu-into-a-full-platform-engineering-environment/)，并且您与VMware内置的诸如Mission Control或Wavefront等所有特殊功能深度集成。

![放大](https://cdn.thenewstack.io/media/2024/02/dd52f366-image2.png)

第三种情况的用户将面临最高的锁定，第一种情况的用户锁定最低。根据您的谈判能力以及您被锁定在VMware产品中的程度，您极有可能会看到大幅提价和所有产品线上的产品开发与支持下降。

如果您不能完全确定自己是VMware会优先考虑的这600个核心客户之一，那么开始退出VMware生态系统的进程对您来说至关重要。

## 逃离供应商锁定的计划

案例1最简单。它有一个快速且努力最小的迁移路径，涉及到模块化内部开发者平台的转型。这可以在很短的时间内完成。

案例2更复杂，但是仍然很容易实现。您将用云原生构建包替换TAS的构建包，然后用平台编排器编排它们。

案例3是最具挑战性的，但也是识别VMware退出路径最关键的，因为这是VMware会收紧的地方。由于您的流程与机群管理、运维工具和可观察性的集成，会带来额外的复杂性。

我们在一份详细的白皮书中讨论了所有这些情况，您的风险以及迁移和缓解选项。如果您是VMware超过30万客户中的一员——还未受到这些变化的影响——那么理解这些变化势在必行，开始有效过渡的时间非常紧迫，这一点很重要。

[Broadcom为收购VMware支付的610亿美元是一笔巨额资金](https://thenewstack.io/vmware-to-be-acquired-by-broadcom-in-a-61-billion-deal/)，而[Broadcom](https://thenewstack.io/dod-software-factories-take-charge-of-their-digital-destinies/)意图收回这笔资金。

立即下载该白皮书并[开始规划您的脱离](https://humanitec.com/whitepapers/escaping-the-vm-ware-grip-with-a-modular-internal-developer-platform)(https://humanitec.com/whitepapers/escaping-the-vm-ware-grip-with-a-modular-internal-developer-platform)。
