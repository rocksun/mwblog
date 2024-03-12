
<!--
title: 使用Bash补全简化Linux和Docker命令行
cover: https://cdn.thenewstack.io/media/2024/03/e3ec3d33-wings.png
-->

通过 Tab 键，Bash 补全可以自动补全您最棘手的 Linux 和 Docker 命令。以下是设置方法。

> 译自 [Simplify Linux and Docker Command Lines with Bash Completion](https://thenewstack.io/simplify-linux-and-docker-command-lines-with-bash-completion/)，作者 Jack Wallen。

您是否难以记住所有 [Docker 命令](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)? 或者您可能无法记住 systemctl（其中有很多）可用的所有命令。如果您是 [Linux 新手](https://thenewstack.io/set-up-python-on-fedora-linux-4-steps/), [大量的命令](https://thenewstack.io/linux-pass-a-text-based-password-manager/)可能会非常令人生畏。

我使用 Linux 已有近 30 年，但我仍然难以记住所有命令。当我第一次踏上开源之路时，记住一个命令都很有挑战性。现在我在台式机和服务器上使用各种命令。

然后您将 Docker 等应用程序添加到组合中，它有许多自己的命令需要记住，学习过程变得更加复杂。

还记得上面提到的 systemctl 吗？可用的命令包括 *add-requires*、*is-enabled*、*reload*、*add-wants*、*is-failed*、*reload-or-restart*、*bind*、*isolate*、*rescue*、*cancel*、*is-system-running*、*reset-failed*、*cat*、*kexec*、*restart*、*condreload*、*kill*、*revert*……这甚至不是 systemctl 拥有的命令的四分之一。

然后是 Docker。在 Linux 上，如果我键入“do”并使用制表符补全（通过按键盘上的 Tab 键），我可能会看到以下内容：*do*、*dockerd-rootless-setuptool.sh*、*docker*、*dockerd-rootless.sh*、*docker-buildx*、*docker-init*、*docker-compose*、*docker-proxy*、*docker-credential-ecr-login*、*domainname*、*docker-credential-none*、*done*、*docker-credential-pass*、*do-release-upgrade*、*docker-credential-secretservice*、*dosfsck*、*dockerd* 和 *dosfslabel*。

这并没有什么帮助，因为尽管它可能让我们意识到 Docker 不止一个命令，但它不仅包含所有以 do 开头的命令，而且也没有帮助我们了解 Docker 包含像 *ps*、*images*、*import*、*info*、*inspect*、*pull*、*push*、*plugin*、*pause* ……您明白了。

也许您知道您要使用的 Docker 子命令以“p”开头，但这就是您所能记住的全部。当然，您可以梳理 Docker 手册页（使用命令“man docker”）。并不是说浏览手册页有什么问题——事实上，我强烈推荐这样做。在这个过程中，您一定会学到一些东西。

但是，当您需要快速回忆一个子命令时，您该怎么做？嗯，有一个小应用程序可以帮助您解决这个问题。所讨论的应用程序称为 [Bash 自动补全](https://github.com/scop/bash-completion)，它可以从 [大多数 Linux 发行版](https://thenewstack.io/linux-server-operating-systems-red-hat-enterprise-linux-and-beyond/) 的标准存储库中获得。

现在，Bash 自动补全应用程序适用于 [Linux 命令](https://thenewstack.io/fosdem-24-can-the-unix-shell-be-improved-hell-yes/)，因此您只需安装它即可开始使用。但是，对于 Docker，您必须执行一个额外的步骤才能使其正常工作。

在我们开始之前，让我们安装此应用程序。

## 安装 Bash 自动补全

某些发行版默认安装了此应用程序。如果您不确定，您可以运行安装命令，您的包管理器会告诉您它是否已经可用。

对于 [基于 Debian/Ubuntu 的发行版](https://thenewstack.io/what-is-ubuntu-pro-and-how-can-you-use-it/)，安装命令为：

```
sudo apt-get install bash-completion -y
```

对于基于 Fedora/ [Red Hat](https://www.openshift.com/try?utm_content=inline-mention) Enterprise Linux 的发行版，命令为：

```
sudo dnf install bash-completion -y
```

安装应用程序后，您可以通过键入以下内容进行测试：

```
systemctl s
```

按键盘 Tab 键两次，您将看到 systemctl 可用的所有子命令。

## 添加 Docker 支持

要为 bash-completion 添加 Docker 支持，您必须下载名为 Docker complete 的文件并将其复制到 */etc/bash_completion* 目录。您可以使用以下命令执行这两个操作：

```
sudo curl https://raw.githubusercontent.com/docker/docker-ce/master/components/cli/contrib/completion/bash/docker -o /etc/bash_completion.d/docker.sh
```

在某些发行版上，您可能会遇到权限错误。如果是这种情况，您需要首先发出命令：

```
sudo -s
```

处理完后，重新运行 curl 命令。它应该会顺利进行。

完成此操作后，您可以使用 Docker 测试 bash-completion。例如，键入：

```
docker i
```

按 Tab 键两次，您将看到如下输出：

```
image images import info inspect
```

键入“docker p”并按 Tab 键两次以显示如下输出：

```bash
pause   plugin  port    ps      pull    push
```

输出应该会唤起你的记忆，以便你可以运行所需的命令。

## 警告

Bash 补全是一个方便的工具，它会很乐意提醒你所需命令可用的子命令。但是，它无法帮助你处理与子命令关联的各种选项。

例如，如果你键入“docker ps”并按两次 Tab 键，它不会列出选项，其中包括
*-a*（或 *–all*）、*-f*（或 *–filter*）、*–format*、*-n*（或 *–last*）、*-l*（或 *–latest*）、*–no-trunc*、*-q*（或 *–quiet*）、*-s*（或 *–size*）。如果你不确定可用选项，久经考验的手册页是你的朋友。

例如，你可以键入：

```
man docker ps
```

按 Enter 键，你将看到该命令可用的所有选项。大多数 Docker 子命令也是如此。键入“man docker”，后跟你要了解的子命令，然后按 Enter 键。知识世界将呈现在你眼前。

这就是简化 Linux 和 Docker 命令行的全部内容。对于 Linux 可用的看似无穷无尽的命令，你应该乐于接受任何可以获得的帮助。
