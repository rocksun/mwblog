# 为什么 Docker Scout 正在改变开发者扫描漏洞的方式

![为什么 Docker Scout 正在改变开发者扫描漏洞的方式的特色图片](https://cdn.thenewstack.io/media/2025/03/090cc738-peter-conrad-ua8pwpht1vw-unsplash-1024x699.jpg)

[Peter Conrad](https://unsplash.com/@pconrad?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在 [Unsplash](https://unsplash.com/photos/a-red-security-sign-and-a-blue-security-sign-UA8PwPht1Vw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 上发布。

容器中的漏洞扫描需求日益增长。随着安全威胁的推进，传统技术需要一种新的方法。企业必须扫描容器的安全性，以降低风险。

Snyk、Trivy 和 Clair 是传统的扫描器。这些工具用于识别漏洞。一般来说，这些工具依赖于预先存在的常见漏洞和暴露 (CVE) 以及它们各自的数据库。尽管如此，它们的有效性在速度和精度方面都有所欠缺。

这就是 Docker Scout 发挥作用的地方。它提供实时的安全洞察，这最终成为可能。此外，它可以无缝集成到 Docker 生态系统的其余部分。

本文将引导您比较 Docker Scout 与传统扫描器。我们还将回顾它们的准确性、集成简易性和自动化能力。

## 传统漏洞扫描器概述

传统工具通过将软件包版本与 CVE 数据库进行比较来检测容器镜像中的安全风险。任何具有版本感知扫描器的工具都可以在这里工作，尽管每个扫描器的工作方式都不同。

它们是如何工作的？

**第一阶段：扫描镜像层**

旧的漏洞扫描器会获取容器镜像并逐层分析，一次分析一层。镜像由许多层组成，这些层代表对基础镜像所做的修改。这些层包含某些依赖项、库和软件，扫描器会检查它们是否存在安全问题。

**第二阶段：与 CVE 进行比较**

一旦确定了依赖项，扫描器就会继续进行 CVE 比较。也就是说，将依赖项与 CVE 数据库进行交叉匹配。这些数据库由某些组织维护，包含已知的漏洞、它们的严重程度以及已检查的软件版本。验证这些记录对于确定镜像中的哪些软件版本构成潜在风险至关重要。

**第三阶段：生成报告**

在某个扫描软件识别出漏洞后，它会生成扫描报告。这些报告包含检测到的 CVE 的摘要、它们的严重程度以及任何具有中等或重大影响的内容，以及一些补救措施。一些 CVE 扫描器还会推荐安全补丁和升级，而其他配置更改也可能会被建议。

**常用工具**

*   Trivy

    *   一个轻量级、快速的基于 CLI 的扫描器，用于容器、文件系统和存储库。
    *   支持离线扫描，并与 CI/CD 管道良好集成。用法示例：

    ```
    # 使用 Trivy 扫描容器镜像中的漏洞
    trivy image my-app:latest
    ```
*   Snyk

    *   分析开源依赖项并识别新的与 CVE 对齐的威胁。此外，它还提供更相关的安全评估。
    *   代表开发人员在部署过程之前使用 CI/CD 集成来保护应用程序。
    *   可以识别错误的配置以及供应链系统中的弱点。
*   Clair

    *   直接与容器注册表一起工作，以进行持续监控。
    *   使用微服务架构，允许可扩展和自动化的扫描。
    *   支持企业环境的自定义安全策略。

虽然这些扫描器有助于定位漏洞，但它们往往会产生误报、引用过时的 CVE 记录，并使手动集成变得复杂。没有其他公司像 Docker Scout 那样集成 Docker。它提供即时信息，并且集成同时发生。

**有哪些局限性**

*   误报：某些标记的问题可能无法利用。
*   过时的 CVE：基于签名的检测可能会错过零日漏洞。
*   集成问题：某些扫描器缺乏无缝的 CI/CD 支持。

## Docker Scout 简介

Docker Scout 是一款为现代开发者构建的安全工具。它提供更深入的分析和实时更新。与传统扫描器不同，它与 Docker Hub 和 CLI 集成。

**主要特点**

*   实时洞察：使用实时漏洞数据以提高准确性。
*   自动修复：在工作流程中建议依赖项更新。
*   内置 Docker 支持：扫描不需要额外的设置。
*   安全报告：提供包含可操作步骤的易于理解的报告。

## Docker Scout 与其他工具的区别？

凭借实时洞察、自动修复和对 Docker 的内置支持，Docker Scout 使容器安全变得轻而易举。反过来，安全性变成了一种工作流程，而不是一种繁琐的工具。现在，让我们解释一下是什么让 Docker Scout 与众不同。
**完全在 Docker 生态系统中运行**

**Docker Scout:** 无需额外设置；Docker 已自动集成。借助 Docker CLI 和 Desktop，您可以检查安全风险，而无需切换工具。

**其他:** 安全解决方案作为单独的安装、自定义插件和 API 集成添加，这使得一切变得繁琐。

**具有实时安全洞察的实时监控**

**Docker Scout:** [提供 24/7 全天候漏洞检测](https://thenewstack.io/immuta-detect-provides-proactive-reactive-data-security/)和更新。因为它是一个持续扫描工具，所以每当出现新的风险时，它都会跟踪图像并通知您。

**其他:** 例行计划扫描程序会产生时间间隔，在此期间安全系统无法提供任何帮助。

**具有分步指导修复计划的智能修复**

**Docker Scout:** 漏洞检测附带有关如何准确解决问题的指南。它会自动建议更新依赖项并提供更好的基础镜像。

**其他:** 大多数工具除了列出风险并让您处理其余的事情之外，什么也不做。

**对开发人员和安全团队来说超级简单**

**Docker Scout:** 专为开发人员设计，无需安全知识。安全团队获得自动化的洞察力，因此无需手动检查。

**其他:** 其他工具具有糟糕的仪表板，需要安全专家，这会减慢每个人的速度。

**设置安全策略和强制控制**

**Docker Scout:** 指定安全规则并在每个阶段的 CI/CD 管道中自动实施它们。这些确保了每次部署的合规性。

**其他:** 一些工具提供策略执行。但是，其中许多工具通常很困难并且需要大量的手动工作。

**具有 SBOM 可见性的整体供应链安全**

**Docker Scout:** 提供全面的[软件物料清单](https://thenewstack.io/generate-a-software-bill-of-materials-for-a-container-image-with-syft/) (SBOM) 来监控依赖项，因此您可以获得供应链。

**其他:** 许多工具发布 SBOM，但很少有工具能进入开发人员的手中，或者更确切地说是工作流程中。

## 功能对比

**准确性和实时更新**

传统的扫描器依赖于定期的 CVE 数据库更新。另一方面，[Docker Scout 获取实时漏洞](https://thenewstack.io/scan-container-images-for-vulnerabilities-with-docker-scout/)数据。这减少了误报并提高了准确性。

**示例：**

```
12345 |
# Scan an image using Trivy trivy image my-app:latest # Scan using Docker Scout docker scout quickview my-app:latest |
```

**与 Docker Hub 和 CLI 集成**

Docker Scout 与 Docker CLI 和 Docker Hub 原生集成。它可以更轻松地进行扫描，而无需额外的工具。

**示例：**

```
12345 |
# Enable Docker Scout docker scout enable # Run vulnerability assessment docker scout cves my-app:latest |
```

**自动修复建议**

Docker Scout 建议修复漏洞。它提供依赖项更新以获得更安全的镜像。

**示例：**

```
12 |
# View fix suggestions docker scout recommendations my-app:latest |
```

**CI/CD 和 DevSecOps 兼容性**

传统的扫描器需要手动 CI/CD 配置。相比之下，[Docker Scout 可以轻松地与 GitHub Actions](https://thenewstack.io/dockerize-a-rust-application-with-aws-ecr-and-github-actions/) 和 Jenkins 集成。

**示例：** GitHub Actions Workflow

```
123456789101112 |
name: Security Scan 
on: [push] 
jobs: 
  scan: 
    runs-on: ubuntu-latest 
    steps: 
      - name: Check out code 
        uses: actions/checkout@v2 
      - name: Run Docker Scout 
        run: docker scout cves my-app:latest |
```

## 用例：何时选择 Docker Scout 而不是其他扫描器

让我们来看看写作的场景

### Docker Scout 的最佳场景

**将 Docker Hub 用作主要注册表的团队**

Docker Scout 经过自动配置，可以毫无困难地与任何在 Docker Hub 中存储和管理其容器镜像的团队一起工作。

由于它是 Docker 生态系统的一部分，因此可以执行镜像扫描、漏洞监控和情报收集等安全操作，而无需使用外部工具。

将安全性集成到工作流程中，而不会中断业务活动的自然过程，有助于提高效率并节省时间和精力。

**需要实时安全洞察的开发人员**

典型的扫描器基于计划。这些会在更新之间的间隔时间内留下安全支持方面的空白。

然而，Docker Scout 通过监控[图像并主动提供实时漏洞](https://thenewstack.io/check-for-container-image-vulnerabilities-with-trivy/)更新来打破这一常规。它允许开发人员立即采取行动，最大限度地减少部署过时和易受攻击的软件的可能性。它有助于使团队领先于威胁，而不是在损害发生后才做出反应。

**寻求自动化修复的组织**
仅仅识别漏洞只完成了一半的工作；高效地修复它们是另一半。Docker Scout 不仅能检测风险，还能提供智能建议来修复这些风险，例如更改为更安全的镜像以及更新依赖项。

提供这种自动化服务减少了所需的手动工作，并使安全团队能够将精力和注意力集中在其他更重要的任务上，而不必担心容器的安全性。

**何时使用传统扫描器？**

*   当项目需要自定义漏洞数据库时。如果您的团队需要支持自定义源的扫描器，那么像 Snyk 这样的传统工具可能更适合。
*   具有严格的遗留合规性需求的公司。某些行业需要特定的合规性框架。在这里，传统的扫描器可能更有效。
*   不使用 Docker CLI 的环境。Docker Scout 内置于 Docker CLI 中，因此非 Docker 环境可能会更多地受益于独立或传统的扫描器。

**过渡到 Docker Scout**

*   在您的系统上启用 Docker Scout：

    ```
    docker scout enable
    ```
*   对现有镜像运行安全扫描：

    ```
    docker scout quickview my-app:latest
    ```
*   监控漏洞并应用修复程序：

    ```
    docker scout recommendations my-app:latest
    ```

## 结论

容器安全一直很重要，但随着 DevOps 世界的快速发展，它已变得至关重要。毫无疑问，像 Trivy、Clair 和 Snyk 这样的扫描器是有效的。但是，Docker Scout 在集成、自动化和实时洞察力方面优于其他扫描器。

这些无疑是注重安全性的 DevOps 团队的解决方案。它与 Docker 的结合消除了阻碍安全流程的障碍。因此，如果您的团队使用容器，请切换到 Docker Scout，并开始提高安全性和生产力。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。