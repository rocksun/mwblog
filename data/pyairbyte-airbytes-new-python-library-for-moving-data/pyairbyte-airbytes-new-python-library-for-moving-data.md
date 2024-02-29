<!--
title: PyAirbyte：Airbyte的新Python库，助力数据迁移
cover: https://cdn.thenewstack.io/media/2024/02/fbca0c5d-airbyte-1024x703.png
-->

[AirByte](https://airbyte.io/)发布了一个开源的Python库，旨在帮助Python程序员加快连接数据源与目标地点的过程。

> 译自 [PyAirbyte: Airbyte’s New Python Library for Moving Data](https://thenewstack.io/pyairbyte-airbytes-new-python-library-for-moving-data/)，作者 Joab Jackson 是《The New Stack》的资深编辑，涵盖云原生计算和系统运维。他已经报道了 IT 基础设施和开发工作超过 25 年，包括在 IDG 和 Government Computer News 的任职。

[AirByte](https://airbyte.io/) 数据平台提供商发布了一个开源的 Python 库，以帮助加快 Python 程序员连接数据源与其他目标的过程。

PyAirbyte 提供了超过 250 个数据连接器，用于通过 API 桥接不同的应用程序。它还与开源的编排工具（如 [Dagster](https://dagster.io/)）配合使用。在 LLM 方面，连接器可以与 [LangChain](https://thenewstack.io/pulumi-templates-for-genai-stacks-pinecone-langchain-first/) 配合使用，用于创建使用[大语言模型](https://thenewstack.io/large-language-models-open-source-llms-in-2023/)（LLMs）的应用程序。

根据[文档](https://docs.airbyte.com/pyairbyte)，PyAirbyte "旨在用于在设置 Airbyte 服务器或云帐户不可行或不可取的情况下使用，例如在 [Jupyter 笔记本](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/)中或在开发人员工作站上迭代早期原型时"。

Airbyte 的联合创始人兼 CEO [Michel Tricot](https://www.linkedin.com/in/micheltricot/) 在一份声明中表示：“今天，绝大多数现有的数据管道都是用 Python 编写的。” “我们看到了对这种能力的不断增长的需求，这与编码工作流程自然契合，只需要运行一个命令。”

![](https://cdn.thenewstack.io/media/2024/02/3e85cfaf-airbyte-diagram.png)

[PyAirByte](https://airbytehq.github.io/PyAirbyte/index.html) 与 Python 3.9 及更高版本兼容。可以通过 Python 命令行进行安装：

```shell
pip install airbyte
```

在 290 个连接器中包括以下内容：

- [亚马逊广告](https://docs.airbyte.com/integrations/sources/amazon-ads#reference)
- [亚马逊卖家合作伙伴](https://docs.airbyte.com/integrations/sources/amazon-seller-partner#reference)
- [亚马逊 SQS](https://docs.airbyte.com/integrations/sources/amazon-sqs#reference)
- [Auth0](https://docs.airbyte.com/integrations/sources/auth0#reference)
- [AWS CloudTrail](https://docs.airbyte.com/integrations/sources/aws-cloudtrail#reference)
- [Azure Blob 存储](https://docs.airbyte.com/integrations/sources/azure-blob-storage#reference)
- [Azure 表存储](https://docs.airbyte.com/integrations/sources/azure-table#reference)
- [GitHub](https://docs.airbyte.com/integrations/sources/github#reference)
- [GitLab](https://docs.airbyte.com/integrations/sources/gitlab#reference)

由于其简单性，[Python](https://thenewstack.io/what-is-python/) 在数据科学社区被广泛使用作为编程语言，并集成在许多数据分析工具中，如 SQL 数据库、Hadoop 和 Spark。

[Airbyte](https://airbyte.com/) 本身专注于通过 Airbyte Open Source、Airbyte Self-Managed、Airbyte Cloud 和 Powered by Airbyte 等产品，将数据在应用程序、API 和数据库之间同步到数据仓库、数据湖和其他目的地。通过连接器支持平台的开源社区已经拥有超过 800 名贡献者。

该公司的其他数据管道增强功能包括 [Airbyte API](https://reference.airbyte.com/reference/start) 和 [Terraform Provider](https://docs.airbyte.com/terraform-documentation)。

欲了解更多信息，请[注册](https://airbyte.com/session/airbyte-monthly-ai-demo)参加将于 3 月 14 日举行的网络研讨会。
