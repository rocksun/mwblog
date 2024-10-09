
<!--
title: 人工智能与物联网的集成将代理带入物理世界
cover: https://cdn.thenewstack.io/media/2024/10/efc035ef-jorge-ramirez-1gldpzticru-unsplashb.jpg
-->

我们探讨了 SenseCAP Watcher 的硬件、软件架构和集成功能，重点介绍了其在 AI 开发人员中的用例。

> 译自 [Integration of AI With IoT Brings Agents to Physical World](https://thenewstack.io/integration-of-ai-with-iot-brings-agents-to-physical-world/)，作者 Janakiram MSV。

生成式人工智能和大型语言模型的兴起将对[物联网](https://thenewstack.io/what-does-it-mean-to-be-on-the-internet-of-things/) (IoT) 和[边缘计算](https://thenewstack.io/edge-computing/) 产生重大影响。随着[小型语言模型](https://thenewstack.io/how-to-get-started-running-small-language-models-at-the-edge/) 和[设备上模型](https://thenewstack.io/google-wants-developers-to-build-on-device-ai-applications/) 的发展，边缘计算开始利用人工智能。开发人员现在可以将传感器、运行设备上模型的边缘设备以及运行在云端的[多模态人工智能模型](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/) 相结合，构建创新的解决方案。这种方法与[代理工作流](https://thenewstack.io/semantic-router-and-its-role-in-designing-agentic-workflows/) 相结合，将自动化提升到一个新的水平。

这种创新的早期例子之一是[SenseCAP Watcher](http://seeedstudio.com/watcher)，这是由[Seeed Studio](https://www.seeedstudio.com/) 开发的一种创新的物理人工智能代理，旨在增强智能环境的能力。它结合了物联网、边缘计算、设备上模型以及运行在云端（或数据中心）的多模态人工智能模型来运行代理工作流。

![](https://cdn.thenewstack.io/media/2024/10/501009d0-sensecap-watcher.jpeg)

本文探讨了 SenseCAP Watcher 的硬件、软件架构和集成功能，同时重点介绍了它对人工智能开发人员的潜在用例。

## 硬件概述

SenseCAP Watcher 凭借其全面的硬件设计而脱颖而出。它包含多个关键组件，这些组件协同工作以提供直观的用户体验。

Watcher 的核心是 [OV5647 摄像头模块](https://www.seeedstudio.com/OV5647-69-1-FOV-Camera-module-for-Raspberry-Pi-3B-4B-p-5484.html?srsltid=AfmBOopBky9Q7r3SP8MtNyey5Iuo_tlIB08uAZgxWvRc-1y1QlcptiDn)，它支持先进的计算机视觉功能。该组件有助于实时监控和分析环境。

![](https://cdn.thenewstack.io/media/2024/10/32e6c96c-sensecap-hw-999x1024.jpeg)

Watcher 配备麦克风和扬声器，支持语音交互，使用户能够无缝地发出命令并接收音频反馈。1.46 英寸触摸屏是导航设置和访问功能的主要界面，增强了用户参与度。

Watcher 基于[ESP32-S3 平台](https://esp32s3.com/)，支持 Wi-Fi 和蓝牙低功耗 (BLE)，以便与其他设备进行高效通信。它还包括一个用于充电和数据传输的 USB 端口，以及一个 microSD 卡插槽，用于扩展存储能力。[Himax HX6538 芯片](https://www.himax.com.tw/products/wiseeye-ai-sensing/wiseeye2-ai-processor/) 采用 Cortex M55 和 US5 内核，使 Watcher 能够处理与人工智能相关的任务，增强其操作智能和响应能力。该芯片能够运行设备上的[TinyML](https://www.tinyml.org/) 模型，提供本地推理。

设备背面的[I2C 接口](https://learn.sparkfun.com/tutorials/i2c/all) 支持超过 100 个[Grove](https://wiki.seeedstudio.com/Grove_System/) 传感器，便于扩展和实验。还有一个[UART 接口](https://docs.arduino.cc/learn/communication/uart/)，用于连接到来自[Arduino](https://www.arduino.cc/) 和[Raspberry Pi](https://www.raspberrypi.org/) 的外部微控制器和板。

## 软件架构

[SenseCraft AI](https://sensecraft.seeed.cc/ai/#/home) 平台为 SenseCAP Watcher 的软件架构提供支持。该平台为任务编排、数据处理和用户交互提供了一个强大的框架。

![](https://cdn.thenewstack.io/media/2024/10/2eff8f2a-infrastructure-1024x574.png)

任务编排服务使 Watcher 能够通过直接语音命令或通过 SenseCraft Mate 应用程序处理任务。任务通过 HTTP 接口路由，由人工智能模型处理，然后返回到设备以执行。Watcher 分析视觉数据的能力是一个改变游戏规则的功能，使用户能够在 SenseCraft 的本地模型和第三方人工智能服务之间进行选择，以实现多功能的图像分析和目标检测。

SenseCAP Watcher 的一个重要优势是其混合处理能力，它利用了设备上人工智能模型和基于云的大型语言模型。这种灵活性使开发人员能够根据任务要求选择最佳处理路径——无论他们优先考虑使用本地模型的速度和响应能力，还是利用基于云的大型语言模型的广泛功能进行复杂分析。

> Watcher 分析视觉数据的能力是一个改变游戏规则的功能。

SenseCAP Watcher 与 SenseCraft AI 的集成是其功能的关键差异化因素。该设备可以利用本地处理和基于云的 LLM，为开发人员提供多种部署选项来增强应用程序性能。用户可以选择云高效处理、混合智能处理和本地安全处理流程——每种流程都提供了效率、数据安全和运营控制的独特平衡。

当代理选择基于云的 LLM 时，后台软件会将摄像头的关键帧转换为提示并将其发送到功能强大的多模态 AI 模型，该模型以结构化格式提取描述。根据响应，它会触发工作流程的其余部分。也可以将提示发送到在开发人员工作站或强大的边缘设备（例如 Nvidia Jetson Orin）上运行的本地 LLM。

该设备可以通过多种渠道传递警报，包括通过 SenseCraft 云推送通知、与其他硬件的 UART 连接以及与本地服务器的 HTTP 连接，确保用户及时收到有关监控事件的更新。

此外，Watcher 支持与流行的物联网平台集成，例如 Node-RED 和 Home Assistant。这种兼容性使开发人员能够创建复杂的自动化和数据流，使其成为各种应用程序的多功能工具。

## 主要用例和场景

SenseCAP Watcher 的功能使其成为各种应用程序的理想选择。在智能家居环境中，Watcher 可以监控活动、检测异常行为并向房主提供警报。例如，它可以识别何时有人进入房间并发送通知，从而增强安全性和意识。

> 该设备的开源性质鼓励开发人员探索其功能，尝试不同的传感器，并为围绕 SenseCraft 平台不断发展的生态系统做出贡献。

在零售环境中，Watcher 可以跟踪客户的移动和互动，使商店老板能够分析流量模式并优化布局策略，以提高客户参与度。同样，在工业自动化中，该设备充当行为传感器，提供有关设备状态和劳动力活动的实时洞察，从而减少停机时间并提高运营效率。

希望利用 SenseCAP Watcher 的开发人员可以通过遵循全面的安装说明（包括设备绑定和网络配置）轻松入门。SenseCraft Mate 移动应用程序是管理任务、监控性能和接收警报的主要界面。它还便于固件更新和设备定制。该设备的开源性质鼓励开发人员探索其功能，尝试不同的传感器，并为围绕 SenseCraft 平台不断发展的生态系统做出贡献。

SenseCAP Watcher 代表了 AIoT 领域的一项飞跃——人工智能与物联网技术的集成。通过将强大的硬件与灵活的软件架构和广泛的集成选项相结合，它为开发人员提供了一个强大的工具，可以在各个领域创建智能应用程序。利用设备上模型和 LLM 的混合方法可以实现针对特定用例的最佳性能，从而增强其可用性。

在本系列的下一部分，我将引导您完成构建由 SenseCraft Watcher 和视觉语言模型驱动的物理 AI 代理的步骤。敬请关注！