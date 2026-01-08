
<!--
title: Kubernetes v1.35：CSI 驱动服务账号令牌传递的全新方案
cover: 
summary: Kubernetes v1.35改进了CSI驱动服务账户令牌传递，通过CSIDriver的serviceAccountTokenInSecrets字段，将令牌从不安全的volume_context移至secrets字段。这避免了意外日志记录，增强了安全性。驱动需选择加入并遵循升级指南。
-->

Kubernetes v1.35改进了CSI驱动服务账户令牌传递，通过CSIDriver的serviceAccountTokenInSecrets字段，将令牌从不安全的volume_context移至secrets字段。这避免了意外日志记录，增强了安全性。驱动需选择加入并遵循升级指南。

> 译自：[Kubernetes v1.35: A Better Way to Pass Service Account Tokens to CSI Drivers](https://kubernetes.io/blog/2026/01/07/kubernetes-v1-35-csi-sa-tokens-secrets-field-beta/)
> 
> 作者：[no-author]

# Kubernetes v1.35: 一种更好的方式将服务账户令牌传递给 CSI 驱动

作者：

**Anish Ramasekar (微软)**

|

2026年1月7日，星期三

如果您维护一个使用服务账户令牌的 CSI 驱动，那么 Kubernetes v1.35 带来了一个您会想了解的改进。自 [TokenRequests 功能](https://kubernetes-csi.github.io/docs/token-requests.html)推出以来，CSI 驱动请求的服务账户令牌一直通过 `volume_context` 字段传递给它们。尽管这种方式可行，但它并非敏感信息的理想位置，我们曾发现令牌在 CSI 驱动中被意外记录的案例。

Kubernetes v1.35 引入了一个 Beta 解决方案来解决此问题：*CSI 驱动通过 Secrets 字段选择接收服务账户令牌*。这允许 CSI 驱动通过 `NodePublishVolumeRequest` 中的 `secrets` 字段接收服务账户令牌，该字段是 CSI 规范中存储敏感数据的合适位置。

## 理解现有方法

当 CSI 驱动使用 [TokenRequests 功能](https://kubernetes-csi.github.io/docs/token-requests.html)时，它们可以通过在 CSIDriver 规范中配置 `TokenRequests` 字段来请求工作负载身份的服务账户令牌。这些令牌作为卷属性映射的一部分传递给驱动，使用的键是 `csi.storage.k8s.io/serviceAccount.tokens`。

`volume_context` 字段虽然可用，但它并非为敏感数据设计。因此，存在一些挑战：

首先，CSI 驱动使用的 [`protosanitizer`](https://github.com/kubernetes-csi/csi-lib-utils/tree/master/protosanitizer) 工具不将卷上下文视为敏感信息，因此当 gRPC 请求被记录时，服务账户令牌可能会出现在日志中。这在 Secrets Store CSI Driver 的 [CVE-2023-2878](https://github.com/kubernetes-sigs/secrets-store-csi-driver/security/advisories/GHSA-g82w-58jf-gcxx) 和 Azure File CSI Driver 的 [CVE-2024-3744](https://kubernetes/kubernetes/issues/124759) 中都发生过。

其次，每个希望避免此问题的 CSI 驱动都需要实现自己的清理逻辑，这导致驱动之间不一致。

CSI 规范在 `NodePublishVolumeRequest` 中已经有一个 `secrets` 字段，正是为此类敏感信息设计的。挑战在于，我们不能简单地改变放置令牌的位置，而不破坏那些期望令牌在卷上下文中的现有 CSI 驱动。

## 了解选择加入机制的工作原理

Kubernetes v1.35 引入了一种选择加入机制，允许 CSI 驱动选择如何接收服务账户令牌。这样，现有驱动可以继续按现有方式工作，而驱动可以在准备好时迁移到更合适的 secrets 字段。

CSI 驱动可以在其 CSIDriver 规范中设置一个新字段：

```
#
# CAUTION: this is an example configuration.
#          Do not use this for your own cluster!
#
apiVersion: storage.k8s.io/v1
kind: CSIDriver
metadata:
  name: example-csi-driver
spec:
  # ... existing fields ...
  tokenRequests:
  - audience: "example.com"
    expirationSeconds: 3600
  # New field for opting into secrets delivery
  serviceAccountTokenInSecrets: true  # defaults to false

```

行为取决于 `serviceAccountTokenInSecrets` 字段：

当设置为 `false`（默认值）时，令牌会像今天一样，以键 `csi.storage.k8s.io/serviceAccount.tokens` 放置在 `VolumeContext` 中。
当设置为 `true` 时，令牌只会以相同的键放置在 `Secrets` 字段中。

## 关于 Beta 版本

`CSIServiceAccountTokenSecrets` 功能门控在 kubelet 和 kube-apiserver 上默认启用。由于 `serviceAccountTokenInSecrets` 字段默认为 `false`，启用功能门控不会改变任何现有行为。所有驱动将继续通过卷上下文接收令牌，除非它们明确选择加入。这就是为什么我们觉得可以从 Beta 而非 Alpha 版本开始的原因。

## CSI 驱动作者指南

如果您维护一个使用服务账户令牌的 CSI 驱动，以下是采用此功能的方法。

### 添加回退逻辑

首先，更新您的驱动代码以检查令牌的两个位置。这将使您的驱动与旧方法和新方法兼容：

```
const serviceAccountTokenKey = "csi.storage.k8s.io/serviceAccount.tokens"

func getServiceAccountTokens(req *csi.NodePublishVolumeRequest) (string, error) {
    // Check secrets field first (new behavior when driver opts in)
    if tokens, ok := req.Secrets[serviceAccountTokenKey]; ok {
        return tokens, nil
    }
    
    // Fall back to volume context (existing behavior)
    if tokens, ok := req.VolumeContext[serviceAccountTokenKey]; ok {
        return tokens, nil
    }
    
    return "", fmt.Errorf("service account tokens not found")
}

```

此回退逻辑是向后兼容的，并且可以在任何驱动版本中发布，甚至在集群升级到 v1.35 之前。

### 推出顺序

CSI 驱动作者在采用此功能时需要遵循特定的顺序，以避免破坏现有卷。

**驱动准备**（随时可以进行）

您可以立即开始准备您的驱动，方法是添加回退逻辑，检查 secrets 字段和卷上下文中的令牌。此代码更改是向后兼容的，并且可以在任何驱动版本中发布，即使在集群升级到 v1.35 之前。我们鼓励您尽早添加此回退逻辑，发布版本，并在可行的情况下向后移植到维护分支。

**集群升级和功能启用**

一旦您的驱动部署了回退逻辑，以下是在集群中启用该功能的安全推出顺序：

1. 完成 kube-apiserver 升级到 1.35 或更高版本
2. 完成所有节点上的 kubelet 升级到 1.35 或更高版本
3. 确保部署了具有回退逻辑的 CSI 驱动版本（如果在准备阶段尚未完成）
4. 完全完成 CSI 驱动 DaemonSet 在所有节点上的推出
5. 更新您的 CSIDriver 清单，将 `serviceAccountTokenInSecrets` 设置为 `true`

### 重要限制

最重要的是要记住时机。如果您的 CSI 驱动 DaemonSet 和 CSIDriver 对象在同一个清单或 Helm chart 中，则需要两次单独的更新。首先部署带有回退逻辑的新驱动版本，等待 DaemonSet 推出完成，然后更新 CSIDriver 规范以将 `serviceAccountTokenInSecrets` 设置为 `true`。

此外，在所有驱动 Pod 推出之前，不要更新 CSIDriver。如果这样做，那些仍在运行旧驱动版本的节点上的卷挂载将失败，因为这些 Pod 只检查卷上下文。

## 为什么这很重要

采用此功能有以下几个好处：

* 它消除了在 gRPC 请求中意外将服务账户令牌作为卷上下文一部分记录的风险
* 它使用了 CSI 规范中指定的敏感数据字段，这很合适
* `protosanitizer` 工具会自动正确处理 secrets 字段，因此您无需进行特定于驱动的变通处理
* 它是选择加入的，因此您可以按照自己的节奏迁移，而不会破坏现有部署

## 行动呼吁

我们（Kubernetes SIG Storage）鼓励 CSI 驱动作者采用此功能并提供关于迁移经验的反馈。如果您对 API 设计有任何想法，或者在采用过程中遇到任何问题，请通过 Kubernetes Slack 上的 [#csi](https://kubernetes.slack.com/archives/C8EJ01Z46) 频道联系我们（邀请链接：<https://slack.k8s.io/>）。

您可以关注 [KEP-5538](https://kep.k8s.io/5538) 以跟踪未来 Kubernetes 版本中的进展。