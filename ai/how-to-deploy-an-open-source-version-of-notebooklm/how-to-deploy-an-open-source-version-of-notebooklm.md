
<!--
title: NotebookLM开源版部署指南
cover: https://cdn.thenewstack.io/media/2025/11/6148b804-markus-winkler-z8ywssx8owe-unsplash.jpg
summary: 
NotebookLM 是 Google 的 AI 笔记工具，可处理用户上传的文档。Open Notebook 是其开源且可自托管的版本，注重隐私。文章详细介绍了如何在 Ubuntu Server 上安装 Docker，并部署 Open Notebook，包括配置 API 密钥以连接 Ollama 和 Google Gemini 等 AI 服务。
-->


NotebookLM 是 Google 的 AI 笔记工具，可处理用户上传的文档。Open Notebook 是其开源且可自托管的版本，注重隐私。文章详细介绍了如何在 Ubuntu Server 上安装 Docker，并部署 Open Notebook，包括配置 API 密钥以连接 Ollama 和 Google Gemini 等 AI 服务。

> 译自：[How To Deploy an Open Source Version of NotebookLM](https://thenewstack.io/how-to-deploy-an-open-source-version-of-notebooklm/)
> 
> 作者：Jack Wallen

[NotebookLM](https://notebooklm.google/) 是由 [Google](https://cloud.google.com/?utm_content=inline+mention) 创建的一个 AI 研究和笔记工具，它使用 [大型语言模型 (LLMs)](https://thenewstack.io/introduction-to-llms/)，允许用户添加自己的来源，然后在 AI 的帮助下，理解和连接这些来源之间的信息。

NotebookLM 就像一个个性化的 AI 助手，它只处理上传的文档、PDF、网站和视频，以生成摘要、回答问题、集思广益以及将内容转换为其他格式。

NotebookLM 是专有的，目前非常受欢迎，但你知道这项技术也有一个开源版本吗？

[Open Notebook](https://www.open-notebook.ai/) 和 NotebookLM 一样强大和有用。最大的区别在于 Open Notebook 是自托管的。虽然两者都可以使用本地 AI 模型，但只有 Open Notebook 可以本地安装。如果你关心隐私和安全，将你的 AI 工具隔离在本地网络中可以带来真正的优势。与 Open Notebook 不同，NotebookLM 托管在 Google 的第三方云服务器上，这可能会引起对隐私和安全的疑问。

Open Notebook 支持超过 16 家 AI 提供商，因此你可以根据你的需求、预算和隐私要求选择要使用的 LLM。

如果你觉得这很有吸引力，请继续阅读，因为我将向你展示如何在你的 LAN 内的一台机器上部署 Open Notebook。

## 你需要什么

要实现这一点，你需要一台支持 [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) 的计算机。如果你想使用其中一个专有 AI 服务（例如 [Google Gemini](https://thenewstack.io/googles-gemini-models-go-deeper/) 或 OpenAI），你将需要相关服务的 API 密钥。

我将向你展示如何在 Ubuntu Server 24.04 上部署 Open Notebook。如果你使用的是不同的操作系统，你需要更改 Docker 的安装方法，但仅此而已。

## 安装 Docker

第一步是安装 Docker。方法如下：

### **1. 添加官方 Docker GPG 密钥**

要添加官方 Docker GPG 密钥，请使用以下命令：

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

### **2. 添加 Docker 仓库**

接下来，你需要添加 Docker 仓库，方法是执行以下命令：

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc]
https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

使用以下命令更新 apt：

```bash
sudo apt-get update
```

### **3. 安装所需软件**

你现在需要使用以下命令安装所有必需的软件：

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git -y
```

### **4. 将你的用户添加到 Docker 组**

你需要将该用户添加到 Docker 组，这样你就可以避免使用管理员权限运行 Docker。使用以下命令将你的用户添加到 Docker 组：

```bash
sudo usermod -aG docker $USER
```


注销并重新登录，以便更改生效。

## 部署 Open Notebook

现在是部署的时候了。首先，使用以下命令克隆必要的 Git 仓库：

```bash
git clone https://github.com/lfnovo/open-notebook.git
```

使用以下命令进入新创建的目录：

此文件包含隐藏的或双向的 Unicode 文本，它可能被解释或编译的方式与下方显示的有所不同。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解更多关于双向 Unicode 字符的信息](https://github.co/hiddenchars)

在该文件夹中，你需要使用以下命令复制并重命名几个文件：

此文件包含隐藏的或双向的 Unicode 文本，它可能被解释或编译的方式与下方显示的有所不同。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解更多关于双向 Unicode 字符的信息](https://github.co/hiddenchars)

|     |     |
| --- | --- |
|     | cp docker-compose.full.yml docker-compose.yml |
|     | cp .env.example docker.env |

你无需编辑 docker-compose.yml 文件，但你需要处理 docker.env 文件。

在 docker.env 文件中，你需要编辑几行。具体需要编辑多少行取决于你想使用哪些 AI 服务。假设你想使用 [Ollama](https://thenewstack.io/connect-to-a-local-ollama-ai-instance-from-within-your-lan/)（必须安装在本地机器上）和 Google Gemini。

首先要做的就是找到这一行：

此文件包含隐藏的或双向的 Unicode 文本，它可能被解释或编译的方式与下方显示的有所不同。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解更多关于双向 Unicode 字符的信息](https://github.co/hiddenchars)

|     |     |
| --- | --- |
|     | API_URL=http://127.0.0.1:5055 |

将 127.0.0.1 更改为主机服务器的 IP 地址。

接下来，找到这一行：

此文件包含隐藏的或双向的 Unicode 文本，它可能被解释或编译的方式与下方显示的有所不同。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解更多关于双向 Unicode 字符的信息](https://github.co/hiddenchars)

你将需要取消注释该行（删除 #）并粘贴你的 Google Gemini API 密钥，使其看起来像这样：

此文件包含隐藏的或双向的 Unicode 文本，它可能被解释或编译的方式与下方显示的有所不同。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解更多关于双向 Unicode 字符的信息](https://github.co/hiddenchars)

|     |     |
| --- | --- |
|     | GOOGLE_API_KEY=AIzaSyCOLZUi8h3wwjfhdSEViQXi9olWUoGKNE |

确保使用你从 [Google 的 API Studio](https://aistudio.google.com/app/api-keys) 创建的 API 密钥。

接下来，找到这一行：

此文件包含隐藏的或双向的 Unicode 文本，它可能被解释或编译的方式与下方显示的有所不同。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解更多关于双向 Unicode 字符的信息](https://github.co/hiddenchars)

|     |     |
| --- | --- |
|     | OLLAMA_API_BASE="http://10.20.30.20:11434" |

你将需要将上述 IP 地址替换为主机服务器的 IP 地址，例如：

此文件包含隐藏的或双向的 Unicode 文本，它可能被解释或编译的方式与下方显示的有所不同。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解更多关于双向 Unicode 字符的信息](https://github.co/hiddenchars)

|     |     |
| --- | --- |
|     | OLLAMA_API_BASE="http://192.168.1.26:11434" |

你可以浏览文件的其余部分，并添加你需要的其他 AI API。完成之后，保存并关闭文件。

你可以在 [这个官方 Open Notebook 文档](https://github.com/lfnovo/open-notebook/blob/main/docs/features/ai-models.md) 中了解更多关于各种模型以及它们最适合的用途。

现在是时候部署 Open Notebook 容器了，方法是：

此文件包含隐藏的或双向的 Unicode 文本，它可能被解释或编译的方式与下方显示的有所不同。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解更多关于双向 Unicode 字符的信息](https://github.co/hiddenchars)

给容器一些时间启动，然后将浏览器指向 http://SERVER:8502（其中 SERVER 是主机服务器的 IP 地址）。

系统会提示你创建一个账户（该账户是免费的，所有信息都保留在本地服务器上）。登录后，你将看到 Open Notebook 的主页（图 1），可以在其中开始根据你的需求进行配置。

[![](https://cdn.thenewstack.io/media/2025/11/c70c64f9-screenshot-2025-11-12-at-10.43.37%E2%80%AFam.png)](https://cdn.thenewstack.io/media/2025/11/c70c64f9-screenshot-2025-11-12-at-10.43.37%E2%80%AFam.png)

图 1：Open Notebook 的用户界面非常友好。

确保首先转到“模型”部分，在那里你可以定义要用于特定任务的模型。完成之后，你就可以创建你的第一个 Notebook 并开始工作了。