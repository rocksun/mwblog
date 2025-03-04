
<!--
title: 边缘战争升温，Arm旨在超越英特尔和高通
cover: https://cdn.thenewstack.io/media/2025/02/53e2e33e-getty-images-uyhsmgcshs8-unsplash-1-1.jpg
-->

> 译自：[Edge Wars Heat Up as Arm Aims to Outflank Intel, Qualcomm](https://thenewstack.io/edge-wars-heat-up-as-arm-aims-to-outflank-intel-qualcomm/)
> 
> 作者：Jeffrey Burt

Arm 的 v9 平台通过数十亿参数的 AI 模型、微控制器的消除以及与领先框架的无缝集成，重新定义了边缘计算，为将 AI 推向极致边缘的开发者提供了支持。

芯片设计公司[Arm](https://www.arm.com/) 推出了一个新的[边缘 AI](https://thenewstack.io/edge-ai-how-to-make-the-magic-happen-with-kubernetes/) 平台，该平台针对[物联网 (IoT)](https://thenewstack.io/edge-computing/) 进行了优化，扩展了可在边缘设备上运行的 AI 模型的规模，包含一个强大的新 CPU，并使开发人员能够更轻松地与流行的 AI 框架集成。

这是该公司首个基于 v9 架构的此类平台，其性能数据包括：与 Arm 此前的平台相比，[机器学习](https://thenewstack.io/use-these-tools-to-build-accurate-machine-learning-models/) 性能提高了八倍，[物联网](https://thenewstack.io/enabling-ai-in-iot-apps-with-a-cloud-to-edge-database/) 性能提高了 70%。

Arm 的新平台标志着本周至少第三家芯片厂商采取行动，以扩大其在[边缘](https://thenewstack.io/what-the-heck-is-the-edge-and-why-should-you-care/) 的影响力。目前，业界正努力将尽可能多的计算能力、AI 功能、数据处理和分析工具以及安全功能带到当今大部分数据创建的地方。

![](https://cdn.thenewstack.io/media/2025/02/e636c22d-arm-platform-1-1.png)

*Arm 平台*

Arm 物联网业务部门高级副总裁兼总经理 Paul Williamson 告诉记者：“只有将 AI 部署到物理设备及其周围的环境中，我们才能实现 AI 的潜力。”“在物联网世界中，边缘 AI 最重要。几年前，边缘 AI 工作负载比今天简单得多。例如，它们专注于基本的降噪或异常检测。但现在工作负载变得更加复杂，它们试图满足更复杂用例的需求。”

## 边缘竞争日益激烈

[英特尔](https://www.intel.com/content/www/us/en/homepage.html) 本周推出了其至强 6 处理器系列的最新产品，[包括一款面向边缘和网络中 AI 工作负载的片上系统 (SoC)](https://thenewstack.io/edge-computing-gets-supercharged-with-intels-new-soc/)，该系统具有集成的加速、连接和安全技术，使更多工作负载能够在更少、更小的系统上运行。

[高通](https://www.qualcomm.com/) 以其用于智能手机和平板电脑的骁龙系列节能芯片而闻名，它推出了一个新的产品品牌组合——[Dragonwing](https://www.qualcomm.com/dragonwing)——用于工业和嵌入式物联网、网络和蜂窝用例，范围从能源和公用事业到零售、制造、电信和供应链。

高通高级副总裁兼首席营销官 Don McGuire [在一篇博文中写道](https://www.qualcomm.com/news/onq/2025/02/unveiling-the-qualcomm-dragonwing-brand-portfolio)：“领先的边缘 AI、高性能、低功耗计算和无与伦比的连接性都内置于定制的硬件、软件和服务产品中，这些产品旨在实现速度、可扩展性和可靠性。”

这一切在很大程度上是由企业采用边缘和物联网驱动的，连接的设备范围从制造车间的庞大工业系统和偏远油井上的小型服务器到自动驾驶汽车、风力涡轮机上的小型传感器以及介于两者之间的所有设备。据估计，这些设备的数量正在增长，从去年的 180 亿增长到[2033 年的 396 亿](https://www.statista.com/statistics/1183457/iot-connected-devices-worldwide/)。

## 强大且节能

芯片制造商正在构建更强大且更节能的 CPU、GPU 和 NPU（神经处理单元），以便在硬件制造商的小型且功能更强大的系统中运行，以满足对更多计算、数据处理和安全功能的快速增长的需求，这些功能在数据创建的地方运行，以减少将大量数据发送到云端带来的延迟和成本。现在，AI 模型和工作负载正在进入边缘，所有这些都促使开发人员为边缘开发 AI 和其他软件。

Arm 的 Williamson 表示：“我们看到需要更高的性能和更好的效率来运行最新的 AI 模型、框架和代理。”“我们看到需要改进安全性以保护围绕这些软件的高价值软件。我们还看到开发人员需要能够在软件部署到现场后对其进行更新、改进和升级。”

在工业自动化、智慧城市、智慧家居等用例中，“边缘 AI 推理的价值越来越明显，”他说。
## 进入新的Cortex-320 CPU

Arm新的v9平台旨在解决其中许多问题，从而能够在设备上运行具有超过10亿个参数的AI模型。它包括设计师新设计的、高效的Cortex-A320 CPU和Ethos-U85边缘加速器，以及性能增强工具，例如用于机器学习作业的标量向量扩展(SVE) 2、对新数据类型BFloat16的支持以及用于更高效AI处理的矩阵乘法指令。

Armv9.2架构还更好地解决了边缘计算的关键安全问题。其功能包括指针认证(PAC)、分支目标识别(BTI)和内存标记扩展(MTE)，这些功能能够提高内存安全性、控制流完整性和软件隔离性。

![](https://cdn.thenewstack.io/media/2025/02/740cad73-arm-compute-security-1.png)

*Arm 计算安全*

“这不仅仅是向前迈出的一小步，”Williamson说。“它代表了我们处理边缘计算和AI处理方式的根本转变。我们相信这将推动未来几年的边缘AI革命。”

## 走一条更直接的路线

关键在于最新的平台消除了对微控制器的需求，他补充说，去年的解决方案“专注于转换网络执行。今年，我们采用了Ethos-U85，并对其驱动程序进行了更新，以便它可以直接由Cortex-A320驱动，而无需循环使用Cortex-M。这将改善延迟，并允许Arm的合作伙伴消除使用这些独立控制器来驱动NPU的成本和复杂性。”

![](https://cdn.thenewstack.io/media/2025/02/058d0d47-arm-direct-drive-1-1.png)

*Arm 直接驱动*

内存也是一个关键改进，Cortex-A320增加了对比Cortex-M平台更大的可寻址内存的支持。CPU在处理多层内存访问延迟方面也更加灵活，使平台能够处理具有更大神经网络并需要软件灵活性的边缘AI用例。

“对能够高效执行更大规模和多模型网络的硬件的持续需求正在推动内存大小需求，因此，具有更好内存访问性能的系统正变得非常必要，才能执行这些更复杂的用例，”他说。

## 开发者获得更多选择

对于软件开发者来说，灵活是关键词。多年来，Arm一直在[构建物联网开发平台](https://thenewstack.io/enabling-ai-in-iot-apps-with-a-cloud-to-edge-database/)，去年继续推出[Kleidi](https://newsroom.arm.com/blog/arm-kleidi)，旨在利用Arm的CPU架构加速AI开发。该程序的首批产品是用于AI框架的KleidiAI库和用于计算机视觉作业的KleidiCV。v9平台带来了用于物联网的Kleidi。KleidiAI已经集成到像Llama.ccp和ExecuTorch这样的物联网框架中，以加快[Meta的Llama](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/)和[微软的Phi-3](https://thenewstack.io/copilot-pcs-understanding-microsofts-evolving-ai-pc-stack/)等模型的性能。

据Arm称，在Llama.ccp上运行微软的Tiny Stories数据集时，它为Cortex-320带来了高达70%的性能提升。

此外，Cortex-A320可以运行使用实时操作系统的应用程序，例如Free RTOS和Zephyr，Williamson说。也就是说，通过Arm的A型架构，它也提供了对Linux的开箱即用支持以及对Android和其他丰富的操作系统的可移植性。

![](https://cdn.thenewstack.io/media/2025/02/a7e4d797-arm-developers-1.png)

*Arm 开发者*

“这带来了前所未有的灵活性，并允许您定位我们的合作伙伴提供的多个细分市场、应用程序或操作系统产品，并在考虑未来产品路线图时为您提供极佳的选择，”他说。“对于使用Linux的开发者来说，他们可以轻松快速地在A320上部署这个丰富的操作系统。这将节省他们的时间、金钱和精力，从而加快他们及其产品的上市时间。”

开发者可以采用高级环境中的[PyTorch](https://thenewstack.io/why-pytorch-gets-all-the-love/)应用程序，并通过Cortex-A320 CPU中的加速功能将其部署到边缘。

“我们还允许通过将神经处理器直接连接到A类内核，首次使他们能够直接寻址与AI加速器相同的内存系统，用于这类始终在线的任务，这也会使开发更容易，”Williamson说。

有了这一切，“您将看到一些有趣的、全新的配置，人们正在突破以前在微控制器中所能做到的界限，同时也为基于Linux的开发者提供优化的性能，”他说。
