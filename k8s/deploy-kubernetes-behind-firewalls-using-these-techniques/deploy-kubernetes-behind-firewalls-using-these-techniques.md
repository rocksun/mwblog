
<!--
title: 在防火墙后部署Kubernetes的技术
cover: https://cdn.thenewstack.io/media/2024/10/d12e571b-growtika-9cxmjhavitm-unsplash-scaled.jpg
-->

防火墙环境下部署和管理 Kubernetes 的可行策略

> 译自 [Deploy Kubernetes Behind Firewalls Using These Techniques](https://thenewstack.io/deploy-kubernetes-behind-firewalls-using-these-techniques/)，作者 Mohan Sitaram。

随着 Kubernetes 和云原生系统成为部署和管理现代应用程序的事实标准，它们扩展到受限或防火墙环境带来了独特的挑战。这些环境通常受监管合规性、安全问题或组织政策驱动，这些因素带来了架构、运营和安全方面的障碍。本文深入探讨了在防火墙后部署 Kubernetes 集群的复杂性，提供了克服这些障碍的解决方案和策略。

防火墙或受限环境限制了外部互联网 [访问以确保数据安全](https://thenewstack.io/data-engineering-survey-shows-security-access-challenges/) 并保护系统免受未经授权的入侵。这些环境在金融、医疗保健和政府等具有严格监管要求的行业中很常见。在这些环境中，通常只允许特定类型的流量，并且需要严格的监督。虽然这些控制措施增强了安全性，但它们为 Kubernetes 等现代云原生基础设施带来了重大挑战，而 Kubernetes 依赖于互联网访问才能实现集群管理、镜像拉取和外部 API 通信等功能。

**在防火墙环境中部署 Kubernetes 的挑战**

1. **镜像管理和分发**：Kubernetes 应用程序需要从容器注册表（如 Docker Hub、gcr.io 或 quay.io）提供容器镜像。在防火墙环境中，访问这些注册表通常受到限制或完全被阻止。这可能会阻止镜像拉取，从而阻碍应用程序的部署和升级。

**解决方案**：为了解决这个问题，企业可以使用具有存储库复制或拉取缓存功能的注册表，在防火墙内本地托管容器镜像。这些注册表可以以受控方式复制或从外部注册表拉取镜像，确保必要的容器镜像可用，而无需持续访问互联网。Harbor 等注册表为这些环境提供了安全的内部镜像存储库。此外，利用镜像提升工作流可以确保只有经过验证的外部来源镜像才能进入安全注册表。

我使用过的另一种方法是通过网关或代理服务器复制镜像，该服务器与源注册表和目标注册表都具有连接性。当源注册表和目标注册表的 capabilities 未知时，此解决方案可能有效。imgpkg、crane 或 skopeo 等工具可以在跨越防火墙边界的注册表之间复制镜像。例如，imgpkg 打包格式将应用程序的 helm 图表及其容器镜像捆绑为一个单元。imgpkg 捆绑包可以从源注册表导出为 tar 存档到代理服务器的本地文件系统。然后，此 tar 存档可以推送到防火墙后的注册表，imgpkg 确保捆绑包中应用程序的 helm 图表中的注册表引用会自动更新为指向目标注册表。

2. **集群管理和控制平面访问**：Kubernetes 的控制平面（API 服务器等）必须与工作节点和外部云 API 通信才能管理集群。但是，在防火墙环境中，外部 [访问这些 API 或控制](https://thenewstack.io/3-frameworks-for-role-based-access-control/) 平面组件通常被阻止或限制，这对监控、扩展和控制集群提出了重大挑战。

**解决方案**：组织可以建立反向代理和 VPN 隧道技术来克服这个问题。部署在非军事化区域 (DMZ) 中的反向代理可以处理来自防火墙内的 API 请求，同时提供安全的入口点。此外，堡垒主机和 VPN 网关可以允许对 Kubernetes 控制平面进行受控的、安全的访问。这些主机位于内部网络之外，但充当受限环境和外部服务之间的桥梁，允许管理员与集群交互，而不会违反防火墙策略。

例如，Azure 允许创建部署在企业私有网络中的“私有” AKS 集群。出于安全原因，默认情况下，对私有 AKS 集群的控制平面的访问受到限制。但 Azure 还提供 Azure Bastion 等解决方案，该解决方案提供从外部世界安全访问私有集群。用户通过本地计算机上的 RDP 或 SSH 连接到 Azure Bastion，并可以通过代理访问私有集群。Bastion 负责保护到私有集群的流量。

3. **外部依赖和 DNS 解析**：有时，在隔离的 Kubernetes 集群中运行的应用程序可能需要拉取外部依赖项，为此它可能需要解析防火墙外部的主机名。从 Pod 内部可能无法直接访问公共 DNS（如 Google DNS 或 Cloudflare DNS），并且应用程序可能无法拉取依赖项并无法启动。这将迫使组织或应用程序开发人员在防火墙内解决依赖项，而这可能并非总是可行。

**解决方案**：在 CoreDNS 中使用 DNS 转发。CoreDNS 是 Kubernetes 集群中的默认 DNS 解析器，可以配置为从防火墙内部解析外部 DNS 查询。可以修改 CoreDNS 以将 DNS 查询转发到特定主机名（如 www.example.com）到外部解析器，并将所有其他查询解析到防火墙内。这可以通过使用“forward”CoreDNS 插件来完成，将 [www.example.com](http://www.example.com) 的查询转发到 Google 或 CloudFlare DNS，并将所有其他内容（用“.”表示）转发到本地解析器，只需将它们指向 /etc/resolv.conf 即可。这确保了关键的 DNS 解析不会被防火墙策略阻止，并且还允许防火墙管理员通过仅允许特定外部查询来保持网络安全。

4. **更新、补丁和 Kubernetes 组件**：定期更新和修补 Kubernetes 组件对于维护安全、合规性和性能至关重要。但是，在防火墙环境中，自动更新可能会被阻止，[使集群容易受到安全风险的攻击](https://thenewstack.io/dont-leave-your-apis-undefended-against-security-risks/)。

**解决方案**：使用本地镜像和内部容器注册表来更新集群。Kubernetes 安装工具（如 Kubespray）允许在离线环境中进行集群管理。通过 Kubespray 安装和修补 Kubernetes 需要访问静态文件（如 kubectl 和 kubeadm）、操作系统包以及核心 Kubernetes 组件的一些容器镜像。静态文件可以通过在防火墙内运行 nginx/HAproxy 服务器来提供。操作系统包可以通过部署 yum 或 Debian 存储库的本地镜像来获取。Kubespray 所需的容器镜像可以通过运行本地实例的“kind”或 docker 注册表来提供，这些注册表中预先填充了镜像。
此外，公司可以使用持续集成/持续交付 (CI/CD) 管道以受控方式处理更新，在将更改推广到生产集群之前，在暂存集群上进行本地测试和验证。GitOps 是 CI/CD 的一个子类别，它会自动将更改部署到目标环境，这些更改由对 Git 存储库的提交触发。暂存和生产集群可以映射到不同的 Git 分支，并且可以通过首先将更改提交到暂存分支，对其进行彻底测试，然后才将相同的更改提交到生产分支来策略性地推出升级和补丁。这确保了集群即使没有自动更新也能使用最新的安全补丁。

5. **第三方集成和监控**：现代 Kubernetes 应用程序通常依赖于第三方集成（如 Datadog）和外部[存储解决方案（如 AWS S3 或 Google Cloud）](https://thenewstack.io/cloud-native/the-most-popular-cloud-native-storage-solutions/)存储。在防火墙环境中，出站流量受到限制，阻止了与这些云托管服务的直接通信。

**解决方案**：组织可以在其防火墙环境中部署自托管的替代方案来维护[可观察性和监控](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/)。例如，可以在内部部署 Prometheus 和 Grafana 来处理指标和可视化，而分布式存储解决方案（如 Ceph 或 MinIO）可以替换外部云存储。这些工具可以复制外部服务的功，同时确保所有数据安全地保留在防火墙内。自托管替代方案的容器镜像和 helm 图表可以使用前面概述的镜像管理和分发技术拉取到隔离的环境中。

6. **安全策略和合规性**：安全和合规性问题通常是将 Kubernetes 部署到防火墙环境中的主要原因。医疗保健和金融等行业需要严格遵守 HIPAA 和 PCI-DSS 等法规，这些法规要求使用安全的环境，并限制对敏感数据的访问。

**解决方案**： Kubernetes 的原生功能，例如 Pod 安全策略 (PSP)、基于角色的访问控制 (RBAC) 和网络策略，可以用来增强防火墙环境中 Kubernetes 集群的安全性。此外，部署 [像 Istio 这样的服务网格](https://thenewstack.io/istio-1-23-drops-the-sidecars-for-a-simpler-ambient-mesh/) 或 Linkerd 可以提供细粒度的流量控制和安全性，确保只有授权的服务才能进行通信。这些网格还提供双向 TLS (mTLS) 用于加密微服务之间的流量，进一步增强安全性并符合法规。

7. **入口控制和负载均衡**：在防火墙环境中，外部负载均衡服务（如 AWS ELB 或 GCP 负载均衡器）可能不可用，导致将流量路由到 Kubernetes 集群中运行的服务变得困难。Kubernetes 的内置 NodePort 类型服务不安全，因为它们需要在所有 Kubernetes 节点上打开一个非标准端口。每个需要在集群外部公开的服务都需要一个单独的 NodePort 服务，从而使防火墙管理变得复杂。

**解决方案**：为了在集群外部公开服务，像 Istio 或 Contour 这样的入口网关可以充当代理，将流量路由到这些服务。它们保护对内部服务的访问，因为它们可以终止 TLS 流量并充当所有需要公开的服务的单一入口点。

私有负载均衡解决方案，如 MetalLB，可以部署以提供入口网关的 IP/主机名的高可用性。使用 MetalLB 和入口网关的组合可以提高安全性。只有一个 IP 地址/主机名需要保护，并且所有暴露服务的网络流量都将被加密。

在防火墙环境中部署和管理 Kubernetes 会带来独特的挑战，从镜像管理和控制平面访问到 DNS 解析和第三方集成。但是，通过正确的策略和工具，组织可以利用 Kubernetes 的强大功能，同时保持防火墙基础设施所需的安全性、合规性和运营稳定性。容器注册表镜像复制、特定查询的 DNS 转发、VPN 隧道、入口网关和自托管监控工具等技术确保 Kubernetes 即使在最受限制的环境中仍然是一个可行的解决方案。

旨在采用 [云原生技术](https://thenewstack.io/cloud-native/) 的组织必须仔细设计其基础设施，确保满足安全要求，而不会牺牲 Kubernetes 提供的可扩展性和灵活性。通过利用上述解决方案，Kubernetes 集群即使在高度受限的环境中也能有效运行。
