<!--
title: Q.ANT 效仿英伟达 CUDA 策略，免费开源光动力 AI 芯片软件工具包
cover: https://cdn.thenewstack.io/media/2026/09/72bd656b-screenshot-2026-09-23-at-3.18.24-pm-1024x581.png
summary: 德国初创公司Q.ANT发布了其光动力AI芯片的免费开源软件开发包，效仿英伟达CUDA模式，允许开发者在普通电脑上模拟测试程序，以降低AI能耗并构建生态。
-->

德国初创公司Q.ANT发布了其光动力AI芯片的免费开源软件开发包，效仿英伟达CUDA模式，允许开发者在普通电脑上模拟测试程序，以降低AI能耗并构建生态。

> 译自：[Q.ANT gives away the software for its light-powered AI chips in a CUDA-style bet on developers](https://thenewstack.io/q-ant-open-sources-cuda/)
> 
> 作者：Matthew Burns

[Q.ANT](https://qant.com/) 是一家总部位于德国斯图加特的初创公司，其制造的处理器利用光而不是电来完成 AI 背后的部分数学计算。该公司将其宣传为一种以极少功耗运行 AI 的方式，而这种功耗仅为当今芯片所需的一小部分。

现在，开发者无需拥有一块芯片就可以开始为这些芯片编写软件了。Q.ANT 本周在 GitHub 上发布了一个免费的开源软件开发包，允许开发者在普通计算机上构建和测试程序，一旦获得访问权限，就可以在真正的芯片上运行它们。

这一举措借鉴了英伟达的 playbook。英伟达在 AI 领域的领先地位，很大程度上归功于 CUDA（开发者用来对其 GPU 进行编程的软件），其重要性不亚于芯片本身。

但对于 Q.ANT 来说，问题在于硬件。Q.ANT 的芯片目前在少数几个研究计算中心运行，其他人则必须等待“未来几个月”通过德国供应商 IONOS 或 Q.ANT 的现场服务器获得云端访问权限。

该开发包名为 [Q.ANT Native Computing Toolkit](https://github.com/Q-ANT-GmbH/qant_native_computing_toolkit)，在 GitHub 上以允许商业使用的许可证免费提供。开发者可以使用 Python 或 C 语言进行开发。其核心部分是一个在普通计算机上模拟芯片的模拟器，无需 Q.ANT 驱动程序。

它今天能做什么？第一个版本中的 AI 工具专注于运行已经训练好的模型。这些示例可以读取手写数字、识别照片中的物体以及勾勒图像中的形状。训练仍然在常规 CPU 和 GPU 上进行。

光子计算的卖点在于功率。AI 芯片在内存和处理器之间来回传输数据会消耗大量能量。Q.ANT 的芯片用光完成部分数学计算，具体来说是类似余弦的波形函数，而常规芯片是以数字方式计算这些函数的。Q.ANT 表示，围绕这些函数构建的 AI 模型以更少的参数就能获得更好的结果，而参数是模型在训练过程中学习的设置。更少的参数意味着更小的模型、更少的数据传输以及更低的功耗。该开发包包含将标准模型与 Q.ANT 方式构建的模型进行比较的示例。这些比较是该公司自己的数据。

“生态系统并非仅由硬件创造。当软件层是开放的且其他人可以在其上构建时，它才会出现，”Q.ANT 创始人兼 CEO Michael Förtsch 说道。他将此次发布称为光子计算的“Linux 时刻”。

Q.ANT 押注光可以自行完成数学计算。Lightmatter 是该领域最著名的公司之一，现在将重点放在 Passage 上，它利用光在芯片之间传输数据。基于光的 AI 的想法也不新鲜。TNS 早在 2017 年就报道了 [MIT 的用于构建光神经网络的光子处理器](https://thenewstack.io/mit-devises-photonic-processor-building-optical-neural-networks/)。

Q.ANT 在 2025 年 7 月由 Cherry Ventures、UVC Partners 和 imec.xpand 领投的一轮融资中筹集了 6200 万欧元。今年 3 月，该公司表示其第二代芯片正在慕尼黑附近的莱布尼茨超级计算中心运行。它从那里[公布的结果](https://qant.com/press-releases/higher-performance-less-energy-q-ant-deploys-second-generation-photonic-processors-at-supercomputing-center-lrz/)将新芯片与旧芯片进行了比较：按照该公司的数据，在执行 AI 模型中大部分工作的数学计算时，速度快了 50 多倍，在典型作业上的能耗降低了六倍。它的一些更大胆的说法（例如高达 30 倍的能效提升）并没有说明它们是与什么进行对比的。

仅凭优秀的软件并不能承载一新芯片。英伟达构建 CUDA 已经将近 20 年，并且仍在为其添加功能，包括去年[对 Python 实现了更深入的原生支持](https://thenewstack.io/nvidia-finally-adds-native-python-support-to-cuda/)。英国 AI 芯片初创公司 Graphcore 拥有自己的软件开发包，但最终还是在 2024 年被软银收购。

Q.ANT 称这是第一个公开可用的用于编程光子处理器的软件开发包。这取决于你如何计算。Xanadu 自 2018 年以来一直为其基于光的量子计算机提供免费的开放软件。目前，开发者可以试用模拟器。他们还不能做的是在自己的模型上测试 Q.ANT 的省电声明。这必须等到芯片开放之后才能实现。