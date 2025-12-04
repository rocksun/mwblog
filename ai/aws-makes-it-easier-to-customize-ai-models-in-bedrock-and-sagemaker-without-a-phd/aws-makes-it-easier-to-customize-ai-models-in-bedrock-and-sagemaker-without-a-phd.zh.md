LAS VEGAS — 昨天，AWS [宣布了 Nova Forge](https://thenewstack.io/with-nova-forge-aws-makes-building-custom-ai-models-easy/)，这是一种企业利用自有数据定制[亚马逊](https://aws.amazon.com/?utm_content=inline+mention) Nova 大型语言模型（LLM）系列的新方式。今天，AWS 通过为其 Amazon Bedrock 和 SageMaker AI 服务添加模型定制选项，来满足一个非常类似的需求。

正如 AWS 代理式 AI 副总裁 Swami Sivasubramanian 在今天发布会前的一次采访中告诉我的那样，SageMaker 中的无服务器模型定制与该公司在 Nova Forge 上的做法不同。

## SageMaker AI 模型定制

SageMaker 的核心始终是构建机器学习模型——基础模型直到最近才被加入其中——基于公司自己的数据，然后帮助他们在其生命周期内部署和管理这些模型。

“这与 Nova Forge 不同，在那里，即使你是一个对[监督式微调]、RL [强化学习]或任何相关知识一无所知的工程师，你也可以与代理聊天并说：‘这是我的用例。这是我拥有的数据集。我应该如何定制它？’它会引导你完成整个过程，从监督式微调到强化学习，再到如何操作。然后它将端到端地启动所有这些工作。”

作为此过程的一部分，该工具甚至会生成自己的合成数据。

对于希望获得更多控制权的开发者，还有第二种代理式体验（AWS 将其描述为“自助式”方法）。开发者可以对过程的每个步骤获得更多控制，但正如 AWS 所指出的，他们仍然无需管理运行这些流程的任何基础设施，而是可以专注于寻找正确的定制技术并进行调整。

Sivasubramanian 强调此功能以前只有专业的 AI 科学家才能使用，并且超出了大多数开发者的能力范围。他还指出，这是一个完全无服务器的产品——就像 SageMaker 的其余部分一样。

## Bedrock 上的强化微调

至于 Bedrock，它是 AWS 提供的完全托管服务，用于访问来自亚马逊自身、Anthropic、Mistral 及其他公司的基础模型，其重点是强化微调（RFT）。与 Nova Forge 一样，AWS 认为开发者为特定用例有效地使用此技术来调整模型，仍难以设置训练管道和基础设施。

强化微调本质上涉及通过调整模型使其在给定任务上表现良好，其方法是让另一个模型对每个答案进行评分，然后将这些答案纳入模型的权重中。与其他的强化学习技术一样，这是一个基于奖励的系统，由评分模型提供分数和奖励。

对于这项服务，开发者可以选择不同的奖励函数——基于 AI 的、基于规则的或即用型模板——然后 Bedrock 将处理微调过程。

“无需机器学习博士学位——只需要清楚了解对业务而言什么是好的结果，”AWS 在其新闻稿中指出。

AWS 认为，对于使用此技术的客户来说，与基础模型相比，其准确率平均提高了 66%，同时还使模型运行起来更简单、更快。

## 竞争

值得注意的是，AWS 并不是第一个推出许多这些功能的公司。谷歌的 Vertex AI [提供](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-use-supervised-tuning)了一套模型定制套件，提供了不少强化学习选项。同样，微软的 AI Foundry 也[提供微调服务](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/fine-tuning-considerations?view=foundry-classic)。

YOUTUBE.COM/THENEWSTACK

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、采访、演示等内容。

[订阅](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

在加入 The New Stack 担任 AI 高级编辑之前，Frederic 曾是 TechCrunch 的企业编辑，在那里他报道了从云计算的兴起、Kubernetes 的早期发展到量子计算的出现等各种主题……

阅读更多 Frederic Lardinois 的文章](https://thenewstack.io/author/frederic-lardinois/)