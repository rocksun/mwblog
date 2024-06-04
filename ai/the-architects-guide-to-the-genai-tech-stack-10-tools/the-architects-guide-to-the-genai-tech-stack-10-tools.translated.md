# 架构师指南：GenAI 技术栈 — 10 种工具

![GenAI 技术栈架构师指南的特色图片 — 10 种工具](https://cdn.thenewstack.io/media/2024/05/664f3fb5-tools-1024x576.jpg)

我之前写过关于 [现代数据湖参考架构](https://thenewstack.io/the-architects-guide-a-modern-data-lake-reference-architecture/)，解决了每个企业面临的挑战 — 更多数据、老化的 Hadoop 工具（特别是 HDFS）以及对 RESTful API（S3）和性能的更大需求 — 但我想填补一些空白。

现代数据湖，有时称为数据湖仓，一半是数据湖，一半是基于开放表格式规范 (OTF) 的数据仓库。两者都建立在现代对象存储之上。

同时，我们深入思考了组织如何构建 AI 数据基础设施，以支持所有 AI/ML 需求 — 不仅仅是训练集、验证集和测试集的原始存储。换句话说，它应该包含训练大型语言模型、MLOps 工具、分布式训练等所需的计算能力。

基于这一思路，我们撰写了另一篇关于如何使用现代数据湖 [参考架构来支持 AI/ML](https://resources.min.io/c/ai-ml-within-a-modern-datalake?x=P9k0ng&lx=exvNTw) 需求的论文。下图展示了 [现代数据湖参考架构](https://resources.min.io/c/modern-datalake-reference-architecture?x=P9k0ng&lx=exvNTw)，其中突出了生成式 AI 所需的功能。

![](https://cdn.thenewstack.io/media/2024/05/6e1f47dc-image2.jpg)

来源： [现代数据湖中的 AI/ML](https://resources.min.io/c/ai-ml-within-a-modern-datalake?x=P9k0ng&lx=exvNTw)

这两篇论文都没有提到特定的供应商或工具。我现在想讨论构建现代数据湖所需的供应商和工具。在这个前 10 名单中，每个条目都是支持生成式 AI 所需的功能。

## 1. 数据湖

企业数据湖建立在对象存储之上。不是你老式的基于设备的对象存储，它服务于廉价且深入的归档用例，而是现代的、高性能的、软件定义的和 Kubernetes 原生的对象存储，这是现代 GenAI 堆栈的基石。它们可用作服务（ [AWS](https://aws.amazon.com/?utm_content=inline+mention)，[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure）或本地或混合/两者，例如 MinIO。

这些数据湖必须支持流式工作负载，必须具有高效的加密和纠删码，需要以原子方式将元数据与对象一起存储，并支持 Lambda 计算等技术。鉴于这些现代替代方案是云原生的，它们将与其他 [云原生技术](https://thenewstack.io/cloud-native/) 的整个堆栈集成 — 从防火墙到可观察性再到用户和访问管理 — 开箱即用。

## 2. 基于 OTF 的数据仓库

对象存储也是基于 OTF 的数据仓库的基础存储解决方案。将对象存储用于数据仓库听起来可能很奇怪，但以这种方式构建的数据仓库代表了下一代数据仓库。这得益于 Netflix、Uber 和 Databricks 编写的 OTF 规范，它使在数据仓库中无缝使用对象存储成为可能。

OTF — Apache Iceberg、Apache Hudi 和 Delta Lake — 的编写是因为市场上没有能够满足创建者数据需求的产品。从本质上讲，它们（以不同的方式）所做的就是定义一个可以构建在对象存储之上的数据仓库。对象存储提供了其他存储解决方案无法提供的可扩展容量和高性能的组合。

由于这些是现代规范，因此它们具有旧式数据仓库所没有的高级功能，例如分区演进、模式演进和零拷贝分支。

可以在 MinIO 上运行其基于 OTF 的数据仓库的两个 MinIO 合作伙伴是 Dremio 和 Starburst。

[Dremio Sonar（数据仓库处理引擎）](https://docs.dremio.com/current/sonar/)
[Dremio Arctic（数据仓库目录）](https://docs.dremio.com/cloud/arctic/)
[开放数据湖仓 | Starburst（目录和处理引擎）](https://www.starburst.io/solutions/open-data-lakehouse/)

## 3. 机器学习运维 (MLOps)

MLOps 对机器学习来说就像 DevOps 对传统软件开发一样。两者都是旨在改善工程团队（开发或机器学习）和 IT 运维（运维）团队之间协作的一组实践和原则。目标是使用自动化简化开发生命周期，从规划和开发到部署和运维。这些方法的主要好处之一是持续改进。
### MLOps 技术和功能

MLOps 技术和功能不断发展。您需要一个由主要参与者支持的工具，以确保该工具不断开发和改进，并提供长期支持。这些工具中的每一个都在底层使用 MinIO 来存储模型生命周期中使用的工件。

## 4. 机器学习框架

您的机器学习框架是您用来创建模型并编写训练它们代码的库（通常用于 Python）。这些库功能丰富，因为它们提供了一系列不同的损失函数、优化器、数据转换工具和神经网络的预构建层。这两个库提供的最重要的功能是张量。张量是可以移动到 GPU 上的多维数组。它们还具有自动微分，用于模型训练。

当今最流行的两个机器学习框架是 PyTorch（来自 Facebook）和 Tensorflow（来自 Google）。

## 5. 分布式训练

分布式模型训练是在多个计算设备或节点上同时训练机器学习模型的过程。这种方法可以加快训练过程，尤其是在需要大型数据集来训练复杂模型时。

在分布式模型训练中，数据集被分成较小的子集，每个子集由不同的节点并行处理。这些节点可以是集群中的各个机器、各个进程或 Kubernetes 集群中的各个 Pod。它们可能可以访问 GPU。每个节点独立处理其数据子集并相应地更新模型参数。以下五个库使开发人员免受分布式训练的大部分复杂性影响。如果您没有集群，可以在本地运行它们，但您需要一个集群才能看到训练时间显着减少。

- [DeepSpeed（来自 Microsoft）](https://www.deepspeed.ai/)
- [Horovod（来自 Uber）](https://horovod.ai/)
- [Ray（来自 Anyscale）](https://www.ray.io/)
- [Spark PyTorch Distributor（来自 Databricks）](https://www.databricks.com/blog/2023/04/20/pytorch-databricks-introducing-spark-pytorch-distributor.html)
- [Spark TensorFlow Distributor（来自 Databricks）](https://docs.databricks.com/en/_extras/notebooks/source/deep-learning/spark-tensorflow-distributor.html)

## 6. 模型中心

模型中心实际上并不是现代数据湖参考架构的一部分，但我还是将其包括在内，因为它对于快速入门生成式 AI 非常重要。Hugging Face 已成为获取大型语言模型的去处。Hugging Face 托管着一个模型中心，工程师可以在其中下载预训练模型并分享他们自己创建的模型。Hugging Face 也是 Transformers 和 Datasets 库的作者，这些库与大型语言模型 (LLM) 及用于训练和微调它们的数据配合使用。

还有其他模型中心。所有主要的云供应商都有一些上传和共享模型的方法，但 Hugging Face 凭借其模型和库集合已成为该领域的领导者。

## 7. 应用程序框架

应用程序框架有助于将 LLM 纳入应用程序。使用 LLM 与使用标准 API 不同。必须做大量工作才能将用户请求转换为 LLM 可以理解和处理的内容。例如，如果您构建了一个聊天应用程序，并且您想使用检索增强生成 (RAG)，那么您需要对请求进行标记化，将标记转换为向量，与向量数据库（如下所述）集成，创建一个提示，然后调用您的 LLM。生成式 AI 的应用程序框架将允许您将这些操作链接在一起。

当今使用最广泛的应用程序框架是 LangChain。它与其他技术集成，例如 Hugging Face Transformer 库和 Unstructured 的文档处理库。它功能丰富，使用起来可能有点复杂，因此下面列出了一些替代方案，供那些没有复杂要求且希望比 LangChain 更简单的东西的人使用。

## 8. 文档处理

大多数组织没有一个包含干净准确文档的单一存储库。相反，文档分散在组织的各个团队门户中，采用多种格式。为生成式 AI 做准备时的第一步是构建一个管道，该管道仅获取已批准与生成式 AI 一起使用的文档，并将它们放入您的向量数据库中。对于大型全球组织来说，这可能是生成式 AI 解决方案最困难的任务。

文档管道应将文档转换为文本，对文档进行分块，并将分块文本通过嵌入模型运行，以便可以将它的向量表示保存到向量数据库中。幸运的是，一些开源库可以针对许多常见文档格式执行此操作。下面列出了一些库。这些库可以与 LangChain 一起使用来构建完整的文档处理管道。
## 9. 向量数据库

向量数据库促进了语义搜索。理解如何做到这一点需要大量的数学背景，并且很复杂。然而，语义搜索在概念上很容易理解。假设您想找到所有讨论与“人工智能”相关的任何内容的文档。要在传统数据库上执行此操作，您需要搜索“人工智能”的所有可能的缩写、同义词和相关术语。您的查询看起来像这样：

```
(人工智能) OR (AI) OR (机器学习) OR (深度学习) OR ...
```

这种手动相似性搜索不仅艰巨且容易出错，而且搜索本身也非常缓慢。向量数据库可以接受如下请求，并更快、更准确地运行查询。如果您希望使用检索增强生成，那么快速准确地运行语义查询的能力非常重要。

下面列出了四个流行的向量数据库：

- Milvus
- Pinecone
- Weaviate
- Vespa

## 10. 数据探索和可视化

拥有允许您整理数据并以不同方式对其进行可视化的工具始终是一个好主意。下面列出的 Python 库提供了数据处理和可视化功能。这些看起来像是您仅在传统 AI 中需要的工具，但它们在生成式 AI 中也很有用。例如，如果您正在进行情绪分析或情感检测，那么您应该检查您的训练、验证和测试集，以确保您在所有类别中都有适当的分布。

## 结论

您已经了解了十种功能，这些功能可以在现代数据湖参考架构中找到，以及针对每种功能的具体供应商产品和库。下面是一个总结这些工具的表格：

| 功能 | 供应商产品/库 |
|---|---|
| 数据湖 | Databricks Lakehouse Platform, Azure Data Lake Storage |
| 基于 OTF 的数据仓库 | Snowflake, Google BigQuery |
| 机器学习框架 | TensorFlow, PyTorch, Keras |
| 机器学习操作 | Kubeflow, MLflow |
| 分布式训练 | Horovod, Ray |
| 模型中心 | ModelDB, Neptune |
| 应用框架 | Flask, Django, Spring Boot |
| 文档处理 | spaCy, NLTK, Gensim |
| 向量数据库 | Milvus, Pinecone, Weaviate, Vespa |
| 数据探索和可视化 | Pandas, Matplotlib, Seaborn |

[YouTube.com/TheNewStack](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。