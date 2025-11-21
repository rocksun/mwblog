[安全](https://thenewstack.io/Security/)不应被视为理所当然，无论你使用何种操作系统。你可能拥有一个 [Linux 桌面](https://thenewstack.io/8-linux-desktop-distributions-to-try/)，并认为它坚不可摧。持有这种想法，你就错了。

如果一台电脑连接到网络，它就是脆弱的。

大声朗读，一遍又一遍。

大多数操作系统都有内置的防火墙和其他保护系统，这很棒。然而，这并不意味着操作系统是固若金汤的。总有某种方式可能导致你的安全和/或隐私被侵犯，一旦发生，糟糕的事情就可能随之而来。

你不想发生那样的事情。

那么，你该怎么做？

你可以使用应用程序防火墙来加强你的桌面或笔记本电脑的安全性。

其中一个防火墙名为 [Portmaster](https://safing.io/)。

Portmaster 是一款免费的应用程序防火墙（尽管有更多功能的付费版本），它提供系统级安全保护，能揭示每个应用程序建立的每一次连接，以检测任何不符合你最佳利益的事物。

通过 Portmaster，你可以拦截广告和跟踪器、恶意软件、不适宜工作（NSFW）内容、欺骗性服务，设置全局和每个应用的选项，监控所有网络活动，设置安全 DNS，允许/阻止特定网站，阻止特定国家，阻止 P2P 连接等。这款应用程序防火墙能够自动化保护，因此它几乎是一个“一劳永逸”的工具。

Portmaster 由 [Safing.io](http://safing.io) 创建并维护，可以安装在 Linux 和 Windows 上（抱歉，不支持 macOS）。

让我们安装 Portmaster 并看看它是如何工作的。

## 你需要准备什么

我将在 Linux 上演示 Portmaster 的安装——具体来说是 [Ubuntu 25.10](https://thenewstack.io/ubuntu-25-10-scraps-x11-for-wayland-a-solid-step-forward/)。如果你使用 macOS 或 Windows，安装过程只需下载安装文件，双击并按照安装向导的指示操作即可。

对于 Linux 安装，你需要一个具有 sudo 权限的用户。对于所有安装，你都需要一个正常工作的网络连接。

就是这样。让我们开始安装吧。

## 在 Linux 上安装 Portmaster

Portmaster 为基于 Ubuntu 和 Fedora 的发行版提供了安装包。要在 Ubuntu Linux 上安装该应用，请将你的网络浏览器指向 [safing.io](http://safing.io) 网站，点击“下载”下拉菜单，然后选择 .deb 选项。做出选择后，点击“免费下载”并将文件保存到你的 ~/Downloads 目录中。

文件下载完成后，打开一个终端窗口，使用以下命令进入 Downloads 目录：

```
cd ~/Downloads
```

使用以下命令安装应用程序：

```
sudo dpkg -i Portmaster*.deb
```

如果你使用的是基于 Fedora 的发行版，安装命令将是：

```
sudo dnf install Portmaster*.deb
```

安装应该会顺利进行。安装完成后，你就可以使用该应用程序了。

## 使用 Portmaster

当你打开 Portmaster 时，会看到一个设置向导。第一步是点击 START NOW（图 1）来启动 Portmaster 服务，

[![screenshot](https://cdn.thenewstack.io/media/2025/11/09558bba-portmaster1.jpg)](https://cdn.thenewstack.io/media/2025/11/09558bba-portmaster1.jpg)

图 1：在 Portmaster 工作之前，你必须启动服务。

向导的下一步是自定义它要阻止的内容（跟踪器、广告等），并默认选择一个安全 DNS 服务。Portmaster 使用 Cloudflare，但你可以选择 Quad9、AdGuard 和 Foundation For Applied Privacy（图 2）。

[![screenshot](https://cdn.thenewstack.io/media/2025/11/8e7a12d5-portmaster4.jpg)](https://cdn.thenewstack.io/media/2025/11/8e7a12d5-portmaster4.jpg)

图 2：选择你的安全 DNS 服务。

安全 DNS 功能的优点在于它提供系统级保护，因此不限于你的网络浏览器。

设置向导完成后，你将进入 Portmaster 控制面板，在这里你可以实时查看正在发生的一切。

此时，打开你的网络浏览器并尝试访问任何网站。你应该在 Portmaster 控制面板上看到有多少连接被阻止了。例如，我只访问了 3 个不同的网站，就发现有 177 个连接被阻止（图 3）。

[![Screenshot](https://cdn.thenewstack.io/media/2025/11/70846388-portmaster6.jpg)](https://cdn.thenewstack.io/media/2025/11/70846388-portmaster6.jpg)

图 3：Portmaster 忙碌工作着。

我故意输入了一个错误的 URL（[msnb.com](http://msnb.com) 而不是 [msnbc.com](http://msnbc.com)），Portmaster 自动阻止了它（很可能是因为这个错误输入的 URL 导向了一个恶意网站）（图 4）。如果发生这种情况，Portmaster 不会提供你绕过阻止的方法；它就是被阻止了，仅此而已。

[![Screenshot](https://cdn.thenewstack.io/media/2025/11/5dc1b492-portmaster8.jpg)](https://cdn.thenewstack.io/media/2025/11/5dc1b492-portmaster8.jpg)

图 4：真遗憾 msnb.com，Portmaster 发现了你。

点击铃铛图标查看你的通知。在我的通知中，我得知有五个应用程序正在建立连接：Speech Dispatcher、Network Manager、Firefox 和 Chronyd。

你可以点击其中一个应用程序，然后配置 Portmaster 以特定方式对其进行操作。例如，当我打开 Firefox 条目（图 5）时，我发现 Portmaster 没有阻止连接（这是其正常运行所必需的）。

[![screenshot](https://cdn.thenewstack.io/media/2025/11/e8b8cdcd-portmaster9.jpg)](https://cdn.thenewstack.io/media/2025/11/e8b8cdcd-portmaster9.jpg)

图 5：配置 Portmaster 处理 Firefox。

我还可以点击“设置”选项卡，配置各种方面，例如网络范围、连接类型、规则、过滤列表等（图 6）。

[![screenshot](https://cdn.thenewstack.io/media/2025/11/3ae42f4d-portmaster10.jpg)](https://cdn.thenewstack.io/media/2025/11/3ae42f4d-portmaster10.jpg)

图 6：你可以自定义许多设置以获得更好的效果。

还有“全局设置”功能，你可以在其中重新配置设置向导中提供的设置，以及网络范围、连接类型、规则、子域阻止等。

我发现 Portmaster 在开箱即用状态下表现非常出色。我本可以花时间进一步配置该应用，但它在无需改动设置的情况下提供了足够的安全性。当然，你可能会发现它需要调整。如果你确实发现它提供的开箱即用安全性不够，请深入研究设置，看看是否可以根据你的需求进行改进。

你可以免费使用 Portmaster，或者购买 Portmaster Plus 账户（每月 4 欧元，约合 4.65 美元）以增加隐私、调查功能和 Safing 支持，或者购买 Portmaster Pro 账户（每月 9.90 欧元，约合 11.52 美元），后者增加了 SPN（Safing 隐私网络，一项专注于隐私的网络服务，通过多个隧道路由互联网连接）。

我建议你尝试一下免费版本。如果这还不够，你随时可以升级。