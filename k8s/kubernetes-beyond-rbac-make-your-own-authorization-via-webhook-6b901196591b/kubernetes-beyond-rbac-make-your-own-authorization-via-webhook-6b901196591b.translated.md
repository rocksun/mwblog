# Kubernetes RBAC 之外 - 通过 Webhook 自定义授权

[https://kubernetes.io](https://kubernetes.io)

Kubernetes 是一款出色的容器编排工具，提供了大量的自定义选项。您可以轻松扩展/替换许多组件，例如 CNI、CSI、调度器，甚至授权组件。

在本文中，您将了解如何编写自己的授权 Webhook，该 Webhook 可在 Kubernetes 上运行以扩展 RBAC 功能或完全移除 RBAC。

我们将探讨以下主题：

- Kubernetes 授权流程
- 为授权 Webhook 配置 Kubernetes API 服务器
- 授权请求的结构
- 编写授权 Webhook
- 生成自签名证书
- Kubectl 身份验证怎么办
- 展示时间 - 全部运行
- 使用场景
- 参考文献

## Kubernetes 授权流程

首先，让我们解释一下 Kubernetes 的内部授权流程。

[https://kubernetes.io/docs/concepts/security/controlling-access/](https://kubernetes.io/docs/concepts/security/controlling-access/)

到达 API 服务器的请求将经过上图所示的流程。

每个发送到 Kubernetes 集群的请求都由 API 服务器进行身份验证，然后启动多个授权流程。在该授权流程之后，API 服务器调用准入控制 Webhook。最后，如果一切顺利，将通过查询或修改 etcd 的状态来完成请求。

由于 Kubernetes 具有可扩展的架构，我们可以扩展上述每个步骤。我们可以集成自定义身份验证解决方案。我们可以编写自己的授权服务器。或者，我们可以干预每个资源的创建或修改。

如果您想了解如何在 Kubernetes 中使用 RBAC 进行授权，请参阅我之前关于配置 RBAC 的文章 👇

## 为授权 Webhook 配置 Kubernetes API 服务器

您需要配置 API 服务器以指定授权 Webhook 地址。

就个人而言，我使用 Kind 在本地测试 Kubernetes。以下配置为 Kubernetes 的 API 服务器启用了 Webhook 授权。让我们将此配置放在名为“kind-cp.yaml”的文件中。

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  extraMounts:
  - hostPath: /Users/emre.savci/Desktop/kube-authz
    containerPath: /files
kubeadmConfigPatches:
- |
  kind: ClusterConfiguration
  apiServer:
    extraArgs:
      enable-admission-plugins: NodeRestriction,MutatingAdmissionWebhook,ValidatingAdmissionWebhook
      authorization-mode: Webhook,RBAC
      authorization-webhook-version: v1
      authorization-webhook-config-file: /files/authz-webhook.yaml
      authorization-webhook-cache-authorized-ttl: 120s
      authorization-webhook-cache-unauthorized-ttl: 30s
    extraVolumes:
    - name: api-server-basic-auth-files
      hostPath: "/files"
      mountPath: "/files"
      readOnly: true
```

如果仔细查看配置文件，您会发现与授权相关的参数。

以下行指定我们的授权模式同时使用原生 RBAC 和我们自定义编写的授权 Webhook：

```
authorization-mode: Webhook, RBAC
```

以下行指定授权 Webhook 的配置文件：

```
authorization-webhook-config-file: /files/authz-webhook.yaml
```

以下是我们的授权 Webhook 配置文件：

```yaml
clusters:
- name: my-cluster
  cluster:
    certificate-authority: /files/webhook.crt
    server: https://authz-webhook/authorize
users:
- name: api-server
  user:
    token: test-token
current-context: my-cluster
contexts:
- context:
    cluster: my-cluster
    user: api-server
  name: my-cluster
```

现在，我们可以使用这些配置创建集群。

```bash
kind create cluster --retain --config kind-cp.yaml
```

## 授权请求的结构

在编写自定义授权 Webhook 之前，让我们看一下 Kubernetes 发送的授权请求。

您始终可以为传入请求定义自定义类型，但由于 Kubernetes api，我们拥有适用于 Golang 的请求类型。

我们可以通过以下命令安装 Kubernetes api 包：

```bash
go get "k8s.io/api/authorization/v1"
```

之后，我们就拥有了授权请求对象：`SubjectAccessReview`。

```go
// SubjectAccessReview 检查用户或组是否可以执行操作。
type SubjectAccessReview struct {
	metav1.TypeMeta `json:",inline"`
	// 标准列表元数据。
	// 更多信息：https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
	// +optional
	metav1.ObjectMeta `json:"metadata,omitempty" protobuf:"bytes,1,opt,name=metadata"`
	// Spec 包含有关正在评估的请求的信息
	Spec SubjectAccessReviewSpec `json:"spec" protobuf:"bytes,2,opt,name=spec"`
	// Status 由服务器填写，指示是否允许该请求
	// +optional
	Status SubjectAccessReviewStatus `json:"status,omitempty" protobuf:"bytes,3,opt,name=status"`
}
```

在这个结构体中，我们有两个重要的字段：

`SubjectAccessReviewSpec`
它包含请求详细信息，如资源属性和用户组信息。

在这种类型中，有两个重要的字段：**ResourceAttributes** 和 **NonResourceAttributes**。

**ResourceAttributes：** 当请求访问 Kubernetes 资源（如 pod、服务等）时，此字段不为空。
**NonResourceAttributes：** 当您尝试通过 **kubectl auth can-i** 检查权限时，此字段不为空。

```go
// SubjectAccessReviewSpec is a description of the access request. Exactly one of ResourceAuthorizationAttributes
// and NonResourceAuthorizationAttributes must be set
type SubjectAccessReviewSpec struct {
// ResourceAuthorizationAttributes describes information for a resource access request
// +optional
ResourceAttributes *ResourceAttributes `json:"resourceAttributes,omitempty" protobuf:"bytes,1,opt,name=resourceAttributes"`
// NonResourceAttributes describes information for a non-resource access request
// +optional
NonResourceAttributes *NonResourceAttributes `json:"nonResourceAttributes,omitempty" protobuf:"bytes,2,opt,name=nonResourceAttributes"`
// User is the user you're testing for.
// If you specify "User" but not "Groups", then is it interpreted as "What if User were not a member of any groups
// +optional
User string `json:"user,omitempty" protobuf:"bytes,3,opt,name=user"`
// Groups is the groups you're testing for.
// +optional
Groups []string `json:"groups,omitempty" protobuf:"bytes,4,rep,name=groups"`
// Extra corresponds to the user.Info.GetExtra() method from the authenticator. Since that is input to the authorizer
// it needs a reflection here.
// +optional
Extra map[string]ExtraValue `json:"extra,omitempty" protobuf:"bytes,5,rep,name=extra"`
// UID information about the requesting user.
// +optional
UID string `json:"uid,omitempty" protobuf:"bytes,6,opt,name=uid"`
}
```

```go
// ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface
type ResourceAttributes struct {
// Namespace is the namespace of the action being requested. Currently, there is no distinction between no namespace and all namespaces
// "" (empty) is defaulted for LocalSubjectAccessReviews
// "" (empty) is empty for cluster-scoped resources
// "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview
// +optional
Namespace string `json:"namespace,omitempty" protobuf:"bytes,1,opt,name=namespace"`
// Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy. "*" means all.
// +optional
Verb string `json:"verb,omitempty" protobuf:"bytes,2,opt,name=verb"`
// Group is the API Group of the Resource. "*" means all.
// +optional
Group string `json:"group,omitempty" protobuf:"bytes,3,opt,name=group"`
// Version is the API Version of the Resource. "*" means all.
// +optional
Version string `json:"version,omitempty" protobuf:"bytes,4,opt,name=version"`
// Resource is one of the existing resource types. "*" means all.
// +optional
Resource string `json:"resource,omitempty" protobuf:"bytes,5,opt,name=resource"`
// Subresource is one of the existing resource types. "" means none.
// +optional
Subresource string `json:"subresource,omitempty" protobuf:"bytes,6,opt,name=subresource"`
// Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all.
// +optional
Name string `json:"name,omitempty" protobuf:"bytes,7,opt,name=name"`
}
```

`SubjectAccessReviewStatus`：此字段包含针对请求的授权响应，表示是允许还是拒绝。

```go
// SubjectAccessReviewStatus
type SubjectAccessReviewStatus struct {
// Allowed is required. True if the action would be allowed, false otherwise.
Allowed bool `json:"allowed" protobuf:"varint,1,opt,name=allowed"`
// Denied is optional. True if the action would be denied, otherwise
// false. If both allowed is false and denied is false, then the
// authorizer has no opinion on whether to authorize the action. Denied
// may not be true if Allowed is true.
// +optional
Denied bool `json:"denied,omitempty" protobuf:"varint,4,opt,name=denied"`
// Reason is optional. It indicates why a request was allowed or denied.
// +optional
Reason string `json:"reason,omitempty" protobuf:"bytes,2,opt,name=reason"`
// EvaluationError is an indication that some error occurred during the authorization check.
// It is entirely possible to get an error and be able to continue determine authorization status in spite of it.
// For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request.
// +optional
EvaluationError string `json:"evaluationError,omitempty" protobuf:"bytes,3,opt,name=evaluationError"`
}
```

有关更详细的说明，您可以查看 [Kubernetes Subject Access Review](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/subject-access-review-v1/)。

## 编写授权 Webhook
不要被标题吓到，创建授权 webhook 是一件非常简单的事情。实际上，webhook 就是一个简单的 HTTP 服务器。

以下是一个简单的授权 webhook，它允许名为“test-user”的服务帐户执行 **list** 和 **get** 操作，但禁止 **delete** 操作：

```go
package main

import (
	"fmt"

	"github.com/gofiber/fiber/v2"
	authorizationv1 "k8s.io/api/authorization/v1"
)

func main() {
	app := fiber.New()
	app.Post("/authorize", func(ctx *fiber.Ctx) error {
		var req authorizationv1.SubjectAccessReview
		ctx.BodyParser(&req)
		req.Status.Allowed = true
		if req.Spec.User == "system:serviceaccount:default:test-user" {
			if req.Spec.ResourceAttributes != nil {
				if req.Spec.ResourceAttributes.Verb == "get" || req.Spec.ResourceAttributes.Verb == "list" {
					req.Status.Allowed = true
				}
				if req.Spec.ResourceAttributes.Verb == "delete" {
					req.Status.Allowed = false
				}
			}
			if req.Spec.NonResourceAttributes != nil {
				if req.Spec.NonResourceAttributes.Verb == "get" || req.Spec.NonResourceAttributes.Verb == "list" {
					req.Status.Allowed = true
				}
				if req.Spec.NonResourceAttributes.Verb == "delete" {
					req.Status.Allowed = false
				}
			}
		}
		return ctx.JSON(req)
	})
	app.Get("/healthz", func(ctx *fiber.Ctx) error {
		fmt.Println("healthz")
		return ctx.SendStatus(200)
	})
	if err := app.ListenTLS(":443", "/app/webhook.crt", "/app/webhook.key"); err != nil {
		fmt.Println(err)
	}
}
```

以下配置适用于我们的授权 webhook。它指定了我们的 webhook 服务器地址和证书颁发机构。

```yaml
clusters:
- name: devx-webhooks
  cluster:
    certificate-authority: /files/webhook.crt
    server: https://devx-webhooks/authorize
users:
- name: api-server
  user:
    token: test-token
current-context: devx-webhooks
contexts:
- context:
    cluster: devx-webhooks
    user: api-server
  name: devx-webhooks
```

让我们运行我们的 webhook。请记住，我们通过 kind 运行 Kubernetes 集群，我们将在 **kind** 网络中使用 Docker 运行 webhook。

```bash
docker build -t go-kube-authz .
docker run -it -d --name devx-webhooks --network kind -p 443:443 go-kube-authz
```

## Webhook 自签名证书

我们需要创建一个自签名证书，以便 api-server 与我们的 webhook 安全通信。我们将在授权 webhook 服务器中使用生成的 webhook.cert 和 webhook.key。我们还将把 webhook.cert 传递给 webhook 配置文件中的 Kubernetes api 服务器。

```bash
openssl genrsa -out webhook.key 2048
```

让我们创建一个名为 **webook.csr.cnf** 的文件，并将以下配置放入其中：

```
[req]
default_bits = 2048
prompt = no
default_md = sha256
distinguished_name = dn
req_extensions = req_ext
[dn]
CN = devx-webhooks
[req_ext]
subjectAltName = @alt_names
[alt_names]
DNS.1 = devx-webhooks
```

```bash
openssl req -new -key webhook.key -out webhook.csr -config webhook.csr.cnf
```

现在创建另一个文件并放入以下几行

```
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names
[alt_names]
DNS.1 = devx-webhooks
```

```bash
openssl x509 -req -in webhook.csr -signkey webhook.key -out webhook.crt -days 365 -extfile webhook.ext
```

我们的 webhook.key 和 webhook.cert 文件现在可以使用了 🚀

## kubectl 身份验证怎么办

众所周知，有一个名为 `auth` 的 kubectl 命令。
借助此命令，您可以检查 ServiceAccount 或您当前的 `kubeconfig`
设置是否有权访问 Kubernetes 上的特定资源。

auth 命令的基本用法如下：

```bash
kubectl auth can-i get pods/logs
```

简而言之，它可以回答授权问题。auth 命令还有另一个功能，即列出您对特定资源的授权操作。

例如，以下命令列出您对 Kubernetes 资源的所有权限：

```bash
kubectl auth can-i --list
```

## 展示时间 - 全部一起运行

现在是时候在 Kubernetes 集群中运行我们的 webhook 了。我们已经使用 [Kind](https://github.com/kubernetes-sigs/kind/) 创建了一个本地集群。

现在让我们通过创建部署来尝试我们的授权规则。请记住，我们允许用户创建部署，但不允许删除它们。

让我们创建一个部署：

```bash
>kubectl create deployment nginx --image=nginx -n default
deployment.apps/nginx created
```

让我们获取 pods：

```bash
>kubectl get pods
NAME READY STATUS RESTARTS AGE
nginx-77b4fdf86c-zjwhr 1/1 Running 0 52m
```

到目前为止，我们的授权 webhook 运行良好。

现在使用受限服务帐户对其进行测试。为此，我们需要创建一个名为 **test-user** 的服务帐户。

```bash
kubectl create sa test-user
```

现在我们可以使用 kubectl auth can-i 命令来检查我们服务帐户的权限。

首先让我们检查 list 和 get 操作：

```bash
>kubectl auth can-i list pods --as=system:serviceaccount:default:test-user
yes
>kubectl auth can-i get pods --as=system:serviceaccount:default:test-user
yes
```

然后检查 delete 操作：
```
`>kubectl auth can-i delete pods --as=system:serviceaccount:default:test-user`

否

正如我们所见，使用我们的服务帐户，我们可以列出和获取 Pod，但根据我们授权 Webhook 的限制，无法删除 Pod。

您可以查看我的[演示存储库](link-to-your-repository)。

## 使用场景

很明显，只要您想超越原生解决方案，就可以使用它。但我认为我可以提到几个用例。

假设您的组织中有数百或数千名开发人员/DevOps/SRE。并且您希望动态更改 Kubernetes 集群用户的权限。通过原生 RBAC 来完成这项工作可能会非常麻烦。

👉 您可能需要为用户授予特定**时间段**的权限
👉 您可能希望添加**审查和批准流程**以向用户授予权限
👉 您可能希望保持**授权规则在不同 Kubernetes 集群之间同步**
👉 您可能还想从**LDAP 等其他来源**或其他**身份提供者**同步授权规则
👉 您可能希望为您的授权规则使用自定义策略引擎

当然，我们可以创建一个很长的列表，根据特定的用例进行更改。在这篇文章中，作为一个例子，我们限制了特定用户/服务帐户的权限。

## 参考资料

* **Webhook 模式**  
   WebHook 是一个 HTTP 回调：当某些事情发生时发生的 HTTP POST；一个通过 HTTP 的简单事件通知…  
   [kubernetes.io](https://kubernetes.io)

* **控制对 Kubernetes API 的访问**  
   本页概述了如何控制对 Kubernetes API 的访问。用户使用…访问 Kubernetes API  
   [kubernetes.io](https://kubernetes.io)

我希望本文能让您大致了解 Kubernetes 中授权的工作原理，以及我们如何超越它。

下篇文章再见。在那之前，祝您代码无 Bug 🙏
```