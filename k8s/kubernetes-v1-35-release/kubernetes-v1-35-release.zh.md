# Kubernetes v1.35: Timbernetes（世界之树版本）

作者

**[Kubernetes v1.35 发布团队](https://github.com/kubernetes/sig-release/blob/master/releases/release-1.35/release-team.md)**

|

2025年12月17日 星期三

**编辑**: Aakanksha Bhende, Arujjwal Negi, Chad M. Crowell, Graziano Casto, Swathi Rao

与之前的版本类似，Kubernetes v1.35 版本引入了新的稳定版、测试版和 Alpha 功能。持续交付高质量版本凸显了我们开发周期的强大实力以及社区的积极支持。

此版本包含 60 项增强功能，其中包括 17 项稳定功能、19 项测试功能和 22 项 Alpha 功能。

此版本还有一些[弃用和移除](#deprecations-and-removals)；请务必阅读相关内容。

## 发布主题和标志

![Kubernetes v1.35 Timbernetes 标志：一个故事书风格的六边形徽章，上面有一棵发光的世界之树，其树枝环绕着地球和白色的 Kubernetes 轮子；三只欢快的松鼠站在下方——一只穿着紫色长袍的巫师手持 LGTM 卷轴，一只手持斧头和蓝色 Kubernetes 盾牌的战士，以及一只身穿海军蓝斗篷、手提灯笼的盗贼——它们站在绿草地上，草地下方是一条写着“World Tree Release”的金色缎带，背景是柔和的山峦和云雾缭绕的天空](/blog/2025/12/17/kubernetes-v1-35-release/k8s-v1.35.png)

2025年以八色：魔法的颜色 (v1.33) 的微光开启，并乘着风与意志 (v1.34) 的阵风。我们以“世界之树”为灵感，结束了这一年，这棵生命之树尤格德拉西尔将许多领域连接起来。正如任何一棵大树一样，Kubernetes 在全球社区的关怀下，一环一环、一个版本一个版本地成长。

其中心是围绕地球的 Kubernetes 轮子，它由那些始终如一地投入工作的坚韧的维护者、贡献者和用户所支撑。在日常工作、生活变迁和稳定的开源管理之间，他们修剪旧的 API，嫁接新的功能，并保持这个世界上最大的开源项目之一的健康。

三只松鼠守护着这棵树：一只巫师手持用于审阅者的 LGTM 卷轴，一只战士手持斧头和 Kubernetes 盾牌，代表那些开辟新分支的发布团队，以及一只手提灯笼的盗贼，代表那些为黑暗的问题队列带来光明的分类人员。

它们共同代表着一个更大的冒险团队。Kubernetes v1.35 为世界之树增添了又一个生长环，这是一个由许多双手、许多路径和不断深入的根系使枝叶高耸的社区所塑造的新切口。

## 重点更新

Kubernetes v1.35 包含了大量新功能和改进。以下是发布团队希望强调的一些精选更新！

### 稳定版：Pod 资源原地更新

Kubernetes 已将 Pod 资源原地更新功能推向通用可用性 (GA)。
此功能允许用户调整 CPU 和内存资源，而无需重新启动 Pod 或容器。以前，此类修改需要重新创建 Pod，这可能会中断工作负载，特别是对于有状态或批处理应用程序。早期 Kubernetes 版本只允许您更改现有 Pod 的基础设施资源设置（请求和限制）。新的原地功能实现了更平滑、非中断的垂直伸缩，提高了效率，还可以简化开发。

这项工作是 SIG Node 领导的 [KEP #1287](https://kep.k8s.io/1287) 的一部分。

### 测试版：用于工作负载身份和安全的 Pod 证书

以前，将证书交付给 Pod 需要外部控制器 (cert-manager, SPIFFE/SPIRE)、CRD 编排和 Secret 管理，轮换则由 Sidecar 或 Init 容器处理。Kubernetes v1.35 实现了具有自动化证书轮换的原生工作负载身份，极大地简化了服务网格和零信任架构。

现在，`kubelet` 生成密钥，通过 PodCertificateRequest 请求证书，并将凭据包直接写入 Pod 的文件系统。`kube-apiserver` 在准入时强制执行节点限制，消除了第三方签名者最常见的陷阱：意外违反节点隔离边界。这实现了纯 mTLS 流，发行路径中没有不记名令牌。

这项工作是 SIG Auth 领导的 [KEP #4317](https://kep.k8s.io/4317) 的一部分。

### Alpha 版：调度前节点声明功能

当控制平面启用新功能但节点落后（Kubernetes 偏差策略允许）时，调度器可能会将需要这些功能的 Pod 放置到不兼容的旧节点上。
节点声明功能框架允许节点声明其支持的 Kubernetes 功能。启用新的 Alpha 功能后，节点会报告其支持的功能，通过新的 `.status.declaredFeatures` 字段将此信息发布到控制平面。然后，`kube-scheduler`、准入控制器和第三方组件可以使用这些声明。例如，您可以强制执行调度和 API 验证约束，以确保 Pod 仅在兼容节点上运行。

这项工作是 SIG Node 领导的 [KEP #5328](https://kep.k8s.io/5328) 的一部分。

## 毕业到稳定版的功能

*以下是 v1.35 发布后已稳定的一些改进的精选。*

### PreferSameNode 流量分发

服务的 `trafficDistribution` 字段已更新，以提供对流量路由更明确的控制。引入了一个新选项 `PreferSameNode`，允许服务严格优先考虑本地节点上的端点（如果可用），否则回退到远程端点。

同时，现有的 `PreferClose` 选项已更名为 `PreferSameZone`。这一更改通过明确指示流量在当前可用区内优先来使 API 不言自明。虽然 `PreferClose` 为向后兼容性而保留，但 `PreferSameZone` 现在是区域路由的标准，确保节点级别和区域级别偏好被清晰区分。

这项工作是 SIG Network 领导的 [KEP #3015](https://kep.k8s.io/3015) 的一部分。

### Job API 的 managed-by 机制

Job API 现在包含一个 `managedBy` 字段，允许外部控制器处理 Job 状态同步。此功能在 Kubernetes v1.35 中毕业到稳定版，主要由 [MultiKueue](https://github.com/kubernetes-sigs/kueue/tree/main/keps/693-multikueue) 驱动，MultiKueue 是一个多集群分发系统，其中在管理集群中创建的 Job 会被镜像并在工作集群中执行，状态更新会传播回去。为了启用此工作流，内置的 Job 控制器不能对特定 Job 资源进行操作，以便 Kueue 控制器可以管理状态更新。

目标是允许将 Job 同步干净地委托给另一个控制器。它不旨在将自定义参数传递给该控制器或修改 CronJob 并发策略。

这项工作是 SIG Apps 领导的 [KEP #4368](https://kep.k8s.io/4368) 的一部分。

### 使用 `.metadata.generation` 进行可靠的 Pod 更新跟踪

历史上，Pod API 缺少其他 Kubernetes 对象（如 Deployments）中存在的 `metadata.generation` 字段。
由于这一遗漏，控制器和用户无法可靠地验证 `kubelet` 是否实际处理了 Pod 规范的最新更改。这种模糊性对于像[Pod 资源原地垂直伸缩](#stable-in-place-update-of-pod-resources)这样的功能尤其成问题，因为它很难确切知道资源调整请求何时生效。

Kubernetes v1.33 为 Pod 添加了 `.metadata.generation` 字段，作为 Alpha 功能。该字段现在在 v1.35 Pod API 中稳定，这意味着每次 Pod 的 `spec` 更新时，`.metadata.generation` 值都会递增。作为此改进的一部分，Pod API 还获得了 `.status.observedGeneration` 字段，该字段报告 `kubelet` 已成功看到和处理的代数。Pod 条件也各自包含自己的 `observedGeneration` 字段，客户端可以报告和/或观察。

由于此功能已在 v1.35 中毕业到稳定版，因此所有工作负载都可用。

这项工作是 SIG Node 领导的 [KEP #5067](https://kep.k8s.io/5067) 的一部分。

### 拓扑管理器可配置的 NUMA 节点限制

[拓扑管理器](/docs/concepts/policy/node-resource-managers/)历史上曾对它支持的最大 NUMA 节点数量使用硬编码的 8 作为限制，以防止亲和性计算期间的状态爆炸。（这里有一个重要细节；一个 *NUMA 节点* 与 Kubernetes API 中的 Node 不同。）这个 NUMA 节点数量的限制阻止了 Kubernetes 充分利用现代高端服务器，这些服务器越来越多地采用具有超过 8 个 NUMA 节点的 CPU 架构。

Kubernetes v1.31 在拓扑管理器策略配置中引入了一个新的**测试版** `max-allowable-numa-nodes` 选项。在 Kubernetes v1.35 中，该选项已稳定。启用它的集群管理员可以使用超过 8 个 NUMA 节点的服务器。

尽管配置选项已稳定，但 Kubernetes 社区意识到大型 NUMA 主机的性能不佳，并且有一个[拟议的增强功能](https://kep.k8s.io/5726) (KEP-5726) 旨在改进它。您可以通过阅读[控制节点上的拓扑管理策略](/docs/tasks/administer-cluster/topology-manager/)了解更多信息。

这项工作是 SIG Node 领导的 [KEP #4622](https://kep.k8s.io/4622) 的一部分。

## 测试版中的新功能

*以下是 v1.35 发布后已变为测试版的一些改进的精选。*

### 通过 Downward API 暴露节点拓扑标签

从 Pod 内部访问节点拓扑信息（例如区域和可用区）通常需要查询 Kubernetes API 服务器。虽然这种方法功能上可行，但它通过要求广泛的 RBAC 权限或 Sidecar 容器仅仅为了检索基础设施元数据而增加了复杂性和安全风险。Kubernetes v1.35 将通过 Downward API 直接暴露节点拓扑标签的功能提升到测试版。

`kubelet` 现在可以将标准拓扑标签（例如 `topology.kubernetes.io/zone` 和 `topology.kubernetes.io/region`）作为环境变量或投影卷文件注入到 Pod 中。主要好处是为工作负载提供了一种更安全、更高效的方式来感知拓扑。这允许应用程序原生适应其可用区或区域，而无需依赖 API 服务器，通过遵循最小权限原则和简化集群配置来增强安全性。

**注意：** Kubernetes 现在将可用的拓扑标签注入到每个 Pod 中，以便它们可以作为 [Downward API](/docs/concepts/workloads/pods/downward-api/) 的输入。在 v1.35 升级后，大多数集群管理员会看到每个 Pod 添加了几个新标签；这是设计的一部分。

这项工作是 SIG Node 领导的 [KEP #4742](https://kep.k8s.io/4742) 的一部分。

### 原生支持存储版本迁移

在 Kubernetes v1.35 中，原生支持存储版本迁移毕业到测试版并默认启用。此举将迁移逻辑直接集成到核心 Kubernetes 控制平面（“树内”），消除了对外部工具的依赖。

历史上，管理员依赖手动“读/写循环”（通常是将 `kubectl get` 管道到 `kubectl replace`）来更新 Schema 或重新加密静态数据。这种方法效率低下且容易发生冲突，特别是对于 Secrets 等大型资源。通过此版本，内置控制器会自动处理更新冲突和一致性令牌，提供了一种安全、简化和可靠的方式来确保存储数据与最小操作开销保持最新。

这项工作是 SIG API Machinery 领导的 [KEP #4192](https://kep.k8s.io/4192) 的一部分。

### 可变卷挂载限制

CSI（容器存储接口）驱动是 Kubernetes 插件，它为存储系统向容器化工作负载公开提供了一种一致的方式。`CSINode` 对象记录了安装在节点上的所有 CSI 驱动的详细信息。然而，节点上报告的实际挂载容量可能不匹配。当 CSI 驱动启动后卷槽被占用时，`kube-scheduler` 可能会将有状态 Pod 分配给容量不足的节点，最终导致 Pod 停留在 `ContainerCreating` 状态。

Kubernetes v1.35 使 `CSINode.spec.drivers[*].allocatable.count` 可变，以便可以动态更新节点的可用卷挂载容量。它还允许 CSI 驱动通过引入一个可配置的刷新间隔（通过 `CSIDriver` 对象定义）来控制 `allocatable.count` 值在所有节点上更新的频率。此外，它在检测到由于容量不足导致卷挂载失败时会自动更新 `CSINode.spec.drivers[*].allocatable.count`。尽管此功能在 v1.34 中毕业到测试版，默认禁用 `MutableCSINodeAllocatableCount` 功能标志，但在 v1.35 中仍保持在测试版，以留出时间获取反馈，但功能标志已默认启用。

这项工作是 SIG Storage 领导的 [KEP #4876](https://kep.k8s.io/4876) 的一部分。

### 机会性批处理

历史上，Kubernetes 调度器按顺序处理 Pod，时间复杂度为 `O(num pods × num nodes)`，这可能导致兼容 Pod 的冗余计算。此 KEP 引入了一种机会性批处理机制，旨在通过“Pod 调度签名”识别此类兼容 Pod 并将其批处理在一起，从而共享它们之间的过滤和评分结果，以提高性能。

Pod 调度签名确保从调度角度来看，两个具有相同签名的 Pod 是“相同”的。它不仅考虑 Pod 和节点属性，还考虑系统中的其他 Pod 以及关于 Pod 放置的全局数据。这意味着任何具有给定签名的 Pod 将从任何任意节点集中获得相同的分数/可行性结果。

批处理机制由两个操作组成，可以随时调用——*创建*和*提名*。创建操作会根据具有有效签名的 Pod 的调度结果创建一组新的批处理信息。提名操作使用创建的批处理信息，从签名与规范 Pod 签名匹配的新 Pod 中设置提名节点名称。

这项工作是 SIG Scheduling 领导的 [KEP #5598](https://kep.k8s.io/5598) 的一部分。

### StatefulSets 的 `maxUnavailable`

StatefulSet 运行一组 Pod 并为每个 Pod 维护一个固定的身份。这对于需要稳定网络标识符或持久存储的有状态工作负载至关重要。当 StatefulSet 的 `.spec.updateStrategy.<type>` 设置为 `RollingUpdate` 时，StatefulSet 控制器将删除并重新创建 StatefulSet 中的每个 Pod。它将按照 Pod 终止的相同顺序（从最大序数到最小序数）进行，一次更新一个 Pod。

Kubernetes v1.24 向 StatefulSet 的 `rollingUpdate` 配置设置添加了一个新的**Alpha**字段，称为 `maxUnavailable`。除非您的集群管理员明确选择启用，否则该字段不属于 Kubernetes API。
在 Kubernetes v1.35 中，该字段已进入测试版并默认可用。您可以使用它来定义更新期间可以不可用的最大 Pod 数量。此设置与 `.spec.podManagementPolicy` 设置为 `Parallel` 结合使用时最有效。您可以将 `maxUnavailable` 设置为正数（例如：2）或所需 Pod 数量的百分比（例如：10%）。如果未指定此字段，它将默认为 1，以保持以前一次只更新一个 Pod 的行为。此改进允许有状态应用程序（可以容忍多个 Pod 停机）更快地完成更新。

这项工作是 SIG Apps 领导的 [KEP #961](https://kep.k8s.io/961) 的一部分。

### `kuberc` 中可配置的凭据插件策略

可选的 [`kuberc` 文件](/docs/reference/kubectl/kuberc/) 是一种将服务器配置和集群凭据与用户偏好分开的方式，而不会通过意外输出扰乱已在运行的 CI 管道。

作为 v1.35 版本的一部分，`kuberc` 获得了额外的功能，允许用户配置凭据插件策略。此更改引入了两个字段 `credentialPluginPolicy`，它允许或拒绝所有插件，并允许使用 `credentialPluginAllowlist` 指定允许的插件列表。

这项工作是 SIG Auth 和 SIG CLI 合作的 [KEP #3104](https://kep.k8s.io/3104) 的一部分。

### KYAML

YAML 是一种人类可读的数据序列化格式。在 Kubernetes 中，YAML 文件用于定义和配置资源，例如 Pod、Service 和 Deployment。然而，复杂的 YAML 难以阅读。YAML 的显著空白需要仔细注意缩进和嵌套，而其可选的字符串引用可能导致意外的类型强制转换（参见：挪威 Bug）。虽然 JSON 是一个替代方案，但它不支持注释，并且对尾随逗号和带引号的键有严格要求。

KYAML 是 YAML 的一个更安全、更少歧义的子集，专为 Kubernetes 设计。作为 v1.34 中可选的 Alpha 功能引入，此功能在 Kubernetes v1.35 中毕业到测试版并已默认启用。可以通过设置环境变量 `KUBECTL_KYAML=false` 来禁用它。

KYAML 解决了 YAML 和 JSON 相关的所有挑战。所有 KYAML 文件也都是有效的 YAML 文件。这意味着您可以编写 KYAML 并将其作为输入传递给任何版本的 kubectl。这也意味着您不需要编写严格的 KYAML 即可解析输入。

这项工作是 SIG CLI 领导的 [KEP #5295](https://kep.k8s.io/5295) 的一部分。

### HorizontalPodAutoscalers 的可配置容忍度

水平 Pod 自动伸缩器 (HPA) 历史上一直依赖于固定的全局 10% 容忍度进行伸缩操作。这种硬编码值的一个缺点是，需要高灵敏度的工作负载（例如那些需要根据 5% 负载增加进行伸缩的工作负载）通常被阻止伸缩，而其他工作负载可能会不必要地振荡。

在 Kubernetes v1.35 中，可配置容忍度功能毕业到测试版并默认启用。此增强功能允许用户在 HPA `behavior` 字段中为每个资源定义自定义容忍度窗口。通过设置特定容忍度（例如，将其降低到 0.05，即 5%），操作员可以精确控制自动伸缩灵敏度，确保关键工作负载快速响应小的指标变化，而无需进行集群范围的配置调整。

这项工作是 SIG Autoscaling 领导的 [KEP #4951](https://kep.k8s.io/4951) 的一部分。

### Pod 中对用户命名空间的支持

Kubernetes 正在增加对用户命名空间的支持，允许 Pod 运行具有隔离的用户和组 ID 映射，而不是共享主机 ID。这意味着容器可以在内部以 root 身份操作，但实际上映射到主机上的非特权用户，从而降低了在发生妥协时权限提升的风险。此功能提高了 Pod 级别的安全性，并使在容器内部需要 root 权限的工作负载运行更安全。随着时间的推移，通过 ID 映射的挂载，支持已扩展到无状态和有状态 Pod。

这项工作是 SIG Node 领导的 [KEP #127](https://kep.k8s.io/127) 的一部分。

### VolumeSource：OCI 制品和/或镜像

创建 Pod 时，您通常需要为容器提供数据、二进制文件或配置文件。这意味着将内容包含到主容器镜像中，或使用自定义 init 容器下载文件并将其解压到 `emptyDir` 中。这两种方法仍然有效。Kubernetes v1.31 添加了对 `image` 卷类型的支持，允许 Pod 声明性地将 OCI 容器镜像制品拉取并解压到卷中。这使您可以使用标准 OCI 注册表工具打包和交付仅包含数据（如配置、二进制文件或机器学习模型）的制品。

通过此功能，您可以将数据与容器镜像完全分离，并消除对额外 init 容器或启动脚本的需求。`image` 卷类型自 v1.33 以来一直处于测试版，并在 v1.35 中默认启用。请注意，使用此功能需要兼容的容器运行时，例如 containerd v2.1 或更高版本。

这项工作是 SIG Node 领导的 [KEP #4639](https://kep.k8s.io/4639) 的一部分。

### `kubelet` 对缓存镜像强制执行凭据验证

`imagePullPolicy: IfNotPresent` 设置目前允许 Pod 使用节点上已缓存的容器镜像，即使 Pod 本身不具备拉取该镜像的凭据。这种行为的一个缺点是它在多租户集群中造成了安全漏洞：如果一个具有有效凭据的 Pod 将一个敏感的私有镜像拉取到节点上，则同一节点上的后续未经授权的 Pod 仅通过依赖本地缓存就可以访问该镜像。

此 KEP 引入了一种机制，其中 `kubelet` 对缓存镜像强制执行凭据验证。在允许 Pod 使用本地缓存镜像之前，`kubelet` 会检查 Pod 是否具有拉取该镜像的有效凭据。这确保只有授权的工作负载才能使用私有镜像，无论它们是否已存在于节点上，从而显著增强了共享集群的安全态势。

在 Kubernetes v1.35 中，此功能已毕业到测试版并默认启用。用户仍然可以通过将 `KubeletEnsureSecretPulledImages` 功能门设置为 false 来禁用它。此外，`imagePullCredentialsVerificationPolicy` 标志允许操作员配置所需的安全级别，从优先考虑向后兼容性的模式到提供最大安全性的严格执行模式。

这项工作是 SIG Node 领导的 [KEP #2535](https://kep.k8s.io/2535) 的一部分。

### 细粒度容器重启规则

历史上，`restartPolicy` 字段严格在 Pod 级别定义，强制 Pod 内所有容器采用相同的行为。这种全局设置的缺点是对于复杂工作负载（例如 AI/ML 训练作业）缺乏粒度。这些工作负载通常需要 `restartPolicy: Never` 以便 Pod 管理作业完成，但单个容器将受益于对特定可重试错误（例如网络故障或 GPU 初始化失败）进行原地重启。

Kubernetes v1.35 通过在容器 API 本身中启用 `restartPolicy` 和 `restartPolicyRules` 来解决此问题。这允许用户为独立于 Pod 整体策略的单个常规和 init 容器定义重启策略。例如，现在可以配置容器仅在其以特定错误代码退出时自动重启，从而避免为瞬时故障重新调度整个 Pod 的昂贵开销。

在此版本中，该功能已毕业到测试版并默认启用。用户可以立即在容器规范中利用 `restartPolicyRules`，以优化长时间运行工作负载的恢复时间和资源利用率，而无需更改 Pod 的更广泛生命周期逻辑。

这项工作是 SIG Node 领导的 [KEP #5307](https://kep.k8s.io/5307) 的一部分。

### CSI 驱动通过 Secrets 字段选择性使用服务账号令牌

向容器存储接口 (CSI) 驱动提供 ServiceAccount 令牌传统上依赖于将它们注入 `volume_context` 字段。这种方法存在显著的安全风险，因为 `volume_context` 用于非敏感配置数据，并且经常被驱动和调试工具以纯文本形式记录，可能导致凭据泄露。

Kubernetes v1.35 引入了一种可选机制，允许 CSI 驱动通过 NodePublishVolume 请求中专用的 Secrets 字段接收 ServiceAccount 令牌。驱动现在可以通过在 `CSIDriver` 对象中将 `serviceAccountTokenInSecrets` 字段设置为 true 来启用此行为，从而指示 `kubelet` 安全地填充令牌。

主要好处是防止日志和错误消息中意外暴露凭据。此更改确保敏感工作负载身份通过适当的安全通道处理，符合秘密管理的最佳实践，同时保持对现有驱动的向后兼容性。

这项工作是 SIG Auth 与 SIG Storage 合作的 [KEP #5538](https://kep.k8s.io/5538) 的一部分。

### Deployment 状态：终止副本计数

历史上，Deployment 状态提供了有关可用和已更新副本的详细信息，但缺乏对正在关闭的 Pod 的明确可见性。这种遗漏的一个缺点是，用户和控制器无法轻易区分稳定的 Deployment 与仍有 Pod 执行清理任务或遵守长宽限期的 Deployment。

Kubernetes v1.35 将 Deployment 状态中的 `terminatingReplicas` 字段提升到测试版。此字段提供了已设置删除时间戳但尚未从系统中删除的 Pod 的计数。此功能是改进 Deployment 处理 Pod 替换的更大举措的基础步骤，为未来关于在 rollout 期间何时创建新 Pod 的策略奠定了基础。

主要好处是改进了生命周期管理工具和操作员的可观测性。通过暴露终止 Pod 的数量，外部系统现在可以做出更明智的决策，例如在继续执行后续任务之前等待完全关闭，而无需手动查询和过滤单个 Pod 列表。

这项工作是 SIG Apps 领导的 [KEP #3973](https://kep.k8s.io/3973) 的一部分。

## Alpha 版中的新功能

*以下是 v1.35 发布后已变为 Alpha 版的一些改进的精选。*

### Kubernetes 中的 Gang 调度支持

调度相互依赖的工作负载，如 AI/ML 训练作业或 HPC 模拟，传统上一直具有挑战性，因为默认的 Kubernetes 调度器单独放置 Pod。这通常会导致部分调度，即一些 Pod 启动，而另一些则无限期等待资源，从而导致死锁和集群容量浪费。

Kubernetes v1.35 通过新的 Workload API 和 PodGroup 概念引入了对所谓的“gang scheduling”的原生支持。此功能实现了“全有或全无”的调度策略，确保只有当集群有足够的资源同时容纳整个组时，才调度一组已定义的 Pod。

主要好处是提高了批处理和并行工作负载的可靠性和效率。通过防止部分部署，它消除了资源死锁，并确保只有当完整作业可以运行时才利用昂贵的集群容量，从而显著优化了大规模数据处理任务的编排。

这项工作是 SIG Scheduling 领导的 [KEP #4671](https://kep.k8s.io/4671) 的一部分。

### 受限模拟

历史上，Kubernetes RBAC 中的 `impersonate` 动词是全有或全无的：一旦用户被授权模拟目标身份，他们就获得了所有相关权限。这种广泛授权的缺点是它违反了最小权限原则，阻止管理员将模拟者限制为特定操作或资源。

Kubernetes v1.35 引入了一个新的 Alpha 功能，受限模拟，它为模拟流添加了二级授权检查。当通过 `ConstrainedImpersonation` 功能门启用时，API 服务器不仅验证基本的 `impersonate` 权限，还会使用新的动词前缀（例如，`impersonate-on:<mode>:<verb>`）检查模拟者是否被授权执行特定操作。这允许管理员定义细粒度策略——例如，允许支持工程师模拟集群管理员仅仅是为了查看日志，而无需授予完整的管理访问权限。

这项工作是 SIG Auth 领导的 [KEP #5284](https://kep.k8s.io/5284) 的一部分。

### Kubernetes 组件的 Flagz

验证 Kubernetes 组件（例如 API 服务器或 `kubelet`）的运行时配置传统上需要对主机节点或进程参数进行特权访问。为了解决这个问题，引入了 `/flagz` 端点以通过 HTTP 暴露命令行选项。然而，其输出最初仅限于纯文本，使得自动化工具难以可靠地解析和验证配置。

在 Kubernetes v1.35 中，`/flagz` 端点已增强以支持结构化、机器可读的 JSON 输出。授权用户现在可以使用标准的 HTTP 内容协商请求带版本号的 JSON 响应，而原始纯文本格式仍可用于人工检查。此更新显著改进了可观测性和合规性工作流，允许外部系统以编程方式审计组件配置，而无需脆弱的文本解析或直接的基础设施访问。

这项工作是 SIG Instrumentation 领导的 [KEP #4828](https://kep.k8s.io/4828) 的一部分。

### Kubernetes 组件的 Statusz

对 Kubernetes 组件（如 `kube-apiserver` 或 `kubelet`）进行故障排除传统上涉及解析非结构化日志或文本输出，这既脆弱又难以自动化。尽管之前存在一个基本的 `/statusz` 端点，但它缺乏标准化、机器可读的格式，限制了其对外部监控系统的实用性。

在 Kubernetes v1.35 中，`/statusz` 端点已增强以支持结构化、机器可读的 JSON 输出。授权用户现在可以使用标准的 HTTP 内容协商请求此格式，以检索精确的状态数据（例如版本信息和健康指标），而无需依赖脆弱的文本解析。此改进为所有核心组件的自动化调试和可观测性工具提供了可靠、一致的接口。

这项工作是 SIG Instrumentation 领导的 [KEP #4827](https://kep.k8s.io/4827) 的一部分。

### CCM：使用 Informer 的基于 watch 的路由控制器协调

在云环境中管理网络路由传统上依赖于云控制器管理器 (CCM) 定期轮询云提供商的 API 以验证和更新路由表。这种固定间隔的协调方法效率低下，通常会产生大量的非必要 API 调用，并在节点状态更改和相应的路由更新之间引入延迟。

对于 Kubernetes v1.35 版本，cloud-controller-manager 库为路由控制器引入了基于 watch 的协调策略。控制器不再依赖计时器，而是利用 Informer 监视特定的节点事件，例如添加、删除或相关的字段更新，并仅在实际发生更改时触发路由同步。

主要好处是显著减少了云提供商 API 的使用，这降低了达到速率限制的风险并减少了操作开销。此外，这种事件驱动模型通过确保路由表在集群拓扑更改后立即更新，提高了集群网络层的响应能力。

这项工作是 SIG Cloud Provider 领导的 [KEP #5237](https://kep.k8s.io/5237) 的一部分。

### 用于基于阈值放置的扩展容忍度操作符

Kubernetes v1.35 通过允许工作负载表达可靠性要求来引入 SLA 感知调度。该功能为容忍度添加了数值比较操作符，允许 Pod 根据面向 SLA 的污点（例如服务保证或故障域质量）匹配或避免节点。

主要好处是增强调度器以实现更精确的放置。关键工作负载可以要求更高 SLA 的节点，而优先级较低的工作负载可以选择较低 SLA 的节点。这提高了利用率并降低了成本，同时不影响可靠性。

这项工作是 SIG Scheduling 领导的 [KEP #5471](https://kep.k8s.io/5471) 的一部分。

### Job 暂停时可变容器资源

运行批处理工作负载通常涉及资源限制的反复试验。目前，Job 规范是不可变的，这意味着如果 Job 由于内存不足 (OOM) 错误或 CPU 不足而失败，用户不能简单地调整资源；他们必须删除 Job 并创建一个新的 Job，从而丢失执行历史和状态。

Kubernetes v1.35 引入了在 Job 处于暂停状态时更新资源请求和限制的功能。通过 `MutableJobPodResourcesForSuspendedJobs` 功能门启用，此增强功能允许用户暂停失败的 Job，使用适当的资源值修改其 Pod 模板，然后使用更正后的配置恢复执行。

主要好处是为配置错误的作业提供了更流畅的恢复工作流。通过允许在暂停期间进行原地修正，用户可以解决资源瓶颈，而不会中断 Job 的生命周期身份或丢失其完成状态的跟踪，从而显著改善了批处理的开发人员体验。

这项工作是 SIG Apps 领导的 [KEP #5440](https://kep.k8s.io/5440) 的一部分。

## 其他值得注意的更改

### 动态资源分配 (DRA) 的持续创新

[核心功能](https://kep.k8s.io/4381)已在 v1.34 中毕业到稳定版，并具有关闭功能。在 v1.35 中，它始终启用。几个 Alpha 功能也得到了显著改进，并已准备好进行测试。我们鼓励用户提供对这些功能的反馈，以帮助它们在即将发布的版本中顺利晋升到测试版。

#### 通过 DRA 扩展资源请求

解决了与通过设备插件进行的扩展资源请求相比的几个功能空白，例如 Init 容器中设备的评分和重用。

#### 设备污点和容忍度

新的“None”效果可用于报告问题而不会立即影响调度或运行中的 Pod。DeviceTaintRule 现在提供有关正在进行的驱逐的状态信息。“None”效果可用于在实际驱逐 Pod 之前进行“试运行”：

* 使用 “effect: None” 创建 DeviceTaintRule。
* 检查状态以查看将驱逐多少个 Pod。
* 将 “effect: None” 替换为 “effect: NoExecute”。

#### 可分区设备

属于同一可分区设备的设备现在可以在不同的 ResourceSlice 中定义。
您可以在[官方文档](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#partitionable-devices)中了解更多信息。

#### 可消耗容量，设备绑定条件

修复了几个错误和/或添加了更多测试。
您可以在官方文档中了解有关[可消耗容量](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#consumable-capacity)和[绑定条件](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#device-binding-conditions)的更多信息。

### 可比较的资源版本语义

Kubernetes v1.35 改变了客户端解释[资源版本](/docs/reference/using-api/api-concepts/#resource-versions)的方式。

在 v1.35 之前，客户端唯一支持的比较是检查字符串相等性：如果两个资源版本相等，则它们是相同的。客户端还可以向 API 服务器提供资源版本，并要求控制平面执行内部比较，例如自特定资源版本以来流式传输所有事件。

在 v1.35 中，所有树内资源版本都符合新的更严格的定义：这些值是特殊形式的十进制数字。而且，由于它们可以比较，客户端可以执行自己的操作来比较两个不同的资源版本。
例如，这意味着在崩溃后重新连接的客户端可以检测何时丢失了更新，这与在此期间有更新但没有丢失更改的情况不同。

语义的这种改变启用了其他重要的用例，例如[存储版本迁移](/docs/tasks/manage-kubernetes-objects/storage-version-migration/)、对 *informer*（客户端辅助概念）的性能改进以及控制器可靠性。所有这些用例都需要知道一个资源版本是否比另一个更新。

这项工作是 SIG API Machinery 领导的 [KEP #5504](https://kep.k8s.io/5504) 的一部分。

## v1.35 中的毕业、弃用和移除

### 毕业到稳定版

此列表包含了所有毕业到稳定版（也称为*通用可用性*）的功能。有关包括新功能以及从 Alpha 版到测试版的所有更新的完整列表，请参阅发布说明。

此版本总共有 15 项增强功能提升到稳定版：

### 弃用、移除和社区更新

随着 Kubernetes 的发展和成熟，为了改善项目的整体健康状况，某些功能可能会被弃用、移除或替换为更好的功能。有关此过程的更多详细信息，请参阅 Kubernetes [弃用和移除策略](/docs/reference/using-api/deprecation-policy/)。Kubernetes v1.35 包含一些弃用。

#### Ingress NGINX 退役

多年来，Ingress NGINX 控制器一直是将流量路由到 Kubernetes 集群的流行选择。它灵活，被广泛采用，并成为无数应用程序的标准入口点。

然而，维护该项目变得不可持续。由于维护者严重短缺和技术债务不断增加，社区最近做出了艰难的决定将其退役。这不完全是 v1.35 版本的一部分，但这是一项重要的更改，我们希望在此强调。

因此，Kubernetes 项目宣布 Ingress NGINX 将仅接受尽力维护，直至 **2026 年 3 月**。在此日期之后，它将被存档，不再有任何更新。推荐的未来路径是迁移到 [Gateway API](https://gateway-api.sigs.k8s.io/)，它为流量管理提供了更现代、安全和可扩展的标准。

您可以在[官方博客文章](/blog/2025/11/11/ingress-nginx-retirement/)中找到更多信息。

#### 移除 cgroup v1 支持

在 Linux 节点上管理资源时，Kubernetes 历史上一直依赖于 cgroups（控制组）。虽然最初的 cgroup v1 功能完备，但它通常不一致且受限。这就是为什么 Kubernetes 早在 v1.25 中就引入了对 cgroup v2 的支持，它提供了更清晰、统一的层次结构和更好的资源隔离。

由于 cgroup v2 现在是现代标准，Kubernetes 已准备好在 v1.35 中停用旧版 cgroup v1 支持。这是对集群管理员的重要通知：如果您仍在运行不支持 cgroup v2 的旧版 Linux 发行版节点，您的 `kubelet` 将无法启动。为了避免停机，您需要将这些节点迁移到启用 cgroup v2 的系统。

要了解更多信息，请阅读[关于 cgroup v2](/docs/concepts/architecture/cgroups/)；
您还可以通过 [KEP-5573: Remove cgroup v1 support](https://kep.k8s.io/5573) 跟踪切换工作。

#### 弃用 `kube-proxy` 中的 IPVS 模式

几年前，Kubernetes 在 `kube-proxy` 中采用了 [`ipvs`](/docs/reference/networking/virtual-ips/#proxy-mode-ipvs) 模式，以提供比标准 [`iptables`](/docs/reference/networking/virtual-ips/#proxy-mode-iptables) 更快的负载均衡。虽然它提供了性能提升，但使其与不断发展的网络需求保持同步产生了过多的技术债务和复杂性。

由于这种维护负担，Kubernetes v1.35 弃用了 `ipvs` 模式。尽管在此版本中该模式仍然可用，但 `kube-proxy` 在启动时配置使用它时会发出警告。目标是精简代码库并专注于现代标准。对于 Linux 节点，您应该开始过渡到 [`nftables`](/docs/reference/networking/virtual-ips/#proxy-mode-nftables)，它现在是推荐的替代方案。

您可以在 [KEP-5495: Deprecate ipvs mode in kube-proxy](https://kep.k8s.io/5495) 中找到更多信息。

#### 对 containerd v1.X 的最终呼吁

尽管 Kubernetes v1.35 仍然支持 containerd 1.7 和其他 LTS 版本，但这是支持这些版本的最后一个版本。SIG Node 社区已将 v1.35 指定为支持 containerd v1.X 系列的最后一个版本。

这是一个重要的提醒：在升级到下一个 Kubernetes 版本之前，您必须切换到 containerd 2.0 或更高版本。为了帮助识别哪些节点需要关注，您可以在集群中监控 `kubelet_cri_losing_support` 指标。

您可以在[官方博客文章](/blog/2025/09/12/kubernetes-v1-34-cri-cgroup-driver-lookup-now-ga/#announcement-kubernetes-is-deprecating-containerd-v1-y-support)或 [KEP-4033: Discover cgroup driver from CRI](https://kep.k8s.io/4033) 中找到更多信息。

#### `kubelet` 重启期间 Pod 稳定性改进

以前，重启 `kubelet` 服务通常会导致 Pod 状态的暂时中断。在重启期间，kubelet 会重置容器状态，导致健康的 Pod 被标记为 `NotReady` 并从负载均衡器中移除，即使应用程序本身仍在正常运行。

为了解决这个可靠性问题，此行为已得到纠正，以确保无缝的节点维护。`kubelet` 现在在启动时会从运行时正确恢复现有容器的状态。这确保了您的工作负载在 `kubelet` 重启或升级期间保持 `Ready` 状态，并且流量持续不中断地流动。

您可以在 [KEP-4781: Fix inconsistent container ready state after kubelet restart](https://kep.k8s.io/4871) 中找到更多信息。

## 发布说明

请在我们的[发布说明](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md)中查看 Kubernetes v1.35 版本的完整详细信息。

## 可用性

Kubernetes v1.35 可在 [GitHub](https://github.com/kubernetes/kubernetes/releases/tag/v1.35.0) 或 [Kubernetes 下载页面](/releases/download/)上下载。

要开始使用 Kubernetes，请查看这些[交互式教程](/docs/tutorials/)或使用 [minikube](https://minikube.sigs.k8s.io/) 运行本地 Kubernetes 集群。您还可以使用 [kubeadm](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/) 轻松安装 v1.35。

## 发布团队

Kubernetes 的成功离不开社区的支持、承诺和辛勤工作。每个发布团队都由敬业的社区志愿者组成，他们共同努力构建组成您所依赖的 Kubernetes 版本的许多部分。这需要我们社区各方面专业人才的技能，从代码本身到其文档和项目管理。

[我们缅怀 Han Kang](https://github.com/cncf/memorials/blob/main/han-kang.md)，他是一位长期贡献者和受人尊敬的工程师，其卓越的技术和富有感染力的热情对 Kubernetes 社区产生了持久的影响。Han 在 SIG Instrumentation 和 SIG API Machinery 中发挥了重要作用，因其关键工作和对项目核心稳定性的持续承诺而荣获[2021 年 Kubernetes 贡献者奖](https://www.kubernetes.dev/community/awards/2021/)。除了技术贡献之外，Han 还因其作为导师的慷慨以及对建立人际关系的激情而深受爱戴。他以“为他人打开大门”而闻名，无论是引导新贡献者完成他们的第一个拉取请求，还是耐心而友善地支持同事。Han 的遗产通过他所启发的工程师、他帮助构建的健壮系统以及他在云原生生态系统中培养的温暖协作精神而得以延续。

我们要感谢整个[发布团队](https://github.com/kubernetes/sig-release/blob/master/releases/release-1.35/release-team.md)为向社区交付 Kubernetes v1.35 版本所付出的辛勤工作。发布团队的成员包括首次参与的 Shadow 到拥有多个发布周期经验的回归团队负责人。我们非常感谢我们的发布负责人 [Drew Hagen](https://github.com/drewhagen)，他的亲身指导和充满活力的能量不仅带领我们克服了复杂的挑战，而且也激发了本次成功发布背后的社区精神。

## 项目速度

CNCF K8s [DevStats](https://k8s.devstats.cncf.io/d/11/companies-contributing-in-repository-groups?orgId=1&var-period=m&var-repogroup_name=All) 项目聚合了与 Kubernetes 及各种子项目速度相关的许多有趣数据点。这包括从个人贡献到贡献公司数量的所有内容，并说明了推动此生态系统发展所付出的努力的深度和广度。

在 2025 年 9 月 15 日至 2025 年 12 月 17 日为期 14 周的 v1.35 发布周期中，Kubernetes 收到了多达 85 家不同公司和 419 名个人的贡献。在更广泛的云原生生态系统中，这个数字上升到 281 家公司，总共有 1769 名贡献者。

请注意，“贡献”是指某人进行提交、代码审查、评论、创建问题或 PR、审查 PR（包括博客和文档）或对问题和 PR 发表评论。
如果您有兴趣贡献，请访问我们的贡献者网站上的[入门指南](https://www.kubernetes.dev/docs/guide/#getting-started)。

这些数据的来源：

## 事件更新

探索即将到来的 Kubernetes 和云原生事件，包括 KubeCon + CloudNativeCon、KCD 和世界各地的其他著名会议。随时了解情况并参与 Kubernetes 社区！

**2026年2月**

**2026年3月**

**2026年5月**

**2026年6月**

**2026年7月**

您可以在[此处](https://community.cncf.io/events/#/list)找到最新的事件详情。
​

## 即将发布的版本网络研讨会

请于 **2026 年 1 月 14 日星期三下午 5:00 (UTC)** 加入 Kubernetes v1.35 发布团队成员，了解此版本的亮点。有关更多信息和注册，请访问 CNCF 线上项目网站上的[活动页面](https://community.cncf.io/events/details/cncf-cncf-online-programs-presents-cloud-native-live-kubernetes-v135-release/)。

## 参与其中

参与 Kubernetes 最简单的方式是加入众多与您兴趣相符的[特殊兴趣小组](https://github.com/kubernetes/community/blob/master/sig-list.md) (SIGs) 之一。有什么想向 Kubernetes 社区宣布的吗？在我们的每周[社区会议](https://github.com/kubernetes/community/tree/master/communication)上以及通过以下渠道发表您的声音。感谢您一直以来的反馈和支持。