# 配置语言 (config DSL) 能解决配置复杂性吗？

过去几年涌现出大量旨在生成配置的领域特定语言 (DSL)，即*配置语言*：[HCL](https://github.com/hashicorp/hcl)，[Dhall](https://dhall-lang.org/)，[Jsonnet](https://jsonnet.org/)，[Starlark](https://github.com/bazelbuild/starlark)，[CUE](https://cuelang.org/)，[Nickel](https://nickel-lang.org/)，[KCL](https://www.kcl-lang.io/)，[Pkl](https://pkl-lang.org/)，以及[其他](https://github.com/rix0rrr/gcl)。我敢肯定至少有[15种](https://xkcd.com/927/)。我通过包含表达式、条件语句、变量和其他语法结构来区分这些语言和 JSON、XML、TOML、INI 等数据序列化语言，这些结构有助于根据输入生成多个具体的配置作为输出。我将 YAML 归类为数据序列化类别。[YAMLScript](https://yamlscript.org/) 比较新，我还没有看到任何使用案例，因此不会介绍它。有关不同类型语言的更详细细分，请参阅[KCL 项目的这篇文章](https://blog.stackademic.com/10-ways-for-kubernetes-declarative-configuration-management-3538673fd0b5)，该文章还[比较了 KCL 与许多这些语言](https://www.kcl-lang.io/docs/user_docs/getting-started/intro)。

为什么有人会选择使用配置语言来编写配置生成器/模板，而不是通用语言或模板语言（例如，Go 模板、Jinja、Mustache）？

对于工具构建者而言，与通用语言相比，一个好处是这些语言（大多）是解释型语言，并且可以嵌入到工具中，尽管模板语言也具有此特性。配置语言也可能比通用语言或模板语言更容易进行静态分析，并且可以轻松地[确保它们不会产生副作用](https://sre.google/workbook/configuration-specifics/)。

除了[根据自己的喜好塑造语言](https://ruudvanasseldonk.com/2024/a-reasonable-configuration-language)之外，创建新的配置语言的好处还在于它可以更好地控制包和注册表系统以及标准库。事实上，其中一些语言最初是[为特定工具创建的](https://www.reddit.com/r/ProgrammingLanguages/comments/gzqsxj/the_future_of_general_purpose_configuration/)，例如 Terraform 的 HCL，Bazel 的 Starlark [Bazel](https://bazel.build/extending/config)，Nix 包管理器的 Nickel [Nix 包管理器](https://www.tweag.io/blog/2023-01-24-nix-with-with-nickel/)，以及 KusionStack 的 KCL [KusionStack](https://www.kusionstack.io/docs/)。

对于用户而言，语法可能比通用语言更简洁。此外，我读到一些非程序员发现 HCL 与脚本语言（如 shell、awk 和/或 perl？）足够相似，与 Python 和 Typescript 等通用语言相比更容易上手。对于程序员而言，[使用熟悉的通用语言](/generating-configuration-using-general-purpose-programming-languages-19230a2c2573) 是 Pulumi 等工具的一个卖点，但也许配置语言可以在多个通用语言用于应用程序的环境中提供一个中立的中间地带。与模板语言相比，配置语言具有更强大的表达能力，并且通常具有更高的类型安全性和模式验证能力。

当然，每位语言设计者在设计语言时都有一些具体目标。例如，[CUE](https://cuelang.org/docs/introduction/) 基于从 Google 内部配置语言中吸取的经验教训（[Jsonnet](https://jsonnet.org/) 也是如此），CUE 的一个目标是[通过不允许覆盖来更容易确定最终值设置的位置](https://cuelang.org/docs/concept/the-logic-of-cue/#relation-to-inheritance)。[Dhall 的一个目标是使导入安全](https://dhall-lang.org/)。Starlark 是一种[可嵌入的 Python 方言](https://github.com/bazelbuild/starlark/?tab=readme-ov-file#design-principles)，对于熟悉 Python 的人来说很熟悉。Jsonnet 是[JSON 的超集](https://jsonnet.org/articles/design.html)。[Nickel 中的类型是可选的](https://nickel-lang.org/user-manual/introduction)。[Pkl](https://www.youtube.com/watch?v=N7zmsHUiTkM)……等等。至少从编程语言设计的角度来看，它们很有趣。
好的，这些语言看起来是什么样的？由于我不精通大多数这些语言，我使用了Claude来生成每个语言的Kubernetes Deployment示例，其中资源名称、标签值和容器镜像都是参数化的。我不得不说，我对Claude印象非常深刻。Claude包含了如何运行每个工具的说明，提到了每种语言的一些好处，并提供了使用特定语言功能进一步改进的建议。我将结果与我能找到的其他示例进行了比较，但没有通过这些工具运行它们。这只是为了说明这些语言的特点。

以下是Deployment的YAML，其中包含一些属性值，这些值是字符串、整数和布尔值，以及映射和数组/列表：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: mydep
  name: mydep
  namespace: example
spec:
  replicas: 3
  selector:
    matchLabels:
      app: mydep
  template:
    metadata:
      labels:
        app: mydep
    spec:
      dnsPolicy: ClusterFirst
      containers:
      - image: nginx:latest
        name: nginx
        ports:
        - containerPort: 8080
```

使用[Kubernetes 提供程序](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/deployment#example-usage) 的HCL：

```hcl
# Variables
variable "deployment_name" {
  description = "Name of the Kubernetes deployment"
  type = string
}

variable "container_image" {
  description = "Container image to deploy"
  type = string
}

# Deployment resource
resource "kubernetes_deployment" "deployment" {
  metadata {
    name      = var.deployment_name
    namespace = "example"
    labels = {
      app = var.deployment_name
    }
  }

  spec {
    replicas = 3
    selector {
      match_labels = {
        app = var.deployment_name
      }
    }
    template {
      metadata {
        labels = {
          app = var.deployment_name
        }
      }
      spec {
        dns_policy = "ClusterFirst"
        container {
          name  = "nginx"
          image = var.container_image
          port {
            container_port = 8080
          }
        }
      }
    }
  }
}
```

Dhall ([官方示例](https://github.com/dhall-lang/dhall-kubernetes/blob/master/examples/deployment.dhall))：

```dhall
-- Type definitions for our configuration
let Kubernetes =
  https://raw.githubusercontent.com/dhall-lang/dhall-kubernetes/master/package.dhall
let deploymentName : Text = "mydep"
let containerImage : Text = "nginx:latest"
let deploymentLabels =
  toMap { app = deploymentName }
let containerPort =
  Kubernetes.ContainerPort::{
    , containerPort = 8080
  }
let container =
  Kubernetes.Container::{
    , name = "nginx"
    , image = Some containerImage
    , ports = Some [ containerPort ]
  }
let podTemplateSpec =
  Kubernetes.PodTemplateSpec::{
    , metadata = Some Kubernetes.ObjectMeta::{ labels = Some deploymentLabels }
    , spec = Some Kubernetes.PodSpec::{
      , containers = [ container ]
      , dnsPolicy = Some "ClusterFirst"
    }
  }
let deploymentSpec =
  Kubernetes.DeploymentSpec::{
    , replicas = Some 3
    , selector = Kubernetes.LabelSelector::{ matchLabels = Some deploymentLabels }
    , template = podTemplateSpec
  }
in Kubernetes.Deployment::{
  , metadata = Kubernetes.ObjectMeta::{
    , name = Some deploymentName
    , namespace = Some "example"
    , labels = Some deploymentLabels
  }
  , spec = Some deploymentSpec
}
```

Jsonnet ([更多Kubernetes示例](https://jsonnet.org/articles/kubernetes.html))：

```jsonnet
// Input parameters
local params = {
  deploymentName: 'mydep',
  containerImage: 'nginx:latest',
};

// Helper to generate consistent labels
local labels = {
  app: params.deploymentName,
};

// Main deployment definition
{
  apiVersion: 'apps/v1',
  kind: 'Deployment',
  metadata: {
    name: params.deploymentName,
    namespace: 'example',
    labels: labels,
  },
  spec: {
    replicas: 3,
    selector: {
      matchLabels: labels,
    },
    template: {
      metadata: {
        labels: labels,
      },
      spec: {
        dnsPolicy: 'ClusterFirst',
        containers: [
          {
            name: 'nginx',
            image: params.containerImage,
            ports: [
              {
                containerPort: 8080,
              },
            ],
          },
        ],
      },
    },
  },
}
```

CUE ([Kubernetes 教程](https://github.com/cue-labs/cue-by-example/tree/main/003_kubernetes_tutorial#controlling-kubernetes-with-cue)) — 我删除了模式，因为它可能已被导入：

```cue
// Input parameters
params: {
  deploymentName: string
  containerImage: string
}

// Default values
params: {
  deploymentName: "mydep"
  containerImage: "nginx:latest"
}

// Deployment configuration
deployment: #Deployment & {
  metadata: {
    name: params.deploymentName
    namespace: "example"
    labels: {
      app: params.deploymentName
    }
  }
  spec: {
    replicas: 3
    selector: {
      matchLabels: {
        app: params.deploymentName
      }
    }
    template: {
      metadata: {
        labels: {
          app: params.deploymentName
        }
      }
      spec: {
        containers: [{
          name: "nginx"
          image: params.containerImage
          ports: [{
            containerPort: 8080
          }]
        }]
      }
    }
  }
}

// Output the deployment
deployment
```

Pkl ([示例](https://github.com/apple/pkl-k8s-examples/tree/main/pkl))：

```pkl
module deployment
import "package://pkg.pkl-lang.org/k8s/apps/v1/1.27" as apps
import "package://pkg.pkl-lang.org/k8s/core/v1/1.27" as core

// Input parameters
deployCfg {
  name: String = "mydep"
  image: String = "nginx:latest"
}

// Create deployment using official K8s types
output = new apps.Deployment {
  metadata {
    name = deployCfg.name
    namespace = "example"
    labels = new {
      app = deployCfg.name
    }
  }
}
```

app = deployCfg.name
}
}
spec {
replicas = 3
selector {
matchLabels = new {
app = deployCfg.name
}
}
template {
metadata {
labels = new {
app = deployCfg.name
}
}
spec {
dnsPolicy = "ClusterFirst"
containers = List(
new core.Container {
name = "nginx"
image = deployCfg.image
ports = List(
new core.ContainerPort {
containerPort = 8080
}
)
}
)
}
}
}
}
Nickel ([示例](https://github.com/tweag/nickel-kubernetes/blob/master/examples/redis-replication-controller.ncl)):

```# 类型契约```
let DeploymentConfig = {
  name | Str,
  image | Str,
}
```# 生成标签的函数```
let makeLabels = fun name => {
  app = name
}
```# 主部署生成器函数```
let makeDeployment = fun config | DeploymentConfig => {
  apiVersion = "apps/v1",
  kind = "Deployment",
  metadata = {
    name = config.name,
    namespace = "example",
    labels = makeLabels config.name,
  },
  spec = {
    replicas = 3,
    selector = {
      matchLabels = makeLabels config.name,
    },
    template = {
      metadata = {
        labels = makeLabels config.name,
      },
      spec = {
        dnsPolicy = "ClusterFirst",
        containers = [
          {
            name = "nginx",
            image = config.image,
            ports = [
              {
                containerPort = 8080,
              },
            ],
          },
        ],
      },
    },
  },
}
```# 默认配置```
let defaultConfig = {
  name = "mydep",
  image = "nginx:latest",
}
```# 使用默认配置生成部署```
makeDeployment defaultConfig
KCL ([示例](https://github.com/kcl-lang/examples)):

```import k8s.api.apps.v1 as appsv1```
import k8s.api.core.v1 as corev1
```# 配置参数```
schema DeploymentConfig:
  name: str = "mydep"
  image: str = "nginx:latest"
```# 配置值```
config = DeploymentConfig {}
```# 使用标准库类型生成部署```
deployment = appsv1.Deployment {
  metadata = corev1.ObjectMeta {
    name = config.name
    namespace = "example"
    labels.app = config.name
  }
  spec = appsv1.DeploymentSpec {
    replicas = 3
    selector = corev1.LabelSelector {
      matchLabels.app = config.name
    }
    template = corev1.PodTemplateSpec {
      metadata = corev1.ObjectMeta {
        labels.app = config.name
      }
      spec = corev1.PodSpec {
        dnsPolicy = "ClusterFirst"
        containers = [
          corev1.Container {
            name = "nginx"
            image = config.image
            ports = [
              corev1.ContainerPort {
                containerPort = 8080
              }
            ]
          }
        ]
      }
    }
  }
}
Starlark ([示例](https://github.com/cruise-automation/isopod/blob/master/examples/ingress.ipd)):

```# 创建一致标签的辅助函数```
def make_labels(name):
  return {"app": name}
```# 主部署生成器函数```
def make_deployment(name = "mydep", image = "nginx:latest"):
  """创建 Kubernetes 部署配置。
  参数：
  name: 部署的名称
  image: 要部署的容器镜像
  返回：
  包含部署配置的字典
  """
  return {
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
      "name": name,
      "namespace": "example",
      "labels": make_labels(name),
    },
    "spec": {
      "replicas": 3,
      "selector": {
        "matchLabels": make_labels(name),
      },
      "template": {
        "metadata": {
          "labels": make_labels(name),
        },
        "spec": {
          "dnsPolicy": "ClusterFirst",
          "containers": [
            {
              "name": "nginx",
              "image": image,
              "ports": [
                {
                  "containerPort": 8080,
                },
              ],
            },
          ],
        },
      },
    },
  }
```# 默认部署配置```
deployment = make_deployment()
def main(ctx):
  """Starlark 配置的主入口点。
  参数：
  ctx: 规则上下文
  返回：
  部署配置
  """
  return deployment
正如不同的通用编程语言一样，[语法](https://github.com/lightbend/config/blob/master/HOCON.md#syntax) 显然也略有不同：是否使用大括号，是否允许尾随逗号，双引号与单引号与无引号，严格嵌套与否，冒号与等号，是否使用类型名称，是否在语言内部定义模式，是否需要显式生成语句，额外的关键字或标点符号等等。有些语言的样板代码稍多一些，有些则稍少一些。类型安全在每种语言中的工作方式也略有不同。不同的语言会让不同的人感觉更熟悉，这取决于他们了解的其他语言。例如，Dhall 可能[对熟悉 Haskell 的人来说更熟悉](https://pv.wtf/posts/taming-the-beast#dhall)。

在这个例子中，这些语言并没有什么显著的优势。我本可以使用 `envsubst`。我没有使用更复杂的例子，例如围绕 Deployment 构建可重用的函数或模块，部分原因是为了保持例子的简单性，部分原因是我已经多次看到[这种抽象被削弱](/the-tension-between-flexibility-and-simplicity-in-infrastructure-as-code-6cec841e3d16)，并且已经看到试图[使配置更可重用适得其反](https://medium.com/itnext/how-software-engineering-instincts-clash-with-infrastructure-as-code-6b18a9cd9cef) 的尝试。在任何这些语言中，具有大量参数的 Kubernetes Deployment 也不会更简单。

无论如何，没有任何配置语言能够比使用 cdk8s 或 Pulumi 等通用语言的工具更强大。配置语言在 JSON 和 YAML 等数据格式与通用语言之间是一种折衷方案。对某些人来说，这是一个恰到好处的选择，而对另一些人来说则不然。或者只是[配置复杂性时钟](https://mikehadlow.blogspot.com/2012/05/configuration-complexity-clock.html)上的一个停顿点。

其目的是，语言施加的约束应该使更容易发现和防止错误，并可能使配置更容易阅读和/或编写。但是，虽然我已经阅读了许多关于哪些语言“更好”或“更差”的[冗长辩论](https://news.ycombinator.com/item?id=22787332)，但它们都是主观的，并且没有达成共识。我没有看到任何关于用不同语言表达配置生成器的定量益处的研究。如果您知道任何此类研究，请告诉我！

此外，虽然这些语言周围的生态系统有时优于模板语言（[Pkl 更强调其集成](https://github.com/apple/pkl/discussions/7)而不是特定语言特性），但它们实际上无法与通用语言相比。配置语言可用的文档、示例、教育内容、工具集成、服务集成等都较少。

原因之一是，所有配置语言的使用范围都远不如 Python 或 Javascript 等流行的编程语言广泛。其中最流行的语言是 HCL，这当然是因为 Terraform 的流行。但是，我没有看到 HCL 在 Terraform 生态系统之外使用，有些人甚至[用 YAML 包装它的用途](https://github.com/AppsFlyer/terra-crust)。就像[Helm 的模板语法](/kubernetes-configuration-in-2024-434abc7a5a1b)一样，并非每个人都喜欢它，但它通常都能完成工作。

好的，我的观点是什么？

如果您读到这里，您可能已经猜到我认为配置语言并不是解决配置复杂性的最佳方案。每种语言都有其优缺点，但没有任何一种语言能带来显著的改变。它们是微优化而不是宏优化。正如我[之前提到的](/fundamental-challenges-with-infrastructure-as-code-imply-the-language-doesnt-matter-41030475c296)那样，没有任何新的配置语言能够解决[IaC 的根本问题](/the-12-anti-factors-of-infrastructure-as-code-acb52fba3ae0)。为了取得显著改进，我们需要对整体方法进行一些宏观层面的改变。

您是否有我未涉及的喜欢的配置语言？它的优势是什么？您是否发现使用配置语言与其他表示和方法相比有任何显著的、可衡量的益处？您是否发现该语言的任何静态分析工具特别有用？您组织中的其他人学习该语言是否遇到任何困难？您是否想知道为什么我们到 2025 年仍在手动编写配置文件？

请随时在此处回复，或通过[LinkedIn](https://www.linkedin.com/in/bgrant0607/), [X/Twitter](https://x.com/bgrant0607), 或[Bluesky](https://bsky.app/profile/bgrant0607.bsky.social)向我发送消息，我计划将此内容交叉发布。

如果您觉得这篇文章有趣，您可能还会对我的[基础设施即代码和声明式配置系列](https://medium.com/@bgrant0607/list/infrastructure-as-code-and-declarative-configuration-8c441ae74836)中的其他文章感兴趣。