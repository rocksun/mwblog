<!--
# 容器安全与安全运行环境的重要性
https://cdn.thenewstack.io/media/2023/10/93993955-secure-containers-1-1024x576.jpg
Image by Trac Vu on Unsplash.

-->

了解容器运行环境的工作机制，缘何若攻击者突破容器的限制，过度耦合的运行环境可能造成主机被接管，以及gVisor和Kata Containers等安全容器运行环境的好处。

译自 [Container Security and the Importance of Secure Runtimes](https://thenewstack.io/container-security-and-the-importance-of-secure-runtimes/) 。

[容器](https://thenewstack.io/containers/)已经彻底改变了我们开发和部署应用程序的方式，它为应用程序及其依赖提供了轻量级和可移植的运行环境。但是我们如何保证容器的安全呢？

我们需要关注的一个关键方面是容器运行时，这是用于启动和管理容器的软件。

尽管像[Docker](https://www.docker.com/?utm_content=inline-mention)和[containerd](https://containerd.io/)这样的容器运行时广为使用，但它们与宿主机操作系统高度耦合可能带来风险。本文我们将深入探讨容器运行时的工作原理，解释为什么高耦合的运行时可能导致容器逃逸后攻击者接管宿主机的风险，以及使用像[gVisor](https://thenewstack.io/how-to-implement-secure-containers-using-googles-gvisor/)和[Kata Containers](https://thenewstack.io/the-road-to-kata-containers-2-0/)等安全容器运行时的重要性。

## 理解容器运行时

容器运行时用于协调容器，管理它们的生命周期，并将容器与宿主机和其他容器隔离开来。通过利用Linux内核的命名空间和cgroup等特性，运行时为容器建立安全边界。

然而，传统运行时与宿主机内核高度耦合，这带来潜在的安全漏洞。如果攻击者设法逃逸出容器，他们可以未经授权访问基础宿主机操作系统，危及整个系统的安全。

高耦合的容器运行时继承了宿主机操作系统的安全态势和攻击面。运行时或宿主机内核中的任何漏洞都可能成为攻击者的潜在入口。

这种风险在多租户环境或运行不可信 workload 时尤为关键。为了降低这种威胁，使用像gVisor和Kata Containers等安全容器运行时至关重要。

这些安全运行时提供额外的隔离和安全层。它们采用创新技术来增强容器化workload的安全性。

例如，gVisor使用用户空间内核实现，Kata Containers利用轻量级虚拟机。这些安全运行时将容器与宿主机操作系统隔离开来，防止攻击者获取基础设施的未授权访问，减轻宿主机被接管的风险。

## 流行容器运行时简介

容器运行时提供创建、部署和执行容器所需的工具和库。

这些容器运行时处理创建和管理容器镜像、启动和停止容器、资源隔离、网络和安全等任务。它们是容器化技术的基石，对于在不同环境中一致运行应用程序至关重要。

以下是一些最流行的运行时。

### Docker

Docker是一个广泛使用的容器运行时，它为构建、打包和运行容器提供完整生态系统。它包括管理容器生命周期的Docker引擎和用于通过命令行与容器交互的Docker CLI。

在底层，Docker使用[runc](https://github.com/opencontainers/runc)作为默认的底层容器运行时。runc根据[Open Container Initiative (OCI)](https://opencontainers.org/)运行时规范来生成和管理容器。

### containerd

[containerd](https://containerd.io/)是Docker开发的开源容器运行时。它着重提供稳定、高性能和可移植的强大运行时。containerd被设计为容器编排系统的核心组件，可以与[Kubernetes](https://thenewstack.io/kubernetes/)等更高层编排平台集成。

与Docker类似，containerd使用runc作为默认的底层容器运行时来创建和管理容器。

### runc

[runc](https://github.com/opencontainers/runc)是OCI开发的轻量级底层运行时，它遵循OCI运行时规范。它通过在隔离沙箱中启动容器来提供基本的容器执行环境。Docker和containerd都利用runc的功能来管理容器生命周期、处理隔离、文件系统挂载等底层容器操作。

### CRI-O

CRI-O是一个专为Kubernetes设计的轻量级容器运行时。它实现了Kubernetes容器运行时接口(CRI)，并为Kubernetes与容器交互提供接口。CRI-O在底层使用runc、containerd等技术。

## 安全容器运行时：gVisor和Kata Containers

[gVisor](https://gvisor.dev/)是一个由谷歌开发的开源容器运行时。它使用轻量级的用户空间内核“沙箱”为容器提供安全执行环境。

[gVisor](https://thenewstack.io/how-to-implement-secure-containers-using-googles-gvisor/)不是直接在宿主机内核上运行容器，而是在隔离的沙箱中运行，增加了额外的安全和隔离层。沙箱拦截容器的系统调用，并应用自己的内核实现，提供针对内核级漏洞的防御。

[Kata Containers](https://katacontainers.io/)是一个将轻量级虚拟机与容器运行时结合的[开源项目](https://thenewstack.io/the-road-to-kata-containers-2-0/)。它使用硬件虚拟化为每个容器启动一个独立VM，在容器之间提供高度隔离。

每个VM运行一个极简的轻量级Guest OS，例如精简版Linux内核。Kata Containers旨在兼具容器的性能优势和VM的安全隔离。

gVisor和Kata Containers都解决了传统容器运行时的某些安全问题。它们有助于降低容器逃逸导致攻击者未经授权访问宿主机的风险。通过增加额外隔离和安全控制，这些运行时增强了容器化workload的保护。

gVisor和Kata Containers并非互斥；事实上，它们可以配合使用，Kata利用gVisor作为运行时。这种组合进一步增强了安全性，结合了VM级隔离和gVisor的额外安全措施。

在运行不可信或容易受攻击的workload时，这些安全运行时特别有用，例如多租户环境或处理不可信第三方代码。

## 在安全运行时中运行容器

使用像gVisor和Kata Containers等安全运行时可以显着提高宿主机保护。您可以从以下安全功能中受益:

- **增强隔离**。gVisor和Kata在容器与宿主机之间提供额外隔离层。这有助于防止容器逃逸，并限制容器内安全漏洞的影响。
- **内核级保护**。gVisor和Kata都可以防范内核级漏洞。gVisor实现自己的内核接口，拦截容器系统调用并执行安全策略。Kata利用硬件虚拟化在独立VM中运行容器，与宿主机内核隔离。
- **多层防御**。将这些运行时的安全机制与访问控制、网络隔离、镜像扫描等最佳实践结合，可以为容器部署建立更强大的安全态势。
- **兼容性和互操作性**。gVisor和Kata与Kubernetes等容器编排平台兼容，您可以在不改变现有容器化应用和部署流程的情况下获得它们的安全优势。

请注意，尽管gVisor和Kata提高了安全性，但由于额外隔离层，它们可能带来一定的性能开销。您需要评估具体用例和性能需求，确定安全优势是否足以抵消潜在性能影响。

## 在安全运行时中运行微服务

[微服务架构](https://thenewstack.io/microservices/)通常涉及在同一基础设施上运行多个独立服务。通过在安全运行时中运行每个微服务，可以确保它们相互隔离。

这有助于防止容器逃逸、特权升级和内核级漏洞，还可以限制安全事故的影响范围。

容器运行时还允许您向每个微服务分配特定资源(如CPU、内存)，确保公平分配，避免资源争用问题被恶意利用影响其他微服务的性能或稳定性。

要在安全运行时中运行微服务，请执行以下步骤：

1. **选择安全的容器运行时**。评估gVisor、Kata等，选择最符合需求的运行时，考虑安全特性、性能影响、基础设施兼容性等因素。
2. **安全构建容器镜像**。使用可信基础镜像，定期更新依赖，扫描镜像漏洞。实施安全的镜像仓库，验证镜像真实性。
3. **安全配置**。根据运行时文档指南，适当配置安全设置，如启用隔离、应用资源限制、设置网络策略、控制主机资源访问等。
4. 实施强访问控制。限制容器权限，为编排平台实施基于角色的访问控制，保护运行时API。
5. **持续监控日志**。实现监控和日志解决方案，跟踪微服务运行情况，监控可疑活动和安全事件。集中式日志分析可快速检测和响应安全事件。
6. **定期更新补丁**。应用安全补丁和更新，确保运行时版本更新，获取最新安全改进和错误修复。
7. **运行安全测试**。定期进行安全评估和渗透测试，识别运行时配置和应用代码中的漏洞。

## gVisor架构

gVisor由两个主要组件组成：Sentry和Gofer。

### Sentry

[Sentry](https://github.com/google/gvisor/tree/master/pkg/sentry)(不要与同名的监控平台[Sentry](https://sentry.io/welcome/?utm_content=inline-mention)相混淆)- 它负责代表容器化应用程序拦截和处理系统调用。它充当类似内核的接口，但不会直接将调用转发给主机内核。

相反，Sentry 是在它自己的隔离环境中服务这些请求的。它在运行的微服务和主机机器之间提供了一层隔离保护。Sentry 进行自身受限的系统调用，这些系统调用与 seccomp 规则紧密绑定，以确保安全执行。

### Gofer

Gofer 是 gVisor 中负责调停文件系统操作的组件。当容器化应用需要访问主机文件系统时，Sentry 会将请求转发给 Gofer。

然后，Gofer 使用主机进行必要的文件系统操作，以代表应用程序。这增加了额外的隔离层，可防止从容器内直接访问主机文件系统。

GVisor 使用一个名为[runsc (runsc sandbox)](https://github.com/google/gvisor/tree/master/runsc)的进程，而不是 runc 作为底层容器运行时。Runsc 是专门为 gVisor 设计的，它充当容器运行时和 gVisor 组件(Sentry 和 Gofer)之间的接口。

它处理容器生命周期管理、进程隔离和其他底层容器操作。Runsc 与 Sentry 和 Gofer 协作，为 gVisor 中的容器化应用提供一个安全的执行环境。

## Kata Containers架构

Kata Container 为每个容器或 Pod 封装专属的 VM，提供了额外的保护层。因为每个 VM 都有自己的内核，其中只包含容器工作负载必需的服务，这样可以减少潜在的攻击面。

除增强安全性外，Kata Container 还优先考虑性能和资源效率。这种精简的占用使 Kata Container 对追求在安全需求与高效利用资源间求平衡的组织具有吸引力。

Kata Container 被设计成与现有的容器化应用和部署基础设施兼容，使组织能在不作重大修改的情况下采用安全运行时功能。

将 Kata Container 视为集群的安全运行时，您可以从其出色的隔离性、轻量资源占用和增强的安全性中获益，这使其成为部署敏感或不可信工作负载的引人注目的选择。

## 配置gVisor容器安全

以下是创建使用gVisor作为容器运行时的RuntimeClass对象和pod清单的代码示例：

```yaml
gvisor.yaml (RuntimeClass object)
 
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
 name: gvisor
handler: runsc
```

这里创建一个名为`gvisor`的RuntimeClass，指定容器运行时处理程序为“runsc”，这是与gVisor交互的命令。

```yaml
gvisor-pod.yaml (Pod manifest)
apiVersion: v1
kind: Pod
metadata:
 name: gvisor-pod
spec:
 runtimeClassName: gvisor
 containers:
 - name: my-container
  image: your-image
```

在 gvisor-pod.yaml 文件中定义了一个名为 `gvisor-pod` 的 Pod。runtimeClassName 字段指定该 Pod 应使用“gvisor” RuntimeClass，对应 gVisor 容器运行时。

containers 部分让您定义容器配置，包括要使用的容器名称和镜像(用实际镜像名称替换 “your-image”)。

准备好 gvisor.yaml 和 gvisor-pod.yaml 文件后，可以使用以下命令创建 RuntimeClass 并部署 pod。

```bash
kubectl apply -f gvisor.yaml
kubectl apply -f gvisor-pod.yaml
```

这些命令将为 gVisor 创建 `RuntimeClass` 对象，并使用 gVisor 作为容器运行时部署 pod。

请注意，您需要确保在 Kubernetes 集群上正确安装和配置 gVisor，以使这些配置正常工作。

下面是创建 `RuntimeClass` 对象和 pod 清单文件的代码片段，它们使用 Kata Containers 作为容器运行时。

```yaml
kata.yaml(RuntimeClass对象)

apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata: 
 name: kata
handler: kata-runtime
```

上面创建一个名为`kata`的RuntimeClass，指定运行时处理程序为“kata-runtime”，对应Kata Containers。

```yaml
kata-pod.yaml(Pod清单)

apiVersion: v1 
kind: Pod
metadata:
 name: kata-pod
spec:
 runtimeClassName: kata
 containers:
 - name: my-container
  image: your-image
```

在 `kata-pod.yaml` 文件中定义了一个名为 `kata-pod` 的 Pod。runtimeClassName 字段指定该 Pod 应使用 `kata` RuntimeClass，对应 Kata Containers 运行时。

containers 部分让您定义容器配置，包括容器名称和要使用的容器镜像(用实际镜像名称替换 `your-image`)。

准备好 kata.yaml 和 kata-pod.yaml 文件后，可以使用以下命令创建 RuntimeClass 并部署 pod：

```bash
kubectl apply -f kata.yaml
kubectl apply -f kata-pod.yaml
```

这些命令将为 Kata Containers 创建 RuntimeClass 对象，并部署 pod，利用 Kata Containers 作为容器运行时。

请确保在 Kubernetes 集群上正确安装和配置 Kata Containers，以使这些配置按预期工作。

## Kubernetes RuntimeClass功能的优势

Kubernetes中的RuntimeClass功能为根据特定需求和安全策略选择不同容器运行时提供了显著灵活性。您可以为集群内不同workload定义和选择合适的运行时。

RuntimeClass的一些关键优势和用例:

**工作负载隔离**。不同工作负载可能有不同的安全需求。通过 RuntimeClass，您可以为每个工作负载选择提供所需隔离级别和安全级别的最合适运行时。

例如，对安全敏感负载可以使用更轻量高效的运行时，如 gVisor 或 Kata Containers；而对其他负载则使用标准运行时，如 Docker 或 containerd。

**自定义运行时**。RuntimeClass 使您能在 Kubernetes 环境中集成使用自定义容器运行时。如果您开发或采用定制的运行时满足需求，可以为其定义 RuntimeClass 并用于特定负载。

**性能优化**。不同容器运行时的性能各有不同。通过 RuntimeClass，您可以为每个负载选择最合适的运行时来优化性能。例如，对需要更好资源效率和更快启动时间的负载，可以选择轻量级运行时，如 gVisor 或 Kata Containers。

**合规和安全策略**。组织通常有特定安全策略或合规要求，规定用于某些负载的运行时。RuntimeClass 让您可以通过为需遵守特定安全指南的负载配置适当运行时来实施这些策略。

**动态运行时切换**。RuntimeClass 还支持为运行负载动态切换运行时。这种灵活性使您可以根据需要在运行时之间切换，以适应变化的负载需求或有效应对安全事件。

## 部署安全运行时的最佳实践

了解何时以及如何使用安全容器运行时，对规划安全的 Kubernetes 环境至关重要。以下是根据具体需求部署安全运行时的一些选项和注意事项。

在集群中每个 Pod 上使用安全运行时。一种方法是在集群所有 Pod 上使用安全运行时(如 gVisor 或 Kata Containers)作为默认运行时。这可以确保所有工作负载一致且强大的隔离，无论其信任级别。

默认使用安全运行时，可以为整个环境提供额外保护层。

在安全容器内运行不可信任的或第三方应用。对于运行不可信任或第三方应用，安全运行时特别有价值。通过在如 gVisor 或 Kata Containers 的运行时的安全容器内部署这些应用，可以降低风险，并与底层主机系统隔离。

这有助于保护主机和其他工作负载免受来自不可信代码的潜在漏洞或恶意活动。

在默认 runC 运行时内部署自研应用。对经过严格安全审查的可信任自研应用，可以选择在默认 runC 运行时内运行。这承认可信应用可能不需要安全运行时提供的额外隔离。

但是，对这些应用实施适当的安全实践(如容器加固和漏洞扫描)至关重要。

考虑具体需求和环境。是否部署安全运行时应基于具体需求、安全要求和风险评估。评估数据敏感性、监管合规性、威胁格局和环境整体安全态势等因素。

另外，考虑使用安全运行时的性能开销和资源使用影响，因为与标准运行时相比，它们可能带来额外开销。
