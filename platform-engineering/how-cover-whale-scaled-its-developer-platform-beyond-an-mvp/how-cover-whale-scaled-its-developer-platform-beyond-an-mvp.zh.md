平台工程在各行业中越来越受欢迎，因为企业正努力应对云原生开发的复杂性。团队希望简化资源调配、部署和可观测性，同时减轻应用开发人员的负担。然而，许多人发现，超越最小可行平台（MVP）需要转变方法。

本案例研究探讨了[Cover Whale](https://www.coverwhale.com/)（一家专注于卡车保险的美国公司）如何在[Kubernetes](https://thenewstack.io/kubernetes-an-overview/)和[AWS](https://aws.amazon.com/?utm_content=inline+mention)上构建其[内部开发者平台（IDP）](https://thenewstack.io/how-do-the-internal-developer-platform-and-portal-connect/)，它在超越MVP进行扩展时面临的挑战以及在此过程中吸取的经验教训。从管理庞大的Helm chart到集成NATS等系统，这段历程展示了许多企业在发展其平台时所遇到的权衡。

这个故事还强调了[Kratix](https://www.kratix.io/)等平台编排工具如何在编写自定义操作符和拼凑脚本之间提供了一个中间地带，以及这对长期可维护性意味着什么。

## 平台工程倡议

最近，Cover Whale启动了一个新的保险平台，以改善其客户体验。为了简化新平台的应用生命周期，他们实施了一个IDP来处理每个新[微服务](https://thenewstack.io/introduction-to-microservices/)工作负载的资源调配、构建、测试、部署和可观测性。

该IDP构建在AWS Elastic Kubernetes Service (EKS)之上，EKS运行一个平台Kubernetes集群，控制着一组工作负载Kubernetes集群。

所有集群和底层基础设施都由OpenTofu和Terramate进行资源调配，并使用App of Apps模式通过[Argo CD](https://thenewstack.io/survey-argocd-leaves-flux-and-other-gitops-platforms-behind/)进行引导。

集群引导通过使用共享工具（例如Karpenter、external-dns、external-secret operator和ingress controller）初始化集群来执行。然后，它为IDP中的每个系统部署一个`Application`，而该`Application`又为该系统内的每个工作负载部署另一个`Application`。整个编排过程封装在一系列由Argo CD加载到集群中的Helm chart中。

## 遇到的挑战

这种设置使得最小可行产品的快速高效开发成为可能。

部署和维护整个工作负载层次结构，同时消除创建Kubernetes清单和构建管道的复杂性，是一个颠覆性的改变，证明了该举措对开发人员和管理层都具有价值。

尽管如此，超越MVP要求我们重新考虑我们的方法，原因如下，我们将在下面详细说明。

### 可扩展性

Argo CD在生成Kubernetes清单方面没有提供太多选择。因此，我们使用了Helm chart……很多很多。更糟糕的是，Helm结构遵循了IDP的系统和工作负载结构，并且针对部署在平台集群或工作负载集群中的内容有单独的chart。

其结果是，特定关注点的资源会分散在多个Helm chart中。随着IDP的增长，这导致了一个非常复杂的代码库，相关逻辑分散在多个chart中。

例如，`external-secret`集成分散在三个不同的Helm chart中。

因此，为了实现更具可扩展性的设置，需要进行范式转变。

### 与非Kubernetes资源的有限集成

MVP依赖于与非Kubernetes资源的一些交互。例如，我们使用[AWS Controllers for Kubernetes](https://aws-controllers-k8s.github.io/community/)生成Elastic Container Registry (ECR)存储库和相关的身份与访问管理（IAM）角色。

然而，由于我们的工作负载依赖于消息系统NATS和Synadia Cloud，动态生成NATS用户是非常理想的，但却没有操作符来实现这一点。我们本可以使用Helm钩子，但这感觉不可靠，而且编写一个成熟的操作符在当时看来比我们期望的要投入更多。

### 后端-前端集成

我们使用[Port.io](https://www.port.io/?utm_content=inline+mention)作为开发者门户，为开发者提供一致的前端，并增强我们的开发者体验（DX）。该门户提供了已部署工作负载的概览、开发人员可用于管理其工作负载的自助服务操作，以及指向可观测性工具和git仓库的链接。

为了在门户中准确表示我们的系统和工作负载结构，我们依赖于Argo CD Applications和代表系统的ApplicationSet的标签和注解。尽管功能正常，但这种设置有些混乱。

例如，一个系统由多个Applications和一个ApplicationSet组成。当我们需要在前端添加有关标签/注解需要添加到何处的信息时，这导致了一些困惑。

理想情况下，我们希望有一个IDP结构的自定义资源定义（CRD）表示，Port.io可以明确地读取。然而，仅仅为了这个目的维护这些CRD感觉有点小题大做。

另一方面，使用这些CRD来驱动IDP并减少我们对Helm chart的依赖，这非常有意义！

## 将Kratix引入我们的IDP

[Kratix](https://www.kratix.io/)提供了一个很好的中间地带，介于编写我们自己的操作符和连接一些脚本来解决上述问题之间。

Kratix监控我们资源的状态并允许周期性协调，使我们无需拥有专门的工作负载来监视kube-apiserver，同时使我们能够管理资源的整个生命周期。

使用“承诺”方法，我们还可以将特定的关注点集中起来，而不必担心IDP的层次结构。

### 概念验证

在新平台的开发过程中，我们必须聚合来自多个服务的API，并以一致的方式对外暴露它们，从而在外部和内部服务之间创建了一个良好的抽象层。这包括来自传统和新客户门户的API，以及各种外部服务的webhook。

我们决定在工作负载清单中添加对此功能的支持，使开发人员能够以分布式方式管理其API，并让IDP将所有API聚合在一个域名下。

为此，我们创建了两个[Kratix promise（承诺）](https://docs.kratix.io/main/guides/writing-a-promise)：

*   ApiAggregator，用于声明API对外暴露的主机名。
*   ApiAggregatorTarget，它附属于一个ApiAggregator，并定义了一个路径列表以及请求应发送到的目标服务。

在幕后，Kratix会创建所有Gateway API资源，让奇迹发生。

我们使用[ytt](https://carvel.dev/ytt/)在我们的promise管道中生成清单，这使得YAML模板化过程更容易，并避免了所有[YAML怪癖](https://hitchdev.com/strictyaml/why/implicit-typing-removed/)，从而保证了一个有效的YAML对象。

由于Argo CD已经在使用，部署Kratix相当容易。我们只是创建了一个专用的状态存储git仓库，并将工作负载集群添加为目标（Destination），作为集群引导过程的一部分。

很快，我们就有了一个可用的概念验证，并在对支持更大请求体大小进行了一些小修补后，我们很快就放心地将其发布到生产环境。

### 声明式NATS支持

继这个概念验证之后，我们决定使用Kratix的完整设置，以消除手动管理NATS用户和凭据的需要。

这项任务有点复杂，因为promise必须与SaaS平台交互以生成用户，同时还要安全地存储他们的凭据。

我们首先开发了一个脚本来管理Synadia Cloud中NATS用户的生命周期并生成凭据。为了简化与API的交互，我们使用[restish](https://rest.sh)而不是原始的curl命令。

将脚本与Kratix promise集成，并管理资源状态以跟踪NATS用户ID和凭据过期，这些都相对简单。我们确保了保存和加载状态、创建和删除用户以及凭据的关注点清晰分离。

然而，操作凭据才是真正的挑战。原因是Kubernetes清单存储在git仓库中，而存储原始秘密信息显然是不可接受的。

### 使用Kratix操作秘密

在探索了多种选项后，我们决定使用Sealed Secret。这个工具使用非对称加密算法，利用平台集群已知的公钥来加密秘密信息，并使用仅工作负载集群已知的私钥来解密它。

这个设置运行得很顺利——持续了几个小时！我们很快注意到我们的工作负载频繁重启。

Kratix期望你的promise是幂等的。实际上，几个小时后，Kratix会运行一个协调作业。在我们的案例中，这次协调运行创建了一个新的NATS认证令牌，更新了现有的认证秘密，从而触发了工作负载的滚动更新。

更糟糕的是，我们无法解密现有秘密或从Synadia云中检索它。此外，不发出密封秘密资源将导致从工作负载集群中删除该秘密。

为了解决这个问题，我们添加了`sealedsecrets.bitnami.com/patch`注解，并生成了一个空的密封秘密来防止秘密被删除。

## 结论

Cover Whale的历程反映了许多企业面临的一个挑战：构建一个能够从概念验证发展成为可持续、可扩展平台的IDP。MVP通常能展现立竿见影的价值，但扩展则需要重新思考围绕Helm、CRD和秘密管理的模式。

团队发现，采用基于“承诺”的Kratix方法提供了一条务实的前进道路。然而，更广泛的教训是，企业应该准备好随着新需求的出现而演进其架构。其他团队的关键经验包括：

*   警惕Helm的蔓延；CRD驱动的方法可以提供更清晰的边界并降低复杂性。
*   在与SaaS系统集成时，及早规划生命周期管理和幂等性。
*   秘密管理仍然是一个棘手的问题；协调和轮换策略必须在实际条件下进行测试。

通过围绕这些经验重新构建IDP，Cover Whale创建了一个更一致、更易于维护的平台基础，该基础随着开发人员需求的增长而不断演进。