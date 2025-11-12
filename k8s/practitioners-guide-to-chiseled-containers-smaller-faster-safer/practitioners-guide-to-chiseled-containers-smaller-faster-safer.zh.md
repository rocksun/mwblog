容器化改变了团队构建和部署应用程序的方式，但也带来了新的操作挑战。传统的[容器镜像](https://thenewstack.io/introduction-to-containers/)通常包含远超所需数量的组件——运行中的应用程序从不需要的shell实用程序、包管理器和库。这种臃肿会增加镜像大小，减慢部署速度，并扩大攻击面。

为了满足现代性能和安全需求，行业应考虑转向更精简、确定性的镜像。这就是凿刻容器（chiseled containers）——只包含运行应用程序所需的基本要素，不包含任何其他内容的镜像——提供了新的前进道路。

## **什么是凿刻容器？**

凿刻容器是通过从基础镜像中删除大多数非必要组件来构建的——没有shell，没有包管理器，没有超出应用程序严格要求的运行时依赖。这一概念在[Ubuntu生态系统](https://thenewstack.io/why-broadcoms-ubuntu-bet-on-vmware-will-delight-devs-and-ops/)中得到实施，自动化“凿除”了不必要的层，同时保持了相同的运行时行为和稳定性。同样的原则也可以应用于其他[Linux发行版和框架](https://thenewstack.io/introduction-to-linux-operating-system/)。

例如，Canonical的基准测试显示，与标准Ubuntu基础镜像相比，.NET应用程序的镜像大小可减少高达90%，[Java](https://thenewstack.io/introduction-to-java-programming-language/)工作负载可减少约50%。更小的镜像意味着更快的部署、更少的CVE和更容易的合规性。

[![显示凿刻镜像与非凿刻镜像大小对比的条形图](https://cdn.thenewstack.io/media/2025/11/4eae37d4-chiseled-nonchisled-graph.jpg)](https://cdn.thenewstack.io/media/2025/11/4eae37d4-chiseled-nonchisled-graph.jpg)

(来源：Broadcom)

## **为什么组织正在采用凿刻容器**

将镜像精简至只包含必要组件可提高：

*   **安全性与合规性：** 通过移除shell、编译器和包工具，凿刻容器显著降低了常见CVE的暴露风险。根据Ubuntu的说法，这种方法将容器的攻击面比传统镜像减少了高达80%，从而大大降低了漏洞风险。这简化了补丁工作流程，并帮助团队根据其法规要求（如安全技术实施指南（STIG）和联邦信息处理标准（FIPS））保持合规性。
*   **性能与效率：** 更小的镜像直接转化为更快的拉取速度、更短的启动时间以及更低的带宽和存储成本。这对于大规模微服务或边缘工作负载尤为关键。
*   **操作简便性：** 凿刻容器在设计上是确定性的和不可变的。没有shell或包管理器，运行时修改变得不可能，这使得跨环境构建保持一致，并消除了经典的“在我的机器上能运行”问题。
*   **可持续性：** 更精简的镜像消耗更少的计算和网络资源，从而降低了成本和环境足迹。

这些优势直接转化为多个关键部署场景中的实际益处。

## **推荐的最小镜像使用案例**

以下是凿刻容器最有用的一些领域。

*   **受监管的工作负载：** 医疗保健、金融和公共部门的工作负载受益于安全、可预测和可审计的运行时环境。
*   **电子商务和突发容量：** 凿刻容器使电子商务和其他突发性应用程序能够在流量高峰期间快速扩展，通过更快的启动和更低的开销来降低成本和能耗。
*   **边缘和物联网部署：** 最小镜像可以在有限连接上快速部署，并在受限设备上高效运行。

## **凿刻容器如何与VKS集成**

随着企业采用最小容器镜像，其Kubernetes环境的跨环境一致性变得至关重要。[VMware vSphere Kubernetes Service](https://blogs.vmware.com/cloud-foundation/2025/08/26/broadcom-canonical-partnership/) (VKS)是内置于VMware Cloud Foundation (VCF)中的[CNCF](https://cncf.io/?utm_content=inline+mention)认证Kubernetes运行时，它使平台工程师能够在统一平台内同时部署和管理传统容器和凿刻容器。

凭借集成的多集群管理、集中的策略执行和一致的安全模型，VKS帮助团队将最小化、确定性的镜像投入运营，同时在跨云和数据中心保持合规性。

Canonical的凿刻Ubuntu容器在部署到VCF上时，展示了组织如何在企业Kubernetes环境中实现高性能和强大的安全性。

此演示展示了在VMware Cloud Foundation (VCF)上使用Canonical凿刻Ubuntu容器的优势。

视频

[YOUTUBE.COM/THENEWSTACK

技术发展迅速，不要错过任何一集。订阅我们的YouTube
频道，观看我们所有的播客、采访、演示等。

订阅](https://youtube.com/thenewstack?sub_confirmation=1)

## **安全应用程序部署的未来**

凿刻容器不仅仅是更小。它们代表了现代应用程序更智能、更安全的基础。通过移除非必要组件，它们在效率、可重现性和合规性方面带来了显著的改进。随着越来越多的组织对其平台进行现代化改造，采用最小化、确定性的镜像将成为一种标准的最佳实践。