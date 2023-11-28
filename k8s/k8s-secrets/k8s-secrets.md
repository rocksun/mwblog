<!-- 
title: 普通Kubernetes Secret足矣
cover: ./cover.png
 -->

众所周知，Kubernetes secret 只是以 base64 编码的字符串，存储在集群的其余状态旁边的 etcd 中。[自 2015 年引入 secret 以来](https://github.com/kubernetes/kubernetes/pull/4514)，安全专家就一直在嘲笑这一决定，并寻求其他替代方案。我认为这些人没有抓住要点。

> 译自 [Plain Kubernetes Secrets are fine](https://www.macchaffee.com/blog/2022/k8s-secrets/)。

密钥 API 的设计可以追溯到 Kubernetes v0.12 之前。在最初的[设计文档之前的一个讨论中](https://github.com/kubernetes/kubernetes/issues/2030#issuecomment-61584588)，有一行字暗示了为什么人们可能会对密钥感到困惑:

> 没有威胁模型，很难评估这些替代方案

这正是问题所在。保护软件的天真方法是盲目实施安全功能清单。但是更深入地了解安全性会很快发现，完美的安全是不可能的；您必须做出权衡并优先考虑最有可能的场景。创建[威胁模型](https://owasp.org/www-community/Threat_Modeling_Process)可以帮助您做出这些决定。让我们为 Kubernetes 密钥创建一个简单的威胁模型，看看会出现什么。

## Kubernetes Secret的简单威胁模型

### 我们在保护什么？

Secret通常用于存储数据库密码和私钥，这意味着它们是一个高价值目标。

### 安全失败看起来像什么？

如果攻击者能够读取Secret，他们可以使用它执行进一步的攻击，例如窃取数据、修改/删除/勒索数据，或者获得授权执行诸如开采加密货币的 Pod 等操作。通常，我们会使用类似 [DREAD](https://wiki.openstack.org/wiki/Security/OSSA-Metrics#DREAD) 的东西来对不同攻击的严重性进行排名，但暴露Secret有点双重的，除非我们有一个特定的Secret。

### 如何偷窃Secret(会出什么问题)？

至少，Secret需要以纯文本的形式存在于需要它的任何应用程序的内存中，在同一节点上的另一个进程可以([几乎](https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/commit/?id=72101855fb9a2b3cd72c051791609a217c4a6281))[总是](https://github.com/n1nj4sec/mimipy)通过足够的毅力来偷窃它。 我们还需要在某个持久的地方存储Secret。 在我们的例子中，Secret存储在 etcd 中，可以从 Kubernetes API 访问。

由于Secret必须存在于这两个地方，所以它们可以通过以下任何方式被窃取:

1. 同一节点上的恶意进程(扫描内存，如果不强制安全上下文，直接从 /proc 或 CRI 读取)
2. 控制平面节点的根访问(读取 etcd 的内存，读取磁盘转储，或窃取客户端证书并直接连接)
3. 工作节点的根访问(窃取 kubelet 的客户端证书并从 API 服务器读取Secret，或直接读取Secret文件/环境变量)
4. 控制平面节点物理服务器的访问(将硬盘连接到另一台计算机并读取 etcd 数据或转储 RAM)
5. 未来意外攻击(这是一个总括，有助于我们选择具有更小攻击面积的解决方案)

一些更古怪的黑客攻击，如社会工程、恶意内部人员、人为错误/配置错误或硬件供应链攻击当然是可能的，但在 Kubernetes 可以现实主义地解决的范围之外。

### 我们如何防止这些攻击？

对于攻击#1：从内存中窃取Secret是我们不得不容忍的风险。 应用程序可以使用自动过期令牌或多重身份验证，但由于这些功能依赖于特定应用程序，因此不在范围内。

对于攻击#2和#3：节点的根访问是一个巨大的问题。 这可以通过常规的服务器加固、修补和[防止特权 Pod 运行来减轻](https://kubernetes.io/docs/concepts/security/pod-security-standards/)，但这是一个非常复杂的威胁要解决。

对于攻击#4：对物理服务器的访问在一定程度上可以通过加密静态磁盘来减轻。 至关重要的是，加密密钥必须存储在单独的安全域中才能获得任何安全性好处。 但由于物理访问通常意味着游戏结束，所以你只需要一些严密的物理安全性。

对于攻击#5：在这里，我们不得不赌一把未来是否会出现零天漏洞。 我们可以通过选择更简单和经过良好测试的方法来提高我们的机会，没有比普通 Kubernetes Secret 更简单的了。

## 威胁模型的启示

威胁模型揭示了一个不方便的事实，即存储Secret很难，因为明文版本必须存在某个地方(与例如密码哈希形成对比)。这只是可逆加密的问题。

任何改进现有Secret实现的方法都必须减轻更多的攻击，但是我认为没有一种替代plain Kubernetes Secret的方案提供足够的额外安全性来值得麻烦。

## Kubernetes 密钥的替代方案

让我们看看一些存在的替代方案，看看它们的测量结果如何。

### etcd 静态加密

我很震惊这个仍然是 #1 推荐的替代方案，考虑到它的作用有多荒谬。

[etcd 静态加密](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/)涉及使用存储在 etcd 本身相同文件系统上的密钥加密 etcd 中的所有Secret。因此，我们的威胁模型中的四种攻击都没有得到缓解。 甚至“物理访问”攻击也不行，因为密钥存储在同一磁盘上! 或者至少是另一个磁盘，可以从同一主机访问(文档中甚至没有提到的选项)。

### 通过 KMS 加密 etcd

您可以使用来自您最[喜欢的云提供商的密钥管理服务](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/)(KMS)替换上述方法中的加密密钥。

虽然这被列为“最强”的方法，但根据我们的威胁模型，它基本上与普通 Kubernetes 密钥一样不安全。 能够访问节点的攻击者可以像 etcd 那样解密Secret，然后再将它们窃取出去。 至少，这可以减轻对磁盘的物理访问，如果且仅当 KMS 客户端使用自动轮换的多重身份验证令牌向云提供商进行身份验证时。

使用此选项需要对云提供商进行硬依赖，需要大量的复杂性，并且如果它曾经中断，会有很大的故障半径。 如果您被迫加密静态Secret以符合合规性，尽管它实际上没有改善您的安全态势，但这确实是您最好的选择。

### Bitnami Sealed Secrets

[Sealed Secrets](https://github.com/bitnami-labs/sealed-secrets)真的不是Secret的替代品，但我见过人们认为它们是。 Sealed Secrets允许您将加密的Secret存储在版本控制中。 当您将 SealedSecret `kubectl apply` 到集群时，它会自动被解密并转换为普通 Kubernetes Secret 的 Sealed Secrets 控制器。

由于 SealedSecrets 会变成普通的Secret，我们的威胁模型中的任何攻击都没有得到缓解。 如果您没有其他安全地方存储Secret，SealedSecrets 是不错的选择，但是我们的威胁模型认为集群外部的Secret存储在范围之外。

### Vault Sidecar 注入器

这是人们指向的大问题。 从本质上说，Vault 只是一个带有一些关键功能的键值存储:

1. 一个聪明的 [Shamir 密封进程](https://www.vaultproject.io/docs/concepts/seal)，人们很快会禁用它，而使用[自动解封](https://www.vaultproject.io/docs/concepts/seal#auto-unseal)，这就像 etcd 通过 KMS 加密一样消除了密封的好处。
2. 一个丰富的策略语言，很少有人会去学习。
3. 很好的审计，没有人监控。

因此，从根本上说，除非您为托管 Vault 实例或公司内 Vault 专家团队支付费用，否则 Vault 只是一个键值存储。 我曾在一家拥有整个团队运行 HSM 支持的企业版 Vault 的公司工作过，但那东西仍然经常宕机。

但是，让我们假设您有足够的财力维护一个不可能完美的 Vault 实例。 您刚刚在 Kubernetes 集群中安装了 [Vault Sidecar 注入器](https://www.vaultproject.io/docs/platform/k8s/injector)。 您能从这个复杂的安排中获得足够的安全性吗? 我认为不能。

sidecar 注入器的工作原理是修改 pod 以包含 Vault 客户端 sidecar，该 sidecar 向您的 Vault 服务器进行身份验证，下载Secret，并将其存储在您的应用程序可以像常规文件一样访问的共享内存卷中。

对于攻击#1：由于Secret仍在内存中，因此攻击者仍然可以从节点中窃取它。

对于攻击#2和#3：如果攻击者入侵任何节点(工作程序或控制平面)，他们可以运行任何具有正确 Vault 注释的 pod 并窃取Secret。

对于攻击#4：如果有人访问物理节点，他们无法从磁盘获取Secret，但他们可以获取与普通Secret相关的服务帐户的保险库凭据，并且如果您在 Kubernetes 内运行 Vault，则可以这样窃取Secret。

但是，您仍然必须担心 Vault 运行所在服务器的物理访问。 Vault 在“密封”时会对静态数据进行加密，但是如果您使用自动解封，则攻击者可以使用磁盘上的云凭据模拟该过程。 该死的，有物理访问权限的人无需麻烦地读取您的磁盘；如果您有一个可用的 PCI 插槽，他们可以直接转储 RAM。

对于攻击#5：运行 Vault 的复杂性极大地增加了您的攻击面。 我比大多数公司都更相信 HashiCorp 会抓住问题，但更多的运动部件总是更多的风险。 有时候这种风险是值得的(是的，散列密码比不散列更复杂，但优点显然大于缺点)，但是只有在缓解了其他 4 种攻击的情况下才值得。

因此，根据我们的威胁模型，使用 Vault 引入了一些间接层，但最终并没有解决比普通 Kubernetes Secrets 更多的攻击。 使用加密磁盘并将密钥存储在安全的地方会以更简单、更便宜的方式提供相同级别的安全性。

## 结论

通过创建一个包括你想要缓解的攻击类型的威胁模型，很明显，安全地管理机密信息非常困难。问题不在于机密信息只是 base64 编码；这从未被设计成一个安全功能。这个问题也不能简单地通过软件/云提供商及其花哨的文档来回避。

对于如此安全敏感和困难的存储机密信息，应从威胁模型开始。如果根据威胁模型，多个解决方案具有类似的安全性，选择更简单的一个来减少整体攻击面。
