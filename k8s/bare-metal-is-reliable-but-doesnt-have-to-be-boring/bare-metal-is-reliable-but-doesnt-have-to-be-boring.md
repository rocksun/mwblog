# 裸机是可靠的，但不一定是无聊的

翻译自 [Bare Metal Is Reliable, But Doesn’t Have to Be Boring](https://thenewstack.io/bare-metal-is-reliable-but-doesnt-have-to-be-boring/) 。

这里有一个丰富而充满活力的生态系统，运行着世界上一些最关键的任务应用程序。

![](https://cdn.thenewstack.io/media/2023/05/5b06a8f1-shutterstock_5-1024x683.jpg)

在过去十年左右的时间里，我将应用程序部署到了各种软件和基础设施服务上，从虚拟机到容器再到 function 。做过这些之后，我天真地把裸金属服务器看作只是非常大的虚拟机的替代品。(预警:我错了!)在 Equinix ，一家领先的裸金属即服务领域公司，工作三个月后，我想和其他更多从应用开发背景来的人分享一些我在学习这种基础设施方面获得的“aha”时刻。

## 为正确的工作提供正确的工具

裸机并不适合所有人。我希望这不是一个有争议的声明。

这取决于您要完成的任务，有点像选择一种交通方式（步行，骑自行车，驾驶，飞行）。我不会送孩子上学，也不会在裸机服务器上部署“Hello， World！”应用程序。任务的性质应决定使用哪种工具。

自从加入团队以来，我一直听说我们的裸机云服务 Equinix Metal 是一个“构建平台的平台”，现在我明白了。如果您想部署一个平台（例如，像 Zoom 这样每天拥有数百万用户的平台），裸机是扩展的绝佳选择。

下面是裸机真正出色的更多示例方案：

* 高性能、低延迟：裸机非常适合需要强大硬件和低延迟的应用程序，例如视频流或在线游戏。它提供对硬件组件（例如 NVMe（非易失性存储器高速）驱动器、NIC（网络接口控制器）和 GPU（图形处理单元））的直接访问，而没有传统虚拟化的性能开销。
* 受监管的工作负载：GDPR 和 PCI-DSS 可能是最常见的数据保护和隐私法规，但还有更多，而且它们因世界而异。全球裸机云平台可帮助您将敏感数据保持在相关法规定义的地理范围内，以保持合规性。
* 可预测的工作负载：云是为了弹性而设计的，但如果工作负载的需求是可预测的，那么从长远来看，将其移动到专用的裸机服务器可能会节省您的成本。（想想围绕网络托管或电子邮件的用例。值得注意的是，Equinix Metal 通过其自动化、快速的服务器配置（稍后会详细介绍），使成本和性能与弹性之间的选择变得更加容易。

## 哇，这是很多网络！

当我第一次登录 Equinix Metal 门户时，我看到的各种网络资源（IP 地址、子网、VLAN（虚拟局域网）、BGP（边界网关协议）、网关、第 2 层等）比我习惯的要多得多。这不是一个云控制台，它为您提供在部署应用程序时自动为您设置的单个 URL。

这是有原因的：控制。堆栈越往下走，您（负责构建应用程序的人）可用的选项就越多。与生活中的大多数事情一样，这涉及到权衡。在这种情况下，交易是在控制和便利之间。您需要两者中的哪一个取决于您要做什么。例如，如果你试图建立一个全球可用的平台，我认为你需要更多的控制，你需要在引擎盖下的所有这些机制以裸露的金属云的方式浮出水面。

![](https://cdn.thenewstack.io/media/2023/05/9a567657-image2.png)

## An API for Colo 用于科洛的 API

我们今天享受的云生态系统的成功和活力很大程度上归功于通过 API 与云平台交互的用户体验。Equinix Metal 为裸机创造了这种体验。其用户可以通过 API 在世界任何地方远程配置，配置和管理专用服务器。这有助于基础架构工程师在几分钟内（而不是几个月）开始在裸机上进行部署。

与 Equinix Metal API 交互的两种流行方法是 [Equinix Terraform](https://registry.terraform.io/providers/equinix/equinix/latest/docs) 模块和 [Equinix Metal CLI](https://deploy.equinix.com/developers/docs/metal/libraries/cli/)。（还有更多可用的方法，记录在 [Equinix 实验室](http://deploy.equinix.com/labs)。

Equinix Metal CLI 的使用示例：

```bash
# Provisions a c3.small.x86 in the Dallas metro running Ubuntu 20.04:
metal device create -p $METAL_PROJECT_ID -P c3.small.x86 -m da -H test-staging-2 -O ubuntu_20_04
```
```bash
Equinix Terraform 模块的使用示例：

resource "equinix_metal_device" "device" {
  hostname         = "tf-device"
  plan             = "c3.small.x86"
  metro            = "sv"
  operating_system = "ubuntu_20_04"
  billing_cycle    = "hourly"
  project_id       = "f2a2d7ad-123-456-789-10ebdf49cf84"
```

## 连接到其他云

虽然术语“混合云”对于一些云纯粹主义者来说可能令人生畏，但现实情况是，许多组织使用各种云平台的服务组合。其中许多组织，无论是政府、金融、电信还是医疗保健，其工作负载在本地运行，由于这些行业的隐私/数据法规，这些工作负载不是迁移到云的优先事项。如果可以的话，这些组织仍然希望将现代云服务的优势用于这些工作负载。

裸机云提供商通过提供与其他云平台的专用网络连接，使这成为可能。 例如，[Equinix Fabric](https://docs.equinix.com/en-us/Content/Interconnection/Fabric/use-cases/Fabric-hybrid-MC-conn-UC.htm) 通过 [AWS Direct Connect](https://docs.equinix.com/en-us/Content/Interconnection/Fabric/connections/Fabric-aws-direct-connect.htm) 、[Azure ExpressRoute](https://docs.equinix.com/en-us/Content/Interconnection/Fabric/connections/Fabric-ms-azure.htm)、[Google Cloud Interconnect](https://docs.equinix.com/en-us/Content/Interconnection/Fabric/connections/Fabric-connect-google.htm)、[IBM Cloud Direct Link](https://docs.equinix.com/en-us/Content/Interconnection/Fabric/connections/Fabric-connect-ibm-cloud.htm) 或任何其他受支持的云等服务，提供从客户自己的托管 IT 基础设施（或其裸机服务器）到云提供商的专用网络连接。

这就是“云邻接”，它是混合多云世界的下一个演变。我的一位同事在最近的一篇[博客文章](https://blog.equinix.com/blog/2022/02/02/why-cloud-adjacency-is-the-new-on-premises-strategy/)中完美地描述了这个概念：

“云邻接是关键：公司获得满足监管机构要求所需的国内物理基础设施。他们还可以利用云服务，而无需将数据发送到国外或使其面临风险。只有需要移动以支持特定云工作负载的数据才会被移动，任何传递到云的数据都将通过私有、安全的互连进行。

![](https://cdn.thenewstack.io/media/2023/05/6cd11478-image1.png)

## 最后一件事...

裸机计算比我以前想象的要多得多。这里有一个丰富而充满活力的生态系统，运行着世界上一些最关键的任务应用程序。生态系统也许有些被低估了，主要是由于许多更新和更闪亮的技术。在最近的 KubeCon 上，我一次又一次地听到人们希望他们的基础设施可靠且无聊。我绝对同意第一部分，但我希望我已经证明基础设施不一定是无聊的，至少不是裸机。