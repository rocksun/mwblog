<!--
title: OpenAI推出Privacy Filter：本地运行，让隐私信息不再“上云”
cover: https://cdn.thenewstack.io/media/2026/04/330df48c-detective-magnifying-lens-scaled.jpg
summary: OpenAI发布了Privacy Filter，一个可本地运行的PII检测脱敏模型。它具备15亿参数和强上下文感知力，支持128k长文本，能有效防止敏感数据上传云端。
-->

OpenAI发布了Privacy Filter，一个可本地运行的PII检测脱敏模型。它具备15亿参数和强上下文感知力，支持128k长文本，能有效防止敏感数据上传云端。

> 译自：[OpenAI's new Privacy Filter runs on your laptop so PII never hits the cloud](https://thenewstack.io/openai-privacy-filter-pii/)
> 
> 作者：Meredith Shubel

OpenAI 推出了 Privacy Filter，这是一个双向标记分类模型，用于检测和脱敏个人身份信息 (PII)，它能够单次扫描长文本，在本地运行，并提供更强的上下文感知能力。

## 单次扫描邮件、数字等文本信息

对于开发大语言模型 (LLM) 的开发者来说，数据隐私一直是一个反复出现的问题。但随着周三发布的全新 Privacy Filter，OpenAI 实际上是开放了其内部用于自身隐私保护工作流的工具。

那么，它是如何工作的呢？

正如 OpenAI 在其发布[博客文章](https://openai.com/index/introducing-openai-privacy-filter/)中所解释的，它从一个自回归预训练检查点开始，并将其转换为一个基于固定隐私标签分类法的标记分类器。

它不是一次生成一个标记，而是“一次性标记输入序列，然后使用受限的 Viterbi 程序解码连贯的跨度”。

共有八种此类标签，允许 Privacy Filter 屏蔽或脱敏姓名、地址、电子邮件、电话号码、URL、日期、账号和机密信息（例如 API 密钥或密码）。

（这是一个相当不错的汇总，但并没有涵盖所有内容；例如，社会安全号码和护照号码被忽略了。）

## 更强的上下文感知，本地运行

OpenAI 声称 Privacy Filter 具有更强的上下文感知能力，使其能够识别更微妙的个人信息并做出更细致的决策。

> “通过将强大的语言理解能力与特定于隐私的标签系统相结合，它可以检测非结构化文本中更广泛的 PII，包括那些正确决策取决于上下文的情况。”

具体而言，这家 AI 公司声称其双向标记分类模型比传统的 PII 检测工具（如正则表达式 (RegEx) 或 NLP 库）更进一步，后者通常依赖于格式的确定性规则。

虽然这些方法在处理较简单的情况（如电话号码或电子邮件地址）时可能奏效，但当上下文引入更多微妙之处时，它们更有可能遇到问题：

“通过将强大的语言理解能力与特定于隐私的标签系统相结合，它可以检测非结构化文本中更广泛的 PII，包括那些正确决策取决于上下文的情况。”

例如，Privacy Filter 应该能够区分可以保留的公开信息和应该屏蔽或脱敏的私密信息，比如公开的商业地址与私人家庭地址。

这种对上下文的关注在处理带有非结构化文本的长文档时也会发挥作用。OpenAI 表示，Privacy Filter 专门设计用于捕获“嘈杂、真实世界”文本中的 PII，例如支持日志、冗长的法律文件等。为了在不分块的情况下扫描这些长文本，该模型支持高达 128,000 个标记的上下文。

Privacy Filter 的体积也显著较小。

该模型总参数为 15 亿，活跃参数为 5000 万，运行速度足够快，可以在浏览器或笔记本电脑上本地运行。除了效率提升外，这意味着开发者可以使用 Privacy Filter 在自己的环境中屏蔽和脱敏 PII，从而降低敏感数据的暴露风险。

## 与竞争对手的对比

在其发布博客文章中，OpenAI 吹嘘 Privacy Filter “在针对我们在评估期间识别的注释问题进行修正后，在 [PII-Masking-300k 基准测试](https://huggingface.co/datasets/ai4privacy/pii-masking-300k)中实现了最先进的性能”。

它所谓的“最先进”是指 F1 分数为 96%（94.04% 的精确率和 98.04% 的召回率）。

当然，OpenAI 并不是第一个提供 PII 检测和脱敏解决方案的公司。

例如，[微软的 Presidio](https://github.com/microsoft/presidio) 是一个用于检测、脱敏、屏蔽和匿名化文本、图像及结构化数据的开源框架。在这里，微软可能会胜出：OpenAI 在其博客文章中直截了当地指出，Privacy Filter 不是一个匿名化工具，而是“更广泛的隐私设计系统中的一个组件”。

与此同时，[亚马逊的 Comprehend](https://aws.amazon.com/comprehend/) 是 AWS 工作流中用于 PII 检测和脱敏的托管服务。

与现有竞争对手相比，Privacy Filter 因其上下文感知和本地运行的设计而脱颖而出。

虽然微软可能比 Privacy Filter 为开发者提供更多功能，但 OpenAI 的模型以更强的上下文感知能力和本地部署弥补了其较小的范围——至少在对抗亚马逊的托管服务时是这样。

## 这对开发者意味着什么

对于构建 RAG 系统、开发客户支持管道或编排任何其他需要将用户文本输入 LLM 的工作流的开发者，OpenAI 表示 Privacy Filter 应该能够很好地融入其中。

微调选项增加了 OpenAI 模型的吸引力。

据称，只需少量数据即可看到效果。在其[模型卡](https://cdn.openai.com/pdf/c66281ed-b638-456a-8ce1-97e9f5264a90/OpenAI-Privacy-Filter-Model-Card.pdf)中，OpenAI 报告称“在 10% 的数据集上进行训练足以使 F1 分数超过 96%”。

这意味着利用相对较少的数据，开发者就可以使 OpenAI 的模型适应不同的数据分布、隐私政策和领域特定任务。

尽管如此，OpenAI 对法律、医疗和财务工作流等高敏感领域表示谨慎，提醒开发者保持人工审核并为潜在错误做好准备。

> “在 10% 的数据集上进行训练足以使 F1 分数超过 96%。”

## OpenAI 技术栈的又一成员

Privacy Filter 现已在 [Hugging Face](https://huggingface.co/openai/privacy-filter) 和 [GitHub](https://github.com/openai/privacy-filter) 上以 Apache 2.0 协议发布。

它与周四发布的 [OpenAI GPT-5.5](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/) 一同推出，OpenAI 称后者为“新一类智能”。