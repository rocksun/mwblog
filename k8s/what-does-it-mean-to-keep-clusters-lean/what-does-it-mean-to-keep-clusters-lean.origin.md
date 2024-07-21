# What Does It Mean to Keep Clusters Lean?
![Featued image for: What Does It Mean to Keep Clusters Lean?](https://cdn.thenewstack.io/media/2024/07/1f4c81ff-carrots-4380095_1280-1024x678.jpg)
[Managing clusters](https://thenewstack.io/managing-kubernetes-clusters-for-platform-engineers/) cost-effectively is becoming increasingly essential as Kubernetes becomes the de facto standard for building modern software delivery platforms. This process has led to the buzzy mantra of “keeping clusters lean.”
Are you practicing [DevOps](https://thenewstack.io/devops/)? That means you’re lean! Lean principles lie at the heart of the DevOps methodology. Not accidentally, the “L” in the CALMS thinking framework (coined by DevOps forefathers John Willis and Damon Edwards and further developed by Jez Humble) stands for Lean delivery practices.

Modern DevOps practices are [rooted in lean management principles](https://thenewstack.io/the-joys-and-pains-of-devops/). These principles, including just-in-time parts delivery and waste elimination, were first defined by the Toyota Production System (TPS) in post-WWII Japan. Later, in the 1990s, the word “lean” was coined in the West to describe these ideas. Books like [“The Machine That Changed the World”](https://www.amazon.com/Machine-That-Changed-World-Revolutionizing/dp/0743299795) explain the TPS and how lean management spread worldwide across industries, including software development.

The book [“Lean Software Development”](https://en.wikipedia.org/wiki/Lean_software_development) was published in 2003 by Mary and Tom Poppendieck, defining the types of waste encountered in software delivery and describing how to eliminate them with structured continuous improvement processes.

## Lean Principles in the Cloud Native World
The principles of lean management, in a nutshell, are as follows:

- Focus on value
- Eliminate waste
- Pursue continuous improvement
Following these principles allows a business to deliver value faster, waste less money, and achieve higher production quality.

Cloud native infrastructure was created to deliver quality software quickly and optimize the value stream by providing cloud resources without lengthy planning processes and underutilized server farms. Autonomous engineering teams deploy autonomous microservices that interact with other services asynchronously and efficiently.

That’s in a dream world, of course. But in real life, most Kubernetes clusters are wasteful and not sufficiently reliable. There’s just too much going on in them to be able to manage them efficiently without applying [a well-defined methodology](https://www.perfectscale.io/blog/fine-tune-your-k8s-clusters-for-optimal-cost-and-performance).

As Kubernetes is becoming the de facto standard way to run production-grade software, be it web services, batch processing, or data pipelines, there’s a growing understanding that only by consciously keeping clusters lean can satisfactory cloud ROI be achieved, therefore staying competitive in the challenging worldwide IT market.

## Keeping Clusters Lean
Here’s a list of practices to help keep Kubernetes clusters lean.

### 1. Focus on Value
Once we’ve standardized our delivery platform to use Kubernetes, it makes sense to run most of our workloads there. However, our workloads and the type of value they provide may differ wildly. Reliability criteria for long-running web services aren’t the same as, for example, ML model training or periodic batch jobs. Also, the level of environmental maturity needs to be considered. Development experiments, performance tests, CI jobs, and one-off maintenance procedures have different availability requirements and justified operational costs.

**Node Selection**
Define the types of VM instances to use for clusters (e.g., choosing spot/preemptible instances instead of reserved capacity) based on the level of availability required and the amount of engineering time saved.

You can use [LearnK8S Kubernetes Instance Calculator](https://learnk8s.io/kubernetes-instance-calculator) for the initial planning.

All cloud providers now offer optimized instances based on purpose-built operating systems (like Bottlerocket OS) or ARM processors.

Using such instances can make our clusters leaner and cheaper, but their appropriateness for our specific workloads needs to be verified beforehand.

**Network Topology Restrictions**
Carefully choosing the network topology for our cluster can significantly impact the cloud bill, especially when running data-intensive workloads. When creating most clusters, the default is running the data plane in three availability zones for improved availability. Each byte transferred on the cross-AZ network within the cluster will cost you additional pennies. So when availability isn’t part of the value we seek to achieve (like for background batch processing, for example) — it makes sense to override the default settings and run all our nodes in the same AZ.

**Storage configuration**
Kubernetes provides multiple storage options that differ in persistence, availability, and performance levels. Focusing on the provided value allows us to choose the most appropriate storage type for the workload.

### 2. Eliminate Risk
The original Toyota Production System pioneered the notion of the Andon Cord — a cable that ran throughout the factory and could be pulled by any worker to stop the production line. The idea is that management trusts the workers to be experts in their field, so they are supposed to pull the cord whenever they discover a problem they perceive as a risk to production quality. Any lurking risk can lead to significant waste down the line. Kubernetes works the same way. Therefore, workloads with potential security and reliability risks should be handled before looking at the waste.

Here are some common Kubernetes workload risks and how to mitigate them:

**Undefined Resource Requests and Limits**
When requests and limits aren’t defined, the Kubernetes scheduler treats all our pods and BestEffort ones. This means there are no reliability guarantees whatsoever. This can be somewhat prevented by using LimitRange objects, but continuous pod right-sizing (described in the next section) is needed to mitigate this.

**Under-provisioned Resource Requests and Limits**
This means that our pods aren’t getting the resources they need, which can lead to undesired failures and increased latencies, impacting application reliability.

**Container Restarts**
Containers are temporary and can be seamlessly restarted in case of failure. This is the default modus operandi for the most common Kubernetes workload types, such as Deployment and Daemon Sets. Yet, frequently occurring restarts signify a problem. Whether it’s an application bug, a permissions issue, or a misconfigured liveness probe, we want to troubleshoot and fix it ASAP to keep the cluster lean.

There are additional types of risk here. We need a targeted observability system to uncover and alert us to reliability risks in the cluster and intelligent autonomous automation to fix the most common issues as they arrive.

### 3. Eliminate Waste
As already mentioned, most clusters need to be more utilized. In other words, using a lot of cloud resources leads to overspending.

The desire to provide our workloads with as many resources as they need is understandable — no engineer wants their app to crawl like a turtle because of CPU throttling or die miserably because of an OOM kill. But alas — even giving one container three or four times its needs provides no reliability guarantees! There could be other rogue containers on the same node with under-provisioned requests and over-provisioned limits, causing our pet container to starve for resources — despite all our generosity.

The only way to hit the desired reliability and cost targets is to understand the sources of waste in our clusters and establish a process for continuously eliminating that waste.

Here are the practices every Kubernetes administrator should employ to keep their clusters waste-free:

**Pod Right-Sizing**
123456789101112131415 |
apiVersion: v1kind: PodMetadata: name: myappspec: containers: - name: app image: images.my-company.example/app:v4 resources: requests: memory: "64Mi" cpu: "250m" limits: memory: "128Mi" cpu: "500m" |
Correctly defining resource requests and limits for the containers in our pods impacts everything — from basic scheduling and eviction to HPA operation and node autoscaling. The trouble is — it takes a lot of work to pinpoint. [Performance testing](https://www.youtube.com/watch?v=-qQnWRRoDFM) can help with the initial definition. Yet, the dynamics of Kubernetes environments require us to monitor runtime resource consumption continuously and update configuration accordingly, preferably in an automated manner. This is the only way to ensure our containers get just the resources they need when needed.
**Node Utilization Monitoring**
Even after our container resources are optimized — we can still encounter additional waste because our node selection is suboptimal. This can stem from not using discounted Spot and Reserved instances when appropriate or provisioning instance types with resources that active workloads can’t efficiently utilize. Lean clusters must be managed by an automated system that provides granular visibility into node utilization by node group and type and intelligent recommendations for reconfiguring node pools for further optimization.

### 4. Just-In-Time Provisioning
Unused infrastructure costs us money and incurs unnecessary maintenance overhead without adding any additional value. The heart of the lean approach is providing resources when needed and releasing them when they are no longer required.

Here are ways to keep your clusters lean:

**Autoscaling**
The autoscaling capabilities make Kubernetes genuinely cloud native. Yet, they are optional! Defining autoscaling requires additional configuration on the pod (HPA, VPA, KEDA) or node level (cluster-autoscaler, Karpenter, etc.). Keeping your clusters lean means investing in this configuration, continuously verifying the autoscaling algorithm’s efficiency, and optimizing it to adapt to the system’s changing requirements.

**Just-In-Time Node Provisioning**
Not all node auto scalers were created the same. For example, the efficiency of the good old cluster-autoscaler is limited by static ASG configurations. Being lean means provisioning precisely what we need when needed — therefore, lean clusters migrate to Karpenter (if on AWS) or Node Auto Provisioning (on GCP and Azure).

**Dynamic Environment Management**
A well-automated Kubernetes setup allows us to provision new environments quickly by creating namespaces in existing clusters or spinning up new ones. This ease of use can lead to many underutilized resources. Staying lean requires devising an operational strategy for managing these environments and retiring them as soon as they are no longer needed. See [here](https://www.perfectscale.io/blog/putting-k8s-resources-to-sleep-with-keda) for an example of how to put your Kubernetes resources to sleep during off-hours.

### 5. Continuous Optimization
The lean approach is based on the context of continuous improvement — i.e., always looking for additional ways to make the production process more efficient, elevate quality, and reduce waste.

In the same way, we want to continuously optimize our Kubernetes clusters by automating resource allocation, analyzing cost and performance trends, redefining SLOs, and relentlessly eliminating risk.

## Summing It All Up
Following the lean approach can help us significantly improve Kubernetes ROI, improve workload performance, and save time spent on maintenance and troubleshooting.

To keep your clusters lean — stick to the following guidelines:

- Focus on Value
- Eliminate Risk
- Eliminate Waste
- Just-In-Time Provisioning
- Continuous Optimization
And may your clusters be lean!

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)