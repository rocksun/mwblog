# SysLinuxOS，专为系统管理员设计的 Linux 发行版

![SysLinuxOS 的特色图片，专为系统管理员设计的 Linux 发行版](https://cdn.thenewstack.io/media/2024/11/32a147b4-screenshot-from-syslinuxos-12-video-1024x587.jpg)

全球各地的系统集成商正在发现 [SysLinuxOS](https://syslinuxos.com/)，这是一个基于 Debian 的发行版，预装了各种网络和系统工具。它旨在满足系统集成商的独特需求，并致力于成为国际现象。其官方博客为读者提供了九种语言选择——包括阿拉伯语、中文、法语、德语、意大利语、葡萄牙语、俄语和西班牙语。它甚至附带了 GNOME 或 MATE 桌面供选择。

但最终，SysLinuxOs 也作为 [Linux 的强大功能](https://thenewstack.io/learning-linux-start-here/) 的又一个例证，以及开源操作系统如何拥有一个超级能力：它们可以无限定制。以及敬业的用户如何实现这种定制……

## SysLinuxOS 背后的创造者

“我觉得有必要有一个包含所有工具且开箱即用的发行版，” [一篇早期博客文章](https://syslinuxos.com/perche-syslinuxos/) 解释道，该发行版来自位于米兰的创建者 [Franco Conidi](https://www.linkedin.com/in/franco-conidi-edm/)。一份在线传记将 Conidi（又名“Edmond”）认定为高级系统集成商、系统管理员和 IT 顾问。

“我首先要说的是，我对计算机充满热情，”Conidi 在其 [个人网站](https://francoconidi.it/info/) 上的一篇简短传记中说，“尤其是 Gnu-Linux，以及与开源世界相关的一切……总的来说，与技术相关的一切都吸引我，我或多或少尝试过所有最重要的发行版……”

Conidi 多年来一直在使用 [Debian](https://thenewstack.io/debian-retools-apt-for-superior-dependency-management/)，并声称对该操作系统有如此深厚的感情，“我拥抱它，我看着它，我不断地研究它。我爱它，也爱 [这个](https://www.debian.org/social_contract)”，指的是 Debian 著名的社会契约，承诺他们的操作系统将始终保持免费和开放。

SysLinuxOS [主页](https://syslinuxos.com/) 通过一些额外的定制向用户承诺“一个强大且功能丰富的操作系统，专为系统集成领域的专业人士设计。它具有增强的桌面、改进的安全措施、高级网络功能和全面的监控工具。”

它的版本号跟踪 Debian 的版本号。2023 年 6 月，[SysLinuxOS 版本 12](https://syslinuxos.com/syslinuxos-12-for-system-integrators/) 与 Debian 12 的发布同时进行——但增加了系统管理员的功能（包括其两个 [监控正在运行的进程、网络状态和 PC 性能的小部件）。它还附带了一个专门用于其网络分析工具的菜单，以及几个默认集成的防火墙（包括 Gufw、Firewalld、Opensnitch 和 Shorewall），以及 Firejail、Firetools、Firewalk 和 Suricata 等安全工具。 conky](https://conky.sourceforge.net/documentation.html)

其广泛的监控工具列表包括 Cacti、Fail2ban、Icinga、Monit、Munin、Nagios4、Zabbix-Agent2 和 Zabbix-Fronted，“以及其他工具，确保有效的系统监控和管理。”

自推出以来，Conidi 尝试添加了各种工具，包括 [两个命令行速度测试工具](https://syslinuxos.com/fast-cli-speedtest-cli-su-syslinuxos/)——Fast-cli 和 Speedtest-cli——以及整个 [XAMPP Web 服务器堆栈](https://syslinuxos.com/xampp-php-8-syslinuxos-11/)，包括 Apache HTTP 服务器、MySQL（或 MariaDB）、PHP 和 Perl，以及 DHCP 网络服务器 [已安装](https://syslinuxos.com/server-dhcp-su-syslinuxos-11/)。（只需将你自己的网络名称添加到 */etc/default/isc-dhcp-server*……）

![SysLinuxOS 当前主页的屏幕截图](https://cdn.thenewstack.io/media/2024/11/a79cecd9-screenshot-from-syslinuxos-home-page-features.png)

SysLinuxOS 当前主页的屏幕截图

## 工具箱的演变

看到 SysLinuxOS 如何演变是件很迷人的事。其 YouTube 频道上的早期视频捕捉了 *conky* 小应用程序的侧边栏，显示了 CPU 和 RAM 利用率，以及网络数据传输和正在运行的进程列表。

虽然它们仍然存在于版本 12 中，但现在桌面上还显示了 CPU、内存和互联网监视器，以及时钟。 [Linux Magazine 中的一篇评论](https://www.linux-magazine.com/Issues/2024/287/SysLinuxOS) 抱怨这“往往会让桌面有点杂乱”，尽管“许多不断变化的状态显示构成了一个真正引人注目的用户界面”。
### MARKDOWN TEXT CORRECTED

但仍有大量工具——如 SysLinuxOS 视频中正在运行的应用程序所证明的那样。有 TeamViewer、AnyDesk、GParted、Oracle VM VirtualBox 和 Remmina（远程桌面客户端）。还有一个“网络”子菜单，其中包含 Angry IP Scanner、CuteCom、EtherApe、Ettercap、GNS3、Gtkterm、LinSSID、Minicom、NpamSI4（nmap 接口）、PackETH（以太网数据包生成器）、Packet Sender、Packet Tracer、Sparrow Wifi、Wifi QR 和 [Wireshark](https://thenewstack.io/wireshark-celebrates-25th-anniversary-with-a-new-foundation/)。（当然，还有 PuTTY 终端模拟器……）

或者，正如其主页所解释的那样，SysLinuxOS “开箱即用，所有网络工具默认已安装”。它承诺通过包含“除内核中包含的驱动程序之外的大量 wifi/视频/声音和蓝牙驱动程序”来“改进”硬件支持。它吹嘘（除了最新的稳定 Linux 内核之外）SysLinuxOS 包含所有主要的 VPN、串行控制台工具、几个远程控制客户端和各种浏览器。

还有很多附加的花里胡哨的东西。在附件下，甚至还有一个 [Raspberry Pi](https://thenewstack.io/the-new-2gb-raspberry-pi-5-another-option-for-linux-sysadmins/) Imager 和 balenaEtcher，用于将映像刷新到 USB 驱动器或 SD 卡上。*Linux Magazine* 指出，它还包括一个完全配置的 Windows 运行时环境 Wine 版本、两个用于防火墙配置的不同 GUI 前端，以及“非常广泛的”软件选择，其中包括 Skype、Zoom、WhatsApp 和 Telegram。（此外还有用于电子邮件的 Thunderbird 和用于协作的思科 WebEx 工具。）

“SysLinuxOS 结束了为管理任务寻找合适工具的时代，”他们总结道，赞扬该发行版提供了“非常广泛的软件选择，特别是用于使用互联网”——包括 Firefox、Chrome、Edge 和 Tor 浏览器。“Tor 实际上是通过脚本从互联网下载的，并在您第一次调用它时集成到系统中。”

“SysLinuxOS 的开发人员没有针对特定的应用程序场景，而是捆绑了各种工具，以应对您能想象到的几乎任何管理任务……”

当然，您可以安装自己的其他工具——但 SysLinuxOS 为您提供了一个预先安装的良好选择。

*Linux Magazine* 指出 SysLinuxOS 的许多软件包源——默认情况下已启用——包括 Skype、Google、Docker 和 Microsoft。“这使您可以访问超过 65,000 个软件包……”它甚至同时附带 Docker 和 Docker Compose 工具，“这极大地简化了容器中应用程序的开发、分发和管理”。

## 热衷于 Debian

一年前多一点，其创建者在 [其博客上的评论](https://syslinuxos.com/things-to-do-after-installing-syslinuxos-12/#comment-82) 中分享了一些个人想法。SysLinuxOS 不仅直接源于他对 Debian 的热情——自推出以来，他一直在“自用”自己的操作系统。“我将 SysLinuxOS 用作我的日常桌面，而且我从未遇到过任何问题。

“当然，有改进的空间，也会有一些错误，但一旦我意识到问题，我将尽我所能解决它们……在这项工作中，只有我一个人，在我身后，永远只有我一个人。”

并且对使用版本 12.3 的用户做出了一个特别的承诺—— [1 月份发布](https://syslinuxos.com/syslinuxos-12-3-released/)。

“我将尽我所能使这个发行版对那些像我一样从事系统集成商或网络管理员工作的人有用且更完整。”

# WebReduce

- 在测试了五项端到端加密云存储服务后，承诺在发现 [未经授权的服务器访问也允许绕过数据加密](https://brokencloudstorage.info/) 后进行修补。
- Redmonk 分析师认为术语开源 [不应该扩展到人工智能领域](https://redmonk.com/sogrady/2024/10/22/from-open-source-to-ai/)。
- GitHub 发布 2024 年开发者调查，“ [Octoverse 现状](https://github.blog/news-insights/octoverse/octoverse-2024/)”。
- 互联网档案发布 [.](https://blog.archive.org/2024/10/30/vanishing-culture-a-report-on-our-fragile-cultural-record/) *消失的文化：我们脆弱的文化记录报告*
- 破解 [帮助结束南非种族隔离的 30 年历史的 PKZIP 文件](https://blog.jgc.org/2024/09/cracking-old-zip-file-to-help-open.html)。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、采访、演示等。