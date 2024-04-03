
<!--
title: Proxmox上的Kubernetes
cover: https://blog.stonegarden.dev/articles/2024/03/proxmox-k8s-with-cilium/featured.webp
-->

在之前的文章中，我们了解了如何从全新的 Debian 12 网络安装开始使用 Cilium 引导 K3s。最近开始使用 Proxmox 虚拟环境，我觉得自然而然地需要了解 OpenTofu/Terraform 和 Cloud-init，以便为 Kubernetes 集群自动配置虚拟机。

> 译自 [Kubernetes on Proxmox](https://blog.stonegarden.dev/articles/2024/03/proxmox-k8s-with-cilium/)，作者 Vegard S Hagen。

在之前的文章中，我们了解了如何从全新的 [Debian 12 网络安装](https://www.debian.org/distrib/netinst) 开始使用 [Cilium 引导 K3s](https://blog.stonegarden.dev/articles/2024/02/bootstrapping-k3s-with-cilium/)。最近开始尝试 [Proxmox 虚拟环境](https://www.proxmox.com/en/proxmox-virtual-environment/overview)，我觉得自然而然地需要了解 [OpenTofu](https://opentofu.org)/ [Terraform](https://www.terraform.io) 和 [Cloud-init](https://cloudinit.readthedocs.io/en/latest/index.html)，以便为 Kubernetes 集群自动配置虚拟机。在本文中，我们将使用 [kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/) 来完成创建 Kubernetes 集群的繁重工作。如果你真的想亲自动手，可以参考 [Kelsey Hightower](https://en.wikipedia.org/wiki/Kelsey_Hightower) 的 [Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)，以及受其启发的类似指南，例如 [Proxmox/KVM 的指南](https://github.com/DushanthaS/kubernetes-the-hard-way-on-proxmox)。

## Proxmox 虚拟环境

本文针对基于 [英特尔 N100](https://ark.intel.com/content/www/us/en/ark/products/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz.html) 的迷你电脑（[华硕 PN42](https://www.asus.com/displays-desktops/mini-pcs/pn-series/asus-expertcenter-pn42/）编写，配备 [32 GB RAM](https://www.kingston.com/en/memory/search?partid=KF432S20IB/32) 和 [1 TB 存储](https://www.westerndigital.com/en-ie/products/internal-drives/wd-black-sn770-nvme-ssd?sku=WDS100T3X0E)。我使用 [Proxmox 虚拟环境 8.1](https://www.proxmox.com/) 作为 [虚拟机管理程序](https://en.wikipedia.org/wiki/Hypervisor)。

要开始使用 Proxmox，只需按照 [官方文档](https://www.proxmox.com/en/proxmox-virtual-environment/get-started) 中的步骤操作即可。我发现 Derek Seaman 撰写的[这篇文章](https://www.derekseaman.com/2023/10/home-assistant-proxmox-ve-8-0-quick-start-guide-2.html)，由 [tteck 的 Proxmox 脚本](https://github.com/tteck/Proxmox) 提供支持，是对 Proxmox（和 Home Assistant）的绝佳介绍。我建议运行上述文章中提到的 post-installation 脚本:

```bash
bash -c "$(wget -qLO - https://github.com/tteck/Proxmox/raw/main/misc/post-pve-install.sh)"
```

这将指导你完成几个步骤，以设置非企业存储库，如果你还没有准备好用你的资金支持 Proxmox。最后。

我建议启用 2FA 并查看 Derek 的另一篇文章 [Proxmox 的 TLS 证书](https://www.derekseaman.com/2023/04/proxmox-lets-encrypt-ssl-the-easy-button.html)。

## Debian（操作系统）

在本文中，我们将使用 [Debian 12 Bookworm](https://cloud.debian.org/images/cloud/) 的*通用*云镜像。

[全尺寸](/articles/2024/03/proxmox-k8s-with-cilium/images/debian-dark.svg))
[全尺寸](/articles/2024/03/proxmox-k8s-with-cilium/images/debian-light.svg))

像 [Ubuntu](https://ubuntu.com/), [Rocky Linux](https://rockylinux.org/), [OpenSUSE](https://www.opensuse.org/), 或 [Arch Linux](https://archlinux.org/) 等其他 Linux 发行版也应该可以工作，但某些步骤可能会有所不同。还有 [Talos Linux](https://www.talos.dev/)，这是一个专为 Kubernetes 构建的不可变操作系统，我计划在不久的将来尝试一下。

## OpenTofu（Terraform）

简单来说，[OpenTofu](https://opentofu.org) 是在 Hashicorp 从开源许可证切换到 [BUSL](https://www.hashicorp.com/license-faq) 之后创建的。用 OpenTofu 自己的话来说，它是“[…] 一个 Terraform 分支，开源、社区驱动，由 Linux 基金会管理”。

在这一点上——就我们的目的而言，它们是可互换的。我个人更喜欢 OpenTofu，并且将在本文中坚持使用它。如果你更喜欢 Terraform，只需将每个 tofu 命令替换为 terraform 即可。

有关如何安装 OpenTofu 的说明，请参阅其文档[此处](https://opentofu.org/docs/intro/install/)。如果你偏爱 Terraform，可以从[此处](https://developer.hashicorp.com/terraform/install)获取。我们将使用 Pavel Boldyrev 维护的 [Proxmox Terraform 提供程序](https://github.com/bpg/terraform-provider-proxmox)来使用 Proxmox 和 Cloud-init 初始化和配置我们的虚拟机。

## Cloud-init

[Cloud-init](https://cloudinit.readthedocs.io/) 是一种类似 [PXE-boot](https://en.wikipedia.org/wiki/Preboot_Execution_Environment) 适用于物理硬件的初始化虚拟机的方式。

由 [Canonical](https://github.com/canonical/cloud-init)维护，Cloud-init 被认为是云中虚拟机初始设置的*事实*标准，并确保了可重复且高效的系统配置方式。

## Kubeadm

[#](#kubeadm) [Kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/) 是一个用于创建 Kubernetes 集群的工具，

我们将在 cloud-init 阶段使用 kubeadm 配置我们的 [Kubernetes](https://kubernetes.io) 集群。

另一个选择是等到 cloud-init 完成，然后应用[Ansible](https://www.ansible.com)剧本。

## Cilium

[Cilium](https://cilium.io) — 凭借其 [eBPF 🐝](https://ebpf.io) 的优势，目前是 Kubernetes 的最热门 [CNI 插件](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)（个人拙见）。

在 [Isovalent](https://isovalent.com/) — Cilium 的创建者，[宣布](https://isovalent.com/blog/post/cisco-acquires-isovalent/) 被 [Cisco](https://www.cisco.com/)收购后，我有一点怀疑。然而 Cilium 是一个 [CNCF](https://www.cncf.io/) 项目，并且在上周在巴黎举行的 [KubeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 上与一些相关人员交谈后，这种怀疑消失了。

## 配置

在本节中，我尝试解释我的配置选择，如果你只想查看完整配置，请转到`摘要`部分。

我对 Proxmox 比较陌生，而且我绝不是 Terraform 专家。如果你认为某些事情可以做得更好——尤其是如果我做错了什么，我很乐意听取你的意见！

### PCI passthrough

我们希望能够将 [PCIe](https://en.wikipedia.org/wiki/PCI_Express) 设备，如 [NIC](https://en.wikipedia.org/wiki/Network_interface_controller) 和 [GPU](https://en.wikipedia.org/wiki/GPU) 传递给我们的虚拟机。按照 [Proxmox wiki](https://pve.proxmox.com/wiki/PCI%28e%29_Passthrough) 的说明，我们必须首先在 BIOS 中启用 [IOMMU](https://en.wikipedia.org/wiki/Input%e2%80%93output_memory_management_unit) 支持。该设置也可以称为 `VT-d`。


如果你使用的是英特尔 CPU，你还需要在[内核命令行](https://pve.proxmox.com/wiki/Host_Bootloader#sysboot_edit_kernel_cmdline) 中添加 `intel_iommu=on`。

如果你使用 GRUB 作为引导加载程序，则可以将 `intel_iommu=on` 添加到
`/etc/default/grub` 中的 GRUB_CMDLINE_LINUX_DEFAULT 变量，然后运行:

```bash
update-grub
```

如果你看到

```bash
W: This system is booted via proxmox-boot-tool:
```

你**没有**使用 [GRUB](https://www.gnu.org/software/grub/) 作为引导加载程序，而是使用了 [Systemd-boot](https://www.freedesktop.org/wiki/Software/systemd/systemd-boot/)。这意味着你应该在 /etc/kernel/cmdline 文件中添加 `intel_iommu=on`。如果你的硬件支持 IOMMU 直通模式，你还可以添加 `iommu=pt` 以可能提高性能。

保存你的编辑并运行:

```bash
proxmox-boot-tool refresh
```

以更新引导加载程序。

重新启动后运行:

```bash
dmesg | grep -e DMAR -e IOMMU
```

如果 PCI 直通已成功启用，你现在应该在终端中看到

```bash
DMAR: IOMMU enabled
```

### Provider

创建一个 `main.tf` 文件并列出所需的 Provider。对于此项目，我们只需要 `bpg/proxmox` Provider。

```
# main.tf
terraform {
  required_providers {
    proxmox = {
      source = "bpg/proxmox"
      version = "0.50.0"
    }
  }
}
```

接下来，我们需要配置所述 Provider。我给 Provider 起了别名 euclid，以我正在运行此提供程序的迷你电脑的主机名命名，这再次受到希腊数学家[欧几里得](https://en.wikipedia.org/wiki/Euclid)的启发。通过给 Provider 一个别名，我们可以使用相同的 Terraform 配置控制多个 Proxmox 实例。

```ruby
# main.tf
provider "proxmox" {
  alias = "euclid"
  endpoint = var.euclid.endpoint
  insecure = var.euclid.insecure
  api_token = var.euclid_auth.api_token
  ssh {
    agent = true
    username = var.euclid_auth.username
  }
  tmp_dir = "/var/tmp"
}
```

连接详细信息被分离到[变量](https://opentofu.org/docs/language/values/variables/)中，因为我更喜欢不将这些信息检入 Git。

```
# variables.tf
variable "euclid" {
  description = "Euclid Proxmox server configuration"
  type = object({
    node_name = string
    endpoint = string
    insecure = bool
  })
}
```

要在你运行 tofu-commands 时自动插入变量，你可以将它们添加到 `variables.auto.tfvars` 文件中。请参阅[文档](https://opentofu.org/docs/language/values/variables/#variable-definitions-tfvars-files)了解更多关于如何向 Terraform 文件提供变量的选项。


```
# variables.auto.tfvars
euclid = {
  node_name = "euclid"
  endpoint = "https://192.168.1.42:8006"
  insecure = true
}
```

此处我已将端点设置为 Proxmox 节点的本地网络 IP 地址。如果您已为 Proxmox 模式设置证书，则可以使用证书支持的 URL 并禁用不安全模式。请参阅[本文](https://www.derekseaman.com/2023/04/proxmox-lets-encrypt-ssl-the-easy-button.html)了解如何为 Proxmox 实例铸造
TLS 证书。

我选择了 SSH 和 API 令牌进行身份验证。由于我比较懒，所以我还重复使用了默认 root 用户。如果您在任何类型的生产环境中运行 Proxmox，我强烈建议您创建一个仅具有必要权限的单独用户！

```
# variables.tf
variable "euclid_auth" {
  description = "Euclid Proxmox 服务器身份验证"
  type = object({
    username = string
    api_token = string
  })
  sensitive = true
}
```

要为 Proxmox 生成 API 令牌，导航到 **Datacenter** 菜单下的 **Permissions** > **API Token**。作为（不安全的）快捷方式，您可以勾选 `Privilege Separation` 框，以向令牌授予与
用户相同的权限 — 同样，在任何类型的生产环境中都不推荐这样做！

![](https://blog.stonegarden.dev/articles/2024/03/proxmox-k8s-with-cilium/images/api-token-dark_hua25b075af5497cfd32d264e30a0f0c68_96242_960x0_resize_q85_h2_lanczos_3.webp)

*在 Proxmox VE 的网络界面生成 API 令牌。*

生成令牌后，将其添加为 <USER>!<TOKEN_NAME>=<TOKEN_SECRET>，如下所示。

```
# variables.auto.tfvars
euclid_auth = {
  username = "root"
  api_token = "root@pam!<TOKEN_NAME>=<TOKEN_SECRET>"
}
```

### 镜像

[#](#image)

配置好 Proxmox Provider 后，我们可以继续选择要用于 VM 的基础镜像。如前所述，我正在使用 Debian 12 Bookworm 镜像。要查找较新的镜像，请导航至 [https://cloud.debian.org/images/cloud/](https://cloud.debian.org/images/cloud/)。您需要 qcow2 格式的镜像，该镜像与 Proxmox 兼容，但您需要使用 .img 扩展名保存它。校验和是可选的，但对下载失败造成的奇怪错误进行双重检查无害。


```
# k8s-config.yaml
resource "proxmox_virtual_environment_download_file" "debian_12_generic_image" {
  provider = proxmox.euclid
  node_name = var.euclid.node_name
  content_type = "iso"
  datastore_id = "local"
  file_name = "debian-12-generic-amd64-20240201-1644.img"
  url = "https://cloud.debian.org/images/cloud/bookworm/20240211-1654/debian-12-generic-amd64-20240211-1654.qcow2"
  checksum = "b679398972ba45a60574d9202c4f97ea647dd3577e857407138b73b71a3c3c039804e40aac2f877f3969676b6c8a1ebdb4f2d67a4efa6301c21e349e37d43ef5"
  checksum_algorithm = "sha512"
}
```

### Cloud-init

为了遵循[DRY 原则](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)，我们将
利用 Terraform 的文件模板化工具。为此，我们创建了一个通用的 cloud-init 配置，可以同时用于控制平面和工作节点。

#### 变量

我确定了以下变量来模板化 cloud-init 配置

```
# variables.tf
variable "vm_user" {
  description = "VM 用户名"
  type = string
}
variable "vm_password" {
  description = "VM 密码"
  type = string
  sensitive = true
}
variable "host_pub-key" {
  description = "主机公钥"
  type = string
}
```

要连接到创建的 VM，我们需要一个用户名和一个公有 SSH 密钥。如果您已经走到这一步，但还没有一个现成的 SSH 密钥，请通过运行以下命令创建一个：

```
ssh-keygen -t ed25519 -C "<EMAIL>"
```

使用[Ed25519](https://en.wikipedia.org/wiki/EdDSA)-algorithm是[首选](https://www.brandonchecketts.com/archives/its-2023-you-should-be-using-an-ed25519-ssh-key-and-other-current-best-practices)，尽管 [RSA](https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29) 得到更广泛的支持。

为了增加一层额外的安全性，我选择为 sudo 使用密码。正如 [cloud-init 文档](https://cloudinit.readthedocs.io/en/latest/reference/examples.html#including-users-and-groups)所述，您不提供明文密码，而是提供其哈希版本。
该文档还警告说，哈希密码很容易被例如 *John the Ripper* 破解，因此请谨慎使用此功能。

如果您没有 mkpasswd，则可以运行
```
docker run -it --rm alpine mkpasswd --method=SHA-512 <PASSWORD>
```
来创建适合 cloud-init 的哈希密码。

为了方便起见，我还添加了 Kubernetes 和 Cilium CLI 版本的变量。

```
# variables.tf
variable "k8s-version" {
  description = "Kubernetes version"
  type        = string
}

variable "cilium-cli-version" {
  description = "Cilium CLI version"
  type        = string
}

```

在涉及 DNS 配置时，我无法完全弄清楚所有活动部分。不过我认为它与 [systemd-resolved](https://wiki.archlinux.org/title/systemd-resolved) 和 [netplan](https://netplan.readthedocs.io/en/stable/) 有关。查看 `/etc/resolv.conf`，在其中一台虚拟机中，我们看到它由 systemd-resolved 管理。我的理论是 systemd-resolved 从 netplan 通过 `/etc/netplan/50-cloud-init.yaml` 获取其配置。netplan 的配置似乎源自 Proxmox **System** > **DNS** 设置，我想这有道理。

这本身应该是可以的，但 `search-entry` 造成的麻烦比我想承认的还要多。例如，运行 `curl` 或 `ping` 直接从虚拟机工作，但尝试从 Kubernetes 编排的容器内部执行相同的操作会将搜索域附加到查询！我敢肯定可以通过 [CoreDNS](https://github.com/coredns/coredns) [咒语](https://en.wikipedia.org/wiki/Incantation) 或其他形式的巫术来解决此问题，但我通过将搜索域设置为 “.” 找到了一个令人满意的解决方案。

```
# variables.tf
variable "vm_dns" {
  description = "DNS config for VMs"
  type        = object({
    domain  = string
    servers = list(string)
  })
}

```

上述变量的示例值是

```
# variables.auto.tfvars
vm_dns = {
  domain  = "."
  servers = ["1.1.1.1", "8.8.8.8"]
}

vm_user      = "<USER>"
vm_password  = "<HASHED PASSWORD>"
host_pub-key = "<PUBLIC SSH KEY>"

k8s-version        = "1.29"
cilium-cli-version = "0.16.4"

```

#### 模板化

创建一个 `cloud-init/k8s-common.yaml.tftpl` 文件并开始填充它

```
users:
  - name: ${username}
    passwd: ${password}
    lock_passwd: false
    groups: [ adm, cdrom, dip, plugdev, lxd, sudo ]
    shell: /bin/bash
    ssh_authorized_keys:
      - ${pub-key}
#    sudo: ALL=(ALL) NOPASSWD:ALL

```

在这里，我们使用前面创建的哈希密码对 `user` 进行模板化。通过不锁定密码，我们可以使用它来运行带有 `sudo` 的命令。或者，您可以添加 `sudo: ALL=(ALL) NOPASSWD:ALL` 并锁定或删除密码以仍然能够发出 `sudo` 命令。

添加您希望用户拥有的组。有关最常见组的概述，请参阅 Debian wiki 上的 [SystemGroups](https://wiki.debian.org/SystemGroups) 和 [LXD](https://wiki.debian.org/LXD)。如果您想进一步自定义用户，请参阅 [cloud-init 文档](https://cloudinit.readthedocs.io/en/latest/reference/modules.html#users-and-groups)。

接下来在同一个 `k8s-common.yaml.tftpl` 文件中，我们设置主机名并告诉 cloud-init 在设置期间更新和升级软件包。还可以在这里设置时区。

```
hostname: ${hostname}
package_update: true
package_upgrade: true
timezone: Europe/Oslo
```

接下来，我们配置 IPv4 转发并让 iptables 查看桥接流量，按照 [Kubernetes 先决条件文档](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#install-and-configure-prerequisites) 进行操作。在 `runcmd` 部分中，我们将运行 `modprobe overlay` 和 `br_netfilter` 以应用此配置。

```
write_files:
  - path: /etc/modules-load.d/k8s.conf
    content: |
      overlay
      br_netfilter      
  - path: /etc/sysctl.d/k8s.conf
    content: |
      net.bridge.bridge-nf-call-ip6tables = 1
      net.bridge.bridge-nf-call-iptables  = 1
      net.ipv4.ip_forward                 = 1      
  - path: /etc/ssh/sshd_config.d/01-harden-ssh.conf
    content: |
      PermitRootLogin no
      PasswordAuthentication no
      ChallengeResponseAuthentication no
      UsePAM no      
```

我们还添加了一个文件来通过不允许 `root` 登录、禁止密码身份验证和所有类型的“*键盘交互*”身份验证以及禁用 [可插拔身份验证模块](https://linux.die.net/man/8/pam) (PAM) 来强化 SSH。

在 `packages` 部分中，我们添加了 [qemu-guest-agent](https://pve.proxmox.com/wiki/Qemu-guest-agent) 以改善客户机和主机操作系统之间的通信。我们还需要 [kubeadm 依赖项](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#installing-kubeadm-kubelet-and-kubectl) 以及一些工具来简化调试。

```
packages:
  - qemu-guest-agent
  - apt-transport-https
  - ca-certificates
  - curl
  - gpg
  - open-iscsi
  - net-tools
  - jq
  - vim
```

最后一部分是运行适当的命令来安装 `kubeadm`，并 [为 containerd 配置 systemd cgroup 驱动程序](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#containerd-systemd)。我们还添加了一个模板命令，我们将在不同的节点上使用它来运行 `kubeadm` 命令。

```
runcmd:
  - systemctl enable qemu-guest-agent
  - systemctl start qemu-guest-agent
  - localectl set-locale LANG=en_US.UTF-8
  - curl -fsSL https://pkgs.k8s.io/core:/stable:/v${k8s-version}/deb/Release.key | gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
  - echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v${k8s-version}/deb/ /' | tee /etc/apt/sources.list.d/kubernetes.list
  - apt update
  - apt install -y kubelet kubeadm kubectl
  - apt-mark hold kubelet kubeadm kubectl
  - apt install -y runc containerd
  - containerd config default | tee /etc/containerd/config.toml
  - sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml
  - modprobe overlay
  - modprobe br_netfilter
  - sysctl --system
  - systemctl restart containerd
  - ${kubeadm-cmd}
```

到目前为止，本节中的所有代码段都应位于 `cloud-init/k8s-common.yaml.tftpl` 文件中。

对于工作器 cloud-init 配置，我们只需在一个名为 `cloud-init/k8s-worker.yaml.tftpl` 的文件中重复使用完整模板

```
#cloud-config
${common-config}
```

对于控制平面节点，我们创建一个 `cloud-init/k8s-control-plane.yaml.tftpl` 文件，其中添加了移动 `kubeconfig` 文件、安装 [cilium-cli](https://github.com/cilium/cilium-cli) 以及 [Cilium CNI](https://docs.cilium.io/en/stable/) 的说明。

```
#cloud-config
${common-config}
  - mkdir -p /home/${username}/.kube
  - cp /etc/kubernetes/admin.conf /home/${username}/.kube/config
  - chown -R ${username}:${username} /home/${username}/.kube
  - curl -sfLO https://github.com/cilium/cilium-cli/releases/download/v${cilium-cli-version}/cilium-linux-amd64.tar.gz
  - tar xzvfC cilium-linux-amd64.tar.gz /usr/local/bin
  - rm cilium-linux-amd64.tar.gz
  - ${cilium-cli-cmd}
```

#### 配置

接下来，在将 cloud-init 模板作为代码段上传到 Proxmox 之前，我们为其提供值。

```ruby
resource "proxmox_virtual_environment_file" "cloud-init-ctrl-01" {
  provider     = proxmox.euclid
  node_name    = var.euclid.node_name
  content_type = "snippets"
  datastore_id = "local"

  source_raw {
    data = templatefile("./cloud-init/k8s-control-plane.yaml.tftpl", {
      common-config = templatefile("./cloud-init/k8s-common.yaml.tftpl", {
        hostname    = "k8s-ctrl-01"
        username    = var.vm_user
        password    = var.vm_password
        pub-key     = var.host_pub-key
        k8s-version = var.k8s-version

        kubeadm-cmd = "kubeadm init --skip-phases=addon/kube-proxy"

      })
      username           = var.vm_user
      cilium-cli-version = var.cilium-cli-version

      cilium-cli-cmd     = "HOME=/home/${var.vm_user} KUBECONFIG=/etc/kubernetes/admin.conf cilium install --set kubeProxyReplacement=true"

    })
    file_name = "cloud-init-k8s-ctrl-01.yaml"
  }
}
```

此处我们利用内置的 [templatefile 函数](https://opentofu.org/docs/language/functions/templatefile/)来嵌套模板文件。对于控制平面节点，我们运行 
`kubeadm init --skip-phases=addon/kube-proxy`（第 15 行）以启动集群。Cilium 将替换
`kube-proxy`，如 `cilium install --set kubeProxyReplacement=true`（第 19 行）命令中所示。

```ruby
resource "proxmox_virtual_environment_file" "cloud-init-work-01" {
  provider     = proxmox.euclid
  node_name    = var.euclid.node_name
  content_type = "snippets"
  datastore_id = "local"

  source_raw {
    data = templatefile("./cloud-init/k8s-worker.yaml.tftpl", {
      common-config = templatefile("./cloud-init/k8s-common.yaml.tftpl", {
        hostname    = "k8s-work-01"
        username    = var.vm_user
        password    = var.vm_password
        pub-key     = var.host_pub-key
        k8s-version = var.k8s-version

        kubeadm-cmd = module.kubeadm-join.stdout

      })
    })
    file_name = "cloud-init-k8s-work-01.yaml"
  }
}
```

为了将更多节点加入我们的集群，我们需要一个来自控制平面节点的令牌。我们在引导阶段从控制平面节点创建此令牌，并在工作器节点上 `kubeadm join` 命令中使用它（第 15 行）。我们稍后会再回到这一点。

#### 代码段

在我们可以将 cloud-init 配置作为所谓的 *代码段* 上传之前，我们需要在 Proxmox 中的目标数据存储上启用内容类型，如[提供程序文档](https://github.com/bpg/terraform-provider-proxmox/blob/e87bc4b941564aace95d60ff987b7ec0d508b437/docs/guides/cloud-init.md)中所述。

要启用代码段内容，请在 Proxmox VE Web 界面中导航到 **Datacenter** 下的 **Storage**，
双击相应行，然后在 **Content** 下拉菜单中添加代码段。

![](https://blog.stonegarden.dev/articles/2024/03/proxmox-k8s-with-cilium/images/snippets-dark_hu5d976c6079a9a6fde9dff1500b500c76_123334_960x0_resize_q85_h2_lanczos_3.webp)

*在 Proxmox VE Web 界面中启用片段内容。*

### 虚拟机
[#](#virtual-machines)

现在我们已经准备好了操作系统映像和 cloud-init 配置，是时候配置虚拟机了。作为概念验证，我们将创建一个控制平面节点并加入一个孤立的工作器节点。

如果你想进一步简化部署，则可以在控制平面节点上允许常规工作负载，从而只需要一个节点用于 Kubernetes “集群”。这可以通过运行来删除：

```bash
kubectl taint nodes --all node-role.kubernetes.io/control-plane-
```

以及为单个控制平面节点准备的 kubeconfig 文件。

[Proxmox VE Wiki](https://pve.proxmox.com/wiki/Qemu/KVM_Virtual_Machines) 是有关虚拟机配置详细信息的宝贵资源。为了帮助驾驭所有杠杆和刻度盘，我们选择的 Provider 幸运地提供了[文档](https://github.com/bpg/terraform-provider-proxmox/blob/014b59e04f30fc08bc512f68cf471fe2cfdc481c/docs/resources/virtual_environment_vm.md)，介绍如何开始。

#### 控制器平面节点

我将尝试解释我选择的选项，不过如果你不同意或知道更好的方法，我洗耳恭听。

第一个有趣的配置是第 11 行的 `machine-type`。将其设置为 `Q35` 提供了一个虚拟 PCIe 总线，允许我们直通 PCIe 设备。

下一个更改是第 12 行的 `scsi_hardware`。provider 默认值为 `virtio-scsi-pci`，但将其更改为 `virtio-scsi-single` — 也是 [Proxmox 默认值](https://pve.proxmox.com/wiki/QEMU/KVM_Virtual_Machines#qm_hard_disk)，启用 IO 线程，并且应该可以[提高性能](https://kb.blockbridge.com/technote/proxmox-aio-vs-iouring/#what-are-iothread)。

由于我们计划通过 PCIe 传输，因此我们应该将 BIOS 类型从 [SeaBIOS 更改为 OVMF](https://pve.proxmox.com/wiki/QEMU/KVM_Virtual_Machines#qm_bios_and_uefi)（第 13 行）。这意味着我们还必须创建一个 EFI 磁盘（第 29 行）。

我们已将 CPU [类型](https://pve.proxmox.com/wiki/QEMU/KVM_Virtual_Machines#qm_cpu) 更改为 host 以获得最大性能（第 17 行）。

如果您计划在具有不同 CPU 的机器之间迁移 VM，则您可能应该将其设置为 x86-64-v2-AES。

在涉及磁盘时，我选择了高速缓存直写（第 39 行），根据 [文档](https://pve.proxmox.com/wiki/Performance_Tweaks#Disk_Cache) 平衡安全性与读取性能。

```ruby
 1
 2
 3
 4
 5
 6
 7
 8
 9
10

11

12

13

14
15
16

17

18
19
20
21
22
23
24
25
26
27
28

29

30
31
32
33
34
35
36
37
38

39

40
41
42
43
44
45
46
47

48

49
50
51

52

53
54
55
56

57

58

59
60
61

62

63

64
65
66
67

68

69
70

	
resource "proxmox_virtual_environment_vm" "k8s-ctrl-01" {
  provider  = proxmox.euclid
  node_name = var.euclid.node_name

  name        = "k8s-ctrl-01"
  description = "Kubernetes Control Plane 01"
  tags        = ["k8s", "control-plane"]
  on_boot     = true
  vm_id       = 8001


  machine       = "q35"

  scsi_hardware = "virtio-scsi-single"

  bios          = "ovmf"


  cpu {
    cores = 4

    type  = "host"

  }

  memory {
    dedicated = 4096
  }

  network_device {
    bridge      = "vmbr0"
    mac_address = "BC:24:11:2E:C0:01"
  }


  efi_disk {

    datastore_id = "local-zfs"
    file_format  = "raw" // To support qcow2 format
    type         = "4m"
  }

  disk {
    datastore_id = "local-zfs"
    file_id      = proxmox_virtual_environment_download_file.debian_12_generic_image.id
    interface    = "scsi0"

    cache        = "writethrough"

    discard      = "on"
    ssd          = true
    size         = 32
  }

  boot_order = ["scsi0"]

  agent {

    enabled = true

  }

  operating_system {

    type = "l26" # Linux Kernel 2.6 - 6.X.

  }

  initialization {
    dns {

      domain  = var.vm_dns.domain

      servers = var.vm_dns.servers

    }
    ip_config {
      ipv4 {

        address = "192.168.1.100/24"

        gateway = "192.168.1.1"

      }
    }

    datastore_id      = "local-zfs"

    user_data_file_id = proxmox_virtual_environment_file.cloud-init-ctrl-01.id

  }
}
```

在第 46 行，我们手动启用 QEMU guest agent 功能。

为了获得更好的 VM 优化，我们可以将 OS 类型设置为 l26（第 52 行），适用于使用高于 2.6 的 Linux 内核版本的 OS。

在初始化阶段，我们明确设置 DNS 服务器和搜索域（第 57-58 行）以规避 [Cloud-init 部分](#variables) 中提到的 DNS 问题。

IP 配置（第 62-63 行）也可能是变量，但这有效。确保不使用冲突的 IP。

在最后，我们输入我们之前制作的 Cloud-init 配置（第 68 行）。

在创建 VM 后，我们获取 IP 地址

```ruby
output "ctrl_01_ipv4_address" {
  depends_on = [proxmox_virtual_environment_vm.k8s-ctrl-01]
  value      = proxmox_virtual_environment_vm.k8s-ctrl-01.ipv4_addresses[1][0]
}
```

并将其存储在文件中。

```
resource "local_file" "ctrl-01-ip" {
  content         = proxmox_virtual_environment_vm.k8s-ctrl-01.ipv4_addresses[1][0]
  filename        = "output/ctrl-01-ip.txt"
  file_permission = "0644"
}
```

这主要是为了让进程等待第一个节点创建，但它失败了，所以我使用 Invicton Labs 的 [shell-data](https://github.com/Invicton-Labs/terraform-external-shell-data) 采用了睡眠函数，以便在每个计划/应用中运行。

```
module "sleep" {
  depends_on   = [local_file.ctrl-01-ip]
  source       = "Invicton-Labs/shell-data/external"
  version      = "0.4.2"
  command_unix = "sleep 150"
}

```

睡眠函数旨在给予 kubeadm 足够的时间来发挥其作用，然后再使用 Inviction Labs 的 [shell-resource](https://github.com/Invicton-Labs/terraform-external-shell-resource)（仅在输入变量更改时重新运行）来获取 kubeconfig 文件

```
module "kube-config" {
  depends_on   = [module.sleep]
  source       = "Invicton-Labs/shell-resource/external"
  version      = "0.4.1"
  command_unix = "ssh -o StrictHostKeyChecking=no ${var.vm_user}@${local_file.ctrl-01-ip.content} cat /home/${var.vm_user}/.kube/config"
}

```

然后，我们将此命令的输出存储在本地文件中

```
resource "local_file" "kube-config" {
  content         = module.kube-config.stdout
  filename        = "output/config"
  file_permission = "0600"
}

```

请注意，我们在这里为 ssh 使用[ -o StrictHostKeyChecking=no](https://stackoverflow.com/questions/21383806/how-can-i-force-ssh-to-accept-a-new-host-fingerprint-from-the-command-line) 参数，这通常不建议使用。

由于我们已经违反了安全最佳实践，我们以类似的方式获取工作节点的 kubeadm 加入令牌

```
module "kubeadm-join" {
  depends_on   = [local_file.kube-config]
  source       = "Invicton-Labs/shell-resource/external"
  version      = "0.4.1"
  command_unix = "ssh -o StrictHostKeyChecking=no ${var.vm_user}@${local_file.ctrl-01-ip.content} /usr/bin/kubeadm token create --print-join-command"
}

```

我绝不满意此流程，并会感谢任何改进建议。

#### 工作节点

工作节点的配置与控制平面节点的配置非常相似，但 RAM 更多（第 21 行），并且安装了 PCIe 设备（第 71 行）。

```ruby
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20

21

22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70

71

72
73
74
75
76
77
78
79
80

	
resource "proxmox_virtual_environment_vm" "k8s-work-01" {
  provider  = proxmox.euclid
  node_name = var.euclid.node_name

  name        = "k8s-work-01"
  description = "Kubernetes Worker 01"
  tags        = ["k8s", "worker"]
  on_boot     = true
  vm_id       = 8101

  machine       = "q35"
  scsi_hardware = "virtio-scsi-single"
  bios          = "ovmf"

  cpu {
    cores = 4
    type  = "host"
  }

  memory {

    dedicated = 8192

  }

  network_device {
    bridge      = "vmbr0"
    mac_address = "BC:24:11:2E:AE:01"
  }

  efi_disk {
    datastore_id = "local-zfs"
    file_format  = "raw" // To support qcow2 format
    type         = "4m"
  }

  disk {
    datastore_id = "local-zfs"
    file_id      = proxmox_virtual_environment_download_file.debian_12_generic_image.id
    interface    = "scsi0"
    cache        = "writethrough"
    discard      = "on"
    ssd          = true
    size         = 32
  }

  boot_order = ["scsi0"]

  agent {
    enabled = true
  }

  operating_system {
    type = "l26" # Linux Kernel 2.6 - 6.X.
  }

  initialization {
    dns {
      domain  = var.vm_dns.domain
      servers = var.vm_dns.servers
    }
    ip_config {
      ipv4 {
        address = "192.168.1.110/24"
        gateway = "192.168.1.1"
      }
    }

    datastore_id      = "local-zfs"
    user_data_file_id = proxmox_virtual_environment_file.cloud-init-work-01.id
  }


  hostpci {

    # Passthrough iGPU
    device  = "hostpci0"
    #id     = "0000:00:02"
    mapping = "iGPU"
    pcie    = true
    rombar  = true
    xvga    = false
  }
}
```

为了让 hostpci 设置与提供程序一起使用，我们首先需要创建一个映射。在 Proxmox VE Web 界面中导航到 **Datacenter ** 下的 **Resource Mappings**，然后单击 *PCI Devices* 下的 *Add*。

![](https://blog.stonegarden.dev/articles/2024/03/proxmox-k8s-with-cilium/images/resource-mapping-dark_hu6fa6f5f837f86980e25ae32b735fead8_154206_960x0_resize_q85_h2_lanczos_3.webp)

在这里，我们添加了 N100 iGPU，以便在工作节点上使用，例如 [QuickSync](https://en.wikipedia.org/wiki/Intel_Quick_Sync_Video) 硬件视频解码。

最后，我们还将工作节点的 IP 输出到文件

```ruby
output "work_01_ipv4_address" {
  depends_on = [proxmox_virtual_environment_vm.k8s-work-01]
  value      = proxmox_virtual_environment_vm.k8s-work-01.ipv4_addresses[1][0]
}

resource "local_file" "work-01-ip" {
  content         = proxmox_virtual_environment_vm.k8s-work-01.ipv4_addresses[1][0]
  filename        = "output/work-01-ip.txt"
  file_permission = "0644"
}
```

## Kubernetes

假设您已成功运行

```
tofu apply
```

你现在应该拥有一个与 Cilium 搭配使用的 Kubernetes 集群 

为双重检查一切是否正常，你可以运行

```
kubectl --kubeconfig output/config get po -A -o wide
```

从您的本地机器查看您刚创建的集群上所有 pod 的状态。

如果一切都正常，您应该会看到类似以下内容

```bash
NAMESPACE NAME READY STATUS RESTARTS AGE IP NODE NOMINATED NODE READINESS GATES
kube-system cilium-operator-577fd997b-sln7f 1/1 Running 0 9m 192.168.1.110 k8s-work-01 <none> <none>
kube-system cilium-t8tgg 1/1 Running 0 9m 192.168.1.110 k8s-work-01 <none> <none>
kube-system cilium-zthd4 1/1 Running 0 9m 192.168.1.100 k8s-ctrl-01 <none> <none>
kube-system coredns-76f75df574-8rqc4 1/1 Running 0 10m 10.0.0.83 k8s-ctrl-01 <none> <none>
kube-system coredns-76f75df574-ct4ml 1/1 Running 0 10m 10.0.0.213 k8s-ctrl-01 <none> <none>
kube-system etcd-k8s-ctrl-01 1/1 Running 0 10m 192.168.1.100 k8s-ctrl-01 <none> <none>
kube-system kube-apiserver-k8s-ctrl-01 1/1 Running 0 10m 192.168.1.100 k8s-ctrl-01 <none> <none>
kube-system kube-controller-manager-k8s-ctrl-01 1/1 Running 0 10m 192.168.1.100 k8s-ctrl-01 <none> <none>
kube-system kube-scheduler-k8s-ctrl-01 1/1 Running 0 10m 192.168.1.100 k8s-ctrl-01 <none> <none>
```

在 k8s-ctrl-01 和 k8s-work-01 上都运行了 Pod。

有关下一步要做什么的灵感，你可以查看我的“mini-kubernetes”GitLab 仓库，或查看我在 GitHub 上较大的家庭实验室仓库。两者都使用 Argo CD + Kustomize + Helm 方法进行声明式 GitOps 配置。

## 问题诊断


这种设置中包含很多运动部件，这导致故障排除变得困难。

通过再次运行下面的命令可以解决我在此方法中遇到的大多数错误

```
tofu apply
```

如果 Kubernetes 挂了，这可能是 Cilium 配置的问题，而这种情况应该运行

```bash
cilium status
```

可能有助于你解决问题。

在这个设置中我发现在不必禁用 swap 时，但如果遇到问题，检查是否已禁用它可能是需要考虑的，尝试运行

```bash
free -m
```

确保 `swap` 返回 0 。

禁用交换使 kubelet 正常运行

```
sudo swapoff -a
```

并在 `/etc/fstab` 中注释掉 swap 以在引导时禁用它

```
sudo sed -e '/swap/ s/^#*/#/' -i /etc/fstab
```

与具有相同 IP 的不同机器建立连接将使 `ssh` 警告您有关潜在的[中间人](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)攻击。只要您在本地网络上，这可能很安全，并且您可以从 `~/.ssh/known_hosts` 文件中删除冒犯的 IP。

## 总结

目录结构

```
❯ tree
.
├── cloud-init
│ ├── k8s-common.yaml.tftpl
│ ├── k8s-control-plane.yaml.tftpl
│ └── k8s-worker.yaml.tftpl
├── k8s-config.tf
├── k8s-vm-control-plane.tf
├── k8s-vm-worker.tf
├── main.tf
├── variables.auto.tfvars
└── variables.tf
```

提供程序配置文件主文件

```
# main.tf
terraform {
  required_providers {
    proxmox = {
      source = "bpg/proxmox"
      version = "0.50.0"
    }
  }
}

provider "proxmox" {
  alias = "euclid"
  endpoint = var.euclid.endpoint
  insecure = var.euclid.insecure
  api_token = var.euclid_auth.api_token
  ssh {
    agent = true
    username = var.euclid_auth.username
  }
  tmp_dir = "/var/tmp"
}
```

所有定义的变量

```
# variables.tf
variable "euclid" {
  description = "Proxmox server configuration for Euclid"
  type = object({
    node_name = string
    endpoint = string
    insecure = bool
  })
}

variable "euclid_auth" {
  description = "Euclid Proxmox server authentication"
  type = object({
    username = string
    api_token = string
  })
  sensitive = true
}

variable "vm_dns" {
  description = "DNS configuration for VMs"
  type = object({
    domain = string
    servers = list(string)
  })
}

variable "vm_user" {
  description = "VM username"
  type = string
}

variable "vm_password" {
  description = "VM password"
  type = string
  sensitive = true
}

variable "host_pub-key" {
  description = "Host public key"
  type = string
}

variable "k8s-version" {
  description = "Kubernetes version"
  type = string
}

variable "cilium-cli-version" {
  description = "Cilium CLI version"
  type = string
}
```

所有的变量值

```
# variables.auto.tfvars
euclid = {
  node_name = "euclid"
  endpoint = "https://192.168.1.42:8006"
  insecure = true
}

euclid_auth = {
  username = "root"
  api_token = "root@pam!<TOKEN_NAME>=<TOKEN_SECRET>"
}

vm_dns = {
  domain = "."
  servers = ["1.1.1.1", "8.8.8.8"]
}

vm_user = "<USER>"
vm_password = "<HASHED PASSWORD>"
host_pub-key = "<PUBLIC SSH KEY>"
k8s-version = "1.29"
cilium-cli-version = "0.16.4"
```

通用配置

```ruby
# k8s-config.tf
resource "proxmox_virtual_environment_download_file" "debian_12_generic_image" {
  provider     = proxmox.euclid
  node_name    = var.euclid.node_name
  content_type = "iso"
  datastore_id = "local"

  file_name          = "debian-12-generic-amd64-20240201-1644.img"
  url                = "https://cloud.debian.org/images/cloud/bookworm/20240211-1654/debian-12-generic-amd64-20240211-1654.qcow2"
  checksum           = "b679398972ba45a60574d9202c4f97ea647dd3577e857407138b73b71a3c3c039804e40aac2f877f3969676b6c8a1ebdb4f2d67a4efa6301c21e349e37d43ef5"
  checksum_algorithm = "sha512"
}

# Make sure the "Snippets" content type is enabled on the target datastore in Proxmox before applying the configuration below.
# https://github.com/bpg/terraform-provider-proxmox/blob/main/docs/guides/cloud-init.md
resource "proxmox_virtual_environment_file" "cloud-init-ctrl-01" {
  provider     = proxmox.euclid
  node_name    = var.euclid.node_name
  content_type = "snippets"
  datastore_id = "local"

  source_raw {
    data = templatefile("./cloud-init/k8s-control-plane.yaml.tftpl", {
      common-config = templatefile("./cloud-init/k8s-common.yaml.tftpl", {
        hostname    = "k8s-ctrl-01"
        username    = var.vm_user
        password    = var.vm_password
        pub-key     = var.host_pub-key
        k8s-version = var.k8s-version
        kubeadm-cmd = "kubeadm init --skip-phases=addon/kube-proxy"
      })
      username           = var.vm_user
      cilium-cli-version = var.cilium-cli-version
      cilium-cli-cmd     = "HOME=/home/${var.vm_user} KUBECONFIG=/etc/kubernetes/admin.conf cilium install --set kubeProxyReplacement=true"
    })
    file_name = "cloud-init-k8s-ctrl-01.yaml"
  }
}

resource "proxmox_virtual_environment_file" "cloud-init-work-01" {
  provider     = proxmox.euclid
  node_name    = var.euclid.node_name
  content_type = "snippets"
  datastore_id = "local"

  source_raw {
    data = templatefile("./cloud-init/k8s-worker.yaml.tftpl", {
      common-config = templatefile("./cloud-init/k8s-common.yaml.tftpl", {
        hostname    = "k8s-work-01"
        username    = var.vm_user
        password    = var.vm_password
        pub-key     = var.host_pub-key
        k8s-version = var.k8s-version
        kubeadm-cmd = module.kubeadm-join.stdout
      })
    })
    file_name = "cloud-init-k8s-work-01.yaml"
  }
}
```

通用 cloud-init 配置

```ruby
users:
  - name: ${username}
    passwd: ${password}
    lock_passwd: false
    groups: [ adm, cdrom, dip, plugdev, lxd, sudo ]
    shell: /bin/bash
    ssh_authorized_keys:
      - ${pub-key}
    #sudo: ALL=(ALL) NOPASSWD:ALL

hostname: ${hostname}
package_update: true
package_upgrade: true
timezone: Europe/Oslo

write_files:
  - path: /etc/modules-load.d/k8s.conf
    content: |
      overlay
      br_netfilter
  - path: /etc/sysctl.d/k8s.conf
    content: |
      net.bridge.bridge-nf-call-ip6tables = 1
      net.bridge.bridge-nf-call-iptables  = 1
      net.ipv4.ip_forward                 = 1
  - path: /etc/ssh/sshd_config.d/01-harden-ssh.conf
    content: |
      PermitRootLogin no
      PasswordAuthentication no
      ChallengeResponseAuthentication no
      UsePAM no

packages:
  - qemu-guest-agent
  - net-tools
  - vim
  - apt-transport-https
  - ca-certificates
  - curl
  - gpg
  - open-iscsi
  - jq

runcmd:
  - systemctl enable qemu-guest-agent
  - systemctl start qemu-guest-agent
  - localectl set-locale LANG=en_US.UTF-8
  - curl -fsSL https://pkgs.k8s.io/core:/stable:/v${k8s-version}/deb/Release.key | gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
  - echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v${k8s-version}/deb/ /' | tee /etc/apt/sources.list.d/kubernetes.list
  - apt update
  - apt install -y kubelet kubeadm kubectl
  - apt-mark hold kubelet kubeadm kubectl
  - apt install -y runc containerd
  - containerd config default | tee /etc/containerd/config.toml
  - sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml
  - modprobe overlay
  - modprobe br_netfilter
  - sysctl --system
  - systemctl restart containerd
  - ${kubeadm-cmd}
```


控制平面节点的 Cloud-init 配置

```bash
#cloud-config
${common-config}
  - mkdir -p /home/${username}/.kube
  - cp /etc/kubernetes/admin.conf /home/${username}/.kube/config
  - chown -R ${username}:${username} /home/${username}/.kube
  - curl -sfLO https://github.com/cilium/cilium-cli/releases/download/v${cilium-cli-version}/cilium-linux-amd64.tar.gz
  - tar xzvfC cilium-linux-amd64.tar.gz /usr/local/bin
  - rm cilium-linux-amd64.tar.gz
  - ${cilium-cli-cmd}
```

工作节点的 Cloud-init 配置

```
#cloud-config
${common-config}
```

控制平面节点的 VM 配置

```ruby
# k8s-vm-control-plane.tf
resource "proxmox_virtual_environment_vm" "k8s-ctrl-01" {
  provider  = proxmox.euclid
  node_name = var.euclid.node_name

  name        = "k8s-ctrl-01"
  description = "Kubernetes Control Plane 01"
  tags        = ["k8s", "control-plane"]
  on_boot     = true
  vm_id       = 8001

  machine       = "q35"
  scsi_hardware = "virtio-scsi-single"
  bios          = "ovmf"

  cpu {
    cores = 4
    type  = "host"
  }

  memory {
    dedicated = 4096
  }

  network_device {
    bridge      = "vmbr0"
    mac_address = "BC:24:11:2E:C0:01"
  }

  efi_disk {
    datastore_id = "local-zfs"
    file_format  = "raw" // To support qcow2 format
    type         = "4m"
  }

  disk {
    datastore_id = "local-zfs"
    file_id      = proxmox_virtual_environment_download_file.debian_12_generic_image.id
    interface    = "scsi0"
    cache        = "writethrough"
    discard      = "on"
    ssd          = true
    size         = 32
  }

  boot_order = ["scsi0"]

  agent {
    enabled = true
  }

  operating_system {
    type = "l26" # Linux Kernel 2.6 - 6.X.
  }

  initialization {
    dns {
      domain  = var.vm_dns.domain
      servers = var.vm_dns.servers
    }
    ip_config {
      ipv4 {
        address = "192.168.1.100/24"
        gateway = "192.168.1.1"
      }
    }

    datastore_id      = "local-zfs"
    user_data_file_id = proxmox_virtual_environment_file.cloud-init-ctrl-01.id
  }
}

output "ctrl_01_ipv4_address" {
  depends_on = [proxmox_virtual_environment_vm.k8s-ctrl-01]
  value      = proxmox_virtual_environment_vm.k8s-ctrl-01.ipv4_addresses[1][0]
}

resource "local_file" "ctrl-01-ip" {
  content         = proxmox_virtual_environment_vm.k8s-ctrl-01.ipv4_addresses[1][0]
  filename        = "output/ctrl-01-ip.txt"
  file_permission = "0644"
}

module "sleep" {
  depends_on   = [local_file.ctrl-01-ip]
  source       = "Invicton-Labs/shell-data/external"
  version      = "0.4.2"
  command_unix = "sleep 150"
}

module "kube-config" {
  depends_on   = [module.sleep]
  source       = "Invicton-Labs/shell-resource/external"
  version      = "0.4.1"
  command_unix = "ssh -o StrictHostKeyChecking=no ${var.vm_user}@${local_file.ctrl-01-ip.content} cat /home/${var.vm_user}/.kube/config"
}

resource "local_file" "kube-config" {
  content         = module.kube-config.stdout
  filename        = "output/config"
  file_permission = "0600"
}

module "kubeadm-join" {
  depends_on   = [local_file.kube-config]
  source       = "Invicton-Labs/shell-resource/external"
  version      = "0.4.1"
  command_unix = "ssh -o StrictHostKeyChecking=no ${var.vm_user}@${local_file.ctrl-01-ip.content} /usr/bin/kubeadm token create --print-join-command"
}
```