<!--
title: 自由软件基金会如何对抗LLM机器人
cover: https://cdn.thenewstack.io/media/2025/07/71053e97-sculpture-outside-san-franciscos-metreon-photo-by-david-cassel-1024x768-2.jpg
summary: 自由软件基金会（FSF）的基础设施自2024年8月以来持续遭受攻击，包括DDoS和LLM爬虫。FSF仅有少量技术人员和志愿者维护70多个站点，面临巨大挑战。攻击目标包括gnu.org、savannah.gnu.org等。FSF通过防火墙、fail2ban等工具进行防御，并呼吁互联网服务提供商采取行动。他们也欢迎志愿者和会员的支持。
-->

自由软件基金会（FSF）的基础设施自2024年8月以来持续遭受攻击，包括DDoS和LLM爬虫。FSF仅有少量技术人员和志愿者维护70多个站点，面临巨大挑战。攻击目标包括gnu.org、savannah.gnu.org等。FSF通过防火墙、fail2ban等工具进行防御，并呼吁互联网服务提供商采取行动。他们也欢迎志愿者和会员的支持。

> 译自：[How the Free Software Foundation Battles the LLM Bots](https://thenewstack.io/how-the-free-software-foundation-battles-the-llm-bots/)
> 
> 作者：David Cassel

系统管理员 [Ian Kelling](https://www.fsf.org/about/staff-and-board#iank) 在 7 月 2 日发表的[一篇博文](https://www.fsf.org/blogs/sysadmin/our-small-team-vs-millions-of-bots)中指出，自由软件基金会的基础设施“自 2024 年 8 月以来一直受到攻击”。

自由软件基金会系统管理员 [Michael McMahon](https://www.fsf.org/about/staff-and-board#michael) 周二告诉 The New Stack：“自文章发表以来，没有任何改变，我们仍在处理所有这些问题。”

该组织只有两名全职技术团队员工和少数“敬业的志愿者”来处理这个问题。

自由软件基金会 7 月份的帖子链接到 [LibreNews 的一份报告](https://thelibre.news/foss-infrastructure-is-under-attack-by-ai-companies/)，其中指出包括 Fedora 项目、KDE GitLab 基础设施、GNOME GitLab 实例、Diaspora 甚至 FOSS 新闻网站 Linux Weekly News 在内的高知名度 FOSS 站点也面临类似的问题。（并且 “[GNOME](https://thenewstack.io/what-makes-gnome-so-appealing/) 自去年 11 月以来一直遇到问题……”）

McMahon 周二表示，像自由软件基金会的文章一样，是一种分享“技术和工具”的方式。但他补充说，一些系统管理员也有一个私人邮件列表，“我们可以在其中协调和分享有效的策略。具体的缓解措施通常无法公布，因为这会给我们的攻击者带来优势。”

从自由软件基金会与机器人的斗争中可以学到很多东西——关于系统管理员的策略，也关于他们今天面临的来自那些“极具攻击性的 LLM 爬虫”的新挑战？正如自由软件基金会在其博文中写道……“看来网络的健康现在存在一些严重的问题。”

## 维护 70 个站点

这比看起来更具挑战性。自由软件基金会技术团队维护着 70 多个不同的网站、服务和平台——不仅为自由软件基金会和 GNU 项目，也为“更广泛的自由软件社区”（包括流行的 Web 框架，如 [Drupal](https://www.fsf.org/working-together/gang/drupal) 和 [MediaWiki](https://directory.fsf.org/wiki/MediaWiki)、[KDE 桌面环境和软件合集](https://directory.fsf.org/wiki/Kde)，甚至经典游戏 [NetHack](https://directory.fsf.org/wiki/Nethack)）。Kelling 写道：“我们最近统计了 70 种不同的服务，并在波士顿地区的两个数据中心拥有十几个物理服务器。”

然而，“我们不使用任何所谓的‘云’服务，”[另一个网页解释说](https://www.fsf.org/blogs/sysadmin/join-the-fsf-and-support-the-tech-team)，“因为他们通常指的‘云’[只是别人的电脑](https://www.gnu.org/philosophy/who-does-that-server-really-serve.html)。我们不会抽象掉 Docker 容器之上框架的问题，这些容器在 Kubernetes 中运行，由某人组装，他们告诉你直接将 curl 输出通过管道传输到 bash 中，并在不查看的情况下以 root 身份安装软件……”

该帖子解释说，自由软件基金会对其堆栈持有更高的标准，“我们以一种我们可以理解和跟踪的方式组装我们的软件堆栈，通过配置由 [Ansible](https://thenewstack.io/red-hat-ansible-and-hashicorp-terraform-will-be-coming-together/) 在带有 libvirt 的虚拟机中协调的服务，这些虚拟机运行在 Trisquel GNU/Linux 上，Trisquel GNU/Linux 运行在我们拥有、运营和信任的裸机 ASUS KGPE-D16 服务器上……“我们尽可能地自托管一切，以便我们使用的软件可以被信任……”

管理团队甚至验证他们的软件是否运行任何非自由依赖项。“我们只运行我们可以运行、修改、复制和共享的代码，甚至在我们的服务器上运行完全自由的 BIOS。”

## 击退持续的攻击

7 月份的博文解释说，维护所有这些站点是一项“巨大的任务”——尤其是在面对那些具有攻击性的 LLM Web 爬虫时，“这些爬虫一直是攻击的重要来源”。

McMahon 周二解释说：“这些可能是 LLM 公司的行为，它们没有留下联系方式，因此除了 IP 地址的所有者之外，没有可以报告的单个公司。”

因此，与其他站点一样，他们的第一道防线是“识别哪些 IP 地址正在发送请求作为 [[分布式拒绝服务](https://thenewstack.io/how-a-popular-combo-provides-ddos-protection/)] 的一部分，然后让服务器忽略来自这些 IP 地址的请求，”该博文解释说。

但这并不像听起来那么简单。去年 12 月，[一篇博文](https://www.fsf.org/bulletin/2024/fall/fsf-sysops-cleaning-up-the-internet) 回忆说，“过去几个月的一次攻击需要阻止来自 DDoS 攻击的 40,000 多个 IP 地址。”本月，Kelling 写道：“该攻击仍在继续，但我们已经缓解了它。”（尽管在这种情况下，“从模式和范围来看，目标很可能是让网站瘫痪，而不是 LLM 爬虫。”）

坏消息是？“从那时起，我们遭受了更多严重程度更高的攻击。”并且有来自各种来源的多次攻击……

* “GNU Savannah，自由软件基金会的协作软件开发系统，[从 1 月份开始受到控制大约 500 万个 IP 的大型僵尸网络的攻击](https://www.fsf.org/bulletin/2025/spring/defending-savannah-from-ddos-attacks)。” 7 月 2 日，它“仍在进行中，但僵尸网络的当前迭代已得到缓解。”管理团队推测其目的是构建 LLM 训练数据集。
* gnu.org 和 ftp.gnu.org 从 5 月 27 日开始遭受新的 DDoS 攻击。（目前也已得到缓解，“其目标似乎是让网站瘫痪……它已经进行了多次迭代，每次迭代都导致了几个小时的停机时间，因为我们需要弄清楚如何保护自己……”）
* Free Software Directory 背后的服务器 directory.fsf.org 在 6 月 18 日受到攻击。两周后，该攻击仍然“非常活跃”，但“部分缓解”。他们认为该攻击“很可能是一个旨在专门针对带有僵尸网络的 Media Wiki 站点的 LLM 抓取器。”
* 还有来自漏洞扫描器和 Web 爬虫的通常的高影响流量，以及伪装成常规用户的爬虫——或其他爬虫。

“我们必须为每次攻击找到具体的防御方法……”该博文解释说。

还有另一种问题。[自动化 CI/CD 管道](https://thenewstack.io/ci-cd/)“通常会发送比必要的更多的请求，这看起来和行为都像 DDoS 攻击，即使它不是有意的”。一个例子是检查——并重新检查——软件重建的可能的新代码更新。McMahon 周二表示，“他们往往不提供联系方式。我们联系他们的方法是向 IP 地址的所有者发送滥用报告，或者运行‘尖叫测试’，即我们阻止该地址并查看他们是否抱怨。

“尖叫测试通常是有效的，并导致关于更好地利用我们资源的建设性对话。”

但该博文指出，地址阻止并不总是有效，而是“经常促使他们寻找更好的方法来实现相同的目标。”

## 反击

首先，像 [Prometheus](https://thenewstack.io/creating-a-path-for-prometheus-success/) 和 [Uptime Kuma](https://uptime.kuma.pet/) 这样的自由软件监控工具会提醒他们注意中断或响应时间变慢，并且“受影响服务的日志通常会讲述一个故事”。（可疑的请求包括在甚至没有使用 WordPress 的站点上搜索特定于 WordPress 的页面或每秒发出多个页面请求等——并且它们使用名为 IPtoASN 的工具根据 IP 地址前缀 ASN 表进行交叉检查）。

然后使用“各种防火墙”阻止地址，并且还使用 [fail2ban](https://github.com/fail2ban/fail2ban) 的工具进行基于行为的阻止，并使用 [Modsecurity](https://modsecurity.org/) 进行基于代理的规则。有时他们甚至会向 ISP 和托管公司发送滥用报告（尽管“该页面可能使用非自由 JavaScript。在这些情况下，我们通常可以通过发送一封电子邮件，其中包含对滥用的描述、日志片段和预期行为来避免使用非自由 JavaScript……”）

这是长期战略的一部分。McMahon 周二表示：“希望互联网服务提供商、云提供商和移动运营商将开始注意到来自其网络的滥用行为，并通过解决更大问题的根源来帮助我们。”

但与此同时，根据该博文，自由软件基金会防火墙可以阻止大多数漏洞扫描器，并且“我们可能需要阻止单个地址、CIDR 地址、VPS 提供商，甚至整个 ASN。”

## 一个更大的问题

自由软件基金会发现其站点面临着“忽略 robots.txt 文件、扫描速度过快并导致站点瘫痪”的网站爬虫——并且在这里，该博文“特别”点名了那些“由大型语言模型公司编写的”爬虫。

根据 [SourceHut 的 CEO/创始人 Drew DeVault 在 3 月份发表的一篇博文](https://drewdevault.com/2025/03/17/2025-03-17-Stop-externalizing-your-costs-on-me.html) 判断，这些爬虫对其他站点来说也是一个问题。DeVault 表示，这些极具攻击性的 LLM 爬虫“使用与最终用户重叠的随机 User-Agents，并且来自数万个 IP 地址——主要是住宅 IP，位于不相关的子网中，每个 IP 在我们尝试测量的任何时间段内发出的 HTTP 请求都不超过一个——积极地、恶意地适应并融入最终用户的流量，并避免尝试描述其行为或阻止其流量。”

DeVault 写道，这正在造成损失。“我们每周都会经历数十次短暂的中断，并且我必须每天多次审查我们的缓解措施，以防止这个数字变得更高……SourceHut 的几项高优先级任务已经被推迟了数周甚至数月，因为我们不断被打断来处理这些机器人，并且许多用户受到了负面影响，因为我们的缓解措施不能总是可靠地区分用户和机器人。我的所有系统管理员朋友都面临着同样的问题。”

一些网站使用 [Anubis](https://github.com/TecharoHQ/anubis)，它会发送一个 JavaScript 程序，要求在允许访问网站之前进行计算。但是，尽管它符合自由软件基金会对自由软件的定义，“我们不支持这种方案，因为它与软件自由的原则相冲突……一个执行用户不希望完成的计算的程序是一种恶意软件，”DeVault 说。

该博文以充满希望的语气结尾。“即使我们正在遭受积极的攻击，gnu.org、ftp.gnu.org 和 savannah.gnu.org 目前也已启动，响应时间正常，并且本周大部分时间都是如此……我们已经保护这些站点免受近一年的猛烈攻击，只要这些攻击继续，我们将继续与之抗争。”

当然，随时欢迎志愿者帮助他们继续完成这项任务。McMahon 周二表示，有一个专门的页面建议 [多种帮助方式](https://libreplanet.org/wiki/Group:FSF:Tech_Team_Volunteers)，“我们会持续招募新的志愿者。”

但即使你不是系统管理员，他们 [在 12 月份指出](https://www.fsf.org/bulletin/2024/fall/fsf-sysops-cleaning-up-the-internet)，“用行动长期支持自由软件基金会系统运维团队和整个自由软件基金会的最好方式是成为自由软件基金会的会员。”