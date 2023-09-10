# 七步实现高效的 Kubernetes 策略

是时候专注于互动式地塑造和执行您组织使用既定 Kubernetes 策略来产生影响的方式了。

![](https://cdn.thenewstack.io/media/2023/09/3f1ada7c-policies-1024x683.jpg)
*图片来自 Shutterstock 的 Net Vector*

您刚开始一份新工作，首次承担部分 Kubernetes 基础设施的操作和管理责任。您对能够深入云原生的发展感到兴奋，但同时也非常担心。

是的，您确实担心如何编写遵循最佳命名和资源使用控制实践的安全应用程序，但生产环境中已经部署的其他应用又该怎么办呢?您开启新的工具查看当前状况，发现存在 100 个 CVE 和严重或关键的 [YAML](https://roadmap.sh/videos/yaml-in-depth) 配置错误。您关闭标签，告诉自己以后再处理这些问题。

你会这样做吗?

也许你们中最有野心和无畏的人会，但问题是，虽然云原生社区喜欢讨论安全性、标准化和“左移”等话题，但这些讨论并没有减轻由安全性、资源、语法和工具问题带来的压力感。似乎还没有哪种开发范式或工具找到在不压垮开发者和运维人员的情况下，使配置错误可见的“最佳点”。

就像我们面对的所有待办事项列表一样，无论是工作还是家务，我们的大脑在同一时间只能有效处理有限的问题数量。太多问题会使我们迷失在切换上下文和优先对症下药而非进行持久改进之间。我们需要更好的方式来限制范围(即分类)，设定里程碑，最后使[安全](https://thenewstack.io/security/)工作变得可管理。

现在是时候忽略问题数量，而专注于互动塑造和执行您的组织使用既定[策略](https://medium.com/kubeshop-i/kubernetes-yaml-policies-101-649a23780371)产生影响的方式了——无需压力感。

## 云原生策略的阴暗历史

自 Kubernetes 最初问世以来，YAML 配置一直是构成正常运行的集群和应用程序的重要组成部分。作为开发者的应用代码与运维工程师保持集群正常运行之间的关键桥梁，YAML 不仅难以完全掌握，也是 [Kubernetes](https://thenewstack.io/kubernetes/) 中大多数部署/服务级问题的源头。更糟的是，无论是开发者还是运维工程师都不想单独为 YAML 负责。 

策略进入云原生领域的目的是实现 YAML 配置的自动化编写和生产环境批准。如果没有一个人或团队愿意根据内部风格指南手动检查每个配置，那么策略可以[慢慢塑造团队如何应对](https://medium.com/kubeshop-i/kubernetes-yaml-policies-101-649a23780371)安全性、资源利用和云原生最佳实践等常见的错误配置，更不用说他们应用中独特的各种规则或习语。

Kubernetes 中的策略面临的挑战在于，Kubernetes 对如何、何时以及为何执行策略持中立态度。您可以用多种方式编写规则，在软件开发生命周期(SDLC)的不同点执行策略，并出于完全不同的原因使用它们。

没有比 2016 年随 Kubernetes 1.3 版引入的 Pod 安全策略(PSP)更能体现这种困惑的例子了。PSP 旨在控制 Pod 的运行方式，拒绝任何不合规的配置。例如，它允许 K8s 管理员[防止开发人员](https://unofficial-kubernetes.readthedocs.io/en/latest/concepts/policy/pod-security-policy/)在处处运行特权 Pod，从根本上解耦了底层 Linux 安全决策与开发生命周期。

由于一些良好的原因，PSP 从未离开测试阶段。这些策略仅在请求创建 Pod 时应用，这意味着无法对 PSP 进行回溯或默认启用。Kubernetes 团队承认 PSP 使意外授予过于广泛权限变得过于容易，此外还存在[其他困难](https://youtu.be/SFtHRmPuhEw?feature=shared&t=970)。

PSP 时代的 Kubernetes 安全是如此艰难，以至于它激发了发布周期管理的新规定：任何 Kubernetes 项目不能在测试阶段停留超过两个发布周期，必须成为稳定版本或被标记为弃用并移除。

另一方面，PSP 在一个积极的方向推动了 Kubernetes 中的安全：通过分离 Kubernetes 安全策略的创建和实例化，PSP 开辟了新的生态系统，用于外部准入控制器和策略执行工具，比如 [Kyverno](https://kyverno.io/)、[Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/) 和[ Monokle](https://monokle.io/)。

正是借助这些工具，我们摆脱了 PSP 的束缚，用 Pod 安全标准(PSS)取而代之。我们一会儿会回到这两者的重大区别。

## 基于阶段的 Kubernetes 策略方法

随着策略创建与实例化的这种确立的解耦，您现在可以在集群、环境和团队中应用一致的策略语言，而不考虑选择哪些工具。您还可以随时切换用于创建和实例化的工具，并在集群中获得可靠的结果。

创建通常发生在集成开发环境(IDE)中，这意味着您可以坚持使用当前喜欢的 IDE 来表达特定规则语言(如 [Open Policy Agent，OPA](https://monokle.io/learn/what-is-opa-for-the-kubernetes-connoisseur-its-as-essential-as-salt))、声明式语法(如 Kyverno)或编程语言(如 Go 或 TypeScript)的规则。

实例化和执行可以发生在软件开发生命周期的不同阶段。正如我们在上一篇关于 Kubernetes YAML 策略的[入门文章](https://medium.com/kubeshop-i/kubernetes-yaml-policies-101-649a23780371)中看到的，您可以在配置生命周期的一个或多个点进行验证:

- 在开发人员的命令行接口(CLI)或 IDE 中预提交
- 通过 CI/CD 管道预部署
- 通过 Kyverno、Gatekeeper 等 [admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) 部署后
- 集群内检查部署状态是否仍符合策略标准

策略实例化、验证和执行在 SDLC 中的时间越晚，错误配置进入生产环境的可能性就越大，识别和修复任何发现的错误配置源所需的工作也就越多。您可以在多个阶段实例化和执行策略，但越早越好——这是 Monokle 擅长的，它拥有强大的预提交和预部署验证支持。

有了前面的场景 —— 可怕的 90 个问题 —— 以及对 Kubernetes 策略环境的理解，您可以开始消除面前的错误配置。

### 步骤 1：实施 Pod 安全标准

首先讲述前面提到的 PSS。Kubernetes 现在描述了[三个](https://kubernetes.io/docs/concepts/security/pod-security-standards/)可以快速在集群中实施和执行的全面的策略。“特权”策略完全不受限制，应仅保留给由管理员管理的系统和基础设施工作负载。

您应该从实施“基线”策略开始，它允许[最小化地指定 Pod](https://youtu.be/SFtHRmPuhEw?t=2018)，这也是大多数刚接触 Kubernetes 的开发人员的起点:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: default
spec:
  containers:
    - name: my-container
      image: my-image
```

基线的优势在于您可以防止已知的特权提升，而无需修改所有现有的 Dockerfile 和 Kubernetes 配置。当然，会有一些例外，我待会儿再谈。

在命名空间级别创建和实例化此策略级别相对简单直接:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: my-baseline-namespace
  labels:
    pod-security.kubernetes.io/enforce: baseline
    pod-security.kubernetes.io/enforce-version: latest
    pod-security.kubernetes.io/warn: baseline
    pod-security.kubernetes.io/warn-version: latest
```

不可避免地会有一些特殊服务需要比基线许可更多的访问权限，比如用于日志和可观测性收集的 [Promtail Agent](https://grafana.com/docs/loki/latest/clients/promtail/)。在这些需要某些有益功能的情况下，这些命名空间将需要在特权策略下运行。您需要跟上来自该供应商的安全改进，以限制您的风险。

通过对大多数配置实施基线 Pod 安全标准，仅为少数配置允许特权，然后修复违反这些策略的任何错误配置，您已经完成了下一个策略里程碑。

### 步骤 2：修复 Label 和 Annotation

Label 用于标识资源以进行分组或过滤，而 Annotation 用于重要但不标识的上下文。如果您的头脑仍然晕头转向，这里有 Richard Li 在 Ambassador Labs 的一个[简单定义](https://blog.getambassador.io/kubernetes-labels-vs-annotations-95fc47196b6d)：“Label 是为 Kubernetes 准备的，Annotation 是为人类准备的。”

Label 应仅用于其预期目的，即使如此，在应用 Label 的位置和方式上也要谨慎。过去，[攻击者曾使用 Label](https://sysdig.com/blog/exposed-prometheus-exploit-kubernetes-kubeconeu/) 深入探索 Kubernetes 集群的架构，包括哪些节点运行了哪些 Pod，而不会留下他们运行的查询的日志。

对 Annotation 也适用相同的想法：虽然它们是为人类准备的，但通常用于[获取凭据](https://github.com/kubernetes/ingress-nginx/issues/8503)，从而使攻击者获得更多机密信息的访问权限。如果您使用 Annotation 描述发生问题时应联系的人员，请知道您正在制造额外的社会工程攻击目标。

### 步骤 3：迁移到受限 PSS

虽然基线是可以接受的但还不够安全，“受限”  Pod 安全标准采用了强化 Pod 的当前最佳实践。正如 Red Hat 的 Mo Khan [曾描述](https://youtu.be/SFtHRmPuhEw?t=1951)的那样，受限标准确保“您能做的最坏的事情就是毁掉自己”，而不是您的集群。

使用受限标准，开发人员必须编写以只读模式运行的应用程序，只启用 Pod 运行所必需的 Linux 功能，在任何时候都不能提升特权等。

我建议先从基线开始，然后迁移到后面的受限，作为单独的里程碑，因为后者几乎总是需要对现有的 Dockerfile 和 Kubernetes 配置进行主动更改。一旦实例化和执行受限策略，您的配置将需要遵守这些策略，否则将被您的验证器或准入控制器拒绝。

### 步骤3a：抑制而不是忽略不可避免的误报

当您逐步实现基线和受限两个里程碑时，您正在接近一个更成熟(并且更复杂)的策略管理阶段。为了确保所有人都在同一页面上了解当前的策略里程碑，您应该开始处理那些即使在受限PSS下也必须明确允许的误报或配置。

在选择忽略规则还是抑制规则时，始终青睐抑制。这需要一个可审计的操作，以日志或配置更改的形式来编码对既定策略框架的异常。您可以在源中添加抑制，直接添加到 K8s 配置中，或者在外部添加，其中开发者请求他们的运维同行重新配置他们的验证器或准入控制器以允许一个“错误配置”通过。

在 Monokle 中，您可以在配置中直接作为 Annotation 添加源抑制，并带上[静态分析结果交换格式(SARIF)规范](https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html)中称为 [justification](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317739) 的内容:

```yaml
metadata:
  annotations:
    monokle.io/suppress.pss.host-path-volumes: Agent requires access to back up cluster volumes
```

### 步骤 4：添加常见加固指南

此时，您已经超越了 Kubernetes 确立的安全框架，这意味着您需要更主动地建立和实现自己的里程碑。

国家安全局(NSA)和网络安全和基础设施安全局(CISA)发布了一份广受欢迎的 [Kubernetes 加固指南](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)，其不仅详细介绍了影响 pod 级别的改进，例如有效使用不可变的容器文件系统，还包括网络隔离、审计日志记录和威胁检测。

### 步骤 5：即插即用时刻

实施建立的部分或全部硬化指南后，每个新策略都涉及选择、信任和权衡。在 Google 或 Stack Overflow 上花点时间，您会找到许多建议将即插即用策略集成到执行机制中的方法。

您可以从众包策略中受益，其中许多来自拥有更独特经验的人，但请记住，虽然规则可能善意的，您不了解建议者的优先事项或操作环境。如果他们必须实施某些“高悬果实”策略，那是因为他们不得不这样做，而不是因为它们广泛有价值。

一个持续争论的问题是是否以及如何严格 limit 容器的资源需求。request 限制也是如此。不配置 limit 可能会引入安全风险，但如果您严格约束 Pod，它们可能无法正常工作。

### 步骤 6：添加自定义规则以解决未知特殊情况

现在，您已经处于 Kubernetes 策略的最前沿，远远超出了造成 80% 负面生产影响的 20% 错误配置和漏洞。但即使现在，在实施所有最佳实践和集体云原生知识之后，您也无法避免意外引发事件或中断的错误配置——安全性和稳定性中美妙的未知未知。

一个好的经验法则是，如果某种特殊的(错误)配置在生产中造成两次问题，那么是时候将其编码为自定义规则，在开发过程中执行或由准入控制器执行。仅仅内部记录地等待开发人员阅读、留意并在彼此的拉取请求审查中发现它们太重要而不能依赖。

一旦将自定义规则编码到现有策略中，它们就成为尽可能接近开发的护栏。如果您能够在开发人员即使提交工作之前就与他们达成验证，Monokle Cloud 可以通过自定义插件和您在本地运行的开发服务器无缝地做到这一点，那么您可以为整个组织节省大量的反复工作和等待 CI/CD 管道不可避免地失败的时间，而不是建立新功能或修复错误。

## 小结

如果您实施了上述所有框架和里程碑，并对 Dockerfile 和 Kubernetes 配置进行了所有必要的更改以满足这些新策略，您会发现 90 个主要漏洞的数量大大减少到一个更易管理的数字。

您已经看到了我们逐步塑造和执行 Kubernetes 策略的方法的价值。您可以像 Monokle 在预提交阶段独特地做的那样，与新策略和规则的影响进行互动，这将使您能够在不压倒自己或他人的情况下采取渐进步骤。

您甚至可能会自豪地宣称您的 Kubernetes 环境完全无误配置。这无疑是一个胜利，但它不是保证——总会有新的 Kubernetes 版本、新应用程序和新最佳实践需要结合您已经做的工作进行整合。这也不是与领导层或管理团队讨论您的成就的最佳方式。

利用框架和加固指南的优势在于，您有更好的共同基础来讨论您对认证、合规性和长期安全目标的影响。

对非专业人员来说，以下哪一个听起来更有说服力:

- 您将 CVE 数量从 90 减少到 X，
- 或者您完全遵守了 NSA 的 Kubernetes 加固指南?

我们越快地不再关心数量而更关注常见的里程碑，并尽可能早在应用生命周期中执行(最好是预提交!)，我们就能越早为每个独特的云原生策略找到可持续的最佳点。