<!--
title: AI应用反向构建：模型-产品难题
cover: https://cdn.thenewstack.io/media/2025/07/f06386ee-artem-sapegin-b18trxc8upq-unsplash-scaled.jpg
summary: AI开发者应重视数据反馈循环和模型组合，将模型开发视为产品一部分，通过用户互动不断优化模型，并结合多个AI系统解决问题，而非依赖通用基础模型。
-->

AI开发者应重视数据反馈循环和模型组合，将模型开发视为产品一部分，通过用户互动不断优化模型，并结合多个AI系统解决问题，而非依赖通用基础模型。

> 译自：[You're Building AI Apps Backwards: The Model-Product Problem](https://thenewstack.io/youre-building-ai-apps-backwards-the-model-product-problem/)
> 
> 作者：Lin Qiao

大多数 AI 开发者都在倒着构建产品。他们从一个基础模型开始，将其包装在一个界面中，然后想知道为什么用户没有得到他们需要的结果。

我到处都看到这种模式。开发者将模型视为 API：插入它们，配置一些参数，然后发布。但是基础模型不是实用程序，而是工程师需要塑造、训练并与用户每天面临的特定问题对齐的起点。

## 为什么通用基础模型在企业应用中会失败

考虑一家金融服务公司的开发者，他们试图使用 GPT-4 来[构建一个投资研究](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/)应用程序。该模型可以分析财务文件并回答有关市场趋势的问题。尽管如此，它并不理解例行的收益电话会议与预示着业务重大[战略转变](https://thenewstack.io/why-businesses-are-rethinking-it-providers-and-shifting-to-strategic-partnerships/)的电话会议之间的区别。它无法区分对您的内部合规团队重要的监管文件与不重要的监管文件。

OpenAI 训练 GPT-4，使其在数千个领域具备广泛的能力。但是这家金融服务公司需要一个能够理解金融分析、监管要求以及团队中投资组合经理的特定工作流程的模型。

根本问题：两个不同的设计目标

具有不同目标的两组完全不同的人设计基础模型和终端用户 AI 应用程序——[研究人员和产品开发者](https://thenewstack.io/why-businesses-want-to-enable-no-code-and-low-code-automation/)。主要模型实验室的研究人员针对跨学术基准的广泛能力进行优化。通常，他们使用与其竞争对手相同的训练数据集。但是[开发者构建应用程序](https://thenewstack.io/google-wants-developers-to-build-on-device-ai-applications/)是为了满足特定的客户和市场需求——食品配送应用程序的客户服务、生产力平台的生成式图形设计、市场研究的自动化竞争对手分析。

从设计上讲，这些方法是不一致的。OpenAI、DeepSeek、Meta 或 Anthropic 的研究人员构建模型，并不是为了让德勤的顾问说“分析这份报告”时，它知道将客户的数据与特定的竞争对手进行比较；或者构建一个能够理解客户服务代表的“紧急”与医生做出医疗诊断的“紧急”之间区别的模型。开发者才是。

模型是原材料。开发者的专有数据会将其塑造成与用户工作流程和业务需求相匹配的产品。

这对您的 [AI 产品战略意味着什么？](https://thenewstack.io/what-generative-ai-means-for-product-strategy-and-how-to-evaluate-it/)

为了实现模型与产品的对齐，开发者必须优先考虑：

## 数据反馈循环：构建能够真正从用户那里学习的模型

有效的应用程序会创建反馈循环，其中每次用户交互都会使模型在特定任务上变得更好。当用户纠正应用程序的输出时，该纠正会反馈到模型训练中。当用户忽略某些建议时，模型会学习停止提出这些建议。

数据反馈循环会产生复合优势。更多的用户会[生成更好的训练数据](https://thenewstack.io/kumo-surfaces-structured-data-patterns-generative-ai-misses/)，从而提高模型性能，从而吸引更多的用户。这些系统不会在扩展时遇到性能瓶颈，而是会得到改进。

这种[方法需要将模型开发视为产品的一部分](https://thenewstack.io/a-portal-as-a-product-approach-for-internal-developer-portals/)，而不是供应商管理。这意味着管理模型在[不同用户群中的性能并解决有关模型版本控制和部署的新问题](https://thenewstack.io/the-complexity-of-solving-performance-problems/)。

## 模型组合：领先公司如何组合多个 AI 系统

最具差异化的 AI 应用程序组合了多个模型和模态来解决问题，而不是依赖于单个模型。一家物流公司可能会将用于包裹扫描的计算机视觉与用于客户沟通的自然语言处理相结合，然后将预测建模用于路线优化——所有这些都作为一个统一的系统工作。

这需要了解模型架构的工程师，他们可以做出战略决策，决定何时使用检索增强生成与微调专用模型。

将会胜出的应用程序不是那些拥有对闭源模型的特权访问权的应用程序。它们是通过仔细对齐、数据收集和迭代改进，投入专门资源将开源模型调整为有价值的最终产品的应用程序。

尽早解决这种对齐问题的开发者将建立起无法复制的护城河。那些没有解决这个问题的开发者将会在任何竞争对手都可以通过切换到最新的闭源模型 API 来复制的功能上展开竞争。