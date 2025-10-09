Kubernetes has evolved through three eras. The first was about survival, just getting containers scheduled and running. The second era was scale, stretching clusters to thousands of nodes.

But scale exposed cracks. Abstractions broke down against messy infrastructure. In 2025, with AI workloads everywhere, those cracks show up at 3 AM when an ML job fails because the scheduler doesn’t understand GPU topology. Or in finance reviews, when inter-zone transfer fees quietly spike the cloud bill. Meanwhile, autoscalers thrash on noisy metrics.

This is the third era of Kubernetes: production reality.

Kubernetes 1.34, *“Of Wind & Will,”* marks this shift. Instead of piling on abstractions, it makes existing ones smarter, more aware of hardware quirks, network bottlenecks, and security boundaries. It closes the gap between what Kubernetes assumes and what operators live every day.

ScaleOps fits here: Kubernetes 1.34 gives you the primitives; ScaleOps closes the loop, turning signals like PSI and DRA into continuous rightsizing, topology-aware placement, and stable autoscaling.

# Advancements in Resource Intelligence

Until now, Kubernetes has treated complex hardware as a simple commodity. This feature changes that, introducing a suite of features that bring intelligence and control over the entire resource lifecycle.

## 1. Dynamic Resource Allocation: The End of the “GPU Lottery” (GA)

GPU scheduling in Kubernetes has always been limited. Requesting `nvidia.com/gpu: 1` doesn’t capture what workloads actually need, like a A100 with NVLink.

The result? Pods fail scheduling or run on mismatched hardware.

With 1.34, Dynamic Resource Allocation (DRA) is GA. But it isn’t plug and play just yet. To use it, you need to:

* Enable the `DynamicResourceAllocation` feature gate on the API server, controller-manager, scheduler, and kubelet.
* Deploy a DRA-capable device plugin (for example, NVIDIA GPU Operator with DRA support)

Once in place, DRA makes resource requests declarative via `ResourceClaim` objects tied to DeviceClass definitions, giving the scheduler topology-aware knowledge of actual devices instead of opaque integers.

This represents a real shift for ML and HPC workloads. Once a claim is allocated, it’s immutable (`AllocateOnce` semantics), so workloads get predictable access to the right resources.  In production, tuning GPU allocation like this can move utilization from [~30% to 60%](https://altersquare.medium.com/cloud-gpu-cost-myths-what-100m-render-minutes-taught-us-about-performance-budgets-f93cf91270b5), effectively doubling performance per dollar.

The catch: if your device plugin doesn’t support DRA, claims won’t bind and pods will stay unschedulable. Driver and plugin readiness are non-negotiable prerequisites.

*Here’s an example of a pod’s ResourceClaim for a specific GPU type*:

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

## 2. Swap Memory Support (Beta)

In memory-constrained environments, a sudden spike can trigger OOMKills. With 1.34, Kubernetes finally acknowledges swap, but with strict guardrails:

* Guaranteed pods are never swapped, avoiding unpredictable latency on critical workloads
* BestEffort pods can’t use swap either, since they declare no memory requests and Kubernetes can’t calculate a fair share
* Burstable pods can use swap, but only in proportion to their memory requests

The intent is controlled degradation under pressure, not unlimited “extra RAM.”

To enable Swap, it must be configured on the node before kubelet can use it, ideally on a dedicated encrypted partition for security. Then, flip the kubelet flag `--feature-gates=NodeSwap=true` (or set `memorySwap.swapBehavior: LimitedSwap` in `KubeletConfiguration`).

```

apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
failSwapOn: false
memorySwap:
  swapBehavior: LimitedSwap   
```

Once active, monitor swap usage via the Summary API or Prometheus metrics (`node_swap_usage_bytes`, `pod_swap_usage_bytes`). Start with a small node pool and label or taint it so that only tolerant workloads land there.

For safety, keep system daemons off swap (`memory.swap.max=0` for `system.slice`) and prefer a dedicated, fast disk for the swap partition. Control plane nodes should remain swap-free. Now you can take advantage of reduced OOM churn and more resilient `Burstable` workloads, at the cost of some latency.

Think of it as an airbag, not an engine upgrade!

## 3. Pressure Stall Information (PSI): Your True Performance Indicator (Beta)

Your application feels slow, yet CPU and memory utilization look perfectly fine. The issue isn’t that the application is busy, it’s that it’s stalled, waiting on memory, or I/O. Traditional metrics don’t capture this kind of delay.

Pressure Stall Information (PSI) fills that gap. Introduced in Linux kernel 4.20 (2018) and exposed under `/proc/pressure/{cpu,memory,io}`, PSI measures how much time tasks spend waiting for resources. With cgroups v2, these metrics can now be reported per cgroup, giving visibility into how much time each container or pod is stalled due to CPU contention, memory reclaim, or I/O backpressure. Historically, PSI was used by kernel engineers and low-level performance tuners, but it wasn’t easily accessible in Kubernetes environments until now.

As of Kubernetes 1.34, PSI is available as a Beta feature via the kubelet feature gate `--feature-gates=KubeletPSI=true`. This shifts the focus from raw utilization to *time spent waiting*, making kernel-level stall metrics a first-class signal in the control plane.

This unlocks a new era of autoscaling: scaling based on *application pain*, not just utilization. While PSI isn’t a native HPA metric source, it can be integrated through an external metrics pipeline such as the Prometheus Adapter.

*Here’s an example of HPA scaling on memory pressure via Prometheus (Beta)*

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

*Note: The exact metric name depends on your Prometheus adapter’s mapping rules. Verify available metrics in your cluster with:*

`kubectl get --raw /apis/custom.metrics.k8s.io/v1beta1`

The real challenge isn’t collecting PSI data. It’s interpreting it. Translating raw stall counters into stable, intelligent scaling signals requires understanding context. A brief spike in I/O pressure shouldn’t trigger an unnecessary scale-up event that drives costs for the next hour.

This is where platforms like ScaleOps excel: ingesting rich kernel-level signals, correlating them with historical workload patterns, and making autonomous scaling and rightsizing decisions that distinguish between a transient bottleneck and a true need for more resources.

# Networking That’s Cheaper and Smarter

If you missed it in 1.33, Kubernetes quietly introduced a new `trafficDistribution` setting for Services. At the time it was Alpha, hidden behind a feature gate, and easy to overlook. In 1.34 it’s now Beta, enabled by default, and finally ready for production use.

The goal is simple: make multi-AZ networking more efficient. In a typical setup, a pod in zone A might send traffic to a pod in zone B, even when an identical endpoint is available locally. The result is unnecessary inter-AZ data transfer costs and higher tail latency.

Originally called `PreferClose,` the feature has been renamed and expanded for clarity. There are now two explicit modes:

* **PreferSameZone** keeps traffic within the same availability zone whenever possible. This is the direct successor to `PreferClose`.
* **PreferSameNode** goes further, keeping traffic node-local when possible. If no local endpoint is available, it gracefully falls back to zone-local, then cluster-wide routing. This mode is ideal for DNS, log shippers, and metrics agents that run on every node.

The result is more predictable network flows, lower bandwidth costs, and reduced tail latency, all without sacrificing high availability.

*Example: Local traffic distribution for DNS*

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

When enabled, kube-proxy (or any proxy that supports the hints) automatically prioritizes the closest endpoint. If your proxy doesn’t support it yet, nothing breaks, traffic simply falls back to standard round-robin behavior.

In practice, this means lower cloud bills, steadier P99s, and network control that finally works in your favor instead of your cloud provider’s.

# Security That’s Built-In, Not Bolted-On

This release continues the trend of baking powerful, native security controls right into the API server.

## 4. Mutating Admissions Policies: Faster, Simpler, Safer (Beta)

Enforcing security defaults like running containers as non-root traditionally required an admission webhook. Every time a Pod was created, the API server had to call an external webhook, wait for a response, and only then continue. It worked—but it added latency, introduced failure points, and required maintaining yet another component: the webhook server, complete with its TLS certificates, RBAC rules, and deployments.

Kubernetes 1.34 streamlines this with Mutating Admission Policies, moving mutation logic directly into the API server. Instead of managing a webhook, you write a policy in CEL (Common Expression Language), and Kubernetes handles the rest. The mutation runs in-process, with no external network calls, no service to maintain, and minimal operational overhead. Policies define the mutation logic, while lightweight bindings determine which resources they apply to.

*Here’s an example policy that ensures all Pods run as non-root:*

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

To enable the feature, start the API server with:

```
--feature-gates=MutatingAdmissionPolicy=true \
--runtime-config=admissionregistration.k8s.io/v1beta1=true
```

This isn’t just for security hardening. You can use Mutating Admission Policies to normalize labels, enforce consistent topology keys, inject sidecar configurations, or standardize resource requests across teams. Because the logic runs inside the API server, there’s no webhook to scale, no certificates to rotate, and no chance of a flaky network hop blocking Pod creation.

For teams already using tools like Kyverno or Gatekeeper, this feature doesn’t replace them, it complements them. Lightweight defaults can now live directly in the API server, freeing policy engines to focus on higher-level use cases like config generation, cross-resource validation, or compliance enforcement. The result is cleaner cluster operations: predictable admission latency, fewer failure modes, and secure, consistent policies defined in a single declarative YAML.

## 5. Selector-Based Authorization: True Least Privilege (GA)

For years, kubelets carried broader permissions than they needed. To function, they were allowed to list all Pods in the cluster, even though each kubelet only required visibility into the Pods running on its own node. This violated the principle of least privilege, if a node credential was ever compromised, it could be used to view or manipulate workloads cluster-wide.

Kubernetes 1.34 finally closes that gap. Authorization now supports `fieldSelectors` and `labelSelectors`, and the Node Authorizer, the in-tree authorizer responsible for kubelet access, uses them to enforce stricter scoping. A kubelet can still list Pods, but only if the request is filtered with `spec.nodeName=<this-node>`. Any unscoped request is now denied. The result is tighter access control and a dramatically smaller blast radius in case of compromise.

You can test this behavior using `kubectl auth can-i`, impersonating a kubelet:

```

kubectl auth can-i list pods --as=system:node:<node-name> --as-group=system:nodes


kubectl auth can-i list pods --as=system:node:<node-name> --as-group=system:nodes \
  --field-selector spec.nodeName=<node-name>
```

Selector awareness isn’t limited to kubelets. Authorization webhooks and the **CEL authorizer** can now also use field and label selectors in their logic, enabling more granular access policies. For example, a monitoring agent could be restricted to watch only Pods labeled `team=observability`, or a webhook could allow DeleteCollection requests only for Pods labeled `env=staging`.

While RBAC syntax hasn’t changed, you won’t see a `fieldSelectors:` block in ClusterRoles, the enforcement layer is now selector-aware. It’s a major step toward true least-privilege access that aligns security boundaries with how clusters actually run in production.

## 6. ServiceAccount Token Image Pulls: Short-Lived Secrets by Default (Beta)

Static `imagePullSecrets` have long been a weak point in Kubernetes security. They live indefinitely in the cluster, and if exposed, they remain valid until manually rotated. Kubernetes 1.34 addresses this with **ServiceAccount token image pulls**, a Beta feature that replaces static credentials with short-lived, automatically rotating tokens.

Instead of relying on a shared secret, the kubelet now fetches credentials just-in-time through the **credential provider API**, using each Pod’s own ServiceAccount token. These tokens are ephemeral, workload-scoped, and refreshed automatically. This not only limits the blast radius of a leaked credential but also eliminates the operational overhead of manual secret rotation.

To enable the feature, configure the kubelet with a credential provider and turn on the feature gate:

```

[Service]
Environment="KUBELET_EXTRA_ARGS=\
  --image-credential-provider-config=/etc/kubernetes/credential-provider-config.yaml \
  --image-credential-provider-bin-dir=/etc/kubernetes/credential-provider \
  --feature-gates=KubeletServiceAccountTokenForCredentialProviders=true"
```

Here’s a minimal credential provider config for AWS ECR:

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

Drop your provider binary into /etc/kubernetes/credential-provider/ and restart the kubelet. From that point on, each Pod pulls images using its own expiring token, automatically rotated, workload-scoped, and far safer than long-lived secrets.

Because it’s still Beta, you’ll need to enable the feature gate, but once active, you’ve effectively replaced static secrets with ephemeral credentials that align Kubernetes image pulls with modern cloud security best practices.

## 7. Anonymous Auth Restrictions: Tighter by Default, Flexible Where Needed (GA)

Anonymous access to the Kubernetes API has always been a tradeoff between convenience and security. It’s useful for simple health probes like `/healthz` or `/readyz`, but it also risked exposing more of the API surface than intended.

With Kubernetes 1.34, **Anonymous Authentication** is now **Stable**, and RBAC gives you fine-grained control over where it applies. Anonymous access remains enabled by default, but you can now restrict it precisely to the endpoints you trust.

The goal is balance: keep anonymous access available for probes, but disable it everywhere else. That preserves simple liveness and readiness checks without leaving unnecessary exposure.

*Example: minimal, production-safe baseline:*

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

With this configuration, only those endpoints are accessible without credentials; everything else requires proper authentication. There are no feature gates to enable, this behavior works out of the box in 1.34.

For production environments, it’s a clean middle ground: compliance teams get the security hardening they need, and operators keep their probes simple and reliable.

# Improving the Operator and Developer Experience

## 8. VolumeAttributesClass: Live Volume Tuning, No Re-Mount Required (GA)

Storage used to be frustratingly static in Kubernetes: once a PVC was bound, its performance tier was locked in. If you needed more IOPS for a peak load, the usual answer was downtime with detach, resize, or migrate to a new class. Kubernetes 1.34 changes that with **VolumeAttributesClass**, now GA. Instead of hard-coding performance at provision time, you can define reusable classes of attributes (like provisioned IOPS or throughput) and switch a bound PVC to a new class on the fly.

Under the hood this relies on the CSI driver’s `ModifyVolume` call. Not every CSI driver supports it, and unsupported changes will fail validation. Where it is supported, there’s no unmounting, no pod eviction, and no service interruption. Just live tuning.

For example, a database PVC can start on a cost-efficient tier and be bumped to a “gold” class during end-of-quarter reporting without taking the app offline:

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

A database PVC can start on a cost-efficient tier and be patched to “gold” during peak reporting hours, all without downtime. Later, it can be bumped to an “ultra” tier in place if the driver supports it.

For operators, this is a major shift. Storage can now evolve dynamically with workload needs, closing one of the last gaps between compute elasticity and storage flexibility.

## 9. Job PodReplacementPolicy: No More Double Scheduling (GA)

Batch workloads often create resource headaches. With the old behavior, when a job pod failed, the controller could immediately create a replacement pod, even before the old one had fully terminated. On nodes under pressure, this meant two pods overlapping: one stuck in “terminating,” another starting up, both consuming CPU and memory. The result was transient spikes, wasted resources, and sometimes cascading failures.

In Kubernetes 1.34, `podReplacementPolicy` has graduated to GA in `batch/v1`. By setting this field, you can tell the Job controller to wait until the old pod is *actually gone* before starting the replacement. That guarantees a flat resource profile: one pod in flight at a time, no sudden double allocation.

Here’s what it looks like:

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

In this example, the Job only creates a new pod when the previous one has fully terminated *and* its status is `Failed`. This avoids “double-scheduling” during retries.

Because it’s GA, there are no feature gates to enable, it works out of the box in 1.34. For production, the main guardrail is awareness: if you were relying on the old overlapping behavior for speed, you’ll need to adjust job parallelism explicitly instead of getting “free” concurrency from misfires.

The net effect is cleaner batch job scheduling, predictable node utilization, and fewer 3 a.m. alerts about OOM kills from overlapping retries.

# Kubernetes Has Grown Up

Kubernetes 1.34 doesn’t dazzle with shiny new abstractions. Instead, it delivers something far more valuable: maturity. The focus is on the things SREs and platform engineers wrestle with every day: resource contention, runaway costs, security, and noisy operations.

Features like Dynamic Resource Allocation, PSI-based scaling, node-local traffic routing, in-process admission policies, and live volume tuning are all cut from the same cloth: they bring Kubernetes closer to how production actually behaves. This is not the era of “Kubernetes magic,” it’s the era of Kubernetes as an honest partner in running infrastructure at scale.

That’s what makes 1.34 special. It’s not about adding layers, it’s about closing gaps. It acknowledges the hard edges of production and hands you the knobs and levers to manage them directly. Kubernetes has stopped pretending infrastructure is simple. It’s grown up, and it’s ready for whatever your workloads throw at it.

Of course, getting these new primitives is only half the battle. Features like PSI, DRA, and smarter networking give you the visibility and control you always wanted, but turning them into real-world savings and stability takes ongoing tuning. That’s where ScaleOps fits in. Our platform continuously rightsizes workloads and predicts demand so that Kubernetes features translate into production results: steadier clusters, fewer wasted nodes, and a cloud bill that reflects efficiency instead of overprovisioning. Kubernetes is growing up, and ScaleOps makes sure your infrastructure grows smarter with it.