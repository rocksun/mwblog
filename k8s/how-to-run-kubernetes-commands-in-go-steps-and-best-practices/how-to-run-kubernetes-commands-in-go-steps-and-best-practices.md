
<!--
title: Go语言执行Kubernetes命令
cover: https://cdn.thenewstack.io/media/2025/06/09545098-lukas-baumann-xxbkdtlzu1k-unsplash.jpg
summary: 本文介绍了如何使用 Go 语言和 client-go 库与 Kubernetes 集群进行交互，包括安装配置 client-go、运行 kubectl 命令、处理身份验证和授权、解析和打印 Kubernetes 对象、错误处理、重试和退避策略，以及单元和集成测试。此外，还提供了构建生产级 CLI 工具的 10 个最佳实践。
-->

本文介绍了如何使用 Go 语言和 client-go 库与 Kubernetes 集群进行交互，包括安装配置 client-go、运行 kubectl 命令、处理身份验证和授权、解析和打印 Kubernetes 对象、错误处理、重试和退避策略，以及单元和集成测试。此外，还提供了构建生产级 CLI 工具的 10 个最佳实践。

> 译自：[How To Run Kubernetes Commands in Go: Steps and Best Practices](https://thenewstack.io/how-to-run-kubernetes-commands-in-go-steps-and-best-practices/)
> 
> 作者：Sunny Yadav

要点：

* 你可以使用 `client-go` 库在 Go 中运行 Kubernetes 命令，或者通过 `exec.Command` 执行原始的 `kubectl` 命令。
* 使用重试循环和退避策略，可靠地处理 API 超时、冲突和瞬时错误。
* 遵循最佳实践，如输入验证、结构化输出和 CLI 框架，来构建生产就绪的工具。

以编程方式运行 [Kubernetes](https://thenewstack.io/kubernetes/) 命令起初可能会让人感到不知所措。你可能会发现在脚本中调用 `kubectl`，或者试图处理复杂的 API，仅仅为了列出几个 Pod 或应用一个配置。从哪里开始，或者如何在 [Golang (Go)](https://thenewstack.io/go-power-microsofts-bold-bet-on-faster-typescript-tools/) 中干净地完成这些操作，并不总是很清楚。

好消息是？你不需要依赖 shell 技巧或猜测。Go 是 Kubernetes 本身编写的语言 —— 并且使用官方的 `client-go` 库，你可以像 `kubectl` 一样直接与你的集群交互。

学习如何在 Go 中运行核心 Kubernetes 操作。从设置客户端到处理身份验证、解析输出和编写可测试的代码，获得构建自己的工具和自动化的实践基础。

## 为什么使用 Go 进行 Kubernetes 自动化

[Go 是使用 Kubernetes 的最佳语言之一](https://thenewstack.io/introduction-to-go-programming-language/)。事实上，Kubernetes 本身就是用 Go 编写的。这意味着在编写工具或自动化脚本时，你可以获得一流的支持和对官方客户端库的访问。

以下是使用 Go 进行 Kubernetes 自动化的一些关键原因：

* **官方支持：** Kubernetes 客户端库是用 Go 编写和维护的。
* **强大的社区：** 许多示例、工具和开源项目都使用 Go。
* **快速的性能：** Go 是编译型的，速度很快，非常适合[命令行界面 (CLI)](https://thenewstack.io/guis-cli-apis-learn-basic-terms-of-infrastructure-as-code/) 工具和控制器。
* **轻松的并发：** Go 的内置并发（通过 goroutine）有助于一次管理许多 Kubernetes 资源。
* **静态类型：** 你可以及早发现错误，这对于自动化工具来说很重要。
* **跨平台：** 轻松构建和运行在任何操作系统上的工具。
* **轻量级二进制文件：** 创建小型、自包含的可执行文件，无需运行时依赖项。

## 在 Go 中运行 Kubernetes 命令的先决条件

在 Go 中运行 Kubernetes 命令之前，你需要准备好一些工具和设置。这些将确保你的 Go 代码可以连接到你的集群并安全地执行操作。以下是你需要的。

### Go 工具链和模块

要编写和运行 [Go 代码](https://thenewstack.io/learn-the-go-programming-language-start-here/)，你需要安装 Go 工具链。这包括 Go 编译器、`go` 命令行工具和对模块的支持（即 Go 的依赖管理系统）。

以下是它为何重要的原因：

* **编译你的代码：** 你需要 Go 编译器来构建你的 Kubernetes 工具。
* **管理依赖项：** Go 模块可以帮助你引入 Kubernetes 客户端库并保持版本井井有条。
* **可重现的构建：** 通过模块，你的代码可以在系统之间一致地共享或部署。

要检查是否已安装 Go，请在你的终端中运行 `go version`。要初始化一个模块，请使用 `go mod init <你的模块名>`。 

### Kubeconfig 访问和 RBAC

要与 Kubernetes 集群交互，你的 Go 程序需要访问 kubeconfig 文件。此文件告诉你的代码如何连接到集群以及使用什么凭据。[基于角色的访问控制 (RBAC)](https://thenewstack.io/role-based-access-control-five-common-authorization-patterns/) 也很重要。它定义了你的代码允许执行的操作。

以下是这为何重要的原因：

* **集群连接：** kubeconfig 文件是你的代码如何知道集群在哪里以及如何与它通信的。
* **权限：** 如果没有正确的 RBAC 角色，你的代码在尝试列出 Pod、创建 Deployment 等时可能会被拒绝。
* **安全性：** RBAC 有助于将操作限制在你需要的范围内，从而降低意外更改的风险。

确保你使用的用户或服务帐户具有你计划自动执行的任务的正确角色。 

## 安装和配置 `client-go`

要在 Go 中运行 Kubernetes 命令，你需要官方的 Go 客户端库，称为 `client-go`。这个库为你的代码提供了连接到你的集群和使用 Kubernetes 资源的工具。以下是如何将它添加到你的项目并加载你的集群凭据。

### 添加模块

首先，你需要将 `client-go` 添加到你的 Go 模块。我们使用 `go get` 命令来完成它，该命令将库拉入你的项目，并允许你在你的代码中使用它。

使用此命令获取最新版本的 `client-go` 库，并将其添加到你的 `go.mod` 文件：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | go get k8s.io/client-go@latest |

你可能还需要相关的软件包，具体取决于你的设置：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | go get k8s.io/apimachinery@latest |

这些库有助于定义和管理 Kubernetes 对象。之后，你的 `go.mod` 文件应该包含依赖项，你就可以开始 [编码](https://thenewstack.io/seven-habits-of-highly-effective-ai-coding/) 了。

### 在代码中加载集群凭据

要连接到 Kubernetes 集群，`client-go` 使用你的 kubeconfig 文件 —— 与你使用 `kubectl` 的文件相同。这是一个加载你的凭据并创建一个客户端的基本示例：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | package main |
|  |  |
|  | import ( |
|  |  |
|  | "flag" |
|  |  |
|  | "fmt" |
|  |  |
|  | "path/filepath" |
|  |  |
|  | "k8s.io/client-go/kubernetes" |
|  |  |
|  | "k8s.io/client-go/tools/clientcmd" |
|  |  |
|  | "k8s.io/client-go/util/homedir" |
|  |  |
|  | ) |
|  |  |
|  | func main() { |
|  |  |
|  | var kubeconfig string |
|  |  |
|  | if home := homedir.HomeDir(); home != "" { |
|  |  |
|  | kubeconfig = filepath.Join(home, ".kube", "config") |
|  |  |
|  | } |
|  |  |
|  | config, err := clientcmd.BuildConfigFromFlags("", kubeconfig) |
|  |  |
|  | if err != nil { |
|  |  |
|  | panic(err.Error()) |
|  |  |
|  | } |
|  |  |
|  | clientset, err := kubernetes.NewForConfig(config) |
|  |  |
|  | if err != nil { |
|  |  |
|  | panic(err.Error()) |
|  |  |
|  | } |
|  |  |
|  | fmt.Println("Kubernetes client configured successfully!") |
|  |  |
|  | } |

这是此代码的作用：

* 在默认位置查找 kubeconfig 文件。
* 加载配置并创建一个 Kubernetes 客户端。
* 准备客户端，以便你可以运行命令，如列出 Pod 或创建 Deployment。

## 运行核心 `kubectl` 等效命令

一旦你使用 `client-go` 设置了你的 Go 项目，你就可以开始执行你通常使用 `kubectl` 执行的相同任务 —— 但以编程方式。这对于构建自定义工具、自动化工作流或编写控制器非常有用。

以下是有关如何使用 Go 列出、创建和删除 Kubernetes 资源的示例。

### 列出 Pod、Deployment 和 Service

以下是如何列出特定[命名空间](https://thenewstack.io/what-are-linux-namespaces-and-how-are-they-used/)中的常用资源：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | pods, err := clientset.CoreV1().Pods("default").List(ctx, metav1.ListOptions{}) |
|  |  |
|  | if err != nil { |
|  |  |
|  | panic(err) |
|  |  |
|  | } |
|  |  |
|  | for \_, pod := range pods.Items { |
|  |  |
|  | fmt.Println("Pod:", pod.Name) |
|  |  |
|  | } |
|  |  |
|  | deployments, err := clientset.AppsV1().Deployments("default").List(ctx, metav1.ListOptions{}) |
|  |  |
|  | if err != nil { |
|  |  |
|  | panic(err) |
|  |  |
|  | } |
|  |  |
|  | for \_, deploy := range deployments.Items { |
|  |  |
|  | fmt.Println("Deployment:", deploy.Name) |
|  |  |
|  | } |
|  |  |
|  | services, err := clientset.CoreV1().Services("default").List(ctx, metav1.ListOptions{}) |
|  |  |
|  | if err != nil { |
|  |  |
|  | panic(err) |
|  |  |
|  | } |
|  |  |
|  | for \_, svc := range services.Items { |
|  |  |
|  | fmt.Println("Service:", svc.Name) |
|  |  |
|  | } |

这类似于运行 `kubectl get pods`、`kubectl get deployments` 或 `kubectl get services`。

### 创建或更新资源

你可以使用 Go 结构体创建一个新的 [Kubernetes Deployment](https://thenewstack.io/a-look-at-kubernetes-deployment/)（或其他资源）。这是一个 Deployment 的基本示例：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | deployment := &appsv1.Deployment{ |
|  |  |
|  | ObjectMeta: metav1.ObjectMeta{ |
|  |  |
|  | Name: "my-deployment", |
|  |  |
|  | }, |
|  |  |
|  | Spec: appsv1.DeploymentSpec{ |
|  |  |
|  | Replicas: pointer.Int32Ptr(2), |
|  |  |
|  | Selector: &metav1.LabelSelector{ |
|  |  |
|  | MatchLabels: map[string]string{"app": "my-app"}, |
|  |  |
|  | }, |
|  |  |
|  | Template: corev1.PodTemplateSpec{ |
|  |  |
|  | ObjectMeta: metav1.ObjectMeta{ |
|  |  |
|  | Labels: map[string]string{"app": "my-app"}, |
|  |  |
|  | }, |
|  |  |
|  | Spec: corev1.PodSpec{ |
|  |  |
|  | Containers: []corev1.Container{ |
|  |  |
|  | { |
|  |  |
|  | Name:  "my-container", |
|  |  |
|  | Image: "nginx", |
|  |  |
|  | }, |
|  |  |
|  | }, |
|  |  |
|  | }, |
|  |  |
|  | }, |
|  |  |
|  | } |
|  |  |
|  | result, err := clientset.AppsV1().Deployments("default").Create(ctx, deployment, metav1.CreateOptions{}) |
|  |  |
|  | if err != nil { |
|  |  |
|  | panic(err) |
|  |  |
|  | } |
|  |  |
|  | fmt.Println("Created deployment:", result.Name) |

对于更新，你可以使用 Update() 代替 Create()，通常是在获取和修改现有资源之后。

### 删除资源

要删除资源，你只需在客户端上调用 delete 方法：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | err := clientset.CoreV1().Pods("default").Delete(ctx, "my-pod", metav1.DeleteOptions{}) |
|  | if err != nil { |
|  | panic(err) |
|  | } |
|  | fmt.Println("Pod deleted.") |

这对于 Deployment、Service 或其他资源的工作方式相同 —— 只需使用适当的客户端组。

## 以编程方式执行“原始” `kubectl` 命令

有时，从你的 Go 代码中运行实际的 `kubectl` 命令更容易或更灵活，特别是如果你不需要完全控制 Kubernetes API，或者如果你想重用熟悉的 CLI 行为。这种方法对于快速脚本、自动化或当你想要避免直接处理复杂的 Kubernetes 类型时很有用。

### 使用 `exec.Command`

Go 中的 `os/exec` 包允许你运行 shell 命令，包括 `kubectl`。以下是如何使用它：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | package main |
|  |  |
|  | import ( |
|  |  |
|  | "fmt" |
|  |  |
|  | "os/exec" |
|  |  |
|  | ) |
|  |  |
|  | func main() { |
|  |  |
|  | cmd := exec.Command("kubectl", "get", "pods", "-n", "default") |
|  |  |
|  | output, err := cmd.CombinedOutput() |
|  |  |
|  | if err != nil { |
|  |  |
|  | panic(err) |
|  |  |
|  | } |
|  |  |
|  | fmt.Println(string(output)) |
|  |  |
|  | } |

此代码运行 `kubectl get pods -n default` 并打印结果。它结合了 stdout 和 stderr，以防出现错误。在运行此代码之前，请确保 `kubectl` 已安装并在系统的 PATH 中可用。

### 流式传输 Stdout/Stderr

如果你想在命令运行时流式传输输出 —— 而不是等待它完成 —— 你可以这样做：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | cmd := exec.Command("kubectl", "logs", "-f", "my-pod", "-n", "default") |
|  |  |
|  | stdout, err := cmd.StdoutPipe() |
|  |  |
|  | if err != nil { |
|  |  |
|  | panic(err) |
|  |  |
|  | } |
|  |  |
|  | stderr, err := cmd.StderrPipe() |
|  |  |
|  | if err != nil { |
|  |  |
|  | panic(err) |
|  |  |
|  | } |
|  |  |
|  | if err := cmd.Start(); err != nil { |
|  |  |
|  | panic(err) |
|  |  |
|  | } |
|  |  |
|  | // Stream both stdout and stderr |
|  |  |
|  | go io.Copy(os.Stdout, stdout) |
|  |  |
|  | go io.Copy(os.Stderr, stderr) |
|  |  |
|  | if err := cmd.Wait(); err != nil { |
|  |  |
|  | panic(err) |
|  |  |
|  | } |

这种方法对于诸如 `kubectl logs -f` 或 `kubectl exec` 之类的命令很有用，在这些命令中，实时输出很重要。

## 处理身份验证和授权

要与 [Kubernetes 集群](https://thenewstack.io/kubernetes-building-blocks-nodes-pods-clusters/) 交互，你的 Go 程序需要适当的身份验证和权限。Kubernetes 支持不同的身份验证方式，具体取决于你的代码在何处运行 —— 在集群内部还是外部。以下是两种最常见的方法。

### 集群内服务帐户

如果你的 Go 程序在 Kubernetes 集群内部运行（例如，在 Pod 中），它可以为身份验证使用内置的服务帐户。

以下是它的工作方式：

* Kubernetes 会自动将令牌和证书挂载到你的 Pod 中，路径为：`/var/run/secrets/kubernetes.io/serviceaccount/`。
* `client-go` 在集群内运行时默认使用此路径。

使用此方法在你的代码中进行设置：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | import ( |
|  |  |
|  | "fmt" |
|  |  |
|  | "k8s.io/client-go/kubernetes" |
|  |  |
|  | "k8s.io/client-go/rest" |
|  |  |
|  | ) |
|  |  |
|  | func main() { |
|  |  |
|  | config, err := rest.InClusterConfig() |
|  |  |
|  | if err != nil { |
|  |  |
|  | panic(err.Error()) |
|  |  |
|  | } |
|  |  |
|  | clientset, err := kubernetes.NewForConfig(config) |
|  |  |
|  | if err != nil { |
|  |  |
|  | panic(err.Error()) |
|  |  |
|  | } |
|  |  |
|  | fmt.Println("Authenticated using in-cluster service account.") |
|  |  |
|  | } |

你还需要为服务帐户设置适当的 RBAC 角色或角色绑定，以控制它可以访问的内容。

### 集群外部令牌和证书

如果你的代码在集群外部运行，例如在你的笔记本电脑或 [CI/CD 管道](https://thenewstack.io/ci-cd/) 上，你通常会使用保存你的凭据的 kubeconfig 文件。

当你使用 `clientcmd.BuildConfigFromFlags` 时，`client-go` 会自动读取此文件。

此 kubeconfig 文件可以包含：

* 用户令牌
* 客户端证书和密钥
* 集群 CA 证书

这是一个快速示例：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | import ( |
|  |  |
|  | "k8s.io/client-go/tools/clientcmd" |
|  |  |
|  | "k8s.io/client-go/kubernetes" |
|  |  |
|  | ) |
|  |  |
|  | config, err := clientcmd.BuildConfigFromFlags("", "/path/to/kubeconfig") |
|  |  |
|  | if err != nil { |
|  |  |
|  | panic(err) |
|  |  |
|  | } |
|  |  |
|  | clientset, err := kubernetes.NewForConfig(config) |
|  |  |
|  | if err != nil { |
|  |  |
|  | panic(err) |
|  |  |
|  | } |

此设置对于在本地测试的开发人员或与 Kubernetes 安全交互的自动化工具很有用。

## 解析和打印 Kubernetes 对象

使用 Go 获取 Kubernetes 资源后，你可能希望以可读的格式（如 [YAML](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/)、JSON 或自定义视图）显示或导出它们。这对于调试、日志记录或构建具有类似于 `kubectl` 的输出的 CLI 工具很有用。以下是在 Go 中格式化 Kubernetes 对象的两种常用方法。

### 转换为 YAML/JSON

可以使用 Go 的编码库将 Kubernetes 对象序列化为 YAML 或 [JSON](https://thenewstack.io/an-introduction-to-json/)。

使用此代码将它们转换为 JSON：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | import ( |
|  |  |
|  | "encoding/json" |
|  |  |
|  | "fmt" |
|  |  |
|  | ) |
|  |  |
|  | data, err := json.MarshalIndent(pod, "", "  ") |
|  |  |
|  | if err != nil { |
|  |  |
|  | panic(err) |
|  |  |
|  | } |
|  |  |
|  | fmt.Println(string(data)) |

以下是将它们转换为 YAML 的代码：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | import ( |
|  |  |
|  | "fmt" |
|  |  |
|  | "sigs.k8s.io/yaml" |
|  |  |
|  | ) |
|  |  |
|  | data, err := yaml.Marshal(pod) |
|  |  |
|  | if err != nil { |
|  |  |
|  | panic(err) |
|  |  |
|  | } |
|  |  |
|  | fmt.Println(string(data)) |

两种格式在保存或显示完整的对象定义时都很有用。

### 使用 Go 模板进行自定义输出

如果你只想打印特定字段，例如 `kubectl get pods -o custom-columns`，则可以使用 Go 模板。

尝试以下代码：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | import ( |
|  |  |
|  | "os" |
|  |  |
|  | "text/template" |
|  |  |
|  | ) |
|  |  |
|  | tmpl := `Name: {{ .Name }} | Namespace: {{ .Namespace }}` |
|  |  |
|  | t := template.Must(template.New("pod").Parse(tmpl)) |
|  |  |
|  | for \_, pod := range podList.Items { |
|  |  |
|  | err := t.Execute(os.Stdout, pod.ObjectMeta) |
|  |  |
|  | if err != nil { |
|  |  |
|  | panic(err) |
|  |  |
|  | } |
|  |  |
|  | fmt.Println() |
|  |  |
|  | } |

这种方法使你可以完全控制打印的内容和方式。你还可以使用此技术来构建具有清晰、用户友好输出的脚本或工具。

## 错误处理、重试和退避策略

在 Go 中使用 Kubernetes 时，事情并非总是一帆风顺。网络中断、临时不可用或权限错误很常见。这就是为什么以优雅的方式处理错误并在需要时重试非常重要的原因。

重试可以帮助你的应用程序从瞬时问题中恢复，而退避策略可确保你不会通过过于激进的重试来使 [API](https://thenewstack.io/introduction-to-api-management/) 过载。

以下是一些简单而有效的策略，可以考虑：

* **检查和记录错误：** 始终检查 `err != nil` 并记录错误详细信息。这有助于调试。
* **使用指数退避：** 在重试之间等待更长的时间，以避免使系统不堪重负。诸如 `k8s.io/apimachinery/pkg/util/wait` 之类的库使这变得容易。
* **限制重试次数：** 不要永远重试。设置最大重试计数以避免挂起或卡住的进程。
* **仅在特定错误时重试：** 某些错误（例如 500 或超时）值得重试。其他错误（例如 403 或 404）通常不是。
* **使用上下文超时或取消：** 这可以防止你的代码重试太长时间，并使用户可以更好地控制请求计时。

|  |  |
| --- | --- |
| ✅ | Kubernetes Go 客户端包括内置的帮助程序，例如 wait.ExponentialBackoff()，用于重试逻辑。你也可以使用它们。 |

## 单元和集成测试

测试你的 Kubernetes 代码是避免在生产中出现意外情况的关键。Go 可以使用 Kubernetes 客户端库轻松编写单元测试和集成测试。

[单元测试](https://thenewstack.io/unit-tests-are-overrated-rethinking-testing-strategies/) 检查你的逻辑，而无需实际的集群。[集成测试](https://thenewstack.io/insights-on-integration-tests-with-foresight/) 针对真实（或模拟）的 Kubernetes 集群运行你的代码。以下是如何处理这两者。

### 用于单元测试的伪造客户端集

`client-go` 库提供了一个伪造客户端，你可以使用它来模拟 Kubernetes 交互。这使你可以在不需要实时集群的情况下测试你的代码。

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | import ( |
|  | "testing" |
|  | "k8s.io/client-go/kubernetes/fake" |
|  | metav1 "k8s.io/apimachinery/pkg/apis/meta/v1" |
|  | ) |
|  |  |
|  | func TestGetPods(t \*testing.T) { |
|  | client := fake.NewSimpleClientset() |
|  |  |
|  | \_, err := client.CoreV1().Pods("default").Create( |
|  | context.TODO(), |
|  | &v1.Pod{ |
|  | ObjectMeta: metav1.ObjectMeta{ |
|  | Name: "test-pod", |
|  | }, |
|  | }, |
|  | metav1.CreateOptions{}, |
|  | ) |
|  | if err != nil { |
|  | t.Fatal(err) |
|  | } |
|  |  |
|  | pods, err := client.CoreV1().Pods("default").List(context.TODO(), metav1.ListOptions{}) |
|  | if err != nil { |
|  | t.Fatal(err) |
|  | } |
|  |  |
|  | if len(pods.Items) != 1 { |
|  | t.Fatalf("Expected 1 pod, got %d", len(pods.Items)) |
|  | } |
|  | } |
|  |  |

### 基于 KinD 的集成测试

Kubernetes in Docker (KinD) 非常适合在本地运行真实的 Kubernetes 集群以进行集成测试。

使用 KinD，你可以：

* 在 CI 管道中或本地启动一个真实的集群。
* 端到端地部署和测试你的 Go 代码。
* 验证你的代码如何与真实的 Kubernetes 行为交互。

以下是如何进行：

* 使用 KinD 创建一个测试集群。

* 在该集群中运行你的应用程序或控制器。

* 使用 `client-go` 测试实际的资源行为。

* 在测试后拆除集群。

诸如 `envtest` 和 `controller-runtime` 之类的工具也有助于自定义控制器中的集成测试。

## 生产级 CLI 工具的 10 个最佳实践

如果你正在构建一个与 Kubernetes 交互的 CLI 工具，那么超越“可工作的代码”非常重要。你的工具应该是可靠的、用户友好的，并且可以用于实际使用。

以下是一些需要遵循的最佳实践：

1. **使用 CLI 框架，如 Cobra：** 这些框架有助于构建命令、添加帮助文本和干净地处理标志。
2. **验证用户输入：** 在执行命令之前，始终检查所需的标志、无效的值或缺少上下文。
3. **提供有用的错误消息：** 确保错误输出清晰且可操作。避免神秘的堆栈跟踪。
4. **支持多个 kubeconfig 上下文：** 如果用户使用多个集群，则允许用户指定一个 `--kubeconfig` 文件或 `--context`。
5. **打印进度和状态：** 向用户显示工具正在执行的操作（例如，“正在创建 Deployment…”）。这有助于透明度和信任。
6. **尊重 [Kubernetes RBAC](https://thenewstack.io/kubernetes-rbac-permissions-you-might-not-know-about-but-should/)：** 不要假设用户具有完全访问权限。捕获权限错误并解释缺少的内容。
7. **优雅地处理超时和取消：** 支持 `--timeout` 标志和 `Ctrl+C`，以便用户可以干净地退出。
8. **包括日志记录和调试模式：** 允许 `--verbose` 或 `--debug` 标志，以便在故障排除期间获得更深入的了解。
9. **使用结构化输出选项：** 支持诸如 `--output=json` 或 `--output=yaml` 之类的标志，以进行脚本编写和自动化。
10. **编写单元和集成测试：** 测试你的 CLI 逻辑和 Kubernetes 交互，以避免回归。

遵循这些最佳实践可以将一个简单的脚本变成一个强大的工具，你的团队或社区可以依赖它。

## 在 Go 中运行 Kubernetes 命令：结论

Go 非常适合 [Kubernetes 自动化](https://thenewstack.io/automation-can-solve-resource-overprovisioning-in-kubernetes/)。使用官方客户端库，你可以直接与集群交互，构建可靠的 CLI 工具，并以编程方式处理复杂的任务 —— 同时保持快速和高效。

无论你是管理资源、构建自定义控制器还是编写内部工具，掌握这些模式都将帮助你在 Go 中创建更强大和生产就绪的 Kubernetes 应用程序。

[学习 Go](https://thenewstack.io/learn-the-go-programming-language-start-here/) 以完全控制你的 Kubernetes 工作流程，并构建可随你的基础架构扩展的工具。