
<!--
title: 博通押宝VMware版Ubuntu：开发运维双狂喜的秘密
cover: https://cdn.thenewstack.io/media/2025/10/6cb9b0cb-devs-ops-broadcom-2.jpg
summary: Broadcom将Ubuntu整合至VCF，简化云原生开发与运维。开发人员受益于直接访问喜爱的Linux，运维团队获统一管理和安全增强，如削减容器，提升效率与安全性。
-->

Broadcom将Ubuntu整合至VCF，简化云原生开发与运维。开发人员受益于直接访问喜爱的Linux，运维团队获统一管理和安全增强，如削减容器，提升效率与安全性。

> 译自：[Why Broadcom's Ubuntu Bet on VMware Will Delight Devs and Ops](https://thenewstack.io/why-broadcoms-ubuntu-bet-on-vmware-will-delight-devs-and-ops/)
> 
> 作者：B. Cameron Gain

当供应商做出一个既能让开发人员又让运维团队都感到高兴的选择时，这种情况并不常见。但 [Broadcom](https://www.broadcom.com/) [决定](https://blogs.vmware.com/cloud-foundation/2025/08/26/broadcom-canonical-partnership/)将 [Canonical](https://canonical.com/) Ubuntu 直接集成到 [VMware Cloud Foundation (VCF)](https://www.vmware.com/products/cloud-infrastructure/vmware-cloud-foundation) 中，这很可能会解决这两个社区在云原生方面的一些痛点。

对于那些希望继续依赖 Photon OS（已默认提供）的用户，Broadcom 正在通过 Ubuntu 操作系统为平台工程师和开发人员扩展选择。

使用 VCF 的开发人员应该会喜欢直接访问一个由 Canonical 全面维护并由 Broadcom 支持的[备受喜爱的 Linux 发行版](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/)。集成 Linux 驱动、管理更新以及其他运维工作并不是开发人员和管理员希望投入时间的事情。事实上，根据 Atlassian 2024 年的一项调查，开发人员[每周大约要花费一整个工作日来处理此类运维任务](https://thenewstack.io/why-do-developers-lose-1-day-a-week-to-inefficiencies/)。

同时，运维团队将对 VCF 在将工作负载投入生产时的生命周期管理功能表示赞赏。此外，他们将很高兴能够依赖 VCF 和 Ubuntu 的企业级功能，用于安全加固、托管更新及其他运维支持。以前，许多此类任务必须手动处理。

所有这些都基于 VCF 与 Argo CD 的集成，这增加了一个 [GitOps](https://thenewstack.io/webinar/the-state-of-gitops-2025-key-findings-and-what-they-mean-to-you/) 平台，用于直接到 Git 的 [Kubernetes 部署](https://thenewstack.io/streamlining-kubernetes-implementation-with-gitops-best-practices/)。（我们将在另一篇即将发布的文章中探讨 [CI/CD](https://thenewstack.io/introduction-to-ci-cd/) 的这一方面以及 GitOps 方法。）

## 为什么 Ubuntu 是备受喜爱的 Linux 发行版

Ubuntu 是备受喜爱的主流 Linux 操作系统（或发行版），原因有以下几点。它在桌面和服务器上都表现良好，并且附加组件和更新保持一致。特别是在 AI 方面，Ubuntu 非常适合，并且经过精心设计，可托管在 GPU 上运行的 AI 应用程序。

开发人员长期以来一直青睐 Ubuntu。开发人员不希望花费大量时间来确保开发中的应用程序符合合规性和安全规范，或满足产品环境的要求。

## Ubuntu 集成如何减少工作负载和复杂性

以前，在使用 VCF 时，开发人员必须记住他们的应用程序最终需要在 Linux 上运行——通常是 RHEL 或 SUSE Linux 环境。现在，在 VCF 中，开发人员可以直接使用 Ubuntu，从而简化了流程。

削减容器（Chiseled containers）也已推出，并正被[越来越多的采用](https://canonical.com/blog/chiseled-ubuntu-containers-openjre)。这些容器是更轻量的镜像，攻击面更小，安全问题更少。这意味着更少的常见漏洞和暴露（CVE），以及更快、更高效的 CI/CD 流水线。

## 运维团队如何从 VCF 上的 Ubuntu 中受益

对于运维而言，这显然消除了管理多个环境的复杂性。随着流行可靠的虚拟机管理程序和完整私有云堆栈的使用，一切都在 VCF 中统一为一个单一平台。Ubuntu 与 VCF 结合——或由 Canonical 开发的 Ubuntu——简化了运维管理，而不是单独管理不同的系统。它还包括安全更新。

TechTarget 企业战略集团分析师 Torsten Volk 表示，消除操作系统复杂性——特别是内核和用户空间差异——作为难以检测的问题来源，对于开发生命周期至关重要。他指出，Linux 发行版的差异是开发人员面临许多问题的原因，尤其是在云原生应用程序方面。

Volk 表示：“统一的操作系统层有助于 IT 团队简化其补丁和合规性流程，从而减少管理工作量和运营风险。”

## 削减容器增强安全性

与开发人员一样，运维团队也受益于削减容器提供的更小的攻击面。削减容器可以配置为移除运行单个容器不需要的周边库。更少的 CVE 意味着更小的攻击面和更少的攻击者可以利用的漏洞。

在 8 月份的 [VMware Explore 2025 年度用户大会](https://www.vmware.com/explore/video-library/video/6377276035112)上展示了削减容器如何将漏洞从 16 个 CVE 减少到一个，而剩余的问题被确定为误报。还展示了效率提升，容器大小从 200MB 减少到 50MB。这种减少转化为更快的开发周期，因为更少的库意味着更少的测试并降低了依赖复杂性。

## 简化气隙环境中的 AI 部署

该合作关系还通过包含预编译的虚拟化 GPU 驱动程序，最大限度地减少对外部存储库的依赖，从而简化了气隙环境中的 AI 部署。

在气隙系统中进行修补的能力进一步加强了安全性，确保这些环境可以保持封闭。这对于具有严格合规性要求的行业尤其有价值，例如国防、金融和医疗保健，这些行业对安全性的担忧是首要的。不再单独管理 RHEL、SUSE、Ubuntu 和容器镜像，所有内容都整合到一个单一平台中。

Volk 表示：“虽然所有主要的 Linux 发行版都支持气隙修补，但标准化为一个操作系统可以减少镜像和补丁流水线的管理，这为 [站点可靠性工程师] 提供了一套集中的操作手册和控制措施。”

Broadcom 选择 Ubuntu 作为其首选发行版，只是让开发人员和运维团队工作更轻松的又一种方式（同样，Photon OS 仍然可用）。虽然我们尚未同步测试 VCF 和 Ubuntu，但我们可以肯定的是，在 Broadcom 的支持下，VCF 已在其核心功能基础上稳固发展，并仍然是云原生计算的领先平台。

我们也高度依赖 Ubuntu，将其作为我们最喜欢的发行版之一。Broadcom 没有理由不成功实现这一点，这将造福开发人员和运维团队。