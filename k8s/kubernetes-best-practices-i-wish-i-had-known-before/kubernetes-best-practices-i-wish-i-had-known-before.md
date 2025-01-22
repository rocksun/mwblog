
<!--
title: 需要尽早知晓的Kubernetes最佳实践
cover: https://www.pulumi.com/blog/kubernetes-best-practices-i-wish-i-had-known-before/meta.png
-->

我希望能早点知道的Kubernetes最佳实践。从我在生产环境中使用Kubernetes的经验中学习，并避免常见的陷阱。

> 译自 [Kubernetes Best Practices I Wish I Had Known Before](https://www.pulumi.com/blog/kubernetes-best-practices-i-wish-i-had-known-before/)，作者 None。

Kubernetes 无可否认地改变了我们构建、交付和运行应用程序的方式。但说实话，开始使用 Kubernetes 感觉就像穿着人字拖攀登珠穆朗玛峰一样。

作为一名云原生开发者和 Kubernetes 爱好者，我通过艰难的经验学习到了一些“早知道就好了”的最佳实践。这些实践本来可以为我节省时间、金钱和麻烦。

![Kubernetes 很容易的冰山一角 meme 是 Kubernetes 具有欺骗性复杂性的经典示例](https://www.pulumi.com/blog/kubernetes-best-practices-i-wish-i-had-known-before/img.png)

*“Kubernetes 很容易”的冰山一角 meme 是 Kubernetes 具有欺骗性复杂性的经典示例*

在这篇文章中，我将重点介绍一些重要的 Kubernetes 最佳实践。这些实践来自我在生产环境中使用 Kubernetes 多年的经验。您可以将此视为您从第一天起就希望拥有的精选“Kubernetes 速查表”。系好安全带；这将是一次激动人心的旅程。

## 1. 不要吝啬资源请求和限制

在 Kubernetes 中的第一个“啊哈！”时刻之一是意识到您可以定义容器请求（保证的资源）和限制（允许的最大值）的 CPU 和内存数量。棘手的部分是：跳过这些设置可能会给您带来麻烦。

- **资源请求（Requests）**：这基本上是您容器的基线。如果您的容器请求 200m CPU 和 512Mi 内存，Kubernetes 调度程序将把您的 Pod 部署到至少具有这么多可用容量的节点上。
- **资源限制（Limits）**：这是上限。如果您的容器试图超过限制，它可能会被限制（CPU）甚至被驱逐（内存）。

专业提示：

- 从某个基线开始，也许是 100-200m CPU、128-512Mi 内存，然后在收集更多数据时进行调整。
- 使用 Prometheus 或 Datadog 等监控工具来分析实际使用情况并根据需要进行调整。

## 2. 像你的生命依赖它一样使用命名空间

如果您将所有内容都部署到默认命名空间中，哦，男孩，是时候进行干预了。命名空间是一种简单而强大的机制，用于组织（和隔离）集群中的资源。

- **基于团队的命名空间**：开发、测试、生产或每个微服务（如果合适）。
- **访问控制**：将命名空间与 RBAC（基于角色的访问控制）策略结合使用，以确保只有合适的人员（和服务）才能访问您的资源。
- **资源配额**：您可以为每个命名空间设置配额（例如，CPU、内存），防止一个流氓微服务占用所有资源。

退一步，设计您的命名空间策略；未来的您会感谢您的。

## 3. 除非必要，否则避免在一个 Pod 中运行多个容器

是的，一个 Pod 可以包含多个容器。但是应该吗？通常，只有当容器紧密耦合并且必须共享资源（如卷或网络命名空间）（例如，用于日志记录或安全代理的 sidecar 模式）时，您才需要在同一个 Pod 中使用多个容器。

为什么要避免多容器 Pod？

- **复杂性**：对单个 Pod 中的多个容器进行故障排除可能很痛苦。
- **耦合**：您失去了独立扩展容器的优势。如果您需要扩展一个容器，您最终会扩展该 Pod 中的所有内容。

遵循“每个 Pod 一个容器”的经验法则，除非您有令人信服的理由（例如 sidecar 模式）。

## 4. 使用包管理器管理您的 YAML 文件

手动处理跨多个微服务的数百个 YAML 文件，就像凌晨 3 点调试意大利面条代码一样有趣。这就是 Helm、Kustomize 或 Timoni 等工具的用武之地。

- [Helm](https://helm.sh/): Kubernetes 的“包管理器”。它使用您可以通过值自定义的 Chart（模板）。
- [Kustomize](https://kustomize.io/): 一个原生 Kubernetes 工具，允许您在基本 YAML 清单上叠加更改。
- [Timoni](https://timoni.sh/): Timoni 是一个 Kubernetes 包管理器，由 CUE 提供支持，并受 Helm 的启发。

专业提示：如果您不熟悉 Helm，请从 Helm Hub 或 Artifact Hub 中的官方 Chart 开始。然后根据您的喜好进行自定义。您将避免 YAML 重复的困扰。

或者，试用 [Pulumi](/docs/get-started/) 并使用真正的编程语言来管理您的 Kubernetes 基础设施。

## 5. Ingress 和网络最佳实践

在 Kubernetes 中，网络可能会很快变得复杂。在服务、Ingress 控制器和负载均衡器之间，很容易陷入困境。请记住以下几点：

- 使用 Ingress 控制器/[Gateway API](https://gateway-api.sigs.k8s.io/)(NGINX、Traefik、HAProxy、Istio Gateway 等)来管理外部访问。
- 利用基于路径和基于子域的路由来简化您的网络拓扑。
- TLS 终止：在您的入口层终止 SSL/TLS。您可以卸载证书管理（例如，通过 cert-manager）并保持集群流量的安全和高效。
- Ingress是Kubernetes中一个强大的概念，请花时间正确设置它。混乱的Ingress配置就像通往漂亮大宅的坑坑洼洼的车道。

![Description of image](https://www.pulumi.com/blog/kubernetes-best-practices-i-wish-i-had-known-before/img_1.png)

## 6. 依靠存活性探针、就绪探针和启动探针

Kubernetes有点像个人助理，但它需要清晰的指令。如果没有正确配置[存活性探针、就绪探针和启动探针](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)，您的集群将无法判断容器的健康状况。

- **存活性探针**: 检查您的容器是否存活。如果失败，Kubernetes将重启容器。
- **就绪探针**: 检查您的容器是否已准备好接收流量。在准备好之前，它不会接收流量。
- **启动探针**: 对于启动需要一段时间才能完成的应用程序非常有用。它可以防止容器在初始加载期间过早被终止。

专业提示：在存活性探针之前先使用就绪探针。您不希望您的容器仅仅因为尚未准备好就被终止。微调阈值、周期和超时参数。

## 7. 注意您的安全：RBAC、Pod安全性和密钥

在Kubernetes中，安全不仅仅是锦上添花——它是至关重要的。如果您的集群遭到破坏，游戏就结束了。

**1. RBAC（基于角色的访问控制）**：

- 从第一天起就实施它。
- 使用最小权限原则。只为每个用户、服务帐户或应用程序提供他们所需的访问权限。

**2. Pod安全**：

- 使用[Pod安全准入](https://kubernetes.io/docs/concepts/security/pod-security-admission/)功能来执行标准（例如，不允许特权容器）。
- 确保您不是在绝对必要的情况下才以root用户身份运行容器。

**3. 正确管理密钥**：

- 不要在容器镜像或环境变量中以纯文本形式存储凭据或API密钥。
- 使用[外部密钥操作符](/docs/esc/integrations/kubernetes/external-secrets-operator/)或[密钥存储CSI驱动程序](/docs/esc/integrations/kubernetes/secret-store-csi-driver/)将密钥存储在外部密钥存储中，例如[AWS密钥管理器](https://aws.amazon.com/secrets-manager/)、[Pulumi ESC](/docs/esc/)或[HashiCorp Vault](https://www.vaultproject.io/)。

## 8. 监控一切（然后更多地监控）

在Kubernetes中，监控不是可选的——而是强制性的。随着容器不断出现和消失，您需要强大的可观察性来了解幕后发生的事情。

[Prometheus + Grafana](https://github.com/prometheus-operator/kube-prometheus)：度量和仪表板的经典组合。
- ELK / EFK / [Grafana Loki](https://grafana.com/oss/loki/)堆栈：Elastic（或OpenSearch）用于日志，加上Kibana和Fluentd/Fluent Bit用于日志收集或Grafana Loki用于日志。
- Jaeger / Zipkin / Tempo：如果您有相互调用的微服务，则用于分布式跟踪。

尽早设置警报。您不希望您第一次遇到麻烦是午夜时分从愤怒的用户那里得到“为什么应用程序这么慢？”的消息。

## 9. 使用CI/CD自动化部署

Kubernetes最大的优势之一是它使自动化整个发布过程变得更容易。如果您仍在进行手动部署，那么现在是时候转向CI/CD管道了。

- Jenkins、[GitLab](https://docs.gitlab.com/ee/ci/)、GitHub Actions，您可以选择。
- 拥抱[GitOps](https://opengitops.dev/)：将所有清单存储在Git中，并让像[Flux](https://fluxcd.io/)或[Argo CD](https://argoproj.github.io/cd/)这样的工具将它们同步到您的集群。
- 如果部署失败，则自动回滚。
- 自动化不仅加快了交付速度，而且还大大减少了人为错误的空间。

## 10. 保持Kubernetes集群和组件更新

运行过时的Kubernetes版本就像在2025年使用运行iOS 6的手机一样。不可取。

**Kubernetes发布周期**: 次要版本大约[每三个月](https://kubernetes.io/releases/release/)发布一次，补丁程序发布频率更高。

**升级策略**：

- 首先在开发环境中进行测试。
- 备份您的etcd（键值存储）。
- 升级控制平面，然后升级工作节点，或者使用为您处理部分此工作的托管服务（例如，EKS、GKE、AKS）。

保持您的依赖项更新（例如，容器运行时、CNI插件等），以从最新的安全性和性能改进中受益。

## 11. 明智地使用标签和注释

[标签（Labels）](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)和[注释（Annotations）](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)乍一看似乎微不足道，但它们对于组织良好的集群来说是改变游戏规则的关键。

- **标签**: 用于 Kubernetes 对象分组和选择的键值对。例如，`app=my-app`、`env=staging`、`team=payments`。
- **注释**: 用于附加非标识元数据的键值对（例如，版本信息、联系邮箱或上次部署时间戳）。一致的标签策略有助于快速过滤资源并维护集群的清晰思维导图。

## 12. 采用多环境方法

如果您的开发、登台和生产环境共享一个集群，您就是在玩火。虽然可以这样做，但最佳实践是将生产工作负载与测试环境隔离。

- **独立集群**: 至少为开发/登台环境和生产环境各准备一个集群。有一些工具，例如[vCluster](https://www.vcluster.com/)，可以在单个集群中创建虚拟集群。
- **命名空间隔离**: 如果您必须在同一个集群中运行它们，请使用严格的基于命名空间的隔离和 RBAC 规则。
保持环境分离可以降低风险，并使在沙箱中测试新功能更容易。

## 13. 优化您的容器镜像

不要交付包含一半 Ubuntu 系统以及随机残留文件的庞大容器镜像。这会导致部署缓慢和资源浪费。

- 使用轻量级基础镜像，例如 [distroless](https://github.com/GoogleContainerTools/distroless)、alpine 或基于最小操作系统的镜像。
- 清理 Dockerfile 中的临时文件和依赖项。
- 使用诸如 [Trivy](https://trivy.dev/latest/) 或 [Anchore](https://anchore.com/) 之类的工具定期扫描您的镜像是否存在漏洞。

## 14. 实施可靠的日志记录策略

日志是您进行故障排除的首选工具，在 Kubernetes 中，您需要一个能够处理短暂 Pod 的解决方案。

- **集中式日志记录**: 无论是 ELK/EFK、Splunk 还是托管服务，请确保日志不会仅仅存储在短暂的容器存储中。
- **结构化日志记录**: JSON 或其他结构化格式有助于您的日志系统更有效地解析和过滤日志。
- **日志保留和轮换**: 定义明确的策略以防止日志存储膨胀。

相信我，您不希望在生产事故发生时四处寻找日志。

## 15. 将 Kubernetes 当作牲畜，而不是宠物

服务器的古老格言——将它们视为牲畜，而不是宠物——也适用于 Kubernetes。不要依赖手动修复或人工干预。尽可能争取不变的基础设施：

- 如果 Pod 出现问题，请在 YAML、[Code](/product/infrastructure-as-code/) 或容器镜像中修复它，重新部署，然后让旧的 Pod 消失。
- 避免对正在运行的容器进行偷偷摸摸的“快速修复”——这些更改会在 Kubernetes 重新启动 Pod 的那一刻消失。
- 拥抱短暂的环境和动态扩展。这就是 Kubernetes 最擅长的事情！

## 16. 对于复杂的部署，考虑更高级的方法

虽然原生 YAML 清单可以用于较小的 Kubernetes 部署，但随着项目和团队的增长，它们往往会变得难以管理。[Pulumi](/blog/yaml-terraform-pulumi-whats-the-smart-choice-for-deployment-automation-with-kubernetes/) 为部署自动化提供了一个强大的替代方案，它提供：

- **真正的编程语言**: 使用 TypeScript、JavaScript、Python、Go、Java 或 C# [用于类型安全、可测试的基础设施代码](/docs/iac/languages-sdks/)。
- **跨云灵活性**: 使用单个工具管理[多个云提供商](/docs/iac/clouds/)和 Kubernetes 中的资源。
- **可重用模块**: 将常见模式抽象为[可重用组件](/docs/iac/using-pulumi/pulumi-packages/)，减少样板代码并防止漂移。
- **强大的工具和生态系统**: 从包管理器、[IDE 集成](/docs/iac/concepts/testing/)和丰富的共享 Pulumi 组件库中受益。

通过采用 Pulumi，您可以避免处理无数 YAML 文件的复杂性，并为您的 Kubernetes 基础设施获得更精简、更易于维护的工作流程。

## 最后的想法

![图片描述](https://www.pulumi.com/blog/kubernetes-best-practices-i-wish-i-had-known-before/img_2.png)

Kubernetes 就像一把瑞士军刀：功能强大、用途广泛，但如果您不小心，也很容易误用。通过采用这些最佳实践、声明式配置、合理的资源分配、强大的安全性、强大的可观察性和自动部署，您可以使您的集群平稳运行。

如果您已经以艰难的方式吸取了一些教训，那么您并不孤单。但是 Kubernetes 的好处在于，每一次挫折都会让您获得更多经验来微调您的方法。

让我们一起学习（和忘记）吧，这样我们才能像专业人士一样驯服这只 Kubernetes 野兽。或者至少，像我们将要成为的专业人士一样！
