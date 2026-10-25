**欧洲各地的政府网站和公共服务**本周[离线](https://thenewstack.io/php2shell-chainguard-embargo-distpute/)，因为各组织正在应对两个新披露的PHP漏洞。德国将几个联邦网站下线，法国暂时关闭了省级网站，比利时的外交部禁用了其网站，荷兰的组织作为预防措施下线了面向公众的服务。这种情况并不局限于欧洲，[无数其他实体和](https://www.reuters.com/world/asia-pacific/eu-agency-warns-websites-may-need-be-taken-offline-php-prepares-patches-2026-10-21/)全球[企业](https://www.reuters.com/world/asia-pacific/eu-agency-warns-websites-may-need-be-taken-offline-php-prepares-patches-2026-10-21/)也在做出类似的响应。

他们都在等待一个尚不存在的PHP漏洞缓解方案。

起因是PHP2Shell：[CVE-2026-109618](https://www.zend.com/php-security-center/CVE-2026-109618) 和 [CVE-2026-109619](https://www.zend.com/php-security-center/CVE-2026-109619)。虽然社区迅速行动，PHP项目于10月21日上午发布了所有社区支持版本的修复程序，但更大的问题仍未解决：[据估计，有40%的PHP用户正在运行不受支持的PHP版本](http://www.zend.com/resources/php-landscape/report)，而此时AI已经呈指数级[加速了CVE的发现](https://thenewstack.io/php2shell-ai-vulnerabilities-maintainers/)。

> “本周发生的事情与以往不同，这是开源生态系统中一场势必长期持续的战斗的第一枪。”

我参与开源贡献已有20多年；我领导着 [Laminas Project](https://getlaminas.org/)，我是Perforce [Zend](http://www.zend.com/) 和 [OpenLogic](http://www.openlogic.com/) 的首席产品经理，我目前还在 [PHP Foundation](https://thephp.foundation/structure/) 的董事会任职——这也就是说，我见证过的新安全威胁数不胜数。

本周发生的事情与以往不同，这是开源生态系统中一场势必长期持续的战斗的第一枪。

## 关于 PHP2Shell，你需要了解什么

[CVE-2026-109618](https://www.zend.com/php-security-center/CVE-2026-109618) 和 [CVE-2026-109619](https://www.zend.com/php-security-center/CVE-2026-109619)（目前被称为 PHP2Shell）由内存溢出 (OOM) 条件与 PHP 错误处理的组合触发，带来了远程代码执行 (RCE) 风险。可以追溯到 5.4 版本的每一个 PHP 版本都至少受其中一个漏洞影响。这两个漏洞尤为令人担忧，因为它们存在于 PHP 本身，而不是单个应用程序、CMS 或框架中；除了打过补丁的 PHP 运行时之外，没有真正的缓解措施。

[Wiz Research](https://www.wiz.io/blog/php2shell-php-rce) 发现，这些漏洞可能允许攻击者远程执行代码或暴露进程内存中的敏感信息，包括密码、身份验证 Token、API 密钥和证书。这种暴露与运行在 PHP 上的应用程序无关。

此外，独立重现了这些漏洞的 [Datadog Security Labs](https://securitylabs.datadoghq.com/articles/php2shell-critical-vulnerabilities-in-php/) 发现，应用层身份验证无法阻止该攻击，因为 PHP 在应用程序代码运行之前就会处理恶意请求。在重现 CVE-2026-109618 时，研究人员报告称该请求“从未到达目标应用程序的代码”。

> “即使具备扎实的应用安全实践，你的应用程序仍然可能暴露，因为漏洞行为发生在应用程序之下、PHP 运行时本身之中。”

这意味着，即使具备扎实的[应用安全实践](https://thenewstack.io/defining-security-in-software-frameworks-compliance-and-best-practices/)，你的应用程序仍然可能暴露，因为漏洞行为发生在应用程序之下、PHP 运行时本身之中。

唯一的解决办法是打补丁。

一旦全面影响在 8 月份明朗化，[PHP Ecosystem Security Team](https://thephp.foundation/blog/2026/05/18/announcing-ecosystem-security-team/)、[PHP Foundation](https://thephp.foundation/) 和版本发布经理就在所有受支持的 PHP 版本中发布了修复程序。在跨生态系统的共同努力下，[他们还与 LTS 供应商合作](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)（例如 [Zend](http://www.zend.com/services/php-long-term-support)），以确保他们同时创建并发布了所有补丁。

这是我 20 多年来第一次看到这样的努力，我为社区朝着这个方向迈进感到喝彩。正是由于这一举措，任何使用社区不再支持的 PHP 版本（8.1 或更早版本）的人都可以免受这些新披露的 CVE 的影响，而不会出现任何漏洞空白。

不幸的是，这种合作也依赖于信任，而信任在这里受到了考验。CVE 编号于 10 月 20 日泄露，导致所有发布时间提前了一天。但截至 UTC 时间 10 月 21 日 14:00，[所有受社区支持的 PHP 版本都已收到更新以缓解这些漏洞](https://www.php.net/archive/2026.php#2026-10-21-5)。我在 Zend 的团队以及其他 LTS 提供商也为 EOL（生命周期结束）的 PHP 版本发布了补丁。

虽然我们在未来几周内需要采取更全面的步骤，但在过渡期间，这些缓解措施将确保为政府、医院、金融机构、学校等提供支持的关键应用程序保持安全和获得支持。

## AI 正在改变漏洞研究的经济学

PHP2Shell 是 AI 让原本困难的安全研究变得更加触手可及的一个典型例子——以及伴随这种知识而来的危险。

[作为 OpenAI “Patch the Planet”计划的一部分，](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/) Calif 使用 GPT-5.6 Sol 发现了一个严重的 PHP 漏洞。PHP 的维护者领导了修复和发布工作，研究人员和安全提供商在披露前贡献了测试、技术支持和协调工作。

> “我们一直在进行漏洞披露、补丁可用性和漏洞利用之间的赛跑。PHP2Shell 证明了这场赛跑可以而且可能会变得多么令人不安和来之不易。”

突显出的是潜在的规模转变。OpenAI 表示，这些已经是它发现并正在努力解决的几个重大漏洞之一，并预计类似的发现在“[未来几个月将急剧增加](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/)”。

我们一直在进行漏洞披露、补丁可用性和漏洞利用 C 之间的赛跑。PHP2Shell 证明了这场赛跑可以而且可能会变得多么令人不安和来之不易。

## 运行 EOL 开源软件 (OSS)？AI 正在提高赌注。

在发生像 PHP2Shell 这样的漏洞后，最简单的建议是立即升级。但运营现实要复杂得多。

PHP 8.1 及更早版本不再从 PHP 项目接收更新，尽管某些发行版和长期支持供应商提供了向后移植的安全修复程序。对于关键应用程序，迁移到新的运行时可能需要更新框架、库、扩展和应用程序代码，以及确保这些更改不会中断生产所需的测试。

随着 AI 改进[漏洞研究](https://thenewstack.io/cve-vulnerability-risk-management/)，这种差距正在扩大，因此这不仅仅是一个 PHP 问题。PHP 只是大多数流行 OSS 技术即将面临的第一个重大例子。例如，我们在过去几个月里看到了[一波 Spring 漏洞报告的涌现](https://www.openlogic.com/blog/spring-boot-dependencies-bom)，并且就在 PHP2Shell 降临的同一天，Node.js 和 Python 也报告了严重漏洞。我还要提及 Linus Torvalds 最近的评论，即由于 [AI 漏洞报告](https://www.theverge.com/tech/932312/linus-torvalds-linux-ai-security-bugs)，[Linux 安全列表正变得难以管理](https://www.theverge.com/tech/932312/linus-torvalds-linux-ai-security-bugs)。

在 Perforce Software 从事 OSS 和 PHP 工作期间，我开始将 LTS 视为通往现代化的桥梁。它允许团队在规划、测试和执行迁移到受支持版本的过程中，继续解决安全漏洞。而且，随着漏洞发现的加速，无限期地停留在不受支持的软件上变得越来越难以证明其合理性。

组织需要在可行的地方保持最新状态，并为无法立即升级的系统制定刻意的安全战略。漏洞被发现的速度越快，这一点就越重要。

## 现在会发生什么？

对于 PHP 用户来说，眼前的首要任务很简单：迁移到修复版本，或者为原本不受支持的版本获取适当的安全修复程序。但让我们谈谈更长期的看法。

人们很容易将 PHP2Shell 作为 PHP 突然变得不那么安全的证据，但事实绝非如此。本周社区和供应商的共同努力证明了这一点。相反，我们需要改变对安全的看法，因为此类漏洞只会变得越来越普遍。

> “是的，我们发现困难安全问题的能力提高了。但我们的响应能力需要跟上步伐。”

AI 正在改变哪些安全调查是切实可行的以及它们发生的速度。当研究人员与项目及更广泛的生态系统合作解决漏洞时，这是很有价值的。但它也给组织带来了更大的压力，要求他们了解自己正在运行什么、尽可能保持在受支持的版本上、建立清晰的漏洞响应流程，并为无法立即升级的应用程序制定计划。

是的，我们发现困难安全问题的能力提高了。但我们的响应能力需要跟上步伐。