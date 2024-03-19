## RapidAI 如何利用边缘、Kubernetes 和 AI 提升中风护理

![用于：RapidAI 如何利用边缘、Kubernetes 和 AI 提升中风护理的特色图片](https://cdn.thenewstack.io/media/2024/03/43e60ff9-edge-kubernetes-ai-stroke-care-1024x576.jpg)

直到最近，为中风患者成功实施治疗的时间窗口还非常窄——大约两小时——此后治疗效果会降低。但 [RapidAI](https://www.rapidai.com) 正致力于通过使用深度临床人工智能 (AI) 来改变这种情况。这家医疗保健 AI 公司为磁共振成像 (MRI) 和非对比和对比 CTA（计算机断层血管造影）扫描提供图像分析。

RapidAI 技术的核心源自斯坦福中风中心的研究所。

RapidAI 的联合创始人之一 [格雷格·阿尔伯斯博士](https://profiles.stanford.edu/gregory-albers) 及其团队使用先进的成像技术扩展了最常见的中风类型——[缺血性中风](https://www.stroke.org/en/about-stroke/types-of-stroke/ischemic-stroke-clots) 的治疗窗口。

他们的 [研究](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6454953/) 阐明了脑缺血的演变，并在 2018 年将理想的缺血性中风治疗窗口从大约两小时延长至 24 小时。“我们说‘时间就是大脑’，因为在中风期间，每分钟都有数百万个脑细胞和神经元死亡，”RapidAI 的首席创新和技术官 [阿米特·法德尼斯](https://www.linkedin.com/in/amphadnis/) 说。

### RapidAI 如何加速中风诊断

RapidAI 充当助手，在临床医生和放射科医生做出护理决策时为他们提供支持。对于中风患者而言，RapidAI 特别提供有关患者是否（或有高风险）中风的重要信息。如果是，它会根据中风是缺血性还是 [出血性](https://www.stroke.org/en/about-stroke/types-of-stroke/hemorrhagic-strokes-bleeds) 提供更详细的信息。

第一级算法执行分类和通知，以指示 AI 是否怀疑出血。单个 CT 扫描可能在 700 到 1,500 张切片（图像）之间，如果您怀疑出血，您必须在该系列中找到它。

法德尼斯说：“我们尝试定位问题所在，然后量化宽度、体积或表面积，并描述该特定组织的疾病状态。”“然后我们在辅助图像上创建可视化效果，以显示 AI 算法的发现。这使得 AI 更加清晰，因此临床医生可以返回原始图像，查看切片并了解实际情况。”

法德尼斯说，除其他外，这有助于临床医生识别可以转诊的患者，这已经在患者成功治疗结果方面产生了巨大差异。“想象一下，得知您有 24 小时的时间将患者从农村环境转诊到您可以进行干预、清除血栓并仍然能够挽救该患者重要功能的更全面的中风中心，”他说。

### 原始架构需要改进

RapidAI 的旗舰产品可作为平台和移动应用程序使用，结果通过该应用程序和其他渠道（如电子邮件）分发。移动应用程序具有内置的工作流和通信功能，因此中风团队内的临床医生可以互动并共享图像。

该系统已部署在 100 个国家/地区的约 2,250 家医院中。目前，它每天处理约 14,000 次扫描，扫描量每年增加 30%。随着公司扩展到新产品，这一数字可能会增长得更快。法德尼斯说：“我们的路线图上有产品，我们的扫描量可能会高出 10 倍。”

原始架构基于每个医院数据中心中运行 AI 算法的本地服务器。RapidAI 一直拥有云足迹来将结果分发到移动设备，但所有处理都在本地完成。虽然 RapidAI 拥有服务器，但每家医院的 IT 团队都控制着服务器部署的环境，包括园区网络和医院周边的防火墙。

此外，管理基础设施是一项重大挑战。由于他们缺乏自动化和集中管理，因此要执行系统升级，他们需要 VPN 访问或向医院派遣现场工程师——这两者都会增加成本并限制更新的频率。

### RapidAI 的软件堆栈和边缘到云架构
**解决问题**

为了解决这个问题，RapidAI 开发了其声称是医疗行业中唯一一个边缘到云平台。Phadnis 说，这为他们带来了三个关键优势。

“首先，它允许我们在边缘和云上支持 AI 模型的处理。其次，我们可以在云上和本地并行运行多个算法，而之前我们必须按顺序逐个运行它们。第三，从网络安全角度来看，在发生网络事件时，我们可以动态地从云端拉回本地，反之亦然，”他说。

新架构还可以与第三方算法集成，并通过相同的工作流对它们进行指导。

Phadnis 强调，提供如此关键的医疗服务使业务连续性至关重要；例如，您不希望由于操作系统升级而导致诊断延迟。“使用 [Palette](https://docs.spectrocloud.com)，我们可以监控云端和本地的一切，”Phadnis 说。“而且，我们可以通过单击一下，无缝地自动化部署并升级整个堆栈——从操作系统到我们领域中的所有算法——而不会影响患者护理。鉴于部署规模，这对我们的客户和运营团队来说绝对至关重要。”

**隐私和连续性**

从软件角度来看，该公司使用广泛的语言。“我们所有的云处理都在 Go 中，但我们已经使用了从 Python 到 C++、Java、JavaScript 和 TypeScript 的所有内容，以及 iOS 移动端的 Swift，”Phadnis 解释说。

完整的系统，包括 AI 算法，使用 [Docker](https://www.docker.com/?utm_content=inline-mention) 和 [Kubernetes](https://thenewstack.io/kubernetes/) 完全容器化，并使用 [Spectro Cloud Palette](https://www.spectrocloud.com/) 部署和管理堆栈。他们出于多种原因选择 Spectro 而非其竞争对手。“我们对 Spectro 团队的质量印象深刻，”Phadnis 说。“他们的解决方案很全面，特别适合我们在医疗保健中的用例。”

为了防止 [与硬件相关的停机](https://thenewstack.io/for-robust-edge-computing-plan-for-the-what-ifs/)，Spectro Cloud 形成一个三节点或五节点 Kubernetes 边缘集群，该集群可以容忍一个或多个节点中的硬件故障。Spectro Cloud 可以支持物理设备和虚拟设备外形，尽管 RapidAI 仅使用后者。

在集群中，任何更新都会滚动进行，其中单个节点会连续分离并升级，然后再重新加入集群。他们维护一个 A/B 分区，其中 A 分区上运行着以前的 operating system 和 Kubernetes 版本。“当我们升级时，我们将新版本放在 B 分区并更改启动顺序，” [Tenry Fu](https://www.linkedin.com/in/tenryfu/)，Spectro Cloud 的首席执行官兼联合创始人解释说。“因此，如果由于某种原因该更新失败，系统将自动回滚并在 A 分区上重新启动。这有效地维护了一个‘最后已知良好状态’。”

为了监控集群，Spectro Cloud 在边缘集群中内置了一个指标代理，该代理会定期收集所有系统运行状况信息。它也是可定制的。“RapidAI 最大的问题之一是磁盘空间不足，”Fu 解释说。“因此，当他们的可用磁盘空间达到某个阈值时，他们需要收到警报。”

RapidAI 处理的数据从隐私的角度来看极其敏感，而且法规因司法管辖区而异。“我们部署的每个系统都有不同的受保护健康信息 (PHI) 策略，规定哪些信息可以上传到云端，哪些信息可以推送到移动设备，等等，”Phadnis 说。

“我们有配置，其中有一个能力中心，其中有一个 Rapid 服务器，可以满足四到五家医院的需求。配置因能力中心或医疗保健系统以及因地点而异。我们必须能够在全球范围内监控和控制该配置，这是一个非同小可的问题。Spectro Cloud 团队一直在帮助我们达到这样的地步：我们有一个单一的控制面板，我们可以通过它监控我们的整个基础设施。”

医疗保健受到严格监管，RapidAI 已在 66 个不同的国家获得批准，并在 100 个国家部署。然而，这意味着它不能使用扫描数据来持续改进算法，即使在技术上是可行的。“我们与 FDA 的关系非常好，但从监管或 FDA 的角度来看，你不能动态更新现场算法并直接部署它，”Phadnis 说。“如果临床适应症有任何变化，可以理解的是需要重新批准。”

**满足未来需求**

为了进一步加强其安全故事，Spectro Cloud 团队正在努力在边缘实现最先进的安全性。2023 年，他们与英特尔合作发表了一篇白皮书，内容是
**安全边缘原生架构**（[https://www.spectrocloud.com/news/spectro-cloud-launches-the-secure-edge-native-architecture-sena](https://www.spectrocloud.com/news/spectro-cloud-launches-the-secure-edge-native-architecture-sena)）为 x86 架构提供端到端加密和安全性。“这涵盖了如何处理安全设备注册、[安全启动](https://thenewstack.io/honey-i-secured-your-boot-edge-trusted-boot-with-kairos)、防篡改静态加密、内存中加密和安全更新，”傅说。该公司目前还与英特尔、高通和英伟达合作，为基于 ARM 的系统提供相同级别的支持。

Spectro Cloud 的傅坚信

**人工智能处理**（[https://thenewstack.io/edge-ai-how-to-make-the-magic-happen-with-kubernetes/](https://thenewstack.io/edge-ai-how-to-make-the-magic-happen-with-kubernetes/)）将越来越多地转向边缘，他认为这是他公司的优势所在。“在边缘站点直接生成了大量数据——在医院，由 CT 扫描仪或 MRI 机器生成——从性能角度来看，将所有内容发送到云端进行处理并不经济，”他说。

“你必须让计算离数据更近，这样你才能更快地处理它。所有新应用程序和人工智能工作负载都需要 Kubernetes，有时它们需要 Kubernetes 集群来实现高可用性。边缘的 Kubernetes 与集中管理功能相结合成为一个有趣的组合。我们还拥有本地人工智能功能，我们正在不断改进——例如，能够运行分布式推理并减少对 GPU 的依赖。”

RapidAI 正在继续加强其产品组合，并向新地区扩张。该公司在血管疾病方面拥有丰富的经验，因此可以扩展到多种急性和非急性疾病状态，例如肺栓塞和动脉瘤。它还看到制药行业临床试验对其技术的需求不断增长。

“我们的目标非常明确，”Phadnis 说。“我们的员工非常清楚，他们花掉的每一分钟都在拯救某人的生命。由于 Rapid 的结果，我们已为超过一百万患者推荐了挽救生命的程序，并且这个数字还在不断增加。”

*详细了解 * *RapidAI 的研究* *，以加速和改善中风护理，以及 * *Spectro Cloud 的解决方案* *，用于管理边缘的 Kubernetes 基础设施和应用程序。*

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。