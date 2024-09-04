如今，看到云原生行业如此蓬勃发展和充满活力，令人兴奋。CNCF Sandbox 在其中发挥着重要作用，为开源项目在生态系统中起步或继续发展提供了一个独特的平台。同时，那里涌现出如此多的新事物，让人难以跟上。

因此，我们想开始这个系列文章，介绍最近加入 CNCF Sandbox 的项目。我们的第一批文章将涵盖 2023 年上半年（3 月 8 日、5 月 17 日和 6 月 22 日）加入 Sandbox 的 13 个项目。我们将按其正式类别列出它们，从最受欢迎的类别开始。

我们将为所有项目的描述提供额外的信息和链接，包括其原始作者以及 Sandbox 提交和入职流程的 GitHub 问题。这将帮助您更深入地了解项目的路径以及加入 CNCF 的正式流程。

## 可观测性
### 1. Inspektor Gadget
[网站](https://inspektor-gadget.io/);[GitHub](https://github.com/inspektor-gadget/inspektor-gadget)- 2100+ GH 星星，~50 位贡献者
- 首次提交：2019 年 3 月 3 日
- 许可证：Apache 2.0
- 原始所有者/创建者：Kinvolk（2021 年被微软收购）
- 语言：C、Go
- CNCF Sandbox：
[沙盒请求](https://github.com/cncf/sandbox/issues/7);[入职问题](https://github.com/cncf/toc/issues/1021);[DevStats](https://inspektorgadget.devstats.cncf.io/)
Inspektor Gadget 是一组基于 eBPF 的工具（称为“小工具”），用于调试 Kubernetes 中的应用程序和资源。

这些小工具打包、部署和执行 eBPF 程序，包括那些基于 [BCC](https://github.com/iovisor/bcc) 工具的程序，在集群中。它们还自动将低级内核原语映射到高级 Kubernetes 资源，简化并加速基本信息检索。

Inspektor Gadget 在每个 K8s 节点上作为 *DaemonSet* 运行。它利用嵌入内核的 eBPF 程序来监控与 Pod 中用户空间程序的系统调用相关的事件。eBPF 程序在内核中运行以收集日志数据，然后 Inspektor Gadget 的用户空间工具检索和显示这些数据。

以下是一些内置小工具的示例：

[advise network-policy](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/advise/network-policy)监控命名空间中的网络活动，并将 TCP 和 UDP 流量信息汇总到一个文件中，该文件可用于生成 Kubernetes 网络策略；[advise seccomp-profile](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/advise/seccomp-profile)监视在选定 Pod 中执行的系统调用，并根据这些调用创建相应的 seccomp 配置文件；[profile block-](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/profile/block-io)[io](https://github.com/inspektor-gadget/inspektor-gadget/blob/main/docs/builtin-gadgets/profile/block-io.md)收集有关磁盘输入/输出使用情况的信息，并创建一个 I/O 延迟分布直方图；[profile cpu](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/profile/cpu)通过采样堆栈跟踪来分析 CPU 性能；[top tcp](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/top/tcp)可视化正在进行的 TCP 活动；[trace dns](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/trace/dns)输出选定 Pod 的 DNS 查询和响应；[trace exec](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/trace/exec)显示新进程是如何创建的；[trace fsslower](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/trace/fsslower)识别并显示性能较差的文件操作；[trace oomkill](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/trace/oomkill)监控 OOM（内存不足）杀手操作；[trace ssl](https://www.inspektor-gadget.io/docs/latest/gadgets/trace_ssl)记录 OpenSSL 函数的使用情况；[traceloop](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/traceloop)记录容器中执行的系统调用。
完整的工具列表可在 [文档](https://www.inspektor-gadget.io/docs/latest/gadgets/) 和 [Artifacts Hub](https://artifacthub.io/packages/search?kind=22) 中找到。

在集群中安装 Inspektor Gadget 后，可以使用以下命令列出其所有组件：

```
$ kubectl gadget --help
Collection of gadgets for Kubernetes developers
Usage:
kubectl-gadget [command]
Available Commands:
advise Recommend system configurations based on collected information
audit Audit a subsystem
completion Generate the autocompletion script for the specified shell
deploy Deploy Inspektor Gadget on the cluster
help Help about any command
profile Profile different subsystems
prometheus Expose metrics using prometheus
run Run a gadget (experimental)
script Run a bpftrace-compatible scripts
snapshot Take a snapshot of a subsystem and print it
sync Synchronize gadget information with server
```
根据给定条件收集、排序和定期报告事件
跟踪并打印系统事件
从过去获取容器的类似 strace 的日志
从集群中取消部署 Inspektor Gadget
显示版本
…

该项目的 README 提供了 [一个不错的列表](https://github.com/inspektor-gadget/inspektor-gadget#talks)，您可以在其中了解 Inspektor Gadget 和其他 eBPF 相关技术的实际应用。

### 2. Headlamp
[网站](https://headlamp.dev/);[GitHub](https://github.com/headlamp-k8s/headlamp)- 约 2000 个 GH 星星，约 60 位贡献者
- 首次提交：2019 年 12 月 19 日
- 许可证：Apache 2.0
- 原始所有者/创建者：Kinvolk（2021 年被微软收购）
- 语言：TypeScript（React）、Go
- CNCF 沙箱：
[沙箱请求](https://github.com/cncf/sandbox/issues/25);[入职问题](https://github.com/cncf/toc/issues/1056);[DevStats](https://headlamp.devstats.cncf.io/)
Headlamp 是一个功能强大的 Kubernetes 用户界面。您可以将其作为本地桌面应用程序运行，也可以将其部署到 Kubernetes 集群中，并通过 Web 浏览器访问它。

Headlamp 允许您查看 K8s 集群的整体状态和资源使用情况，滚动浏览您的 K8s 资源并修改其清单，查看日志，并执行到容器中。

![](https://blog.palark.com/wp-content/uploads/2024/08/headlamp-workloads-list-1024x617.png)
从安全角度来看，它尊重 RBAC 用户角色，以防止未经授权的操作。它还允许您撤消修改操作。

Headlamp 提供了一个强大的插件系统，用于扩展和自定义其功能。官方插件可在 [此仓库](https://github.com/headlamp-k8s/plugins) 中找到。目前，它们有三个：*app-catalog* 用于管理 Helm 图表，*prometheus* 用于提供有关工作负载的详细信息，以及 *kompose* 用于将您的 `docker-compose` 清单转换为工具。Artifact Hub 还托管了 [OpenCost 的插件](https://artifacthub.io/packages/headlamp/headlamp-plugins/headlamp_opencost)。

### 3. Kepler
[网站](https://sustainable-computing.io/);[GitHub](https://github.com/sustainable-computing-io/kepler)- 约 1100 个 GH 星星，50 多位贡献者
- 首次提交：2022 年 2 月 2 日
- 许可证：Apache 2.0
- 原始所有者/创建者：Red Hat
- 语言：Go、C
- CNCF 沙箱：
[沙箱请求](https://github.com/cncf/sandbox/issues/19);[入职问题](https://github.com/cncf/toc/issues/1054);[DevStats](https://kepler.devstats.cncf.io/)
Kepler（**K**ubernetes-based **E**fficient **P**ower **L**evel **E**xporte**r**）是一个 Prometheus 导出器，它利用 eBPF 探测与能耗相关的系统统计信息，例如 CPU 性能计数器。它从 *cgroupfs* 和 *sysfs* 收集数据和统计信息，并使用 ML（机器学习）模型来估计 Kubernetes 消耗的能量。

Kepler 将所有这些指标导出到您的 Kubernetes Pod 和节点的 Prometheus。它们包括：

`kepler_container_joules_total`
— 特定容器的 CPU、DRAM、GPU 和其他主机组件的总能耗；`kepler_container_core_joules_total`
和`kepler_container_gpu_joules_total`
— 容器的 CPU 内核/GPU 的总能耗；`kepler_container_cpu_cycles_total`
— 容器通过硬件计数器使用的 CPU 周期；`kepler_node_core_joules_total`
— 与相关容器指标相同，但针对节点上的所有容器进行聚合；- 等等。
您可以在 [文档](https://sustainable-computing.io/design/metrics/#kepler-metrics-overview) 中找到 Kepler 公开的指标的完整列表。

这是一个关于 Kepler 工作原理的优秀图表：

![](https://blog.palark.com/wp-content/uploads/2024/08/kepler-architecture-1024x505.png)
您可以使用其 [Helm 图表](https://github.com/sustainable-computing-io/kepler-helm-chart) 或 [Kubernetes 运算符](https://github.com/sustainable-computing-io/kepler-operator) 在您的集群中安装 Kepler。完成后，您可以利用预生成的 Kepler 仪表板在 Grafana 中可视化您的与能量相关的 Kubernetes 指标。

## 安全与合规性
### 4. SlimToolkit
[网站](https://slimtoolkit.org/);[GitHub](https://github.com/slimtoolkit/slim)- 19000 多个 GH 星星，60 多位贡献者
- 首次提交：2015 年 9 月 10 日
- 许可证：Apache 2.0
- 原始所有者/创建者：Kyle “kcq” Quest
- 语言：Go
- CNCF 沙箱：
[沙箱请求](https://github.com/cncf/sandbox/issues/22);[入职问题](https://github.com/cncf/toc/issues/1055);[DevStats](https://slimtoolkit.devstats.cncf.io/)
SlimToolkit（最初称为 *DockerSlim*）是您优化、探索和调试容器的首选工具。它简化了容器的创建、定制和使用方式，使它们更小、更安全、更高效。
SlimToolkit 与 Elixir、Go、Java、Node.js、PHP、Python、Ruby 和 Rust 应用程序在 Alpine、CentOS、Debian、Ubuntu 以及无发行版容器上无缝协作。顾名思义，最初的想法是让容器更精简。为了实现这一点，在完全自动化的方式下执行了几个操作：

![](https://blog.palark.com/wp-content/uploads/2024/08/slimtoolkit-workflow.jpg)

以这种方式处理容器会导致 Node.js 应用程序镜像缩小 30 倍（对于 `ubuntu:14.04`）和 16 倍（对于 `debian:jessie`）。Go 应用程序承诺的缩减幅度更加令人印象深刻，因为基于 `golang:latest` 的 700 MB 镜像可以缩小到只有 1.5 MB（！） 。该项目有一个专门的 [示例](https://github.com/slimtoolkit/examples) 存储库，您可以在其中找到各种应用程序以及 SlimToolkit 如何减小其镜像的大小。

由于它是一个 *工具包*，`slim` 附带了许多您可以对容器执行的命令，例如：

`xray` — 对镜像进行静态分析；`lint` — 分析 Dockerfile 中的容器指令；`vulnerability` — 基于 EPSS（漏洞预测评分系统）信息的漏洞相关操作；`registry` — 仓库相关操作；- 等等。

SlimToolkit 还提供交互模式，为每个命令或标志提供提示，以及与 CI/CD（基于 Jenkins 或 GitHub Actions）的即用型集成。

### 5. SOPS
[网站](https://getsops.io/);[GitHub](https://github.com/getsops/sops)- 16000+ GH 星星，140+ 贡献者
- 首次提交：2015 年 8 月 14 日
- 许可证：MPL 2.0
- 原作者/创建者：Mozilla
- 语言：Go
- CNCF 沙箱：
[沙箱请求](https://github.com/cncf/sandbox/issues/28);[入职问题](https://github.com/cncf/toc/issues/1057);[DevStats](https://sops.devstats.cncf.io/)

SOPS（**S**ecrets **OP**eration**S**）是一个著名的加密文件编辑器，最初由 Mozilla 于 2015 年创建。它可以帮助您自动加密机密和基础设施凭据及其分发。它支持多种格式（YAML、JSON、ENV、INI 和二进制文件），并使用 Hashicorp Vault、AWS KMS、GCP KMS、Azure Key Vault、`age` 和 PGP 进行加密。

它还能够进行密钥轮换，并为各种用例提供众多功能，例如：

- 将机密写入标准输出、磁盘上的文件、子进程的环境以及临时文件；
- 密钥组 - 多个主密钥来解密文件；
- 密钥服务 - 转发套接字以访问远程机器上的加密密钥；
- 生成审计日志以分析加密文件的所有活动。

SOPS 与 Git 无缝集成，允许您在比较不同版本时解密文件。这对于查看更改或可视化历史记录特别有用。

顺便说一下，有一个著名的 [helm-secrets](https://github.com/jkroepke/helm-secrets) Helm 插件，允许您使用 SOPS 加密 Helm 值文件并将它们存储在 Git 中。

## 调度和编排
### 6. Clusternet
[网站](https://clusternet.io/);[GitHub](https://github.com/clusternet/clusternet)- 1300+ GH 星星，约 50 位贡献者
- 首次提交：2021 年 6 月 10 日
- 许可证：Apache 2
- 原作者/创建者：腾讯
- 语言：Go
- CNCF 沙箱：
[沙箱请求](https://github.com/cncf/sandbox/issues/10);[入职问题](https://github.com/cncf/toc/issues/1022);[DevStats](https://clusternet.devstats.cncf.io/)

Clusternet 简化了对多个 Kubernetes 集群的访问和管理，为各种环境提供统一的方法：本地、公有云或私有云、混合云和边缘。

部署 Clusternet 后，您可以通过简单的 `kubectl` 命令对 Kubernetes 集群执行各种操作（例如，列出/创建/删除资源、进行端口转发等），并在它们之间部署应用程序。它可以自动发现、注册和标记新的集群。

从技术上讲，Clusternet 使用一组组件（中心、调度程序和控制器管理器）扩展了 Kubernetes，用于父集群和子集群中的代理。这些子集群通过对父集群 API 服务器的请求进行管理，为操作人员创建了一个无缝流程。

![](https://blog.palark.com/wp-content/uploads/2024/08/clusternet-architecture-1024x568.png)

该项目有一个 [快速入门](https://clusternet.io/docs/quick-start/) 用于在本地设置 Clusternet（使用 `kind`），之后可以遵循其他教程，指导您将应用程序部署到多个 K8s 集群。

### 7. Eraser
[网站](https://eraser-dev.github.io/eraser/docs/);[GitHub](https://github.com/eraser-dev/eraser)- 约 500 个 GH 星星，30 多位贡献者
- 首次提交：2021 年 6 月 1 日
- 许可证：Apache 2
- 原作者/创建者：微软（Azure）
- 语言：Go
- CNCF 沙箱：
[沙箱请求](https://github.com/cncf/sandbox/issues/24);[入职问题](https://github.com/cncf/toc/issues/1092);[DevStats](https://eraser.devstats.cncf.io/)
Eraser 的使命很简单——通过从所有集群节点中删除未使用的和存在漏洞的镜像来防止 Kubernetes 节点的磁盘变得混乱。

虽然 Kubernetes 拥有自己的 [垃圾回收](https://kubernetes.io/docs/concepts/architecture/garbage-collection/#containers-images) 机制，但 Eraser 为您提供了更多选择来选择要删除的镜像，包括其漏洞状态。*(如果您也想知道为什么它不应该成为 Kubernetes 的一部分，您可以在此处找到答案。)*

默认情况下，Eraser 会定期启动清理，并根据 Trivy 或自定义扫描程序执行的漏洞扫描结果删除镜像。您可以选择要执行哪些安全检查以及哪些漏洞在您的集群中是不可接受的。您也可以选择禁用漏洞扫描，在这种情况下，Eraser 将充当常规的垃圾收集器。

以下是一个很好的图表，展示了 Eraser 在自动模式下的工作原理：

![](https://blog.palark.com/wp-content/uploads/2024/08/eraser-automated-workflow.png)
您也可以通过指定要删除的镜像，使用 Eraser 手动删除镜像。

## 持续集成与交付
### 8. PipeCD
[网站](https://pipecd.dev/);[GitHub](https://github.com/pipe-cd/pipecd)- 1000+ GH 星星，~90 位贡献者
- 首次提交：2020 年 6 月 12 日
- 许可证：Apache 2
- 原作者/创建者：CyberAgent, Inc.
- 语言：Go
- CNCF 沙盒：
[沙盒请求](https://github.com/cncf/sandbox/issues/12);[入职问题](https://github.com/cncf/toc/issues/1053);[DevStats](https://pipecd.devstats.cncf.io/)
PipeCD 是一个基于 GitOps 的平台，用于跨不同环境进行一致的部署。这意味着它不仅允许您部署到 Kubernetes，还可以部署到另外四个目标：Terraform、GCP CloudRun、AWS Lambda 和 AWS ECS。

要使用 PipeCD，您需要通过将其提交到 Git 存储库来定义您的应用程序（资源和配置），在 PipeCD 中“注册”它（例如，指定其平台提供商），并在需要时自定义其管道。完成后，PipeCD 将开始根据 GitOps 拉取式方法交付此应用程序及其更改。

PipeCD 与 CI 工具无缝集成，并提供自动部署分析、回滚机制和配置漂移检测。您可以在多云环境中使用它，在多集群和多租户设置中使用它。

![](https://blog.palark.com/wp-content/uploads/2024/08/pipecd-automatic-rollback-1024x465.png)
它还支持基本的安全功能（例如单点登录、RBAC 和内置的秘密管理），并通过部署管道 UI 和实时应用程序状态可视化提供了极佳的可视性。

该项目的 [快速入门](https://pipecd.dev/docs-dev/quickstart/) 说明了如何在 Kubernetes 上开始使用 PipeCD。总的来说，其文档非常全面，涵盖了该工具提供的丰富功能集。

## 应用程序定义和镜像构建
### 9. Microcks
[网站](https://microcks.io/);[GitHub](https://github.com/microcks/microcks)- 1300+ GH 星星，~50 位贡献者
- 首次提交：2015 年 2 月 23 日
- 许可证：Apache 2
- 原作者/创建者：Laurent Broudoux（后来由 Postman, Inc. 赞助）
- 语言：Java、TypeScript（Angular）
- CNCF 沙盒：
[沙盒请求](https://github.com/cncf/sandbox/issues/37);[入职问题](https://github.com/cncf/toc/issues/1096);[DevStats](https://microcks.devstats.cncf.io/)
Microcks 是一款用于 API 测试的云原生工具，允许您轻松创建实时模拟。它支持各种格式和规范，包括 SoapUI 项目 (XML) 5.1+、Postman 集合 (JSON) 1.0/2.x、Apicurio (Studio) OpenAPI 3.x、OpenAPI (YAML、JSON) 2.x/3.x、gRPC (protobuf) 3.x 和 GraphQL (schema IDL)。

Microcks 将吸收您现有的工件——即您支持的格式中的 API 规范、模式、集合和项目——来构建其知识库。基于此基础，它会生成：

- 立即在特定端点上可用的模拟，供您的消费者使用（甚至不知道这是一个假的 API）；
- 可以验证您的实际 API 实现是否符合预期（如工件中所述）的测试。
Microcks 允许吸收多个工件以获得更好的结果。例如，主要工件（基于 OpenAPI）将为您的服务和操作提供主要元数据。次要工件（Postman 集合）将使用其他请求、响应和事件样本来丰富现有操作。

您可以使用干净的 Web UI 管理 Microcks。例如，在导入所有工件后，您可以看到由该工具控制的 API 和服务，只需单击一下即可启动测试，浏览每个资源的详细测试结果等。

![](https://blog.palark.com/wp-content/uploads/2024/08/microcks-api-testing-ui-1024x637.png)
Microcks 可以作为操作符或使用 Helm 图表安装在 Kubernetes 集群中。或者，您可以使用 Docker Compose、`kind` 或 Minikube 在本地部署它。该项目的 [大量文档](https://microcks.io/documentation/) 包含将 Microcks 与 CI/CD（GitHub Actions、Jenkins、GitLab CI/CD 和 Tekton）以及其他工具（如 Postman 工作区和 Backstage）集成的示例（尽管后者仍在进行中）。

## 自动化和配置
### 10. kpt
[网站](https://kpt.dev/);[GitHub](https://github.com/kptdev/kpt)- 约 1700 个 GH 星星，100 多位贡献者
- 首次提交：2019 年 9 月 17 日
- 许可证：Apache 2
- 原始所有者/创建者：Google
- 语言：Go
- CNCF 沙盒：
[沙盒请求](https://github.com/cncf/sandbox/issues/34);[入职问题](https://github.com/cncf/toc/issues/1095);[DevStats](https://kpt.devstats.cncf.io/)
kpt 是一套全面的工具，旨在以 WYSIWYG *(所见即所得)* 方式为 Kubernetes 和相关基础设施创建、自动化和交付配置。

大多数 K8s 用户使用命令行工具 (`kubectl`)、GUI 和直接与 Kubernetes API 交互的自动化工具（如 K8s 操作符）或声明式自定义工具（如 Helm、Terraform、[cdk8s](https://blog.palark.com/cdk8s-framework-for-kubernetes-manifests/) 等）来管理其资源。通过允许用户通过 WYSIWYG 管理配置，kpt 使此过程更加方便。

声明式 *配置即数据* 方法是 kpt 的核心。它将配置数据视为真相来源，并将其与实时（实际）状态分开存储。它依赖于统一的数据模型来表示配置，并将配置结构和存储从任何配置数据操作中抽象出来。为了实现这一点，kpt 执行配置转换，类似于 Kustomize，但将其 *就地* 呈现，而不是 *异地* 呈现。

kpt 允许您通过 GitOps 或直接应用部署配置。它附带一个包含可立即使用的函数和 SDK 的目录，用于创建新的函数（在 Go、Typescript 和 Starlark 中）。它还支持打包配置，甚至有一个专门的包编排器（称为 [Porch](https://github.com/nephio-project/porch)）来处理它们。

最后，kpt 还有一个实验性的 [Backstage 插件](https://github.com/GoogleContainerTools/kpt-backstage-plugins)：

![](https://blog.palark.com/wp-content/uploads/2024/09/kpt-backstage-plugin-1024x399.png)
您还可以 [结合](https://github.com/kptdev/kpt/tree/main/package-examples/kustomize) 使用 kpt 和 kustomize，前者用于打包，后者用于自定义。

## 协调和服务发现
### 11. Xline
[网站](https://xline.cloud/);[GitHub](https://github.com/xline-kv/Xline)- 约 600 个 GH 星星，20 多位贡献者
- 首次提交：2022 年 5 月 5 日
- 许可证：Apache 2
- 原始所有者/创建者：DatenLord Technology
- 语言：Rust
- CNCF 沙盒：
[沙盒](https://github.com/cncf/sandbox/issues/31)[请求](https://github.com/cncf/sandbox/issues/11);[入职](https://github.com/cncf/toc/issues/1105)[问题](https://github.com/cncf/toc/issues/1093);[DevStats](https://xline.devstats.cncf.io/)
Xline 是一款高性能分布式键值 (KV) 存储，用于管理跨多个集群的元数据。

此云原生解决方案支持地理分布式部署，并依赖于 CURP 共识协议，即使在全球网络环境中也能提供高性能和一致性。您可以在 [项目的博客](https://datenlord.github.io/xline-home/#/deep-dive/Consensus) 中详细了解 CURP，并了解它与其他共识协议（如 etcd 中使用的 Raft）的比较。

![Xline 架构](https://blog.palark.com/wp-content/uploads/2024/09/xline-architecture.png)
Xline 提供了一套全面的 KV 接口，与 etcd API 完全兼容。此外，它被宣传为现有 etcd 用户无缝迁移的基础，在地理分布式、多集群环境中提供更好的性能和高级功能（用于处理索引、权限和配置）。

您可以按照 [此快速入门](https://github.com/xline-kv/Xline/blob/master/doc/QUICK_START.md) 手动安装 Xline（有趣的是，`etcdctl` 在这里用于发送基本请求）或利用 [xline-operator](https://github.com/xline-kv/xline-operator)。

## 云原生存储
### 12. HwameiStor
[网站](https://hwameistor.io/);[GitHub](https://github.com/hwameistor/hwameistor)- 500 多个 GH 星星，40 多位贡献者
- 首次提交：2022 年 3 月 7 日
- 许可证：Apache 2
- 原始所有者/创建者：DaoCloud
- 语言：Go
- CNCF 沙盒：
[沙盒请求](https://github.com/cncf/sandbox/issues/29);[入职问题](https://github.com/cncf/toc/issues/1094);[DevStats](https://hwameistor.devstats.cncf.io/)
HwameiStor is a flexible local storage system designed for cloud-native stateful workloads in Kubernetes. It:

- Creates a centralized pool of local resources for managing various types of disks;
- Leverages CSI (Container Storage Interface) to provide local volumes for distributed services, offering persistent storage for stateful applications.

By doing so, it aims to be a lightweight and cost-effective alternative to expensive SAN-class storage.

*Note. If you are interested in running stateful applications in Kubernetes, you might like our recent article, "Stateful Applications in Kubernetes. From History and Fundamentals to Operators".*

HwameiStor supports HDD, SSD, and NVMe, and automates the discovery, allocation, and management of disks.

![](https://blog.palark.com/wp-content/uploads/2024/09/hwameistor-architecture-1024x403.png)

This solution comes with:

- Disk state monitoring and auditing for all resources (CRDs);
- LVM volume snapshotting/restoring and automatic resizing;
- Affinity-based scheduling;
- High availability (HA) mode based on DRBD, achieving data synchronization through cross-node replication;
- Web-based GUI.

The recommended way to install HwameiStor is using [its operator](https://hwameistor.io/docs/install/operator).

## Platforms/Certifications Kubernetes - Installers
### 13. KubeClipper
[Website](https://kubeclipper.io/en/);[GitHub](https://github.com/kubeclipper/kubeclipper)- ~300 GH stars, ~20 contributors
- First commit: July 2, 2022
- License: Apache 2
- Original owner/creator: 99Cloud
- Language: Go
- CNCF Sandbox:
[Sandbox request](https://github.com/cncf/sandbox/issues/31);[Incubation issue](https://github.com/cncf/toc/issues/1105);[DevStats](https://kubeclipper.devstats.cncf.io/)

KubeClipper is a web service that implements a user-friendly GUI, API, and CLI tools for managing Kubernetes clusters. The project covers the entire cluster lifecycle and various settings, with an ambitious goal to help operators "manage Kubernetes in the most lightweight and convenient way".

In particular, KubeClipper helps with:

- Cluster installation/uninstallation, upgrade, scaling, backup/restore, and remote access;
- Deploying clusters on any infrastructure: cloud, VM, and bare metal;
- Automatic registration of new cluster nodes;
- Access management: RBAC-based permissions, OIDC integration.

Furthermore, the project roadmap includes going further in providing application lifecycle management and integrating a large number of plugins for load balancers and ingress, monitoring, Kubernetes dashboards, etc.

Technically, KubeClipper consists of four main components: `kc-agent` (deployed on K8s nodes), `kc-server` (collecting information from agents), `kc-etcd` (backend database for *kc-server*), and `kcctl` (a CLI tool for managing clusters).

You can install KubeClipper by entering login and password credentials or SSH keys via `kcctl`. Once installed, you can manage your setup through the web interface or CLI tools.

![](https://blog.palark.com/wp-content/uploads/2024/09/kubeclipper-create-cluster-1024x608.png)

The project's [documentation](https://kubeclipper.io/en/docs/tutorials/) includes tutorials on creating new Kubernetes clusters and connecting existing ones, managing clusters and their nodes, and controlling access.

## Epilogue

Based on these new CNCF projects, we can see that most projects are written in Go, released under the Apache 2.0 license, and come from large companies. However, not all projects are like that. What's more interesting is *when* they decided to enter the sandbox:

- Most projects are 2-3 years old;
- Four projects are very new (born a year or even less before applying): Kepler, HwameiStor, Xline, and KubeClipper;
- Three projects are over 7 years old (!) (started in 2015): Microcks, SlimToolkit, and SOPS.

The latter clearly shows that even mature software is looking for a reliable, vendor-neutral home.

It will be interesting to see how these projects evolve under the guidance of the CNCF. Which of them will gain more community attention and boost their development? Feel free to share your experience using any of these 13 CNCF projects!

## Comments