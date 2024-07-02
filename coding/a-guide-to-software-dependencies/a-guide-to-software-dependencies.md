
<!--
title: 软件依赖指南
cover: https://cdn.thenewstack.io/media/2024/07/9d571027-dependencies.jpg
-->

让我们深入了解软件依赖项是什么，探索它们的类型，并讨论有效依赖项管理的最佳实践。

> 译自 [A Guide to Software Dependencies](https://thenewstack.io/a-guide-to-software-dependencies/)，作者 Aaron Linskens。

如今的软件开发严重依赖于相互关联的组件网络，[其中绝大多数是开源的](https://www.linuxfoundation.org/blog/blog/a-summary-of-census-ii-open-source-software-application-libraries-the-world-depends-on)。

理解[软件依赖](https://www.sonatype.com/resources/articles/what-are-software-dependencies)——软件组件正常运行所需的构建块——对于旨在构建健壮、安全应用程序的开发人员和组织至关重要。

让我们深入了解软件依赖是什么，探索它们的类型，并讨论有效依赖管理的最佳实践。

## 了解软件依赖

软件依赖是指软件模块或应用程序正常运行所需的外部组件或库。

这些可以从完整的库到较小的代码片段，它们构成了大多数现代软件的支柱，有助于简化开发流程并增强功能。

## 软件依赖的类型有哪些？

软件依赖主要存在两种形式：

- **直接依赖**: 这些是您的软件直接调用和使用的依赖项。例如，如果您的应用程序使用 JSON 解析库，那么该库就是直接依赖项。
- **传递依赖**: 这些是您依赖项的依赖项。使用相同的示例，如果您使用的 JSON 解析库依赖于字符串操作工具包，那么该工具包将成为您应用程序的传递依赖项。

直接依赖项对于项目的正常运行至关重要，并在软件的配置中进行管理，让您完全控制它们的更新和集成。

相比之下，传递依赖项通常不受您的直接控制，这使得解决其中的问题更具挑战性。它们代码库中的任何修复或更新都必须通过[软件供应链](https://www.sonatype.com/resources/articles/what-is-software-supply-chain)传播，才能使您的项目受益。如果传递依赖项被多个组件广泛使用，这种延迟可能会加剧，延长更新到达您项目的所需时间，并可能影响[应用程序的安全性](https://thenewstack.io/a-guide-to-open-source-software-security/)。

## 依赖项的重要性是什么？

依赖项至关重要，因为它们决定了程序的运行可靠性和安全性。依赖项管理不当会导致软件故障和[安全漏洞](https://www.sonatype.com/resources/articles/what-are-open-source-vulnerabilities)，尤其是在依赖项过时或遭到破坏的情况下。

[管理依赖项需要](https://thenewstack.io/better-incident-management-requires-more-than-just-data/)了解它们的性质以及对项目的影响，通常通过以下概念：

- **声明和管理**: 直接依赖项在项目的配置文件中明确声明。相比之下，传递依赖项通常不是由项目声明的，而是由直接依赖项引入的。
- **重要性**: 虽然直接依赖项对于项目的直接功能至关重要，但传递依赖项支持直接依赖项，并且同样重要。
- **控制和可见性**: 直接依赖项在您的控制之下，并在您的项目管理工具中可见。然而，传递依赖项可能是隐藏的，难以管理，通常需要专门的工具来检测和管理它们。

有效的依赖项管理不仅可以提高应用程序的稳定性和安全性，还可以确保两种类型的依赖项都针对性能和[风险缓解](https://thenewstack.io/navigating-open-source-software-risks-whose-job-is-it-anyway/)进行了优化。

## 如何有效地管理依赖项？

在依赖项管理的背景下，一个重大挑战是避免“[依赖地狱](https://en.wikipedia.org/wiki/Dependency_hell)”，在这种情况下，依赖项的冲突版本或广泛的依赖项链会导致不可预测的冲突和集成问题。这种复杂性可能会因某些项目处理的依赖项数量之多而加剧，使得有效跟踪和管理每个依赖项变得困难。

此外，保持依赖项更新是一项至关重要的但具有挑战性的任务。过时的依赖项是安全漏洞和兼容性问题的常见来源。此外，项目的不同部分可能需要同一依赖项的不同版本，从而导致难以解决的冲突。

下面我们将介绍几种帮助有效管理依赖项的方法。

### 依赖项扫描
在任何开发工作流程中，定期[扫描依赖项](https://www.sonatype.com/blog/rule-over-your-dependencies-and-scan-at-your-own-open-source-risk)都是必不可少的。此过程涉及评估每个依赖项的健康状况和安全状态，以确保它们不会引入安全漏洞或合规性问题。

通过定期扫描您的软件组件，您可以及早发现和缓解潜在风险，从而控制依赖项并防止它们损害项目的完整性。

### 依赖项映射
除了简单的扫描之外，[依赖项映射](https://www.sonatype.com/blog/dependency-mapping-a-beginners-guide)创建了依赖项之间关系的可视化，提供了更全面的视图，了解组件如何在您的软件中交互。这种做法对于识别直接依赖项以及广泛的传递依赖项网络都非常宝贵。

通过创建这些关系的详细地图，开发人员可以查明隐藏的风险，更好地了解其[软件的结构并确保任何更改或更新](https://thenewstack.io/security-of-software-update-systems-in-2023/)不会破坏关键依赖项。

## 依赖项管理最佳实践
随着软件项目复杂性的增加，依赖项的数量可能会变得难以管理，难以跟踪和难以管理。定期更新的依赖项有助于防止安全漏洞和兼容性问题。

以下是一些最佳实践，以确保依赖项对项目的健康和效率做出积极贡献。

### 定期审计

定期[审计您的依赖项](https://ossindex.sonatype.org/)，以确保它们是最新的和安全的。这种做法不仅有助于识别过时的组件，还有助于评估依赖项生态系统的整体健康状况。定期审查允许及时更新和调整，最大限度地降低安全风险并提高应用程序性能。

### 自动化工具

利用[用于依赖项管理的自动化工具](https://www.sonatype.com/products/open-source-security-dependency-management)。这些类型的工具通过根据项目文件中的规范自动下载和链接必要的依赖项来简化库和框架的管理。

集成[自动依赖项管理](https://thenewstack.io/unlocking-the-power-of-automatic-dependency-management/)工具可以改变这项任务，确保依赖项始终是最新的，并且在没有人工监督的情况下得到良好维护。

### 监控依赖项漏洞

持续监控您的依赖项是否存在漏洞。使用集成到您的开发环境中的扫描方法，允许[主动识别和修复潜在的安全威胁](https://thenewstack.io/down-with-detection-obsession-proactive-security-in-2024/)。

可以创建可消费、可共享资源（例如[软件物料清单 (SBOM)](https://www.sonatype.com/resources/articles/what-is-software-bill-of-materials)）的工具，可以特别有效。[扫描漏洞](https://www.sonatype.com/products/vulnerability-scanner)确保您在整个开发生命周期中保持高标准的安全性和合规性。

## 主动依赖项管理，打造安全应用程序

有效管理软件依赖项对于维护安全、可靠和高效的应用程序至关重要。

通过采用定期审计、使用自动化工具和持续监控漏洞等主动做法，开发人员可以提高应用程序性能并适应技术变化。

严格的依赖项[管理不仅仅是技术需求](https://thenewstack.io/why-kubernetes-cluster-management-needs-to-be-easier-for-developers/)，而是一种战略优势，它确保了软件项目在日益由开源组件驱动的世界中的可持续性和成功。
