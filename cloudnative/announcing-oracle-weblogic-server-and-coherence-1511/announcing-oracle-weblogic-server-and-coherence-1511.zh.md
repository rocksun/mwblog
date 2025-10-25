Oracle 很高兴宣布推出 Oracle WebLogic Server 和 Coherence 15.1.1 版本！新版本带来了对 Jakarta EE 9.1 的更新支持，继续兼容 Java SE 17 和 21，并全面支持运行 Spring Framework 6.x 和 Hibernate 6.6.x，以及利用 Jakarta 依赖项的应用程序。

WebLogic Server 和 Coherence 15.1.1 支持本地部署和云端部署，包括 Oracle Cloud 认证以及在容器和 Kubernetes 环境中运行 WebLogic Server 和 Coherence 的工具。我们的解决方案与广泛的平台、Oracle 产品和服务集成，为您的应用程序提供卓越的性能和可用性。最新软件可从 [Oracle 技术网络](https://www.oracle.com/middleware/technologies/fusionmiddleware-downloads.html) 和 [Oracle 软件交付云](https://edelivery.oracle.com/osdc/faces/SoftwareDelivery) 下载。您还可以查阅更新的 [产品文档](https://docs.oracle.com/en/middleware/standalone/weblogic-server/15.1.1/index.html) 以获取更多详细信息。

**支持 Spring Framework 6.x 和 Hibernate 6.6.x**

通过增强对 Jakarta EE 9.1 的支持，WebLogic Server 和 Coherence 15.1.1 使应用程序能够利用最新的第三方库，从而提高可升级性并帮助您的企业解决方案面向未来。使用 Spring Framework 6.x 和 Hibernate 6.6.x 构建的、利用“Jakarta”包命名空间的应用程序现在可以无缝部署到 WebLogic Server 和 Coherence 15.1.1。

**升级指南**

我们致力于维护 WebLogic Server 各版本之间的兼容性并简化升级过程。WebLogic Server 15.1.1 中的一个显著要求是将应用程序迁移到“Jakarta”命名空间。利用基于社区的 OpenRewrite 技术工具简化并自动化了这一过渡，特别是对于从 WebLogic Server 12.2.1.4、14.1.1 和 14.1.2 升级的应用程序。全面的 OpenRewrite 脚本减少了人为错误并降低了成本，尤其是在管理大型应用程序组合时。

通用升级过程包括：

– 转换应用程序

– 升级域

– 部署转换后的应用程序

详细的 [升级指南](//docs.oracle.com/en/middleware/standalone/weblogic-server/15.1.1/wlupg/index.html) 和实操教程可供参考，请参阅 [重写 WebLogic](https://github.com/oracle/rewrite-recipes/blob/main/rewrite-weblogic/README.md)。

## **证书管理**

WebLogic Server 15.1.1 引入了自动化证书管理功能，旨在简化安全域配置，包括使用“安全生产模式”SSL 设置的配置。这项新功能自动化了 WebLogic 域和服务器内的证书生成、续订和分发。它支持由嵌入式 WebLogic CA、外部证书颁发机构和 OCI 证书服务颁发的证书。

我们正在将证书管理作为技术预览版提供，让用户可以提前体验此功能。此功能的全面支持将在 WebLogic Server 15.1.1 的后续更新中提供，请持续关注我们的博客以获取未来公告。

## **与 Oracle 数据库集成**

Oracle WebLogic Server 继续提供与 Oracle 数据库的一流集成。15.1.1 版本捆绑了 Oracle JDBC 23ai 驱动程序，提供对 Oracle Database 19c 和 23ai 的认证支持，并解锁新的数据库功能。值得注意的是，通过 23ai 支持，WebLogic Server 现在可以支持 JSON 数据库，允许用户通过 SODA 驱动程序存储和查询关系型和 JSON 数据。

其他 JDBC 23ai 驱动程序增强功能包括：

– 改进的诊断和日志记录

– 对 Oracle 数据库分片的原生 UCP 数据源支持

– 原生布尔数据类型支持

– 增强的透明应用程序连续性

WebLogic Server 15.1.1 还引入了数据源的调优属性，优化了非活动或低利用率期间的连接池。

## **可观测性和 OpenTelemetry 支持**

借助 WebLogic Server 对 Oracle JDBC 23ai 驱动程序的支持，用户可以利用 OpenTelemetry 实现从 WebLogic Server 到 Oracle Database 23ai 的全面可观测性。OpenTelemetry 提供与供应商无关的遥测数据，增强了性能监控，加速了故障排除，并支持企业 Java 应用程序中主动的、数据驱动的运营。在文章 [使用 OpenTelemetry 实现 WebLogic Server 的可观测性和监控](https://blogs.oracle.com/weblogicserver/post/wls-observability) 中，您将找到一个概念验证——如何在 WebLogic 环境中利用 OpenTelemetry 的功能。

**云原生和 Kubernetes 支持**

WebLogic Kubernetes 工具包已得到增强，可全面支持 WebLogic Server 15.1.1 域，实现即时部署到 Kubernetes。WebLogic Kubernetes Operator 有效管理 WebLogic Server 15.1.1 域的整个生命周期，确保跨传统和新部署的简化操作。WebLogic Deploy Tooling (WDT) 也已更新，支持在虚拟机、Kubernetes 持久卷和云环境中进行内省、配置和域创建。

在 Kubernetes 中运行的 WebLogic 域可以通过与 Horizontal Pod Autoscalers (HPA) 以及 Prometheus 或 KEDA 提供的指标的无缝集成而受益于集群弹性。操作员可以根据流量阈值自动扩展或缩减集群，支持动态、高可用性环境。您可能有兴趣阅读博客 [集群起源：使用 Prometheus 和 Keda 在 Kubernetes 上自动扩展 WebLogic 集群。](https://medium.com/oracledevs/clusterception-autoscaling-weblogic-clusters-on-kubernetes-using-prometheus-and-keda-cd4550c458c9)

Oracle 继续每季度将 WebLogic Server 和 Coherence 镜像发布到 Oracle Container Registry (OCR)，并预先修补了最新的关键补丁更新 (CPU)。来自 OCR 的镜像可以自动化更新并保护您在 Kubernetes 中运行的 WebLogic 和 Coherence 15.1.1 域。

## **Oracle Coherence 15.1.1**

Coherence 15.1.1 运行在 Java 17 和 Java 21 上，保持与 Jakarta EE 9.1 规范兼容，并引入了多项增强功能，包括：

– 向量数据库

Coherence 15.1.1 增加了对 Coherence 集群内密集向量嵌入的优化存储的支持，以及使用 Coherence 聚合器对这些嵌入并行执行相似性搜索的能力。它还允许用户创建基于 HNSW 和二进制量化的向量索引，这可以显著提高搜索性能。

– Lucene 全文索引

Coherence 15.1.1 还增加了对分区 Lucene 全文索引的支持，以及对这些索引的并行搜索，并对结果进行复杂的重新排序，确保将最佳匹配返回给客户端。

– Coherence RAG

Coherence RAG 基于核心向量数据库和 Lucene 索引功能，并添加了更高级别的 API，允许您轻松地将相似性或混合搜索结果与远程 LLM 集成，从而使用生成式 AI 实现端到端的 RAG 解决方案。它还支持从多个文档源（包括自定义源）进行大规模并行文档内容摄取和向量化，以及与本地和远程嵌入、重排和聊天模型的无缝集成。

Coherence RAG 允许您利用数百甚至数千个 CPU 核心来执行向量嵌入创建，其速度与在 GPU 上运行时相当甚至更快，并且如果 GPU 可用，它也将利用 GPU 的优势。

– 远程客户端的 OpenTelemetry 支持

Coherence 15.1.1 还为远程 Extend 和 gRPC Java 客户端添加了 OpenTelemetry 支持，允许用户真正端到端地跟踪 Coherence 应用程序内的请求：从远程客户端，一直到最终用于存储数据的外部数据存储（如果存在），或者 Coherence 存储层，包括内置磁盘持久化（如果不存在）。

**支持生命周期**

WebLogic Server 和 Coherence 15.1.1 被指定为长期支持 (LTS) 版本，这意味着五年的一级支持加上三年的扩展支持。这提供了八年的错误和安全修复，确保卓越的应用程序性能、可靠性和安全性，并为未来的云采用提供了明确的现代化路径。

我们邀请您今天就试用 Oracle WebLogic Server 和 Coherence 15.1.1。请持续关注我们的博客，以获取更多公告和资源，支持您迈向现代化的云就绪应用程序之旅。