[treebeardtech](../)

- 文章
- Kubernetes 上的高性能计算 (HPC)

# Kubernetes 上的高性能计算 (HPC)

## ML 平台工程提示

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1ddf7a27-490a-4884-bbfc-3036e3f3dbf6/Nanoscience_High-Performance_Computing_Facility.jpg?t=1712250549)

机器学习 (ML) 工程在过去几年已演变为一门学科和职业道路。软件工程师构建 Web、移动和嵌入式体验，而 ML 工程师提供模型版本、推理和整个 RAG 应用程序。

这对整个工程组织意味着什么？我的主要收获是，负责提高 ML 团队杠杆率的平台工程团队必须提供一组不同的原语，这些原语将在 ML 工程师经历其 *MLOps* 流程时为其提供支持。

最大化 ML 团队的杠杆率需要 (a) 最小化繁琐工作（手动工作流），(b) 提高其交付速度，以及 (c) 降低固有风险，例如安全或成本管理故障。如果您能做到这三点，您将能够扩大您的运营规模。

此建议可应用于许多不同类型的 ML 组件：

- **“无服务器”推理应用程序**用于实时客户交互，以进行欺诈检测、产品推荐或聊天机器人
- **异步推理应用程序**用于图像和视频生成或理解，可能使用从某些请求流中读取的长时运行工作进程
- **批处理系统**可用于数据准备、训练、离线推理或评估

在本文中，我们将探讨 ML 平台工程师为其 Kubernetes 平台上的内部客户提供批处理功能的一些可用选项。

## 从 HPC 到 Kubernetes

基于 Kubernetes 的云原生计算已成为新软件项目的实际标准。对于许多用例来说，这很简单，但高性能计算 (HPC) 并不是一个简单的领域。

随着大数据应用程序从低级分布式计算库（如 MPI）演变为 Spark 和 Ray 等框架，Slurm 和 LSF 等底层平台也受到 Kubernetes 的挑战，Kubernetes 可以适应以提供 HPC 作业队列界面。

在 Kubernetes 上构建 HPC 环境需要了解用于构建更具生产力、效率和安全性的 ML 工程环境的工具概况。

### Kuberay

Ray 项目是使 Python 编程语言扩展到大型分布式环境的最成功且通用的方法。

它在 ML 工程师中取得的成功意味着 Kuberay Operator 是提高团队成员代理权的一种有前途的方法。此项目有效地将您的 K8s 集群转换为 Ray 平台，该平台可用于为任何团队提供自助 Ray 集群和作业。

### Kubeflow Spark Operator

虽然 Ray 因其 Python 原生特性而具有吸引力。Spark 已经存在很长时间了，这意味着有大量的 Spark 应用程序和从业者。

此 Spark 运算符类似于 Kuberay，只是它管理 Spark 集群。它最初由 Google Cloud 开发，最近捐赠给了 Kubeflow 项目 ([在此处阅读更多内容](https://treebeardtech.beehiiv.com/p/treebeard-update))。

### Volcano

虽然前两个项目为分布式系统提供了一个 Pythonic 入口点，但确保作业以有效利用云资源的方式可靠执行非常重要。

如前所述，HPC/作业队列工作负载对您可能希望在 Kubernetes 上托管的许多其他应用程序有不同的要求。对于 pod 调度逻辑尤其如此，默认情况下由 kube-scheduler 处理。

ML 团队可能需要根据优先级调度作业或等待一组作业全部准备好后再运行这些作业的功能。

这就是 Volcano 项目让您实现的目标，它通过替换默认的 kube-scheduler 来实现此目标。

### Kueue

虽然 Volcano 通过替换 kube-scheduler 提供高级调度功能，但 Kueue 可以通过补充调度程序来实现此目的。

Kueue 通过准入 Webhook 提供作业排队和优先级排序——即它在您创建作业时捕获作业并暂停它们，直到轮到它们。

### Armada

Kueue 和 Volcano 都对 Kubernetes 的调度功能提供了相对轻量级的修改，但这需要付出代价。未决作业存储在集群配置存储 (etcd) 中，这可能会根据作业队列的大小造成可用性风险。

Armada 通过使用其自己的控制平面（而不是使用 Kubernetes 控制平面）提供此功能来解决此问题。

HPC 用户可以直接向 Armada API 提交作业，当作业准备就绪时，API 将逐渐将作业提交给 Kubernetes 控制平面。
**得益于此设计选择，Armada 可以扩展到大量作业，并且非常适合多集群环境。**

## 结论

就像人工智能的进步为产品团队增加了机器学习工程师的概念一样，它也为基础设施团队增加了机器学习平台工程。

为机器学习工程师提供服务需要针对他们正在构建的系统类型提供专门的解决方案，无论是无服务器推理应用程序、异步推理应用程序还是批处理系统。

由于 Kubernetes 在云基础设施中扮演着核心角色，因此我们重点介绍了 5 个开源项目，这些项目可以在批处理/HPC 系统中使用，因为您在机器学习平台工程之旅中取得了进展。