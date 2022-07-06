# 通过 Maple 设置 Windows 全局代理

今天想尝试安装 windows 版的 podman，执行 podman 的某个命令时撞墙了，所以突然决定，把我荒废很久的全局代理搞起来。

我有一个本地代理，以前主要作为浏览器的 socket 代理使用。有一段时间，曾经用过 proxifier + 本地代理，实现其他程序通过代理访问网络。不过 proxifier 并不是免费的工具，已经很久没用了。所以今天我决定试试 [Maple](https://github.com/YtFlow/Maple)。

我的环境是 windows 10。

## 下载安装 Maple

可以到 Maple 的 [Releases](https://github.com/YtFlow/Maple/releases) 页下载压缩包，解压后会看到多个文件。

在 *.cer 上右键，选择“安装证书”，然后完成证书安装。然后在 *.appxbundle 上右键，选择“安装”即可完成安装。

然后左下角快速启动就可以看到 maple。

## 配置 maple

打开 maple，默认配置太多，看不懂，先输入一个简单的:

```ini
[General]
loglevel = error
tun-fd = 233
dns-server = 223.5.5.5, 114.114.114.114

[Proxy]
Direct = direct
Reject = reject

# Shadowsocks
Sock_local_1080 = socks, 127.0.0.1, 1080

[Rule]
IP-CIDR, 224.0.0.0/8, Direct
IP-CIDR, 239.0.0.0/8, Direct
IP-CIDR, xxx.xxx.xxx.xxx, Direct
DOMAIN, my.proxy.server.domain, Direct
FINAL, Sock_local_1080

```

Sock_local_1080 对应的是我的本地代理地址和端口。而 xxx.xxx.xxx.xxx 是我的代理服务器的地址，不应该走代理，所以加上了 Direct 访问。点击 save， 完成配置的保存。

然后 maple 是作为 VPN 运行的，所以还要在 Maple 上选择 Setting，可以看到会列出上网的网卡，我会选择我的无线网卡，然后点击 Generate Profile，即会在 windows 增加一个 Maple VPN 的配置。这一步也可以根据 Maple 官方文档手工执行。

## 让 maple 支持本地代理

Maple 作为 Windows 市场的应用，会限制对于 127.0.0.1 的代理的访问，这里需要下载[EnableLoopback Utility](https://telerik-fiddler.s3.amazonaws.com/fiddler/addons/enableloopbackutility.exe)。解压缩运行，选择 “Maple”，然后选择“Save Changes”，这时 Maple 就可以连接本地代理了。

## 验证功能

打开 Maple，点击右上角的 Off ，如果一起正常，就会变成 On。最初我的 Maple 一直闪退，应该是 Config 错误造成的。

如果变成 On，这时运行`curl www.google.com`，应该可以得到正确的结果。

如果 curl 命令很长时间才反馈，这应该是 Maple 还是没有起到作用；如果快速反馈 `curl: (56) Recv failure: Connection was reset`，这是因为没有用 EnableLoopback Utility 处理本地代理访问问题。


## 参考文档

* [为Windows apps应用设置本地代理](https://kiritox.me/setup-proxy-for-windows-apps/)