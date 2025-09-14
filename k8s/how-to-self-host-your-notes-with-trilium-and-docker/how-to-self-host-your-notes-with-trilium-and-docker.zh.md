我一直在寻找一款笔记应用，它不需要依赖第三方或云服务来使我的笔记在不同设备上同步。我希望能够在我的书桌旁或家里的任何地方通过笔记本电脑处理我的笔记。

有很多选择，但我希望使用 [Linux 作为我的服务器](https://thenewstack.io/linux-server-operating-systems-red-hat-enterprise-linux-and-beyond/)，我发现 [Trilium](https://github.com/TriliumNext/Trilium) 非常适合。Trilium 唯一的缺点是没有官方的移动应用程序。你可以从 Google Play 商店之外侧载一个 Trilium 应用程序，但我不建议在 Android 上侧载应用程序，因为你永远不知道会得到什么。

我的设置使用 [Ubuntu 24.04](https://thenewstack.io/how-to-safely-upgrade-ubuntu-22-04-to-ubuntu-24-04/) 作为服务器，并在 Linux ([Pop!\_OS](https://thenewstack.io/pop_os-one-of-the-best-linux-distros-for-creators-of-all-types/)) 和 macOS 上安装桌面应用程序。一旦我启动并运行所有内容，它显然成为了我的首选笔记设置。不，我无法在我的局域网之外访问它（主要是因为我的 ISP 不允许），但如果我在我的家庭网络上，我可以从任何地方访问它。

## 为什么选择 Trilium 进行自托管笔记？

除了它满足了我所有的操作系统要求外，Trilium 拥有我需要的所有功能，包括：

* 用于存储笔记的树状结构
* WYSIWYG 编辑器，包括表格、图像、数学和 markdown 自动格式化
* 语法高亮
* 笔记版本控制
* 查询和高级脚本
* OpenID 和 TOTP 支持
* 自托管服务器
* 共享到公共网络
* 所有笔记的强加密
* 关系图
* 草图图表
* 思维导图
* 带有位置图钉和 GPX 轨迹的地理地图
* 通过 REST API 自动化
* 触摸优化
* 深色和浅色主题
* Evernote 和 Markdown 导入/导出
* 可定制的 UI
* 指标

正如你所看到的，Trillium 包括你在笔记应用程序中需要的所有功能，正是这个功能列表让我决定设置它。

说到这里，让我们开始吧。

## 安装所需的内容

要将 Trilium 部署为服务器，你需要一个支持 Docker 和 [Docker Compose](https://thenewstack.io/build-your-own-private-cloud-at-home-with-docker/) 的操作系统。至于桌面端，你可以将该应用程序安装在 Linux、macOS 或 Windows 上。确保从 [Trilium 发布页面](https://github.com/TriliumNext/Trilium/releases/tag/v0.98.1) 下载正确的安装程序。

至于 Docker/Docker Compose 的安装，具体方法取决于你使用的操作系统。对于我的目的，我可以作弊并使用以下命令从标准 Ubuntu 存储库安装 Docker 和 Docker Desktop：

```
sudo apt-get install docker.io docker-compose -y
```

完成后，使用以下命令将你的用户添加到 Docker 组：

```
sudo usermod -aG docker $USER
```

注销并重新登录，以使更改生效。

让我们部署我们的服务器。

## 使用 Docker 部署 Trilium 服务器容器

你可以使用单个命令部署服务器，该命令会提取最新版本的 Trilium 服务器，设置主机名，将外部端口 8080 映射到内部端口 8080，挂载卷并设置 LOCALE。

该命令是：

```
docker run -d \
--name trilium \
--hostname HOSTNAME \
-p 8080:8080 \
-v trilium-data:/root/trilium-data \
-e TZ=LOCALE \
zadam/trilium:latest
```

其中 HOSTNAME 是你要为实例设置的主机名，LOCALE 是你所在的位置（例如 America/New York）。该命令将提取 Trilium 的最新镜像并开始部署容器。命令完成后，你将看到报告的容器 ID。

然后，你可以通过将浏览器指向 http://SERVER:8080 （其中 SERVER 是托管服务器的 IP 地址）来访问基于 Web 的 UI。

## 将桌面应用程序连接到 Trilium 服务器

我不知道你怎么想，但我不喜欢在使用完全合适的桌面应用程序时打开另一个浏览器选项卡（Trilum 就是这种情况）。鉴于桌面应用程序能够连接到服务器，因此你的所有实例都彼此同步，这非常有意义。你的桌面应用程序和服务器应用程序的版本相同非常重要。如果你使用的是最新的服务器和较旧的桌面客户端，它们将无法同步。

首先，你必须在你的操作系统上安装桌面应用程序。这应该相当简单。安装应用程序后，从桌面菜单启动它。当设置向导的第一页出现时（图 1），选择“我已经有一个服务器实例，并且想要设置与其同步。”

[![Screenshot](https://cdn.thenewstack.io/media/2025/09/27fa2534-trilium1.jpg)](https://cdn.thenewstack.io/media/2025/09/27fa2534-trilium1.jpg) 图 1：Trilium 设置非常简单。

单击“下一步”，然后在结果页面上（图 2），填写必要的信息，这将是 Trilium 服务器地址 (http://IP\_ADDRESS:PORT，其中 IP\_ADDRESS 是托管服务器的地址，PORT 是 8080)。此外，你需要为此实例设置密码。

[![Screenshot](https://cdn.thenewstack.io/media/2025/09/adb45fa2-trilium2.jpg)](https://cdn.thenewstack.io/media/2025/09/adb45fa2-trilium2.jpg) 图 2：你还可以设置代理服务器，但我们的 LAN 设置不需要它。

单击“完成设置”，应该建立连接。设置向导将自动将你重定向到 Trilim 主页，你应在该页面上看到你之前添加的任何笔记（图 3）。

[![Screenshot](https://cdn.thenewstack.io/media/2025/09/dd82f114-trilium3.jpg)](https://cdn.thenewstack.io/media/2025/09/dd82f114-trilium3.jpg) 图 3：请务必查看 Trilium 演示笔记，以便了解应用程序的工作方式。

我的笔记朋友们，这就是部署你自己的内部同步笔记服务的所有内容。我发现这种组合对我的需求非常有效，我相信你也会有同样的感觉。