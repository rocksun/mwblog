一个开源容器平台，[Apptainer](https://apptainer.org/)（前身为 Singularity）专为安全的[高性能计算](https://thenewstack.io/hpc-kubernetes-ai-training-on-3500-gpus/)（HPC）环境设计。与[主导桌面和云服务](https://thenewstack.io/docker-containers-that-could-be-essential-for-your-small-business/)的 Docker 不同，Apptainer 在多用户 Linux 系统（如 HPC 集群）中表现出色，这些系统需要不带 root 权限的用户空间容器。它提供与 Docker 类似的功能，包括与大多数 Docker 镜像的兼容性，同时满足 HPC 环境中的安全性和可移植性需求。

本指南将帮助熟悉 Docker 的开发人员在 Linux 上探索 Apptainer，涵盖安装、基本用法和用例。

## Ubuntu 上 Apptainer 的入门

在 Linux 上安装 Apptainer 可以通过包管理器或从源代码进行。Apptainer 需要一个现代 Linux 内核（为非特权使用启用用户命名空间），并且在没有 Linux 虚拟机的情况下无法在 Windows/Mac 上运行。

对于许多 Debian/Ubuntu 用户来说，最简单的方法是使用官方的个人包存档（PPA）：

```
sudo apt update &amp;&amp; sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:apptainer/ppa
sudo apt update &amp;&amp; sudo apt install -y apptainer    # use apptainer-suid for SUID mode
```

这些命令默认以非特权模式安装 Apptainer（没有 setuid 二进制文件）。如果需要需要 SUID 的功能（用于旧内核或某些挂载功能的 setuid root 助手），请安装 apptainer-suid 包。在非特权模式下，Apptainer 利用用户命名空间，因此可以作为普通用户完全运行容器。

安装后，通过执行一个简单的容器来验证它是否工作，例如：

```
apptainer exec docker://alpine cat /etc/alpine-release
```

[![](https://cdn.thenewstack.io/media/2025/11/712f600a-apptainer-0-1024x409.png)](https://cdn.thenewstack.io/media/2025/11/712f600a-apptainer-0-1024x409.png)

此命令拉取一个微小的 [Alpine Linux](https://thenewstack.io/alpine-linux-heart-docker/) 镜像并打印其版本文件，确认 Apptainer 已正确设置。

你会注意到 Apptainer 将 Docker 镜像转换为当前目录中的 SIF 文件。Singularity 镜像格式（SIF）是 Apptainer 和 Singularity 使用的标准容器镜像格式。SIF 将整个容器环境——操作系统、软件、元数据和配置——封装在一个单一的、不可变的文件中。

与 Docker 镜像一样，这种设计确保了科学、HPC 和企业工作负载的可移植性、可重现性和安全性。SIF 镜像主要是只读的，支持签名验证和加密，并与并行文件系统无缝集成。由于整个镜像存储在一个文件中，容器的分发和归档变得容易。可写覆盖和主机挂载选项在需要时提供灵活性。

.sif 文件通常从定义（.def）文件构建，该文件概述了构建步骤、安装的包和环境设置。一旦创建，.sif 镜像就作为一个可靠、可验证、生产质量的容器镜像，具有可移植性并确保可重现执行，因为其内容在创建后永远不会改变。Apptainer 可以使用此文件来实例化容器、运行特定命令、启动应用程序或提供交互式 shell。

下面显示了一个基本的 Apptainer .def 文件。它从现有 Docker 镜像构建镜像定义。

```
Bootstrap: docker
From: ubuntu:22.04

%post
    apt-get update
    apt-get install -y python3

%runscript
    echo "Hello from Apptainer!"

%help
    This container installs Python 3 on Ubuntu 22.04 and prints a message when run.
```

可以使用以下命令构建镜像：

```
sudo apptainer build myimage.sif myfile.def
```

Apptainer 内部维护一个用于中间文件和层的缓存，通常在系统上的 `~/.apptainer/cache`。

## 运行基本容器

Apptainer 的命令行界面与 Docker 类似，但没有涉及守护进程。你可以通过 apptainer 命令直接运行容器。常见的子命令包括 run、exec 和 shell，它们分别类似于 Docker 的 `docker run`、`docker exec` 和用于交互式 shell 的 `docker run -it`。

使用 `apptainer run` 执行镜像的默认 runscript。例如，拉取 Apptainer 镜像（.sif 文件）后，你可以简单地运行它：

```
apptainer pull docker://alpine
apptainer run alpine_latest.sif
```

如果镜像定义了 runscript，`apptainer run` 将执行该脚本。否则，它将回退到交互式 shell。你还可以通过 URI 直接运行镜像而无需保存它们。

```
apptainer run docker://ghcr.io/apptainer/lolcow
```

你可以使用 `apptainer exec` 在容器内运行特定命令。例如：

```
apptainer exec alpine_latest.sif echo "Hello from inside container"
```

这与 `docker exec` 类似，但甚至可以在镜像文件或 Docker Hub URI 上运行。如果你还没有镜像，Apptainer 将在一步中获取它并运行命令。

使用 `apptainer shell` 进入容器内的 shell，这对于探索或调试很有用。例如：

```
apptainer shell alpine_latest.sif
<img class="aligncenter size-large wp-image-22805178" src="https://cdn.thenewstack.io/media/2025/11/487e0cc1-apptainer-1-1024x285.png" alt="" width="1024" height="285" />
```

## Apptainer 如何执行容器

与 Docker 相比，Apptainer 采用了一种根本不同的容器运行时方法。没有后台守护进程，运行容器是直接调用，在进程中创建容器环境。当你运行 Apptainer 容器时，它会执行一系列步骤：在最小的 Linux 用户命名空间中挂载 SIF 镜像（这是一个 [SquashFS](https://docs.kernel.org/filesystems/squashfs.html) 文件系统），根据需要设置必要的命名空间（挂载、PID 等），然后使用 `exec()` 系统调用在容器上下文中启动指定进程。结果是容器化应用程序作为 Apptainer 命令的子进程运行，没有留下任何额外的垫片或包装器。Apptainer 的设计导致最小的开销：一旦容器进程启动，就没有持续的管理器进程——你的应用程序直接在主机内核上运行，并应用了容器隔离。

重要的是，Apptainer 容器默认以与主机相同的用户身份运行。如果你以非特权用户身份启动容器，那么在容器内你也将是该用户（UID/GID 保留）。没有 docker0 网络或默认 NAT：默认情况下，Apptainer 共享主机网络栈（因此除非使用明确选项，否则网络不会隔离）。容器进程可以看到并使用主机资源，如 GPU、网络接口和文件（受挂载限制），只要用户允许。此模型与 HPC 用例一致，在这种情况下，你不希望容器拥有比调用者更多的权限，并且希望高效访问硬件，例如高速互连。

为了在没有 root 权限的情况下进行容器设置，Apptainer 可以安装在 setuid 模式或完全非特权模式下。在 setuid 模式下，Apptainer 的一小部分代码 (apptainer-suid) 以 root 权限运行以执行挂载操作，然后放弃权限。在非特权模式下，它使用用户命名空间功能（在内核 ≥ 4.18 上可用）来模拟新命名空间中的 root 进行设置。无论哪种方式，结果是您不需要运行 root 守护进程服务。容器在用户的会话中运行，使 Apptainer 本质上是无守护进程且与内核集成的。从开发人员的角度来看，这意味着您可以像任何其他 CLI 工具一样调用 Apptainer 命令，并且当您的命令完成时容器会退出，不会留下任何残留的容器进程。

## 何时使用 Apptainer 而不是 Docker

在以下几种情况下，Apptainer 比 Docker 更受青睐，尤其是在高性能计算（HPC）和安全的多租户环境中：

### 无 root 执行和安全性

Apptainer 允许用户在不[需要 root](https://thenewstack.io/linux-cgroups-v2-brings-rootless-containers-superior-memory-management/)（管理员）权限的情况下运行容器，通过避免 Docker 守护进程模型常见的特权升级风险，使其在多租户系统和共享 HPC 集群上本质上更安全。

### HPC 和科学计算重点

Apptainer 专门为科学计算和 HPC 设计，与资源管理器和作业调度程序集成，而 Docker 主要为微服务和企业应用程序部署工作流开发。

### 单文件容器镜像

Apptainer 使用 Singularity 镜像格式（SIF），它将整个容器打包成一个单一的、不可变的文件。这使得分发、共享和归档比 Docker 更容易，Docker 将容器结构化为 tar 文件中的镜像层堆栈。

### 本机用户身份保留

容器外的用户身份（UID/GID）在容器内得到保留，确保了透明的文件系统和权限处理，这在大学集群或协作研究环境中至关重要。

### 与现有 HPC 基础设施的兼容性

Apptainer 与现有的 HPC 工具和存储无缝协作，无需更改基础设施。其容器与并行文件系统和大规模作业调度程序原生集成，并且不像 Docker 那样需要运行 root 权限的后台守护进程。

这些优势使 Apptainer 成为安全、大规模和以研究为重点的计算环境的首选，其中无 root 操作和无缝集成是优先事项。