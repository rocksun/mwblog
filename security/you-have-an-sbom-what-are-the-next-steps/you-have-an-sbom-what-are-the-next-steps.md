
<!--
title: 您有一个 SBOM — 接下来的步骤是什么？
cover: https://cdn.thenewstack.io/media/2024/11/84c9c532-supplychain.jpg
-->

将软件成分分析与 SBOM 结合起来，可以帮助您构建一个全面的方法来管理和保护您的软件供应链。

> 译自 [You Have an SBOM — What Are the Next Steps?](https://thenewstack.io/you-have-an-sbom-what-are-the-next-steps/)，作者 Aaron Linskens。

正如建筑师依赖蓝图了解建筑物的详细信息一样，软件开发人员使用特定资源来跟踪其应用程序中的每个组件：[软件物料清单 (SBOM)](https://thenewstack.io/how-to-create-a-software-bill-of-materials/)。

作为一份详细的清单，SBOM 帮助您了解软件供应链中的每个组件，从专有代码到开源代码。通过保留一份全面的清单，您可以更好地增强安全性并快速解决漏洞。

但一个关键问题仍然存在：一旦您拥有 SBOM，接下来的步骤是什么？

## 验证您的 SBOM

SBOM 不仅仅是组件列表。它是帮助维护软件透明性和完整性的[一份重要文档](https://www.sonatype.com/blog/why-sboms-are-essential-for-every-organization)。当您验证 SBOM 并确认其内容准确反映软件的当前状态时，真正的价值才会显现。

考虑以下 SBOM 验证步骤：

1. **验证组件准确性**：使用自动化工具交叉检查 SBOM 与您的实际[软件依赖项](https://thenewstack.io/a-guide-to-software-dependencies/)，并更新 SBOM 以更正差异。
2. **确认版本一致性**：确保列出的版本与您的构建环境中的版本匹配，以识别需要更新的任何过时组件。
3. **检查许可信息**：验证每个组件的许可详细信息是否准确，以保持合规性并避免法律风险。
4. **扫描已知漏洞**：使用[软件成分分析 (SCA)](https://www.sonatype.com/resources/articles/what-is-software-composition-analysis)工具将 SBOM 组件与漏洞数据库进行比较，确保它们没有高风险问题。
5. **记录验证结果**：保留您的验证过程和任何补救措施的记录，以简化未来的审计并增强安全响应。

持续的 SBOM 验证增强了决策制定，实现了组件来源的跟踪并提高了安全性。通过提供对所有组件的透明性，它减少了对供应商声明的依赖并简化了审计。定期验证还确保组件是最新的，从而支持主动的安全态势。

## 添加软件成分分析

保护您的软件最有效的方法之一是结合 SBOM 管理和 SCA。虽然 SBOM 提供组件列表，但 SCA 工具会分析这些组件的许可问题、合规风险和漏洞。

[SBOM 管理和 SCA](https://thenewstack.io/software-composition-analysis-and-sboms-a-united-defense/) 共同构建了一种管理软件供应链的综合方法。

作为一种双重方法，请考虑以下策略：

- **交叉检查合规性和安全性**：验证后，SBOM 可以交叉引用 SCA 扫描结果。这有助于检测差异，确保 SBOM 和 SCA 发现保持一致，并解决许可、质量和安全问题。
- **使用 SBOM 见解增强 SCA**：SBOM 可以通过阐明数据库或操作系统等难以评估的领域来增强 SCA 扫描，确保更彻底的风险评估。

SBOM 管理与 SCA 共同创建了软件的整体视图，并有助于维护其完整性。这促进了主动风险管理，确保了符合监管标准，并保护了您的软件免受潜在威胁。

## 将 SBOM 集成到开发生命周期中

为了最大化 SBOM 的好处，[将它们集成到您的 SDLC](https://www.sonatype.com/blog/how-to-integrate-sboms-into-the-software-development-life-cycle) 中，并在可能的情况下自动化该过程。这确保了实时更新，并在您的软件不断发展时保持准确性。定期更新降低了数据过时的风险，增强了透明性和安全性。

通过将 SBOM 创建自动化并将其集成到 CI/CD 管道中，可以确保每次构建都带有 SBOM，从而提供软件组件的可靠记录。通过在 CI/CD 工作流中设置质量门，您可以扫描 SBOM 以查找安全漏洞和许可问题，从而阻止不符合要求的组件在部署中继续前进。

在质量保证 (QA) 期间，SBOM 对于确保发布前的合规性和安全性至关重要。它们确保每个版本都符合行业标准和最佳实践。通过将 SBOM 集成到 CI/CD 和 QA 流程中，开发团队建立了一个稳健的透明性和合规性框架，从而在所有阶段提升软件供应链安全性。

## 管理和监控 SBOM 以查找漏洞

有效的 SBOM 管理不仅限于开发阶段。在生产中，需要持续监控 SBOM 以确保持续的安全性和合规性，尤其是在出现新漏洞时。

要有效监控 SBOM，请考虑以下最佳实践：

* **维护 SBOM 存档**：为与生产中或交付给客户的软件相关的所有 SBOM 创建一个最新的存储库。此存档对于在整个 SDLC 中审核和跟踪组件更改至关重要。
* **长期保留**：在软件版本整个使用期间保留 SBOM。这支持合规性并能够快速响应漏洞。
* **主动风险管理**：当您发现漏洞时，请使用您的 SBOM 存档快速识别并修复受影响的组件。这可以快速补救并减少风险。
* **第三方 SBOM 监控**：定期监控第三方供应商的 SBOM，以提高您对零日漏洞和软件供应链攻击的响应能力。


通过这些最佳实践，您可以降低风险并保护您的软件免受安全威胁，同时保持符合行业标准。

## 利用 SBOM 实现长期安全性

随着 SBOM 采用的增加，组织必须加强其管理实践以确保稳健的软件安全性，尤其是开源。

通过专注于验证、集成和监控，您可以依靠您的 SBOM 作为管理软件安全性和合规性的强大资源。

这种方法不仅创建了一个更加透明且负责的软件开发过程，而且还加强了对漏洞和软件供应链攻击的防御。