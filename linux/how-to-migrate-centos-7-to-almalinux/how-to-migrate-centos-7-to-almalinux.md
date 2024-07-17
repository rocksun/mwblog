
<!--
title: 如何从CentOS 7迁移到AlmaLinux
cover: https://cdn.thenewstack.io/media/2024/07/31ad3212-alma-linux.jpg
-->

CentOS 7 已寿终正寝。虽然旅程愉快，但它已经结束了。迁移到 AlmaLinux 是一个简单的升级路径。它比你想象的更容易。以下是操作方法。

> 译自 [How to Migrate CentOS 7 to AlmaLinux](https://thenewstack.io/how-to-migrate-centos-7-to-almalinux/)，作者 Jack Wallen。

以前的 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) CentOS 7 Linux 发行版 [已经停止维护](https://thenewstack.io/havent-migrated-off-centos-yet-you-have-until-june-30/)。这是一段 [有趣的旅程](https://thenewstack.io/centos-9-stream-is-now-available-but-should-you-use-it/)，但它已经结束了。您可以将 CentOS 7 升级到 [CentOS Stream](https://thenewstack.io/wherefore-art-thou-centos-rocky-linux-cloudlinux-and-centos-stream/)，但大多数人对此持谨慎态度（因为 Stream 的滚动发布特性）。另一个选择是迁移到其他发行版，例如 [AlmaLinux](https://thenewstack.io/jack-aboutboul-how-almalinux-came-to-be-and-why-it-was-needed/)。

听起来很复杂，对吧？您可能需要部署一台运行最新版 [AlmaLinux](https://thenewstack.io/almalinux-captures-the-soul-of-centos/) 的新服务器，将所有数据从一台机器复制到另一台机器，重建您的应用程序/服务以使其运行，并希望一切顺利。

幸运的是，由于 [AlmaLinux](https://thenewstack.io/linux-and-cloud-native-security-almalinux/) 开发人员的努力，现在有一个更简单的方法可以做到这一点。

我将带您完成此过程。

## 您需要什么

要使此操作正常工作，您需要一个运行的 CentOS 7 实例，一个具有 [sudo 权限](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/) 的用户，以及一个外部驱动器（以防万一）。

## 备份关键数据

在执行任何操作之前，请确保将 CentOS 7 服务器上的所有关键数据备份到外部驱动器。我建议您备份以下信息：

- 配置文件（例如在 /etc 中找到的那些文件）。
- 用户数据。
- 应用程序数据。
- 任何自定义脚本。
- 定时任务。
- 服务配置（例如 SSH、Apache、Samba）。
- SSH 密钥。
- 关键任务日志。
- 虚拟主机。
- 容器。
- 电子邮件配置。

确保获取所有内容。

## 更新 CentOS 7

在进行迁移之前，您需要确保升级 CentOS 7。CentOS 7 的生命周期已于 2024 年 6 月 30 日结束，因此可能没有可用的更新。

要更新，请执行以下命令：

```
sudo dnf update -y
```

更新完成后，使用以下命令重新启动服务器：

```
sudo reboot
```

## 安装必要的软件包

接下来，我们需要安装 elevate-release 软件包，该软件包用于迁移。要安装此软件包，请执行以下命令：

```
sudo yum install -y http://repo.almalinux.org/elevate/elevate-release-latest-el$(rpm --eval %rhel).noarch.rpm
```

elevate-release 软件包确实包含对第三方存储库的支持，例如 EPEL、Imunify、KernelCare、MariaDB、nginx 和 PostgreSQL。

完成后，使用以下命令安装 *leapp-upgrade* 和 data 软件包：

```
sudo yum install -y leapp-upgrade leapp-data-almalinux
```

## 运行预升级检查

要继续，您必须运行预升级检查，这将让您知道是否可以继续迁移。您可能会发现报告中包含必须克服的错误，才能运行迁移。

预升级命令为：

```
sudo leapp preupgrade
```

这将生成一个包含可能问题的答案文件。要查看该文件，请执行以下命令：

```
sudo cat /var/log/leapp/answerfile
```

您可能会发现某些软件包不再可用，已被替代品替换。例如，pam_pkcs11_module 已被 SSSD 替换，因此您必须确认该问题的解决方案，这可以通过以下命令完成：

```
sudo leapp answer –section remove_pam_pkcs11_module_check.confirm=True
```

您也可以手动编辑文件，逐个查看每个问题并按照说明进行操作。例如，上述模块的手动验证需要您更改以下行：

```
# Confirm = 
```

至

```
Confirm = True
```

AlmaLinux 已编译了一个 [常见 ELevate 问题列表](https://wiki.almalinux.org/elevate/ELevate-frequent-issues.html)。如果您在报告中看到错误，请确保检查问题页面以查看您的问题是否包含在内（以及问题的解决方法）。

以下修复程序应解决从 CentOS 7 迁移时最常报告的问题：

```
sudo rmmod pata_acpi
echo PermitRootLogin yes | sudo tee -a /etc/ssh/sshd_config
sudo leapp answer --section remove_pam_pkcs11_module_check.confirm=True
```

## 开始升级

解决预升级检查中发现的问题后，就可以使用以下命令启动迁移：

```
sudo leapp upgrade
```

升级完成后，您需要重新启动机器。您现在应该发现机器正在运行 AlmaLinux 8。现在是时候升级到最新版本了。

## 升级 AlmaLinux
现在您已从 CentOS 7 迁移到 AlmaLinux 8，是时候从 AlmaLinux 8 升级到 AlmaLinux 9 了。为此，您必须使用以下命令打开 **yum.conf** 文件进行编辑：

```
sudo nano /etc/yum.conf
```

在该文件中，确保删除与 elevate 或 leapp 相关的 exclude= 行中的任何内容（例如 leapp-upgrade-el7toel8）。完成此操作后，保存并关闭文件。

接下来，使用以下命令打开 **dnf.conf** 文件：

```
sudo nano /etc/dnf/dnf.conf
```

在此文件中执行与 **yum.conf** 中相同的操作。

运行检查以查看是否存在来自 CentOS 7 的任何剩余软件包，命令如下：

```
rpm -qa | grep el7
```

如果您在输出中看到任何内容，请考虑删除这些软件包。通过检查 elevate 或 leapp 软件包执行相同的操作，命令如下：

```
rpm -qa | grep elevate
rpm -qa | grep leapp
```

如有必要，请从上述两个命令的输出中删除任何软件包。

最后，使用以下命令清理所有内容：

```
sudo dnf clean all
```

要将 AlmaLinux 8 迁移到 9，请使用以下命令安装 elevate-release 软件包：

```
sudo yum install -y http://repo.almalinux.org/elevate/elevate-release-latest-el$(rpm --eval %rhel).noarch.rpm
```

使用以下命令运行安装：

```
sudo yum install -y leapp-upgrade leapp-data-almalinux
```

最后，使用以下命令运行提升：

```
sudo leapp upgrade
```

完成后，您可以使用以下命令重新启动：

```
sudo reboot
```

此时，您的发行版应为 AlmaLinux 9（使用命令 `cat /etc/os-release` 检查）。如果一切正常运行，则您已完成。

我建议您首先在非生产机器上运行此过程。您也可以在开始此过程之前克隆 CentOS 7 驱动器。这样，如果发生任何灾难性事件，您可以将克隆的映像复制回服务器。
