
<!--
title: Kubernetes 1.30命名功能更强大
cover: https://cdn.thenewstack.io/media/2024/04/22cfa2f9-kubernetes-1-30.png
-->

在发现几个关键漏洞后，Kubernetes 开始认真考虑使用用户命名空间保护 Pod。此外，还提供了更精细的容器扩展。

> 译自 [Kubernetes 1.30 Gets Better at Naming Things](https://thenewstack.io/kubernetes-1-30-gets-better-at-naming-things/)，作者 Joab Jackson。


**请出示护照！**

继去年 1 月公开披露容器泄漏事件后，Kubernetes 1.30 版本提供了更多安全检查点，加强了权限和访问控制。不再允许错误进程在 K8s 管理的容器和 Pod 中匿名漫游。

感谢 [KEP 24](https://github.com/kubernetes/enhancements/issues/24)（“AppArmor 支持”），Kubernetes 容器和 Pod 可通过 [AppArmor](https://apparmor.net/) 获得保护，AppArmor 是一个 Linux 安全模块，用于在运行时强制执行策略。它限制了应用程序根据其配置文件对系统执行的操作。

用户通过 [API](https://thenewstack.io/API-management/) 指定 AppArmor 配置文件。

该增强提案已提出约三年。权限强制执行是一项艰巨的任务。

另一项增强功能：现在 Pod 可以拥有用户名，这要归功于 [KEP 127](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/127-user-namespaces#summary)（“支持用户命名空间”），[相关工作被迅速推进](https://kubernetes.io/blog/2024/04/22/userns-beta/)，因为在 1 月份发现了一系列关键容器漏洞，这些漏洞利用了这种访问权限缺失的问题。

Kubernetes 此次最新版本的发布负责人 [Kat Cosgrove](https://github.com/katcosgrove) 表示，此功能“让你可以更好地隔离 Pod”。

同样出于安全考虑，[KEP 3488](https://github.com/kubernetes/enhancements/tree/master/keps/sig-api-machinery/3488-cel-admission-control#summary)（“用于准入控制的 CEL”）引入了一种更丰富的表达式语言用于准入控制，Cosgrove 表示，这提供了一种“更具动态性和表现力的方式来评估任何准入请求”。

“你可以在 Kubernetes API 中定义和强制执行一些非常复杂的策略，这使得安全和治理功能更容易控制，同时不会影响性能。”

## 团队负责人：需要协调

此版本绰号为“Uwubernetes”，相当常规。没有弃用任何值得注意的功能，并且它带来了一些非常及时的安全增强功能。总体而言，v1.30 带来了 45 项增强功能——17 项稳定，18 项为 Beta，10 项为 Alpha。

[云原生计算基金会](https://cncf.io/?utm_content=inline+mention) 的 Kubernetes 的发布负责人有点像“牧猫”，[Cosgrove](https://github.com/katcosgrove) 说。

“有很多政治活动”要做。

Cosgrove 领导着一个庞大的团队，有 9 名直接下属，35 名向他们汇报工作。他们分布在全球，跨越五个不同的子团队。

## Kubernetes 增强

将一项功能纳入 Kubernetes 的下一个版本涉及多个障碍。

一项提议的功能始于 [Kubernetes 增强提案](https://www.kubernetes.dev/resources/keps/) (KEP)。一个特殊兴趣小组必须赞助一个 KEP，以便在下一个版本中考虑。提名者进入增强冻结期，在此之后，不会考虑任何新的 KEP。

Cosgrove 说，由于提名的随机性，由此产生的新功能堆积可能是一个“完全的赌博”。Cosgrove 说，在增强冻结期之后，代码冻结期生效，“很多 KEP 会在此期间被放弃”。也许许多人发现，让他们的代码达到生产级别比预期的要[更费力](https://thenewstack.io/5-lessons-from-linkedins-first-foray-into-genai-development/)。

在最近一轮中，95 个 KEP 进入了增强冻结期，但只有 45 个进入了代码冻结期。

Cosgrove 说：“在增强冻结期，人们对自己完成某项工作的能力非常乐观。这没关系，这完全正常。”“然后我们在代码冻结期面对现实。”

在此整个时间范围内已完成测试，并且还可能发布了即将发布版本的几个 Alpha 和 Beta 版本（这些版本并未得到广泛使用）。因此，候选版本将在不久后开始发布。

在完成所有这些协调工作后，SIG 通常要求团队发布负责人休息一个周期，然后再重新投入战斗。

Cosgrove 说：“我准备休息一段时间了。”

## Kubernetes 1.30：你是谁？

除了安全性之外，其他功能还为运维带来了细微差别。例如，[KEP 1610](https://github.com/kubernetes/enhancements/issues/1610)（“基于容器资源的 Pod 自动伸缩”）带来了根据容器资源使用情况自动进行 Pod 伸缩的能力。

Cosgrove 说：“这让你可以根据单个容器的资源使用情况配置自动伸缩，而不是整个 Pod 的总资源使用情况。”

这种微调可以帮助降低云成本，例如，不再需要扩展整个 Pod 来满足特定资源密集型容器的需求。

[Sergey Pronin](https://www.linkedin.com/in/sergeypronin/?originalSubdomain=ru) 注意到了这一点，他是数据库服务提供商 [Percona](https://www.percona.com/?utm_content=inline+mention) 的小组经理。

迄今为止，由于数据限制，数据库系统无法与 Kubernetes Pod 自动扩缩器配合良好。

“随着对分离存储和计算的数据技术（如 [Neon](https://thenewstack.io/neon-branching-in-serverless-postgresql/)、[Xata](https://thenewstack.io/automatically-generate-types-for-your-postgresql-database/)) 兴趣的增长，此功能可能使用户能够正确扩展，”Pronin 在一封电子邮件中指出。

Pronin 还指出了 [KEP-4381](https://github.com/kubernetes/enhancements/issues/4381) “DRA：结构化参数”) 作为“k8s 生态系统的一个非常重要的补充”。这是另一个用于更好地扩展资源的功能，动态资源分配提供了一个 API，用于在 Pod 和 Pod 内的容器之间请求和共享资源。

它被添加到 Kubernetes 中，作为 [v1.26 中的 alpha 功能](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)，尽管在 Kubernetes 1.30 中引入的结构化参数的包含似乎使其更容易使用。

文档指出，“用于动态资源分配的结构化参数提供了一个框架，该框架允许驱动程序自行管理资源，‘使用 Kubernetes 预先定义的特定“结构化模型”’”。
