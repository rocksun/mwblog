## Kubernetes GUI、CLI、支持 Linux 的 Web UI

根据过去几天我发现的内容整理了这份快速清单。希望对寻找集群管理工具的 Linux 用户有所帮助。可能：几乎可以肯定不详尽。

### GUI 和 IDE

旨在让 Linux 用户更容易从其 Linux 工作站管理 Kubernetes 集群的 GUI 和 IDE：

- [Aptakube](https://aptakube.com/) 管理集群的 GUI。可作为适用于 Ubuntu 和基于 Debian 的发行版的 Debian 以及 appimage 使用。15 天免费试用，之后为订阅服务。
- [Kubernetic](https://www.kubernetic.com/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)：营销标语：“Kubernetes 桌面客户端 - 集群管理，简化”。Linux 客户端是一个 appimage。
- [Lens - Kubernetes IDE](https://k8slens.dev/)：对于希望使用 GUI 来帮助管理其集群的 Linux 用户来说，Lens Desktop 可能是一个最全面的解决方案（意见）。对于 Linux，有一个 .deb、一个 .rpm、一个 .snap 和一个 AppImage - 因此无论你运行的是什么发行版，都应该很容易启动并运行它。Lens 是一个 IDE，还提供了一个终端环境。
- [Podman Desktop](https://podman-desktop.io/)：对于 Linux，有一个 flatpak 和一个 tar.gz。你可以使用 Podman Engine 直接解析 Kubernetes YAML 文件，并从现有 pod 生成 Kubernetes YAML。
- [JetPilot](https://github.com/unxsist/jet-pilot)：Jet Pilot 是一个跨平台 Kubernetes 桌面客户端，可以在 Linux 上运行。
也可以：使用 VSCode + Kubernetes 扩展。
[指南](https://code.visualstudio.com/docs/azure/kubernetes)。

**总结：**Lens 可能是在 K8s 特定的 IDE 和 GUI 中最强大的选项，但还有其他几个选项也值得一试

### 将在 Linux 机器上运行的 Web UI

（几乎总是）不是特定于 Linux 的 Web UI，但也可以在 Linux 本地主机上运行

- [Kubernetes Dashboard](https://github.com/kubernetes/dashboard) 当然不是特定于 Linux 的，但是... 作为 Linux 用户，你可以在本地主机上运行它来管理你的集群（无论它是在本地运行还是在远程运行）
- [Portainer:](https://www.portainer.io/) 对于希望通过在本地机器上运行 Web UI 来管理其集群的 Linux 用户来说，Portainer 是另一个不错的选择。Portainer 通过在远程集群上安装代理来工作，然后你可以通过 Web UI 进行管理（也适用于 Docker 和 Docker Swarm）
- [Headlamp](https://headlamp.dev/)：“开箱即用，Headlamp 是一个功能齐全的 Kubernetes UI。通过利用其强大的插件系统，构建者可以塑造 Headlamp 以适应其定制用例、产品和环境。”
- [minikube GUI](https://minikube.sigs.k8s.io/docs/tutorials/setup_minikube_gui/)：处于原型阶段

### 支持 Linux 的 CLI（和“混合”）

用于 Kubernetes 管理的 CLI 是尝试采用 Kubernetes 管理的核心 CLI 并用一些附加功能（或通常通过使它们在视觉上更具交互性）来丰富它们的工具

- [KUI](https://kui.tools/)“我们喜欢 CLI，并认为它们对于以灵活的方式与云进行交互至关重要。我们需要偏离正轨的力量。但 ASCII 很乏味。Kui 接受你的正常 kubectl 命令行请求并以图形响应。你将看到可排序的表格，而不是 ASCII 表格。在 Kui 中，你只需单击即可，而无需复制和粘贴长自动生成的资源名称来深入了解。”
- [k9s](https://github.com/derailed/k9s)：”Kubernetes CLI 以时尚的方式管理你的集群”

### 其他支持 Linux 的 Kubernetes 工具

用于其他功能的工具，例如可视化在 Kubernetes 集群上运行的应用程序：

- [Octant](https://octant.dev/community/) - “供开发人员了解应用程序如何在 Kubernetes 集群上运行的工具。”该项目由 VMWare 支持，尽管其 Github 页面处于仅存档模式，因此开源分支的开发可能不再活跃。该项目的[最新版本](https://github.com/vmware-archive/octant/releases)是在 2022 年 2 月，但包括一个 .deb、一个 .rpm 和一个 .tar.gz（适用于 64 位和 ARM 架构）