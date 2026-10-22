<!--
title: AI揪出支撑全球70%网站的代码漏洞，修复花费两个月
cover: https://cdn.thenewstack.io/media/2026/10/c9b4537d-owl-illustration-agency-liqwdvdxug-unsplash-1-scaled.jpg
summary: 研究人员借助前沿AI模型发现了影响全球70%网站的PHP核心高危漏洞PHP2Shell。该漏洞潜伏长达十年之久，引发了业界对AI在网络安全攻防中双刃剑作用的广泛讨论与应对。
-->

研究人员借助前沿AI模型发现了影响全球70%网站的PHP核心高危漏洞PHP2Shell。该漏洞潜伏长达十年之久，引发了业界对AI在网络安全攻防中双刃剑作用的广泛讨论与应对。

> 译自：[AI found flaws in the code behind 70% of the web. The fix took two months.](https://thenewstack.io/ai-php2shell-disclosure-framework/)
> 
> 作者：Amanda Caswell

**PHP支撑了全球大约70%的网站**，[根据Wiz Research的数据](https://www.wiz.io/blog/php2shell-php-rce)，因此其核心引擎中的一个漏洞所影响的范围远超任何单一应用程序。周三，研究人员披露了在顶尖AI模型的协助下发现的两个严重漏洞。OpenAI还针对AI正在协助发现的日益增多的安全漏洞，提出了一个新的处理框架。

这些漏洞被追踪为 CVE-2026-109618 和 CVE-2026-109619，统称为 PHP2Shell，在 CVSS v4.0 严重性评分标准上的得分为 9.2 分。[Calif.io](https://calif.io/php2shell/) 的研究人员使用 OpenAI 的 GPT-5.6 Sol 发现了一个漏洞，而 Wiz 则独立使用其 Wiz Atlas 工具以及谷歌的 Gemini 4 Argon 和 GPT-5.6 Sol 发现了这两个漏洞。Cloudflare 还将 Quarkslab 列为披露这些漏洞的参与方之一。

## 潜伏十年的缺陷

问题始于 PHP 处理错误的方式。当请求耗尽内存或崩溃时，PHP 可能会留下对已被释放的内存的引用。同一个工作进程处理的下一个请求可能仍然将这些引用视为有效。Wiz 发现攻击者可以利用这种行为来访问敏感数据或运行恶意代码。

这些是内存安全漏洞，包括释放后重用（use-after-free）和类型混淆，多年来开发人员一直试图通过[将关键的 C 语言代码迁移到 Rust 等语言中](https://thenewstack.io/code-wars-rust-vs-c-in-the-battle-for-billion-device-safety/)来防止这些漏洞。PHP 的引擎是用 C 语言编写的，Wiz 表明攻击者可以利用这些漏洞在无需登录的情况下在 WordPress、Drupal 和 Joomla 上运行代码。研究人员还演示了在不执行代码的情况下暴露服务器内存的攻击。

过去十年发布的每一个 PHP 版本都至少受到其中一个漏洞的影响，部分漏洞代码甚至可以追溯到 PHP 5.4。这些漏洞长期未被发现，是因为利用它们需要将多个弱点以难以发掘的方式结合起来。

这就是 AI 发挥作用的地方。Wiz 表示，一名研究人员利用顶尖模型在一周左右的时间内完成了一支专家团队以前可能需要数月才能完成的工作。该公司将这些发现称为“AI 的一个转折点”，并认为这些漏洞一直存在，但 AI 让它们更容易变成可用的攻击利用程序。

Google DeepMind 旗下 Gemini Security 的负责人 [Raluca Ada Popa](https://www.linkedin.com/in/ralucaadapopa/) 在 [Wiz 发表的一份声明中](https://www.wiz.io/blog/php2shell-php-rce)称，前沿 AI 是“网络防御的游戏规则改变者”。安全团队已经在投入使用类似工具。Cursor 最近发布了[一组智能体的蓝图](https://thenewstack.io/cursor-open-sources-security-agents/)，这些智能体会搜索其代码库中的漏洞并在拉取请求（pull request）中阻止它们，这反映出人们越来越担心攻击者会使用相同的技术来率先发现弱点。

## 耗时两个月修复

Wiz 表示，它于 8 月 19 日发现了第一个漏洞，并在第二天确认了针对 Drupal 的未经身份验证的代码执行。它于 8 月 21 日对 WordPress 进行了同样的演示，并于 8 月 24 日向 PHP 的安全团队报告了这些漏洞。该团队于 9 月 21 日确认了报告并开始构建协同修复方案，修复后的版本于周三（也就是详情公开的同一天）发布。

> Wiz 感谢包括 Cloudflare、Google Cloud、AWS、Microsoft 和 Akamai 在内的合作伙伴协助协调保护措施和指导。

部分挑战在于确保修复方案涵盖了该漏洞的每个版本。Wiz 表示，其研究人员在 PHP 处理内存的方式中发现了同一潜在问题的几个变体。在细节公开之前，托管服务提供商、云平台、安全供应商和 Linux 发行商也需要时间进行准备。Wiz 感谢包括 Cloudflare、Google Cloud、AWS、Microsoft 和 Akamai 在内的合作伙伴协助协调保护措施和指导。

## 九小时的预警

详细信息在计划披露日期之前就泄露了。[Cloudflare](https://blog.cloudflare.com/php-vulnerabilities-waf-protection/) 表示，它在周三协调世界时（UTC）凌晨 3:02 开始默认保护其客户，比公开宣布早了大约九小时，并且它在观察客户的同时监控了针对这些客户的攻击流量，同时看着攻击者修改其有效负载以规避规则。该公司表示，仅凭请求数据并不总能显示漏洞利用是否成功，因此其新的保护措施还会检查服务器的响应。

> “客户应该补全其 PHP 库。”

Cloudflare 对防火墙能做什么和不能做什么直言不讳。“客户应该补全其 PHP 库，”该公司[写道](https://blog.cloudflare.com/php-vulnerabilities-waf-protection)，将其规则描述为更新窗口期间的一层额外的防御，而不是修复方案的替代品。这些规则可以阻止漏洞利用尝试，但它们不会消除运行在服务器上的软件中潜在的根本缺陷。

## 重新思考规则手册

在过去的两个月里，OpenAI 领导了一项针对 PHP 的联合行动，这是其[“修补地球”（Patch the Planet）](https://patchtheplanet.org)倡议的一部分。该公司表示，PHP 的维护者领导了修复和发布工作，而 OpenAI 及其合作伙伴则贡献了研究、技术支持和协调工作，随后它利用这一契机提出了一个应对前沿 AI 发现的严重漏洞的框架，[并请安全社区](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/)协助对其进行完善。

整个过程分为五个阶段：维护者、研究人员和关键技术合作伙伴首先确认并修复漏洞，然后用前沿模型测试补丁以寻找绕过方法；接着，受影响的组织会根据其行动能力获得提前信息，以便分发商可以向后移植（backport）修复程序、托管服务提供商可以测试缓解措施、安全供应商可以编写检测规则，政府机构随后跟进以帮助指导触达关键基础设施的运营者。

一旦修复和披露计划稳定下来，分发商和服务提供商就会在其产品中准备更新，同时公共指导可帮助运营者确认更新正在运行。OpenAI [表示其在 PHP 上的工作](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/)涉及美国网络安全和基础设施安全局（CISA）、国家网络总监办公室、白宫超级智能力量（Super Intelligence Force）以及国际合作伙伴。

> “同样的能力也可以帮助攻击者迅速开发出进攻性工具和漏洞利用程序。”

OpenAI 还谈到了其自身技术的另一面，写道“同样的能力也可以帮助攻击者迅速开发出进攻性工具 and 漏洞利用程序”，并称 PHP 漏洞是“近年来最具影响力的安全问题之一”。

该公司通过[“保卫前线突破”（Daybreak for Frontline Defenders）](https://openai.com/index/daybreak-for-frontline-defenders/)项目承诺提供 10 亿美元的补贴访问权限，旨在帮助那些安全资源有限但肩负保护基本服务职责的组织，它还通过[“开源代码库的 Codex”（Codex for OSS）](https://openai.com/form/codex-for-oss/)订阅以及对项目的直接赞助来支持维护者。

资金和对 AI 模型的访问权限可以提供帮助，但它们无法解决开源维护人员面临的日益增加的工作量。发现漏洞的工具同时也正在生成[必须由维护人员进行审查的 AI 编写代码](https://thenewstack.io/vibe-coding-when-ai-writes-the-code-who-secures-it/?utm_source=chatgpt.com)，这给原本就要求严格的工作增添了负担。OpenAI 承认，每个项目都有自己的优先级，这意味着支持可能无法触及每一个需要它的项目。

## 先打补丁，永远保护

[PHP 安全公告](https://www.php.net/archive/2026.php#2026-10-21-5)列出了 10 月 21 日发布的四个已修复版本：PHP 8.5.12、8.4.27、8.3.36 和 8.2.35。使用 Linux 发行版或托管托管服务提供商的团队应与其供应商核实，因为修复程序可以在不改变 PHP 版本号的情况下进行向后移植。

OpenAI 还发布了一个 [PHP 版本检查器](https://github.com/openai/php2shell-checker)，其中包含两个用于检查本地服务器和网站的 Codex 技能。该工具可以标记出易受攻击的版本，但无法确认是否已经应用了补丁，特别是当供应商向后移植了修复程序时。