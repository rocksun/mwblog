# 使用 SQL 支持的 RAG 更好地分析数据库数据与 GenAI

![使用 SQL 支持的 RAG 更好地分析数据库数据与 GenAI 的特色图片](https://cdn.thenewstack.io/media/2024/04/fe2bcf3a-paris-je-taime-1024x576.jpeg)

您知道您的组织需要开始利用生成式 AI (GenAI)。但您如何开始？由于数据存储在包含公司关键信息的数据库中，因此将 [大型语言模型 (LLM)](https://thenewstack.io/llm/) 应用于该数据可能看起来很复杂。但是，您实际上可以使用 [SQL](https://thenewstack.io/how-to-write-sql-queries/) 支持的检索增强生成 (RAG) 在 Oracle 自治数据库中分析数据，只需几分钟。

## 什么是检索增强生成 (RAG)？

RAG 允许您将 LLM 的强大功能（例如创造力、对语言细微差别的深刻理解）应用于模型几乎或完全不了解的信息。这种缺乏知识可能是因为信息是私有的（例如，在您的数据库中）或比模型的训练数据更新。通过用权威信息增强 AI 生成的内容，RAG 可以帮助 [提高 GenAI 输出的准确性、相关性和可靠性](https://thenewstack.io/retrieval-augmented-generation-for-llms/)。

RAG 通常与 [向量数据库](https://thenewstack.io/vector-databases-where-geometry-meets-machine-learning/) 相关联，后者通过允许从存储引擎（例如，非结构化数据、PDF、文档）超快速检索类似数据，而不是仅仅精确关键字匹配，从而帮助为 LLM 提供上下文。要使用 RAG 获得见解：

- 使用自然语言定义您的任务。
- 对您的数据执行向量相似性搜索以获取上下文。
- 将该信息传递给 LLM。

您现在可以回答一个自然语言问题，例如：“我的客户认为这套公寓很漂亮。波士顿地区还有哪些公寓看起来像那套，并且在她的价格范围内？”这会返回她可以负担得起的相似外观的房屋，这些房屋基于图像相似性和数据库中包含的她的私人财务信息。

## 什么是 SQL 支持的 RAG？

还有其他方法可以为 LLM 提供上下文，这些方法更简单，但可能不如上面描述的那么强大。此方法适用于可供您的自治数据库部署访问的数据（例如，内部表、数据湖、链接表）。要将 RAG 与自治数据库配合使用：

- 使用自然语言定义您的任务。
- 对您的数据提供一个 SQL 查询以获取上下文。
- 将该信息传递给 LLM。

从概念上讲，这看起来与使用向量数据库的 RAG 非常相似。以下是如何在自治数据库中使用示例 Oracle APEX 应用程序应用这些步骤的示例。

## 使用 SQL 支持的 RAG

自治数据库提供了一个名为 Select AI 的功能，允许您将 LLM 与您的数据一起使用。使用 Select AI 的一种流行方式是进行自然语言查询（请参阅 [自治数据库说“人类”](https://blogs.oracle.com/datawarehousing/post/autonomous-database-speaks-human?source=:ex:pw:::::&SC=:ex:pw:::::&pcode=) 和 [对话是自然语言查询的下一代](https://blogs.oracle.com/datawarehousing/post/conversations-are-the-next-generation-in-natural-language-queries?source=:ex:pw:::::TNS2&SC=:ex:pw:::::TNS2&pcode=))。

这与自然语言查询有点不同；它不是生成查询，而是将 SQL 查询的结果与任务指令相结合以生成提示。该提示被传递给 LLM 并进行处理，从而产生建议、摘要或您的项目要求它执行的任何操作。要实现此目的：

- 将自治数据库连接到 LLM，例如 OCI 生成式 AI 上的 Cohere。
- 使用自然语言告诉 LLM 您想要完成什么。
- 定义一个包含您要分析的信息的查询。
- 将数据和指令打包到一个“增强”提示中。
- 将增强提示发送到 LLM 并获取结果。

以下是每个步骤的代码示例。如果您想自己运行这些步骤，请查看此 [LiveLabs 研讨会](https://apexapps.oracle.com/pls/apex/r/dbpm/livelabs/view-workshop?wid=3910)。

### 1. 将自治数据库连接到 LLM

Select AI 使用 AI 配置文件封装与 AI 提供商的连接信息。使用 [DBMS_CLOUD_AI.create_profile PLSQL 过程](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/dbms-cloud-ai-package.html#GUID-D51B04DE-233B-48A2-BBFA-3AAB18D8C35C) 创建配置文件：

- 此配置文件连接到 OCI 生成式 AI，但您可以连接到其他提供商，例如 OpenAI 和 Azure OpenAI。
- OCI 生成式 AI 支持多个模型；上述连接到 cohere.command LLM。
- 凭据用于对请求进行签名。这使用自治数据库
**资源主体**（[https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/resource-principal.html#GUID-E283804C-F266-4DFB-A9CF-B098A21E496A](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/resource-principal.html#GUID-E283804C-F266-4DFB-A9CF-B098A21E496A)）这意味着您的数据库实例需要使用身份管理 (IAM) 策略访问 OCI Generative AI 服务。对于 Azure OpenAI 等服务，必须使用您的秘密 API 密钥创建凭证。

### 2. 使用自然语言告诉 LLM 您想做什么

围绕 [提示工程](https://roadmap.sh/prompt-engineering) 出现了一门新兴科学，试图回答这个问题：“向 LLM 提供指令的最佳方式是什么？”您需要测试不同的提示，以了解哪些提示能产生最佳结果。以下是一个示例：

- 挑选 5 件在该地点可以做的很棒的事情
- 鼓励客户执行这些建议。
- 考虑提供的所有有关客户的信息，包括家庭或宠物情况、是否有车以及收入水平。
- 使用表情符号设置结果格式，并使其有趣。

### 3. 使用您想要分析的信息定义查询

LLM 不了解前往该地点的人员。提供一个数据库查询，使用旅客的个人资料来扩充指令：

### 4. 将数据和指令打包到扩充提示中

您需要向 LLM 提供明确的指令，以帮助它产生最佳结果。提供 JSON 文档是组织这些指令的绝佳方式，并且使用 Autonomous Database 的内置 JSON_OBJECT 函数将 SQL 查询打包为 JSON 非常容易：

此查询返回一个结构良好的 JSON 文档：

### 5. 将扩充提示发送到 LLM 并获取结果

Select AI 提供了一个简单的函数 [DBMS_CLOUD_AI.GENERATE](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/dbms-cloud-ai-package.html#GUID-7B438E87-0E9A-4318-BA01-3BE1A5851229) 用于与 LLM 通信。它使用之前创建的个人资料，从而可以轻松测试来自不同提供商的结果：

查看 Jennine 的结果：

以下是根据您的偏好和情况为您在巴黎推荐的五项活动：

- 🥂 参观埃菲尔铁塔，与您的配偶享用浪漫的野餐。🍽️ 在享用一些法式美食的同时，欣赏这座爱情之城的壮丽景色。别忘了拍一些照片留念！
- ✨ 在卢浮宫沉浸在艺术氛围中。🎨 探索大量的杰作，在陈列着《蒙娜丽莎》等标志性艺术品的走廊中流连忘返。花时间欣赏各种艺术形式，深入了解法国的历史和文化。
- 🚶 体验蒙马特的魅力，漫步在鹅卵石街道上。✨ 探索毕加索和梵高等艺术家喜爱的充满活力的街区。从圣心大教堂的顶部欣赏城市迷人的景色，同时欣赏这个独特的巴黎街区的迷人氛围。
- ☕️ 在一家古色古香的咖啡馆享受奢华的咖啡时光。🧐 在探索这座城市时，在一家迷人的咖啡馆休息一下，享用最棒的法式糕点和香浓的咖啡。享受观赏人群的乐趣，一瞥当地人的生活方式。
- 🐶 如果您是动物爱好者，可以考虑参观卢森堡花园。🐶 这个郁郁葱葱的公园不仅是放松和欣赏大自然的好地方，还有一个专门的区域，您可以在那里欣赏四处游荡的可爱流浪猫。如果您愿意，还可以带上自己的零食来喂猫。

我希望这些建议对您有所帮助！如果您有任何偏好或其他信息希望我考虑，请告诉我，我将很乐意提供更多个性化建议。

在巴黎玩得开心！

请注意，虽然上述建议主要是为了让您享受，但在访问巴黎期间进行彻底的研究并提前预订或预订总是明智之举，以确保您获得顺畅的体验。

旅途愉快，享受您的住宿！

我认为 Jennine 会在巴黎度过一段美好的时光！

## 摘要

GenAI 极其强大，借助合适的工具，您可以轻松将其应用于您组织的数据。试一试吧！查看链接以获得实践经验。

- [了解有关 RAG 的更多信息](https://www.oracle.com/artificial-intelligence/generative-ai/retrieval-augmented-generation-rag/?source=:ex:pev:::::TNS3&SC=:ex:pev:::::TNS3&pcode=)
- LiveLab：
  - [使用 GenAI、Autonomous Database 和 React 开发应用](https://apexapps.oracle.com/pls/apex/r/dbpm/livelabs/view-workshop?wid=3910)
- Livelab：
  - [使用生成式 AI 在 Autonomous Database 中与您的数据聊天](https://apexapps.oracle.com/pls/apex/r/dbpm/livelabs/view-workshop?wid=3831) [
    YOUTUBE.COM/THENEWSTACK
    技术发展迅速，不要错过任何一集。订阅我们的 YouTube
[频道](https://youtube.com/thenewstack?sub_confirmation=1)，用于播放我们所有的播客、访谈、演示等。