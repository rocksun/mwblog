
<!--
title: Linux xz后门的破坏可能比想象的更大
cover: https://cdn.thenewstack.io/media/2024/03/11d74142-ren-wang-pnynuo0dt6s-unsplash-augmented.jpg
-->

一位神秘的贡献者植入了后门，在过去两年中帮助维护了广泛使用的 xz 压缩库。那么，还有什么隐藏在里面？

> 译自 [Linux xz Backdoor Damage Could Be Greater Than Feared](https://thenewstack.io/linux-xz-backdoor-damage-could-be-greater-than-feared/)，作者 Joab Jackson。

当你的家被闯入时，你可能最初无法理解被拿走了什么，或者造成了什么损害。这就是 [Linux 社区](https://thenewstack.io/Linux/) 目前对[最近发现的 xz 后门](https://thenewstack.io/malicious-code-in-linux-xz-libraries-endangers-ssh/)安全漏洞的担忧。

“这种上游供应链安全攻击是多年来人们一直称之为歇斯底里的噩梦场景，”Kubernetes 安全主席 [Ian Coldwater](https://www.linkedin.com/in/iancoldwater/) 在 [X 上写道](https://twitter.com/IanColdwater/status/1773797427603980393)。“这是真的。”

一名 Microsoft 工程师首先检测到后门，他将其追溯到 xz 压缩库的最近更新。库更新是最近的一次，但它已经出现在某些 Linux 发行版的滚动和高级“快速”版本中。

后门需要满足某些条件和依赖项才能触发。然而，一旦触发，攻击者就可以在完全没有身份验证的情况下进入你的系统。

错误的代码已被迅速清除，但现在的问题是这个后门已经造成的潜在损害——以及是谁植入了这个诡计，他们的目的是什么。

更令人担忧的是，这个库中可能还存在其他尚未发现的后门，或者已经植根于更多服务器仍在使用的库的早期版本中。

## 如果不是一个爱管闲事的工程师...

感谢那些足够极客的工程师，他们在 [SSH 会话](https://thenewstack.io/linux-run-a-single-command-across-multiple-servers-with-ssh/) 中调试缓慢的登录时间。

Microsoft 原理软件工程师（Principle Software Engineer） [Andres Freund](https://github.com/anarazel) [注意到](https://www.openwall.com/lists/oss-security/2024/03/29/4) 他的 [远程 ssh 登录](https://thenewstack.io/secure-remote-linux-server-logins-with-ssh-key-authentication/) 比应有的时间长 500 毫秒。他将延迟追溯到 SSH 对 [liblzma](https://tukaani.org/) 压缩库发出的系统调用，原因是该库包含在 Freund 的 [Debian sid](https://wiki.debian.org/DebianUnstable) 安装中嵌入的 [xz 实用程序](https://tukaani.org/) 中。

他在安装过程中用于 Debian 的 xz 实用程序 tarball 中追踪到了后门代码——尽管它们不在库的原始 GitHub 源代码中。

额外的包袱是一个[混淆脚本](https://gynvael.coldwind.pl/?lang=en&id=782)，它将在 tarball 的配置设置结束时执行。

Freund 向 Debian 安全部门报告了错误的 tarball，然后向分销商渠道报告。Red Hat 将此问题提交为 [CVE-2024-3094](https://access.redhat.com/security/cve/CVE-2024-3094)，严重性为 10。

对于 Freund 来说，这种看似恶意的代码注入发生在 Linux 发行周期的上游，这让他很担心。

“考虑到数周的活动，提交者要么直接参与其中，要么他们的系统遭到了一些非常严重的破坏。不幸的是，鉴于他们在各种列表中就上述‘修复’进行了交流，后者似乎不太可能，”他写道。

## Jia Tan 是谁？

[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 工程师 [Richard WM Jones](https://rwmj.wordpress.com/) 一直与后门的明显作者联系，他在 Hacker News 上 [转发](https://news.ycombinator.com/item?id=39865810)。

这位名为 Jia Tan 的贡献者一直“试图将 xz 5.6.x 添加到 Fedora 40 和 41”，因为它“‘有很棒的新功能’”。

![](https://cdn.thenewstack.io/media/2024/03/12d925be-jia_tan-150x150.jpg)

*来自 Jia Tan 的 GitHub 帐户。*

“他加入 xz 项目已有 2 年，添加了各种二进制测试文件，老实说，有了这种复杂程度，我甚至会怀疑更早版本的 xz，直到有相反的证据，”Jones 写道。

发现包含后门的 XZ Utils [5.6.0](https://github.com/tukaani-project/xz/releases/tag/v5.6.0) 和 [5.6.1](https://github.com/tukaani-project/xz/releases/tag/v5.6.1) 版本 tarball。两者均由 Jia Tan（[JiaT75](https://github.com/JiaT75)）创建并签名。

安全专家 [Michal Zalewski](https://lcamtuf.coredump.cx/) 指出，Jia Tan 可能是一个化名，[解释说这个角色显然在 2021 年凭空出现](https://lcamtuf.substack.com/p/technologist-vs-spy-the-xz-backdoor)。

JiaT75 于 2021 年在 GitHub 上注册，此前没有任何活动记录，并立即开始处理 [xz 实用程序](https://github.com/tukaani-project) 项目。该帐户除了一个 gmail 地址外，没有其他身份信息。

xz 首席维护者是 Lasse Collin（[Larhzu](https://github.com/Larhzu)），自项目成立以来一直参与其中。他通常会对 xz tarball（多个文件的捆绑包）进行签名以进行分发。然而，他让 Tan 处理了最近的几个版本。

Collin 对 Tan 了解多少并未明确。就在这场混乱之前，Collin 已下线，处在网络休假中，只上网一次，[在项目网站上发布了一条简短的回复](https://tukaani.org/xz-backdoor/)。

Zaleski 的侦查发现，过去几年中，Collin 一直受到网络骚扰者的[纠缠](https://www.mail-archive.com/xz-devel@tukaani.org/msg00566.html)，要求他辞去 xz 管理员的职务。

![](https://cdn.thenewstack.io/media/2024/03/469e4a89-xz-troll.png)

*网络骚扰者要求 xz 维护者下台*

在一条消息中，Collin 承认他最近几乎没有时间跟进不断增加的 Backlog。“从长远来看，必须做出一些改变，”他[写道](https://www.mail-archive.com/xz-devel@tukaani.org/msg00563.html)，并补充说，随着时间的推移，他希望 Tan 承担更多职责。

Zaleski 怀疑 JiaT75 的工作，鉴于其总体的高质量，并非业余爱好者的工作。

Zaleski 推测，“所有迹象都表明这是一项专业且有偿的工作”，甚至可能是外国政府所为。

其他安全专家似乎也同意注入代码的整体复杂性：

“这可能是我们见过的描述最详细的供应链攻击，这是一个噩梦般的场景：恶意、有能力、在广泛使用的库中获得上游授权，”开源维护者 [Filippo Valsorda](https://filippo.io/) 在 BlueSky 上 [写道](https://bsky.app/profile/filippo.abyssdomain.expert/post/3kouaom62oi2b)。

Jia Tan 只能访问托管在 GitHub 上的 xz 文件；Collin 保留对网站的控制权。出于安全考虑，GitHub 已禁用所有 xz 实用程序存储库，并暂停了 Tan 和 Collin 的帐户。

## Linux 服务器上部署了 xz 僵尸网络后门吗？

如果您运行 Linux 或 macOS 系统，您很可能拥有 xz 和 liblzma 依赖项的某个版本，这些依赖项是解压缩软件包以进行安装和更新所必需的。

到目前为止，主要是滚动发布和快速更新发行版引入了 XZ Utils 5.6.0 和 5.6.1，例如 Fedora Linux 40 和 Fedora Rawhide 以及 [Debian 高级发行版](https://lists.debian.org/debian-security-announce/2024/msg00057.html)。

Ubuntu 24.04 LTS（Noble Numbat）也包含受感染文件， [现已删除](https://discourse.ubuntu.com/t/xz-liblzma-security-update/43714/3)。[Arch](https://archlinux.org/news/the-xz-package-has-been-backdoored/) 和 [openSUSE](https://lwn.net/ml/opensuse-factory/5d7acd45-7021-4c09-8c0b-6f4b8797aecd@suse.com/) 也发布了公告。

Red Hat 已[报告](https://www.redhat.com/en/blog/urgent-security-alert-fedora-41-and-rawhide-users)没有任何 Red Hat Enterprise Linux 版本受到损害。

后门似乎仅通过一组特定条件触发：根据 Gentoo Linux 开发者 [Sam James](https://wiki.gentoo.org/wiki/User:Sam) 发布的 [za-utils 后门常见问题解答](https://gist.github.com/thesamesam/223949d5a074ebc3dce9ee78baad9e27)，通过“连接到公共 SSH 端口的远程非特权系统”。

除了安装 5.6.0 或 5.6.1 tarball 之外，该漏洞还必须是在 AMD64 硬件上运行的 Linux 发行版，并使用 [glibc](https://www.gnu.org/software/libc/) 库（例如所有那些 Debian 和 Red Hat 衍生版本）。

[systemd](https://thenewstack.io/systemds-lennart-poettering-wants-to-bring-linux-home-directories-into-the-21st-century/) 和已修补的 *openssh* 的组合似乎也是后门的要求。

payload 由 `/usr/sbin/.`  中运行的 `sshd` 守护进程触发。恶意代码实际上被嵌入到 *sshd* 本身中，这要归功于最近的 sshd 补丁，以支持 [systemd-notify](https://www.freedesktop.org/software/systemd/man/249/systemd-notify.html)，允许其他服务（包括 liblzma）在 sshd 运行时收到警报。

一旦进入 `sshd`，有效载荷会将 sshd 的解密功能重定向以绕过用户身份验证。

“其他系统此时可能存在漏洞，但我们不知道，”James 写道。

Red Hat [警告其用户](https://www.redhat.com/en/blog/urgent-security-alert-fedora-41-and-rawhide-users)妥协的严重性：

“在适当的情况下，这种干扰可能会让恶意行为者有机会绕过 sshd 身份验证，并远程获得整个系统的未授权访问权限。”

## xz后门有多少？

鉴于上面列出的这些条件，如果你正在运行一个可公开访问的 SSH 的服务器实例，James 建议你应该“**立即立即立即更新。**”

他强调，目前已知的关于后门触发器及其感染版本的信息非常有限。

“虽然不是危言耸听，但明确一点很重要，在这个阶段，我们很幸运，而且受感染的 liblzma 可能会产生其他影响，”James 写道。

一方面，JiaT75 可能会在他任职期间（至少可以追溯到 v5.3.1）在 xz 的早期版本中植入其他隐藏得更好的后门？

当然，这意味着 [Linux 发行版池更大](https://thenewstack.io/vendoring-why-you-still-have-overlooked-security-holes/) [可能会受到影响](https://thenewstack.io/chainguard-outdated-containers-accumulate-vulnerabilities/)。

根据 Red Hat 的说法，美国网络安全和基础设施安全局 ( [CISA](https://www.cisa.gov/)) 目前正在进一步调查后门。

好消息是情况本可以更糟：原始上游 OpenSSH 不会受到影响——除非 *liblzma* 被添加为依赖项。

尽管如此，OpenSUSE 建议其 Tumbleweed 用户为面向公众的服务器重新安装 SSH，因为无法判断这些服务器是否已被入侵。

无论如何，后门是如何如此接近如此多的生产系统的，这可能是对互联网基础设施状态的一个警示故事。

“不过，我认为这意味着应该结束手动构建上游 tarball 而非直接提取 git 源的惯例，例如 debian 等发行版所支持的惯例，”一位评论员 [在 LXN.net 上指出](https://lwn.net/Articles/967180/)。

“这是唯一一个在其他相当可复制的管道中很少有人关注的薄弱环节，而这实际上只是时间问题，直到有人利用它。”
