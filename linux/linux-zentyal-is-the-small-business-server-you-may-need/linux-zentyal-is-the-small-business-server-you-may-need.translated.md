# Linux：Zentyal可能是您需要的SMB服务器

![Featued image for: Linux: Zentyal Is the Small Business Server You May Need](https://cdn.thenewstack.io/media/2025/01/bae3809b-zentyal-1024x683.png)

在[Linux](https://thenewstack.io/learning-linux-start-here/)领域，某些发行版专门面向企业服务器使用。最受欢迎的选项包括[Red Hat Enterprise Linux](https://www.openshift.com/try?utm_content=inline+mention)、[AlmaLinux](https://thenewstack.io/almalinux-10-beta-supports-older-x86-chipsets/)、[Rocky Linux](https://thenewstack.io/ciq-unveils-a-version-of-rocky-linux-for-the-enterprise/)、[Oracle Linux](https://orca.security/?utm_content=inline+mention)和[CentOS Stream](https://thenewstack.io/back-to-the-future-a-look-at-centos-streams/)。

但这并非所有可用的选项。有些发行版可能知名度不高，但这并不意味着它们不可行。

其中一个发行版是[Zentyal](https://www.zentyal.com)，它是Windows Server的Linux替代方案，包括以下功能：

- 域和目录服务器
- 邮件服务器
- 防火墙
- 入侵检测/入侵防御系统
- Iproute2、Netfilter、Squid、Suricata和FreeRADIUS
- 基于域的HTTPS网页阻止
- NTP服务器
- 证书颁发机构
- VPN
- 备份
- FTP
- IPSec/L2TP
- 反病毒
- 实时警报
- 每日报告
- 内核管理
- HTTP代理中的用户身份验证
- Docker容器
- 入侵防护
- Jabber服务器
- Web服务器
- 等等

Zentyal提供免费的社区版和付费版。付费版有多个价格等级。（更多信息，请查看[Zentyal定价矩阵](https://www.zentyal.com/price-yearly-zentyal-server-subscription/)。）我建议您先[下载并安装社区版](https://download02.public.zentyal.com/zentyal-8.0-development-amd64.iso?_gl=1*r7qpip*_gcl_au*MTkwNTI2MTQ3OS4xNzE1MTgxOTMw*_ga*MTg2OTA1MTc5Ny4xNzE1MTgxOTMw*_ga_N2CRZTM10X*MTcyMTE1NDU2NS40My4xLjE3MjExNTY2MzQuNTkuMC4w&_ga=2.204391384.972608446.1721055844-1869051797.1715181930)。如果您喜欢，可以考虑购买完整产品的许可证。

我已经有一段时间没有测试Zentyal了，所以我下载了最新版本，并在Pop!_OS Linux的VirtualBox中将其作为虚拟机运行了一下。以下是我的一些印象。

## 安装

鉴于Zentyal基于[Ubuntu 22.04](https://thenewstack.io/how-to-safely-upgrade-ubuntu-22-04-to-ubuntu-24-04/)，因此安装非常容易也就不足为奇了。事实上，这几乎是一个点击即可完成的操作，不到五分钟就能进入登录提示符。如果您能够安装软件，那么您就能安装Zentyal。

## 安装后

这时我开始回忆为什么Zentyal给我留下了如此深刻的印象。首次登录后，默认浏览器将打开。在登录页面，您会看到一个入门向导。通过此向导，您可以选择要安装的软件（图1）。

<br>

图1：选择要在Zentyal服务器上安装的软件包。

<br>

选择您想要的软件包，向下滚动并单击“安装”。然后系统会提示您通过单击“继续”来确认所选软件包的安装。将出现一个新页面（带有可爱的熊猫），显示软件包安装的进度。单击“继续”几分钟后，我选择的所有软件都已安装并可以使用。应用程序安装完成后，系统会提示您配置网络接口（图2）。

<br>

图2：我只有一个网络接口，因此设置很简单。

<br>

然后系统会要求您选择服务器类型，即独立服务器或附加域控制器（图3）。

<br>

图3：如果您的Zentyal服务器是域的一部分，请确保选择“附加域控制器”。

<br>

根据您添加到服务器的组件，您可能还需要执行一些其他配置步骤，例如为邮件服务器创建虚拟邮件域。完成所有操作后，单击“完成”，配置将被应用。

## 在当前的Ubuntu部署上安装Zentyal

如果您已经部署了Ubuntu服务器，可以在其上添加Zentyal的社区版。以下是执行此操作的命令：

首先，使用以下命令下载安装脚本：

```bash
wget https://raw.githubusercontent.com/zentyal/zentyal/master/extra/ubuntu_installers/zentyal_installer_8.0.sh
```

使用以下命令授予安装程序可执行权限：

```bash
sudo chmod u+x zentyal_installer_8.0.sh
```

最后，运行安装程序：

```bash
sudo ./zentyal_installer_8.0.sh
```

选择您是想通过控制台还是GUI安装Zentyal。（如果您将Zentyal作为虚拟机安装，建议使用控制台选项；否则，您可能会遇到问题。）
按照安装步骤进行操作。完成后，您可以通过 https://SERVER:8443/ （其中 SERVER 是主机 IP 地址）访问 Zentyal Web 界面。

需要注意的是，以这种方式安装后，Zentyal 允许 [sudo 组](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/) 中的任何用户访问 Web 界面。因此，您可能需要考虑将某些用户从该组中移除，或在 `/etc/sudoers` 中配置它们以限制其访问权限。

无论您如何安装 Zentyal，您都可以通过 https://SERVER:8443/Dashboard/Index 页面（其中 SERVER 是主机 IP 地址）访问仪表板。您可以从仪表板管理所有服务。例如，如果您计划将 Zentyal 用于 Docker 容器，请单击侧边栏中的 Docker 条目，然后系统会提示您启用 Portainer（用作容器管理器）。

## 最后

我不会说 Zentyal 是一个轻松愉快的傻瓜式操作软件。是的，它确实有一个设计良好的基于 Web 的界面，但仍然存在一定的学习曲线。某些组件必须按照一定的顺序进行配置——例如那些依赖于 SSL 证书的组件，需要您先颁发新的证书才能正常工作。这将取决于您安装的模块及其依赖项。

就为您的企业部署 Linux 服务器而言，Zentyal 是一个极好的选择。它可能不如其他一些服务器系统那样“即插即用”，但对于任何管理员来说，Zentyal 都足够容易部署和使用，并能满足几乎任何企业的需求。

[订阅我们的 YouTube 频道](https://youtube.com/thenewstack?sub_confirmation=1) 以观看我们的播客、访谈、演示等等。技术发展迅速，不要错过任何一集！