
<!--
title: Podman和Libkrun
cover: ./cover.png
-->

Podman machine 的主要虚拟化驱动程序被称为“提供程序”。在 2024 年 4 月，我为 MacOS 添加了对 krun 作为提供程序的支持。我们对该添加的提及很少，因为我们还需要整理回归测试、测试环境和支持细节等项目。但随着我们接近完成这些项目，我们已准备好让 krun 支持从动物园中逃脱。

> 译自 [Podman and Libkrun](https://blog.podman.io/2024/07/podman-and-libkrun/)，作者 Brent Baude。

我们添加对 krun 支持的关键原因之一是它能够为 Mac 上的 Podman machine 提供 GPU 的直通支持。此功能使 MacOS 上的容器化 AI 工作负载变得现实，并显着扩展了开发人员的体验。

使用 libkrun 与 Podman machine 的基本步骤如下：

1. 安装适当的软件（Podman 和 libkrun 组件）
2. 配置 Podman 以使用 libkrun 提供程序。
3. 创建并启动 Podman machine。

## 1. 注意事项

如果您想尝试 krun 和 podman machine，我建议您先执行 `podman machine reset`。这不是必需的，并且具有破坏性，因为它会删除您所有现有的 Podman machine 以及您下载（和缓存）的任何机器映像。

## 2. 安装软件

截至撰写本文时，安装 Podman 和所需的 libkrun 组件主要有两种方法：通过 [brew](https://brew.sh/) 或通过 Podman 安装程序和其他下载。

### 使用 Brew

（如果您没有 brew，请跳到下面的下一节）

本节假设您已经安装了 homebrew。如果您已经安装了 brew 和 podman（通过 brew），那么您可以直接跳到添加 krun 组件的步骤。我个人更喜欢下载软件并自行安装，但两种方法都可以获得相同的 Podman 用户体验。

#### 安装 Podman

要在您的 Mac 上安装 Podman，请从终端提示符发出以下命令：

```
% brew install podman
==> Downloading https://formulae.brew.sh/api/formula.jws.json
#################################################################################################...  
[ omitted for brevity ]
==> Running `brew cleanup podman`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
```

#### 安装 krunkit

要使用 libkrun，您需要安装 krunkit。在 Podman 5.2 或更高版本中，它将捆绑到 Podman Mac 安装程序中。但目前，像这样安装它就足够了：

```
brentbaude@Mac-mini ~ % brew tap slp/krun
==> Tapping slp/krun
Cloning into '/opt/homebrew/Library/Taps/slp/homebrew-krun'...
remote: Enumerating objects: 291, done.
remote: Counting objects: 100% (28/28), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 291 (delta 22), reused 17 (delta 17), pack-reused 263
Receiving objects: 100% (291/291), 169.33 MiB | 3.79 MiB/s, done.
Resolving deltas: 100% (113/113), done.
Tapped 4 formulae (20 files, 195MB).
bbrentbaude@Mac-mini ~ % brew install krunkit
==> Downloading https://formulae.brew.sh/api/formula.jws.json
==> Downloading https://formulae.brew.sh/api/cask.jws.json
==> Fetching dependencies for slp/krunkit/krunkit: dtc, libepoxy, molten-vk, slp/krunkit/virglrenderer and slp/krunkit/libkrun-efi
[ omitted for brevity ]
==> Installing slp/krunkit/krunkit
==> Pouring krunkit-0.1.1.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/krunkit/0.1.1: 7 files, 1.2MB
==> Running `brew cleanup krunkit`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
```

### 不使用 Brew

如果您无法或选择不使用 brew。坦白地说，我更喜欢这种方法，因为您可以获得社区自己生成的二进制文件。

#### Podman

下载 [最新版本](https://github.com/containers/podman/releases) 的 Podman Mac 安装程序，并按照安装说明进行操作。

#### Krunkit

**注意**：此步骤在 Podman 5.2 及更高版本中将不再需要。krunkit 二进制文件将包含在 Podman 安装程序中，并且也已签名。

您可以从其 [GitHub 版本](https://github.com/containers/krunkit/releases) 获取 krunkit 的最新版本。下载最新版本并将 tarball 解压缩到您的文件系统。

```
brentbaude@Mac-mini ~ % sudo tar xzf ~/Downloads/krunkit-podman-unsigned-0.1.1.tgz -C /opt/podman
```

krunkit 二进制文件未经其上游社区签名，除非您 [明确允许它](https://support.apple.com/guide/mac-help/open-a-mac-app-from-an-unidentified-developer-mh40616/mac)，否则它将无法执行。这可以通过以下命令完成：

```
brentbaude@Mac-mini ~ % sudo xattr -dr com.apple.quarantine /opt/podman/bin/krunkit
```

## 3. 更改 Podman machine 提供程序

MacOS 上的默认 Podman 机器提供程序称为 vfkit。要切换到其他提供程序（如 libkrun），您只需在配置文件中定义首选提供程序即可。对于 Podman，此文件（默认情况下不存在）为 `$HOME/.config/containers/containers.conf`。您可能还需要创建 `$HOME/.config/containers` 目录，具体取决于您之前使用 Podman 的情况。它是一个基于 YAML 的配置文件。在最简单的情况下，以下内容就足够了：

```
brentbaude@Mac-mini ~ % mkdir ~/.config/containers/
brentbaude@Mac-mini ~ % cat ~/.config/containers/containers.conf
[machine]
provider="libkrun"
```

您可以使用 `podman info` 命令验证提供程序：

```
brentbaude@Mac-mini ~ % podman info
OS: darwin/arm64
provider: libkrun
version: 5.1.2
```

## 4. 创建并启动 Podman 机器

在安装了先决条件软件并验证了正在使用正确的提供程序后，我们可以使用一条命令创建并启动 Podman 机器：

```
brentbaude@Mac-mini ~ % podman machine init --now
Looking up Podman Machine image at quay.io/podman/machine-os:5.1 to create VM
Extracting compressed file: podman-machine-default-arm64: done
Machine init complete
Starting machine "podman-machine-default"
This machine is currently configured in rootless mode. If your containers
require root permissions (e.g. ports < 1024), or if you run into compatibility
issues with non-podman clients, you can switch using the following command:
podman machine set --rootful
API forwarding listening on: /var/folders/ml/3yfmdg5n4qn0zq05f7sl34z40000gn/T/podman/podman-machine-default-api.sock
The system helper service is not installed; the default Docker API socket
address can't be used by podman. If you would like to install it, run the following commands:
sudo /opt/homebrew/Cellar/podman/5.1.1/bin/podman-mac-helper install
podman machine stop; podman machine start
You can still connect Docker API clients by setting DOCKER_HOST using the
following command in your terminal session:
export DOCKER_HOST='unix:///var/folders/ml/3yfmdg5n4qn0zq05f7sl34z40000gn/T/podman/podman-machine-default-api.sock'
Machine "podman-machine-default" started successfully
```

现在机器正在运行，您可以使用 `podman machine ls` 验证 VM 类型是否为 libkrun：

```
brentbaude@Mac-mini ~ % podman machine ls
NAME VM TYPE CREATED LAST UP CPUS MEMORY DISK SIZE
podman-machine-default* libkrun 29 seconds ago Currently running 4 2GiB 100GiB
```

### 确保 GPU 存在

您可以通过查看 Podman 机器本身的设备来检查 GPU 是否存在。渲染设备的存在代表着 GPU 的存在。

```
brentbaude@Mac-mini ~ % podman machine ssh ls -l /dev/dri
total 0
drwxr-xr-x. 2 root root 80 Jul 11 06:33 by-path
crw-rw----. 1 root video 226, 0 Jul 11 06:33 card0
crw-rw-rw-. 1 root render 226, 128 Jul 11 06:33 renderD128
```

注意：当运行需要访问 GPU 的容器时，您需要将 `--device /dev/dri` 引用传递给 `podman run` 命令。

