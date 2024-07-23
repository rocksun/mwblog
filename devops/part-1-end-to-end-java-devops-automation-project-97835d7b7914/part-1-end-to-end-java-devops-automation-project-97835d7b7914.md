
<!--
title: 端到端Java DevOps自动化项目-第1部分
cover: ./cover.png
-->

在当今快节奏的软件开发环境中，自动化部署流程对于确保效率和可靠性至关重要。本文将深入探讨如何创建端到端的 Jenkins 流水线来部署 Java 应用程序。本综合指南旨在从头开始引导您完成整个过程，即使您是 DevOps 新手也能轻松上手。

> 译自 [Part-1 End-to-End Java DevOps Automation Project](https://medium.com/@navin5556/part-1-end-to-end-java-devops-automation-project-97835d7b7914)，作者 Naveen Kumar。

我们将从设置基础设施、配置服务器和设置基本工具开始。接下来，我们将创建一个 Kubernetes 集群和一个用于源代码的私有仓库。在继续的过程中，我们将推送源代码、编写 Jenkins 流水线并实施强大的监控系统来跟踪应用程序的性能。

我们将把这个项目分成四个部分：

## 第1部分：基础设施设置

在第一部分中，我们将通过设置必要的基础设施和工具为我们的 CI/CD 流水线奠定基础。这包括：

1. **设置基础设施和工具**: 我们将设置服务器、配置它们并安装必要的工具，为我们的 CI/CD 流水线创建坚实的基础。
2. **创建 Kubernetes 集群**: 学习如何创建和配置 Kubernetes 集群来管理我们的容器化应用程序。
3. **设置 Jenkins、Nexus 和 SonarQube 服务器**: 我们将安装和配置 Jenkins 用于自动化，Nexus 用于工件管理，SonarQube 用于代码质量分析。

## 第2部分：源代码管理

第二部分侧重于管理我们的源代码，包括：

1. **创建私有 Git 仓库**: 设置一个 Git 仓库来安全地存储我们的源代码，确保没有未经授权的访问。
2. **推送源代码**: 将源代码推送到仓库并验证其可见性和可访问性。

## 第3部分：CI/CD 流水线配置

在第三部分中，我们将配置我们的 CI/CD 流水线，其中包括：

1. **构建 Jenkins 流水线**: 使用 Jenkins，我们将编写一个流水线，其中包括源代码编译、运行单元测试和使用 SonarQube 进行代码质量检查等阶段。
2. **安全扫描**: 使用 Trivy 等工具对源代码和依赖项实施漏洞扫描。
3. **工件管理**: 打包应用程序、生成工件并将它们发布到 Nexus 仓库以进行版本控制。
4. **容器化**: 构建 Docker 镜像，适当地标记它们并将它们推送到 Docker Hub。
5. **Kubernetes 部署**: 将应用程序部署到安全的 Kubernetes 集群，使用 kube-audit 等工具确保集群的安全性。

## 第 4 部分：监控和安全

最后部分涉及设置全面的监控和安全检查，包括：

1. **监控和通知**: 使用 Grafana 和 Prometheus 设置监控，包括使用 node exporter 进行系统级监控和使用 blackbox exporter 进行应用程序级监控。我们还将配置电子邮件通知以告知流水线成功或失败。

通过遵循这四个部分，我们将构建一个强大且安全的 Jenkins 流水线，能够高效地部署 Java 应用程序。

到本文结束时，您将拥有一个功能齐全的 Jenkins 流水线，能够将 Java 应用程序从代码提交部署到生产环境，并包含全面的监控和安全实践。无论您是开发人员还是 DevOps 工程师，本指南都将为您提供实施强大的 CI/CD 流水线和简化部署流程的知识。

加入我，踏上掌握使用 Jenkins 自动化 Java 应用程序部署的艺术之旅。让我们开始吧！

### 1. 设置基础设施和工具:

对于这个项目，我们将使用默认 VPC。在企业环境中，我们通常在私有 VPC 中设置所有内容以增强安全性。第一步是创建一个安全组，我们将将其附加到我们创建的每个实例。

以下是名为 **devops-automation-primary-sg** 的安全组的 **入站规则** 的详细信息。

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*CaXCYrZcxLhH-cUGRNcRXg.png)

我们将创建 **7 个 EC2 实例**，使用以下配置运行 Ubuntu Server 20.04：

* **实例类型:** t3.xlarge
* **安全组:** primary-SG
* **卷:** 1 个卷 (gp3) — 30 GiB

这些实例将相应地命名：

- master
- slave-1
- slave-2
- jenkins
- sonarqube
- nexus
- monitoring

**注意:** 您也可以选择使用 **Ubuntu Server 20.04** 的 **t3.medium** 实例。我在使用 **t3.medium** 时遇到了错误，因此我选择了 **t3.xlarge**，这会产生更高的成本。您也可以通过根据 **YUM** 兼容性替换命令来尝试使用 Linux 服务器。如果您遇到错误，解决它们将增强您的信心。

![](https://miro.medium.com/v2/resize:fit:1006/format:webp/1*fJWdgW5zaaafNYXrB3GKRw.png)

### 2. 创建 Kubernetes 集群:

我建议使用 MobaXterm 或 MTPuTTY 通过 SSH 登录服务器。

**在主节点和工作节点上运行的命令**

```bash
sudo su -
sudo apt-get update
sudo apt install docker.io -y
sudo chmod 666 /var/run/docker.sock
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
sudo mkdir -p -m 755 /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.28/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt update
sudo apt install -y kubeadm=1.28.1-1.1 kubelet=1.28.1-1.1 kubectl=1.28.1-1.1
```

**仅在主节点上运行的命令**

```
sudo su -
# Run the output of the following command on the worker node to join it to the cluster
sudo kubeadm init --pod-network-cidr=10.244.0.0/16
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.49.0/deploy/static/provider/baremetal/deploy.yaml
```

如果您忘记加入工作节点，您可以使用以下命令检索令牌并在工作节点上运行它：

```
kubeadm token create --print-join-command
```

现在我们的 k8 集群已准备就绪，您可以执行 kubectl 命令

**主节点上的 K8s 集群扫描**

要扫描 Kubernetes 集群，请在主节点上运行以下命令。请注意，由于我们尚未设置 RBAC 等所有内容，因此它将显示许多错误。输出可供基础设施团队使用。

```
wget https://github.com/Shopify/kubeaudit/releases/download/v0.22.1/kubeaudit_0.22.1_linux_amd64.tar.gz
tar -xvzf kubeaudit_0.22.1_linux_amd64.tar.gz
sudo mv kubeaudit /usr/local/bin/
kubeaudit all
```

### 3. 设置 Jenkins

**安装 Jenkins 脚本**

将以下脚本保存在一个文件中，例如 `install_jenkins.sh`:

```
#!/bin/bash
# Install OpenJDK 17 JRE Headless (pre-requisite)
sudo apt install openjdk-17-jre-headless -y
# Download Jenkins GPG key (official code link - https://www.jenkins.io/doc/book/installing/linux/#debianubuntu)
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
# Add Jenkins repository to package manager sources
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
# Update package manager repositories
sudo apt-get update
# Install Jenkins
sudo apt-get install jenkins -y
```

使脚本可执行并运行它：

```
chmod +x install_jenkins.sh
./install_jenkins.sh
```


此脚本将自动执行 OpenJDK 17 JRE Headless 和 Jenkins 的安装过程。

**安装 Docker 脚本**

将以下脚本保存在一个文件中，例如 `install_docker.sh`:

```
#!/bin/bash

# Update package manager repositories
sudo apt-get update

# Install necessary dependencies
sudo apt-get install -y ca-certificates curl

# Create directory for Docker GPG key
sudo install -m 0755 -d /etc/apt/keyrings

# Download Docker's GPG key
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

# Ensure proper permissions for the key
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add Docker repository to Apt sources
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package manager repositories
sudo apt-get update

# Install Docker packages
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

使脚本可执行并运行它：

```
chmod +x install_docker.sh
./install_docker.sh
```

授予其他用户运行 Docker 命令的权限：

```
sudo chmod 666 /var/run/docker.sock
```

运行这些命令后，Jenkins 将在您的主机上的 [http://IP:8080](http://IP:8080.)[.](http://IP:8080.) 可访问。

### 4. 设置 Nexus

**步骤 1：安装 Docker**

首先，我们需要安装 Docker。将以下脚本保存在名为 `install_docker.sh` 的文件中:

```
#!/bin/bash

# Update package manager repositories
sudo apt-get update

# Install necessary dependencies
sudo apt-get install -y ca-certificates curl

# Create directory for Docker GPG key
sudo install -m 0755 -d /etc/apt/keyrings

# Download Docker's GPG key
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

# Ensure proper permissions for the key
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add Docker repository to Apt sources
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package manager repositories again
sudo apt-get update

# Install Docker packages
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

使脚本可执行并运行它：

```
chmod +x install_docker.sh
./install_docker.sh
```

授予其他用户运行 Docker 命令的权限：

```
sudo chmod 666 /var/run/docker.sock
```

**步骤 2：创建 Nexus Docker 容器**

要创建一个运行 Nexus 3 并将其暴露在端口 8081 上的 Docker 容器，请使用以下命令：

```
docker run -d --name nexus -p 8081:8081 sonatype/nexus3:latest
```

此命令执行以下操作：

* `-d`: 分离容器并在后台运行。
* `--name nexus`: 将容器命名为“nexus”。
* `-p 8081:8081`: 将主机上的端口 8081 映射到容器上的端口 8081，允许通过端口 8081 访问 Nexus。
* `sonatype/nexus3:latest`: 使用 Sonatype 存储库中的最新版本的 Nexus 3。

运行此命令后，您可以在主机上的 `http://<your_IP>:8081` 访问 Nexus。

**步骤 3：检索 Nexus 初始密码**

要访问存储在容器中的 Nexus 初始管理员密码，请按照以下步骤操作：

1. **获取容器 ID**: 列出所有正在运行的容器以查找 Nexus 容器的 ID。
```
docker ps
```

2. **访问容器的 Bash Shell**: 执行以下命令以访问容器的 bash shell：
```
docker exec -it <container_ID> /bin/bash
```
将 `<container_ID>` 替换为 Nexus 容器的实际 ID。

3. **导航到 Nexus 目录**: 在容器的 bash shell 中，导航到 Nexus 存储其配置的目录：
```
cd sonatype-work/nexus3
```

4. **查看管理员密码**: 显示 `admin.password` 文件的内容以查看管理员密码：
```
cat admin.password
```

5. **退出容器 Shell**: 检索到密码后，退出容器的 bash shell：
```
exit
```

此过程允许您访问存储在容器中的 Nexus 管理员密码。确保将此密码保密，因为它授予您对 Nexus 实例的管理访问权限。

注意：在 Nexus 中设置密码时 - 允许匿名访问

用例示例：

示例场景

假设您有一个开源项目的文档服务器。您希望让每个人都能访问项目的文档，而无需用户创建帐户。以下是如何配置它：

* 访问：启用匿名访问。
* 用户名：设置为“anonymous”。
* 领域：设置为“本地授权领域”以定义匿名用户操作的上下文。

此设置确保任何人都可以访问文档，而无需进行身份验证，从而使信息广泛可用且易于访问。

通过仔细考虑用例并适当地配置设置，您可以利用匿名访问来提高可访问性，同时保持对敏感资源的安全性和控制。

### 5. 设置 SonarQube

**步骤 1：安装 Docker**

首先，我们需要安装 Docker。将以下脚本保存在名为 `install_docker.sh` 的文件中：

```
#!/bin/bash

# Update package manager repositories
sudo apt-get update

# Install necessary dependencies
sudo apt-get install -y ca-certificates curl

# Create directory for Docker GPG key
sudo install -m 0755 -d /etc/apt/keyrings

# Download Docker's GPG key
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

# Ensure proper permissions for the key
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add Docker repository to Apt sources
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo \"$VERSION_CODENAME\") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package manager repositories again
sudo apt-get update

# Install Docker packages
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

使脚本可执行并运行它：

```
chmod +x install_docker.sh
./install_docker.sh
```

授予其他用户运行 Docker 命令的权限：

```
sudo chmod 666 /var/run/docker.sock
```

**步骤 2：创建 SonarQube Docker 容器**

要在 Docker 容器中运行 SonarQube，请使用以下命令：

```
docker run -d --name sonar -p 9000:9000 sonarqube:lts-community
```

此命令执行以下操作：

* `-d`: 分离容器并在后台运行。
* `--name sonar`: 将容器命名为“sonar”。
* `-p 9000:9000`: 将主机上的端口 9000 映射到容器上的端口 9000，允许通过端口 9000 访问 SonarQube。
* `sonarqube:lts-community`: 使用 Docker Hub 中的 SonarQube 的长期支持 (LTS) 社区版。

运行此命令后，您可以在主机上的 `http://<your_VM_IP>:9000` 访问 SonarQube。

**步骤 3：访问 SonarQube**

要访问 SonarQube，请打开 Web 浏览器并导航到 `http://<your_VM_IP>:9000`。

这将启动 SonarQube 服务器，您应该能够使用提供的 URL 访问它。如果您在远程服务器或其他端口上运行 Docker，请替换 `<your_VM_IP>`。
使用适当的主机名或 IP 地址，并相应地调整端口。

注意：这是**第一部分：基础设施设置**的结尾，第二部分将涵盖**源代码管理**。