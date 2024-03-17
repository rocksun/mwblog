<!--
title: 使用Borgmatic备份您的Linux服务器
cover: https://cdn.thenewstack.io/media/2024/03/31123857-ai-generated-7822840_1280-1024x682.jpg
-->

我们将一步步引导您完成Borgmatic的安装和配置，确保您的服务器数据在发生意外时得到及时备份和恢复。

> 译自 [Back up Your Linux Server with Borgmatic](https://thenewstack.io/back-up-your-linux-server-with-borgmatic/)，作者 Jack Wallen。

作为 [Linux 管理员](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/)或[开发人员](https://thenewstack.io/start-developing-with-rocky-linux-as-a-docker-container/)，您完全理解备份的重要性。事实上，您应该将其视为必须的。毕竟，抵抗是徒劳的。

想象一下，您部署了一台存储大量数据或最新开发项目的服务器，但出现了某些问题。如果所有这些数据丢失了，会发生什么情况？

别再想了。

这就是为什么备份是必须的。没有备份，您就有可能失去不仅仅是信息，还有时间、金钱、客户等等重要的东西。

那么，为什么要冒这个风险呢？

幸运的是，这是 Linux，这意味着有几种备份服务器的方法。其中一种方法是通过 [Borgmatic](https://torsion.org/borgmatic/) 进行，它是一种简单的、基于配置的解决方案，可以使用客户端加密备份文件和数据库，并支持第三方集成。

我想引导您完成 [Borgmatic](https://torsion.org/borgmatic/) 的安装和设置，这样您就不用再为满足您需求的备份解决方案而担心了。

## 您需要什么

我将在 Ubuntu Server 22.04 上演示，这意味着您只需要操作系统的正在运行的实例和具有 [sudo 权限](https://thenewstack.io/serious-sudo-trouble-for-linux-distros/)的用户。准备好这两个条件后，就可以开始安装了。

## 安装 Borgmatic

登录到您的 Ubuntu Server 实例。您可能应该先运行一次更新/升级。但是，请记住，如果内核被升级，您需要重新启动服务器才能使更改生效。您可以使用以下命令运行更新/升级:

```bash
sudo apt-get update && sudo apt-get upgrade -y
```

当上述操作完成后，重启(如果需要)，然后使用以下命令安装 Borgmatic:

```bash
sudo apt-get install borgmatic -y
```

安装完成后，您就可以继续下一步操作了。

## 初始化第一个仓库

创建一个新目录，用作 Borgmatic 仓库。假设您有一个外部驱动器(即 /dev/sda1)连接到机器上，并挂载到 /backup 目录。要做到这一点，您必须在 /etc/fstab 文件中添加一个条目，如下所示:

```bash
/dev/sda1 /backup ext4 defaults 0 0
```

您必须确保 /backup 目录存在。如果不存在，请使用以下命令创建:

```bash
sudo mkdir /backup
```

您可以使用以下命令测试挂载:

```bash
mount -a
```

如果输出为空，说明一切正常。

完成后，切换到备份目录，使用以下命令:

```bash
cd /backup
```

使用以下命令初始化仓库:

```bash
borg init -e repokey data.borg
```

您可以给仓库起任何您喜欢的名字(替换 data.borg)。在此过程中，系统会提示您输入并验证新仓库的密码。完成后，您将在 /backup 中找到一个名为 data.borg 的新目录。

## 配置 Borgmatic

下一步是生成第一个配置文件，使用以下命令:

```bash
generate-borgmatic-config -d data.yaml
```

确保将 YAML 文件命名为您为仓库命名的名称(为了保持一致性)。使用以下命令打开该文件进行编辑:

```bash
nano data.yaml
```

首先，您需要修改 source_directories 部分，它看起来像这样:

```bash
source_directories:
     - /home
     - /etc
     - /var/log/syslog*
```

删除或添加您希望备份的任何目录。例如，如果您想备份 /var/www/html/，它将如下所示:

```bash
source_directories:
     - /home
     - /etc
     - /var/log/syslog*
     - /var/www/html
```

滚动到 repositories 部分，它看起来像这样:

```bash
repositories:
     - user@backupserver:sourcehostname.borg
     - user@backupserver:{fqdn}
```

注释掉默认的 repositories 并添加新的一个，使它看起来像这样:

```bash
repositories:
     - data.borg
#     - user@backupserver:sourcehostname.borg
#     - user@backupserver:{fqdn}
```

您也可以直接删除该部分的最后两行(而不是注释掉)。

保存并关闭文件。

## 运行您的第一次备份

一切就绪后，是时候开始测试 Borgmatic 了。要启动第一次备份，请输入命令:

```bash
sudo borgmatic --config data.yaml --verbosity 1
```

出现提示时，输入您的 sudo 密码。然后系统会提示您输入第二个密码，这是您为 data.borg 设置的仓库密码。备份应该开始并完成。您的备份目录中包含的数据量将决定备份所需的时间长短。完成后，您应该会看到一个时间戳和一个随机字符串。

## 自动化您的备份

您不希望每次都手动运行备份命令，因此让我们来设置一个自动化的备份过程。编辑您的 data.yaml 文件，在文件末尾添加以下内容:

```bash
location:
    source_directories:
        - /backup/borgmatic
    repositories:
        - data.borg

retention:
    keep_daily: 7
    keep_weekly: 4
    keep_monthly: 6
    keep_yearly: 3

consistency:
    checks:
        - repository
        - data 

scripts:
    backup_folders.sh: |
        borg create --stats --filter=AME --list=always --compression lz4 --verbose {repository.data_path}::{source_data_name}_{hostname}_{current_date} {source_directory.path} {flags}

schedule:
    hourly:
        disabled: True
    daily:
        time: "6:00"
    weekly:
        disabled: True
    monthly:
        disabled: True
```

您可以更改定时器配置，使其在您需要的日期/时间运行。您在上面看到的内容每天在午夜运行。

保存并关闭文件。

使用以下命令启动并启用 Borgmatic 以在启动时运行：

```bash
sudo systemctl enable --now borgmatic.timer
```

再次，系统将提示您输入 data.borg 存储库密码。一旦您成功认证，备份将被启用，并且每天在午夜运行。

就是这样，您刚刚在 Linux 服务器上创建了一个可靠且高效的备份系统。如需了解有关 Borgmatic 的更多信息，请务必查阅[官方文档](https://torsion.org/borgmatic/docs/reference/configuration/)。