![2026年11月盐湖城 KubeCon + CloudNativeCon 北美峰会上的 Chainguard 展位。(图片来源：The New Stack)](https://cdn.thenewstack.io/media/2026/11/f70453f4-chainguard-kube-con-booth-na-2026-1024x586.png)

**在本周的 2026 KubeCon + [CloudNativeCon 北美峰会](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)上**，Chainguard 联合创始人兼 CTO Matt Moore 为该公司的决定进行了辩护：在与其它合作伙伴约定解除保密期之前，该公司就发布了已修补的 PHP 镜像。

当 Chainguard 在 10 月 21 日协调安全发布前六个多小时发布[已修补的 PHP 容器镜像](https://thenewstack.io/php2shell-chainguard-embargo-dispute/)时，PHP 维护者指责该公司让攻击者抢占了先机。而 Chainguard 则辩称攻击者早已占得先机。

![](https://cdn.thenewstack.io/media/2026/11/0285dd07-chainguard-cto-matt-moore.jpeg)

*Chainguard 创始人兼 CTO Matt Moore*

在接受 *The New Stack* 采访时，[Moore](https://www.linkedin.com/in/mattmoor/) 表示：“我们对选择这样做这一决定负责。没有人能强迫我们这么做——但我们也不是在真空中做出这个决定的。”他在与 TNS 的讨论中还描述了保密期内的其他参与者以及安全供应商关于在 Chainguard 发布镜像之前针对这些漏洞进行攻击活动的报告。

Chainguard 并不是说他们修补得更快所以他们率先发布。据 Moore 称，Chainguard 认为攻击者已经可以利用这些漏洞，或者至少快要弄清楚如何利用——或者正在试图弄清楚。

这两个漏洞，[CVE-2026-109618（内存越界损坏）](https://nvd.nist.gov/vuln/detail/cve-2026-109618)和[CVE-2026-109619（陈旧的全局状态）](https://nvd.nist.gov/vuln/detail/cve-2026-109619)统称为 PHP2Shell，是严重的内存管理和错误处理缺陷。在适当的条件下，未经身份验证的攻击者可以在 PHP 服务器上执行代码。

这两个漏洞涉及 PHP 对内存耗尽的处理以及其在请求之间未能清除对已释放内存的引用的失败。在第一种情况下，在错误的时机达到内存限制可能会在 PHP 完成设置内部数据之前中断它。后续处理可能会将该未完成的数据误认为是有效信息。在第二个漏洞中，错误可能会导致 PHP 保留对先前已被释放的内存的引用。随后的请求随后可以访问该无效内存。在可利用的条件下，这些故障可能让攻击者在服务器的 PHP 进程内运行代码。

研究人员证明了通过 Apache/mod_php 和应用程序级别的 PHP-FPM 路径对第一个漏洞进行远程代码执行，以及针对真实世界的 Apache/mod_php 应用程序对第二个漏洞进行远程代码执行。

这些是 PHP 本身的问题，而不是管理员通过简单更新 WordPress 插件就能修复的问题。这是一个根本性的、令人讨厌的安全漏洞。

## 漏洞究竟有多严重？

根据[通用漏洞评分系统](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w) (CVSS) v4.0，PHP 的公告将这两个漏洞评分为 9.2 分，即严重级别。可利用性取决于 PHP 构建、服务器配置、扩展和应用程序行为。公告并**没有**确定每个 PHP 安装都可能受到损害。PHP 在版本 8.2.35、8.3.36、8.4.27 和 8.5.12 中发布了修复程序。潜在的暴露面是巨大的：截至 11 月 11 日，W3Techs 报告称，在其能够识别服务器端编程语言的网站中，PHP 驱动了 [68.8% 的网站](https://w3techs.com/technologies/comparison/pl-php)。

根据[PHP 基金会的说明](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)，一名开发人员在调查 2024 年安全审计的问题时发现了内存耗尽问题，但当时尚未建立具体的攻击路径。拟议的修复方案存在破坏兼容性、引发新的拒绝服务问题或跨 PHP 扩展发生更改的风险。

8 月 11 日，[Calif](https://calif.io/) 的研究人员 Ryan A. 报告了由相同底层问题引起的远程代码执行。从那天起，修复该问题成为 PHP 基金会安全团队的首要任务。OpenAI 独立报告了相同的底层漏洞。Wiz 在 8 月 24 日提供了额外的攻击向量，OpenAI 在 9 月 18 日报告了更多漏洞。

## PHP 安全补丁是如何破裂的

作为回应，PHP 的维护者与研究人员和分销商协调了修复方案。然后，有关发布过程的细节开始泄露。

10 月 20 日，[CVE 标识符在公开场合流传](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)，并附带了不正确的发布时间和严重性评分。PHP 的回应是发出警告，并将发布时间提前一天，至 10 月 21 日 UTC 时间 14:00。作为报告安全公司之一的 Calif 随后错误地发布了一段展示其概念验证的视频。尽管该视频已被删除，但副本仍在流传。PHP 还承认，向关键基础设施提供商提供的缓解建议可能已经泄露。

简而言之，在 Chainguard 发布任何内容之前，信息环境就已经一团糟了。

但 PHP 基金会坚称其剩余的协调窗口仍然有其目的：具体而言，分销商正在打包修复程序，如果立即发布，将使许多用户没有直接的更新途径。10 月 21 日 UTC 时间 07:41，Chainguard 还是发布了其修补后的镜像——比约定时间早了整整六小时 19 分钟。

PHP 基金会[批评](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/#:~:text=the%20coordinated%20release%2C-,Chainguard%20unilaterally%20broke%20the%20embargo%20and%20published%20built%20images%20containing%20the%20fix.,-Like%20other%20distributors)了这一举动：“Chainguard 单方面打破了保密期，并发布了包含修复程序的构建镜像。”他们认为，这意味着“任何攻击者现在都可以以二进制形式研究修复程序，而所有其他 PHP 用户仍在等待发布。”

> 打了一个补丁的二进制文件可以保护安装它的人。它也可以告诉攻击者去哪里寻找。

这是 PHP 基金会的核心反对意见。打了补丁的二进制文件可以保护安装它的人。它也可以告诉攻击者去哪里寻找。

## Moore 的辩护：优势已经向攻击者倾斜

Moore 并不否认发布打过补丁的二进制文件可能会帮助攻击者。他认为，到那时，保密期原本旨在维持的优势已经侵蚀殆尽。

他告诉 *The New Stack*，当只有防御者知道漏洞时，机密性给了他们准备的时间。一旦攻击者有足够的信息来利用它，扣留可用的修复程序就会逆转这种优势：攻击者可以采取行动，而保密期之外的用户无法保护自己。

Moore 说：“如果我们看到野外的漏洞利用，我们就有责任将其发布。”在他看来，其他安全供应商的报告才是推动 Chainguard 得出这一结论的原因。

Moore 表示，Chainguard 在发布前的星期五得知 PHP 存在漏洞，便将漏洞挖掘工具指向该软件，并在几小时内发现了该漏洞或产出了概念验证。这是 Chainguard 对自身研究的说法。但这有助于解释该公司打破保密期的想法：如果你的工具能快速找到漏洞，你就必须考虑攻击者的工具是否也能做到这一点。

他还反驳了关于 Chainguard 单干的暗示。据 Moore 称，当欧洲的 PHP 维护者还在睡觉时，其他保密期参与者叫醒了 [Chainguard CEO Dan Lorenc](https://www.linkedin.com/in/danlorenc) 来讨论局势。Moore 拒绝透露这些参与者的身份。

Moore 接受了 Chainguard 做出最终决定的事实。然而，这确实区分了该公司对有争议的紧急决定的说法，与那种在没有讨论的情况下忽视所有人的说法不同。

## 证据支持担忧，而非确定性

公开证据支持 Chainguard 的担忧，即攻击者已经在针对这些缺陷进行攻击。例如，亚马逊威胁情报中心报告称，在其 MadPot 蜜罐网络上发现了 [PHP2Shell 漏洞利用尝试](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/)，时间是在 10 月 17 日，即公开披露前四天。它还报告了从 10 月 21 日 UTC 时间 02:00 左右开始的概念验证漏洞利用，随后在接下来的六个小时内来自匿名基础设施的其他尝试。其中一些活动明显早于 Chainguard 在 07:41 的发布。

Cloudflare 同样报告称，在官方发布之前，观察到了针对其客户的攻击流量。该公司表示，其免费和付费的[Web 应用防火墙保护](https://blog.cloudflare.com/php-vulnerabilities-waf-protection)从 10 月 21 日 UTC 时间 03:02 开始默认启用。

所以，不，Chainguard 并不是在凭空想象对这些漏洞的敌意兴趣。

但亚马逊包含了一个重要的限定条件：“技术分析仍在进行中，目前尚不清楚这些尝试是否能在现实世界的系统中成功。”与此同时，PHP 安全团队表示，他们检查了流传的概念验证，并且“在发布/公开披露时未发现任何功能性的漏洞利用。”

这些声明并不一定矛盾。蜜罐可以记录旨在利用漏洞的请求，但这并不等于证明它能够对真实应用程序实现远程代码执行。同样，PHP 未能找到功能性的公开漏洞利用，并不能证明没有攻击者私下拥有它。

后续的证据不应与那天早上已知的情况相混淆。10 月 26 日，CISA 将这两个漏洞都加入了其[已知被利用漏洞目录](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/4309083)。这证实了到那时已知存在漏洞利用；但它并没有确定第一次成功攻陷发生的时间，也没有确定 Chainguard 的提前发布是否促成了这一点。

欢迎来到安全事件响应的世界。证据很少带有整洁的标签。

## 二进制文件是否给了攻击者他们原本没有的东西？

Moore 的第二个论点更狭窄。攻击者已经在探测相关代码，因此发布打过补丁的二进制文件可能并没有太大帮助。

他告诉 TNS：“我没有看到任何证据表明我们所做的事情以攻击者原本没有的方式帮助了他们。”他承认，比较打补丁和未打补丁的二进制文件可以识别脆弱的代码，包括通过 AI 辅助的反汇编。但他认为，识别代码并不一定等于构建可工作的漏洞利用。

很中肯。定位内存损坏漏洞并将其可靠地转化为远程代码执行是不同的工程问题。

尽管如此，这种辩护也有局限性。有证据表明某些攻击者知道去哪里找，但这并不等于证明每个潜在的攻击者都知道。它也不能证明补丁中没有包含除了漏洞位置之外的有用线索。Chainguard 的论点取决于已经有多少可操作的信息以及它的可靠性如何。

同样的限制也适用于针对 Chainguard 的指责。发布二进制文件创造了研究更改的机会。它本身并不能证明某个特定的攻陷是因为 Chainguard 提前发布而发生的。

双方在评估不同的风险。Chainguard 强调了在看到敌意活动时向用户扣留现成补丁的危险。PHP 强调了在更广泛的生态系统更新之前分发新信息的危险。这两种风险都是真实的。

## AI 使时间问题变得更糟

更广泛的担忧是，[AI 辅助的漏洞研究](https://thenewstack.io/php2shell-ai-vulnerabilities-maintainers/)可能会缩短防御者响应的时间。这里引用的公开报告并没有确定发布前的 PHP2Shell 尝试是否使用了 AI，也没有确定这是同类事件中的第一起。

对 Moore 来说，PHP 的争端契合了一个更大的问题：攻击者将漏洞信息转化为漏洞利用的能力可能会超越防御者构建和分发修复程序的能力。

他描述了一种情景：Chromium 补丁公开了，攻击者开发漏洞利用的速度比编译浏览器还要快。这是一个关于行业发展方向的警告，而不是声称确切发生了这种情景。

他说：“你简直无法以足够快的速度生产构建版本。”而构建只是开始。即使 Chainguard 迅速生产出更新的镜像，客户仍然必须将其整合、重新构建他们的应用程序、进行测试并部署。

> 更快并不意味着瞬时，供应商的发布时间也不是客户的修复时间。

这就是“更快打补丁”答案中令人不安的部分。更快是有用的。更快并不意味着瞬时，供应商的发布时间也不是客户的修复时间。

Moore 提出的长期应对措施是首先减少需要这场竞赛的漏洞数量。他与 TNS 讨论了构建与 ABI 兼容的替代品以取代[Rust 中的基础软件组件](https://thenewstack.io/white-house-warns-against-using-memory-unsafe-languages/)的工作，以及旨在排除特定类别缺陷的形式化验证技术。这些仍然是需要评估的工程雄心。

在 Chainguard 的批评者眼中，它们也没有解决该公司在 10 月 21 日应该做什么的问题。一个拥有较少内存损坏漏洞的未来将是受欢迎的，但他们会认为，正在处理当前漏洞的管理员仍然需要一个可行的披露流程。

## 教训比 Chainguard 更宏大

很容易把这起事件看作只是一个关于某个供应商打破规则的故事。同样很容易把它看作是一个关于敏捷安全公司将用户从行动迟缓的上游项目中拯救出来的故事。事情没那么简单。

PHP 自身的复盘承认了一个更深层次的失败。基金会将这种延迟称为“结构性失败”，涉及决策制定和资源不足。

更快地发现bug并不能自动提供[修复它们所需的工程师](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/)。而且，在一家公司准备好补丁并不意味着分发版、托管服务提供商、扩展和应用程序的生态系统已经准备好部署它。

许多人跳出来攻击 Chainguard 的决定。例如，CISA 漏洞管理代理副主任 [Jay Gazlay](http://linkedin.com/in/jay-gazlay-58535) 在华盛顿 10 月 28 日的红帽会议上表示：“这种行为是危险的，我们必须[谨慎对待保持保密期](https://federalnewsnetwork.com/cybersecurity/2026/10/dangerous-cisa-official-criticizes-companys-decision-to-release-php-bug-early/)。”

修复关系可能仍有空间。[*Federal News Network*](https://federalnewsnetwork.com/cybersecurity/2026/10/dangerous-cisa-official-criticizes-companys-decision-to-release-php-bug-early/) 援引 [*Politico*](https://www.politico.eu/article/the-cyber-flaw-scramble-that-brought-the-ai-threat-to-life/) 的报道称，PHP 基金会执行董事 Elizabeth Barron 对 Chainguard 表示失望，但希望恢复信任并继续合作。

Moore 称其为“两个非常非常糟糕的选择”之间的“一个艰难的决定”。他说得对。

维护者和分销商需要提前就何时提前解除保密期、谁做出该决定以及其他分销商如何将修复程序交付给用户达成一致。

我们需要尽快做到这一点。否则，下一次事件将以同样的方式结束，供应商们在争论谁打破了保密期。与此同时，管理员们试图弄清楚他们是否能在有人破坏服务器之前打上补丁。

这篇文章最初发布在 [The New Stack](https://thenewstack.io) 上，原标题为 [Chainguard defends its choice to break the PHP security embargo: “We own the decision.”](https://thenewstack.io/chainguard-php-embargo-defense/)