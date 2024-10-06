
<!--
title: MongoDB 8 专注于时间序列数据和横向扩展
cover: https://cdn.thenewstack.io/media/2024/10/5d6d4528-mongodb.png
-->

优化使数据库系统性能提高了 32%。时间序列聚合使性能提高了 200%，可扩展性提高了 50%。

> 译自 [MongoDB 8 Goes Hard on Time-Series Data, Horizontal Scaling](https://thenewstack.io/mongodb-8-goes-hard-on-time-series-data-horizontal-scaling/)，作者 Joab Jackson。

[MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention) 发布了其同名文档数据库的 [版本 8](https://www.mongodb.com/try)，并针对高端、性能导向的工作负载进行了优化。优化使数据库系统性能提升了 32%。时间序列聚合的速度提高了 200%，可扩展性提高了 50%，数据库的独特功能 [可查询加密](https://thenewstack.io/mongodb-6-0-brings-encrypted-queries-time-series-data-collection/) 扩展到更多类型的查询。

在发布前一个月，该公司还停用了许多使用较少的特性和产品。

[MongoDB](https://thenewstack.io/benchmarking-postgresql-vs-mongodb-for-genai/) 的商业支持 [MongoDB Enterprise 平台](https://www.mongodb.com/atlas) 有超过 50,000 个客户，而基础 [开源数据库](https://github.com/mongodb/mongo) 已在数百万个部署中使用。
对于其商业客户，该公司一直在努力使软件 [更加健壮](https://thenewstack.io/mongodb-builds-out-its-full-platform-play/)。

“各行各业的客户都告诉我们，他们的核心运营数据库的性能至关重要，无论规模如何，”MongoDB 首席技术官 [Jim Scharf](https://www.mongodb.com/company/newsroom/press-releases/mongo-db-announces-jim-scharf-as-chief-technology-officer) 在一份声明中表示。“MongoDB 8.0 旨在超越我们客户最严格的安全、持久性、可用性和性能要求。”

## 时间序列数据处理

这些改进旨在提高各种用例的整体性能，即使是轻微的次优性能也会导致用户不满。

架构中的各种优化通过更智能的内存使用和更高效的查询，从软件中挤出了额外的 32% 的性能提升。

时间序列处理提高了惊人的 200%。一种新的批量处理 INSERT、UPDATE 和 DELETE 的方法将批量写入速度提高了 56%，数据复制并发写入速度提高了 20%。

这意味着该公司声称 MongoDB 可以处理更高数量的时间序列数据，同时执行复杂的聚合。

## 水平扩展

该公司和项目的贡献者也更加努力地提高水平扩展能力，即软件从数千用户扩展到数百万用户的可能性。

这通常通过将数据拆分为多个服务器或分片上的“分片”来完成。从 8.0 版本开始，MongoDB 现在可以将数据分布到多个分片上，速度提高 50%，无需任何额外的配置或设置。

该软件还可以更好地处理工作负载需求的意外峰值。它现在包括设置运行查询的默认最大时间限制、拒绝重复出现的类型的问题查询以及设置查询设置以在数据库重启等事件中持久化，以帮助确保应用程序在高需求情况下保持高性能。

进一步增强 [Kubernetes 用户](https://thenewstack.io/5-reasons-to-run-mongodb-on-kubernetes/) 的弹性是 MongoDB Enterprise Kubernetes Operator 的新多集群支持，用于在本地和地理分布式多个集群中部署 MongoDB。

这可以让用户将部署分散到地理上分离的集群中，以提高弹性。

## 盒子里还有什么？

MongoDB 8 附带的其他改进包括：

* **MongoDB 可查询加密**用于范围函数。这是对之前在网络和存储期间加密数据，甚至在查询时保持加密的工作的后续工作。此扩展现在涵盖了一种新的查询类型，即范围函数。这些查询在最终用户使用适当的解密密钥查看之前保持加密。
* **用于 IntelliJ 的 MongoDB 插件**将帮助 Java 开发人员更有效地编写和测试数据库的 Java 查询。
* **用于 VS Code 的 MongoDB CoPilot 参与者公开预览**为为数据库系统编写的开发人员提供了一个聊天界面，为开发人员提供查询，并直接在 VS Code 中解释模式。

## 其他更改
MongoDB 一直在精简其产品线，主要围绕其 Atlas 云数据服务。上个月，该公司宣布将 [停止](https://medium.com/@stevdza-san/this-is-bad-mongodb-is-shutting-down-their-services-c2c6048d667b) [Atlas Data API 和自定义 HTTP 端点](https://www.mongodb.com/community/forums/t/mongodb-atlas-data-api-and-custom-https-endpoints-end-of-life-and-deprecation/296686)，[Atlas 设备同步和 Atlas 设备 SDK](https://www.mongodb.com/blog/post/realm-now-part-atlas-platform)，[Atlas 数据湖](https://www.metarouter.io/post/the-power-of-mongodb-atlas-data-lake) 和 [Atlas 边缘服务器](https://www.mongodb.com/products/updates/product-support-deprecation)。客户 [可以使用](https://medium.com/@stevdza-san/this-is-bad-mongodb-is-shutting-down-their-services-c2c6048d667b) 这些功能，直到 2025 年 9 月 30 日。

MongoDB 将其路线图设定为满足客户需求，并非所有引入的功能都能找到其受众，MongoDB 产品高级副总裁 [Andrew Davidson](https://www.linkedin.com/in/andrewad/) 在一封电子邮件声明中解释道。

“MongoDB 基于客户反馈进行投资，我们开发路线图以满足他们的需求，”他表示。

然而，该公司拥有广泛的合作伙伴生态系统，这些合作伙伴应该能够提供这些功能。

“我们致力于帮助受影响的客户成功迁移到我们广泛的合作伙伴网络中的其中一个替代解决方案，”他指出。

MongoDB 8.0 现在可通过 [MongoDB Atlas](https://www.mongodb.com/atlas) 在 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)，Google Cloud 和 Microsoft Azure 上使用。MongoDB Enterprise Advanced [现在运行](http://mongodb.com/try) 在 8.0 上。
