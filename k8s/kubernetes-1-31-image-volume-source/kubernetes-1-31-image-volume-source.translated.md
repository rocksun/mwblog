# Kubernetes 1.31: Read-Only Volumes Based on OCI Artifacts (alpha)

The Kubernetes community is working hard to meet more Artificial Intelligence (AI) and Machine Learning (ML) use cases in the future. While the project has historically been designed to meet microservice architectures, it's time to listen to end-users and introduce more AI/ML-focused features.

One such requirement is direct support for [Open Container Initiative (OCI)](https://opencontainers.org) compatible images and artifacts (referred to as OCI objects) as native volume sources. This allows users to focus on the OCI standard and enables them to use OCI registries to store and distribute anything. Such functionality gives the Kubernetes project the opportunity to expand beyond the use case of running specific images.

With this in mind, the Kubernetes community is proud to introduce a new alpha feature in v1.31: Image Volume Source ([KEP-4639](https://kep.k8s.io/4639)). This feature allows users to specify an image reference as a volume in a pod, while re-using it as a volume mount in a container:

```
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

The above example will result in `my-image:tag` being mounted to `/path/to/directory` in the pod's container.

## Use Cases

The goal of this enhancement is to be as close as possible to the existing [container image](/docs/concepts/containers/images/) implementation in kubelet, while introducing a new API surface to allow for a wider range of use cases.

For example, users can share configuration files between multiple containers in a pod without including the files in the main image, minimizing security risks and reducing the overall image size. They can also use OCI images to package and distribute binary artifacts and mount them directly into Kubernetes pods, simplifying their CI/CD pipelines.

Data scientists, MLOps engineers, or AI developers can mount large language model weights or machine learning model weights alongside a model server in a pod so that they can serve them efficiently without including them in the model server container image. They can package these into OCI objects to leverage OCI distribution and ensure efficient model deployment. This allows them to separate model specifications/content from the executables that process them.

Another use case is that security engineers can use public images to scan for malware and mount private (commercial) malware signatures into a volume so that they can load these signatures without creating their own combined image (which may not be allowed by the public image copyright). These files are independent of the operating system or version of the scanning software.

But in the long run, it will be up to **you**, as the end-user of this project, to outline further important use cases for the new functionality.
[SIG Node](https://github.com/kubernetes/community/blob/54a67f5/sig-node/README.md)
is happy to receive any feedback or suggestions to further enhance the feature to allow for more advanced use cases. You can provide feedback by using the [Kubernetes Slack (#sig-node)](https://kubernetes.slack.com/messages/sig-node)
channel or the [SIG Node mailing list](https://groups.google.com/g/kubernetes-sig-node).

## Detailed Example

The Kubernetes alpha feature gate [ ImageVolume](/docs/reference/command-line-tools-reference/feature-gates/)
needs to be enabled on both

[API Server](/docs/reference/command-line-tools-reference/kube-apiserver/) and
[kubelet](/docs/reference/command-line-tools-reference/kubelet/) for it to work. If that is the case, and
[container runtime](/docs/setup/production-environment/container-runtimes/) supports the feature (like CRI-O ≥ v1.31), you can create an example
`pod.yaml`
like this:

```
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

This pod declares a new volume using `image.reference` of `quay.io/crio/artifact:v1`, which references an OCI object containing two files.
`pullPolicy`
behaves the same as container images and allows the following values:

`Always`: kubelet always tries to pull the reference, and if the pull fails, container creation will fail. `Never`: kubelet never pulls the reference, only uses local images or artifacts. If the reference does not exist, container creation will fail. `IfNotPresent`: kubelet will pull if the reference does not exist on disk. If the reference does not exist and the pull fails, container creation will fail.
`volumeMounts`
该字段表示名为`test`的容器应将卷挂载到`/volume`路径下。

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
- 字段`spec.securityContext.fsGroupChangePolicy`对这种卷类型没有影响。
- 该功能也将与`AlwaysPullImages`一起使用，如果启用。

感谢您阅读本文的结尾！SIG Node 很自豪也很高兴将此功能作为 Kubernetes v1.31 的一部分提供。

作为本文的作者，我要特别感谢所有参与其中的人！你们都很棒，让我们继续黑客攻击！