<!--
title: 红帽企业Linux 10：一个AI驱动的、量子就绪的平台
cover: https://cdn.thenewstack.io/media/2025/05/7a5a6ecd-getty-images-el0zyfxt1gi-unsplash-redhat.jpg
summary: 重磅！Red Hat Enterprise Linux 10 (RHEL 10) 发布，AI加持！集成 GenAI 的 Red Hat Enterprise Linux Lightspeed 助力 Linux 管理，首发抗量子算法，FIPS 合规！引入 immutable Linux “镜像模式”，更有 Security Select Add-On 自定义 CVE 修复，云原生时代效率飞升！
-->

重磅！Red Hat Enterprise Linux 10 (RHEL 10) 发布，AI加持！集成 GenAI 的 Red Hat Enterprise Linux Lightspeed 助力 Linux 管理，首发抗量子算法，FIPS 合规！引入 immutable Linux “镜像模式”，更有 Security Select Add-On 自定义 CVE 修复，云原生时代效率飞升！

> 译自：[Red Hat Enterprise Linux 10: An AI-Driven, Quantum-Ready Platform](https://thenewstack.io/red-hat-enterprise-linux-10-an-ai-driven-quantum-ready-platform/)
> 
> 作者：Steven J Vaughan-Nichols

波士顿 — 在其年度 [Red Hat Summit](https://www.redhat.com/en/summit) 大会上，[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 推出了 [Red Hat Enterprise Linux 10 (RHEL 10)](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux)，将其旗舰操作系统的最新版本定位为下一代混合云和 AI 驱动的企业 IT 的基础。

像当今几乎所有公司一样，Red Hat 首席执行官 Matt Hicks 赞扬了 AI 将为其程序带来的好处。与 AI 铅笔刀不同，Red Hat 实际上通过其 AI 产品提供有用的功能。

正如 Hicks 所说，“AI 将使 Linux 管理员的生活更美好。” 如何实现？通过引入 [Red Hat Enterprise Linux Lightspeed](https://www.redhat.com/en/about/press-releases/red-hat-infuses-generative-ai-across-hybrid-cloud-portfolio-red-hat-lightspeed)。这项新功能将生成式 AI (GenAI) 直接集成到平台中，通过自然语言界面提供上下文相关的指导和可操作的建议。

## Lightspeed，一个新 Shell

当 Red Hat 说“直接”时，指的是直接进入 [Linux shell](https://thenewstack.io/learning-linux-start-here/) 本身。借助 Lightspeed，系统管理员可以寻求 shell 命令和脚本方面的帮助。因此，例如，如果您想最终完善一个古老的备份或恢复脚本，Lightspeed 可以与您一起清理它，一劳永逸。或者，假设您是一名新的系统管理员，您还可以使用可选的 AI 驱动的命令行助手来查找特定问题的特定命令及其适当的语法。

Red Hat 这样做是因为，根据 Red Hat 赞助的 IDC 研究 [The business value of standardizing on Red Hat Enterprise Linux](https://www.redhat.com/en/resources/idc-business-value-of-standardizing-analyst-material)，“组织正在努力雇用他们需要的 Linux 技能来运营和支持他们不断扩展的发行版，这使他们在安全性、合规性和应用程序停机方面面临更大的风险。”

除了 AI 和 Linux 管理的结合之外，RHEL 10 还引入了 [Federal Information Processing Standards (FIPS) compliance for post-quantum cryptography.](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) RHEL 是第一个包含抗量子算法的 Linux 发行版。关键是 Red Hat 希望使您能够保护组织免受新兴威胁，例如“[harvest now, decrypt later](https://www.keyfactor.com/blog/harvest-now-decrypt-later-a-new-form-of-attack/)”攻击，并帮助客户满足不断变化的监管要求。简而言之，RHEL 是第一个后量子密码 Linux。

## 不可变的 Linux

在 RHEL 10 中，Red Hat 引入了“镜像模式”。这本质上是一个 [immutable Linux](https://thenewstack.io/3-immutable-operating-systems-bottlerocket-flatcar-and-talos-linux/)。镜像模型已经酝酿了很长时间。借助这种新模型，Red Hat 将 RHEL 作为可启动的容器镜像交付，您可以使用容器原生工具和工作流程来使用它。在其中，核心程序和文件系统在运行时是只读的。对操作系统的更改需要构建和部署新镜像，然后重新启动。

虽然不可变的 Linux 发行版（例如 [Fedora CoreOS](https://fedoraproject.org/coreos/)）很常见，但 RHEL 是第一个转向不可变模型的主要服务器 Linux 操作系统。习惯于 shell 脚本和 [Cockpit](https://cockpit-project.org/) 的资深 Linux 管理员可能对这一举动并不满意。Red Hat 向其用户保证，这种方法统一了操作系统和应用程序的构建、部署和管理。这种转变最大限度地减少了配置漂移，并使 IT 团队能够使用一致的工具和工作流程来管理其整个基础设施，包括容器化应用程序及其底层平台。

Red Hat 高级副总裁兼首席产品官 Ashesh Badani 在一次采访中解释说：“补丁是每个系统管理员都会做的事情，并且总是会出现问题，这会导致与所需系统的偏差，这就是我们最终遇到漂移的时候。能够管理这种漂移对我们的客户来说是一个巨大的痛点。因此，能够为 RHEL 引入镜像模式实际上就是容器的概念，并且能够将操作系统作为容器进行管理是一个巨大的推动力。”
Salesforce 软件架构师 [Anish Bhatt](https://www.linkedin.com/in/anishbhatt/) 称赞了新的镜像模式：“它为我们的环境带来了稳定性，减少了配置漂移，并实现了更一致的部署体验。镜像模式是朝着简化云原生应用程序开发和 IT 运维在单个管道中的一个有意义的步骤。”

为了帮助新老 RHEL 管理员进行迁移，最新版本的 [Red Hat Insights](https://www.redhat.com/en/technologies/management/insights)（该平台的分析引擎）现在提供镜像构建器软件包建议和增强的规划工具。Insights 帮助您在构建时做出更明智的决策。

在底层，RHEL 使用 Linux 内核 6.11.0 版本作为其基线。这与 RHEL 9 的 5.14 内核相比是一个很大的飞跃。对于那些想要更新内核的人来说，CentOS Stream 现在基于 Linux 6.12。

## Red Hat 安全性

管理员需要注意其他一些变化。我认为最大的变化是[新创建的用户默认情况下将具有管理权限](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10-beta/html/10.0_beta_release_notes/overview#overview-major-changes)。不！这个想法让我感到不安。幸运的是，您可以关闭此选项。

在一个相关的变化中，使用新的 [sudo](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/) RHEL 系统角色，您可以在 RHEL 系统上大规模地一致地管理 sudo 配置。我对这个没意见。

在安全性方面，RHEL 10 [OpenSSL TLS 工具包](https://github.com/openssl/openssl) 引入了符合 FIPS 标准的 [Public-Key Cryptography Standards (PKCS) #12 文件](https://www.globalsign.com/en/blog/what-is-a-pkcs12-file)的创建、用于使用硬件令牌的 pkcs11-provider 以及许多其他改进。Red Hat 还更新了 9.8 版本的 [OpenSSH](https://www.openssh.com/) 套件，与 RHEL 9 的 OpenSSH 8.7 相比，它提供了许多修复和改进。最后，[SELinux](https://www.redhat.com/en/topics/linux/what-is-selinux) 用户空间版本 3.7 引入了一个新的 audit2allow 选项，提供 CIL 输出模式、Wayland 对 SELinux 沙箱的支持以及其他改进。

我怀疑许多公司会觉得有吸引力的一项安全更改是，Red Hat 正在为其客户提供一种新的方式来自定义对常见漏洞和暴露 (CVE) 修复的支持。借助 Security Select Add-On，订阅者可以选择购买 10 个他们选择的 CVE 修复。因此，如果您认为存在一个您认为非常麻烦的安全漏洞，即使没有其他人这么认为，您也可以让 Red Hat 为您修复它。Red Hat 认为，这对于医疗保健、金融、电信和政府等高度监管的行业尤其有用。

RHEL Security Select Add-on 将于 2025 年第三季度开始向包含 RHEL [Extended Life Cycle Support](https://www.redhat.com/en/resources/els-datasheet) 或 RHEL [Extended Update Support](https://www.redhat.com/en/resources/eus-datasheet) 的订阅客户提供。换句话说，如果一个过时的 RHEL 中存在一个旧的、令人讨厌的 CVE 困扰着您，Red Hat 也会为您修复该错误。

IDC 研究经理 [Ryan Caskey](https://www.linkedin.com/in/ryan-caskey-96307a17/) 指出了维护多样化 Linux 环境的挑战，并表示 RHEL 10“旨在为当前和未来的 IT 战略举措建立一个强大、基础的层。”
毋庸置疑，RHEL 10 还包括为您的开发人员更新的语言和工具包。

新的 RHEL 还附带了针对 AWS、Google Cloud 和 Microsoft Azure 预先调整、完全支持的 RHEL 镜像。RHEL 最终也完全支持 Oracle Cloud Infrastructure (OCI)。

除了通常的 x86、64 位 ARM、IBM POWER 和 IBM Z 架构之外，RHEL 10 还与 SiFive 合作，以 RISC-V 架构的开发者预览版形式提供，目标是 HiFive P550 平台的早期采用者。

与往常一样，RHEL 10 现在可以通过 Red Hat 客户门户获得。开发人员可以通过 [Red Hat 的开发者计划](https://developers.redhat.com/home) 免费访问 RHEL 10。因此，无论您已经是 RHEL 客户还是只是想试用一下，RHEL 10 都已为您准备就绪。