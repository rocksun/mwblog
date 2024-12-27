# Kubernetes 正在接管：使用 4 种新技术更智能地部署

Kubernetes (K8s) 是一个用于构建、测试、修改和扩展基于容器的应用程序的容器编排平台。

它有多种“版本”可供选择，并且能够在本地和云中运行，因此已成为事实上的标准。根据最近的数据，[Kubernetes 处于领先地位](https://thenewstack.io/magic-is-happening-in-kubernetes/)，市场份额超过 95%。

如果您正在考虑将 K8s 用于您的企业环境，或者想要扩展 Kubernetes 部署的范围，以下列出了四个培训要点和八个最佳实践。

**Kubernetes 成功 的 4 个重要培训主题**

无论这是您第一次使用 Kubernetes，还是让新的团队成员了解容器管理，从基础开始都是至关重要的。

就像员工需要 AWS 数据科学、Google Analytics 或 [Power BI 培训课程](https://www.accelebrate.com/power-bi-training) 来有效地利用这些解决方案一样，让用户掌握关键的 Kubernetes 培训主题至关重要。这些主题包括：

**1. 容器编排基础知识**

容器很常见。Docker、Podman 和 OpenVZ 等解决方案允许公司创建和 [部署虚拟容器](https://thenewstack.io/deploy-a-virtual-machine-with-oracles-open-source-virtualbox/) 用于存储、数据处理或应用程序开发。

Kubernetes 帮助您集体管理这些容器以最大限度地提高其效率。此过程称为编排。标准编排功能包括启用跨容器通信、确保容器安全和扩展容器集群。

**2. K8s 术语**

Kubernetes 的关键术语包括：

* **Pod —** Pod 由一个或多个容器组成。它们是 K8s 中最小的执行单元。
* **Node —** 节点是托管 Pod 的物理服务器或虚拟机 (VM)。
* **Cluster —** 集群是一组节点，通常由主节点管理。
* **Etcd —** 主节点包含 etcd，通常称为 Kubernetes 事实来源。在 K8s 中进行的任何更改都以 JSON 格式存储在 etcd 中。
* **API server —** API 服务器启用与 Kubernetes API 的通信。用户、程序和 kubectl 命令行界面 (CLI) 都可以使用它。
* **Controller manager —** 控制器[管理器告诉 K8s](https://thenewstack.io/kubecost-cloud-manages-k8s-costs-for-finops-teams/) 控制器创建帐户、访问 API 并将服务连接到 Pod。
* **Scheduler —** 调度程序将工作分配到各个节点，并计算资源需求以确定 Pod 何时运行以及哪些节点应运行这些 Pod。

**3. 可能的部署路径**

使用 K8s，有多种可能的部署路径。您可以在物理机或虚拟机上本地部署 Kubernetes，在云中运行该解决方案，或将两者结合起来。

**简化 K8s 部署的八个最佳实践**

一旦员工掌握了 Kubernetes 的基础知识，下一步就是部署。但是，鉴于 K8s 的范围和规模，团队很容易不知所措。

以下列出了八个最佳实践，以帮助简化部署。

**1. 选择合适的版本**

除了不同的部署选项外，Kubernetes 还提供多种“版本”，每种版本都有其优势。

* **本地选项：** KIND (Kubernetes in [Docker](https://www.docker.com/?utm_content=inline+mention)) 和 Docker Desktop 是开发和测试的绝佳选择。这些轻量级工具允许团队在扩展到生产环境之前进行实验和微调配置。
* **云原生服务：** 像 [Google](https://cloud.google.com/?utm_content=inline+mention) Kubernetes Engine (GKE)、[Amazon](https://aws.amazon.com/?utm_content=inline+mention) Elastic Kubernetes Service (EKS) 和 [Azure](https://news.microsoft.com/?utm_content=inline+mention) Kubernetes Service (AKS) 这样的云提供商提供了完全托管的环境，简化了 [基础设施](https://thenewstack.io/platform-engineering-needs-to-manage-infrastructure-too/) 管理。这些选项通过处理更新、监控和扩展来减少运营开销。
* **企业解决方案：** [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) OpenShift 和 [VMware](https://tanzu.vmware.com?utm_content=inline+mention) Tanzu 提供了额外的自动化、监控和合规性层。这些工具适用于具有复杂多集群环境或严格监管要求的组织。

仔细评估您的工作负载、团队专业知识和部署目标，以选择最适合您用例的版本。

**2. 使用 Kubernetes 命名空间**

命名空间充当 Kubernetes 集群中的虚拟分区。这些逻辑隔离允许您有效地组织资源，在同一个集群中管理多个项目，并根据需要隔离工作负载。
例如，您可以为开发、测试和生产环境创建单独的命名空间以避免资源冲突。命名空间还有助于执行资源配额，使跨团队或应用程序公平分配 CPU、内存和存储资源变得更容易。随着集群规模和复杂性的增长，这种级别的组织变得至关重要。

**定义资源限制**
资源限制是优化集群性能的关键保障。通过为 CPU 和内存设置最小和最大资源限制，您可以防止一个应用程序消耗所有可用资源并影响其他应用程序的性能。

例如，您可以配置资源请求以保证关键应用程序的最小 CPU 级别，同时设置限制以防止在峰值负载期间过度消耗。这些配置在多租户环境中特别有价值，在多租户环境中，公平的资源分配是保持平稳运行的关键。

**4. 考虑滚动更新**
滚动更新是一种强大的策略，可以最大限度地减少部署期间的应用程序停机时间。这种方法不是同时更新所有容器实例，而是逐步替换它们。

如果一个应用程序跨越五个 Pod，Kubernetes 可以一次关闭一个 Pod，用新版本替换它，同时保持其他 Pod 运行。这允许最终用户不间断地服务，并在最新部署出现问题时提供回滚机制。将滚动更新集成到 CI/CD [管道中强烈推荐用于更安全、更高效的](https://thenewstack.io/5-bottlenecks-impacting-rag-pipeline-efficiency-in-production/)实现。

**5. 实施基于角色的访问控制 (RBAC)**
RBAC 是一项安全功能，可在 Kubernetes 中启用细粒度的访问管理。通过定义角色并将它们分配给用户或组，您可以控制谁可以在集群中对资源执行特定操作。

例如，开发人员可能能够修改[开发命名空间中的部署配置，但不能对生产环境进行更改](https://thenewstack.io/does-cloud-native-change-developer-productivity-and-experience/)。RBAC 降低了[意外错误配置的风险并增强了安全性](https://thenewstack.io/want-to-mitigate-risk-invest-in-automation/)，使其成为任何 Kubernetes 环境的基本实践。

**6. 设置 Pod Disruption 预算 (PDB)**
PDB 定义在计划维护或意外中断期间可以运行的 Pod 的最小数量。通过配置 PDB，您可以在这些事件期间保持应用程序可用性。

例如，如果应用程序需要至少三个副本才能正常运行，则可以将 PDB 设置为一次只允许中断一个 Pod。这确保即使发生中断也能处理用户请求，从而保持关键服务的可用性。

**7. 利用自定义资源定义 (CRD)**
CRD 允许您通过扩展 Kubernetes API 来定义自定义资源和控制器。在实践中，这允许训练有素的工作人员构建特定于应用程序的工作流程。对于具有独特应用程序工作流程或要求的组织，此功能非常方便。

一个例子是创建一个自定义资源类型来管理特定配置，例如数据库连接或应用程序密钥。这种级别的自定义使团队能够自动化重复性任务，简化复杂的工作流程，并提高管理 Kubernetes 环境的效率。

**8. 利用 Kubernetes 服务选项**
诸如 Azure Kubernetes Service (AKS) 之类的解决方案可以在云中利用 K8s。但是，除了管理容器之外，您的团队还可以通过其他服务选项来扩展 Kubernetes 的影响。

例如，Azure 容器实例提供了一种轻量级的 Azure VM 替代方案，而 Azure Service Fabric 允许您创建和管理有状态服务。此结构支持各种 Microsoft 服务，包括 Power BI、Cosmos BD 和 Dynamics 365。

**充分利用 Kubernetes**
Kubernetes 是一个功能强大、灵活的容器管理平台。但是，请充分利用此解决方案。

无论您是在本地托管 K8s，利用云供应商产品，还是使用企业级管理工具，全面的培训和有针对性的最佳实践都有助于简化部署并最大限度地提高 K8s 的影响。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)