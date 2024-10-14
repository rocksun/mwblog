
<!--
title: Ubuntu Linux：安装 Suricata 入侵检测系统
cover: https://cdn.thenewstack.io/media/2024/09/ffe09c33-suricata.jpg
-->

Suricata 是一款高性能的开源网络分析和威胁检测软件，其功能包括警报、自动协议阻止、Lua 脚本和行业标准输出。

> 译自 [Ubuntu Linux: Install the Suricata Intrusion Detection System](https://thenewstack.io/ubuntu-linux-install-the-suricata-intrusion-detection-system/)，作者 Jack Wallen。


# Ubuntu Linux：安装 Suricata 入侵检测系统

![Ubuntu Linux：安装 Suricata 入侵检测系统的特色图片](https://cdn.thenewstack.io/media/2024/09/ffe09c33-suricata-1024x746.jpg)

入侵检测系统 (IDS) 对于监控网络流量和检查恶意活动至关重要。如果您的服务器是 [Linux 类型](https://thenewstack.io/linux-choose-an-installation-platform/)，您有很多选择，其中之一是 Suricata。

Suricata 是一款高性能的开源网络分析和威胁检测软件，被众多私人和公共组织使用，其功能包括警报、自动协议检测、Lua 脚本和行业标准输出。它提供六种操作模式：

- 入侵检测系统（默认）
- 入侵防御系统
- 网络安全监控系统
- 全包捕获
- 条件 PCAP 捕获
- 防火墙

大多数用户会选择默认模式，它是 IDS 和网络安全监控的组合，可确保警报包含有关协议、流、文件事务/提取、异常和流日志的信息。您可以从 [官方网站](https://suricata.io) 了解更多关于 Suricata 的信息。

Suricata 可以免费安装和使用。

我想要做的是引导您完成在 [Ubuntu Server 22.04](https://thenewstack.io/how-to-install-ubuntu-pro-on-your-servers/) 上安装此 IDS 的过程。

## 您需要什么

要启动并运行 Suricata，您需要一个正在运行的 Ubuntu Server 22.04 实例和一个具有 [sudo 权限](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/) 的用户。就是这样……让我们开始工作吧。

## 安装必要的依赖项

首先要做的是安装必要的依赖项。登录到您的 Ubuntu 服务器并使用以下命令安装这些软件包：

```bash
sudo apt install autoconf automake build-essential cargo cbindgen libjansson-dev libpcap-dev libcap-ng-dev libmagic-dev liblz4-dev libpcre2-dev libtool libyaml-dev make pkg-config rustc zlib1g-dev -y
```

当上述命令完成后，您就可以继续了。

## 下载并解压源代码

接下来，我们可以下载 Suricata 源代码并解压。使用以下命令下载压缩的存档文件：

```bash
wget https://www.openinfosecfoundation.org/download/suricata-7.0.6.tar.gz
```

您可能需要访问 [Suricata 下载页面](https://www.openinfosecfoundation.org/download/) 以确保您获取的是最新版本。
使用以下命令解压文件：

```bash
tar xvzf suricata-7.0.6.tar.gz
```

上述命令将创建一个名为 suricata-7.0.6 的新文件夹。

## 构建并安装软件包

我们现在可以构建软件包了。使用以下命令切换到新创建的目录：

```bash
cd suricata-7.0.6
```

在该目录中，使用以下命令运行配置脚本：

```bash
./configure --enable-nfqueue --prefix=/usr --sysconfdir=/etc --localstatedir=/var
```

上述命令大约需要一分钟才能完成。
最后，使用以下命令安装软件包：

```bash
sudo make && sudo make install-full
```

安装过程将花费 5-10 分钟，具体取决于您的硬件速度。

另一种安装 Surcicata 的方法是通过 PPA 存储库。使用以下命令添加存储库：

```bash
sudo add-apt-repository ppa:oisf/suricata-stable
```

使用以下命令更新 apt：

```bash
sudo apt-get update
```

使用以下命令安装 Suricata：

```bash
sudo apt-get install suricata -y
```

请注意：我更喜欢使用 PPA 方法安装，因为它添加了一个 [systemd 启动](https://thenewstack.io/systemds-lennart-poettering-wants-to-bring-linux-home-directories-into-the-21st-century/) 文件，以便于服务控制。

## 启动服务

安装完成后，就可以使用以下命令启动服务了：

```bash
sudo systemctl enable --now suricata
```

## 配置 Suricata

现在是配置 Suricata 的时候了。使用以下命令打开配置文件：

```bash
sudo nano /etc/suricata/suricata.yaml
```

我假设您将在局域网上使用 Suricata。为此，请查找以 `HOME_NET` 开头的行。在该行中，您需要配置您的子网（例如 `192.168.1.0/16`）。

接下来，查找 `af-packet` 行。在其下方，您将看到 `-interface: eth0`。您需要将 `eth0` 更改为您的网络接口的名称（可以使用 `ip a` 命令找到）。

完成此操作后，您需要添加以下内容以启用实时规则重新加载。以下内容可以添加到配置文件的底部：

```yaml
detect-engine:
  - rule-reload: true
```

保存并关闭文件。

## 更新 Suricata 规则

完成配置后，您需要使用以下命令更新 Suricata 规则集：

```bash
sudo suricata-update
```

## 运行 Suricata

现在是时候测试运行 Suricata 了。规则更新后，我们将使用以下命令测试规则：

```bash
sudo suricata -T -c /etc/suricata/suricata.yaml -v
```
您不应该收到任何错误消息，测试将以以下内容结束：

*注意：suricata：提供的配置已成功加载。正在退出。*

使用以下命令重启服务：

```
sudo systemctl restart suricata
```

## 测试 Suricata

让我们进行一个快速测试。以下命令用于触发错误警报。执行以下操作：

从第二个终端（或选项卡）登录服务器。在第一个窗口中，发出以下命令：

```
tail -f /var/log/suricata/fast.log
```

在第二个终端中，发出以下命令：

```
curl http://testmynids.org/uid/index.html
```

在第一个窗口中，您应该看到如下输出：

```
09/04/2024-17:44:43.767928 [**] [1:2100498:7] GPL ATTACK_RESPONSE id check returned root [**] [Classification: Potentially Bad Traffic] [Priority: 2] {TCP} 2600:9000:24d7:6c00:0018:30b3:e400:93a1:80 -> 2600:1700:6d90:f6b0:0000:0000:0000:001c:35524
```

Suricata 捕获了错误警报。

现在您已经启动并运行 Suricata（并成功测试），请查看 Suricata 规则的官方文档，这些规则可以帮助您充分利用这个免费的开源入侵检测系统。Suricata 是一个使用起来相当复杂的系统，因此我建议您通读官方文档以更好地了解其工作原理。

如果您更喜欢使用 GUI 管理 Suricata，我建议您查看 [IDS Tower](https://idstower.com)。

[YOUTUBE.COM/THENEWSTACK 技术发展日新月异，请勿错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、采访、演示等内容。](https://youtube.com/thenewstack?sub_confirmation=1)