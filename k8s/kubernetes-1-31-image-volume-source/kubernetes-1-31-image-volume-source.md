
<!--
title: Kubernetes 1.31：基于OCI工件的只读卷（alpha）
cover: ./cover.png
-->

Kubernetes 社区正在努力在未来满足更多人工智能 (AI) 和机器学习 (ML) 的用例。虽然该项目过去一直被设计用来满足微服务架构，但现在是时候倾听最终用户的意见，并引入更侧重于 AI/ML 的功能。这些需求之一是直接支持 Open Container Initiative (OCI) 兼容的镜像和工件（称为 OCI 对象）作为原生卷源。

> 译自 [Kubernetes 1.31: Read Only Volumes Based On OCI Artifacts (alpha)](https://kubernetes.io/blog/2024/08/16/kubernetes-1-31-image-volume-source/)，作者 Sascha Grunert。

Kubernetes 社区正在朝着满足未来更多的 AI 和 ML 的用例而迈进。此前该项目被设计为服务于微服务架构，而现在是听取最终用户意见并引进更多专注于 AI/ML 的功能的时候了。

其中一项需求便是支持将 Open Container Initiative (OCI) 兼容的镜像和构件（称为 OCI 对象）直接作为一个原生卷来源。这便能让用户专注于 OCI 标准，且能使用 OCI 存储库储存和分发任何内容。像这样的功能能让 Kubernetes 项目扩展到超出运行特定镜像的用例。

就此，Kubernetes 社区很自豪地推出 v1.31 中引入的新阿尔法功能：Image Volume Source (KEP-4639)。这项功能使用户能够指定一个镜像引用作为 pod 中的卷，同时在容器中将它重新用作卷装载：

```yaml
…
kind: Pod
spec:
  containers:
    - …
      volumeMounts:
        - name: my-volume
          mountPath: /path/to/directory
  volumes:
    - name: my-volume
      image:
        reference: my-image:tag
```

上述示例将导致将 my-image:tag 挂载到容器中的 /path/to/directory 中。

## 用例

这项改进的目标是尽可能贴合 kubelet 中现有的容器镜像实现，同时引入一个新的 API 表面，以允许更多扩展用例。

例如，用户可以在一个 Pod 中的多个容器间共享一个配置文件，而无需将该文件包含在主镜像中，这样他们就可以最大程度减小安全风险和整体镜像大小。他们还可以使用 OCI 镜像打包和分发二进制制品，并直接将其挂载到 Kubernetes Pod 中，例如这样可以精简其 CI/CD 流水线。

数据科学家、MLOps 工程师或 AI 开发人员可以将大型语言模型权重或机器学习模型权重与模型服务器一同安装在一个 pod 中，以便在不将它们包含在模型服务器容器镜像中时高效地提供服务。他们可以将这些打包到 OCI 对象中，以利用 OCI 的分布和确保高效地部署模型。这让他们能够将模型规范/内容与处理它们的执行文件分开。

另一个用例是安全工程师可以使用恶意软件扫描仪的公共镜像，并挂载包含私有（商业）恶意软件签名的卷，这样他们就可以加载这些签名，而不用将自己组合的镜像（公共镜像的版权可能不允许这样做）烘焙出来。这些文件适用于任何操作系统或扫描软件版本。

但从长远角度来看，将由您作为此项目的最终用户来概述新功能的其他重要用例。SIG 节点乐于收集任何反馈或针对允许更多高级使用场景的进一步增强提出的建议。欢迎通过 Kubernetes Slack (#sig-node) 频道或 SIG 节点邮件列表提供反馈。

## 详细示例

Kubernetes alpha 功能闸门 ImageVolume 需要在 API 服务器以及 kubelet 上启用才能发挥作用。如果情况如此并且容器运行时支持该功能（如 CRI-O ≥ v1.31），则可以创建如下所示的样例 pod.yaml：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod
spec:
  containers:
    - name: test
      image: registry.k8s.io/e2e-test-images/echoserver:2.3
      volumeMounts:
        - name: volume
          mountPath: /volume
  volumes:
    - name: volume
      image:
        reference: quay.io/crio/artifact:v1
        pullPolicy: IfNotPresent
```

Pod 声明了一个新卷，使用 quay.io/crio/artifact:v1 的 image.reference，它引用了一个包含两个文件 OCI 对象。pullPolicy 的行为与容器镜像相同，它允许使用以下值：

- **Always**：kubelet 始终尝试提取引用并且提取失败时容器创建将失败。
- **Never**：kubelet 永不提取引用并且仅使用本地镜像或制品。引用不存在时容器创建会失败。
- **IfNotPresent**：kubelet 将在磁盘上不存在引用时提取引用。引用不存在且提取失败时容器创建会失败。

`volumeMounts` 该字段表示名为`test`的容器应将卷挂载到`/volume`路径下。

如果您现在创建 Pod：

```
kubectl apply -f pod.yaml
```
并执行到其中：

```
kubectl exec -it pod -- sh
```
然后您可以调查已挂载的内容：

```
/ # ls /volume
dir file
/ # cat /volume/file
2
/ # ls /volume/dir
file
/ # cat /volume/dir/file
1
```

**您成功使用 Kubernetes 使用了 OCI 构件！**

容器运行时会拉取镜像（或构件），将其挂载到容器中，并最终使其可供直接使用。实现中有很多细节，这些细节与 kubelet 的现有镜像拉取行为密切相关。例如：

- 如果提供`：latest`标签作为`reference`，则`pullPolicy`将默认为`Always`，而在任何其他情况下，如果未设置，则将默认为`IfNotPresent`。
- 如果 Pod 被删除并重新创建，则卷将被重新解析，这意味着新的远程内容将在 Pod 重新创建时可用。在 Pod 启动期间无法解析或拉取镜像会导致容器无法启动，并可能增加大量延迟。将使用正常的卷回退重试失败，并将报告在 Pod 原因和消息中。
- 拉取机密将通过查找节点凭据、服务帐户镜像拉取机密和 Pod 规范镜像拉取机密，以与容器镜像相同的方式进行组装。
- OCI 对象通过以与容器镜像相同的方式合并清单层，被挂载到单个目录中。
- 卷被挂载为只读（`ro`）和不可执行文件（`noexec`）。
- 不支持容器的子路径挂载（`spec.containers[*].volumeMounts.subpath`）。
- 字段 `spec.securityContext.fsGroupChangePolicy` 对这种卷类型没有影响。
- 该功能也将与`AlwaysPullImages`一起使用，如果启用。

感谢您阅读本文的结尾！SIG Node 很自豪也很高兴将此功能作为 Kubernetes v1.31 的一部分提供。
