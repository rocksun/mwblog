<!--
title: 15个Kubernetes调度情景实用指南
cover: https://teckbootcamps.com/wp-content/uploads/2024/01/doc-3.png
-->

Kubernetes调度是确保集群中的Pod在适当节点上运行的关键组件。通过灵活配置调度策略，可以提高资源利用率、负载平衡和高可用性。

在本文中，我们将深入探讨一些实际的Kubernetes调度场景，并提供相应的配置示例和最佳实践。

> 译自 [15 Kubernetes Scheduling Scenario Practical Guide](https://teckbootcamps.com/kubernetes-scheduling-scenario-practical-guide/)，作者 Mohamed BEN HASSINE。

## 1. 基本场景 – NodeSelector

**场景描述**：我们有一些标记有SSD硬盘的节点，并且希望将需要高性能存储的Pod调度到这些节点上。

**Pod配置：**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: high-performance-pod
spec:
  containers:
  - name: my-container
    image: my-image
  nodeSelector:
    disktype: ssd
```

## 2. 高级场景 – 节点亲和性

**场景描述**：我们希望将需要GPU的任务调度到带有GPU标签的节点上。

**Pod配置**：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: gpu-pod
spec:
  containers:
  - name: my-container
    image: my-image
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: gpu
            operator: In
            values:
            - "true"
```

## 3. 资源分配 – Pod优先级和预选调度

**场景描述**：为了确保关键任务具有更高的优先级，我们可以定义一个PriorityClass并将其应用到Pod上。

**PriorityClass配置**：

```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 1000000
globalDefault: false
description: "High priority class"
```

**Pod配置**：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: high-priority-pod
spec:
  containers:
  - name: my-container
    image: my-image
  priorityClassName: high-priority
```

## 4. 防止Pod在同一节点上运行 – Pod反亲和性

**场景描述**：通过Pod反亲和性，我们可以确保同一组中的Pod不会被调度到同一节点上以提高高可用性。

**Pod配置**：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: anti-affinity-pod
spec:
  containers:
  - name: my-container
    image: my-image
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: app
            operator: In
            values:
            - web
        topologyKey: kubernetes.io/hostname
```

## 5. 多副本拓扑域分布 – Pod拓扑分布

**场景描述**：确保同一应用的多个Pod分布在不同的拓扑域以提高可用性。

**部署配置**：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: "app"
                operator: In
                values:
                - "web"
            topologyKey: "kubernetes.io/hostname"
```

## 6. 节点Taints和PodTolerations

**场景描述**：通过节点的Taints，我们可以标记节点，只有具有相应Tolerations的Pod才能被调度到这些节点上。

**节点配置**：

```yaml
apiVersion: v1
kind: Node
metadata:
  name: node1
spec:
  taints:
  - key: special
    value: unique
    effect: NoSchedule
```

Pod配置：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: toleration-pod
spec:
  containers:
  - name: my-container
    image: my-image
  tolerations:
  - key: "special"
    operator: "Equal"
    value: "unique"
    effect: "NoSchedule"
```

## 7. 自定义调度器 – 自定义调度器

**场景描述**：定制调度器以满足特定的调度需求，例如基于业务规则或特殊硬件条件。

**自定义调度器示例**：

1. 创建自定义调度器插件

```go
// my_scheduler.go
package main

import (
	"k8s.io/kubernetes/pkg/scheduler"
	"k8s.io/kubernetes/pkg/scheduler/framework"
	"k8s.io/kubernetes/pkg/scheduler/framework/plugins/defaultbinder"
	"k8s.io/kubernetes/pkg/scheduler/framework/plugins/defaultpreemption"
	"k8s.io/kubernetes/pkg/scheduler/framework/plugins/names"
)

const (
	// YourSchedulerName is the name of your custom scheduler
	YourSchedulerName = "my-scheduler"
)

// New initializes a new scheduler with your custom plugins
func New() *scheduler.Config {
	return &scheduler.Config{
		Client:              scheduler.NewHTTPClient(),
		SchedulerName:       YourSchedulerName,
		PercentageOfNodesToScore: 0.25,
		Profiles: []scheduler.Profile{
			{
				Name: YourSchedulerName,
				Plugins: []scheduler.Plugin{
					defaultpreemption.Name: defaultpreemption.New,
					defaultbinder.Name:     defaultbinder.New,
					names.NewNodeResourcesFit(),
					names.NewNodePorts(),
					names.NewNodeAffinity(YourSchedulerName),
					names.NewNodeAffinityPriority(YourSchedulerName),
				},
			},
		},
	}
}

func main() {
	// Use the New() function to create a new scheduler with your custom plugins
	config := New()
	command := app.NewSchedulerCommand(
		// Use the WithConfig function to set your custom scheduler configuration
		app.WithConfig(config),
	)
	f := command.Flags()
	f.AddGoFlagSet(flag.CommandLine)

	if err := command.Execute(); err != nil {
		os.Exit(1)
	}
}
```

2. 编译并运行自定义调度器

```bash
go build my_scheduler.go
./my_scheduler
```

## 8. Pod 优先级和抢占 – Pod 优先级和抢占

**场景描述**：通过设置 Pod 的优先级和抢占策略，确保关键任务被优先处理。

**Pod 配置**：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: priority-pod
spec:
  containers:
  - name: my-container
    image: my-image
  priorityClassName: high-priority
```

## 9. 资源限制和请求 – 资源限制和请求

**场景描述**：通过为 Pod 设置资源限制和请求，调度器可以更好地优化资源利用。

**Pod 配置**：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: resource-pod
spec:
  containers:
  - name: my-container
    image: my-image
    resources:
      limits:
        cpu: "2"
        memory: "1Gi"
      requests:
        cpu: "1"
        memory: "500Mi"
```

## 10. 亲和性和反亲和性规则 – 亲和性和反亲和性规则

**场景描述**：使用亲和性和反亲和性规则确保 Pod 在特定节点上，或避免与其他 Pod 被调度到同一节点。

**Pod 配置**：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: affinity-pod
spec:
  containers:
  - name: my-container
    image: my-image
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: security
            operator: In
            values:
            - "high"
        topologyKey: kubernetes.io/hostname
```

## 11. Pod 中断预算 – Pod 中断预算

**场景描述**：使用 Pod 中断预算限制允许在维护期间中断的 Pod 数量，以确保系统稳定性。

**PodDisruptionBudget 配置**：

```yaml
apiVersion: policy/v1beta1
kind: PodDisruptionBudget
metadata:
  name: web-pdb
spec:
  maxUnavailable: 1
  selector:
    matchLabels:
      app: web
```

## 12.  水平 Pod 自动缩放器 – 水平扩展器

**场景描述**：使用水平扩展器根据 CPU 使用率或其他指标自动调整 Pod 数量，以满足应用需求。

**HorizontalPodAutoscaler 配置**：

```yaml
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: web-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web-deployment
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

## 13. Pod 开销 – Pod 开销

**场景描述**：通过设置 Pod 开销，告知调度器考虑 Pod 需要的额外资源，以避免在节点上调度过多的 Pod。

**Pod 配置**：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: overhead-pod
spec:
  containers:
  - name: my-container
    image: my-image
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
    overhead:
      podFixed: 100Mi
      ephemeral-storage: 1Gi
```

## 14. 节点本地 DNS 缓存 – 节点本地 DNS 缓存

**场景描述**：在节点上启用本地 DNS 缓存以提高 DNS 查询性能。

**kubelet 配置**：

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
clusterDomain: cluster.local
featureGates:
  CoreDNSLocalCache: true
```

## 15. Pod 优先级类别 – Pod 优先级类别

**场景描述**：使用 Pod 优先级类别将 Pod 划分为不同的优先级，以确保关键任务被优先调度。

**PriorityClass 配置**：

```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 1000000
globalDefault: false
description: "High priority class"
preemptionPolicy: PreemptLowerPriority
```

## 结论

这些场景涵盖了从基础到高级的 Kubernetes 调度实际案例。根据您的需求，您可以选择适当的场景进行配置，以优化集群的资源利用率和性能。

在实际应用中，根据具体需求调整配置，确保调度器的策略符合业务和性能要求。