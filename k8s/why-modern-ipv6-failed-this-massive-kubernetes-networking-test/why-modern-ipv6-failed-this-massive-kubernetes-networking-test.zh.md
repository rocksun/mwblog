巴黎——20世纪80年代我在NASA工作时，曾协助使用[xBase](https://en.wikipedia.org/wiki/XBase)构建一个近地空间网络跟踪程序作为前端，并使用VAX/VMS上的[Datatrieve](https://products.vmssoftware.com/datatrieve)作为后端。完成后，它手动跟踪了超过一千个静态网络链接。

与[德国电信](https://www.telekom.com/)试图做的事情相比，这根本不值一提——德国电信正尝试创建一个高性能仿真平台，用于模拟卫星和地面站：庞大、动态的通信网络，例如SpaceX的[星链](https://www.starlink.com/fr?srsltid=AfmBOor4cOvUEpw_mRdkjxuTxCKKtsB1k094-kTKDD5DoWfdv0OfsrG)。

这并非易事，正如德国电信云架构师 Andreas Florath 和德国电信高级技术专家 Matthias Britsch 在 [2025年欧洲OpenInfra峰会](https://summit2025.openinfra.org/)上的一次演讲中解释的那样。

他们面临的问题是，虽然低地球轨道（LEO）和中地球轨道（MEO）的巨型星座正在彻底改变电信业，但传统的网络路由协议，如开放最短路径优先（OSPF）和边界网关协议（BGP），难以应对其动态拓扑结构——更不用说下一代互联网协议 [IPv6](https://thenewstack.io/why-is-ipv6-adoption-slow/) 了。

## 模拟动态卫星网络的挑战

因此，目标是模拟大规模的卫星网状网络，其中节点在绕地球运行时不断移动，并进出接触，而地球则在它们下方旋转。德国电信的解决方案（仍在进行中）是构建一个可扩展的、基于容器的测试平台，能够准确地再现这些网络动态。

迄今为止最好的成果是一个破纪录的Kubernetes集群。该集群成功地在一个工作节点上运行了2,000个Pod，每个Pod有五个网络接口，总共使用[Multus](https://www.redhat.com/en/blog/demystifying-multus)（来自[红帽](https://www.openshift.com/try?utm_content=inline+mention)的多网络插件）实现了10,000个接口。

正如 Florath 告诉 OpenInfra 听众的那样，“我们不知道有任何其他项目能将Kubernetes扩展到这个级别。”这一成就为高密度容器网络设定了新标准。它还为旨在模拟大规模动态拓扑的企业运营商和卫星网络研究人员提供了重要经验。

达到这一点实属不易。精确的网络仿真不仅需要大量的[容器](https://thenewstack.io/introduction-to-containers/)，还需要反映真实世界节点移动的复杂且不断变化的拓扑结构。正如 Florath 告诉听众的那样，“这些网络的特点是节点在移动，它们的位置在变化，而今天的路由算法并非为此而设计。”真是说得一点没错。

## 构建破纪录的Kubernetes集群

确实，在构建他们的仿真时，他们发现许多网络构建模块都无法胜任这项挑战。例如，团队使用IPv6作为网络地址。你可能会认为，鉴于[IPv6的采用率](https://thenewstack.io/mythbusting-ipv6-why-adoption-lags-and-what-will-change-it/)在2020年全球网络使用中已超过25%，并且所有主流平台、ISP和移动网络都已将其投入生产，我们应该已经解决了所有错误。但你错了。

Britsch 报告说，基于[OpenStack Ironic](https://docs.openstack.org/ironic/latest/)的 Medicube 安装程序“为IPv6创建了完全错误的配置”。即使在正确配置所有内容后，自动化设置仍然持续产生无效的IPv6设置，这表明该工具的网络供应过程中存在根深蒂固的错误。

## IPv6实施中意想不到的故障

团队还难以使用[通过IPv6进行的网络启动安装](https://thenewstack.io/kubernetes-warms-up-to-ipv6/)。某些戴尔（Dell）的BIOS实现缺乏完整的IPv6启动支持，即使有也存在缺陷。这导致了启动停滞或失败。工具链需要手动修复或内核级变通方案，以实现可靠的PXE/HTTP IPv6启动。戴尔最终确实修补了BIOS，缓解了这些问题。

然而，总而言之，他们不得不构建自定义的供应工具，以使其大规模Kubernetes部署中的IPv6能够正常工作。其他希望部署高密度网络的人士应予以关注。

工程师们还面临并克服了只有在这些前所未有的规模下才会出现的严重瓶颈。这些限制包括网络接口和MAC地址表溢出、IP地址消失、数据包处理的CPU周期配置错误，以及与BIOS更新挑战相关的系统崩溃。他们尝试并放弃了一系列工具——Canonical等商业安装在文档和可靠性方面表现不佳，而网络自动化和自定义磁盘镜像创建则为实现稳定平台提供了途径。

## 克服前所未有的扩展瓶颈

至关重要的是，套接字缓冲区大小、内核配置参数和网络设备地址表都需要进行重大调整。Multus插件使得每个Pod能够处理多个接口，但一旦扩展到数千个，主要的IP地址管理问题就出现了。这促使团队通过使地址对每个Pod本地化、优化内核限制并关闭一些硬件限制来强制进行MAC地址处理，从而重新设计了地址分配方式。

正如 Britsch 指出的那样，他们发现的网络接口卡限制“对我来说是全新的；即使是最新的网卡也无法处理那么多MAC地址。”

经过数月的故障排除和逐步改进，该设置达到了一个稳定的点：2,000个Pod在每个节点上承载10,000个接口，持续超过三个月。最后，正如 Britsch 自豪地表示：“我们完全自动化了一切：从零开始安装，完全配置的堆栈。”

## 实现稳定性和全面自动化

然而，进一步的扩展尝试揭示了新的、尚未解决的瓶颈，这表明虽然目前的水平足以满足模拟任务，但未来的增强将需要解决额外的网络保真度和数据包处理延迟问题。简而言之，工作尚未完成。

尽管如此，团队最终成功自动化了他们的堆栈部署，并正在探索与卫星定位数据集成，以模拟动态视距网络条件。这是朝着在轨道规模上验证下一代路由协议（例如 [IS-IS](https://networklessons.com/is-is/introduction-to-is-is)）迈出的关键一步。

随着卫星网络和语音服务（例如 [T-Mobile的T-Satellite卫星电话服务](https://www.t-mobile.com/coverage/satellite-phone-service)）的兴起，我们需要这些服务来理解我们空中的互联网。工程师们正在与他们的老板讨论开源他们的部署脚本和模块化启动解决方案，以便所有人都能从他们的工作中受益。