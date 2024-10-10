# 避免地缘政治开源末日

开源社区的分裂是否正在逼近？我最近参加了[CNCF: KubeCon + CloudNativeCon 中国香港峰会](https://events.linuxfoundation.org/kubecon-cloudnativecon-open-source-summit-ai-dev-china/)，中国演讲者和演讲占据主导地位。这在香港是意料之中的，但也许最令人启发的是，中国正在开发的全新开源项目数量。

近年来，中国已成为开源世界越来越重要的中心。中国公司在[OpenInfra](https://openinfra.dev/members/)和[CNCF](https://www.cncf.io/about/members/)等主要开源基金会中也占有重要地位。我们是否正在目睹开源世界潜在的未来裂痕？是否会出现一个东部和一个西部生态系统，它们只偶尔接触？或者我们能否为了共同利益克服分歧？

中国进军开源领域可能始于 1999 年红旗 Linux 的出现，但此后，中国出现了大量新的开源项目。中国开发者在这些项目中占据主导地位，但他们寻求获得验证和建立信任，通常通过加入开源基金会。

根据 TechTarget (APAC) 最近的一篇文章[中国开源的兴起](https://www.computerweekly.com/news/366608127/The-rise-and-rise-of-open-source-in-China)，作者[Aaron Tan](https://www.techtarget.com/contributor/Aaron-Tan?_gl=1*eww77p*_ga*OTk1MTI2NDY1LjE3MjQzMTkxNzk.*_ga_TQKE4GS5P9*MTcyNDMxOTE3OC4xLjEuMTcyNDMxOTM4MC4wLjAuMA..)，“根据 GitHub 副总裁 Stormy Peters 在活动上的主题演讲，中国在 GitHub 上的开发者数量位居全球第二。”中国现在也占基金会赞助的 10% 以上。经[Stormy Peters](https://www.linkedin.com/in/stormy) 许可，我将从她的主题演讲中包含一张幻灯片来说明这些要点：

## 西方会采用中国软件吗？

我认为这一切都不应该让人感到意外。与大多数国家一样，中国希望掌握自己的命运，因此创建了自己的 Linux 发行版，并推动了本土开源项目的蓬勃发展。这对开源世界来说似乎是件好事。

当然，你不能责怪中国想要成为开源领域的领头羊。西方长期主导着开源领域，中国公司使用主要由中国开发者编写的软件也就不足为奇了。

但问题就在这里：鉴于当前的地缘政治环境，西方公司是否愿意采用相同的软件？很难想象一家大型美国金融机构会从[RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux)迁移到[Open Euler](https://www.openeuler.org/en/)或[OpenKylin](https://www.openkylin.top/index-en.html)。我们已经看到西方国家在一定程度上排挤华为等硬件公司。

感觉只是时间问题，就会出现越来越大的压力，要求使用[主要由西方开发者开发的开源软件](https://thenewstack.io/osis-definition-of-open-source-ai-raises-critical-legal-concerns-for-developers-and-businesses/)。与此同时，中国机构可能会更青睐本土开源项目，而不是那些起源于西方并由西方主导的项目。

在上面提到的 CNCF 活动中，我的同事建议与一个主要在中国开发的开源数据库即服务 (DBaaS) 项目合作。当我考虑我们投资组合中的客户类型时，我意识到这对于大型金融机构、政府实体、电信公司等来说将很难推销。

当我查看这家 DBaaS 公司网站上的客户列表时，他们列出的所有客户都是中国客户。风险敏感的西方公司采用在东方编写并在东方主要使用的开源软件，这很难推销。也许会有人担心其他国家，但这似乎不太可能成为问题，因为这些国家没有生产那么多开源软件，而且它们也不像中国和俄罗斯那样被视为国家安全风险。
有些人认为开源软件通常更安全，但事实并非如此。主要由西方国家开发的开源软件本身也存在着有据可查的安全问题，部分原因是它严重依赖于工作过度和志愿者维护人员。[保护开源软件](https://thenewstack.io/inside-a-150-million-plan-for-open-source-software-security/)需要时间、精力和勤奋。不幸的是，许多项目资源非常有限，缺乏[所需的](https://thenewstack.io/verification-scans-or-automated-security-requirements-which-comes-first/) [寻找安全](https://thenewstack.io/verification-scans-or-automated-security-requirements-which-comes-first/)风险的专业知识。

更重要的是，没有开源软件是孤立存在的。相反，任何给定的开源软件都有一条很长的依赖关系“供应链”，因此出现了[SBOM](https://security.cms.gov/learn/software-bill-materials-sbom)（软件物料清单）来验证在采用给定软件时包含了哪些其他代码。但是，这并不能保证安全性。

最近，一个很可能是国家支持的行为者[通过攻击其软件供应链，将后门植入 OpenSSH](https://lcamtuf.substack.com/p/technologist-vs-spy-the-xz-backdoor)。该[漏洞](https://www.openwall.com/lists/oss-security/2024/03/29/4)被插入到一些 Linux 发行版的依赖项中，它被缓慢地引入，然后被故意游说纳入不同的发行版。

所有这些都是开源软件，但根据上面由网络安全研究员和[终身成就 Pwnie 奖](https://www.theregister.com/2018/08/10/pwnie_awards/)获得者[Michał Zalewski](https://lcamtuf.coredump.cx/)撰写的 Substack 文章，“我们刚刚见证了我职业生涯中最大胆的信息安全行动之一”。开源软件并非仅仅因为代码可见就天生更安全；在某些方面，它可能更容易受到[恶意行为者利用](https://thenewstack.io/openjs-foundations-leader-details-the-threats-to-open-source/)。持续验证和保护开源软件将是未来对所有人来说的巨大挑战，无论东西方。

## 我们为什么需要一个开源公共领域
这就是导致潜在的开源末日的原因：开源被分成东西方。双方会互相信任吗？或者我们正在看着部落主义推动堡垒心态，导致开源领域出现重大分裂？开源之所以有效是因为它是一个公共领域。分裂将创造两个开源世界，一个彼此不信任的分裂，类似于我们今天在东西方贸易战中看到的情况。这种分裂可能会减缓双方对最佳解决方案的创新和采用。

作为一个社区，我们必须超越地缘政治冲突，[推动建立一个值得信赖的开源软件公共领域](https://thenewstack.io/3-ways-to-drive-open-source-software-maturity/)，包括其供应链。所有利益相关者之间的参与策略是强制性的。围绕为所有参与者保护软件供应链创建共同利益和群体至关重要，但仅仅依靠独立的开源基金会是不够的。

基金会只能做这么多来弥合分歧。如今的基金会并没有在安全、代码分析或帮助[软件供应链管理](https://thenewstack.io/what-you-can-do-now-to-manage-your-software-supply-chain-risk/)方面投入大量资金。它们更多地充当组织和营销实体，依靠其成员来实施技术措施。我们需要类似于[CVE](https://www.cve.org/)（由 MITRE 公司创建）背后的理念的独立机构，其使命是帮助保护开源软件和供应链。

这些机构可能是什么样子？首先，它们需要来自所有地区的领导层，一种代表所有人的开源联合国。理想情况下，它不应该是“付费才能玩”的情况，那些拥有更多资金的人拥有更大的发言权。这些机构将提供保护开源供应链的最佳实践，强制执行特定的代码库治理模型以实现安全认证。

它们将与拥有代码审计和扫描能力的公共和私人机构合作，这些能力可以用于任何开源项目。它们可以提供一种方法来验证和验证[开源贡献者](https://thenewstack.io/navigating-the-messy-world-of-open-source-contributor-data/)的身份，以便有一种方法可以为提交提供问责制。仅仅提供最佳实践、免费工具和开发人员身份验证将极大地提高人们对开源供应链的信任。
目前，我们以项目为单位管理代码库安全，只要这种情况持续存在，我们所有人都会面临风险。我们必须作为一个全球社区来保护我们的[开源软件供应链](https://thenewstack.io/open-source-supply-chains-can-fix-your-dependency-headaches/)，以避免未来的开源末日。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1) 科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。