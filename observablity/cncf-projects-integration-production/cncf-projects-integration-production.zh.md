我仍然记得我们第一次为了一个并非 Bug 的问题而彻夜难眠的情景。

那是某个周二。Grafana 仪表板显示 Cilium 网络指标的面板全是空白。Hubble 运行正常——DNS 可视化、TCP 流和 HTTP 延迟在 Hubble UI 中一应俱全。但凌晨 2 点盯着 Grafana 的值班工程师却什么也看不见。原因何在？Prometheus 没有连接到 Cilium agent 和 operator Pod 的 ServiceMonitors。两个[云原生计算基金会](https://www.cncf.io/) (CNCF) 项目虽然都安装正确，却彼此完全“隐身”。

这就是所谓的“集成税”。它是[在生产环境中同时运行多个](https://thenewstack.io/the-hidden-costs-of-multiple-service-catalogs-in-development/) CNCF 项目的隐形成本，也是大多数平台团队花费 80% 时间的地方——不是在安装项目，也不是在单独调优它们，而是在进行编排对接。只有这样，它们才能真正地相互通信。

> “这就是所谓的集成税。它是生产环境中运行多个 CNCF 项目的隐形成本。”

## 每个团队都在构建相同的堆栈，却以不同的方式崩溃

CNCF [全景图](https://landscape.cncf.io/?group=projects-and-products&view-mode=grid)拥有约 250 个项目。在实践中，大多数生产环境的 [Kubernetes](https://kubernetes.io/) 平台最终都会选择由 20–30 个云原生工具组成的核心堆栈。用于监控的 [Prometheus](https://prometheus.io/)，用于 GitOps 的 [ArgoCD](https://argoproj.github.io/cd/)，用于网络的 [Cilium](https://cilium.io/)，用于 TLS 的 [cert-manager](https://cert-manager.io/)，用于备份的 [Velero](https://velero.io/)，用于凭证管理的 [Sealed Secrets](https://fluxcd.io/flux/guides/sealed-secrets/)，以及用于策略的 [Kyverno](https://kyverno.io/)。你安装它们，编写 values 文件。

编排对接完成了。接着故障就开始了，而且这些故障永远不会出现在任何单个项目的 Issue 追踪器里。

## CNCF 项目碰撞的地方

**cert-manager 对阵 Ingress 控制器。** 我们在三个云提供商那里都遇到了这个问题。cert-manager 的 HTTP-01 ACME 挑战期望通过纯 HTTP 提供令牌。但如果你的 Ingress 控制器强制执行全局 HTTP 到 HTTPS 的重定向（出于安全考虑理应如此），那么每个 ACME 验证请求在到达 cert-manager 的 solver Pod 之前都会收到 301 重定向。证书续订会静默失败。直到客户在浏览器中看到 TLS 过期警告时，你才会发现。修复方法？通过 Route53、Cloud DNS 或 Azure DNS 进行 DNS-01 挑战。但那是特定于云平台的 IAM 权限范围，没有任何 Helm chart 会默认配置。你只有在事故发生后才会发现这些限制。

**Prometheus 对阵 kubelet。** 这是一个让我们花了数周时间才诊断出来的案例。kubelet 在四个抓取路径上暴露指标。其中两个——`/metrics` 和 `/metrics/probes`——都会发出带有相同时间戳的 `process_start_time_seconds`，因为它们属于同一个进程。Prometheus 尽职地抓取了这两个路径，发现了重复样本，并触发了 `PrometheusDuplicateTimestamps` 告警。告警吵闹不堪。如果不阅读 kubelet 源码，根本无法发现根本原因。而修复方法是一个 Jsonnet 重打标签（relabeling）规则，用于丢弃整个抓取端点。这些都不是 Bug。每个项目都完全按照文档运行。故障存在于缝隙之中。

> “这些都不是 Bug。每个项目都完全按照文档运行。故障存在于缝隙之中。”

## Cluster API 为四种云提供了统一的工作流

在 [Cluster API](https://github.com/kubernetes-sigs/cluster-api) (CAPI) 出现之前，配置集群意味着选择云厂商的 CLI。AWS 用 `eksctl`，GCP 用 `gcloud container clusters create`，Azure 用 `az aks create`。每一个都有自己的生命周期模型、升级路径和灾难恢复方案。你不仅被锁定在某个云平台上，还被锁定在了该平台管理 Kubernetes 的理念中。

CAPI 改变了游戏规则。你的集群现在是一组 Kubernetes 原生资源——Cluster、MachineDeployment、MachinePool——而特定于云的提供程序（provider）会将它们转换为基础设施。我们在 AWS 上运行 CAPA，在 GCP 上运行 CAPG，在 Azure 上运行 CAPZ，在 Hetzner 裸机上运行 CAPH。引导序列在任何地方都是相同的：K3D 管理集群 -> 部署提供程序 -> 创建工作负载集群 -> `clusterctl move` 使其实现自我管理。

但真正的价值在于：Day-2 运营。Kubernetes 版本升级变成了对 `MachineDeployment` 的一行修改。CAPI 处理封锁（cordon）、排空（drain）和滚动替换。`MachineHealthCheck` 会自动移除不健康的节点。灾难恢复意味着重建管理集群，从[云存储还原 Velero 备份](https://thenewstack.io/a-practical-guide-to-kubernetes-stateful-backup-and-recovery/)，并让 CAPI 资源进行调解（reconcile）。整个集群会根据 Git 状态自行重建。在这里，Cluster API——就像 CNCF 堆栈的其余部分一样——会揭示你的集成工作是否真的能在压力下保持稳固。

## 终于止血的架构

在经历了多年跨云集成失败的“救火”之后，我们最终确定了一个让事情变得可持续的模式：双仓库 GitOps 分离。无论你是使用商业平台还是从开源项目构建自己的堆栈，这种方法都适用。

**平台仓库 (Platform repo)：** 包含 100 多个经过生产测试默认值的 Helm chart。每个 chart 中都植入了 Cilium NetworkPolicies。预先连接了 Prometheus ServiceMonitors。为正确的挑战类型配置了 cert-manager 注解。此配置在所有云平台的所有集群中共享。

**配置仓库 (Config repo)：** 每个客户或环境一个。只包含集群之间真正不同的值：域名、节点数量、GCP 项目 ID、AWS 角色账号和 Hetzner 服务器类型。

ArgoCD 同时监控这两个仓库。当我们在平台仓库中修复了 Prometheus 重复时间戳问题时，该修复会通过版本更新传播到每个集群（AWS、GCP、Azure、裸机）。一次 Pull Request。无需为每个集群创建工单。不需要人肉记忆“哦，我们需要更新三个不同系统的重打标签规则”；集成逻辑存在于代码中。

## 来自生产环境的沉重教训

**生成监控，而不是手动组装。** 我们使用 Jsonnet 从单个集群变量文件生成整个 kube-prometheus 堆栈。自定义告警 Mixins——如 Velero 备份时长、[CloudNativePG](https://cloudnative-pg.io/) 复制延迟、kubelet 证书到期——作为 Jsonnet 库与上游规则并存。单个 build.sh 脚本产出所有内容。可复现、可 Diff、版本化。当 Prometheus 升级破坏你的自定义规则时，差异会立即显现，且修复在进入生产环境前是可测试的。

**将 NetworkPolicies 嵌入 Chart，而不是放在部署后的操作手册里。** 我们在 20 多个 Helm chart 中提供 Cilium NetworkPolicy 模板。每个 chart 声明自己的出站需求：调用哪些外部 API 以及需要哪些内部服务。部署后通过 Hubble 流日志反向工程网络规则，就像发布后再写测试一样。你的策略会发生偏移，安全变成了猜谜。将它们嵌入 chart 意味着策略存在于其维护的地方。

**在引导时自动化灾难恢复。** 我们的配置过程会在初始集群设置期间创建用于 Velero 备份的云存储桶（S3、GCS、Azure Blob），而不是作为留在 Jira 工单里拖上半年才做的后续任务。如果你能运行引导程序，你就能从整个集群丢失中恢复。灾难恢复不再是一种愿望，而是一个可测试的现实。

**加密密钥，然后提交。** 每一个凭证——部署密钥、云 IAM 和 TLS 证书——在进入 Git 之前都会使用 Sealed Secrets 进行加密。解密密钥会备份到云存储。你的 Git 仓库变成了每个集群状态（包括密钥）的完整、可审计记录。漂移检测有效，恢复只需一个 Pull Request 和一次 clusterctl move。

**让机器强制执行策略。** Kyverno 会拦截缺少资源限制（resource limits）的部署。Kubescape 持续扫描 CIS 基准并将违规情况汇总到 Prometheus 告警中。结合 Cilium 网络分段，你的安全态势变成了审计员可以通过 Git 历史和实时集群状态验证的东西——而不是两个季度前最后更新的电子表格。

## 滚雪球般的成本

[集成税](https://thenewstack.io/virtual-clusters-kubernetes-cost-isolation/)并不是一次性费用。每一次 Kubernetes 版本更新、每一次 Helm chart 升级以及每一个新的 CNCF 项目都会引入新的集成界面。如果你的监控是手工编写的 YAML，将 kube-prometheus 从 v0.13 升级到 v0.17 意味着要手动对比数百个生成的工程文件。如果是 Jsonnet，只需一行代码——债务就在这里复合增长。

CNCF 生态系统异常强大。但没有集成的力量只是一堆 Helm 安装列表。真正重要的工作——漂移检测、协调更新和灾难恢复自动化——发生在编排对接中。那是你的平台要么熬过第二年，要么沦为你不再信任的工具集合的分水岭。

*有兴趣进一步探索本文讨论的框架的读者，可以在 [KubeAid 仓库](https://github.com/Obmondo/kubeaid)和 [KubeAid 网站](https://kubeaid.io/)上找到项目的源代码和详细文档。*