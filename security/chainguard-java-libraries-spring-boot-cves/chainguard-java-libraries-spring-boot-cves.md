<!--
title: Chainguard推出即插即用型修复库，靶向解决Java遗留漏洞积压问题
cover: https://cdn.thenewstack.io/media/2026/06/b6dea50f-pawel-czerwinski-lh8vmlcc1ju-unsplash.jpg
summary: Chainguard推出了Java修复库，通过提供带有补丁的库版本，帮助企业在不立即进行复杂版本升级的情况下，解决Spring Boot等生态中遗留的严重漏洞问题，从而降低供应链安全风险。
-->

Chainguard推出了Java修复库，通过提供带有补丁的库版本，帮助企业在不立即进行复杂版本升级的情况下，解决Spring Boot等生态中遗留的严重漏洞问题，从而降低供应链安全风险。

> 译自：[Chainguard targets Java's unpatched vulnerability backlog with drop-in remediated libraries](https://thenewstack.io/chainguard-java-libraries-spring-boot-cves/)
> 
> 作者：Darryl K. Taft

传统的 [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) 企业用户正面临着日益堆积的未修复漏洞。 [Chainguard](https://www.chainguard.dev/) 声称有办法解决这个问题。

本周，该公司宣布 [Chainguard Libraries](https://thenewstack.io/javascript-gets-supply-chain-security-with-chainguard-libraries/) for Java 正式发布，将其 CVE 修复能力扩展至其安全的 [软件供应链](https://thenewstack.io/securing-the-software-supply-chain-a-2035-blueprint/) 产品中。该公司首先从 [Spring Boot](https://thenewstack.io/quarkus-gives-spring-boot-users-a-path-to-serverless-and-live-coding/) 生态系统入手，为 spring-boot、spring-framework、spring-security 和 h2database 中的关键及高危 CVE 提供向后移植（backporting）的补丁。该公司表示，发布时已有数十个 CVE 得到了修复。

## 环境越恶劣，漏洞越多

威胁环境已经变得显著恶化。人工智能辅助的扫描工具正在以惊人的速度生成漏洞报告。

“人工智能工具现在正以每月产生数百份新安全报告的速度扫描开源项目，” Chainguard 资深产品营销经理 [Ross Gordon](https://www.linkedin.com/in/rosscgordon/) 在一篇 [博文](https://www.chainguard.dev/unchained/chainguard-libraries-for-java-is-now-ga-and-includes-cve-remediation) 中写道。“仅在 2026 年 4 月，Spring 就收到了 482 份新报告。”

对于 90% 依赖 Java 构建核心系统的财富 500 强公司来说，这暴露了一个极其棘手的问题。该公司表示，许多组织正在使用旧版本的框架——例如，Spring Boot 2.7 已于 2023 年 11 月停止支持（EOL），其 79 个项目中包含 143 个 CVE，且上游均未提供补丁。

## 三种选择

Gordon 解释说，工程团队通常面临三种选择：

1. **他们可以尝试从安全团队获得使用该库的例外许可。** 然而，这并不能使他们更安全，也无法解决眼前的风险问题。
2. **他们可以尝试自行向后移植 CVE 修复程序。** 然而，这需要耗费数小时，且无法在数百个应用程序和 API 中使用相同易受攻击库的团队之间扩展。
3. **他们可以尝试升级到修复了关键 CVE 的新版本。** 然而，升级可能需要数月（有时甚至一年），并阻碍团队构建推动营收的新产品功能。与第二种选择一样，这也无法扩展，因为每个团队都需要升级到主要版本，同时还要确保在此过程中应用程序不会崩溃。

## 第四条路径

Gordon 解释说，Chainguard 提供了第四条路径。团队只需更新 pom.xml 文件中的单个引用，即可将易受攻击的库替换为 Chainguard 修复后的版本。修复后的软件包包含向后移植的补丁，并以带有 -0.cgr.N 后缀的新版本标识符发布，因此制品在漏洞扫描器和审计员眼中是“干净”的，而不会被标记为已打补丁的易受攻击版本。

Gordon 表示，这种区分对于审计目的非常重要。竞争对手的方法是将补丁覆盖在原始库之上，这会使原始版本标识符在扫描器中可见，从而留下了一个包含已知 CVE 且带有手动修改的尴尬记录。

每个修复后的软件包都附带 [SBOM](https://thenewstack.io/sbom-everywhere-the-openssf-plan-for-sboms/) 和来源证明。Wiz、AWS Inspector、[Grype](https://thenewstack.io/how-to-create-a-software-bill-of-materials/) 和 [Trivy](https://thenewstack.io/teampcp-trivy-supply-chain-attack/) 均可识别 Chainguard 的 Java 修复库，未来计划支持更多扫描器。Chainguard 控制台会显示特定版本中已修复的 CVE、其他包含相同向后移植修复的版本，并提供公告详情链接。修复后的版本也可通过 Chainguard 的公共 [VEX](https://thenewstack.io/vex-standardization-for-a-vulnerability-exploit-data-exchange-format/) 源进行访问。

## 保持安全

Chainguard 的解决方案是，团队可以在当前版本保持安全，同时按照自己的计划完成升级，无需因为已知关键 CVE 的压力而被迫进行匆忙的迁移。对于管理着跨多个团队的数百个应用程序的组织而言，能够应用修复后的直接替换方案而无需协调并行升级，代表了大规模的风险降低。

供应链安全已成为企业软件领域的热门战场之一，而 [Chainguard 一直是扩张覆盖范围最积极的供应商之一](https://thenewstack.io/chainguard-os-packages-containers/)。

该公司 [最初凭借强化容器镜像建立了声誉](https://thenewstack.io/chainguard-its-all-about-that-base-image/)。将这种姿态扩展到 Java 库生态系统，特别是针对财富 500 强企业的 Spring Boot，表明了其旨在解决依赖栈上游漏洞债务的意图。

最后，Ross 补充道：“此公告专门针对 Chainguard Libraries for Java。更广泛地说，Chainguard Libraries 是一个包含 JavaScript、Python 和 Java 依赖项的安全目录，旨在取代工程团队对 [npm](https://thenewstack.io/18-popular-npm-packages-compromised-in-attack/)、[PyPI](https://thenewstack.io/what-developers-can-grok-from-the-latest-pypi-package-attack/) 和 [Maven Central](https://thenewstack.io/how-camunda-automated-dev-releases-to-maven-central/) 的依赖。如今，[Chainguard Libraries for JavaScript](https://thenewstack.io/javascript-gets-supply-chain-security-with-chainguard-libraries/)（如同我们支持的其他语言一样）提供了多层安全控制，包括从源代码构建、冷却期、恶意软件和灰软扫描以及自定义阻止策略。”

Chainguard Libraries for Java 现已可用。