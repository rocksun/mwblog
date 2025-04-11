
<!--
title: GitHub的新安全活动利用AI修复安全漏洞
cover: https://cdn.thenewstack.io/media/2025/04/f627f17e-peter-conrad-ua8pwpht1vw-unsplash.jpg
summary: GitHub推出基于AI的**Copilot Autofix**，通过**Security Campaigns**大规模修复安全漏洞！利用AI代码扫描代理，**Security Campaigns**能识别并修复开发者工作流程中的安全问题，解决积压漏洞，提升**GitHub Advanced Security and GitHub Code Security**客户的代码安全。
-->

GitHub推出基于AI的**Copilot Autofix**，通过**Security Campaigns**大规模修复安全漏洞！利用AI代码扫描代理，**Security Campaigns**能识别并修复开发者工作流程中的安全问题，解决积压漏洞，提升**GitHub Advanced Security and GitHub Code Security**客户的代码安全。

> 译自：[GitHub's New Security Campaigns Fix Security Debt With AI](https://thenewstack.io/githubs-new-security-campaigns-fix-security-debt-with-ai/)
> 
> 作者：Loraine Lawson

GitHub 周二推出了一款新的基于 AI 的工具，用于消除其 [GitHub Advanced Security and GitHub Code Security](https://github.blog/changelog/2025-03-04-introducing-github-secret-protection-and-github-code-security/) 客户的安全漏洞。现在，组织可以运行[安全活动](https://docs.github.com/en/enterprise-cloud@latest/code-security/securing-your-organization/fixing-security-alerts-at-scale/about-security-campaigns)，这有助于识别和修复开发者 GitHub 工作流程中现有的[安全](https://thenewstack.io/security/)问题。

“[安全漏洞](https://thenewstack.io/avoiding-technical-security-debt-during-cloud-transformation/)是我们数据显示客户面临的最大未解决风险：从历史上看，只有 10% 的合并代码中遗留的安全漏洞得到解决，这意味着直到今天，90% 的风险没有得到优先处理，”[GitHub](https://github.com/) 的高级产品经理 James Fletcher 周二在公司博客上宣布[安全活动全面上市](https://github.blog/security/application-security/found-means-fixed-reduce-security-debt-at-scale-with-github-security-campaigns/)时写道。“现在，我们的数据显示，安全活动中包含的 55% 的安全漏洞已得到修复。”

它依赖于一个名为 [Copilot Autofix](https://thenewstack.io/copilot-autofix-ais-answer-to-code-vulnerability-woes/) 的 AI 代码扫描代理，该代理于 2023 年发布。扫描可以按计划触发，也可以在指定事件发生时触发，例如推送到分支或打开拉取请求。

## 安全活动解决安全漏洞

GitHub 新任产品副总裁 Marcelo Oliveira 告诉 The New Stack，安全活动不仅仅是修复漏洞。安全活动旨在修复已在生产代码中存在的安全漏洞。

“在大多数组织中，我们谈论的是成千上万甚至数万个漏洞积压，这些组织根本不可能人为地修复所有这些问题，”他说。

范围意味着这些问题往往会持续存在。

“我们一直未能真正大幅帮助人们修复或降低安全风险，”Oliveira 说。“一个季度又一个季度，一年又一年，我会去拜访客户，漏洞趋势继续向上发展，而不是真正改善。”

安全活动通过修复开发者 GitHub 工作流程中长期存在的问题来解决这些现有漏洞。安全活动甚至带有基于常用主题的预定义模板，以帮助确定活动范围。例如，一个模板是 [MITRE 的十大已知漏洞利用漏洞](https://cwe.mitre.org/top25/archive/2023/2023_kev_list.html)。

[GitHub 的安全](https://thenewstack.io/github-rolls-out-free-secret-risk-assessment-tool/)概述还为组织提供统计数据和指标，总结其整体风险状况。
“并不是开发者不想解决问题，”Oliveira 说。“这只是他们面临的一个竞争优先事项，所以[我们]正在尽我们所能来减少他们的开销。”

他补充说，在安全活动之后，GitHub 内部提供支持，以帮助[代码保持清洁](https://thenewstack.io/arming-developers-with-the-power-of-clean-code/)，并确保开发者不会将新的漏洞引入流程中。

为了保持这种状态，Oliveira 说，安全活动允许“开发者和安全人员协作，我应该首先修复哪些问题，以降低我的应用程序在整个组织中的风险？”

## 自动化漏洞修复

Oliveira 说，安全活动会将安全问题分类并优先处理到正常的软件开发生命周期中，然后制定扭转这种趋势的策略。

当应用程序安全经理创建安全活动时，他们会概述组织想要修复的一组漏洞。

例如，应用程序安全经理可能希望消除组织中暴露于 Internet 的应用程序上的所有 SQL 注入漏洞。该解决方案允许经理标记任何暴露于 Internet、已在生产中的存储库，然后它会显示与 SQL 注入相关的任何漏洞。

> “并非开发者不想解决问题，而是因为对他们来说存在优先级竞争，所以[我们]正尽可能多地完成工作，以减少他们的额外负担。”
>
> — Marcelo Oliveira, GitHub 产品副总裁

Oliveira 说：“它们具有高或危急的严重性，然后这将为我过滤我的组织内符合该标准的所有内容。现在我可以将所有这些漏洞打包到一个活动中，并将它分派给我组织中合适的开发者——他们需要[修复漏洞](https://thenewstack.io/root-out-vulnerabilities-in-github-as-you-merge-code-changes/)。”

一旦经理定义了需要修复的漏洞范围，信息就会自动发送到 GitHub 中的开发者，他们会收到问题的警报，收到活动的通知，然后被告知他们需要关注哪些漏洞。

当活动创建时，Copilot Autofix 会自动生成修复建议，并呈现需要更改的代码来解决问题。

他说：“开发者看到的不仅仅是‘嘿，修复这个’的警报，而是‘我们需要修复这个警报，因为它已由应用程序安全团队根据此标准确定了优先级’。”

然后代码通过 [CI 流程](https://thenewstack.io/engineering-best-practices-of-ci-pipelines/) 运行，并通过管道进行修复，他说。

Oliveira 说，安全活动基本上扩展了协作平台，将应用程序安全经理包括在内，这使得应用程序安全经理和开发者能够更有效地协作。

他补充说：“在[自动化问题修复](https://thenewstack.io/aiops-done-right-automating-remediation-and-resiliency/)方面，我们也正在尽我们所能。”

## 在代码存在的地方修复漏洞

一旦选择了活动警报并且应用程序安全经理指定了时间表，活动就会自动将信息传达给任何正在处理相关存储库的开发者。

活动定义的修复程序会显示为存储库中要解决的问题，因此开发者可以像处理任何其他功能工作一样处理和管理问题。

Fletcher 在 GitHub 博客上写道：“使用 Copilot Autofix 一次为多达 1,000 个代码扫描警报生成代码建议，安全活动可帮助安全团队处理分类和优先级排序，同时您可以使用 Autofix 快速解决问题——而不会中断您的开发势头。修复警报变得像审查差异和创建拉取请求一样容易。”