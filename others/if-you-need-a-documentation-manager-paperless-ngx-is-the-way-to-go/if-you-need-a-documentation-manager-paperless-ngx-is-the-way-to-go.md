<!--
title: 文档管理神器：Paperless-Ngx，你的终极解决方案
cover: https://cdn.thenewstack.io/media/2025/12/6210ba16-a-c-phcgjakfxl4-unsplash.jpg
summary: 面对开发人员流失导致的未文档化代码，可使用 Paperless-Ngx 文档管理系统。它能数字化、组织、搜索文档，并通过OCR、机器学习等功能，简化文档维护与新开发人员培训。
-->

面对开发人员流失导致的未文档化代码，可使用 Paperless-Ngx 文档管理系统。它能数字化、组织、搜索文档，并通过OCR、机器学习等功能，简化文档维护与新开发人员培训。

> 译自：[If You Need a Documentation Manager, Paperless-Ngx Is the Way To Go](https://thenewstack.io/if-you-need-a-documentation-manager-paperless-ngx-is-the-way-to-go/)
> 
> 作者：Jack Wallen

你是一家拥有一个开发人员或一个开发团队的公司。这些开发人员创建了多个内部应用程序和服务，它们集成到你的系统中，并且相当复杂。

一段时间后，人员流失导致一些开发人员离开，你发现那些特殊的代码片段从未被文档化。

你会怎么做？

你将如何培训下一批开发人员，让他们能够继续无缝地维护这些代码片段？

那是个问题。

如果你的开发人员对他们的工作和系统进行了文档，你只需将这些新团队成员指向相应的文档，他们就能迅速了解情况。

也许那些开发人员确实记录了东西，但文档是随意创建的，并且散落在不同的位置，形式也各不相同。

如果有一个文档管理系统来简化这一切就好了。

幸运的是，确实有这样一个强大的工具，它就是 [Paperless-Ngx](https://docs.paperless-ngx.com/)。

Paperless-Ngx 是 Paperless 和 Paperless-Ng 的官方延续。这个[文档管理系统](https://thenewstack.io/why-the-document-model-is-more-cost-efficient-than-rdbms/)是开源的、自托管的，通过将文档转换为在线档案，极大地简化了文档的数字化、组织和搜索过程。Paperless-Ngx 甚至包括[光学字符识别 (OCR)](https://thenewstack.io/why-upstage-builds-small-language-models/)，因此你可以轻松扫描文档和图像，使其可搜索、可标记和可索引。

借助 Paperless-Ngx，你可以消除杂乱和混乱，并确保文档随时可用。

Paperless-Ngx 包含以下功能：

*   通过标签、往来单位、类型等进行组织。
*   所有数据都本地存储，从不传输或共享。
*   内置 OCR 支持。
*   利用开源 Tesseract 引擎支持 100 多种语言。
*   文档以 PDF/A 格式保存。
*   机器学习自动添加标签和文档类型。
*   支持 PDF、图像、纯文本文件、MS Office/LibreOffice 文档。
*   带统计数据的可定制仪表板。
*   过滤。
*   批量编辑标签、往来单位、类型等。
*   拖放上传文档。
*   可定制视图。
*   自定义字段。
*   可共享的公共链接，可选择设置过期日期。
*   全文搜索。
*   自动完成以建议相关词。
*   邮件处理。
*   消息可以标记为已读、删除等。
*   多用户权限系统。
*   用于更多控制的工作流系统。
*   针对多核系统优化。
*   集成健全性检查器，确保文档档案的健康状况良好。

你可能认为部署这样一个系统会很有挑战性。多亏了 [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)，事实并非如此。

让我带你了解安装这个出色的文档管理系统的过程。

## 所需条件

你唯一需要的是一个支持 Docker 的操作系统和一个正常的互联网连接。我将在 Ubuntu Server 24.04 上演示这个过程。如果你使用的是不同的操作系统，你需要修改安装 Docker 的步骤。如果你已经安装了 Docker，可以直接跳到安装 Paperless-Ngx 部分。

准备好了吗？开始吧。

## 安装 Docker

在安装 Paperless-Ngx 之前，你需要先安装 Docker。以下是分四步完成安装的方法。

### 步骤 1：添加官方 Docker GPG 密钥

你必须做的第一件事是使用以下命令添加官方 Docker GPG 密钥：

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

### 步骤 2：添加所需的 Docker 仓库

添加密钥后，现在可以使用以下命令添加必要的仓库：

```bash
echo \ "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \ $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \ sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### 步骤 3：更新 Apt 并安装所需软件

让我们使用以下命令更新 apt：

```bash
sudo apt-get update
```

完成后，安装所需软件：

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git -y
```

### 步骤 4：将你的用户添加到 Docker 组

最后，要以标准用户身份运行 Docker 命令，你需要将该用户添加到 Docker 组。通过这样做，你可以避免使用 sudo 运行 Docker，这可能会带来安全问题。使用以下命令将你的用户添加到 Docker 组：

```bash
sudo usermod -aG docker $USER
```

完成这些后，请注销并重新登录，以使更改生效。

## 部署 Paperless-Ngx

终于到了部署我们的系统的时候了。回到终端窗口，执行以下命令：

```bash
bash -c "$(curl -L https://raw.githubusercontent.com/paperless-ngx/paperless-ngx/main/install-paperless-ngx.sh)"
```

在基于文本的安装程序中，你需要回答几个问题，其中大部分都很简单。事实上，当出现提示时，你可能希望通过按 Enter 键来保留所有默认设置。

当被问及端口号时，请密切注意。默认情况下，Paperless-Ngx 希望使用端口 8000。我的 [Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/) 24.04 服务器上运行着其他几个服务，第一次尝试部署 Paperless-Ngx 时，我记得端口 8000 已经被占用。于是我将其配置为端口 8081，一切正常。

安装完成后，在连接到你[局域网](https://thenewstack.io/git-set-up-a-local-repository-accessible-by-lan/)的机器上打开网页浏览器，并指向 http://SERVER:PORT（其中 SERVER 是服务器的 IP 地址，PORT 是你配置的端口）。

当登录页面打开时（**图 1**），输入你的新账户的电子邮件地址和密码。

[![](https://cdn.thenewstack.io/media/2025/12/eec98d4e-screenshot-2025-12-17-at-1.06.59-pm.png)](https://cdn.thenewstack.io/media/2025/12/eec98d4e-screenshot-2025-12-17-at-1.06.59-pm.png)

***图 1：** Paperless-Ngx 登录界面也是你创建新账户的地方。*

创建账户后，你将进入 Paperless-Ngx 主页面（**图 2**），在那里你可以开始为你的系统上传或创建文档。

[![](https://cdn.thenewstack.io/media/2025/12/3c1930e7-screenshot-2025-12-17-at-1.08.10-pm-scaled.png)](https://cdn.thenewstack.io/media/2025/12/3c1930e7-screenshot-2025-12-17-at-1.08.10-pm-scaled.png)

***图 2：** Paperless-Ngx 已准备好提供服务。*

永远不要将文档视为理所当然。如果你有适当的文档，你就不必担心新的开发团队难以跟上之前的工作。

你还应该制定关于文档外观和阅读方式的策略。尽量使其简单明了，这样随着公司的发展和演变，你将面临的问题会很少。