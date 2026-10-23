<!--
title: AI发现PHP重大漏洞：更大的安全危机始于2024年
cover: https://cdn.thenewstack.io/media/2026/07/851e8d95-egor-komarov-9kndef3kkbm-unsplash-scaled.jpg
summary: AI技术加速挖掘出影响全球的PHP重大漏洞，引发了关于漏洞披露时效、行业协作以及开源维护资源短缺的激烈讨论，敲响了开源安全警钟。
-->

AI技术加速挖掘出影响全球的PHP重大漏洞，引发了关于漏洞披露时效、行业协作以及开源维护资源短缺的激烈讨论，敲响了开源安全警钟。

> 译自：[AI found a critical PHP flaw. The bigger failure began in 2024.](https://thenewstack.io/php2shell-chainguard-embargo-dispute/)
> 
> 作者：Steven J. Vaughan-Nichols

**周三你最喜欢的网站之一宕机了吗？** 一些网站确实如此，因为运营商在等待修复[PHP中的两个关键漏洞](https://thenewstack.io/ai-php2shell-disclosure-framework/)（支撑着互联网大部分流量的编程语言）期间将服务下线。

这种预防措施并不意味着这些网站遭到黑客攻击。漏洞本身是非常严重的坏消息。但从长远来看，更大的担忧可能是如何处理补丁的保密禁令。

PHP支撑了大约70%的网站，但这个数字反映的是PHP的覆盖范围，而不是易受攻击或被攻陷的网站数量。

WordPress告知网站所有者更新PHP；这些漏洞不需要更新WordPress。

这些漏洞分别是 CVE-2026-109618 和 CVE-2026-109619。PHP项目的修复版本为 8.2.35、8.3.36、8.4.27 和 8.5.12；旧版本PHP的用户需要进行受支持的升级或使用分发商的反向移植（backport）。

这场被称为 PHP2Shell 的PHP安全紧急事件，不仅暴露了这个广泛使用的语言中存在的危险漏洞，还引发了一场关于协同披露的争端，并凸显了随着[AI辅助研究人员](https://thenewstack.io/anthropic-oss-scanner-vulnerabilities/)发现并开发漏洞的速度越来越快，[开源维护者](https://thenewstack.io/php2shell-ai-vulnerabilities-maintainers/)所面临的巨大压力。

通往这场紧急事件的导火索是OpenAI的[Patch the Planet](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/)计划。在该计划中，安全公司Calif利用 GPT-5.6 Sol 找到了实现远程代码执行的路径，并于8月11日将其报告给PHP。OpenAI在当天独立报告了相同的基础问题；Wiz则于8月24日报告了其调查结果。PHP的维护者主导了修复工作。他们早在2024年就发现了该基础内存溢出问题的迹象，但直到今年8月其全面影响才显现出来。

> “这可以说是范围最广的关键漏洞了。”

OX Security的[Moshe Siman Tov Bustan](https://il.linkedin.com/in/hexploit)在一份声明中表示：“这可以说是范围最广的关键漏洞了。如果你有一个公开可访问的PHP实例且尚未打补丁，请从你已经暴露的假设开始。如果你发现遭受攻击的证据，请假定已被攻陷，而不仅仅是暴露。”

OX Security首席执行官[Neatsun Ziv](https://www.linkedin.com/in/neatsun-ziv-ab7394)补充道：“这就是互联网规模漏洞的真实写照。当漏洞袭击如此普及的技术时，其影响范围就不只是一个产品或一个行业，而是整个互联网。”

在这些警告的背后，[开源领导者](https://thenewstack.io/there-is-just-one-way-to-do-open-source-security-together/)正在探讨当漏洞发现速度超越修复速度时，行业应如何应对。*The New Stack* 此前曾报道过维护者所面临的[海量AI生成漏洞报告](https://thenewstack.io/akrites-ai-vulnerability-reports/)；而PHP的案例则引发了另一场争端：一旦细节开始泄露，保密禁令是否还能真正保护用户。

## 披露争端与对失败的承认

在补丁发布之前，PHP2Shell的细节开始泄露。PHP基金会表示，两个CVE编号在10月20日开始流传，随后是一段不小心发布的攻击验证（PoC）视频。

Chainguard首席执行官兼联合创始人[Dan Lorenc](https://www.linkedin.com/in/danlorenc)随后在10月21日协调发布时间前六个多小时，发布了打过补丁的容器镜像。他表示，他认为有关积极攻击（active exploitation）的报道证明了打破保密禁令的决定是合理的。

速度方面的担忧是真实存在的：在WordPress于9月22日发布7.1.2版本以修复 CVE-2026-87902 后，Patchstack观察到当天就有针对WordPress网站的探测行为，次日便出现了写文件的尝试。

顺便说一句，这已经足够糟糕了。但WordPress的插曲并没有证实，当Chainguard发布其镜像时，攻击者是否成功利用了这些PHP漏洞。

## 为什么Lorenc要打破时间表

在一封致 *The New Stack* 的电子邮件中（随后体现在他的LinkedIn帖子中），Lorenc表示，Chainguard利用其[测试框架](https://thenewstack.io/chainguard-mythos-security-harness/)以及被提示“在PHP中寻找严重漏洞”的前沿AI模型，独立发现了相同的问题。

Lorenc表示，Chainguard于10月16日星期五首次听说将有一个PHP问题出现。他们当晚独立发现了该问题，于10月17日星期六收到了完整的简报，并协助测试了修复方案。

他表示，消息于10月19日星期星期一开始泄露，讨论在周二晚间加剧，当时几个供应商报告了他们认为在野外（in the wild）出现的漏洞利用。

Lorenc写道，在与其他研究人员进行视频通话后，他决定发布修复程序并立即通知披露小组。他认为，当有证据表明野外存在漏洞利用时，协同披露指南允许提前发布。

Lorenc表示，这一决定由三个考量驱动：Chainguard独立发现漏洞并构建攻击载荷的难易程度、关于漏洞和修复方案的流传信息有多少，以及关于积极攻击的共享证据。

Chainguard使其打过补丁的镜像公开可访问，而不是将其限制给客户。Lorenc承认PHP基金会并不同意他的决定。

他们的确无法达成一致。[PHP基金会的说法](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)更加直言不讳：“Chainguard单方面打破了保密禁令，并发布了包含修复程序的构建镜像。”该基金会表示，Chainguard之所以提前收到补丁，是为了让客户能够在商定的披露时间进行更新。

在该基金会看来，发布构建镜像给了攻击者研究修复方案的机会，而其他PHP用户还在等待补丁。

> “我们不可能永远都做对，也不是所有人都赞同我们的决定。”

Lorenc写道，他为自己的决定给PHP维护者增加了压力感到抱歉。“我们不可能永远都做对，也不是所有人都赞同我们的决定，”他补充说，Chainguard的目标是保护最多的人。

## 什么是漏洞利用（Exploit）？

分歧的核心在于什么才算作积极攻击的证据。Lorenc表示，其他供应商已经在野外看到了漏洞利用。而PHP基金会则表示，在其发布时，安全团队尚未在流传的PoC中识别出功能性的漏洞利用。

亚马逊威胁情报（Amazon Threat Intelligence）随后报告称，其某个蜜罐在10月17日遭到了一次明显的漏洞利用尝试，并在10月21日早些时候遭到了更多尝试。尽管如此，该公司表示目前尚不清楚这些尝试在真实系统上是否会成功。

权衡之下的风险是显而易见的。是的，[保持保密禁令](https://thenewstack.io/ai-php2shell-disclosure-framework/)给分发商留出了共同准备更新的时间。没错，提前发布修复程序可以保护那些能够获取它的用户。但这也为攻击者提供了线索，而其他PHP用户仍在等待补丁。

## 潜在的大写“B”级问题

PHP基金会还承认了其应对措施中的另一个失误。开发人员在2024年的一次审计中注意到了某个CVE背后的内存溢出问题的迹象，但当时并未找到通往远程代码执行的具体路径。

该基金会表示，相互竞争的修复方案带来了艰难的兼容性和安全权衡，工作因此一再陷入停滞。它将这一延迟归咎于决策流程和资源缺乏所导致的“结构性失败”。

*The New Stack* 此前曾报道过[付费维护](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/)与安全实践之间的联系。该基金会现在正寻求依赖PHP的公司、托管服务商和政府提供更多支持。

Ubuntu Linux的母公司[Canonical](https://canonical.com/)对整体应对措施给出了相对温和的评估。在电子邮件中，Canonical的安全工程经理[Luci Stanescu](https://ro.linkedin.com/in/lucistanescu)表示：“Canonical支持并建议根据最佳实践进行协同漏洞披露。第三方过早泄露保密禁令是不幸的，但我们相信披露流程运转良好。”

这一评估的侧重点与PHP基金会的批评有所不同：一次泄露可能会削弱流程的一部分，但不一定会使更广泛的协同努力失效。

对于Rocky Linux的发起赞助商CIQ的首席技术官[Peter Nelson](https://www.linkedin.com/in/peter-nelson-774a6)而言，这起PHP插曲契合了Linux安全领域正在发生的一场更广泛的变革。

Nelson表示：“过去六个月里，我们已经看到AI被用于内核空间的漏洞利用。这代表着更多的研究正投入到PHP等其他广泛使用的软件程序中。随着开源项目继续使用AI和其他手段来加固代码并提供更强的防御以抵御此类漏洞，我们预计未来会看到更多这种情况。”

> “今天，此类漏洞利用需要一个前沿模型。明天将不再如此。”

Nelson预计，随着高级漏洞研究能力的普及，这种压力将持续下去。“今天，此类漏洞利用需要一个前沿模型。明天将不再如此。”

Lorenc也将这一挑战视为整个行业的问题，而非局限于PHP的问题。“不幸的是，这是该行业的新常态，我们需要像一个团队一样紧密合作，才有机会足够快地保护我们的关键基础设施，从而阻止攻击者造成真正的损害。”

## 打补丁不能等待常规的维护窗口。

对于企业用户而言，直接后果是运营层面的。红帽（Red Hat）Lightwell项目的副总裁兼总经理[Gunnar Hellekson](https://www.linkedin.com/in/gunnarhellekson)（该项目是红帽与IBM联合解决易受攻击的[开源依赖项](https://thenewstack.io/aikido-acquires-root-security/)的举措）在电子邮件中告诉 *The New Stack*，PHP漏洞说明了组织可能很少考虑的可靠软件中所蕴含的风险。

Hellekson表示，即便在AI驱动的发现增加了漏洞发现的数量和速度之际，稳定的生产软件也容易被忽视。他说，PHP的问题提醒我们，开源技术已经多么深地融入到了运行业务的系统中。

他强调要从受信供应商那里获取经过测试的更新，特别是当漏洞影响到PHP等至关重要的程序时。“鉴于这些漏洞的潜在影响，红帽建议客户一从红帽等受信任来源获取到经过验证、测试的补丁，就立即部署它们，甚至可以在常规补丁窗口之外进行。”

> “支撑数百万个网站的软件，不能仅仅依靠少数维护者来独自应对日益复杂的威胁。”

除此之外，我们总体上需要为[开源软件维护](https://thenewstack.io/security-needs-create-more-work-for-open-source-maintainers/)和安全投入更多资源。正如[HackerOne](https://www.hackerone.com/)首席执行官[Kara Sprague](https://www.linkedin.com/in/ksprague08)在发给媒体的声明中所言：“PHP的发现也提醒我们，开源安全是每个人的责任。支撑数百万个网站的软件，不能仅仅依靠少数维护者来独自应对日益复杂的威胁。”

不，确实不能。

对于运行受影响PHP系统的组织来说，“立即打补丁！”的问题依然存在：部署修复后的构建版本，并审查系统是否存在攻击尝试的迹象，包括可追溯到10月17日的活动。

这正是各种互补评估交汇的地方。资金更充足的维护者、更具弹性的披露程序以及更广泛地获取防御工具，可以解决长远的问题。这正是本周补丁背后的资本级“B”问题。