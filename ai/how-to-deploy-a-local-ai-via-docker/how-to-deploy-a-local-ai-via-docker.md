
<!--
title: Docker本地AI部署：从入门到实践
cover: https://cdn.thenewstack.io/media/2025/10/9494dfc7-getty-images-n2nzsickofg-unsplash.jpg
summary: 文章详述了通过Docker部署本地AI的优势（隐私、安全、环境友好）及具体步骤。涵盖Docker安装、无GPU、NVIDIA和AMD GPU环境下的部署方法，并说明如何访问AI。
-->

文章详述了通过Docker部署本地AI的优势（隐私、安全、环境友好）及具体步骤。涵盖Docker安装、无GPU、NVIDIA和AMD GPU环境下的部署方法，并说明如何访问AI。

> 译自：[How To Deploy a Local AI via Docker](https://thenewstack.io/how-to-deploy-a-local-ai-via-docker/)
> 
> 作者：Jack Wallen

如果你厌倦了担心你的[AI 查询](https://thenewstack.io/why-ai-and-sql-go-together-like-peanut-butter-and-jelly/)或其中共享的数据被用于[训练大型语言模型 (LLM)](https://thenewstack.io/meeting-the-operational-challenges-of-training-llms/)或创建你的个人资料，你总可以使用本地AI选项。我实际上已经到了只使用本地AI的地步。对我来说，这不仅是为了隐私和安全，也是为了AI对电网和环境造成的负担。如果我能尽自己的一份力来防止全面崩溃，我当然会这样做。

大多数情况下，我直接在我的机器上部署本地AI。然而，在某些情况下，我希望快速将本地AI部署到远程服务器（无论是在我的[局域网](https://thenewstack.io/connect-to-a-local-ollama-ai-instance-from-within-your-lan/)内还是之外的服务器）。当这种需求出现时，我有两种选择：

*   以我安装在桌面的相同方式安装本地AI服务。
*   将其容器化。

将其容器化的好处是，本地安装的AI与系统的其他部分隔离开来，给我带来更多的隐私。此外，如果我想停止本地安装的AI，我可以通过一个快速简便的[Docker 命令](https://thenewstack.io/how-to-use-the-docker-exec-command/)来完成。

我甚至可以说，将你的本地AI容器化是让它启动并运行最快、最简单的方法。

多亏了 Docker。

没错，我们将把本地AI服务部署为Docker容器。

让我告诉你这是如何做到的。

## 所需条件

首先，你需要一个支持 Docker 的操作系统，可以是[Linux](https://thenewstack.io/introduction-to-linux-operating-system/)、macOS 或 Windows。你还需要系统上有足够的空间来拉取任何你想使用的 LLM。最后，你需要一个拥有管理员权限的用户和网络连接。我将会在 Ubuntu Server 24.04 上演示这一点。

## 安装 Docker

我们要做的第一件事是安装 Docker。方法如下。

首先，你需要使用以下命令添加官方 Docker GPG 密钥：

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

接下来，使用以下命令添加所需的 Docker 仓库：

```bash

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

使用以下命令安装所需软件：

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git -y
```

要以标准用户身份运行 Docker 命令，你需要将该用户添加到 Docker 组中。这样做是为了你可以无需 sudo 权限即可运行 Docker 命令。使用以下命令将你的用户添加到 Docker 组：

```bash
sudo usermod -aG docker $USER
```

注销并重新登录以使更改生效。

## 使用 Docker 部署本地 AI

使用 Docker 部署本地 AI 有三种不同的方法。

### 没有 GPU

第一种部署方法适用于没有[NVIDIA GPU](https://thenewstack.io/nvidia-gpu-dominance-at-a-crossroads/)的机器，这意味着本地 AI 将完全依靠 CPU 运行。为此，命令是：

```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

这是最简单的方法。

### 使用 NVIDIA GPU

如果你的机器上有 NVIDIA GPU，则必须采取以下几个步骤。

你必须做的第一件事是使用以下命令为 NVIDIA Container Toolkit 添加必要的仓库：

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey \
    | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list \
    | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' \
    | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt-get update
```

你现在可以使用以下命令安装 NVIDIA Container Toolkit：

```bash
sudo apt-get install -y nvidia-container-toolkit -y
```

然后，你需要使用以下两个命令配置 Docker 以与 NVIDIA 工具包配合使用：

```bash
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

你现在可以使用以下命令部署 [Ollama](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/) 容器：

```bash
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

### 使用 AMD GPU

如果你有 [AMD GPU](https://thenewstack.io/gunslinging-amd-tough-on-software-as-developers-balk/)，命令是：

此文件包含可能与下面显示内容解释或编译方式不同的隐藏或双向 Unicode 文本。要查看，请在显示隐藏 Unicode 字符的编辑器中打开文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

```bash
docker run -d --device /dev/kfd --device /dev/dri -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:rocm
```

## 访问本地 AI

一切都运行起来后，我们现在必须访问 AI 提示。假设你想拉取 Llama 3.2 LLM。你可以使用以下命令拉取它并访问提示：

```bash
docker exec -it ollama ollama run llama3.2
```

上述命令将把你带到 Ollama 提示符，你可以在那里运行你的第一个查询。

这就是通过 Docker 容器部署本地 AI 的全部内容。