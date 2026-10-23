网络上遭遇的最大规模安全威胁之一正在引发广泛混乱，促使企业、医院、学校和政府机构[临时关闭](https://www.reuters.com/technology/websites-taken-offline-over-php-risks-2026-10-21/)网站和在线服务，因为他们争相防范[PHP](https://www.php.net/)（支撑了互联网大半壁江山的[编程语言](https://thenewstack.io/php-performance-operational-planning/)）中的两个严重漏洞。

这些漏洞被统称为[PHP2Shell](https://www.php2shell.com/)，可能会允许未经验证的攻击者在受影响的服务器上执行恶意代码。各大科技公司一直在竞相保护用户，[Cloudflare部署了](https://blog.cloudflare.com/php-vulnerabilities-waf-protection?utm_source=chatgpt.com)防火墙保护，[Automattic确认](https://automattic.com/2026/10/21/php2shell/)其平台（包括WordPress.com、WordPress VIP和Tumblr）托管的网站已得到安全保护。与此同时，维基媒体基金会[将几个支撑服务离线](https://diff.wikimedia.org/2026/10/21/impact-of-php-vulnerabilities-on-wikimedia-tools-and-services/?utm_source=chatgpt.com)，直到它们打上补丁。

周三，PHP项目为8.2到8.5版本[发布了](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)紧急修复程序。旧版本不再获得官方支持，尽管一些发行版和供应商提供了遗留修复程序，并且PHP已为7.4到8.1版本发布了有限的补丁。

然而，尽管PHP漏洞本身是一件大事，但其发现、修补和披露的过程却让我们得以一窥开源社区正面临的日益严峻的压力——随着AI让发现严重安全缺陷变得更加容易。

## “在PHP中寻找严重的漏洞”：提示词发现

有关即将发布补丁的消息于[周二浮出水面](https://www.php.net/archive/2026.php#2026-10-20-1)，此前详细信息在预定披露前夕遭到泄露。次日，[OpenAI透露](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/)，安全公司[Calif](https://calif.io/)使用其[GPT-5.6 Sol模型](https://thenewstack.io/gpt-sol-chatgpt-split/)发现了其中一个缺陷，而[谷歌旗下的Wiz](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/wiz-acquisition/)则独立识别出了这两个漏洞。OpenAI表示，作为其[“保卫地球”计划](https://openai.com/index/patch-the-planet/)的一部分，该公司花了两个月时间协调各方响应，包括PHP维护者、安全研究人员、Cloudflare以及政府网络安全机构。

然而，当软件供应链安全公司[Chainguard](https://www.chainguard.dev/)在约定时间前六个多小时发布了打好补丁的PHP容器镜像时，这一努力被打乱了。首席执行官[Dan Lorenc](https://www.linkedin.com/in/danlorenc/)[在LinkedIn上](https://www.linkedin.com/posts/danlorenc_i-wanted-to-share-what-happened-with-the-share-7518756991520120832-QX2_/)承认是他做出了这个决定，并指出Chainguard使用前沿AI模型和简单的提示词“*find bad vulnerabilities in PHP*”（在PHP中寻找严重的漏洞），独立重新发现了这个缺陷。

Lorenc为这一决定进行了辩护，他指出了有关攻击的报道以及复现该漏洞的简易性。而PHP Foundation则认为，在其他供应商仍在准备补丁的同时，提前发布可能会帮助攻击者。

PHP Foundation[指出](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)：“这无视了多方为实现协调披露而付出的数周工作。”

PHP Foundation董事会成员兼[Composer](https://getcomposer.org/)的创建者和共同维护者[Nils Adermann](https://www.linkedin.com/in/nilsadermann/)表示，“没有确认的攻击行为，”并补充说任何已识别的活动都只是人们尝试攻击的行为。

> “你在没有与PHP团队进行任何沟通的情况下单方面做出的决定，既不负责任又极不专业。”

Adermann在回应Lorenc的帖子时[写道](https://lnkd.in/p/eB5nTM2J)：“在披露和公开发布之前有一个明确的禁令期，随着信息的到来，这一禁令期经过了反复讨论和评估，权衡了利用漏洞的风险与在没有完整更新的情况下发布补丁的保护作用。你在没有与PHP团队进行任何沟通的情况下单方面做出的决定，既不负责任又极不专业。这里正确做法是道歉，而不是为你明显的错误行为辩护。”

## 新常态

然而，PHP的混乱凸显了一个更大的担忧：AI正在让发现安全漏洞变得更加容易，而负责修复这些漏洞的人员却无法做出足够快的响应。正如Lorenc本人所说：“不幸的是，这是该行业的新常态。”

就在OpenAI披露的前一天，Anthropic[发布了一项研究](https://www.anthropic.com/research/attack-surface-reduction)，表明Claude在包含500多万行代码的25个开源项目中识别出了493个安全问题。其中一个配置缺陷在21年里一直未被发现，它有可能禁用身份验证要求，允许未经授权的客户端访问理应受限制的服务器。

虽然Anthropic发现的并非全部都是可被利用的漏洞，但它们凸显了一个日益严重的问题：AI可以大规模发现安全弱点，但评估这些弱点并开发出可靠的修复方案仍然需要时间和专业知识。

[Akrites](https://thenewstack.io/akrites-ai-vulnerability-reports/)的CTO兼开源安全基金会（[OpenSSF](https://openssf.org/)）CTO兼首席安全架构师[Christopher Robinson](https://www.linkedin.com/in/darthcrob/)表示，PHP的紧急事件也提醒人们，当严重的漏洞*确实*出现时，做好响应准备是多么重要。

> “尽量减少像PHP2Shell这类事件影响的最佳方法，就是为这些事情的发生做好准备和规划。”

Robinson告诉 *The New Stack*：“尽量减少像 *PHP2Shell* 这类事件影响的最佳方法，就是为这些事情的发生做好准备和规划。拥有漏洞管理流程并了解在问题变得过于复杂时谁能提供帮助，是开源项目和商业实体都能做出的最佳举措。”

## 当寻找漏洞变得比修复漏洞更容易时

对于拥有超过[32,000个GitHub Star](https://github.com/atuinsh/atuin)的开源开发者工具[Atuin](https://atuin.sh/)的软件工程师兼CTO [Michelle Tilley](https://www.linkedin.com/in/michellektilley/)来说，为PHP实施的那种应急响应很难在较小的开源项目中复制。

Tilley告诉 *The New Stack*：“这里的响应看起来像是一个厂商紧急事件，有联盟、政府机构以及[WAF](https://en.wikipedia.org/wiki/Web_application_firewall)（Web应用防火墙）规则。这对于PHP这样的项目很有效，但没有人会为了一个鲜为人知的、由3名维护者组成、却在世界各地软件中被使用的库去组建一个联盟。”

> “这对于PHP这样的项目很有效，但没有人会为了一个鲜为人知的、由3名维护者组成、却在世界各地软件中被使用的库去组建一个联盟。”

Tilley说，Atuin本身就已经收到了越来越多的AI生成的漏洞报告和拉取请求（Pull Requests）。虽然她的公司有足够的工程资源来处理这些问题，但许多较小的项目依赖于利用业余时间工作的无报酬维护者，他们可能会不堪重负并选择离开。

Tilley继续说道：“这些开发者可能会、也确实会倦怠。有时他们会安排其他人接管该项目；通常情况下，他们只是停止维护，而下游用户永远不会知道。这就是为什么项目最终会出现永远不会被修补的漏洞。”

归根结底，她希望将更多的责任推给研究人员和依赖该代码的企业。

Tilley说：“没有单一的修复方案，但方向很明确。修复的成本必须转移到发现漏洞的人以及依赖该代码的公司身上。”

这种压力也延伸到了更大的项目上。AWS首席工程师兼[Valkey](https://thenewstack.io/valkey-proxy-redis-percona/)数据库维护者[Madelyn Olson](https://www.linkedin.com/in/madelyn-olson-valkey/)表示，该项目今年发现和修复的安全漏洞也比以往多得多。

Olson告诉 *The New Stack*：“最困难的部分已经从发现漏洞转变为了修复漏洞。PHP就是一个很好的例子。”

本周其中一个漏洞背后的根本问题，最初是一名PHP开发人员在修复由开源技术改进基金会（[OSTIF](https://ostif.org/)）组织的[2024年安全审计](https://ostif.org/php-audit-complete/)期间发现的问题时识别出来的。然而，解决该问题的尝试陷入了停顿，因为提出的修复方案有可能破坏兼容性、影响性能或扰乱第三方扩展。[据PHP Foundation称](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)，很少有工程师具备解决这些权衡取舍的专业知识。

Olson说：“AI在寻找漏洞方面变得非常厉害。但做出正确的修复仍然需要经验丰富的维护者，这正是来自公司的支持最重要的地方。”

> “AI在寻找漏洞方面变得非常厉害。但做出正确的修复仍然需要经验丰富的维护者，这正是来自公司的支持最重要的地方。”

为了应对涌入的问题，[Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/ "Valkey")正在缩小其安全漏洞的定义范围，使用AI来检查自己的代码，并让反向移植（Backporting）和发布变得更容易。

Chainguard的这场风波也引发了一个问题：披露时间表是否需要改变。Olson回忆说，有三名研究人员在一周内各自使用LLM独立报告了同一个Valkey漏洞。Valkey目前正朝着缩短禁令期的方向努力——尽管这与打破商定的发布日期是两码事。

Olson说：“如果你用LLM发现了漏洞，可以说别人也能发现。这就支持了缩短禁令期和更快发布的观点，Valkey现在正朝着缩短禁令期的方向努力，这是我们在大多数大型项目中看到的趋势。”

## 不断增长的安全积压

OSTIF执行董事[Derek Zimmer](https://www.linkedin.com/in/derek-zimmer-2164a441/)表示，合法发现和低质量报告的数量都在造成积压，维护者不得不花费本就稀缺的工程时间来确定哪些问题是真实的。

> “维护者正淹没在来自公众的漏洞报告海洋中，其中既有垃圾报告，也有不花大量时间进行分类就几乎无法区分的合法报告。”

Zimmer告诉 *The New Stack*：“2026年的现实是，发现严重漏洞比以往任何时候都容易，维护者正淹没在来自公众的漏洞报告海洋中，其中既有垃圾报告，也有不花大量时间进行分类就几乎无法区分的合法报告。”

为了提供帮助，OSTIF正在试行诸如[项目 V-LAT](https://ostif.org/security-engineer-in-residence-program/)等计划，该计划将工程师嵌入到项目中以审查调查结果并开发修复程序，同时帮助维护者改进报告的处理方式。

Robinson还强调了共享安全专业知识以及能够支持上游项目的专职工程师的必要性。他反驳了“暴露更多缺陷必然会使开源变得更不安全”的说法，并指出依赖该代码的公司有机会贡献修复方案。然而，许多项目既没有资金也没有专业知识来独立应对。

Robinson说：“大多数上游维护者同时也是项目中的志愿者，几乎没有甚至没有预算、基础设施或支持工具。这里不会有‘一刀切’的方法，我们需要采用多种并行的方法，以获得最广泛的成功结果的机会。”