<!--
title: 使用Kyverno和OPA Gatekeeper简化Kubernetes安全性
cover: https://cdn.thenewstack.io/media/2025/06/e0086a79-door.jpeg
summary: 想搞定 Kubernetes 安全？试试 Kyverno 和 OPA Gatekeeper！前者用 YAML 策略，简单易上手；后者用 Rego，灵活但复杂。轻松实现镜像安全、合规性检查，避免 root 权限等风险。一键安装 Helm，快速部署，让你的 K8s 集群更安全！
-->

想搞定 Kubernetes 安全？试试 Kyverno 和 OPA Gatekeeper！前者用 YAML 策略，简单易上手；后者用 Rego，灵活但复杂。轻松实现镜像安全、合规性检查，避免 root 权限等风险。一键安装 Helm，快速部署，让你的 K8s 集群更安全！

> 译自：[Simplify Kubernetes Security With Kyverno and OPA Gatekeeper](https://thenewstack.io/simplify-kubernetes-security-with-kyverno-and-opa-gatekeeper/)
> 
> 作者：Adetokunbo Ige

[Kubernetes](https://thenewstack.io/securing-kubernetes-with-external-secrets-operator-on-aws/) 无疑是管理容器化应用程序的首选工具，但它也带来了一个特殊的挑战：安全性！由于其复杂性，确保您的 [Kubernetes 部署](https://thenewstack.io/kubernetes/) 安全并符合最佳实践可能会让人感到不知所措。

但有个好消息。像 [Kyverno](https://thenewstack.io/using-the-kyverno-cli-to-write-policy-test-cases/) 和 [OPA Gatekeeper](https://thenewstack.io/getting-open-policy-agent-up-and-running/) 这样的工具可以帮助您保护集群。这些策略执行引擎确保您的 Kubernetes 资源在进入集群之前是安全且合规的。听起来像是改变游戏规则，对吧？

以下是这些工具如何简化您的 Kubernetes 安全设置，并帮助您避免常见的陷阱，例如以 root 身份运行容器或使用来自可疑来源的镜像。

## 为什么 Kubernetes 安全性很重要

Kubernetes 是编排的强大工具，但如果没有正确的控制，您就敞开了潜在安全风险的大门。从不受信任的镜像到过度的资源分配，风险会迅速累积。这就是策略引擎的用武之地。它们充当护栏，在安全性和开发人员自主性之间创建平衡。

## 进入 Kyverno 和 OPA Gatekeeper

[Kyverno](https://kyverno.io/) 和 [OPA Gatekeeper](https://github.com/open-policy-agent/gatekeeper) 都旨在锁定您的 Kubernetes 环境，而不会增加不必要的复杂性。可以将它们视为您的 Kubernetes 安全保镖。它们验证您的配置，确保合规性，并在漏洞进入您的系统之前将其阻止。

## 聚焦 Kyverno

Kyverno 专为 Kubernetes 构建，并且易于使用。策略以 [YAML](https://yaml.org) 编写，YAML 是一种人类友好的数据序列化语言，无需额外的编程语言。无论您是强制执行命名空间、应用集群范围的规则，还是在部署前使用 CLI 工具测试策略，Kyverno 都能满足您的需求。额外的好处是？您可以直接获得合规性报告。Kyverno 的一些主要亮点包括：

- 易于编写的 YAML 策略
- 与 Kubernetes 工具的原生集成
- 一个 CLI 工具，用于在推出策略之前预览策略
- 跨命名空间和集群的策略执行

## 内置合规性报告

Kyverno 不仅强制执行安全性，还使组织能够清晰而精确地理解和调整其策略。

## 如何在 Kubernetes 集群中安装 Kyverno

您需要在工作站中安装 Helm。您将使用 [Helm](https://helm.sh/) 来安装 Kyverno。

## 开始使用 Kyverno

为什么要使用 Helm 安装 Kyverno？因为它：

- 更适合生产
- 更容易在集群中安装和升级软件包或软件

**步骤 1：安装 Helm（如果尚未安装）**

**在 macOS 上安装 brew（使用 Homebrew）：**

```bash
brew install helm
```

**在 Linux 上安装 brew：**

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

**在 Windows 上安装 brew（使用 Chocolatey）：**

```bash
choco install kubernetes-helm
```

**步骤 2：添加 Kyverno Helm Repo**

```bash
helm repo add kyverno https://kyverno.github.io/kyverno/
helm repo update
```

![](https://cdn.thenewstack.io/media/2025/06/072db800-image1a.png)

**步骤 3：安装 Kyverno**

```bash
helm install kyverno kyverno/kyverno --namespace kyverno --create-namespace
```

![](https://cdn.thenewstack.io/media/2025/06/dd3643cf-image2a.png)

**步骤 4：验证 Kyverno 安装**

```bash
kubectl get pods -n kyverno
```

## Kyverno 策略示例

**用例 1**：它阻止用户部署使用 `:latest tag` 的容器。

如果该代码段存在问题，则很难跟踪或回滚，因为您不确定它的所有实例是否都具有相同的版本。该镜像也可能具有其他难以追踪或修复的依赖项。

请将以下代码段复制并粘贴到文件名为 `disallow-latest-tag.yaml` 的文件中，并使用此命令在您的集群中执行它。以下策略将阻止用户在您的集群中使用镜像标签 `:latest`。

```bash
kubectl apply -f disallow-latest-tag.yaml
```

![](https://cdn.thenewstack.io/media/2025/06/2e832ed5-image4a.png)

**使用“Latest”标签应用 NGINX**

请将以下代码段复制并粘贴到文件名为 `nginx-latest.yaml` 的文件中，并使用此命令在您的集群中执行它。以下清单使用带有 `nginx:latest` 的镜像。Kyverno 策略应阻止您应用该清单：

```bash
kubectl apply -f nginx-latest-tag.yaml
```

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-latest
  labels:
    app: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest  #This will trigger the policy to block
        ports:
        - containerPort: 80
```

您可以在下面看到我们无法使用最新镜像标签创建 NGINX pod。这是使用像 Kynervo 这样的策略引擎来强制执行安全最佳实践的本质。

![](https://cdn.thenewstack.io/media/2025/06/883c1dcc-image5a.png)

通过强制执行诸如禁止可变镜像标签（latest）之类的策略，团队可以：

- 防止未版本化或不稳定镜像的意外部署
- 提高可追溯性和可重复性
- 加强集群的整体安全态势

## 什么是 OPA Gatekeeper？

[Open Policy Agent (OPA) Gatekeeper](https://www.openpolicyagent.org/integrations/gatekeeper/) 是一种专门为 Kubernetes 设计的策略执行工具。策略使用 [Rego，OPA 的声明式查询语言](https://www.openpolicyagent.org/docs/policy-language) 编写，以定义规则并动态执行安全策略。它允许你编写策略来检查 Kubernetes 设置中的某些内容是否违反了定义的规则。

OPA Gatekeeper 充当 Kubernetes 准入控制器，在部署资源之前评估策略，并帮助从一开始就确保合规性。

以下是一个简单的 Rego 规则示例，用于确保 Kubernetes 集群中的所有命名空间都具有 team 标签：

```
package kubernetes.admission

violation[{"msg": "Namespace must have a 'team' label"}] {
  api_object.kind == "Namespace"
  not has_label(api_object.metadata.labels, "team")
}

has_label(labels, label) {
  labels[label]
}
```

## OPA Gatekeeper 的主要特性

- 策略逻辑与约束分离，使其可在不同的策略中重用。以 Rego 编写的策略逻辑定义了应该检查的内容（例如：“命名空间必须具有 team 标签”），而约束告诉 Gatekeeper 在何处以及何时应用策略逻辑（例如：“将此规则应用于此集群中的所有命名空间”）。
- 它可以扫描现有资源以查找违规行为。

## Kyverno 和 OPA Gatekeeper 的比较

| 特性       | Kyverno | OPA Gatekeeper |
| ---------- | ------- | -------------- |
| 策略语言   | YAML    | Rego           |
| 复杂性     | 简单    | 复杂           |
| 变更支持   | 是      | 否             |
| 自定义资源支持 | 是      | 有限           |
| 灵活性     | 中等    | 高             |
| 学习曲线   | 低      | 高             |

## 选择 Kyverno 还是 OPA Gatekeeper

Kyverno 和 OPA Gatekeeper 之间的选择取决于你的具体需求和技术专长：

**如果满足以下条件，请选择 Kyverno**：

- 你更喜欢 Kubernetes 原生方法，使用 YAML 将策略定义为 CRD。
- 你和你的团队熟悉 Kubernetes 概念和 YAML。
- 你需要一种更简单、更直观的方式来定义常见的 Kubernetes 安全策略。

**如果满足以下条件，请选择 OPA Gatekeeper**：

- 你和你的组织在 Rego 方面拥有现有专业知识，或者愿意投资学习它。
- 你需要表达高度复杂和自定义的策略逻辑。
- 你需要使用更成熟且被广泛采用的策略引擎，并获得更广泛的社区支持。
- 你需要一个通用的策略引擎，该引擎可以跨多个系统使用。OPA Gatekeeper 不仅可以用于在 Kubernetes 环境中执行策略，还可以跨各种系统（如微服务、云平台等）执行策略。

Kyverno 和 OPA Gatekeeper 在实施后，都可以强制执行安全最佳实践，例如：

- 强制执行基于命名空间的资源配额。
- 限制特权容器执行。
- 要求特定的标签和注解。

## 在你的集群中安装 OPA Gatekeeper

你需要在你的工作站上运行 [Helm](https://helm.sh/)。

**步骤 1：添加 Gatekeeper Helm Repo：**

```
helm repo add gatekeeper https://open-policy-agent.github.io/gatekeeper/charts
helm repo update
```

![](https://cdn.thenewstack.io/media/2025/06/bc38a892-image6a.png)

**步骤 2：安装 Gatekeeper**

```
helm install gatekeeper gatekeeper/gatekeeper \
  --namespace gatekeeper-system \
  --create-namespace
```

![](https://cdn.thenewstack.io/media/2025/06/5e241521-image7a.png)

![](https://cdn.thenewstack.io/media/2025/06/8a6277c4-image8a.png)

## OPA Gatekeeper 策略示例

**用例 1**：它阻止用户部署使用 `:latest` 标签的容器。

**步骤 1：创建约束模板（它定义逻辑）**

请将以下代码段复制并粘贴到文件名为 `disallow-latest-tag-constraint-template.yaml` 的文件中。

`kubectl apply -f disallow-latest-tag-constraint-template.yaml`

```yaml
apiVersion: templates.gatekeeper.sh/v1beta1
kind: ConstraintTemplate
metadata:
  name: k8sdisallowlatesttag
spec:
  crd:
    spec:
      names:
        kind: K8sDisallowLatestTag
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        package k8sdisallowlatesttag

        # Function to check containers for "latest" tag
        check_container(container) = msg {
          endswith(container.image, ":latest")
          msg := sprintf("Container '%s' is using a disallowed image tag 'latest'.", [container.name])
        }

        # Violations for regular containers in Pods
        violation[{"msg": msg}] {
          input.review.object.kind == "Pod"
          container := input.review.object.spec.containers[_]
          msg := check_container(container)
        }

        # Violations for init containers in Pods
        violation[{"msg": msg}] {
          input.review.object.kind == "Pod"
          container := input.review.object.spec.initContainers[_]
          msg := check_container(container)
        }

        # Violations for containers in Deployments
        violation[{"msg": msg}] {
          input.review.object.kind == "Deployment"
          container := input.review.object.spec.template.spec.containers[_]
          msg := check_container(container)
        }

        # Violations for init containers in Deployments
        violation[{"msg": msg}] {
          input.review.object.kind == "Deployment"
          container := input.review.object.spec.template.spec.initContainers[_]
          msg := check_container(container)
        }

        # Violations for containers in StatefulSets
        violation[{"msg": msg}] {
          input.review.object.kind == "StatefulSet"
          container := input.review.object.spec.template.spec.containers[_]
          msg := check_container(container)
        }

        # Violations for init containers in StatefulSets
        violation[{"msg": msg}] {
          input.review.object.kind == "StatefulSet"
          container := input.review.object.spec.template.spec.initContainers[_]
          msg := check_container(container)
        }

```

**步骤 2：约束（激活并应用模板）**

请将以下代码段复制并粘贴到文件名为 `disallow-latest-tag-gatekeeper.yaml` 的文件中。

`kubectl apply -f disallow-latest-tag-gatekeeper.yaml`

```yaml
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sDisallowLatestTag
metadata:
  name: disallow-latest-tag
spec:
  enforcementAction: deny
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
      - apiGroups: ["apps"]
        kinds: ["Deployment", "StatefulSet", "DaemonSet"]
```

![](https://cdn.thenewstack.io/media/2025/06/93d1f56f-image9a.png)

**步骤 3：应用带有“Latest”标签的 NGINX**

请将以下代码段复制并粘贴到文件名为 `nginx-latest.yaml` 的文件中。使用此命令在你的集群中执行它。以下清单使用带有 `nginx:latest` 的镜像。Gatekeeper Rego 策略应阻止你应用该清单。

`kubectl apply -f nginx-latest-tag.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-latest
  labels:
    app: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest  #This will trigger the policy to block
        ports:
        - containerPort: 80
```

![带有标签 latest 的容器。](https://cdn.thenewstack.io/media/2025/06/9aebb6e9-image10a-1024x107.png)

*带有标签“latest”的容器。*

## 结论

Kyverno 和 OPA Gatekeeper 都是确保 Kubernetes 工作负载安全的实用工具。Kyverno 以其简单的、基于 YAML 的策略和 Kubernetes 原生设计脱颖而出，使其易于使用。另一方面，OPA Gatekeeper 通过其 Rego 语言带来了强大的灵活性，该语言擅长处理复杂的设置或跨多个平台工作。选择哪一个真正取决于您的团队需求、您的经验水平和您的安全目标。这两种工具都可以帮助开发人员快速而自信地行动，同时遵守规则，确保安全性、合规性和最佳实践融入到所有环节中，而不会拖慢任何人的速度。

了解如何创建一个端到端的解决方案，以自动化基于 Kubernetes 的 Node.js REST API 的构建、测试和部署流程，请参阅 Andela 的指南“[使用 GitHub 和 Argo CD 为 Kubernetes 构建可扩展的 CI/CD 管道](https://www.andela.com/blog-posts/make-a-scalable-ci-cd-pipeline-for-kubernetes-with-github-and-argo-cd/?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack&utm_content=kubernetes-gatekeeper&utm_term=writers-room)”。