<!--
title: Arm通过Cortex-M52芯片将AI引入到最小的物联网设备中
cover: https://cdn.thenewstack.io/media/2023/11/b9fb22f1-alexandre-debieve-fo7jilwjotu-unsplash-e1700666642495-1024x683.jpg
-->

借助最新设计的Cortex-M52芯片，Arm使边缘端最小物联网设备也能实现AI计算.

> 译自 [Arm Pushes AI into the Smallest IoT Devices with Cortex-M52 Chip](https://thenewstack.io/arm-pushes-ai-into-the-smallest-iot-devices-with-cortex-m52-chip/)，作者 Jeffrey Burt 已经当记者30多年了，其中20多年都在报道科技新闻。在eWEEK工作超过16年，之后以自由科技记者的身份，他报道的范围涉及从数据中心基础设施和协作技术到人工智能、云计算、量子计算、网络安全和渠道合作。

如今人工智能无处不在，但它真正需要应用的地方是边缘计算的最深处，那里[物联网(IoT)](https://thenewstack.io/the-internet-of-things-on-the-edge/)设备正在生成大量的数据，这些数据需要分析，那里可以收集并采取预测性的洞察力，并且可以运行经过机器学习优化的计算。

Arm 的 IoT 业务线高级副总裁兼总经理 [Paul Williamson ](https://www.linkedin.com/in/paulwilliamson/)说：“只有到那时，我们才能真正扩展 IoT，并推动我们认为存在的进一步创新和部署。但开发人员面临挑战。他们需要扩展其平台的硬件功能，但也需要一个简化的软件开发平台。”

[Arm](https://thenewstack.io/is-arm-architecture-the-future-of-cloud-computing/) 称正在通过其新的 Cortex-M52 提供这一平台，这是该芯片设计公司面向最小 IoT 和嵌入式设备的低成本和高能效 Cortex-M 微控制器系列的最新补充，Williamson 在一次记者简报会上向记者表示。

他说：“人工智能的进步与连接技术的普遍性的交汇意味着在小型和敏感成本的设备中可以实现局部智能，并且它们可以变得更加智能和更加强大。由于对云的依赖较少，这些设备可以以极大的隐私和可靠性运行。”

Williamson 还表示，“为了实现这一机会，芯片提供商和开发人员需要访问更多 AI 能力，以提供小型嵌入式设备典型的成本和功耗受限区域所需的智能。”

## 快速增长的 AI-in-IoT 市场

随着组织转向人工智能和机器学习来理解这些设备(现在有大约150亿个IoT设备)生成的数据，AI-in-IoT领域是一个快速增长的空间。Pragma 市场研究预计这个市场细分，去年产生了103亿美元，到[2032年将增长到917亿美元](https://www.linkedin.com/pulse/ai-iot-market-size-share-growth-analysis-trends-2030-shrivastav/)。

Enderle集团的首席分析师[Rob Enderle](https://www.linkedin.com/in/rob-enderle-03729/)告诉The New Stack："这是IoT成功的核心，那就是尽量把更多的智能放到端点中，以减少相关云服务的负载，但它必须非常高效，因为端点中通常有非常少的电力可用，包括电池，有时是太阳能。"

Arm构建Cortex-M52以包含公司的Helium技术，这是Armv8.1-M架构的扩展，为机器学习和数字信号处理(DSP)应用程序带来了性能改进。通过Helium，Cortex-M52将为DSP和机器学习性能提供提升，而无需专用DSP或机器学习加速器，或者Arm Ethos神经处理单元(NPU)，这些可以在Arm的高端Cortex-M85和中端M55中找到。

## Helium 的优势

来自Helium的性能提升让开发人员能够部署更复杂的机器学习算法。Cortex-M52是通过Arm与Arm中国的工程团队合作创建的，为现在在Cortex-M4和M33上运行的工作负载提供了容身之处。

它为机器学习工作带来了5.6倍的性能提升，为DSP任务带来了2.7倍的性能提升，与以前的Cortex-M代相比，功耗降低了2.1倍。

硅片面积也减少了23%，这为在性能和成本之间进行权衡时给硅片制造商带来了更多选择。

在安全性方面，Cortex-M52使用最新的Armv8.1-M指针认证和分支目标识别(PACBTI)扩展和Arm的可信执行环境(TrustZone)技术。它还将帮助芯片制造商达到PSA 2级认证硅片要求，以创建PSA认证的[IoT设备](https://thenewstack.io/why-webassembly-is-perfect-for-tiny-iot-devices/)。

## 开发者得到统一的环境

对于开发人员来说，它打开了广泛的用例，包括振动、异常和关键词检测以及传感器融合。

Enderle说："它为优化IoT解决方案提供了更多选择。"

这款新芯片设计提供了统一的软件开发环境和Cortex-M工具链。其他Cortex-M芯片包含嵌入式代码、DSP代码和神经网络模型。所有这些都融入到Cortex-M52中的一个软件开发流程中，为程序员提供了一个更容易的开发路径，该路径与常见的机器学习框架和现有工具兼容。

![](https://cdn.thenewstack.io/media/2023/11/6cc1c9d3-arm-cortex-m52-unifed-development-e1700667452157-300x152.png)

Willamson说："开发人员可以使用单一语言针对通用API进行编码，在应用程序的DSP和ML元素中实现所需的性能提升。他们不需要了解底层处理器的特定硬件细节。"

软件开发人员需要DSP和机器学习性能来利用AI的作用。以前，这意味着使用CPU、DSP和NPU。

他说："这意味着他们将不得不建立硬件，一旦建立，他们可能不得不编写、调试和链接跨多个芯片或单个设计内多个处理器的代码，我可能需要三个独立的工具链、编译器、调试器，开发人员将不得不对跨多个处理器的事件的计时、内存访问和调度有非常深入的理解。一个非常复杂的任务。"

他说，芯片制造商已经拥有Cortex-M52，它将在明年开始出现在硅片上。

## 关注RISC-V

从英特尔、AMD和英伟达到越来越多的小公司在努力为物联网和嵌入式设备带来更多AI功能，但根据Enderle的说法，Arm的"潜在的大曝光来自[RISC-V](https://thenewstack.io/open-source-hardware-the-rise-of-risc-v/)，RISC-V一直在取得进展，使用ASIC代替这些处理器。"

大约10年前，RISC-V随着一个开源的芯片设计的出现[撞上了这一行业的景象](https://thenewstack.io/risc-v-finds-its-foothold-in-a-rapidly-evolving-processor-ecosystem/)，RISC-V国际正在开发这种芯片架构，可以作为x86和Arm的替代方案。这是RISC-V国际在最近的RISC-V峰会上提出的口号，推动RISC-V架构可以在任何设备中使用的理念，从物联网和云到PC和数据中心服务器。

它正在获得一些牵引力，苹果在其硅片中加入了控制器，Meta、AMD和高通等其他公司也在研究这种体系结构。

目前，Arm似乎处于有利地位。尽管RISC-V核心市场份额预计在未来几年内会有所增加，达到100亿个，但估计那时Arm已经输送了1000亿个Cortex-M设备。

然而，RISC-V带来了开发者和组织通过Linux和其他开源软件已经习惯的开放氛围。公司可以许可它，创建芯片自己的版本。

“它更便宜，支持者也更开放，”Enderle说。“许多ARM开发者已经或将切换到这项技术。高通和AMD也在研究这项技术。”

RISC-V开放、免费的本质也被中国所利用，这使该技术卷入了中美之间处理器的持续争议。美国立法者和拜登政府正在考虑限制那些希望向中国出口RISC-V技术的美国公司。

在与记者的问答环节中，Williamson避开了有关Cortex-M52可能是对中国对RISC-V日益增长的兴趣的回应的问题，他说Arm已经“多年来一直高度关注DSP和机器学习性能”，这是“下一步发展路线，将其带入性能更低、功耗更低、约束更多的设备中”。这是我们的一个长期关键开发重点。”

他还谈到了Arm相对RISC-V在合作伙伴和软件生态系统方面的显著优势，指出了Arm架构市场上的广泛功能，从最小的嵌入式设备到大型服务器，同时具有一致的库和工具。

“我们拥有强大生态系统合作伙伴投资于我们的工具的原因在于，他们知道，当他们生产一个工具时，然后它可以跨所有这些产品和市场区域部署的所有这些不同领域使用技术。”这对我们和我们的生态系统来说是一个非常有价值的事情......这种一致性存在着推动可扩展性。”

然而，虽然Enderle同意Arm在其生态系统方面处于领先地位，但RISC-V仍在努力建立其功能和合作伙伴关系，并引起了关注。

“最近对许可使用者的定价行动和诉讼使开发者对该平台感到害怕，而RISC-V则非常相似但没有这些包袱，”这位分析师说。
