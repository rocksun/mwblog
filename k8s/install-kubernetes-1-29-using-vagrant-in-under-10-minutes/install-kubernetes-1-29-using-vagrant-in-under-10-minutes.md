<!--
title: 10分钟Vagrant安装Kubernetes 1.29
cover: ./cover.png
-->

逐步安装Kubernetes 1.29集群，包括1个主节点和3个工作节点，在Ubuntu虚拟机上使用Vagrant。

> 译自 [Install Kubernetes 1.29 using Vagrant in under 10 minutes](https://itnext.io/install-kubernetes-1-29-using-vagrant-in-under-10-minutes-2fce7108af6d)。作者 Akriotis Kyriakos。

## 我们的目标是什么？

完成本文的所有步骤后，您将拥有一个在Ubuntu虚拟机上运行的自动化无人值守脚本，用于创建本地 Kubernetes 1.29 集群。

## 我们需要什么？

1. **Vagrant** https://www.vagrantup.com/docs/installation 。Vagrant是由HashiCorp开发的开源工具，用于创建和管理虚拟化开发环境。它允许用户轻松配置和复制开发设置，跨不同机器进行复制。
2. **VirtualBox** https://www.virtualbox.org。VirtualBox是由Oracle提供的免费开源虚拟化平台。
3. **4个虚拟机**。一个用于主节点（3GB RAM，1 vCPU），其他三个作为工作节点（3GB RAM，1 vCPU）。它们将通过Vagrant自动进行配置，这实际上是本文的部分范围。
4. 一个额外的**VirtualBox Host-Only网络**。Host-Only网络是一种网络配置，允许虚拟机与主机系统进行通信，但**不能**与外部网络通信。它为虚拟机和主机之间提供了一个私有网络，用于在虚拟机和主机之间进行隔离通信。这对于开发和测试场景非常有用，特别是在想要创建封闭网络环境的情况下。

## 先决条件

为了进行管理和配置任务，Vagrant会自动将默认的VirtualBox NAT网络绑定到每个虚拟机上（请注意，**不是**命名网络！）。

我们将指示Vagrant绑定一个额外的Host-Only网络，首先需要在VirtualBox中创建该网络。

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*lF7slOb3CFkuf8f-HHZjpQ.png)

在我的情况下，我选择了一个CIDR为192.168.57.0/24的网络，如果您选择或创建了不同地址空间的网络，您需要调整Vagrantfile。确保您已启用DHCP服务器。

克隆包含必要文件的存储库，然后让我们开始：

## 分析Vagrantfile

Vagrantfile是Vagrant使用的配置文件；它用[Ruby](https://www.ruby-lang.org/en/)编写，定义了每个环境的设置和配置，指定了基本操作系统盒、网络设置、硬件规格和许多其他自定义内容的参数。它扮演着在不同机器上创建和配置可重复和一致的**虚拟化**开发环境的蓝图的角色。

> 如果您的系统尚未安装Vagrant，请访问[此链接](https://developer.hashicorp.com/vagrant/install)获取安装说明。

Vagrantfile的第一个元素（第1-5行）是全局配置变量，我们稍后将将其用作在主节点和工作节点上执行的脚本中的环境变量。您可以随意更改它们，但请确保master_node_ip属于我们先前创建的Host-Only网络的地址空间。

```ruby
domain = "kubernetes.lab"
control_plane_endpoint = "k8s-master." + domain + ":6443"
pod_network_cidr = "10.244.0.0/16"
master_node_ip = "192.168.57.100"
version = "v1.29"
```

变量`version`只能取v1.29或v1.28中的一个值，原因在于Google于2023年8月废弃了托管Kubernetes包存储库。您可以在[此处](https://kubernetes.io/blog/2023/08/15/pkgs-k8s-io-introduction/)阅读更多详细信息。

> 如果您需要安装旧版本 - 那么本指南不适用于您 - 您可以浏览我的文章列表，那里有逐步在Ubuntu、CentOS 8上安装Kubernetes或使用CNI（如Cilium）的指南。

下一个元素（第46-50行）是将应用于每个基本框的提供者配置，而不考虑其角色：3GB内存，1 vCPU，并将默认NAT网络（我们在上一段中讨论过）绑定到每个框的第一个网络适配器。

```ruby
config.vm.provider "virtualbox" do |vb|
  vb.memory = "3072"
  vb.cpus = "1"
  vb.customize ["modifyvm", :id, "--nic1", "nat"]
end
```
> 我们将使用Kubeadm安装Kubernetes，这需要每个框至少有2个CPU。在这里，我们仅使用1个，稍后我们将讨论如何通过一个小的无害的变通方法绕过这个要求。免责声明：这里是非生产环境，请勿让我陈述显而易见的事实！

Vagrant文件的最后两部分是基本 box 本身的配置和初始化：一个**通用**的，一个用于**主**节点，一个用于**工作**节点。

我们将为每个 box 打下基础，通过在所有 box 上运行相同的引导脚本（第9行）来完成，该脚本将安装所有必要的先决条件并进行所有必要的配置，以便Kubeadm稍后可以将这些节点提升为主节点或工作节点。

```ruby
config.vm.provision :shell, path: "kubeadm/bootstrap.sh", env: { "VERSION" => version }
```

请注意这里，我们如何可以轻松地将我们的Vagrantfile全局变量作为环境变量传递到每个独立的脚本中：

```ruby
env: { “VERSION” => version }
```

这是我们将在整个Vagrantfile中遵循的一种模式。

对于主节点（第10-23行），除了一些微不足道的工作，如设置基本 box 的操作系统、主机名和Host-Only网络中的IP地址；我们还运行了两个额外的配置脚本。一个是内联脚本，它在每个 box 的/etc/hosts中定义了本地网络中主机名和IP地址的自定义映射。



```ruby
config.vm.define "master" do |master|
  master.vm.box = "ubuntu/focal64"
  master.vm.hostname = "k8s-master.#{domain}"
  master.vm.network "private_network", ip: "#{master_node_ip}"
  
  <<-SHELL
  echo "$MASTER_NODE_IP k8s-master.$DOMAIN k8s-master" >> /etc/hosts
  SHELL
  
  master.vm.provision "shell", env: {"DOMAIN" => domain, "MASTER_NODE_IP" => master_node_ip} ,inline: (1..3).each do |nodeIndex|
    <<-SHELL
    echo "192.168.57.10$NODE_INDEX k8s-worker-$NODE_INDEX.$DOMAIN k8s-worker-$NODE_INDEX" >> /etc/hosts
    SHELL
  end
  
  master.vm.provision "shell", path:"kubeadm/init-master.sh", env: {"K8S_CONTROL_PLANE_ENDPOINT" => control_plane_endpoint, "K8S_POD_NETWORK_CIDR" => pod_network_cidr, "MASTER_NODE_IP" => master_node_ip}
end
```

然后是一个外部的脚本 `kubeadm/init-master.sh`，它将采取所有必要的步骤，将此 box 转换为Kubernetes主节点。

现在是工作节点（第24-44行），事情遵循与主节点相同的模式，但有一些小变化。在工作节点上，将按顺序运行两个额外的脚本。首先，执行自动生成的脚本 `kubeadm/init-worker.sh`，该脚本将此框添加为刚刚使用 `kubeadm/init-master.sh` 脚本创建的群集中的工作节点。后者将在每次通过 `vagrant up` 命令创建环境时自动创建前者的脚本。



```ruby
(1..3).each do |nodeIndex|
  config.vm.define "worker-#{nodeIndex}" do |worker|
    worker.vm.box = "ubuntu/focal64"
    worker.vm.hostname = "k8s-worker-#{nodeIndex}.#{domain}"
    worker.vm.network "private_network", ip: "192.168.57.10#{nodeIndex}"
    
    worker.vm.provision "shell", env: {"DOMAIN" => domain, "MASTER_NODE_IP" => master_node_ip} ,inline: <<-SHELL
      echo "$MASTER_NODE_IP k8s-master.$DOMAIN k8s-master" >> /etc/hosts
    SHELL
    
    (1..3).each do |hostIndex|
      worker.vm.provision "shell", env: {"DOMAIN" => domain, "NODE_INDEX" => hostIndex}, inline: <<-SHELL
        echo "192.168.57.10$NODE_INDEX k8s-worker-$NODE_INDEX.$DOMAIN k8s-worker-$NODE_INDEX" >> /etc/hosts
      SHELL
    end
    
    worker.vm.provision "shell", path:"kubeadm/init-worker.sh"
    worker.vm.provision "shell", env: { "NODE_INDEX" => nodeIndex}, inline: <<-SHELL
      echo ">>> FIX KUBELET NODE IP"
      echo "Environment=\"KUBELET_EXTRA_ARGS=--node-ip=192.168.57.10$NODE_INDEX\"" | sudo tee -a /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
      sudo systemctl daemon-reload
      sudo systemctl restart kubelet
    SHELL
  end
end
```

## 分析引导脚本

正如我们之前提到的，`kubeadm/bootstrap.sh` 在每个 box 上运行，并执行以下步骤：

0. 从所有配置的源更新软件包信息：

```bash
sudo apt-get update
```

1. 配置IPv4转发，并允许iptables查看桥接流量：

```bash
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

sudo modprobe overlay
sudo modprobe br_netfilter

cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF

sudo sysctl --system
```

参考[这里](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#forwarding-ipv4-and-letting-iptables-see-bridged-traffic)。

2. 安装容器运行时（此处使用 [containerd](https://containerd.io/)）并配置 cgroup 驱动程序：

```bash
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
sudo apt-get install ca-certificates curl gnupg -y

sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=\"$(dpkg --print-architecture)\" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo \"$VERSION_CODENAME\") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

cat <<EOF | sudo tee -a /etc/containerd/config.toml
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
SystemdCgroup = true
EOF

sudo sed -i 's/^disabled_plugins \=/\#disabled_plugins \=/g' /etc/containerd/config.toml

sudo mkdir -p /opt/cni/bin/
sudo wget -nv https://github.com/containernetworking/plugins/releases/download/v1.4.0/cni-plugins-linux-amd64-v1.4.0.tgz
sudo tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-v1.4.0.tgz

systemctl enable containerd
systemctl restart containerd
```

参考[这里](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)。

3. 将**特定版本**的 Kubernetes 社区拥有的存储库添加到机器，并安装必要的 kube 相关工具，如 kubeadm、kubelet 和 kubectl：

```bash
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gpg
curl -fsSL https://pkgs.k8s.io/core:/stable:/${VERSION}/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/${VERSION}/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```

参考[这里](https://kubernetes.io/blog/2023/08/15/pkgs-k8s-io-introduction/)。

4. 在每个机器关闭 swap：

```bash
sudo sed -ri '/\sswap\s/s/^#?/#/' /etc/fstab
sudo swapoff -a
```

参考[这里](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#before-you-begin)。

## 分析 kubeadm 脚本

首先，我们将检查 `kubeadm/init-master.sh`，该脚本仅在主节点上运行，并执行以下步骤：

0. 启用 kubelet daemon：

```bash
sudo systemctl enable kubelet
```

1. 初始化控制平面节点：

```bash
kubeadm init \
  --apiserver-advertise-address=$MASTER_NODE_IP \
  --control-plane-endpoint $MASTER_NODE_IP \
  --pod-network-cidr=$K8S_POD_NETWORK_CIDR \
  --skip-phases=addon/kube-proxy \
  --ignore-preflight-errors=NumCPU 
```

> 如果您还记得，我们之前提到过我们使用了一个小的变通方法来绕过最低 2 个必需的 CPU。`--ignore-preflight-errors` 标志是其中之一！

参考[这里](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#initializing-your-control-plane-node)。

2. 为各种用户准备 kubeconfig 文件：

```bash
sudo mkdir -p $HOME/.kube
sudo cp -f /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

mkdir -p /home/vagrant/.kube
sudo cp -f /etc/kubernetes/admin.conf /home/vagrant/.kube/config
sudo chown $(id -u):$(id -g) /home/vagrant/.kube/config

sudo chown -R vagrant /home/vagrant/.kube
sudo chgrp -R vagrant /home/vagrant/.kube

sudo cp -f /home/vagrant/.kube/config /vagrant/.kube/config.vagrant
```

> 如果要手动安装此步骤，可以省略所有与 Vagrant 相关的部分，只保留前三行。

3. 更新 **kubelet** 并安装 Pod 网络插件（这里使用 [Canal](https://docs.tigera.io/calico/latest/getting-started/kubernetes/flannel/install-for-flannel)）

```bash
echo "Environment=\"KUBELET_EXTRA_ARGS=--node-ip=$MASTER_NODE_IP\"" | sudo tee -a /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
envsubst < /vagrant/cni/canal/canal.yaml | kubectl apply -f -
```

> 这是一个有主见的使用 Canal 进行安装，当然您可以根据自己的喜好更换网络插件。
>
> 请注意，`envsubst` 在 canal 清单中替换了我们在 Vagrantfile 中作为环境变量传递给此脚本的 `K8S_POD_NETWORK_CIDR` 的值。

参考[这里](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#pod-network)。

4. 初始化 kube-proxy 插件：

```bash
kubeadm init phase addon kube-proxy \
  --control-plane-endpoint $MASTER_NODE_IP \
  --pod-network-cidr=$K8S_POD_NETWORK_CIDR
```

> 如果您注意到我们在前面跳过了初始化 kube-proxy 插件的步骤，那是有原因的。有一个记录的小问题，您可以在这个 [GitHub 问题](https://itnext.io/install-kubernetes-1-29-using-vagrant-in-under-10-minutes-2fce7108af6d#https://github.com/kubernetes/kubeadm/issues/2699#issuecomment-1280098175)中找到整个讨论。

5. 在 `kubeadm/init-worker.sh` 中创建工作节点的加入命令：

```bash
rm -f /vagrant/kubeadm/init-worker.sh
kubeadm token create --print-join-command >> /vagrant/kubeadm/init-worker.sh
```

参考[这里](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#join-nodes)。

我们的第二个 kubeadm 脚本，刚刚在上一步中自动生成的脚本是 `kubeadm/init-worker.sh`，是一个一行的脚本，将在每个即将成为工作节点的节点上运行（在它们启动后）。它的内容示例（在每次执行时会有所变化，因为令牌是针对每次安装和集群创建的）：

```bash
kubeadm join 192.168.57.100:6443 --token ks3jah.lckxyk98oqpaxxxx --discovery-token-ca-cert-hash sha256:852407xxxxxxx
```

## 将其试用

在存储库中，您将找到一个额外的 bash 脚本，用于构建环境：

```bash
#!/bin/bash

rm -rf .kube/config.vagrant
rm -rf kubeadm/init-worker.sh

vagrant up master --provider=virtualbox
cp -f .kube/config.vagrant ~/.kube/config.vagrant

for i in {1..3}
do 
    sleep 5
    vagrant up worker-$i &
done
```

它将从以前运行中自动生成的文件中清理本地文件夹，首先将主节点配置，然后并行启动 3 个工作节点。它将在您的本地主机中导出一个 kubeconfig 文件 `~/.kube/config.vagrant`，一旦主节点运行起来，您就可以直接用它连接到您的集群：

```bash
export KUBECONFIG=~/.kube/config.vagrant
```

所有在本文中讨论的文件都可以在此[存储库](https://github.com/akyriako/kubernetes-vagrant-ubuntu-v2)中找到。


如果您发现此信息有用，请别忘了在本文下方点赞 👏 并关注我的账号，以获取有关 Kubernetes 的更多内容。敬请期待...
