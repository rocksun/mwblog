<!-- 
# MySQL HeatWave获取生成式AI和JavaScript等强大新功能
https://cdn.thenewstack.io/media/2023/09/d96f03f1-lakeside-7403897_1280-1024x692.jpg
 -->

除了获取Generative AI和JavaScript的支持外，甲骨文的MySQL HeatWave“另一个数据库”还获取了数据湖仓库、机器学习、AutoPilot、分析、OLTP和多云等一系列强大的新功能。

译自 [MySQL HeatWave Gets Generative AI and JavaScript， Slew of New Features](https://thenewstack.io/mysql-heatwave-gets-generative-ai-and-javascript-slew-of-new-features/) 。

随着甲骨文CloudWorld大会本周在拉斯维加斯召开，甲骨文的MySQL团队宣布MySQL HeatWave平台获得了一系列强大的增强功能，这不仅增强了其核心功能，还增加了生成式AI的支持，改进了对采用数据湖仓库方式进行分析数据管理、自治运维和数据库内机器学习的支持，并提升了核心编程性能和OLTP方面的效果。

## 开发者福音

MySQL团队首先从分析方面入手介绍新功能，而将面向开发者的功能留到最后。对我们The New Stack的读者来说，我认为他们把最大的亮点藏到了最后，所以我要先从MySQL团队最后才提到的开发者福音开始：即为开发者提供了JavaScript和JSON支持。

基础MySQL平台对JSON的支持可以将JSON数据物化到表中的二进制列、文本列或虚拟列中。它还允许将JSON payload作为参数传递给存储过程和函数。MySQL支持在客户端使用兼容MongoDB API的[XDevAPI](https://dev.mysql.com/doc/x-devapi-userguide/en/)，并且MySQL shell可以使用多种编程语言来操作JSON数据的输入和输出。现在JSON数据可以导入到HeatWave中，以二进制格式存储，进行分区和压缩，并可以横向扩展到多个节点。MySQL团队表示，简单的过滤器查询可以提速20倍，聚合查询可提速22倍，大型连接查询可提速144倍。

除了支持JSON格式，现在HeatWave的存储过程也可以使用JavaScript语言进行编码，此前只支持SQL。SQL是声明式的基于集合的语言，这使其难以执行更具命令性的任务。JavaScript存储过程和函数消除了这种限制，调用和使用方式与基于SQL的完全相同，无论是在查询、视图、数据操作语言命令还是数据定义语言命令中。

这两种语言之间的数据类型转换是隐式实现的。 JavaScript代码在[GraalVM](https://www.graalvm.org/)虚拟机中执行，提供了安全的沙箱计算和内存使用，并阻止直接网络和文件系统访问。

## 数据湖仓库功能加强

接下来看看HeatWave的数据湖仓库功能，它有多个方面的加强。首先，HeatWave开始支持[Apache Avro](https://avro.apache.org/)数据文件格式，以增强对CSV和[Apache Parquet](https://parquet.apache.org/)格式的兼容性。该功能支持多种压缩算法，在不同算法之间性能一致。Avro支持还包括利用HeatWave的“[Autopilot](https://www.mysql.com/products/mysqlheatwave/autopilot/)”自动驾驶功能进行模式推断、数据加载操作的集群容量估计以及时间估计。

公告的关键是，HeatWave现在支持了一种针对行式数据进行了优化的数据格式。与未优化的基于文本的CSV和列式的Parquet格式相比，可以看出甲骨文的MySQL团队不仅重视分析工作负载，也关注OLTP工作负载，这是HeatWave的原始卖点。同时，分析方面还可以从支持Parquet标准之上的开源表格式[Delta](https://delta.io/)、[Iceberg](https://iceberg.apache.org/)和[Hudi](https://hudi.apache.org/)中受益。

接下来，HeatWave增加了在亚马逊网络服务云上运行的支持。这意味着客户在[亚马逊S3](https://aws.amazon.com/s3/)对象存储中已经存在的任何格式的数据现在都可以在HeatWave中处理。即使HeatWave本身运行在甲骨文自己的AWS账户中，但仍可以连接到客户账户中的数据。简单地在CREATE TABLE命令中提供ENGINE = LAKEHOUSE子句，就可以将S3数据添加到HeatWave，该命令本身可以通过Autopilot自动生成，利用之前讨论的模式推理。

## AutoML增强，支持生成式AI

在AI领域，HeatWave的AutoML(自动机器学习)可以利用这种S3数据访问(包括新的Avro支持)在HeatWave内构建机器学习模型，并在HeatWave数据上训练。HeatWave AutoML还支持推荐模型，而不仅仅是其他AutoML平台通常支持的分类、回归、聚类/异常检测和时间序列预测模型。

在竞争方面，甲骨文声称HeatWave的训练速度比[亚马逊Redshift](https://aws.amazon.com/redshift/)快25倍，这意味着作为AWS的数据仓库，HeatWave优于亚马逊自己的Redshift。与Snowflake的[SnowPark ML](https://docs.snowflake.com/en/developer-guide/snowpark-ml/index)相比，后者仅提供一个[scikit-learn](https://scikit-learn.org/stable/index.html#)的桥接，没有内置的AutoML。

MySQL AutoML中还支持生成AI，有两种形式：支持[大语言模型(LLM)](https://thenewstack.io/nvidia-shaves-up-to-30-off-large-language-model-training-times/)和内置向量存储。 在LLM方面，HeatWave可以使用[BERT](https://huggingface.co/docs/transformers/model_doc/bert)和[Tfidf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)从数据库文本列内容生成嵌入，并与标量数据列的数值表示一起提交给AutoML。从所有这些输入生成优化的模型。

对象存储中的文档也可以转换为向量嵌入，存储和索引到HeatWave向量存储中。结合使用，这些功能可以对生成式AI查询给出更具上下文的答案，因为向量存储中的数据可以用来增强发送到LLM的提示。

## Autopilot自动驾驶增强

接下来看看HeatWave的Autopilot自动驾驶功能，它使用AI实现自动化操作或高级功能的辅助。团队为Autopilot添加了索引、自动卸载、自动压缩和自适应查询执行的支持。根据MySQL团队的说法，后者可以在查询执行开始后，根据遇到的数据分布动态调整数据结构和系统资源，第一次运行可以将性能提高10%到25%。

Autopilot索引是一种基于机器学习的服务，它可以为OLTP工作负载推荐辅助索引，包括建议新索引和识别无用的重复索引应该删除的建议。Autopilot索引会考虑查询和DML操作，如UPDATE、INSERT和DELETE。该服务还可以预测存储需求和性能，并解释其建议的原因。

自动加载和卸载根据访问频率将数据在常规MySQL数据库和HeatWave集群之间移动，帮助开发人员避免手动执行这些操作。自动列压缩会为每个列选择匹配的压缩算法，在内存使用和性能之间找到最佳平衡。公司称内存节省可达6-25%，性能提升可达6-10%。在内存和性能之间进行算法优化，而不是让开发人员在两者间作选择，这证明了其价值。

## 更多

其他功能还包括批量数据加载、分区、分析函数、SET操作，以及在多云([AWS](https://aws.amazon.com/?utm_content=inline-mention)、Azure和[Oracle Cloud](https://www.oracle.com/cloud/))上的运行支持。这些功能加强了MySQL HeatWave的持续发展势头，甲骨文称在数字营销、游戏、医疗保健和金融科技领域已经看到了这种势头。这充分展示了甲骨文将MySQL视为产品组合中的战略资产。甲骨文数据库自己是否主宰一切?也许吧。但拥有数十年生态系统和大社区的MySQL，以其模块化、可插拔的引擎体系结构，已经在云、分析、机器学习和现在的生成式AI中焕发出新的生机。
