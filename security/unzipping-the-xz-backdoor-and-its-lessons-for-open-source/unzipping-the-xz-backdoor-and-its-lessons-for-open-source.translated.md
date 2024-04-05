# 解压 XZ 后门及其对开源的教训

![解压 XZ 后门及其对开源的教训的特色图片](https://cdn.thenewstack.io/media/2024/04/176ff530-intruder123-1024x576.jpg)

到目前为止，你可能已经听说过最近发现的 [xz 实用程序](https://thenewstack.io/malicious-code-in-linux-xz-libraries-endangers-ssh/) 的 5.6.0 和 5.6.1 版本的后门，这是一个流行的 xz 文件压缩/解压缩库，在特定条件下提供未经授权的远程访问。此漏洞在 [CVE-2024-3094](https://access.redhat.com/security/cve/CVE-2024-3094) 下进行了报告。发现此漏洞的 Microsoft 的 Andres Freund [很好地总结了它](https://www.openwall.com/lists/oss-security/2024/03/29/4)。

由于引入此后门的方式以及此后门引入的风险程度，这一最初的公告迅速在整个开源生态系统中引起了轩然大波。这（再次）引发了许多关于开源维护的吃力不讨好的工作的问题，特别是当个人贡献者在几乎没有继续这样做的动机的情况下承担这项任务时。

这是我对这种类型的漏洞的来龙去脉以及原因的看法，以及行业可以采取哪些措施来尝试改变这一令人担忧的趋势。

## 发生了什么以及它是如何被发现的

虽然这
[仍然是一个发展中的故事](https://thenewstack.io/linux-xz-backdoor-damage-could-be-greater-than-feared/)，但已经揭示了许多关于此库是如何被破坏的细节。它始于 2021 年，当时一个名为 Jia Tan 的 GitHub 帐户在 libarchive 中打开了一个可疑的 PR。然后在 2022 年，他被添加为 xz 项目的维护者，而该项目的官方维护者 Lasse Collin 正在处理个人问题。Jia Tan 逐渐在 2023 年提交并合并了后门的部分内容到 xz 中。

3 月 29 日，Freund 说他不是安全研究员，他开始在 sshd 中体验到一些缓慢，sshd 在某些 Linux 发行版中依赖 xz 库，并且 CPU 也很高。在调查问题的根源后，他发现了 xz 包中的后门，该后门作为看似无害的提交的一部分引入，旨在向存储库添加更多测试，并最终修改构建过程以引入恶意软件。

![](https://cdn.thenewstack.io/media/2024/04/4347ee46-image1a.png)
来源：
[https://xkcd.com/2347/](https://xkcd.com/2347/)

## 谁受到影响？

以下 Linux 发行版已发布声明，称受到后门影响：

请尽快按照每个发行版的说明进行操作，以升级或还原到该软件包的先前版本。

[Debian](https://lists.debian.org/debian-security-announce/2024/msg00057.html)维护人员承认受损软件包是发行版测试的一部分，但稳定版本不应该受到影响。[Ubuntu](https://ubuntu.com/security/CVE-2024-3094)发行版以及 Amazon Linux 不受影响。

## 防止供应链攻击

尽管后门被引入到 Linux 发行版和 MacOS 系统中发现的软件包中，但它再次引发了对供应链攻击的担忧。确保构建管道的完整性以及项目中使用的所有依赖项至关重要。Jit 编排了多个工具来帮助你自动化这些艰巨的任务，包括 GitHub 错误配置和依赖项检查 (SCA)。

## 开源的未来

这一偶然发现概述了开源库中存在的潜在风险，这些库只有一个维护者，他们不堪重负且承受着持续的压力。这也是对整个社区的求助。虽然一些大公司可能会从
[开源世界](https://thenewstack.io/making-europes-romantic-open-source-world-more-practical/) 中获得商业利益，但他们通常通过捐赠而不是允许其员工在工作时间内积极帮助修复这些项目来做出贡献。另一方面，还需要赞助报酬过低维护人员——GitHub Sponsors 和 Open Collective 等平台可以提供帮助。

来自 Linux 基金会和 Apache 基金会等非营利组织的倡议是提供治理支持、法律援助和财务支持以帮助
[确保重要项目的长期性](https://thenewstack.io/tracy-ragan-my-favorite-open-source-security-projects/) 的好方法。得到整个社区的支持肯定会减轻单个维护者的压力。这里发生的事情应该是一个警告信号，表明现在是采取行动并深入了解
[开源维护者](https://thenewstack.io/bots-emojis-and-open-source-maintainers-how-people-and-tools-make-the-difference/) 的日常斗争的时候了。采取行动还为时不晚。现在是作为一个社区崛起的时候了。

## 摘要以及如何获取信息和保护
由于此后门的爆炸性，社区中的许多人都密切关注它并实时报告它。一个提供大量详细信息和几乎每分钟更新的好地方是 [此帖子](https://boehs.org/node/everything-i-know-about-the-xz-backdoor?utm_source=tldrwebdev)，它深入研究了时间线和一些 OSINT（开源情报）来追踪引入此后门的恶意实体。

关于 xz-utils 后门的风险和可用信息的另一个好参考是 [此常见问题解答帖子](https://gist.github.com/thesamesam/223949d5a074ebc3dce9ee78baad9e27)，它分享了详细信息、建议实施的安全措施以及社区可以参与的讨论，以了解受影响的不同 OSS 项目。

这是对整个开源行业的又一次警醒，提醒我们幕后的辛勤工作使我们优秀的 OSS 生态系统得以蓬勃发展，我们当然需要重新审视我们如何激励维护者并对关键任务和广泛采用的项目创造更大的共享所有权。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。