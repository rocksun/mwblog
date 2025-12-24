东京 — 那么，您是否想要漫长、漫长——再强调一遍，饱含感情地——*漫长*的 [Kubernetes](https://kubernetes.io/) 长期支持？Canonical 公司为您提供了绝佳方案。

在 [Open Source Summit Japan](https://events.linuxfoundation.org/open-source-summit-japan/) 上，该公司高级芯片联盟经理 Youssef Eltoukhy 透露，Canonical 现在为 Kubernetes 提供长达 15 年的长期支持 (LTS)。此前，这家总部位于英国的 Linux 和开源公司在 2 月份宣布，已将其 [Kubernetes 发行版的支持延长至 12 年。](https://thenewstack.io/canonical-extends-kubernetes-distro-support-to-a-dozen-years/)

具体来说，Canonical 正在将其 Kubernetes 发行版的长期支持延长至多达 15 年，从而将 Kubernetes 维护推向大型机领域。它通过将 Canonical Kubernetes LTS 与其 [Ubuntu Pro](https://ubuntu.com/pro) 和新的 [Legacy 附加组件](https://canonical.com/blog/canonical-expands-total-coverage-for-ubuntu-lts-releases-to-15-years-with-legacy-add-on)相结合来实现这一目标。Legacy 为 Canonical 的 LTS Ubuntu Linux 发行版提供了长达 15 年的扩展付费支持。

对于 Kubernetes 来说，这意味着从 [Kubernetes 1.32](https://thenewstack.io/kubernetes-1-32-aces-api-conformance-testing/) 开始，[MicroK8s](https://canonical.com/microk8s)、[Charmed Kubernetes](https://ubuntu.com/kubernetes/charmed-k8s) 和 [Canonical Kubernetes](https://ubuntu.com/kubernetes) 将获得长达 2040 年的扩展支持。此支持包将在 Canonical 所有支持的平台上线：裸金属、公有云、MicroCloud、[OpenStack](https://www.openstack.org/?utm_content=inline+mention) 和 [VMware by Broadcom](https://www.vmware.com/?utm_content=inline+mention)。

Youssef Eltoukhy 告诉 OSS Japan 的与会者，公司正在将 Ubuntu LTS 模型移植到 Kubernetes 上，并将其描述为将公司“10 多年的定期安全补丁”概念带到容器编排层。

他说，Kubernetes LTS 版本将以两年一次的节奏发布，与 Ubuntu LTS 保持一致，而临时的 Canonical Kubernetes 版本将遵循上游大约四个月的发布节奏，并获得短期维护。

## 响应真实世界的需求

为什么需要如此长的长期支持？毕竟，[红帽](https://www.openshift.com/try?utm_content=inline+mention)仅为 [OpenShift 4.14](https://www.redhat.com/en/blog/announcing-additional-extended-update-support-openshift-414-and-beyond) 及其后续偶数版本 Red Hat OpenShift 4.x 系列发布提供三年的扩展更新支持 (EUS)。

大多数云供应商也提供超出 Kubernetes 项目所提供的支持。例如，[Microsoft Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/products/kubernetes-service) 提供两年的支持，而 [Amazon](https://aws.amazon.com/?utm_content=inline+mention) [Elastic Kubernetes Service (EKS)](https://thenewstack.io/how-amazon-eks-auto-mode-simplifies-kubernetes-cluster-management-part-1/) 提供 26 个月的扩展支持。

Youssef Eltoukhy 表示，Canonical 提供这项服务，是为了应对快速发展的软件即服务 (SaaS) 和人工智能开发人员与银行、医学影像和电信等高度受监管行业之间的紧张关系。

他说，一方面，超大规模和 SaaS 团队希望 Kubernetes 充当一个抽象层，他们可以每隔几个月刷新一次；另一方面，电信运营商则坚称他们希望堆栈在 10 到 15 年内保持不变，同时仍能获得安全修复。

他指出真实的升级周期，以证明上游大约 14 个月的支持窗口与企业实践脱节。“一家北欧银行，当我们说‘顺便说一句，您需要每三到四个月更新一次 Kubernetes’时，他们的回应是‘别开玩笑了！’” Youssef Eltoukhy 说，“‘要更新 Kubernetes，我需要提前六个月做准备。我每两年才能做一次。’”

扩展的 Canonical Kubernetes LTS，结合长期存在的 Ubuntu Pro 和 Legacy 覆盖，被宣传为一种无需强制进行持续破坏性平台重构即可保持这些集群打补丁和合规的方式。

Youssef Eltoukhy 说，这将奏效，因为 Canonical 的生命周期设计遵循每个上游 Kubernetes 发布一个 Canonical Kubernetes 版本，并将每第六个上游发布指定为 LTS。

对于这些 LTS 构建，客户可以在 Ubuntu Pro 下获得至少 12 年的 Kubernetes 安全维护，然后通过 Legacy 附加组件将其延长，为特定的长期部署提供长达 15 年的组合平台支持。

## 稳定性 vs. 灵活性

在开源峰会会议上，Youssef Eltoukhy 描述了希望向前发展的企业如何通过中间版本升级或在 LTS 版本之间跳跃。他强调了在每个新的 LTS 发布后引入的一年宽限期，在此期间，之前的 LTS 将继续获得全面支持，给客户时间做出决定。

他还强调，Canonical 并非重新发明 Kubernetes 本身，而是将其上游的、[云原生计算基金会](https://cncf.io/?utm_content=inline+mention)兼容的 Kubernetes 与自己的工具（如 snaps、charms 和 Cluster API）打包。这些将作为自管理平台或由 Canonical 工程师为 [欧洲航天局 (ESA)](https://www.esa.int/) 等客户运营的完全托管服务提供。

具体来说，在 Kubernetes 方面，Canonical 将 LTS 产品与其新发布的[启用 FIPS 的 Kubernetes](https://canonical.com/blog/canonical-releases-fips-enabled-kubernetes) 变体配对，该变体专为联邦和其他高合规性工作负载设计。这些实体需要经过 FIPS 验证的加密模块和强化指南，例如[国防信息系统局安全技术实施指南 (DISA‑STIG)](https://public.cyber.mil/stigs/)，而不是单独的付费功能。

Youssef Eltoukhy 还强调了 Canonical 为 Nvidia、电信公司和 VMware 等合作伙伴提供并维护幕后开源组件的合作，将公司定位为组件供应链，使内核、用户空间、Kubernetes 和 GPU 运算符在长时间内保持一致并获得支持。

在问答环节中，Youssef Eltoukhy 承认，一个 15 年未触动的堆栈将使任何最终的迁移都成为一项艰巨的任务。尽管如此，他认为对于电信网络基础设施等具有相似寿命的设备和平台，稳定性是优先考虑的因素。他补充说，在许多情况下，硬件本身会在软件支持窗口关闭之前达到生命周期结束。

他还指出，“遗留”窗口期最近应合作伙伴要求从两年扩展到五年。随后，他暗示战略客户的总支持寿命可能会进一步延长，表明 15 年可能不是最终的上限。

目前，Canonical 押注一个能够在 2030 年代末之前保持打补丁和支持的 Kubernetes 发行版将吸引那些厌倦了像一位听众所描述的“每三个月”升级 Kubernetes 的痛苦，转而寻求具有传统基础设施寿命的容器平台的运营商。

YOUTUBE.COM/THENEWSTACK

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。

[订阅](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols，又名 sjvn，自 CP/M-80 是尖端 PC 操作系统、300bps 是快速互联网连接、WordStar 是最先进的文字处理器，并且我们喜欢它以来，他一直在撰写有关技术和技术业务的文章。

[阅读更多来自 Steven J. Vaughan-Nichols 的文章](https://thenewstack.io/author/sjvn/)