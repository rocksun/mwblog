Running containerized applications at scale with Kubernetes demands careful resource management. One very complicated but common challenge is preventing Out-of-Memory (OOM) kills, which occur when a container’s memory consumption surpasses its allocated limit. This brutal termination by the Kubernetes kernel’s OOM killer disrupts application stability and can affect application availability and the health of your overall environment.

In this post, we’ll explore the reasons that OOM kills can occur and provide tactics to combat and prevent them.

Before diving in, it’s worth noting that OOM kills represent one symptom that can have a variety of root causes. It’s important for organizations to implement a system that solves the root cause analysis problem with speed and accuracy, allowing reliability engineering teams to respond rapidly, and to potentially prevent these occurrences in the first place.

## Deep dive into an OOM kill
An Out-Of-Memory (OOM) kill in [Kubernetes](https://www.causely.io/resources/glossary-cloud-native-technologies/) occurs when a container exceeds its memory limit, causing the Kubernetes kernel’s OOM killer to terminate the container. This impacts application stability and requires immediate attention.

Several factors can trigger OOM kills in your Kubernetes environment, including:

**Memory limits exceeded:**This is the most common culprit. If a container consistently pushes past its designated memory ceiling, the OOM killer steps in to prevent a system-wide meltdown.**Memory leaks:**Applications can develop memory leaks over time, where they allocate memory but fail to release it properly. This hidden, unexpected growth eventually leads to OOM kills.**Resource overcommitment:**Co-locating too many resource-hungry pods onto a single node can deplete available memory. When the combined memory usage exceeds capacity, the OOM killer springs into action.**Bursting workloads:**Applications with spiky workloads can experience sudden memory surges that breach their limits, triggering OOM kills.
As an example, a web server that experiences a memory leak code bug may gradually consume more and more memory until the OOM killer intervenes to prevent a crash.

Another case could be when a Kubernetes cluster over-commits resources by scheduling too many pods on a single node. The OOM killer may need to step in to free up memory and ensure system stability.

## The devastating effects of OOM kills: Why they matter
OOM kills aren’t normally occurring events. They can trigger a cascade of negative consequences for your applications and the overall health of the cluster, such as:

**Application downtime:**When a container is OOM-killed, it abruptly terminates, causing immediate application downtime. Users may experience service disruptions and outages.**Data loss:**Applications that rely on in-memory data or stateful sessions risk losing critical information during an OOM kill.**Performance degradation:**Frequent OOM kills force containers to restart repeatedly. This constant churn degrades overall application performance and user experience.**Service disruption:**Applications often interact with each other. An OOM kill in one container can disrupt inter-service communication, causing cascading failures and broader service outages.
If a container running a critical database service experiences an OOM kill, it could result in data loss and corruption. This leads to service disruptions for other containers that rely on the database for information, causing cascading failures across the entire application ecosystem.

## Combating OOM kills
There are a few different tactics to combat OOM kills in attempt to operate a memory-efficient Kubernetes environment.

### Set appropriate resource requests and limits
For example, you can set a memory request of 200Mi and a memory limit of 300Mi for a particular container in your Kubernetes deployment. Requests ensure the container gets at least 200Mi of memory, while limits cap it at 300Mi to prevent excessive consumption.

`resources:`
` requests:`
` memory: "200Mi"`
` limits:`
` memory: "300Mi"`
While this may mitigate potential memory use issues, it is a very manual process and does not deal at all with the dynamic nature of what we can achieve with Kubernetes. It also doesn’t solve the source issue, which may be a code-level problem triggering memory leaks or failed GC processes.

### Transition to autoscaling
Leveraging [autoscaling](https://www.causely.io/resources/glossary-cloud-native-technologies/) capabilities is a core dynamic option for resource allocation. There are two autoscaling methods:

**Vertical Pod Autoscaling (VPA):**[VPA](https://kubernetes.io/docs/concepts/workloads/autoscaling/)dynamically adjusts resource limits based on real-time memory usage patterns. This ensures containers have enough memory to function but avoids over-provisioning.**Horizontal Pod Autoscaling (HPA):**[HPA](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)scales the number of pods running your application up or down based on memory utilization. This distributes memory usage across multiple pods, preventing any single pod from exceeding its limit. The following HPA configuration shows an example of scaling based on memory usage:
`apiVersion: autoscaling/v2beta2`
`kind: HorizontalPodAutoscaler`
`metadata:`
` name: my-app-hpa`
`spec:`
` scaleTargetRef:`
` apiVersion: apps/v1`
` kind: Deployment`
` name: my-app`
` minReplicas: 2`
` maxReplicas: 10`
` metrics:`
` - type: Resource`
` resource:`
` name: memory`
` target:`
` type: Utilization`
` averageUtilization: 80`
### Monitor memory usage
Proactive monitoring is key. For instance, you can configure [Prometheus](https://www.causely.io/resources/glossary-cloud-native-technologies/) to scrape memory metrics from your Kubernetes pods every 15 seconds and set up [Grafana](https://grafana.com/) dashboards to visualize memory usage trends over time. Additionally, you can create alerts in Prometheus to trigger notifications when memory usage exceeds a certain threshold.

### Optimize application memory usage
Don’t underestimate the power of code optimization. Address memory leaks within your applications and implement memory-efficient data structures to minimize memory consumption.

### Pod disruption budgets (PDB)
When deploying updates, [PDBs](https://www.causely.io/resources/glossary-cloud-native-technologies/) ensure a minimum number of pods remain available, even during rollouts. This mitigates the risk of widespread OOM kills during deployments. Here is a PDB configuration example that helps ensure minimum pod availability.

`apiVersion: policy/v1`
`kind: PodDisruptionBudget`
`metadata:`
` name: my-app-pdb`
`spec:`
` minAvailable: 80%`
` selector:`
` matchLabels:`
` app: my-app`
### Manage node resources
You can apply a node selector to ensure that a memory-intensive pod is only scheduled on nodes with a minimum of 8GB of memory. Additionally, you can use taints and tolerations to dedicate specific nodes with high memory capacity for memory-hungry applications, preventing OOM kills due to resource constraints.

`nodeSelector:`
` disktype: ssd`
`tolerations:`
` - key: "key"`
` operator: "Equal"`
` value: "value"`
` effect: "NoSchedule"`
### Use QoS classes
Kubernetes offers Quality of Service ([QoS](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/)) classes that prioritize resource allocation for critical applications. Assign the highest QoS class to applications that can least tolerate OOM kills. Here is a sample resource configuration with QoS parameters:

`resources:`
` requests:`
` memory: "1Gi"`
` cpu: "500m"`
` limits:`
` memory: "1Gi"`
` cpu: "500m"`
These are a few potential strategies to help prevent OOM kills. The challenge comes with the frequency with which they can occur, and the risk to your applications when they happen.

As you can imagine, it’s not possible to manually manage resource utilization, and guarantee the stability and performance of your containerized applications within your Kubernetes environment.

## Manual thresholds = Rigidity and risk
These techniques can help reduce the risk of OOM kills. The issue is not entirely solved though. By setting manual thresholds and limits, you’re removing many of the dynamic advantages of Kubernetes.

A more ideal way to solve the OOM kill problem is to use adaptive, dynamic resource allocation. Even if you get resource allocation right on initial deployment, there are many factors that change that affect how your application consumes resources. There is also a risk because application and resource issues don’t just affect one pod, or one container. Resource issues can reach every part of the cluster and degrade the other running applications and services.

## Which strategy works best to prevent OOM kills?
Vertical Pod Autoscaling (VPA) and Horizontal Pod Autoscaling (HPA) are common strategies used to manage resource limits in Kubernetes containers. VPA adjusts resource limits based on real-time memory usage patterns, while HPA scales pods based on memory utilization.

Monitoring with tools like Prometheus may help with the troubleshooting of memory usage trends. Optimizing application memory usage is no easy feat because it’s especially challenging to identify whether it is infrastructure or code causing the problem.

Pod Disruption Budgets (PDB) may help ensure a minimum number of pods remain available during deployments, while node resources can be managed using node selectors and taints. Quality of Service (QoS) classes prioritize resource allocation for critical applications.

One thing is certain: OOM kills are a common and costly challenge to manage using traditional monitoring tools and methods.

At [Causely](https://www.causely.io/), we’re focused on applying causal reasoning software to help organizations keep applications healthy and resilient. By automating root cause analysis, issues like OOM kills can be resolved in seconds, and unintended consequences of new releases or application changes can be avoided.


## Related resources
[Read the blog](https://www.causely.io/blog/understanding-kubernetes-readiness-probe-to-ensure-your-applications-availability/): Understanding the Kubernetes Readiness Probe: A Tool for Application Health[Read the blog](https://www.causely.io/blog/bridging-the-gap-between-observability-and-automation-with-causal-reasoning/): Bridging the gap between observability and automation with causal reasoning[Watch the webinar](https://www.causely.io/podcast/webinar/what-is-causal-ai-why-do-devops-need-it/): What is Causal AI and why do DevOps teams need it?