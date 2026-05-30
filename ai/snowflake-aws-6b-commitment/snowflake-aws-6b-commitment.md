<!--
title: Snowflake承诺向AWS投入60亿美元，加速布局AI
cover: https://cdn.thenewstack.io/media/2026/05/0507016d-img_2913-scaled.jpg
summary: Snowflake宣布五年内向AWS承诺投入60亿美元，用于采购Graviton计算和GPU加速实例，旨在通过强化AI基础设施加速向“AI时代平台”转型。
-->

Snowflake宣布五年内向AWS承诺投入60亿美元，用于采购Graviton计算和GPU加速实例，旨在通过强化AI基础设施加速向“AI时代平台”转型。

> 译自：[Snowflake commits $6B to AWS as it pushes deeper into AI](https://thenewstack.io/snowflake-aws-6b-commitment/)
> 
> 作者：Frederic Lardinois

Snowflake 正向亚马逊云科技（AWS）承诺在五年内投入 60 亿美元，用于 Graviton 计算和 AI 基础设施，这是该数据公司迄今为止最大的一笔云支出承诺，也是其在 AI 领域雄心的明确信号。

这一多年期战略合作协议由 AWS 于周三宣布，涵盖了 AWS 基于 ARM 的 Graviton 处理器以及 GPU 加速的 EC2 实例，Snowflake 将利用这些资源进行 AI 模型的训练和推理。

有趣的是，这里并没有提到 AWS 的专用 Trainium 芯片（尽管有搭载 Trainium 芯片的[加速 EC2 实例](https://aws.amazon.com/ec2/instance-types/trn2/)）。由于 AWS 的公告特别提及了“GPU 加速”实例，因此这里的重点很可能是英伟达（Nvidia）GPU。

鉴于 Snowflake 支持多种云厂商，该公司可能不希望将自己绑定在特定厂商的平台上（并为此投入工程资源来提供支持）。对于基于 ARM 的通用计算实例，目前这方面的担忧要少得多。

该交易还扩大了双方通过 AWS Marketplace 的联合入市（go-to-market）合作，AWS 表示 Snowflake 在该市场上的累计销售额现已超过 70 亿美元。

60 亿美元的承诺本身就非常引人注目（毕竟这相当于 [6 个 Instagram](https://techcrunch.com/2012/04/09/facebook-to-acquire-instagram-for-1-billion/)），但同样有趣的是，Snowflake 将使用 AWS 具有成本效益的 Graviton 实例来为其传统的数仓业务提供动力，从而可能腾出资金用于极其昂贵的 AI 训练和推理工作负载。

## Snowflake 的 AI 转型

在 CEO [Sridhar Ramaswamy](https://www.linkedin.com/in/sridhar-ramaswamy/)（于 2024 年接替 Frank Slootman）的领导下，Snowflake 正从云数据仓库重新定位为该公司如今所称的“AI 时代的平台”。

Cortex AI 是 Snowflake 的一系列 AI 产品套件，允许客户直接在 Snowflake 内部受监管的数据上构建和部署用于 text-to-SQL（文本转 SQL）、摘要、情感分析和实体抽取的应用程序。通过 Cortex Code，Snowflake 还提供了一个 AI 编码助手。

“我们正在步入智能体企业（agentic enterprise）时代，在这个时代，AI 系统不仅能回答问题，还能帮助企业对可信数据进行推理、协调工作流并推动真正的业务成果，”Ramaswamy 在公告中表示。“通过与 AWS 合作，我们让企业能够更轻松地将 AI 直接引入受监管的数据中。”

## Snowflake 扩展其 AWS 区域

Snowflake 还将其 AWS 业务版图扩展至 10 个新区域，包括新西兰、南非、泰国以及 AWS 欧洲主权云。考虑到企业正越来越多地面临本地化数据驻留要求（尤其是在欧洲），主权云这部分尤为重要。对于许多公司而言，支持这些要求正成为选择供应商的先决条件，而不仅仅是针对 AI 工作负载。

## Snowflake 峰会

值得注意的是，Snowflake 的年度峰会（Summit）将于 6 月 1 日至 4 日在旧金山举行。无需水晶球也能预测，我们届时将在会上听到更多关于该公司 AI 重点以及它计划如何使用所有这些计算资源的消息。