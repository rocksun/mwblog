<!--
# 什么是基础设施即代码扫描？
https://cdn.thenewstack.io/media/2023/09/3ed59a41-finger-2081169_1280-1-1024x576.jpg
Image by ar130405 from Pixabay.
-->

如果支配你的 IaC 工作流程的代码是不安全的，IaC 很快就会成为安全风险的来源。使用 IaC 扫描仪可以减轻这种危险。

译自 [What Is Infrastructure as Code Scanning?](https://thenewstack.io/what-is-infrastructure-as-code-scanning/) 。

基础设施即代码，简称 IaC，往往能同时激发 [DevOps](https://orca.security/resources/blog/devops-security/) 团队和安全团队的兴趣。对于 DevOps 来说，IaC 提供了一种自动化和扩展原本需要大量手动完成的流程的方法。从安全角度来看， IaC 提供了减少工程师由于手动配置疏忽或错误而向 IT 环境中引入安全风险的好处。

也就是说，只有当你的 IaC 代码本身是安全的，IaC 才能使 IT 环境更加安全。如果在使用代码之前没有识别出 IaC 代码中的问题，这些问题很容易成为你安全策略中最薄弱的环节。

这就是为什么拥有 [IaC 扫描策略](https://orca.security/resources/blog/how-orca-secures-infrastructure-as-code-iac/)对于确保开发人员、DevOps 工程师以及任何其他利用 IaC 的人都能在不损害安全优先事项的情况下这样做至关重要。继续阅读以了解为什么 IaC 扫描很重要，它的工作原理以及如何充分利用它。

## 基础设施即代码(IaC)是什么？

IaC 是使用代码来管理 IT 基础设施供应和配置的方法。在使用 IaC 时，您编写定义希望资源如何供应的代码。然后，您使用 IaC 平台(例如 Terraform 或 Ansible，只举几个流行的 IaC 工具的名字)自动将该配置应用于您指定的资源。

通过这种方式，IaC 为工程师省去了大量时间，因为它允许他们自动将相同的配置应用于尽可能多的资源。IaC 还减少了如果工程师逐台手动设置每个资源并在某些实例中意外应用了错误设置而可能发生的配置错误的风险。

## 什么是 IaC 扫描？

IaC 扫描是使用自动化工具来验证 IaC 配置文件。换句话说，在执行 IaC 扫描时，您扫描定义希望资源如何配置的 IaC 代码。IaC 扫描器可以检测代码中存在的潜在错误或安全问题。

IaC 扫描与代码向左移的概念相辅相成，这意味着尽可能早地在软件交付生命周期中执行安全检查。使用 IaC 扫描，您可以在应用配置之前轻松验证计划的配置是否安全。通过这种方式，您可以在软件交付过程的更早阶段检测到安全风险，而不是在配置部署之后。

## 为什么 IaC 扫描很重要？

IaC 扫描很重要，因为 IaC 代码中存在的错误或疏忽会在将代码应用于资源时重复出现。通过在应用代码之前扫描 IaC 代码，您可以在问题影响实时资源之前捕获并解析问题。

举个例子，思考一下如何使用 IaC 扫描使组织受益，假设您编写了以下 IaC 代码使用 Terraform 部署容器化应用程序：

```t
resource "docker_container" "my_container" {

  name = "my_container"
  image = "my_image"
  command = "bash"
  privileged = true
  user = "root"
}
```

该代码配置一个以 root 用户身份在特权模式下运行的容器。Terraform 不会阻止您以这种方式运行容器，但这样做存在安全风险。如果您的容器以 root 身份运行，入侵者如果设法接管容器，可以更轻松地将攻击升级为接管主机操作系统以及系统上运行的任何其他容器。

因此，大多数 IaC 扫描器会标记此配置并警告您可能的危险。然后，您可以修改代码，以便在基于此代码部署容器时不以特权模式运行它们。

IaC 扫描还可以帮助检测配置错误，例如错误配置的文件路径或用户参数，这可能会导致资源无法正常运行。然而，IaC 扫描的主要好处是它有助于防范安全风险。

## 选择 IaC 扫描解决方案的最佳实践

当今市场上有许多 IaC 扫描器。在从各种选择中进行选择时，请寻找具有以下功能的 IaC 扫描工具：

* **广泛的 IaC 框架支持**：理想情况下，您的 IaC 扫描器将能够验证为任何 IaC 框架编写的 IaC 代码 —— Terraform、Ansible、CloudFormation 等，而不仅仅支持一种或两种类型的 IaC 框架。
* **CI/CD 集成**：最高效的 IaC 扫描器与 CI/CD 工具集成，以便扫描成为软件交付过程中不可或缺的一部分。
* **全面风险检测**：IaC 代码中可能存在的错误形式各不相同。最好的 IaC 扫描器能够检测到广泛的问题 —— 从易受攻击的依赖项到访问控制错误配置，以及可能导致安全策略无法正确应用的输入错误等等。
* **风险优先级** — 不是所有的 [IaC 安全风险](https://orca.security/resources/blog/infrastructure-as-code-common-risks/)都具有相同的严重性。一个好的 IaC 扫描器会评估它发现的每个风险，并突出显示那些构成最大威胁的风险，以便您知道首先应该解决哪些风险。

## 结论：负责任地使用 IaC

IaC 是一种强大的工具，可以加速和扩展复杂的 IT 过程，同时避免由手动配置疏忽引发的安全问题。

然而，如果支配您的 IaC 工作流程的代码不安全，IaC 很快就会成为安全风险的来源，而不是减轻它们的方式。通过在 [CI/CD 过程](https://orca.security/resources/blog/secure-cicd-services/)中部署 IaC 扫描器并利用扫描来推动代码向左移，降低这种挑战。

想了解更多如何保护云基础设施并提高整体安全态势的信息吗？

[Orca Security](https://orca.security/?utm_content=inline-mention) 通过将 IaC 扫描整合到 CI/CD 过程的早期，提供了一种代码[向左移动的安全方法](https://orca.security/platform/shift-left-security/)。Orca 云安全平台为您的云环境中漏洞、配置错误和合规性问题提供了全面解决方案，提供您的风险态势的全面视图。通过识别并尽早在开发周期中缓解安全风险，Orca Security 帮助您实现代码向左移安全并降低云基础设施的整体风险。

[请求演示](https://orca.security/demo/)或[注册免费云风险评估](https://orca.security/lp/cloud-security-risk-assessment/)，以了解 Orca Security 如何帮助您保护云基础架构并提高整体安全性。
