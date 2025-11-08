Sidero Labs 的 [Talos Linux](https://thenewstack.io/open-source-talos-linux-bringing-simplicity-to-kubernetes/) [不是一个正统的 Linux 发行版](https://thenewstack.io/no-ssh-what-is-talos-this-linux-distro-for-kubernetes/)。它旨在为管理不同的 Kubernetes 和其他部署所带来的高成本和复杂性提供一种全新的替代方案。

可以说，它与 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 的 Linux OpenShift、SUSE Rancher 以及其他 Kubernetes 发行版的功能相反。在所有这些发行版中，Kubernetes 都安装并运行在一个通用操作系统之上。

[Sidero Labs](https://www.siderolabs.com/?utm_content=inline+mention) 凭借其开源的 Talos Linux，认为整个基础不仅不必要，而且是一种负担，特别是对于私有云和边缘用例。

在本教程中，我们将展示如何在您的 Mac 上本地安装 Talos Linux。可以假定，当使用 Linux 操作系统时，这些命令大多数也适用。

## 开始

首先，从命令行安装 Homebrew，以便在需要时安装 Talos Linux 和其他依赖项。如果您已经安装了 Homebrew，在安装 Talos Linux 的过程中，更新将自动安装，如下面的截图中所示。如果您的 Mac 上未安装 Homebrew，则使用此命令下载并安装它：

[![](https://cdn.thenewstack.io/media/2025/11/044ebf72-screenshot-2025-11-05-at-9.13.18%E2%80%AFpm-1024x22.png)](https://cdn.thenewstack.io/media/2025/11/044ebf72-screenshot-2025-11-05-at-9.13.18%E2%80%AFpm-1024x22.png)

Homebrew 安装完成后，使用它来安装 Talos Linux：

[![](https://cdn.thenewstack.io/media/2025/11/258bb7d0-screenshot-2025-11-04-at-12.44.46%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/258bb7d0-screenshot-2025-11-04-at-12.44.46%E2%80%AFpm.png)

启动 socket\_vmnet 服务，以便连接虚拟机：

[![](https://cdn.thenewstack.io/media/2025/11/3e9ace3e-screenshot-2025-11-05-at-9.19.02%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/3e9ace3e-screenshot-2025-11-05-at-9.19.02%E2%80%AFpm.png)

现在您可以为您的 Talos 集群初始化引导 Kubernetes 控制平面：

[![](https://cdn.thenewstack.io/media/2025/11/a587c75f-screenshot-2025-11-05-at-9.49.18%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/a587c75f-screenshot-2025-11-05-at-9.49.18%E2%80%AFpm.png)

Homebrew 将开始为您安装所有内容。这是泡一杯 H2O 和其他好东西的真正咖啡的好时机，但整个过程应该只需要几分钟：

[![](https://cdn.thenewstack.io/media/2025/11/8c2c2531-screenshot-2025-11-04-at-12.46.52%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/8c2c2531-screenshot-2025-11-04-at-12.46.52%E2%80%AFpm.png)

## 安装 Talos 集群

现在您已准备好安装您的 Talos 集群：

[![](https://cdn.thenewstack.io/media/2025/11/4f12fa79-screenshot-2025-11-04-at-12.49.32%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/4f12fa79-screenshot-2025-11-04-at-12.49.32%E2%80%AFpm.png)

配置 kubeconfig，以便 talosctl 将新集群的配置合并到默认的 kubeconfig 文件中：

[![](https://cdn.thenewstack.io/media/2025/11/6778e4d9-screenshot-2025-11-05-at-9.42.00%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/6778e4d9-screenshot-2025-11-05-at-9.42.00%E2%80%AFpm.png)

现在请确保您的集群正在运行：

[![](https://cdn.thenewstack.io/media/2025/11/d9f01f9f-screenshot-2025-11-05-at-9.47.34%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/d9f01f9f-screenshot-2025-11-05-at-9.47.34%E2%80%AFpm.png)

打开 [Docker](https://www.docker.com/?utm_content=inline+mention) 并检查它是否正在运行：

[![](https://cdn.thenewstack.io/media/2025/11/0b0ac949-screenshot-2025-11-04-at-12.53.24%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/0b0ac949-screenshot-2025-11-04-at-12.53.24%E2%80%AFpm.png)

您应该会看到以下内容：

[![](https://cdn.thenewstack.io/media/2025/11/c2a681c0-screenshot-2025-11-04-at-1.03.51%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/c2a681c0-screenshot-2025-11-04-at-1.03.51%E2%80%AFpm.png)

您运行这些命令，然后 Talos Linux 管理您的集群。运行上述命令后，Talos Linux 应该可以用于管理您的 Kubernetes 集群。

与许多其他 Kubernetes 管理平台相比，安装过程要简单得多。设置和试用它也很有趣。