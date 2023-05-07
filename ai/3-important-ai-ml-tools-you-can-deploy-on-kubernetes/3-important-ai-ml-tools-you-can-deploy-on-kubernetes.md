# 可以在 Kubernetes 上部署的 3 个重要 AI/ML 工具

翻译自 [3 Important AI/ML Tools You Can Deploy on Kubernetes](https://thenewstack.io/3-important-ai-ml-tools-you-can-deploy-on-kubernetes/) 。

组织们都知道在 Kubernetes 上获取完整应用程序堆栈的重要性，人工智能是下一个。

![](https://cdn.thenewstack.io/media/2023/03/39137cbd-shutterstock_1-1024x622.jpg)

基础设施技术的世界变化很快。不久以前，在 Kubernetes 上运行数据库被认为过于棘手，不值得这么做。但那只是昨天的问题。云原生应用程序的构建者已经擅长于运行有状态的工作负载，因为 Kubernetes 是一种快速、高效地创建虚拟数据中心的强大方式。

上一次撰写相关内容时，我扩大了视野，考虑了虚拟数据中心中应用程序栈的其他部分，特别是流式工作负载和分析。

随着这两个成为 Kubernetes 的主流，关于用例的讨论变得更加有趣。如果我们可以访问这些基础数据工具，我们将如何处理它们？

幸运的是，我们不必深入研究，因为行业已经选择了方向： AI/ML 工作负载。推动这一趋势的是对更快、更灵活的 MLOps 的需求，以支持在线预测，也被称为实时人工智能（AI）。Uber 和 Netflix 等公司都是早期采用者，但是有许多很棒的项目可以帮助您更快地使用 Kubernetes。

## Feast 支持的特征服务

构建和维护机器学习（ML）模型正在从后台转向更靠近用户的生产环境。特征存储作为数据和机器学习模型之间的桥梁，提供了模型在离线和在线阶段访问数据的一致方式。它管理模型训练期间的数据处理要求，并在在线阶段提供低延迟的实时访问模型。这确保了两个阶段的数据一致性，并满足在线和离线的需求。Feast 是在 Kubernetes 中运行的特征存储的一个例子。

Feast 是一款开源工具，可帮助组织在离线训练和在线推理阶段一致地存储和提供特征。它不仅提供了传统数据库的功能，还提供了专业的特性，如时点正确性。同时，Feast 运行在 Kubernetes 中，使得它可以很好地与云原生应用配合使用。

## KServe 支持的模型服务

KServe 是用于在 Kubernetes 中部署机器学习模型的 API 端点，处理模型的获取、加载和确定是否需要使用 CPU 或 GPU 。它与 KNative 事件集成以实现扩展，并提供 metrics 和日志等可观测性特性。

最好的部分？它很容易使用。只需将 KServe 指向您的模型文件，它将创建一个 API 并处理其余的部分。解释器功能提供了有关为什么会作出每个预测决策的见解，提供特征重要性并突出显示导致特定结果的模型因素。

这可以用于检测模型漂移和偏差，这是机器学习中“重要但困难”的部分之一。这些功能减少了 MLOps 所需的工作量，并增强了对应用程序的信任。 KServe 最近从 Google KubeFlow 项目中分离出来，并被彭博社作为其构建 ML 推理平台的努力的一部分进行了重点介绍。

## 矢量相似性搜索

传统的寻找数据的方法有所不同，向量相似度搜索（Vector Similarity Search，VSS）是一种机器学习工具，它使用向量数学来找出两个事物彼此之间的“接近程度”。这是通过 K 最近邻（K-nearest neighbor，KNN）算法来完成的，该算法将数据表示为向量。

然后，使用一个 CPU 密集型的 KNN 算法将数据进行向量化，然后进行索引以进行低 CPU 消耗的搜索。终端用户可以提供一个向量，使用 VSS 服务器提供的查询机制找到与其相似的事物。可在 Kubernetes 中部署的开源 VSS 服务器包括 [Weaviate](https://weaviate.io/) 和 [Milvus](https://milvus.io/) 。两者均提供了添加相似性搜索到应用程序堆栈所需的所有内容。

## 组建团队

结合我[之前的文章](https://thenewstack.io/the-path-to-getting-the-full-data-stack-on-kubernetes/)和这篇文章，你就有了在 Kubernetes 中部署完整堆栈的秘诀。每个组织都应该努力实现的结果是提高生产力和降低成本。最近的调查表明，数据领域的领导者在 Kubernetes 中部署数据基础架构时发现了这两种情况。

AI/ML 工作负载可能是您刚刚开始探索的内容，因此现在可能是正确开始的最佳时机。提到的三个领域——特征服务、模型服务和向量相似性搜索——都包含在我与 Jeff Carpenter 合著的书“[Managing Cloud Native Data with Kubernetes](https://learning.oreilly.com/library/view/managing-cloud-native/9781098111380/)”中。应用程序堆栈中 AI/ML 的大局：实时需求将很快在大多数 AI 应用程序中变得普遍。使用 Kubernetes 快速运行并可靠地构建不再是 AI 的幻觉。