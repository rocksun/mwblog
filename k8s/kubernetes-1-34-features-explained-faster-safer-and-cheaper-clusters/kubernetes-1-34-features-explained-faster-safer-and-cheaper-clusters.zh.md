Kubernetes 已经历了三个时代。第一个时代是关于生存，仅仅是让容器被调度并运行。第二个时代是规模，将集群扩展到数千个节点。

但规模暴露了裂痕。抽象在混乱的基础设施面前崩溃。2025年，随着AI工作负载的普及，当ML作业因为调度器不理解GPU拓扑而失败时，这些裂痕会在凌晨3点显现。或者在财务审查中，当跨区域传输费用悄然推高云账单时。同时，自动伸缩器会在嘈杂的指标上徒劳挣扎。

这就是 Kubernetes 的第三个时代：生产现实。

Kubernetes 1.34，*“风与意志”*，标志着这一转变。它没有堆砌抽象，而是让现有抽象更智能，更了解硬件怪癖、网络瓶颈和安全边界。它弥合了 Kubernetes 假设与运维人员日常所面对的现实之间的鸿沟。

ScaleOps 正好契合这里：Kubernetes 1.34 提供了原语；ScaleOps 闭合了循环，将 PSI 和 DRA 等信号转化为持续的资源优化（rightsizing）、拓扑感知的放置和稳定的自动伸缩。

# 资源智能的进步

在此之前，Kubernetes 将复杂硬件视为简单的商品。此功能改变了这一点，引入了一套功能，为整个资源生命周期带来了智能和控制。

## 1. 动态资源分配：告别“GPU 抽签”（GA）

Kubernetes 中的 GPU 调度一直存在局限性。请求 `nvidia.com/gpu: 1` 无法捕获工作负载实际所需，例如带 NVLink 的 A100。

结果呢？Pod 调度失败或运行在不匹配的硬件上。

随着 1.34 的发布，动态资源分配（DRA）已达到 GA 状态。但它并非即插即用。要使用它，你需要：

* 在 API 服务器、控制器管理器、调度器和 kubelet 上启用 `DynamicResourceAllocation` 功能门。
* 部署一个支持 DRA 的设备插件（例如，支持 DRA 的 NVIDIA GPU Operator）。

一旦部署到位，DRA 通过与 DeviceClass 定义绑定的 `ResourceClaim` 对象，使资源请求具有声明性，从而让调度器拥有实际设备的拓扑感知知识，而不是不透明的整数。

这代表着 ML 和 HPC 工作负载的真正转变。一旦分配了资源声明，它就是不可变的（`AllocateOnce` 语义），因此工作负载可以预测性地访问正确的资源。在生产环境中，像这样调整 GPU 分配可以将利用率从 [约 30% 提高到 60%](https://altersquare.medium.com/cloud-gpu-cost-myths-what-100m-render-minutes-taught-us-about-performance-budgets-f93cf91270b5)，有效地使每美元性能翻倍。

但要注意：如果你的设备插件不支持 DRA，资源声明将无法绑定，Pod 将无法调度。驱动程序和插件的就绪状态是不可谈判的先决条件。

*这是一个 Pod 针对特定 GPU 类型的 ResourceClaim 示例：*

```
apiVersion: resource.k8s.io/v1
kind: ResourceClaim
metadata:
  name: ml-training-claim 
spec:
  devices: 
    requests: 
      - name: gpu-req 
        exactly: 
          deviceClassName: nvidia-gpu 
          allocationMode: ExactCount 
          count: 2 
          selectors: 
            - cel: 
                expression:
                  | 
                  device.capacity["nvidia.com"].memory.compareTo(quantity("40Gi")) >= 0 &&
                  device.attributes["nvidia.com"].nvlink == "true" &&
                  device.attributes["nvidia.com"].product == "A100"

```

## 2. 交换内存支持（Beta）

在内存受限的环境中，突然的峰值可能触发 OOMKills。在 1.34 中，Kubernetes 终于承认了交换内存，但有严格的防护措施：

* Guaranteed Pod 永远不会被交换出去，避免关键工作负载出现不可预测的延迟。
* BestEffort Pod 也不能使用交换内存，因为它们没有声明内存请求，Kubernetes 无法计算公平份额。
* Burstable Pod 可以使用交换内存，但只能按其内存请求的比例使用。

其意图是在压力下进行受控降级，而不是提供无限的“额外内存”。

要启用交换内存，必须在 kubelet 使用之前在节点上进行配置，最好在专用的加密分区上以确保安全。然后，启用 kubelet 标志 `--feature-gates=NodeSwap=true`（或在 `KubeletConfiguration` 中设置 `memorySwap.swapBehavior: LimitedSwap`）。

```

apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
failSwapOn: false
memorySwap:
  swapBehavior: LimitedSwap   
```

一旦激活，可以通过 Summary API 或 Prometheus 指标（`node_swap_usage_bytes`、`pod_swap_usage_bytes`）监控交换内存使用情况。从一个小的节点池开始，并对其进行标签或污点处理，以便只有容忍的工作负载才会调度到那里。

为了安全起见，将系统守护进程排除在交换内存之外（`memory.swap.max=0` 用于 `system.slice`），并优先使用专用、快速的磁盘作为交换分区。控制平面节点应保持无交换内存状态。现在，你可以利用减少的 OOM 抖动和更具弹性的 `Burstable` 工作负载，但会牺牲一些延迟。

把它想象成安全气囊，而不是引擎升级！

## 3. 压力停顿信息（PSI）：你真正的性能指标（Beta）

你的应用程序感觉很慢，但 CPU 和内存利用率看起来却很好。问题不在于应用程序繁忙，而在于它停滞了，等待内存或 I/O。传统指标无法捕获这种延迟。

压力停顿信息（PSI）填补了这一空白。PSI 在 Linux 内核 4.20（2018年）中引入，并在 `/proc/pressure/{cpu,memory,io}` 下暴露，它衡量任务等待资源的时间。通过 cgroups v2，这些指标现在可以按 cgroup 报告，从而可以查看每个容器或 Pod 由于 CPU 争用、内存回收或 I/O 反压而停滞了多少时间。历史上，PSI 由内核工程师和底层性能调优人员使用，但直到现在才在 Kubernetes 环境中变得易于访问。

从 Kubernetes 1.34 开始，PSI 作为 Beta 功能通过 kubelet 功能门 `--feature-gates=KubeletPSI=true` 提供。这使得焦点从原始利用率转移到*等待时间*，使内核级别的停顿指标成为控制平面中的一等信号。

这开启了自动伸缩的新时代：基于*应用程序痛点*而非仅仅利用率进行伸缩。虽然 PSI 不是原生的 HPA 指标源，但可以通过外部指标管道（如 Prometheus Adapter）进行集成。

*这是一个通过 Prometheus 基于内存压力进行 HPA 伸缩的示例（Beta）*

```
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler

  metrics:
  
  - type: External
    external:
      metric:
        name: psi_memory_stall_seconds_total
      target:
        type: AverageValue
        averageValue: "0.1" 
```

*注意：确切的指标名称取决于你的 Prometheus 适配器的映射规则。使用以下命令验证集群中可用的指标：*

`kubectl get --raw /apis/custom.metrics.k8s.io/v1beta1`

真正的挑战不在于收集 PSI 数据，而在于解释它。将原始停顿计数器转换为稳定、智能的伸缩信号需要理解上下文。I/O 压力的短暂飙升不应触发不必要的扩容事件，导致接下来一小时的成本上升。

这正是 ScaleOps 等平台的优势所在：摄取丰富的内核级信号，将其与历史工作负载模式关联起来，并做出自主伸缩和资源优化决策，以区分瞬时瓶颈和真正的资源需求。

# 更便宜、更智能的网络

如果你在 1.33 中错过了，Kubernetes 悄悄地为 Services 引入了一个新的 `trafficDistribution` 设置。当时它是 Alpha 版本，隐藏在一个功能门后面，很容易被忽略。在 1.34 中，它现在是 Beta 版本，默认启用，并最终准备好用于生产。

目标很简单：使多可用区（multi-AZ）网络更高效。在典型设置中，区域 A 中的 Pod 可能会将流量发送到区域 B 中的 Pod，即使本地有相同的端点可用。结果是产生不必要的跨可用区数据传输成本和更高的尾部延迟。

该功能最初名为 `PreferClose`，现已更名并扩展，以提高清晰度。现在有两种明确的模式：

* **PreferSameZone** 尽可能将流量保持在同一个可用区内。这是 `PreferClose` 的直接继承者。
* **PreferSameNode** 更进一步，尽可能将流量保持在节点本地。如果没有本地端点可用，它会优雅地回退到区域本地，然后是集群范围的路由。此模式非常适合 DNS、日志发送器和在每个节点上运行的指标代理。

结果是更可预测的网络流、更低的带宽成本和更低的尾部延迟，所有这些都不会牺牲高可用性。

*示例：DNS 的本地流量分发*

```
apiVersion: v1
kind: Service
metadata:
  name: local-dns
spec:
  selector:
    app: dns
  ports:
  - port: 53
    targetPort: 53
    protocol: UDP
  trafficDistribution: PreferSameNode
```

启用后，kube-proxy（或任何支持这些提示的代理）会自动优先选择最近的端点。如果你的代理尚不支持，没有任何东西会中断，流量只会回退到标准的轮询行为。

实际上，这意味着更低的云账单、更稳定的 P99，以及最终对你有利而不是对你的云提供商有利的网络控制。

# 内置安全，而非后期添加

此版本延续了将强大的原生安全控制直接集成到 API 服务器的趋势。

## 4. 变更准入策略：更快、更简单、更安全（Beta）

传统上，强制执行非特权容器运行等安全默认设置需要准入 webhook。每次创建 Pod 时，API 服务器都必须调用外部 webhook，等待响应，然后才能继续。它确实有效——但这增加了延迟，引入了故障点，并且需要维护另一个组件：webhook 服务器，包括其 TLS 证书、RBAC 规则和部署。

Kubernetes 1.34 通过变更准入策略简化了这一点，将变更逻辑直接移入 API 服务器。你无需管理 webhook，而是用 CEL（通用表达式语言）编写策略，Kubernetes 处理其余部分。变更在进程内运行，没有外部网络调用，无需维护服务，并且运维开销最小。策略定义了变更逻辑，而轻量级绑定决定了它们适用于哪些资源。

*这是一个确保所有 Pod 作为非特权用户运行的策略示例：*

```
apiVersion: admissionregistration.k8s.io/v1beta1
kind: MutatingAdmissionPolicy
metadata:
  name: enforce-non-root
spec:
  matchConstraints:
    resourceRules:
    - apiGroups: [""]
      apiVersions: ["v1"]
      operations: ["CREATE"]
      resources: ["pods"]
  matchConditions:
  - name: must-have-non-root
    expression: "object.spec.securityContext == null || object.spec.securityContext.runAsNonRoot != true"
  failurePolicy: Fail
  reinvocationPolicy: IfNeeded
  mutations:
  - patchType: ApplyConfiguration
    applyConfiguration:
      expression: >
        Object{
          spec: Object.spec{
            securityContext: Object.spec.securityContext{
              runAsNonRoot: true
            }
          }
        }
---
apiVersion: admissionregistration.k8s.io/v1beta1
kind: MutatingAdmissionPolicyBinding
metadata:
  name: enforce-non-root-binding
spec:
  policyName: enforce-non-root
```

要启用此功能，请使用以下参数启动 API 服务器：

```
--feature-gates=MutatingAdmissionPolicy=true \
--runtime-config=admissionregistration.k8s.io/v1beta1=true
```

这不仅仅用于安全强化。你可以使用变更准入策略来规范标签、强制执行一致的拓扑键、注入 Sidecar 配置，或跨团队标准化资源请求。由于逻辑在 API 服务器内部运行，因此无需扩缩 webhook，无需轮换证书，也避免了网络抖动阻塞 Pod 创建的可能性。

对于已经使用 Kyverno 或 Gatekeeper 等工具的团队，此功能并非取代它们，而是补充它们。轻量级默认值现在可以直接存在于 API 服务器中，使策略引擎能够专注于更高级别的用例，例如配置生成、跨资源验证或合规性强制执行。结果是更清晰的集群操作：可预测的准入延迟、更少的故障模式，以及在一个声明式 YAML 中定义的安全、一致的策略。

## 5. 基于选择器的授权：真正的最小权限（GA）

多年来，kubelet 拥有的权限比它们实际需要的要广。为了正常运行，它们被允许列出集群中的所有 Pod，即使每个 kubelet 只需要查看在其自身节点上运行的 Pod。这违反了最小权限原则，如果节点凭据被泄露，它可能被用于查看或操纵集群范围内的所有工作负载。

Kubernetes 1.34 最终弥补了这一差距。授权现在支持 `fieldSelectors` 和 `labelSelectors`，而 Node Authorizer（负责 kubelet 访问的内置授权器）使用它们来强制执行更严格的范围。kubelet 仍然可以列出 Pod，但仅当请求用 `spec.nodeName=<this-node>` 过滤时。任何无范围的请求现在都会被拒绝。结果是更严格的访问控制和在发生泄露时大大缩小的爆炸半径。

你可以使用 `kubectl auth can-i` 模拟 kubelet 来测试此行为：

```

kubectl auth can-i list pods --as=system:node:<node-name> --as-group=system:nodes


kubectl auth can-i list pods --as=system:node:<node-name> --as-group=system:nodes \
  --field-selector spec.nodeName=<node-name>
```

选择器感知不限于 kubelet。授权 webhook 和 **CEL 授权器**现在也可以在其逻辑中使用字段和标签选择器，从而实现更细粒度的访问策略。例如，监控代理可以被限制为只观察带有 `team=observability` 标签的 Pod，或者 webhook 可以只允许针对带有 `env=staging` 标签的 Pod 的 DeleteCollection 请求。

虽然 RBAC 语法没有改变，你不会在 ClusterRoles 中看到 `fieldSelectors:` 块，但强制执行层现在是选择器感知的。这是迈向真正最小权限访问的重要一步，它使安全边界与集群在生产中实际运行的方式保持一致。

## 6. ServiceAccount 令牌镜像拉取：默认使用短期秘密（Beta）

静态 `imagePullSecrets` 长期以来一直是 Kubernetes 安全的薄弱点。它们在集群中无限期存在，一旦暴露，在手动轮换之前一直有效。Kubernetes 1.34 通过 **ServiceAccount 令牌镜像拉取**解决了这个问题，这是一项 Beta 功能，它用短期、自动轮换的令牌取代了静态凭证。

kubelet 不再依赖共享秘密，而是通过 **credential provider API** 及时获取凭证，使用每个 Pod 自己的 ServiceAccount 令牌。这些令牌是临时的、工作负载范围的，并自动刷新。这不仅限制了泄露凭证的爆炸半径，还消除了手动秘密轮换的运维开销。

要启用此功能，请为 kubelet 配置一个凭证提供程序并开启功能门：

```

[Service]
Environment="KUBELET_EXTRA_ARGS=\
  --image-credential-provider-config=/etc/kubernetes/credential-provider-config.yaml \
  --image-credential-provider-bin-dir=/etc/kubernetes/credential-provider \
  --feature-gates=KubeletServiceAccountTokenForCredentialProviders=true"
```

以下是 AWS ECR 的最小凭证提供程序配置：

```

apiVersion: credentialprovider.kubelet.k8s.io/v1
kind: CredentialProviderConfig
providers:
- name: ecr-credential-provider
  matchImages:
  - "*.dkr.ecr.*.amazonaws.com"
  defaultCacheDuration: 12h
  apiVersion: credentialprovider.kubelet.k8s.io/v1
  args: ["get-credentials"]
  env:
  - name: AWS_REGION
    value: us-west-2
```

将你的提供程序二进制文件放入 /etc/kubernetes/credential-provider/ 并重新启动 kubelet。从那时起，每个 Pod 都会使用自己的过期令牌拉取镜像，这些令牌会自动轮换、限定于工作负载，并且比长期存在的秘密安全得多。

因为它仍处于 Beta 阶段，你需要启用功能门，但一旦激活，你就有效地用与现代云安全最佳实践相符的临时凭证取代了静态秘密进行 Kubernetes 镜像拉取。

## 7. 匿名认证限制：默认更严格，按需灵活（GA）

对 Kubernetes API 的匿名访问始终是便利性与安全性之间的权衡。它对于 `/healthz` 或 `/readyz` 等简单的健康探测很有用，但它也可能暴露超出预期的 API 表面。

随着 Kubernetes 1.34 的发布，**匿名认证**现在已**稳定**，RBAC 为你提供了对其适用范围的细粒度控制。匿名访问默认保持启用状态，但你现在可以将其精确限制在你信任的端点上。

目标是平衡：保持匿名访问可用于探测，但在其他所有地方禁用它。这保留了简单的存活和就绪检查，而不会留下不必要的暴露。

*示例：最小、生产安全的基线：*

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: unauthenticated-healthz
rules:
- nonResourceURLs: ["/healthz", "/readyz", "/livez", "/version"]
  verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: unauthenticated-healthz-binding
subjects:
- kind: Group
  name: system:unauthenticated
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: unauthenticated-healthz
  apiGroup: rbac.authorization.k8s.io
```

通过此配置，只有这些端点可以在没有凭证的情况下访问；其他所有内容都需要适当的身份验证。无需启用任何功能门，此行为在 1.34 中开箱即用。

对于生产环境，这是一个干净的折衷方案：合规团队获得了他们需要的安全强化，而运维人员保持了他们的探测简单可靠。

# 改进运维和开发者体验

## 8. 卷属性类：实时卷调优，无需重新挂载（GA）

过去，Kubernetes 中的存储是令人沮丧的静态：一旦 PVC 绑定，其性能层就被锁定。如果需要为高峰负载提供更多 IOPS，通常的解决方案是停机，然后进行卸载、调整大小或迁移到新类。Kubernetes 1.34 通过现已 GA 的 **VolumeAttributesClass** 改变了这一点。你可以在配置时不必硬编码性能，而是定义可重用的属性类（例如预置 IOPS 或吞吐量），并动态地将已绑定的 PVC 切换到新类。

其底层依赖于 CSI 驱动程序的 `ModifyVolume` 调用。并非所有 CSI 驱动程序都支持此功能，不支持的更改将无法通过验证。在支持的情况下，无需卸载、无需 Pod 驱逐，也无需服务中断。只需实时调优。

例如，数据库 PVC 可以从经济高效的层开始，并在季度末报告期间提升到“黄金”类，而无需使应用程序下线：

```
apiVersion: storage.k8s.io/v1
kind: VolumeAttributesClass
metadata:
  name: gold-performance
driverName: csi.vendor.com
parameters:
  provisioned-iops: "5000"
  throughput: "200MiB/s"
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: db-pvc
spec:
  storageClassName: fast-ssd
  volumeAttributesClassName: gold-performance
  resources:
    requests:
      storage: 100Gi
```

数据库 PVC 可以从经济高效的层开始，在高峰报告时段被修补为“黄金”层，全程无需停机。之后，如果驱动程序支持，它可以在原地提升到“超高”层。

对于运维人员来说，这是一个重大转变。存储现在可以根据工作负载需求动态演进，弥合了计算弹性与存储灵活性之间的最后差距之一。

## 9. Job Pod 替换策略：告别双重调度（GA）

批处理工作负载常常带来资源难题。在旧的行为中，当 Job Pod 失败时，控制器可能会立即创建一个替换 Pod，即使旧 Pod 尚未完全终止。在压力下的节点上，这意味着两个 Pod 重叠：一个停留在“终止中”，另一个正在启动，两者都消耗 CPU 和内存。结果是瞬时峰值、资源浪费，有时还会导致级联故障。

在 Kubernetes 1.34 中，`podReplacementPolicy` 已在 `batch/v1` 中毕业至 GA。通过设置此字段，你可以告诉 Job 控制器等待旧 Pod *真正消失*后才开始替换。这保证了平坦的资源配置文件：一次只有一个 Pod 在运行，没有突然的双重分配。

它的样子如下：

```
apiVersion: batch/v1
kind: Job
metadata:
  name: cleanup-job
spec:
  template:
    spec:
      containers:
      - name: cleanup
        image: busybox
        command: ["sh", "-c", "run-something"]
      restartPolicy: OnFailure
  podReplacementPolicy: Failed
```

在这个例子中，Job 只有在前一个 Pod 完全终止 *并且* 其状态为 `Failed` 时才会创建一个新的 Pod。这避免了重试期间的“双重调度”。

因为它已是 GA 版本，所以无需启用功能门，在 1.34 中开箱即用。对于生产环境，主要的防护措施是意识：如果你之前为了速度而依赖旧的重叠行为，你将需要明确调整 Job 并行度，而不是从故障中获得“免费”的并发。

其最终效果是更清晰的批处理作业调度、可预测的节点利用率，以及更少的凌晨 3 点因重叠重试导致的 OOM Kills 警报。

# Kubernetes 已成熟

Kubernetes 1.34 并没有用闪亮的新抽象来炫耀。相反，它提供了更有价值的东西：成熟。它关注的是 SRE 和平台工程师每天都要应对的问题：资源争用、失控的成本、安全和嘈杂的运维。

动态资源分配、基于 PSI 的伸缩、节点本地流量路由、进程内准入策略和实时卷调优等功能都出自同一源头：它们让 Kubernetes 更贴近生产实际行为。这不再是“Kubernetes 魔法”的时代，而是 Kubernetes 作为大规模运行基础设施的真诚合作伙伴的时代。

这就是 1.34 的特别之处。它不是为了增加层级，而是为了弥合差距。它承认生产的硬性边缘，并为你提供了直接管理它们的旋钮和杠杆。Kubernetes 已停止假装基础设施是简单的。它已经成熟，并准备好应对你的工作负载抛出的任何挑战。

当然，获得这些新原语仅仅是成功的一半。PSI、DRA 和更智能的网络等功能为你提供了你一直想要的可见性和控制力，但要将它们转化为实际的节省和稳定性，还需要持续的调优。这就是 ScaleOps 的用武之地。我们的平台持续对工作负载进行资源优化并预测需求，以便 Kubernetes 功能能够转化为生产结果：更稳定的集群、更少的浪费节点，以及反映效率而非过度配置的云账单。Kubernetes 正在成长，ScaleOps 确保你的基础设施也随之变得更智能。