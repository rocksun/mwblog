
<!--
title: 10 个用于在 AWS 上构建基于 LLM 的应用程序的关键产品
cover: https://cdn.thenewstack.io/media/2024/02/5a177a39-josue-isai-ramos-figueroa-qvbynmunj9a-unsplash-1.jpg
-->

10 款旨在让开发人员为其当前和未来产品组合添加生成式 AI 功能的关键 AWS 产品一览。

> 译自 [10 Key Products for Building LLM-Based Apps on AWS](https://thenewstack.io/10-key-products-for-building-llm-based-apps-on-aws/)，作者 Torsten Volk。


# 构建基于 LLM 的 AWS 应用程序的 10 个关键产品

![用于构建基于 LLM 的 AWS 应用程序的 10 个关键产品的特色图片](https://cdn.thenewstack.io/media/2024/02/5a177a39-josue-isai-ramos-figueroa-qvbynmunj9a-unsplash-1-1024x746.jpg)

在去年年底的 AWS [re:Invent](https://reinvent.awsevents.com/) 会议上，[生成式 AI](https://thenewstack.io/generative-ai-in-2023-genai-tools-became-table-stakes/) 的重新发明是 [Adam Selipsky](https://www.linkedin.com/in/adamselipsky/) 主题演讲中的重要议题。在开场主题演讲中，[亚马逊网络服务 (AWS)](https://aws.amazon.com/?utm_content=inline-mention) 首席执行官 Selipsky 专注于基于 [大型语言模型 (LLM)](https://thenewstack.io/llm-app-ecosystem-whats-new-and-how-cloud-native-is-adapting/) 的生成式 AI 如何为开发人员的生产力提供“涡轮增压”，同时还能实现前所未有的针对每个客户的定制化程度。AWS 数据和 AI 副总裁 [Swami Sivasubramanian](https://www.linkedin.com/in/swaminathansivasubramanian/) 表示，“生成式 AI 有可能重新定义各行业的客户体验。”

生成式 AI 的这种变革性特征基于根据各个用户视角创建高度个性化应用程序体验的能力。生成式 AI 通过基于单个用户视角处理海量数据的能力实现了这种“大规模定制”。

## 有什么大不了的

这里的大问题是，生成式 AI 最终可以提供最终用户在特定时间点完成特定任务或解决特定挑战所需的准确数据、用户体验和应用程序功能。[生成式 AI 驱动的](https://thenewstack.io/is-ai-a-job-killer-ai-driven-development-tools-offer-clues/) 应用程序“了解”每个用户的优先级和整体情境，因此可以提供个性化定制的仪表板、见解、建议和自动化解决方案。基于对最终用户的深入了解，生成式 AI 可以提供最佳生产力的护栏。

例如，LLM 可以监听客户支持电话，并自动向支持工程师提供有关如何最快解决问题的建议。这意味着对于同一个问题，LLM 可以根据线路另一端的客户的语调提出不同的建议。

这些建议还可能取决于许多其他因素，例如客户的消费记录、与相同或类似客户的先前支持电话、公司防止客户流失的优先级以及其他任何因素。此示例表明，基于硬编码指令的传统软件开发永远无法奏效，因为组织、其客户和员工周围的情境复杂性太多。

## 10 个关键 AWS 产品和注意事项

现在让我们来看看 10 个关键的 AWS 产品，这些产品旨在让开发人员能够为其当前和未来的产品组合添加生成式 AI 功能。

## 1. 基础模型即服务：Amazon Bedrock

[Amazon Bedrock](https://aws.amazon.com/bedrock/) 允许开发人员以托管服务的形式使用来自 [AI21 Labs](https://thenewstack.io/ai21-labs-releases-jurassic-2-its-new-large-language-model/)、Anthropic、[Cohere](https://thenewstack.io/cohere-vs-openai-in-the-enterprise-which-will-cios-choose/)、Meta、Stability AI 和亚马逊本身的不同基础模型。开发人员可以使用自己的数据微调这些模型，以执行文本摘要、问题解答或图像生成等任务。Bedrock 支持针对特定行业和领域的定制，从而提高 AI 响应的相关性和准确性。用例包括使用 [RAG](https://en.wikipedia.org/wiki/Prompt_engineering#Retrieval-augmented_generation)（检索增强生成）使用专有数据丰富 AI 响应、在公司系统中执行复杂任务以及创建用于客户交互或订单处理的代理。简而言之，Bedrock 的重要性在于它能够为开发人员提供一个 API，让他们在没有太多启动时间的情况下开始使用和微调 LLM。

## 2. 控制 LLM 输出：Bedrock 的护栏
## Bedrock 的护栏

[Bedrock 的护栏](https://aws.amazon.com/bedrock/guardrails/) 为开发人员提供了一个开发者 API，用于定义 Bedrock 基础模型给出的答案的边界集合。例如，开发人员可以确保他们的聊天机器人只回答属于特定主题类别的提问，或者他们可以防止他们的机器人使用技术术语或有问题的语言。开发人员还可以使用护栏 API 来控制法规遵从性、限制法律责任、确保品牌声音一致性，并根据当地文化敏感性做出回应。与医疗保健相关的 LLM 可以进行调整，以避免提供医疗建议，并始终警告用户寻求专业帮助，而不是将生成式 AI 作为医生的替代品。

## 3. 加速模型训练：SageMaker HyperPod

虽然 [SageMaker HyperPod](https://aws.amazon.com/sagemaker/hyperpod/) 不是一个 [无服务器](https://thenewstack.io/serverless/) 产品，但 AWS 通过 AWS 管理控制台和命令行界面实现了简单的配置、配置和维护。Hyperpod 集群附带了分布式训练所需的全部 SageMaker 库，可以在节点之间暂停、分析和优化训练过程，而无需重新开始的风险。Hyperpod 允许从一个 GPU 即时扩展到数千个 GPU，而无需重建集群。对于应用程序开发人员来说，这两个因素可以决定是否轻松满足交付截止日期，或者由于缓慢的需要反复训练和重新训练 LLM 而导致关键路径爆炸。但请记住，由于您要为 HyperPod 集群中 [计算实例](https://thenewstack.io/cloud-bill-risks-of-aws-reserved-instances-and-savings-plans/) 的大小、数量和持续时间付费，因此始终存在过度配置或忘记取消配置昂贵资源的风险。

## 4. 高性能硅：AWS Trainium2 和 Graviton4 芯片

作为一名开发人员，您可以通过各种 [EC2](https://thenewstack.io/inside-a-privilege-escalation-attack-via-amazon-web-services-ec2/) 实例利用 AWS 最新硅创新技术的力量。每个配备 16 个 [Trainium2](https://aws.amazon.com/machine-learning/trainium/) 芯片的 EC2 Trn2 实例旨在加速模型训练，提供高达四倍的速度提升。另一方面，配备 [Graviton4](https://aws.amazon.com/ec2/graviton/) 处理器的 EC2 R8g 实例专为 CPU 和内存密集型任务（如 AI 推理和 [实时分析](https://thenewstack.io/top-5-reasons-for-moving-from-batch-to-real-time-analytics/））而设计。从本质上讲，虽然 Trainium2 专注于加速模型训练过程，但 Graviton4 解决了推理方面的问题，为实时分析和内存缓存中的高效数据处理等任务提供了计算能力。

## 5. 高性能存储：Amazon S3 Express One Zone

[S3 Express One Zone](https://aws.amazon.com/s3/storage-classes/express-one-zone/) 为开发人员提供低延迟高性能存储。这种类型的存储对于需要处理大型数据集的项目非常重要。LLM 训练和大数据分析都是可以从 S3 Express One Zone 中显著受益的主要工作负载，因为 Amazon 承诺与标准 S3 存储相比，数据访问速度提高了 10 倍，请求延迟始终在个位毫秒内，API 请求成本降低了 50%。由于 S3 Express One Zone 在实际数据存储成本方面要昂贵得多，因此根据消耗自动向上或向下扩展的自动分层功能对于控制成本至关重要。

## 6. 在隐私中协作：AWS Clean Rooms ML

许多 AI 项目由于 [数据隐私](https://thenewstack.io/llms-and-data-privacy-navigating-the-new-frontiers-of-ai/) 问题而夭折，当数据所有者决定项目的收益不足以抵消其可能带来的合规风险时。[AWS Clean Rooms](https://aws.amazon.com/clean-rooms/) ML 允许模型训练，而无需披露甚至移动训练数据。这项新服务允许多方提供数据进行模型训练，但不允许访问这些数据。例如，IT、销售和营销可以合并他们的数据来创建联合模型，帮助 IT 根据潜在业务影响对服务单据进行优先级排序，而销售和市场团队可以预测其活动对公司 IT 的影响。Clean Rooms ML 是一种完全托管的“无服务器”产品，按使用指标（例如查询或训练的 AI 模型的数量和复杂性）收费。

## 7. 企业聊天机器人：Q
## Amazon Q
[Amazon Q](https://aws.amazon.com/q/) 是开发人员的变革性工具，将生成式 AI 集成到 AWS 服务的核心。凭借其以 API 为中心的设计，它使开发人员能够创建定制的 AI 助手，利用从 [Amazon S3](https://thenewstack.io/amazon-s3-express-one-zone-introduces-near-real-time-object-storage/) 到 GitHub 的广泛数据源。此功能不仅仅是渐进式增强；它是一种范式转变，提供了一个可定制的、私有的 LLM 实例，可以与特定应用程序或用户需求紧密对齐。作为完全托管的聊天机器人，Amazon Q 简化了通常与此类集成相关的复杂性，提供了一种经济高效、基于使用情况的计费模式。这使 Q 成为现代开发人员工具包中的一项重要资产，释放了应用程序智能和用户交互的新潜力。

## 数据驱动的见解：支持 LLM 的 Amazon Redshift ML
[Amazon Redshift ML](https://aws.amazon.com/redshift/features/redshift-ml/) 现在支持 LLM，使开发人员能够在分析中利用 LLM 的强大功能。借助此增强功能，开发人员可以在 Amazon Redshift 中对其产品反馈数据进行推理，执行诸如总结反馈、实体提取、情绪分析和产品反馈分类之类的任务。此功能需要在 Amazon SageMaker JumpStart 中为 LLM 创建一个端点，该端点可以是预定义模型或使用您自己的数据训练的自定义模型。LLM 与 Redshift ML 的集成将 AI 的强大功能带入了 [数据分析](https://thenewstack.io/whats-pipeline-free-real-time-data-analytics/)，使开发人员能够从数据中提取更多价值并做出更明智的决策。

## 简化的实验：AWS 上的生成式 AI 应用程序构建器
[AWS 上的生成式 AI 应用程序构建器](https://aws.amazon.com/solutions/implementations/generative-ai-application-builder-on-aws/) 加快了开发并简化了实验。它提供了与各种 LLM 的预构建连接器，包括来自 Amazon Bedrock 和选定的第三方 LLM。此解决方案在部署所选模型和集成首选 AWS 和第三方服务方面提供了灵活性。它还提供企业级安全性、可扩展性、高可用性和低延迟。开发人员可以通过集成现有项目或本机连接其他 AWS 服务来扩展此解决方案的功能。该解决方案包括 [LangChain 编排](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/) 库和用于连接第三方服务的 Lambda 函数，使其成为构建和部署 AI 应用程序的综合工具。

## 简化的 AI 开发：LangChain
AWS 提供 [LangChain](https://aws.amazon.com/what-is/langchain/) 作为开发人员简化 AI 开发、与各种 AWS 服务集成和部署 LLM 应用程序的工具。LangChain 通过抽象数据源集成和提示优化来简化 AI 开发。它将 Amazon Bedrock、Amazon Kendra、Amazon SageMaker JumpStart 和您的 LLM 等各种组件联系在一起，从而能够在企业数据上构建高度准确的生成式 AI 应用程序。LangChain 充当连接这些组件的接口，使开发人员可以更轻松地设置和访问生成模型。这种 AI 开发的简化使开发人员可以更多地关注应用程序逻辑，而更少地关注 AI 模型管理的复杂性。

## 结论
鉴于 LLM 的资源密集型特性，开发人员必须设计可优化 AWS 资源的可扩展应用程序。这包括选择合适的实例类型、管理计算资源和采用经济高效的策略。

在 AWS 上构建基于 LLM 的应用程序需要对 LLM 技术和 AWS 生态系统有细致的了解。开发人员必须考虑可扩展性、成本、数据隐私、与其他 AWS 服务的集成和用户体验等方面。通过关注这些考虑因素，开发人员可以充分利用 AWS 的潜力，构建强大、高效且有效的 LLM 驱动的应用程序。

随着 LLM 领域的不断发展，了解最新趋势和最佳实践对于开发人员至关重要。AWS 上 LLM 相关开发的一系列公告仅仅标志着 AI 和机器学习领域激动人心的旅程的开始。
去年年底在芝加哥举行的 [AWS re:Invent](https://thenewstack.io/aws-goes-deep-on-ai-chip-power-and-cost-savings/) 代表了 AWS 上基于 LLM 的应用程序的能力和效率的重大飞跃。开发人员必须随时了解这些发展，将这些工具和考虑因素集成到他们的应用程序中，以充分利用 AWS 和 LLM 技术的潜力。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、采访、演示等。