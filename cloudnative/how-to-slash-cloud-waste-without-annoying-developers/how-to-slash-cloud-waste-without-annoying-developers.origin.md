# How to Slash Cloud Waste Without Annoying Developers
![Featued image for: How to Slash Cloud Waste Without Annoying Developers](https://cdn.thenewstack.io/media/2025/05/5a30715f-slash-cloud-spend-1024x576.jpg)
LONDON — The massive and surging volume of software being generated with AI is contributing to skyrocketing cloud costs. It’s also exponentially increasing demand for additional compute resources to manage all of that code across cloud native infrastructures. These factors make cloud cost optimization even more critical for enterprises than ever.

Adding to the challenge, [Kubernetes](https://thenewstack.io/kubernetes/) introduces significant complexity at scale. There’s often limited visibility into how resources are used and what is being spent — a difficult environment for cost optimization. But existing [GitOps practices](https://thenewstack.io/4-core-principles-of-gitops/) orchestrated by Flux and Argo CD, based on traditional GitHub- or Git-type operations, are inadequate for proper resource optimization.

What’s required is an abstraction geared specifically towards resource optimization. It must automate analytics that cover the minutiae of infrastructure inside every pod and at scale across potentially multiple clusters and cloud and on-premises environments. In addition to automating the operations aspect of infrastructure management, such a platform should remove any concern around resource provisioning that might otherwise involve manual [YAML configuration](https://thenewstack.io/yall-against-my-lingo-why-everyone-hates-on-yaml/) or other operations-related tasks.

## Waste Makes Waste
Waste in cloud spending is not necessarily due to negligence or a lack of resources; it’s often due to poor visibility and understanding of how to optimize costs and resource allocations. Ironically, Kubernetes and GitOps were designed to enable DevOps practices by providing building blocks to facilitate collaboration between operations teams and developers, Gartner’s [Tony Iams](https://www.linkedin.com/in/tonyiams/) wrote in “[Cost Optimization for Containers and Kubernetes in the Cloud](https://www.gartner.com/en/documents/5692519).”

“However, while the operations team is responsible for only some sizing aspects, the responsibility for specifying the necessary resources to applications ultimately falls to developer teams,” Iams wrote. “The key to implementing optimization is to facilitate collaboration between development and operations teams. With the right tools and practices in place, and by working together, these teams can control the costs of running containers in the cloud and eventually optimize them.”

Many organizations that run large-scale or even mid-scale production environments on Kubernetes face a common issue: Workloads are either grossly overprovisioned or severely underprovisioned. Developers set the resource requests for CPU and memory, but they are forced to overprovision because the dynamics of the clusters constantly change. Overprovisioning means resources are allocated but remain unused, but the alternative, underprovisioning, negatively impacts performance. This inefficiency is exacerbated by the increasing workloads and complexity of modern software development, including CI/CD and AI.

The main challenge is the multidimensional character of scheduling decisions within Kubernetes clusters. On the one hand, developers set high resource limits and provision for peak demand, while administrators lack accurate data on actual resource needs over time, [Torsten Volk](https://www.linkedin.com/in/torstenvolk), an analyst with TechTarget’s Enterprise Strategy Group, told me. At the same time, affinity rules are often set based on simple static labels that are not informed by an application’s actual performance requirements. Resource requests only consider CPU and memory, without being able to define network throughput and latency. High-priority apps might unnecessarily evict lower-priority ones, despite not actually requiring more resources, Volk said.

“All of this leads to a multilevel guessing game, where developers want to make sure to build in a static buffer to proof their application for worst-case scenarios, while operators are unable to cut down the resulting waste as they do not understand how an application might react,” Volk said. “In a nutshell, Kubernetes does not know anything about the real-life resource requirements of an application, while the application pod is entirely unaware of the performance of the underlying cluster hardware.”

## Oh, So Human
Historically, resource allocation strategies were specified statically in YAML files and synced by a human manager using Flux or Argo CD. While Flux and Argo CD vendors and users seek to integrate resource optimization into their feature sets, they often fall short.

A few years ago, Git-based workflows were the standard for resource provisioning. However, with the acceleration of software development and CI/CD pipelines, and the rise of AI-generated code, “these traditional methods are breaking down,” noted[ Guy Baron,](https://www.linkedin.com/in/rhinof/?originalSubdomain=il) ScaleOps’ CTO and co-founder, when I spoke with him at [KubeCon+CloudNativeCon Europe](https://thenewstack.io/kubecon-cloudnativecon-eu-2025/) in April.

Instead, automating resource allocation in real time is required, along with optimizing vertical and horizontal scaling and pod placement. Such a platform continuously adjusts resource allocation based on workload needs and cluster health, ensuring efficiency and cost savings across associated multicloud and hybrid infrastructures at scale.

The optimization should cover:

- Vertical scaling: Adjusting the amount of CPU and memory assigned to each pod.
- Horizontal scaling: Optimizing the number of replicas in Horizontal Pod Autoscaler (HPA) or Argo-supported workloads.
- Placement optimization: Intelligently scheduling pods to maximize cluster efficiency.
ScaleOps’ platform serves as an example of an option that abstracts and automates the process. It’s positioned not as a platform for analysis and visibility but for resource automation. ScaleOps automates decision-making by eliminating the need for manual analysis and intervention, helping resource management become a continuous optimization of the infrastructure map.

Scaling decisions, such as determining how to vertically scale, horizontally scale, and schedule pods onto the cluster to maximize performance and cost savings, are then made in real time. This capability forms the core of the ScaleOps platform.

Savings and scaling efficiency are achieved through real-time usage data and predictive algorithms that determine the correct amount of resources needed at the pod level at the right time. The platform is “fully context-aware,” automatically identifying whether a workload involves a MySQL database, a stateless HTTP server, or a critical Kafka broker, and incorporating this information into scaling decisions, Baron said.

With ScaleOps, cluster state is monitored continuously. If a pod is scheduled on a node with noisy neighbors that impact performance or health checks, it’s automatically migrated to a more suitable node with greater available resources.

Recognizing that a WordPress website, a Kafka broker, a MySQL database, and an Airflow pipeline have different availability requirements and criticality levels, each workload is treated uniquely. Resource allocation and scaling decisions are adjusted dynamically to meet these needs.

The platform also responds in real time to changes within the cluster, supporting auto-healing and adjusting to usage spikes.

In practice, developers no longer have to worry about operational responsibilities, like cost tracking and resource allocation, and have more time to code and engineer software to solve business needs more directly. Operations teams are no longer perceived as blockers to software development and deployment by imposing rigid constraints that stifle agility. They also do not have to worry as much about overprovisioning and overpaying for redundant resources to account for spikes in future demand by the developers, which CTOs and — especially — CFOs do not appreciate amid rising cloud costs.

The platform serves developers by automating resource allocation and requests. Instead of developers handling these tasks manually, the platform introduces an infrastructure layer that takes care of them. At the same time, it gives developers visibility and insight into how their workloads and resources are being utilized in production, Baron said. “Ultimately, it’s about finding a balance — automating repetitive tasks while keeping developers informed and empowered.”

## Taking ScaleOps Out for a Ride
ScaleOps has a [free trial option](https://scaleops.com/), which is a good platform to get started, because the playground offers an immediate way to link ScaleOps directly to your cluster. For example, I easily attached ScaleOps to Helm, and then ScaleOps began seeking the cluster to manage.

The interface itself is very straightforward, allowing you to easily navigate between different time periods — whether it’s 70 days, 30 days, etc. — in a time series graph that shows CPU usage and memory over time. Metrics such as optimized requests, usage and waste are among the key indicators displayed in the time series graph.

For more detailed analysis, each workload offers a range of functionalities and data analysis that is both straightforward and accessible. This includes cost savings achieved for each workload. It’s also possible to change policies — whether it’s batch, cost, high availability, production or others — meaning the system offers leeway to dynamically change or update policy on an as-needed basis.

For a positive developer experience, the platform was designed to automate the mundane and dynamic aspects of resource allocation and scaling while keeping developers “in the loop,” garnering insights into how their workloads and resources are performing in production, Baron said.

The platform serves developers by automating resource allocation and requests. Instead of developers handling these tasks manually, the platform introduces an infrastructure layer that takes care of them. At the same time, it gives developers visibility and insight into how their workloads and resources are being utilized in production, Baron said. “Ultimately, it’s about finding a balance — automating repetitive tasks while keeping developers informed and empowered.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)