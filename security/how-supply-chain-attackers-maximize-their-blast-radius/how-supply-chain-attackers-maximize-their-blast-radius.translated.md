# 供应链攻击者如何最大化其攻击范围

![供应链攻击者如何最大化其攻击范围的特色图片](https://cdn.thenewstack.io/media/2025/01/4b6a195d-supplychainattackersmaximizeblastradius-1024x576.jpg)

现代软件开发严重依赖开源软件包。npm、PyPI 和 GitHub 等平台共同托管数百万个软件包，每月促成数十亿次下载。

虽然开源软件 (OSS) 的互联互通、协作性质促进了创新，但也[使生态系统面临恶意活动](https://thenewstack.io/what-developers-can-grok-from-the-latest-pypi-package-attack/)。攻击者越来越多地利用这些可信的供应链传播恶意软件，包括加密矿工、信息窃取者和后门。[Sonatype](https://www.sonatype.com/?utm_content=inline+mention) 的 2024 年报告强调[恶意软件包增加了 156%](https://www.sonatype.com/state-of-the-software-supply-chain/introduction)，与去年相比，这预示着对软件供应链日益增长的紧迫威胁。

## 最小障碍，最大风险

发布开源软件包的简易性无意中创造了一个环境，该环境的进入门槛低，但对各级恶意行为者来说却有可观的回报。只需付出最小的努力，对手就能使用一次性身份生成和分发大量恶意软件包，从而使追踪和缓解工作变得复杂。

在威胁环境的高端，民族国家行为者，特别是那些[与朝鲜政府有关联的](https://www.darkreading.com/application-security/japan-blames-north-korea-for-pypi-supply-chain-cyberattack)行为者，逐渐转向 npm 和 PyPI 软件包。他们将这些平台用作旨在渗透组织和窃取加密货币的活动的一部分。

这些威胁迫使软件包注册表和安全研究人员陷入被动应付的“打地鼠”场景，在长时间未被发现的活动之后，才识别和清除这些威胁。

## 扩展攻击面

现代开发对相互关联的依赖链的依赖放大了单个受损软件包的潜在影响。虽然一个项目可能只有少数直接依赖项，但在 npm 中，传递依赖项通常每个软件包超过 1000 个。

基于 AI 的代码生成工具的使用激增加剧了这些风险。代码生成模型“[产生幻觉”]几乎 20% 的生成的软件包](https://arxiv.org/abs/2406.10279v1)，暗示不存在甚至恶意库。随着开发人员采用大型语言模型 (LLM) 工具来加快开发速度，供应链受损的可能性也在增加。

## 开源软件供应链攻击的主要类别

开源软件包生态系统攻击可分为两大类：劫持可信软件包和模仿可信软件包。

### 被劫持的软件包

旨在最大化其攻击范围的攻击者可能会试图劫持一个高知名度的软件包，该软件包被许多应用程序或开发人员使用。这些攻击的有效性取决于项目的现有用户群和声誉。与一次性恶意软件包不同，这些事件往往更复杂，因此更难以检测和预防。

但是，由于流行的软件包自然会受到更大的审查，因此许多开源软件供应链攻击由于社区的警惕而被发现。

为了执行软件包劫持攻击，攻击者通常需要拥有目标项目的维护者或所有者权限。他们通过帐户泄露或在社区中逐渐建立声誉来获得访问权限。

#### 维护者接管

威胁行为者可以通过多种方式破坏维护者帐户——弱密码、有针对性的网络钓鱼攻击、窃取会话 Cookie 或 API 令牌或注册已过期的电子邮件域名。攻击者也可能会抓住机会控制被放弃的项目。

项目所有者可以通过加强维护者和贡献者的身份验证和安全机制来减轻此类攻击。像[Sigstore](https://thenewstack.io/need-to-sign-your-code-and-havent-a-clue-sigstore-can-help/)这样的工具使维护者能够对工件进行密码签名并提供来源证明。

#### 恶意的新的贡献者

复杂的攻击者可能不会破坏现有的维护者，而是选择通过耐心建立信任和声誉（自然地或其他方式）来渗透项目，然后请求更高的权限。

自然的信任建立涉及“[缓慢的社会工程]”，这可能需要数月甚至数年时间。(https://thenewstack.io/the-xz-hack-reveals-a-looming-8-8-trillion-infrastructure-disaster-hidden-in-plain-sight/)此类活动将近似于开源开发中的正常模式，因此很难将其与良性贡献区分开来。
一些人会试图通过使用“[傀儡账号](https://en.wikipedia.org/wiki/Sock_puppet_account)”来提高可信度，或者通过购买GitHub上的星标和关注者来操纵指标。这些策略将信任建立过程游戏化，制造虚假的合法性来支持他们作为维护者的说法。

一旦攻击者获得项目访问权限，他们就需要触发其有效负载的执行，以将其传播到所有下游用户。最明显的方法是提交一些恶意代码，可能跨多个文件和阶段，以避免被其他贡献者和用户检测到。

另一种选择是利用CI/CD管道。例如，最近的[Ultralytics PyPI 泄露事件](https://blog.pypi.org/posts/2024-12-11-ultralytics-attack-analysis/)就依赖于GitHub Actions缓存中毒。

团队应该严格审查所有拉取请求并监控CI/CD流程。诸如[Minder](https://thenewstack.io/stacklok-donates-minder-security-project-to-openssf/)和[Stacklok Insight](https://thenewstack.io/codegate-open-source-tool-secures-ai-coding-assistants/)之类的工具可以识别可疑的代码添加、已弃用的依赖项或异常模式。

### 模仿软件包
大多数威胁参与者会采取更简单的方法，即创建模仿合法软件包的伪造软件包，而不是试图直接劫持原始软件包。此类攻击（包括错字劫持和星标劫持）依赖于欺骗用户信任并下载其软件包。通过这种方法，攻击者可以完全控制软件包的交付、源代码和外观的所有方面。

这种方法不仅简化了执行，而且使此类攻击更容易检测。但是，它们的范围通常有限——一些攻击者为了避免广泛的审查而故意选择这样做。

#### 错字劫持
错字劫持长期以来一直是恶意软件和垃圾邮件活动中的一种常用技术。攻击者注册域名时略微拼写错误或替换字符，以诱骗用户访问恶意网站。例如，一个欺诈性的[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 登录页面可能会使用类似 microsoft-auth.xyz/login 的域名。

同样的策略也适用于软件包；攻击者会选择与合法软件包几乎相同的名称，使用轻微的错字、额外的标记或字符替换。例如，他们可能会使用[eth-gasreportr](https://www.insight.stacklok.com/report/npm/eth-gasreportr)而不是[eth-gas-reporter](https://www.insight.stacklok.com/report/npm/eth-gas-reporter)。

#### 星标劫持
星标劫持通常伴随着错字劫持。由于大多数软件包注册表允许未经验证的用户声明存储库链接，因此攻击者可以劫持高信誉软件包的流行度统计数据。在恶意软件包上显示合法软件包的星标计数和贡献者列表，使其获得不应有的可信度。

![一个“星标劫持”的软件包——唯一的区别是主标题拼写错误为“eth-gasreportr”，而不是eth-gas-reporter](https://cdn.thenewstack.io/media/2025/01/5c8f6c64-eth-gasreportr-typosquat-1024x742.png)
一个“星标劫持”的软件包使用错字劫持伪装成合法网站。

![一个合法的存储库](https://cdn.thenewstack.io/media/2025/01/b42a280a-eth-gas-reporter-legit-1024x744.png)
eth-gas-reporter 的合法存储库

团队应该避免仅仅依靠显示的流行度指标来建立信任，因为这些指标并非可靠的合法性指标。经过验证的软件包来源可以保证软件包代码源自其声称链接到的存储库。

## 结论
从针对性维护者接管到欺骗性软件包模仿，这些恶意策略说明了开源生态系统中固有的漏洞。

虽然这些方法是最常见的方法，但它们只代表了不断发展的威胁环境中的一小部分。

新的攻击媒介，例如利用AI生成的代码或利用CI/CD管道中的新漏洞，仍在不断出现。解决这些挑战需要持续的警惕、[安全工具的创新](https://thenewstack.io/stacklok-builds-on-sigstore-to-identify-safe-open-source-libraries/)以及开源社区的集体努力来[保护软件供应链](https://thenewstack.io/who-should-be-responsible-for-software-security/)。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)