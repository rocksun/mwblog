
<!--
title: Canonical宣布12年的Kubernetes LTS
cover: https://ubuntu.com/wp-content/uploads/d18a/Kubernetes_12_year_LTS_featured_image.png
-->

Canonical 发布 12 年 Kubernetes LTS 版本，增强企业软件基础设施安全性并简化操作

> 译自 [Canonical announces 12 year Kubernetes LTS | Canonical](https://canonical.com/blog/12-year-lts-for-kubernetes)，作者 Canonical Ltd; Canonical。

Canonical 的 Kubernetes LTS（长期支持）将支持 FedRAMP 合规性，并在裸机、公共云、OpenStack、Canonical MicroCloud 和 VMware 上获得至少 12 年的承诺安全维护和企业支持。

**2025 年 2 月 11 日** 今天，Canonical 宣布了一项为期 12 年的安全维护和支持承诺，从 Kubernetes 1.32 开始。新版本易于安装、操作和升级，具有一流的开源网络、DNS、网关、指标服务器、本地存储、负载均衡器和入口服务。Canonical Kubernetes 使客户能够按照自己的节奏进行升级，对于喜欢快速发展的组织，每四个月发布新的上游版本，对于需要长期支持环境的组织，则提供 12 年的承诺。

“持续的 Kubernetes 升级会耗尽企业团队的精力。部署 Canonical Kubernetes 1.32 LTS 的客户可以专注于未来，因为他们的集群将在整整 12 年内收到安全更新，”Mark Shuttleworth 说。“结合涵盖最广泛的开源应用程序的 Ubuntu Pro ，现在可以更有信心地运行整个开源堆栈，并且更简单地符合 FedRAMP 等强化标准。从公共云到数据中心再到边缘，在服务器和工作站以及连接的设备上，我们很高兴提供一种简单的‘部署并向前发展’的企业级容器方法，使业务重点放在应用程序和创新上，而不是基础设施上。”

Canonical Kubernetes 是一种多云发行版，为开发者工作站、云、数据中心和边缘部署提供统一的生产级 Kubernetes 体验。MicroK8s 和 Charmed Kubernetes 的未来版本将基于 Canonical Kubernetes 构建，并也将获得 12 年的 LTS。客户还可以使用独立的 Canonical Kubernetes LTS 二进制文件和容器镜像来编排他们的 Kubernetes 集群，并获得 Canonical 的全面企业支持。

## 长期支持和最新的上游 Kubernetes

上游 Kubernetes 的发布周期节奏很快，每四个月发布一个新版本，并提供 14 个月的安全维护。频繁的 Kubernetes 版本升级会中断业务连续性，并需要耗时且昂贵的维护。与此同时，Kubernetes 的创新步伐使较新的版本对开发人员和新的部署具有吸引力。

Canonical 将每四个月提供其 Kubernetes 软件包的临时版本，与上游 Kubernetes 的发布节奏和版本保持一致。这些临时版本将获得 14 个月的安全维护和支持，并提供从一个版本到另一个版本的升级路径。

与 Ubuntu 类似，Canonical 将每两年发布一次 Kubernetes 的 LTS 软件包，从 Canonical Kubernetes 1.32 LTS 开始。通过 Ubuntu Pro 订阅，这些 LTS 版本将获得至少 12 年的 CVE 安全修复。此后，Canonical 将继续根据客户对电信和其他关键基础设施中超长寿命部署的需求，支持和修补这些 Kubernetes 版本。

通过这种方式，Canonical 对 Kubernetes 的打包和 LTS 承诺既能使快速发展的部署和开发人员快速获取最新的上游版本，又能为需要多年保持稳定的生产部署提供长期维护。

## 一流的开源

Canonical Kubernetes 附带一流的开源组件，用于基本功能，并且仅使用标准的 Kubernetes 抽象和 API 来实现完全的 Kubernetes 一致性。这使平台能够以最小的用户中断发展到更新的实现。Canonical Kubernetes 1.32 LTS 将默认提供 Cilium、MetalLB、CoreDNS、OpenEBS 和 Metrics Server。客户可以在极少数需要这样做的情况下替换这些组件，并且 Canonical 提供的元素仍将受到支持。

Canonical 还将提供流行的 Kubernetes 生态系统服务的标准化容器镜像，例如 Istio、Cert Manager 或 OpenTelemetry Collector——同样具有 12 年的安全和支持承诺。客户可以通过 [Everything LTS](https://canonical.com/blog/canonical-offers-12-year-lts-for-any-open-source-docker-image) 产品组合请求将其他开源组件添加到此 Kubernetes 生态系统产品组合中。

## 易于在各种环境中安装和操作

DevOps 团队通常在应用程序开发和部署生命周期中使用不同的 Kubernetes 发行版或版本。当工作负载从开发转移到测试再到生产时，这些环境之间的任何差异都是摩擦、成本和错误的根源。

Canonical Kubernetes 在整个软件生命周期中提供了一种简单的、低接触的操作方法。相同的软件包在开发者工作站环境、小型集群，甚至更大、更复杂的场景中提供相同的 API。

对于单节点或较小的多节点集群，Canonical Kubernetes 的安装只需每个节点两条命令。这些集群将自动更新，仅包含该版本的维护生命周期内的安全修复程序，使其成为边缘和工作站的简易解决方案。

Canonical Kubernetes 也可以在更复杂的环境中进行编排，以实现自定义存储、网络（包括满足电信需求的 Multus）以及用于 AI/ML 训练和模型服务的 GPU。它还通过 Juju 提供集群生命周期自动化，并可以集成其他 [Canonical 基础设施](https://canonical.com/solutions/infrastructure) 堆栈组件。

“Canonical Kubernetes 平台让您可以自由地以自己的方式操作 Kubernetes，”Canonical Kubernetes 产品经理 Marcin Stożek 说。“它使您可以在自动集群升级或保持长期支持版本以获得更长的稳定性之间进行选择。通过可靠的安全维护、生命周期自动化和其他开源组件来解决 Kubernetes 的主要挑战之一——基础设施复杂性，我们简化了所有用户的云原生平台操作。”

## 可用性

Canonical Kubernetes 1.32 LTS 目前已发布，可供生产使用。有关更多信息，请访问 [https://ubuntu.com/kubernetes](https://canonical.com/kubernetes)。

我们新的 Kubernetes 产品的文档可在 [https://documentation.ubuntu.com/canonical-kubernetes](https://documentation.ubuntu.com/canonical-kubernetes) 上找到。

要了解有关 Canonical 基础设施组合的更多信息，请访问 [https://canonical.com/solutions/infrastructure](https://canonical.com/solutions/infrastructure)。

Canonical Kubernetes 的安全维护和支持可以通过 Ubuntu Pro 订阅购买。请访问 [https://ubuntu.com/pro](https://canonical.com/pro) 了解更多信息。

## 关于 Canonical

Ubuntu 的发布者 Canonical 提供开源软件、安全、支持和服务。产品组合涵盖关键系统，从最小的设备到最大的云，从内核到容器，从数据库到 AI。
