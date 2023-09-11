# Kubernetes 中的策略管理正在改变

在前面的[一篇文章](https://yylives.cc/2023/09/10/7-steps-to-highly-effective-kubernetes-policies/)中我们介绍了如何实现 Kubernetes 的策略管理。下面，让我们了解一下 Kubernetes 开发中的内置策略管理工具。译自 [Policy Management in Kubernetes is Changing](https://eminalemdar.medium.com/policy-management-in-kubernetes-is-changing-9d4808f548a0)。

Kubernetes API 服务器是 Kubernetes 控制平面中的核心组件之一。该组件公开了Kubernetes API，并充当控制平面的前端。当用户或进程与 Kubernetes 交互时，API 服务器处理这些请求，并且 API 服务器也验证和配置 Kubernetes API 对象，例如部署或命名空间。当然，这还需要 Kubernetes Admission Controller 的帮助。那么，什么是 Admission Controller 呢？

正如 Kubernetes 官方文档中所解释的，Admission Controller 是一段代码，它会在持久化对象之前拦截发往 Kubernetes API 服务器的请求，但在请求被认证和授权之后。有两种类型的 Admission Controller：修改的（Mutating）和验证的（Validating）。一些控制器可能两者兼具，但一般来说，控制器要么变更请求并修改对象，要么如其名所示，校验请求。

为了更清楚地理解它，让我解释一下它的工作原理。假设您有一个带有一些 Kubernetes 对象定义的 YAML 文件，例如部署或 pod，并且您想将其应用到集群中。当您将该请求发送到 API 服务器时，它首先检查您是否具有创建该对象的必要权限。然后该请求被转发到可变更（Mutating ） Admission Controller。这些 Controller 可以根据集群中的配置更改该对象的定义。之后，如果定义模式有效，请求将被转发到校验（Validating） Admission Controller。 如果一切正确，资源将被创建，对象的详细信息将被发送到 etcd。

![准入控制器的工作方式](https://miro.medium.com/v2/resize:fit:828/format:webp/1*ysfawao2_9xTZYsWr_HztQ.png)

像 [Kyverno](https://kyverno.io/)、[OPA Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/) 和 [Datree](https://www.datree.io/) 这样的第三方策略引擎工具使用修改和校验准入 Webhook 来管理策略。 例如，Kyverno 作为集群内的动态准入控制器运行。它从 Kubernetes API 服务器接收修改和校验 Webhook 请求， 并应用匹配的策略来返回执行准入策略或拒绝请求的结果。 OPA Gatekeeper 也类似。它是一个执行 [Open Policy Agent](https://www.openpolicyagent.org/) 策略的校验和修改 Webhook。 但这些工具都有自己的策略定义格式，当然也存在差异。例如，OPA 使用一种名为 Rego 的语言， 由于这是一种不同的语言，并且存在学习曲线，因此一些人可能难以编写或理解策略。

但是在 Kubernetes 1.26 中，首次发布了 Kubernetes [校验准入策略](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/)的 alpha 版本。 在 Kubernetes 1.28 中，它现在处于 beta 阶段。此功能正在将标准化的声明式策略管理引入 Kubernetes API。这意味着我们可以以 Kubernetes 本机的方式管理和定义策略。 校验准入策略使用[通用表达式语言](https://github.com/google/cel-spec)(CEL)来定义策略规则，并允许我们拥有参数化和作用域策略。 构建、安装和管理第三方 Webhook 可能非常复杂，但此新功能将消除对调用远程 Webhook 的所有需求， 并允许我们在集群内部以内置过程的形式管理 API 中的策略，带有 CEL 表达式。

这是否意味着第三方工具的终结？我个人认为不会，我相信像 OPA Gatekeeper 和 Kyverno 这样的工具会适应这种新方法。但如果他们不适应，我认为这些工具可能会遇到问题，因为大多数 Kubernetes 用户在策略管理已经在 Kubernetes API 中以本地方式可用的情况下，不会选择管理策略的不同工具。这当然只是我个人的看法。

## 让我们看看Kubernetes校验准入策略的实际效果！

在进入演示之前，我应该提醒您，此功能在 Kubernetes API 中默认未启用，您需要启用必要的 `ValidatingAdmissionPolicy` 功能开关。根据您的 Kubernetes 版本，您还需要在 API 中启用 `admissionregistration.k8s.io/v1alpha1` 或 `admissionregistration.k8s.io/v1beta1`。 在此演示中，我将使用 Kubernetes 1.27 版本的集群，并将使用 “v1alpha1” API 版本的 Validating Admission Policy 资源。

对于策略，我们需要两种资源。首先，定义实际规则的策略以及验证操作，其次，将实际策略绑定到例如命名空间的绑定资源。

我将使用一个简单的示例策略，该策略将为定义了标签的命名空间中的 deployment 对象定义副本数量限制的规则。 让我首先创建一个简单的命名空间资源。

```yaml
apiVersion: v1
kind: Namespace  
metadata:
  labels:    
    environment: demo  
  name: demo
```

这里当然没什么特别的，我将使用 kubectl apply 创建此命名空间。 让我们定义我们的策略:

```yaml
apiVersion: admissionregistration.k8s.io/v1alpha1
kind: ValidatingAdmissionPolicy
metadata:
  name: "demo-policy"  
spec:
  matchConstraints:
    resourceRules:
    - apiGroups:   ["apps"]
      apiVersions: ["v1"]
      operations:  ["CREATE"， "UPDATE"]
      resources:   ["deployments"]
  validations:
    - expression: "object.spec.replicas <= 5"
      message: "You can not have more than 5 replicas in the demo namespace for deployments"
```

该策略将检查 deployment 资源，并跟踪创建和更新操作。 这些 deployment 需要定义 5 个或更少的副本。 但我也需要一个策略绑定资源：

```yaml
apiVersion: admissionregistration.k8s.io/v1alpha1
kind: ValidatingAdmissionPolicyBinding  
metadata:
  name: "demo-binding"
spec:
  policyName: "demo-policy"
  validationActions: [Deny]
  matchResources:  
    namespaceSelector:
      matchLabels:
        environment: demo
```

正如您从绑定资源中看到的，此策略将对标签为 “environment = demo” 的命名空间中的 deployment 资源强制执行。 让我们使用 kubectl apply 创建这些资源。

现在是时候测试我们的新策略了。 我将使用一个简单的 deployment 定义:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: demo-app
  labels:
    app: nginx
spec:
  replicas: 6  
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx
        name: nginx
```

我不会为此 deployment 对象定义服务或任何特定内容。 让我们应用此 deployment：

```yaml
kubectl apply -f deployment.yaml -n demo
```

我无法创建 deployment 对象，正如预期的那样。 策略生效，这里是错误消息：

```
The deployments "demo-app" is invalid: : ValidatingAdmissionPolicy  
'demo-policy' with binding 'demo-binding' denied request:
You can not create more than 5 replicas in the demo namespace for deployments
```

对于本演示的目的而言，这当然是成功的。 如果我将 spec.replicas 更改为 5，deployment 将成功创建。

正如我在本博文中展示的示例演示中所见，校验准入策略使您可以在 Kubernetes 中编写、执行和使用策略变得非常简单，而无需第三方工具。 这也非常灵活。 通过使用 CEL 表达式，您可以为多项操作和多项验证规则创建精心定义的自定义策略。 您当然可以添加更多的验证规则来扩展这些策略，或者您可以使用不同的验证操作。 我真的相信这将成为 Kubernetes 中的策略管理事实标准。

此功能现在处于 Kubernetes 1.28 的 beta 阶段，因此您可以通过启用功能开关来自己尝试，但我相信当它默认启用或移动到 stable 时，此功能将非常方便。
