<!--
title: SpaceX设计了轨道版Vera Rubin，辐射挑战紧随其后
cover: https://cdn.thenewstack.io/media/2026/08/5a1dc2db-hqf-xdqx0aampts.jpeg
summary: SpaceX与Nvidia正合作开发轨道版Vera Rubin NVL72 AI平台，计划于2027年发射。该项目旨在将地面AI数据中心架构引入太空，面临真空环境下的散热及严苛的抗辐射设计挑战，其核心在于如何在高密度计算与空间环境复杂性之间取得平衡。
-->

SpaceX与Nvidia正合作开发轨道版Vera Rubin NVL72 AI平台，计划于2027年发射。该项目旨在将地面AI数据中心架构引入太空，面临真空环境下的散热及严苛的抗辐射设计挑战，其核心在于如何在高密度计算与空间环境复杂性之间取得平衡。

> 译自：[SpaceX designed an orbital Vera Rubin. Radiation comes next.](https://thenewstack.io/spacex-nvidia-orbital-ai/)
> 
> 作者：Steven J. Vaughan-Nichols

**SpaceX和Nvidia表示，他们正在进行改造**，将Vera Rubin NVL72机架式AI平台用于轨道环境，SpaceX计划在2027年第四季度进行首次发射。

[太空AI数据中心](https://thenewstack.io/spacex-and-nvidias-orbital-ai-datacenter-fantasy/)的梦想，随着SpaceX和Nvidia在8月24日宣布，用于近地轨道（LEO）[Starmind](https://www.spacex.com/spacexai/starmind) AI卫星的平台将基于[Vera Rubin NVL72](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)芯片家族和架构而继续延续。

这一拟议中的系统将构成[SpaceXAI第一代Starmind AI卫星的计算核心](https://blogs.nvidia.com/blog/vera-rubin-lpx-spectrum-x-nvlink-fusion/#spacexai-vera-cpus)，并将Nvidia的架构从地面AI数据中心扩展到太空。

SpaceX首席执行官Elon Musk当天在X上发布消息称：“SpaceX与Nvidia合作，设计了一种针对太空优化的Vera Rubin NVL72系统，计划于明年第四季度发射入轨，并在2028年实现大规模部署。”

在Musk发帖之前，他曾在[SpaceX的2026年第二季度财报电话会议上表示](https://s21.q4cdn.com/184289198/files/doc_financials/2026/q2/SpaceX-Q2-2026-Earnings_Transcript-FINAL.pdf)：“展望未来，我们决定完全基于Nvidia构建，因为我们认为Vera Rubin架构是最好的架构。”Musk继续说道：“这并非什么遥远的未来之事；我们预计明年开始发射。我们认为NVL72 VR计算机的设计比传统的机架式设计要好得多。因此，我们预计将其部署在地面以及轨道上，因为我们认为这将是对标准NVL72机架的根本性简化。它的成本更低，效率更高。如果我们打算把它送入太空，为什么不把它也用在地面上呢？我认为这会非常酷。”

在地球上，[Vera Rubin NVL72](https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents/)是Nvidia的机架式AI设计，它结合了72个Rubin GPU和36个Vera CPU，以及诸如ConnectX-9 SuperNIC等高速网络组件。Nvidia表示，SpaceXAI计划中的Starmind卫星将基于该系统的优化版本。

> 传统的NVL72机架假设存在重力、技术人员、稳定的电网电力、建筑规模的液体循环系统以及频繁的故障部件更换。而轨道环境消除了所有这些假设。

这个想法比在航天器上放置一个传统的边缘AI加速器更具雄心。Nvidia和SpaceXAI提议将AI数据中心中使用的改良架构带入轨道，同时根据轨道运行要求进行改造。

然而，在轨道上实现这一点说起来容易做起来难。

正如[Kingy AI](https://kingy.ai/)的创始人[Curtis Pyke](https://www.linkedin.com/in/curtis-pyke-4b52a420/)所写：“传统的NVL72机架假设存在重力、技术人员、稳定的电网电力、建筑规模的液体循环系统以及频繁的故障部件更换。[轨道环境消除了所有这些假设。](https://kingy.ai/blog/spacex-nvidia-orbital-ai-supercomputer-2027/)”

> “散热是无情的。太空很冷，但真空无法通过对流带走热量。”

特别是，Pyke继续说道：“散热是无情的。太空很冷，但真空无法通过对流带走热量。热量必须从芯片传导到散热器表面，然后以红外辐射的形式离开。SpaceX表示，AI1可以省去冷水机组、冷却塔和风扇，并将冷却开销降低一个数量级。”

SpaceX解释说，AI1将改为在航天器内部使用闭环液体冷却，并使用大型可展开散热器将热量直接以红外辐射的形式散发到太空中。虽然所声称的减少在理论上是物理上合理的，但目前还没有证据表明这些AI卫星的冷却系统能够达标。

另一个悬而未决的重大问题是，如何使轨道机架具备抗辐射能力。使Vera Rubin NVL72具备抗辐射能力，远不止是将普通的NVL72机架放入屏蔽卫星外壳中那么简单。它需要围绕特定的轨道和任务寿命，对GPU、CPU、内存、网络、电源、冷却、固件和操作进行系统级的重新设计。

近地轨道并非良性环境。[NASA指出，500公里以下低倾角近地轨道航天器的典型捕获粒子剂量率为每年100至1,000 rad(Si)](https://llis.nasa.gov/lesson/824)。这种辐射水平对电子设备来说不是立即的死亡判决，但在多年的任务中会导致累积退化。[抗辐射航天硬件](https://spacenexus.us/blog/radiation-hardening-space-electronics-strategies-trade-offs)可以应对这种情况。而商用现成（COTS）电子设备则是另一回事。真正的抗辐射Rubin GPU还需要在晶体管和电路层面进行设计变更。

即使Nvidia制造了这样的芯片，对于像SpaceX设计这样的高密度AI系统，担忧的不仅仅是单个处理器是否能在5年或10年的剂量下存活。卫星包含许多对辐射敏感的元件，例如GPU逻辑、SRAM缓存、寄存器文件、系统内存和内存控制器。拥有数千个核心和数十亿个存储单元，总体故障率——而不是单个组件的行为——决定了设计。

最现实的短期答案将是一个抗辐射、具备故障管理能力的Rubin衍生轨道系统，而不是传统军事航天意义上完全抗辐射的NVL72。它可能会使用经过挑选的Nvidia商用部件、充足的屏蔽措施、ECC（纠错码）和数据完整性机制、冗余控制器和电源路径、主动故障检测、软件恢复以及性能降低的操作模式。