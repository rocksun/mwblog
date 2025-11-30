亚特兰大 — [博通](https://thenewstack.io/why-broadcoms-ubuntu-bet-on-vmware-will-delight-devs-and-ops/) 利用 [KubeCon + CloudNativeCon 北美](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 大会消除了人们对其削减开源支持的担忧，强调了对 [VMware](https://tanzu.vmware.com?utm_content=inline+mention) 开发项目的持续支持，并公布了对 [云原生计算基金会 (CNCF)](https://cncf.io/?utm_content=inline+mention) 的进一步贡献。

博通的 [VMware Cloud Foundation (VCF)](https://www.vmware.com/products/cloud-infrastructure/vmware-cloud-foundation) 工程师和开发人员一直持续为开源做贡献，博通仍然是 CNCF 五大开源贡献者之一，也是 [Kubernetes](https://thenewstack.io/kubernetes/) 的主要贡献者。

## 加大投入

在 KubeCon + CloudNativeCon 北美大会上，博通 VMware 的代表们试图向社区保证，他们正在加大对开源的支持和贡献。

博通 VCF 部门产品营销副总裁 Prashanth Shenoy 在一次媒体和分析师吹风会上表示，博通正在“加倍投入”开源。他描述了正在做出的新贡献，包括在与 Kubernetes 相关的关键开源领域更积极地工作。

这些云原生贡献包括诊断工具、增强功能和操作特性，可帮助 VCF 支持分布式环境中的 Kubernetes 集群。这些努力使客户能够利用现代开发者服务、基础设施即服务 (IaaS) 服务和原生集成到 VCF 中的开源功能。

一个关键贡献是将 etcd-diagnosis 工具捐赠给 CNCF。该工具能够对集群配置、状态和健康一致性进行自动化分析，帮助操作员快速识别 etcd（Kubernetes 的记录系统）中的潜在问题。博通还开发了 etcd-recovery，一个开源配套工具，旨在简化 etcd 集群失去仲裁时的恢复。这些工具共同减少了手动、易出错的过程，并提高了 Kubernetes 环境的可靠性和稳定性。

另一个重点是开源 [Cluster API (CAPI)](https://thenewstack.io/is-cluster-api-really-the-future-of-kubernetes-deployment/)，它解决了管理多个 Kubernetes 集群整个生命周期的复杂性。通过使用声明式、Kubernetes 风格的 API，CAPI 自动化了集群调配、升级和日常管理，使组织能够以更一致的方式、更低的开销操作集群舰队。这种标准化使团队能够专注于交付应用程序，而不是管理基础设施。

此外，Harbor（最初由 VMware 开发）继续作为安全存储容器镜像和工件的开源行业标准。作为可信的云原生注册表，它确保应用程序镜像以强大的安全性、合规性和性能能力进行管理，使其成为构建和部署现代云原生应用程序的组织的基础组件。

博通首席工程师 Nabarun Pal 和博通软件工程师 Arka Saha 在他们的会议演讲“Kubernetes 和 etcd：常见陷阱及规避方法”中讨论了影响 Kubernetes 稳定性和性能的 etcd 故障的常见原因。他们详细介绍了如何改进运行中集群中 etcd 的诊断。在演讲中，他们涵盖了操作 etcd 的最佳实践，包括升级、备份、恢复以及确保弹性控制平面的关键变通方法。

TechTarget 企业战略集团分析师 Torsten Volk 此前曾以顾问身份与 ReveCom 合作，他告诉我，虽然博通根据 ReveCom、ESG 和 CNCF 指标是 Kubernetes 的顶级贡献者，但这些统计数据并未说明全部情况。

Volk 说：“纯粹的贡献数量往往不如其背后的实际策略有意义。”“这种策略需要在为上游社区做贡献和为公司自身软件产品组合添加集成之间取得平衡。”

Shenoy 在媒体和分析师吹风会上表示，VMware 历史上对开源的承诺，现在在博通的支持下得到了加强，确保客户可以依赖 VCF 作为运行 Kubernetes 的强大平台，同时符合 CNCF 认证的 Kubernetes AI 平台合规性计划等开放社区标准。

Shenoy 解释说：“博通是首批通过此计划认证的供应商之一，保证 VKS 上的 AI 工作负载符合社区定义的 API、配置和基础设施能力标准。”

市场研究表明，客户将开源项目视为其转型战略的关键要素。Volk 表示，用户从解决特定问题并持续支持这些解决方案的社区中受益匪浅，因为他们自己的业务依赖于这种支持。换句话说，VCF 的信誉和博通优化 VCF 以满足客户需求变化的能力。这将取决于博通能否像传统上那样，继续与开源社区紧密合作，开发和调整 VCF 以适应不断变化的需求。

Volk 说：“因此，可信的开源参与是博通 VMware 在平台竞争中取得成功的关键。”“除了完全专注于将 Kubernetes 与其自身平台集成的贡献外，公司的上游贡献也发挥着作用。”