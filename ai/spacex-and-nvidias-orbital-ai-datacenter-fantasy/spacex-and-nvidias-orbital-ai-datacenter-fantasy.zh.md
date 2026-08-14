太空AI数据中心听起来很棒，但从实际角度来看，它们几乎是不可能实现的。

对于科技狂热者来说，这听起来确实很不错。两家最热门的科技巨头 [SpaceX](https://www.spacex.com/) 和 [NVIDIA](https://www.nvidia.com/en-us/) 正在合作，利用刚刚宣布的 [Starmind AI1 卫星](https://www.spacex.com/spacexai/starmind) 将 AI 数据中心送入太空。

这些 30 米高、拥有 75 米太阳能电池阵列翼展的卫星，将搭载最新的 NVIDIA Vera CPU 和 Rubin GPU。它们将驻留在距离地球约 600 公里的近地轨道（LEO）上。在网络方面，它将使用 Starlink 的激光链路。SpaceX 表示，首颗 AI1 航天器将在轨道上执行局部 AI 计算，并通过 Starlink 将结果中继回地球。

据 SpaceX 称，AI1 的设计围绕着峰值功率为 250 kW、平均功率为 175 kW 的计算负载。与需要频繁建设新发电厂的地面竞争对手不同，它将依靠太阳能供电。

![](https://cdn.thenewstack.io/media/2026/08/ba299be7-starmind-ai1-satellite-1024x425.jpeg)

来源：SpaceX。

Starmind 不仅仅是一个发射到轨道的传统 NVIDIA AI 集群。这项工作依赖于将高密度加速器硬件与能够发电、排出废热、抵御辐射、维持激光通信并能大规模生产的航天器平台集成在一起。这些都不是易事。

一旦进入轨道（这将需要 SpaceX 尚未完全准备好投入使用的 Starship 火箭来发射预计 2.3 公吨重的卫星），这些卫星将协同工作。

最终，为了实现 [SpaceX 拥有百万颗（这不是笔误，真的是一百万颗）Starmind 卫星的目标](https://www.fcc.gov/document/sb-accepts-filing-spacexs-application-orbital-data-centers)，两家公司需要设计一种标准化的航天器模型。这些卫星将在 SpaceX 位于德克萨斯州巴斯特罗普县（Bastrop County）的 1100 万平方英尺制造园区——[Gigasat 工厂](https://www.kvue.com/article/tech/science/aerospace/spacex-plans-gigasat-factory-manufacture-ai-satellite-data-centers-bastrop-county-texas/269-bed7c221-ad0c-4171-9a7f-eeb483d9cad7)中建造，该工厂目前仍在建设中。

这一太空 AI 提案是 SpaceX 首席执行官 Elon Musk 将能源密集型 AI 基础设施置于轨道上的梦想中最雄心勃勃的一个。在那里，这些卫星无需与日益紧张的地面数据中心建设争夺土地、电网容量或水资源。

然而，SpaceX 对将这一愿景变为现实所涉及的技术问题避而不谈。

## 太空数据中心的冷却

让我们从最令人头疼的问题开始：冷却。

与你从糟糕的科幻电影中可能产生的想法相反，太空的真空本身并不寒冷。物体的表面是热还是冷，完全取决于它是否面向太阳。面向太阳的一面会升温，而背向太阳的一面最终会冷却到深空的 3 开尔文背景温度。

关键词是“最终”。你不能简单地使用对流、冷却塔或蒸发冷却来带走热量。热量必须以红外辐射的形式散发出去，这是一个非常缓慢的过程。

物理学在计算能力、散热器面积、航天器质量和工作温度之间造成了直接的权衡。一个运行数百千瓦 AI 硬件的系统必须将几乎所有的功率作为废热排出。液体冷却可以将热量从芯片上带走，但它并不能消除对大面积散热表面的需求。

正如 NASA 所发现的那样，“[卫星在轨道上经历了严酷的环境](https://ntrs.nasa.gov/api/citations/20230003714/downloads/Thermal%20Design%20for%20Spaceflight.pptx.pdf)”，温度范围从全日照下的约 393 开尔文（248 华氏度）一直到约 3 开尔文（-454 华氏度）。

为了冷却 Starmind 卫星，每一颗都将拥有一个可展开的液体散热器系统，测量面积为 160 平方米。什么液体？我们尚不清楚。伯明翰大学航天学教授 [Hugh Lewis](https://research.birmingham.ac.uk/en/persons/hugh-lewis/) [预计它将使用氨](https://www.pcmag.com/news/spacexs-orbiting-data-centers-will-use-liquid-cooling-but-dont-expect-water)，这在[国际空间站（ISS）上已经在使用](https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf)。这种方案能否可靠地扩展到具有巨大热量的数据中心级 AI 部署中，还有待观察。

## 轨道上的网络限制

另一个问题是它的网络。该架构严重依赖 Starlink 的光学星间链路。SpaceX 表示，AI1 卫星将使用高速激光链路与其他航天器通信，并通过 Starlink 网络将 AI 结果发送到地球。

Starlink 已发布的技​​术规范描述了在长达 4000 公里的距离上运行速度高达 25 Gbps 的微型激光终端，而 SpaceX 称其客户服务的延迟约为 25 毫秒。

这些数据表明，这是一个对于分发推理结果、传输模型更新、连接轨道传感器到计算节点以及避免对地面站通道的依赖来说可能很有用的网络。但它们并不能证明卫星星座可以像地面 AI 超级计算机紧密耦合的网络架构那样运作。

我们不会看到太空中的大规模机器学习和训练。这需要巨大的、可预测的带宽以及用于 GPU 到 GPU 通信的极低延迟。轨道网络还将面临物理传播延迟、激光链路捕获和切换、跨移动星座的路由以及每颗航天器可用容量的限制。

## 碎片、战争和太阳风暴

据长期关注太空的知名人士 [Doug Mohney](https://www.linkedin.com/in/dougmohney/) 称，另一个问题是碎片。“在倒霉的一天，一块随机的垃圾撞上了一颗卫星，它分裂成多块弹片，撞击了另一颗卫星，以此类推，直到你引发一场 [凯斯勒现象（Kessler event）](https://aerospaceamerica.aiaa.org/features/understanding-the-misunderstood-kessler-syndrome/)，将选定的轨道变成一团游荡的碎片云。”

凯斯勒现象是指当一颗卫星解体，其碎片撞击另一颗卫星，以此类推，直到一片近地轨道区域充满了残骸，而不是可用的卫星。

![](https://cdn.thenewstack.io/media/2026/08/5323dd86-kesler-event-1024x786.jpg)

凯斯勒现象可能的样子。来源：ESA。

雪上加霜的是，凯斯勒现象可能并非偶然发生。Mohney 还观察到太空战争是一个现实的威胁：“像俄罗斯、中国、伊朗或朝鲜这样的不良行为者可以使用动能（非随机垃圾！）手段来针对一颗或多颗卫星，从而产生太空碎片。” 或者，“一枚好的核武器使用电磁脉冲可以一次性摧毁所有卫星。俄罗斯和中国（以及美国）已经拥有反卫星（ASAT）武器计划。朝鲜可能拥有反卫星能力，但核武器将确保轨道能力的彻底毁灭。”

如果这听起来很疯狂，请记住 Starlink 卫星已经被乌克兰使用，而 [俄罗斯一直在试图阻止它们的传输](https://www.reuters.com/business/aerospace-defense/russia-tries-jam-musks-starlink-systems-counter-ukrainian-drones-2026-07-08/)。也有可靠的报道称 [俄罗斯正在开发专门用于击落 Starlink 卫星的反卫星武器](https://apnews.com/article/russia-starlink-musk-ukraine-space-china-canada-c69c1fda5ffc93828712ab723e606a2c)。更大、更脆弱的 Starmind 卫星将更加脆弱。

Mohney 还担心太空天气这个“已知的未知数”。

“一场袭击地球的太阳耀斑，如果程度达到 1859 年的 [卡林顿事件（Carrington Event）](https://spacedaily.com/sd-in-1859-a-solar-storm-now-called-the-carrington-event-induced-currents-so-strong-in-north-american-telegraph-lines-that-operators-disconnected-their-batteries-and-kept-sending-messages-on-the-geoma/)（这是记录在案的最大太阳风暴），将摧毁所有卫星的轨道电子设备。” 这反过来，随着失控的卫星偏离轨道，可能会导致凯斯勒现象。较小的事件已经将近地轨道卫星推离了太空。例如，[2022 年 2 月的地磁风暴迫使 38 颗刚发射的 Starlink 卫星脱离轨道](https://repository.library.noaa.gov/view/noaa/53091)。

## 1700 亿美元的问题

还存在商业担忧。尽管新建和扩建的地面 AI 数据中心面临诸多障碍，但能源分析公司 [Wood Mackenzie](https://www.woodmac.com/) 认为，“一个假设的 1 GW 轨道数据中心估计耗资 1700 亿美元，是同等地面设施的三倍多，其中发射和卫星成本占总额的约 60%。要使轨道成本与地面替代方案持平，需要降低 70% 的成本。”

该公司认为这可能是可能的，但 Wood Mackenzie 研究总监 [Robert Liew](http://linkedin.com/in/robert-liew-sg?originalSubdomain=sg) 指出：“如果没有在发射成本上持续且巨大的进步，这个差距就无法缩小。我们预测 2024 年到 2040 年间地面数据中心的投资将达到 9 万亿美元。这就是资本首先要去的地方。轨道数据中心是一个严肃的长期命题，但目前它们仍然是对成本曲线的押注。”

目前，SpaceX 提供了一个广泛的技术愿景和与 NVIDIA 的硬件合作伙伴关系，但几乎没有提供可以建立商业可行性的运营指标。真正的考验将是 SpaceX Starship 是否能成为一种实用的运载火箭，并能否克服其冷却和安全问题。然后，AI1 还必须证明其每公斤、每千瓦、每平方米散热器和每美元发射成本所产生的可用计算能力，足以超越或补充地面 AI 基础设施。我认为这在短期内不会发生。