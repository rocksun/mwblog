# 新私有云架构师指南

![Featued image for: The Architect’s Guide to the New Private Cloud](https://cdn.thenewstack.io/media/2024/07/84cd53b3-privatecloud-1024x576.jpg)

几年来，“私有云”一词一直带有负面含义。但正如我们所知，技术更像一个轮子而不是一支箭，私有云应运而生，并获得了极大的关注——而且都是积极的。

数据很清楚：Forrester 的 2023 年基础设施云调查显示，在 1300 名受访的企业决策者中，有 79% 的人表示正在实施私有云。根据英国 Citrix 的一份报告，93% 的 IT 领导者参与了数据回迁工作。久负盛名的 IDC 发现，80% 的公司在将数据迁移到云一年内将部分或全部数据回迁。

云工业综合体的“这里没什么可看的”说法不攻自破。

原因多种多样，我们将详细说明，但更重要的是，[回迁](https://thenewstack.io/pros-and-cons-of-cloud-repatriation-is-it-right-for-you/) 的正确架构是什么？[私有云](https://thenewstack.io/parity-check-announcements-private-clouds-death-premature/) 的工程第一性原理是什么？最后，如何为 AI 的数据基础设施需求设计？

**回迁到私有云的原因**

公司回迁的主要原因是成本。他们通过回迁节省了高达 70% 的成本。这已得到 [37 Signals](https://www.theregister.com/2023/09/18/37_signals_cloud_repatriation_savings/?ref=blog.min.io)、[X](https://www.datacenterdynamics.com/en/news/xtwitter-claims-100m-in-annual-savings-after-exiting-sacramento-data-center/?ref=blog.min.io) 和 [Ahrefs](https://www.theregister.com/2023/03/13/ahrefs_on_prem_savings/?ref=blog.min.io) 等不同公司的公开证明。

相关但并不相同的是可预测性。私有云的弹性较低，但可预测性更高。（我们在下面讨论了一些弹性技巧。）对于大多数了解其工作负载的 CIO 来说，这种权衡是值得的。对于 CFO 来说，这是一个更容易的选择。

安全问题位居第三。这并不是说公有云本身不安全，它不是。它确实表明 CISO 不完全信任他们的公有云合作伙伴——事实上，大多数云提供商保留查看您的存储桶的权利——在这方面。在 AI 时代，风险只会越来越高。

相关的是，控制是每个 CIO 的清单。与成本节省、可预测性和安全性一起，您不仅可以完全控制您的 AI 数据基础设施，而且这些数据对于所有应用程序来说都很容易获取。这使您能够将模型托管在 AI 数据基础设施上，您和您的团队可以设置安全标准以满足您的独特安全要求——甚至包括物理访问。

成熟度也排在榜单上。现代云是一种运营模式，而不是一个位置。这种模式曾经是主要公有云的专属，现在无处不在——从边缘到核心。容器化、编排、[微服务](https://thenewstack.io/microservices/)、软件定义基础设施和 RESTful API 是标准操作程序。您在哪里运行它们并不重要——如果它不重要，为什么要支付两到三倍的成本？

法规也发挥着作用，尤其是在法规不断发展的情况下。一些架构、一些地理位置甚至一些部署场景（军事/情报）最初并不需要私有云，但现在需要了。

同样，原因会有所不同，但效果是一样的。私有云又重新流行起来。问题是：过去几年发生了什么变化？

**私有云的设计模式是现代数据湖**

如上所述，私有云与公有云一样，运行在云运营模式上。边缘云运行在云运营模式上。托管运行在云运营模式上。

这种运营模式定义了一种特定的架构，一次又一次地，这种架构使现代数据湖成为可能。当然还有其他架构，但使用私有云构建您的现代数据湖可以让组织只为他们需要的资源付费。当他们的业务增长时，扩展就像向集群添加更多资源一样简单。不需要重新设计。

[AI/ML](https://blog.min.io/the-full-stack-ai-engineer-a-modern-day-polymath/) 受支持。[高级分析？](https://blog.min.io/enterprise-object-store-observability/) 受支持。日志分析/威胁分析？受支持。[HDFS 替换/迁移](https://blog.min.io/migrating-from-hadoop-without-rip-and-replace/)？受支持。
现代数据湖是数据仓库和数据湖的结合，它使用对象存储来存储所有数据。对象存储层是软件定义的、可扩展的、云原生的，并且性能出色。可以通过选择[硬件（NVMe）和网络（100 GbE 或更高）](https://blog.min.io/nvme_benchmark/)来调整性能，这些硬件和网络可以方便地从 Supermicro、Dell 和 HPE 等供应商处购买。

使用对象存储与数据湖是标准做法，使用对象存储与数据仓库是新趋势，这得益于 Apache Iceberg、Apache Hudi 和 Delta Lake 等开放式表格格式 (OTF)。关于此架构的更多细节超出了本文的范围。为此，我建议阅读 Keith Pijanowski 的完整[关于现代数据湖的文章](https://thenewstack.io/the-architects-guide-a-modern-data-lake-reference-architecture/)。以下是架构图：

此架构旨在实现以下目标，所有这些目标都是核心云运行原则，也是私有云的核心原则：

**高性能：**虽然私有云可以设计为具有高容量，但现代私有云旨在提供大规模的性能。此架构优先考虑强调速度和效率的工具。正如杰夫·贝索斯所说，谁愿意花更多钱，等待更长时间才能得到它？同样的原则也适用于这里：谁想要更慢？**解耦计算和存储：**将这些组件分离提供了更高的灵活性和可扩展性，使您选择的基础设施、服务和工具能够在其各自的专业领域中脱颖而出。**开放标准：**开放标准不仅鼓励互操作性，而且还使您的投资具有未来可期性。这不仅包括开源解决方案，还包括开放式表格格式，正如我们将要探讨的那样。不要出于这些原因（以及它们永远不会成为云原生）而构建一个带有存储设备的私有云。**与 RESTful API 的兼容性：**互连性是必不可少的。您的工具应该共享一种通用语言，其中 S3 作为云存储的通用语言。出于这个原因，不要构建一个以 POSIX 为中心的私有云，即使它声称支持 S3。选择真正的 S3。**软件驱动/基础设施即代码：**自动化并让 Kubernetes 负责编排您的基础设施，使您能够抽象化手动管理的复杂性，并实现快速高效的可扩展性。**增强的安全性和合规性：**由于私有云提供专用基础设施，因此它们可以更好地控制数据并提供增强的安全措施。这对处理敏感信息的行业（如金融和医疗保健）尤其有利。**法规遵从性：**此架构可以通过提供可定制的安全设置和审计控制来支持法规遵从性，以满足特定行业标准。
**将您的私有云投入使用**
我们已经看到了许多方法来点亮私有云。所有这些方法都可以奏效；这实际上取决于企业和用例。

- 时间有限的混合模式，其中一些数据和应用程序保留在公有云中，而私有云正在被填充。
- 从公有云完全迁移到私有云。
- 私有云的绿地构建。这在企业将 AI 实验投入生产时尤其受欢迎。
- 棕地迁移，您将公有云数据和基础设施迁移回现有的私有云部署。虽然经济实惠，但这种方法也有一些缺点。
- “其他”类别（突发和外部表）。
**时间有限的混合方法**
时间有限的混合方法本质上将公有云变成了冷存储，并在一段时间内（几个月/季度，而不是几年）构建您的私有云足迹。这包括在私有云上购买和配置您的基础设施和软件堆栈。

然后，您将数据管道指向私有云，而不是公有云。

使用时间有限的混合方法，随着时间的推移，公有云从冷存储变为冻结，而私有云成为主要和主要的存储类型。

您可能需要一段时间同时进行这两种操作。然而，目标是将公有云用作分层冷存储，将私有云用作热存储。随着时间的推移，公有云从冷存储变为冻结，而私有云成为主要和主要的存储类型。
一家领先的网络安全公司采取了以下措施。它首先与 MinIO 和 Equinix 合作建立了一个私有云，然后将每天 250 泽字节 (TiB) 的数据洪流转向该方向。鉴于日志分析在运营价值方面具有较高的衰减函数，因此新的私有云很快成为威胁狩猎数据的主要来源。这个私有云已经发展到近 1 泽字节（并且很快就会超过这个阈值），将这些工作负载（实际上是核心业务）迁移到私有云（以运营支出而不是资本支出）的决定将企业的毛利率提高了 2% 以上。因此，这家公司的估值倍数令其同行羡慕。

**完全回迁**
有时，将应用程序和数据保留在公有云和私有云上都是不可行的。在这种情况下，您需要与您的云提供商分手。这很难，即使消除了退出费用，他们也会让它变得很痛苦。（细则基本上说，要获得任何退出费用减免，一切都必须离开。）

这是完全可行的；它只需要多一点计划和多一点业务摩擦。在这种情况下，配置您的托管数据中心或私有云和应用程序堆栈。然后备份数据卡车或租赁网络将数据传输到您的私有云数据基础设施。

此时您就自由了，但如果您是那种喜欢双重保险的人，请做好支付一两个月双倍费用的准备。

一家领先的流媒体公司在离开公有云时采用了这种方法。它将近 1 泽字节的数据迁移到新的私有云，包括所有电影、节目、纪录片等。整个过程大约需要三个季度。然而，回报是巨大的，并且管理服务的团队的复杂性大大降低。他们还享受了“[首次字节时间](https://blog.min.io/time-to-first-byte-streaming-media/)” 显著提升的额外好处——这是该领域的一个关键指标。

**全新私有云**
这是一个相当直接的提议，通常涉及所有新事物。项目是新的；项目上的数据将是新的（或比较新的）或从某个即将上线的来源生成（例如一个大型制造工厂或一个新的云视频点播服务）。在这里，您对工作负载进行规模调整——您甚至可以在公有云上对其进行测试——但想法是，它从一开始就在私有云上运行。

采用全新方法，一切都将是新的。您可以在公有云上对其进行测试，但想法是，它从一开始就在私有云上运行，不仅是为了规模，还为了安全、隐私和控制。

我们经常在 AI 数据基础设施中看到这种情况。早期的实验是在公有云中进行的。数据并不那么重要。GPU 的可用性相当好。尽管如此，企业知道工作负载需要在私有云上运行以进行生产——不仅是为了规模，还为了安全、隐私和控制。

世界上领先的汽车公司之一最近将其完全自动驾驶计划从基于规则的系统转变为基于实际驾驶员行为的系统。这种行为是通过从其车辆中获取的数百万视频和日志文件“学习”到的。优秀的驾驶员、糟糕的驾驶员、一般的驾驶员。不仅来自视频，还来自汽车遥测的其他元素，例如制动、加速、转向扭矩等。基于规则的 ML 方法的规模为 PB 级；视频的规模为 EB 级。该公司不会与任何人共享这些数据（事实上，两家公有云都有竞争的计划）。该 AI 工作负载——所有超过 300 台服务器——一直都是私有云计划。

**棕地私有云**
我们在这里要坦诚地说：我们看到了这种情况，但我们并不喜欢它。这包括尝试在硬盘驱动器上运行高性能工作负载，以便在 [SAN/NAS 之上](https://blog.min.io/no-san-nas/)（存储区域网络/网络附加存储）分层 MinIO。

它有效，但很少是最佳解决方案。它经济实惠（您正在重复使用硬件）；它摩擦力低（无需采购）；但很少能达到高性能。尽管如此，我们在这里将其包含在内以确保全面性。

它确实提出了一点。在任何情况下设计私有云时，都要规划异构性。这是保证，坦率地说应该是计划的一部分。在上述场景之一中，一半的硬件来自 Supermicro，另一半来自戴尔。随着世界发生变化，新技术变得可用，您的软件不应该关心。

**其他**
还有两种不太常见但应该纳入考虑范围的场景。一个是混合突发方法，另一个是外部表方法。两者都与混合选项相关，但可能不受时间限制。
在混合突发方法中，您维护一个私有云，同时将其设计为无缝扩展或“突发”到公有云以获得额外的灵活性。这种策略通常被采用以利用额外的 GPU 容量或使用特定的云服务。在此模型中，某些任务会暂时转移到公有云进行处理。分析完成后，结果将发送回私有云，然后公有云资源将被停用。

在新的私有云中，我们必须让现有的硬件发挥作用，而不是仅仅报废硬件并购买新的硬件。基础设施管理是一项工作。它不应该是可怕的，但应该计划好。

我们有一家主要的金融服务客户正在使用这种方法进行信用风险和市场风险计算。它使用公有云进行一些计算操作，并将其与使用 MinIO 和 Dremio 的私有云数据湖相结合。

云运营模型的美妙之处在于，架构应该支持两个地方的操作。它实际上是一条双向道。在某一点上，它是一条单行道，但世界已经改变，企业有选择权。

通过外部表选项，组织仍然可以通过将现有的云数据仓库（如 [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) 和 SQL Server）与构建在私有云上的数据湖集成，来从云运营模型的原则中获益。这种混合设置使企业能够从现代数据湖的性能、数据安全和开放标准设计中获益，同时仍然利用对云基础设施的现有投资。现在，每个主要数据库供应商都提供对外部表的支持。此功能允许用户查询对象存储中的数据，无论它在哪里，就好像它是数据库中的常规表一样，而无需迁移的麻烦。您的数据保留在私有云中，但可以在需要的地方使用。

**最终想法和建议**
多年来，我们一直参与了许多私有云回迁/新建项目。团队感到惊讶的一件事是再次管理硬件。在云中，它是透明的。DevOps 和站点可靠性工程师只在 API 级别与基础设施交互。如果虚拟机出现故障，请终止并启动一个新的虚拟机来代替它。不幸的是，在新的私有云中，我们必须让现有的硬件发挥作用，而不是仅仅报废硬件并购买新的硬件。

基础设施管理是一项工作。它是不可避免的。它不应该是可怕的，但应该计划好。软件工程/DevOps 方面和数据中心工程师之间需要明确责任划分。数据中心的这位 SME（主题专家）应该了解所有硬件的来龙去脉。他们将负责与硬件相关的任何事情，包括故障、更换和任何维护。

软件在这里很重要。这就是 MinIO 在其全局控制台中构建可观察性的原因。在私有云的世界中，您应该运行智能软件和哑硬件。但是，该软件必须承担这种经济效益的操作负担。硬件人员根本无法构建可观察性层，MinIO 必须这样做。

如果您是一个每周部署一次的组织，这意味着每次部署可能都是一场盛事。这是因为，由于部署频率低，很难预测和修复错误。当部署没有按计划进行时，所有人都需要参与。通常，流程如下：

- 设计以分布式方式部署您的应用程序。
- 在本地环境中对其进行测试。
- 在开发和阶段环境中进一步验证。
- 添加监控、指标、跟踪和更改。
- 在本地、混合和云环境中部署。
当这些 CI/CD 原则在实践中应用时，一位经验丰富的强力数据中心工程师与另一位经验丰富的强力 DevOps/SRE 工程师密切合作，可以轻松管理私有云或托管设施中的 5,000 多个节点。我们有客户正在做这件事。一旦您遵循 CI/CD 基线原则，几乎所有事情都可以并且应该自动化，数据中心和 DevOps 工程师将只专注于那些无法自动化的任务。
最后，如果您错过了，colos 与我们对私有云的定义是同义词。托管机房在完全本地基础设施和公有云之间提供了一个中间地带，提供了两全其美的优势。通过访问顶级网络和靠近公有云提供商，托管机房促进了低延迟连接和混合云设置，从而实现高效的数据传输和处理。这种灵活性以及成功部署混合云的潜力对于旨在优化运营并保持竞争优势的企业至关重要。要详细了解其工作原理，请查看我们的 [MinIO 和 Equinix 页面](https://min.io/solutions/equinix)。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等。