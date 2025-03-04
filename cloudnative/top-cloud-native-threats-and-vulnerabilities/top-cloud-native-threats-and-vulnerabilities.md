
<!--
title: 2024年顶级云原生威胁和漏洞
cover: https://www.aquasec.com/wp-content/uploads/2025/02/social-Cloud-Security-trends-1200x628-1.jpg
-->

> 译自：[Top Cloud Native Threats and Vulnerabilities of 2024](https://www.aquasec.com/blog/top-cloud-native-threats-and-vulnerabilities/)
> 
> 作者：Erin Stephan; Aqua Team

云原生安全漏洞是指任何威胁参与者可以利用的风险，包括软件缺陷、不安全的代码、错误配置的云、IAM、API等等

云环境的复杂性意味着存在几乎无限数量的潜在安全风险和漏洞，这些风险和漏洞可能出现在云基础设施或工作负载中。也就是说，一些云安全威胁比其他威胁更为普遍——了解哪些风险和漏洞是趋势的关键在于了解在管理组织的攻击面时需要优先考虑什么。为此，本文详细介绍了2024年出现的七个最突出的云威胁和漏洞，其中包括Aqua研究人员发现的几个漏洞。

## 什么是云原生漏洞？

云原生安全漏洞是指任何类型的威胁或风险，威胁参与者可以利用这些威胁或风险来破坏云原生服务，例如容器。常见云漏洞类型的示例包括：

- 运行在云服务器上的操作系统服务器中的软件漏洞。
- [容器镜像中的不安全代码](https://www.aquasec.com/cloud-native-academy/application-security/container-scanning/)用于将应用程序部署到云中。
- 容器内的错误配置，这是可能导致容器化应用程序被破坏的另一个风险。
- 错误配置的[身份和访问管理](https://www.aquasec.com/cloud-native-academy/application-security/identity-and-access-management/)(IAM)设置，这可能导致敏感信息泄露或为控制应用程序提供攻击媒介。
- 云API中的缺陷，威胁参与者可以滥用这些缺陷来获得未经授权的访问或窃取敏感数据。

有效的云安全取决于在攻击者利用这些威胁之前发现和修复这些威胁的能力。

### 2024年七大云原生威胁和漏洞
云安全工具的目标应该是发现所有类型的安全风险和漏洞。但是，再次强调，关注最新、最常见或最严重的风险是帮助决定优先处理哪些类型威胁的一种方法。

以下容器和云漏洞属于此类别，因为大多数都是相对新颖的威胁，如果任其存在，可能会对云环境和基于云的工作负载造成重大损害。

### #1 Perfctl

正如Aqua[在2024年10月报道的那样](https://www.aquasec.com/blog/perfctl-a-stealthy-malware-targeting-millions-of-linux-servers/)，perfctl是一种针对Linux服务器的恶意软件。该恶意软件已经活跃了三到四年，其目标是在访问受害者服务器后运行加密挖掘软件作为[加密劫持攻击](https://www.aquasec.com/cloud-native-academy/cloud-attacks/cryptojacking/)的一部分。为此，它利用Polkit漏洞([CVE-2021-4034](https://nvd.nist.gov/vuln/detail/cve-2021-4034))来发起权限提升攻击。

使perfctl尤其值得注意——而且特别危险的是——它用来逃避检测的复杂技术。它依赖于rootkit来隐藏其存在，在用户在系统中活动时停止运行（为了避免产生可能提醒用户注意漏洞的“噪音”），并删除其二进制文件并作为后台服务运行。

诸如[网络分段](https://www.aquasec.com/cloud-native-academy/container-security/network-segmentation/)和文件执行限制之类的实践可以增强服务器对这种恶意软件和类似恶意软件的防御能力。

### #2 Bucket Monopoly

[Bucket Monopoly](https://www.aquasec.com/blog/bucket-monopoly-breaching-aws-accounts-through-shadow-resources/)是Amazon Web Services (AWS)云中运行的六项服务中的一个漏洞，允许攻击者执行各种攻击，包括远程代码执行和在某些情况下接管帐户。
此漏洞利用所谓的“影子资源”攻击媒介，该媒介滥用AWS服务自动生成的资源，通常在用户不知情的情况下。

在发现这些云安全漏洞后，Aqua将其报告给AWS，AWS在公开披露这些漏洞之前对其进行了修复。尽管如此，这一威胁提醒我们，即使是管理最好的公共云也可能在其核心云服务中遇到重大的安全漏洞。

### #3 Snap Trap

在2024年2月，Aqua详细介绍了一种称为[Snap Trap](https://www.aquasec.com/blog/snap-trap-the-hidden-dangers-within-ubuntus-package-suggestion-system/)的云安全威胁，该威胁允许威胁参与者在运行Ubuntu Linux的系统上植入恶意软件包。更具体地说，它允许滥用Ubuntu软件包管理系统中自动建议软件包名称的功能。通过操纵该功能的工作方式，威胁参与者可能会诱骗用户安装恶意软件包而不是合法软件包。
该漏洞也可能被用于在容器内植入恶意代码，因为基于Ubuntu的容器通常使用Ubuntu的包管理工具在运行时安装软件。

此缺陷自2016年以来就已为人所知，但从未得到明确的缓解。防御它的最佳方法是利用一些功能——例如Aqua平台提供的功能——来阻止危险的功能，例如使用包管理器在容器内安装软件。


### #4 Hadooken

[Hadooken](https://www.aquasec.com/blog/hadooken-malware-targets-weblogic-applications/)，Aqua研究人员在夏末发现的恶意软件，目标是Oracle WebLogic，这是一种广泛使用的Java EE应用服务器。利用此漏洞需要滥用弱凭据或易受攻击的管理员控制台来访问WebLogic系统。一旦进入内部，攻击者就可以通过运行任意代码或横向移动来破坏其他系统，从而升级入侵。Hadooken是一个典型的例子，说明了为什么漏洞扫描仍然至关重要，即使对于依赖Oracle等可靠供应商平台的组织也是如此。


### #5 GitHub代码库密钥泄露

作为一个由人为风险行为而非技术缺陷造成的云安全威胁的例子，2024年5月，Azure和Red Hat平台的访问凭据已被[通过GitHub代码库泄露](https://www.aquasec.com/blog/github-repos-expose-azure-and-red-hat-secrets/)。泄露发生是因为这些科技公司的员工为个人项目创建了GitHub代码库，并在其中意外存储了访问凭据。

这一威胁提醒我们，教育用户了解安全最佳实践以及扫描GitHub代码库等资源以查找[管理不当的密钥](https://www.aquasec.com/cloud-native-academy/supply-chain-security/secrets-management/)非常重要。


### #6 CUPS漏洞

CUPS，一个开源打印服务器，看起来可能足够不起眼。但正如安全研究人员在2024年9月报道的那样，运行CUPS的Linux系统[容易受到攻击](https://www.aquasec.com/blog/cups-a-critical-9-9-linux-vulnerability-reviewed/)，允许远程威胁参与者执行任意代码。由于攻击相对容易实施且影响非常流行的软件服务，因此它被认为是一个严重的漏洞。

为了阻止此漏洞，管理员可以从受影响的系统中删除CUPS软件或阻止网络访问CUPS。为了大规模缓解威胁，可以考虑使用Aqua强制执行运行时策略，以防止CUPS服务在所有系统上运行。


### #7 Lucifer

正如我们在2024年2月报道的那样，Lucifer是一个针对Apache Hadoop和Apache Druid（流行的开源“大数据”软件）的恶意软件活动。最初，攻击者的目标似乎是尝试[防御规避](https://www.aquasec.com/cloud-native-academy/cloud-attacks/defense-evasion/)技术，但Lucifer可能导致更严重的威胁，包括远程代码执行。


### 使用Aqua缓解云安全威胁和漏洞

作为一个全面的云和容器安全平台，Aqua使组织能够检测和缓解各种类型的云安全威胁——从perfctl等操作系统漏洞，到Bucket Monopoly等不安全的云服务，再到GitHub密钥泄露事件等不安全的密钥管理，以及更广泛的威胁。