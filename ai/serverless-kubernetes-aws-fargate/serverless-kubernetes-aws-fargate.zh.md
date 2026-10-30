一个Pod一个节点：AWS无服务器Kubernetes背后的架构设计

通过Pod级别的演练，了解准入路由、专用调度和网络隔离，无需工作节点

无服务器Kubernetes改变了谁来管理节点，而不是Kubernetes对节点的期望。Kubernetes期望节点能够向控制平面注册、报告容量、运行Kubelet、提供网络支持并托管工作负载。AWS Fargate提供这些行为，而无需客户创建、修补、扩展或替换[一组工作节点](https://thenewstack.io/eks-zonal-shift-resilience/)。

[Amazon Elastic Kubernetes Service](https://thenewstack.io/eks-kubernetes-upgrade-rollback/) (EKS) Fargate通过将Pod作为基础设施单元来解决这个问题。当选择一个Pod用于Fargate时，EKS会配置一个专用的计算环境，启动所需的Kubernetes组件，在客户的虚拟私有云（VPC）中为该Pod分配一个弹性网络接口（ENI），并在Pod消失时拆除该环境。

> “无服务器Kubernetes改变了谁来管理节点，而不是Kubernetes对节点的期望。”

这种客户体验取决于几个协同的设计选择。准入时路由可防止默认调度程序认领Fargate Pod。Fargate专用的调度程序会配置容量，而不是从预先存在的节点池中进行选择。精简的运行时镜像提供Kubernetes节点组件，而独立的网络命名空间使平台路径与工作负载路径保持区别。节点上的准入处理器将工作负载限制在适合“一个Pod、一个环境”模型的模式中。

本文将从准入和调度到节点运行时和网络，跟踪使Pod配置成为可能的各个组件。

![说明 EKS Fargate 工作原理的图表](https://cdn.thenewstack.io/media/2026/10/a71f1ab0-image1-1024x489.png)

*图 1. 该图显示了 EKS 如何在调度前路由 Pod、请求专用容量，以及启动用于验证和运行 Pod 的 Kubernetes 运行时。*

## 在调度前路由 Pod

EKS集群可以同时使用来自Amazon Elastic Compute Cloud (Amazon EC2)和Fargate的节点。因此，在常规调度流程开始之前，必须明确放置位置。

EKS提供了一个Fargate配置文件（Profile），这是一个AWS资源，指示哪些Pod在Fargate上运行。配置文件通过选择命名空间（Namespace）和可选的Pod标签来表达该意图。它还指定用于Pod弹性网络接口的私有子网和安全组，因此放置位置和网络访问是一起选择的。

对于启用了Fargate的集群，AWS作为Kubernetes控制的一部分，管理和运营一个准入WebHook。当Pod与配置文件匹配时，突变WebHook（Mutating Webhook）会将匹配的配置文件的名称添加到Pod的标签中。它还将Pod的调度程序名称设置为Fargate调度程序，以便Pod遵循Fargate调度路径。此决策发生在Pod对象持久化到Kubernetes数据库（etcd）之前，以及默认调度程序认领它之前。

配置文件还指定了Pod执行角色，这是Fargate基础设施用于注册其kubelet并从Amazon Elastic Container Registry (Amazon ECR)拉取镜像的AWS Identity and Access Management (IAM)角色。该角色与应用程序身份容器使用的角色不同。由于这是无服务器基础设施，EC2实例元数据对Fargate Pod不可用，因此调用AWS服务的应用程序应使用服务账户的IAM角色。

### 为 Pod 配置节点

Fargate调度程序是一个运行在Kubernetes控制平面上的专用调度程序。它根据Pod的资源需求及其匹配的Fargate配置文件为Pod请求新容量，而不是搜索现有节点的池。

> “Fargate调度程序是一个运行在Kubernetes控制平面上的专用调度程序。它为Pod请求新容量，而不是搜索现有节点的池。”

一旦请求了容量，调度程序就会将Pod与指定的节点进行暂时关联。这可以防止重试或重新同步为同一个Pod配置第二个环境。当环境准备就绪时，Fargate运行时会注册Kubernetes Node对象，并且调度程序在节点报告就绪后执行最终绑定。然后，运行时启动Pod并通过API服务器报告其状态。

当Pod终止时，运行时会删除节点并释放其容量。如果配置或绑定失败，对账（Reconciliation）将清除临时分配并在重试之前回收容量。

## 一个 Pod，一个网络接口

Fargate通过其ENI将每个Pod连接到客户的VPC。Fargate配置文件定义了用于该接口的私有子网和安全组。因此，安全组规则和VPC路由适用于Pod的ENI，而不是共享的、客户管理的工作节点。

ENI赋予Pod在VPC中的一流地位。VPC流日志（Flow Logs）可以识别接口，安全组规则可以表达预期的工作负载边界。

网络路径必须同时服务于两个受众。Fargate平台需要一条用于托管遥测、凭据和配置的路径。Kubernetes组件需要一条通往API服务器的路径，客户Pod需要一条通往VPC的路径。Fargate在Kubernetes要求的地方保持这些路径连接，同时将平台流量与工作负载流量分开。

![说明 EKS Fargate 的 Pod 执行环境的图表。](https://cdn.thenewstack.io/media/2026/10/ce6eb4f2-image2-1024x509.png)

*图 2. 执行环境将平台、Kubernetes 组件和 Pod 网络命名空间分隔开，而客户 ENI 则承载面向 Kubernetes 和 VPC 的路径。*

Fargate配置了三个逻辑Linux网络命名空间。平台命名空间承载Fargate平台服务，包括遥测、凭据分发和配置。节点命名空间承载Kubernetes核心数据平面组件和客户ENI。工作负载命名空间运行客户工作负载。底层的Fargate实现可能会更改，但这种隔离使托管平台、Kubernetes节点组件和工作负载保持在不同的路径上。

客户ENI被移动到节点命名空间中，它为Kubernetes控制平面通信和Pod流量提供路径。可以从节点命名空间访问任务元数据终端节点，允许节点运行时的AWS身份验证路径获得将节点向API服务器注册所需的凭据，同时阻止来自工作负载命名空间的访问。由[容器网络接口](https://thenewstack.io/cloud-native-networking-as-kubernetes-starts-its-second-decade/) (CNI)创建的网桥和虚拟以太网（veth）对将节点命名空间连接到工作负载命名空间。节点命名空间处理发送到Kubernetes管理端点的流量；所有其他流量都传递到工作负载命名空间并通过客户ENI流出。过滤可防止Pod访问平台元数据和管理进程。

## 运行时镜像是一个微缩版的 Kubernetes 节点

运行时镜像与Kubernetes控制平面版本相匹配，因此kubelet及其支持组件保持兼容。它提供注册节点、接收Pod规范、启动和重启容器、运行探针、报告状态以及提供日志和exec等操作所需的kubelet和Kubernetes节点组件。

在kubelet启动验证期间，默认调度程序可以在Fargate kubelet完成初始化之前放置Pod。EKS运行一个自定义的PodAdmitHandler，它在Pod启动之前对其进行验证，并且仅准入旨在用于Fargate调度路径的Pod。当在kubelet启动时观察到另一个Pod时，这可以保护每个节点一个Pod的模型，并在API服务器准入之后提供第二个验证边界。

托管的kubelet不需要通用节点上可用的所有功能。Kubernetes提供了禁用日志、性能剖析（Profiling）和调试标志处理程序的控件，EKS使用它们将运行时表面保持在服务所需的操纵范围内。我们通过禁用日志处理程序以及禁用性能剖析和调试标志的更改，向社区贡献了其中一些控件。

## Fargate 修补与注意事项

Fargate的托管运行时会持续维护，EKS会定期替换Fargate Pod，以便它们在没有客户管理节点操作的情况下获得最新的可用安全补丁。当Fargate环境需要打补丁时，EKS会识别受影响的Pod，通知客户，并使用Kubernetes驱逐API（Eviction API）在回收环境之前正常移除Pod。对于由控制器管理的工作负载，这使替换Pod有机会在旧环境退役之前变得就绪。

客户的PodDisruptionBudget（Pod中断预算）控制在该过程中多少应用程序容量可以不可用。EKS在请求驱逐时尊重该预算，并在驱逐违反预算时进行重试。预算必须为计划内中断留出空间；如果驱逐在计划的终止时间仍无法成功，EKS最终可以删除Pod以便其创建打过补丁的环境。副本和就绪探针决定了应用程序是否继续提供流量。

客户必须围绕这个独立的Pod生命周期进行设计。每个Pod必须匹配一个Fargate配置文件。

客户应据此规划ENI和子网容量。由于许多Pod共享一个节点的接口而在EC2上行之有效的设计，必须考虑每个Fargate Pod一个ENI。Fargate配置文件使用私有子网，并且不为Fargate Pod分配公共IP地址。互联网或AWS服务访问通常使用私有子网的网络地址转换（NAT）网关或VPC终端节点设计。由于客户ENI同时承载Kubernetes数据平面流量和Pod流量，其安全组必须允许诸如 `kubectl logs` 和 `kubectl exec` 等操作所需的Kubernetes管理流量。

## 适合该模型的工作负载契约

大多数Kubernetes应用程序工作负载自然适合Fargate，包括Deployments、Jobs以及其隔离边界是Pod的多租户应用程序。需要节点级控制的工作负载（例如DaemonSets、主机网络、主机端口、特权操作或GPU）超出了Fargate Pod契约，需要提供节点级访问的执行模型。

存储遵循相同的边界。HostPath和主机附加块存储依赖于持久节点，并且Amazon Elastic Block Store (Amazon EBS)无法挂载到Fargate Pod。对于持久共享文件存储，Amazon Elastic File System (Amazon EFS)是受支持的模式。有关支持的Kubernetes功能，请阅读当前的[EKS Fargate文档](https://docs.aws.amazon.com/eks/latest/userguide/fargate.html)。

> “使Kubernetes无服务器化需要的不仅仅是隐藏工作节点。EKS必须在改变底层生命周期的同时保留Kubernetes行为。”

使Kubernetes无服务器化需要的不仅仅是隐藏工作节点。EKS必须在改变底层生命周期的同时保留Kubernetes行为。准入在调度程序竞争之前建立放置意图。调度程序配置容量并等待节点证明就绪。运行时组件提供节点契约，而节点级准入保护Pod边界。VPC网络为每个Pod赋予直接的、可控的身份，而命名空间和VM边界使托管平台与工作负载保持分离。

这些决定在起作用时大多是不可见的。部署选择配置文件，Pod以预期的VPC访问权限启动，日志和exec的表现就像Kubernetes操作一样，并且底层环境在工作负载消失时消失。

这种不可见性正是该服务的意义所在。客户可以使用熟悉的Kubernetes对象和工作流，而EKS和Fargate则承担配置、隔离、节点生命周期和运行时维护的工作。基础设施是托管的，但契约仍然是Kubernetes：Pod作为一流的工作负载被准入、调度、连接和可观测。