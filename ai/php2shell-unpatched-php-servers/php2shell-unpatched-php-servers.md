<!--
title: “恐慌并未化为补丁”：安全研究员如何看待PHP2Shell应对现状
cover: https://cdn.thenewstack.io/media/2026/07/3dbc5db0-egor-komarov-swezl05imji-unsplash-scaled.jpg
summary: 本文探讨了高危PHP2Shell漏洞爆发后，尽管安全警报频传且攻击激增，但绝大多数企业和服务器修复速度极为缓慢，超九成暴露在风险中，面临严峻的安全威胁。
-->

本文探讨了高危PHP2Shell漏洞爆发后，尽管安全警报频传且攻击激增，但绝大多数企业和服务器修复速度极为缓慢，超九成暴露在风险中，面临严峻的安全威胁。

> 译自：[“The panic hasn’t turned into patching”: What security researchers really think about the PHP2Shell response](https://thenewstack.io/php2shell-unpatched-php-servers/)
> 
> 作者：Steven J. Vaughan-Nichols

**PHP恐慌并未转化为打补丁行动：**随着PHP2Shell攻击的加剧，这个坏消息可以说是“大写加粗”的坏。

我们知道，[成对的PHP漏洞 CVE-2026-109618 和 CVE-2026-109619，即 PHP2Shell](https://thenewstack.io/ai-php2shell-disclosure-framework/)，其通用漏洞评分系统（CVSS）高达 9.2 分，可以说是极度危险。毕竟，大约 70% 带有可识别服务器端语言的网站都运行在诸如 WordPress 等基于 PHP 的系统上。

但这是否意味着人们正以最快速度为服务器打补丁呢？

借用 [Ox security](https://www.ox.security/) 的 Moshe Siman Tov Bustan 的话来说：“恐慌并没有转化为打补丁的行动。”Ox 在一篇新的博客文章中指出，截至 10 月 26 日（漏洞披露五天后），情况几乎没有变化——[高达 93.6% 的系统仍然暴露在外。](https://www.ox.security/blog/php2shell-day-5-the-panic-hasnt-turned-inspired-patching/)“

真是太糟糕了！太痛了！

> “……修复工作并未处于恐慌状态，它简直如蜗牛般缓慢，头条新闻铺天盖地，野外修复的实例却寥寥无几”

Bustan 接着写道：“修复速度太慢了，当所有人都在为 PHP 的 CVE 漏洞恐慌时，修复工作并没有进入恐慌状态，它简直如蜗牛般缓慢，头条新闻铺天盖地，野外修复的实例却寥寥无几……我们错失了真正将补丁发布的良机——而现在，当漏洞利用程序已经出现、在野外被证实并非只是猜测时——我们却将最宝贵的资产暴露在外，任由下一个黑客利用。”

我们真的很喜欢在危险边缘试探，不是吗？

不仅 Ox 报道了糟糕的 PHP2Shell 补丁数据。安全公司 [Censys](https://censys.com/) 在其截至周二的 PHP2Shell 调查中报告称，约有 1120 万个面向互联网的 PHP 服务显示已安装[打过补丁的版本](https://php2shell.censys.com/)。这并没有听上去那么令人印象深刻。这些统计基于服务器报告的 PHP 版本，由于 Linux 发行版经常在不改变版本号的情况下进行漏洞修复的反向移植（backport），一些“易受攻击”的服务可能实际上已经打过补丁了。

大约有 3250 万个服务仍然显示其运行的是不安全的 PHP 版本。同时，Censys 无法确认 61,303,506 个 PHP 服务（占检测总数的 58%）正在运行什么版本。其中许多服务可能正在运行不受支持的 PHP 版本。

这是一个令人头皮发麻的消息。安全公司 [Flare](https://flare.io/) 在 10 月 22 日的一份报告中发现，在其追踪的 220 万个 PHP 服务记录中，“近四分之三声明使用的是 PHP 项目[不再支持](https://flare.io/learn/resources/blog/php2shell-exposure)的分支。”

另一家利用 AI 追踪互联网危险的安全公司 [Mallory](https://mallory.ai/) 对 260 万个服务进行了研究，发现大约有 [190 万个面向互联网的服务](https://mallory.ai/blog/php-rce-rapid-response)在运行不受支持的 PHP 版本。这大约占所调查服务的 73.5%。

> 此类系统不会获得官方补丁发布。它们必须升级到受支持的版本。

此类系统不会获得官方补丁发布。它们必须升级到受支持的版本。这比单纯给受支持的 PHP 版本打补丁要复杂得多。

正如 AI 安全公司 [ArmorCode](https://www.armorcode.com/) 高级首席解决方案工程师 Ramy Rahman 在周二的一份声明中所说：“现实情况是，许多组织可能正在运行较旧的、不受支持的版本，这引入了额外的复杂性，例如升级应用程序、解决兼容性问题，或者与供应商合作获取受支持的修复程序。”

话虽如此，正如美国国家安全局（NSA）在 PHP2Shell 首次出现时所言：“建议所有使用 PHP 系统的组织做好准备，进行更新以解决两个关键漏洞……如果无法立即更新，建议[组织将系统下线，直到完全缓解风险。](https://x.com/NSACyber/status/2112903220209098897)“

显然，虽然某些组织已经这样做了，例如 [Wikimedia 基金会](https://www.reuters.com/world/asia-pacific/eu-agency-warns-websites-may-need-be-taken-offline-php-prepares-patches-2026-10-21/)和互联网档案馆（Internet Archive），并且有两个[由 PHP 驱动的网络游戏已永久关闭](https://kotaku.com/two-of-japans-oldest-mobile-games-have-been-forced-permanently-offline-because-of-the-new-exploit-ravaging-the-web-2000748511)，但大多数人并没有这么做。与此同时，一些政府已强制要求打补丁。最大的例子是美国。网络安全和基础设施安全局（CISA）强制[联邦民事行政分支机构进行 PHP2Shell 修复](https://www.cisa.gov/news-events/alerts/2026/10/26/cisa-adds-two-known-exploited-vulnerabilities-catalog)，截止日期为 2026 年 10 月 29 日星期四。

说起来容易做起来难。正如我们所看到的，PHP2Shell 攻击目前正在持续进行。CISA 没有透露任何细节，但这些 CVE 报告现在已被列入其[已知被利用漏洞](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)目录中。

此外，[Perplexity AI](https://www.perplexity.ai/) 的检测与响应负责人 [Adel Karimi](https://www.linkedin.com/in/adelka/) 表示，他的[蜜罐记录了证据](https://github.com/0x4D31/honeypot-data/tree/main/reports/php2shell/2026-10-24-rce-evidence)，证实了针对运行打补丁前漏洞版本的 PHP 8.4.26 的 Apache mod_php 安装存在[远程代码执行](https://github.com/0x4D31/honeypot-data/blob/main/reports/php2shell/2026-10-24-confirmed-rce.md)。Karimi 警告说，他的单工作进程设置故意对攻击者更有利。

> 在公告发布后的 45 分钟内，这一数字跃升至数万，2 小时内达到数十万，而现在则达到了数百万。

正如 [Cloudflare](https://www.cloudflare.com/) 首席执行官 [Matthew Prince](https://www.linkedin.com/in/mprince/) 在 [X](https://x.com/eastdakota/status/211307935268257005) 上所发：“在公开宣布前的 10 个小时里，在 @Cloudflare 网络中，我们看到了数千次利用它的尝试。在公告发布后的 45 分钟内，这一数字跃升至数万，2 小时内达到数十万，而现在则达到了数百万。”

情况只会变得更糟。很快，这波攻击尝试将变成成功攻击的洪流。系好安全带，这将是一段颠簸的旅程。