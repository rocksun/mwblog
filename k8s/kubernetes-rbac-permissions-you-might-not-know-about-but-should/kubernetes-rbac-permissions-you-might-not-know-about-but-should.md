
<!--
title: 你需要了解的Kubernetes RBAC权限
cover: https://cdn.thenewstack.io/media/2024/05/b1762463-kubernetes-rbac-permissions-featured-image.jpg
-->

K8s RBAC 提供了三个具有隐藏权限的权限，这些权限可能会被恶意使用。了解如何控制其使用。

> 译自 [Kubernetes RBAC Permissions You Might Not Know About, but Should](https://thenewstack.io/kubernetes-rbac-permissions-you-might-not-know-about-but-should/)，作者 Dmitrii Bubnov。

基于角色的访问控制 ([RBAC](https://thenewstack.io/3-frameworks-for-role-based-access-control/) ) 是 [Kubernetes (K8s)](https://thenewstack.io/kubernetes/) 中的默认访问控制方法。此模型使用特定动词对权限进行分类，以定义与资源的允许交互。在此系统中，三个鲜为人知的权限 —— escalate, bind 和 impersonate ——可以覆盖现有的角色限制，授予对受限区域的未经授权的访问权限，公开机密数据，甚至允许完全控制集群。本文解释了这些强大的权限，提供了对其功能的见解以及减轻其相关风险的指导。

## 关于 RBAC 角色和动词

如果你还不熟悉[Kubernetes](https://roadmap.sh/kubernetes) RBAC 的[关键概念](https://roadmap.sh/kubernetes) ，请参阅 [Kubernetes 文档](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) 。

但是，我确实需要简要描述一个与本文直接相关的重要的概念：角色。这描述了特定命名空间内对 K8s 资源的访问权限和可用操作。角色由规则列表组成。规则包括动词——已定义资源的可用操作。

以下是从 K8s 文档中获取的一个角色的示例，该角色授予对 Pod 的读取访问权限：

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: view-pod
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "watch", "list"]
```

诸如 `get`、`watch` 和 `list` 的动词通常使用。但是，也存在更有趣的动词。

## 三个鲜为人知的 Kubernetes RBAC 权限

对于更精细和复杂的权限管理，K8s RBAC 具有以下动词：

- `escalate`: 允许用户创建和编辑角色，即使他们最初没有这样做权限。
- `bind`: 允许用户创建和编辑角色绑定和集群角色绑定，而无需分配权限。
- `impersonate`: 允许用户模拟其他用户并在集群或不同组中获得其权限。可以使用此动词访问关键数据。

下面，你将更详细地了解这些动词。但首先，创建一个测试命名空间并将其命名为
`rbac`：

```
kubectl create ns rbac
```

然后，在刚创建的 `rbac` 命名空间中创建一个名为 `privsec` 的测试服务帐户 (SA) 资源：

```
kubectl -n rbac create sa privesc
```

你将在本教程的其余部分中使用它们。

### Escalate

默认情况下，Kubernetes RBAC API 不允许用户通过简单地编辑角色或角色绑定来提升权限。即使禁用了 RBAC 授权器，此限制也在 API 级别起作用。唯一的例外是如果角色具有
`Escalate` 动词。

在下图中，仅具有 `update` 和 `patch` 权限的 SA 无法向角色添加新动词。但是，如果你添加一个具有 `Escalate` 动词的新角色，则可以实现。

![向角色添加升级动词如何允许用户更改角色权限并添加新动词](https://cdn.thenewstack.io/media/2024/05/4c6c8e84-kubernetes-rbac-permissions-2-1024x356.png)

*向角色添加 `Escalate` 动词允许用户更改角色权限并添加新动词。*

创建一个角色，允许在该命名空间中只读访问 Pod 和角色：

```
kubectl -n rbac create role view --verb=list,watch,get --resource=role,pod
```

将此角色绑定到 SA `privsec`：

```
kubectl -n rbac create rolebinding view --role=view --serviceaccount=rbac:privesc
```

检查是否可以更新角色：

```
kubectl auth can-i update role -n rbac --as=system:serviceaccount:rbac:privesc
```

SA 可以读取角色，但不能编辑角色。

创建一个新角色，允许在 `rbac` 命名空间中编辑角色：

```
kubectl -n rbac create role edit --verb=update,patch --resource=role
```

将此新角色绑定到 SA `privsec`：

```
kubectl -n rbac create rolebinding edit --role=edit --serviceaccount=rbac:privesc
```

检查是否可以更新角色：

```
kubectl auth can-i update role -n rbac --as=system:serviceaccount:rbac:privesc
```

检查是否可以删除角色：

```
kubectl auth can-i delete role -n rbac --as=system:serviceaccount:rbac:privesc
```

SA 现在可以编辑角色，但不能删除角色。

为了实验的准确性，请使用 JSON Web 令牌 (JWT) 检查 SA 功能：

```
TOKEN=$(kubectl -n rbac create token privesc --duration=8h)
```

从配置中删除旧的身份验证参数，因为
[Kubernetes 将首先检查用户的证书](https://stackoverflow.com/questions/60083889/kubectl-token-token-doesnt-run-with-the-permissions-of-the-token) ，如果它已经知道证书，则不会检查令牌。

```bash
cp ~/.kube/config ~/.kube/rbac.conf
export KUBECONFIG=~/.kube/rbac.conf
kubectl config delete-user kubernetes-admin
kubectl config set-credentials privesc --token=$TOKEN
kubectl config set-context --current --user=privesc
```

此角色显示你可以编辑其他角色：

```
kubectl -n rbac get role edit -oyaml

apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: edit
  namespace: rbac
rules:
- apiGroups:
  - rbac.authorization.k8s.io
  resources:
  - roles
  verbs:
  - update
  - patch
```

尝试添加一个新动词，`list`，你已经在只读视图角色中使用过它：

```
kubectl -n rbac edit role edit 

OK

apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: edit
  namespace: rbac
rules:
- apiGroups:
  - rbac.authorization.k8s.io
  resources:
  - roles
  verbs:
  - update
  - patch
  - list   # the new verb we added
```

成功。

现在，尝试添加一个新动词，delete ，您在其他角色中未使用的：

```bash
kubectl -n rbac edit  role edit

apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: edit
  namespace: rbac
rules:
- apiGroups:
  - rbac.authorization.k8s.io
  resources:
  - roles
  verbs:
  - update
  - patch
  - delete   # trying to add a new verb
```

这确认了 Kubernetes 不允许用户或服务帐户添加新权限，如果他们没有这些权限，则只能在用户或服务帐户绑定到具有此类权限的角色时。

因此，扩展 privesc SA 权限。通过使用管理员配置并添加一个具有 escalate 动词的新角色来执行此操作：

```
KUBECONFIG=~/.kube/config kubectl -n rbac create role escalate --verb=escalate --resource=role
```

现在，将 privesc SA 绑定到新角色：

```
KUBECONFIG=~/.kube/config kubectl -n rbac create rolebinding escalate --role=escalate --serviceaccount=rbac:privesc
```

检查您现在是否可以向角色添加新动词：

```bash
kubectl -n rbac edit  role edit

apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: edit
  namespace: rbac
rules:
- apiGroups:
  - rbac.authorization.k8s.io
  resources:
  - roles
  verbs:
  - update
  - patch
  - delete   # the new verb we added

role.rbac.authorization.k8s.io/edit edited
```

现在可以了。用户可以通过编辑现有角色来提升 SA 权限。这意味着 escalate 动词授予适当的管理员权限，包括命名空间管理员甚至集群管理员的权限。

### Bind

bind 动词允许用户编辑 RoleBinding 或 ClusterRoleBinding 对象以进行权限提升，类似于 escalate，它允许用户编辑 Role 或 ClusterRole。

在下图中，具有具有 update、patch 和 create 动词的角色绑定的 SA 无法添加 delete，直到您使用 bind 动词创建新角色。

![向角色添加 bind 动词如何允许用户更改角色权限并添加新动词](https://cdn.thenewstack.io/media/2024/05/261d0c3a-kubernetes-rbac-permissions-3-1024x356.png)

*使用 bind 动词添加新角色允许用户扩展角色的绑定权限。*

仔细了解其工作原理。

将 kubeconfig 文件更改为管理员：

```
export KUBECONFIG=~/.kube/config
```

删除旧角色和绑定：

```
kubectl -n rbac delete rolebinding view edit escalate
kubectl -n rbac delete role view edit escalate
```

允许 SA 查看和编辑命名空间中的角色绑定和 pod 资源：

```bash
kubectl -n rbac create role view --verb=list,watch,get --resource=role,rolebinding,pod
 
kubectl -n rbac create rolebinding view --role=view --serviceaccount=rbac:privesc
 
kubectl -n rbac create role edit --verb=update,patch,create --resource=rolebinding,pod
 
kubectl -n rbac create rolebinding edit --role=edit --serviceaccount=rbac:privesc
```

创建单独的角色来处理 pod，但仍不绑定角色：

```
kubectl -n rbac create role pod-view-edit --verb=get,list,watch,update,patch --resource=pod
 
kubectl -n rbac create role delete-pod --verb=delete --resource=pod
```

将 kubeconfig 更改为 SA privesc 并尝试编辑角色绑定：

```bash
export KUBECONFIG=~/.kube/rbac.conf
 
kubectl -n rbac create rolebinding pod-view-edit --role=pod-view-edit --serviceaccount=rbac:privesc
 
rolebinding.rbac.authorization.k8s.io/pod-view-edit created
```

新角色已成功绑定到 SA。请注意，pod-view-edit 角色包含动词和资源，这些动词和资源已通过绑定 view 和 edit 的角色绑定到 SA。

现在，尝试绑定具有新动词的角色，delete，该动词在绑定到 SA 的角色中缺失：

```
kubectl -n rbac create rolebinding delete-pod --role=delete-pod --serviceaccount=rbac:privesc
 
error: failed to create rolebinding: rolebindings.rbac.authorization.k8s.io "delete-pod" is forbidden: user "system:serviceaccount:rbac:privesc" (groups=["system:serviceaccounts" "system:serviceaccounts:rbac" "system:authenticated"]) is attempting to grant RBAC permissions not currently held:
{APIGroups:[""], Resources:["pods"], Verbs:["delete"]}
```

即使您有权编辑和创建角色绑定，Kubernetes 也不允许这样做。但您可以使用
bind 动词修复此问题。使用管理员配置执行此操作：

```
KUBECONFIG=~/.kube/config kubectl -n rbac create role bind --verb=bind --resource=role
 
role.rbac.authorization.k8s.io/bind created
 
KUBECONFIG=~/.kube/config kubectl -n rbac create rolebinding bind --role=bind --serviceaccount=rbac:privesc
 
rolebinding.rbac.authorization.k8s.io/bind created
```

再次尝试使用新 delete 动词创建角色绑定：

```
kubectl -n rbac create rolebinding delete-pod --role=delete-pod --serviceaccount=rbac:privesc
 
rolebinding.rbac.authorization.k8s.io/delete-pod created
```

现在可以了。因此，使用 bind 动词，SA 可以将任何角色绑定到自身或任何用户。

### Impersonate

K8s 中的 impersonate 动词类似于 Linux 中的 sudo。如果用户拥有 impersonate 访问权限，他们可以以其他用户身份进行身份验证并代表他们运行命令。kubectl 工具具有 --as、--as-group 和 --as-uid 选项，分别允许以不同的用户、组或通用唯一标识符 (UUID) 运行命令。如果用户被授予模拟权限，他们将成为命名空间管理员，或者——如果命名空间中存在 cluster-admin 服务帐户——甚至成为集群管理员。

impersonate 动词有助于检查委派给用户的 RBAC 权限。管理员应根据模板执行命令  `kubectl auth can-i --as=$USERNAME -n $NAMESPACE $VERB $RESOURCE` 并检查授权是否按设计工作。

在此示例中，SA 不会通过仅执行 `kubectl -n rbac get pod` 来获取 rbac 命名空间中 Pod 的信息。但如果存在具有 impersonate 动词的角色，则可以实现：

```
kubectl auth can-i get pod -n rbac --as=system:serviceaccount:rbac:privesc
 
yes
```

```
KUBECONFIG=~/.kube/config kubectl -n rbac create sa impersonator
 
serviceaccount/impersonator created
```

现在，创建一个具有 impersonate 动词和角色绑定的角色：

```
KUBECONFIG=~/.kube/config kubectl -n rbac create role impersonate --resource=serviceaccounts --verb=impersonate --resource-name=privesc
```

（看看上面的指令中的 --resource-name 参数：它只允许模拟为 privesc SA。）

```bash
role.rbac.authorization.k8s.io/impersonate created
 
KUBECONFIG=~/.kube/config kubectl -n rbac create rolebinding impersonator --role=impersonate --serviceaccount=rbac:impersonator
 
rolebinding.rbac.authorization.k8s.io/impersonator created
```

![具有 impersonate 动词的角色帮助用户获取有关 Pod 的信息](https://cdn.thenewstack.io/media/2024/05/045d18b5-kubernetes-rbac-permissions-4-1024x335.png)

*获取具有 impersonate 动词的角色的 Pod 信息。*

创建一个新上下文：

```bash
TOKEN=$(KUBECONFIG=~/.kube/config kubectl -n rbac create token impersonator --duration=8h)
 
kubectl config set-credentials impersonate --token=$TOKEN   
 
User "impersonate" set.
 
kubectl config set-context impersonate@kubernetes  --user=impersonate --cluster=kubernetes       
 
Context "impersonate@kubernetes" created.
 
kubectl config use-context impersonate@kubernetes                                      
 
Switched to context "impersonate@kubernetes".
```

检查权限：

```bash
kubectl auth can-i --list -n rbac
 
Resources                                       Non-Resource URLs                     Resource Names   Verbs
selfsubjectaccessreviews.authorization.k8s.io   []                                    []               [create]
selfsubjectrulesreviews.authorization.k8s.io    []                                    []               [create]
 
...
 
serviceaccounts                                 []     
```

除了角色中指定的 impersonate 之外，不存在其他附加权限。但如果你将 impersonator SA 作为 privsec SA 进行 impersonate，则会获得 privsec SA 拥有的相同权限：

```bash
kubectl auth can-i --list -n rbac --as=system:serviceaccount:rbac:privesc
 
Resources                                       Non-Resource URLs                     Resource Names   Verbs
roles.rbac.authorization.k8s.io                 []                                    [edit]           [bind escalate]
selfsubjectaccessreviews.authorization.k8s.io   []                                    []               [create]
selfsubjectrulesreviews.authorization.k8s.io    []                                    []               [create]
pods                                            []                                    []               [get list watch update patch delete create]
 
...
 
rolebindings.rbac.authorization.k8s.io          []                                    []               [list watch get update patch create bind escalate]
roles.rbac.authorization.k8s.io                 []                                    []               [list watch get update patch create bind escalate]
configmaps                                      []                                    []               [update patch create delete]
secrets                                         []                                    []               [update patch create delete]
```

因此，impersonate SA 拥有其自身的所有权限以及它所 impersonate 的 SA 的所有权限，包括命名空间管理员拥有的权限。

## 如何减轻潜在威胁

escalate、bind 和 impersonate 动词可用于创建灵活的权限，从而实现对 K8s 基础设施的访问的精细管理。但这些动词也为恶意使用打开了大门，因为在某些情况下，它们使用户能够以管理员权限访问关键的基础设施组件。

三种做法可以帮助你减轻这些动词被滥用或恶意使用的潜在危险：

1. 定期检查 RBAC 清单。
2. 在 Role 和 ClusterRole 清单中使用 resourceNames 字段。
3. 使用外部工具来监视角色。

依次查看每种做法。

### 定期检查 RBAC 清单

为了防止未经授权的访问和 RBAC 配置错误，请定期检查你的集群 RBAC 清单：

```bash
kubectl get clusterrole -A -oyaml | yq '.items[] | select (.rules[].verbs[] | contains("esalate" | "bind" | "impersonate"))  | .metadata.name'
 
kubectl get role -A -oyaml | yq '.items[] | select (.rules[].verbs[] | contains("esalate" | "bind" | "impersonate"))  | .metadata.name'
```

### 使用 resourceNames 字段

为了限制使用 escalate、bind、impersonate 或任何其他动词，请在 Role 和 ClusterRole 清单中配置 resourceNames 字段。在那里，你可以（并且应该）输入可以使用的资源的名称。

以下是一个 ClusterRole 的示例，它允许使用名为 edit 和 view 的 roleRef 创建 ClusterRoleBinding：

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: role-grantor
rules:
- apiGroups: ["rbac.authorization.k8s.io"]
  resources: ["clusterroles"]
  verbs: ["bind"]
  resourceNames: ["edit","view"]
```

你可以对 escalate 和 impersonate 执行相同的操作。

请注意，在 bind 的情况下，管理员为角色设置权限，并且用户仅在 resourceNames 中被允许这样做时才能将该角色绑定到自己。使用 escalate，用户可以在角色中编写任何参数，并成为命名空间或集群的管理员。因此，bind 限制了用户，而 escalate 为他们提供了更多选项。如果你需要授予这些权限，请记住这一点。

### 使用外部工具来监视角色

考虑使用自动系统来监控创建或编辑具有可疑内容的角色，例如 [Falco](https://thenewstack.io/falco-is-a-cncf-graduate-now-what/) 或 [Tetragon](https://thenewstack.io/tetragon-1-0-promises-a-new-era-of-kubernetes-security-and-observability/)。

您还可以将 Kubernetes 审计日志重定向到日志管理系统，例如 [Gcore 托管日志记录](https://gcore.com/cloud/managed-logging)，这对于分析和解析 K8s 日志非常有用。为防止意外删除资源，请创建一个具有 `delete` 动词的单独服务帐户，并允许用户仅模拟该服务帐户。这是最小权限原则。为简化此过程，您可以使用 kubectl 插件 [kubectl-sudo](https://github.com/postfinance/kubectl-sudo)。

在 Gcore，我们使用这些方法来使我们的 [托管 Kubernetes 服务](https://gcore.com/cloud/managed-kubernetes) 更加安全；我们建议所有客户也这样做。使用托管服务并不能保证您的服务在默认情况下完全安全，但在 Gcore，我们尽一切可能确保客户的保护，包括鼓励 RBAC 最佳实践。

## 结论

`escalate`、`bind` 和 `impersonate` 动词允许管理员灵活地管理对 K8s 基础设施的访问，并允许用户提升其权限。这些是功能强大的工具，如果滥用，可能会对 K8s 集群造成重大损害。仔细查看这些动词的任何用法，并确保遵循最小权限规则。用户必须拥有操作所需的最低权限，不得更多。
