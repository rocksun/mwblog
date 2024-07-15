# Linux：了解 sudo 命令，掌控你的服务器

![关于 Linux：了解 sudo 命令，掌控你的服务器 的特色图片](https://cdn.thenewstack.io/media/2024/07/7bf564a8-jigar-panchal-rmxbyhgbxru-unsplash-sudo-1024x576.jpg)

你可能看过 XKCD 的漫画，其中一个人要求另一个人给自己做三明治。当第二个人拒绝时，第一个人回答说，“sudo 做个三明治给我”。

![XKCD 漫画“给我做个三明治”](https://cdn.thenewstack.io/media/2024/07/c692c1c0-xkcd-sandwich.png)

来源：[XKCD](https://imgs.xkcd.com/comics/sandwich.png)

当然，任何 Linux 用户都会对这个想法嗤之以鼻，因为他们知道第二个人别无选择，只能做三明治。为什么？因为…… *sudo*！

*Sudo* 代表超级用户执行，相当于 Windows 的 *以管理员身份运行* 命令。
让我给你一些背景信息。

当我第一次开始使用 Linux（大约在 1997 年）时，为了安装软件、编译内核或执行任何需要管理员权限的操作，我必须首先使用 *su* 命令（或 *su –*，如果你需要包含 root 的环境）切换到 root（或超级）用户。那时，我们对此毫不关心。事实上，人们可以以 root 用户身份登录 Linux 计算机，甚至以 root 用户身份安全地 shell 登录到机器。

这就像猫和狗住在一起一样，我们不知道这会带来什么危险。

你看，有了 root 用户，任何人都可以访问这些权限（如果他们知道——或者可以破解——root 用户的密码）。允许 root [SSH 访问](https://thenewstack.io/linux-limit-concurrent-users-on-your-server-with-ssh/) 就像[一场灾难的预兆](https://thenewstack.io/the-terrapin-attack-a-new-threat-to-ssh-integrity/)。

想象一下这种情况：你以 root 用户身份登录到你的 Linux 机器并执行一些随机任务。然后你被叫离电脑，忘记锁定桌面。任何人都可以走到机器旁，为所欲为……拥有完全的管理员权限。

你不想陷入这样的境地。事实上，作为经验法则，你永远不应该以 root 用户身份登录，并尽可能避免切换到 root 用户。这就是你需要[ sudo](https://www.sudo.ws/) 的帮助的原因。

幸运的是，在我开始使用 Linux 之前很久，Robert Coggeshall 和 Cliff Spenser 就编写了 *sudo* 的原始子系统。最初的版本大约是在 1980 年发布的。在 1986 年到 1993 年之间，*sudo* 由科罗拉多大学博尔德分校的 IT 员工进行了大量修改。大约在 1994 年，sudo 落到了 Todd C. Miller（一位 OpenBSD 开发者）的监护之下，他一直是守护者。

## sudo 的作用是什么？
本质上，*sudo* 为用户（属于[必要组](https://thenewstack.io/linux-user-and-group-management/)）提供了临时提升的权限，以便他们可以运行管理员任务（例如安装软件或使用类似 */etc/* 的文件修改配置文件）。

要使用此工具，用户键入 *sudo* 后面跟着他们要运行的命令。然后系统会提示他们输入用户密码，并在身份验证成功后运行该命令。

通过使用 *sudo*，root 用户不会被使用、触碰或影响。一旦用户成功使用 *sudo* 运行命令，他们将有 5 分钟的宽限期，在此期间他们无需再次输入用户密码即可运行另一个 *sudo* 命令。

换句话说，你可以运行类似 *sudo apt-get upgrade -y* 的命令，并在它完成后，转而运行类似 *sudo systemctl restart sshd* 的命令，而无需再次输入用户密码。如果下一个命令在 5 分钟窗口之外运行，则需要重新输入用户密码。

## 将用户添加到所需组
当你将用户添加到 Linux 时，一些发行版会自动将他们添加到 sudo。然而，大多数发行版不会这样做。将用户添加到所需组的方法取决于你使用的发行版。例如，基于 Ubuntu 的发行版使用 sudo 组，而基于 Fedora 的发行版使用 wheel 组。

因此，要将用户添加到 *sudo* 组，命令类似于：

```
sudo usermod -aG sudo USER
```

其中 USER 是要添加的用户名。

要将用户添加到 wheel 组，命令类似于：

```
sudo usermod -aG wheel USER
```

其中 USER 是用户名。

然后用户必须注销并重新登录才能使更改生效。一旦他们重新登录，他们就可以随意使用 sudo 的全部功能。

## sudoers 文件
这就是 *sudo* 变得有点棘手的地方。sudoers 文件是 *sudo* 的配置位置。此文件非常重要，它有自己的内置编辑器（换句话说，永远不要使用普通文本编辑器编辑 */etc/sudoers*），称为 *visudo*。*visudo* 编辑器会在你保存时验证 sudoers 文件的语法。这样，你就不太可能在配置中引入错误，这可能会造成灾难性的后果。
要打开 sudoers 文件，请执行以下命令：

1. `sudo visudo`

系统会提示您输入用户密码，验证成功后，您将在默认文本编辑器（例如 nano）中看到 sudoers 文件。sudoers 文件行的布局如下：

1. `root ALL=(ALL:ALL) ALL`

每个 ALL 都有特定的含义：

- 第一个 ALL 表示该规则适用于所有主机。
- 第二个 ALL 表示 root 用户可以以所有用户身份运行命令。
- 第三个 ALL 表示 root 用户可以以所有组身份运行命令。
- 第四个 ALL 表示该规则适用于所有命令。

我告诉过你，这很棘手。

您可以在 sudoers 文件中创建别名，以更轻松地创建自定义规则。假设您要创建一个适用于 olivia、camille、anton 和 clara 用户的规则。假设您想让这些用户访问 apt-get update 和 apt-get upgrade 命令，并且仅限于这些命令。为此，您可以在 sudoers 文件中创建如下别名：

1. `User_Alias GROUPONE = olivia, camille, anton, clara`

然后，您将像这样授予新组对命令的访问权限：

1. `GROUPONE ALL = /usr/bin/apt-get update`
2. `GROUPONE ALL = /usr/bin/apt-get upgrade`

保存并关闭文件后，GROUPONE 中的用户将能够运行这两个命令。

但是，您最好使用 *sudo* 和 wheel 组，这样您就不会通过 sudoers 文件对机器造成破坏。但是，如果您需要对管理员权限进行细粒度控制，sudoers 是最佳选择。

sudo 命令是正确 [Linux 管理和使用](https://thenewstack.io/how-to-manage-linux-storage/) 的必备工具。要了解有关 *sudo* 的更多信息，请使用命令 `man sudo` 阅读 [手册页](https://linux.die.net/man/8/sudo)。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)