<!--
title: 蜂鸟：红帽版“小而美”系统，比肩Alpine、Ubuntu Chiseled和Wolfi
cover: https://cdn.thenewstack.io/media/2025/11/f7458409-getty-images-njrp-x3anjk-unsplash.jpg
summary: Red Hat 推出 Project Hummingbird，提供微型、零 CVE、带 SBOM 的容器镜像，以加速云原生开发并增强安全性，汲取 Alpine、Ubuntu Chiseled 和 Wolfi 经验。
-->

Red Hat 推出 Project Hummingbird，提供微型、零 CVE、带 SBOM 的容器镜像，以加速云原生开发并增强安全性，汲取 Alpine、Ubuntu Chiseled 和 Wolfi 经验。

> 译自：[Hummingbird: Red Hat's Answer to Alpine, Ubuntu Chiseled, Wolfi](https://thenewstack.io/hummingbird-red-hats-answer-to-alpine-ubuntu-chiseled-wolfi/)
> 
> 作者：Steven J. Vaughan-Nichols

Linux 巨头 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 宣布推出 [Project Hummingbird](https://gitlab.com/redhat/hummingbird/containers) 项目，该项目旨在通过为企业环境提供微型容器镜像来加速云原生开发。

等等，你们中的一些人可能会说，[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 不是在 2018 年收购了 CoreOS 及其最小化的 Linux 发行版 Container Linux 吗？而且，Container Linux 不是明确为容器化工作负载和自动化更新而设计的吗？是的，它是。

## Flatcar Container Linux：专为容器工作负载设计

继续说，Container Linux 已演变为 [Flatcar Container Linux](https://thenewstack.io/flatcar-container-linux-moves-beyond-coreos-roots-with-commercial-editions/)，并且在 2025 年，它现在是 [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) 的一个活跃 [项目](https://thenewstack.io/flatcar-container-linux-hitches-a-ride-with-the-cncf/)。那么，这里有什么新鲜事呢？

根据 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 和 [CNCF](https://cncf.io/?utm_content=inline+mention) 的文档，它们各自扮演的角色是这样的。

[Flatcar Container Linux](https://flatcar-linux.org/) 是一个完整的、不可变的 Linux 操作系统，旨在直接在裸机、虚拟机或云实例上运行容器工作负载。它提供自动操作系统更新、内置容器运行时，并强调系统不可变性，使其成为集群和边缘部署的理想选择。

它被设计为用于大规模编排和运行容器的宿主操作系统，尤其是在 Kubernetes 或托管的 [Oracle](https://www.oracle.com/developer?utm_content=inline+mention) Cloud Infrastructure (OCI) 环境中，这些环境需要管理员拥有健壮、可复现的基础设施。

## 推出 Project Hummingbird：微型容器镜像

Project Hummingbird 提供微型、生产就绪的容器镜像，专注于为企业客户提供极致的简洁性、供应链安全和合规性。Hummingbird 的镜像不是一个完整的 Linux 发行版，而是为容器精心策划的基础镜像，在发布时执行零已知漏洞（CVE）的策略，并默认包含全面的软件物料清单（SBOM）。

它针对 CI/CD 流水线、软件供应链要求以及超小镜像尺寸和透明度至关重要的合规驱动用例进行了优化。

都明白了？很好。

Project Hummingbird 从现代精简的 Linux 发行版（如 [Alpine Linux](https://www.alpinelinux.org/)、[Ubuntu Chiseled Images](https://ubuntu.com/containers/chiseled) 和 [Chainguard Wolfi](https://edu.chainguard.dev/open-source/wolfi/overview/)）中汲取灵感，旨在帮助组织在保持强大的供应链安全和合规标准的同时，加快应用程序交付速度。

## 从 Alpine、Ubuntu Chiseled、Wolfi 中汲取灵感

Project Hummingbird 的方法与 Alpine Linux 类似，其 [musl-libc](https://musl.libc.org/) 的极简设计和在容器部署中小的攻击面。与 Alpine 和像 Wolfi 这样注重安全的替代品一样，Wolfi 是一个强调供应链完整性和细粒度 SBOM 的“非发行版”，Hummingbird 的构建旨在实现快速安全补丁和最小化风险。

Ubuntu Chiseled Images 提供了另一个强有力的类比：使用 [Canonical 的“Chisel”工具](https://github.com/canonical/chisel) ，这些 Ubuntu 版本允许用户精确定制容器基础，从而生成小至 5MB 且仅包含必要运行时依赖项的镜像。

## Project Hummingbird 的关键企业特性

Project Hummingbird 现在以早期访问的形式向 Red Hat 订阅客户提供，作为一组经过加固的、生产就绪的容器镜像。这些镜像基于 [Fedora Linux](https://www.fedoraproject.org/) 组件构建，移除了非必需的软件包，从而减小了攻击面并最小化了潜在漏洞。值得注意的特性包括：

*   **零 CVE 状态**：所有镜像在发货时都没有已知漏洞，并且事先完成了彻底的生产测试，以确保稳定性和可用性。
*   **微型镜像**：核心语言、运行时（如 .NET、Go、Java、Node）、流行数据库（MariaDB、PostgreSQL）和必需的 Web 服务器均以超小镜像形式提供，以减少集成工作和资源使用。
*   **完整的 SBOM**：每个镜像都包含一个完整的软件物料清单，支持合规需求和透明审计。

企业支持：在通用可用性（GA）时，将通过 Red Hat 订阅提供全面的支持，并以类似于 Red Hat UBI 的模型提供免费、可再分发的镜像。

正如 [Red Hat Enterprise Linux (RHEL) 的 Red Hat 总经理 Gunnar Hellekson](https://www.linkedin.com/in/gunnarhellekson/) 在声明中所说，“Project Hummingbird 旨在通过提供一个最小化、可信赖且透明的零 CVE 基础来构建云原生应用程序，从而消除‘快速移动与维护安全’之间的权衡。”

“这限制了漏洞，因此开发和 IT 安全团队可以通过速度、敏捷性、安全性和安心感，直接走向业务价值。”

## Red Hat 对安全云原生企业 Linux 的愿景

Project Hummingbird 试图将 Red Hat 定位为下一代安全、云原生企业 Linux 演进中的主要参与者。

凭借其零 CVE 承诺、生产就绪的最小化镜像以及与企业工作流程的深度集成，该计划为在日益增长的供应链威胁中采用容器化工作负载的组织提供了一个引人注目的替代方案。