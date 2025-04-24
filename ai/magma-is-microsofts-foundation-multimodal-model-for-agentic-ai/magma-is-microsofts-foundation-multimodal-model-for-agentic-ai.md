
<!--
title: Magma是微软用于Agentic AI的基础多模态模型
cover: https://cdn.thenewstack.io/media/2025/04/e74db13e-microsoft-magma-4.jpeg
summary: 微软发布多模态基础模型 **Magma**，赋能 **Agentic AI**！集成视觉、语言、动作 (VLA)，预训练于海量数据集，创新 **SoM** 和 **ToM** 标注，UI 导航和机器人操作表现卓越，或将革新云原生 AI 交互方式！
-->

微软发布多模态基础模型 **Magma**，赋能 **Agentic AI**！集成视觉、语言、动作 (VLA)，预训练于海量数据集，创新 **SoM** 和 **ToM** 标注，UI 导航和机器人操作表现卓越，或将革新云原生 AI 交互方式！

> 译自：[Magma Is Microsoft's Foundation Multimodal Model for Agentic AI](https://thenewstack.io/magma-is-microsofts-foundation-multimodal-model-for-agentic-ai/)
> 
> 作者：Kimberley Mok

最近，围绕 [agentic AI](https://thenewstack.io/the-promises-of-agentic-ai-and-how-to-sidestep-challenges/) 出现了很多令人兴奋的事情，并且随着 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 最近发布的 [Magma](https://microsoft.github.io/Magma/)，该公司认为其新的基础 AI 模型将使 AI 代理能够在数字和现实世界环境中高效地执行多模态任务，无论是通过软件还是物理机器人。

Magma 源于 Microsoft、[KAIST](https://www.kaist.ac.kr/en/)、马里兰大学、威斯康星大学麦迪逊分校和华盛顿大学的研究人员之间的合作，它扩展了先前在 [视觉语言模型](https://huggingface.co/blog/vlms) (VLM) 方面的工作，使其成为 AI 驱动的自动化向前迈出的重要一步。

更具体地说，Magma 是一个多模态 [多模态](https://thenewstack.io/top-7-tools-for-building-multimodal-ai-applications/) 视觉-语言-动作 (VLA) 模型，它集成了视觉感知、语言理解和动作推理，使 AI 系统能够处理上下文中的图像和基于文本的指令，并提出相关的动作。

“Magma 是第一个用于多模态 AI 代理的基础模型，”该团队在 Magma 的项目页面上 [写道](https://microsoft.github.io/Magma/)。“作为多模态 agentic 模型的基础，它具有强大的能力来扎实地感知多模态世界，并精确地采取目标驱动的行动。

“通过有效地从免费提供的视觉和语言数据中转移知识，Magma 桥接了语言、空间和时间智能，以在数字和物理世界的复杂任务和环境中导航。”

![](https://cdn.thenewstack.io/media/2025/04/042ac26a-magma-1.png)

*通过微软研究院。*

## 视觉-语言-动作是多合一的 AI 模型

直到最近，现代机器人控制系统的底层编程很难适应现实世界动态且通常混乱的性质。例如，可能会指示机器人移动到工厂中的指定位置，将东西放在架子上，但是如果一个意外的物体挡住了它的路，机器可能会停止，并且如果它没有被明确编程这样做，则在绕过这个计划外的障碍时会遇到问题。

传统的机器人可能会“看到”障碍物（视觉），但可能难以推理下一步该做什么（语言）以及如何做（动作），因为这些任务是以一种更加脱节的方式处理的。

相比之下，VLA 模型背后的统一架构和方法允许机器人以人为的方式处理这些计划外的意外情况，通过在一个集成的过程中合并视觉、语言和动作，使机器人能够即时发挥。VLA 模型本质上是多合一的 AI 模型，允许机器人看到它们的环境，了解该做什么，并以集成和自适应的方式行动。

## Magma 缩小了差距

Magma 专门作为机器人系统的多用途解决方案而创建，它集成了实时感知和动作，使 AI 代理能够采取多个步骤来自主控制软件和机器人，而无需人工干预。

Magma 在大量各种视觉语言数据集上进行了预训练，包括图像、文本、视频和机器人数据。文本被标记化为 tokens，而各种类型的视觉数据通过共享的视觉编码器进行编码。生成的 tokens 由大型语言模型 (LLM) 解析，该模型以语言、空间和动作类别生成输出。

然而，根据研究人员的说法，Magma 的预训练管道代表了对其前身的重大改进。

“由于各种数字和物理环境之间的巨大差异，因此训练和使用单独的 VLA 模型用于不同的环境，”Magma 团队在 Microsoft Research Blog 上的一篇文章中 [写道](https://www.microsoft.com/en-us/research/blog/magma-a-foundation-model-for-multimodal-ai-agents-across-digital-and-physical-worlds/)。“因此，这些模型难以推广到其训练数据之外的新任务和环境。此外，这些模型中的大多数没有利用预训练的视觉语言 (VL) 模型或各种 VL 数据集，这阻碍了它们对 VL 关系和通用性的理解。

“据我们所知，Magma 是首批可以适应数字和物理环境中的新任务的 VLA 基础模型之一，这有助于 AI 驱动的助手或机器人了解它们周围的环境并提出适当的行动。”

![Magma 如何将视频转换为文本的两个示例。](https://cdn.thenewstack.io/media/2025/04/41957214-video-conversation-1024x480.png)

*来自 Magma 项目网站的两个例子展示了 AI 模型如何将视频转换为文本，从而回答用户提示。*

Magma 改进的性能归功于该团队的新型训练方法，该方法侧重于微软研究院开发的两种主要标注方法，旨在为模型提供一种更结构化的方式来理解在导航用户界面和机器人操作中的任务：

- **Set-of-Mark (SoM):** 这种方法旨在通过为环境中任何交互元素（如可以单击的按钮或可以拾取的对象）分配数字标签，从而在所有数据模式中对可操作的任务进行定位。“通过提供 SoM，我们为 Magma 提供了一个关于‘需要关注什么’的高级提示——任务的基本要素——而无需指定顺序或方法，”该团队写道。
- **Trace-of-Mark (ToM):** 当专门应用于视频和机器人数据时，这使得模型能够从视频数据中学习可能的运动模式，从而能够“捕捉这些元素在整个交互过程中如何变化或移动”，从而在规划潜在动作时预测未来状态。

![](https://cdn.thenewstack.io/media/2025/04/0439519f-microsoft_magma-2.jpeg)

*通过微软研究院。*

在测试过程中，该团队发现 Magma-8B 在各种基准测试中表现出强大的性能，尤其是在 UI 导航和涉及机器人操作的任务中。对于后者，Magma 的性能实际上超过了各种任务中的开源 [OpenVLA](https://openvla.github.io/)。

正如微软团队指出的那样，Magma 只是该公司设想的未来代理 AI 系统的一个组成部分，该系统能够在数字和物理世界中执行任务。该公司最近还推出了最新版本的 [AutoGen](https://www.microsoft.com/en-us/research/project/autogen/)，这是一个流行的开源编程框架，用于[开发多代理 AI 系统](https://thenewstack.io/a-developers-guide-to-the-autogen-ai-agent-framework/)，并且目前正在试验由基础代理 AI 模型提供支持的全新用户体验系统。