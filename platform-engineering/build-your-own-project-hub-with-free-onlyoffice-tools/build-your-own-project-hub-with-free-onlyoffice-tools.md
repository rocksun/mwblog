
<!--
title: 使用免费ONLYOFFICE工具构建你自己的项目中心
cover: https://cdn.thenewstack.io/media/2025/06/6cef833a-philip-oroni-bjat6xdzgqi-unsplash.jpg
summary: 告别昂贵和隐私泄露！用免费 ONLYOFFICE 搭建私有项目中心。基于 Docker 部署 ONLYOFFICE Workspace 社区版，低成本实现项目、CRM、邮件等一体化管理。更有备份、存储、LDAP、SSO 等高级功能，中小企业和开发者必备！
-->

告别昂贵和隐私泄露！用免费 ONLYOFFICE 搭建私有项目中心。基于 Docker 部署 ONLYOFFICE Workspace 社区版，低成本实现项目、CRM、邮件等一体化管理。更有备份、存储、LDAP、SSO 等高级功能，中小企业和开发者必备！

> 译自：[Build Your Own Project Hub With Free ONLYOFFICE Tools](https://thenewstack.io/build-your-own-project-hub-with-free-onlyoffice-tools/)
> 
> 作者：Jack Wallen

[项目管理工具](https://thenewstack.io/anti-agile-project-tracker-linear-the-latest-to-take-on-jira/) 在团队合作中是绝对必要的。如果没有项目管理解决方案，这些项目将变得非常难以管理。

当然，你可以选择使用第三方解决方案，但有两个原因可能让你不想这样做：

- 成本
- 隐私

如果你是一家小型企业，甚至是独立开发者，你可能仍然需要一个不仅经济高效，而且不会将你的项目文件存储在第三方服务器上的项目管理解决方案。这两个原因都应该让你考虑像 [ONLYOFFICE Workspace](https://thenewstack.io/the-best-office-suites-for-linux/) 这样的工具。

这个应用程序有两个版本：企业版和社区版。显然，如果你是一家更大的公司，你会想要选择企业版。但是，如果你是一家较小的企业（或小型团队），你应该考虑社区版。或者，如果你只是想试用一下这个工具（看看企业版是否是更好的选择），你可以安装社区版，测试一下，然后（如果适合你）迁移到更大的版本。

我想向你展示如何部署 ONLYOFFICE Workspace 社区项目管理软件。

## 你需要什么

我将在 Ubuntu Server 24.04 上演示这个过程，但你可以在任何支持 [Docker](https://thenewstack.io/containers-in-the-age-of-ai-a-chat-with-new-docker-president-mark-cavage/) 的机器上部署该软件。你需要在步骤中进行的唯一更改是如何在你的机器上安装 Docker。为此，你需要一个运行的、支持 Docker 的操作系统实例和一个具有管理员权限的用户（对于 Ubuntu，这将需要 sudo 访问权限）。

至于系统要求，你至少需要：

- CPU：至少 4 核（推荐 6 核）
- 内存：至少 8GB（推荐 12GB）
- 硬盘：至少 40GB 的可用空间
- 附加要求：至少 6GB 的交换空间
- 操作系统：内核版本 3.10 或更高版本的 amd64 Linux 发行版

让我们开始吧。

## 安装 Docker

登录到你的 Ubuntu Server 实例，首先使用以下命令更新/升级系统：

```bash
sudo apt-get update && sudo apt-get upgrade -y
```

如果在此过程中升级了内核，你需要重新启动服务器以使更改生效，这可以使用以下命令完成：

```
sudo reboot
```

服务器重新启动后，使用以下命令安装必要的 Docker 组件：

```
sudo apt-get install docker.io docker-compose -y
```

安装完成后，你需要使用以下命令将你的用户添加到 Docker 组：

```
sudo usermod -aG docker $USER
```

注销并重新登录以使更改生效。

## 安装 ONLYOFFICE Workspace

现在是时候安装 ONLYOFFICE Workspace 了。为此，首先使用以下命令下载安装脚本：

```
wget https://download.onlyoffice.com/install/workspace-install.sh
```

使用以下命令授予脚本可执行权限：

```
chmod u+x workspace-install.sh
```

运行以下命令：

```
sudo ./workspace-install.sh
```

在安装过程中，你首先会被问到是否要运行 Docker 的安装。按 Enter 接受安装。接下来，你会被问到是否要安装 ONLYOFFICE 邮件服务器。我跳过了这一部分，因为我将其安装在我的家庭局域网上。如果你的服务器有关联的域名（并且你知道你需要邮件组件，这很可能），请继续进行邮件服务器安装。你需要输入你的 FQDN 才能继续安装。

此时，安装将开始拉取必要的 Docker 容器，大约需要 5-10 分钟（具体取决于你的机器和网络连接的速度）。

安装完成后，你可以通过发出以下命令来验证它：

```
docker ps -a
```

你应该会看到几个容器正在运行，例如 communityserver、onlyoffice-control-panel、onlyoffice-document-server、onlyoffice-elasticsearch 和 onlyoffice-mysql-server。这些都应该被列为 Up。

## 访问服务

在连接到与 ONLYOFFICE 服务器相同网络的机器上打开一个 Web 浏览器，并将其指向 [http://SERVER](http://server)（其中 SERVER 是托管服务器的 IP 地址或域名）。

你将看到一个页面，你必须在其中键入/验证用户的密码，添加注册的电子邮件地址，然后选择语言和时区（图 1）。

![](https://cdn.thenewstack.io/media/2025/06/7932e6c5-ooportal1.jpg)

*图 1. 最终安装的第一页。*

完成此操作后，单击服务条款的复选框，然后单击“继续”。这将使你进入 ONLYOFFICE Workspace 主页（图 2），你将在其中看到“项目”、“CRM”、“邮件”、“人员”和“控制面板”的图标。

![](https://cdn.thenewstack.io/media/2025/06/ebbd34f9-ooportal2.jpg)

*图 2. ONLYOFFICE Workspace 主页面。*

点击控制面板，然后您可以为该服务配置多个选项（图 3），例如备份、存储、更新、全文搜索、品牌、多租户、私有房间、LDAP、SSO、登录历史、审计跟踪和数据导入。

![ONLYOFFICE Workspace 控制面板](https://cdn.thenewstack.io/media/2025/06/18bc0ceb-ooportal3.jpg)

*图 3. ONLYOFFICE Workspace 控制面板。*

返回到门户并单击“项目”，系统将提示您创建您的第一个项目（图 4）。

![使用 ONLYOFFICE Workspace 创建您的第一个项目](https://cdn.thenewstack.io/media/2025/06/b638bf39-ooportal4.jpg)

*图 4. 使用 ONLYOFFICE Workspace 创建您的第一个项目。*

此时，只需设置您的项目以满足您的需求，这非常简单。

恭喜，您现在拥有一个为您的中小企业或开发团队运行的项目管理工具。如果您发现 ONLYOFFICE Workspace 足以满足您的需求，那么您就可以开始了。如果您渴望更多功能和可扩展性，请考虑企业版。您可以在此[价格矩阵](https://www.onlyoffice.com/workspace-prices.aspx)上阅读有关不同企业版的功能和成本的信息。