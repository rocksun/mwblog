<!--
title: 维护者倦怠引发 Kubernetes 安全灾难
cover: https://cdn.thenewstack.io/media/2025/09/0c405f89-eso.png
summary: Kubernetes External Secrets Operator (ESO) 由于维护者倦怠和缺乏支持而面临危机，项目冻结，新功能和修复暂停。社区正在努力寻找至少五名维护者以恢复项目活力，预计需要至少六个月。这反映了开源项目普遍存在的维护问题。
-->

Kubernetes External Secrets Operator (ESO) 由于维护者倦怠和缺乏支持而面临危机，项目冻结，新功能和修复暂停。社区正在努力寻找至少五名维护者以恢复项目活力，预计需要至少六个月。这反映了开源项目普遍存在的维护问题。

> 译自：[How Maintainer Burnout Is Causing a Kubernetes Security Disaster](https://thenewstack.io/how-maintainer-burnout-is-causing-a-kubernetes-security-disaster/)
> 
> 作者：Steven J. Vaughan-Nichols

与太多开源项目一样，我们对 [Kubernetes External Secrets Operator (ESO)](https://external-secrets.io/) 的关注度不够。我们只是想当然地认为该程序会保持更新，并且会一直存在。这是一个很大的错误。最近，ESO 的一位维护者在 Reddit 上写道：“[贡献者基础没有随着用户基础的扩大而扩大](https://www.reddit.com/r/kubernetes/comments/1mp34uk/eso_maintainer_update_we_need_help/)。目前，只有一个非常小的维护者团队负责所有事情。” 事实上，根据瑞典 Kubernetes 咨询公司 [Stakater](https://www.stakater.com/) 的 CEO [Rasheed Amir](https://www.linkedin.com/in/rasheedwaraich/) 在 LinkedIn 上的说法，“[只剩下一名活跃的维护者了。](https://www.linkedin.com/posts/rasheedwaraich_heads-up-for-kubernetes-users-relying-activity-7361460297049563138-PmqW/)”

总而言之，“哎哟！”

结果呢？当时，该项目实际上已经关闭。不会有官方支持：没有 Slack、没有 GitHub 讨论，并且在至少五名活跃维护者站出来之前，不会有新版本。

这是一件大事。ESO 已经成为在 Kubernetes 环境中保护密钥的关键实用程序。ESO 通常是部署到 Kubernetes 部署中的首批附加组件之一。该[程序充当桥梁，用于安全地同步密钥](https://zesty.co/finops-glossary/external-secrets-operator/)，从外部提供商（如 [AWS](https://aws.amazon.com/?utm_content=inline+mention) [Secrets Manager](https://aws.amazon.com/secrets-manager/)、[Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault) 和 [HashiCorp Vault](https://www.hashicorp.com/en/products/vault)）直接同步到 Kubernetes 中。

[![Diagram](https://cdn.thenewstack.io/media/2025/09/7f55a11f-eso-diagrams-high-level-simple-1.png)](https://cdn.thenewstack.io/media/2025/09/7f55a11f-eso-diagrams-high-level-simple-1.png)

*ESO 工作原理的高级图。*

## 什么是 Kubernetes External Secrets Operator (ESO)？

当 ESO 连接到一个或多个外部密钥提供商时，它会通过安全 API 获取敏感数据，例如凭据、API 密钥或证书。然后，它将这些密钥作为原生 Kubernetes Secret 对象注入，以便应用程序可以在运行时安全地访问它们。由于 Kubernetes 的原生密钥存储在 [etcd](https://etcd.io/) 中且未加密，因此 ESO 对于使密钥能够安全地存在于具有审计跟踪和访问控制等功能的外部密钥管理器中至关重要。

ESO 还支持实时更新和自动密钥轮换。这意味着如果[外部系统中的密钥发生更改](https://thenewstack.io/securing-kubernetes-with-external-secrets-operator-on-aws/)，ESO 会自动在 Kubernetes 内部更新它。

## 核心问题：维护者倦怠和缺乏支持

这样一个重要的项目是如何落到如此境地的？ESO 维护者 [Gustavo Fernandes de Carvalho](https://github.com/gusfcarvalho) 在 [ESO GitHub](https://github.com/external-secrets/external-secrets) 上解释说，维护者“[只是‘要做的事情太多了’。](https://github.com/external-secrets/external-secrets/issues/5084) 我们的贡献数量增加了，支持请求增加了，”而活跃的社区成员数量却在不断减少。此外，“我们的维护团队大多已经倦怠了。” 他补充说，“我们现在唯一活跃的维护者是 [@Skarlso](https://github.com/Skarlso) (Gergely Brautigam)——这是一个不好的迹象。上周，当他休假时，我们有 0 个 Pull Requests 合并，+ 20 个问题打开（其中大多数是支持问题）。”

这种情况不能再继续下去了。

## 项目冻结：ESO 的直接后果

剩余的团队已经宣布，在他们拥有至少五名维护者之前，该项目将被冻结。不会有新功能、错误修复或安全补丁。哦，至于指导“初级人员成为维护者”，他们没有[时间和资源来让他们尽快上手](https://thenewstack.io/speeding-time-to-value-the-just-in-time-data-analytics-stack/)。

de Carvalho 报告说，自从他们首次呼吁帮助以来，已有 300 多人自愿提供帮助。此外，“我们已经与 [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) 进行了交谈，他们分享了确保项目长期健康的指导意见。”

然而，他继续说道，“虽然我们信任新的维护者，但只有当我们确信我们通过这个贡献者阶梯拥有一个健康的贡献生命周期时，我们才能恢复发布软件。这意味着我们需要花时间进行练习、测试和调整，然后才能有足够的信心发布它。”

## 社区的反应和恢复之路

这意味着必须连续举行六次社区会议，至少有五名成员/审核员/维护者出席。我们有持续的贡献者加入我们的阶梯，永久的审核员当选，永久的维护者当选。

这不会在一夜之间发生。de Carvalho 预计这个过程可能“至少需要 6 个月。请据此计划。”

ESO 已经到了一个关键时刻。它的未来取决于其用户群和更广泛的 Kubernetes 社区是否愿意通过解决这场危机来维持生态系统中最关键的密钥管理工具之一的活力。

## 对更广泛的开源生态系统的警告

看来他们将度过这场风暴。然而，ESO 远非唯一[面临缺乏支持的项目](https://thenewstack.io/12-critical-open-source-projects-losing-security-support-in-2025/)。[维护者倦怠正成为一个越来越普遍的问题](https://www.linkedin.com/pulse/when-open-source-breaks-silent-impact-maintainer-burnout-vaughan-xelle/)。必须解决这个问题，否则在不久的将来（而且不会太久），我们将看到一个至关重要但鲜为人知的开源项目从支持的裂缝中掉落。企业将发现自己面临零日安全问题，没有任何警告或如何解决这些问题的线索。