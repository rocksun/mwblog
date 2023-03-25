# LinkedIn 使用 Apache Beam 统一流和批处理

翻译自 [LinkedIn Unifies Stream and Batch Processing with Apache Beam](https://thenewstack.io/linkedin-unifies-stream-and-batch-processing-with-apache-beam/) 。

通过迁移到 Apache Beam，社交网络服务 LinkedIn 统一了其流式和批处理源代码文件，并将数据处理时间减少了 94%。

![](https://cdn.thenewstack.io/media/2023/03/63ce913b-shutterstock_2038294955-1024x585.jpg)

通过迁移到 Apache Beam ，社交网络服务 LinkedIn 统一了其流式处理和批处理的源代码文件，将数据处理时间缩短了 94% 。

最初，刷新数据集的作业“回填（backfilling）”是作为一组流处理作业运行的，但随着作业变得越来越复杂，就会出现越来越多的问题，LinkedIn 的一篇多作者博客文章在周四发布时解释说。

然后，回填通过 Lambda 架构作为批处理进行处理，带来了一系列新问题 - 现在有两个不同的代码库，拥有和维护两套源代码带来的所有挑战。 Lambda 架构被 Beam API 取代，它只需要一个源代码文件即可进行批处理和流处理。该项目取得了成功，并且总体资源使用量下降了 50%。

思想领袖和流处理软件公司正在就实时处理与批处理展开辩论。一方坚定地认为，在流处理真正成为主流之前，软件必须变得更易于开发者使用。反驳说，开发人员必须达到更高的技能要求，才能处理组成当前流处理系统的不一致的技术栈和语言。

LinkedIn 最近通过使用 Apache Beam 将其流处理和批处理管道统一，将数据处理时间缩短了 94％ ，这为简化论证提供了一个重大胜利。

## 回填的挑战

LinkedIn 的标准化过程是将用户数据输入字符串（职位名称、技能、教育背景）映射到内部 ID 的过程。标准化数据用于搜索索引和推荐模型。在流水线中还使用更高级的 AI 模型，将复杂数据（工作类型和工作经验）连接起来，以标准化数据以供进一步使用。

标准化需要使用两种方法进行数据处理：实时计算以反映即时更新和定期回填以在引入新模型时刷新数据。当实时计算和回填处理作为流处理时，它们通过运行 Beam 流水线的 Apache Samza Runner 执行。这种方法一直运行正常，直到以下问题变得不可克服：


* 实时作业在回填处理期间未能满足时间和资源要求。
* 由于训练模型变得越来越复杂，每个回填作业要求为每秒 40,000 个/秒，无法实现 9 亿 profiles 的目标。
* 流式集群未针对回填作业的不稳定资源高水位进行优化。

![Figure 1](https://cdn.thenewstack.io/media/2023/03/a3442543-linkedin_original_streaming_architecture-300x270.jpg)

第一次优化将回填处理移至批处理，并使用 Lambda 架构执行逻辑。这是操作上的解决方案，但并不是最优的，因为 Lambda 架构带来了一系列挑战 —— 第二个代码库。引入第二个代码库开始要求开发人员在两种不同的语言和堆栈中构建、学习和维护两个代码库。

该过程的下一次迭代带来了 Apache Beam API 的引入。使用 Apache Beam 意味着开发人员可以返回处理一个源代码文件。

## 解决方案：Apache Beam

Apache Beam 是一个开源的统一的模型，用于定义批处理和流处理的数据并行处理流水线。开发人员可以使用开源 Beam SDK 之一构建程序来定义流水线。然后，流水线由 Beam 的分布式处理后端之一执行，其中有几个选项，如 Apache Flink、Spark 和 Google Cloud Dataflow。

![](https://cdn.thenewstack.io/media/2023/03/ab1e5b44-linkedin_beam_architecture.jpg)

在这个特定的用例中，统一的管道由 Beam 的 Samza 和 Spark 后端驱动。Samza 每天处理 2 万亿条消息，具有大规模状态和容错能力。Beam Samza Runner 作为 Samza 应用程序在本地执行 Beam 流水线。Spark 后端使用 LinkedIn 的 eternal shuffling 服务和模式元数据存储处理 PB 级数据。Beam Apache Spark Runner 就像本地的 Spark 应用程序一样，使用 Spark 执行 Beam 流水线。

## 如何实现的

Beam 流水线管理一个有向无环图的处理逻辑。下面的图示流水线读取 ProfileData，将其与 sideTable 进行连接，应用名为 Standardizer() 的用户定义函数，并通过将标准化结果写入数据库来完成。这段代码片段由 Samza 集群和 Spark 集群执行。

即使在使用相同源代码的情况下，批处理和流处理作业接受不同的输入并返回不同的输出，即使在使用 Beam 时也是如此。流处理输入来自无界源，如 Kafka，它们的输出会更新数据库，而批处理输入来自有界源，如 HDFS，并生成数据集作为输出。

PTransforms 是 Beam 工作流中开箱即用的步骤，它从任一来源获取输入并执行处理功能，然后产生零个或多个输出。 LinkedIn 添加了功能以进一步简化其 Unified PTransforms 中的 Beam API。 Unified PTransforms 为流和批处理提供了两个 expand() 函数。在运行时检测管道类型，并相应地调用适当的 expand()。

![成功指标](https://cdn.thenewstack.io/media/2023/03/295f1f62-linkedin_unified_ptransforms.jpg)

以流处理的原始回填处理方法需要超过 5,000 GB-小时的内存和近 4,000 小时的 CPU 时间。迁移到 Beam 后，这些数字减少了一半。完成作业所需的七个小时缩短为迁移后的仅 25 分钟。

![](https://cdn.thenewstack.io/media/2023/03/daeacc64-linkedin_success_metrics.jpg)

总体而言，这意味着节省了 94% 的处理时间和 50% 的总体资源使用。基于成本分析，操作成本降低了 11 倍。

## 展望未来

这只是迈向真正的端到端融合解决方案的第一步。LinkedIn 继续致力于降低使用流式处理和批处理解决方案的复杂性。尽管只有一个源代码文件，但不同的运行时二进制堆栈（流中的 Beam Samza 运行器和批处理中的 Beam Spark 运行器）仍然会带来额外的复杂性，例如学习如何运行、调整和调试两个集群、操作和两个引擎运行时的维护成本，以及两个运行器代码库的维护。

LinkedIn 高级软件工程师 Yuhong Cheng 是 LinkedIn 帖子的主要作者，Yuhong Cheng、Shangjin Zhang、Xinyu Liu 和 Yi Pan 是共同作者。

