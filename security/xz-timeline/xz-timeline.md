
<!--
title: xz开源攻击时间线
cover: ./cover.png
-->

在两年多的时间里，一位化名“Jia Tan”的攻击者一直作为 xz 压缩库的勤奋、高效的贡献者，最终获得了提交访问权限和维护权限。利用该权限，他们在 liblzma 中安装了一个非常微妙、精心隐藏的后门，而 liblzma 是 xz 的一部分，恰好也是 Debian、Ubuntu、Fedora 和其他基于 systemd 的 Linux 系统上的 OpenSSH sshd 的依赖项。该后门会监视攻击者在 SSH 会话开始时发送的隐藏命令，从而使攻击者能够在目标系统上运行任意命令，而无需登录：未经身份验证的、有针对性的远程代码执行。

> 译自 [Timeline of the xz open source attack Posted on Monday, April 1, 2024.](None)，作者 Russ Cox。

该攻击[于 2024 年 3 月 29 日公开披露](https://www.openwall.com/lists/oss-security/2024/03/29/4)，似乎是针对广泛使用的开源软件的首次已知严重供应链攻击。无论好坏，它标志着开源供应链安全的一个分水岭时刻。

这篇文章是我构建的攻击社会工程方面的详细时间线，该攻击似乎可以追溯到 2021 年底。关键事件以粗体时间表示。

欢迎在 [Bluesky](https://bsky.app/profile/swtch.com/post/3kp4my7wdom2q)、[Mastodon](https://hachyderm.io/@rsc/112199506755478946) 或[邮件](mailto:rsc@swtch.com)上联系。

## 序幕

**2005-2008 年**：[Lasse Collin 在他人的帮助下](https://github.com/kobolabs/liblzma/blob/87b7682ce4b1c849504e2b3641cebaad62aaef87/doc/history.txt)，使用 LZMA 压缩算法设计了 .xz 文件格式，该算法将文件压缩到 gzip 的约 70% [1]。随着时间的推移，此格式被广泛用于压缩 tar 文件、Linux 内核映像和许多其他用途。

## Jia Tan 携配角登场

**2021-10-29**：Jia Tan 向 xz-devel 邮件列表发送了 [第一个无害补丁](https://www.mail-archive.com/xz-devel@tukaani.org/msg00512.html)，添加了 “.editorconfig” 文件。

**2021-11-29**：Jia Tan 向 xz-devel 邮件列表发送了 [第二个无害补丁](https://www.mail-archive.com/xz-devel@tukaani.org/msg00519.html)，修复了一个明显的可重现构建问题。更多看似（即使在回顾中）不错的补丁随之而来。

**2022-04-19**：Jia Tan 向 xz-devel 邮件列表发送了 [另一个无害补丁](https://www.mail-archive.com/xz-devel@tukaani.org/msg00553.html)。

**2022-04-22**：“Jigar Kumar”发送了 [几封电子邮件中的第一封](https://www.mail-archive.com/xz-devel@tukaani.org/msg00557.html)，抱怨 Jia Tan 的补丁没有落地。（“补丁在这个邮件列表上花费了数年。没有理由认为很快就会有什么结果。”）此时，Lasse Collin 已经接受了Jia Tan的四个补丁，在提交消息中标有“感谢 Jia Tan”。

**2022-05-19**：“Dennis Ens”向 xz-devel 发送[邮件](https://www.mail-archive.com/xz-devel@tukaani.org/msg00562.html)，询问是否维护 XZ for Java。

**2022-05-19**：Lasse Collin [回复](https://www.mail-archive.com/xz-devel@tukaani.org/msg00563.html)，为速度慢道歉，并补充说“Jia Tan 在 XZ Utils 中帮助了我，他将来可能在 XZ Utils 中发挥更大的作用。很明显，我的资源太有限了（因此有许多电子邮件等待回复），所以从长远来看必须做出一些改变。”

**2022-05-27**：Jigar Kumar 向补丁线程发送[催促电子邮件](https://www.mail-archive.com/xz-devel@tukaani.org/msg00565.html)。“超过 1 个月，但距离合并还很遥远。这并不奇怪。”

**2022-06-07**：Jigar Kumar 向 Java 线程发送 [催促电子邮件](https://www.mail-archive.com/xz-devel@tukaani.org/msg00566.html)。“在有新维护者之前，不会有进展。XZ for C 的提交日志也很稀疏。Dennis，你最好等到新维护者出现或自己分叉。如今，在此处提交补丁毫无意义。当前维护者失去了兴趣或不再关心维护。对于这样的仓库来说，这令人遗憾。”

**2022-06-08**：Lasse Collin [回击](https://www.mail-archive.com/xz-devel@tukaani.org/msg00567.html)。“我并没有失去兴趣，但我关心事情的能力一直相当有限，这主要是由于长期的精神健康问题，但也由于其他一些事情。最近我与 Jia Tan 在 XZ Utils 上进行了一些非公开的工作，也许他将来会发挥更大的作用，我们拭目以待。还要记住，这是一个无偿的业余项目。”

**2022-06-10**：Lasse Collin 合并了[第一个提交，其中 Jia Tan 作为 git 元数据中的作者](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=aa75c5563a760aea3aa23d997d519e702e82726b)（“测试：为硬件功能创建测试”）。

**2022-06-14**: Jigar Kumar 发送[催促邮件](https://www.mail-archive.com/xz-devel@tukaani.org/msg00568.html)。“以你目前的进度，我非常怀疑今年能看到 5.4.0 版本。自 4 月以来，唯一进展就是对测试代码进行了一些小改动。你忽略了在这个邮件列表中逐渐腐烂的许多补丁。你现在扼杀了你的仓库。为什么等到 5.4.0 才更换维护者？为什么拖延你的仓库需要的东西？”

**2022-06-21**: Dennis Ens 发送[催促邮件](https://www.mail-archive.com/xz-devel@tukaani.org/msg00569.html)。“我很抱歉你的心理健康问题，但意识到自己的局限性很重要。我知道这对所有贡献者来说都是一个业余项目，但社区需要更多。为什么不将 XZ for C 的维护权转让出去，以便你可以更多地关注 XZ for Java？或者将 XZ for Java 转让给其他人，以便专注于 XZ for C？试图同时维护两者意味着两者都没有得到很好的维护。”

**2022-06-21**: Lasse Collin [回复](https://www.mail-archive.com/xz-devel@tukaani.org/msg00571.html)：“正如我在之前的电子邮件中暗示的那样， Jia Tan 未来可能在该项目中扮演更大的角色。他一直在场外提供很多帮助，实际上已经是联合维护者了。 :-) 我知道 git 存储库中还没有发生太多事情，但事情都是一步一步发生的。无论如何，至少对于 XZ Utils，维护权的变更已经开始进行。”

**2022-06-22**: Jigar Kumar 向 C 补丁线程发送[催促邮件](https://www.mail-archive.com/xz-devel@tukaani.org/msg00570.html)。“这件事有什么进展吗？Jia，我看到你最近提交了一些内容。为什么你不能自己提交？”

##  Jia Tan 成为维护者

在这一点上，Lasse 似乎已经开始与 Jia Tan 更紧密地合作。Evan Boehs [观察到](https://boehs.org/node/everything-i-know-about-the-xz-backdoor) Jigar Kumar 和 Dennis Ens 都有 nameNNN@mailhost 电子邮件地址，这些地址从未出现在互联网上的其他地方，也没有出现在 xz-devel 中。他们很可能是为了推动 Lasse 给 Jia 更多控制权而创建的假地址。这奏效了。在接下来的几个月里， Jia 开始在 xz-devel 上权威地回复有关即将发布的 5.4.0 版本的主题。

**2022-09-27**:  Jia Tan 为 5.4.0 提供[发布摘要](https://www.mail-archive.com/xz-devel@tukaani.org/msg00593.html)。（“包含多线程解码器的 5.4.0 版本计划在 12 月发布。我正在跟踪与 5..4.0 [原文如此] 相关的未解决问题列表，其中包括... ”）

**2022-11-30**: Lasse Collin [修改 Bug 报告电子邮件](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=764955e2d4f2a5e8d6d6fec63af694f799e050e7) ，从他的个人地址更改为一个同时发给他和 Jia Tan 的别名，在 README 中注明“可以联系项目维护者Lasse Collin 和 Jia Tan ，邮箱：[xz@tukaani.org](mailto:xz@tukaani.org)”。

**2022-12-30**:  Jia Tan 合并[第一个直接提交到 xz 仓库](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=8ace358d65059152d9a1f43f4770170d29d35754)（“CMake：更新 .gitignore 以获取源构建中的 CMake 工件”）。在这一点上，我们知道他们有提交权限。

**2023-01-11**: Lasse Collin [标记并构建了他的最终版本](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=18b845e69752c975dfeda418ec00eda22605c2ee)，v5.4.1。

**2023-03-18**:  Jia Tan [标记并构建了他们的第一个版本](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=6ca8046ecbc7a1c81ee08f544bfd1414819fb2e8)，v5.4.2。

**2023-03-20**:  Jia Tan [更新 Google oss-fuzz 配置](https://github.com/google/oss-fuzz/commit/6403e93344476972e908ce17e8244f5c2b957dfd) 以向他们发送 Bug。

**2023-06-22**: Hans Jansen 发送了两个补丁，由 Lasse Collin 合并，它们使用“ [GNU 间接函数](https://maskray.me/blog/2021-01-18-gnu-indirect-function)”功能在启动时选择一个快速的 CRC 函数。此更改很重要，因为它提供了一个挂钩，通过该挂钩后门代码可以在全局函数表重新映射为只读之前修改它们。虽然此更改本身可能是一种无害的性能优化，但 Hans Jansen 在 2024 年回来推广带后门的 xz，并且在互联网上不存在。

**2023-07-07**:  Jia Tan [在 oss-fuzz 构建期间禁用 ifunc 支持](https://github.com/google/oss-fuzz/commit/d2e42b2e489eac6fe6268e381b7db151f4c892c5)，声称 ifunc 与地址清理器不兼容。这本身可能无害，尽管它也是以后使用 ifunc 的更多基础工作。

**2024-01-19**:  Jia Tan [将网站移至 GitHub 页面](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=c26812c5b2c8a2a47f43214afe6b0b840c73e4f5)，让他们控制 XZ Utils 网页。Lasse Collin 大概为指向 GitHub 页面的 xz.tukaani.org 子域创建了 DNS 记录。在攻击被发现后，Lasse Collin 删除了此 DNS 记录，以移回他控制的 [tukaani.org](tukaani.org)。

## 攻击开始

**2024-02-23**：Jia Tan 将后门二进制代码巧妙隐藏在一些二进制测试输入文件中实现了合并。相关的自述文件声称：“此目录包含用于测试解码器实现中对 .xz、.lzma (LZMA_Alone) 和 .lz (lzip) 文件处理的一系列文件。很多文件都是通过十六进制编辑器手工创建的，因此没有比文件本身更好的“源代码”。

**2024-02-24**：Jia Tan [标记并构建 v5.6.0](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=2d7d862e3ffa8cec4fd3fdffcd84e984a17aa429) 并发布 xz-5.6.0.tar.gz 发行版，其中包含一个额外的恶意 build-to-host.m4，在构建 deb/rpm 包时会添加后门。源代码存储库中不存在该 m4 文件，但同时也会在打包期间添加许多其他合法文件，因此它本身并不可疑。但是已从通常的副本修改脚本以添加后门。详情请参阅我的 [xz 脚本演练文章](https://research.swtch.com/xz-script)。

**2024-02-24**： Gentoo [在 5.6.0 中开始出现崩溃](https://bugs.gentoo.org/925415)。这看起来是一个真实的 ifunc 错误，而不是隐藏的后门中的错误，因为这是包含 Hans Jansen ifunc 变更的第一个 xz。

**2024-02-26**：Debian [将 xz-utils 5.6.0-0.1 添加](https://tracker.debian.org/news/1506761/accepted-xz-utils-560-01-source-into-unstable/) 到不稳定版。

**2024-02-28**：Debian [将 xz-utils 5.6.0-0.2 添加](https://tracker.debian.org/news/1507917/accepted-xz-utils-560-02-source-into-unstable/) 到不稳定版。

**2024-02-29**：在 GitHub 上，@teknoraver 发送了一个停止将 liblzma 链接到 libsystemd 的[拉取请求](https://github.com/systemd/systemd/pull/31550)。似乎这将会制止攻击。[Kevin Beaumont 推断](https://doublepulsar.com/inside-the-failed-attempt-to-backdoor-ssh-globally-that-got-caught-by-chance-bbfe628fafdd)，知道这件事即将发生可能让攻击者的计划加快进度。目前尚不清楚是否早前的讨论透露过任何信息。

**2024-02-28**：Jia Tan 通过在用于检查 landlock 支持的 C 程序中添加一个微妙的拼写错误来[中断了 configure 脚本中的 landlock 检测](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=a100f9111c8cc7f5b5f0e4a5e8af3de7161c7975)。为了检查 [landlock 支持](https://docs.kernel.org/userspace-api/landlock.html)，该 configure 脚本尝试编译并运行该 C 程序，但由于该 C 程序中含有语法错误，它将永远无法被编译和运行，而且该脚本会一直判断没有 landlock 支持。Lasse Collin 是提交者，他可能错过了该精妙的类型，或可能该作者是伪造的。可能是前者，因为 Jia Tan 在许多其他改动中都没有费心伪造提交者。这篇补丁似乎在为除 sshd 更改之外的其他事情做准备，因为 landlock 支持属于 xz 命令而不是 liblzma 的一部分。具体是什么还不清楚。

**2024-03-04**：在 liblzma 的 _get_cpuid（后门入口）中，RedHat 发行版已开始[发现 Valgrind 错误](https://bugzilla.redhat.com/show_bug.cgi?id=2267598)。

**2024-03-05**：[libsystemd PR 已合并](https://github.com/systemd/systemd/commit/3fc72d54132151c131301fc7954e0b44cdd3c860)以删除 liblzma。

**2024-03-05**：Debian [将 xz-utils 5.6.0-0.2 添加](https://tracker.debian.org/news/1509743/xz-utils-560-02-migrated-to-testing/)到 testing。

**2024-03-05**：Jia Tan 提交 [两个 ifunc](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=ed957d39426695e948b06de0ed952a2fbbe84bd1) [Bug 修复](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=4e1c97052b5f14f4d6dda99d12cbbd01e66e3712)。这些看起来是对实际 ifunc bug 的真正修复。一次提交链接到了 Gentoo Bug，并错误地输入了一个[上游 GCC Bug](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=114115)。

**2024-03-08**：Jia Tan [提交了所谓的 Valgrind 修复](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=82ecc538193b380a21622aea02b0ba078e7ade92)。这是一个错误的方向，但却是有效的。

**2024-03-09**：Jia Tan [提交更新的后门文件](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=74b138d2a6529f2c07729d7c77b1725a8e8b16f1)。这是真正的 Valgrind 修复，更改了包含攻击代码的两个测试文件。“原始文件是用随机本地代码生成的。为了在将来更好地重现这些文件，使用一个常量种子重新创建了这些文件。”

**2024-03-09**：Jia Tan [标记并构建了 v5.6.1](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=74b138d2a6529f2c07729d7c77b1725a8e8b16f1)，以及发布了包含了新后门的 xz 5.6.1 发行版。到目前为止，我还没有看到对新旧后门有何不同之处有任何分析。

**2024-03-25**：Hans Jansen 回来了（！），[提交 Debian bug](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1067708) 以将 xz-utils 更新至 5.6.1。与 2022 年的施压活动一样，更多在互联网上不存在的 name###@mailhost 地址出现并为其辩护。

**2024-03-28**： Jia Tan  [提交 Ubuntu bug](https://bugs.launchpad.net/ubuntu/+source/xz-utils/+bug/2059417) 以从 Debian 将 xz-utils 更新至 5.6.1。

## 攻击已检测到

**2024-03-28**：Andres Freund 发现 bug，私下通知 Debian 和 distros@openwall。RedHat 分配 CVE-2024-3094。

**2024-03-28**：Debian [回滚 5.6.1](https://tracker.debian.org/news/1515519/accepted-xz-utils-561really545-1-source-into-unstable/)，引入 5.6.1+really5.4.5-1。

**2024-03-29**：Andres Freund [发布后门警告](https://www.openwall.com/lists/oss-security/2024/03/29/4) 至公开的 oss-security@openwall 列表，称他在“过去几周”发现了它。

**2024-03-29**：RedHat [宣布后门 xz 已在 Fedora Rawhide 和 Fedora Linux 40 beta 中发布](https://www.redhat.com/en/blog/urgent-security-alert-fedora-41-and-rawhide-users)。

**2024-03-30**：Debian [关闭构建](https://fulda.social/@Ganneff/112184975950858403) 以使用 Debian stable 重新构建其构建机器（以防恶意软件 xz 逃离其沙箱？）。

## 延伸阅读

- Evan Boehs, [Everything I know about the XZ backdoor](https://boehs.org/node/everything-i-know-about-the-xz-backdoor)(2024-03-29).
- Filippo Valsorda, [Bluesky](https://bsky.app/profile/filippo.abyssdomain.expert/post/3kowjkx2njy2b)re backdoor operation (2024-03-30).
- Michał Zalewski, [Techies vs spies: the xz backdoor debate](https://lcamtuf.substack.com/p/technologist-vs-spy-the-xz-backdoor)(2024-03-30).
- Michał Zalewski, [OSS backdoors: the folly of the easy fix](https://lcamtuf.substack.com/p/oss-backdoors-the-allure-of-the-easy)(2024-03-31).
- Connor Tumbleson, [Watching xz unfold from afar](https://connortumbleson.com/2024/03/31/watching-xz-unfold-from-afar/)(2024-03-31).
- nugxperience, [Twitter](https://twitter.com/nugxperience/status/1773906926503591970) re awk and rc4 (2024-03-29)
- birchb0y, [Twitter](https://twitter.com/birchb0y/status/1773871381890924872) re time of day of commit vs level of evil (2024-03-29)
- Dan Feidt, ['xz utils' Software Backdoor Uncovered in Years-Long Hacking Plot](https://unicornriot.ninja/2024/xz-utils-software-backdoor-uncovered-in-years-long-hacking-plot/)(2024-03-30)
- smx-smz, [[WIP] XZ Backdoor Analysis and symbol mapping](https://gist.github.com/smx-smx/a6112d54777845d389bd7126d6e9f504)
- Dan Goodin,[What we know about the xz Utils backdoor that almost infected the world](https://arstechnica.com/security/2024/04/what-we-know-about-the-xz-utils-backdoor-that-almost-infected-the-world/)(2024-04-01)
- Akamai Security Intelligence Group, [XZ Utils Backdoor — Everything You Need to Know, and What You Can Do](https://www.akamai.com/blog/security-research/critical-linux-backdoor-xz-utils-discovered-what-to-know)(2024-04-01)
- Kevin Beaumont, [Inside the failed attempt to backdoor SSH globally — that got caught by chance](https://doublepulsar.com/inside-the-failed-attempt-to-backdoor-ssh-globally-that-got-caught-by-chance-bbfe628fafdd)(2024-03-31)
- amlweems, [xzbot: notes, honeypot, and exploit demo for the xz backdoor](https://github.com/amlweems/xzbot)(2024-04-01)
- Rhea's Substack, [XZ Backdoor: Times, damned times, and scams](https://rheaeve.substack.com/p/xz-backdoor-times-damned-times-and)(2024-03-30)