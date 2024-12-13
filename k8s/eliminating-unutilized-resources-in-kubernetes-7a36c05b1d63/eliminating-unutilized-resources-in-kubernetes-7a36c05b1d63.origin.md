# Eliminating Unutilized Resources in Kubernetes
Unutilized resources in Kubernetes aren’t just a budget line item — they’re a silent killer of efficiency, scalability, and performance.

Wasted CPU cycles, idle memory, and underutilized nodes all add up, increasing costs while leaving clusters less capable of handling real workloads. If you’ve worked with Kubernetes at scale, you know how these inefficiencies can snowball into real operational headaches.

Today, with the rise of new smart automation tools like [Scaleops](https://scaleops.com/) and others, you can rather quickly and easily detect, fix and prevent unutilized resources including “[unevictable workloads](https://scaleops.com/blog/scaleops-pod-placement-optimizing-unevictable-workloads/)” such as PDBs, misconfigured Safe-to-Evict Annotations, and “naked pods”.** **Automating this process minimizes both resource waste and manual work simultaneously.

## What Are Unutilized Resources in Kubernetes?
Unutilized resources are the leftover compute, memory, or storage capacity that remains idle but reserved, often due to poor configuration or workload placement. These inefficiencies show up in various ways:

- Pods using far less than their requested resources.
- Nodes sitting idle because of unevictable workloads.
- Over-provisioned clusters wasting valuable cloud resources.
# Why Unutilized Resources Matter More Than Ever
Every idle CPU core or unclaimed GB of memory represents money wasted. Beyond cost, resource inefficiency undermines scalability, leaving clusters bloated and unable to respond effectively to changing workloads.

As clusters scale, these inefficiencies compound, turning manageable problems into operational crises. Addressing unutilized resources isn’t just about saving money — it’s about unlocking the full potential of your Kubernetes setup.

## Why Is This Happening?
The flexibility of Kubernetes comes with a price: complexity. While it gives teams the tools to manage resources precisely, achieving optimal utilization requires a deep understanding of resource requests, limits, scheduling policies, and autoscaler mechanics.

Some [common causes](https://scaleops.com/blog/scaleops-pod-placement-optimizing-unevictable-workloads/) of unutilized resources include:

- Misconfigured
**Pod Disruption Budgets (PDBs)**, which prevent pods from being evicted. - Overuse of the
`safe-to-evict: false`
annotation. - Naked pods that lack a managing controller, making them unevictable.
- Conservative resource requests that far exceed actual usage.
## Key Challenges in Addressing Unutilized Resources
**Visibility:**Without robust monitoring, unutilized resources can go unnoticed until costs spike or performance degrades.**Unevictable Workloads:**PDBs and critical annotations often prevent autoscalers from optimizing resources.**Manual Effort:**Identifying, analyzing, and fixing inefficiencies requires significant time and expertise, detracting from other engineering priorities.**Scalability:**The bigger the cluster, the harder it is to fine-tune resource allocations across hundreds or thousands of nodes manually.
## Achieving a Solution
Modern tools like [ ScaleOps](https://scaleops.com/) automate the heavy lifting.

By **detecting** inefficiencies, intelligently **rescheduling** **workloads**, and **continuously** **monitoring** for resource waste, tools like ScaleOps bridge the gap between Kubernetes’ raw capabilities and practical usability.

With intelligent algorithms and an intuitive dashboard, ScaleOps and other modern tools make it possible to optimize resource usage without the constant manual tinkering, and with optimal outcomes.

## What You’ll Learn
In this guide, we’ll break down:

- What unutilized resources in Kubernetes are and why they’re critical to address.
- The main causes of unutilized resources, including “unevictable workloads.”
- Tools and strategies, including ScaleOps, for automating resource optimization.
- Best practices and pitfalls for managing resource efficiency in your clusters.
Let’s dive in and tackle the inefficiencies draining your Kubernetes clusters.

# Understanding Unutilized Resources in Kubernetes
Efficient resource usage in Kubernetes is essential for maintaining cost-effectiveness, scalability, and performance. However, various factors can lead to resources being allocated but underutilized, leaving them idle and driving up costs. Let’s explore what unutilized resources are, why they occur, and how to address them effectively.

# What Are Unutilized Kubernetes Resources?
Unutilized resources are portions of CPU, memory, or storage allocated to nodes or pods in a Kubernetes cluster but not actively used by applications or workloads. These idle resources often occur due to:

**Over-provisioning:**Allocating more resources than needed.**Improper scheduling:**Workloads poorly distributed across nodes.**Autoscaler limitations:**Inability to adjust or scale down nodes due to specific pod configurations or constraints.
# Why It Happens
**Conservative Resource Requests:**Developers often overestimate resource needs to avoid outages, leading to pods using far less than their allocated CPU or memory.**Restricted Workload Mobility:**Certain workloads, like critical system pods, are configured to remain on specific nodes.**Imbalanced Scheduling:**Kubernetes’ default scheduling might leave some nodes over-allocated and others idle due to insufficient bin-packing algorithms.**Node-level Constraints:**Cluster Autoscaler and other tools are restricted from evicting pods marked as non-evictable, leaving nodes underutilized.
# Detecting Unutilized Resources
Monitor cluster metrics using tools like **Prometheus** and **Grafana** to identify discrepancies between requested and actual resource usage. For example, the following PromQL query shows CPU usage by pods:

`rate(container_cpu_usage_seconds_total[5m])`
Pair this with `kube_pod_container_resource_requests`
to compare requested vs. actual usage:

`kube_pod_container_resource_requests{resource="cpu"}`
These metrics can highlight over-provisioned pods or underutilized nodes.

# Types of Unutilized Resources
## General Underutilization
General underutilization occurs when resources (CPU, memory) are allocated but not fully consumed by pods. This often stems from overly conservative resource requests and misaligned scaling policies.

## Why It Happens
**Overhead for Peaks:**Developers provision resources based on potential peak usage rather than actual average usage.**Static Resource Allocation:**Fixed resource limits for workloads that vary in demand over time.
## How to Detect
Check for a low **resource utilization ratio** by comparing actual usage against requests using monitoring tools:

`kubectl top pods`
This command shows the current CPU and memory consumption for each pod, making it easy to identify underutilized ones.

## Example: Over-Allocated Deployment
`apiVersion: apps/v1`
kind: Deployment
metadata:
name: over-provisioned-app
spec:
replicas: 3
template:
spec:
containers:
- name: app-container
image: app-image:v1
resources:
requests:
cpu: "500m"
memory: "1Gi"
limits:
cpu: "1"
memory: "2Gi"
If the actual usage of each pod is around `200m`
CPU and `512Mi`
memory, this deployment wastes over half of its allocated resources.

## Common Use Cases
**Pre-production environments**: Resources are over-provisioned to simulate peak loads.**Burstable workloads**: Applications with sporadic spikes in usage often lead to over-provisioning.
# Unevictable Workloads
Unevictable workloads refer to pods that cannot be rescheduled or removed by Kubernetes, making them a significant obstacle to autoscaler efficiency. Getting rid o them or preventing them is easy [with the right tools](https://scaleops.com/blog/scaleops-pod-placement-optimizing-unevictable-workloads/) but can be an everlasting pain when done manually.

## Key Contributors to Unevictable Workloads
**Pod Disruption Budgets (PDBs)**
PDBs define the minimum number of replicas that must remain running during disruptions. This prevents critical workloads from being evicted but can hinder node scaling.
**Example PDB Configuration:**
`apiVersion: policy/v1`
kind: PodDisruptionBudget
metadata:
name: my-app-pdb
spec:
minAvailable: 2
selector:
matchLabels:
app: my-app
This configuration ensures two replicas are always running but can block eviction when scaling down nodes, leaving some underutilized.

**2. Safe-to-Evict Annotations**
Pods marked with `safe-to-evict: false`
cannot be removed or rescheduled during node scaling or bin-packing operations.
**Annotation Example:**
`metadata:`
annotations:
cluster-autoscaler.kubernetes.io/safe-to-evict: "false"
**3. Naked Pods**
Pods created directly without a controller (e.g., Deployments, ReplicaSets) lack the automation needed for rescheduling or scaling.
**Naked Pod Example:**
`apiVersion: v1`
kind: Pod
metadata:
name: standalone-pod
spec:
containers:
- name: app-container
image: app-image:v1
These pods prevent nodes from being scaled down, leading to idle resources.

# How to Address Unevictable Workloads
Before we start, my recommendation is to automate the process using smart designated tools, and my favorite one is [Scaleops](https://scaleops.com/).

The reasons I prefer choosing such tools are simple:

- After a 10-minute installation (no code changes/configs) you will see a 95%+ elimination of unutilized resources, and they’re not coming back.
- It does so automatically without any manual work required.
- It does so continuously while detecting, fixing and preventing unitizled resources automatically and ongoingly. Launch and forget.
## Kubernetes VPA: Pros and Cons & Best Practices
### Explore Kubernetes VPA pros, cons & best practices, including how it works, key metrics, configuration, and usage…
scaleops.com

But, you can also choose the do this manually, and repeatedly, for whatever reason forcing you to do so. If you do, here are some steps that can help:

## 1. Adjust Pod Disruption Budgets
Review and update PDBs to allow more flexibility in evictions where possible:

`apiVersion: policy/v1`
kind: PodDisruptionBudget
metadata:
name: updated-pdb
spec:
maxUnavailable: 1
selector:
matchLabels:
app: my-app
## 2. Use Safe-to-Evict Sparingly
Apply the `safe-to-evict`
annotation only for critical workloads.

## 3. Replace Naked Pods with Controllers
Deploy workloads using controllers like Deployments or StatefulSets to ensure proper management and scalability.

**Example Deployment for a Previously Naked Pod:**
`apiVersion: apps/v1`
kind: Deployment
metadata:
name: managed-app
spec:
replicas: 2
selector:
matchLabels:
app: my-app
template:
metadata:
labels:
app: my-app
spec:
containers:
- name: app-container
image: app-image:v1
This ensures Kubernetes can scale and reschedule the workload effectively.

By addressing both general underutilization and unevictable workloads, Kubernetes clusters can operate more efficiently, cutting costs and improving scalability. Stay proactive with regular audits and automated tools to maintain optimal resource utilization.

# Detecting, Fixing, and Preventing Unutilized Resources
## Why Detect and Prevent Unutilized Resources?
Unutilized resources result in:

**Increased costs:**Idle resources inflate cloud bills.**Degraded performance:**Resource fragmentation affects workload efficiency.**Limited scalability:**Inefficient clusters struggle to handle scaling needs.
## How Smart Automation Tools Like Help
Tools like ScaleOps provides an automated solution to resource inefficiencies with:

**Detection:**Identifies underutilized nodes, unevictable pods, and resource allocation issues through comprehensive cluster analysis.**Fixing:**Applies intelligent scheduling algorithms to redistribute workloads without violating PDBs or safe-to-evict rules.**Prevention:**Continuously monitors clusters, ensuring unevictable workloads are minimized and resources are effectively utilized.
Here’s how ScaleOps optimizes unevictable workloads:

`# Example ScaleOps optimization`
apiVersion: scaleops/v1
kind: PodOptimization
metadata:
name: optimize-workloads
spec:
policies:
- type: "reschedule"
targets:
- labelSelector: "safe-to-evict: false"
action: "optimize-placement"
This configuration identifies unevictable pods and optimizes their placement for better resource distribution.

# Manual Methods to Detect and Fix Unutilized Resources in Kubernetes
While automated tools like ScaleOps streamline the detection and correction of unutilized resources, manual methods provide flexibility and hands-on control. Using Kubernetes-native tools and commands, you can analyze resource usage and address inefficiencies in your cluster.

# Detecting Unutilized Resources
## Using `kubectl top`
to Identify Underutilized Pods
The `kubectl top`
command retrieves metrics for resource usage, such as CPU and memory, for pods and nodes in the cluster. To identify underutilized pods:

`kubectl top pods --all-namespaces`
This command shows the current resource usage of all running pods. Compare the reported values with the resource requests defined in the pod configurations. For example, a pod using only `100m`
CPU but requesting `500m`
CPU indicates over-provisioning.

# Analyzing Nodes for Resource Inefficiencies
To analyze nodes and their utilization levels, run:

`kubectl top nodes`
This command displays the total CPU and memory usage across nodes. Nodes with consistently low utilization may have unevictable workloads or imbalanced scheduling.

# Comparing Resource Requests with Actual Usage
Use Prometheus metrics to compare requested and actual usage. For CPU utilization, the following PromQL queries are helpful:

`rate(container_cpu_usage_seconds_total[5m])`
Compare this with requested resources:

`kube_pod_container_resource_requests{resource="cpu"}`
This comparison highlights pods that are allocated more resources than they consume.

# Fixing Over-Provisioned Resources
# Adjusting Resource Requests and Limits
Over-provisioned pods waste resources that could be allocated elsewhere. To fix this, update the resource requests and limits for underutilized pods. For example:

`apiVersion: apps/v1`
kind: Deployment
metadata:
name: resource-optimized-app
spec:
replicas: 2
template:
spec:
containers:
- name: app-container
image: app-image:v1
resources:
requests:
cpu: "250m"
memory: "512Mi"
limits:
cpu: "500m"
memory: "1Gi"
This update aligns resource requests with observed usage, reducing wastage while maintaining performance.

# Addressing Unevictable Workloads
## Reviewing and Modifying Pod Disruption Budgets (PDBs)
Pod Disruption Budgets (PDBs) can block evictions, leading to stranded resources. List all PDBs in the cluster:

`kubectl get pdb --all-namespaces`
Inspect the `minAvailable`
or `maxUnavailable`
values. For example:

`apiVersion: policy/v1`
kind: PodDisruptionBudget
metadata:
name: app-pdb
spec:
minAvailable: 3
selector:
matchLabels:
app: critical-app
If the `minAvailable`
value is too high, adjust it to allow more flexibility during scaling:

`spec:`
minAvailable: 2
## Removing Safe-to-Evict Annotations
Safe-to-evict annotations prevent pods from being evicted by the autoscaler. To find pods with this annotation:

`kubectl get pods --all-namespaces -o json | jq '.items[] | select(.metadata.annotations."cluster-autoscaler.kubernetes.io/safe-to-evict" == "false") | .metadata.name'`
Once identified, edit the pod configuration to remove the annotation:

`kubectl edit pod <pod-name>`
Delete the following annotation:

`metadata:`
annotations:
cluster-autoscaler.kubernetes.io/safe-to-evict: "false"
## Converting Naked Pods to Managed Workloads
Naked pods, which lack controllers, block node scaling. Convert them to managed workloads like Deployments. Export the pod configuration:

`kubectl get pod naked-pod -o yaml > naked-pod.yaml`
Modify the YAML to create a Deployment:

`apiVersion: apps/v1`
kind: Deployment
metadata:
name: managed-app
spec:
replicas: 1
selector:
matchLabels:
app: naked-pod
template:
metadata:
labels:
app: naked-pod
spec:
containers:
- name: app-container
image: app-image:v1
Apply the updated configuration and remove the original naked pod:

`kubectl apply -f managed-app.yaml`
kubectl delete pod naked-pod
## Ongoing Monitoring and Optimization
Regular monitoring is key to preventing unutilized resources from recurring. Use tools like Prometheus and Grafana to set up dashboards and alerts for resource usage metrics. Monitor discrepancies between requested and actual usage to proactively adjust resource allocations. This hands-on approach ensures clusters remain optimized and cost-effective.

# Best Practices for Managing Unutilized Resources
When not using smart automation solutions and going fully manual, make sure to:

**Regularly Audit PDBs**
Ensure PDB configurations allow necessary evictions during scaling or maintenance. Avoid overly restrictive policies that lock pods in place.**Use Safe-to-Evict Annotations Sparingly**
Restrict the use of`safe-to-evict: false`
to truly critical workloads. Overuse limits the autoscaler’s ability to optimize.**Deploy Workloads with Controllers**
Avoid naked pods by deploying workloads using controllers like Deployments, ReplicaSets, or StatefulSets. This ensures proper management and eviction when needed.**Adopt Automated Resource Management Tools**
Leverage tools like ScaleOps to automate the detection and optimization of underutilized resources.**Monitor Resource Usage Continuously**
Implement robust monitoring to track resource utilization and identify inefficiencies in real-time.
# Pitfalls to Watch Out For
When not using smart automation solutions and going fully manual, watch out for:

**Restrictive PDBs**
Misconfigured PDBs can block autoscaler operations, leading to stranded resources.**Overuse of Non-Evictable Annotations**
Marking too many pods as non-evictable hampers autoscaling efforts and increases costs.**Neglecting Naked Pods**
Failing to manage naked pods effectively can prevent node scaling and waste resources.**Inconsistent Resource Monitoring**
Clusters without regular audits or monitoring risk accumulating inefficiencies over time.**Lack of Automation**
Relying on manual processes to manage cluster resources can lead to errors and delays.
# Conclusion
Efficient resource management is key to maintaining scalable, cost-effective Kubernetes clusters. By understanding and addressing unutilized resources, engineering teams can unlock significant cost savings and performance gains.

We discussed:

- Types of unutilized resources, including unevictable workloads.
- Challenges in detecting and fixing these issues manually.
- How tools like ScaleOps automate optimization, improve visibility, and simplify resource management.
Start by reviewing your cluster for inefficiencies using Kubernetes-native tools or dive into automated solutions like ScaleOps for a more streamlined approach. If you’ve faced similar challenges or have tips to share, let us know in the comments below.

Thank you for reading!

# Learn More
## Kubernetes VPA: Pros and Cons & Best Practices
### Explore Kubernetes VPA pros, cons & best practices, including how it works, key metrics, configuration, and usage…
scaleops.com

## Kubernetes Pod Rightsizing: A Practical Guide
### Efficient resource allocation is crucial for optimizing both the cost and performance of applications running in…
overcast.blog