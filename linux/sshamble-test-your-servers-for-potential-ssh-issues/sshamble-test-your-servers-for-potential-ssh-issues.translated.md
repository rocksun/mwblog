# SSHamble：测试您的服务器是否存在潜在的 SSH 问题

![SSHamble：测试您的服务器是否存在潜在的 SSH 问题的特色图片](https://cdn.thenewstack.io/media/2024/08/26c52924-shamble-1024x683.png)

对于大多数 [Linux 管理员](https://thenewstack.io/learning-linux-start-here/) 来说，使用 [安全 Shell](https://thenewstack.io/linux-ssh-and-key-based-authentication/)（[SSH](https://thenewstack.io/dr-torq-go-remote-with-ssh/)) 是必要的。这种安全的网络协议不仅允许您远程访问需要管理的机器，还可以将文件复制到服务器和从服务器复制文件（使用 [scp 命令](https://thenewstack.io/linux-lesson-copy-files-over-your-network-with-scp/))，并使用 SSH 密钥身份验证（为了更高的安全性）。

但是，仅仅因为 SSH 比类似协议安全得多，并不意味着它就无懈可击。多年来，已经发现（并修补）了几个 SSH 漏洞，这证明没有什么是 100% 安全的。

这就是为什么尽可能保证 SSH 安全至关重要的原因。这可以通过配置文件（例如 */etc/ssh/sshd_config* 和 */etc/ssh/ssh_config*）来完成。但这并不总是足够的，因为您可能知道也可能不知道您的 SSH 配置有多容易受到攻击。

幸运的是，有一些工具可以帮助您，比如 [SSHamble](https://github.com/runZeroInc/sshamble)。SSHamble 是一个由 RunZero 管理的开源项目，被定义为 SSH 实现的研究工具。该工具检查以下内容：

- 针对身份验证的攻击
- 会话后身份验证攻击
- 身份验证前状态转换
- 身份验证计时分析
- 会话后枚举

根据 [SSHamble](https://www.runzero.com/sshamble/) 网站的说法，该应用程序“模拟潜在的攻击场景，包括由于意外状态转换导致的未经授权的远程访问、会话后登录实现中的远程命令执行，以及通过无限高速身份验证请求导致的信息泄露。SSHamble 交互式 shell 提供对会话后（但执行前）环境中 SSH 请求的原始访问，允许对环境控制、信号处理、端口转发等进行简单测试。”

听起来很重要，对吧？

是的。非常重要。

但是如何使用 SSHamble 呢？

让我来向您展示。

## 安装 SSHamble

您必须做的第一件事是安装 SSHamble。因为它在标准存储库中找不到，所以您需要执行几个步骤才能启动并运行它。我将演示两种不同的安装方法。

第一种方法需要安装 Go。我将在 Ubuntu Desktop 22.04 的实例上进行演示。如果您使用的是不同的 Linux 发行版，则需要修改 Go 安装步骤。不幸的是，SSHambe 要求 Go 的最低版本为 1.23，而从标准存储库安装的版本不满足该依赖关系。相反，请使用以下命令下载 Go 源代码：

```bash
wget https://go.dev/dl/go1.23.0.linux-386.tar.gz
```

接下来，使用以下命令安装 Go：

```bash
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.23.0.linux-386.tar.gz
```

使用以下命令将 /usr/local/go/bin 添加到您的 $PATH 中：

```bash
export PATH=$PATH:/usr/local/go/bin
```

您还可以将上述行添加到 ~/.bashrc 文件的底部。完成后，使用以下命令获取文件：

```bash
source ~/.bashrc
```

安装 Go 后，使用以下命令克隆 SSHamble Git 存储库：

```bash
git clone https://github.com/runZeroInc/sshamble
```

如果该命令提示 git 未安装，请使用以下命令 [解决该问题](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/)：

```bash
sudo apt-get install git -y
```

使用以下命令切换到新创建的目录：

```bash
cd sshamble
```

使用以下命令构建 SSHamble：

```bash
go build -o sshamble
```

如果您收到一条错误消息，指出“bits/libc-header-start.h: No such file or directory”，则可以使用以下命令安装 *gcc-multilib* 来更正它：

```bash
sudo apt-get install gcc-multilib -y
```

安装完成后，使用以下命令将 SSHamble 二进制文件复制到 */usr/local/bin*（以便可以从文件系统层次结构中的任何位置运行该命令）：

```bash
sudo cp sshamble /usr/local/bin
```

然后，您可以通过发出以下命令来验证安装：

```bash
sshamble -h
```

您应该会看到帮助文件出现。如果是这样，您就可以开始了。

## 使用 SSHamble

首先，发出以下命令：

```bash
sshamble scan -h
```

这将列出可用于测试的全套目标。
假设您要对网络中的每台机器运行扫描。我们假设 IP 地址方案为 192.168.1.0/24。为此，请发出以下命令：

```bash
sshamble scan -o results.json 192.168.1.0/24
```

根据您网络上的机器数量，扫描可能需要一些时间。扫描完成后，您将在当前工作目录中找到 results.json 文件。
下一步是分析结果。您可以遍历整个 [JSON 文件](https://thenewstack.io/an-introduction-to-json/) 以尝试理解，或者您可以使用如下所示的分析选项：

```bash
sshamble analyze -o results-directory results.json
```

分析所需的时间比扫描少得多。如果随后进入 results-directory 文件夹，您将看到几个 .csv 文件，例如 *stats_auth_methods.csv*、*stats_hostkey_algos.csv*、*stats_kex_algos.csv* 和 *stats_session_methods.csv*（在我的结果目录中，完整网络扫描后有 12 个文件）。
例如，在 *stats_auth_methods.csv* 文件中，我看到以下结果：

```
publickey,6,192.168.1.11 192.168.1.142 192.168.1.166 192.168.1.176 192.168.1.253 192.168.1.30
password,6,192.168.1.11 192.168.1.142 192.168.1.166 192.168.1.176 192.168.1.253 192.168.1.30
keyboard-interactive,1,192.168.1.253
```

以上表明哪些机器包含 SSH 密钥身份验证，哪些使用密码，以及哪些具有键盘交互（例如用于 2FA）。

浏览每个文件，查看 SSHamble 发现了什么。您可能会惊讶地发现，您可能需要弥补几个问题，才能尽可能地保证 SSH 的安全。

这就是使用 SSHamble 测试网络上 SSH 实现的全部内容。尽管 SSHamble 的文档有点少，但以上命令应该足以让您开始使用这个方便的工具。

[YOUTUBE.COM/THENEWSTACK
技术发展日新月异，请勿错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、采访、演示等内容。](https://youtube.com/thenewstack?sub_confirmation=1)