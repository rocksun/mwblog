# 联邦政府：关键软件必须在2026年前放弃C/C++，否则将面临风险

![Featued image for: Feds: Critical Software Must Drop C/C++ by 2026 or Face Risk](https://cdn.thenewstack.io/media/2024/10/543f458a-getty-images-bxeiwnalzai-unsplash-1024x683.jpg)

美国联邦政府正在加强对其危险的[软件开发](https://thenewstack.io/software-development/)实践的警告，美国网络安全与基础设施安全局（[CISA](https://thenewstack.io/who-should-be-responsible-for-software-security/)）和联邦调查局（FBI）发布了严厉警告，指出持续困扰关键基础设施的基本安全漏洞。

CISA和FBI最近联合发布的一份关于[产品安全不良实践](https://www.cisa.gov/resources-tools/resources/product-security-bad-practices)的报告警告软件制造商注意诸如使用C和C++等[内存不安全编程语言](https://thenewstack.io/out-with-c-and-c-in-with-memory-safety/)等不良做法。

报告指出：“为关键基础设施或[国家关键职能](https://thenewstack.io/white-house-warns-against-using-memory-unsafe-languages/)NCF服务而开发使用[内存不安全语言](https://thenewstack.io/white-house-warns-against-using-memory-unsafe-languages/)（例如，C或C++）的新产品线，而存在可用的替代内存安全语言，这是危险的，并且会显著增加对国家安全、国家经济安全以及国家公共卫生和安全的风险。”


## 三个类别

报告称，不良做法分为三大类：

- 产品属性，描述软件产品的可观察的安全相关特性。
- 安全特性，描述产品支持的安全功能。
- 组织流程和策略，描述软件制造商为确保其安全方法具有强大的透明度而采取的行动。

报告的目标是开发用于支持关键基础设施或NCF的软件产品和服务的软件制造商，包括本地软件、云服务和软件即服务（SaaS），报告称。


## 避免不良做法，遵循建议

此外，报告还鼓励所有软件制造商避免这些产品安全不良做法。“通过遵循本指南中的建议，制造商将向客户表明他们正在承担客户安全结果的责任，这是[安全设计](https://www.cisa.gov/securebydesign)的关键原则，”报告称。

“[Omdia](https://omdia.tech.informa.com/)”的分析师说：“这份指南当然是对美国政府此前就此问题发表声明的后续行动，这些声明可以追溯到2022年，告诫技术提供商和企业用户采用或迁移到内存安全语言。”

他表示：“撇开所有新代码不谈，幸运的是，这份文件以及美国政府都没有呼吁立即[从C/C++迁移到Rust](https://thenewstack.io/can-darpas-tractor-pull-c-to-rust-for-memory-safe-overhaul/)——只是一个例子。”“CISA的‘安全设计’文件承认，软件维护人员根本无法像那样批量迁移其代码库。”

这份指导虽然是自愿的，但代表了CISA迄今为止对基线安全实践的最强硬立场——让公司注意到在关键基础设施方面，什么是疏忽的软件开发实践。


## 时间紧迫

然而，软件制造商的时间紧迫。公司必须在2026年1月1日前制定内存安全路线图。

报告称：“对于使用内存不安全语言编写的现有产品，到2026年1月1日没有发布内存安全路线图是危险的，并且会显著增加对国家安全、国家经济安全以及国家公共卫生和安全的风险。”

此外，必须在同一天取消管理员帐户的默认密码。这些截止日期标志着从建议转向预期标准的转变。

报告还指出，内存安全路线图应概述制造商消除优先代码组件（例如，面向网络的代码或处理敏感功能（如加密操作）的代码）中内存安全漏洞的优先方法。

报告称：“制造商应证明内存安全路线图将导致其产品中内存安全漏洞的显著减少，并证明他们正在合理努力遵循内存安全路线图。”
企业持续大规模维护COBOL和Fortran代码有两个充分的理由：成本和风险，“Shimmin告诉The New Stack。“迁移数百万行代码在经济上根本不可行，任何负责任的组织也不会冒这个险。”

然而，根据报告，关键基础设施仍然存在“极其危险”的做法，例如：

- 默认密码。
- 直接SQL注入漏洞。
- 缺乏基本的入侵检测。
- 缺少多因素身份验证。

## 开源

关于开源软件，报告指出应特别注意开源漏洞。其他建议包括：

- 公司必须维护软件物料清单 (SBOM)。
- 要求缓存依赖项，而不是从公共资源中提取。
- 需要为其依赖的开源项目做出负责任的贡献。

报告称：“软件制造商应负责任地使用并可持续地为其依赖的开源软件做出贡献。”

报告还敦促提高透明度，声明：

- 公司必须发布漏洞披露政策。
- 要求为所有关键漏洞发布CVE。
- 必须提供关于安全问题的清晰文档。
- 预计维护六个月的安全日志。

## 好事

最后，CISA建议拥有关键软件的公司应在2026年初制定明确的攻击计划，这是一件好事，Shimmin说。这很好，因为它将给行业更多时间来想出更巧妙的方法来确保关键软件资产的安全，他说。

“这些方法可能包括硬件制造商加强潜在的攻击媒介，以及编程语言维护者提出诸如[Safe C++提案](https://safecpp.org/P3390R0.html)之类的想法，该提案呼吁创建一个[C++的超集，以解决内存安全问题](https://thenewstack.io/can-the-safe-c-proposal-copy-rusts-memory-safety)，而无需强制进行主要的代码重写，”他说。

## 纸老虎？

“CISA正在对使用C/C++或汇编语言构建的非内存安全应用程序采取强硬措施。由于截止日期不到15个月，这将导致用户和提供商争先恐后地遵守规定，因为政府系统的许多关键资产仍在使用C/C++，”Constellation Research的分析师[Holger Mueller]告诉The New Stack。“现在，所有人的目光都将集中在提供商和开发人员身上，看看能否实现这一截止日期——几个月后我们将看到这个CISA命令是纸老虎、带齿的老虎还是一个得到广泛遵守的标准法规。时间会证明一切。”

## 转向内存安全

据[Tim McNamara]，Accelerant.dev的创始人兼《Rust in Action》的作者说，企业构建更安全软件的压力肯定越来越大。该行业正在摆脱不安全的做法，这是一个健康的转变。

“然而，该文件仍然留有很大的回旋余地来维持现状，”McNamara告诉The New Stack。“作者显然很注意不要越权。请注意，文本中使用了诸如‘强烈建议’、‘应该’和‘合理努力’之类的词语。”

此外，McNamara说，该文件的规定也相当宽松。新的软件应该使用内存安全的编程语言编写。拥有现有产品的软件生产商被要求在2025年制定“内存安全路线图”。

“这份路线图是生产商随着时间推移减少内存安全漏洞的计划，”McNamara说。“还有一些重要的例外。尽管许多软件往往会比预期持续更长时间，但对于2030年即将停产的产品，不需要路线图。”

McNamara指出，2007年，[MITRE]发布了一份名为[不可原谅的漏洞](https://cwe.mitre.org/documents/unforgivable_vulns/unforgivable.pdf)的报告，该报告将内存安全问题列在首位。然而，这些错误在软件开发中并未被视为疏忽。“我没有看到其他领域可以接受不将已知的解决方案应用于重大的安全问题，”他说。

尽管如此，“观察业界如何回应评论邀请将很有趣，特别是考虑到在此期间将举行选举，”McNamara说。“希望这些担忧能够超越政治争论。”

CISA已就其指导意见启动了公众评论期，截止日期为2024年12月16日。请访问[联邦公报](https://www.federalregister.gov/documents/2024/10/29/2024-25078/request-for-comment-on-product-security-bad-practices-guidance)提交评论。

[YOUTUBE.COM/THENEWSTACK]
技术发展日新月异，不要错过任何一期。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等：[https://youtube.com/thenewstack?sub_confirmation=1](https://youtube.com/thenewstack?sub_confirmation=1)