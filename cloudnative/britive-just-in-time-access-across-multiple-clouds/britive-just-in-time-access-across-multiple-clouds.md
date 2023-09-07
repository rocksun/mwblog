# Britive: 即时跨多云访问

这家初创公司正接受自动化跨云临时访问的挑战，不仅针对人类，也针对机器处理。

翻译自 [Britive: Just-in-Time Access across Multiple Clouds](https://thenewstack.io/britive-just-in-time-access-across-multiple-clouds/) 。

![](https://cdn.thenewstack.io/media/2023/09/d72d1d27-image2-1024x659.jpg)
*图片来自 Britive*

过去，当用户被授予对某个应用或服务的访问权限时，他们会一直保持这种访问权限，直到离开公司。不幸的是，即使在那之后，访问权限通常也不会被撤销。这种永久的 24/7 访问权限使公司面临各种安全漏洞的风险。

最近，[即时（JIT）访问](https://thenewstack.io/just-in-time-authorization-with-openid-sse-and-caep/)的理念开始流行，以解决公司由于特权激增而带来的扩大的攻击面。与持续访问不同，即时访问的思路是仅在特定时间段内授予访问权限。

但是，对员工每天使用的无数技术手动管理访问权限，尤其是对于拥有成千上万员工的公司来说，将是一项艰巨的任务。随着许多公司采用[混合云](https://cloudacademy.com/blog/azure-hybrid-identity-authentication-methods/#:~:text=Password%20hash%20synchronization%20(PHS)，cloud%2Dbased%20Azure%20AD%20instance.)策略，每个云都有自己的身份和访问管理(IAM)协议，负担就更重了。[零信任架构](https://thenewstack.io/what-is-zero-trust-security/)的支柱之一是零站立特权，即时访问为实现这一目标铺平了道路。

总部位于加利福尼亚州格伦代尔的 [Britive](https://www.britive.com/) 正接受自动化跨多云即时访问的挑战，不仅针对人类，还针对机器处理。

“我们认识到，在云中，访问通常不需要是永久的，” Britive CEO 兼联合创始人 [Art Poghosyan](https://www.linkedin.com/in/artyompoghosyan/) 指出。“大多数访问都是频繁变化和动态的，它实际上不必是永久的持续访问权限......如果您能够在用户需要时使用身份进行配置。有了适当的安全措施、防护栏和授权在位，您实际上不需要永远保留那种访问权限。......这就是我们所做的，我们称之为即时临时特权管理或访问管理。”

## "最好交给自动化处理"

近年来，滥用用户特权已经导致了一些大规模的安全漏洞，例如 [Solarwinds](https://thenewstack.io/behind-the-scenes-of-the-sunburst-attack/)、MGM Resorts、Uber 和 Capital One 等公司。甚至身为身份和访问管理（IAM）供应商的 [Okta 也成为了受害者](https://thenewstack.io/the-okta-mess-is-even-worse-than-it-appears/)。

在云安全联盟的报告“[云计算的顶级威胁](https://cloudsecurityalliance.org/research/working-groups/top-threats/)”中，超过 700 名行业专家将身份问题列为最大的整体威胁。

在“[2022 年数字身份安全趋势](https://21078271.fs1.hubspotusercontent-na1.net/hubfs/21078271/2022%20Trends%20in%20Securing%20Digital%20Identities.pdf?utm_medium=email&_hsmi=217049379&_hsenc=p2ANqtz-81MilDCQxKM0uq6UEdk_fzK-w-NUmVZKoD3leyngKd697qJyckrv-d5ASytfkEuRoxLGt67QUumQcv9mA0e38sWOqB4Q&utm_content=217049379&utm_source=hs_automation)”中，超过 500 名受访者中有 98% 表示，身份数量正在增加，主要是由云采用、第三方关系和机器身份推动的。

特别指出[云身份配置错误](https://thenewstack.io/palo-alto-networks-botched-access-management-an-easy-opening-for-cloud-attacks/)，这是一个经常发生的问题，当时的 [Palo Alto Networks](https://www.paloaltonetworks.com/cloud-security?utm_content=inline-mention) 的公共云首席安全官 [Matthew Chiodi](https://www.linkedin.com/in/mattchiodi/) 提到了缺乏 IAM 治理和标准，再加上“在每个云帐户中创建的用户和机器角色、权限和服务的数量之多”。

Chiodi 补充说：“人类在许多方面表现出色，但理解有效的权限并识别跨越数百个角色和不同云服务提供商的风险策略是最好交给算法和自动化来完成的任务。”

JIT 系统考虑了用户是否被授权访问、用户的位置以及他们当前任务的上下文。只有在给定的情况下才授予访问权限，并在任务完成后撤销权限。

## 满足速度需求

成立于 2018 年，Britive 自动化处理了人员和软件在多个云上访问云服务和应用程序的 JIT 访问权限，包括令牌和密钥。

除了与 Azure、[Oracle](https://developer.oracle.com/?utm_content=inline-mention)、[Amazon Web Services（AWS）](https://aws.amazon.com/?utm_content=inline-mention) 和 Google 等云平台涉及的不同身份管理流程之外，Poghosyan 特别指出，开发人员需要访问各种工具。

“考虑到他们的工作很多需要即时访问…速度对用户来说是最重要的，对吧？”他说。

“所以他们使用很多自动化工具，像 HashiCorp Terraform、GitHub 或 GitLab 等。所有这些工具也需要访问权限、密钥和令牌。这与传统的 IAM 工具不太合适，因为后者主要是从公司的中心化、繁重的工作流和审批过程出发。

“因此，我们首先构建了一种可以适应云环境用户需要的高速度和高度自动化流程的技术，特别是开发团队需要的技术。”他还补充说，其他团队，如需要访问 Snowflake 或 Google Big Query 等内容并且需求快速变化的数据分析师，也会发现它有价值。

“这再次需要一个可以动态适应用户需求和他们日常工作中使用的工具的工具或系统。”他说。

## 超越基于角色的访问

作为用户与云平台或应用程序之间的抽象层，Britive 采用 API 为用户授予授权的权限级别。一个临时服务账户位于开发者访问的容器内，而不是使用硬编码的凭据。

虽然用户通常使用他们日常工作所需的最低权限，但即时访问将在特定时间段内授予提升的权限，并在时间到期时撤销这些权限。该系统[不仅限于基于角色的访问（RBAC](https://www.forbes.com/sites/forbestechcouncil/2022/06/22/access-control-in-the-cloud-choosing-the-right-system-for-your-business-security/?sh=7e1dddea5d40)），而且足够灵活，可以允许公司根据资源属性（基于属性的访问）或策略（基于策略的访问）来提供访问权限，Poghosyan 表示。

该专利平台与大多数云提供商以及 Jenkins 和 Terraform 等 CI/CD 自动化工具集成。

其跨云可见性提供了对云基础设施、平台和数据工具的问题（如配置错误、高风险权限和异常活动）的单一视图。数据分析提供基于历史使用模式的风险评分和权益访问建议。访问地图提供了策略、角色、组和资源之间关系的视觉表示，让您了解谁有权访问什么以及如何使用。

该公司在 2021 年添加了云基础设施权限管理（CIEM），以了解跨多云环境的权限，并在访问级别高于应有权限时识别和减轻风险。

该公司于 2022 年 3 月推出了 [Cloud Secrets Manager](https://www.britive.com/blog/cloud-secrets-manager/)，这是一个用于静态秘密和密钥的云保险库，当临时访问不可行时使用。它应用了 JIT 概念，即临时创建人员和机器 ID，如用户名或密码、数据库凭据、API 令牌、TLS 证书、SSH 密钥等。它解决了在一个单一平台中管理硬编码的秘密的问题，通过根据需求检索密钥来替代代码中嵌入的 API 密钥，并提供了谁有权访问哪些秘密以及如何以及何时使用它们的可见性。

今年 8 月，公司推出了 Access Builder，该工具提供了对关键云基础设施、应用程序和数据的自助访问请求。用户可以设置一个用作访问基础的配置文件，并跟踪批准流程。与此同时，管理员可以跟踪请求的权限，深入了解哪些身份请求访问特定的应用程序和基础设施。

## 各种集成

Poghosyan 之前共同创立了 Advancive，这是一家 IAM 咨询公司，于 2016 年被 Optiv 收购。Poghosyan 和 [Alex Gudanis](https://www.linkedin.com/in/ACoAAABHOdwB87IsPMqSs_nqt1ypYH-LzLThKYE/) 于 2018 年创立了 Britive。该公司已筹集了 3590 万美元，最近一次是于今年 3 月宣布的 B 轮融资中筹集了 2050 万美元。其客户包括 Gap、丰田、Forbes 等公司。

身份和安全分析公司 KuppingerCole 在其 2022 年领导力指南报告中将 Britive 列为创新领袖之一，与 CyberArk、EmpowerID、Palo Alto Networks、Senhasegura、SSH 和 StrongDM 等公司一起，这些公司因拥抱“云基础设施权限管理（CIEM）和 DREAM（动态资源授权和访问管理）能力的新世界”而被提及。

报告指出，Britive 对于 JIT 机器和非机器访问云服务（包括基础设施、平台、数据和其他“作为服务”的解决方案）具有最广泛的兼容性之一，包括一些根据客户的特定要求提供的云服务，如 Snowflake、Workday、Okta Identity Cloud、Salesforce、ServiceNow、Google Workspace 等等。这扩展了它在云领域的影响力，超越了许多竞争对手，成为了开箱即用的解决方案。”

报告还指出，在高风险的开发环境中，它“在支持多云访问方面非常令人瞩目”。

Poghosyan 指出，公司未来的重点是两个方面：一是为非公有云环境提供支持，因为这仍然是企业的现实，另一个是在非基础设施技术领域进行更广泛的拓展。他说，他们正在建立一个框架，使任何云应用程序或云技术供应商都能够与 Britive 的模型集成。
